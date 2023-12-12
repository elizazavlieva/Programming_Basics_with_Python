total_tickets_for_one_movie = 0
stud_tickets = 0
standard_ticket = 0
kids_ticket = 0
total_tickets = 0
total_stud_tickets = 0
total_standard_tickets = 0
total_kids_tickets = 0
while True:
    movie_name = input()
    if movie_name == 'Finish':
        stud_tickets_prs = total_stud_tickets / total_tickets * 100
        standard_ticket_prs = total_standard_tickets / total_tickets * 100
        kids_ticket_prs = total_kids_tickets / total_tickets * 100
        print(f"Total tickets: {total_tickets}")
        print(f"{stud_tickets_prs:.2f}% student tickets.")
        print(f"{standard_ticket_prs:.2f}% standard tickets.")
        print(f"{kids_ticket_prs:.2f}% kids tickets.")
        break

    free_seats = int(input())
    stud_tickets = 0
    standard_ticket = 0
    kids_ticket = 0
    total_tickets_for_one_movie = 0
    for i in range(1, free_seats + 1):
        ticket_type = input()
        if ticket_type == 'End':
            break
        if ticket_type == 'student':
            stud_tickets += 1
            total_stud_tickets += 1
        elif ticket_type == 'standard':
            standard_ticket += 1
            total_standard_tickets += 1
        elif ticket_type == 'kid':
            kids_ticket += 1
            total_kids_tickets += 1
        total_tickets_for_one_movie += 1
        total_tickets += 1
        if total_tickets_for_one_movie >= free_seats:
            break
    taken_seats_prs = total_tickets_for_one_movie / free_seats * 100
    print(f'{movie_name} - {taken_seats_prs:.2f}% full.')
