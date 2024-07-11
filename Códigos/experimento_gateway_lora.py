from pyLoraRFM9x import LoRa, ModemConfig
import time

# This is our callback function that runs when a message is received
def on_recv(payload):
    print("From:", payload.header_from)
    print("Received:", payload.message)
    print("Msg:", payload.header_id)
    print()
    print("RSSI: {}; SNR: {}".format(payload.rssi, payload.snr))
    lora.send_ack(payload.header_to, payload.header_id)
    print("ACK SENT to ")
    lora.set_mode_rx()  
    time.sleep(5)

# Use chip select 1. GPIO pin 5 will be used for interrupts and set reset pin to 25
# The address of this device will be set to 2
lora = LoRa(1, 5, 2, reset_pin = 25, modem_config=ModemConfig.Bw125Cr48Sf4096, tx_power=18, acks=False, receive_all=True)
lora.on_recv = on_recv
lora.set_mode_rx()  

# Send a message to a recipient device with address 10
# Retry sending the message twice if we don't get an  acknowledgment from the recipient
message = "Hello there!/n"
while(True):
	time.sleep(3) #Necessário uma linha de código para manter rodando indefinidamente. 
