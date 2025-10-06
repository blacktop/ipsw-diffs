## FileProviderDaemon

> `/System/Library/PrivateFrameworks/FileProviderDaemon.framework/FileProviderDaemon`

```diff

-1835.102.2.0.0
-  __TEXT.__text: 0x9867b8
+1835.120.53.0.0
+  __TEXT.__text: 0x98c720
   __TEXT.__auth_stubs: 0x5410
-  __TEXT.__objc_methlist: 0x6108
-  __TEXT.__cstring: 0x4042e
-  __TEXT.__oslogstring: 0xd8df
-  __TEXT.__const: 0x18770
-  __TEXT.__gcc_except_tab: 0x9c80
+  __TEXT.__objc_methlist: 0x6120
+  __TEXT.__cstring: 0x40a5e
+  __TEXT.__oslogstring: 0xd94b
+  __TEXT.__const: 0x18980
+  __TEXT.__gcc_except_tab: 0x9cbc
   __TEXT.__ustring: 0x189a
   __TEXT.__dlopen_cstrs: 0x50
-  __TEXT.__constg_swiftt: 0xe0ac
+  __TEXT.__constg_swiftt: 0xe0b0
   __TEXT.__swift5_typeref: 0xd8e3
-  __TEXT.__swift5_reflstr: 0x822e
-  __TEXT.__swift5_fieldmd: 0x7728
-  __TEXT.__swift5_capture: 0x11ef4
+  __TEXT.__swift5_reflstr: 0x82ae
+  __TEXT.__swift5_fieldmd: 0x7774
+  __TEXT.__swift5_capture: 0x11f98
   __TEXT.__swift5_proto: 0x11b4
-  __TEXT.__swift5_types: 0x7c4
+  __TEXT.__swift5_types: 0x7c8
   __TEXT.__swift5_builtin: 0x5f0
   __TEXT.__swift5_mpenum: 0xdc
   __TEXT.__swift5_protos: 0x68
   __TEXT.__swift5_assocty: 0x1990
-  __TEXT.__unwind_info: 0x139c4
-  __TEXT.__eh_frame: 0x205b8
-  __TEXT.__objc_classname: 0xb1a
-  __TEXT.__objc_methname: 0x177e1
+  __TEXT.__unwind_info: 0x13f34
+  __TEXT.__eh_frame: 0x20740
+  __TEXT.__objc_classname: 0xb1b
+  __TEXT.__objc_methname: 0x17925
   __TEXT.__objc_methtype: 0x5321
-  __TEXT.__objc_stubs: 0xe160
+  __TEXT.__objc_stubs: 0xe140
   __DATA_CONST.__got: 0xf38
   __DATA_CONST.__const: 0x4758
   __DATA_CONST.__objc_classlist: 0x430
   __DATA_CONST.__objc_catlist: 0x70
   __DATA_CONST.__objc_protolist: 0x288
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_const: 0x1bf80
-  __DATA_CONST.__objc_selrefs: 0x4fc0
+  __DATA_CONST.__objc_const: 0x1c010
+  __DATA_CONST.__objc_selrefs: 0x4fe8
   __DATA_CONST.__objc_protorefs: 0xf8
   __DATA_CONST.__objc_classrefs: 0x748
   __DATA_CONST.__objc_superrefs: 0x200
-  __DATA_CONST.__objc_arraydata: 0xb0
-  __AUTH_CONST.__cfstring: 0x5760
-  __AUTH_CONST.__const: 0x3d8d8
+  __DATA_CONST.__objc_arraydata: 0xb8
+  __AUTH_CONST.__cfstring: 0x57a0
+  __AUTH_CONST.__const: 0x3daf8
   __AUTH_CONST.__objc_const: 0x2078
-  __AUTH_CONST.__objc_arrayobj: 0x78
+  __AUTH_CONST.__objc_arrayobj: 0x90
   __AUTH_CONST.__objc_intobj: 0xc0
   __AUTH_CONST.__objc_dictobj: 0x28
   __AUTH_CONST.__auth_got: 0x2a18
-  __AUTH.__objc_data: 0x3188
-  __AUTH.__data: 0x59e0
-  __DATA.__objc_ivar: 0x980
-  __DATA.__objc_data: 0x48
-  __DATA.__data: 0x100b0
-  __DATA.__bss: 0x22b20
-  __DATA.__common: 0x590
-  __DATA_DIRTY.__objc_data: 0xd20
-  __DATA_DIRTY.__bss: 0x120
+  __AUTH.__objc_data: 0x1288
+  __AUTH.__data: 0x17f8
+  __DATA.__objc_ivar: 0x98c
+  __DATA.__data: 0xae58
+  __DATA.__bss: 0x1dc50
+  __DATA.__common: 0x140
+  __DATA_DIRTY.__objc_data: 0x2c68
+  __DATA_DIRTY.__data: 0xa358
+  __DATA_DIRTY.__bss: 0x4ff8
+  __DATA_DIRTY.__common: 0x450
   - /System/Library/Frameworks/Accounts.framework/Accounts
   - /System/Library/Frameworks/CloudKit.framework/CloudKit
   - /System/Library/Frameworks/Combine.framework/Combine

   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  UUID: 35607EE5-2993-3B5A-8B2D-933276596A6D
-  Functions: 31930
-  Symbols:   22139
-  CStrings:  10958
+  UUID: DC0E9E62-D348-3B18-9EF3-A5C4F0C27CD7
+  Functions: 31992
+  Symbols:   22166
+  CStrings:  10995
 
Symbols:
+ -[FPDAccessRight domain]
+ -[FPDConfigurationStore dynamicErrorSampleRatePerProvider]
+ -[FPDDomain isProviderForRealPathURL:]
+ -[FPDDomainDeadEndBackend isProviderForRealPathURL:]
+ -[FPDDomainExtensionBackend isProviderForRealPathURL:]
+ -[FPDSharedScheduler lastDeferralDate]
+ _FPInvalidParameterErrorWithExpectation
+ _OBJC_IVAR_$_FPDAccessRight._domain
+ _OBJC_IVAR_$_FPDConfigurationStore._dynamicErrorSampleRatePerProvider
+ _OBJC_IVAR_$_FPDSharedScheduler._lastDeferralDate
+ ___100-[FPDXPCServicer _test_importItemsPendingScanningProviderProgressForDomainWithID:completionHandler:]_block_invoke.384
+ ___63-[FPDXPCServicer fetchDaemonOperationIDsWithCompletionHandler:]_block_invoke.324
+ ___63-[FPDXPCServicer listPausedURLsWithBundleID:completionHandler:]_block_invoke.397
+ ___63-[FPDXPCServicer listPausedURLsWithBundleID:completionHandler:]_block_invoke.397.cold.1
+ ___63-[FPDXPCServicer listPausedURLsWithBundleID:completionHandler:]_block_invoke.397.cold.2
+ ___68-[FPDXPCServicer scheduleActionOperationWithInfo:completionHandler:]_block_invoke.322
+ ___70-[FPDXPCServicer copyDatabaseForFPCKStartingAtPath:completionHandler:]_block_invoke.315
+ ___70-[FPDXPCServicer reindexAllSearchableItemsWithAcknowledgementHandler:]_block_invoke.320
+ ___71-[FPDXPCServicer waitForStabilizationOfDomainWithID:completionHandler:]_block_invoke.319
+ ___73-[FPDXPCServicer waitForChangesOnItemsBelowItemWithID:completionHandler:]_block_invoke.318
+ ___74-[FPDXPCServicer startAccessingServiceWithName:itemURL:completionHandler:]_block_invoke.335
+ ___76-[FPDXPCServicer fetchLatestVersionForItemAtURL:bundleID:completionHandler:]_block_invoke.394
+ ___76-[FPDXPCServicer pauseSyncForItemAtURL:behavior:bundleID:completionHandler:]_block_invoke.388
+ ___77-[FPDXPCServicer _performWithCheckedEnumerationAttributes:completionHandler:]_block_invoke.336
+ ___77-[FPDXPCServicer resumeSyncForItemAtURL:behavior:bundleID:completionHandler:]_block_invoke.391
+ ___78-[FPDXPCServicer _test_callRemoveTrashedItemsOlderThanDate:completionHandler:]_block_invoke.367
+ ___78-[FPDXPCServicer _test_callRemoveTrashedItemsOlderThanDate:completionHandler:]_block_invoke.367.cold.1
+ ___82-[FPDXPCServicer dumpStateTo:limitNumberOfItems:providerFilter:completionHandler:]_block_invoke.297
+ ___82-[FPDXPCServicer fetchAndStartEnumeratingWithSettings:observer:completionHandler:]_block_invoke.343
+ ___96-[FPDXPCServicer _test_importItemsPendingScanningDiskProgressForDomainWithID:completionHandler:]_block_invoke.381
+ ___98-[FPDXPCServicer _test_importItemsPendingReconciliationProgressForDomainWithID:completionHandler:]_block_invoke.378
+ ___block_literal_global.168
+ ___block_literal_global.327
+ __unnamed_array_storage.164
+ _block_copy_helper.2515
+ _block_copy_helper.2594
+ _block_copy_helper.2600
+ _block_copy_helper.2650
+ _block_copy_helper.2683
+ _block_copy_helper.2692
+ _block_copy_helper.2699
+ _block_copy_helper.2706
+ _block_copy_helper.2746
+ _block_copy_helper.2753
+ _block_copy_helper.2759
+ _block_copy_helper.2776
+ _block_copy_helper.2782
+ _block_copy_helper.2802
+ _block_copy_helper.2821
+ _block_copy_helper.2945
+ _block_copy_helper.2957
+ _block_copy_helper.2960
+ _block_copy_helper.2979
+ _block_copy_helper.2985
+ _block_copy_helper.3021
+ _block_copy_helper.3025
+ _block_copy_helper.3028
+ _block_copy_helper.3097
+ _block_copy_helper.3100
+ _block_copy_helper.3107
+ _block_copy_helper.3143
+ _block_copy_helper.3165
+ _block_copy_helper.3191
+ _block_copy_helper.3222
+ _block_copy_helper.3228
+ _block_copy_helper.3249
+ _block_copy_helper.3255
+ _block_copy_helper.3261
+ _block_copy_helper.3283
+ _block_copy_helper.3297
+ _block_copy_helper.3307
+ _block_copy_helper.3313
+ _block_copy_helper.3322
+ _block_copy_helper.3360
+ _block_copy_helper.3367
+ _block_copy_helper.3374
+ _block_copy_helper.3384
+ _block_copy_helper.3394
+ _block_copy_helper.3401
+ _block_copy_helper.3411
+ _block_copy_helper.3418
+ _block_copy_helper.3425
+ _block_copy_helper.3435
+ _block_copy_helper.3493
+ _block_copy_helper.3499
+ _block_copy_helper.3545
+ _block_copy_helper.3580
+ _block_copy_helper.3600
+ _block_copy_helper.3610
+ _block_copy_helper.3616
+ _block_copy_helper.3665
+ _block_copy_helper.3676
+ _block_copy_helper.3692
+ _block_copy_helper.3742
+ _block_copy_helper.3745
+ _block_copy_helper.3751
+ _block_copy_helper.3761
+ _block_copy_helper.3772
+ _block_copy_helper.3793
+ _block_copy_helper.3866
+ _block_copy_helper.4043
+ _block_copy_helper.4053
+ _block_copy_helper.4063
+ _block_copy_helper.4074
+ _block_copy_helper.4087
+ _block_copy_helper.4100
+ _block_copy_helper.4129
+ _block_copy_helper.4151
+ _block_copy_helper.4161
+ _block_copy_helper.62
+ _block_descriptor.2517
+ _block_descriptor.2596
+ _block_descriptor.2602
+ _block_descriptor.2652
+ _block_descriptor.2685
+ _block_descriptor.2694
+ _block_descriptor.2701
+ _block_descriptor.2708
+ _block_descriptor.2748
+ _block_descriptor.2755
+ _block_descriptor.2761
+ _block_descriptor.2778
+ _block_descriptor.2784
+ _block_descriptor.2804
+ _block_descriptor.2823
+ _block_descriptor.2947
+ _block_descriptor.2959
+ _block_descriptor.2962
+ _block_descriptor.2981
+ _block_descriptor.2987
+ _block_descriptor.3023
+ _block_descriptor.3027
+ _block_descriptor.3030
+ _block_descriptor.3099
+ _block_descriptor.3102
+ _block_descriptor.3109
+ _block_descriptor.3145
+ _block_descriptor.3167
+ _block_descriptor.3193
+ _block_descriptor.3224
+ _block_descriptor.3230
+ _block_descriptor.3251
+ _block_descriptor.3257
+ _block_descriptor.3263
+ _block_descriptor.3285
+ _block_descriptor.3299
+ _block_descriptor.3309
+ _block_descriptor.3315
+ _block_descriptor.3324
+ _block_descriptor.3362
+ _block_descriptor.3369
+ _block_descriptor.3376
+ _block_descriptor.3386
+ _block_descriptor.3396
+ _block_descriptor.3403
+ _block_descriptor.3413
+ _block_descriptor.3420
+ _block_descriptor.3427
+ _block_descriptor.3437
+ _block_descriptor.3495
+ _block_descriptor.3501
+ _block_descriptor.3547
+ _block_descriptor.3582
+ _block_descriptor.3602
+ _block_descriptor.3612
+ _block_descriptor.3618
+ _block_descriptor.3667
+ _block_descriptor.3678
+ _block_descriptor.3694
+ _block_descriptor.3744
+ _block_descriptor.3747
+ _block_descriptor.3753
+ _block_descriptor.3763
+ _block_descriptor.3774
+ _block_descriptor.3795
+ _block_descriptor.3868
+ _block_descriptor.4045
+ _block_descriptor.4055
+ _block_descriptor.4065
+ _block_descriptor.4076
+ _block_descriptor.4089
+ _block_descriptor.4102
+ _block_descriptor.4131
+ _block_descriptor.4153
+ _block_descriptor.4163
+ _block_descriptor.64
+ _block_destroy_helper.2516
+ _block_destroy_helper.2595
+ _block_destroy_helper.2601
+ _block_destroy_helper.2651
+ _block_destroy_helper.2684
+ _block_destroy_helper.2693
+ _block_destroy_helper.2700
+ _block_destroy_helper.2707
+ _block_destroy_helper.2747
+ _block_destroy_helper.2754
+ _block_destroy_helper.2760
+ _block_destroy_helper.2777
+ _block_destroy_helper.2783
+ _block_destroy_helper.2803
+ _block_destroy_helper.2822
+ _block_destroy_helper.2946
+ _block_destroy_helper.2958
+ _block_destroy_helper.2961
+ _block_destroy_helper.2980
+ _block_destroy_helper.2986
+ _block_destroy_helper.3022
+ _block_destroy_helper.3026
+ _block_destroy_helper.3029
+ _block_destroy_helper.3098
+ _block_destroy_helper.3101
+ _block_destroy_helper.3108
+ _block_destroy_helper.3144
+ _block_destroy_helper.3166
+ _block_destroy_helper.3192
+ _block_destroy_helper.3223
+ _block_destroy_helper.3229
+ _block_destroy_helper.3250
+ _block_destroy_helper.3256
+ _block_destroy_helper.3262
+ _block_destroy_helper.3284
+ _block_destroy_helper.3298
+ _block_destroy_helper.3308
+ _block_destroy_helper.3314
+ _block_destroy_helper.3323
+ _block_destroy_helper.3361
+ _block_destroy_helper.3368
+ _block_destroy_helper.3375
+ _block_destroy_helper.3385
+ _block_destroy_helper.3395
+ _block_destroy_helper.3402
+ _block_destroy_helper.3412
+ _block_destroy_helper.3419
+ _block_destroy_helper.3426
+ _block_destroy_helper.3436
+ _block_destroy_helper.3494
+ _block_destroy_helper.3500
+ _block_destroy_helper.3546
+ _block_destroy_helper.3581
+ _block_destroy_helper.3601
+ _block_destroy_helper.3611
+ _block_destroy_helper.3617
+ _block_destroy_helper.3666
+ _block_destroy_helper.3677
+ _block_destroy_helper.3693
+ _block_destroy_helper.3743
+ _block_destroy_helper.3746
+ _block_destroy_helper.3752
+ _block_destroy_helper.3762
+ _block_destroy_helper.3773
+ _block_destroy_helper.3794
+ _block_destroy_helper.3867
+ _block_destroy_helper.4044
+ _block_destroy_helper.4054
+ _block_destroy_helper.4064
+ _block_destroy_helper.4075
+ _block_destroy_helper.4088
+ _block_destroy_helper.4101
+ _block_destroy_helper.4130
+ _block_destroy_helper.4152
+ _block_destroy_helper.4162
+ _block_destroy_helper.63
+ _fpfs_get_purgeable_stats
+ _objc_msgSend$fp_fpfsProviderDomainID:skipTypeCheck:error:
+ _objc_msgSend$fp_realPathRelationshipToItemAtRealPathURL:
+ _objc_msgSend$isProviderForRealPathURL:
+ _objectdestroy.2473Tm
+ _objectdestroy.2489Tm
+ _objectdestroy.2529Tm
+ _objectdestroy.2539Tm
+ _objectdestroy.2542Tm
+ _objectdestroy.2545Tm
+ _objectdestroy.2592Tm
+ _objectdestroy.2816Tm
+ _objectdestroy.285Tm
+ _objectdestroy.288Tm
+ _objectdestroy.2899Tm
+ _objectdestroy.295Tm
+ _objectdestroy.3137Tm
+ _objectdestroy.3176Tm
+ _objectdestroy.3527Tm
+ _objectdestroy.3530Tm
+ _objectdestroy.3536Tm
+ _objectdestroy.3720Tm
+ _objectdestroy.3828Tm
+ _objectdestroy.3977Tm
+ _objectdestroy.3984Tm
+ _symbolic G0R12_
+ _symbolic G1R12_
+ _symbolic _____ 9libfssync14FPDVolumeStatsV
+ _symbolic _____Sg 9libfssync14FPDVolumeStatsV
- -[FPDDomain isProviderForURL:]
- -[FPDDomainDeadEndBackend isProviderForURL:]
- -[FPDDomainExtensionBackend isProviderForURL:]
- -[FPDXPCServicer addDomain:forProviderIdentifier:byImportingDirectoryAtURL:nonWrappedURL:userAllowedDBDrop:knownFolders:completionHandler:].cold.7
- _OUTLINED_FUNCTION_33
- ___100-[FPDXPCServicer _test_importItemsPendingScanningProviderProgressForDomainWithID:completionHandler:]_block_invoke.387
- ___63-[FPDXPCServicer fetchDaemonOperationIDsWithCompletionHandler:]_block_invoke.327
- ___63-[FPDXPCServicer listPausedURLsWithBundleID:completionHandler:]_block_invoke.400
- ___63-[FPDXPCServicer listPausedURLsWithBundleID:completionHandler:]_block_invoke.400.cold.1
- ___63-[FPDXPCServicer listPausedURLsWithBundleID:completionHandler:]_block_invoke.400.cold.2
- ___68-[FPDXPCServicer scheduleActionOperationWithInfo:completionHandler:]_block_invoke.325
- ___70-[FPDXPCServicer copyDatabaseForFPCKStartingAtPath:completionHandler:]_block_invoke.318
- ___70-[FPDXPCServicer reindexAllSearchableItemsWithAcknowledgementHandler:]_block_invoke.323
- ___71-[FPDXPCServicer waitForStabilizationOfDomainWithID:completionHandler:]_block_invoke.322
- ___73-[FPDXPCServicer waitForChangesOnItemsBelowItemWithID:completionHandler:]_block_invoke.321
- ___74-[FPDXPCServicer startAccessingServiceWithName:itemURL:completionHandler:]_block_invoke.338
- ___76-[FPDXPCServicer fetchLatestVersionForItemAtURL:bundleID:completionHandler:]_block_invoke.397
- ___76-[FPDXPCServicer pauseSyncForItemAtURL:behavior:bundleID:completionHandler:]_block_invoke.391
- ___77-[FPDXPCServicer _performWithCheckedEnumerationAttributes:completionHandler:]_block_invoke.339
- ___77-[FPDXPCServicer resumeSyncForItemAtURL:behavior:bundleID:completionHandler:]_block_invoke.394
- ___78-[FPDXPCServicer _test_callRemoveTrashedItemsOlderThanDate:completionHandler:]_block_invoke.370
- ___78-[FPDXPCServicer _test_callRemoveTrashedItemsOlderThanDate:completionHandler:]_block_invoke.370.cold.1
- ___82-[FPDXPCServicer dumpStateTo:limitNumberOfItems:providerFilter:completionHandler:]_block_invoke.300
- ___82-[FPDXPCServicer fetchAndStartEnumeratingWithSettings:observer:completionHandler:]_block_invoke.346
- ___96-[FPDXPCServicer _test_importItemsPendingScanningDiskProgressForDomainWithID:completionHandler:]_block_invoke.384
- ___98-[FPDXPCServicer _test_importItemsPendingReconciliationProgressForDomainWithID:completionHandler:]_block_invoke.381
- ___block_literal_global.330
- _block_copy_helper.2490
- _block_copy_helper.2496
- _block_copy_helper.2528
- _block_copy_helper.2538
- _block_copy_helper.2617
- _block_copy_helper.2623
- _block_copy_helper.2673
- _block_copy_helper.2707
- _block_copy_helper.2730
- _block_copy_helper.2747
- _block_copy_helper.2764
- _block_copy_helper.2770
- _block_copy_helper.2777
- _block_copy_helper.2783
- _block_copy_helper.2800
- _block_copy_helper.2806
- _block_copy_helper.2826
- _block_copy_helper.2845
- _block_copy_helper.2969
- _block_copy_helper.2981
- _block_copy_helper.2984
- _block_copy_helper.300
- _block_copy_helper.3003
- _block_copy_helper.3009
- _block_copy_helper.3045
- _block_copy_helper.3049
- _block_copy_helper.3052
- _block_copy_helper.3121
- _block_copy_helper.3124
- _block_copy_helper.3131
- _block_copy_helper.3167
- _block_copy_helper.3189
- _block_copy_helper.3239
- _block_copy_helper.3270
- _block_copy_helper.3273
- _block_copy_helper.3276
- _block_copy_helper.3279
- _block_copy_helper.328
- _block_copy_helper.3285
- _block_copy_helper.3288
- _block_copy_helper.3295
- _block_copy_helper.3306
- _block_copy_helper.3346
- _block_copy_helper.3356
- _block_copy_helper.3362
- _block_copy_helper.3371
- _block_copy_helper.3381
- _block_copy_helper.3409
- _block_copy_helper.3419
- _block_copy_helper.3429
- _block_copy_helper.3436
- _block_copy_helper.3446
- _block_copy_helper.3453
- _block_copy_helper.3463
- _block_copy_helper.3521
- _block_copy_helper.3527
- _block_copy_helper.3573
- _block_copy_helper.3608
- _block_copy_helper.3628
- _block_copy_helper.3638
- _block_copy_helper.3644
- _block_copy_helper.3693
- _block_copy_helper.3704
- _block_copy_helper.3720
- _block_copy_helper.3770
- _block_copy_helper.3773
- _block_copy_helper.3779
- _block_copy_helper.3789
- _block_copy_helper.3800
- _block_copy_helper.3821
- _block_copy_helper.3894
- _block_copy_helper.4071
- _block_copy_helper.4091
- _block_copy_helper.4102
- _block_copy_helper.4109
- _block_copy_helper.4115
- _block_copy_helper.4128
- _block_copy_helper.4157
- _block_copy_helper.4179
- _block_copy_helper.4186
- _block_descriptor.2492
- _block_descriptor.2498
- _block_descriptor.2530
- _block_descriptor.2540
- _block_descriptor.2619
- _block_descriptor.2625
- _block_descriptor.2675
- _block_descriptor.2709
- _block_descriptor.2732
- _block_descriptor.2749
- _block_descriptor.2766
- _block_descriptor.2772
- _block_descriptor.2779
- _block_descriptor.2785
- _block_descriptor.2802
- _block_descriptor.2808
- _block_descriptor.2828
- _block_descriptor.2847
- _block_descriptor.2971
- _block_descriptor.2983
- _block_descriptor.2986
- _block_descriptor.3005
- _block_descriptor.3011
- _block_descriptor.302
- _block_descriptor.3047
- _block_descriptor.3051
- _block_descriptor.3054
- _block_descriptor.3123
- _block_descriptor.3126
- _block_descriptor.3133
- _block_descriptor.3169
- _block_descriptor.3191
- _block_descriptor.3241
- _block_descriptor.3272
- _block_descriptor.3275
- _block_descriptor.3278
- _block_descriptor.3281
- _block_descriptor.3287
- _block_descriptor.3290
- _block_descriptor.3297
- _block_descriptor.330
- _block_descriptor.3308
- _block_descriptor.3348
- _block_descriptor.3358
- _block_descriptor.3364
- _block_descriptor.3373
- _block_descriptor.3383
- _block_descriptor.3411
- _block_descriptor.3421
- _block_descriptor.3431
- _block_descriptor.3438
- _block_descriptor.3448
- _block_descriptor.3455
- _block_descriptor.3465
- _block_descriptor.3523
- _block_descriptor.3529
- _block_descriptor.3575
- _block_descriptor.3610
- _block_descriptor.3630
- _block_descriptor.3640
- _block_descriptor.3646
- _block_descriptor.3695
- _block_descriptor.3706
- _block_descriptor.3722
- _block_descriptor.3772
- _block_descriptor.3775
- _block_descriptor.3781
- _block_descriptor.3791
- _block_descriptor.3802
- _block_descriptor.3823
- _block_descriptor.3896
- _block_descriptor.4073
- _block_descriptor.4093
- _block_descriptor.4104
- _block_descriptor.4111
- _block_descriptor.4117
- _block_descriptor.4130
- _block_descriptor.4159
- _block_descriptor.4181
- _block_descriptor.4188
- _block_destroy_helper.2491
- _block_destroy_helper.2497
- _block_destroy_helper.2529
- _block_destroy_helper.2539
- _block_destroy_helper.2618
- _block_destroy_helper.2624
- _block_destroy_helper.2674
- _block_destroy_helper.2708
- _block_destroy_helper.2731
- _block_destroy_helper.2748
- _block_destroy_helper.2765
- _block_destroy_helper.2771
- _block_destroy_helper.2778
- _block_destroy_helper.2784
- _block_destroy_helper.2801
- _block_destroy_helper.2807
- _block_destroy_helper.2827
- _block_destroy_helper.2846
- _block_destroy_helper.2970
- _block_destroy_helper.2982
- _block_destroy_helper.2985
- _block_destroy_helper.3004
- _block_destroy_helper.301
- _block_destroy_helper.3010
- _block_destroy_helper.3046
- _block_destroy_helper.3050
- _block_destroy_helper.3053
- _block_destroy_helper.3122
- _block_destroy_helper.3125
- _block_destroy_helper.3132
- _block_destroy_helper.3168
- _block_destroy_helper.3190
- _block_destroy_helper.3240
- _block_destroy_helper.3271
- _block_destroy_helper.3274
- _block_destroy_helper.3277
- _block_destroy_helper.3280
- _block_destroy_helper.3286
- _block_destroy_helper.3289
- _block_destroy_helper.329
- _block_destroy_helper.3296
- _block_destroy_helper.3307
- _block_destroy_helper.3347
- _block_destroy_helper.3357
- _block_destroy_helper.3363
- _block_destroy_helper.3372
- _block_destroy_helper.3382
- _block_destroy_helper.3410
- _block_destroy_helper.3420
- _block_destroy_helper.3430
- _block_destroy_helper.3437
- _block_destroy_helper.3447
- _block_destroy_helper.3454
- _block_destroy_helper.3464
- _block_destroy_helper.3522
- _block_destroy_helper.3528
- _block_destroy_helper.3574
- _block_destroy_helper.3609
- _block_destroy_helper.3629
- _block_destroy_helper.3639
- _block_destroy_helper.3645
- _block_destroy_helper.3694
- _block_destroy_helper.3705
- _block_destroy_helper.3721
- _block_destroy_helper.3771
- _block_destroy_helper.3774
- _block_destroy_helper.3780
- _block_destroy_helper.3790
- _block_destroy_helper.3801
- _block_destroy_helper.3822
- _block_destroy_helper.3895
- _block_destroy_helper.4072
- _block_destroy_helper.4092
- _block_destroy_helper.4103
- _block_destroy_helper.4110
- _block_destroy_helper.4116
- _block_destroy_helper.4129
- _block_destroy_helper.4158
- _block_destroy_helper.4180
- _block_destroy_helper.4187
- _objc_msgSend$URLWithString:
- _objc_msgSend$fp_fpfsProviderDomainID:
- _objc_msgSend$isProviderForURL:
- _objc_msgSend$uid
- _objectdestroy.2552Tm
- _objectdestroy.2562Tm
- _objectdestroy.2565Tm
- _objectdestroy.2568Tm
- _objectdestroy.2615Tm
- _objectdestroy.2840Tm
- _objectdestroy.2923Tm
- _objectdestroy.3161Tm
- _objectdestroy.3200Tm
- _objectdestroy.338Tm
- _objectdestroy.3391Tm
- _objectdestroy.341Tm
- _objectdestroy.348Tm
- _objectdestroy.3555Tm
- _objectdestroy.3558Tm
- _objectdestroy.3564Tm
- _objectdestroy.3748Tm
- _objectdestroy.3856Tm
- _objectdestroy.4005Tm
- _objectdestroy.4012Tm
- _objectdestroy.623Tm
- _symbolic G0R9_
- _symbolic G1R9_
CStrings:
+ "\x01\xe3q"
+ "\x04$"
+ "\nGROUP BY metadata_is_dataless"
+ "\nWHERE metadata_is_in_pinned_folder AND metadata_kind = "
+ "/Library/Caches/com.apple.xbs/Sources/FileProviderTools/fssync/libfssync/implementations/file-system/persistence/SQLSnapshot.swift"
+ "Failed to gather volume stats on %@: %@"
+ "Invalid call on FP snapshot"
+ "Invalid call on FS snapshot"
+ "Retrieved statfs() for volume %@"
+ "SELECT SUM(metadata_size),\n       SUM(CASE WHEN DATETIME(metadata_last_used_date, 'unixepoch') >= date('now', '-30 days') THEN metadata_size ELSE 0 END),\n       SUM(CASE WHEN DATETIME(metadata_last_used_date, 'unixepoch') >= date('now', '-60 days') THEN metadata_size ELSE 0 END),\n       SUM(CASE WHEN DATETIME(metadata_last_used_date, 'unixepoch') >= date('now', '-90 days') THEN metadata_size ELSE 0 END)\n  FROM "
+ "SELECT SUM(metadata_size), metadata_is_dataless\n FROM "
+ "SELECT rec.fs_id, rec.item_is_flocked, throttle.job_type, throttle.last_error\n  FROM reconciliation_table AS rec\nLEFT JOIN fs_throttle AS throttle ON throttle.item_id == rec.fs_id\nWHERE rec.fs_disk_import_status == "
+ "SQLDB: building FP telemetry report"
+ "T@\"NSArray\",R,N,V_dynamicErrorSampleRatePerProvider"
+ "[CRIT] domain's persona %@ doesn't exist anymore, cleaning up"
+ "[ERROR] %@ called fileproviderd to add a domain for an extension with persona %@ while running in persona %@"
+ "_dynamicErrorSampleRatePerProvider"
+ "_lastDeferralDate"
+ "available_disk_size"
+ "com.apple.CloudDocs.iCloudDriveFileProvider:5"
+ "dynamicErrorSampleRatePerProvider"
+ "evaluateWithObject:"
+ "fp_fpfsProviderDomainID:skipTypeCheck:error:"
+ "fp_realPathRelationshipToItemAtRealPathURL:"
+ "isProviderForRealPathURL:"
+ "itemPendingReconciliationJobCode"
+ "lastDeferralDate"
+ "optimize_storage"
+ "pinned_documents_size"
+ "pinned_resident_pct"
+ "purgeable_high_size"
+ "purgeable_low_size"
+ "purgeable_medium_size"
+ "recent_documents_size_30_days"
+ "recent_documents_size_60_days"
+ "recent_documents_size_90_days"
+ "setXpcActivityTimeSinceLastAbleToRun:"
+ "total_account_size"
+ "xpcActivityIsActive"
+ "⚔️  Fetch thumbnail for %@ finished after global handler was called"
+ "⚔️  Fetch thumbnail for %@ has an unbalanced fetch %ld"
+ "⚔️  Global fetch thumbnail is executed before %ld thumbnails fetch finished"
+ "⚔️ Global fetch thumbnail failed: %@"
- "\x01\xe3"
- "\x04#"
- "- Iconsistent item "
- "SELECT rec.fs_id, rec.item_is_flocked, throttle.job_type\n  FROM reconciliation_table AS rec\nLEFT JOIN fs_throttle AS throttle ON throttle.item_id == rec.fs_id\nWHERE rec.fs_disk_import_status == "
- "URLWithString:"
- "[DEBUG] domain's persona %@ doesn't exist anymore, cleaning up"
- "fp_fpfsProviderDomainID:"
- "isProviderForURL:"
- "uid"
- "unexpected persona %@ (%i) instead of expected %@"

```
