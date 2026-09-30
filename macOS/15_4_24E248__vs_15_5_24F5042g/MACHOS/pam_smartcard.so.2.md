## pam_smartcard.so.2

> `/usr/lib/pam/pam_smartcard.so.2`

```diff

-213.0.0.0.0
-  __TEXT.__text: 0xa914
-  __TEXT.__auth_stubs: 0xc10
+213.120.1.0.0
+  __TEXT.__text: 0xa948
+  __TEXT.__auth_stubs: 0xc20
   __TEXT.__objc_stubs: 0x100
-  __TEXT.__cstring: 0x119f
+  __TEXT.__cstring: 0x11ce
   __TEXT.__const: 0x88
   __TEXT.__oslogstring: 0xc09
   __TEXT.__dlopen_cstrs: 0xea
   __TEXT.__objc_methname: 0x99
   __TEXT.__unwind_info: 0x1e8
-  __DATA_CONST.__auth_got: 0x610
+  __DATA_CONST.__auth_got: 0x618
   __DATA_CONST.__got: 0x198
   __DATA_CONST.__auth_ptr: 0x18
   __DATA_CONST.__const: 0x560

   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libpam.2.dylib
   Functions: 200
-  Symbols:   628
-  CStrings:  302
+  Symbols:   629
+  CStrings:  303
 
Symbols:
+ _time
CStrings:
+ "Timeout when waiting for the unreachable nodes"

```
