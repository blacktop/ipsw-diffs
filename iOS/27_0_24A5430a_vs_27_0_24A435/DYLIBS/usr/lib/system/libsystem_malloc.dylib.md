## libsystem_malloc.dylib

> `/usr/lib/system/libsystem_malloc.dylib`

```diff

 886.0.8.0.0
-  __TEXT.__text: 0x43304
+  __TEXT.__text: 0x43484
   __TEXT.__const: 0x614
   __TEXT.__cstring: 0xb5c5
   __TEXT.__dof_magmalloc: 0x912
Functions:
~ __xzm_free : 1932 -> 1940
~ __xzm_xzone_malloc_small : 2300 -> 2304
~ __xzm_xzone_chunk_madvise_free_slices : 328 -> 332
~ _mfm_alloc : 1060 -> 1068
~ _mfm_free : 1620 -> 1628
~ __xzm_initialize_const_zone_data : 1344 -> 1348
~ __xzm_segment_group_span_mark_smaller : 496 -> 476
~ _tiny_malloc_from_free_list : 1852 -> 1856
~ _tiny_free_list_add_ptr : 620 -> 624
~ _free_tiny : 844 -> 848
~ _tiny_free_no_lock : 2060 -> 2072
~ _free_small : 1804 -> 1808
~ _tiny_try_realloc_in_place : 1484 -> 1488
~ _tiny_size : 452 -> 456
~ _small_size : 244 -> 252
~ _small_try_realloc_in_place : 756 -> 760
~ _tiny_memalign : 760 -> 768
~ _tiny_try_shrink_in_place : 332 -> 336
~ _small_memalign : 788 -> 796
~ __xzm_segment_group_segment_free : 412 -> 416
~ _tiny_finalize_region : 456 -> 460
~ _rack_init : 332 -> 336
~ __xzm_xzone_malloc_small_freelist : 1212 -> 1220
~ _mfmi_enumerator : 464 -> 460
~ _bitarray_set : 412 -> 420
~ _bitarray_zap : 556 -> 564
~ _scalable_zone_info_task : 604 -> 612
~ _scalable_zone_statistics : 364 -> 372
~ _szone_force_lock : 484 -> 492
~ _szone_force_unlock : 284 -> 292
~ _szone_locked : 416 -> 424
~ _szone_reinit_lock : 100 -> 108
~ _szone_statistics_task : 536 -> 544
~ _szone_check_all : 456 -> 460
~ _szone_print : 1288 -> 1296
~ _small_try_shrink_in_place : 380 -> 384
~ _small_check_region : 948 -> 968
~ _small_in_use_enumerator : 868 -> 884
~ _print_small_free_list : 800 -> 804
~ _small_free_list_check : 720 -> 724
~ _print_mfm_arena : 736 -> 740
~ __xzm_introspect_chunk_blocks : 1496 -> 1476
~ _check_metadata : 112 -> 116
~ _nanov2_malloc : 572 -> 580
~ _nanov2_malloc_type : 580 -> 588
~ _nanov2_madvise_block : 220 -> 224
~ _nanov2_calloc : 696 -> 704
~ _nanov2_calloc_type : 704 -> 712
~ _nanov2_malloc_zero_on_alloc : 616 -> 624
~ _nanov2_malloc_type_zero_on_alloc : 628 -> 636
~ _nanov2_pressure_relief : 684 -> 692
~ _nanov2_find_block_and_allocate : 1528 -> 1540
~ _nanov2_allocate_from_block : 352 -> 356
~ _nanov2_create_zone : 1072 -> 1080
~ _nanov2_ptr_in_use_enumerator : 1500 -> 1516
~ _nanov2_print : 1552 -> 1568
~ _nanov2_statistics : 752 -> 756
~ _tiny_check_region : 1540 -> 1552
~ _tiny_in_use_enumerator : 1048 -> 1064
~ _tiny_batch_free : 732 -> 736
~ _print_tiny_free_list : 576 -> 580
~ _tiny_free_list_check : 668 -> 672
~ _tiny_check : 380 -> 384
```
