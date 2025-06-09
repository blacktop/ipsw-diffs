## IOUSBLib

> `/System/Library/Extensions/IOUSBHostFamily.kext/PlugIns/IOUSBLib.bundle/IOUSBLib`

```diff

-1402.100.21.0.0
-  __TEXT.__text: 0x8b70
-  __TEXT.__auth_stubs: 0x410
-  __TEXT.__cstring: 0x266
-  __TEXT.__const: 0x7c
+1493.0.6.0.0
+  __TEXT.__text: 0x85a8
+  __TEXT.__auth_stubs: 0x370
+  __TEXT.__cstring: 0x218
+  __TEXT.__const: 0x74
   __TEXT.__gcc_except_tab: 0x7c
-  __TEXT.__unwind_info: 0x1d8
-  __DATA_CONST.__auth_got: 0x210
-  __DATA_CONST.__got: 0x40
+  __TEXT.__unwind_info: 0x1d0
+  __DATA_CONST.__auth_got: 0x1c0
+  __DATA_CONST.__got: 0x30
   __DATA_CONST.__const: 0x4a0
-  __DATA_CONST.__cfstring: 0x360
+  __DATA_CONST.__cfstring: 0x320
   __DATA.__data: 0x490
   __DATA.__common: 0x4
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/IOKit.framework/Versions/A/IOKit
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libc++.1.dylib
-  UUID: 45CAD855-4283-3A2A-ACD9-DDD3DC642809
+  UUID: 85A8715A-844A-3B2A-A6A0-6082B2B28CBF
   Functions: 279
-  Symbols:   371
-  CStrings:  60
+  Symbols:   359
+  CStrings:  54
 
Symbols:
- _CFDictionaryCreateMutable
- _CFDictionarySetValue
- _IOIteratorNext
- _IORegistryEntryGetChildIterator
- _IORegistryEntryGetRegistryEntryID
- _IORegistryEntryIDMatching
- _IOServiceGetMatchingService
- _IOServiceGetState
- _IOServiceMatching
- _kCFTypeDictionaryKeyCallBacks
- _kCFTypeDictionaryValueCallBacks
- _usleep
Functions:
~ __ZN16IOUSBDeviceClass5startEPK14__CFDictionaryj : 1968 -> 1288
~ __ZN19IOUSBInterfaceClass5startEPK14__CFDictionaryj : 1036 -> 236
CStrings:
- "AppleUSBAlternateServiceRegistryID"
- "AppleUSBHostPort"
- "IOPropertyMatch"
- "IOService"

```
