vertex_shader = '''
#version 450 core

layout (location = 0) in vec3 position;
layout (location = 1) in vec2 texCoords;
layout (location = 2) in vec3 normals;

out vec2 outTexCoords;
out vec3 outNormals;
out vec4 outPosition;

uniform float time;
uniform mat4 modelMatrix;
uniform mat4 viewMatrix;
uniform mat4 projectionMatrix;


void main()
{
    outPosition = modelMatrix * vec4(position, 1.0);
	gl_Position = projectionMatrix * viewMatrix * outPosition;

    outTexCoords = texCoords;
    outNormals = normals;
}
'''

fat_shader = '''
#version 450 core

layout (location = 0) in vec3 position;
layout (location = 1) in vec2 texCoords;
layout (location = 2) in vec3 normals;

out vec2 outTexCoords;
out vec3 outNormals;
out vec4 outPosition;


uniform float time;
uniform mat4 modelMatrix;
uniform mat4 viewMatrix;
uniform mat4 projectionMatrix;


void main()
{
    outPosition = modelMatrix * vec4(position + normals * sin(time) / 10, 1.0);
	gl_Position = projectionMatrix * viewMatrix * outPosition;
    outTexCoords = texCoords;
    outNormals = normals;
}
'''

water_shader = '''
#version 450 core

layout (location = 0) in vec3 position;
layout (location = 1) in vec2 texCoords;
layout (location = 2) in vec3 normals;

out vec2 outTexCoords;
out vec3 outNormals;
out vec4 outPosition;

uniform float time;
uniform mat4 modelMatrix;
uniform mat4 viewMatrix;
uniform mat4 projectionMatrix;


void main()
{
    outPosition = modelMatrix * vec4(position + vec3(0,1,0) * sin(time * position.x * 10) /10, 1.0);
	gl_Position = projectionMatrix * viewMatrix * outPosition;
    outTexCoords = texCoords;
    outNormals = normals;
}
'''

skybox_vertex_shader = '''
#version 450 core

layout (location = 0) in vec3 inPosition;

uniform mat4 viewMatrix;
uniform mat4 projectionMatrix;

out vec3 texCoords;

void main()
{
    texCoords = inPosition;
    gl_Position = projectionMatrix * viewMatrix * vec4(inPosition, 1.0);
}

'''

fragment_shader = '''
#version 450 core

in vec2 outTexCoords;
in vec3 outNormals;
in vec4 outPosition;


uniform sampler2D tex;
uniform vec3 pointLight;


out vec4 fragColor;

void main()
{
    float intensity = dot(outNormals, normalize(pointLight - outPosition.xyz) );
	fragColor = texture(tex, outTexCoords) * intensity;
}
'''

negative_shader = '''
#version 450 core

in vec2 outTexCoords;
in vec3 outNormals;
in vec4 outPosition;

uniform sampler2D tex;


out vec4 fragColor;

void main()
{
	fragColor = 1 - texture(tex, outTexCoords);
}
'''

skybox_fragment_shader = '''
#version 450 core

uniform samplerCube skybox;

in vec3 texCoords;

out vec4 fragColor;

void main()
{
    fragColor = texture(skybox, texCoords);
}

'''

# Nuevos Shaders

animated_vertex_shader = '''
#version 450 core

layout (location = 0) in vec3 position;
layout (location = 1) in vec2 texCoords;
layout (location = 2) in vec3 normals;

out vec2 outTexCoords;
out vec3 outNormals;
out vec3 FragPos;  // Pasamos la posición del fragmento en espacio mundo

uniform float time;
uniform mat4 modelMatrix;
uniform mat4 viewMatrix;
uniform mat4 projectionMatrix;

void main()
{
    // Animación del vértice
    vec3 animatedPosition = position;
    animatedPosition.y += sin(position.x * 5.0 + time) * 0.1;
    
    // Calcular FragPos en espacio mundo (solo con modelMatrix)
    FragPos = vec3(modelMatrix * vec4(animatedPosition, 1.0)); 

    // Pasar normales al espacio mundo
    outNormals = mat3(transpose(inverse(modelMatrix))) * normals;
    
    // Pasar coordenadas de textura
    outTexCoords = texCoords;
    
    // Calcular la posición final del vértice
    gl_Position = projectionMatrix * viewMatrix * vec4(FragPos, 1.0);
}
'''

