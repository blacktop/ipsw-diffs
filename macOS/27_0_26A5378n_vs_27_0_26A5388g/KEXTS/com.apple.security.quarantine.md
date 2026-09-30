## com.apple.security.quarantine

> `com.apple.security.quarantine`

### Sections with Same Size but Changed Content

- `__DATA_CONST.__const`
- `__DATA_CONST.__kalloc_type`
- `__DATA_CONST.__auth_got`
- `__DATA_CONST.__got`

```diff

-217.0.2.0.0
+217.0.3.0.0
   __TEXT.__const: 0x71
-  __TEXT.__cstring: 0x7e6
+  __TEXT.__cstring: 0x715
   __TEXT.__os_log: 0x3ba
-  __TEXT_EXEC.__text: 0x9940
+  __TEXT_EXEC.__text: 0x9820
   __TEXT_EXEC.__auth_stubs: 0x900
-  __DATA.__data: 0xcfb
+  __DATA.__data: 0xcc3
   __DATA.__common: 0x24
   __DATA.__bss: 0x348
   __DATA_CONST.__const: 0xc8
   __DATA_CONST.__kalloc_type: 0x280
   __DATA_CONST.__auth_got: 0x480
   __DATA_CONST.__got: 0x58
-  Functions: 143
-  Symbols:   377
-  CStrings:  109
+  Functions: 142
+  Symbols:   375
+  CStrings:  103
 
Symbols:
- _is_string_in_list
- should_collect_policy_mismatch_analytics_for_signing_id.signing_ids
Functions:
~ _hook_proc_notify_exec_complete : 508 -> 540
~ _hook_vnode_notify_create : 984 -> 980
~ _hook_vnode_notify_rename : 732 -> 728
~ _hook_vnode_notify_open : 632 -> 628
~ _hook_vnode_notify_link : 728 -> 724
~ _qtn_taint_vnode_if_needed : 576 -> 572
~ _vnode_recalculate_flags : 336 -> 140
- _is_string_in_list
~ _vnode_update_flags : 592 -> 588
CStrings:
- "com.apple.ClassKit.pdtool"
- "com.apple.CloudDocs.iCloudDriveFileProvider"
- "com.apple.CloudDocs.iCloudDriveFileProviderManaged"
- "com.apple.Safari"
- "com.apple.WorkflowKit.BackgroundShortcutRunner"
- "com.apple.nsurlsessiond"
```
