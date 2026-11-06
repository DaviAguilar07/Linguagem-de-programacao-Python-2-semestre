html_doc = """
    <!DOCTYPE HTML>
    <html>
    <head>
    Site web com back e front
    </head>
    <style>
    
    body{
        font-family: 'Arial', sans-serif; 
        background-color: #f8f8f8;
        margin: 0;
        display: flex;
        justify-content: center;
        align-items: center;
        height: 100vh;            
    }

    .container{
        text-align: center;
        padding: 40px;
        background-color: #fff;
        border-radius: 8px;
        box-shadow: 0 0 20px rgba(0, 0, 0, 0.2);    
    }

    h1{
        color: #3498db;
        font-size: 2em;
        margin-bottom: 20px;
    }

    p{
    color: #fff;
    font-size: 1.2em;
    }

    button {
        background-color: #3498db;
        color: #fff;
        font-size: 1.2em;
        padding: 10px 20px;
        border: none;
        border-radius: 4px;
        cursor: pointer;
        transition: background-color 0.3s ease;
    }
    
    button:hover {
        background-color: #2980b9;
    }    
    </style>
    
    <body>
    
    <div class = "container">

    <h1>Olá Mundo!</h1>
    <p>Esta é minha primeira página web criada com Python no Colab. Bem-vindo ao mundo da programação web!</p>
    <button "alert('Botão clicado!')">Clique aqui</button>
    
    </div>

    </body>
    </html>
"""

# Exibindo a página HTML

from IPython.display import HTML

HTML(html_doc)
