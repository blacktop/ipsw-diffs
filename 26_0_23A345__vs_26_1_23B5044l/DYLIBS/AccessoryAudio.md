## AccessoryAudio

> `/System/Library/PrivateFrameworks/AccessoryAudio.framework/AccessoryAudio`

```diff

-1124.2.1.0.0
-  __TEXT.__text: 0x338c
+1139.40.1.0.0
+  __TEXT.__text: 0x3404
   __TEXT.__auth_stubs: 0x330
   __TEXT.__objc_methlist: 0x2bc
   __TEXT.__const: 0xa0
   __TEXT.__cstring: 0x210
-  __TEXT.__oslogstring: 0x506
+  __TEXT.__oslogstring: 0x545
   __TEXT.__gcc_except_tab: 0x1d0
-  __TEXT.__unwind_info: 0x170
+  __TEXT.__unwind_info: 0x168
   __TEXT.__objc_classname: 0x77
   __TEXT.__objc_methname: 0x5c0
   __TEXT.__objc_methtype: 0x1e1

   - /System/Library/Frameworks/Foundation.framework/Foundation
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: A16EAB73-631D-34B9-9301-AE890A2A3F53
+  UUID: 63129CD1-0987-3135-B29F-59426D2FD62A
   Functions: 81
-  Symbols:   387
-  CStrings:  167
+  Symbols:   389
+  CStrings:  168
 
Symbols:
+ ___35-[ACCAudioClient initWithDelegate:]_block_invoke.cold.3
Functions:
~ ___35-[ACCAudioClient initWithDelegate:]_block_invoke : 436 -> 576
~ ___33-[ACCAudioClient connectToServer]_block_invoke : 292 -> 272
~ ___33-[ACCAudioClient connectToServer]_block_invoke.63 : 284 -> 264
~ ___33-[ACCAudioClient connectToServer]_block_invoke.66 : 300 -> 308
~ -[ACCAudioClient unregisterForAccessoryDigitalAudioNotifications] : 56 -> 68
CStrings:
+ "ACCAudioClient deallocated during server availability callback"

```
