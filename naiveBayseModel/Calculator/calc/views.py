from django.shortcuts import render, render_to_response, get_object_or_404, redirect
from calc.models import Hypoteses, NaiveBaysesModel
# Create your views here.


def index(request):
    # Lidando com segundo acesso, uma vez que já se tem algum dados:
    if request.method == "POST":
        # Recebendo post (QueryDict):
        form = request.POST 

        # Transformando objeto em dicioniario
        form = dict(form)

        # Importando entradas:
        form = form['dados']

        # Leitura dos dados para uma lista de inteiros:
        dados = form[0].split(',')
        dados = [int(dado) for dado in dados]

        # Acessando a base de dados:
        hypoteses = Hypoteses.objects.all()

        # Contruindo Modelo:
        model = NaiveBaysesModel(hypoteses)

        # Exibindo probabilidade das hipóteses:
        print(dados)
        print(model.posteriors(dados))
        print("")

        if len(dados)<3:
            guess = ""
        else:
            guess = str(model.guess(dados));

        if len(dados)<5:
            isReportReady = False
        else:
            isReportReady = True

        if dados[-1] != 0:
            # Retornando dados com entradas:
            return render(request,'index.html',{"dados":str(form)[2:-2],
                                                "guess":guess,
                                                "reportFlag": isReportReady})

    # Lidando com o primeiro acesso do usuário:
    return render(request, 'index.html')
