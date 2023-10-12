from flask import Flask, render_template, jsonify

app = Flask(__name__)

# Exemplo de projetos
projects = [
    {
        "title": "Docker to Build APKs (IONIC 6.20.6)",
        "description": "Esse é um projeto para BUILDAR/GERAR apks usando qualquer sistema operacional (com tanto que tenha o docker instalado), DOCKER usa como base o Debian 11.7.",
        "link": "https://github.com/gustavogoncalvesdiasneves/Docker_BUILD_APKS_IONIC_6.20.6",
        "card_id": "geral",
        "image": "./static/Docker_IONIC6.png",
        "p": "Venha Conferir!"
    },
    {
        "title": "Automação Forms + Email (Power Automate & Python)",
        "description": "Esse projeto tem como o objetivo compartilhar uma base de meu conhecimento do uso do power automate, nesse projeto automatizei gatilhos(quando uma pessoa envia um forms), automatizando o envio de email personalizado (html + dados).",
        "link": "",
        "card_id": "geral",
        "image": "./static/Power_Automate.png",
        "p": "Em breve" #Venha Conferir!
    },
    {
        "title": "Finanças Pessoais - APP",
        "description": "Esse projeto é algo mais pessoal a minha necessidade, nele tem uma tela de orçamento onde o usuario pode ver suas finanças no que ele saiu no lucro/prejuizo conforme os meses, uma aba para VTs(Vale Transportes), onde seria configurado para descontar o valor que o usuario configurou, aba de Orçamentos (calculo), historico de lucros/prejuizos, e muito mais... ",
        "link": "https://www.youtube.com/watch?v=VSarnYTveeI&ab_channel=PlayerG4",
        "card_id": "geral",
        "image": "./static/Finanças_Pessoais_APP.png",
        "p": "Em breve" #Venha Conferir!
    },
    {
        "title": "XML Editer (Videos Automation)",
        "description": "Esse é um Aplicativo que automatiza edições de videos para editores que suportam importação de XML, tendo a possibilidade de colocar IMAGENS e VIDEOS nas propriedades do XML, assim podendo exportar o video pelo editor sem precisar editar cada label um por um.",
        "link": "",
        "card_id": "geral",
        "image": "./static/XML_Editer.png",
        "p": "Em breve"
    },
    {
        "title": "Automação Forms (Perguntas e Respostas) Python",
        "description": "Essa é uma automação desenvolvida nos meus parametros de necessidade, onde a automação feita em PYTHON pega a questão do forms, pesquisa no google, pega a resposta e me trás um Excel com <br>[Questão, Questão do Site(resposta), Resposta]; <br>AUTOMAÇÃO TEM 3 VERSÕES <br>(ChatGPT, Brainly e PD).",
        "link": "",
        "card_id": "geral",
        "image": "./static/Python_Automação_QR.png",
        "p": "Em breve"
    },
    {
        "title": "Automação TEAMS + Email (Power Automate)",
        "description": "Essa é uma automação desenvolvida nos meus parametros de necessidade, onde queria que os emails do Teams WEB da Tutora da minha faculdade chegasse em meu Email Pessoal sem precisar ficar trocando de conta/entrando no Teams, Automação feita utilizando gatilhos em nuvem(teams) + envio de emails com html personalizado.",
        "link": "",
        "card_id": "geral",
        "image": "./static/Automation_TEAMS.png",
        "p": "Em breve"
    },
    {
        "title": "Streaming de Video Local (C++)",
        "description": "Esse é um aplicativo que permite a transmissão de vídeo local, como um serviço de streaming de vídeo em tempo real.",
        "link": "",
        "card_id": "geral",
        "image": "./static/Streaming_Video_Local.png",
        "p": "Em breve"
    },
    {
        "title": "Automation Link Repair (Python)",
        "description": "Automação feita para reparação de links de sites que estão com varios links quebrados <br>(ex: https://google/pagina87) sendo o destino antigo, com a automação corrigindo e passando o parametro de correção pro link <br>(ex: https://google/pages/pagina87).",
        "link": "",
        "card_id": "geral",
        "image": "./static/Python_Automação_QR.png",
        "p": "Em breve"
    },
    # Adicione mais projetos conforme necessário
]

@app.route("/")
def homepage():
    # Renderiza a página inicial
    return render_template("home.html", projects=projects)

@app.route("/get_additional_projects/<int:start_index>")
def get_additional_projects(start_index):
    # Retorna projetos adicionais a partir de start_index
    num_projects = 3  # Número de projetos a serem carregados de cada vez
    next_projects = projects[start_index:start_index + num_projects]
    return jsonify(next_projects)

if __name__ == "__main__":
    app.run(debug=True)
