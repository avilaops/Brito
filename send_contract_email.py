import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders
from datetime import datetime

# Configurações do remetente
SENDER_NAME = "Nicolas, o Avassalador"
SENDER_EMAIL = "nicolas@avila.inc"
SENDER_WHATSAPP = "+55 17 99781-1471"

# Configurações do destinatário
RECIPIENT_NAME = "Britto, fi do Huck"
RECIPIENT_EMAIL = "Renanbrito80@gmail.com"
RECIPIENT_WHATSAPP = "+55 17 99664-5886"

# Configurações SMTP
SMTP_SERVER = "smtp.porkbun.com"
SMTP_PORT = 587
SMTP_PASSWORD = "7Aciqgr7@3278579"

def create_email_body():
    """Cria o corpo do email em HTML"""
    return f"""
<!DOCTYPE html>
<html lang="pt-BR">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <style>
        body {{
            font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
            line-height: 1.6;
            color: #333;
            max-width: 700px;
            margin: 0 auto;
            padding: 20px;
            background-color: #f5f5f5;
        }}
        .container {{
            background: white;
            padding: 40px;
            border-radius: 10px;
            box-shadow: 0 2px 10px rgba(0,0,0,0.1);
        }}
        .header {{
            text-align: center;
            padding-bottom: 30px;
            border-bottom: 3px solid #00f5ff;
            margin-bottom: 30px;
        }}
        .header h1 {{
            color: #8b5cf6;
            margin: 0;
            font-size: 28px;
        }}
        .header p {{
            color: #666;
            margin: 10px 0 0 0;
        }}
        .section {{
            margin: 25px 0;
        }}
        .section h2 {{
            color: #8b5cf6;
            font-size: 20px;
            margin-bottom: 15px;
            border-left: 4px solid #00f5ff;
            padding-left: 15px;
        }}
        .detail-grid {{
            background: #f8f9fa;
            padding: 20px;
            border-radius: 8px;
            margin: 15px 0;
        }}
        .detail-item {{
            display: grid;
            grid-template-columns: 150px 1fr;
            padding: 10px 0;
            border-bottom: 1px solid #e0e0e0;
        }}
        .detail-item:last-child {{
            border-bottom: none;
        }}
        .detail-label {{
            font-weight: 600;
            color: #555;
        }}
        .detail-value {{
            color: #333;
        }}
        .highlight-box {{
            background: linear-gradient(135deg, #8b5cf6 0%, #ff006e 100%);
            color: white;
            padding: 25px;
            border-radius: 10px;
            text-align: center;
            margin: 30px 0;
        }}
        .highlight-box h3 {{
            margin: 0 0 10px 0;
            font-size: 22px;
        }}
        .payment-summary {{
            background: #f0f9ff;
            border-left: 4px solid #00f5ff;
            padding: 20px;
            margin: 20px 0;
        }}
        .footer {{
            margin-top: 40px;
            padding-top: 30px;
            border-top: 2px solid #e0e0e0;
            text-align: center;
            color: #666;
        }}
        .contact-info {{
            background: #f8f9fa;
            padding: 20px;
            border-radius: 8px;
            margin: 20px 0;
        }}
        .button {{
            display: inline-block;
            background: #00f5ff;
            color: #0a0a0f;
            padding: 12px 30px;
            text-decoration: none;
            border-radius: 6px;
            font-weight: 600;
            margin: 10px 5px;
        }}
        .clause {{
            background: #fafafa;
            padding: 15px;
            margin: 10px 0;
            border-left: 3px solid #8b5cf6;
            border-radius: 4px;
        }}
        .clause strong {{
            color: #8b5cf6;
        }}
    </style>
</head>
<body>
    <div class="container">
        <div class="header">
            <h1>📄 Contrato Digital de Parcelamento</h1>
            <p>Formalização da Transação Comercial</p>
            <p style="font-size: 14px; color: #999;">Data: {datetime.now().strftime('%d de %B de %Y')}</p>
        </div>

        <div class="section">
            <h2>👥 Partes Envolvidas</h2>
            <div class="detail-grid">
                <div class="detail-item">
                    <span class="detail-label">Vendedor:</span>
                    <span class="detail-value">Nicolas Rosa (o Avassalador)</span>
                </div>
                <div class="detail-item">
                    <span class="detail-label">E-mail:</span>
                    <span class="detail-value">{SENDER_EMAIL}</span>
                </div>
                <div class="detail-item">
                    <span class="detail-label">WhatsApp:</span>
                    <span class="detail-value">{SENDER_WHATSAPP}</span>
                </div>
            </div>

            <div class="detail-grid" style="margin-top: 20px;">
                <div class="detail-item">
                    <span class="detail-label">Comprador:</span>
                    <span class="detail-value">Renan Britto (fi do Huck)</span>
                </div>
                <div class="detail-item">
                    <span class="detail-label">E-mail:</span>
                    <span class="detail-value">{RECIPIENT_EMAIL}</span>
                </div>
                <div class="detail-item">
                    <span class="detail-label">WhatsApp:</span>
                    <span class="detail-value">{RECIPIENT_WHATSAPP}</span>
                </div>
            </div>
        </div>

        <div class="section">
            <h2>🔥 Objeto da Transação</h2>
            <div class="detail-grid">
                <div class="detail-item">
                    <span class="detail-label">Produto:</span>
                    <span class="detail-value">Fogão Brastemp</span>
                </div>
                <div class="detail-item">
                    <span class="detail-label">Marca:</span>
                    <span class="detail-value">Brastemp</span>
                </div>
                <div class="detail-item">
                    <span class="detail-label">Linha:</span>
                    <span class="detail-value">Fogão Brastemp Clean / 4 Bocas</span>
                </div>
                <div class="detail-item">
                    <span class="detail-label">Modelo:</span>
                    <span class="detail-value">BYS4 (ou variações BYS4T / BYS4N)</span>
                </div>
                <div class="detail-item">
                    <span class="detail-label">Tipo:</span>
                    <span class="detail-value">Piso, com mesa em inox e tampa de vidro temperado</span>
                </div>
                <div class="detail-item">
                    <span class="detail-label">Acendimento:</span>
                    <span class="detail-value">Automático</span>
                </div>
                <div class="detail-item">
                    <span class="detail-label">Forno:</span>
                    <span class="detail-value">Porta de vidro espelhado (modelo mais recente da linha Clean)</span>
                </div>
            </div>
        </div>

        <div class="highlight-box">
            <h3>💎 A Única Garantia</h3>
            <p style="font-size: 18px; margin: 0;">A Palavra & A Amizade</p>
        </div>

        <div class="section">
            <h2>💰 Condições de Pagamento</h2>
            <div class="payment-summary">
                <p style="margin: 0 0 10px 0;"><strong>Valor Total:</strong> R$ 800,00</p>
                <p style="margin: 0;"><strong>Forma de Pagamento:</strong> 8 parcelas mensais de R$ 100,00</p>
            </div>

            <h3 style="color: #8b5cf6; margin-top: 25px;">📅 Cronograma de Pagamento:</h3>
            <ul style="list-style: none; padding: 0;">
                <li style="padding: 8px 0; border-bottom: 1px solid #e0e0e0;">✓ Parcela 1: R$ 100,00 - 24/Dez/2025</li>
                <li style="padding: 8px 0; border-bottom: 1px solid #e0e0e0;">✓ Parcela 2: R$ 100,00 - 24/Jan/2026</li>
                <li style="padding: 8px 0; border-bottom: 1px solid #e0e0e0;">✓ Parcela 3: R$ 100,00 - 24/Fev/2026</li>
                <li style="padding: 8px 0; border-bottom: 1px solid #e0e0e0;">✓ Parcela 4: R$ 100,00 - 24/Mar/2026</li>
                <li style="padding: 8px 0; border-bottom: 1px solid #e0e0e0;">✓ Parcela 5: R$ 100,00 - 24/Abr/2026</li>
                <li style="padding: 8px 0; border-bottom: 1px solid #e0e0e0;">✓ Parcela 6: R$ 100,00 - 24/Mai/2026</li>
                <li style="padding: 8px 0; border-bottom: 1px solid #e0e0e0;">✓ Parcela 7: R$ 100,00 - 24/Jun/2026</li>
                <li style="padding: 8px 0;">✓ Parcela 8: R$ 100,00 - 24/Jul/2026</li>
            </ul>
        </div>

        <div class="section">
            <h2>📋 Termos e Condições</h2>
            <div class="clause">
                <p><strong>Cláusula 1:</strong> Este acordo é firmado com base na confiança mútua e na amizade existente entre as partes.</p>
            </div>
            <div class="clause">
                <p><strong>Cláusula 2:</strong> O comprador Renan Britto se compromete a efetuar 8 (oito) pagamentos mensais de R$ 100,00 (cem reais) cada.</p>
            </div>
            <div class="clause">
                <p><strong>Cláusula 3:</strong> A única garantia deste contrato é a palavra empenhada entre amigos, valor este inestimável e de honra. Não existe multa, juros ou correção monetária... porque a cobrança é moral mesmo.</p>
            </div>
            <div class="clause">
                <p><strong>Cláusula 4:</strong> O fio é meu.</p>
            </div>
            <div class="clause">
                <p><strong>Cláusula 5:</strong> O fio é meu.</p>
            </div>
            <div class="clause" style="background: linear-gradient(135deg, rgba(255, 216, 155, 0.3) 0%, rgba(25, 84, 123, 0.3) 100%); border-left-color: #19547b;">
                <p><strong>Cláusula 6:</strong> Oficialmente, o fio é meu.</p>
            </div>
        </div>

        <div class="section" style="text-align: center; margin-top: 40px;">
            <h2>🔗 Acesse o Contrato Digital</h2>
            <p>Para visualizar o contrato completo com os vídeos do produto, acesse:</p>
            <a href="https://avilaops.github.io/Brito/" class="button">Ver Contrato Online</a>
        </div>

        <div class="footer">
            <p style="font-style: italic; color: #8b5cf6; font-size: 16px; margin-bottom: 20px;">
                "Na amizade, a palavra vale mais que qualquer contrato."
            </p>
            <p style="font-size: 14px; color: #999;">
                Que este fogão aqueça muitas refeições e momentos felizes!
            </p>
            <p style="font-size: 12px; color: #999; margin-top: 30px;">
                Este é um documento digital gerado automaticamente.<br>
                Em caso de dúvidas, entre em contato via WhatsApp.
            </p>
        </div>
    </div>
</body>
</html>
"""

