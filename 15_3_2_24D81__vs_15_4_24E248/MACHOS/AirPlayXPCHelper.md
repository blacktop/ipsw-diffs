## AirPlayXPCHelper

> `/usr/libexec/AirPlayXPCHelper`

```diff

-845.5.1.0.0
-  __TEXT.__text: 0x778
+850.19.1.0.0
+  __TEXT.__text: 0x71c
   __TEXT.__auth_stubs: 0x2f0
-  __TEXT.__const: 0x20
-  __TEXT.__cstring: 0x306
-  __TEXT.__oslogstring: 0x9d
+  __TEXT.__const: 0x18
+  __TEXT.__cstring: 0x37e
+  __TEXT.__oslogstring: 0x3a
   __TEXT.__unwind_info: 0x68
   __DATA_CONST.__auth_got: 0x178
   __DATA_CONST.__got: 0x30
   __DATA_CONST.__const: 0x60
   __DATA_CONST.__cfstring: 0x20
   __DATA_CONST.__objc_imageinfo: 0x8
+  __DATA.__data: 0x70
   - /System/Library/Frameworks/AudioToolbox.framework/Versions/A/AudioToolbox
   - /System/Library/Frameworks/CoreAudio.framework/Versions/A/CoreAudio
   - /System/Library/Frameworks/CoreFoundation.framework/Versions/A/CoreFoundation

   - /System/Library/PrivateFrameworks/WiFiPeerToPeer.framework/Versions/A/WiFiPeerToPeer
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 87C59CF1-EEF7-3CB9-80D0-A5F2C4797A95
+  UUID: F45DCC10-D254-3CF7-B605-9E9D56C5619A
   Functions: 3
   Symbols:   57
-  CStrings:  24
+  CStrings:  25
 
Symbols:
+ _LogPrintF
+ __LogCategory_Initialize
+ _getprogname
+ _sandbox_init
- _free
- _mkdir
- _realpath$DARWIN_EXTSN
- _sandbox_init_with_parameters
Functions:
~ sub_100002de8 -> sub_100000ee8 : 1180 -> 1088
CStrings:
+ "%s: failed to initialize temp directory: %s"
+ "%s: will use temp directory '%s'"
+ "AirPlayMain"
+ "sandbox_init() failed: %s"
+ "void setupTempDirectory(const char *)"
- "Failed to enter sandbox: %s"
- "Failed to initialize temporary directory (%d): %s"
- "Failed to resolve temporary directory (%d): %s"
- "TMPDIR"

```
