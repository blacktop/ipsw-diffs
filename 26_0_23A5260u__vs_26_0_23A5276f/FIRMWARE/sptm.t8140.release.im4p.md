## sptm.t8140.release.im4p

> `sptm.t8140.release.im4p`

```diff

-611.0.9.0.0
+611.0.16.0.0
   __TEXT.__const: 0xa00
-  __TEXT.__cstring: 0x10bcc
+  __TEXT.__cstring: 0x10ce2
   __TEXT.__binname: 0x40
   __TEXT.__chain_starts: 0x24
-  __DATA_CONST.__const: 0x73c0
-  __LATE_CONST.__late_const: 0x65878
-  __TEXT_EXEC.__text: 0x570d4
+  __DATA_CONST.__const: 0x73d0
+  __LATE_CONST.__late_const: 0x65880
+  __TEXT_EXEC.__text: 0x574c4
   __LAST.__pinst: 0x8
   __DATA.__auth_ptr: 0x18
   __DATA.__data: 0xe
   __DATA.__bss: 0x5e28
   __DATA.__common: 0x58d0
   __BOOTDATA.__data: 0x14000
-  UUID: 49779904-55CE-3CFB-9BB5-3DC4968F5EB1
-  Functions: 357
+  UUID: 9F0C973D-B934-3F2D-BC18-B4E3F1DE55D9
+  Functions: 360
   Symbols:   1
-  CStrings:  2137
+  CStrings:  2149
 
CStrings:
+ "%s: %d is not a valid type ID (valid type IDs are 0-%d)"
+ "%s: Attempted to update refcnts on a non-cpu-page: %s"
+ "%s: Unexpected [fte->type] while retyping page: %s"
+ "%s: Unexpected [new_type] while retyping page: %s"
+ "-1"
+ "SPTM-611.0.16|2025-06-13:22:37:57.950015|"
+ "VIOLATION_INVALID_DT_RANGE"
+ "VIOLATION_INVALID_IO_PADDR"
+ "VIOLATION_INVALID_RESTRICTED_IO_PADDR"
+ "cpu_root_table_user_address_space_set_up"
+ "cpu_root_table_user_address_space_tear_down"
+ "mapping-enforcement-mode"
+ "num_pages"
+ "propSize"
+ "prop_name"
+ "prop_offset"
+ "sptm_io.c"
+ "type_id_to_string"
- "%s: Attempted to update refcnts on a non-cpu-page: %d"
- "%s: Unexpected [fte->type] while retyping page %d"
- "%s: Unexpected [new_type] while retyping page %d"
- "SPTM-611.0.9|2025-05-30:18:56:54.012991|"
- "user_address_space_set_up"
- "user_address_space_tear_down"

```
