import glm

from OpenGL.GL import *
from OpenGL.GL.shaders import compileProgram, compileShader
from numpy import array, float32


class Buffer(object):
    def __init__(self, data):
        self.vertBuffer = array(data, float32)

        # vertex Buffer Obeject
        self.VBO = glGenBuffers(1)

        # Vertex Array Object
        self.VAO = glGenVertexArrays(1)

    def Render(self):
        glBindBuffer(GL_ARRAY_BUFFER, self.VBO)
        glBindVertexArray(self.VAO)

        # send vertex information
        glBufferData(GL_ARRAY_BUFFER,  # Buffer ID
                     self.vertBuffer.nbytes,  # Buffer size in bytes
                     self.vertBuffer,  # Buffer data
                     GL_STATIC_DRAW,  # Usage
                     )

        # Attributes
        glVertexAttribPointer(0,  # Attribute number (let on 0)
                              3,  # Size (data size)
                              GL_FLOAT,  # Type
                              GL_FALSE,  # Is it normalized?
                              4 * 8,  # Stride in bytes
                              ctypes.c_void_p(0),  # Offset
                              )

        glEnableVertexAttribArray(0)

        # textures attirbutes
        glVertexAttribPointer(1,  # Attribute number (let on 0)
                              2,  # Size (data size)
                              GL_FLOAT,  # Type
                              GL_FALSE,  # Is it normalized?
                              4 * 8,  # Stride in bytes
                              ctypes.c_void_p(4 * 3),  # Offset
                              )

        glEnableVertexAttribArray(1)

        # normals attirbutes
        glVertexAttribPointer(2,  # Attribute number (let on 0)
                              3,  # Size (data size)
                              GL_FLOAT,  # Type
                              GL_FALSE,  # Is it normalized?
                              4 * 8,  # Stride in bytes
                              ctypes.c_void_p(4 * 5),  # Offset
                              )

        glEnableVertexAttribArray(2)

        glDrawArrays(GL_TRIANGLES, 0, int(len(self.vertBuffer) / 8))