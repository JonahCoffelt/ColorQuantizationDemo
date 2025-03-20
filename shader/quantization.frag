#version 330 core

layout (location = 0) out vec4 fragColor;


in vec2 uv;

uniform sampler2D screenTexture;

const int n = 4;


float grayscale(vec3 color) {
    return dot(color.rgb, vec3(0.299, 0.587, 0.114));
}


void main()
{
    vec4 color = texture(screenTexture, uv);
    float value = grayscale(color.rgb);

    float quantized = floor((value) * n) / n;

    fragColor = vec4(vec3(quantized), 1.0);
}