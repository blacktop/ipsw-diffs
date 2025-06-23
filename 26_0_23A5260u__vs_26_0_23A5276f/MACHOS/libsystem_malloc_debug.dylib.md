## libsystem_malloc_debug.dylib

> `/System/ExclaveKit/usr/lib/system/libsystem_malloc_debug.dylib`

```diff

-778.0.0.0.0
-  __TEXT.__text: 0x46510
+784.0.0.0.0
+  __TEXT.__text: 0x46628
   __TEXT.__auth_stubs: 0x1f0
-  __TEXT.__cstring: 0xd3b1
+  __TEXT.__cstring: 0xd3ee
   __TEXT.__const: 0x228
   __TEXT.__unwind_info: 0x340
   __TEXT.__eh_frame: 0x48

   - /System/ExclaveKit/usr/lib/system/liblibc.dylib
   - /System/ExclaveKit/usr/lib/system/liblibc_plat.dylib
   - /System/ExclaveKit/usr/lib/system/libsystem_blocks.dylib
-  UUID: DACE366D-1009-3B1C-8B25-4DDDB27443E4
-  Functions: 351
-  Symbols:   407
-  CStrings:  422
+  UUID: 68BB1460-D300-379E-88F1-69D52B66D2EF
+  Functions: 353
+  Symbols:   409
+  CStrings:  423
 
Symbols:
+ __malloc_type_zone_malloc_with_options_outlined
+ __xzm_free_abort
+ _malloc_type_zone_malloc_with_options
+ _malloc_zone_malloc_with_options
- __malloc_type_zone_malloc_with_options_np_outlined
- _malloc_type_zone_malloc_with_options_np
CStrings:
+ "free to empty or invalid chunk detected (likely double-free)"
+ "malloc assertion \"!_xzm_chunk_is_full(zone, xz, chunk)\" failed (/Library/Caches/com.apple.xbs/Sources/libmalloc_exclavekit/src/xzone/xzone_malloc.c:2935)"
+ "malloc assertion \"!_xzm_chunk_is_full(zone, xz, chunk)\" failed (/Library/Caches/com.apple.xbs/Sources/libmalloc_exclavekit/src/xzone/xzone_malloc.c:3139)"
+ "malloc assertion \"!_xzm_chunk_is_full(zone, xz, chunk)\" failed (/Library/Caches/com.apple.xbs/Sources/libmalloc_exclavekit/src/xzone/xzone_malloc.c:3194)"
+ "malloc assertion \"!_xzm_chunk_is_full(zone, xz, chunk)\" failed (/Library/Caches/com.apple.xbs/Sources/libmalloc_exclavekit/src/xzone/xzone_malloc.c:3208)"
+ "malloc assertion \"!_xzm_chunk_is_full(zone, xz, chunk)\" failed (/Library/Caches/com.apple.xbs/Sources/libmalloc_exclavekit/src/xzone/xzone_malloc.c:4072)"
+ "malloc assertion \"!_xzm_slice_kind_uses_xzones(chunk->xzc_bits.xzcb_kind) || block_index < xz->xz_chunk_capacity\" failed (/Library/Caches/com.apple.xbs/Sources/libmalloc_exclavekit/src/xzone/xzone_malloc.c:4504)"
+ "malloc assertion \"!list || !SLIST_FIRST(list)\" failed (/Library/Caches/com.apple.xbs/Sources/libmalloc_exclavekit/src/xzone/xzone_malloc.c:2875)"
+ "malloc assertion \"!old_meta.xca_on_partial_list && !old_meta.xca_on_empty_list\" failed (/Library/Caches/com.apple.xbs/Sources/libmalloc_exclavekit/src/xzone/xzone_malloc.c:2423)"
+ "malloc assertion \"!old_meta.xca_on_partial_list\" failed (/Library/Caches/com.apple.xbs/Sources/libmalloc_exclavekit/src/xzone/xzone_malloc.c:2429)"
+ "malloc assertion \"!old_meta.xca_walk_locked\" failed (/Library/Caches/com.apple.xbs/Sources/libmalloc_exclavekit/src/xzone/xzone_malloc.c:4174)"
+ "malloc assertion \"!push_to_partial\" failed (/Library/Caches/com.apple.xbs/Sources/libmalloc_exclavekit/src/xzone/xzone_malloc.c:2374)"
+ "malloc assertion \"!xz\" failed (/Library/Caches/com.apple.xbs/Sources/libmalloc_exclavekit/src/xzone/xzone_malloc.c:4612)"
+ "malloc assertion \"(is_main && front_random) || (!is_main && !front_random)\" failed (/Library/Caches/com.apple.xbs/Sources/libmalloc_exclavekit/src/xzone/xzone_malloc.c:6346)"
+ "malloc assertion \"(uintptr_t)ptr % alignment == 0\" failed (/Library/Caches/com.apple.xbs/Sources/libmalloc_exclavekit/src/xzone/xzone_malloc.c:3735)"
+ "malloc assertion \"(uintptr_t)slots >= (uintptr_t)xzones + sizeof(struct xzm_xzone_s) * xzone_count\" failed (/Library/Caches/com.apple.xbs/Sources/libmalloc_exclavekit/src/xzone/xzone_malloc.c:6230)"
+ "malloc assertion \"(uintptr_t)zone + size >= (uintptr_t)slots + sizeof(struct xzm_xzone_allocation_slot_s) * xzone_count * slot_count\" failed (/Library/Caches/com.apple.xbs/Sources/libmalloc_exclavekit/src/xzone/xzone_malloc.c:6228)"
+ "malloc assertion \"(zone->xzz_flags & MALLOC_PURGEABLE) == 0\" failed (/Library/Caches/com.apple.xbs/Sources/libmalloc_exclavekit/src/xzone/xzone_malloc.c:3635)"
+ "malloc assertion \"2 * alignment <= XZM_SMALL_BLOCK_SIZE_MAX\" failed (/Library/Caches/com.apple.xbs/Sources/libmalloc_exclavekit/src/xzone/xzone_malloc.c:3723)"
+ "malloc assertion \"_xzm_malloc_zone_is_main((xzm_malloc_zone_t)main_zone)\" failed (/Library/Caches/com.apple.xbs/Sources/libmalloc_exclavekit/src/xzone/xzone_malloc.c:5791)"
+ "malloc assertion \"_xzm_malloc_zone_is_main((xzm_malloc_zone_t)main_zone)\" failed (/Library/Caches/com.apple.xbs/Sources/libmalloc_exclavekit/src/xzone/xzone_malloc.c:5800)"
+ "malloc assertion \"_xzm_malloc_zone_is_main((xzm_malloc_zone_t)main_zone)\" failed (/Library/Caches/com.apple.xbs/Sources/libmalloc_exclavekit/src/xzone/xzone_malloc.c:5809)"
+ "malloc assertion \"_xzm_malloc_zone_is_xzm(main_zone)\" failed (/Library/Caches/com.apple.xbs/Sources/libmalloc_exclavekit/src/xzone/xzone_malloc.c:5790)"
+ "malloc assertion \"_xzm_malloc_zone_is_xzm(main_zone)\" failed (/Library/Caches/com.apple.xbs/Sources/libmalloc_exclavekit/src/xzone/xzone_malloc.c:5799)"
+ "malloc assertion \"_xzm_malloc_zone_is_xzm(main_zone)\" failed (/Library/Caches/com.apple.xbs/Sources/libmalloc_exclavekit/src/xzone/xzone_malloc.c:5808)"
+ "malloc assertion \"_xzm_mem_is_zero(ptr, size)\" failed (/Library/Caches/com.apple.xbs/Sources/libmalloc_exclavekit/src/xzone/xzone_malloc.c:3643)"
+ "malloc assertion \"_xzm_slice_meta_is_batch_pointer(zone, chunk)\" failed (/Library/Caches/com.apple.xbs/Sources/libmalloc_exclavekit/src/xzone/xzone_malloc.c:5512)"
+ "malloc assertion \"_xzm_slice_meta_is_batch_pointer(zone, chunk)\" failed (/Library/Caches/com.apple.xbs/Sources/libmalloc_exclavekit/src/xzone/xzone_malloc.c:5689)"
+ "malloc assertion \"_xzm_slice_meta_is_batch_pointer(zone, chunk2)\" failed (/Library/Caches/com.apple.xbs/Sources/libmalloc_exclavekit/src/xzone/xzone_malloc.c:5529)"
+ "malloc assertion \"_xzm_slice_meta_is_batch_pointer(zone, next)\" failed (/Library/Caches/com.apple.xbs/Sources/libmalloc_exclavekit/src/xzone/xzone_malloc.c:2282)"
+ "malloc assertion \"_xzm_slice_meta_is_batch_pointer(zone, xz->xz_chunkq_batch)\" failed (/Library/Caches/com.apple.xbs/Sources/libmalloc_exclavekit/src/xzone/xzone_malloc.c:3165)"
+ "malloc assertion \"alignment <= XZM_SMALL_BLOCK_SIZE_MAX\" failed (/Library/Caches/com.apple.xbs/Sources/libmalloc_exclavekit/src/xzone/xzone_malloc.c:3720)"
+ "malloc assertion \"allocation_front_count == 2\" failed (/Library/Caches/com.apple.xbs/Sources/libmalloc_exclavekit/src/xzone/xzone_malloc.c:6116)"
+ "malloc assertion \"block_index <= xz->xz_chunk_capacity\" failed (/Library/Caches/com.apple.xbs/Sources/libmalloc_exclavekit/src/xzone/xzone_malloc.c:2986)"
+ "malloc assertion \"byte < XZM_FRONT_RANDOM_SIZE\" failed (/Library/Caches/com.apple.xbs/Sources/libmalloc_exclavekit/src/xzone/xzone_malloc.c:6121)"
+ "malloc assertion \"chunk\" failed (/Library/Caches/com.apple.xbs/Sources/libmalloc_exclavekit/src/xzone/xzone_malloc.c:2896)"
+ "malloc assertion \"chunk\" failed (/Library/Caches/com.apple.xbs/Sources/libmalloc_exclavekit/src/xzone/xzone_malloc.c:3161)"
+ "malloc assertion \"chunk->xzc_bits.xzcb_kind == XZM_SLICE_KIND_SMALL_CHUNK\" failed (/Library/Caches/com.apple.xbs/Sources/libmalloc_exclavekit/src/xzone/xzone_malloc.c:3920)"
+ "malloc assertion \"chunk->xzc_bits.xzcb_kind == kind\" failed (/Library/Caches/com.apple.xbs/Sources/libmalloc_exclavekit/src/xzone/xzone_malloc.c:4399)"
+ "malloc assertion \"chunk->xzc_bits.xzcb_on_partial_list\" failed (/Library/Caches/com.apple.xbs/Sources/libmalloc_exclavekit/src/xzone/xzone_malloc.c:3135)"
+ "malloc assertion \"chunk->xzc_bits.xzcb_on_partial_list\" failed (/Library/Caches/com.apple.xbs/Sources/libmalloc_exclavekit/src/xzone/xzone_malloc.c:4027)"
+ "malloc assertion \"chunk->xzc_free == 0\" failed (/Library/Caches/com.apple.xbs/Sources/libmalloc_exclavekit/src/xzone/xzone_malloc.c:2830)"
+ "malloc assertion \"chunk->xzc_mzone_idx == XZM_MZONE_INDEX_INVALID\" failed (/Library/Caches/com.apple.xbs/Sources/libmalloc_exclavekit/src/xzone/xzone_malloc.c:2832)"
+ "malloc assertion \"chunk->xzc_used == 0\" failed (/Library/Caches/com.apple.xbs/Sources/libmalloc_exclavekit/src/xzone/xzone_malloc.c:2831)"
+ "malloc assertion \"freelist_count <= old_meta.xca_free_count\" failed (/Library/Caches/com.apple.xbs/Sources/libmalloc_exclavekit/src/xzone/xzone_malloc.c:4366)"
+ "malloc assertion \"kind == chunk->xzc_bits.xzcb_kind\" failed (/Library/Caches/com.apple.xbs/Sources/libmalloc_exclavekit/src/xzone/xzone_malloc.c:2278)"
+ "malloc assertion \"new_size\" failed (/Library/Caches/com.apple.xbs/Sources/libmalloc_exclavekit/src/xzone/xzone_malloc.c:4799)"
+ "malloc assertion \"new_zone != NULL\" failed (/Library/Caches/com.apple.xbs/Sources/libmalloc_exclavekit/src/xzone/xzone_malloc.c:8154)"
+ "malloc assertion \"old_meta.xca_alloc_head == XZM_FREE_MADVISING\" failed (/Library/Caches/com.apple.xbs/Sources/libmalloc_exclavekit/src/xzone/xzone_malloc.c:2191)"
+ "malloc assertion \"old_size\" failed (/Library/Caches/com.apple.xbs/Sources/libmalloc_exclavekit/src/xzone/xzone_malloc.c:5269)"
+ "malloc assertion \"our_size != 0\" failed (/Library/Caches/com.apple.xbs/Sources/libmalloc_exclavekit/src/xzone/xzone_malloc.c:5230)"
+ "malloc assertion \"powerof2(alignment)\" failed (/Library/Caches/com.apple.xbs/Sources/libmalloc_exclavekit/src/xzone/xzone_malloc.c:3710)"
+ "malloc assertion \"ptr\" failed (/Library/Caches/com.apple.xbs/Sources/libmalloc_exclavekit/src/xzone/xzone_malloc.c:3211)"
+ "malloc assertion \"ptr\" failed (/Library/Caches/com.apple.xbs/Sources/libmalloc_exclavekit/src/xzone/xzone_malloc.c:3613)"
+ "malloc assertion \"ptr\" failed (/Library/Caches/com.apple.xbs/Sources/libmalloc_exclavekit/src/xzone/xzone_malloc.c:3641)"
+ "malloc assertion \"ptr\" failed (/Library/Caches/com.apple.xbs/Sources/libmalloc_exclavekit/src/xzone/xzone_malloc.c:3734)"
+ "malloc assertion \"ptr\" failed (/Library/Caches/com.apple.xbs/Sources/libmalloc_exclavekit/src/xzone/xzone_malloc.c:4798)"
+ "malloc assertion \"rg_idx < main->xzmz_range_group_count\" failed (/Library/Caches/com.apple.xbs/Sources/libmalloc_exclavekit/src/xzone/xzone_malloc.c:7875)"
+ "malloc assertion \"roundup(size, 4 * alignment) <= XZM_SMALL_BLOCK_SIZE_MAX\" failed (/Library/Caches/com.apple.xbs/Sources/libmalloc_exclavekit/src/xzone/xzone_malloc.c:3727)"
+ "malloc assertion \"segment != NULL\" failed (/Library/Caches/com.apple.xbs/Sources/libmalloc_exclavekit/src/xzone/xzone_malloc.c:4828)"
+ "malloc assertion \"sg->xzsg_id == XZM_SEGMENT_GROUP_POINTER_XZONES\" failed (/Library/Caches/com.apple.xbs/Sources/libmalloc_exclavekit/src/xzone/xzone_malloc.c:7871)"
+ "malloc assertion \"sgid == XZM_SEGMENT_GROUP_DATA\" failed (/Library/Caches/com.apple.xbs/Sources/libmalloc_exclavekit/src/xzone/xzone_malloc.c:6429)"
+ "malloc assertion \"size <= XZM_SMALL_BLOCK_SIZE_MAX\" failed (/Library/Caches/com.apple.xbs/Sources/libmalloc_exclavekit/src/xzone/xzone_malloc.c:3623)"
+ "malloc assertion \"size <= XZM_SMALL_BLOCK_SIZE_MAX\" failed (/Library/Caches/com.apple.xbs/Sources/libmalloc_exclavekit/src/xzone/xzone_malloc.c:3730)"
+ "malloc assertion \"slice_idx >= chunk_idx\" failed (/Library/Caches/com.apple.xbs/Sources/libmalloc_exclavekit/src/xzone/xzone_malloc.c:2997)"
+ "malloc assertion \"slice_idx >= chunk_idx\" failed (/Library/Caches/com.apple.xbs/Sources/libmalloc_exclavekit/src/xzone/xzone_malloc.c:3950)"
+ "malloc assertion \"success\" failed (/Library/Caches/com.apple.xbs/Sources/libmalloc_exclavekit/src/xzone/xzone_malloc.c:4207)"
+ "malloc assertion \"xas\" failed (/Library/Caches/com.apple.xbs/Sources/libmalloc_exclavekit/src/xzone/xzone_malloc.c:2477)"
+ "malloc assertion \"xas->xas_chunk == chunk\" failed (/Library/Caches/com.apple.xbs/Sources/libmalloc_exclavekit/src/xzone/xzone_malloc.c:3207)"
+ "malloc assertion \"xz\" failed (/Library/Caches/com.apple.xbs/Sources/libmalloc_exclavekit/src/xzone/xzone_malloc.c:2483)"
+ "malloc assertion \"xz\" failed (/Library/Caches/com.apple.xbs/Sources/libmalloc_exclavekit/src/xzone/xzone_malloc.c:2507)"
+ "malloc assertion \"xz\" failed (/Library/Caches/com.apple.xbs/Sources/libmalloc_exclavekit/src/xzone/xzone_malloc.c:6063)"
+ "malloc assertion \"xz->xz_block_size == chunk->xzc_freelist_block_size\" failed (/Library/Caches/com.apple.xbs/Sources/libmalloc_exclavekit/src/xzone/xzone_malloc.c:4622)"
+ "malloc assertion \"xz->xz_block_size > XZM_TINY_BLOCK_SIZE_MAX\" failed (/Library/Caches/com.apple.xbs/Sources/libmalloc_exclavekit/src/xzone/xzone_malloc.c:5503)"
+ "malloc assertion \"xz->xz_chunk_capacity == chunk->xzc_freelist_chunk_capacity\" failed (/Library/Caches/com.apple.xbs/Sources/libmalloc_exclavekit/src/xzone/xzone_malloc.c:4623)"
+ "malloc assertion \"xz->xz_chunkq_batch_count <= batch_size\" failed (/Library/Caches/com.apple.xbs/Sources/libmalloc_exclavekit/src/xzone/xzone_malloc.c:3966)"
+ "malloc assertion \"xz->xz_slot_config <= zone->xzz_max_slot_config\" failed (/Library/Caches/com.apple.xbs/Sources/libmalloc_exclavekit/src/xzone/xzone_malloc.c:3069)"
+ "malloc assertion \"xzone_count <= UINT8_MAX\" failed (/Library/Caches/com.apple.xbs/Sources/libmalloc_exclavekit/src/xzone/xzone_malloc.c:6775)"
+ "malloc assertion \"zone->xzz_slot_count == _xzm_get_limit_allocation_index(zone->xzz_max_slot_config)\" failed (/Library/Caches/com.apple.xbs/Sources/libmalloc_exclavekit/src/xzone/xzone_malloc.c:6480)"
- "malloc assertion \"!_xzm_chunk_is_full(zone, xz, chunk)\" failed (/Library/Caches/com.apple.xbs/Sources/libmalloc_exclavekit/src/xzone/xzone_malloc.c:2920)"
- "malloc assertion \"!_xzm_chunk_is_full(zone, xz, chunk)\" failed (/Library/Caches/com.apple.xbs/Sources/libmalloc_exclavekit/src/xzone/xzone_malloc.c:3124)"
- "malloc assertion \"!_xzm_chunk_is_full(zone, xz, chunk)\" failed (/Library/Caches/com.apple.xbs/Sources/libmalloc_exclavekit/src/xzone/xzone_malloc.c:3179)"
- "malloc assertion \"!_xzm_chunk_is_full(zone, xz, chunk)\" failed (/Library/Caches/com.apple.xbs/Sources/libmalloc_exclavekit/src/xzone/xzone_malloc.c:3193)"
- "malloc assertion \"!_xzm_chunk_is_full(zone, xz, chunk)\" failed (/Library/Caches/com.apple.xbs/Sources/libmalloc_exclavekit/src/xzone/xzone_malloc.c:4056)"
- "malloc assertion \"!_xzm_slice_kind_uses_xzones(chunk->xzc_bits.xzcb_kind) || block_index < xz->xz_chunk_capacity\" failed (/Library/Caches/com.apple.xbs/Sources/libmalloc_exclavekit/src/xzone/xzone_malloc.c:4488)"
- "malloc assertion \"!list || !SLIST_FIRST(list)\" failed (/Library/Caches/com.apple.xbs/Sources/libmalloc_exclavekit/src/xzone/xzone_malloc.c:2860)"
- "malloc assertion \"!old_meta.xca_on_partial_list && !old_meta.xca_on_empty_list\" failed (/Library/Caches/com.apple.xbs/Sources/libmalloc_exclavekit/src/xzone/xzone_malloc.c:2408)"
- "malloc assertion \"!old_meta.xca_on_partial_list\" failed (/Library/Caches/com.apple.xbs/Sources/libmalloc_exclavekit/src/xzone/xzone_malloc.c:2414)"
- "malloc assertion \"!old_meta.xca_walk_locked\" failed (/Library/Caches/com.apple.xbs/Sources/libmalloc_exclavekit/src/xzone/xzone_malloc.c:4158)"
- "malloc assertion \"!push_to_partial\" failed (/Library/Caches/com.apple.xbs/Sources/libmalloc_exclavekit/src/xzone/xzone_malloc.c:2363)"
- "malloc assertion \"!xz\" failed (/Library/Caches/com.apple.xbs/Sources/libmalloc_exclavekit/src/xzone/xzone_malloc.c:4596)"
- "malloc assertion \"(is_main && front_random) || (!is_main && !front_random)\" failed (/Library/Caches/com.apple.xbs/Sources/libmalloc_exclavekit/src/xzone/xzone_malloc.c:6330)"
- "malloc assertion \"(uintptr_t)ptr % alignment == 0\" failed (/Library/Caches/com.apple.xbs/Sources/libmalloc_exclavekit/src/xzone/xzone_malloc.c:3719)"
- "malloc assertion \"(uintptr_t)slots >= (uintptr_t)xzones + sizeof(struct xzm_xzone_s) * xzone_count\" failed (/Library/Caches/com.apple.xbs/Sources/libmalloc_exclavekit/src/xzone/xzone_malloc.c:6214)"
- "malloc assertion \"(uintptr_t)zone + size >= (uintptr_t)slots + sizeof(struct xzm_xzone_allocation_slot_s) * xzone_count * slot_count\" failed (/Library/Caches/com.apple.xbs/Sources/libmalloc_exclavekit/src/xzone/xzone_malloc.c:6212)"
- "malloc assertion \"(zone->xzz_flags & MALLOC_PURGEABLE) == 0\" failed (/Library/Caches/com.apple.xbs/Sources/libmalloc_exclavekit/src/xzone/xzone_malloc.c:3619)"
- "malloc assertion \"2 * alignment <= XZM_SMALL_BLOCK_SIZE_MAX\" failed (/Library/Caches/com.apple.xbs/Sources/libmalloc_exclavekit/src/xzone/xzone_malloc.c:3707)"
- "malloc assertion \"_xzm_malloc_zone_is_main((xzm_malloc_zone_t)main_zone)\" failed (/Library/Caches/com.apple.xbs/Sources/libmalloc_exclavekit/src/xzone/xzone_malloc.c:5775)"
- "malloc assertion \"_xzm_malloc_zone_is_main((xzm_malloc_zone_t)main_zone)\" failed (/Library/Caches/com.apple.xbs/Sources/libmalloc_exclavekit/src/xzone/xzone_malloc.c:5784)"
- "malloc assertion \"_xzm_malloc_zone_is_main((xzm_malloc_zone_t)main_zone)\" failed (/Library/Caches/com.apple.xbs/Sources/libmalloc_exclavekit/src/xzone/xzone_malloc.c:5793)"
- "malloc assertion \"_xzm_malloc_zone_is_xzm(main_zone)\" failed (/Library/Caches/com.apple.xbs/Sources/libmalloc_exclavekit/src/xzone/xzone_malloc.c:5774)"
- "malloc assertion \"_xzm_malloc_zone_is_xzm(main_zone)\" failed (/Library/Caches/com.apple.xbs/Sources/libmalloc_exclavekit/src/xzone/xzone_malloc.c:5783)"
- "malloc assertion \"_xzm_malloc_zone_is_xzm(main_zone)\" failed (/Library/Caches/com.apple.xbs/Sources/libmalloc_exclavekit/src/xzone/xzone_malloc.c:5792)"
- "malloc assertion \"_xzm_mem_is_zero(ptr, size)\" failed (/Library/Caches/com.apple.xbs/Sources/libmalloc_exclavekit/src/xzone/xzone_malloc.c:3627)"
- "malloc assertion \"_xzm_slice_meta_is_batch_pointer(zone, chunk)\" failed (/Library/Caches/com.apple.xbs/Sources/libmalloc_exclavekit/src/xzone/xzone_malloc.c:5496)"
- "malloc assertion \"_xzm_slice_meta_is_batch_pointer(zone, chunk)\" failed (/Library/Caches/com.apple.xbs/Sources/libmalloc_exclavekit/src/xzone/xzone_malloc.c:5673)"
- "malloc assertion \"_xzm_slice_meta_is_batch_pointer(zone, chunk2)\" failed (/Library/Caches/com.apple.xbs/Sources/libmalloc_exclavekit/src/xzone/xzone_malloc.c:5513)"
- "malloc assertion \"_xzm_slice_meta_is_batch_pointer(zone, next)\" failed (/Library/Caches/com.apple.xbs/Sources/libmalloc_exclavekit/src/xzone/xzone_malloc.c:2280)"
- "malloc assertion \"_xzm_slice_meta_is_batch_pointer(zone, xz->xz_chunkq_batch)\" failed (/Library/Caches/com.apple.xbs/Sources/libmalloc_exclavekit/src/xzone/xzone_malloc.c:3150)"
- "malloc assertion \"alignment <= XZM_SMALL_BLOCK_SIZE_MAX\" failed (/Library/Caches/com.apple.xbs/Sources/libmalloc_exclavekit/src/xzone/xzone_malloc.c:3704)"
- "malloc assertion \"allocation_front_count == 2\" failed (/Library/Caches/com.apple.xbs/Sources/libmalloc_exclavekit/src/xzone/xzone_malloc.c:6100)"
- "malloc assertion \"block_index <= xz->xz_chunk_capacity\" failed (/Library/Caches/com.apple.xbs/Sources/libmalloc_exclavekit/src/xzone/xzone_malloc.c:2971)"
- "malloc assertion \"byte < XZM_FRONT_RANDOM_SIZE\" failed (/Library/Caches/com.apple.xbs/Sources/libmalloc_exclavekit/src/xzone/xzone_malloc.c:6105)"
- "malloc assertion \"chunk\" failed (/Library/Caches/com.apple.xbs/Sources/libmalloc_exclavekit/src/xzone/xzone_malloc.c:2881)"
- "malloc assertion \"chunk\" failed (/Library/Caches/com.apple.xbs/Sources/libmalloc_exclavekit/src/xzone/xzone_malloc.c:3146)"
- "malloc assertion \"chunk->xzc_bits.xzcb_kind == XZM_SLICE_KIND_SMALL_CHUNK\" failed (/Library/Caches/com.apple.xbs/Sources/libmalloc_exclavekit/src/xzone/xzone_malloc.c:3904)"
- "malloc assertion \"chunk->xzc_bits.xzcb_kind == kind\" failed (/Library/Caches/com.apple.xbs/Sources/libmalloc_exclavekit/src/xzone/xzone_malloc.c:4383)"
- "malloc assertion \"chunk->xzc_bits.xzcb_on_partial_list\" failed (/Library/Caches/com.apple.xbs/Sources/libmalloc_exclavekit/src/xzone/xzone_malloc.c:3120)"
- "malloc assertion \"chunk->xzc_bits.xzcb_on_partial_list\" failed (/Library/Caches/com.apple.xbs/Sources/libmalloc_exclavekit/src/xzone/xzone_malloc.c:4011)"
- "malloc assertion \"chunk->xzc_free == 0\" failed (/Library/Caches/com.apple.xbs/Sources/libmalloc_exclavekit/src/xzone/xzone_malloc.c:2815)"
- "malloc assertion \"chunk->xzc_mzone_idx == XZM_MZONE_INDEX_INVALID\" failed (/Library/Caches/com.apple.xbs/Sources/libmalloc_exclavekit/src/xzone/xzone_malloc.c:2817)"
- "malloc assertion \"chunk->xzc_used == 0\" failed (/Library/Caches/com.apple.xbs/Sources/libmalloc_exclavekit/src/xzone/xzone_malloc.c:2816)"
- "malloc assertion \"freelist_count <= old_meta.xca_free_count\" failed (/Library/Caches/com.apple.xbs/Sources/libmalloc_exclavekit/src/xzone/xzone_malloc.c:4350)"
- "malloc assertion \"kind == chunk->xzc_bits.xzcb_kind\" failed (/Library/Caches/com.apple.xbs/Sources/libmalloc_exclavekit/src/xzone/xzone_malloc.c:2276)"
- "malloc assertion \"new_size\" failed (/Library/Caches/com.apple.xbs/Sources/libmalloc_exclavekit/src/xzone/xzone_malloc.c:4783)"
- "malloc assertion \"new_zone != NULL\" failed (/Library/Caches/com.apple.xbs/Sources/libmalloc_exclavekit/src/xzone/xzone_malloc.c:8131)"
- "malloc assertion \"old_meta.xca_alloc_head == XZM_FREE_MADVISING\" failed (/Library/Caches/com.apple.xbs/Sources/libmalloc_exclavekit/src/xzone/xzone_malloc.c:2189)"
- "malloc assertion \"old_size\" failed (/Library/Caches/com.apple.xbs/Sources/libmalloc_exclavekit/src/xzone/xzone_malloc.c:5253)"
- "malloc assertion \"our_size != 0\" failed (/Library/Caches/com.apple.xbs/Sources/libmalloc_exclavekit/src/xzone/xzone_malloc.c:5214)"
- "malloc assertion \"powerof2(alignment)\" failed (/Library/Caches/com.apple.xbs/Sources/libmalloc_exclavekit/src/xzone/xzone_malloc.c:3694)"
- "malloc assertion \"ptr\" failed (/Library/Caches/com.apple.xbs/Sources/libmalloc_exclavekit/src/xzone/xzone_malloc.c:3196)"
- "malloc assertion \"ptr\" failed (/Library/Caches/com.apple.xbs/Sources/libmalloc_exclavekit/src/xzone/xzone_malloc.c:3597)"
- "malloc assertion \"ptr\" failed (/Library/Caches/com.apple.xbs/Sources/libmalloc_exclavekit/src/xzone/xzone_malloc.c:3625)"
- "malloc assertion \"ptr\" failed (/Library/Caches/com.apple.xbs/Sources/libmalloc_exclavekit/src/xzone/xzone_malloc.c:3718)"
- "malloc assertion \"ptr\" failed (/Library/Caches/com.apple.xbs/Sources/libmalloc_exclavekit/src/xzone/xzone_malloc.c:4782)"
- "malloc assertion \"rg_idx < main->xzmz_range_group_count\" failed (/Library/Caches/com.apple.xbs/Sources/libmalloc_exclavekit/src/xzone/xzone_malloc.c:7852)"
- "malloc assertion \"roundup(size, 4 * alignment) <= XZM_SMALL_BLOCK_SIZE_MAX\" failed (/Library/Caches/com.apple.xbs/Sources/libmalloc_exclavekit/src/xzone/xzone_malloc.c:3711)"
- "malloc assertion \"segment != NULL\" failed (/Library/Caches/com.apple.xbs/Sources/libmalloc_exclavekit/src/xzone/xzone_malloc.c:4812)"
- "malloc assertion \"sg->xzsg_id == XZM_SEGMENT_GROUP_POINTER_XZONES\" failed (/Library/Caches/com.apple.xbs/Sources/libmalloc_exclavekit/src/xzone/xzone_malloc.c:7848)"
- "malloc assertion \"sgid == XZM_SEGMENT_GROUP_DATA\" failed (/Library/Caches/com.apple.xbs/Sources/libmalloc_exclavekit/src/xzone/xzone_malloc.c:6413)"
- "malloc assertion \"size <= XZM_SMALL_BLOCK_SIZE_MAX\" failed (/Library/Caches/com.apple.xbs/Sources/libmalloc_exclavekit/src/xzone/xzone_malloc.c:3607)"
- "malloc assertion \"size <= XZM_SMALL_BLOCK_SIZE_MAX\" failed (/Library/Caches/com.apple.xbs/Sources/libmalloc_exclavekit/src/xzone/xzone_malloc.c:3714)"
- "malloc assertion \"slice_idx >= chunk_idx\" failed (/Library/Caches/com.apple.xbs/Sources/libmalloc_exclavekit/src/xzone/xzone_malloc.c:2982)"
- "malloc assertion \"slice_idx >= chunk_idx\" failed (/Library/Caches/com.apple.xbs/Sources/libmalloc_exclavekit/src/xzone/xzone_malloc.c:3934)"
- "malloc assertion \"success\" failed (/Library/Caches/com.apple.xbs/Sources/libmalloc_exclavekit/src/xzone/xzone_malloc.c:4191)"
- "malloc assertion \"xas\" failed (/Library/Caches/com.apple.xbs/Sources/libmalloc_exclavekit/src/xzone/xzone_malloc.c:2462)"
- "malloc assertion \"xas->xas_chunk == chunk\" failed (/Library/Caches/com.apple.xbs/Sources/libmalloc_exclavekit/src/xzone/xzone_malloc.c:3192)"
- "malloc assertion \"xz\" failed (/Library/Caches/com.apple.xbs/Sources/libmalloc_exclavekit/src/xzone/xzone_malloc.c:2468)"
- "malloc assertion \"xz\" failed (/Library/Caches/com.apple.xbs/Sources/libmalloc_exclavekit/src/xzone/xzone_malloc.c:2492)"
- "malloc assertion \"xz\" failed (/Library/Caches/com.apple.xbs/Sources/libmalloc_exclavekit/src/xzone/xzone_malloc.c:6047)"
- "malloc assertion \"xz->xz_block_size == chunk->xzc_freelist_block_size\" failed (/Library/Caches/com.apple.xbs/Sources/libmalloc_exclavekit/src/xzone/xzone_malloc.c:4606)"
- "malloc assertion \"xz->xz_block_size > XZM_TINY_BLOCK_SIZE_MAX\" failed (/Library/Caches/com.apple.xbs/Sources/libmalloc_exclavekit/src/xzone/xzone_malloc.c:5487)"
- "malloc assertion \"xz->xz_chunk_capacity == chunk->xzc_freelist_chunk_capacity\" failed (/Library/Caches/com.apple.xbs/Sources/libmalloc_exclavekit/src/xzone/xzone_malloc.c:4607)"
- "malloc assertion \"xz->xz_chunkq_batch_count <= batch_size\" failed (/Library/Caches/com.apple.xbs/Sources/libmalloc_exclavekit/src/xzone/xzone_malloc.c:3950)"
- "malloc assertion \"xz->xz_slot_config <= zone->xzz_max_slot_config\" failed (/Library/Caches/com.apple.xbs/Sources/libmalloc_exclavekit/src/xzone/xzone_malloc.c:3054)"
- "malloc assertion \"xzone_count <= UINT8_MAX\" failed (/Library/Caches/com.apple.xbs/Sources/libmalloc_exclavekit/src/xzone/xzone_malloc.c:6759)"
- "malloc assertion \"zone->xzz_slot_count == _xzm_get_limit_allocation_index(zone->xzz_max_slot_config)\" failed (/Library/Caches/com.apple.xbs/Sources/libmalloc_exclavekit/src/xzone/xzone_malloc.c:6464)"

```
