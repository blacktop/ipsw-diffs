## adid

> `/usr/libexec/adid`

```diff

-18.2.0.0.0
-  __TEXT.__text: 0x183218
+18.4.0.0.0
+  __TEXT.__text: 0x1840b4
   __TEXT.__auth_stubs: 0x10
-  __TEXT.__const: 0x6b230
-  __TEXT.__oslogstring: 0x24
+  __TEXT.__const: 0x6b2a0
+  __TEXT.__oslogstring: 0x2b
   __TEXT.__cstring: 0xf
   __TEXT.__unwind_info: 0x1a0
   __DATA_CONST.__auth_got: 0x8
   __DATA_CONST.__got: 0x8
   __DATA_CONST.__auth_ptr: 0x10
-  __DATA_CONST.__const: 0x11620
+  __DATA_CONST.__const: 0x11590
   __DATA_CONST.__cfstring: 0x20
   __DATA.__data: 0x1770
   __DATA.__common: 0x141

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libbsm.0.dylib
   Functions: 134
-  Symbols:   117
-  CStrings:  5
+  Symbols:   120
+  CStrings:  6
 
Symbols:
+ _os_release
+ _os_transaction_create
+ _pthread_set_qos_class_self_np
CStrings:
+ "A5: %u"

```
