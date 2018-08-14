# Copyright 2018 Sabino Miranda Jimenez

# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at

#     http://www.apache.org/licenses/LICENSE-2.0

# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
from setuptools import setup
import ConceptModelling
version = ConceptModelling.__version__

setup(
    name="ConceptModelling",
    description="""ConceptModelling""",
    version=version,
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Environment :: Console",
        "Intended Audience :: Science/Research",
        "License :: OSI Approved :: Apache Software License",
        "Natural Language :: English",
        "Operating System :: MacOS :: MacOS X",
        "Operating System :: POSIX :: Linux",
        'Programming Language :: Python :: 3',
        "Topic :: Scientific/Engineering :: Artificial Intelligence"],
    url='https://github.com/ingeotec/ConceptModelling',
    author="Sabino Miranda Jimenez",
    author_email="mgraffg@ieee.org",
    packages=['ConceptModelling', 'ConceptModelling/tests'],
    include_package_data=True,
    zip_safe=False,
    # package_data={'ConceptModelling/conf': ['default_parameters.json'],
    #               'ConceptModelling/tests': ['tweets.json']},
    # install_requires=['B4MSA', 'EvoDAG'],
    # entry_points={
    #     'console_scripts': ['ConceptModelling-train=ConceptModelling.command_line:train',
    #                         'ConceptModelling-predict=ConceptModelling.command_line:predict',
    #                         'ConceptModelling-utils=ConceptModelling.command_line:utils',
    #                         'ConceptModelling-performance=ConceptModelling.command_line:performance']
    # }
)
