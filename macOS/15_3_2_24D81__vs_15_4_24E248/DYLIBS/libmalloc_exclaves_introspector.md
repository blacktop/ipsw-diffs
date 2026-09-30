## libmalloc_exclaves_introspector

> `/System/Library/PrivateFrameworks/libmalloc_exclaves_introspector.framework/Versions/A/libmalloc_exclaves_introspector`

```diff

-657.80.3.0.0
-  __TEXT.__text: 0x3a90
+715.100.22.0.0
+  __TEXT.__text: 0x3e2c
   __TEXT.__auth_stubs: 0x210
   __TEXT.__const: 0x83
-  __TEXT.__cstring: 0x173a
+  __TEXT.__cstring: 0x1b45
   __TEXT.__unwind_info: 0x108
   __DATA_CONST.__got: 0x20
-  __DATA_CONST.__const: 0x120
+  __DATA_CONST.__const: 0x128
   __AUTH_CONST.__auth_got: 0x108
   __AUTH_CONST.__const: 0x280
   __DATA.__crash_info: 0x40
   __DATA.__bss: 0x11
   __DATA.__common: 0x4
   - /usr/lib/libSystem.B.dylib
-  UUID: 7FE3D870-141D-37F8-8D04-A47220F04F7B
+  UUID: 8D8AB8A6-AA64-3834-A1A0-708755547A75
   Functions: 57
   Symbols:   123
-  CStrings:  175
+  CStrings:  207
 
Symbols:
+ __block_descriptor_tmp.136
+ __block_descriptor_tmp.164
+ __block_descriptor_tmp.169
+ __block_descriptor_tmp.46
+ __xzm_print_block_invoke.131
+ __xzm_print_block_invoke.137
+ __xzm_print_block_invoke.165
- __block_descriptor_tmp.107
- __block_descriptor_tmp.133
- __block_descriptor_tmp.138
- __block_descriptor_tmp.44
- __xzm_print_block_invoke.102
- __xzm_print_block_invoke.108
- __xzm_print_block_invoke.134
Functions:
~ _mfmi_enumerator : 584 -> 576
~ _mfmi_good_size : 20 -> 28
~ _mfmi_locked : 56 -> 60
~ _print_mfm_arena : 984 -> 992
~ _xzm_segment_group_segment_foreach_span : 360 -> 356
~ _xzm_print_task : 2932 -> 3540
~ __xzm_introspect_enumerate : 752 -> 768
~ ___xzm_ptr_in_use_enumerator_block_invoke : 80 -> 92
~ ___xzm_ptr_in_use_enumerator_block_invoke_3 : 248 -> 256
~ ___xzm_ptr_in_use_enumerator_block_invoke_4 : 76 -> 112
~ ____xzm_introspect_enumerate_block_invoke : 268 -> 284
~ ____xzm_introspect_enumerate_block_invoke_2 : 1088 -> 1164
~ __xzm_print_block_invoke.33 : 452 -> 504
~ __xzm_print_block_invoke.102 -> __xzm_print_block_invoke.131 : 288 -> 284
~ __xzm_print_block_invoke.108 -> __xzm_print_block_invoke.137 : 956 -> 1008
~ __xzm_print_block_invoke.134 -> __xzm_print_block_invoke.165 : 504 -> 556
~ _malloc_vreport : 896 -> 892
~ __malloc_put : 416 -> 412
CStrings:
+ " \n"
+ "            \"address\": \"%p\", \n"
+ "            \"behavior\": %u, \n"
+ "            \"id\": %u, \n"
+ "            \"size\": %u, \n"
+ "        \"batch_count\": %u, \n"
+ "        \"busy\": %llu, \n"
+ "        \"early_budget\": %u, \n"
+ "        \"head\": %llu, \n"
+ "        \"segment_group_id\": %d, \n"
+ "        \"slice_metadata\": \"%p\", \n"
+ "        \"tail\": %llu \n"
+ "        { \n"
+ "        }"
+ "    \"buffer_len\": %llu, \n"
+ "    \"entries\": [ \n"
+ "    \"indices\": { \n"
+ "    \"last_accounting_given_to_kernel\": %llu, \n"
+ "    \"max_len\": %llu, \n"
+ "    \"va_in_buffer\": %llu, \n"
+ "    ] \n"
+ "    }, \n"
+ "\"batch_size\": %u, \n"
+ "\"defer_small\": %s, \n"
+ "\"defer_tiny\": %s, \n"
+ "\"ptr_bucket_count\": %d, \n"
+ "\"range_group_count\": %u, \n"
+ "\"reclaim_buffer\": { \n"
+ "\"segment_group_count\": %u, \n"
+ "\"segment_group_ids_count\": %u, \n"
+ "%s    \"reclaim_id\": %llu, \n"
+ "%s    \"reclaim_id\": -1, \n"
+ "BUG IN LIBMALLOC: malloc assertion \"main_address\" failed (/AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/libmalloc_frameworks/src/xzone/xzone_introspect.c:781)"
+ "BUG IN LIBMALLOC: malloc assertion \"zone\" failed (/AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/libmalloc_frameworks/src/xzone/xzone_introspect.c:779)"
+ "i20@?0^{xzm_slice_s=(?={?=II{lock_exclaves_s=[4I]}C}{?=(xzm_chunk_atomic_meta_u={?=b11b11b6b1b1b1b13b20}{?=Q}Q)SS})(?={?=^{xzm_slice_s}^^{xzm_slice_s}}{?=^{xzm_slice_s}}[2^{xzm_slice_s}])(xzm_chunk_bits_u={?=b4b1b1b1b1}C)CSII}8I16"
+ "i32@?0Q8^{xzm_segment_s={?=[2Q]}^{xzm_segment_group_s}IIIC{?=^{xzm_segment_s}^^{xzm_segment_s}}^vQ[256(xzm_xzone_slice_metadata_u=Q^{xzm_slice_s})][256{xzm_slice_s=(?={?=II{lock_exclaves_s=[4I]}C}{?=(xzm_chunk_atomic_meta_u={?=b11b11b6b1b1b1b13b20}{?=Q}Q)SS})(?={?=^{xzm_slice_s}^^{xzm_slice_s}}{?=^{xzm_slice_s}}[2^{xzm_slice_s}])(xzm_chunk_bits_u={?=b4b1b1b1b1}C)CSII}]}16r*24"
+ "i44@?0Q8^{xzm_segment_s={?=[2Q]}^{xzm_segment_group_s}IIIC{?=^{xzm_segment_s}^^{xzm_segment_s}}^vQ[256(xzm_xzone_slice_metadata_u=Q^{xzm_slice_s})][256{xzm_slice_s=(?={?=II{lock_exclaves_s=[4I]}C}{?=(xzm_chunk_atomic_meta_u={?=b11b11b6b1b1b1b13b20}{?=Q}Q)SS})(?={?=^{xzm_slice_s}^^{xzm_slice_s}}{?=^{xzm_slice_s}}[2^{xzm_slice_s}])(xzm_chunk_bits_u={?=b4b1b1b1b1}C)CSII}]}16^{xzm_slice_s=(?={?=II{lock_exclaves_s=[4I]}C}{?=(xzm_chunk_atomic_meta_u={?=b11b11b6b1b1b1b13b20}{?=Q}Q)SS})(?={?=^{xzm_slice_s}^^{xzm_slice_s}}{?=^{xzm_slice_s}}[2^{xzm_slice_s}])(xzm_chunk_bits_u={?=b4b1b1b1b1}C)CSII}24I32Q36"
+ "i68@?0Q8^{xzm_segment_s={?=[2Q]}^{xzm_segment_group_s}IIIC{?=^{xzm_segment_s}^^{xzm_segment_s}}^vQ[256(xzm_xzone_slice_metadata_u=Q^{xzm_slice_s})][256{xzm_slice_s=(?={?=II{lock_exclaves_s=[4I]}C}{?=(xzm_chunk_atomic_meta_u={?=b11b11b6b1b1b1b13b20}{?=Q}Q)SS})(?={?=^{xzm_slice_s}^^{xzm_slice_s}}{?=^{xzm_slice_s}}[2^{xzm_slice_s}])(xzm_chunk_bits_u={?=b4b1b1b1b1}C)CSII}]}16^{xzm_slice_s=(?={?=II{lock_exclaves_s=[4I]}C}{?=(xzm_chunk_atomic_meta_u={?=b11b11b6b1b1b1b13b20}{?=Q}Q)SS})(?={?=^{xzm_slice_s}^^{xzm_slice_s}}{?=^{xzm_slice_s}}[2^{xzm_slice_s}])(xzm_chunk_bits_u={?=b4b1b1b1b1}C)CSII}24I32Q36^{xzm_xzone_s=(?={?={?=^{xzm_slice_s}}{?=^{xzm_slice_s}}{?=^{xzm_slice_s}}^{xzm_slice_s}I{lock_exclaves_s=[4I]}}{?=(xzm_chunk_list_head_u=(?={?=b47b16b1}{?=b47b10b6b1})Q)(xzm_chunk_list_head_u=(?={?=b47b16b1}{?=b47b10b6b1})Q)(xzm_chunk_list_head_u=(?={?=b47b16b1}{?=b47b10b6b1})Q)(xzm_chunk_list_head_u=(?={?=b47b16b1}{?=b47b10b6b1})Q)(xzm_chunk_list_head_u=(?={?=b47b16b1}{?=b47b10b6b1})Q)})SCQQIICSCCb1{xzm_xzone_guard_config_s=CC}}44^{?=QQ}52Q60"
+ "thread cache slab"
- "\"defer_xzones\": %s, \n"
- "BUG IN LIBMALLOC: malloc assertion \"main_address\" failed (/AppleInternal/Library/BuildRoots/d187755d-b9a3-11ef-83e5-aabfac210453/Library/Caches/com.apple.xbs/Sources/libmalloc_frameworks/src/xzone/xzone_introspect.c:559)"
- "BUG IN LIBMALLOC: malloc assertion \"zone\" failed (/AppleInternal/Library/BuildRoots/d187755d-b9a3-11ef-83e5-aabfac210453/Library/Caches/com.apple.xbs/Sources/libmalloc_frameworks/src/xzone/xzone_introspect.c:557)"
- "i20@?0^{xzm_slice_s=(?={?=II{lock_exclaves_s=[4I]}C}(xzm_chunk_atomic_meta_u={?=b11b11b6b1b1b1b7b13b13}{?=Q}Q))(?={?=^{xzm_slice_s}^^{xzm_slice_s}}{?=^{xzm_slice_s}}[2^{xzm_slice_s}])(xzm_chunk_bits_u={?=b4b1b1b1b1}C)CSII}8I16"
- "i32@?0Q8^{xzm_segment_s={?=[2Q]}^{xzm_segment_group_s}IIIC{?=^{xzm_segment_s}^^{xzm_segment_s}}Q^v[256Q][256{xzm_slice_s=(?={?=II{lock_exclaves_s=[4I]}C}(xzm_chunk_atomic_meta_u={?=b11b11b6b1b1b1b7b13b13}{?=Q}Q))(?={?=^{xzm_slice_s}^^{xzm_slice_s}}{?=^{xzm_slice_s}}[2^{xzm_slice_s}])(xzm_chunk_bits_u={?=b4b1b1b1b1}C)CSII}]}16r*24"
- "i44@?0Q8^{xzm_segment_s={?=[2Q]}^{xzm_segment_group_s}IIIC{?=^{xzm_segment_s}^^{xzm_segment_s}}Q^v[256Q][256{xzm_slice_s=(?={?=II{lock_exclaves_s=[4I]}C}(xzm_chunk_atomic_meta_u={?=b11b11b6b1b1b1b7b13b13}{?=Q}Q))(?={?=^{xzm_slice_s}^^{xzm_slice_s}}{?=^{xzm_slice_s}}[2^{xzm_slice_s}])(xzm_chunk_bits_u={?=b4b1b1b1b1}C)CSII}]}16^{xzm_slice_s=(?={?=II{lock_exclaves_s=[4I]}C}(xzm_chunk_atomic_meta_u={?=b11b11b6b1b1b1b7b13b13}{?=Q}Q))(?={?=^{xzm_slice_s}^^{xzm_slice_s}}{?=^{xzm_slice_s}}[2^{xzm_slice_s}])(xzm_chunk_bits_u={?=b4b1b1b1b1}C)CSII}24I32Q36"
- "i68@?0Q8^{xzm_segment_s={?=[2Q]}^{xzm_segment_group_s}IIIC{?=^{xzm_segment_s}^^{xzm_segment_s}}Q^v[256Q][256{xzm_slice_s=(?={?=II{lock_exclaves_s=[4I]}C}(xzm_chunk_atomic_meta_u={?=b11b11b6b1b1b1b7b13b13}{?=Q}Q))(?={?=^{xzm_slice_s}^^{xzm_slice_s}}{?=^{xzm_slice_s}}[2^{xzm_slice_s}])(xzm_chunk_bits_u={?=b4b1b1b1b1}C)CSII}]}16^{xzm_slice_s=(?={?=II{lock_exclaves_s=[4I]}C}(xzm_chunk_atomic_meta_u={?=b11b11b6b1b1b1b7b13b13}{?=Q}Q))(?={?=^{xzm_slice_s}^^{xzm_slice_s}}{?=^{xzm_slice_s}}[2^{xzm_slice_s}])(xzm_chunk_bits_u={?=b4b1b1b1b1}C)CSII}24I32Q36^{xzm_xzone_s=(?={?={?=^{xzm_slice_s}}{?=^{xzm_slice_s}}{?=^{xzm_slice_s}}{lock_exclaves_s=[4I]}}{?=(xzm_chunk_list_head_u={?=b47b16b1}Q)(xzm_chunk_list_head_u={?=b47b16b1}Q)(xzm_chunk_list_head_u={?=b47b16b1}Q)(xzm_chunk_list_head_u={?=b47b16b1}Q)})S^{xzm_segment_group_s}QQIICSCCb1{xzm_xzone_guard_config_s=CC}}44^{?=QQ}52Q60"

```
