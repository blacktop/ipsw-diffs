## DAEASOAuthFramework

> `/System/Library/PrivateFrameworks/DAEASOAuthFramework.framework/DAEASOAuthFramework`

```diff

-2073.0.0.0.0
-  __TEXT.__text: 0xce88
+2074.0.0.0.0
+  __TEXT.__text: 0xcea4
   __TEXT.__auth_stubs: 0x4f0
   __TEXT.__objc_methlist: 0xc40
   __TEXT.__const: 0x98

   __TEXT.__oslogstring: 0x167d
   __TEXT.__unwind_info: 0x290
   __TEXT.__objc_classname: 0x249
-  __TEXT.__objc_methname: 0x2a47
-  __TEXT.__objc_methtype: 0x4bc
+  __TEXT.__objc_methname: 0x2a58
+  __TEXT.__objc_methtype: 0x4d1
   __TEXT.__objc_stubs: 0x2240
   __DATA_CONST.__got: 0x2f0
   __DATA_CONST.__const: 0x4c0

   - /System/Library/PrivateFrameworks/Preferences.framework/Preferences
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 33B70DD7-9739-309C-B04A-8285EC8D523F
+  UUID: 295DBE3B-644F-37D6-AE62-E9BAB4A37495
   Functions: 243
   Symbols:   1192
-  CStrings:  1015
+  CStrings:  1016
 
Symbols:
+ -[DAEASOAuthWebViewController initWithAccount:isFirstTimeSetup:accountStore:presentationBlock:]
- -[DAEASOAuthWebViewController initWithAccount:accountStore:presentationBlock:]
Functions:
~ -[DAEASOAuthWebViewController initWithAccount:accountStore:presentationBlock:] -> -[DAEASOAuthWebViewController initWithAccount:isFirstTimeSetup:accountStore:presentationBlock:] : 196 -> 212
~ ___90-[DAEASOAuthWebViewController _extensionRequestDidCompleteWithTokens:extensionCompletion:]_block_invoke_2 : 2336 -> 2348
CStrings:
+ "@44@0:8@16B24@28@?36"
+ "initWithAccount:isFirstTimeSetup:accountStore:presentationBlock:"
- "initWithAccount:accountStore:presentationBlock:"

```
