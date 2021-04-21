

def email_search(mails, searched_mail):
    for mail in mails:
        if mail == searched_mail:
            print("Emails on the list")
            return True

    print("Emails not on the list")
    return False


email_list = ["lala@gmail.com", "ola@gmail.com", "jola@wp.pl", "olaf10000@gmail.com", "zenek.kowal@onet.eu"]
searched_mail = "laloooo@gmail.com"

print(email_search(email_list, searched_mail))
# def check_mails(mails, check):
#     for mail in mails:
#         if mail == check:
#             return True
#     return False
#
# #---
#
# mails_list = [ 'a@a.pl', 'b@b.pl', 'c@c.pl']
# searched_mail = 'b@b.pl'
#
# print(check_mails(mails_list, searched_mail))