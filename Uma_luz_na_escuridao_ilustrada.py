'''
Aventura solo pronta para você ler e jogar.

Caso queira você pode criar a versão executável para rodar sem a necessidade do Python. Neste caso:
(i) No terminal digite pip install pyinstaller
(ii) Em seguinda, ainda no terminal, digite pyinstaller --onefile Uma_luz_na_escuridao.py

Não sou formado em computação. Sendo assim, o código não é tão elegante nem tão eficiente. Contudo, para tal
funcionalidade está bom. Se melhorar ou criar uma nova história eu gostaria de ver.
Meu email: allansoares007@gmail.com
'''


#################################################CÓDIGO COMPLETO#################################################
# Sugestão: Crie sua própria história a partir desta.

import PySimpleGUI as sg



layout = [  [sg.Text('Aventura Solo: Uma Luz na Escuridão \n' \
                     'Aperte "Tutorial" para começar.')],
            [sg.Output(size=(110,25),font='Times 12 italic bold'),
             sg.Image(filename='image.png',key='image.png',visible=True)], # Anything you 'print' will show upo here
            [sg.Text('Escolha: ')],
            [sg.Input(key='-IN-', do_not_clear=False)], # flag set to clear user's input automatically
            [sg.Button('Seguir', bind_return_key=True, key='Seguir',visible=True),
             sg.Button('Inventário',bind_return_key=True),
             sg.Button('Caminho',bind_return_key=True),
             sg.Button('Tutorial',bind_return_key=True),
             sg.Button('Exit',bind_return_key=True)]  ]


window = sg.Window('Aventura Solo', layout)     #Chama o layout

event = 0
inventario = []
caminho = []



while event != 'Exit':              #A janela criada fica aberta até que o botão "Exit" seja apertado
    event, values = window.read()   #Parte do código que faz a leitura dos valores digitados

    user_input = values['-IN-']     #Entradas fornecidas pelo jogador
    extracao = str(values)          #Extrai o texto digitado pelo jogador inciando com "{'-IN-':" e terminando
                                    #com "'}".

    t=extracao[10:len(extracao)-2]      #A variável t extrai os caracteres de texto eliminando os citados no passo
                                        #deixando somente o texto digitado pelo jogador.

    if t=='inicio':                     #Parte do código que retoma valores iniciais caso o jogador queira jogar
        event = 0                       #após ter perdido, chegado ao fim, ou queira reiniciar a história.
        caminho = []
        print('Digite 0-2 para retornar ao começo da história. O caminho trilhado, e o inventário '
              'retornaram ao que eram no início da história.\n')
    if event == 0:
        x = 'image.png'
    elif event == 1:
        x = 'image1.png'

#################################################CARACTERÍSTICAS#################################################
    if event == 'Caminho':
        window['image.png'].Update('caminho.png', visible=True)#Parte do código que guarda as escolhas feitas pelo jogador
        if caminho == []:
            print('Você ainda está na fase inicial.\n')
        else:
            print('Caminho:',', '.join(caminho))
            print('\n')

    if event == 'Inventário':
        window['image.png'].Update('inventario.png', visible=True)
        #Parte do código que armazena os itens que o jogador tem
        if inventario == []:                            #disponíveis durante a história
            print('Até o momento você não porta nada de util.\n')
        else:
            print('Inventário:',', '.join(inventario))
            print('\n')


    if event == 'Tutorial':         #Tutorial apresentado a jogadores de primeira viagem
        window['image.png'].Update('tutorial.png', visible=True)
        print('Tutorial:\n'
              'I. Uma história interativa é uma história na qual '
              'você escolhe* o caminho que o personagem irá trilhar. Diferente '
              'de um livro comum, neste tipo de história você pode obter'
              'o sucesso chegando ao FIM ou simplesmente ficar pelo meio'
              'do caminho. Se não obtiver êxito tente novamente. Coloque '
              'os seus amigos para jogar. Leia para eles e a maioria decide '
              'por onde o personagem deve ir, “enfrentar a víbora usando um '
              'porrete” ou “tentar atear fogo a sala para afugentá-la”, você '
              'decide. Acredite, você vai gostar. \n'
              'II. Clicando em "Inventário" você terá acesso aos objetos pessoais'
              'que podem ou não ser importantes em algumas partes da trama.\n'
              'III. Clicando em "Caminho" você terá uma recordação do caminho feito'
              'até o momento em que se encontra.\n'
              'Em cada situação que tiver que escolher entre '\
              'duas ou mais opções você deverá digitar no campo '\
              '"Escolhas" o valor\codigo correspondente à opção e apertar '\
              '"Seguir". Para começar, digite "0-1"(0 traço 1, sem aspas) e aperte "Seguir".\n')

