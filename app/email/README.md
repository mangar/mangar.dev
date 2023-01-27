

# Providers

## SMTP4DEV

        docker run -p 3030:80 -p 2525:25 -d --name smtpdev rnwood/smtp4dev


__smtp-cli__


        sudo apt-get install  libio-socket-ssl-perl  libdigest-hmac-perl  libterm-readkey-perl libmime-lite-perl libfile-libmagic-perl libio-socket-inet6-perl -y


        wget https://raw.githubusercontent.com/mludvig/smtp-cli/HEAD/smtp-cli

        chmod +x smtp-cli

       ./smtp-cli --verbose --server localhost --port=2525 

        # send email
        ./smtp-cli --verbose --server localhost --port=2525 --from test@example.org --to test@example.net --data data.txt




## MailDev


        docker run -p 1080:1080 -p 1025:1025 -d --name maildev maildev/maildev


.
- Web: http://localhost:1080
- SMTP: http://localhost:1025

.

        ./smtp-cli --verbose --server localhost --port=1025 --from test@example.org --to test@example.net --data data.txt

