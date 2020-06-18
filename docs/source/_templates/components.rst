{% if metapackage_toctree %}
.. toctree::
    :maxdepth: 2
    :hidden:

    Metapackage documentation <{{intersphinx_mapping['labscript-suite'][0]}}>

{% endif %}
*labscript suite* components
============================

The *labscript suite* is modular by design, and is comprised of:

.. list-table:: Python libraries
    :widths: 10 90
    :header-rows: 0

    {% for prog, item in libs.items() %}
    * - .. image:: {{item.img}}
             :target: {{intersphinx_mapping['%s' | format(prog)][0]}}
             :class: labscript-suite-icon
      - |{{prog}}|_ --- {{item.desc}}
    {% endfor %}

.. list-table:: Graphical applications
    :widths: 10 90
    :header-rows: 0

    {% for prog, item in guis.items() %}
    * - .. image:: {{item.img}}
             :target: {{intersphinx_mapping['%s' | format(prog)][0]}}
             :class: labscript-suite-icon
      - |{{prog}}|_ --- {{item.desc}}
    {% endfor %}

.. toctree::
    :maxdepth: 2
    :hidden:

    {% for prog in toctree_entries %}
    {{prog}} <{{intersphinx_mapping['%s' | format(prog)][0]}}>
    {% endfor %}

{% for prog in rst_defs %}
.. |{{prog}}| replace:: **{{prog}}**
.. _{{prog}}: {{intersphinx_mapping['%s' | format(prog)][0]}}
{% endfor %}