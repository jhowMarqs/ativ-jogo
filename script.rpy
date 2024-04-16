# personagens
define d = Character("Dante")
define u = Character("Duma")
define t = Character("Trollbias")
define m = Character("Mãe")
define l = Character("Líder da gangue")
define g = Character("Gangue de Goblins")

# o jogo começa aqui

label start:

    scene florestadante
    with fade
    play music "/audio/misterio.mp3"
    show dante at left
    show trollbias at center
    show mae at right

    "Dante era um jovem duende pobre que morava em um pântano junto de sua mãe e o seu pequeno irmão."
    "Por serem duendes da cor azul, eles sempre sofriam racismo dos duendes da cor verde"

    hide trollbias
    hide mae
    show dante at center

    "Dante sempre saia de casa bem cedo para ir ao seu trabalho"
    
    "Qual deve ser o trabalho do Dante"

menu:

    "Entregar panfletos":
        jump panfletos

    "Trabalhar na loja de um gob":
        jump loja

label panfletos:

    scene cidade with fade
    show dante at center
    "Dante vai para a cidade entregar panfletos de apartamentogumelos a venda na cidade"
    jump principal

label loja:

    scene cidade with fade
    show dante at center
    "Dante vai para a cidade trabalhar na loja de um gob, uma loja que vende qualquer coisa por um preço acessivel"
    jump principal

label principal:

    "Mesmo tentando manter um sorriso no rosto"
    hide dante
    show dante_tri at center
    "Dante na verdade é muito infeliz com seu baixo salário"
    "No horario de almoço, Dante sempre vai almoçar em um restaurante de comida caseira ali perto"
    "É a única refeição que seu salário pode pagar"
    hide dante_tri
    show dante
    "Mas Dante não se importa com isso, ele gosta dessa comida"
    show dante at left
    show mulher_rica_gostosa at right
    "Dante saia do trabalho e ia para casa as 18:00 horas, um horario de pico no centro"
    show mulher_rica_gostosa at center
    show dante at center
    "Em toda essa correria, muitas pessoas não percebem o que acontece ao seu redor..."
    show mulher_rica_gostosa at left
    show dante at right
    "Muitos acabam perdendo seus pertences..."
    show dante_uau at right
    hide mulher_rica_gostosa
    hide dante
    show pertences at left
    show mulher_rica_gostosa at left
    "E outros..."
    hide mulher_rica_gostosa
    show dante_viu at right
    hide dante_uau
    "Ganham oportunidades"
    "Em toda essa correria, Dante nota que uma duende derrubou muito dinheiro no chão"
    "Dinheiro suficiente para mudar de vida"
    "O que Dante deve fazer?"

menu: 

    "Devolver o dinheiro para a moça":
        jump bom

    "Pegar o dinheiro para si":
        jump ruim

label bom:
    scene cidade
    show dante_uau_dir at right
    d "Moça! Moça!"
    show mulher_rica_gostosa_desc at left
    hide dante_uau_dir at right
    show dante_desc at right
    "..."
    u "Pois não?"
    hide dante_desc
    show dante_dir at right
    show pertences
    d "A senhora deixou isso cair"
    hide mulher_rica_gostosa_desc
    show mulher_rica_gostosa_uau at left
    "A moça não acredita no que ela viu"
    hide pertences
    u "Garoto, mesmo com todo o preconceito e racismo nessa cidade, você ainda quis ajudar alguem?"
    d "É... Eu sei que você não tem culpa de nada, além disso, se eu ficasse com o dinheiro, eu nunca poderia me perdoar"
    hide mulher_rica_gostosa_uau
    show mulher_rica_gostosa_desc at left
    u "Garoto qual seu nome? "
    d "Dante, senhora"
    hide mulher_rica_gostosa_desc
    show mulher_rica_gostosa_esq at left
    u "Prazer, Dante, meu nome é Duma"
    u "É de mais pessoas como você que essa cidade precisa"
    u "E minha empresa tambêm"
    hide dante_dir
    show dante_uau_dir at right
    u "Sua honestidade me impressiona, é dificil encontrar alguem como você para trabalhar com as contas da minha empresa"
    d "Eu... Eu..."

menu: 

    "Aceitar a proposta":
        jump sim

    "Recusar a proposta":
        jump nao

label sim:
    hide dante_uau_dir
    show dante_dir at right
    d "Sim! Eu aceito!"
    u "Perfeito vamos resolver toda a papelada imediatamente"
    return

label nao:
    d "Senhora Duma, muito obrigado pela proposta mas eu prefiro continuar onde estou trabalhando"
    u "Entendo"
    u "Espero te ver mais vezes"
    u "Até mais, Dante"
    d "Até mais"
    return

label ruim:
    scene cidade
    show dante_ladrao
    "Dante pega o dinheiro e sai correndo do local"
    "Enquanto corria evitando os outros duendes"
    "Dante entra em um beco"
    "Nesse beco Dante tromba com uma gangue de goblins"
    show lider_esq
    hide dante_ladrao
    show dante_tenso at left
    l "Ei! O que é isso, quem bateu em mim?"
    hide lider_esq
    show lider
    l "E aí parceiro, tá querendo problemas?"
    d "Eu... Eu..."
    hide dante_tenso
    show dante_ladrao at left
    "Em toda a tensão, Dante deixa o dinheiro cair"
    hide lider
    show lider_rindo
    l "He he he, e todo esse dinheiro aí?"
    show gangue at right
    l "Rapazes! Peguem ele!"
    hide dante_ladrao
    hide lider_rindo
    hide gangue
    show dante_ladrao at left
    show gangue at right
    l "Não deixem vestígios"
    g "Pode deixar chefe"
    hide dante_ladrao
    hide gangue
    "E dês de esse dia, Dante não voltou para casa..."