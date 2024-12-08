# Auto Play Pong
An automated version of the classic Pong game where computer-controlled players compete against each other. This game uses threading to manage concurrent gameplay actions.

Features    

• Automated Players: Two computer-controlled players simulate a real-time Pong game.

• Threaded Gameplay: Utilizes threading for concurrent player and ball movements, ensuring responsive and fluid gameplay.

• Customizable Speed: Adjust player speeds and ball dynamics for varied difficulty levels.

• Real-time Collision Detection: Players and ball interact realistically within the game environment.

Requirements    

• Python 3.x

• turtle graphics module

• threading module

Usage    

1. Set Up the Game Environment:

• The game creates a main screen with specified dimensions and background color.

2. Initialize Players and Ball:

• Two players (right and left) are created with different speeds.

• The ball is initialized at a starting position.

3. Main Game Loop:

• The game loop runs continuously, updating the screen and managing ball and player actions.

• The ball and players' positions are tracked, and collision detection is implemented to determine hits.

• The game ends when the ball exits the defined play area.

4. Start the Game:

• Run the script to start the Auto Play Pong game.

• Observe the automated players compete against each other in a thrilling Pong match.