gradient_fragment_shader = '''
#version 450 core

in vec2 outTexCoords;
in vec3 outNormals;
in vec3 FragPos;

out vec4 fragColor;

uniform sampler2D tex;

void main()
{
    // Usamos la coordenada Y de FragPos (en espacio mundo) para determinar el color
    float height = FragPos.y;
    vec3 color = mix(vec3(0.0, 0.0, 1.0), vec3(1.0, 0.0, 0.0), height);
    
    // Combinar el color del degradado con la textura
    fragColor = vec4(color, 1.0) * texture(tex, outTexCoords);
}
'''

pulsating_vertex_shader = '''
#version 450 core

layout (location = 0) in vec3 position;
layout (location = 1) in vec2 texCoords;
layout (location = 2) in vec3 normals;

out vec2 outTexCoords;
out vec3 outNormals;
out vec3 FragPos;

uniform float time;
uniform mat4 modelMatrix;
uniform mat4 viewMatrix;
uniform mat4 projectionMatrix;

void main()
{
    // Efecto de pulsación usando seno del tiempo
    float scale = 1.0 + 0.1 * sin(time * 2.0);
    vec3 pulsatingPosition = position * scale;

    // Calcular FragPos en espacio mundo
    FragPos = vec3(modelMatrix * vec4(pulsatingPosition, 1.0));

    // Pasar normales al espacio mundo
    outNormals = mat3(transpose(inverse(modelMatrix))) * normals;

    // Pasar coordenadas de textura
    outTexCoords = texCoords;

    // Calcular la posición final del vértice
    gl_Position = projectionMatrix * viewMatrix * vec4(FragPos, 1.0);
}
'''

pulsating_fragment_shader = '''
#version 450 core

in vec2 outTexCoords;
in vec3 outNormals;
in vec3 FragPos;

out vec4 fragColor;

uniform sampler2D tex;
uniform float time;

void main()
{
    // Cambiar el color entre azul y amarillo usando el tiempo
    vec3 color = mix(vec3(0.0, 0.0, 1.0), vec3(1.0, 1.0, 0.0), (sin(time * 2.0) + 1.0) / 2.0);
    
    // Combinar el color del pulsado con la textura
    fragColor = vec4(color, 1.0) * texture(tex, outTexCoords);
}
'''

scan_vertex_shader = '''
#version 450 core

layout (location = 0) in vec3 position;
layout (location = 1) in vec2 texCoords;
layout (location = 2) in vec3 normals;

out vec2 outTexCoords;
out vec3 FragPos;

uniform mat4 modelMatrix;
uniform mat4 viewMatrix;
uniform mat4 projectionMatrix;

void main()
{
    FragPos = vec3(modelMatrix * vec4(position, 1.0));
    outTexCoords = texCoords;

    // Transformación final de la posición del vértice
    gl_Position = projectionMatrix * viewMatrix * modelMatrix * vec4(position, 1.0);
}
'''

scan_fragment_shader = '''
#version 450 core

in vec2 outTexCoords;
in vec3 FragPos;

out vec4 fragColor;

uniform sampler2D tex;
uniform float time;

void main()
{
    // Efecto de escaneo basado en la coordenada Y y el tiempo
    float frequency = 5.0; // Ajusta la frecuencia de la franja de escaneo
    float scanLine = sin(time + FragPos.y * frequency) * 0.5 + 0.5;

    // Color de escaneo (blanco brillante) y mezcla con el color de la textura
    vec3 scanColor = mix(texture(tex, outTexCoords).rgb, vec3(1.0, 1.0, 1.0), scanLine);

    // Color final del fragmento
    fragColor = vec4(scanColor, 1.0);
}
'''
