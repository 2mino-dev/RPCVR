# RPCVR Rich Presence VR

![VR Image](https://cdn.discordapp.com/attachments/1478916905430421627/1480034664256372878/image.png?ex=69ae3531&is=69ace3b1&hm=9a7a747b291dae08656c0140f0c9a7fe033c4222070ae3a523c39309b823cc64&animated=true)

This is a simple Discord Meta Quest Rich Presence `discord.py-self`

> [!WARNING]
> Your account could be suspended or banned if detected

## Features
- Shows Meta Quest Rich Presence 
- Displays details state and large image

## Requirements
- Python 3.10+
- `discord.py-self`
- `rich`

## How to Use
1. Open the `config.json` file in the project folder

2. Edit the following fields with your information
   - `"token"` → Replace with your Discord token
   - `"application_id"` → Replace with your Discord application ID
   - `"name"` → Set the name you want to display in Rich Presence
   - `"details"` → Optional set details about your activity
   - `"state"` → Optional set a custom state
   - `"large_image"` → Replace with the image url

## Note 
   - party.enable → show/hide party

   - loop → enable/disable activity loop

   - loop1 / loop2 → alternative activities for loop

You can install dependencies with

```bash
pip install -r requirements.txt
```
## Run

```bash
python main.py
```
