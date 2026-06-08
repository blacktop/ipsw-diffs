## libffi.dylib

> `/usr/lib/libffi.dylib`

```diff

 40.0.0.0.0
-  __TEXT.__text: 0xd310
-  __TEXT.__auth_stubs: 0x100
+  __TEXT.__text: 0xd32c
   __TEXT.__const: 0x150
   __TEXT.__cstring: 0xa5
-  __TEXT.__unwind_info: 0x118
+  __TEXT.__unwind_info: 0x120
   __TEXT.__eh_frame: 0x90
-  __DATA_CONST.__got: 0x10
+  __TEXT.__auth_stubs: 0x0
   __DATA_CONST.__const: 0x50
-  __AUTH_CONST.__auth_got: 0x80
+  __DATA_CONST.__got: 0x0
   __AUTH_CONST.__const: 0x20
+  __AUTH_CONST.__auth_got: 0x80
   __DATA.__data: 0x60
   __DATA.__bss: 0x18
   - /usr/lib/libSystem.B.dylib
-  UUID: C14F8E49-EF85-3C06-A5C4-DC3B64E55672
+  UUID: E67985C2-2FC3-39BB-AF10-CA0F57610A6E
   Functions: 48
   Symbols:   109
   CStrings:  7
Functions:
~ _ffi_java_ptrarray_to_raw : 204 -> 244
~ _ffi_ptrarray_to_raw : 308 -> 316
~ _ffi_get_struct_offsets : 13680 -> 13632
~ _ffi_call_int : 1300 -> 1304
~ _ffi_prep_closure_loc : 128 -> 132
~ _ffi_closure_SYSV_inner : 932 -> 952

```
