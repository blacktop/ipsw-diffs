## libxcselect.dylib

> `/usr/lib/libxcselect.dylib`

```diff

 2409.0.0.0.0
-  __TEXT.__text: 0x1e54
+  __TEXT.__text: 0x1e4c
   __TEXT.__auth_stubs: 0x3a0
-  __TEXT.__cstring: 0xf6a
+  __TEXT.__cstring: 0xf68
   __TEXT.__const: 0x1020
   __TEXT.__oslogstring: 0x60
-  __TEXT.__unwind_info: 0xd8
+  __TEXT.__unwind_info: 0xe0
   __DATA_CONST.__got: 0x18
   __DATA_CONST.__const: 0xf0
   __AUTH_CONST.__auth_got: 0x1d0
   __AUTH_CONST.__const: 0x60
   __DATA.__bss: 0x20
   - /usr/lib/libSystem.B.dylib
-  UUID: 797C7846-E0BE-3DC6-ABB9-893597412813
-  Functions: 30
-  Symbols:   106
-  CStrings:  89
+  UUID: 4D9907F8-4105-3A19-BB45-08F82D34F503
+  Functions: 32
+  Symbols:   108
+  CStrings:  88
 
Symbols:
+ lazyCFSymbol.cold.1
+ xcselect_host_sdk_path.cold.1
Functions:
~ _xcselect_get_developer_dir_path : 852 -> 856
~ _get_developer_dir_from_symlink : 220 -> 212
~ _is_path_xcrun_shim : 744 -> 740
~ _xcselect_find_developer_contents_from_path : 508 -> 504
~ _xcselect_host_sdk_path : 736 -> 720
~ _xcselect_bundle_is_developer_tool : 152 -> 148
~ _lazyCFSymbol : 116 -> 100
+ xcselect_host_sdk_path.cold.1
CStrings:
- "/"

```
