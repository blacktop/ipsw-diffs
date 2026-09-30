## livefiles_ntfs.dylib

> `/System/Library/PrivateFrameworks/UserFS.framework/PlugIns/livefiles_ntfs.dylib`

```diff

-166.0.0.0.0
-  __TEXT.__text: 0x43a04
+168.0.0.0.0
+  __TEXT.__text: 0x42bf8
   __TEXT.__auth_stubs: 0x4a0
-  __TEXT.__const: 0xde8
-  __TEXT.__cstring: 0x13953
-  __TEXT.__oslogstring: 0xf3d
-  __TEXT.__unwind_info: 0x578
+  __TEXT.__const: 0xdd0
+  __TEXT.__cstring: 0x13963
+  __TEXT.__oslogstring: 0x108c
+  __TEXT.__unwind_info: 0x628
   __TEXT.__objc_methname: 0x6e
   __TEXT.__objc_stubs: 0x80
   __DATA_CONST.__got: 0x30

   - /System/Library/PrivateFrameworks/UserFS.framework/UserFS
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 2958F0AF-5247-3916-8B14-E5E5764E8321
-  Functions: 1037
-  Symbols:   2810
-  CStrings:  1655
+  UUID: 2F3A4273-2072-31B6-8031-23DFDBD83D28
+  Functions: 1157
+  Symbols:   3078
+  CStrings:  1660
 
Symbols:
+ _OUTLINED_FUNCTION_11
+ _OUTLINED_FUNCTION_12
+ _OUTLINED_FUNCTION_13
+ _OUTLINED_FUNCTION_14
+ _OUTLINED_FUNCTION_15
+ _OUTLINED_FUNCTION_16
+ _OUTLINED_FUNCTION_17
+ _OUTLINED_FUNCTION_18
+ _OUTLINED_FUNCTION_19
+ _OUTLINED_FUNCTION_20
+ _objc_retainAutoreleasedReturnValue
+ _plugin_fsops_get_fs_representation
+ _plugin_fsops_get_fs_representation.cold.1
+ _plugin_fsops_get_fs_representation.cold.2
+ _plugin_fsops_get_fs_representation.cold.3
+ _plugin_fsops_get_fs_representation.cold.4
+ _plugin_fsops_get_fs_representation.cold.5
- _ntfs_default_security_id_init.cold.3
- _ntfs_index_descend_into_child_node.cold.5
- _objc_claimAutoreleasedReturnValue
CStrings:
+ "%s:%s: Failed to convert UTF-16 string (length %lu) to UTF-8. (buffer size %lu): %s (%d)"
+ "%s:%s: Failed to convert UTF-8 string '%s' (length %lu) to UTF-16: %s (%d)"
+ "%s:%s: Got NULL name or result buffer: %s (%d)"
+ "%s:%s: Got an empty name: %s (%d)"
+ "%s:%s: The given buffer size (%lu) is too small for the result name (length %lu): %s (%d)"
+ "plugin_fsops_get_fs_representation"
- "%s(): !index_ctx\n\n"

```
