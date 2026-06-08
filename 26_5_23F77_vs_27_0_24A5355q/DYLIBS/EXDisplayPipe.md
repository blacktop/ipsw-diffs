## EXDisplayPipe

> `/System/Library/PrivateFrameworks/EXDisplayPipe.framework/EXDisplayPipe`

```diff

-8.1.12.0.0
-  __TEXT.__text: 0x8d8
-  __TEXT.__auth_stubs: 0xb0
+9.1.40.0.0
+  __TEXT.__text: 0xa68
   __TEXT.__const: 0x40
-  __TEXT.__cstring: 0x248
-  __TEXT.__unwind_info: 0x58
-  __DATA_CONST.__got: 0x10
-  __AUTH_CONST.__auth_got: 0x58
+  __TEXT.__cstring: 0x2a1
+  __TEXT.__unwind_info: 0x68
+  __TEXT.__auth_stubs: 0x0
+  __DATA_CONST.__got: 0x0
+  __AUTH_CONST.__cfstring: 0x20
+  __AUTH_CONST.__auth_got: 0x0
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/IOKit.framework/Versions/A/IOKit
   - /usr/lib/libSystem.B.dylib
-  UUID: 7B7611A7-DA6D-3B28-8FBD-83BA0B957C75
-  Functions: 14
-  Symbols:   29
-  CStrings:  20
+  UUID: 1E384FA1-9885-342D-BAF4-46F60AB180F5
+  Functions: 16
+  Symbols:   38
+  CStrings:  25
 
Symbols:
+ _CFNumberGetValue
+ _CFRelease
+ _EXDisplayPipeGetFrameInfo
+ _EXDisplayPipeOpenDisplay
+ _IOIteratorNext
+ _IOObjectRelease
+ _IORegistryEntrySearchCFProperty
+ _IOServiceGetMatchingServices
+ ___CFConstantStringClassReference
+ _kCFAllocatorDefault
- _IOServiceGetMatchingService
Functions:
~ _EXDisplayPipeOpen : 276 -> 12
+ _EXDisplayPipeOpenDisplay
CStrings:
+ "EXDisplayPipeGetFrameInfo"
+ "IOService"
+ "display-index"
+ "error: failed to get matching services"

```
