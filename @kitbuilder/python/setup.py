from distutils.core import setup
setup(
  name = 'kitbuilder',         # How you named your package folder (MyLib)
  packages = [
    'kitbuilder',
    'kitbuilder/parser',
    'kitbuilder/bases',
    'kitbuilder/constants',
    'kitbuilder/environment',
    'kitbuilder/errors',
    'kitbuilder/factory',
    'kitbuilder/function',
    'kitbuilder/meta',
    'kitbuilder/reader',
    'kitbuilder/utils'
  ],   # Chose the same as "name"
  version = 'v0.0.1',      # Start with a small number and increase it with every change you make
  license='MIT',        # Chose a license from here: https://help.github.com/articles/licensing-a-repository
  description = ' KitBuilder is a library used for generating API-based and CLI-based SDK using only one file! ',   # Give a short description about your library
  author = 'Sergej Zivkovic',                   # Type in your name
  author_email = 'zivkovicsergej501@gmail.com',      # Type in your E-Mail
  url = 'https://github.com/szivkovicx/kitbuilder',   # Provide either the link to your github or to your website
  keywords = ['sdk', 'api', 'cli', 'requests', 'rest-api', 'configuration'],   # Keywords that define your package best
  include_package_data=True
)