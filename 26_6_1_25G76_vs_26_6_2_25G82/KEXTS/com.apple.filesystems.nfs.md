## com.apple.filesystems.nfs

> `com.apple.filesystems.nfs`

### Sections with Same Size but Changed Content

- `__DATA.__data`
- `__DATA_CONST.__auth_got`
- `__DATA_CONST.__got`
- `__DATA_CONST.__auth_ptr`
- `__DATA_CONST.__mod_init_func`
- `__DATA_CONST.__mod_term_func`
- `__DATA_CONST.__const`
- `__DATA_CONST.__kalloc_type`
- `__DATA_CONST.__kalloc_var`

```diff

 343.160.4.0.0
   __TEXT.__cstring: 0x9c42
   __TEXT.__const: 0x39c
-  __TEXT_EXEC.__text: 0x9d2a0
+  __TEXT_EXEC.__text: 0x9d218
   __TEXT_EXEC.__auth_stubs: 0x0
   __DATA.__data: 0xf00
   __DATA.__common: 0xee4
Functions:
~ _nfs4_named_attr_get : 17388 -> 17196
~ _nfs4_default_attrs_for_referral_trigger : 476 -> 496
~ _nfs_nget : 4604 -> 4572
~ _nfs_vnop_reclaim : 3508 -> 3512
~ _nfs_lookitup : 948 -> 960
~ _nfsm_chaim_add_exclusive_create_verifier : 340 -> 356
~ _nfs3_setlock_rpc : 544 -> 556
~ _nfs3_unlock_rpc : 408 -> 420
~ _nfs3_getlock_rpc : 520 -> 532
```
