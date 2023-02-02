---
# Feel free to add content and custom Front Matter to this file.
# To modify the layout, see https://jekyllrb.com/docs/themes/#overriding-theme-defaults

layout: default
permalink: /
---

<p style="font-size: x-large;">
    Benchmarking progress in Natural Language Processing applications to Moral Foundations Theory.
</p>
## About
[Moral Foundations Theory (MFT)](https://moralfoundations.org/) is a theory of moral psychology that proposes that
several univeral foundations underlie human morality. Since its inception, various methods have been proposed to
operationalize
MFT on natural language data, including dictionary-based approaches and deep neural networks.

Natural Language Processing (NLP) tasks benefit from standardized dataset, model, and performance
repositories. See [HuggingFace Dataset Hub](https://huggingface.co/docs/datasets/index), [ HuggingFace Model Hub ](https://huggingface.co/models), and [PaperswithCode](https://paperswithcode.com/).

NLP applications of MFT have some commonalities with mainstream NLP tasks, but also have some differences. 
This site aims to cater to the unique needs of MFT NLP approaches, and synchronize with standard ecosystem tools wherever possible.

This site aims to provide an inventory of **tasks**, **datasets**, NLP **methods** for MFT and their performance
results, to facilitate the development of improved methods. It is mainly intended as a resource for researchers in NLP, MFT, and related fields.

<div style="display: flex; flex-direction: row; flex-wrap: wrap; column-gap: 4em; row-gap: 1em">
    {% for collection in site.collections %}
        {% if collection.label != "posts" %}

        <div class="collection-list">
        <div class="collection-list-title">
        <a href="{{site.url}}/{{collection.label}}">
            <h2>{{collection.name}}</h2>
        </a>
        </div>
        <div class="collection-list-inner">
            {% for item in site[collection.label] %}
            <div class="card">
                <a href="{{site.url}}/{{collection.label}}/{{ item.name }}">
                    <h3> {{ item.title }} </h3>
                </a>
                <p>{{item.description}} </p>
            </div>
            {% endfor %}
        </div>
        </div>
        {% endif %}
    {% endfor %}
</div>