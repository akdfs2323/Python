full_dot = '●'
empty_dot = '○'

def create_character (name,strength,intelligence,charisma):
    if not isinstance(name, str):
        return 'The character name should be a string'
    if name == "":
        return 'The character should have a name'
    if len(name) > 10 :
        return 'The character name is too long'
    if " " in name:
        return 'The character name should not contain spaces'
    
    stats = [strength,intelligence,charisma]
    if not all(isinstance(stat, int) for stat in stats):
        return 'All stats should be integers'
    if any(stat < 1 for stat in stats):
        return 'All stats should be no less than 1'
    if any(stat > 4 for stat in stats):
        return 'All stats should be no more than 4'
    if sum(stats) != 7:
        return 'The character should start with 7 points'
    
    str_line = 'STR ' + full_dot * strength + empty_dot * (10-strength)
    int_line = 'INT ' + full_dot * intelligence + empty_dot * (10-intelligence)
    char_line = 'CHA '+ full_dot * charisma + empty_dot * (10-charisma)
    return f'{name}\n{str_line}\n{int_line}\n{char_line}'

