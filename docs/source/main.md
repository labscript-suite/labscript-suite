# the _labscript suite_

### Experiment control and automation system

___

The _labscript suite_ is a powerful and extensible framework for experiment [composition](https://github.com/labscript-suite/labscript), [control](https://github.com/labscript-suite/runmanager), [execution](https://github.com/labscript-suite/blacs), and [analysis](https://github.com/labscript-suite/labscript). Developed for quantum science and quantum engineering, from laboratory to in-field devices. Applicable to optics, microscopy, materials engineering, biophysics, and any application predicated on the repetition of parameterised, hardware-timed experiments.


## Features

* Flexible and automated oversight of heterogeneous hardware.
* The most mature and widely used open-source control system in quantum science.
* Multiple analysis-based feedback modes.
* Extensible plugin architecture (e.g. machine learning online optimisation).
* Readily integrates with other software, including image acquisition, analysis, and even other control systems.
* Compose experiments as human-readable Python code, leveraging modularity, revision control and re-use.
* Dynamic visualisation of experiment composition and results.
* Remote operation: different modules can run on physically separate hosts / single modules can be run on multiple hosts (including hardware supervisor, [blacs](https://github.com/labscript-suite/blacs)).
* Auto-generating user-interfaces.
* High-level scripting: all user-interface interaction can be programatically synthesised.


## Citing the _labscript suite_

If you use the _labscript suite_ to control your experiment or perform analysis, please cite one or more of the following publications:

<!-- 1. _A scripted control system for autonomous hardware-timed experiments,_ [Review of Scientific Instruments **84**, 085111 (2013)](https://doi.org/10.1063/1.4817213). arXiv: [1303.0080](http://arxiv.org/abs/1303.0080). -->

<details>
  <summary>P. T. Starkey, <em><a href="https://doi.org/10.26180/5d1db8ffe29ef">A software framework for control and automation of precisely timed experiments</a>.</em>  PhD thesis, Monash University (2019).</summary>

  ```bibtex
    @phdthesis{starkey_phd_2019, 
      title = {State-dependent forces in cold quantum gases}, 
      author = {Starkey, P. T.},
      year = {2019},
      url = {https://doi.org/10.26180/5d1db8ffe29ef}, 
      doi = {10.26180/5d1db8ffe29ef},
      school = {Monash University},
    }
  ```
</details>

<details>
  <summary>C. J. Billington, <em><a href="https://doi.org/10.26180/5bd68acaf0696">State-dependent forces in cold quantum gases</a>.</em>  PhD thesis, Monash University (2018).</summary>

  ```bibtex
    @phdthesis{billington_phd_2018, 
      title = {State-dependent forces in cold quantum gases}, 
      author = {Billington, C. J.},
      year = {2018},
      url = {https://doi.org/10.26180/5bd68acaf0696}, 
      doi = {10.26180/5bd68acaf0696},
      school = {Monash University},
    }
  ```
</details>

<details>
  <summary><em><a href="https://doi.org/10.1063/1.4817213">A scripted control system for autonomous hardware-timed experiments</a>,</em> Review of Scientific Instruments <b>84</b>, 085111 (2013). arXiv:<a href="http://arxiv.org/abs/1303.0080">1303.0080</a>.</summary>

  ```bibtex
    @article{labscript_2013,
      author = {Starkey, P. T. and Billington, C. J. and Johnstone, S. P. and
                Jasperse, M. and Helmerson, K. and Turner, L. D. and Anderson, R. P.},
      title = {A scripted control system for autonomous hardware-timed experiments},
      journal = {Review of Scientific Instruments},
      volume = {84},
      number = {8},
      pages = {085111},
      year = {2013},
      doi = {10.1063/1.4817213},
      url = {https://doi.org/10.1063/1.4817213},
      eprint = {https://doi.org/10.1063/1.4817213}
    }
  ```
</details>
