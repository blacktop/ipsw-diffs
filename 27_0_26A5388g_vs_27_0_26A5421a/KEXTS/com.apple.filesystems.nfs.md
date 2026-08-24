## com.apple.filesystems.nfs

> `com.apple.filesystems.nfs`

```diff

-356.0.5.0.0
+356.0.6.0.0
   __TEXT.__cstring: 0x9c42
   __TEXT.__const: 0x39c
-  __TEXT_EXEC.__text: 0x9df90
+  __TEXT_EXEC.__text: 0x9dfb0
   __TEXT_EXEC.__auth_stubs: 0x1530
   __DATA.__data: 0xf00
   __DATA.__common: 0xee4
Symbols:
+ nfs_gss_clnt_ctx_copy.kalloc_type_view_2368
+ nfs_gss_clnt_ctx_copy.kalloc_type_view_2372
+ nfs_gss_clnt_ctx_destroy.kalloc_type_view_2429
+ nfs_gss_clnt_rpcdone.kalloc_type_view_2145
- nfs_gss_clnt_ctx_copy.kalloc_type_view_2367
- nfs_gss_clnt_ctx_copy.kalloc_type_view_2371
- nfs_gss_clnt_ctx_destroy.kalloc_type_view_2428
- nfs_gss_clnt_rpcdone.kalloc_type_view_2144
Functions:
~ _nfs_gss_clnt_ctx_init_retry : 5732 -> 5728
~ _nfs4_named_attr_get : 17428 -> 17416
~ _nfs4_parsefattr : 18660 -> 18656
~ _nfs4_default_attrs_for_referral_trigger : 476 -> 496
~ _nfs_nget : 4664 -> 4628
~ _nfs_vnop_reclaim : 3460 -> 3464
~ _nfs_lookitup : 948 -> 960
~ _nfsm_chaim_add_exclusive_create_verifier : 340 -> 356
~ _nfs3_setlock_rpc : 544 -> 556
~ _nfs3_unlock_rpc : 408 -> 420
~ _nfs3_getlock_rpc : 520 -> 532
```
