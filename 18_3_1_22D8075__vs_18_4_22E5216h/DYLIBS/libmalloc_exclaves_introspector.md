## libmalloc_exclaves_introspector

> `/System/Library/PrivateFrameworks/libmalloc_exclaves_introspector.framework/libmalloc_exclaves_introspector`

```diff

-657.80.3.0.0
-  __TEXT.__text: 0x3a60
+715.100.19.502.1
+  __TEXT.__text: 0x3af4
   __TEXT.__auth_stubs: 0x200
   __TEXT.__const: 0x7b
-  __TEXT.__cstring: 0x18d6
+  __TEXT.__cstring: 0x1ab9
   __TEXT.__unwind_info: 0xf0
   __DATA_CONST.__got: 0x20
-  __DATA_CONST.__const: 0x238
+  __DATA_CONST.__const: 0x240
   __AUTH_CONST.__auth_got: 0x100
   __AUTH_CONST.__auth_ptr: 0x8
   __AUTH_CONST.__const: 0x130

   - /usr/lib/libSystem.B.dylib
   Functions: 47
   Symbols:   93
-  CStrings:  199
+  CStrings:  207
 
CStrings:
+ "            \"id\": %u, \n"
+ "        \"batch_count\": %u, \n"
+ "        \"early_budget\": %u, \n"
+ "        \"segment_group_id\": %d, \n"
+ "        \"slice_metadata\": \"%p\", \n"
+ "    \"max_len\": %llu, \n"
+ "\"batch_size\": %u, \n"
+ "\"defer_small\": %s, \n"
+ "\"defer_tiny\": %s, \n"
+ "\"ptr_bucket_count\": %d, \n"
+ "\"range_group_count\": %u, \n"
+ "\"segment_group_count\": %u, \n"
+ "\"segment_group_ids_count\": %u, \n"
+ "BUG IN LIBMALLOC: malloc assertion \"main_address\" failed (/Library/Caches/com.apple.xbs/Sources/libmalloc_frameworks/src/xzone/xzone_introspect.c:781)"
+ "BUG IN LIBMALLOC: malloc assertion \"zone\" failed (/Library/Caches/com.apple.xbs/Sources/libmalloc_frameworks/src/xzone/xzone_introspect.c:779)"
+ "i20@?0^{xzm_slice_s=(?={?=II{lock_exclaves_s=[4I]}C}{?=(xzm_chunk_atomic_meta_u={?=b11b11b6b1b1b1b13b20}{?=Q}Q)SS})(?={?=^{xzm_slice_s}^^{xzm_slice_s}}{?=^{xzm_slice_s}}[2^{xzm_slice_s}])(xzm_chunk_bits_u={?=b4b1b1b1b1}C)CSII}8I16"
+ "i32@?0Q8^{xzm_segment_s={?=[2Q]}^{xzm_segment_group_s}IIIC{?=^{xzm_segment_s}^^{xzm_segment_s}}^vQ[256(xzm_xzone_slice_metadata_u=Q^{xzm_slice_s})][256{xzm_slice_s=(?={?=II{lock_exclaves_s=[4I]}C}{?=(xzm_chunk_atomic_meta_u={?=b11b11b6b1b1b1b13b20}{?=Q}Q)SS})(?={?=^{xzm_slice_s}^^{xzm_slice_s}}{?=^{xzm_slice_s}}[2^{xzm_slice_s}])(xzm_chunk_bits_u={?=b4b1b1b1b1}C)CSII}]}16r*24"
+ "i44@?0Q8^{xzm_segment_s={?=[2Q]}^{xzm_segment_group_s}IIIC{?=^{xzm_segment_s}^^{xzm_segment_s}}^vQ[256(xzm_xzone_slice_metadata_u=Q^{xzm_slice_s})][256{xzm_slice_s=(?={?=II{lock_exclaves_s=[4I]}C}{?=(xzm_chunk_atomic_meta_u={?=b11b11b6b1b1b1b13b20}{?=Q}Q)SS})(?={?=^{xzm_slice_s}^^{xzm_slice_s}}{?=^{xzm_slice_s}}[2^{xzm_slice_s}])(xzm_chunk_bits_u={?=b4b1b1b1b1}C)CSII}]}16^{xzm_slice_s=(?={?=II{lock_exclaves_s=[4I]}C}{?=(xzm_chunk_atomic_meta_u={?=b11b11b6b1b1b1b13b20}{?=Q}Q)SS})(?={?=^{xzm_slice_s}^^{xzm_slice_s}}{?=^{xzm_slice_s}}[2^{xzm_slice_s}])(xzm_chunk_bits_u={?=b4b1b1b1b1}C)CSII}24I32Q36"
+ "i68@?0Q8^{xzm_segment_s={?=[2Q]}^{xzm_segment_group_s}IIIC{?=^{xzm_segment_s}^^{xzm_segment_s}}^vQ[256(xzm_xzone_slice_metadata_u=Q^{xzm_slice_s})][256{xzm_slice_s=(?={?=II{lock_exclaves_s=[4I]}C}{?=(xzm_chunk_atomic_meta_u={?=b11b11b6b1b1b1b13b20}{?=Q}Q)SS})(?={?=^{xzm_slice_s}^^{xzm_slice_s}}{?=^{xzm_slice_s}}[2^{xzm_slice_s}])(xzm_chunk_bits_u={?=b4b1b1b1b1}C)CSII}]}16^{xzm_slice_s=(?={?=II{lock_exclaves_s=[4I]}C}{?=(xzm_chunk_atomic_meta_u={?=b11b11b6b1b1b1b13b20}{?=Q}Q)SS})(?={?=^{xzm_slice_s}^^{xzm_slice_s}}{?=^{xzm_slice_s}}[2^{xzm_slice_s}])(xzm_chunk_bits_u={?=b4b1b1b1b1}C)CSII}24I32Q36^{xzm_xzone_s=(?={?={?=^{xzm_slice_s}}{?=^{xzm_slice_s}}{?=^{xzm_slice_s}}^{xzm_slice_s}I{lock_exclaves_s=[4I]}}{?=(xzm_chunk_list_head_u=(?={?=b47b16b1}{?=b47b10b6b1})Q)(xzm_chunk_list_head_u=(?={?=b47b16b1}{?=b47b10b6b1})Q)(xzm_chunk_list_head_u=(?={?=b47b16b1}{?=b47b10b6b1})Q)(xzm_chunk_list_head_u=(?={?=b47b16b1}{?=b47b10b6b1})Q)(xzm_chunk_list_head_u=(?={?=b47b16b1}{?=b47b10b6b1})Q)})SCQQIICSCCb1{xzm_xzone_guard_config_s=CC}}44^{?=QQ}52Q60"
+ "thread cache slab"
- "            \"flags\": \"0x%x\" \n"
- "            \"index\": %u, \n"
- "        \"reclaim_id\": %llu, \n"
- "        \"reclaim_id\": -1, \n"
- "    \"buffer\": \"%p\", \n"
- "\"defer_xzones\": %s, \n"
- "BUG IN LIBMALLOC: malloc assertion \"main_address\" failed (/Library/Caches/com.apple.xbs/Sources/libmalloc_frameworks/src/xzone/xzone_introspect.c:559)"
- "BUG IN LIBMALLOC: malloc assertion \"zone\" failed (/Library/Caches/com.apple.xbs/Sources/libmalloc_frameworks/src/xzone/xzone_introspect.c:557)"
- "i20@?0^{xzm_slice_s=(?={?=II{lock_exclaves_s=[4I]}C}(xzm_chunk_atomic_meta_u={?=b11b11b6b1b1b1b7b13b13}{?=Q}Q))(?={?=^{xzm_slice_s}^^{xzm_slice_s}}{?=^{xzm_slice_s}}[2^{xzm_slice_s}])(xzm_chunk_bits_u={?=b4b1b1b1b1}C)CSII}8I16"
- "i32@?0Q8^{xzm_segment_s={?=[2Q]}^{xzm_segment_group_s}IIIC{?=^{xzm_segment_s}^^{xzm_segment_s}}Q^v[256Q][256{xzm_slice_s=(?={?=II{lock_exclaves_s=[4I]}C}(xzm_chunk_atomic_meta_u={?=b11b11b6b1b1b1b7b13b13}{?=Q}Q))(?={?=^{xzm_slice_s}^^{xzm_slice_s}}{?=^{xzm_slice_s}}[2^{xzm_slice_s}])(xzm_chunk_bits_u={?=b4b1b1b1b1}C)CSII}]}16r*24"
- "i44@?0Q8^{xzm_segment_s={?=[2Q]}^{xzm_segment_group_s}IIIC{?=^{xzm_segment_s}^^{xzm_segment_s}}Q^v[256Q][256{xzm_slice_s=(?={?=II{lock_exclaves_s=[4I]}C}(xzm_chunk_atomic_meta_u={?=b11b11b6b1b1b1b7b13b13}{?=Q}Q))(?={?=^{xzm_slice_s}^^{xzm_slice_s}}{?=^{xzm_slice_s}}[2^{xzm_slice_s}])(xzm_chunk_bits_u={?=b4b1b1b1b1}C)CSII}]}16^{xzm_slice_s=(?={?=II{lock_exclaves_s=[4I]}C}(xzm_chunk_atomic_meta_u={?=b11b11b6b1b1b1b7b13b13}{?=Q}Q))(?={?=^{xzm_slice_s}^^{xzm_slice_s}}{?=^{xzm_slice_s}}[2^{xzm_slice_s}])(xzm_chunk_bits_u={?=b4b1b1b1b1}C)CSII}24I32Q36"
- "i68@?0Q8^{xzm_segment_s={?=[2Q]}^{xzm_segment_group_s}IIIC{?=^{xzm_segment_s}^^{xzm_segment_s}}Q^v[256Q][256{xzm_slice_s=(?={?=II{lock_exclaves_s=[4I]}C}(xzm_chunk_atomic_meta_u={?=b11b11b6b1b1b1b7b13b13}{?=Q}Q))(?={?=^{xzm_slice_s}^^{xzm_slice_s}}{?=^{xzm_slice_s}}[2^{xzm_slice_s}])(xzm_chunk_bits_u={?=b4b1b1b1b1}C)CSII}]}16^{xzm_slice_s=(?={?=II{lock_exclaves_s=[4I]}C}(xzm_chunk_atomic_meta_u={?=b11b11b6b1b1b1b7b13b13}{?=Q}Q))(?={?=^{xzm_slice_s}^^{xzm_slice_s}}{?=^{xzm_slice_s}}[2^{xzm_slice_s}])(xzm_chunk_bits_u={?=b4b1b1b1b1}C)CSII}24I32Q36^{xzm_xzone_s=(?={?={?=^{xzm_slice_s}}{?=^{xzm_slice_s}}{?=^{xzm_slice_s}}{lock_exclaves_s=[4I]}}{?=(xzm_chunk_list_head_u={?=b47b16b1}Q)(xzm_chunk_list_head_u={?=b47b16b1}Q)(xzm_chunk_list_head_u={?=b47b16b1}Q)(xzm_chunk_list_head_u={?=b47b16b1}Q)})S^{xzm_segment_group_s}QQIICSCCb1{xzm_xzone_guard_config_s=CC}}44^{?=QQ}52Q60"

```
