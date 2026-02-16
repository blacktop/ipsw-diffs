## libSystemHealth.dylib

> `/usr/lib/libSystemHealth.dylib`

```diff

-921.80.171.0.1
-  __TEXT.__text: 0x7a4
-  __TEXT.__auth_stubs: 0x1b0
+921.100.255.0.0
+  __TEXT.__text: 0x7c8
+  __TEXT.__auth_stubs: 0x180
   __TEXT.__objc_methlist: 0xc8
   __TEXT.__const: 0x60
   __TEXT.__cstring: 0xf7

   __DATA_CONST.__objc_selrefs: 0xb0
   __DATA_CONST.__objc_protorefs: 0x8
   __DATA_CONST.__objc_superrefs: 0x10
-  __AUTH_CONST.__auth_got: 0xe0
+  __AUTH_CONST.__auth_got: 0xc8
   __AUTH_CONST.__const: 0x40
   __AUTH_CONST.__cfstring: 0xe0
   __AUTH_CONST.__objc_const: 0x1c8

   - /usr/lib/libMobileGestalt.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 25AEF26C-A285-34FA-AAB0-81D5DC7EEA13
+  UUID: AAB8A34E-12DA-37F5-82AD-7D869A2034B4
   Functions: 16
-  Symbols:   119
+  Symbols:   116
   CStrings:  68
 
Symbols:
+ _objc_retainAutoreleasedReturnValue
+ _objc_retain_x19
- _objc_claimAutoreleasedReturnValue
- _objc_retain_x1
- _objc_retain_x2
- _objc_retain_x4
- _objc_retain_x8
Functions:
~ -[SystemHealthManager init] : 200 -> 204
~ -[SystemHealthManager postComponentStatusEventFor:status:withReply:] : 552 -> 572
~ ___68-[SystemHealthManager postComponentStatusEventFor:status:withReply:]_block_invoke : 88 -> 92
~ ___68-[SystemHealthManager postComponentStatusEventFor:status:withReply:]_block_invoke.23 : 288 -> 296
~ _handleForCategory : 128 -> 124
~ -[SystemHealthClient getComponentStatusWithError:] : 112 -> 116

```
