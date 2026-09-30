## libsystem_malloc_debug.dylib

> `/System/DriverKit/usr/lib/system/libsystem_malloc_debug.dylib`

### Sections with Same Size but Changed Content

- `__TEXT.__dof_magmalloc`
- `__TEXT.__unwind_info`
- `__TEXT.__eh_frame`
- `__DATA_CONST.__const`
- `__AUTH_CONST.__const`
- `__AUTH.__data`
- `__AUTH.__v_zone`

```diff

 886.0.8.0.0
-  __TEXT.__text: 0xf0b64
+  __TEXT.__text: 0xf0ed4
   __TEXT.__const: 0x69f
   __TEXT.__cstring: 0x30b45
   __TEXT.__dof_magmalloc: 0x8c7
Functions:
~ _bitarray_set : 752 -> 756
~ _bitarray_zap : 752 -> 756
~ _bitarray_zap_first_set : 1388 -> 1392
~ _xzm_chunk_mark_free : 2388 -> 2392
~ _xzm_chunk_mark_used : 2612 -> 2616
~ _xzm_guard_slot_mark_free : 2448 -> 2456
~ _xzm_guard_slot_mark_used : 2672 -> 2680
~ __xzm_segment_group_update_guard_chunk_generic : 3340 -> 3356
~ _xzm_segment_group_alloc_chunk : 4384 -> 4388
~ __xzm_segment_group_alloc_huge_chunk : 3016 -> 3024
~ __xzm_segment_group_find_and_allocate_chunk : 4592 -> 4596
~ _xzm_segment_group_segment_madvise_chunk : 1460 -> 1464
~ _xzm_guard_slot_overwrite : 2228 -> 2236
~ _xzm_segment_group_free_chunk : 4180 -> 4188
~ __xzm_segment_group_free_huge_chunk : 664 -> 668
~ __xzm_segment_group_segment_is_valid : 3380 -> 3388
~ __xzm_segment_group_segment_span_free_coalesce : 2480 -> 2496
~ __xzm_segment_group_segment_free : 1324 -> 1332
~ __xzm_segment_group_span_mark_free : 1040 -> 1044
~ _xzm_segment_group_try_realloc_large_chunk : 6072 -> 6100
~ __xzm_segment_group_span_mark_smaller : 1908 -> 1924
~ __xzm_segment_group_segment_slice_split : 1072 -> 1080
~ _xzm_segment_group_try_realloc_huge_chunk : 3056 -> 3064
~ __xzm_segment_group_init_segment : 1912 -> 1916
~ __xzm_segment_group_split_huge_segment : 1740 -> 1744
~ __xzm_segment_group_alloc_huge_chunk_from_cache : 1492 -> 1496
~ __xzm_segment_group_cache_invalidate : 184 -> 188
~ __xzm_segment_group_segment_span_init_run : 1116 -> 1124
~ __xzm_segment_group_segment_create_guard_page : 1100 -> 1120
~ __xzm_segment_group_free_huge_chunk_to_cache : 2764 -> 2768
~ __xzm_segment_group_cache_evict : 684 -> 688
~ __xzm_segment_group_span_mark_used : 1220 -> 1224
~ __xzm_segment_group_segment_span_free : 868 -> 876
~ _rack_init : 776 -> 784
~ _mfm_initialize : 628 -> 632
~ _xzm_segment_group_segment_foreach_span : 1000 -> 1008
~ __xzm_introspect_guard_chunk_slots : 864 -> 868
~ _xzm_print : 11568 -> 11576
~ __xzm_print_block_invoke.285 : 2536 -> 2544
~ ___xzm_statistics_block_invoke_3 : 960 -> 964
~ _deallocate : 660 -> 668
~ __xzm_foreach_lock : 1560 -> 1568
~ _xzm_ptr_lookup_4test : 6400 -> 6424
~ __xzm_initialize_const_zone_data : 9532 -> 9536
~ __xzm_small_xzone_lock_all : 2932 -> 2948
~ __xzm_gzone_reinit_quarantine_finish : 1548 -> 1552
~ __xzm_gzone_free_chunk : 2408 -> 2412
~ __xzm_xzone_freelist_chunk_block_is_free_slow : 3720 -> 3728
~ _xzm_malloc_zone_size : 6076 -> 6096
~ _xzm_malloc_zone_destroy : 8244 -> 8260
~ _xzm_malloc_zone_free_slow : 12396 -> 12436
~ _xzm_malloc_zone_free_definite_size_slow : 12392 -> 12432
~ _xzm_malloc_zone_try_free_default_slow : 12372 -> 12412
~ _xzm_malloc_zone_malloc_type_realloc_slow : 28612 -> 28700
~ __xzm_malloc_large_huge : 5900 -> 5904
~ __xzm_xzone_malloc_tiny : 8316 -> 8320
~ __xzm_xzone_malloc_small_freelist : 8316 -> 8320
~ __xzm_xzone_malloc_small : 7544 -> 7556
~ __xzm_xzone_malloc_from_freelist_chunk : 5332 -> 5336
~ __xzm_xzone_find_and_malloc_from_freelist_chunk : 4796 -> 4800
~ __xzm_chunk_list_pop : 1364 -> 1372
~ __xzm_xzone_malloc_from_empty_freelist_chunk : 2688 -> 2692
~ __xzm_xzone_allocate_chunk_from_isolation : 1432 -> 1436
~ __xzm_xzone_malloc_from_fresh_freelist_chunk : 2324 -> 2328
~ __xzm_xzone_chunk_memtag_init : 1044 -> 1048
~ __xzm_xzone_madvise_batch : 3212 -> 3228
~ __xzm_xzone_small_chunks_mark_empty : 2336 -> 2344
~ __xzm_xzone_alloc_from_chunk : 3252 -> 3264
~ __xzm_chunk_find_dirtiest_slice : 4352 -> 4372
~ __xzm_gzone_malloc : 4268 -> 4276
~ __xzm_gzone_reinit_quarantine : 3744 -> 3748
~ __xzm_gzone_malloc_from_chunk : 4564 -> 4576
~ __xzm_gzone_alloc_chunk : 1660 -> 1664
~ __xzm_gzone_init_chunk : 3372 -> 3376
~ __xzm_free_outlined : 5832 -> 5852
~ __xzm_xzone_madvise_freelist_chunk : 640 -> 644
~ __xzm_xzone_free_freelist : 5264 -> 5272
~ __xzm_gzone_free_slot : 5228 -> 5240
~ __xzm_free_large_huge : 944 -> 948
~ __xzm_xzone_free_to_chunk : 1612 -> 1616
~ __xzm_xzone_chunk_madvise_free_slices : 4500 -> 4516
~ __xzm_xzone_chunk_free : 3684 -> 3692
~ __xzm_gzone_free_all_slots : 2156 -> 2164
~ __xzm_realloc : 7796 -> 7820
~ __xzm_gzone_realloc : 2060 -> 2072
```
