from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/email-to-remarks', methods=['POST'])
def email_to_remarks():
    data = request.json
    subject = data.get('subject', '')
    sender = data.get('sender', 'Vendor')
    body = data.get('body', '')

    summary = f"Email regarding: {subject}. Sender reported: {body[:100]}..."
    reply = (
        f"Hi {sender.split()[0]},\n\n"
        "Thanks for the update. I’ve reviewed your note and we’ll proceed accordingly. "
        "Please let me know if there are any changes or additional details required.\n\n"
        "Best,\nKen"
    )
    order_remarks = (
        f"4/7 KT – Received email from {sender} regarding \"{subject}\". Summary of message: {body[:100]}... "
        "Replied confirming receipt and acknowledging next steps. Awaiting further updates if needed."
    )

    return jsonify({
        "summary": summary,
        "reply": reply,
        "order_remarks": order_remarks
    })

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
