from django.shortcuts import render, get_object_or_404

def clubes(request):
    clubes = {
        'Deportes': [
            {'nombre': 'Club de Fútbol', 'imagen': 'https://clubmontesur.com.mx/cdn/shop/articles/club-deportivo-y-social.jpg?v=1700095211', 'integrantes': 25},
            {'nombre': 'Club de Baloncesto', 'imagen': 'https://clubmontesur.com.mx/cdn/shop/articles/club-deportivo-y-social.jpg?v=1700095211', 'integrantes': 18},
            {'nombre': 'Club de Voleibol', 'imagen': 'https://clubmontesur.com.mx/cdn/shop/articles/club-deportivo-y-social.jpg?v=1700095211', 'integrantes': 20},
            {'nombre': 'Club de Ajedrez', 'imagen': 'https://clubmontesur.com.mx/cdn/shop/articles/club-deportivo-y-social.jpg?v=1700095211', 'integrantes': 15},
            {'nombre': 'Club de Atletismo', 'imagen': 'https://clubmontesur.com.mx/cdn/shop/articles/club-deportivo-y-social.jpg?v=1700095211', 'integrantes': 22},
        ],
        'Ciencia': [
            {'nombre': 'Club de Ingles', 'imagen': 'https://clubmontesur.com.mx/cdn/shop/articles/club-deportivo-y-social.jpg?v=1700095211', 'integrantes': 30},
            {'nombre': 'Club de Astronomía', 'imagen': 'https://clubmontesur.com.mx/cdn/shop/articles/club-deportivo-y-social.jpg?v=1700095211', 'integrantes': 22},
            {'nombre': 'Club de Matemáticas', 'imagen': 'https://clubmontesur.com.mx/cdn/shop/articles/club-deportivo-y-social.jpg?v=1700095211', 'integrantes': 25},
            {'nombre': 'Club de Química', 'imagen': 'https://clubmontesur.com.mx/cdn/shop/articles/club-deportivo-y-social.jpg?v=1700095211', 'integrantes': 18},
            {'nombre': 'Club de Física', 'imagen': 'https://clubmontesur.com.mx/cdn/shop/articles/club-deportivo-y-social.jpg?v=1700095211', 'integrantes': 19},
        ],
    }

    return render(request, 'clubes.html', {'clubes': clubes})

