## com.apple.filesystems.nfs

> `com.apple.filesystems.nfs`

```diff

-356.0.6.0.0
-  __TEXT.__cstring: 0x9c42
+356.40.4.0.0
+  __TEXT.__cstring: 0x9c53
   __TEXT.__const: 0x39c
-  __TEXT_EXEC.__text: 0x9d9b0
+  __TEXT_EXEC.__text: 0x9dadc
   __TEXT_EXEC.__auth_stubs: 0x1530
   __DATA.__data: 0xf00
   __DATA.__common: 0xee4

   __DATA_CONST.__auth_ptr: 0x8
   Functions: 1000
   Symbols:   1762
-  CStrings:  1156
+  CStrings:  1157
 
Symbols:
+ gss_krb5_destroy_context.kalloc_type_view_2799
+ gss_krb5_make_context.kalloc_type_view_2778
+ gss_krb5_make_context.kalloc_type_view_2781
+ nfs_sillyrename.kalloc_type_view_7074
+ nfs_sillyrename.kalloc_type_view_7133
+ nfs_vnop_reclaim.kalloc_type_view_1181
- gss_krb5_destroy_context.kalloc_type_view_2795
- gss_krb5_make_context.kalloc_type_view_2774
- gss_krb5_make_context.kalloc_type_view_2777
- nfs_sillyrename.kalloc_type_view_7070
- nfs_sillyrename.kalloc_type_view_7129
- nfs_vnop_reclaim.kalloc_type_view_1164
Functions:
~ _nfs_recover : 3476 -> 3524
~ _nfs_request_finish : 2936 -> 2940
~ _nfs_vnop_reclaim : 3468 -> 3604
~ _nfs_dir_buf_freespace : 52 -> 64
~ _nfs3_readdir_rpc : 4748 -> 4832
~ _mbuf_walk : 604 -> 620
CStrings:
+ "nfswaitdelegscan"
```
