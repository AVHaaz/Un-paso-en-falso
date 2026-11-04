# Coloca el código de tu juego en este archivo.

# Declara los personajes usados en el juego como en el ejemplo:



label start:

    "¿Cómo te gustaría que te llamen?"

    $jugador=renpy.input("Escribe tu nombre")

    if jugador == "":
        $jugador = "Jugador"

    "Mucho gusto, [jugador], disfruta de la experiencia."
   

    scene SALON
    "Después de un lluvioso día en la escuela, tus clases terminan exactamente a las 6PM."

    show amigop1
    amigo "No puedo creer que el maestro se tomará exactamente las 2 horas clase."

    show amigap1
    amiga "¡Exacto! más con la lluvia que ya lleva rato!"
    amiga "¿Acaso no sabe lo mal que se ponen las calles después de que caen tres gotas en esta ciudad?"
   
    hide amigap1
    hide amigop1

    "Tu y tus amigos siguen platicando sin rumbo un par de minutos hasta que uno de ellos muestra algo de su celular."

    show amigop1
    amigo "¿Oigan ya vieron lo que publicaron en la facultad?"
    amigo "Es sobre el fenómeno del Niño."

    "Miras el anuncio en el celular."
    call screen ver_cartel
   
    amigo "Se supone que hoy llegaba algo fuerte."

    show amigap1

    "Todos miran con detenimiento la publicación."
    "Puede que sea información útil para el futuro."

    amiga "Chanfle y yo que aun tengo que recoger a mi hermano de la escuela a las 7."

    amigo "Que mala suerte la tuya jaja."

    amiga "¡Ya basta! no se rían."

    amigo "Bueno jaja, yo ya me voy porque ya va a llegar mi camión."
    amigo "¡Suerte con la lluvia chicos!"

    amiga "¡Adióssss!"

    hide amigop1
    
    amiga "Lo siento [jugador] me gustaría seguir platicando pero ya me tengo que ir antes de que se haga más tráfico."
    amiga "Tu deberías hacer lo mismo, no te vayas a quedar atrapado en la tormenta."
    amiga "Jaja cuidado con tu carro chaparro y los charcos."

    scene ESTACIONAMIENTO
    "Tu y tu amiga se despiden en la entrada del estacionamiento de la facultad y toman caminos diferentes."
    "Subes a tu carro {i}chaparro{/i}, según tu amiga, y sales del campus."

    scene CARRO1
    "El camino es algo largo pero te motiva saber que al llegar te espera tu perrito “Chancho” con mucho entusiasmo."
    "Por un rato no observas mucho tráfico entonces vas a una velocidad moderada, sin embargo más adelante te das cuenta que en la bajada de la calle hay una laguna que cubre todos los carriles a lo ancho de la calle."
    "¿Qué harás?"

    menu:
        "Seguir con tu velocidad normal y pasar sin perder el tiempo":
            "Wujuu pasaste sin ningun problema y hasta le salpicaste a otro carro cercano."
            "Pero no le tomas importancia porque significa que vas a ver a Chancho más rápido."

            "*Sonido de carro apagandose*"

            jugador "Oh…?"

            "De un momento a otro tu carro deja de marchar y te quedas varado a unos metros de la laguna."
            "Salpicaste agua de forma que entró a tu motor y lo dejó inhabil por unas horas."

            scene NEGRO
            FIN "{b}FINAL 1: Hidrobloqueo{/b} \nNo llegaste a casa a tiempo y por no bajar la velocidad no pudiste ver a tu perrito Chancho esa noche."
            return

        "Pasar con una velocidad baja y constante con precaución":
            "Bajaste la velocidad de tu carro y pasaste sin levantar el agua de la laguna."
            "A lado de ti pasa un carro similar al tuyo a la misma velocidad a la que ibas tú anteriormente."
            "Al pasar te salpica."

            jugador "Nooo ya me ensucio este."

            "No pasan muchos metros hasta que lo alcanzas."
            "Miras que su carro está detenido y no puede prenderse."
            "Al parecer le entró agua."

            jugador "Uy… que bueno que no soy ese."

            "Continuas con tu camino como de costumbre."
            "¡GRACIAS POR JUGAR LA VERSION BETA DE ESTA EXPERIENCIA!"
            "CONTINUARÁ…"


    # Finaliza el juego:

    return
