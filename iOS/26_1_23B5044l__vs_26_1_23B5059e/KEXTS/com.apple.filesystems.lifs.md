## com.apple.filesystems.lifs

> `com.apple.filesystems.lifs`

```diff

-737.40.5.0.0
-  __TEXT.__os_log: 0x13b7
-  __TEXT.__cstring: 0x2220
+737.40.13.0.0
+  __TEXT.__os_log: 0x13e3
+  __TEXT.__cstring: 0x2226
   __TEXT.__const: 0x2c0
-  __TEXT_EXEC.__text: 0x1ba50
+  __TEXT_EXEC.__text: 0x1bad0
   __TEXT_EXEC.__auth_stubs: 0x0
   __DATA.__data: 0x5d0
   __DATA.__common: 0x138
   __DATA.__bss: 0x90
-  __DATA_CONST.__auth_got: 0x7e8
+  __DATA_CONST.__auth_got: 0x7f8
   __DATA_CONST.__got: 0x80
   __DATA_CONST.__auth_ptr: 0x8
   __DATA_CONST.__mod_init_func: 0x18

   __DATA_CONST.__const: 0x16b8
   __DATA_CONST.__kalloc_type: 0xbc0
   __DATA_CONST.__kalloc_var: 0xf0
-  UUID: 59DB1B21-2C6B-3F23-AFF0-6A021A77D104
+  UUID: F04893FC-E8F8-32DF-87DA-8F32CD933341
   Functions: 406
   Symbols:   0
-  CStrings:  402
+  CStrings:  403
 
Functions:
~ sub_fffffe000b06da80 -> sub_fffffe000b0be020 : 744 -> 776
~ sub_fffffe000b06f05c -> sub_fffffe000b0bf61c : 704 -> 680
~ sub_fffffe000b0787fc -> sub_fffffe000b0c8da4 : 492 -> 612
CStrings:
+ "\"%s: lnode %p vp %p async_io_inflights (%d) < 0\" @%s:%d"
+ "Skipping directory entry contains '/': %.*s"
- "\"%s: lnode %p async_io_inflights (%d) < 0\" @%s:%d"

```
