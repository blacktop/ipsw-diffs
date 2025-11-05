## libSMC.dylib

> `/usr/lib/libSMC.dylib`

```diff

-34.0.0.0.0
-  __TEXT.__text: 0x56f0
+38.0.0.0.0
+  __TEXT.__text: 0x5930
   __TEXT.__auth_stubs: 0x3e0
   __TEXT.__const: 0xd9a40
   __TEXT.__oslogstring: 0x6d1
   __TEXT.__cstring: 0x265
-  __TEXT.__unwind_info: 0x140
+  __TEXT.__unwind_info: 0x150
   __DATA_CONST.__got: 0x40
   __DATA_CONST.__const: 0xac0
   __AUTH_CONST.__auth_got: 0x1f0

   - /System/Library/Frameworks/CoreFoundation.framework/Versions/A/CoreFoundation
   - /System/Library/Frameworks/IOKit.framework/Versions/A/IOKit
   - /usr/lib/libSystem.B.dylib
-  UUID: E7EAB738-D9B0-3E10-913E-B8D053CD21EE
-  Functions: 121
-  Symbols:   298
+  UUID: 2C7E9774-AF67-3CF9-8ED4-082FEEBBC501
+  Functions: 122
+  Symbols:   304
   CStrings:  68
 
Symbols:
+ SMCRegisterForSubTypeNotification.cold.4
+ SMCUnregisterForNotification.cold.1
+ _SMCReadPKey
+ __block_descriptor_tmp.12
+ __block_descriptor_tmp.6
+ _smcNotificationCallback.cold.1
+ _unregisterForNotification.cold.2
+ getSMCQueue.cold.1
- _OUTLINED_FUNCTION_5
- __block_descriptor_tmp.10
- __block_descriptor_tmp.5

```
