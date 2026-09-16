## PhotoLibraryServicesCore

> `/System/Library/PrivateFrameworks/PhotoLibraryServicesCore.framework/PhotoLibraryServicesCore`

```diff

-912.0.235.0.0
-  __TEXT.__text: 0xc7078
-  __TEXT.__objc_methlist: 0x834c
+916.40.110.0.0
+  __TEXT.__text: 0xc7ff8
+  __TEXT.__objc_methlist: 0x8364
   __TEXT.__const: 0x23cc
   __TEXT.__dlopen_cstrs: 0x19c
-  __TEXT.__gcc_except_tab: 0x5710
-  __TEXT.__cstring: 0x161df
-  __TEXT.__oslogstring: 0xb26b
+  __TEXT.__gcc_except_tab: 0x57cc
+  __TEXT.__cstring: 0x162ab
+  __TEXT.__oslogstring: 0xb38c
   __TEXT.__ustring: 0x4
-  __TEXT.__unwind_info: 0x4250
+  __TEXT.__unwind_info: 0x42a0
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0
   __TEXT.__objc_classname: 0x0
   __TEXT.__objc_methname: 0x0
   __TEXT.__objc_methtype: 0x0
-  __DATA_CONST.__const: 0x3cb0
+  __DATA_CONST.__const: 0x3ca8
   __DATA_CONST.__objc_classlist: 0x408
   __DATA_CONST.__objc_catlist: 0x10
   __DATA_CONST.__objc_protolist: 0x160
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x4ca8
+  __DATA_CONST.__objc_selrefs: 0x4cc8
   __DATA_CONST.__objc_protorefs: 0xc8
   __DATA_CONST.__objc_superrefs: 0x268
-  __DATA_CONST.__objc_arraydata: 0x420
+  __DATA_CONST.__objc_arraydata: 0x428
   __DATA_CONST.__got: 0xa48
-  __AUTH_CONST.__const: 0x35e8
+  __AUTH_CONST.__const: 0x3660
   __AUTH_CONST.__cfstring: 0x122e0
-  __AUTH_CONST.__objc_const: 0xaa08
-  __AUTH_CONST.__objc_intobj: 0x918
+  __AUTH_CONST.__objc_const: 0xaa00
+  __AUTH_CONST.__objc_intobj: 0x930
   __AUTH_CONST.__objc_floatobj: 0x10
   __AUTH_CONST.__objc_dictobj: 0x50
-  __AUTH_CONST.__objc_arrayobj: 0x288
-  __AUTH_CONST.__auth_got: 0xe48
+  __AUTH_CONST.__objc_arrayobj: 0x2a0
+  __AUTH_CONST.__auth_got: 0xe50
   __AUTH.__objc_data: 0x370
   __DATA.__objc_ivar: 0x678
   __DATA.__data: 0x10e0

   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libperfcheck.dylib
   - /usr/lib/libsqlite3.dylib
-  Functions: 3976
-  Symbols:   9456
-  CStrings:  3697
+  Functions: 3988
+  Symbols:   9472
+  CStrings:  3704
 
Symbols:
+ +[PLFileUtilities addOwnerWritePermissionIfNecessaryToFileAtPath:]
+ +[PLSecurity isEntitledForPrivatePhotosTCCForToken:]
+ -[PLAssetsdLibraryInternalClient getSearchDonationProgressShouldCompute:shouldReport:completionHandler:]
+ -[PLAssetsdNonBindingDebugClient stateCaptureDictionary]
+ -[PLLazyObject isValid]
+ -[PLLazyObject wasInvalidated]
+ GCC_except_table1807
+ GCC_except_table1818
+ GCC_except_table1828
+ GCC_except_table1836
+ GCC_except_table1844
+ GCC_except_table1945
+ GCC_except_table1964
+ GCC_except_table1968
+ GCC_except_table2122
+ GCC_except_table2130
+ GCC_except_table2185
+ GCC_except_table2188
+ GCC_except_table2191
+ GCC_except_table2331
+ GCC_except_table2420
+ GCC_except_table2460
+ GCC_except_table2494
+ GCC_except_table2526
+ GCC_except_table2529
+ GCC_except_table2543
+ GCC_except_table2550
+ GCC_except_table258
+ GCC_except_table2586
+ GCC_except_table2594
+ GCC_except_table2597
+ GCC_except_table2602
+ GCC_except_table2608
+ GCC_except_table2612
+ GCC_except_table2620
+ GCC_except_table2623
+ GCC_except_table2625
+ GCC_except_table2629
+ GCC_except_table263
+ GCC_except_table2633
+ GCC_except_table2637
+ GCC_except_table2641
+ GCC_except_table2645
+ GCC_except_table2649
+ GCC_except_table2653
+ GCC_except_table2657
+ GCC_except_table266
+ GCC_except_table2661
+ GCC_except_table2665
+ GCC_except_table2669
+ GCC_except_table2673
+ GCC_except_table268
+ GCC_except_table2684
+ GCC_except_table2688
+ GCC_except_table2692
+ GCC_except_table2696
+ GCC_except_table270
+ GCC_except_table2700
+ GCC_except_table2708
+ GCC_except_table2711
+ GCC_except_table2714
+ GCC_except_table2720
+ GCC_except_table2724
+ GCC_except_table2728
+ GCC_except_table2732
+ GCC_except_table2736
+ GCC_except_table2740
+ GCC_except_table2744
+ GCC_except_table2748
+ GCC_except_table275
+ GCC_except_table2756
+ GCC_except_table2761
+ GCC_except_table2764
+ GCC_except_table2766
+ GCC_except_table2767
+ GCC_except_table2772
+ GCC_except_table2776
+ GCC_except_table2778
+ GCC_except_table2781
+ GCC_except_table2784
+ GCC_except_table2787
+ GCC_except_table2790
+ GCC_except_table2793
+ GCC_except_table2796
+ GCC_except_table2799
+ GCC_except_table2802
+ GCC_except_table2805
+ GCC_except_table2808
+ GCC_except_table281
+ GCC_except_table2811
+ GCC_except_table2814
+ GCC_except_table2817
+ GCC_except_table2819
+ GCC_except_table284
+ GCC_except_table2875
+ GCC_except_table289
+ GCC_except_table292
+ GCC_except_table2942
+ GCC_except_table2945
+ GCC_except_table297
+ GCC_except_table300
+ GCC_except_table3002
+ GCC_except_table303
+ GCC_except_table3056
+ GCC_except_table3067
+ GCC_except_table3069
+ GCC_except_table3073
+ GCC_except_table3075
+ GCC_except_table3094
+ GCC_except_table3102
+ GCC_except_table312
+ GCC_except_table318
+ GCC_except_table324
+ GCC_except_table3255
+ GCC_except_table3257
+ GCC_except_table3259
+ GCC_except_table3268
+ GCC_except_table327
+ GCC_except_table3271
+ GCC_except_table3274
+ GCC_except_table3277
+ GCC_except_table3280
+ GCC_except_table3283
+ GCC_except_table330
+ GCC_except_table333
+ GCC_except_table3335
+ GCC_except_table3337
+ GCC_except_table336
+ GCC_except_table3372
+ GCC_except_table3496
+ GCC_except_table3562
+ GCC_except_table3566
+ GCC_except_table3573
+ GCC_except_table3635
+ GCC_except_table3641
+ GCC_except_table3650
+ GCC_except_table3664
+ GCC_except_table3668
+ GCC_except_table3672
+ GCC_except_table3696
+ GCC_except_table3705
+ GCC_except_table3718
+ GCC_except_table3736
+ GCC_except_table3744
+ GCC_except_table3746
+ GCC_except_table3751
+ GCC_except_table3755
+ GCC_except_table3761
+ GCC_except_table3766
+ GCC_except_table3769
+ GCC_except_table3772
+ GCC_except_table3776
+ GCC_except_table3779
+ GCC_except_table3786
+ GCC_except_table3789
+ GCC_except_table3792
+ GCC_except_table3795
+ GCC_except_table3802
+ GCC_except_table3805
+ GCC_except_table3808
+ GCC_except_table3811
+ GCC_except_table3815
+ GCC_except_table3819
+ GCC_except_table3833
+ GCC_except_table3836
+ GCC_except_table385
+ GCC_except_table3880
+ GCC_except_table3903
+ GCC_except_table3904
+ GCC_except_table3907
+ GCC_except_table3909
+ GCC_except_table3911
+ GCC_except_table3912
+ GCC_except_table3914
+ GCC_except_table3917
+ GCC_except_table3918
+ GCC_except_table3927
+ GCC_except_table3952
+ GCC_except_table3957
+ GCC_except_table405
+ GCC_except_table409
+ GCC_except_table418
+ GCC_except_table431
+ GCC_except_table487
+ GCC_except_table492
+ GCC_except_table495
+ GCC_except_table498
+ GCC_except_table501
+ GCC_except_table504
+ GCC_except_table507
+ GCC_except_table510
+ GCC_except_table513
+ GCC_except_table516
+ GCC_except_table520
+ GCC_except_table524
+ GCC_except_table527
+ GCC_except_table531
+ GCC_except_table535
+ GCC_except_table541
+ GCC_except_table544
+ GCC_except_table552
+ GCC_except_table555
+ GCC_except_table558
+ _OBJC_IVAR_$_PLLazyObject._invalidated
+ _PLIsErrorOrUnderlyingErrorDatalessMaterializationPrevented
+ _PLPlatformVisualIntelligenceSyncSupported
+ ___104-[PLAssetsdLibraryInternalClient getSearchDonationProgressShouldCompute:shouldReport:completionHandler:]_block_invoke
+ ___23-[PLLazyObject isValid]_block_invoke
+ ___30-[PLLazyObject wasInvalidated]_block_invoke
+ ___39-[PLLibraryServicesStateNode terminate]_block_invoke
+ ___52+[PLSecurity isEntitledForPrivatePhotosTCCForToken:]_block_invoke
+ ___56-[PLAssetsdNonBindingDebugClient stateCaptureDictionary]_block_invoke
+ ___block_descriptor_98_e8_32bs40n18_8_8_t0w1_s8_t16w32_e51_v16?0"<PLAssetsdLibraryInternalServiceProtocol>"8l
+ _fchmodat
+ _objc_msgSend$addOwnerWritePermissionIfNecessaryToFileAtPath:
+ _objc_msgSend$getSearchDonationProgressShouldCompute:shouldReport:reply:
+ _objc_msgSend$getStateCaptureDictionaryWithReply:
+ _objc_msgSend$isEntitledForPrivatePhotosTCCForToken:
- -[PLPhotoLibraryPathManagerCore assetUUIDRecoveryMappingPath]
- -[PLPhotoLibraryPathManagerCore postInit]
- -[PLPhotoLibraryPathManagerCore setAssetUUIDRecoveryMappingPath:]
- GCC_except_table1806
- GCC_except_table1825
- GCC_except_table1833
- GCC_except_table1841
- GCC_except_table1942
- GCC_except_table1961
- GCC_except_table1965
- GCC_except_table2125
- GCC_except_table2175
- GCC_except_table2181
- GCC_except_table2183
- GCC_except_table2326
- GCC_except_table2414
- GCC_except_table2454
- GCC_except_table2488
- GCC_except_table2493
- GCC_except_table2496
- GCC_except_table2537
- GCC_except_table2544
- GCC_except_table257
- GCC_except_table2579
- GCC_except_table2583
- GCC_except_table2587
- GCC_except_table2595
- GCC_except_table2598
- GCC_except_table2601
- GCC_except_table2609
- GCC_except_table2613
- GCC_except_table2618
- GCC_except_table262
- GCC_except_table2622
- GCC_except_table2626
- GCC_except_table2630
- GCC_except_table2634
- GCC_except_table2638
- GCC_except_table2642
- GCC_except_table2646
- GCC_except_table265
- GCC_except_table2650
- GCC_except_table2654
- GCC_except_table2658
- GCC_except_table2662
- GCC_except_table2666
- GCC_except_table267
- GCC_except_table2670
- GCC_except_table2674
- GCC_except_table2685
- GCC_except_table2689
- GCC_except_table269
- GCC_except_table2693
- GCC_except_table2697
- GCC_except_table2701
- GCC_except_table2707
- GCC_except_table2710
- GCC_except_table2713
- GCC_except_table2721
- GCC_except_table2725
- GCC_except_table2729
- GCC_except_table2733
- GCC_except_table2737
- GCC_except_table274
- GCC_except_table2741
- GCC_except_table2745
- GCC_except_table2749
- GCC_except_table2754
- GCC_except_table2757
- GCC_except_table2760
- GCC_except_table2762
- GCC_except_table2765
- GCC_except_table2771
- GCC_except_table2774
- GCC_except_table2777
- GCC_except_table2780
- GCC_except_table2783
- GCC_except_table2786
- GCC_except_table2789
- GCC_except_table2792
- GCC_except_table2795
- GCC_except_table2798
- GCC_except_table280
- GCC_except_table2801
- GCC_except_table2804
- GCC_except_table2807
- GCC_except_table2810
- GCC_except_table2812
- GCC_except_table283
- GCC_except_table2868
- GCC_except_table288
- GCC_except_table291
- GCC_except_table2935
- GCC_except_table2938
- GCC_except_table296
- GCC_except_table299
- GCC_except_table2995
- GCC_except_table302
- GCC_except_table3049
- GCC_except_table3060
- GCC_except_table3062
- GCC_except_table3066
- GCC_except_table3068
- GCC_except_table3087
- GCC_except_table3095
- GCC_except_table311
- GCC_except_table317
- GCC_except_table323
- GCC_except_table3248
- GCC_except_table3250
- GCC_except_table3252
- GCC_except_table3256
- GCC_except_table326
- GCC_except_table3261
- GCC_except_table3267
- GCC_except_table3270
- GCC_except_table3273
- GCC_except_table329
- GCC_except_table332
- GCC_except_table335
- GCC_except_table3358
- GCC_except_table3483
- GCC_except_table3550
- GCC_except_table3554
- GCC_except_table3561
- GCC_except_table3614
- GCC_except_table3617
- GCC_except_table3623
- GCC_except_table3632
- GCC_except_table3648
- GCC_except_table3652
- GCC_except_table3681
- GCC_except_table3684
- GCC_except_table3706
- GCC_except_table3724
- GCC_except_table3732
- GCC_except_table3734
- GCC_except_table3739
- GCC_except_table3743
- GCC_except_table3749
- GCC_except_table3754
- GCC_except_table3757
- GCC_except_table3760
- GCC_except_table3764
- GCC_except_table3767
- GCC_except_table3774
- GCC_except_table3777
- GCC_except_table3780
- GCC_except_table3783
- GCC_except_table3787
- GCC_except_table3790
- GCC_except_table3793
- GCC_except_table3796
- GCC_except_table3803
- GCC_except_table3807
- GCC_except_table3821
- GCC_except_table3824
- GCC_except_table383
- GCC_except_table3868
- GCC_except_table3891
- GCC_except_table3892
- GCC_except_table3893
- GCC_except_table3895
- GCC_except_table3897
- GCC_except_table3899
- GCC_except_table3900
- GCC_except_table3902
- GCC_except_table3906
- GCC_except_table3915
- GCC_except_table3928
- GCC_except_table3933
- GCC_except_table404
- GCC_except_table408
- GCC_except_table417
- GCC_except_table430
- GCC_except_table486
- GCC_except_table491
- GCC_except_table494
- GCC_except_table497
- GCC_except_table500
- GCC_except_table503
- GCC_except_table506
- GCC_except_table509
- GCC_except_table512
- GCC_except_table515
- GCC_except_table519
- GCC_except_table523
- GCC_except_table526
- GCC_except_table530
- GCC_except_table534
- GCC_except_table540
- GCC_except_table543
- GCC_except_table551
- GCC_except_table554
- GCC_except_table557
- _OBJC_IVAR_$_PLPhotoLibraryPathManagerCore._assetUUIDRecoveryMappingPath
- _PLAssetUUIDRecoveryMappingFileName
- _PLIsSharedCollectionsFeatureEnabled
- _PUTGetCurrentAccess
- ___62+[PLSecurity isEntitledForPhotoKitOrPrivatePhotosTCCForToken:]_block_invoke
- _objc_msgSend$postInit
- _objc_msgSend$setAssetUUIDRecoveryMappingPath:
CStrings:
+ "-[PLAssetsdLibraryInternalClient getSearchDonationProgressShouldCompute:shouldReport:completionHandler:]_block_invoke"
+ "-[PLAssetsdNonBindingDebugClient stateCaptureDictionary]_block_invoke"
+ "Added owner read and write permission to %@ (was %o)"
+ "Failed to add owner read and write permission to %@ (%{public}s)."
+ "PLPhotosErrorCollectionShareNotEnabled"
+ "PLXPC Client: getSearchDonationProgressShouldCompute:shouldReport:completionHandler:"
+ "PLXPC Client: stateCaptureDictionary"
+ "Refusing to change permissions of symlink %@"
+ "Unable to open file %@ to save extended attributes (%{public}s)."
+ "\x86"
- "Unable to open file to save extended attributes (%{public}s)."
- "assetUUIDForPath.plist"
- "\x87"
```
