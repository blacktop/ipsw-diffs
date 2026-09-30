## lifs

> `/System/Library/Extensions/lifs.kext/lifs`

```diff

-531.120.18.0.0
+531.120.18.0.2
   __TEXT.__os_log: 0x12f9
   __TEXT.__cstring: 0x217f
   __TEXT.__const: 0x2c0
-  __TEXT_EXEC.__text: 0x1b138
+  __TEXT_EXEC.__text: 0x1b14c
   __TEXT_EXEC.__auth_stubs: 0xfa0
   __DATA.__data: 0x5d0
   __DATA.__common: 0x138
Symbols:
+ lifs_fsync_internal.kalloc_type_view_3703
+ lifs_reclaim_done.kalloc_type_view_4615
+ lifs_setfsattr_done.kalloc_type_view_3634
+ lifs_vnop_reclaim.kalloc_type_view_4659
+ lifs_vnop_reclaim.kalloc_type_view_4713
- lifs_fsync_internal.kalloc_type_view_3694
- lifs_reclaim_done.kalloc_type_view_4606
- lifs_setfsattr_done.kalloc_type_view_3625
- lifs_vnop_reclaim.kalloc_type_view_4650
- lifs_vnop_reclaim.kalloc_type_view_4704

```
