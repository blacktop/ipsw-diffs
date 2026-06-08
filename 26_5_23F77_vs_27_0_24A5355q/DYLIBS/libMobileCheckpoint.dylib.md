## libMobileCheckpoint.dylib

> `/usr/lib/libMobileCheckpoint.dylib`

```diff

 40.0.0.0.0
-  __TEXT.__text: 0x874
-  __TEXT.__auth_stubs: 0x1e0
+  __TEXT.__text: 0x81c
   __TEXT.__cstring: 0x1dd
   __TEXT.__unwind_info: 0x78
-  __TEXT.__objc_methname: 0x109
-  __TEXT.__objc_stubs: 0x160
-  __DATA_CONST.__got: 0x38
+  __TEXT.__objc_stubs: 0x0
+  __TEXT.__auth_stubs: 0x0
+  __TEXT.__objc_methname: 0x0
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_selrefs: 0x58
-  __AUTH_CONST.__auth_got: 0xf8
+  __DATA_CONST.__got: 0x0
   __AUTH_CONST.__cfstring: 0x100
+  __AUTH_CONST.__auth_got: 0x0
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/Foundation.framework/Foundation
   - /System/Library/PrivateFrameworks/MobileSystemServices.framework/MobileSystemServices
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 046DC12A-C965-3951-BD0A-35410A9E73A8
+  UUID: CED260CA-52F7-3791-88C2-A56326404FD7
   Functions: 5
-  Symbols:   57
-  CStrings:  31
+  Symbols:   56
+  CStrings:  20
 
Symbols:
+ _objc_claimAutoreleasedReturnValue
+ _objc_retain_x8
- _objc_retainAutoreleasedReturnValue
- _objc_retain_x20
- _objc_retain_x23
Functions:
~ _MCCopyCheckpoint : 592 -> 560
~ __cacheValid : 336 -> 324
~ _MCCopyCheckpointData : 352 -> 340
~ _MCCopyCheckpointValue : 644 -> 620
~ _getResponseForCommand : 240 -> 232
CStrings:
- "UTF8String"
- "dataWithPropertyList:format:options:error:"
- "dictionaryWithObjects:forKeys:count:"
- "initWithContentsOfFile:"
- "initWithContentsOfFile:options:error:"
- "initWithObjects:"
- "lastPathComponent"
- "numberWithUnsignedInt:"
- "objectForKey:"
- "stringWithFormat:"
- "stringWithUTF8String:"

```