#################################################EVENTOS#################################################
#Texto com as escolhas que o usuário faz ao longo da história. Algumas escolhas podem atualizar o inven-
#tário acrescentando ou removendo objetos que o jogador poderia usar durante a história.

    if event == 'Seguir' and t == '0-1':
        window['image.png'].Update('image0-1.png', visible=True)
        print('[0-1] Parece que você entendeu! Digite "0-2" (e aperte "Seguir") para ler a Introdução.\n')

    if event == 'Seguir' and t == '0-2':
        window['image.png'].Update('image0-2.png', visible=True)
        print('[0-2] Introdução: \n'
              'Seu nome é Dasmius, clérigo da deusa da luz Amiz. Desde os 14 '
              'anos, quando sua mãe o trouxe ao templo, você tem se devotado '
              'à deusa cumprindo um rigoroso código de conduta assim como '
              'todos os outros cinco clérigos que residem neste templo. Por '
              'diversas vezes, durante momentos de perigo e insegurança, você '
              'acreditou ser salvo pelos poderes de Amiz. Hoje você tem 21 '
              'anos e acaba de ser condecorado clérigo da luz. Digite [0-3].\n')
    if event == 'Seguir' and t == '0-3':
        inventario.append('Maça')               #O item Maça vai para o inventário
        inventario.append('Armadura de Metal')  #Idem
        inventario.append('Escudo')             #Idem
        window['image.png'].Update('image0-3.png', visible=True)
        print('[0-3] Sua Missão:\n'
              'Após sua condecoração como mais novo clérigo do templo de Amiz, '
              'Josh Knolan, também clérigo da luz, responsável por você até então, '
              'se aproxima de você e diz:\n'
              '- Olá mais novo sacerdote da luz, estou feliz por vê-lo chegar até '
              'aqui. Saiba que muitos almejam seguir o caminho da luz, mas poucos '
              'conseguem percorrê-lo sem se ofuscar com seu brilho intenso ou se '
              'desviar para as trevas. Hoje começa a sua jornada, tome aqui a sua '
              'maça, armadura de metal e escudo. Faça um bom uso destas armas em '
              'sua defesa e também na luta por justiça. Que a luz de Amiz o guie.\n'
              'Knolan o cumprimenta novamente e se dirige à saída do salão que '
              'ocorrera a cerimônia de sua condecoração. Quando sobre a soleira '
              'da porta ele para, vira-se novamente para você e diz:\n'
              '- Meu caro Dasmius tenho uma primeira missão para você. Claro, '
              'sei que pode está bastante eufórico por se tornar um clérigo da luz '
              'e talvez não tenha cabeça para realiza-la por esses dias. Entenderei '
              'se não quiser ir e pedirei a um dos outros clérigos que a faça. Se '
              'quiser aceitar a missão vá até meus aposentos pelo fim da tarde.\n'
              'Se quiser aceitar a missão digite 1, se não digite 5.\n')


    if event == 'Seguir' and t == '1':
        inventario.append('Pergaminho')
        inventario.append('Bússola')
        caminho.append('1')     #O caminho aprende a escolha "1"
        window['image.png'].Update('image1.png',visible=True)
        print('[1] Já passa do meio dia e seu estômago parece ter um buraco. Todos os '
              'clérigos se reúnem no refeitório junto a você, mas não há nada para '
              'comer! Knolan se aproxima novamente de você, abre um sorriso e '
              'prossegue:\n'
              '- Meu caro Dasmius, havia me esquecido, há uma missão irrecusável '
              'para você. Fazer a nossa comida. Todos dão boas risadas. Algum tempo '
              'depois, você traz a comida, um belo pernil assado, prato que foi lhe '
              'ensinado pelo seu pai quando você ainda tinha 12 anos. Todos comem até '
              'se fartar e o elogiam pelos seus dotes culinários. Após o banquete você '
              'vai aos seus aposentos descansar até o fim da tarde. Pouco antes da '
              'hora marcada você aplica um polimento em seus itens e então se dirige '
              'aos aposentos de Knolan. Lá, o mesmo está de pé, olhando pela janela e '
              'parece nem notar a sua presença. Você espera impaciente por cerca por '
              'algum tempo ao pé da porta. Relutante, tenta dirigir a palavra a ele '
              'quando o mesmo o interrompe com um gesto de silêncio.\n'
              '- xhiii, espere um momento. Veja este belo por do sol. Com fim da luz '
              'do dia vai nossa visão humana e fica somente aquela proporcionada por '
              'Amiz. Durante a noite ou em meio à escuridão, Armiz fará com que a luz '
              'venha até você garantindo que chegue a salvo ao seu destino. '
              'Knolan vai até uma mesa de madeira no canto do quarto, e pega um '
              'pergaminho e o entrega.\n'
              '- Ha um dia de viagem, a leste daqui, existe um pequeno vilarejo e preciso '
              'que vá até lá levar esse pergaminho a um homem chamado Lázaro. Aqui '
              'nesta mochila há uma bússola para que não se perca no caminho e '
              'mantimentos para dois dias, um de ida e o outro de volta. Não abra o '
              'pergaminho, pois é confidencial, apenas o entregue e volte para este '
              'templo. Descanse e pela manhã pegue um dos cavalos e vá.\n Digite 3.\n')

    if event == 'Seguir' and t == '2':
        caminho.append('2')
        window['image.png'].Update('image2.png', visible=True)
        print('[2] Nem louco você iria sem um bússola. Poderia se perder. E, além disso, '
                'se fosse realmente algo urgente, Knolan não haveria enviado você em '
                'sua primeira missão. Você resolve espera por ele e o vê somente na manhã'
                'seguinte. Seu argumento de que não poderia ir sem uma bússola parece o '
                'ter incomodado, mas ele não diz nada, apenas toma o pergaminho da sua '
                'mão e se recolhe para seus aposentos. Curioso sobre o que havia no '
                'pergaminho você pergunta a ele. Ele diz:\n'
                '- Meu caro Dasmius, não havia nada de mais. Somente um feitiço de '
                'cura, mas não se preocupe com isso. Todas as coisas tem um motivo.\n'
                'Se você não foi é por que não era para você ir. Digite 11.\n')


    if event == 'Seguir' and t == '3':
        if 'Bússola' in inventario:
            inventario.remove('Bússola')
            inventario.append('Bússola Quebrada')
        caminho.append('3')
        window['image.png'].Update('image3.png', visible=True)
        print('[3] Você faz suas refeições e então segue para o salão principal para fazer '
              'suas orações. Parece que você é o único que veio aqui esta noite. Aos '
              'pés da estátua da deusa Amiz você pede proteção para em sua primeira missão, '
              'que ela lhe guie pelo caminho da luz e não deixe que sua visão se ofusque '
              'frente às escolhas. Após realizar suas orações você parte para seus aposentos '
              'onde repousa durante o resto da noite. Pela manhã, pega a sua mochila e com a '
              'bússola e mantimentos para a viagem. Ao conferir a bússola você percebe que a '
              'mesma está quebrada e não aponta para direção alguma, falta-lhe o ponteiro. '
              'Você decide então procurar Knolan para que o mesmo lhe forneça um mapa ou uma '
              'nova bússola. Contudo, você não o encontra. Parece que você terá que escolher. '
              'Se quiser ir sem a bússola, confiando que Amiz o guiará digite 7, se preferir '
              'esperar por Knolan digite 2.\n')

    if event == 'Seguir' and t == '4':
        caminho.append('4')
        window['image.png'].Update('image4.png', visible=True)
        print('[4] Você acredita que esperar não é uma opção, pois você nem ao menos sabe do '
              'que se proteger. Você avalia o local e vê que há dois possíveis pontos de '
              'ataque, um por cima e outro pela frente. Contudo, pela frente parece óbvio. '
              'Você dá alguns passos até a saída dos rochedos e percebe que não há nada por '
              'ali. Mesmo assim, resolve procurar mais um pouco.'
              '\nSe você tem uma tocha e quer ir atrás do invasor, digite 8. Se você não '
              'tem uma tocha e quer ir atrás do invasor mesmo assim, digite 15. Se não tem uma tocha e preferir '
              'montar em seu cavalo em busca de um local mais seguro digite 12.\n')

    if event == 'Seguir' and t == '5':
        caminho.append('5')
        window['image.png'].Update('image5.png', visible=True)
        print('[5] Você está muito eufórico com sua condecoração e decide não aceitar sua missão, '
              'pois, certamente novas missões surgirão. Knolam designa Heragon, um dos outros '
              'quatro clérigos do templo de Amiz. Você resolve dar um passeio '
              'pelo templo e depois de um tempo, entediado vai para os seus aposentos. Dois '
              'dias depois você recebe a notícia que Heragon foi emboscado e morto '
              'no caminho de ida. A culpa o toma, pois um amigo morreu em seu lugar. Talvez '
              'aquela missão fosse exclusivamente para você. A aventura acabou!\n'
              'Digite "inicio" para jogar novamente.\n')

        print('Autoria: Allan de Sousa Soares - IFBA VDC')
        print('Canal: https://www.youtube.com/c/MatematicaParaGenteGrande\n')


    if event == 'Seguir' and t == '6':
        caminho.append('6')
        window['image.png'].Update('image6.png', visible=True)
        print('[6] Claro! Sendo um filho de um exímio caçador, escalar algumas árvores em busca '
              'de combustível para a tocha não será difícil e fará você economizar um bom '
              'tempo. Você encontra uma árvore e localiza em seu topo, uma espécie de coco '
              'muito rico em óleo, combustível suficiente para uma noite inteira. Você então '
              'começa a escalar a árvore. Perto do meio, suas pernas e braços começam a tremer, '
              'pois está fora de forma. Contudo, você consegue chegar até o topo. Não foi tão '
              'difícil assim. Você descansa por alguns minutos no topo da árvore e, antes de '
              'descer lança  o coco ao solo. Em certo momento da descida você pisa em falso e '
              'despenca. Ao cair acaba atingindo-o em cheio um galho e depois o solo, sua visão '
              'fica turva, você simplesmente apaga. Você acorda no templo de Amiz e fica sabendo '
              'que lhe levaram todos os seus pertences, sua armadura, maça, escudo e cavalos e por '
              'sorte um viajante o encontrou caído em meio à mata e o trouxe para o templo. '
              'A aventura acabou!\n'
              'Digite "inicio" para jogar novamente.\n')

        print('Autoria: Allan de Sousa Soares - IFBA VDC')
        print('Canal: https://www.youtube.com/c/MatematicaParaGenteGrande\n')

    if event == 'Seguir' and t == '7':
        caminho.append('7')
        window['image.png'].Update('image7.png', visible=True)
        print('[7] Pensando ser algo urgente e confiante que Amiz o guiará, você pega a bússola, mesmo '
              'quebrada, os mantimentos, suas armas e monta em seu cavalo rumo ao leste. Para sua '
              'sorte, você se lembra que certa vez foi comprar mantimentos em um vilarejo e, se não '
              'lhe falha a memória, é exatamente para lá que você deve ir agora. Uma pequena trilha '
              'pela floresta dos risos o levará até seu destino. Dizem que esta floresta é responsável '
              'por desaparecimentos de viajantes. Mas a sua confiança em Amiz e seu respeito por '
              'Knolan o enchem de confiança para seguir. No meio da manhã você parte pela trilha em '
              'meio às altas árvores desta floresta. Certamente, se tudo correr bem, amanhã pela '
              'manhã você estará chegando ao seu destino. Andando por algumas horas dentro da mata '
              'você decide parar para descansar. Sentado, em frente a uma fogueira improvisada você '
              'esquenta petiscos de carne e queijo e os come para matar a fome. Enquanto descansa '
              'você imagina como será a noite em meio à mata e lembra que não trouxe tochas caso '
              'precise deixar o acampamento. Se você quiser tentar improvisar tochas digite 17. Se '
              'não, digite 10.\n')

    if event == 'Seguir' and t == '8':
        caminho.append('8')
        window['image.png'].Update('image8.png', visible=True)
        if 'Tocha' in inventario:
            print('[8] De posse de uma tocha e filho de um grande caçador você sabe que perigos como esses '
                  'devem ser enfrentados antes que eles os surpreendam. Contudo, carregar a tocha, a maça '
                  'e o escudo com apenas duas mãos é bastante desconfortável. Se você optar por '
                  'colocar o escudo nas costas e seguir com a maça na mão direita e a tocha na mão '
                  'esquerda, digite 14. Se preferir segurar a tocha numa das mãos, juntamente com o '
                  'escudo 19.\n')
        else:
            print('[8] Você não tem uma tocha, digite')

    if event == 'Seguir' and t == '9':
        caminho.append('9')
        inventario.append('Tocha Improvisada')
        window['image.png'].Update('image9.png', visible=True)
        print('[9] Mesmo sendo filho de um exímio caçador, a vida no templo é um pouco sedentária e '
              'você certamente estaria correndo perigo escalando árvores tão altas. Você se lembra '
              'de pequenos coquinhos que caem das árvores quando maduros. Ao serem esmagados oferecem '
              'um bom óleo combustível. Você os recolhe durante cerca de uma hora e os amassa, retirando '
              'assim um pouco de óleo para embeber as tochas para que durem mais. Agora poderá andar '
              'pela noite se preciso for. Você então retorna para a trilha. Digite 10.\n')

    if event == 'Seguir' and t == '10':
        caminho.append('10')
        window['image.png'].Update('image10.png', visible=True)
        print('[10] Você segue pela trilha em meio às árvores da floresta dos risos e logo se dá conta de '
              'por que ela tem este nome. Pequenos sons, semelhantes a risos de crianças vem da copa das '
              'árvores com o passar dos fortes ventos que sopram acima. Por sorte, os ventos são barrados '
              'pelas árvores e você sente apenas uma leve brisa refrescante. Com o cair da noite a brisa '
              'aumenta e já é hora de armar acampamento. Andar, além de perigoso, poderia lhe render um '
              'resfriado. Você recolhe alguns gravetos, faz uma cama e uma fogueira improvisadas. Embora '
              'não fiquem tão bons quanto o que o seu velho fazia, darão certamente para passar a noite. '
              'Digite 16.\n')

    if event == 'Seguir' and t == '11':
        caminho.append('11')
        window['image.png'].Update('image11.png', visible=True)
        print('[11] Intrigado, você resolve investigar a que se destinava o pergaminho de cura. Alguns dias '
              'depois você fica sabendo da morte de uma pequena garotinha na vila a qual recusara a ir. '
              'A culpa toma conta do seu ser. Desde aquele dia você nunca mais se perdoou. A aventura '
              'acabou!\n'
              'Digite "inicio" para jogar novamente.\n')

        print('Autoria: Allan de Sousa Soares - IFBA VDC')
        print('Canal: https://www.youtube.com/c/MatematicaParaGenteGrande\n')

    if event == 'Seguir' and t == '12':
        caminho.append('12')
        window['image.png'].Update('image12.png', visible=True)
        print('[12] Você não tem uma tocha, mas quem precisa de uma quando se tem um cavalo veloz. Você pega '
              'suas coisas, arranca, da fogueira, um pedaço de lenha ainda em chamas e se coloca a correr '
              'pela trilha. A silhueta da criatura começa a ficar para traz, mas um forte vento aliado à sua '
              'velocidade apagam a tocha o deixando no escuro total, mas ainda em disparada sobre o cavalo. '
              'Você tenta pará-lo, mas ele parece não obedecer aos seus comandos. Você se irrita e aplica-lhe '
              'as esporas com força. Neste momento ele para bruscamente e você é arremessado para frente '
              'chocando-se com uma árvore. Você vê que bateu com a cabeça e que está sangrando muito. Meio '
              'tonto e confuso, como o barulho dos risos provenientes do encontro da copa das árvores com o '
              'vento você vê o mundo girar cada vez mais rápido e simplesmente desmaia. Algum tempo depois, '
              'sem estar certo de quanto, você acorda. Em sua frente, uma criatura parece preparar algo para '
              'comer em um grande caldeirão. O cheiro dos temperos parece bom, mas para seu desespero você '
              'parece ser a carne. A aventura acabou.\n'
              'Digite "inicio" para jogar novamente.\n')

        print('Autoria: Allan de Sousa Soares - IFBA VDC')
        print('Canal: https://www.youtube.com/c/MatematicaParaGenteGrande\n')

    if event == 'Seguir' and t == '13':
        caminho.append('13')
        window['image.png'].Update('image13.png', visible=True)
        print('[13] Seu coração bate acelerado. Você se mantém fixamente olhando para frente, mas alguns minutos '
              'se passam e parece que o quer que tenha tentado adentrar no acampamento se afastou. Você então '
              'se senta um pouco, pois a noite ainda é longa conforme observa que a fogueira pouco queimou...\n' 
              '“XHIMM”\n'
              'Este é o barulho de uma espada atingindo em cheio sua cabeça e descendo pelas suas costas. O '
              'intruso decidiu atacar por cima saltando sobre você. Caído ao chão você percebe que não consegue '
              'movimentar os braços e as pernas. A criatura, de aspecto humanoide, tem feições semelhantes às de '
              'um porco. Ela se aproxima de você pega seus mantimentos e armas e o ignora deixando-o para traz. '
              'Certamente, o local que escolheu, é um pouco inacessível o que dificultará que alguém o socorra. '
              'Você começa a gritar por socorro. Eis que escuta o barulho de passos sobre os gravetos secos. '
              'Alguém parece ter escutado seus gritos e veio ajuda-lo. Para sua surpresa um enorme urso aparece, '
              'provavelmente atraído pelo cheiro de seu sangue! A aventura terminou.\n'
              'Digite "inicio" para jogar novamente.\n')

        print('Autoria: Allan de Sousa Soares - IFBA VDC')
        print('Canal: https://www.youtube.com/c/MatematicaParaGenteGrande\n')

    if event == 'Seguir' and t == '14':
        caminho.append('14')
        window['image.png'].Update('image14.png', visible=True)
        print('[14] Sua reputação de guerreiro nunca foi tão boa assim para lutar sem sua maça. Seria abusar da '
              'sorte lutar de posse de um escudo e uma tocha, pois seus golpes poderiam ser ineficientes. Você '
              'coloca o escudo nas costas e segue com sua maça na mão direita e a tocha na mão esquerda. A criatura, '
              'percebendo que você dispõe de uma tocha e a está perseguindo, parece ter decidido fugir. Contudo, '
              'você quer saber de que se trata e tirar satisfações. Você, mesmo de placas, se move com certa '
              'facilidade pela mata, habilidade herdade desde a infância. Em certo ponto, já próximo à criatura a '
              'mesma desaparece o que indica uma provável emboscada. Em alerta você caminha cuidadosamente '
              'pela mata.\n'
              '“HURRAAA”\n'
              'Este é o grito que a criatura, cujas feições são uma mistura de homem e porco, '
              'provavelmente um orc asqueroso, lança no exato momento em que te ataca com toda sua força. '
              'Mas você estava atento e consegue aparar e devolver-lhe um poderoso golpe no peito a deixando '
              'sem ar. Você retira a arma da mão dela e dá uma ordem para que fuja. Visivelmente intimidada, '
              'a criatura foge. Você sabe que ela não o importunará mais. Você refaz a armadilha e volta a '
              'descansar. Digite 18.\n')

    if event == 'Seguir' and t == '15':
        caminho.append('15')
        window['image.png'].Update('image15.png', visible=True)
        print('[15] Você ciente de que esperar não é uma boa escolha decide procurar. A falta de uma tocha não '
              'é um problema para você, pois um pedaço de lenha, em chamas, retirado da fogueira, deve ser '
              'o suficiente. Você vai até a fogueira retira um pedaço grande e caminha em direção à mata. '
              'Você parece ver a criatura se afastando, mas ainda assim decide andar um pouco mais na direção '
              'dela. Após cerca de dois minutos de caminhada, mata a dentro, uma forte ventania sopra e apaga '
              'as chamas do pedaço de madeira que iluminava seu caminho. Você dá meia volta e começa a correr '
              'desesperadamente para em direção à luz do acampamento. Você tropeça algumas vezes e a cerca de '
              '10 metros dos rochedos e então para por alguns instantes para descansar...'
              '“CRUSHI”\n'
              'Este é o barulho de uma espada perfurando o seu peito. Parece que a criatura o surpreendeu '
              'enquanto você se levantava. O golpe lhe deixa sem forças para lutar, mas ainda para perceber '
              'que se trata de uma criatura com feições semelhantes à de um porco. O inimigo sorri para você '
              'enquanto seu sangue escorre pela lâmina de sua espada. Não há mais nada o que fazer. A aventura '
              'acabou.\n'
              'Digite "inicio" para jogar novamente.\n')

        print('Autoria: Allan de Sousa Soares - IFBA VDC')
        print('Canal: https://www.youtube.com/c/MatematicaParaGenteGrande\n')

    if event == 'Seguir' and t == '16':
        caminho.append('16')
        window['image.png'].Update('image16.png', visible=True)
        print('[16] Você está um pouco cansado depois de um longo dia cavalgando e após a montagem do acampamento '
              'você resolve dar uma cochilada. O local que escolheu para acampar, entre dois rochedos, parece '
              'bastante seguro e relativamente inacessível a perigos. Você arma uma pequena armadilha para '
              'avisar da presença de intrusos que se aproximem a menos de quinze metros de você. A armadilha '
              'é bastante simples, consta apenas de alguns gravetos que se partirão anunciando a presença de '
              'algo maior que um cachorro. Você então repousa sobre sua cama improvisada e adormece...\n'
              '“CRAK”\n'
              'Você acorda em alerta ao após ouvir os sons de gravetos se partindo. Parece que algo se '
              'aproximou do acampamento. Bastante atento você pega sua maça, escudo e caminha por uns dois '
              'metros. Olhando fixamente para frente durante cerca de 10 segundos sua vista começa a perceber '
              'uma silhueta humana, mas ela se afasta mais para o escuro. Você sabe que seja o que for que '
              'estiver na mata certamente irá ataca-lo a menos que você o combata antes. Se preferir esperar '
              'no acampamento digite 13. Se preferir ir atrás da do invasor digite 4.\n')

    if event == 'Seguir' and t == '17':
        caminho.append('17')
        window['image.png'].Update('image17.png', visible=True)
        print('[17] Você se lembra de conselhos de seu pai de nunca andar a noite sem uma tocha ou lampião. Além disso, '
              'sendo filho de um exímio caçador improvisar algumas tochas não é tarefa difícil para você '
              'apenas um pouco demorado. Se quiser improvisar tochas mais rapidamente, pegando um pouco de '
              'óleo de coco, no topo das árvores locais, digite 6. Se preferir não se arriscar tanto subindo em '
              'árvores e quiser procurar por materiais oleaginosos em terra, mesmo que isto gaste mais tempo, digite 9. '
              'Se acha que uma tocha não é importante e que uma fogueira, ao acampar já é o suficiente, digite 10.\n')

    if event == 'Seguir' and t == '18':
        caminho.append('18')
        window['image.png'].Update('image18.png', visible=True)
        print('[18] Já pela manhã, você apaga a fogueira, desmancha o acampamento e segue para o vilarejo. As '
              'grandes árvores vão ficando para trás e você já pode avistar as primeiras casas. Você se dirige '
              'a um homem que trabalha em uma horta e o pergunta sobre Lázaro. O mesmo, sem dizer uma só palavra '
              'faz um sinal para que você o acompanhe. Ele o leva até uma casa simples e vocês são recebidos '
              'por um senhor de aparência cansada. O homem então anuncia:\n'
              '- Este é Lázaro.\n'
              'Você então entrega ao mesmo o pergaminho. Ele o toma em suas mãos, o abre, dar um sorriso de '
              'canto de boca e com uma voz tímida diz:\n'
              '- Eu não sei ler senhor. De que se trata?\n'
              'Você toma o pergaminho e nota que trata-se de um feitiço de cura. Ao mencionar isso, Lázaro '
              'o puxa e o leva até um quarto no qual uma garotinha repousa enferma sobre uma cama.\n'
              '- Deve ser para ela senhor.\n'
              'Sem prensar duas vezes você lê as palavras e um raio de luz branca se dirige à garotinha. '
              'Pouco tempo depois a mesma se levanta. Lázaro não consegue pronunciar uma só palavra pois lágrimas '
              'de euforia correm pelos seu olhos. Você então sobe em seu cavalo e deixa a vila sob os aplausos '
              'de todos ali presentes. Vá para 20.\n')

    if event == 'Seguir' and t == '19':
        caminho.append('19')
        window['image.png'].Update('image19.png', visible=True)
        print('[19] Embora, sua reputação de guerreiro não seja tão boa, lutar sem uma defeza apropriada não'
              'parece adequado. Você então pega sua tocha com a mão direita e o escudo com a mão esquerda e deixa'
              'sua maça amarrada à cintura caso precise usar. A criatura, percebendo que você dispõe de uma tocha '
              'e a está perseguindo, parece ter decidido fugir. Contudo, você quer saber de que se trata e tirar '
              'satisfações. Você, mesmo de placas, se move com certa facilidade pela mata, habilidade herdade desde '
              'a infância. Em certo ponto, já próximo à criatura a mesma desaparece o que indica uma provável '
              'emboscada. Em alerta você caminha cuidadosamente pela mata.\n'
              '“HURRAAA”\n'
              'Este é o grito que a criatura, cujas feições são uma mistura de homem e porco, '
              'provavelmente um orc asqueroso, lança no exato momento em que te ataca com toda sua força. '
              'Mas você estava atento e consegue bloquear e golpeá-la no rosto com a tocha atingindo seus olhos '
              'deixando-a com a visão comprometida. Você retira a arma da mão dela e dá uma ordem para que fuja. '
              'Visivelmente intimidada, a criatura foge. Você sabe que ela não o importunará mais. Você refaz a '
              'armadilha e volta a descansar. Digite 18.\n')

        print('Autoria: Allan de Sousa Soares - IFBA VDC')
        print('Canal: https://www.youtube.com/c/MatematicaParaGenteGrande\n')

    if event == 'Seguir' and t == '20':
        caminho.append('20')
        window['image.png'].Update('image20.png', visible=True)
        print('[20] Intrigado, você parte rumo ao templo de Amiz a fim de saber por que Knolan tinha lhe dado uma bússola'
              ' quebrada. Ao chegar lá Knolan o espera com um sorriso discreto.\n'
              '- Olá meu caro Dasmius, já de volta. Hoje o almoço será por minha conta.\n'
              'Você o questiona sobre o motivo de ter-lhe entregue uma bússola quebrada.\n'
              '- Este era o seu destino meu caro Dasmius. Se perdeu em algum momento?\n'
              'Você responde que não se perdera, pois lembrava o caminho e que graças aos conhecimentos que '
              'seu pai lhe passara na infância conseguiu sobreviver aos perigos da floresta. Ele olha para '
              'você e diz.\n'
              '- Veja a tocha em sua cintura, ela o guiou para o caminho certo em meio à escuridão. Amiz '
              'lhe agraciou com um belo presente...\n'
              'Digite "inicio" para jogar novamente.\n')

        print('Autoria: Allan de Sousa Soares - IFBA VDC')
        print('Canal: https://www.youtube.com/c/MatematicaParaGenteGrande\n')

window.close()

