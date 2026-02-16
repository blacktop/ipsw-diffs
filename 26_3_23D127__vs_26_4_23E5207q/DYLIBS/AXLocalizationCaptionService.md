## AXLocalizationCaptionService

> `/System/Library/PrivateFrameworks/AXLocalizationCaptionService.framework/AXLocalizationCaptionService`

```diff

-3191.7.24.0.0
-  __TEXT.__text: 0x40c
-  __TEXT.__auth_stubs: 0x160
+3191.19.0.0.0
+  __TEXT.__text: 0x468
+  __TEXT.__auth_stubs: 0x130
   __TEXT.__objc_methlist: 0x1e4
   __TEXT.__const: 0x8
   __TEXT.__cstring: 0x8b
-  __TEXT.__unwind_info: 0x78
+  __TEXT.__unwind_info: 0x88
   __TEXT.__objc_classname: 0x3b
   __TEXT.__objc_methname: 0x4cc
   __TEXT.__objc_methtype: 0x247

   __DATA_CONST.__objc_protolist: 0x10
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_selrefs: 0x168
-  __AUTH_CONST.__auth_got: 0xb8
+  __AUTH_CONST.__auth_got: 0xa0
   __AUTH_CONST.__const: 0x20
   __AUTH_CONST.__cfstring: 0x60
   __AUTH_CONST.__objc_const: 0x260

   - /System/Library/PrivateFrameworks/AccessibilityUtilities.framework/AccessibilityUtilities
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 634DC9FE-CD5D-37A8-886D-7685663F9C87
+  UUID: D0779FFF-B6A2-3240-8E9E-3B68632ADA41
   Functions: 12
-  Symbols:   100
+  Symbols:   97
   CStrings:  91
 
Symbols:
+ _objc_retainAutoreleasedReturnValue
+ _objc_retain_x20
- _objc_claimAutoreleasedReturnValue
- _objc_release_x22
- _objc_retainAutoreleaseReturnValue
- _objc_retain_x23
- _objc_retain_x4
Functions:
~ +[AXLocalizationCaptionService service] : 68 -> 84
~ -[AXLocalizationCaptionService _clientIdentifier] : 152 -> 164
~ -[AXLocalizationCaptionService client] : 132 -> 140
~ +[AXLocalizationCaptionService _sendMessage:withIdentifier:errorHandler:] : 260 -> 264
~ ___73+[AXLocalizationCaptionService _sendMessage:withIdentifier:errorHandler:]_block_invoke : 172 -> 168
~ -[AXLocalizationCaptionService connectionWithServiceWasInterruptedForUserInterfaceClient:] : 116 -> 120
~ -[AXLocalizationCaptionService setClient:] : 12 -> 64

```
