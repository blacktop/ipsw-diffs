## PersonalAudio

> `/System/Library/PrivateFrameworks/PersonalAudio.framework/PersonalAudio`

```diff

-496.13.0.0.0
-  __TEXT.__text: 0x1512c
-  __TEXT.__auth_stubs: 0x4e0
+496.15.0.0.0
+  __TEXT.__text: 0x1522c
+  __TEXT.__auth_stubs: 0x4f0
   __TEXT.__objc_methlist: 0xea8
   __TEXT.__const: 0x110
   __TEXT.__gcc_except_tab: 0x39c
   __TEXT.__cstring: 0x1247
-  __TEXT.__oslogstring: 0xc39
+  __TEXT.__oslogstring: 0xd5d
   __TEXT.__dlopen_cstrs: 0x163
-  __TEXT.__unwind_info: 0x5e8
+  __TEXT.__unwind_info: 0x5f0
   __TEXT.__objc_classname: 0xdb
   __TEXT.__objc_methname: 0x32b7
   __TEXT.__objc_methtype: 0x419
-  __TEXT.__objc_stubs: 0x2e60
+  __TEXT.__objc_stubs: 0x2ea0
   __DATA_CONST.__got: 0x190
   __DATA_CONST.__const: 0x720
   __DATA_CONST.__objc_classlist: 0x50

   __DATA_CONST.__objc_selrefs: 0xe98
   __DATA_CONST.__objc_superrefs: 0x40
   __DATA_CONST.__objc_arraydata: 0x40
-  __AUTH_CONST.__auth_got: 0x280
+  __AUTH_CONST.__auth_got: 0x288
   __AUTH_CONST.__const: 0x300
   __AUTH_CONST.__cfstring: 0x1500
   __AUTH_CONST.__objc_const: 0x1038

   - /usr/lib/libAccessibility.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 932021CC-DC75-308B-B241-C47DD23BAAAE
-  Functions: 437
-  Symbols:   1634
-  CStrings:  1077
+  UUID: 101EE20B-38A7-3460-83D2-7E66D10C995F
+  Functions: 439
+  Symbols:   1641
+  CStrings:  1078
 
Symbols:
+ ___53-[PAAccessoryManager sendPMEConfigurationToAccessory]_block_invoke.39
+ ___53-[PAAccessoryManager sendPMEConfigurationToAccessory]_block_invoke.44
+ ___53-[PAAccessoryManager sendPMEConfigurationToAccessory]_block_invoke_2.cold.1
+ ___block_literal_global.41
+ ___block_literal_global.47
+ _dispatch_async
+ _objc_msgSend$pmeHysteresisTimer
+ _objc_msgSend$setPmeHysteresisTimer:
- ___53-[PAAccessoryManager sendPMEConfigurationToAccessory]_block_invoke.41
- ___block_literal_global.40
- ___block_literal_global.46
Functions:
~ ___53-[PAAccessoryManager sendPMEConfigurationToAccessory]_block_invoke : 228 -> 412
~ ___53-[PAAccessoryManager sendPMEConfigurationToAccessory]_block_invoke_2 : 280 -> 180
~ -[PAAccessoryManager sendPMEConfigurationToAccessory] : 344 -> 148
+ ___53-[PAAccessoryManager sendPMEConfigurationToAccessory]_block_invoke.39
+ ___53-[PAAccessoryManager sendPMEConfigurationToAccessory]_block_invoke_2.cold.1
CStrings:
+ "PAAccessoryManager: Couldn't send PME configuration, media settings nil or identifier can't be found [%@]. Config is %@"
+ "PAAccessoryManager: Found PME supported %@"
+ "PAAccessoryManager: Not sending PME configuration, device isn't supported [%d, %d, %d] %@"
+ "PAAccessoryManager: Sent PME configuration updates to buds with error %@"
+ "PAAccessoryManager: Skipping PME configuration update"
+ "PAAccessoryManager: Skipping PME configuration update because pending timer"
+ "PAAccessoryManager: Starting PME configuration processing"
- "Device isn't supported [%d, %d, %d] %@"
- "Found PME supported %@"
- "Media settings nil or identifier can't be found [%@]. Config is %@"
- "Sent updates to buds with error %@"
- "Skipping update because pending timer"
- "Starting processing"

```
