## libmalloc_exclaves_introspector

> `/System/Library/PrivateFrameworks/libmalloc_exclaves_introspector.framework/libmalloc_exclaves_introspector`

```diff

-715.120.13.0.0
-  __TEXT.__text: 0x3af4
+778.0.0.0.0
+  __TEXT.__text: 0x3d08
   __TEXT.__auth_stubs: 0x200
   __TEXT.__const: 0x7b
-  __TEXT.__cstring: 0x1ab9
+  __TEXT.__cstring: 0x1c93
   __TEXT.__unwind_info: 0xf0
   __DATA_CONST.__got: 0x20
-  __DATA_CONST.__const: 0x240
+  __DATA_CONST.__const: 0x248
   __AUTH_CONST.__auth_got: 0x100
   __AUTH_CONST.__const: 0x130
-  __DATA.__crash_info: 0x40
+  __DATA.__crash_info: 0x148
   __DATA.__bss: 0x11
   __DATA.__common: 0x4
   - /usr/lib/libSystem.B.dylib
-  UUID: 725392EC-E48C-3703-9196-48CA9FFAB0BD
+  UUID: A1E89624-7D02-36A9-90DC-1776BD40D1B5
   Functions: 47
   Symbols:   162
-  CStrings:  207
+  CStrings:  227
 
Symbols:
+ ___block_descriptor_tmp.152
+ ___block_descriptor_tmp.177
+ ___block_descriptor_tmp.179
+ ___block_descriptor_tmp.35
+ ___block_descriptor_tmp.48
- ___block_descriptor_tmp.134
- ___block_descriptor_tmp.159
- ___block_descriptor_tmp.161
- ___block_descriptor_tmp.32
- ___block_descriptor_tmp.45
Functions:
~ _xzm_ptr_in_use_enumerator : 564 -> 568
~ _xzm_print_task : 3540 -> 4012
~ ___xzm_ptr_in_use_enumerator_block_invoke_3 : 256 -> 272
~ ____xzm_introspect_enumerate_block_invoke_2 : 1164 -> 1184
~ ___xzm_print_block_invoke_4 : 1008 -> 1028
CStrings:
+ "                \"operations\": %lu,\n"
+ "        \"chunk_count\": %llu, \n"
+ "        \"direction\": \"%s\"\n"
+ "        \"front\": %d, \n"
+ "        \"list_config\": \"%s\",\n"
+ "        \"range_group\": \"%p\", \n"
+ "        \"remaining\": %zu, \n"
+ "        \"skip_addr\": \"%p\", \n"
+ "        \"skip_size\": %zu, \n"
+ "    \"busy\": %llu, \n"
+ "    \"head\": %llu, \n"
+ "    \"last_sample_abs\": %llu, \n"
+ "    \"reclaimable_bytes\": %llu, \n"
+ "    \"reclaimable_bytes_min\": %llu, \n"
+ "    \"sampling_period_abs\": %llu, \n"
+ "    \"tail\": %llu \n"
+ "\"allocation_front_count\": %u, \n"
+ "\"chunk_threshold\": %u, \n"
+ "\"deallocate_segment\": %s, \n"
+ "\"initial_slot_config\": %d, \n"
+ "\"max_list_config\": %d, \n"
+ "\"segment_group_front_count\": %u, \n"
+ "\"slot_initial_threshold\": %u, \n"
+ "\"use_early_alloc\": %s, \n"
+ "BUG IN LIBMALLOC: malloc assertion \"main_address\" failed (/Library/Caches/com.apple.xbs/Sources/libmalloc_frameworks/src/xzone/xzone_introspect.c:784)"
+ "BUG IN LIBMALLOC: malloc assertion \"zone\" failed (/Library/Caches/com.apple.xbs/Sources/libmalloc_frameworks/src/xzone/xzone_introspect.c:782)"
+ "down"
+ "i68@?0Q8^{xzm_segment_s={?=[2Q]}^{xzm_segment_group_s}IIIC{?=^{xzm_segment_s}^^{xzm_segment_s}}^vQ[256(xzm_xzone_slice_metadata_u=Q^{xzm_slice_s})][256{xzm_slice_s=(?={?=II{lock_exclaves_s=[4I]}C}{?=(xzm_chunk_atomic_meta_u={?=b11b11b6b1b1b1b13b20}{?=Q}Q)SS})(?={?=^{xzm_slice_s}^^{xzm_slice_s}}{?=^{xzm_slice_s}}[2^{xzm_slice_s}])(xzm_chunk_bits_u={?=b4b1b1b1b1}C)CSII}]}16^{xzm_slice_s=(?={?=II{lock_exclaves_s=[4I]}C}{?=(xzm_chunk_atomic_meta_u={?=b11b11b6b1b1b1b13b20}{?=Q}Q)SS})(?={?=^{xzm_slice_s}^^{xzm_slice_s}}{?=^{xzm_slice_s}}[2^{xzm_slice_s}])(xzm_chunk_bits_u={?=b4b1b1b1b1}C)CSII}24I32Q36^{xzm_xzone_s=(?={?={?=^{xzm_slice_s}}{?=^{xzm_slice_s}}{?=^{xzm_slice_s}}^{xzm_slice_s}I{lock_exclaves_s=[4I]}}{?=(xzm_chunk_list_head_u=(?={?=b47b16b1}{?=b47b10b6b1})Q)(xzm_chunk_list_head_u=(?={?=b47b16b1}{?=b47b10b6b1})Q)(xzm_chunk_list_head_u=(?={?=b47b16b1}{?=b47b10b6b1})Q)(xzm_chunk_list_head_u=(?={?=b47b16b1}{?=b47b10b6b1})Q)})SCCQQIIQCSCCCb1{xzm_xzone_guard_config_s=CC}}44^{?=QQ}52Q60"
+ "pointer"
+ "small_freelist_chunk"
+ "up"
- "        \"busy\": %llu, \n"
- "        \"head\": %llu, \n"
- "        \"remaining\": %zu\n"
- "        \"tail\": %llu \n"
- "    \"indices\": { \n"
- "    \"last_accounting_given_to_kernel\": %llu, \n"
- "    \"va_in_buffer\": %llu, \n"
- "    }, \n"
- "BUG IN LIBMALLOC: malloc assertion \"main_address\" failed (/Library/Caches/com.apple.xbs/Sources/libmalloc_frameworks/src/xzone/xzone_introspect.c:781)"
- "BUG IN LIBMALLOC: malloc assertion \"zone\" failed (/Library/Caches/com.apple.xbs/Sources/libmalloc_frameworks/src/xzone/xzone_introspect.c:779)"
- "i68@?0Q8^{xzm_segment_s={?=[2Q]}^{xzm_segment_group_s}IIIC{?=^{xzm_segment_s}^^{xzm_segment_s}}^vQ[256(xzm_xzone_slice_metadata_u=Q^{xzm_slice_s})][256{xzm_slice_s=(?={?=II{lock_exclaves_s=[4I]}C}{?=(xzm_chunk_atomic_meta_u={?=b11b11b6b1b1b1b13b20}{?=Q}Q)SS})(?={?=^{xzm_slice_s}^^{xzm_slice_s}}{?=^{xzm_slice_s}}[2^{xzm_slice_s}])(xzm_chunk_bits_u={?=b4b1b1b1b1}C)CSII}]}16^{xzm_slice_s=(?={?=II{lock_exclaves_s=[4I]}C}{?=(xzm_chunk_atomic_meta_u={?=b11b11b6b1b1b1b13b20}{?=Q}Q)SS})(?={?=^{xzm_slice_s}^^{xzm_slice_s}}{?=^{xzm_slice_s}}[2^{xzm_slice_s}])(xzm_chunk_bits_u={?=b4b1b1b1b1}C)CSII}24I32Q36^{xzm_xzone_s=(?={?={?=^{xzm_slice_s}}{?=^{xzm_slice_s}}{?=^{xzm_slice_s}}^{xzm_slice_s}I{lock_exclaves_s=[4I]}}{?=(xzm_chunk_list_head_u=(?={?=b47b16b1}{?=b47b10b6b1})Q)(xzm_chunk_list_head_u=(?={?=b47b16b1}{?=b47b10b6b1})Q)(xzm_chunk_list_head_u=(?={?=b47b16b1}{?=b47b10b6b1})Q)(xzm_chunk_list_head_u=(?={?=b47b16b1}{?=b47b10b6b1})Q)(xzm_chunk_list_head_u=(?={?=b47b16b1}{?=b47b10b6b1})Q)})SCQQIICSCCb1{xzm_xzone_guard_config_s=CC}}44^{?=QQ}52Q60"

```
