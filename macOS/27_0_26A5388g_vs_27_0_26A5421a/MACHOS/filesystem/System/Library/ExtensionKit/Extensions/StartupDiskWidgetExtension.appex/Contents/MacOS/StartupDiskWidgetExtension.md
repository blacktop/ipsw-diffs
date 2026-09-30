## StartupDiskWidgetExtension

> `/System/Library/ExtensionKit/Extensions/StartupDiskWidgetExtension.appex/Contents/MacOS/StartupDiskWidgetExtension`

### Sections with Same Size but Changed Content

- `__TEXT.__cstring`

```diff

-912.0.0.0.0
+914.0.0.0.0
   __TEXT.__text: 0x8730
   __TEXT.__auth_stubs: 0x890
   __TEXT.__objc_stubs: 0xa0
CStrings:
+ "Name of the current startup disk"
+ "The “Startup Disk” setting page is located under the “General” section in System Settings. This setting allows the user to modify the startup disk, which is the disk that the system will boot when it is started."
+ "This will return the name of the current startup disk."
- "Name of the current Startup Disk"
- "The “Startup Disk” setting page is located under the “General” section in System Settings. This setting allows the user to modify the Startup Disk, which is the disk that the system will boot when it is started."
- "This will return the name of the current Startup Disk."
```
