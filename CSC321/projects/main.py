def web_page():
  if led.value() == 1:
    gpio_state="ON"
  else:
    gpio_state="OFF"
  
  html = """
<html lang="en">
  <head>
    <meta charset="UTF-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0" />
    <title>Tap-Tap-Pay</title>
    <style>
      body {
        font-family: Arial, sans-serif;
        display: flex;
        justify-content: center;
        align-items: center;
        height: 100vh;
        margin: 0;
      }
      .container {
        display: flex;
        flex-direction: column;
        align-items: center;
      }
      input {
        font-size: 1.5rem;
        text-align: center;
        width: 200px;
        margin-bottom: 20px;
      }
      .dialpad {
        display: grid;
        grid-template-columns: repeat(3, 1fr);
        grid-gap: 10px;
        width: 200px;
      }
      .dialpad button {
        font-size: 1.5rem;
        background-color: #e0e0e0;
        border: none;
        padding: 10px;
        cursor: pointer;
      }
      .dialpad button:hover {
        background-color: #b3b3b3;
      }
    </style>
    <script>
      function promptForPin() {
        const pin = prompt("Please enter your PIN:");
        if (pin === null || pin === "") {
          alert("PIN entry cancelled.");
        } else {
          submitAmount(pin);
        }
      }
      function submitAmount(pin) {
        const inputField = document.getElementById("inputField");
        const amount = inputField.value;
        if (amount === "" || parseFloat(amount) <= 0) {
          alert("Please enter a valid amount.");
        } else {
          var xhr = new XMLHttpRequest();
          xhr.onreadystatechange = function () {
            if (xhr.readyState == 4 && xhr.status == 200) {
              clearInputField();
            }
          };
          xhr.open(
            "GET",
            "/?amount=" +
              encodeURIComponent(amount) +
              "&pin=" +
              encodeURIComponent(pin),
            true
          );
          xhr.send();
        }
      }
      function addToInput(num) {
        const inputField = document.getElementById("inputField");
        inputField.value += num;
      }
      function clearInputField() {
        const inputField = document.getElementById("inputField");
        inputField.value = "";
      }
    </script>
  </head>
  <body>
    <div class="container">
      <input id="inputField" type="text" readonly />
      <div class="dialpad">
        <button onclick="addToInput(1)">1</button>
        <button onclick="addToInput(2)">2</button>
        <button onclick="addToInput(3)">3</button>
        <button onclick="addToInput(4)">4</button>
        <button onclick="addToInput(5)">5</button>
        <button onclick="addToInput(6)">6</button>
        <button onclick="addToInput(7)">7</button>
        <button onclick="addToInput(8)">8</button>
        <button onclick="addToInput(9)">9</button>
        <button onclick="addToInput('.')">.</button>
        <button onclick="addToInput(0)">0</button>
        <button
          style="background-color: #4caf50; color: white;"
          onclick="promptForPin()"
        >
          OK
        </button>
      </div>
    </div>
  </body>
</html>
"""
  return html

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(('', 80))
s.listen(5)

def read_and_write_card(pin, amount):
    print("PIN: %s" % pin)
    print("Read 1000")
    print("Now reads %s" % (1000-amount))
    return True

while True:
    conn, addr = s.accept()
    print('Got a connection from %s' % str(addr))
    request = conn.recv(1024)
    request = str(request)
    amount_submit = request.find('/?amount=')
    if amount_submit == 6:
        query = request[amount_submit + 9 :].split(' ')[0]
        amount, pin = query.split('&')
        amount = amount.split('=')[1]
        pin = pin.split('=')[1]
        if amount and float(amount) > 0:
            success = read_and_write_card(pin, float(amount))
            if success:
                print('Amount written to card:', amount)
            else:
                print('Failed to write amount to card')
    else:
        print('Invalid amount')
    response = web_page()
    conn.send('HTTP/1.1 200 OK\n')
    conn.send('Content-Type: text/html\n')
    conn.send('Connection: close\n\n')
    conn.sendall(response)
    conn.close()