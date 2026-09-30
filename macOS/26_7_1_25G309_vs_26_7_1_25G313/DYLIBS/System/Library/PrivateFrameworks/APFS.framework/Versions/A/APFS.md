## APFS

> `/System/Library/PrivateFrameworks/APFS.framework/Versions/A/APFS`

```diff

-2811.160.7.701.3
-  __TEXT.__text: 0x58c1c
+2811.160.7.702.4
+  __TEXT.__text: 0x58e34
   __TEXT.__auth_stubs: 0xdc0
   __TEXT.__const: 0x85b0
-  __TEXT.__cstring: 0xec97
+  __TEXT.__cstring: 0xecaa
   __TEXT.__oslogstring: 0x17be
   __TEXT.__gcc_except_tab: 0x1c
-  __TEXT.__unwind_info: 0x9f0
+  __TEXT.__unwind_info: 0x9f8
   __DATA_CONST.__got: 0x88
   __DATA_CONST.__const: 0x520
   __AUTH_CONST.__auth_got: 0x6e8

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libc++.1.dylib
   - /usr/lib/libutil.dylib
-  Functions: 940
-  Symbols:   1199
-  CStrings:  1475
+  Functions: 941
+  Symbols:   1200
+  CStrings:  1476
 
Symbols:
+ _btree_node_val_space_total
Functions:
+ _btree_node_val_space_total
~ _btree_node_compact : 1188 -> 1536
~ _spaceman_iterate_free_extents_internal : 5896 -> 5932
~ _spaceman_alloc_iterate_chunks : 4108 -> 4184
~ _spaceman_modify_bits : 3536 -> 3512
~ _jobj_validate_key_val : 580 -> 604
CStrings:
+ "2811.160.7.702.4"
+ "btree_node_compact"
- "2811.160.7.701.3"
```
