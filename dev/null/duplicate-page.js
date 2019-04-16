javascript:
nd = window.open().document;
nd.head.innerHTML = document.head.innerHTML;
base = document.createElement("body");
base.href = window.location.href;
nd.head.appendChild(base);
nd.body.innerHTML = document.body.innerHTML;
