## libremovefile.dylib

> `/usr/lib/system/libremovefile.dylib`

```diff

-84.0.0.0.0
-  __TEXT.__text: 0x205c
+85.100.6.0.0
+  __TEXT.__text: 0x20ac
   __TEXT.__auth_stubs: 0x300
-  __TEXT.__const: 0x50
+  __TEXT.__const: 0x40
   __TEXT.__cstring: 0x2d
   __TEXT.__unwind_info: 0xa8
   __DATA_CONST.__got: 0x10

   - /usr/lib/system/libsystem_kernel.dylib
   - /usr/lib/system/libsystem_malloc.dylib
   - /usr/lib/system/libsystem_platform.dylib
-  UUID: FE4A2C77-C202-32D3-853B-A02C73DCFAD3
+  UUID: 20B472A5-FF83-3415-9916-86463EF28DAB
   Functions: 21
   Symbols:   81
   CStrings:  5
Symbols:
+ ___memmove_chk
+ ___strncpy_chk
- _memmove
- _strncpy
Functions:
~ _removefile : 724 -> 732
~ ___removefile_tree_walker_slim : 1208 -> 1232
~ ___removefile_tree_walker : 1212 -> 1268
~ ___removefile_rename_unlink : 640 -> 660
~ ___removefile_sunlink : 772 -> 768
~ _overwrite_file : 1028 -> 1040
~ _overwrite_bytes : 332 -> 296

```
