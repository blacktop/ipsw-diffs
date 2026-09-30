## libsysmon.dylib

> `/usr/lib/libsysmon.dylib`

```diff

-127.0.0.0.0
+129.0.0.0.0
   __TEXT.__text: 0x1780
   __TEXT.__auth_stubs: 0x370
   __TEXT.__objc_methlist: 0x4c

   __DATA_CONST.__objc_superrefs: 0x18
   __AUTH_CONST.__auth_got: 0x1b8
   __AUTH_CONST.__objc_const: 0x6f8
-  __AUTH.__objc_data: 0x140
   __DATA.__data: 0x218
+  __DATA_DIRTY.__objc_data: 0x140
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
   Functions: 45

```
