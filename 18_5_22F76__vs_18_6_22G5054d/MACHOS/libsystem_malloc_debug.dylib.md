## libsystem_malloc_debug.dylib

> `/System/ExclaveKit/usr/lib/system/libsystem_malloc_debug.dylib`

```diff

-715.120.13.0.0
-  __TEXT.__text: 0x41918
+715.140.5.0.0
+  __TEXT.__text: 0x4156c
   __TEXT.__auth_stubs: 0x1f0
   __TEXT.__cstring: 0xc220
   __TEXT.__const: 0x368
-  __TEXT.__unwind_info: 0x328
+  __TEXT.__unwind_info: 0x320
   __TEXT.__eh_frame: 0x48
   __DATA_CONST.__got: 0x10
   __AUTH_CONST.__auth_got: 0xf8

   - /System/ExclaveKit/usr/lib/system/liblibc.dylib
   - /System/ExclaveKit/usr/lib/system/liblibc_plat.dylib
   - /System/ExclaveKit/usr/lib/system/libsystem_blocks.dylib
-  UUID: 0755F0D5-3678-34B6-887F-DEFE3AB1C77E
+  UUID: B72A656A-8077-3C9B-92A9-9D41B09D8B27
   Functions: 344
   Symbols:   405
   CStrings:  394
Functions:
~ _sanitizer_malloc : 396 -> 316
~ _sanitizer_calloc : 424 -> 344
~ _sanitizer_valloc : 1120 -> 1040
~ _sanitizer_free : 640 -> 668
~ _sanitizer_realloc : 408 -> 328
~ _sanitizer_memalign : 408 -> 328
~ _sanitizer_malloc_with_options : 432 -> 344
~ _sanitizer_malloc_type_malloc : 204 -> 124
~ _sanitizer_malloc_type_calloc : 2200 -> 2120
~ _sanitizer_malloc_type_realloc : 4212 -> 4132
~ _sanitizer_malloc_type_memalign : 1636 -> 1556
~ _sanitizer_malloc_type_malloc_with_options : 1256 -> 1176
~ _sanitizer_malloc_type_malloc_noalign_with_options : 2816 -> 2736
CStrings:
+ "malloc assertion \"!_xzm_chunk_is_full(zone, xz, chunk)\" failed (/Library/Caches/com.apple.xbs/Sources/libmalloc_exclavekit/src/xzone/xzone_malloc.c:3845)"
+ "malloc assertion \"!_xzm_slice_kind_uses_xzones(chunk->xzc_bits.xzcb_kind) || block_index < xz->xz_chunk_capacity\" failed (/Library/Caches/com.apple.xbs/Sources/libmalloc_exclavekit/src/xzone/xzone_malloc.c:4270)"
+ "malloc assertion \"!old_meta.xca_walk_locked\" failed (/Library/Caches/com.apple.xbs/Sources/libmalloc_exclavekit/src/xzone/xzone_malloc.c:3947)"
+ "malloc assertion \"!xz\" failed (/Library/Caches/com.apple.xbs/Sources/libmalloc_exclavekit/src/xzone/xzone_malloc.c:4377)"
+ "malloc assertion \"(uintptr_t)ptr % alignment == 0\" failed (/Library/Caches/com.apple.xbs/Sources/libmalloc_exclavekit/src/xzone/xzone_malloc.c:3504)"
+ "malloc assertion \"(uintptr_t)slots >= (uintptr_t)xzones + sizeof(struct xzm_xzone_s) * xzone_count\" failed (/Library/Caches/com.apple.xbs/Sources/libmalloc_exclavekit/src/xzone/xzone_malloc.c:5980)"
+ "malloc assertion \"(uintptr_t)zone + size >= (uintptr_t)slots + sizeof(struct xzm_xzone_allocation_slot_s) * xzone_count * slot_count\" failed (/Library/Caches/com.apple.xbs/Sources/libmalloc_exclavekit/src/xzone/xzone_malloc.c:5978)"
+ "malloc assertion \"2 * alignment <= XZM_SMALL_BLOCK_SIZE_MAX\" failed (/Library/Caches/com.apple.xbs/Sources/libmalloc_exclavekit/src/xzone/xzone_malloc.c:3492)"
+ "malloc assertion \"_xzm_malloc_zone_is_main((xzm_malloc_zone_t)main_zone)\" failed (/Library/Caches/com.apple.xbs/Sources/libmalloc_exclavekit/src/xzone/xzone_malloc.c:5529)"
+ "malloc assertion \"_xzm_malloc_zone_is_main((xzm_malloc_zone_t)main_zone)\" failed (/Library/Caches/com.apple.xbs/Sources/libmalloc_exclavekit/src/xzone/xzone_malloc.c:5538)"
+ "malloc assertion \"_xzm_malloc_zone_is_main((xzm_malloc_zone_t)main_zone)\" failed (/Library/Caches/com.apple.xbs/Sources/libmalloc_exclavekit/src/xzone/xzone_malloc.c:5547)"
+ "malloc assertion \"_xzm_malloc_zone_is_xzm(main_zone)\" failed (/Library/Caches/com.apple.xbs/Sources/libmalloc_exclavekit/src/xzone/xzone_malloc.c:5528)"
+ "malloc assertion \"_xzm_malloc_zone_is_xzm(main_zone)\" failed (/Library/Caches/com.apple.xbs/Sources/libmalloc_exclavekit/src/xzone/xzone_malloc.c:5537)"
+ "malloc assertion \"_xzm_malloc_zone_is_xzm(main_zone)\" failed (/Library/Caches/com.apple.xbs/Sources/libmalloc_exclavekit/src/xzone/xzone_malloc.c:5546)"
+ "malloc assertion \"_xzm_slice_meta_is_batch_pointer(zone, chunk)\" failed (/Library/Caches/com.apple.xbs/Sources/libmalloc_exclavekit/src/xzone/xzone_malloc.c:5263)"
+ "malloc assertion \"_xzm_slice_meta_is_batch_pointer(zone, chunk)\" failed (/Library/Caches/com.apple.xbs/Sources/libmalloc_exclavekit/src/xzone/xzone_malloc.c:5427)"
+ "malloc assertion \"_xzm_slice_meta_is_batch_pointer(zone, chunk2)\" failed (/Library/Caches/com.apple.xbs/Sources/libmalloc_exclavekit/src/xzone/xzone_malloc.c:5280)"
+ "malloc assertion \"alignment <= XZM_SMALL_BLOCK_SIZE_MAX\" failed (/Library/Caches/com.apple.xbs/Sources/libmalloc_exclavekit/src/xzone/xzone_malloc.c:3489)"
+ "malloc assertion \"chunk->xzc_bits.xzcb_kind == XZM_SLICE_KIND_SMALL_CHUNK\" failed (/Library/Caches/com.apple.xbs/Sources/libmalloc_exclavekit/src/xzone/xzone_malloc.c:3693)"
+ "malloc assertion \"chunk->xzc_bits.xzcb_kind == kind\" failed (/Library/Caches/com.apple.xbs/Sources/libmalloc_exclavekit/src/xzone/xzone_malloc.c:4156)"
+ "malloc assertion \"chunk->xzc_bits.xzcb_on_partial_list\" failed (/Library/Caches/com.apple.xbs/Sources/libmalloc_exclavekit/src/xzone/xzone_malloc.c:3800)"
+ "malloc assertion \"freelist_count <= old_meta.xca_free_count\" failed (/Library/Caches/com.apple.xbs/Sources/libmalloc_exclavekit/src/xzone/xzone_malloc.c:4131)"
+ "malloc assertion \"new_size\" failed (/Library/Caches/com.apple.xbs/Sources/libmalloc_exclavekit/src/xzone/xzone_malloc.c:4560)"
+ "malloc assertion \"new_zone != NULL\" failed (/Library/Caches/com.apple.xbs/Sources/libmalloc_exclavekit/src/xzone/xzone_malloc.c:7485)"
+ "malloc assertion \"old_size\" failed (/Library/Caches/com.apple.xbs/Sources/libmalloc_exclavekit/src/xzone/xzone_malloc.c:5030)"
+ "malloc assertion \"our_size != 0\" failed (/Library/Caches/com.apple.xbs/Sources/libmalloc_exclavekit/src/xzone/xzone_malloc.c:4991)"
+ "malloc assertion \"powerof2(alignment)\" failed (/Library/Caches/com.apple.xbs/Sources/libmalloc_exclavekit/src/xzone/xzone_malloc.c:3479)"
+ "malloc assertion \"ptr\" failed (/Library/Caches/com.apple.xbs/Sources/libmalloc_exclavekit/src/xzone/xzone_malloc.c:3503)"
+ "malloc assertion \"ptr\" failed (/Library/Caches/com.apple.xbs/Sources/libmalloc_exclavekit/src/xzone/xzone_malloc.c:4559)"
+ "malloc assertion \"roundup(size, 4 * alignment) <= XZM_SMALL_BLOCK_SIZE_MAX\" failed (/Library/Caches/com.apple.xbs/Sources/libmalloc_exclavekit/src/xzone/xzone_malloc.c:3496)"
+ "malloc assertion \"segment != NULL\" failed (/Library/Caches/com.apple.xbs/Sources/libmalloc_exclavekit/src/xzone/xzone_malloc.c:4589)"
+ "malloc assertion \"size <= XZM_SMALL_BLOCK_SIZE_MAX\" failed (/Library/Caches/com.apple.xbs/Sources/libmalloc_exclavekit/src/xzone/xzone_malloc.c:3499)"
+ "malloc assertion \"slice_idx >= chunk_idx\" failed (/Library/Caches/com.apple.xbs/Sources/libmalloc_exclavekit/src/xzone/xzone_malloc.c:3723)"
+ "malloc assertion \"success\" failed (/Library/Caches/com.apple.xbs/Sources/libmalloc_exclavekit/src/xzone/xzone_malloc.c:3980)"
+ "malloc assertion \"xz\" failed (/Library/Caches/com.apple.xbs/Sources/libmalloc_exclavekit/src/xzone/xzone_malloc.c:5790)"
+ "malloc assertion \"xz->xz_block_size == chunk->xzc_tiny_block_size\" failed (/Library/Caches/com.apple.xbs/Sources/libmalloc_exclavekit/src/xzone/xzone_malloc.c:4387)"
+ "malloc assertion \"xz->xz_block_size > XZM_TINY_BLOCK_SIZE_MAX\" failed (/Library/Caches/com.apple.xbs/Sources/libmalloc_exclavekit/src/xzone/xzone_malloc.c:5254)"
+ "malloc assertion \"xz->xz_chunk_capacity == chunk->xzc_tiny_chunk_capacity\" failed (/Library/Caches/com.apple.xbs/Sources/libmalloc_exclavekit/src/xzone/xzone_malloc.c:4388)"
+ "malloc assertion \"xz->xz_chunkq_batch_count <= batch_size\" failed (/Library/Caches/com.apple.xbs/Sources/libmalloc_exclavekit/src/xzone/xzone_malloc.c:3739)"
+ "malloc assertion \"xzone_count <= UINT8_MAX\" failed (/Library/Caches/com.apple.xbs/Sources/libmalloc_exclavekit/src/xzone/xzone_malloc.c:6384)"
- "malloc assertion \"!_xzm_chunk_is_full(zone, xz, chunk)\" failed (/Library/Caches/com.apple.xbs/Sources/libmalloc_exclavekit/src/xzone/xzone_malloc.c:3841)"
- "malloc assertion \"!_xzm_slice_kind_uses_xzones(chunk->xzc_bits.xzcb_kind) || block_index < xz->xz_chunk_capacity\" failed (/Library/Caches/com.apple.xbs/Sources/libmalloc_exclavekit/src/xzone/xzone_malloc.c:4266)"
- "malloc assertion \"!old_meta.xca_walk_locked\" failed (/Library/Caches/com.apple.xbs/Sources/libmalloc_exclavekit/src/xzone/xzone_malloc.c:3943)"
- "malloc assertion \"!xz\" failed (/Library/Caches/com.apple.xbs/Sources/libmalloc_exclavekit/src/xzone/xzone_malloc.c:4373)"
- "malloc assertion \"(uintptr_t)ptr % alignment == 0\" failed (/Library/Caches/com.apple.xbs/Sources/libmalloc_exclavekit/src/xzone/xzone_malloc.c:3500)"
- "malloc assertion \"(uintptr_t)slots >= (uintptr_t)xzones + sizeof(struct xzm_xzone_s) * xzone_count\" failed (/Library/Caches/com.apple.xbs/Sources/libmalloc_exclavekit/src/xzone/xzone_malloc.c:5976)"
- "malloc assertion \"(uintptr_t)zone + size >= (uintptr_t)slots + sizeof(struct xzm_xzone_allocation_slot_s) * xzone_count * slot_count\" failed (/Library/Caches/com.apple.xbs/Sources/libmalloc_exclavekit/src/xzone/xzone_malloc.c:5974)"
- "malloc assertion \"2 * alignment <= XZM_SMALL_BLOCK_SIZE_MAX\" failed (/Library/Caches/com.apple.xbs/Sources/libmalloc_exclavekit/src/xzone/xzone_malloc.c:3488)"
- "malloc assertion \"_xzm_malloc_zone_is_main((xzm_malloc_zone_t)main_zone)\" failed (/Library/Caches/com.apple.xbs/Sources/libmalloc_exclavekit/src/xzone/xzone_malloc.c:5525)"
- "malloc assertion \"_xzm_malloc_zone_is_main((xzm_malloc_zone_t)main_zone)\" failed (/Library/Caches/com.apple.xbs/Sources/libmalloc_exclavekit/src/xzone/xzone_malloc.c:5534)"
- "malloc assertion \"_xzm_malloc_zone_is_main((xzm_malloc_zone_t)main_zone)\" failed (/Library/Caches/com.apple.xbs/Sources/libmalloc_exclavekit/src/xzone/xzone_malloc.c:5543)"
- "malloc assertion \"_xzm_malloc_zone_is_xzm(main_zone)\" failed (/Library/Caches/com.apple.xbs/Sources/libmalloc_exclavekit/src/xzone/xzone_malloc.c:5524)"
- "malloc assertion \"_xzm_malloc_zone_is_xzm(main_zone)\" failed (/Library/Caches/com.apple.xbs/Sources/libmalloc_exclavekit/src/xzone/xzone_malloc.c:5533)"
- "malloc assertion \"_xzm_malloc_zone_is_xzm(main_zone)\" failed (/Library/Caches/com.apple.xbs/Sources/libmalloc_exclavekit/src/xzone/xzone_malloc.c:5542)"
- "malloc assertion \"_xzm_slice_meta_is_batch_pointer(zone, chunk)\" failed (/Library/Caches/com.apple.xbs/Sources/libmalloc_exclavekit/src/xzone/xzone_malloc.c:5259)"
- "malloc assertion \"_xzm_slice_meta_is_batch_pointer(zone, chunk)\" failed (/Library/Caches/com.apple.xbs/Sources/libmalloc_exclavekit/src/xzone/xzone_malloc.c:5423)"
- "malloc assertion \"_xzm_slice_meta_is_batch_pointer(zone, chunk2)\" failed (/Library/Caches/com.apple.xbs/Sources/libmalloc_exclavekit/src/xzone/xzone_malloc.c:5276)"
- "malloc assertion \"alignment <= XZM_SMALL_BLOCK_SIZE_MAX\" failed (/Library/Caches/com.apple.xbs/Sources/libmalloc_exclavekit/src/xzone/xzone_malloc.c:3485)"
- "malloc assertion \"chunk->xzc_bits.xzcb_kind == XZM_SLICE_KIND_SMALL_CHUNK\" failed (/Library/Caches/com.apple.xbs/Sources/libmalloc_exclavekit/src/xzone/xzone_malloc.c:3689)"
- "malloc assertion \"chunk->xzc_bits.xzcb_kind == kind\" failed (/Library/Caches/com.apple.xbs/Sources/libmalloc_exclavekit/src/xzone/xzone_malloc.c:4152)"
- "malloc assertion \"chunk->xzc_bits.xzcb_on_partial_list\" failed (/Library/Caches/com.apple.xbs/Sources/libmalloc_exclavekit/src/xzone/xzone_malloc.c:3796)"
- "malloc assertion \"freelist_count <= old_meta.xca_free_count\" failed (/Library/Caches/com.apple.xbs/Sources/libmalloc_exclavekit/src/xzone/xzone_malloc.c:4127)"
- "malloc assertion \"new_size\" failed (/Library/Caches/com.apple.xbs/Sources/libmalloc_exclavekit/src/xzone/xzone_malloc.c:4556)"
- "malloc assertion \"new_zone != NULL\" failed (/Library/Caches/com.apple.xbs/Sources/libmalloc_exclavekit/src/xzone/xzone_malloc.c:7481)"
- "malloc assertion \"old_size\" failed (/Library/Caches/com.apple.xbs/Sources/libmalloc_exclavekit/src/xzone/xzone_malloc.c:5026)"
- "malloc assertion \"our_size != 0\" failed (/Library/Caches/com.apple.xbs/Sources/libmalloc_exclavekit/src/xzone/xzone_malloc.c:4987)"
- "malloc assertion \"powerof2(alignment)\" failed (/Library/Caches/com.apple.xbs/Sources/libmalloc_exclavekit/src/xzone/xzone_malloc.c:3475)"
- "malloc assertion \"ptr\" failed (/Library/Caches/com.apple.xbs/Sources/libmalloc_exclavekit/src/xzone/xzone_malloc.c:3499)"
- "malloc assertion \"ptr\" failed (/Library/Caches/com.apple.xbs/Sources/libmalloc_exclavekit/src/xzone/xzone_malloc.c:4555)"
- "malloc assertion \"roundup(size, 4 * alignment) <= XZM_SMALL_BLOCK_SIZE_MAX\" failed (/Library/Caches/com.apple.xbs/Sources/libmalloc_exclavekit/src/xzone/xzone_malloc.c:3492)"
- "malloc assertion \"segment != NULL\" failed (/Library/Caches/com.apple.xbs/Sources/libmalloc_exclavekit/src/xzone/xzone_malloc.c:4585)"
- "malloc assertion \"size <= XZM_SMALL_BLOCK_SIZE_MAX\" failed (/Library/Caches/com.apple.xbs/Sources/libmalloc_exclavekit/src/xzone/xzone_malloc.c:3495)"
- "malloc assertion \"slice_idx >= chunk_idx\" failed (/Library/Caches/com.apple.xbs/Sources/libmalloc_exclavekit/src/xzone/xzone_malloc.c:3719)"
- "malloc assertion \"success\" failed (/Library/Caches/com.apple.xbs/Sources/libmalloc_exclavekit/src/xzone/xzone_malloc.c:3976)"
- "malloc assertion \"xz\" failed (/Library/Caches/com.apple.xbs/Sources/libmalloc_exclavekit/src/xzone/xzone_malloc.c:5786)"
- "malloc assertion \"xz->xz_block_size == chunk->xzc_tiny_block_size\" failed (/Library/Caches/com.apple.xbs/Sources/libmalloc_exclavekit/src/xzone/xzone_malloc.c:4383)"
- "malloc assertion \"xz->xz_block_size > XZM_TINY_BLOCK_SIZE_MAX\" failed (/Library/Caches/com.apple.xbs/Sources/libmalloc_exclavekit/src/xzone/xzone_malloc.c:5250)"
- "malloc assertion \"xz->xz_chunk_capacity == chunk->xzc_tiny_chunk_capacity\" failed (/Library/Caches/com.apple.xbs/Sources/libmalloc_exclavekit/src/xzone/xzone_malloc.c:4384)"
- "malloc assertion \"xz->xz_chunkq_batch_count <= batch_size\" failed (/Library/Caches/com.apple.xbs/Sources/libmalloc_exclavekit/src/xzone/xzone_malloc.c:3735)"
- "malloc assertion \"xzone_count <= UINT8_MAX\" failed (/Library/Caches/com.apple.xbs/Sources/libmalloc_exclavekit/src/xzone/xzone_malloc.c:6380)"

```
