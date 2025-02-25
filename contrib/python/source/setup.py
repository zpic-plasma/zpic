from setuptools import setup, Extension
from Cython.Build import cythonize

# Removes the debug options and replaces the optimization flag
import sysconfig
from setuptools.command.build_ext import build_ext

cflags = sysconfig.get_config_var('CFLAGS')
cflags = cflags.replace(' -g', '')
cflags = cflags.replace('-O3', '-Ofast')
cflags += ' -std=c99 -fPIC'

# Removes unrecognized gcc option if present
cflags = cflags.replace(' -fexceptionsrecord-gcc-switches', '')

cc = sysconfig.get_config_var('CC')

class custom_build_ext(build_ext):
	def build_extensions(self):
		self.compiler.set_executable("compiler_so", cc + " " + cflags)
		build_ext.build_extensions(self)

# Get the path to the C source file root
import pathlib
csource = str(pathlib.Path("../../").resolve()) + "/"

em2d_rr = Extension("em2d_rr",
                sources=["em2d_rr.pyx",
                csource + "em2d_rr/current.c",
				csource + "em2d_rr/emf.c",
				csource + "em2d_rr/particles.c",
				csource + "em2d_rr/random.c",
				csource + "em2d_rr/simulation.c",
				csource + "em2d_rr/timer.c",
				csource + "em2d_rr/zdf.c"]
)

# Compile extensions
setup(name="zpic,
    ext_modules = cythonize([em2d_rr]), 
	zip_safe=False,
    cmdclass={"build_ext": custom_build_ext}
)
