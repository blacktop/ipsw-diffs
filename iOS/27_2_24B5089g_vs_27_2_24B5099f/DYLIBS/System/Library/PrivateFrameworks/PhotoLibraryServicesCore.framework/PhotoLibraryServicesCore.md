## PhotoLibraryServicesCore

> `/System/Library/PrivateFrameworks/PhotoLibraryServicesCore.framework/PhotoLibraryServicesCore`

```diff

-916.45.110.0.0
-  __TEXT.__text: 0xc8078
-  __TEXT.__objc_methlist: 0x8364
+916.51.202.0.0
+  __TEXT.__text: 0xc9254
+  __TEXT.__objc_methlist: 0x83d4
   __TEXT.__const: 0x23cc
   __TEXT.__dlopen_cstrs: 0x19c
-  __TEXT.__gcc_except_tab: 0x57cc
-  __TEXT.__cstring: 0x162ab
-  __TEXT.__oslogstring: 0xb37a
+  __TEXT.__gcc_except_tab: 0x5860
+  __TEXT.__cstring: 0x16311
+  __TEXT.__oslogstring: 0xb4d5
   __TEXT.__ustring: 0x4
-  __TEXT.__unwind_info: 0x42a0
+  __TEXT.__unwind_info: 0x42e8
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0
   __TEXT.__objc_classname: 0x0

   __DATA_CONST.__objc_catlist: 0x10
   __DATA_CONST.__objc_protolist: 0x160
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x4cc8
+  __DATA_CONST.__objc_selrefs: 0x4d18
   __DATA_CONST.__objc_protorefs: 0xc8
   __DATA_CONST.__objc_superrefs: 0x268
   __DATA_CONST.__objc_arraydata: 0x428
-  __DATA_CONST.__got: 0xa48
-  __AUTH_CONST.__const: 0x3660
-  __AUTH_CONST.__cfstring: 0x122e0
-  __AUTH_CONST.__objc_const: 0xaa00
+  __DATA_CONST.__got: 0xa58
+  __AUTH_CONST.__const: 0x36d0
+  __AUTH_CONST.__cfstring: 0x12380
+  __AUTH_CONST.__objc_const: 0xaa50
   __AUTH_CONST.__objc_intobj: 0x930
   __AUTH_CONST.__objc_floatobj: 0x10
   __AUTH_CONST.__objc_dictobj: 0x50
   __AUTH_CONST.__objc_arrayobj: 0x2a0
-  __AUTH_CONST.__auth_got: 0xe50
+  __AUTH_CONST.__auth_got: 0xe58
   __AUTH.__objc_data: 0xa0
-  __DATA.__objc_ivar: 0x678
+  __DATA.__objc_ivar: 0x67c
   __DATA.__data: 0x10e0
   __DATA_DIRTY.__objc_data: 0x27b0
   __DATA_DIRTY.__data: 0x8

   - /System/Library/Frameworks/VideoToolbox.framework/VideoToolbox
   - /System/Library/Frameworks/_LocationEssentials.framework/_LocationEssentials
   - /System/Library/PrivateFrameworks/AppSupport.framework/AppSupport
+  - /System/Library/PrivateFrameworks/AuthKit.framework/AuthKit
   - /System/Library/PrivateFrameworks/CMPhoto.framework/CMPhoto
   - /System/Library/PrivateFrameworks/CoreAnalytics.framework/CoreAnalytics
   - /System/Library/PrivateFrameworks/PhotoFoundation.framework/PhotoFoundation

   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libperfcheck.dylib
   - /usr/lib/libsqlite3.dylib
-  Functions: 3988
-  Symbols:   7930
-  CStrings:  3704
+  Functions: 4006
+  Symbols:   7956
+  CStrings:  3713
 
Symbols:
+ +[PLAppPrivateData _isOptedIntoLibraryPrivateDataCreationTracking]
+ -[PLAppPrivateData clearWasCreatedFlag]
+ -[PLAppPrivateData setWasNewlyCreated:]
+ -[PLAppPrivateData wasCreated]
+ -[PLAppPrivateData wasNewlyCreated]
+ -[PLAssetsdCloudInternalClient updateAccessRequestForParticipantWithUUID:toAcceptanceStatus:inCollectionShareWithIdentifier:completionHandler:]
+ -[PLAssetsdLibraryInternalClient migrateLimitedLibraryAccessFromApplication:toApplication:completionHandler:]
+ -[PLAssetsdLibraryInternalClient transferAssetsWithUuids:fromLibraryURL:transferOptions:completionHandler:]
+ -[PLAssetsdLibraryInternalClient transferPersonsWithUuids:fromLibraryURL:transferOptions:completionHandler:]
+ GCC_except_table1014
+ GCC_except_table1054
+ GCC_except_table1118
+ GCC_except_table1121
+ GCC_except_table1454
+ GCC_except_table1469
+ GCC_except_table1478
+ GCC_except_table1595
+ GCC_except_table1618
+ GCC_except_table1623
+ GCC_except_table1660
+ GCC_except_table1676
+ GCC_except_table1702
+ GCC_except_table1704
+ GCC_except_table1711
+ GCC_except_table1714
+ GCC_except_table1717
+ GCC_except_table1720
+ GCC_except_table1723
+ GCC_except_table1726
+ GCC_except_table1729
+ GCC_except_table1732
+ GCC_except_table1738
+ GCC_except_table1742
+ GCC_except_table1745
+ GCC_except_table1748
+ GCC_except_table1759
+ GCC_except_table1762
+ GCC_except_table1765
+ GCC_except_table1768
+ GCC_except_table1771
+ GCC_except_table1774
+ GCC_except_table1777
+ GCC_except_table1780
+ GCC_except_table1783
+ GCC_except_table1786
+ GCC_except_table1793
+ GCC_except_table1797
+ GCC_except_table1800
+ GCC_except_table1803
+ GCC_except_table1806
+ GCC_except_table1817
+ GCC_except_table1820
+ GCC_except_table1823
+ GCC_except_table1826
+ GCC_except_table1852
+ GCC_except_table1953
+ GCC_except_table1972
+ GCC_except_table1976
+ GCC_except_table2131
+ GCC_except_table2139
+ GCC_except_table2189
+ GCC_except_table2194
+ GCC_except_table2195
+ GCC_except_table2197
+ GCC_except_table2200
+ GCC_except_table2340
+ GCC_except_table2429
+ GCC_except_table2469
+ GCC_except_table2503
+ GCC_except_table2532
+ GCC_except_table2535
+ GCC_except_table2538
+ GCC_except_table2552
+ GCC_except_table2559
+ GCC_except_table259
+ GCC_except_table2595
+ GCC_except_table2599
+ GCC_except_table2603
+ GCC_except_table2606
+ GCC_except_table2611
+ GCC_except_table2614
+ GCC_except_table2617
+ GCC_except_table2621
+ GCC_except_table2632
+ GCC_except_table2634
+ GCC_except_table2638
+ GCC_except_table264
+ GCC_except_table2642
+ GCC_except_table2646
+ GCC_except_table2650
+ GCC_except_table2654
+ GCC_except_table2658
+ GCC_except_table2662
+ GCC_except_table2666
+ GCC_except_table267
+ GCC_except_table2670
+ GCC_except_table2674
+ GCC_except_table2678
+ GCC_except_table2682
+ GCC_except_table2686
+ GCC_except_table2690
+ GCC_except_table2694
+ GCC_except_table2697
+ GCC_except_table2701
+ GCC_except_table2705
+ GCC_except_table2709
+ GCC_except_table2713
+ GCC_except_table272
+ GCC_except_table2721
+ GCC_except_table2727
+ GCC_except_table2730
+ GCC_except_table2733
+ GCC_except_table2737
+ GCC_except_table2741
+ GCC_except_table2745
+ GCC_except_table2749
+ GCC_except_table2753
+ GCC_except_table2757
+ GCC_except_table2765
+ GCC_except_table2774
+ GCC_except_table2777
+ GCC_except_table2779
+ GCC_except_table278
+ GCC_except_table2780
+ GCC_except_table2782
+ GCC_except_table2785
+ GCC_except_table2789
+ GCC_except_table2791
+ GCC_except_table2794
+ GCC_except_table2797
+ GCC_except_table2800
+ GCC_except_table2803
+ GCC_except_table2806
+ GCC_except_table2809
+ GCC_except_table2812
+ GCC_except_table2815
+ GCC_except_table2818
+ GCC_except_table2821
+ GCC_except_table2824
+ GCC_except_table2827
+ GCC_except_table2830
+ GCC_except_table2832
+ GCC_except_table286
+ GCC_except_table2888
+ GCC_except_table294
+ GCC_except_table2955
+ GCC_except_table2958
+ GCC_except_table3015
+ GCC_except_table3080
+ GCC_except_table3082
+ GCC_except_table3086
+ GCC_except_table3088
+ GCC_except_table309
+ GCC_except_table3107
+ GCC_except_table3115
+ GCC_except_table315
+ GCC_except_table321
+ GCC_except_table3270
+ GCC_except_table3272
+ GCC_except_table3281
+ GCC_except_table3284
+ GCC_except_table3287
+ GCC_except_table3290
+ GCC_except_table3293
+ GCC_except_table3296
+ GCC_except_table3348
+ GCC_except_table3350
+ GCC_except_table3385
+ GCC_except_table3509
+ GCC_except_table3575
+ GCC_except_table3579
+ GCC_except_table3586
+ GCC_except_table3639
+ GCC_except_table3642
+ GCC_except_table3648
+ GCC_except_table3651
+ GCC_except_table3654
+ GCC_except_table3657
+ GCC_except_table3663
+ GCC_except_table3669
+ GCC_except_table3673
+ GCC_except_table3677
+ GCC_except_table3681
+ GCC_except_table3685
+ GCC_except_table3706
+ GCC_except_table3709
+ GCC_except_table3731
+ GCC_except_table3749
+ GCC_except_table3757
+ GCC_except_table3759
+ GCC_except_table3764
+ GCC_except_table3768
+ GCC_except_table3774
+ GCC_except_table3782
+ GCC_except_table3785
+ GCC_except_table381
+ GCC_except_table3812
+ GCC_except_table3818
+ GCC_except_table382
+ GCC_except_table3821
+ GCC_except_table3824
+ GCC_except_table3828
+ GCC_except_table3832
+ GCC_except_table3846
+ GCC_except_table3849
+ GCC_except_table3893
+ GCC_except_table3919
+ GCC_except_table3920
+ GCC_except_table3922
+ GCC_except_table3924
+ GCC_except_table3926
+ GCC_except_table3929
+ GCC_except_table3932
+ GCC_except_table3933
+ GCC_except_table3958
+ GCC_except_table3963
+ GCC_except_table3970
+ GCC_except_table3975
+ GCC_except_table402
+ GCC_except_table406
+ GCC_except_table415
+ GCC_except_table428
+ GCC_except_table484
+ GCC_except_table489
+ GCC_except_table517
+ GCC_except_table521
+ GCC_except_table528
+ GCC_except_table532
+ GCC_except_table538
+ GCC_except_table549
+ GCC_except_table562
+ GCC_except_table618
+ GCC_except_table680
+ GCC_except_table712
+ GCC_except_table717
+ GCC_except_table729
+ GCC_except_table742
+ GCC_except_table778
+ GCC_except_table783
+ GCC_except_table787
+ GCC_except_table820
+ GCC_except_table848
+ GCC_except_table852
+ GCC_except_table893
+ GCC_except_table895
+ GCC_except_table912
+ GCC_except_table934
+ GCC_except_table938
+ GCC_except_table955
+ _OBJC_CLASS_$_AKAccountManager
+ _OBJC_IVAR_$_PLAppPrivateData._wasNewlyCreated
+ _PLGetSandboxExtensionTokenCanonical
+ _PLGetSandboxExtensionTokenForProcessCanonical
+ _PLIsChinaAccount
+ _PLNoFollowPath
+ _PLPlatformBackgroundSearchIndexingSupported
+ _PLVettedResourcePath
+ _SANDBOX_EXTENSION_CANONICAL
+ ___107-[PLAssetsdLibraryInternalClient transferAssetsWithUuids:fromLibraryURL:transferOptions:completionHandler:]_block_invoke
+ ___108-[PLAssetsdLibraryInternalClient transferPersonsWithUuids:fromLibraryURL:transferOptions:completionHandler:]_block_invoke
+ ___109-[PLAssetsdLibraryInternalClient migrateLimitedLibraryAccessFromApplication:toApplication:completionHandler:]_block_invoke
+ ___109-[PLAssetsdLibraryInternalClient migrateLimitedLibraryAccessFromApplication:toApplication:completionHandler:]_block_invoke_2
+ ___143-[PLAssetsdCloudInternalClient updateAccessRequestForParticipantWithUUID:toAcceptanceStatus:inCollectionShareWithIdentifier:completionHandler:]_block_invoke
+ ___block_descriptor_112_e8_32s40s48bs56n18_8_8_t0w1_s8_t16w32_e51_v16?0"<PLAssetsdLibraryInternalServiceProtocol>"8l
+ ___block_descriptor_120_e8_32s40s48bs56n18_8_8_t0w1_s8_t16w32_e49_v16?0"<PLAssetsdCloudInternalServiceProtocol>"8l
+ _sLibraryURLsCreatedThisLaunch
+ _sLibraryURLsCreatedThisLaunchLock
+ _sandbox_check_by_audit_token
- -[PLAssetsdLibraryClient transferAssetsWithUuids:fromLibraryURL:transferOptions:completionHandler:]
- -[PLAssetsdLibraryClient transferPersonsWithUuids:fromLibraryURL:transferOptions:completionHandler:]
- GCC_except_table1017
- GCC_except_table1053
- GCC_except_table1117
- GCC_except_table1119
- GCC_except_table1453
- GCC_except_table1468
- GCC_except_table1477
- GCC_except_table1594
- GCC_except_table1617
- GCC_except_table1622
- GCC_except_table1659
- GCC_except_table1675
- GCC_except_table1701
- GCC_except_table1709
- GCC_except_table1712
- GCC_except_table1715
- GCC_except_table1718
- GCC_except_table1721
- GCC_except_table1724
- GCC_except_table1727
- GCC_except_table1730
- GCC_except_table1733
- GCC_except_table1737
- GCC_except_table1743
- GCC_except_table1746
- GCC_except_table1749
- GCC_except_table1760
- GCC_except_table1763
- GCC_except_table1766
- GCC_except_table1769
- GCC_except_table1772
- GCC_except_table1775
- GCC_except_table1778
- GCC_except_table1781
- GCC_except_table1785
- GCC_except_table1792
- GCC_except_table1795
- GCC_except_table1798
- GCC_except_table1801
- GCC_except_table1804
- GCC_except_table1807
- GCC_except_table1818
- GCC_except_table1828
- GCC_except_table1945
- GCC_except_table1964
- GCC_except_table1968
- GCC_except_table2122
- GCC_except_table2130
- GCC_except_table2180
- GCC_except_table2185
- GCC_except_table2186
- GCC_except_table2188
- GCC_except_table2191
- GCC_except_table2331
- GCC_except_table2420
- GCC_except_table2460
- GCC_except_table2494
- GCC_except_table2499
- GCC_except_table2502
- GCC_except_table2505
- GCC_except_table2543
- GCC_except_table2550
- GCC_except_table258
- GCC_except_table2586
- GCC_except_table2590
- GCC_except_table2594
- GCC_except_table2597
- GCC_except_table2602
- GCC_except_table2605
- GCC_except_table2608
- GCC_except_table2612
- GCC_except_table2616
- GCC_except_table2620
- GCC_except_table2623
- GCC_except_table263
- GCC_except_table2633
- GCC_except_table2637
- GCC_except_table2641
- GCC_except_table2645
- GCC_except_table2649
- GCC_except_table2653
- GCC_except_table2657
- GCC_except_table266
- GCC_except_table2661
- GCC_except_table2665
- GCC_except_table2669
- GCC_except_table2673
- GCC_except_table2677
- GCC_except_table268
- GCC_except_table2681
- GCC_except_table2684
- GCC_except_table2688
- GCC_except_table2692
- GCC_except_table2696
- GCC_except_table270
- GCC_except_table2700
- GCC_except_table2704
- GCC_except_table2708
- GCC_except_table2711
- GCC_except_table2714
- GCC_except_table2720
- GCC_except_table2728
- GCC_except_table2732
- GCC_except_table2736
- GCC_except_table2740
- GCC_except_table2744
- GCC_except_table2748
- GCC_except_table275
- GCC_except_table2752
- GCC_except_table2756
- GCC_except_table2759
- GCC_except_table2764
- GCC_except_table2766
- GCC_except_table2767
- GCC_except_table2776
- GCC_except_table2778
- GCC_except_table2781
- GCC_except_table2784
- GCC_except_table2787
- GCC_except_table2790
- GCC_except_table2793
- GCC_except_table2796
- GCC_except_table2799
- GCC_except_table2802
- GCC_except_table2805
- GCC_except_table2808
- GCC_except_table2811
- GCC_except_table2814
- GCC_except_table2817
- GCC_except_table2819
- GCC_except_table284
- GCC_except_table2875
- GCC_except_table292
- GCC_except_table2942
- GCC_except_table2945
- GCC_except_table3002
- GCC_except_table303
- GCC_except_table3056
- GCC_except_table3067
- GCC_except_table3073
- GCC_except_table3075
- GCC_except_table3094
- GCC_except_table3102
- GCC_except_table312
- GCC_except_table318
- GCC_except_table3255
- GCC_except_table3257
- GCC_except_table3259
- GCC_except_table3264
- GCC_except_table3271
- GCC_except_table3274
- GCC_except_table3280
- GCC_except_table3283
- GCC_except_table3335
- GCC_except_table3337
- GCC_except_table336
- GCC_except_table3372
- GCC_except_table3496
- GCC_except_table3562
- GCC_except_table3566
- GCC_except_table3573
- GCC_except_table3626
- GCC_except_table3629
- GCC_except_table3635
- GCC_except_table3638
- GCC_except_table3641
- GCC_except_table3644
- GCC_except_table3650
- GCC_except_table3656
- GCC_except_table3660
- GCC_except_table3664
- GCC_except_table3668
- GCC_except_table3672
- GCC_except_table3693
- GCC_except_table3696
- GCC_except_table3705
- GCC_except_table3736
- GCC_except_table3744
- GCC_except_table3746
- GCC_except_table3751
- GCC_except_table3755
- GCC_except_table3761
- GCC_except_table3766
- GCC_except_table3769
- GCC_except_table3772
- GCC_except_table3776
- GCC_except_table3786
- GCC_except_table3795
- GCC_except_table3811
- GCC_except_table3819
- GCC_except_table3833
- GCC_except_table3836
- GCC_except_table384
- GCC_except_table385
- GCC_except_table3880
- GCC_except_table3903
- GCC_except_table3904
- GCC_except_table3905
- GCC_except_table3907
- GCC_except_table3909
- GCC_except_table3911
- GCC_except_table3912
- GCC_except_table3914
- GCC_except_table3917
- GCC_except_table3940
- GCC_except_table3952
- GCC_except_table3957
- GCC_except_table405
- GCC_except_table409
- GCC_except_table418
- GCC_except_table431
- GCC_except_table487
- GCC_except_table516
- GCC_except_table520
- GCC_except_table527
- GCC_except_table531
- GCC_except_table535
- GCC_except_table544
- GCC_except_table558
- GCC_except_table565
- GCC_except_table621
- GCC_except_table683
- GCC_except_table715
- GCC_except_table726
- GCC_except_table744
- GCC_except_table748
- GCC_except_table781
- GCC_except_table786
- GCC_except_table817
- GCC_except_table847
- GCC_except_table851
- GCC_except_table894
- GCC_except_table896
- GCC_except_table913
- GCC_except_table933
- GCC_except_table937
- GCC_except_table956
- GCC_except_table958
- ___100-[PLAssetsdLibraryClient transferPersonsWithUuids:fromLibraryURL:transferOptions:completionHandler:]_block_invoke
- ___99-[PLAssetsdLibraryClient transferAssetsWithUuids:fromLibraryURL:transferOptions:completionHandler:]_block_invoke
CStrings:
+ "/.nofollow"
+ "CN"
+ "PLXPC Client: migrateLimitedLibraryAccessFromApplication:toApplication:completionHandler:"
+ "PLXPC Client: updateAccessRequestForParticipantWithUUID:toAcceptanceStatus:inCollectionShareWithIdentifier:completionHandler:"
+ "Refusing to map '%@': redirected or non-regular."
+ "Unable to update access request (%@)"
+ "Unable to update access request for participant in collection share with identifier: %@. (%@)"
+ "XCTestCase"
+ "newBundleIdentifier"
+ "oldBundleIdentifier"
- "XCTestProbe"
```
