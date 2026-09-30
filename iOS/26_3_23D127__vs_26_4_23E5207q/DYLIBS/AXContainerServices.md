## AXContainerServices

> `/System/Library/PrivateFrameworks/AXContainerServices.framework/AXContainerServices`

```diff

-3191.7.24.0.0
-  __TEXT.__text: 0x84c
-  __TEXT.__auth_stubs: 0x1b0
+3191.19.0.0.0
+  __TEXT.__text: 0x8c0
+  __TEXT.__auth_stubs: 0x160
   __TEXT.__objc_methlist: 0x68
   __TEXT.__const: 0x8
   __TEXT.__cstring: 0x6b

   __DATA_CONST.__objc_classlist: 0x8
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_selrefs: 0x70
-  __AUTH_CONST.__auth_got: 0xe0
+  __AUTH_CONST.__auth_got: 0xb8
   __AUTH_CONST.__const: 0x20
   __AUTH_CONST.__cfstring: 0x60
   __AUTH_CONST.__objc_const: 0xd0

   - /System/Library/PrivateFrameworks/AccessibilityUtilities.framework/AccessibilityUtilities
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 1E6930F7-4CBC-3680-A667-B8D0B28AD210
+  UUID: BC173CB0-0592-34B3-9FD3-9679FF2B42AE
   Functions: 13
-  Symbols:   92
+  Symbols:   87
   CStrings:  31
 
Symbols:
+ _objc_retainAutoreleasedReturnValue
- _objc_claimAutoreleasedReturnValue
- _objc_retainAutoreleaseReturnValue
- _objc_retain_x1
- _objc_retain_x22
- _objc_retain_x3
- _objc_retain_x4
Functions:
~ -[AXContainerManager containerServerClient] : 160 -> 172
~ +[AXContainerManager sharedManager] : 68 -> 84
~ -[AXContainerManager readDataForFileAtAccessibilityContainerPath:completion:] : 340 -> 344
~ ___77-[AXContainerManager readDataForFileAtAccessibilityContainerPath:completion:]_block_invoke : 192 -> 204
~ _getErrorCascading : 356 -> 364
~ ___78-[AXContainerManager writeData:toFileAtAccessibilityContainerPath:completion:]_block_invoke : 96 -> 100
~ -[AXContainerManager deleteFileAtAccessibilityContainerPath:completion:] : 340 -> 344
~ ___72-[AXContainerManager deleteFileAtAccessibilityContainerPath:completion:]_block_invoke : 96 -> 100
~ -[AXContainerManager setContainerServerClient:] : 12 -> 64

```
