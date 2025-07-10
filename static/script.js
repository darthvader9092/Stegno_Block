async function revealHash(event, blockName) {
  event.preventDefault();
  const form = event.target;
  const authKey = form.querySelector('input:nth-of-type(1)').value;
  const privateKey = form.querySelector('input:nth-of-type(2)').value;
  const output = form.querySelector('.hash-output');

  const res = await fetch("/view_hash", {
    method: "POST",
    headers: { 'Content-Type': 'application/x-www-form-urlencoded' },
    body: `block=${blockName}&auth_key=${authKey}&private_key=${privateKey}`
  });

  const data = await res.json();
  output.textContent = data.hash;
  return false;
}