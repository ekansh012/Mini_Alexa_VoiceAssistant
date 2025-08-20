# 🎙️ Mini Alexa Voice Assistant

A Python-based **mini voice assistant** that listens to your voice commands, responds with speech, and performs tasks like:

* 🎵 Playing songs on YouTube
* ⏰ Telling the current time
* 📚 Fetching quick Wikipedia summaries
* 😂 Cracking jokes

---

## 🚀 Features

* Voice activation using the keyword **“Alexa”**
* Natural voice responses with `pyttsx3`
* Handles multiple commands like **play, time, who is, joke**
* Lightweight and easy to run locally

---

## 🛠️ Installation

1. Clone the repository:
   <pre class="overflow-visible!" data-start="713" data-end="835"><div class="contain-inline-size rounded-2xl relative bg-token-sidebar-surface-primary"><div class="sticky top-9"><div class="absolute end-0 bottom-0 flex h-9 items-center pe-2"><div class="bg-token-bg-elevated-secondary text-token-text-secondary flex items-center gap-4 rounded-sm px-2 font-sans text-xs"><span class="" data-state="closed"></span></div></div></div><div class="overflow-y-auto p-4" dir="ltr"><code class="whitespace-pre! language-bash"><span><span>git </span><span>clone</span><span> https://github.com/YOUR-USERNAME/Mini_Alexa_VoiceAssistant.git
   </span><span>cd</span><span> Mini_Alexa_VoiceAssistant
   </span></span></code></div></div></pre>
2. Install dependencies:
   <pre class="overflow-visible!" data-start="865" data-end="948"><div class="contain-inline-size rounded-2xl relative bg-token-sidebar-surface-primary"><div class="sticky top-9"><div class="absolute end-0 bottom-0 flex h-9 items-center pe-2"><div class="bg-token-bg-elevated-secondary text-token-text-secondary flex items-center gap-4 rounded-sm px-2 font-sans text-xs"><span class="" data-state="closed"></span></div></div></div><div class="overflow-y-auto p-4" dir="ltr"><code class="whitespace-pre! language-bash"><span><span>pip install speechrecognition pyttsx3 pywhatkit wikipedia pyjokes
   </span></span></code></div></div></pre>

---

## ▶️ Usage

Run the assistant:

<pre class="overflow-visible!" data-start="986" data-end="1013"><div class="contain-inline-size rounded-2xl relative bg-token-sidebar-surface-primary"><div class="sticky top-9"><div class="absolute end-0 bottom-0 flex h-9 items-center pe-2"><div class="bg-token-bg-elevated-secondary text-token-text-secondary flex items-center gap-4 rounded-sm px-2 font-sans text-xs"><span class="" data-state="closed"></span></div></div></div><div class="overflow-y-auto p-4" dir="ltr"><code class="whitespace-pre! language-bash"><span><span>python alexa.py
</span></span></code></div></div></pre>

Say **“Alexa”** followed by your command, e.g.:

* `Alexa play Believer`
* `Alexa what time is it`
* `Alexa who is Elon Musk`
* `Alexa tell me a joke`

---

## 📄 License

This project is licensed under the MIT License.
