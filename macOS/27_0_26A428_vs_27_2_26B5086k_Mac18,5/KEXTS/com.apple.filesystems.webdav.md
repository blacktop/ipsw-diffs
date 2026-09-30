## com.apple.filesystems.webdav

> `com.apple.filesystems.webdav`

```diff

-413.0.0.0.0
+413.40.2.0.0
   __TEXT.__cstring: 0x904
   __TEXT.__const: 0xd0
-  __TEXT_EXEC.__text: 0x5cfc
-  __TEXT_EXEC.__auth_stubs: 0x770
+  __TEXT_EXEC.__text: 0x5d04
+  __TEXT_EXEC.__auth_stubs: 0x790
   __DATA.__data: 0x340
   __DATA.__common: 0x38
   __DATA_CONST.__kalloc_type: 0x240
-  __DATA_CONST.__auth_got: 0x3b8
+  __DATA_CONST.__auth_got: 0x3c8
   __DATA_CONST.__got: 0x30
   Functions: 66
-  Symbols:   244
+  Symbols:   246
   CStrings:  62
 
Symbols:
+ _ubc_upl_map_range
+ _ubc_upl_unmap_range
+ webdav_get.kalloc_type_view_884
+ webdav_get.kalloc_type_view_908
+ webdav_get.kalloc_type_view_983
+ webdav_vnop_reclaim.kalloc_type_view_3830
+ webdav_vnop_write.kalloc_type_view_2581
+ webdav_vnop_write.kalloc_type_view_2702
- webdav_get.kalloc_type_view_883
- webdav_get.kalloc_type_view_907
- webdav_get.kalloc_type_view_982
- webdav_vnop_reclaim.kalloc_type_view_3829
- webdav_vnop_write.kalloc_type_view_2580
- webdav_vnop_write.kalloc_type_view_2701
Functions:
~ _webdav_vnop_pageout : 1008 -> 1016
```
