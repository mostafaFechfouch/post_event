# post_event
This is a basic post event tool that allows you to create certificates for all your attendees and send it to them by email

# Setup instructions
<ol>
  <li>git clone https://github.com/mostafaFechfouch/post_event.git</li>
        you will get the project in your computer
  <li>you should have python3 installed (otherwise install it from here: https://www.python.org/downloads/release/python-3101/)</li>
  <li>install the following libraries:</li>
  <ul>run in the cli:
          <li>pip install unicodecsv</li>
          <li>pip install Pillow</li>
          <li>pip install arabic-reshaper</li>
          <li>pip install python-bidi</li>
          <li>pip install dotenv</li>
  </ul>
  <li>You should have a certificate template in png format</li>
  <li>You should have a message template in text format</li>
  <li>You should have your favorite fonts to use in writing</li>
  <li>You should have a csv file containing your participants names and emails</li>
  <li>Create a authentication.env file in an ENV folder containing your email and password</li>
  <li>Once you have all the requirements in place</li>
  <ul>run the following commands in cli:
    <li> <i> python certificate_generator.py </i> This will generate all your certificates in pdf format</li>
    <li> <i> python email_sender.py </i> This will send emails to all your participants with their certificates attached</li>
  </ul>
</ol>
# Congratulations!
