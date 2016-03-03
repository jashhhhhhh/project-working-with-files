#please do not edit this file, it is used for automated testing

import shutil
shutil.rmtree('answers')
shutil.rmtree('quizzes')
import randomQuizGenerator, os

def testDirectories():
    initialDirectory = os.getcwd()
    os.chdir('answers')
    assert (os.getcwd() == os.path.join(initialDirectory,'answers'))
    
    os.chdir('../quizzes')
    assert (os.getcwd() == os.path.join(initialDirectory,'quizzes'))
    
    os.chdir('../')

def testFiles():
    answers=0
    quizzes=0
    
    for filenames in os.listdir('quizzes'):
        quizzes += 1
    
    assert quizzes == 5

    for filenames in os.listdir('answers'):
        answers += 1
    
    assert answers == 5