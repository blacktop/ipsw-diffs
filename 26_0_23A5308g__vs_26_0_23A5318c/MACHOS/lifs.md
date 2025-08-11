## lifs

> `/System/Library/Extensions/lifs.kext/lifs`

```diff

-737.0.29.0.2
+737.2.1.0.0
   __TEXT.__os_log: 0x13b7
   __TEXT.__cstring: 0x2220
   __TEXT.__const: 0x2c0
-  __TEXT_EXEC.__text: 0x1b9e8
+  __TEXT_EXEC.__text: 0x1ba50
   __TEXT_EXEC.__auth_stubs: 0xfd0
   __DATA.__data: 0x5d0
   __DATA.__common: 0x138

   __DATA_CONST.__const: 0x16b8
   __DATA_CONST.__kalloc_type: 0xbc0
   __DATA_CONST.__kalloc_var: 0xf0
-  UUID: CBF03198-0DAD-30AC-9D58-2612E7928A3B
+  UUID: F17BF81E-057A-30D8-BB3C-0C9726F2C231
   Functions: 406
   Symbols:   3082
   CStrings:  402
Symbols:
+ lifs_fsync_internal.kalloc_type_view_3788
+ lifs_reclaim_done.kalloc_type_view_4700
+ lifs_setfsattr_done.kalloc_type_view_3716
+ lifs_vnop_reclaim.kalloc_type_view_4744
+ lifs_vnop_reclaim.kalloc_type_view_4798
- lifs_fsync_internal.kalloc_type_view_3775
- lifs_reclaim_done.kalloc_type_view_4687
- lifs_setfsattr_done.kalloc_type_view_3703
- lifs_vnop_reclaim.kalloc_type_view_4731
- lifs_vnop_reclaim.kalloc_type_view_4785
Functions:
~ _lifs_vnop_write : 1184 -> 1276
~ _lifs_vnop_getattr : 1104 -> 1116

```
