import basilisk as bsk

engine = bsk.Engine()
scene = bsk.Scene(engine)

# Load meshes
sphere_mesh = bsk.Mesh('models/sphere.obj')
monkey_mesh = bsk.Mesh('models/monkey.obj')

# Add nodes to the scene
node = bsk.Node(mesh=sphere_mesh)
scene.add(node)

# Set the shader to one with a more agressive gradient
blinnPhongShader = bsk.Shader(engine, frag='shader/blinnPhong.frag')
scene.shader = blinnPhongShader

# Set the lights (just looks better with this shader)
quantization_shader = bsk.Shader(engine, 'shader/frame.vert', 'shader/quantization.frag')
scene.light_handler.directional_lights = scene.light_handler.directional_lights[:-1]
scene.light_handler.write(scene.shader)

# Color Quantization tools
quantization_renderer = bsk.Framebuffer(engine, quantization_shader)
quantization_fbo = bsk.Framebuffer(engine)


while engine.running:
    scene.update()

    quantization_renderer.bind(scene.frame.output_buffer.texture, 'screenTexture', 0)
    quantization_renderer.render(quantization_fbo, auto_bind=False)
    quantization_fbo.render()

    engine.update()