def send_email():
    """Envia o email formatado"""
    try:
        # Criar mensagem
        msg = MIMEMultipart('alternative')
        msg['From'] = SENDER_EMAIL
        msg['To'] = RECIPIENT_EMAIL
        msg['Subject'] = "📄 Contrato Digital - Fogão Brastemp Parcelado | Formalização"

        # Corpo do email em HTML
        html_body = create_email_body()
        msg.attach(MIMEText(html_body, 'html', 'utf-8'))

        # Conectar ao servidor SMTP
        print(f"Conectando ao servidor SMTP {SMTP_SERVER}:{SMTP_PORT}...")
        server = smtplib.SMTP(SMTP_SERVER, SMTP_PORT)
        server.set_debuglevel(1)  # Ativar debug para ver o processo
        server.ehlo()
        server.starttls()
        server.ehlo()

        # Fazer login
        print(f"Autenticando como {SENDER_EMAIL}...")
        server.login(SENDER_EMAIL, SMTP_PASSWORD)

        # Enviar email
        print(f"Enviando email para {RECIPIENT_EMAIL}...")
        server.send_message(msg)

        # Fechar conexão
        server.quit()

        print("\n" + "="*60)
        print("✅ EMAIL ENVIADO COM SUCESSO!")
        print("="*60)
        print(f"De: {SENDER_NAME} ({SENDER_EMAIL})")
        print(f"Para: {RECIPIENT_NAME} ({RECIPIENT_EMAIL})")
        print(f"Assunto: {msg['Subject']}")
        print("="*60)

        return True

    except Exception as e:
        print("\n" + "="*60)
        print("❌ ERRO AO ENVIAR EMAIL")
        print("="*60)
        print(f"Erro: {str(e)}")
        print("="*60)
        return False

if __name__ == "__main__":
    print("="*60)
    print("📧 SISTEMA DE ENVIO DE CONTRATO DIGITAL")
    print("="*60)
    print(f"Remetente: {SENDER_NAME}")
    print(f"Destinatário: {RECIPIENT_NAME}")
    print(f"Servidor SMTP: {SMTP_SERVER}:{SMTP_PORT}")
    print("="*60)
    print()

    send_email()
