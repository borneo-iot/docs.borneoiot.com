# Mobile App

## Building from Source

### Environment Setup

First, please refer to the official Google [Flutter documentation](https://docs.flutter.dev/get-started) to set up the development environment, ensuring that the `flutter` command is added to the `%PATH%` or `$PATH` environment variable.

### Building and Running

Prepare a mobile emulator or connect a real device, navigate to the `client` directory, and execute:

```bash
flutter pub get
flutter run
```

Since the app uses the Flutter cross-platform framework, it can also run on Windows, Linux and MacOS, though it has not been adapted for landscape screen.

I do not own any Apple devices, so iOS and MacOS support is theoretical and untested.