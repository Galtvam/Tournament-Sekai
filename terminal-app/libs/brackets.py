from colorama import init, Fore, Style

from .prompt import *

init()

class Bracket:
    BLOCK_WIDTH = 20
    BLOCK_HEIGHT = 3
    MAX_LENGTH = 16
    HORIZONTAL_SPACING = 3
    TEXT_MARGIN_X = 2
    VERTICAL_SPACING = 1

    def __init__(self, participant_one, participant_two, winner=None):
        self.participant_one = participant_one 
        self.participant_two = participant_two 
        self.winner = winner
        self.draw_position = None

    def draw(self, x, y):
        reference_position = x, y
        
        self.draw_position = self.get_participant_one_position(reference_position)
        self.draw_connection(self.draw_position)
        self.draw_participant_one(reference_position)
        self.draw_participant_two(reference_position)

        move_cursor(x, y + Bracket.BLOCK_HEIGHT * 2 + Bracket.VERTICAL_SPACING)
    
    def get_participant_one_text(self):
        text_participant_one = self.participant_one
        if isinstance(text_participant_one, Bracket):
            text_participant_one = self.participant_one.winner
        return text_participant_one or ''
    
    def get_participant_two_text(self):
        text_participant_two = self.participant_two
        if isinstance(text_participant_two, Bracket):
            text_participant_two = self.participant_two.winner
        return text_participant_two or ''

    def get_participant_one_position(self, reference_position):
        if isinstance(self.participant_one, Bracket):
            position_participant_one = self.participant_one.draw_position
            position_participant_two = self.participant_one.get_participant_two_position(position_participant_one)
            
            distance = position_participant_two[1] - position_participant_one[1]
            position_x = position_participant_one[0] + Bracket.BLOCK_WIDTH + Bracket.HORIZONTAL_SPACING
            position_y = position_participant_one[1] + distance - Bracket.BLOCK_HEIGHT - Bracket.VERTICAL_SPACING
            # FIXME: Gambiarra para fazer funcionar para a primeira fase
            if position_y == position_participant_one[1]:
                position_y += 2
            position = position_x, position_y
        else:
            position = reference_position
        return position

    def get_participant_two_position(self, reference_position):
        if isinstance(self.participant_two, Bracket):
            position_participant_one = self.participant_two.draw_position
            position_participant_two = self.participant_two.get_participant_two_position(position_participant_one)
            
            distance = position_participant_two[1] - position_participant_one[1]
            position_x = position_participant_one[0] + Bracket.BLOCK_WIDTH + Bracket.HORIZONTAL_SPACING
            position_y = position_participant_one[1] + distance - Bracket.BLOCK_HEIGHT - Bracket.VERTICAL_SPACING
            # FIXME: Gambiarra para fazer funcionar para a primeira fase
            if position_y == position_participant_one[1]:
                position_y += 2
            position = position_x, position_y
        else:
            position = reference_position[0], reference_position[1] + Bracket.BLOCK_HEIGHT + Bracket.VERTICAL_SPACING
        return position
    
    def draw_participant_one(self, reference_position):
        participant_one_position = self.get_participant_one_position(reference_position)
        
        text_participant_one = self.get_participant_one_text()
        if self.winner:
            if self.winner == text_participant_one: 
                Bracket.draw_block(participant_one_position, text_participant_one, green_text)
            else:
                Bracket.draw_block(participant_one_position, text_participant_one, red_text)
        else:
            Bracket.draw_block(participant_one_position, text_participant_one)
        

    def draw_participant_two(self, reference_position):
        participant_two_position = self.get_participant_two_position(reference_position)
        
        text_participant_two = self.get_participant_two_text()
        if self.winner:
            if self.winner == text_participant_two: 
                Bracket.draw_block(participant_two_position, text_participant_two, green_text)
            else:
                Bracket.draw_block(participant_two_position, text_participant_two, red_text)
        else:
            Bracket.draw_block(participant_two_position, text_participant_two)
        
    
    def draw_connection(self, reference_position):
        if isinstance(self.participant_one, Bracket):
            position_participant_one = self.participant_one.draw_position
            position_participant_two = self.participant_one.get_participant_two_position(position_participant_one)
            
            block_1 = self.draw_position
            Bracket.draw_block_connections(
                position_participant_one, position_participant_two, block_1
            )
        
        if isinstance(self.participant_two, Bracket):
            position_participant_one = self.participant_two.draw_position
            position_participant_two = self.participant_two.get_participant_two_position(position_participant_one)

            block_2 = self.get_participant_two_position(self.draw_position)
            Bracket.draw_block_connections(
                position_participant_one, position_participant_two, block_2
            )
            
    def is_bracket_depedent(self):
        return isinstance(self.participant_one, Bracket) or isinstance(self.participant_two, Bracket)

    def participants(self):
        return self.participant_one, self.participant_two
    
    @staticmethod
    def draw_block(position, text, filter_text=None):
        x, y = position
        move_cursor(x, y)
        print('┌' + '─' * (Bracket.MAX_LENGTH + 2) + '┐', end='')
        move_cursor(x, y + 1)
        print('│' + ' ' * (Bracket.MAX_LENGTH + 2) + '│', end='')
        move_cursor(x, y + 2)
        print('└' + '─' * (Bracket.MAX_LENGTH + 2) + '┘', end='')

        text_position = x + Bracket.TEXT_MARGIN_X, y + 1
        move_cursor(*text_position)
        center_text = text.center(Bracket.MAX_LENGTH)
        center_text = filter_text(center_text) if callable(filter_text) else center_text
        print(center_text, end='\n')
    
    @staticmethod
    def draw_final_block(final_bracket):
        participant_one_position = final_bracket.draw_position
        participant_two_position = final_bracket.get_participant_two_position(final_bracket.draw_position)

        distance = participant_two_position[1] - participant_one_position[1]
        position_y = participant_one_position[1] + (distance // 2)
        position_x = participant_one_position[0] + Bracket.BLOCK_WIDTH + Bracket.HORIZONTAL_SPACING
        position = position_x, position_y

        winner = final_bracket.winner or ''
        Bracket.draw_block(position, winner, green_text)
        Bracket.draw_block_connections(
            participant_one_position, participant_two_position, position
        )
    
    @staticmethod
    def draw_block_connections(block_one, block_two, block_tree):
        position_participant_one = block_one

        x, y = position_participant_one
        position_participant_one = x + Bracket.BLOCK_WIDTH, y + (Bracket.BLOCK_HEIGHT // 2) 
        move_cursor(*position_participant_one)
        print('┐', end='\n')
        
        position_participant_two = block_two
        x, y = position_participant_two
        position_participant_two = x + Bracket.BLOCK_WIDTH, y + (Bracket.BLOCK_HEIGHT // 2) 
        move_cursor(*position_participant_two)
        print('┘', end='\n')
        
        for y in range(position_participant_one[1] + 1, position_participant_two[1]):
            move_cursor(x + Bracket.BLOCK_WIDTH, y)
            print('│', end='\n')
            
        x, y = block_tree
        move_cursor(x - Bracket.HORIZONTAL_SPACING + 1, y + (Bracket.BLOCK_HEIGHT // 2))
        print('─' * (Bracket.HORIZONTAL_SPACING - 1), end='\n')

    @staticmethod
    def draw_tree(brackets, position):
        x, y = position
        left_brackets = set(brackets)        
        drawed_brackets = set()

        current_position = position
        tree_height = None
        while len(left_brackets) > 0:
            for bracket in brackets:
                if bracket not in drawed_brackets and (not bracket.is_bracket_depedent() 
                    or all(p in drawed_brackets for p in bracket.participants())):
                    bracket.draw(*current_position)
                    drawed_brackets.add(bracket)
                    left_brackets.remove(bracket)
                    next_y = current_position[1] + Bracket.BLOCK_HEIGHT * 2 + Bracket.VERTICAL_SPACING + 1
                    current_position = current_position[0], next_y
            if not tree_height:
                tree_height_y = current_position[1] - Bracket.BLOCK_HEIGHT * 2 - Bracket.VERTICAL_SPACING
                tree_height = current_position[0], tree_height_y
        
        Bracket.draw_final_block(bracket)
        move_cursor(*tree_height)

bracket_1 = Bracket('Igor', 'Sheldon', winner='Igor')
bracket_2 = Bracket('Marcos', 'Seninha', winner='Seninha')
bracket_3 = Bracket('Amigo 1', 'Amigo 2')
bracket_4 = Bracket('Amigo 3', 'Amigo 4', winner='Amigo 3')
bracket_5 = Bracket(bracket_1, bracket_2, winner='Igor')
bracket_6 = Bracket(bracket_3, bracket_4)

clear_screen()
Bracket.draw_tree([bracket_1, bracket_2, bracket_3, bracket_4, bracket_5, bracket_6], (1, 3))