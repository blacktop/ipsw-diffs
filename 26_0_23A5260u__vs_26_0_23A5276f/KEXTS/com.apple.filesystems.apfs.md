## com.apple.filesystems.apfs

> `com.apple.filesystems.apfs`

```diff

-2632.0.15.0.1
-  __TEXT.__const: 0xa10
-  __TEXT.__cstring: 0x4bd01
-  __TEXT_EXEC.__text: 0x1571e4
+2632.0.36.0.1
+  __TEXT.__const: 0xa18
+  __TEXT.__cstring: 0x4c0a1
+  __TEXT_EXEC.__text: 0x1575ac
   __TEXT_EXEC.__auth_stubs: 0x0
   __DATA.__data: 0x640
   __DATA.__bss: 0xca8
-  __DATA_CONST.__auth_got: 0x1150
+  __DATA_CONST.__auth_got: 0x1160
   __DATA_CONST.__got: 0x198
   __DATA_CONST.__auth_ptr: 0x8
   __DATA_CONST.__mod_init_func: 0x10

   __DATA_CONST.__kalloc_type: 0x4e80
   __DATA_CONST.__kalloc_var: 0x2990
   __DATA_CONST.__assert: 0x14
-  UUID: CE1763BE-1281-3E3A-8F33-0C3E059FC742
+  UUID: 6DF5D1D5-3D11-3B11-8CC7-8E8EA183BF4F
   Functions: 2308
   Symbols:   0
-  CStrings:  6547
+  CStrings:  6558
 
Functions:
~ sub_fffffff00ad8ec90 -> sub_fffffff00addbc10 : 484 -> 632
~ _convert_file_into_dataless_fault : 2680 -> 2668
~ _container_rootmount : 3480 -> 3960
~ sub_fffffff00addf3dc -> sub_fffffff00ae2c5c4 : 152 -> 160
~ _set_parent_chain_noflush : 716 -> 712
~ _nx_resize_mark_metadata_allocated : 860 -> 884
~ _apfs_vfs_getattr : 1896 -> 1900
~ _handle_dir_stats_op : 944 -> 952
~ _fs_obj_create_name_checked : 2560 -> 2636
~ _sanitize_op_flags : 948 -> 1080
~ __setup_dir_stats_cb : 2648 -> 2720
~ _unset_dir_stats_handle_origin : 984 -> 1016
CStrings:
+ "%s:%d: %s DS_OP_ONLY_SPEC_TELEMETRY can't be specified alone\n"
+ "%s:%d: %s DS_OP_ONLY_SPEC_TELEMETRY can't be used externally\n"
+ "%s:%d: %s Speculative download hierarchy can be set only on SAF hierarchy ino origin %llu\n"
+ "%s:%d: Can't create a matching dictionary for BSD device name: %s (devvp: %p)\n"
+ "%s:%d: Can't find (IOMedia) object in IORegistry for devvp %p (%s)\n"
+ "%s:%d: Can't find APFS container parent in IORegistry for devvp %p (%s)\n"
+ "%s:%d: Can't find AppleAPFSMedia for devvp %p (%s)\n"
+ "%s:%d: Can't find IOService for BSD device name: %s (devvp: %p)\n"
+ "%s:%d: Can't find a bootable volume in container: %s, devvp: %p\n"
+ "%s:%d: Invalid AppleAPFSMedia in IORegistry (expected IOMedia with BSD major/minor, got %s), devvp %p (%s)\n"
+ "%s:%d: Invalid IORegistry object for APFS container parent (expected IOMedia with BSD major/minor, got %s), devvp %p (%s)\n"
+ "%s:%d: Invalid IOService object (expected IOMedia with BSD major/minor, got %s), devvp %p (%s)\n"
+ "%s:%d: Invalid bootable volume inside the container (pairname: %s, idx: %d)\n"
+ "2025/06/16"
+ "23:39:37"
+ "2632.0.36.0.1"
+ "Jun 16 2025"
+ "apfs-2632.0.36.0.1"
- "%s:%d: %s Speculative download hierarchy can be set only on SAF hierarchy ino %llu\n"
- "18:53:02"
- "18:53:03"
- "2025/05/30"
- "2632.0.15.0.1"
- "May 30 2025"
- "apfs-2632.0.15.0.1"

```
