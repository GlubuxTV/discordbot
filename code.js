const Discord = require('discord.js');
const client = new Discord.Client();
const token = 'YOUR_BOT_TOKEN';

client.on('ready', () => {
  console.log('Bot is online!');
});

client.on('message', message => {
  if (message.content === 'ping') {
    message.reply('pong');
  }
});

client.login(token);
