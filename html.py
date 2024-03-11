html = """
<!DOCTYPE html>
<html lang="pt-br">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Simulação de E-mail</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            margin: 20px;
            padding: 20px;
            background-color: #f4f4f4;
        }

        .email-container {
            max-width: 600px;
            margin: 0 auto;
            background-color: #fff;
            padding: 20px;
            border-radius: 5px;
            box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
        }

        h1, p {
            color: #333;
        }

        h1 {
            font-size: 24px;
        }

        p {
            font-size: 16px;
            line-height: 1.6;
        }

        strong {
            color: #3498db;
            font-weight: bold;
        }

        em {
            color: #e74c3c;
            font-style: italic;
        }

        .sender-info {
            margin-bottom: 20px;
        }

        .message-content {
            margin-bottom: 20px;
        }

        .footer {
            text-align: center;
            color: #888;
        }
    </style>
</head>
<body>

    <div class="email-container">
        <div class="sender-info">
            <img src="result-0 (4).png" alt="Descrição da Imagem">
            <h1>Nome do <span style="color: #27ae60;">Remetente</span></h1>
            <p>remetente@example.com</p>
        </div>

        <div class="message-content">
            <p><strong>Assunto:</strong> <span style="color: #e67e22;">Título do E-mail com Destaque</span></p>
            <p><em>Lorem Ipsum</em> é simplesmente uma simulação de texto da indústria tipográfica.</p>
            <p>É amplamente utilizado em trabalhos de design gráfico para preencher espaços em layouts.</p>
            <p>O <span style="color: #3498db;">texto Lorem Ipsum</span> tem sido o texto padrão da indústria desde a década de 1500.</p>
            <p>Quando um artista de meios digitais se depara com um dilema...</p>
            <p><span style="color: #e74c3c;">Lorem Ipsum é uma escolha sábia</span>.</p>
            <p>Atenciosamente,<br><span style="font-weight: bold;">Seu Nome</span></p>
        </div>

        <div class="footer">
            <p>Este é um e-mail simulado.</p>
        </div>
    </div>

</body>
</html>

"""