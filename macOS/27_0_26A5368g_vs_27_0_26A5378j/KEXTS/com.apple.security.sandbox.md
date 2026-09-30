## com.apple.security.sandbox

> `com.apple.security.sandbox`

```diff

   __TEXT.__os_log: 0x255d
-  __TEXT.__const: 0x204ff
+  __TEXT.__const: 0x204d7
   __TEXT.__cstring: 0x7d64
-  __TEXT_EXEC.__text: 0x54194
-  __TEXT_EXEC.__auth_stubs: 0x1500
+  __TEXT_EXEC.__text: 0x541e4
+  __TEXT_EXEC.__auth_stubs: 0x1510
   __DATA.__data: 0x410
   __DATA.__bss: 0x7f190
   __DATA_CONST.__const: 0x3f68
   __DATA_CONST.__kalloc_type: 0x1700
   __DATA_CONST.__kalloc_var: 0x550
-  __DATA_CONST.__auth_got: 0xa80
+  __DATA_CONST.__auth_got: 0xa88
   __DATA_CONST.__got: 0x100
   __DATA_CONST.__auth_ptr: 0x8
-  Functions: 967
-  Symbols:   2104
+  Functions: 969
+  Symbols:   2107
   CStrings:  1603
 
Sections:
~ __DATA.__data : content changed
~ __DATA_CONST.__const : content changed
~ __DATA_CONST.__kalloc_type : content changed
~ __DATA_CONST.__kalloc_var : content changed
~ __DATA_CONST.__got : content changed
~ __DATA_CONST.__auth_ptr : content changed
Symbols:
+ _sandbox_requires_quarantine_for_vnode
+ _sb_bundle_remove
+ _vfs_nativexattrs
+ holder_alloc.kalloc_type_view_143
+ holder_destroy.kalloc_type_view_166
+ pending_swap_begin.kalloc_type_view_2118
+ pending_swap_release.kalloc_type_view_2073
+ reference_alloc.kalloc_type_view_259
+ reference_destroy.kalloc_type_view_285
- holder_alloc.kalloc_type_view_135
- holder_destroy.kalloc_type_view_158
- pending_swap_begin.kalloc_type_view_2108
- pending_swap_release.kalloc_type_view_2063
- reference_alloc.kalloc_type_view_251
- reference_destroy.kalloc_type_view_277
Functions:
~ _macl_add_entry_locked : 232 -> 268
~ _macl_record : 1648 -> 1640
~ _deconstruct_path : 496 -> 488
+ _sandbox_requires_quarantine_for_vnode
~ _iokit_check_nvram_set : 1204 -> 1184
~ _hook_policy_init : 6764 -> 6748
~ _holder_lookup_locked : 224 -> 212
~ _sandbox_reference_release_by_holder : 432 -> 420
~ _syscall_reference_retain : 876 -> 872
~ _syscall_reference_release : 480 -> 468
~ _populate_event_context : 4096 -> 4108
~ _hook_cred_label_update_execve : 4576 -> 4568
~ _sandbox_create_for_executable : 1096 -> 1088
~ _path_simplify : 748 -> 752
+ _sb_bundle_remove
~ _syscall_appbundle_scan_start : 1188 -> 1156
~ _syscall_appbundle_scan_end : 212 -> 132
~ _syscall_check_sandbox : 4208 -> 4196
~ _macl_copy_for_vnode : 2324 -> 2288

```