def detalle_club(request, nombre):
    clubes = {
        'Club de Fútbol': {
            'imagenes': [
                'https://clubmontesur.com.mx/cdn/shop/articles/club-deportivo-y-social.jpg?v=1700095211',
            ],
            'descripcion': ' un espacio donde la pasión por el deporte se mezcla con el espíritu de superación y trabajo en equipo, hemos cultivado un ambiente de aprendizaje y competencia, llevando a nuestros jugadores a alcanzar logros impresionantes, incluyendo la clasificación a los nacionales. Nuestra Misión: Promover el desarrollo integral de los estudiantes a través del fútbol, fomentando valores como la disciplina, el respeto y la camaradería, mientras se perfeccionan sus habilidades deportivas. Logros Destacados: Clasificación a los nacionales en [año], donde nuestros jugadores mostraron su talento y determinación ante los mejores equipos del país. Campeones de [nombres de torneos o ligas relevantes], consolidando nuestra reputación como un club competitivo y destacado. Entrenamientos y Formación: Nuestro equipo de entrenadores está compuesto por profesionales apasionados que brindan formación de calidad, adaptada a cada nivel. Nos enfocamos en el desarrollo técnico, táctico y físico de nuestros jugadores, preparándolos para enfrentar desafíos en el campo.'
        },
        'Club de Baloncesto': {
            'imagenes': [
                'https://clubmontesur.com.mx/cdn/shop/articles/club-deportivo-y-social.jpg?v=1700095211',
            ],
            'descripcion': 'donde la pasión por el baloncesto se encuentra con el espíritu de trabajo en equipo y superación personal. Desde nuestra creación en [año], hemos forjado un camino de éxito, llevando a nuestros jugadores a alcanzar la competencia nacional. Nuestra Misión: Fomentar el desarrollo integral de los estudiantes a través del baloncesto, promoviendo valores como la disciplina, el respeto y la perseverancia, mientras potenciamos sus habilidades deportivas. Logros Destacados: Clasificación a los nacionales en [año], donde nuestros Leones demostraron su talento y determinación frente a los mejores equipos del país. Campeones de [nombres de torneos o ligas relevantes], consolidando nuestra posición como un club competitivo y destacado en el ámbito escolar.'
        },
        'Club de Voleibol': {
            'imagenes': [
                'https://clubmontesur.com.mx/cdn/shop/articles/club-deportivo-y-social.jpg?v=1700095211',
            ],
            'descripcion': 'un espacio dedicado al desarrollo de habilidades, la diversión y el trabajo en equipo a través del emocionante deporte del voleibol. Nuestro Club está diseñado para estudiantes de todos los niveles, desde principiantes hasta aquellos con experiencia previa, y busca fomentar un ambiente inclusivo y motivador. Objetivos del Club: Desarrollo de Habilidades: Enseñar las técnicas fundamentales del voleibol, incluyendo saque, recepción, colocación y remate, adaptadas al nivel de cada participante. Promoción del Trabajo en Equipo: Fomentar la comunicación y la colaboración entre los jugadores, destacando la importancia del trabajo en equipo en el deporte. Fomento de la Actividad Física: Incentivar un estilo de vida saludable a través de la práctica regular de deporte, mejorando la condición física y la coordinación. Estructura del Club: Sesiones Prácticas: Entrenamientos semanales que incluyen ejercicios técnicos, tácticos y juegos adaptados para practicar lo aprendido de manera divertida. Torneos Internos: Organización de competiciones amistosas para aplicar las habilidades adquiridas en un ambiente de juego real y disfrutar del espíritu competitivo.'
        },
        'Club de Ajedrez': {
            'imagenes': [
                'https://clubmontesur.com.mx/cdn/shop/articles/club-deportivo-y-social.jpg?v=1700095211',
            ],
            'descripcion': ' un espacio donde la estrategia, la lógica y la creatividad se unen para desarrollar habilidades mentales a través del fascinante juego del ajedrez. Este taller está diseñado para estudiantes de todos los niveles, desde principiantes que desean aprender las reglas hasta jugadores experimentados que buscan mejorar su juego.Fomento del Pensamiento Crítico: Desarrollar habilidades de análisis y resolución de problemas mediante la práctica del ajedrez, promoviendo la toma de decisiones estratégicas. Mejora de la Concentración: Ayudar a los estudiantes a mejorar su enfoque y concentración, habilidades que son valiosas tanto en el juego como en su vida académica. Creación de Comunidad: Fomentar un ambiente de colaboración y amistad, donde los participantes puedan compartir conocimientos y experiencias.'
        },
        'Club de Atletismo': {
            'imagenes': [
                'https://clubmontesur.com.mx/cdn/shop/articles/club-deportivo-y-social.jpg?v=1700095211',
            ],
            'descripcion': ' un espacio diseñado para fomentar la pasión por el deporte y el desarrollo físico a través de diversas disciplinas atléticas. Este taller está abierto a estudiantes de todos los niveles, desde principiantes que quieren explorar el atletismo hasta atletas experimentados que desean perfeccionar sus habilidades.'
        },
        'Club de Ingles': {
            'imagenes': [
                'https://clubmontesur.com.mx/cdn/shop/articles/club-deportivo-y-social.jpg?v=1700095211',
            ],
            'descripcion': 'Un espacio dedicado a mejorar las habilidades lingüísticas de los estudiantes a través de actividades interactivas y dinámicas. Este taller está diseñado para todos los niveles, desde principiantes que quieren aprender lo básico hasta estudiantes más avanzados que buscan perfeccionar su dominio del idioma.'
        },
        'Club de Astronomía': {
            'imagenes': [
                'https://clubmontesur.com.mx/cdn/shop/articles/club-deportivo-y-social.jpg?v=1700095211',
            ],
            'descripcion': 'Un espacio dedicado a explorar el fascinante mundo del cosmos y desarrollar habilidades en este apasionante campo. Este taller está diseñado para estudiantes de todos los niveles, desde aquellos que están comenzando a interesarse por la astronomía hasta los que desean profundizar su conocimiento y participar en competencias.'
        },
        'Club de Matemáticas': {
            'imagenes': [
                'https://clubmontesur.com.mx/cdn/shop/articles/club-deportivo-y-social.jpg?v=1700095211',
            ],
            'descripcion': 'Un espacio diseñado para fortalecer tus habilidades matemáticas y hacer que el aprendizaje de esta disciplina sea divertido y accesible. Mejora de Habilidades Matemáticas: Desarrollar competencias en áreas clave como álgebra, geometría, cálculo y estadística, a través de ejercicios prácticos y actividades interactivas.'
        },
        'Club de Química': {
            'imagenes': [
                'https://clubmontesur.com.mx/cdn/shop/articles/club-deportivo-y-social.jpg?v=1700095211',
            ],
            'descripcion': 'Espacio emocionante donde la ciencia cobra vida a través de experimentos, descubrimientos y aprendizaje práctico. Desarrollo de Habilidades Prácticas: Realizar experimentos y prácticas de laboratorio que permitan a los estudiantes aplicar la teoría y observar la química en acción.'
        },
        'Club de Física': {
            'imagenes': [
                'https://clubmontesur.com.mx/cdn/shop/articles/club-deportivo-y-social.jpg?v=1700095211',
            ],
            'descripcion': 'Nuestra Misión: Fomentar un amor por la física y desarrollar habilidades críticas en la resolución de problemas, el pensamiento analítico y la colaboración en equipo. A través de proyectos y desafíos, queremos preparar a nuestros miembros para enfrentar retos en competencias científicas. Desarrollo de Habilidades Prácticas: Realizar experimentos y construir prototipos que ilustren conceptos físicos, desde la mecánica hasta la termodinámica. Esto no solo ayuda a comprender la teoría, sino que también refuerza el aprendizaje a través de la práctica.'
        }
    }

    club = get_object_or_404(clubes, nombre)

    publicaciones = [
        {'titulo': f'Publicación {i+1}', 'contenido': f'Contenido de la publicación {i+1}', 'imagenes': ['https://clubmontesur.com.mx/cdn/shop/articles/club-deportivo-y-social.jpg?v=1700095211'], 'videos': []} 
        for i in range(20)
    ]

    miembros = [
        {'nombre': f'Miembro {i+1}', 'imagen': 'https://clubmontesur.com.mx/cdn/shop/articles/club-deportivo-y-social.jpg?v=1700095211'}
        for i in range(10)
    ]

    return render(request, 'detallesClub.html', {
        'nombre': nombre,
        'imagenes': club['imagenes'],
        'descripcion': club['descripcion'],
        'publicaciones': publicaciones,
        'miembros': miembros
    })
