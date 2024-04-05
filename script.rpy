
# personagens
define d = Character("dante")
define u = Character("duma")
define g = Character("gnomia")
define t = Character("trollbias")
define m = Character("mae")
define l = Character("líder")

# o jogo começa aqui

label start:

    scene florestadante
    with fade
    play music "misterio.mp3"
    show dante(1) at left
    show trollbias(1) at center
    show mae(1) at right

    "Dante era um jovem duende pobre que morava em um pântano junto de sua mãe e o seu pequeno irmão."
    

    return

