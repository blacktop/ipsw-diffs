## libAHTRestore.dylib

> `/usr/lib/libAHTRestore.dylib`

```diff

-9100.29.1.0.0
-  __TEXT.__text: 0x186c
-  __TEXT.__auth_stubs: 0x2c0
+9140.6.0.0.0
+  __TEXT.__text: 0x193c
+  __TEXT.__auth_stubs: 0x280
   __TEXT.__objc_methlist: 0x134
   __TEXT.__const: 0x20
   __TEXT.__cstring: 0x254

   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_selrefs: 0x1a0
   __DATA_CONST.__objc_superrefs: 0x8
-  __AUTH_CONST.__auth_got: 0x168
+  __AUTH_CONST.__auth_got: 0x148
   __AUTH_CONST.__const: 0x20
   __AUTH_CONST.__cfstring: 0x3e0
   __AUTH_CONST.__objc_const: 0x190

   - /System/Library/Frameworks/IOKit.framework/Versions/A/IOKit
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 41431ECF-512D-3DD3-8C15-68C5B309AAFA
+  UUID: F8706A86-8C7A-3F8B-8FB7-4C66B4CC97D4
   Functions: 31
-  Symbols:   184
+  Symbols:   180
   CStrings:  147
 
Symbols:
+ _objc_retainAutoreleasedReturnValue
- _objc_claimAutoreleasedReturnValue
- _objc_retain
- _objc_retain_x1
- _objc_retain_x2
- _objc_retain_x8
Functions:
~ +[AHTLoader allDevices] : 360 -> 372
~ ___23+[AHTLoader allDevices]_block_invoke : 132 -> 128
~ +[AHTLoader withName:] : 344 -> 356
~ +[AHTLoader bootloaderPropertiesForImageTag:] : 272 -> 280
~ -[AHTLoader description] : 184 -> 192
~ -[AHTLoader fullDescription] : 608 -> 648
~ ___28-[AHTLoader fullDescription]_block_invoke : 80 -> 84
~ ___28-[AHTLoader fullDescription]_block_invoke_2 : 392 -> 420
~ +[AHTLoader errorFromKernel:error:] : 264 -> 276
~ +[AHTLoader errorFromAfuKextResult:error:] : 296 -> 308
~ -[AHTLoader loadImage:payloadOnly:options:error:] : 516 -> 536
~ -[AHTLoader overrideFDR:fdrClass:fdrSubclass:error:] : 452 -> 448
~ -[AHTLoader overrideNextLoadOptions:error:] : 116 -> 120
~ +[AHTLoader registryPropertiesForService:] : 88 -> 92
~ _AHTRestoreCreateDeviceList : 504 -> 528
~ _AHTRestoreUpdateDevice : 196 -> 200
~ _AHTRestoreUpdateDeviceWithOverrides : 484 -> 504
~ _AHTRestoreFailureCleanup : 188 -> 192

```
