def add_event(tick_nw_event, event_list, nw_event):
    while tick_nw_event in event_list:
        tick_nw_event += 1

    event_list[tick_nw_event] = nw_event
    return event_list


def simulate(nP, nA, tmax, E):
    # total_units = nP + nA
    # proposals = 1
    # proposers = [computer(number= i, is_proposer= True) for i in range(nP)]
    accepters = [computer(number=i, is_proposer=False) for i in range(nA)]
    event_list = {1: Event()}
    for tick in range(tmax):
        event = event_list[tick]

        if event.name == "Propose":
            event.src.pro_val = event.pro_number
            event.src.value = event.value

            for acc in accepters:
                tick_nw_event = tick + 1
                nw_event = Event(event.src, acc, "Prepare", event.pro_number)
                event_list = add_event(tick_nw_event, event_list, nw_event)

        elif event.name == "Prepare":
            if event.dst.proposal == None:
                nw_event = Promise(event.dst, event.src, "Promise",
                                   event.pro_number, None)
                event_list = add_event(tick, event_list, nw_event)

        elif event.name == "Promise":
            event.dst.promise_list.append(event.value)
            promise_list = dst.promise_list
            if len(promise_list) > accepters / 2:
                if any(promise_list):
                    for prom in promise_list:
                        if prom is not None:
                            event.dst.value == prom
                            break
                    
                    for acc in accepters:
                        tick_nw_event = tick + 1
                        nw_event = Accept(event.dst, acc, "Accept", event.pro_number, event.dst.value)
                        event_list = add_event(tick_nw_event, event_list, nw_event)
        
        elif event.name == "Accept":
            if event.dst.consensus_val == None:
                event.dst.consensus_val = event.value
                tick_nw_event = tick + 1
                nw_event = Accepted(event.dst, event_src, "Accepted", event.pro_number, event.dst.value)
                event_list = add_event(tick_nw_event, event_list, nw_event)
            
            else:
                tick_nw_event = tick + 1
                nw_event = Rejected(event.dst, event_src, "Rejected", event.pro_number, event.dst.value)
                event_list = add_event(tick_nw_event, event_list, nw_event)

            

