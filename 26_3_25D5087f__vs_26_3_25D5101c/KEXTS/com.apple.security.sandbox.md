## com.apple.security.sandbox

> `com.apple.security.sandbox`

```diff

-2680.80.14.0.0
+2680.80.17.0.0
   __TEXT.__os_log: 0x1fae
   __TEXT.__const: 0x1f33f
-  __TEXT.__cstring: 0x78b6
-  __TEXT_EXEC.__text: 0x4e064
+  __TEXT.__cstring: 0x7930
+  __TEXT_EXEC.__text: 0x4e178
   __TEXT_EXEC.__auth_stubs: 0x0
   __DATA.__data: 0x2c8
   __DATA.__bss: 0x7f128

   __DATA_CONST.__const: 0x3d18
   __DATA_CONST.__kalloc_type: 0x13c0
   __DATA_CONST.__kalloc_var: 0x4b0
-  UUID: 1F2F1550-A71F-368E-9B35-65E84DAD38CA
+  UUID: 4F1BEA07-4571-39FE-BF3B-7E1D73093D4F
   Functions: 927
   Symbols:   1980
-  CStrings:  1512
+  CStrings:  1516
 
Symbols:
+ __block_descriptor_tmp.1.2404
+ __block_descriptor_tmp.1018
+ __block_descriptor_tmp.11.2642
+ __block_descriptor_tmp.11.3061
+ __block_descriptor_tmp.12.1501
+ __block_descriptor_tmp.12.2599
+ __block_descriptor_tmp.13.1581
+ __block_descriptor_tmp.13.1740
+ __block_descriptor_tmp.1355
+ __block_descriptor_tmp.1408
+ __block_descriptor_tmp.1470
+ __block_descriptor_tmp.15.2651
+ __block_descriptor_tmp.15.3036
+ __block_descriptor_tmp.1577
+ __block_descriptor_tmp.16.1019
+ __block_descriptor_tmp.1738
+ __block_descriptor_tmp.21.3051
+ __block_descriptor_tmp.23.2618
+ __block_descriptor_tmp.2412
+ __block_descriptor_tmp.2495
+ __block_descriptor_tmp.25.1476
+ __block_descriptor_tmp.25.2672
+ __block_descriptor_tmp.2596
+ __block_descriptor_tmp.2633
+ __block_descriptor_tmp.2697
+ __block_descriptor_tmp.300
+ __block_descriptor_tmp.3045
+ __block_descriptor_tmp.5.2423
+ __block_descriptor_tmp.5.3050
+ __block_descriptor_tmp.66
+ __block_descriptor_tmp.7.1431
+ __block_descriptor_tmp.7.1739
+ __block_descriptor_tmp.8.2638
+ __block_descriptor_tmp.8.3056
+ __block_descriptor_tmp.9.2515
+ __block_literal_global.1353
+ __block_literal_global.2403
+ __block_literal_global.2597
+ __block_literal_global.2649
+ __block_literal_global.2670
+ __block_literal_global.302
+ _block_invoke._os_log_fmt.2615
+ _derive_app_container_id
+ approval_do_callout._os_log_fmt.310
+ approval_response_wait._os_log_fmt.312
+ approval_response_wait._os_log_fmt.313
+ creation_context_log_entitlement_error._os_log_fmt.20
+ free_queued_events.kalloc_type_view_1467
+ handle_microstackshot.kalloc_type_view_1844
+ macl_lock_group.1416
+ operation_names.2713
+ pending_swap_list.2436
+ sandbox_lock_grp.1475
+ sb_user_approval._os_log_fmt.33
+ sb_user_approval._os_log_fmt.38
+ sb_user_approval._os_log_fmt.40
+ schedule_microstackshot.kalloc_type_view_1675
+ schedule_microstackshot.kalloc_type_view_1688
+ schedule_microstackshot.kalloc_type_view_1702
+ submit_queued_events_to_sandboxd.kalloc_type_view_1551
+ thread_ustackshot_destroy.kalloc_type_view_1621
- __block_descriptor_tmp.1.2402
- __block_descriptor_tmp.1016
- __block_descriptor_tmp.11.2640
- __block_descriptor_tmp.11.3058
- __block_descriptor_tmp.12.1499
- __block_descriptor_tmp.12.2597
- __block_descriptor_tmp.13.1579
- __block_descriptor_tmp.13.1738
- __block_descriptor_tmp.1353
- __block_descriptor_tmp.1406
- __block_descriptor_tmp.1468
- __block_descriptor_tmp.15.2649
- __block_descriptor_tmp.15.3033
- __block_descriptor_tmp.1575
- __block_descriptor_tmp.16.1017
- __block_descriptor_tmp.1736
- __block_descriptor_tmp.21.3048
- __block_descriptor_tmp.23.2616
- __block_descriptor_tmp.2410
- __block_descriptor_tmp.2493
- __block_descriptor_tmp.25.1474
- __block_descriptor_tmp.25.2670
- __block_descriptor_tmp.2594
- __block_descriptor_tmp.2631
- __block_descriptor_tmp.2695
- __block_descriptor_tmp.298.2751
- __block_descriptor_tmp.3042
- __block_descriptor_tmp.5.2421
- __block_descriptor_tmp.5.3047
- __block_descriptor_tmp.67
- __block_descriptor_tmp.7.1429
- __block_descriptor_tmp.7.1737
- __block_descriptor_tmp.8.2636
- __block_descriptor_tmp.8.3053
- __block_descriptor_tmp.9.2513
- __block_literal_global.1351
- __block_literal_global.2401
- __block_literal_global.2595
- __block_literal_global.2647
- __block_literal_global.2668
- __block_literal_global.300
- _block_invoke._os_log_fmt.2613
- _derive_third_party_group_container_id
- approval_do_callout._os_log_fmt.306
- approval_response_wait._os_log_fmt.310
- approval_response_wait._os_log_fmt.311
- creation_context_log_entitlement_error._os_log_fmt.18
- free_queued_events.kalloc_type_view_1465
- handle_microstackshot.kalloc_type_view_1842
- macl_lock_group.1414
- operation_names.2711
- pending_swap_list.2434
- sandbox_lock_grp.1473
- sb_user_approval._os_log_fmt.34
- sb_user_approval._os_log_fmt.39
- sb_user_approval._os_log_fmt.41
- schedule_microstackshot.kalloc_type_view_1673
- schedule_microstackshot.kalloc_type_view_1686
- schedule_microstackshot.kalloc_type_view_1700
- submit_queued_events_to_sandboxd.kalloc_type_view_1549
- thread_ustackshot_destroy.kalloc_type_view_1619
Functions:
~ _eval : 8684 -> 8724
~ _hook_vnode_check_exec : 900 -> 988
~ _serialize_context : 9252 -> 9284
~ _derive_third_party_group_container_id -> _derive_app_container_id : 288 -> 404
CStrings:
+ "/library/containers/"
+ "PrivateAppGroupContainers"
+ "com.apple.private.security.sandbox-spawnattrs"
+ "forbidden-sandbox-spawnattrs"

```
