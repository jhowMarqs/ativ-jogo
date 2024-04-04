
# personagens
define d = Character("Dante")
define h = Character("Husk")
define k = Character("Kai")


# o jogo começa aqui

label start:

    scene cenarioluacheia
    with fade
    play music "risk-136788.mp3"

    "Dante era um jovem duende pobre que morava em um pântano junto de sua mãe e seus dois pequenos irmãos."

    show pisquinha at center
    with dissolve

    p "Não quero brigar com você, irmão"

    p "Essa luta não faz sentido para mim"

    hide pisquinha

    show husk at center
    with dissolve

    h "Deixa de conversa mole Pisquinha"

    h "Isto para mim tem outro nome"

    h "Covardia"

    hide husk

    "Pisquinha deve enfrentar o irmão Husk?"

menu:

    "Sim":
        jump game

    "Não":
        jump book

label game:

    show pisquinha at center
    with dissolve
    p "Se não há outra escolha, eu estou pronto, irmão"

    hide pisquinha

    show husk at center
    with dissolve

    h "Farei o que for necessário"

    hide husk

    jump marry

label book:

    show husk at center
    with dissolve

    h "Você não tem escolha, lembre-se a força vem do seu interior"

    hide husk

    show pisquinha at center
    with dissolve

    p "Eu não queria, mas se é o unico jeito..."

    hide pisquinha

    jump marry

label marry:

    "Então os irmãos batalham"
    stop music

    return