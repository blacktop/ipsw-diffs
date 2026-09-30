## com.apple.security.quarantine

> `com.apple.security.quarantine`

```diff

-181.80.2.0.0
-  __TEXT.__const: 0x71
+181.100.13.0.0
+  __TEXT.__const: 0x51
   __TEXT.__cstring: 0x649
   __TEXT.__os_log: 0x2a7
-  __TEXT_EXEC.__text: 0x956c
+  __TEXT_EXEC.__text: 0x8d54
   __TEXT_EXEC.__auth_stubs: 0x0
   __DATA.__data: 0xcc3
   __DATA.__common: 0x24
   __DATA.__bss: 0x28
-  __DATA_CONST.__auth_got: 0x420
+  __DATA_CONST.__auth_got: 0x428
   __DATA_CONST.__got: 0x48
   __DATA_CONST.__const: 0xc8
   __DATA_CONST.__kalloc_type: 0x280
-  UUID: 0FC9B4D0-5F71-36DC-9C68-AC8C04538C3D
-  Functions: 183
-  Symbols:   379
+  UUID: D9FE33C0-8E3B-37DC-A4B4-414448BD8777
+  Functions: 131
+  Symbols:   381
   CStrings:  83
 
Symbols:
+ _hook_mount_notify_mount
+ _memcpy
+ _vfs_vnodecovered_noblock
+ hook_mount_notify_mount.empty
+ identity_create_from_executable_vnode.cold.3
- _read_responsibility_set_audittoken_args
- _vfs_vnodecovered
- hook_mount_label_associate.empty

```
