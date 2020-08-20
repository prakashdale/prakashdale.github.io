---
layout: post
title:  Enhancing RASA NLU model with custom components
comments: true
categories: [Rasa]
excerpt: Enhance existing NLU model with your own custom components to take your AI assistants to whole new level!
---

Enhance existing NLU model with your own custom components to take your AI assistants to whole new level!

A processing pipeline is the main building block of the RASA NLU model. It defines what processing stages the incoming user messages will have to go through until the model output is produced. Those stages can be tokenization, featurization, intent classification, entity extraction, pattern matching, etc. By default, RASA NLU comes with a bunch of pre-built components for you to use. Below is an example of a possible RASA NLU pipline configuration:

```
pipeline:
- name: "SpacyNLP"
- name: "SpacyTokenizer"
- name: "SpacyFeaturizer"
- name: "RegexFeaturizer"
- name: "CRFEntityExtractor"
- name: "EntitySynonymMapper"
- name: "SklearnIntentClassifier" 
```

Once pipeline is defined, each component is called one after the other and produces the output which is either directly added to the RASA NLU model output, or used as an input for other components. 

![Component life cycle train](/assets/misc/Rasa-Component-Lifecycle-Train.png "Component Life Cycle")

Components go through three main stages:

- create: initialization of the component before training.
- train: the component trains itself using the context and potentially the output of the previous components.
- persist: saving the trained component on disk for the future use.

Before the first component is initialized, a so-called *context* is created which is used to pass the information between the components. For example, one component can calculate feature vectors for the training data, store that within the context and another component can retrieve these feature vectors from the context and do intent classification. Once all components are created, trained and persisted, the model metadata is created which describes the overall NLU model.

## Custom Components

Adding custom components to the NLU pipeline is process of implementing the custom component class with the necessary methods and referencing it inside the RASA NLU pipeline configuration file. In general, there are two types of components you might want to use:

- Components which come as already pre-trained models (for example, trained on different datasets and packaged as python libraries, .pkl files, etc.)
- Components which train on your RASA NLU training data and improve as you make changes to the training examples or add more to them.

## Follow below steps to create custom component

- Create new RASA project with `rasa init`
- Add a new component file in the folder. You may use below template
  <script src="https://gist-it.appspot.com/https://github.com/prakashdale/prakashdale.github.io/raw/master/src/rasa/custom_component/ducklingplus.py?footer=0"></script>
- Update *config.yml*, add compoent name in the component pipeline. e.g. `- name: "ducklingplus.DucklingPlus"` as shown below.
  <script src="https://gist-it.appspot.com/https://github.com/prakashdale/prakashdale.github.io/raw/master/src/rasa/custom_component/config.yml?footer=0"></script>
- Add your code to *process* method to enhance your component further.

