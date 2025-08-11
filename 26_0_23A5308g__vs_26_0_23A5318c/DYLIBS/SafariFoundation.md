## SafariFoundation

> `/System/Library/PrivateFrameworks/SafariFoundation.framework/SafariFoundation`

```diff

-622.1.21.10.3
-  __TEXT.__text: 0x281c8
+622.1.22.10.4
+  __TEXT.__text: 0x28260
   __TEXT.__auth_stubs: 0xa40
   __TEXT.__objc_methlist: 0x1e14
   __TEXT.__cstring: 0x29dc
   __TEXT.__const: 0x258
   __TEXT.__gcc_except_tab: 0x11e0
-  __TEXT.__oslogstring: 0x104c
+  __TEXT.__oslogstring: 0x10a9
   __TEXT.__dlopen_cstrs: 0x203
   __TEXT.__ustring: 0x1ee
   __TEXT.__swift5_typeref: 0x163

   __TEXT.__unwind_info: 0xf58
   __TEXT.__eh_frame: 0x518
   __TEXT.__objc_classname: 0x4b1
-  __TEXT.__objc_methname: 0x73b6
+  __TEXT.__objc_methname: 0x73c2
   __TEXT.__objc_methtype: 0xb59
   __TEXT.__objc_stubs: 0x47a0
   __DATA_CONST.__got: 0x4d0

   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  UUID: 983AAFAF-A5CB-3627-98B0-CA2EBD6E883F
+  UUID: 5D6276BF-E270-3AF2-873E-0ED95FE16FF2
   Functions: 1018
   Symbols:   3448
-  CStrings:  1752
+  CStrings:  1753
 
Symbols:
+ -[SFAutoFillOneTimeCode initWithNotificationOneTimeCode:displayCode:timestamp:sourceAppName:sourceAppApplicationIdentifer:]
+ _objc_msgSend$initWithNotificationOneTimeCode:displayCode:timestamp:sourceAppName:sourceAppApplicationIdentifer:
- -[SFAutoFillOneTimeCode initWithNotificationOneTimeCode:timestamp:sourceAppName:sourceAppApplicationIdentifer:]
- _objc_msgSend$initWithNotificationOneTimeCode:timestamp:sourceAppName:sourceAppApplicationIdentifer:
Functions:
~ -[SFAppAutoFillOneTimeCodeProvider oneTimeCodeClient:detectedOneTimeCodes:] : 672 -> 808
~ -[SFAutoFillOneTimeCode initWithNotificationOneTimeCode:timestamp:sourceAppName:sourceAppApplicationIdentifer:] -> -[SFAutoFillOneTimeCode initWithNotificationOneTimeCode:displayCode:timestamp:sourceAppName:sourceAppApplicationIdentifer:] : 304 -> 320
CStrings:
+ "Ignoring OTC from notification from %{private}@ because displayCode string was nil or empty."
+ "initWithNotificationOneTimeCode:displayCode:timestamp:sourceAppName:sourceAppApplicationIdentifer:"
- "initWithNotificationOneTimeCode:timestamp:sourceAppName:sourceAppApplicationIdentifer:"

```
