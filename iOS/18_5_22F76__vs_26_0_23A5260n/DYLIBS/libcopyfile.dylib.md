## libcopyfile.dylib

> `/usr/lib/system/libcopyfile.dylib`

```diff

-221.122.1.0.0
-  __TEXT.__text: 0x74e8
+226.0.0.0.0
+  __TEXT.__text: 0x75f4
   __TEXT.__auth_stubs: 0x660
   __TEXT.__const: 0x1c8
-  __TEXT.__cstring: 0x19c8
-  __TEXT.__unwind_info: 0xe8
+  __TEXT.__cstring: 0x1a10
+  __TEXT.__unwind_info: 0xe0
   __DATA_CONST.__got: 0x28
   __DATA_CONST.__const: 0x3b0
   __AUTH_CONST.__auth_got: 0x330

   - /usr/lib/system/libsystem_kernel.dylib
   - /usr/lib/system/libsystem_malloc.dylib
   - /usr/lib/system/libxpc.dylib
-  UUID: 675716DC-E2FE-3850-9BE6-C8D0B0B7C278
+  UUID: 0C082ADD-C725-3116-80A9-53A8EED3D673
   Functions: 37
   Symbols:   188
-  CStrings:  189
+  CStrings:  191
 
Functions:
~ _copyfile_open : 3636 -> 3784
~ _copyfile_internal : 7604 -> 7612
~ _copyfile_data : 3344 -> 3340
~ _fcopyfile -> sub_2122edca8 : 620 -> 72
~ _copyfile_fix_perms -> sub_2122edcf0 : 204 -> 72
~ _copyfile_state_get -> _fcopyfile : 356 -> 620
~ sub_20d1b80ac -> _copyfile_fix_perms : 72 -> 204
~ _copyfile_state_set -> _copyfile_state_get : 452 -> 356
~ sub_20d1b82b8 -> _copyfile_state_set : 72 -> 452
~ _copyfile_pack : 4384 -> 4500
CStrings:
+ "file %s changed behind our feet: %m"
+ "fstat on open fd failed for %s\n: %m"

```
