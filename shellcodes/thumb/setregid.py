
def generate(gid=0):
    """setregid(gid, gid) to get egid's privilige
        
        argument:
            gid (int/str/reg) - effective gid number
    """
    try:
        xgid = '#%s' % int(gid)
    except:
        xgid = '%s' % gid

    sc = """
    mov r0, %s
    mov r1, %s
    mov r7, #71
    svc 1
    """ % (xgid, xgid)
    return sc
