## libremovefile.dylib

> `/usr/lib/system/libremovefile.dylib`

```diff

-85.100.6.0.0
-  __TEXT.__text: 0x20ac
-  __TEXT.__auth_stubs: 0x300
-  __TEXT.__const: 0x40
-  __TEXT.__cstring: 0x2d
+94.0.0.0.0
+  __TEXT.__text: 0x1fc8
+  __TEXT.__const: 0x48
+  __TEXT.__cstring: 0x5d
   __TEXT.__unwind_info: 0xa8
-  __DATA_CONST.__got: 0x10
-  __AUTH_CONST.__auth_got: 0x180
+  __TEXT.__auth_stubs: 0x0
+  __DATA_CONST.__const: 0x50
+  __DATA_CONST.__got: 0x0
+  __AUTH_CONST.__auth_got: 0x1a0
   - /usr/lib/system/libcompiler_rt.dylib
   - /usr/lib/system/libdyld.dylib
+  - /usr/lib/system/libsystem_blocks.dylib
   - /usr/lib/system/libsystem_c.dylib
+  - /usr/lib/system/libsystem_containermanager.dylib
   - /usr/lib/system/libsystem_kernel.dylib
   - /usr/lib/system/libsystem_malloc.dylib
   - /usr/lib/system/libsystem_platform.dylib
-  UUID: F15FF19D-C319-37D0-87A3-985A0F46C299
-  Functions: 21
-  Symbols:   81
-  CStrings:  5
+  UUID: BD6C2143-87F1-3839-B8DA-BBF362443BDB
+  Functions: 22
+  Symbols:   90
+  CStrings:  6
 
Symbols:
+ __Block_object_dispose
+ __NSConcreteStackBlock
+ _____removefile_tree_walker_slim_block_invoke
+ _____removefile_tree_walker_slim_block_invoke_2
+ ___block_descriptor_tmp
+ ___block_descriptor_tmp.2
+ _container_traverse_directory
+ _container_traverse_node_get_depth_from_origin
+ _container_traverse_node_get_optional_flags
+ _container_traverse_node_get_path
+ _container_traverse_node_is_directory
- _dirfd
- _malloc_type_realloc
- _move_to_parent_dir
Functions:
+ ___removefile_tree_walker_slim
- ___removefile_tree_walker_slim
- _move_to_parent_dir
~ _overwrite_bytes : 296 -> 300
+ _____removefile_tree_walker_slim_block_invoke
+ _____removefile_tree_walker_slim_block_invoke_2
CStrings:
+ "B16@?0r*8"
+ "B24@?0^{container_traverse_node_s=}8^B16"
- "%s"

```
