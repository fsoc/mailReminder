import configparser, os, subprocess, random

def getMsg():
    data = configparser.ConfigParser(allow_no_value=True)
    data.read('msg.ini')

    s = random.choice(list(data['suffix'].keys()))
    p = random.choice(list(data['prefix'].keys()))
    return [p,s]


def runData():
    data = configparser.ConfigParser()
    data.read('data.ini')
    getMsg()
    
    for section in data.sections():
        s = data[section]
        mail(s['from'], s['to'], s['sub'], section)


def mail(fr, to, sub, extraMsg):
    final_message = '%s %s. %s' % (getMsg()[0], extraMsg, getMsg()[1])
    command_line = 'echo "%s"|mail -s "%s" -r %s %s' % (final_message, sub, fr, to)
    data = subprocess.check_output(command_line, shell=True)
    print('output of mail cmd: %s', data)
    print('mail sent to %s m:%s s:%s' % (to ,final_message, sub))

runData()
