from setuptools import setup

setup(
    name='EYES',
    options={
        'build_apps': {
            # Build asteroids.exe as a GUI application
            'console_apps': {
                'EYES': 'run.py',
            },

            # Set up output logging, important for GUI apps!
            'log_filename': 'output.log',
            'log_append': False,

            # Specify which files are included with the distribution
            'include_patterns': [
                'img.mf',
                'config/Config.prc'
            ],

            'use_optimized_wheels': False,

            # Include the OpenGL renderer and OpenAL audio plug-in
            'plugins': [
                'pandagl',
                'p3openal_audio',
            ],

            'platforms': ['win_amd64']
        }
    }
)