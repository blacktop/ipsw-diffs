## libmalloc_exclaves_introspector

> `/System/Library/PrivateFrameworks/libmalloc_exclaves_introspector.framework/libmalloc_exclaves_introspector`

```diff

-812.100.31.0.0
-  __TEXT.__text: 0x43cc
-  __TEXT.__auth_stubs: 0x200
+883.0.0.0.0
+  __TEXT.__text: 0x4520
   __TEXT.__const: 0x7b
-  __TEXT.__cstring: 0x20ff
-  __TEXT.__unwind_info: 0xf8
-  __DATA_CONST.__got: 0x20
-  __DATA_CONST.__const: 0x270
-  __AUTH_CONST.__auth_got: 0x100
+  __TEXT.__cstring: 0x2191
+  __TEXT.__unwind_info: 0xf0
+  __TEXT.__auth_stubs: 0x0
+  __DATA_CONST.__const: 0x2a0
+  __DATA_CONST.__got: 0x0
   __AUTH_CONST.__const: 0x130
+  __AUTH_CONST.__auth_got: 0x108
   __DATA.__crash_info: 0x148
   __DATA.__bss: 0x11
   __DATA.__common: 0x4
   - /usr/lib/libSystem.B.dylib
-  UUID: 0DAAB8E8-0093-3140-890F-CF3F4C3384A9
-  Functions: 48
-  Symbols:   162
-  CStrings:  268
+  UUID: 9CF7F864-F315-325E-BC62-2C41C799A435
+  Functions: 47
+  Symbols:   161
+  CStrings:  270
 
Symbols:
+ _memcpy
- _xzm_segment_table_foreach
Functions:
~ _mfmi_enumerator : 576 -> 584
~ _print_mfm_arena : 992 -> 1008
~ _xzm_segment_group_segment_foreach_span : 356 -> 412
- _xzm_segment_table_foreach
~ _xzm_print_task : 5052 -> 5168
~ __xzm_introspect_enumerate : 816 -> 860
~ ____xzm_introspect_enumerate_block_invoke : 332 -> 516
~ ____xzm_introspect_enumerate_block_invoke_2 : 1404 -> 1408
~ ___xzm_print_block_invoke : 632 -> 628
~ ___xzm_print_block_invoke_2 : 512 -> 480
~ ___xzm_print_block_invoke_3 : 284 -> 268
~ ___xzm_print_block_invoke_4 : 1356 -> 1464
~ ___xzm_print_block_invoke_5 : 552 -> 560
CStrings:
+ "\n}"
+ "            \"type\": \"%s\",\n"
+ "        \"huge_alloc_counter\": \"%u\", \n"
+ "        \"is_pristine\": %d,\n"
+ "        \"on_multi_segment\": %d\n"
+ "        \"on_partial_list\": %d,\n"
+ "        \"user_slices\": %u,\n"
+ "\"bin_step\": %d, \n"
+ "\"narrow_bucketing\": %d, \n"
+ "%s    \"segment_group\": %lu, \n"
+ "BUG IN LIBMALLOC: malloc assertion \"main_address\" failed (/Library/Caches/com.apple.xbs/6409CED4-6942-4E87-A58C-A4235E3C0398/TemporaryDirectory.BWaVby/Sources/libmalloc_frameworks/src/xzone_malloc/xzone_introspect.c:960)"
+ "BUG IN LIBMALLOC: malloc assertion \"zone\" failed (/Library/Caches/com.apple.xbs/6409CED4-6942-4E87-A58C-A4235E3C0398/TemporaryDirectory.BWaVby/Sources/libmalloc_frameworks/src/xzone_malloc/xzone_introspect.c:958)"
+ "guard_object"
+ "i20@?0^{xzm_slice_s=(?={?=II{lock_exclaves_s=[4I]}C}{?=(xzm_chunk_atomic_meta_u={?=b11b11b6b1b1b1b13b20}{?=Q}Q)SSB}{?=Q{lock_exclaves_s=[4I]}b5b5b5S})(?={?=^{xzm_slice_s}^^{xzm_slice_s}}{?=^{xzm_slice_s}}[2^{xzm_slice_s}])(xzm_chunk_bits_u={?=b4b1b1b1b1}C)(?=CC)SII(xzm_xzone_slice_metadata_u=Q^{xzm_slice_s})}8I16"
+ "i24@?0Q8^v16"
+ "i32@?0Q8^{xzm_segment_s={?={?=[2Q]}{?=^{xzm_segment_s}^^{xzm_segment_s}}^{xzm_segment_group_s}IIICI^v^vQ[0{xzm_slice_s=(?={?=II{lock_exclaves_s=[4I]}C}{?=(xzm_chunk_atomic_meta_u={?=b11b11b6b1b1b1b13b20}{?=Q}Q)SSB}{?=Q{lock_exclaves_s=[4I]}b5b5b5S})(?={?=^{xzm_slice_s}^^{xzm_slice_s}}{?=^{xzm_slice_s}}[2^{xzm_slice_s}])(xzm_chunk_bits_u={?=b4b1b1b1b1}C)(?=CC)SII(xzm_xzone_slice_metadata_u=Q^{xzm_slice_s})}]}}16r*24"
+ "i44@?0Q8^{xzm_segment_s={?={?=[2Q]}{?=^{xzm_segment_s}^^{xzm_segment_s}}^{xzm_segment_group_s}IIICI^v^vQ[0{xzm_slice_s=(?={?=II{lock_exclaves_s=[4I]}C}{?=(xzm_chunk_atomic_meta_u={?=b11b11b6b1b1b1b13b20}{?=Q}Q)SSB}{?=Q{lock_exclaves_s=[4I]}b5b5b5S})(?={?=^{xzm_slice_s}^^{xzm_slice_s}}{?=^{xzm_slice_s}}[2^{xzm_slice_s}])(xzm_chunk_bits_u={?=b4b1b1b1b1}C)(?=CC)SII(xzm_xzone_slice_metadata_u=Q^{xzm_slice_s})}]}}16^{xzm_slice_s=(?={?=II{lock_exclaves_s=[4I]}C}{?=(xzm_chunk_atomic_meta_u={?=b11b11b6b1b1b1b13b20}{?=Q}Q)SSB}{?=Q{lock_exclaves_s=[4I]}b5b5b5S})(?={?=^{xzm_slice_s}^^{xzm_slice_s}}{?=^{xzm_slice_s}}[2^{xzm_slice_s}])(xzm_chunk_bits_u={?=b4b1b1b1b1}C)(?=CC)SII(xzm_xzone_slice_metadata_u=Q^{xzm_slice_s})}24I32Q36"
+ "i68@?0Q8^{xzm_segment_s={?={?=[2Q]}{?=^{xzm_segment_s}^^{xzm_segment_s}}^{xzm_segment_group_s}IIICI^v^vQ[0{xzm_slice_s=(?={?=II{lock_exclaves_s=[4I]}C}{?=(xzm_chunk_atomic_meta_u={?=b11b11b6b1b1b1b13b20}{?=Q}Q)SSB}{?=Q{lock_exclaves_s=[4I]}b5b5b5S})(?={?=^{xzm_slice_s}^^{xzm_slice_s}}{?=^{xzm_slice_s}}[2^{xzm_slice_s}])(xzm_chunk_bits_u={?=b4b1b1b1b1}C)(?=CC)SII(xzm_xzone_slice_metadata_u=Q^{xzm_slice_s})}]}}16^{xzm_slice_s=(?={?=II{lock_exclaves_s=[4I]}C}{?=(xzm_chunk_atomic_meta_u={?=b11b11b6b1b1b1b13b20}{?=Q}Q)SSB}{?=Q{lock_exclaves_s=[4I]}b5b5b5S})(?={?=^{xzm_slice_s}^^{xzm_slice_s}}{?=^{xzm_slice_s}}[2^{xzm_slice_s}])(xzm_chunk_bits_u={?=b4b1b1b1b1}C)(?=CC)SII(xzm_xzone_slice_metadata_u=Q^{xzm_slice_s})}24I32Q36(xzm_gxzone_u=^{xzm_gzone_s}^{xzm_xzone_s})44^{?=QQ}52Q60"
- "            \"type\": %u,\n"
- "        \"is_pristine\": %d\n"
- "        \"on_multi_segment\": %d,\n"
- "        \"slot_slices\": %u,\n"
- "    }\n"
- "\"%d\": {\n"
- "\"%p\": {\n"
- "%s    \"segment_group\": \"%s\", \n"
- ", "
- "BUG IN LIBMALLOC: malloc assertion \"main_address\" failed (/Library/Caches/com.apple.xbs/FB491110-B229-4C38-BCD3-DF25C3C71EE8/TemporaryDirectory.J5DpC0/Sources/libmalloc_frameworks/src/xzone_malloc/xzone_introspect.c:838)"
- "BUG IN LIBMALLOC: malloc assertion \"zone\" failed (/Library/Caches/com.apple.xbs/FB491110-B229-4C38-BCD3-DF25C3C71EE8/TemporaryDirectory.J5DpC0/Sources/libmalloc_frameworks/src/xzone_malloc/xzone_introspect.c:836)"
- "i16@?0Q8"
- "i20@?0^{xzm_slice_s=(?={?=II{lock_exclaves_s=[4I]}C}{?=(xzm_chunk_atomic_meta_u={?=b11b11b6b1b1b1b13b20}{?=Q}Q)SSB}{?=Q{lock_exclaves_s=[4I]}CCCC})(?={?=^{xzm_slice_s}^^{xzm_slice_s}}{?=^{xzm_slice_s}}[2^{xzm_slice_s}])(xzm_chunk_bits_u={?=b4b1b1b1b1}C)(?=CC)SII(xzm_xzone_slice_metadata_u=Q^{xzm_slice_s})}8I16"
- "i32@?0Q8^{xzm_segment_s={?=[2Q]}^{xzm_segment_group_s}IIIC{?=^{xzm_segment_s}^^{xzm_segment_s}}^vQ[0{xzm_slice_s=(?={?=II{lock_exclaves_s=[4I]}C}{?=(xzm_chunk_atomic_meta_u={?=b11b11b6b1b1b1b13b20}{?=Q}Q)SSB}{?=Q{lock_exclaves_s=[4I]}CCCC})(?={?=^{xzm_slice_s}^^{xzm_slice_s}}{?=^{xzm_slice_s}}[2^{xzm_slice_s}])(xzm_chunk_bits_u={?=b4b1b1b1b1}C)(?=CC)SII(xzm_xzone_slice_metadata_u=Q^{xzm_slice_s})}]}16r*24"
- "i44@?0Q8^{xzm_segment_s={?=[2Q]}^{xzm_segment_group_s}IIIC{?=^{xzm_segment_s}^^{xzm_segment_s}}^vQ[0{xzm_slice_s=(?={?=II{lock_exclaves_s=[4I]}C}{?=(xzm_chunk_atomic_meta_u={?=b11b11b6b1b1b1b13b20}{?=Q}Q)SSB}{?=Q{lock_exclaves_s=[4I]}CCCC})(?={?=^{xzm_slice_s}^^{xzm_slice_s}}{?=^{xzm_slice_s}}[2^{xzm_slice_s}])(xzm_chunk_bits_u={?=b4b1b1b1b1}C)(?=CC)SII(xzm_xzone_slice_metadata_u=Q^{xzm_slice_s})}]}16^{xzm_slice_s=(?={?=II{lock_exclaves_s=[4I]}C}{?=(xzm_chunk_atomic_meta_u={?=b11b11b6b1b1b1b13b20}{?=Q}Q)SSB}{?=Q{lock_exclaves_s=[4I]}CCCC})(?={?=^{xzm_slice_s}^^{xzm_slice_s}}{?=^{xzm_slice_s}}[2^{xzm_slice_s}])(xzm_chunk_bits_u={?=b4b1b1b1b1}C)(?=CC)SII(xzm_xzone_slice_metadata_u=Q^{xzm_slice_s})}24I32Q36"
- "i68@?0Q8^{xzm_segment_s={?=[2Q]}^{xzm_segment_group_s}IIIC{?=^{xzm_segment_s}^^{xzm_segment_s}}^vQ[0{xzm_slice_s=(?={?=II{lock_exclaves_s=[4I]}C}{?=(xzm_chunk_atomic_meta_u={?=b11b11b6b1b1b1b13b20}{?=Q}Q)SSB}{?=Q{lock_exclaves_s=[4I]}CCCC})(?={?=^{xzm_slice_s}^^{xzm_slice_s}}{?=^{xzm_slice_s}}[2^{xzm_slice_s}])(xzm_chunk_bits_u={?=b4b1b1b1b1}C)(?=CC)SII(xzm_xzone_slice_metadata_u=Q^{xzm_slice_s})}]}16^{xzm_slice_s=(?={?=II{lock_exclaves_s=[4I]}C}{?=(xzm_chunk_atomic_meta_u={?=b11b11b6b1b1b1b13b20}{?=Q}Q)SSB}{?=Q{lock_exclaves_s=[4I]}CCCC})(?={?=^{xzm_slice_s}^^{xzm_slice_s}}{?=^{xzm_slice_s}}[2^{xzm_slice_s}])(xzm_chunk_bits_u={?=b4b1b1b1b1}C)(?=CC)SII(xzm_xzone_slice_metadata_u=Q^{xzm_slice_s})}24I32Q36(xzm_gxzone_u=^{xzm_gzone_s}^{xzm_xzone_s})44^{?=QQ}52Q60"

```
