"""contiene los datos html de cada página"""
page_data = {}

page_data[0] = """
Página <b>zero</b>
"""


page_data[1] = """
<h1>Charla: Herramientas para crear sitios web</h1>
<p>Hola soy Henry Tong</p>
<p><img src="henry.jpg" alt="foto de Henry Tong" title="Henry Tong" /></p>
<p>Me dedico al estudio, diseño y creación de software desde hace más de 20 años participando en proyectos de informática.</p>
<p>Mi correo electrónico es:  taksantong@gmail.com</p>
"""

page_data[2] = """
<h1>Agenda</h1>
<p>En esta charla hablaremos de:</p>
<ul>
<li>Herramientas disponibles que nos permiten sitios web</li>
<li>Qué es un CMS</li>
<li>Qué es un LMS</li>
<li>Compartiva Wordpress versus Joomla versus Drupal</li>
</ul>
"""

page_data[3] = """
<h1>Qué es un sitio web</h1>
<ul>
<li>Todos necesitamos por una razón u otra tener una prescencia en internet</li>
<li>Blog, portafolio, página web de una empresa o de una comunidad</li>
</ul>
<h2>Cómo lograrlo?</h2>
<p>Tres principales opciones:</p>
<ol>
<li>Programar o codificar un sitio web</li>
<li>Utilizar un servicio en línea. Ejemplo: Servicio Wix</li>
<li>Utilizar una plataforma o herramienta. Ejemplo: Wordpress</li>
</ol>
<p>Esta charla se enfoca en la tercera opción</p>
"""
page_data[4] = """
<h1>Qué es un CMS</h1>
<ul>
<li>Abreviación del inglés que Significa Sistema de Manejo de Contenido</li>
<li>Herramienta que nos permite, sin tener conocimientos de programación, armar un sitio web en todos sus aspectos: diseño, contenido, roles, analíticas y SEO.</li>
<li>CMS populares: Wordpress, Joomla y Drupal</li>
<li>CMS conocidos: Backdrop, Modx</li>
</ul>
<p>Nota: A pesar de que Drupal, Backdrop y Modx ofrecen muy buena accesibilidad, no son lo más utilizados</p>
"""
page_data[5] = """
<h1>Qué es un LMS</h1>
<ul>
<li>Abreviación del inglés que Significa Sistema de Manejo de Contenido especializado en Educación (Tanto de aprendizaje como de evaluación de los alumnos)</li>
<li>LMS popular y gratuito: Moodle</li>
<li>LMS populares y comerciales: Canva, Blackboard</li>
<li>Otra opción interesante es tomar de base un CMS y agregale un plugin de LMS</li>
</ul>
"""
page_data[6] = """
<h1>Comparativa de los tres CMS más populares</h1>
<p>Nota: El CMS debe ser accesible para el creador de contenido, no solamente para el visitante web.</p>
<h2>Drupal</h2>
<ul>
<li>Alto nivel de accesibilidad</li>
<li>Complejo de aprender, usar, instalar</li>
</ul>
<h2>Joomla</h2>
<ul>
<li>Medio nivel de accesibilidad</li>
</ul>
<h2>Wordpress</h2>
<ul>
<li>Medio nivel de accesibilidad</li>
<li>Muy fácil de instalar, aprender y usar</li>
<li>Abundante cantidad de plugins y documentación</li>
</ul>
"""
page_data[7] = """
<h1>Editor de contenido Gutenberg</h1>
<ul>
<li>Recientemente agregado a Wordpress como el editor por defecto</li>
<li>Editor visual (arrastrar bloques en pantalla) inaccesible inicialmente pero ha mejorado mucho últimamente</li>
<li>Hoy se usa para editar el texto; pero a futuro se podría usar para editar el sitio completo</li>
<li>El editor clásico de Wordpress todavía se puede utilizar hasta el 2022</li>
<li>Se ha creado el plugin Gutenberg para Drupal</li>
<li>El editor por defecto de Joomla es TinyMCE que ofrece buena accesibilidad</li>
</ul>
"""
page_data[8] = """
<h1>Joomla 4</h1>
<ul>
<li>Pronto (Agosto 2021) se lanzará la versión 4 de Joomla que promete mejoras de accesibilidad</li>
</ul>
"""
page_data[9] = """
Página en construcción
"""
page_data[10] = """
Página en construcción
"""

def get_page_html(page_id) -> str:
    """get_page_html"""
    return page_data[page_id]