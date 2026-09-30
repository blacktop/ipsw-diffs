## libsystem_malloc_debug.dylib

> `/System/DriverKit/usr/lib/system/libsystem_malloc_debug.dylib`

```diff

-646.0.9.0.0
-  __TEXT.__text: 0x94ca4
+646.0.10.0.0
+  __TEXT.__text: 0x94d00
   __TEXT.__auth_stubs: 0x6b0
   __TEXT.__const: 0x614
   __TEXT.__cstring: 0x14af4
CStrings:
+ "BUG IN LIBMALLOC: malloc assertion \"!chunk->xzc_bits.xzcb_enqueued\" failed (/Library/Caches/com.apple.xbs/Sources/libmalloc_driverkit/src/xzone/xzone_malloc.c:3934)"
+ "BUG IN LIBMALLOC: malloc assertion \"!chunk->xzc_bits.xzcb_preallocated\" failed (/Library/Caches/com.apple.xbs/Sources/libmalloc_driverkit/src/xzone/xzone_malloc.c:3916)"
+ "BUG IN LIBMALLOC: malloc assertion \"!chunk->xzc_bits.xzcb_preallocated\" failed (/Library/Caches/com.apple.xbs/Sources/libmalloc_driverkit/src/xzone/xzone_malloc.c:3922)"
+ "BUG IN LIBMALLOC: malloc assertion \"!chunk->xzc_bits.xzcb_preallocated\" failed (/Library/Caches/com.apple.xbs/Sources/libmalloc_driverkit/src/xzone/xzone_malloc.c:3932)"
+ "BUG IN LIBMALLOC: malloc assertion \"!chunk->xzc_bits.xzcb_preallocated\" failed (/Library/Caches/com.apple.xbs/Sources/libmalloc_driverkit/src/xzone/xzone_malloc.c:3955)"
+ "BUG IN LIBMALLOC: malloc assertion \"(uintptr_t)slots >= (uintptr_t)xzones + sizeof(struct xzm_xzone_s) * xzone_count\" failed (/Library/Caches/com.apple.xbs/Sources/libmalloc_driverkit/src/xzone/xzone_malloc.c:4276)"
+ "BUG IN LIBMALLOC: malloc assertion \"(uintptr_t)zone + size >= (uintptr_t)slots + sizeof(struct xzm_xzone_allocation_slot_s) * xzone_count * slot_count\" failed (/Library/Caches/com.apple.xbs/Sources/libmalloc_driverkit/src/xzone/xzone_malloc.c:4274)"
+ "BUG IN LIBMALLOC: malloc assertion \"_xzm_malloc_zone_is_main((xzm_malloc_zone_t)main_zone)\" failed (/Library/Caches/com.apple.xbs/Sources/libmalloc_driverkit/src/xzone/xzone_malloc.c:3853)"
+ "BUG IN LIBMALLOC: malloc assertion \"_xzm_malloc_zone_is_main((xzm_malloc_zone_t)main_zone)\" failed (/Library/Caches/com.apple.xbs/Sources/libmalloc_driverkit/src/xzone/xzone_malloc.c:3862)"
+ "BUG IN LIBMALLOC: malloc assertion \"_xzm_malloc_zone_is_main((xzm_malloc_zone_t)main_zone)\" failed (/Library/Caches/com.apple.xbs/Sources/libmalloc_driverkit/src/xzone/xzone_malloc.c:3871)"
+ "BUG IN LIBMALLOC: malloc assertion \"_xzm_malloc_zone_is_xzm(main_zone)\" failed (/Library/Caches/com.apple.xbs/Sources/libmalloc_driverkit/src/xzone/xzone_malloc.c:3852)"
+ "BUG IN LIBMALLOC: malloc assertion \"_xzm_malloc_zone_is_xzm(main_zone)\" failed (/Library/Caches/com.apple.xbs/Sources/libmalloc_driverkit/src/xzone/xzone_malloc.c:3861)"
+ "BUG IN LIBMALLOC: malloc assertion \"_xzm_malloc_zone_is_xzm(main_zone)\" failed (/Library/Caches/com.apple.xbs/Sources/libmalloc_driverkit/src/xzone/xzone_malloc.c:3870)"
+ "BUG IN LIBMALLOC: malloc assertion \"boothash_prefix_value <= UINT32_MAX\" failed (/Library/Caches/com.apple.xbs/Sources/libmalloc_driverkit/src/xzone/xzone_malloc.c:4539)"
+ "BUG IN LIBMALLOC: malloc assertion \"chunk->xzc_alloc_idx == j+1\" failed (/Library/Caches/com.apple.xbs/Sources/libmalloc_driverkit/src/xzone/xzone_malloc.c:3933)"
+ "BUG IN LIBMALLOC: malloc assertion \"chunk->xzc_atomic_meta.xca_alloc_head != XZM_FREE_MADVISED\" failed (/Library/Caches/com.apple.xbs/Sources/libmalloc_driverkit/src/xzone/xzone_malloc.c:3968)"
+ "BUG IN LIBMALLOC: malloc assertion \"new_zone != NULL\" failed (/Library/Caches/com.apple.xbs/Sources/libmalloc_driverkit/src/xzone/xzone_malloc.c:5399)"
+ "BUG IN LIBMALLOC: malloc assertion \"retries < 10\" failed (/Library/Caches/com.apple.xbs/Sources/libmalloc_driverkit/src/xzone/xzone_malloc.c:4001)"
+ "BUG IN LIBMALLOC: malloc assertion \"size == XZM_TINY_CHUNK_SIZE\" failed (/Library/Caches/com.apple.xbs/Sources/libmalloc_driverkit/src/xzone/xzone_malloc.c:4012)"
+ "BUG IN LIBMALLOC: malloc assertion \"span->xzc_bits.xzcb_kind == XZM_SLICE_KIND_TINY_CHUNK\" failed (/Library/Caches/com.apple.xbs/Sources/libmalloc_driverkit/src/xzone/xzone_malloc.c:3992)"
+ "BUG IN LIBMALLOC: malloc assertion \"xz\" failed (/Library/Caches/com.apple.xbs/Sources/libmalloc_driverkit/src/xzone/xzone_malloc.c:4088)"
+ "BUG IN LIBMALLOC: malloc assertion \"xz->xz_block_size > XZM_TINY_BLOCK_SIZE_MAX\" failed (/Library/Caches/com.apple.xbs/Sources/libmalloc_driverkit/src/xzone/xzone_malloc.c:3605)"
+ "BUG IN LIBMALLOC: malloc assertion \"xzone_count <= UINT8_MAX\" failed (/Library/Caches/com.apple.xbs/Sources/libmalloc_driverkit/src/xzone/xzone_malloc.c:4638)"
- "BUG IN LIBMALLOC: malloc assertion \"!chunk->xzc_bits.xzcb_enqueued\" failed (/Library/Caches/com.apple.xbs/Sources/libmalloc_driverkit/src/xzone/xzone_malloc.c:3933)"
- "BUG IN LIBMALLOC: malloc assertion \"!chunk->xzc_bits.xzcb_preallocated\" failed (/Library/Caches/com.apple.xbs/Sources/libmalloc_driverkit/src/xzone/xzone_malloc.c:3915)"
- "BUG IN LIBMALLOC: malloc assertion \"!chunk->xzc_bits.xzcb_preallocated\" failed (/Library/Caches/com.apple.xbs/Sources/libmalloc_driverkit/src/xzone/xzone_malloc.c:3921)"
- "BUG IN LIBMALLOC: malloc assertion \"!chunk->xzc_bits.xzcb_preallocated\" failed (/Library/Caches/com.apple.xbs/Sources/libmalloc_driverkit/src/xzone/xzone_malloc.c:3931)"
- "BUG IN LIBMALLOC: malloc assertion \"!chunk->xzc_bits.xzcb_preallocated\" failed (/Library/Caches/com.apple.xbs/Sources/libmalloc_driverkit/src/xzone/xzone_malloc.c:3954)"
- "BUG IN LIBMALLOC: malloc assertion \"(uintptr_t)slots >= (uintptr_t)xzones + sizeof(struct xzm_xzone_s) * xzone_count\" failed (/Library/Caches/com.apple.xbs/Sources/libmalloc_driverkit/src/xzone/xzone_malloc.c:4275)"
- "BUG IN LIBMALLOC: malloc assertion \"(uintptr_t)zone + size >= (uintptr_t)slots + sizeof(struct xzm_xzone_allocation_slot_s) * xzone_count * slot_count\" failed (/Library/Caches/com.apple.xbs/Sources/libmalloc_driverkit/src/xzone/xzone_malloc.c:4273)"
- "BUG IN LIBMALLOC: malloc assertion \"_xzm_malloc_zone_is_main((xzm_malloc_zone_t)main_zone)\" failed (/Library/Caches/com.apple.xbs/Sources/libmalloc_driverkit/src/xzone/xzone_malloc.c:3852)"
- "BUG IN LIBMALLOC: malloc assertion \"_xzm_malloc_zone_is_main((xzm_malloc_zone_t)main_zone)\" failed (/Library/Caches/com.apple.xbs/Sources/libmalloc_driverkit/src/xzone/xzone_malloc.c:3861)"
- "BUG IN LIBMALLOC: malloc assertion \"_xzm_malloc_zone_is_main((xzm_malloc_zone_t)main_zone)\" failed (/Library/Caches/com.apple.xbs/Sources/libmalloc_driverkit/src/xzone/xzone_malloc.c:3870)"
- "BUG IN LIBMALLOC: malloc assertion \"_xzm_malloc_zone_is_xzm(main_zone)\" failed (/Library/Caches/com.apple.xbs/Sources/libmalloc_driverkit/src/xzone/xzone_malloc.c:3851)"
- "BUG IN LIBMALLOC: malloc assertion \"_xzm_malloc_zone_is_xzm(main_zone)\" failed (/Library/Caches/com.apple.xbs/Sources/libmalloc_driverkit/src/xzone/xzone_malloc.c:3860)"
- "BUG IN LIBMALLOC: malloc assertion \"_xzm_malloc_zone_is_xzm(main_zone)\" failed (/Library/Caches/com.apple.xbs/Sources/libmalloc_driverkit/src/xzone/xzone_malloc.c:3869)"
- "BUG IN LIBMALLOC: malloc assertion \"boothash_prefix_value <= UINT32_MAX\" failed (/Library/Caches/com.apple.xbs/Sources/libmalloc_driverkit/src/xzone/xzone_malloc.c:4538)"
- "BUG IN LIBMALLOC: malloc assertion \"chunk->xzc_alloc_idx == j+1\" failed (/Library/Caches/com.apple.xbs/Sources/libmalloc_driverkit/src/xzone/xzone_malloc.c:3932)"
- "BUG IN LIBMALLOC: malloc assertion \"chunk->xzc_atomic_meta.xca_alloc_head != XZM_FREE_MADVISED\" failed (/Library/Caches/com.apple.xbs/Sources/libmalloc_driverkit/src/xzone/xzone_malloc.c:3967)"
- "BUG IN LIBMALLOC: malloc assertion \"new_zone != NULL\" failed (/Library/Caches/com.apple.xbs/Sources/libmalloc_driverkit/src/xzone/xzone_malloc.c:5398)"
- "BUG IN LIBMALLOC: malloc assertion \"retries < 10\" failed (/Library/Caches/com.apple.xbs/Sources/libmalloc_driverkit/src/xzone/xzone_malloc.c:4000)"
- "BUG IN LIBMALLOC: malloc assertion \"size == XZM_TINY_CHUNK_SIZE\" failed (/Library/Caches/com.apple.xbs/Sources/libmalloc_driverkit/src/xzone/xzone_malloc.c:4011)"
- "BUG IN LIBMALLOC: malloc assertion \"span->xzc_bits.xzcb_kind == XZM_SLICE_KIND_TINY_CHUNK\" failed (/Library/Caches/com.apple.xbs/Sources/libmalloc_driverkit/src/xzone/xzone_malloc.c:3991)"
- "BUG IN LIBMALLOC: malloc assertion \"xz\" failed (/Library/Caches/com.apple.xbs/Sources/libmalloc_driverkit/src/xzone/xzone_malloc.c:4087)"
- "BUG IN LIBMALLOC: malloc assertion \"xz->xz_block_size > XZM_TINY_BLOCK_SIZE_MAX\" failed (/Library/Caches/com.apple.xbs/Sources/libmalloc_driverkit/src/xzone/xzone_malloc.c:3604)"
- "BUG IN LIBMALLOC: malloc assertion \"xzone_count <= UINT8_MAX\" failed (/Library/Caches/com.apple.xbs/Sources/libmalloc_driverkit/src/xzone/xzone_malloc.c:4637)"

```
