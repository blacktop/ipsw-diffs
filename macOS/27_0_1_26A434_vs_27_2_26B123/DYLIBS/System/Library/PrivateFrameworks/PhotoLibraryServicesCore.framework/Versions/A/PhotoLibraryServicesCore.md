## PhotoLibraryServicesCore

> `/System/Library/PrivateFrameworks/PhotoLibraryServicesCore.framework/Versions/A/PhotoLibraryServicesCore`

```diff

-911.0.134.0.0
-  __TEXT.__text: 0xd3df0
-  __TEXT.__objc_methlist: 0x8494
+916.58.114.0.0
+  __TEXT.__text: 0xd645c
+  __TEXT.__objc_methlist: 0x851c
   __TEXT.__const: 0x22b4
   __TEXT.__dlopen_cstrs: 0xe1
-  __TEXT.__gcc_except_tab: 0x56a4
-  __TEXT.__cstring: 0x157b8
-  __TEXT.__oslogstring: 0xb61c
+  __TEXT.__gcc_except_tab: 0x57f4
+  __TEXT.__cstring: 0x158ea
+  __TEXT.__oslogstring: 0xb92d
   __TEXT.__ustring: 0x4
-  __TEXT.__unwind_info: 0x3298
+  __TEXT.__unwind_info: 0x3338
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0
   __TEXT.__objc_classname: 0x0
   __TEXT.__objc_methname: 0x0
   __TEXT.__objc_methtype: 0x0
-  __DATA_CONST.__const: 0x22f0
+  __DATA_CONST.__const: 0x22e8
   __DATA_CONST.__objc_classlist: 0x400
   __DATA_CONST.__objc_catlist: 0x10
   __DATA_CONST.__objc_protolist: 0x160
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x5080
+  __DATA_CONST.__objc_selrefs: 0x5100
   __DATA_CONST.__objc_protorefs: 0xc8
   __DATA_CONST.__objc_superrefs: 0x258
-  __DATA_CONST.__objc_arraydata: 0x438
-  __DATA_CONST.__got: 0xa08
-  __AUTH_CONST.__const: 0x5240
-  __AUTH_CONST.__cfstring: 0x11b80
-  __AUTH_CONST.__objc_const: 0xac30
-  __AUTH_CONST.__objc_intobj: 0x900
+  __DATA_CONST.__objc_arraydata: 0x440
+  __DATA_CONST.__got: 0xa20
+  __AUTH_CONST.__const: 0x5310
+  __AUTH_CONST.__cfstring: 0x11c20
+  __AUTH_CONST.__objc_const: 0xac78
+  __AUTH_CONST.__objc_intobj: 0x918
   __AUTH_CONST.__objc_dictobj: 0x50
-  __AUTH_CONST.__objc_arrayobj: 0x2a0
-  __AUTH_CONST.__auth_got: 0xd08
+  __AUTH_CONST.__objc_arrayobj: 0x2b8
+  __AUTH_CONST.__auth_got: 0xd18
   __AUTH_CONST.__auth_ptr: 0x0
-  __AUTH.__objc_data: 0x2f8
-  __DATA.__objc_ivar: 0x694
+  __AUTH.__objc_data: 0xf0
+  __DATA.__objc_ivar: 0x698
   __DATA.__data: 0x10e0
-  __DATA.__bss: 0x878
-  __DATA_DIRTY.__objc_data: 0x2508
+  __DATA.__bss: 0x898
+  __DATA_DIRTY.__objc_data: 0x2710
   __DATA_DIRTY.__data: 0x8
-  __DATA_DIRTY.__bss: 0x8c8
+  __DATA_DIRTY.__bss: 0x8b8
   - /System/Library/Frameworks/AVFoundation.framework/Versions/A/AVFoundation
   - /System/Library/Frameworks/CoreFoundation.framework/Versions/A/CoreFoundation
   - /System/Library/Frameworks/CoreGraphics.framework/Versions/A/CoreGraphics

   - /System/Library/Frameworks/UniformTypeIdentifiers.framework/Versions/A/UniformTypeIdentifiers
   - /System/Library/Frameworks/_LocationEssentials.framework/Versions/A/_LocationEssentials
   - /System/Library/PrivateFrameworks/AppSupport.framework/Versions/A/AppSupport
+  - /System/Library/PrivateFrameworks/AuthKit.framework/Versions/A/AuthKit
   - /System/Library/PrivateFrameworks/CMPhoto.framework/Versions/A/CMPhoto
   - /System/Library/PrivateFrameworks/CoreAnalytics.framework/Versions/A/CoreAnalytics
   - /System/Library/PrivateFrameworks/PhotoFoundation.framework/Versions/A/PhotoFoundation

   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libperfcheck.dylib
   - /usr/lib/libsqlite3.dylib
-  Functions: 4054
-  Symbols:   9742
-  CStrings:  3655
+  Functions: 4086
+  Symbols:   9800
+  CStrings:  3673
 
Symbols:
+ +[PLAppPrivateData _isOptedIntoLibraryPrivateDataCreationTracking]
+ +[PLFileUtilities addOwnerWritePermissionIfNecessaryToFileAtPath:]
+ +[PLSecurity isEntitledForPrivatePhotosTCCForToken:]
+ -[PLAppPrivateData clearWasCreatedFlag]
+ -[PLAppPrivateData setWasNewlyCreated:]
+ -[PLAppPrivateData wasCreated]
+ -[PLAppPrivateData wasNewlyCreated]
+ -[PLAssetsdCloudInternalClient updateAccessRequestForParticipantWithUUID:toAcceptanceStatus:inCollectionShareWithIdentifier:completionHandler:]
+ -[PLAssetsdLibraryInternalClient getSearchDonationProgressShouldCompute:shouldReport:completionHandler:]
+ -[PLAssetsdLibraryInternalClient migrateLimitedLibraryAccessFromApplication:toApplication:completionHandler:]
+ -[PLAssetsdLibraryInternalClient transferAssetsWithUuids:fromLibraryURL:transferOptions:completionHandler:]
+ -[PLAssetsdLibraryInternalClient transferPersonsWithUuids:fromLibraryURL:transferOptions:completionHandler:]
+ -[PLAssetsdNonBindingDebugClient stateCaptureDictionary]
+ -[PLLazyObject isValid]
+ -[PLLazyObject wasInvalidated]
+ GCC_except_table1034
+ GCC_except_table1036
+ GCC_except_table1038
+ GCC_except_table1055
+ GCC_except_table1077
+ GCC_except_table1081
+ GCC_except_table1098
+ GCC_except_table1157
+ GCC_except_table1198
+ GCC_except_table1524
+ GCC_except_table1539
+ GCC_except_table1548
+ GCC_except_table1665
+ GCC_except_table1698
+ GCC_except_table1705
+ GCC_except_table1741
+ GCC_except_table1759
+ GCC_except_table1785
+ GCC_except_table1787
+ GCC_except_table1789
+ GCC_except_table1818
+ GCC_except_table1821
+ GCC_except_table1823
+ GCC_except_table1834
+ GCC_except_table1837
+ GCC_except_table1840
+ GCC_except_table1866
+ GCC_except_table1869
+ GCC_except_table1872
+ GCC_except_table1876
+ GCC_except_table1889
+ GCC_except_table1892
+ GCC_except_table1895
+ GCC_except_table1898
+ GCC_except_table1900
+ GCC_except_table1903
+ GCC_except_table1906
+ GCC_except_table1909
+ GCC_except_table1919
+ GCC_except_table1927
+ GCC_except_table1935
+ GCC_except_table2037
+ GCC_except_table2056
+ GCC_except_table2208
+ GCC_except_table2216
+ GCC_except_table2266
+ GCC_except_table2271
+ GCC_except_table2272
+ GCC_except_table2274
+ GCC_except_table2277
+ GCC_except_table2417
+ GCC_except_table2498
+ GCC_except_table2539
+ GCC_except_table256
+ GCC_except_table2578
+ GCC_except_table2581
+ GCC_except_table2584
+ GCC_except_table2589
+ GCC_except_table2592
+ GCC_except_table2595
+ GCC_except_table2598
+ GCC_except_table2601
+ GCC_except_table2604
+ GCC_except_table2607
+ GCC_except_table2610
+ GCC_except_table262
+ GCC_except_table2624
+ GCC_except_table2633
+ GCC_except_table2681
+ GCC_except_table2685
+ GCC_except_table2689
+ GCC_except_table2692
+ GCC_except_table2697
+ GCC_except_table270
+ GCC_except_table2700
+ GCC_except_table2718
+ GCC_except_table2720
+ GCC_except_table2724
+ GCC_except_table2728
+ GCC_except_table2732
+ GCC_except_table2736
+ GCC_except_table2740
+ GCC_except_table2744
+ GCC_except_table2748
+ GCC_except_table2752
+ GCC_except_table2756
+ GCC_except_table276
+ GCC_except_table2760
+ GCC_except_table2764
+ GCC_except_table2768
+ GCC_except_table2772
+ GCC_except_table2776
+ GCC_except_table2780
+ GCC_except_table2783
+ GCC_except_table2787
+ GCC_except_table279
+ GCC_except_table2791
+ GCC_except_table2799
+ GCC_except_table2803
+ GCC_except_table2807
+ GCC_except_table2813
+ GCC_except_table2816
+ GCC_except_table2819
+ GCC_except_table2823
+ GCC_except_table2827
+ GCC_except_table2831
+ GCC_except_table2835
+ GCC_except_table284
+ GCC_except_table2843
+ GCC_except_table2851
+ GCC_except_table2855
+ GCC_except_table2858
+ GCC_except_table2860
+ GCC_except_table2863
+ GCC_except_table2866
+ GCC_except_table287
+ GCC_except_table2875
+ GCC_except_table2898
+ GCC_except_table2901
+ GCC_except_table2904
+ GCC_except_table2907
+ GCC_except_table2910
+ GCC_except_table2913
+ GCC_except_table2916
+ GCC_except_table2918
+ GCC_except_table292
+ GCC_except_table295
+ GCC_except_table2974
+ GCC_except_table298
+ GCC_except_table3041
+ GCC_except_table3044
+ GCC_except_table307
+ GCC_except_table3101
+ GCC_except_table315
+ GCC_except_table3156
+ GCC_except_table3168
+ GCC_except_table3170
+ GCC_except_table3174
+ GCC_except_table3176
+ GCC_except_table3194
+ GCC_except_table3202
+ GCC_except_table3208
+ GCC_except_table323
+ GCC_except_table326
+ GCC_except_table329
+ GCC_except_table332
+ GCC_except_table335
+ GCC_except_table3363
+ GCC_except_table3365
+ GCC_except_table3372
+ GCC_except_table3376
+ GCC_except_table3379
+ GCC_except_table3382
+ GCC_except_table3385
+ GCC_except_table3388
+ GCC_except_table3391
+ GCC_except_table3443
+ GCC_except_table3445
+ GCC_except_table3480
+ GCC_except_table3585
+ GCC_except_table3656
+ GCC_except_table3660
+ GCC_except_table3667
+ GCC_except_table3721
+ GCC_except_table3730
+ GCC_except_table3733
+ GCC_except_table3739
+ GCC_except_table3745
+ GCC_except_table3751
+ GCC_except_table3755
+ GCC_except_table3759
+ GCC_except_table3763
+ GCC_except_table3767
+ GCC_except_table3788
+ GCC_except_table3791
+ GCC_except_table3800
+ GCC_except_table3813
+ GCC_except_table3831
+ GCC_except_table3839
+ GCC_except_table384
+ GCC_except_table3841
+ GCC_except_table3846
+ GCC_except_table385
+ GCC_except_table3850
+ GCC_except_table3856
+ GCC_except_table3861
+ GCC_except_table3864
+ GCC_except_table3867
+ GCC_except_table3871
+ GCC_except_table3874
+ GCC_except_table3884
+ GCC_except_table3892
+ GCC_except_table3896
+ GCC_except_table3899
+ GCC_except_table3902
+ GCC_except_table3905
+ GCC_except_table3908
+ GCC_except_table3912
+ GCC_except_table3916
+ GCC_except_table3930
+ GCC_except_table3933
+ GCC_except_table4002
+ GCC_except_table4003
+ GCC_except_table4004
+ GCC_except_table4006
+ GCC_except_table4008
+ GCC_except_table4011
+ GCC_except_table4013
+ GCC_except_table4016
+ GCC_except_table4017
+ GCC_except_table4029
+ GCC_except_table4042
+ GCC_except_table4047
+ GCC_except_table405
+ GCC_except_table4055
+ GCC_except_table4060
+ GCC_except_table411
+ GCC_except_table420
+ GCC_except_table433
+ GCC_except_table489
+ GCC_except_table494
+ GCC_except_table497
+ GCC_except_table500
+ GCC_except_table503
+ GCC_except_table506
+ GCC_except_table509
+ GCC_except_table514
+ GCC_except_table517
+ GCC_except_table520
+ GCC_except_table527
+ GCC_except_table531
+ GCC_except_table534
+ GCC_except_table538
+ GCC_except_table542
+ GCC_except_table548
+ GCC_except_table551
+ GCC_except_table559
+ GCC_except_table563
+ GCC_except_table573
+ GCC_except_table632
+ GCC_except_table694
+ GCC_except_table728
+ GCC_except_table733
+ GCC_except_table745
+ GCC_except_table749
+ GCC_except_table759
+ GCC_except_table919
+ GCC_except_table924
+ GCC_except_table928
+ GCC_except_table961
+ GCC_except_table989
+ GCC_except_table993
+ OBJC_IVAR_$_PLAppPrivateData._wasNewlyCreated
+ OBJC_IVAR_$_PLLazyObject._invalidated
+ _OBJC_CLASS_$_AKAccountManager
+ _OBJC_CLASS_$_NSMutableCharacterSet
+ _PLCreateDirectoryIfNeededAndGetSandboxExtensionToken
+ _PLGetSandboxExtensionTokenCanonical
+ _PLGetSandboxExtensionTokenForProcessCanonical
+ _PLIsChinaAccount
+ _PLIsErrorOrUnderlyingErrorDatalessMaterializationPrevented
+ _PLIsValidContextualVideoThumbnailIdentifier
+ _PLNoFollowPath
+ _PLPlatformBackgroundSearchIndexingSupported
+ _PLPlatformVisualIntelligenceSyncSupported
+ _PLVettedResourcePath
+ _SANDBOX_EXTENSION_CANONICAL
+ __104-[PLAssetsdLibraryInternalClient getSearchDonationProgressShouldCompute:shouldReport:completionHandler:]_block_invoke
+ __143-[PLAssetsdCloudInternalClient updateAccessRequestForParticipantWithUUID:toAcceptanceStatus:inCollectionShareWithIdentifier:completionHandler:]_block_invoke
+ __56-[PLAssetsdNonBindingDebugClient stateCaptureDictionary]_block_invoke
+ ___104-[PLAssetsdLibraryInternalClient getSearchDonationProgressShouldCompute:shouldReport:completionHandler:]_block_invoke
+ ___107-[PLAssetsdLibraryInternalClient transferAssetsWithUuids:fromLibraryURL:transferOptions:completionHandler:]_block_invoke
+ ___108-[PLAssetsdLibraryInternalClient transferPersonsWithUuids:fromLibraryURL:transferOptions:completionHandler:]_block_invoke
+ ___109-[PLAssetsdLibraryInternalClient migrateLimitedLibraryAccessFromApplication:toApplication:completionHandler:]_block_invoke
+ ___109-[PLAssetsdLibraryInternalClient migrateLimitedLibraryAccessFromApplication:toApplication:completionHandler:]_block_invoke_2
+ ___143-[PLAssetsdCloudInternalClient updateAccessRequestForParticipantWithUUID:toAcceptanceStatus:inCollectionShareWithIdentifier:completionHandler:]_block_invoke
+ ___23-[PLLazyObject isValid]_block_invoke
+ ___30-[PLLazyObject wasInvalidated]_block_invoke
+ ___39-[PLLibraryServicesStateNode terminate]_block_invoke
+ ___52+[PLSecurity isEntitledForPrivatePhotosTCCForToken:]_block_invoke
+ ___56-[PLAssetsdNonBindingDebugClient stateCaptureDictionary]_block_invoke
+ ___block_descriptor_112_e8_32s40s48bs56n18_8_8_t0w1_s8_t16w32_e51_v16?0"<PLAssetsdLibraryInternalServiceProtocol>"8l
+ ___block_descriptor_120_e8_32s40s48bs56n18_8_8_t0w1_s8_t16w32_e49_v16?0"<PLAssetsdCloudInternalServiceProtocol>"8l
+ ___block_descriptor_98_e8_32bs40n18_8_8_t0w1_s8_t16w32_e51_v16?0"<PLAssetsdLibraryInternalServiceProtocol>"8l
+ _fchmodat
+ _objc_msgSend$_isOptedIntoLibraryPrivateDataCreationTracking
+ _objc_msgSend$addCharactersInRange:
+ _objc_msgSend$addOwnerWritePermissionIfNecessaryToFileAtPath:
+ _objc_msgSend$appleIDCountryCodeForAccount:
+ _objc_msgSend$characterSetWithRange:
+ _objc_msgSend$descriptionWithPath:
+ _objc_msgSend$getSearchDonationProgressShouldCompute:shouldReport:reply:
+ _objc_msgSend$getStateCaptureDictionaryWithReply:
+ _objc_msgSend$isEntitledForPrivatePhotosTCCForToken:
+ _objc_msgSend$migrateLimitedLibraryAccessFromApplication:toApplication:completionHandler:
+ _objc_msgSend$primaryAuthKitAccount
+ _objc_msgSend$setWasNewlyCreated:
+ _objc_msgSend$updateAccessRequestForParticipantWithUUID:toAcceptanceStatus:inCollectionShareWithIdentifier:reply:
+ _objc_msgSend$wasNewlyCreated
+ _sLibraryURLsCreatedThisLaunch
+ _sLibraryURLsCreatedThisLaunchLock
+ _sandbox_check_by_audit_token
- -[PLAssetsdLibraryClient transferAssetsWithUuids:fromLibraryURL:transferOptions:completionHandler:]
- -[PLAssetsdLibraryClient transferPersonsWithUuids:fromLibraryURL:transferOptions:completionHandler:]
- -[PLPhotoLibraryPathManagerCore assetUUIDRecoveryMappingPath]
- -[PLPhotoLibraryPathManagerCore postInit]
- -[PLPhotoLibraryPathManagerCore setAssetUUIDRecoveryMappingPath:]
- GCC_except_table1032
- GCC_except_table1037
- GCC_except_table1039
- GCC_except_table1056
- GCC_except_table1076
- GCC_except_table1080
- GCC_except_table1099
- GCC_except_table1101
- GCC_except_table1160
- GCC_except_table1196
- GCC_except_table1522
- GCC_except_table1537
- GCC_except_table1546
- GCC_except_table1663
- GCC_except_table1696
- GCC_except_table1703
- GCC_except_table1739
- GCC_except_table1757
- GCC_except_table1783
- GCC_except_table1788
- GCC_except_table1791
- GCC_except_table1817
- GCC_except_table1819
- GCC_except_table1822
- GCC_except_table1833
- GCC_except_table1836
- GCC_except_table1839
- GCC_except_table1867
- GCC_except_table1871
- GCC_except_table1874
- GCC_except_table1877
- GCC_except_table1888
- GCC_except_table1891
- GCC_except_table1894
- GCC_except_table1897
- GCC_except_table1907
- GCC_except_table1915
- GCC_except_table1923
- GCC_except_table2025
- GCC_except_table2044
- GCC_except_table2201
- GCC_except_table2251
- GCC_except_table2256
- GCC_except_table2257
- GCC_except_table2259
- GCC_except_table2262
- GCC_except_table2402
- GCC_except_table2482
- GCC_except_table2523
- GCC_except_table254
- GCC_except_table2557
- GCC_except_table2562
- GCC_except_table2565
- GCC_except_table2568
- GCC_except_table2576
- GCC_except_table2579
- GCC_except_table2582
- GCC_except_table2585
- GCC_except_table2588
- GCC_except_table2591
- GCC_except_table2594
- GCC_except_table260
- GCC_except_table2608
- GCC_except_table2617
- GCC_except_table263
- GCC_except_table2664
- GCC_except_table2668
- GCC_except_table267
- GCC_except_table2672
- GCC_except_table2675
- GCC_except_table2680
- GCC_except_table2683
- GCC_except_table2686
- GCC_except_table2690
- GCC_except_table2694
- GCC_except_table2698
- GCC_except_table2701
- GCC_except_table2719
- GCC_except_table272
- GCC_except_table2723
- GCC_except_table2727
- GCC_except_table2731
- GCC_except_table2735
- GCC_except_table2739
- GCC_except_table2743
- GCC_except_table2747
- GCC_except_table2751
- GCC_except_table2755
- GCC_except_table2759
- GCC_except_table2762
- GCC_except_table2766
- GCC_except_table2770
- GCC_except_table2774
- GCC_except_table2778
- GCC_except_table278
- GCC_except_table2782
- GCC_except_table2786
- GCC_except_table2789
- GCC_except_table2792
- GCC_except_table2798
- GCC_except_table2802
- GCC_except_table2806
- GCC_except_table281
- GCC_except_table2814
- GCC_except_table2818
- GCC_except_table2822
- GCC_except_table2826
- GCC_except_table2830
- GCC_except_table2834
- GCC_except_table2837
- GCC_except_table2842
- GCC_except_table2844
- GCC_except_table2845
- GCC_except_table2850
- GCC_except_table2854
- GCC_except_table2856
- GCC_except_table2859
- GCC_except_table286
- GCC_except_table2862
- GCC_except_table2874
- GCC_except_table289
- GCC_except_table2897
- GCC_except_table294
- GCC_except_table2953
- GCC_except_table297
- GCC_except_table300
- GCC_except_table3020
- GCC_except_table3023
- GCC_except_table3080
- GCC_except_table309
- GCC_except_table3135
- GCC_except_table3147
- GCC_except_table3149
- GCC_except_table3153
- GCC_except_table3155
- GCC_except_table317
- GCC_except_table3173
- GCC_except_table3181
- GCC_except_table3187
- GCC_except_table325
- GCC_except_table328
- GCC_except_table331
- GCC_except_table334
- GCC_except_table3342
- GCC_except_table3344
- GCC_except_table3346
- GCC_except_table3350
- GCC_except_table3355
- GCC_except_table3358
- GCC_except_table3361
- GCC_except_table3364
- GCC_except_table337
- GCC_except_table3452
- GCC_except_table3558
- GCC_except_table3629
- GCC_except_table3633
- GCC_except_table3640
- GCC_except_table3694
- GCC_except_table3697
- GCC_except_table3703
- GCC_except_table3706
- GCC_except_table3709
- GCC_except_table3712
- GCC_except_table3718
- GCC_except_table3728
- GCC_except_table3732
- GCC_except_table3740
- GCC_except_table3761
- GCC_except_table3764
- GCC_except_table3773
- GCC_except_table3786
- GCC_except_table3804
- GCC_except_table3812
- GCC_except_table3814
- GCC_except_table3819
- GCC_except_table3823
- GCC_except_table3829
- GCC_except_table3834
- GCC_except_table3837
- GCC_except_table3840
- GCC_except_table3844
- GCC_except_table3847
- GCC_except_table3854
- GCC_except_table3857
- GCC_except_table386
- GCC_except_table3862
- GCC_except_table3865
- GCC_except_table3869
- GCC_except_table387
- GCC_except_table3872
- GCC_except_table3875
- GCC_except_table3878
- GCC_except_table3885
- GCC_except_table3903
- GCC_except_table3906
- GCC_except_table3950
- GCC_except_table3973
- GCC_except_table3974
- GCC_except_table3975
- GCC_except_table3979
- GCC_except_table3981
- GCC_except_table3982
- GCC_except_table3984
- GCC_except_table3987
- GCC_except_table3988
- GCC_except_table3997
- GCC_except_table4015
- GCC_except_table4023
- GCC_except_table4028
- GCC_except_table407
- GCC_except_table413
- GCC_except_table422
- GCC_except_table435
- GCC_except_table491
- GCC_except_table496
- GCC_except_table499
- GCC_except_table502
- GCC_except_table505
- GCC_except_table508
- GCC_except_table511
- GCC_except_table516
- GCC_except_table519
- GCC_except_table522
- GCC_except_table529
- GCC_except_table533
- GCC_except_table536
- GCC_except_table540
- GCC_except_table544
- GCC_except_table550
- GCC_except_table553
- GCC_except_table561
- GCC_except_table565
- GCC_except_table576
- GCC_except_table635
- GCC_except_table697
- GCC_except_table731
- GCC_except_table742
- GCC_except_table748
- GCC_except_table761
- GCC_except_table765
- GCC_except_table922
- GCC_except_table927
- GCC_except_table958
- GCC_except_table988
- GCC_except_table992
- OBJC_IVAR_$_PLPhotoLibraryPathManagerCore._assetUUIDRecoveryMappingPath
- _PLAssetUUIDRecoveryMappingFileName
- _PLIsSharedCollectionsFeatureEnabled
- _PUTGetCurrentAccess
- ___100-[PLAssetsdLibraryClient transferPersonsWithUuids:fromLibraryURL:transferOptions:completionHandler:]_block_invoke
- ___62+[PLSecurity isEntitledForPhotoKitOrPrivatePhotosTCCForToken:]_block_invoke
- ___99-[PLAssetsdLibraryClient transferAssetsWithUuids:fromLibraryURL:transferOptions:completionHandler:]_block_invoke
- _objc_msgSend$postInit
- _objc_msgSend$setAssetUUIDRecoveryMappingPath:
CStrings:
+ "%s%@%@.%s"
+ "-[PLAssetsdLibraryInternalClient getSearchDonationProgressShouldCompute:shouldReport:completionHandler:]_block_invoke"
+ "-[PLAssetsdNonBindingDebugClient stateCaptureDictionary]_block_invoke"
+ "/.nofollow"
+ "Added owner read and write permission to %@ (was %o)"
+ "CN"
+ "Contextual video thumbnail identifier is not usable as part of a filename"
+ "Failed to add owner read and write permission to %@ (%{public}s)."
+ "PLCreateDirectoryIfNeededAndGetSandboxExtensionToken: failed to create directory=%@ error=%@"
+ "PLFileBackedLogger: Failed to open log file at %@. Error: %@"
+ "PLFileBackedLogger: close url backed logger: %@"
+ "PLFileBackedLogger: open url backed logger: %@"
+ "PLFileBackedLogger: open url found a corrupt log file. Attempting repair for: %@"
+ "PLPhotosErrorCollectionShareNotEnabled"
+ "PLXPC Client: getSearchDonationProgressShouldCompute:shouldReport:completionHandler:"
+ "PLXPC Client: migrateLimitedLibraryAccessFromApplication:toApplication:completionHandler:"
+ "PLXPC Client: stateCaptureDictionary"
+ "PLXPC Client: updateAccessRequestForParticipantWithUUID:toAcceptanceStatus:inCollectionShareWithIdentifier:completionHandler:"
+ "Refusing to change permissions of symlink %@"
+ "Refusing to map '%@': redirected or non-regular."
+ "Unable to open file %@ to save extended attributes (%{public}s)."
+ "Unable to update access request (%@)"
+ "Unable to update access request for participant in collection share with identifier: %@. (%@)"
+ "XCTestCase"
+ "newBundleIdentifier"
+ "oldBundleIdentifier"
+ "\x83"
- "%s%@%s.%s"
- "PLFileBackedLogger: Failed to open log file. Error: %@"
- "PLFileBackedLogger: close url backed logger: %{public}@"
- "PLFileBackedLogger: open url backed logger: %{public}@"
- "PLFileBackedLogger: open url found a corrupt log file. Attempting repair for: %{public}@"
- "Unable to open file to save extended attributes (%{public}s)."
- "XCTestProbe"
- "assetUUIDForPath.plist"
- "\x84"
```
