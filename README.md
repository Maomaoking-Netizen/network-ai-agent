# network-ai-agent
An AI-based Network Operation and Maintenance Assistant powered by Large Language Models (LLMs). It supports network troubleshooting, protocol Q&amp;A, configuration generation, and configuration analysis for OSPF, VLAN, RIP, and DHCP using Python, Flask, and OpenAI API.
# Intelligent Network Operation and Maintenance Assistant

基于大语言模型（LLM）的智能网络运维助手。

## 项目简介

本项目是一个基于 OpenAI 大语言模型构建的智能网络运维助手，能够通过自然语言完成网络故障分析、协议问答、配置生成以及网络配置检查等功能。

系统结合 Flask Web 框架与 LLM 推理能力，实现智能化网络运维支持。

---

## 功能特性

- 网络故障诊断
- OSPF/RIP/VLAN/DHCP 问答
- Cisco/Huawei 配置生成
- 网络配置分析
- 自然语言交互
- AI 智能运维助手

---

## 技术栈

- Python
- Flask
- OpenAI API
- LangChain
- HTML/CSS

---

## 系统架构

User → Web Interface → Flask Server → LLM Agent → Network Tools

---

## 项目结构

```bash
network-ai-agent/
│
├── app.py
├── agent.py
├── requirements.txt
├── templates/
├── static/
└── tools/
