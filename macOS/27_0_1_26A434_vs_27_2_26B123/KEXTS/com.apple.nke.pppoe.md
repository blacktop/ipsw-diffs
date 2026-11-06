## com.apple.nke.pppoe

> `com.apple.nke.pppoe`

```diff

-1031.0.0.0.4
+1043.0.0.0.0
   __TEXT.__cstring: 0x94b
   __TEXT.__const: 0x29
-  __TEXT_EXEC.__text: 0x3a88
-  __TEXT_EXEC.__auth_stubs: 0x370
-  __DATA.__data: 0xe4
+  __TEXT_EXEC.__text: 0x3ad8
+  __TEXT_EXEC.__auth_stubs: 0x380
+  __DATA.__data: 0xf0
   __DATA.__common: 0x744
   __DATA.__bss: 0x18
   __DATA_CONST.__const: 0x18
   __DATA_CONST.__kalloc_type: 0x280
-  __DATA_CONST.__auth_got: 0x1b8
+  __DATA_CONST.__auth_got: 0x1c0
   __DATA_CONST.__got: 0x60
   Functions: 65
-  Symbols:   156
+  Symbols:   158
   CStrings:  60
 
Symbols:
+ _memcpy
+ pppoe_rfc_connect.nextUnique
Functions:
~ _pppoe_rfc_connect : 368 -> 416
~ _pppoe_rfc_timer : 400 -> 432
```
