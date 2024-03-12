const accountSid = "ACc436a63f1a376b9569583540a47df9f8"; // Your Twilio Account SID
const authToken = "e99fae94513389200e056c9fea3d045f"; // Your Twilio Auth Token
const client = require("twilio")(accountSid, authToken);

// Function to send a text message
async function sendTextMessage() {
  try {
    const message = await client.messages.create({
      body: "Hello, this is a test message!",
      from: "'+918459190688'", // Your Twilio phone number
      to: "+918237326365", // The recipient's phone number
    });
    console.log("Message sent successfully. SID:", message.sid);
  } catch (error) {
    console.error("Error sending message:", error);
  }
}

// Call the function to send the text message
sendTextMessage();
