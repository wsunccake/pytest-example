from pybuilder.core import use_plugin, init

use_plugin("python.core")
#use_plugin("python.unittest")
use_plugin("python.install_dependencies")
use_plugin("python.flake8")
#use_plugin("python.coverage")
use_plugin("python.distutils")

# pycharm plugin
use_plugin('python.pycharm')

use_plugin('pypi:pybuilder_pytest')
use_plugin('pypi:pybuilder_pytest_coverage')

name = "pytest-example"
default_task = "publish"


@init
def set_properties(project):
    project.build_depends_on('pymongo')
    project.build_depends_on('tinydb')

    # project.get_property("pytest_extra_args").append("-q")
    # project.get_property("pytest_extra_args").append("-x")
    # project.get_property("pytest_extra_args").append("-k asdict")
    # project.get_property("pytest_extra_args").append("-k asdict or default")
    # project.get_property("pytest_extra_args").append("-m run_replace")
    # project.get_property("pytest_extra_args").append("--setup-show")
    # project.get_property("pytest_extra_args").append("--fixtures")

    project.get_property("pytest_extra_args").append("-v")
    # project.get_property("pytest_extra_args").append("--tb=no")

    project.get_property("pytest_extra_args").append("-k add_5")

    # pytest-html plugin
    project.get_property("pytest_extra_args").append("--html=report.html")

    project.set_property('coverage_threshold_warn', 70)
    project.set_property('coverage_break_build', False)
    project.set_property('pytest_coverage_html', True)

