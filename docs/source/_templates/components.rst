{% if current_project != 'the labscript suite' %}
.. toctree::
    :maxdepth: 2
    :hidden:

    the labscript suite <{{intersphinx_mapping['labscript-suite'][0]}}>

{% endif %}
*labscript suite* components
============================

The *labscript suite* is modular by design, and is comprised of:

.. list-table:: Python libraries
    :widths: 10 90
    :header-rows: 0

    {% for prog, item in programs.items() if item.type == 'lib' %}
    * - .. image:: {{img_path}}/{{item.icon}}
             :target: {{intersphinx_mapping['%s' | format(prog)][0]}}
             :class: labscript-suite-icon
      - |{{prog}}|_ --- {{item.desc}}
    {% endfor %}

.. list-table:: Graphical applications
    :widths: 10 90
    :header-rows: 0

    {% for prog, item in programs.items() if item.type == 'gui' %}
    * - .. image:: {{img_path}}/{{item.icon}}
             :target: {{intersphinx_mapping['%s' | format(prog)][0]}}
             :class: labscript-suite-icon
      - |{{prog}}|_ --- {{item.desc}}
    {% endfor %}

.. toctree::
    :maxdepth: 2
    :hidden:

    {% for prog in programs|sort if prog != current_project %}
    {{prog}} <{{intersphinx_mapping['%s' | format(prog)][0]}}>
    {% endfor %}

{% for prog in programs %}
.. |{{prog}}| replace:: **{{prog}}**
.. _{{prog}}: {{intersphinx_mapping['%s' | format(prog)][0]}}
{% endfor %}