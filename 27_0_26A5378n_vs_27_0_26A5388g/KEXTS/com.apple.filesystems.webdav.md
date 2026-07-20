## com.apple.filesystems.webdav

> `com.apple.filesystems.webdav`

### Sections with Same Size but Changed Content

- `__DATA.__data`
- `__DATA_CONST.__got`

```diff

-410.0.0.0.0
-  __TEXT.__cstring: 0x878
+412.0.0.0.0
+  __TEXT.__cstring: 0x904
   __TEXT.__const: 0xd0
-  __TEXT_EXEC.__text: 0x5cd0
-  __TEXT_EXEC.__auth_stubs: 0x740
+  __TEXT_EXEC.__text: 0x5c90
+  __TEXT_EXEC.__auth_stubs: 0x770
   __DATA.__data: 0x340
   __DATA.__common: 0x38
   __DATA.__bss: 0x818
-  __DATA_CONST.__auth_got: 0x3a0
+  __DATA_CONST.__kalloc_type: 0x240
+  __DATA_CONST.__auth_got: 0x3b8
   __DATA_CONST.__got: 0x30
   Functions: 66
-  Symbols:   232
-  CStrings:  57
+  Symbols:   244
+  CStrings:  62
 
Symbols:
+ _hashdestroy
+ _kalloc_data
+ _kalloc_type_impl
+ _kfree_data
+ _kfree_type_impl
+ webdav_get.kalloc_type_view_883
+ webdav_get.kalloc_type_view_907
+ webdav_get.kalloc_type_view_982
+ webdav_mount.kalloc_type_view_323
+ webdav_mount.kalloc_type_view_454
+ webdav_unmount.kalloc_type_view_535
+ webdav_vnop_reclaim.kalloc_type_view_3829
+ webdav_vnop_write.kalloc_type_view_2580
+ webdav_vnop_write.kalloc_type_view_2701
- __FREE
- __MALLOC
Functions:
~ _webdav_hashdestroy : 88 -> 96
~ _webdav_mount : 1220 -> 1148
~ _webdav_unmount : 312 -> 324
~ _webdav_vfs_getattr : 756 -> 772
~ _webdav_get : 680 -> 648
~ _webdav_vnop_write : 848 -> 852
~ _webdav_vnop_reclaim : 116 -> 120
~ _webdav_read_bytes : 364 -> 360
CStrings:
+ "1211122222222222222222222"
+ "22111111222222222222222222112"
+ "site.struct webdav_request_writeseq"
+ "site.struct webdavmount"
+ "site.struct webdavnode"
```
