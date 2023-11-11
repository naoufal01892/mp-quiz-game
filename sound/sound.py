import os
import pygame

class SoundPlayer:
    def __init__(self, sound_file='./sound/.mp3'):
        pygame.mixer.init()
        
        # Get the absolute path to the sound file
        sound_file_path = os.path.abspath(sound_file)
        
        if not os.path.exists(sound_file_path):
            raise FileNotFoundError(f"File not found: {sound_file_path}")
        
        pygame.mixer.music.load(sound_file_path)

    def play(self):
        pygame.mixer.music.play()

class ValidationPlayer(SoundPlayer):
    def __init__(self):
        super().__init__('./sound/v.mp3')

class ErrorPlayer(SoundPlayer):
    def __init__(self):
        super().__init__('./sound/e.mp3')

def main():
    

    validation_player = ValidationPlayer()
    validation_player.play()

    error_player = ErrorPlayer()
    error_player.play()

    input("Press Enter to exit...")

if __name__ == "__main__":
    main()
