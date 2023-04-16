const contactsList = document.getElementById('contacts-list');



// get called when button is pressed
function getContacts() {
    fetch('http://127.0.0.1:5000/contacts')
      .then(response => response.json())
      .then(contacts => {
        for (let contact of contacts) {
          const li = document.createElement('li');
          li.textContent = `_id: ${contact._id.$oid} name: ${contact.name} email: ${contact.email} phone: ${contact.phone} address: ${contact.address} company: ${contact.company} fullname: ${contact.fullname}`;
          contactsList.appendChild(li);
        }
      })
      .catch(error => {
        console.error('Error fetching contacts:', error);
      });
}
  