## com.apple.filesystems.tmpfs

> `com.apple.filesystems.tmpfs`

```diff

-80.0.0.0.0
+82.0.0.0.0
   __TEXT.__cstring: 0x4b7
   __TEXT.__const: 0x40
   __TEXT.__os_log: 0x20a
-  __TEXT_EXEC.__text: 0x960c
+  __TEXT_EXEC.__text: 0x9554
   __TEXT_EXEC.__auth_stubs: 0x0
   __DATA.__data: 0x180
   __DATA.__bss: 0x8

   __DATA_CONST.__got: 0x20
   __DATA_CONST.__const: 0x4d0
   __DATA_CONST.__kalloc_type: 0x480
-  UUID: 51195246-87D0-321C-A9F2-440A35E4AF43
-  Functions: 156
-  Symbols:   367
+  UUID: BC0B1B17-22A4-36C2-9073-45657479D143
+  Functions: 152
+  Symbols:   366
   CStrings:  46
 
Symbols:
+ tmpfs_extent_free.kalloc_type_view_2196
+ tmpfs_extents_insert.kalloc_type_view_2156
+ tmpfs_free_links.kalloc_type_view_2499
+ tmpfs_node_add_xattr.kalloc_type_view_1898
+ tmpfs_node_add_xattr.kalloc_type_view_1908
+ tmpfs_node_remove_xattr.kalloc_type_view_1937
+ tmpfs_remove_link_origin.kalloc_type_view_2468
+ tmpfs_update_link_origin.kalloc_type_view_2445
- tmpfs_alloc_node.cold.1
- tmpfs_extent_free.kalloc_type_view_2199
- tmpfs_extents_insert.kalloc_type_view_2159
- tmpfs_free_links.kalloc_type_view_2502
- tmpfs_node_add_xattr.kalloc_type_view_1901
- tmpfs_node_add_xattr.kalloc_type_view_1911
- tmpfs_node_remove_xattr.kalloc_type_view_1940
- tmpfs_remove_link_origin.kalloc_type_view_2471
- tmpfs_update_link_origin.kalloc_type_view_2448

```
