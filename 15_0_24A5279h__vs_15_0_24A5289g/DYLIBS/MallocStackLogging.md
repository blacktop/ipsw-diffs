## MallocStackLogging

> `/System/Library/PrivateFrameworks/MallocStackLogging.framework/Versions/A/MallocStackLogging`

```diff

-64566.89.1.0.0
-  __TEXT.__text: 0x95d8
+64566.95.1.0.0
+  __TEXT.__text: 0x91e8
   __TEXT.__auth_stubs: 0x6b0
   __TEXT.__const: 0x130
-  __TEXT.__cstring: 0x203f
-  __TEXT.__unwind_info: 0x278
+  __TEXT.__cstring: 0x1f7c
+  __TEXT.__unwind_info: 0x270
   __DATA_CONST.__got: 0x48
   __DATA_CONST.__const: 0x20
   __AUTH_CONST.__auth_got: 0x358

   - /usr/lib/system/libsystem_malloc.dylib
   - /usr/lib/system/libsystem_platform.dylib
   - /usr/lib/system/libsystem_pthread.dylib
-  Functions: 236
-  Symbols:   400
-  CStrings:  210
+  Functions: 229
+  Symbols:   395
+  CStrings:  204
 
Symbols:
+ uniquing_table_stack_retain_internal.cold.14
+ uniquing_table_stack_retain_internal.cold.15
+ uniquing_table_stack_retain_internal.cold.16
- _assert_nonzero_slot
- _release_nonzero_slot
- assert_nonzero_slot.cold.1
- assert_nonzero_slot.cold.2
- release_nonzero_slot.cold.1
- release_nonzero_slot.cold.2
- uniquing_table_node_release_internal.cold.2
- uniquing_table_stack_release.cold.1
CStrings:
- "check_result.size_count_slot.size_count > 0"
- "previous_size_count >= size"
- "retrieved.size_count_slot.size_count > 0"
- "size"
- "sub_result.size_count_slot.size_count >= amount"
- "uniquing_table_stack_release"

```
