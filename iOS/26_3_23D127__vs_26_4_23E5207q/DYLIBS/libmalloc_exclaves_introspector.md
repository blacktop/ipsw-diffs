## libmalloc_exclaves_introspector

> `/System/Library/PrivateFrameworks/libmalloc_exclaves_introspector.framework/libmalloc_exclaves_introspector`

```diff

-792.80.2.0.0
-  __TEXT.__text: 0x3d5c
+812.100.27.0.0
+  __TEXT.__text: 0x43cc
   __TEXT.__auth_stubs: 0x200
   __TEXT.__const: 0x7b
-  __TEXT.__cstring: 0x1cf2
-  __TEXT.__unwind_info: 0xf0
+  __TEXT.__cstring: 0x20ff
+  __TEXT.__unwind_info: 0xf8
   __DATA_CONST.__got: 0x20
-  __DATA_CONST.__const: 0x248
+  __DATA_CONST.__const: 0x270
   __AUTH_CONST.__auth_got: 0x100
   __AUTH_CONST.__const: 0x130
   __DATA.__crash_info: 0x148
   __DATA.__bss: 0x11
   __DATA.__common: 0x4
   - /usr/lib/libSystem.B.dylib
-  UUID: 07D8A863-BAE9-3F5C-B73B-BC27D6896915
-  Functions: 47
+  UUID: 3543EEE1-CBFD-3631-AAD4-D21F6F9F4547
+  Functions: 48
   Symbols:   162
-  CStrings:  231
+  CStrings:  268
 
Symbols:
+ ___block_descriptor_tmp.215
+ ___block_descriptor_tmp.217
+ ___block_descriptor_tmp.36
+ ___block_descriptor_tmp.49
- ___block_descriptor_tmp.156
- ___block_descriptor_tmp.181
- ___block_descriptor_tmp.35
- ___block_descriptor_tmp.48
CStrings:
+ "            \"density\": %u,\n"
+ "            \"length\": %u,\n"
+ "            \"reuse\": %u\n"
+ "            \"type\": %u,\n"
+ "            { \"count\": %u }"
+ "        \"block_size\": %u,\n"
+ "        \"empty\": %u,\n"
+ "        \"guard_config\": {\n"
+ "        \"guards\": %u,\n"
+ "        \"last_dealloc_ts\": \"%llu\", \n"
+ "        \"on_multi_segment\": %d,\n"
+ "        \"quarantine\": %u,\n"
+ "        \"runq_full\": [\n"
+ "        \"runq_partial\": [\n"
+ "        \"runq_quarantine\": [\n"
+ "        \"slot_slices\": %u,\n"
+ "        \"slot_state\": \"0x%llx\",\n"
+ "        \"tagged\": %d,\n"
+ "        ],\n"
+ "        }\n"
+ "    \"%p\": {\n"
+ "    \"%u\": {\n"
+ "    \"guard_pages_enabled\": %d, \n"
+ "    \"large_chunk_slots\": %d,\n"
+ "    \"large_guard_density\": %d,\n"
+ "    \"large_guard_force_quarantine\": %d,\n"
+ "    \"large_guard_reinit\": %d,\n"
+ "    \"large_guard_reuse\": %d\n"
+ "    \"large_guards_enabled\": %d,\n"
+ "    \"large_max_chunks\": %d,\n"
+ "\"guard_object_config\": {\n"
+ "\"guard_page_config\": {\n"
+ "\"guard_zones\": {\n"
+ "\"multi_segment_size\": %zu, \n"
+ "%s}"
+ ",\n"
+ "BUG IN LIBMALLOC: malloc assertion \"main_address\" failed (/Library/Caches/com.apple.xbs/E5141CFD-4FBE-4400-8736-02E65444DC9D/TemporaryDirectory.GmIvNN/Sources/libmalloc_frameworks/src/xzone_malloc/xzone_introspect.c:838)"
+ "BUG IN LIBMALLOC: malloc assertion \"zone\" failed (/Library/Caches/com.apple.xbs/E5141CFD-4FBE-4400-8736-02E65444DC9D/TemporaryDirectory.GmIvNN/Sources/libmalloc_frameworks/src/xzone_malloc/xzone_introspect.c:836)"
+ "guard_chunk"
+ "i20@?0^{xzm_slice_s=(?={?=II{lock_exclaves_s=[4I]}C}{?=(xzm_chunk_atomic_meta_u={?=b11b11b6b1b1b1b13b20}{?=Q}Q)SSB}{?=Q{lock_exclaves_s=[4I]}CCCC})(?={?=^{xzm_slice_s}^^{xzm_slice_s}}{?=^{xzm_slice_s}}[2^{xzm_slice_s}])(xzm_chunk_bits_u={?=b4b1b1b1b1}C)(?=CC)SII(xzm_xzone_slice_metadata_u=Q^{xzm_slice_s})}8I16"
+ "i32@?0Q8^{xzm_segment_s={?=[2Q]}^{xzm_segment_group_s}IIIC{?=^{xzm_segment_s}^^{xzm_segment_s}}^vQ[0{xzm_slice_s=(?={?=II{lock_exclaves_s=[4I]}C}{?=(xzm_chunk_atomic_meta_u={?=b11b11b6b1b1b1b13b20}{?=Q}Q)SSB}{?=Q{lock_exclaves_s=[4I]}CCCC})(?={?=^{xzm_slice_s}^^{xzm_slice_s}}{?=^{xzm_slice_s}}[2^{xzm_slice_s}])(xzm_chunk_bits_u={?=b4b1b1b1b1}C)(?=CC)SII(xzm_xzone_slice_metadata_u=Q^{xzm_slice_s})}]}16r*24"
+ "i44@?0Q8^{xzm_segment_s={?=[2Q]}^{xzm_segment_group_s}IIIC{?=^{xzm_segment_s}^^{xzm_segment_s}}^vQ[0{xzm_slice_s=(?={?=II{lock_exclaves_s=[4I]}C}{?=(xzm_chunk_atomic_meta_u={?=b11b11b6b1b1b1b13b20}{?=Q}Q)SSB}{?=Q{lock_exclaves_s=[4I]}CCCC})(?={?=^{xzm_slice_s}^^{xzm_slice_s}}{?=^{xzm_slice_s}}[2^{xzm_slice_s}])(xzm_chunk_bits_u={?=b4b1b1b1b1}C)(?=CC)SII(xzm_xzone_slice_metadata_u=Q^{xzm_slice_s})}]}16^{xzm_slice_s=(?={?=II{lock_exclaves_s=[4I]}C}{?=(xzm_chunk_atomic_meta_u={?=b11b11b6b1b1b1b13b20}{?=Q}Q)SSB}{?=Q{lock_exclaves_s=[4I]}CCCC})(?={?=^{xzm_slice_s}^^{xzm_slice_s}}{?=^{xzm_slice_s}}[2^{xzm_slice_s}])(xzm_chunk_bits_u={?=b4b1b1b1b1}C)(?=CC)SII(xzm_xzone_slice_metadata_u=Q^{xzm_slice_s})}24I32Q36"
+ "i68@?0Q8^{xzm_segment_s={?=[2Q]}^{xzm_segment_group_s}IIIC{?=^{xzm_segment_s}^^{xzm_segment_s}}^vQ[0{xzm_slice_s=(?={?=II{lock_exclaves_s=[4I]}C}{?=(xzm_chunk_atomic_meta_u={?=b11b11b6b1b1b1b13b20}{?=Q}Q)SSB}{?=Q{lock_exclaves_s=[4I]}CCCC})(?={?=^{xzm_slice_s}^^{xzm_slice_s}}{?=^{xzm_slice_s}}[2^{xzm_slice_s}])(xzm_chunk_bits_u={?=b4b1b1b1b1}C)(?=CC)SII(xzm_xzone_slice_metadata_u=Q^{xzm_slice_s})}]}16^{xzm_slice_s=(?={?=II{lock_exclaves_s=[4I]}C}{?=(xzm_chunk_atomic_meta_u={?=b11b11b6b1b1b1b13b20}{?=Q}Q)SSB}{?=Q{lock_exclaves_s=[4I]}CCCC})(?={?=^{xzm_slice_s}^^{xzm_slice_s}}{?=^{xzm_slice_s}}[2^{xzm_slice_s}])(xzm_chunk_bits_u={?=b4b1b1b1b1}C)(?=CC)SII(xzm_xzone_slice_metadata_u=Q^{xzm_slice_s})}24I32Q36(xzm_gxzone_u=^{xzm_gzone_s}^{xzm_xzone_s})44^{?=QQ}52Q60"
+ "multi-segment metadata slab"
+ "multi_segment"
+ "},\n"
- "    \"guards_enabled\": %d, \n"
- "\"guard_config\": {\n"
- "%s}\n"
- "BUG IN LIBMALLOC: malloc assertion \"main_address\" failed (/Library/Caches/com.apple.xbs/Sources/libmalloc_frameworks/src/xzone/xzone_introspect.c:774)"
- "BUG IN LIBMALLOC: malloc assertion \"zone\" failed (/Library/Caches/com.apple.xbs/Sources/libmalloc_frameworks/src/xzone/xzone_introspect.c:772)"
- "i20@?0^{xzm_slice_s=(?={?=II{lock_exclaves_s=[4I]}C}{?=(xzm_chunk_atomic_meta_u={?=b11b11b6b1b1b1b13b20}{?=Q}Q)SSB})(?={?=^{xzm_slice_s}^^{xzm_slice_s}}{?=^{xzm_slice_s}}[2^{xzm_slice_s}])(xzm_chunk_bits_u={?=b4b1b1b1b1}C)CSII}8I16"
- "i32@?0Q8^{xzm_segment_s={?=[2Q]}^{xzm_segment_group_s}IIIC{?=^{xzm_segment_s}^^{xzm_segment_s}}^vQ[256(xzm_xzone_slice_metadata_u=Q^{xzm_slice_s})][256{xzm_slice_s=(?={?=II{lock_exclaves_s=[4I]}C}{?=(xzm_chunk_atomic_meta_u={?=b11b11b6b1b1b1b13b20}{?=Q}Q)SSB})(?={?=^{xzm_slice_s}^^{xzm_slice_s}}{?=^{xzm_slice_s}}[2^{xzm_slice_s}])(xzm_chunk_bits_u={?=b4b1b1b1b1}C)CSII}]}16r*24"
- "i44@?0Q8^{xzm_segment_s={?=[2Q]}^{xzm_segment_group_s}IIIC{?=^{xzm_segment_s}^^{xzm_segment_s}}^vQ[256(xzm_xzone_slice_metadata_u=Q^{xzm_slice_s})][256{xzm_slice_s=(?={?=II{lock_exclaves_s=[4I]}C}{?=(xzm_chunk_atomic_meta_u={?=b11b11b6b1b1b1b13b20}{?=Q}Q)SSB})(?={?=^{xzm_slice_s}^^{xzm_slice_s}}{?=^{xzm_slice_s}}[2^{xzm_slice_s}])(xzm_chunk_bits_u={?=b4b1b1b1b1}C)CSII}]}16^{xzm_slice_s=(?={?=II{lock_exclaves_s=[4I]}C}{?=(xzm_chunk_atomic_meta_u={?=b11b11b6b1b1b1b13b20}{?=Q}Q)SSB})(?={?=^{xzm_slice_s}^^{xzm_slice_s}}{?=^{xzm_slice_s}}[2^{xzm_slice_s}])(xzm_chunk_bits_u={?=b4b1b1b1b1}C)CSII}24I32Q36"
- "i68@?0Q8^{xzm_segment_s={?=[2Q]}^{xzm_segment_group_s}IIIC{?=^{xzm_segment_s}^^{xzm_segment_s}}^vQ[256(xzm_xzone_slice_metadata_u=Q^{xzm_slice_s})][256{xzm_slice_s=(?={?=II{lock_exclaves_s=[4I]}C}{?=(xzm_chunk_atomic_meta_u={?=b11b11b6b1b1b1b13b20}{?=Q}Q)SSB})(?={?=^{xzm_slice_s}^^{xzm_slice_s}}{?=^{xzm_slice_s}}[2^{xzm_slice_s}])(xzm_chunk_bits_u={?=b4b1b1b1b1}C)CSII}]}16^{xzm_slice_s=(?={?=II{lock_exclaves_s=[4I]}C}{?=(xzm_chunk_atomic_meta_u={?=b11b11b6b1b1b1b13b20}{?=Q}Q)SSB})(?={?=^{xzm_slice_s}^^{xzm_slice_s}}{?=^{xzm_slice_s}}[2^{xzm_slice_s}])(xzm_chunk_bits_u={?=b4b1b1b1b1}C)CSII}24I32Q36^{xzm_xzone_s=(?={?={?=^{xzm_slice_s}}{?=^{xzm_slice_s}}{?=^{xzm_slice_s}}^{xzm_slice_s}I{lock_exclaves_s=[4I]}}{?=(xzm_chunk_list_head_u=(?={?=b47b16b1}{?=b47b10b6b1})Q)(xzm_chunk_list_head_u=(?={?=b47b16b1}{?=b47b10b6b1})Q)(xzm_chunk_list_head_u=(?={?=b47b16b1}{?=b47b10b6b1})Q)(xzm_chunk_list_head_u=(?={?=b47b16b1}{?=b47b10b6b1})Q)})SCCQQIIQCSCCCb1b1{xzm_xzone_guard_config_s=CC}}44^{?=QQ}52Q60"

```
