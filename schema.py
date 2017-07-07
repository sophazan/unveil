import random
user = []
game = []
user_game = []
game_question = []
game_user_question_answer_guess_guessdiff = []
question = [{'id': 1, 'question': 'Been arrested?'}, {'id': 2, 'question':'Laughed until something you were drinking came out your nose?'}, {'id': 3, 'question':'Still love someone you shouldn\'t?'}]


RAND_NUMBER = random.randint(0, 10000)

def start_game(user_name):

    user.append({'id': 1000, 'name': user_name})
    game.append({'id': 10, 'rand_num':RAND_NUMBER})
    user_game.append({'game_id':10, 'user_id':1000})
    return RAND_NUMBER



def user_join(user_name, RAND_NUMBER):

    user.append({'id': 1001, 'name': user_name})
    for d in game:
        if d['rand_num'] == RAND_NUMBER:
            user_game.append({'game_id': d['id'], 'user_id': 1001})



def show_joined_users(game_id):

    for d in user_game:
        if d['game_id'] == 10:
            yield d['user_id']



def next_question(game_id):

    rand_question = random.choice(question)
    game_question.append({'game_id': game_id, 'question_id': rand_question['id']})
    return rand_question



def answer(game_id, question_id, user_id, answer, guess):
    game_user_question_answer_guess_guessdiff.append({'game_id': game_id, 'question_id': question_id, 'user_id': user_id, 'answer': answer, 'guess_yes': guess})



def everyone_answered(game_id, question_id):

    count_user = 0
    count_answers = 0

    for user in user_game:
        if user['game_id'] == game_id:
            count_user += 1
    for answer in game_user_question_answer_guess_guessdiff:
        if answer['game_id'] == game_id and answer['question_id'] == question_id:
            count_answers += 1

    if count_user == count_answers:
        return True
    else:
        return False


def show_result(game_id, question_id):

    results = []
    for result in game_user_question_answer_guess_guessdiff:
        if result['game_id'] == game_id and result['question_id'] == question_id:
            results.append(result['answer'])

    total_yes = results.count('yes')

    for user in game_user_question_answer_guess_guessdiff:
        score = abs(total_yes - user['guess_yes'] )
        for gu in game_user_question_answer_guess_guessdiff:
            if gu['user_id'] == user['user_id']:
                gu['score'] = score
            return gu['score']
        # Get Username


def evaluate_loser(game_id, question_id):

    max_user = None
    max_score = 0
    for score in game_user_question_answer_guess_guessdiff:
        if score['game_id'] == game_id and score['question_id'] == question_id:
            if score['score'] > max_score:
                max_user = score['user_id']

    return max_user

def end(game_id):
    loser = None
    max_score = 0
    for loser in game_user_question_answer_guess_guessdiff:
        if loser['game_id'] == game_id:
            if loser['score'] > max_score:
                max_score = loser['score']
                loser = loser['user_id']
            return loser

print('RAND_NUMBER: ' + str(start_game('abc')))
print("USER JOIN: " + str(user_join('nono', RAND_NUMBER)))
print("USER JOIN: " + str(user_join('dd', RAND_NUMBER)))
print('JOINED USERS: ' + str(list(show_joined_users(10))))
print('NEXT QUESTION: ' + str(next_question(10)))
print('EVERYONE ANSWERED: ' + str(everyone_answered(10, 2)))
print('' + str(answer(10, 2, 1001, "no", 2)))
print('SHOW RESULT: ' + str(show_result(10, 2)))
print("QUESTION LOSER: " + str(evaluate_loser(10,2)))
print("GAME LOSER: " + str(end(10)))

print('users: '+str(user))
print('game: ' +str(game))
print('user_game: '+str(user_game))
print('game_question: '+str(game_question))
print('game_user_question_answer_guess_guessdiff: '+str(game_user_question_answer_guess_guessdiff))