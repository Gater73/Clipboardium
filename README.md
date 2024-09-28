# Clipboardium

Clipboardium is a secure clipboard sharing application designed to allow users to share clipboard data over the internet without the need for Bluetooth or being on the same network. The application ensures data privacy by keeping rooms in memory and using encryption for data transmission.

## Screenshot
![Clipboardium](https://i.imgur.com/CDF4iFA.png)

## Features

- **Real-Time Clipboard Sharing**: Share clipboard data seamlessly between users.
- **Secure Data Transmission**: Clipboard data is encrypted using AES (Advanced Encryption Standard) before transmission.
- **In-Memory Rooms**: Rooms are stored in memory for privacy and are purged when the application restarts.
- **Multi-Language Support**: Easily toggle between English and Portuguese.
- **User-Friendly Interface**: Built using the Bulma CSS framework for a modern look.

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/Gater73/Clipboardium.git
   cd Clipboardium
   ```

2. Create a virtual environment using Conda:
   ```bash
   conda create --name clipboardium python=3.8
   conda activate clipboardium
   ```

3. Install the required packages:
   ```bash
   pip install -r requirements.txt
   ```

4. Run the Flask application:
   ```bash
   python app.py
   ```

5. Access the app in your web browser at `https://localhost:5000`.

## Usage

## Warning
> :warning: **USE A WSGI**: The in-transport security of Clipboardium relies on TLS/SSL encryption being enabled for the website! 

1. Copy the text you want to share to your clipboard.
2. Create a room and share the generated room code with another user.
3. The second user can enter the room code to join the session.
4. Click the "Send Clipboard" button to share the clipboard data.
5. The shared data will appear in real-time for both users.

## Security

Clipboardium employs the following security measures:

- **TLS/SSL Encryption**: All data transmission is secured using TLS to prevent eavesdropping and tampering.
- **AES Encryption**: Clipboard data is encrypted using a symmetric key (AES) before being sent over the network.
- **In-Memory Storage**: Room data is not stored persistently, ensuring user privacy.

## License

This project is licensed under the [GNU General Public License v3.0](https://www.gnu.org/licenses/gpl-3.0.html). You are free to use, modify, and distribute this software, provided that any copies or substantial portions of the software include the original license.

## Contributing

Contributions are welcome! Please feel free to open issues or submit pull requests.

## Acknowledgments

- **Flask**: A micro web framework for Python.
- **Socket.IO**: Enables real-time, bidirectional communication between web clients and servers.
- **Bulma**: A modern CSS framework based on Flexbox.

## Contact

For any questions or inquiries, please reach out via [your email or contact method].
