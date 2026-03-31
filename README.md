# RPCVR Rich Presence VR

![VR Image](https://media.discordapp.net/attachments/1481811360626114623/1488360199801540740/Screenshot_From_2026-03-08_20-50-17.png?ex=69cc7ef4&is=69cb2d74&hm=8372128413f6d7e2dbdafc7b513d73ddf655d540de45473e44e94d01737d799d&=&format=webp&quality=lossless)

This is a simple Discord Meta Quest Rich Presence `discord.py-self`

> [!WARNING]
> Your account could be suspended or banned if detected

## Features
- Shows Meta Quest Rich Presence 
- Displays details state and large image

- ![VR Image](https://media.discordapp.net/attachments/1481811360626114623/1488360199180779550/Screenshot_From_2026-03-08_05-49-14.png?ex=69cc7ef3&is=69cb2d73&hm=2c03974cbc8d7394b07ce13d2cb82d7f840b31df34c3c9b6f50f64f845e39ee2&=&format=webp&quality=lossless)

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
