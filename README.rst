Gmailpy
=======

A simple API wrapper for sending emails with  Gmail

Getting Started
---------------

Install via pip (recommended)

.. code:: bash

    pip install gmailpy

Install from source

.. code:: bash

    pip install git+https://github.com/iDutchy/gmailpy
    
Getting Started
---------------

First you need to create your client:

.. code:: python

    import gmailpy
    
    client = gmailpy.Client("john.doe@gmail.com", "P@$$w0rd")

Usage
-----

await client.send(receiver, content, subject=None, bcc=None, attachment_bytes=None, attachment_name=None)
#########################################################################################################

* **Parameters:**
    * reveiver (string): The receivers email address
    * content (string): The content of the email
    * subject (string): The email subject. *Defaults to "No subject"*
    * bcc (list): A list of other email addresses you want to send the mail to as BCC. *Defaults to None*
    * attachment_bytes (byte array): Attach anything  to the email. This has to be a byte array! When providing this, the `attachment_bytes` argument becomes required! *Defaults to None*
    * attachment_name (string): The **full** name of the attachment. This has to contain the file extension too! e.g "dog.png". This is required when providing `attachment_bytes`. *Defaults to None*
