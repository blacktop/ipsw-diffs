## libsystem_malloc_debug.dylib

> `/System/ExclaveKit/usr/lib/system/libsystem_malloc_debug.dylib`

```diff

-646.40.3.0.0
-  __TEXT.__text: 0x40eec
+657.60.19.0.0
+  __TEXT.__text: 0x40f84
   __TEXT.__auth_stubs: 0x1f0
-  __TEXT.__cstring: 0xa678
+  __TEXT.__cstring: 0xa702
   __TEXT.__const: 0x368
   __TEXT.__unwind_info: 0x320
   __TEXT.__eh_frame: 0x48
CStrings:
+ "Failed to allocate memory at address 0x%!l(MISSING)x of size 0x%!l(MISSING)x with flags %!d(MISSING): %!d(MISSING)\n"
+ "Failed to deallocate at address %!p(MISSING) of size 0x%!l(MISSING)x: %!d(MISSING)\n"
+ "Unsupported deallocation address %!p(MISSING) or size %!l(MISSING)u: %!d(MISSING)\n"
+ "malloc assertion \"!xz || xz->xz_chunk_capacity == chunk_capacity\" failed (/Library/Caches/com.apple.xbs/Sources/libmalloc_exclavekit/src/xzone/../xzone/xzone_inline_internal.h:795)"
+ "malloc assertion \"block_idx <= last_block && last_block < chunk_capacity\" failed (/Library/Caches/com.apple.xbs/Sources/libmalloc_exclavekit/src/xzone/../xzone/xzone_inline_internal.h:986)"
+ "malloc assertion \"chunk && chunk->xzc_bits.xzcb_kind == XZM_SLICE_KIND_SMALL_CHUNK\" failed (/Library/Caches/com.apple.xbs/Sources/libmalloc_exclavekit/src/xzone/../xzone/xzone_inline_internal.h:1003)"
+ "malloc assertion \"chunk && chunk->xzc_bits.xzcb_kind == XZM_SLICE_KIND_SMALL_CHUNK\" failed (/Library/Caches/com.apple.xbs/Sources/libmalloc_exclavekit/src/xzone/../xzone/xzone_inline_internal.h:948)"
+ "malloc assertion \"chunk->xzc_atomic_meta.xca_alloc_head == XZM_FREE_MADVISED\" failed (/Library/Caches/com.apple.xbs/Sources/libmalloc_exclavekit/src/xzone/../xzone/xzone_inline_internal.h:809)"
+ "malloc assertion \"chunk->xzc_atomic_meta.xca_free_count == 0\" failed (/Library/Caches/com.apple.xbs/Sources/libmalloc_exclavekit/src/xzone/../xzone/xzone_inline_internal.h:810)"
+ "malloc assertion \"chunk->xzc_bits.xzcb_kind == XZM_SLICE_KIND_SMALL_CHUNK\" failed (/Library/Caches/com.apple.xbs/Sources/libmalloc_exclavekit/src/xzone/../xzone/xzone_inline_internal.h:1105)"
+ "malloc assertion \"chunk->xzc_bits.xzcb_kind == XZM_SLICE_KIND_SMALL_CHUNK\" failed (/Library/Caches/com.apple.xbs/Sources/libmalloc_exclavekit/src/xzone/../xzone/xzone_inline_internal.h:919)"
+ "malloc assertion \"chunk->xzc_bits.xzcb_kind == XZM_SLICE_KIND_SMALL_CHUNK\" failed (/Library/Caches/com.apple.xbs/Sources/libmalloc_exclavekit/src/xzone/../xzone/xzone_inline_internal.h:929)"
+ "malloc assertion \"diff >= 0 && diff < (ptrdiff_t)rounded_size\" failed (/Library/Caches/com.apple.xbs/Sources/libmalloc_exclavekit/src/xzone/../xzone/xzone_inline_internal.h:436)"
+ "malloc assertion \"end >= start\" failed (/Library/Caches/com.apple.xbs/Sources/libmalloc_exclavekit/src/xzone/../xzone/xzone_inline_internal.h:930)"
+ "malloc assertion \"first <= last\" failed (/Library/Caches/com.apple.xbs/Sources/libmalloc_exclavekit/src/xzone/../xzone/xzone_inline_internal.h:1129)"
+ "malloc assertion \"left >= chunk_idx\" failed (/Library/Caches/com.apple.xbs/Sources/libmalloc_exclavekit/src/xzone/../xzone/xzone_inline_internal.h:1042)"
+ "malloc assertion \"map_addr == addr\" failed (/Library/Caches/com.apple.xbs/Sources/libmalloc_exclavekit/src/xzone/../xzone/xzone_inline_internal.h:399)"
+ "malloc assertion \"offset >= chunk_idx * XZM_SEGMENT_SLICE_SIZE\" failed (/Library/Caches/com.apple.xbs/Sources/libmalloc_exclavekit/src/xzone/../xzone/xzone_inline_internal.h:716)"
+ "malloc assertion \"out_slice >= ((xzm_segment_t)((uintptr_t)slice & ~(XZM_METAPOOL_SEGMENT_BLOCK_SIZE - 1)))->xzs_slices\" failed (/Library/Caches/com.apple.xbs/Sources/libmalloc_exclavekit/src/xzone/../xzone/xzone_inline_internal.h:582)"
+ "malloc assertion \"right <= chunk_idx + chunk->xzcs_slice_count\" failed (/Library/Caches/com.apple.xbs/Sources/libmalloc_exclavekit/src/xzone/../xzone/xzone_inline_internal.h:1051)"
+ "malloc assertion \"slice >= span\" failed (/Library/Caches/com.apple.xbs/Sources/libmalloc_exclavekit/src/xzone/../xzone/xzone_inline_internal.h:560)"
+ "malloc assertion \"span <= 32\" failed (/Library/Caches/com.apple.xbs/Sources/libmalloc_exclavekit/src/xzone/../xzone/xzone_inline_internal.h:934)"
- "Failed to allocate memory at address 0x%!l(MISSING)x of size 0x%!l(MISSING)x with flags %!d(MISSING)\n"
- "Failed to deallocate at address %!p(MISSING) of size 0x%!l(MISSING)x\n"
- "Unsupported deallocation address %!p(MISSING) or size %!l(MISSING)u\n"
- "malloc assertion \"!xz || xz->xz_chunk_capacity == chunk_capacity\" failed (/Library/Caches/com.apple.xbs/Sources/libmalloc_exclavekit/src/xzone/../xzone/xzone_inline_internal.h:797)"
- "malloc assertion \"block_idx <= last_block && last_block < chunk_capacity\" failed (/Library/Caches/com.apple.xbs/Sources/libmalloc_exclavekit/src/xzone/../xzone/xzone_inline_internal.h:988)"
- "malloc assertion \"chunk && chunk->xzc_bits.xzcb_kind == XZM_SLICE_KIND_SMALL_CHUNK\" failed (/Library/Caches/com.apple.xbs/Sources/libmalloc_exclavekit/src/xzone/../xzone/xzone_inline_internal.h:1005)"
- "malloc assertion \"chunk && chunk->xzc_bits.xzcb_kind == XZM_SLICE_KIND_SMALL_CHUNK\" failed (/Library/Caches/com.apple.xbs/Sources/libmalloc_exclavekit/src/xzone/../xzone/xzone_inline_internal.h:950)"
- "malloc assertion \"chunk->xzc_atomic_meta.xca_alloc_head == XZM_FREE_MADVISED\" failed (/Library/Caches/com.apple.xbs/Sources/libmalloc_exclavekit/src/xzone/../xzone/xzone_inline_internal.h:811)"
- "malloc assertion \"chunk->xzc_atomic_meta.xca_free_count == 0\" failed (/Library/Caches/com.apple.xbs/Sources/libmalloc_exclavekit/src/xzone/../xzone/xzone_inline_internal.h:812)"
- "malloc assertion \"chunk->xzc_bits.xzcb_kind == XZM_SLICE_KIND_SMALL_CHUNK\" failed (/Library/Caches/com.apple.xbs/Sources/libmalloc_exclavekit/src/xzone/../xzone/xzone_inline_internal.h:1107)"
- "malloc assertion \"chunk->xzc_bits.xzcb_kind == XZM_SLICE_KIND_SMALL_CHUNK\" failed (/Library/Caches/com.apple.xbs/Sources/libmalloc_exclavekit/src/xzone/../xzone/xzone_inline_internal.h:921)"
- "malloc assertion \"chunk->xzc_bits.xzcb_kind == XZM_SLICE_KIND_SMALL_CHUNK\" failed (/Library/Caches/com.apple.xbs/Sources/libmalloc_exclavekit/src/xzone/../xzone/xzone_inline_internal.h:931)"
- "malloc assertion \"diff >= 0 && diff < (ptrdiff_t)rounded_size\" failed (/Library/Caches/com.apple.xbs/Sources/libmalloc_exclavekit/src/xzone/../xzone/xzone_inline_internal.h:438)"
- "malloc assertion \"end >= start\" failed (/Library/Caches/com.apple.xbs/Sources/libmalloc_exclavekit/src/xzone/../xzone/xzone_inline_internal.h:932)"
- "malloc assertion \"first <= last\" failed (/Library/Caches/com.apple.xbs/Sources/libmalloc_exclavekit/src/xzone/../xzone/xzone_inline_internal.h:1131)"
- "malloc assertion \"left >= chunk_idx\" failed (/Library/Caches/com.apple.xbs/Sources/libmalloc_exclavekit/src/xzone/../xzone/xzone_inline_internal.h:1044)"
- "malloc assertion \"offset >= chunk_idx * XZM_SEGMENT_SLICE_SIZE\" failed (/Library/Caches/com.apple.xbs/Sources/libmalloc_exclavekit/src/xzone/../xzone/xzone_inline_internal.h:718)"
- "malloc assertion \"out_slice >= ((xzm_segment_t)((uintptr_t)slice & ~(XZM_METAPOOL_SEGMENT_BLOCK_SIZE - 1)))->xzs_slices\" failed (/Library/Caches/com.apple.xbs/Sources/libmalloc_exclavekit/src/xzone/../xzone/xzone_inline_internal.h:584)"
- "malloc assertion \"right <= chunk_idx + chunk->xzcs_slice_count\" failed (/Library/Caches/com.apple.xbs/Sources/libmalloc_exclavekit/src/xzone/../xzone/xzone_inline_internal.h:1053)"
- "malloc assertion \"slice >= span\" failed (/Library/Caches/com.apple.xbs/Sources/libmalloc_exclavekit/src/xzone/../xzone/xzone_inline_internal.h:562)"
- "malloc assertion \"span <= 32\" failed (/Library/Caches/com.apple.xbs/Sources/libmalloc_exclavekit/src/xzone/../xzone/xzone_inline_internal.h:936)"
- "populate of chunk failed"

```
