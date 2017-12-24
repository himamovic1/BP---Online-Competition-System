class Permission:
    """ Class defining list of possible permissions of each user """
    FULL_ACCESS = 0xff
    STUDENT_ACCESS = 0x02
    STUDENT_UNCONFIRMED_ACCESS = 0x01
    PUBLIC_ACCESS = 0x00

    CREATE_COMPETITION = 0x01
    MODIFY_COMPETITION = 0x02
    CREATE_RESULTS = 0x04
    VIEW_RESULTS = 4


def redirect_unconfirmed(student, allowed_endpoints=[]):
    from flask import request, redirect, url_for

    if student.is_authenticated \
            and not student.confirmed \
            and request.endpoint not in allowed_endpoints:
        return redirect(url_for('auth.unconfirmed'))

    return None


def send_email(sender, recipients, subject, text_body='', template=None, **kwargs):
    from flask import current_app, render_template
    from flask_mail import Message

    from competition import mail
    from competition.decorators import async

    @async
    def send_email_async(app, message):
        with app.app_context():
            mail.send(message)

    msg = Message(subject=subject, sender=sender, recipients=recipients)
    msg.body = text_body

    if template:
        msg.html = render_template(template, **kwargs)

    with current_app.app_context():
        mail.send(msg)

    # send_email_async(app=current_app, message=msg)
