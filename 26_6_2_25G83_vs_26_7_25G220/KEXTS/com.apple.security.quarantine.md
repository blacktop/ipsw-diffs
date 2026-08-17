## com.apple.security.quarantine

> `com.apple.security.quarantine`

```diff

-196.160.2.0.0
+196.160.2.700.3
   __TEXT.__const: 0x71
   __TEXT.__cstring: 0x649
   __TEXT.__os_log: 0x2a7
-  __TEXT_EXEC.__text: 0x8d88
+  __TEXT_EXEC.__text: 0x8da0
   __TEXT_EXEC.__auth_stubs: 0x0
   __DATA.__data: 0xcc3
   __DATA.__common: 0x24
-  __DATA_CONST.__auth_got: 0x430
+  __DATA_CONST.__auth_got: 0x438
   __DATA_CONST.__got: 0x48
   __DATA_CONST.__const: 0xc8
   __DATA_CONST.__kalloc_type: 0x280
   Functions: 137
-  Symbols:   345
+  Symbols:   346
   CStrings:  83
 
Symbols:
+ _sandbox_requires_quarantine_for_vnode
Functions:
~ _hook_policy_syscall : 8192 -> 8188
~ _hook_vnode_notify_create : 984 -> 980
~ _hook_vnode_notify_rename : 732 -> 728
~ _hook_vnode_notify_open : 632 -> 628
~ _hook_vnode_notify_link : 728 -> 724
~ _qtn_taint_vnode_if_needed : 576 -> 572
~ _vnode_recalculate_flags : 120 -> 140
~ _quarantine_getinfo : 432 -> 464
~ _vnode_update_flags : 592 -> 588
```
