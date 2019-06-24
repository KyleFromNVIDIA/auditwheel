from setuptools import setup, Extension
import subprocess

cmd = 'gcc -fPIC -shared -o b/libb.so b/b.c'
subprocess.check_call(cmd.split())
cmd = (
    'gcc -fPIC -shared -o a/liba.so '
    '-Wl,--disable-new-dtags -Wl,-rpath=$ORIGIN/../b '
    '-Ib -Lb -lb a/a.c'
)
subprocess.check_call(cmd.split())

setup(
    name='testrpath',
    version='0.0.1',
    packages=['testrpath'],
    package_dir={'': 'src'},
    ext_modules=[
        Extension(
            'testrpath/testrpath',
            sources=['src/testrpath/testrpath.c'],
            include_dirs=['a'],
            libraries=['a'],
            library_dirs=['a'],
        )
    ],
)
