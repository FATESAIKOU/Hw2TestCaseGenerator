from pprint import pprint

def makeTestCases(q_fac, cfg):
    inputs = []
    outputs = []
    
    q_gen = q_fac.createGenerator(cfg)

    while True:
        ip, op = q_gen.next()

        if ip == None and op == None:
            break

        inputs.append(ip)
        outputs.append(op)

    return inputs, outputs
