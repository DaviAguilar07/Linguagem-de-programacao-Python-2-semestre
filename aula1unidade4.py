from IPython.display import HTML
doc_html = """
    <!DOCTYPE HTML>
    <html lang = en>
    <head>
    <meta charset = "utf 8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    </head>

    <title>Meu portfolio</title>
    <body style = "font-family: Arial, sans serif; background-color: #f8f8f8; margin: 0; padding: 0">
    <header style= "text-align: center; background-color: #3498db; color: #fff; padding: 20px;">
    <h1 style = "margin: 0;">Davi de Aguilar Timoteo</h1>
    <p style = "margin 5 px 0;">Desenvolvedor back-end</p>
    </header>

    <section style="margin: 20px; text-align: center;">
    <img src="https://media.licdn.com/dms/image/v2/D4D03AQEOrJorE-hXew/profile-displayphoto-scale_400_400/B4DZ5e8fGNKwAs-/0/1779709379580?e=1791417600&v=beta&t=9hOvu_saM4OiQs33Y7R6Z0kMq5EkWSIw1JA3U-y_XsI" alt="Sua Foto" style="border-radius: 50%; margin-bottom: 20px;">
    <div id="informacoes-pessoais" style="max-width: 400px; margin: 0 auto;">
    <h2>Informações pessoais</h2>
    <p><b>Cidade:</b> Belo Horizonte</p>
    <p><b>País:</b> Brasil</p>
    <p><b>Interesses:</b> Desenvolvimento, suporte na construção do software</p>
    </div>
    </section>

    <section style="margin: 20px; text-align:center;">
    <h2>Habilidades</h2>
    <ul style="list-style: none; padding: 0;">
    <li><b>Linguagens:</b> Python, HTML, CSS, C</li>
    <li><b>Ferramentas:</b> GitHub, GitHub desktop, Git, VS code</li>
    </ul>
    </section>

    <section style="margin: 20px; text-align: center;">
    <h2>Projeto Recente</h2>
    <p>Trabalhando na construção do meu portfólio</p>
    </section>

    <footer style="text-align: center; margin-top: 20px;">
    <a href="https://www.linkedin.com/in/davi-aguilar-1a4851407/" target="_blank" style="margin: 0 10px; color: #3498db; text-decoration: none;">Meu LinkedIn</a>
    </footer>
    </body>
    </html>
"""
HTML(doc_html)