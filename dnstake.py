import requests
import dns.resolver
import argparse
import smtplib
from email.mime.text import MIMEText
import logging
import json

# Konfigurasi logging
logging.basicConfig(filename='dnstake.log', level=logging.INFO, format='%(asctime)s %(levelname)s:%(message)s')

# Daftar penyedia DNS umum
DNS_PROVIDERS = [
    "aws", "azure", "google", "akamai", "cloudflare"
]

# Fungsi untuk memeriksa pengambilalihan DNS
def check_dns_takeover(domain):
    try:
        answers = dns.resolver.resolve(domain, 'NS')
        for server in answers:
            if server.target.to_text().split('.')[0] in DNS_PROVIDERS:
                return True, server.target.to_text()
    except dns.resolver.NXDOMAIN:
        return False, "Domain does not exist."
    except dns.resolver.NoAnswer:
        return False, "No answer from DNS server."
    except dns.resolver.Timeout:
        return False, "Timeout querying DNS server."
    except dns.resolver.NoNameservers:
        return True, "No nameservers found, possible takeover."
    return False, "No vulnerable DNS providers found."

# Fungsi untuk mengirim email notifikasi
def send_email_notification(subject, body, to_email):
    from_email = "your_email@example.com"  # Gantilah dengan email Anda
    password = "your_email_password"  # Gantilah dengan password email Anda

    msg = MIMEText(body)
    msg['Subject'] = subject
    msg['From'] = from_email
    msg['To'] = to_email

    try:
        server = smtplib.SMTP_SSL('smtp.example.com', 465)
        server.login(from_email, password)
        server.sendmail(from_email, to_email, msg.as_string())
        server.quit()
        logging.info(f"Email notifikasi berhasil dikirim ke {to_email}")
    except Exception as e:
        logging.error(f"Gagal mengirim email: {e}")

# Fungsi utama
def main():
    parser = argparse.ArgumentParser(description="DNSTake: Alat untuk memeriksa zona DNS yang hilang.")
    parser.add_argument("domain", help="Domain atau subdomain yang akan diperiksa")
    parser.add_argument("--batch", help="File yang berisi daftar subdomain untuk pemeriksaan batch")
    parser.add_argument("--output", help="File untuk menyimpan hasil pemeriksaan")
    parser.add_argument("--email", help="Email untuk mengirim notifikasi jika ditemukan kerentanan")
    args = parser.parse_args()

    domains = []
    if args.batch:
        with open(args.batch, 'r') as file:
            domains = [line.strip() for line in file]
    else:
        domains.append(args.domain)

    results = []
    for domain in domains:
        result, message = check_dns_takeover(domain)
        results.append({'domain': domain, 'vulnerable': result, 'message': message})
        if result:
            logging.warning(f"{domain} rentan terhadap pengambilalihan DNS: {message}")
            if args.email:
                send_email_notification(f"Kerentanan DNS Takeover Ditemukan pada {domain}", message, args.email)
        else:
            logging.info(f"{domain} tidak rentan: {message}")

    if args.output:
        with open(args.output, 'w') as file:
            json.dump(results, file, indent=4)

    for result in results:
        status = "[!]" if result['vulnerable'] else "[-]"
        print(f"{status} {result['domain']}: {result['message']}")

if __name__ == "__main__":
    main()
