## liblockdown.dylib

> `/usr/lib/liblockdown.dylib`

```diff

-1350.2.1.0.0
-  __TEXT.__text: 0x5e6c
-  __TEXT.__auth_stubs: 0x970
+1350.40.8.0.0
+  __TEXT.__text: 0x5e4c
+  __TEXT.__auth_stubs: 0x990
   __TEXT.__const: 0x460
   __TEXT.__cstring: 0x191d
   __TEXT.__oslogstring: 0x550

   __DATA_CONST.__const: 0x528
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_selrefs: 0x10
-  __AUTH_CONST.__auth_got: 0x4c0
+  __AUTH_CONST.__auth_got: 0x4d0
   __AUTH_CONST.__const: 0x80
   __AUTH_CONST.__cfstring: 0x1b80
   __DATA_DIRTY.__data: 0x30

   - /System/Library/PrivateFrameworks/MobileKeyBag.framework/MobileKeyBag
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 5486A61C-3366-39C5-B3F4-6FF02FA18792
+  UUID: 6F44E789-DD10-3A64-A737-6DD9CCFF2331
   Functions: 120
-  Symbols:   514
+  Symbols:   516
   CStrings:  543
 
Symbols:
+ _xpc_connection_get_context
+ _xpc_connection_set_context
Functions:
~ ___lockdown_checkin_xpc_block_invoke : 656 -> 628
~ ___lockdown_checkin_xpc_block_invoke_2 : 1336 -> 1332

```
