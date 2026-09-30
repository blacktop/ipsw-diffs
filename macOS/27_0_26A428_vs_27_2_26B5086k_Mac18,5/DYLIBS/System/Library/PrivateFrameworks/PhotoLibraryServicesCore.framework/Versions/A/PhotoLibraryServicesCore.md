## PhotoLibraryServicesCore

> `/System/Library/PrivateFrameworks/PhotoLibraryServicesCore.framework/Versions/A/PhotoLibraryServicesCore`

```diff

-911.0.134.0.0
-  __TEXT.__text: 0xcf034
-  __TEXT.__objc_methlist: 0x8494
+916.41.100.0.0
+  __TEXT.__text: 0xd01cc
+  __TEXT.__objc_methlist: 0x84ac
   __TEXT.__const: 0x22b4
   __TEXT.__dlopen_cstrs: 0xe1
-  __TEXT.__gcc_except_tab: 0x56a4
-  __TEXT.__cstring: 0x157b8
-  __TEXT.__oslogstring: 0xb61c
+  __TEXT.__gcc_except_tab: 0x5760
+  __TEXT.__cstring: 0x15884
+  __TEXT.__oslogstring: 0xb79a
   __TEXT.__ustring: 0x4
-  __TEXT.__unwind_info: 0x4198
+  __TEXT.__unwind_info: 0x41f0
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
+  __DATA_CONST.__objc_selrefs: 0x50a0
   __DATA_CONST.__objc_protorefs: 0xc8
   __DATA_CONST.__objc_superrefs: 0x258
-  __DATA_CONST.__objc_arraydata: 0x438
+  __DATA_CONST.__objc_arraydata: 0x440
   __DATA_CONST.__got: 0xa08
-  __AUTH_CONST.__const: 0x5240
+  __AUTH_CONST.__const: 0x52b0
   __AUTH_CONST.__cfstring: 0x11b80
-  __AUTH_CONST.__objc_const: 0xac30
-  __AUTH_CONST.__objc_intobj: 0x900
+  __AUTH_CONST.__objc_const: 0xac28
+  __AUTH_CONST.__objc_intobj: 0x918
   __AUTH_CONST.__objc_dictobj: 0x50
-  __AUTH_CONST.__objc_arrayobj: 0x2a0
-  __AUTH_CONST.__auth_got: 0xd08
+  __AUTH_CONST.__objc_arrayobj: 0x2b8
+  __AUTH_CONST.__auth_got: 0xd10
   __AUTH.__objc_data: 0x2f8
   __DATA.__objc_ivar: 0x694
   __DATA.__data: 0x10e0

   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libperfcheck.dylib
   - /usr/lib/libsqlite3.dylib
-  Functions: 4054
-  Symbols:   9742
-  CStrings:  3655
+  Functions: 4067
+  Symbols:   9762
+  CStrings:  3663
 
Symbols:
+ +[PLFileUtilities addOwnerWritePermissionIfNecessaryToFileAtPath:]
+ +[PLSecurity isEntitledForPrivatePhotosTCCForToken:]
+ -[PLAssetsdLibraryInternalClient getSearchDonationProgressShouldCompute:shouldReport:completionHandler:]
+ -[PLAssetsdNonBindingDebugClient stateCaptureDictionary]
+ -[PLLazyObject isValid]
+ -[PLLazyObject wasInvalidated]
+ GCC_except_table1197
+ GCC_except_table1523
+ GCC_except_table1538
+ GCC_except_table1547
+ GCC_except_table1664
+ GCC_except_table1697
+ GCC_except_table1704
+ GCC_except_table1740
+ GCC_except_table1758
+ GCC_except_table1784
+ GCC_except_table1789
+ GCC_except_table1792
+ GCC_except_table1795
+ GCC_except_table1798
+ GCC_except_table1801
+ GCC_except_table1804
+ GCC_except_table1807
+ GCC_except_table1810
+ GCC_except_table1813
+ GCC_except_table1816
+ GCC_except_table1818
+ GCC_except_table1820
+ GCC_except_table1823
+ GCC_except_table1826
+ GCC_except_table1829
+ GCC_except_table1832
+ GCC_except_table1834
+ GCC_except_table1837
+ GCC_except_table1840
+ GCC_except_table1843
+ GCC_except_table1846
+ GCC_except_table1849
+ GCC_except_table1852
+ GCC_except_table1855
+ GCC_except_table1858
+ GCC_except_table1861
+ GCC_except_table1864
+ GCC_except_table1868
+ GCC_except_table1872
+ GCC_except_table1875
+ GCC_except_table1878
+ GCC_except_table1881
+ GCC_except_table1884
+ GCC_except_table1887
+ GCC_except_table1890
+ GCC_except_table1892
+ GCC_except_table1895
+ GCC_except_table1898
+ GCC_except_table1901
+ GCC_except_table1911
+ GCC_except_table1919
+ GCC_except_table1927
+ GCC_except_table2029
+ GCC_except_table2048
+ GCC_except_table2199
+ GCC_except_table2207
+ GCC_except_table2263
+ GCC_except_table2265
+ GCC_except_table2268
+ GCC_except_table2408
+ GCC_except_table2489
+ GCC_except_table2530
+ GCC_except_table255
+ GCC_except_table2564
+ GCC_except_table2569
+ GCC_except_table2572
+ GCC_except_table2575
+ GCC_except_table2580
+ GCC_except_table2583
+ GCC_except_table2586
+ GCC_except_table2589
+ GCC_except_table2592
+ GCC_except_table2595
+ GCC_except_table2598
+ GCC_except_table2601
+ GCC_except_table261
+ GCC_except_table2615
+ GCC_except_table2624
+ GCC_except_table264
+ GCC_except_table266
+ GCC_except_table2676
+ GCC_except_table268
+ GCC_except_table2688
+ GCC_except_table2691
+ GCC_except_table2702
+ GCC_except_table2706
+ GCC_except_table2709
+ GCC_except_table273
+ GCC_except_table2763
+ GCC_except_table2767
+ GCC_except_table279
+ GCC_except_table2790
+ GCC_except_table2794
+ GCC_except_table2797
+ GCC_except_table2800
+ GCC_except_table2803
+ GCC_except_table282
+ GCC_except_table2838
+ GCC_except_table2852
+ GCC_except_table2853
+ GCC_except_table2855
+ GCC_except_table2858
+ GCC_except_table2864
+ GCC_except_table2867
+ GCC_except_table287
+ GCC_except_table2870
+ GCC_except_table2873
+ GCC_except_table2876
+ GCC_except_table2879
+ GCC_except_table2882
+ GCC_except_table2885
+ GCC_except_table2888
+ GCC_except_table2891
+ GCC_except_table2894
+ GCC_except_table290
+ GCC_except_table2900
+ GCC_except_table2903
+ GCC_except_table2905
+ GCC_except_table295
+ GCC_except_table2961
+ GCC_except_table298
+ GCC_except_table301
+ GCC_except_table3028
+ GCC_except_table3031
+ GCC_except_table3088
+ GCC_except_table310
+ GCC_except_table3143
+ GCC_except_table3157
+ GCC_except_table3161
+ GCC_except_table3163
+ GCC_except_table318
+ GCC_except_table3189
+ GCC_except_table3195
+ GCC_except_table326
+ GCC_except_table329
+ GCC_except_table332
+ GCC_except_table335
+ GCC_except_table3352
+ GCC_except_table3354
+ GCC_except_table3359
+ GCC_except_table3363
+ GCC_except_table3366
+ GCC_except_table3369
+ GCC_except_table3372
+ GCC_except_table3375
+ GCC_except_table3378
+ GCC_except_table338
+ GCC_except_table3430
+ GCC_except_table3432
+ GCC_except_table3467
+ GCC_except_table3572
+ GCC_except_table3642
+ GCC_except_table3646
+ GCC_except_table3653
+ GCC_except_table3707
+ GCC_except_table3710
+ GCC_except_table3716
+ GCC_except_table3719
+ GCC_except_table3722
+ GCC_except_table3725
+ GCC_except_table3731
+ GCC_except_table3737
+ GCC_except_table3741
+ GCC_except_table3745
+ GCC_except_table3749
+ GCC_except_table3753
+ GCC_except_table3774
+ GCC_except_table3777
+ GCC_except_table3799
+ GCC_except_table3817
+ GCC_except_table3825
+ GCC_except_table3827
+ GCC_except_table3832
+ GCC_except_table3836
+ GCC_except_table3842
+ GCC_except_table3850
+ GCC_except_table3853
+ GCC_except_table3860
+ GCC_except_table3867
+ GCC_except_table3870
+ GCC_except_table388
+ GCC_except_table3882
+ GCC_except_table3888
+ GCC_except_table3891
+ GCC_except_table3894
+ GCC_except_table3898
+ GCC_except_table3902
+ GCC_except_table3916
+ GCC_except_table3919
+ GCC_except_table3963
+ GCC_except_table3986
+ GCC_except_table3990
+ GCC_except_table3992
+ GCC_except_table3994
+ GCC_except_table3995
+ GCC_except_table4000
+ GCC_except_table4001
+ GCC_except_table4036
+ GCC_except_table4041
+ GCC_except_table408
+ GCC_except_table414
+ GCC_except_table423
+ GCC_except_table436
+ GCC_except_table492
+ GCC_except_table497
+ GCC_except_table500
+ GCC_except_table503
+ GCC_except_table506
+ GCC_except_table509
+ GCC_except_table512
+ GCC_except_table517
+ GCC_except_table520
+ GCC_except_table523
+ GCC_except_table530
+ GCC_except_table534
+ GCC_except_table537
+ GCC_except_table541
+ GCC_except_table545
+ GCC_except_table551
+ GCC_except_table554
+ GCC_except_table562
+ GCC_except_table566
+ OBJC_IVAR_$_PLLazyObject._invalidated
+ _PLCreateDirectoryIfNeededAndGetSandboxExtensionToken
+ _PLIsErrorOrUnderlyingErrorDatalessMaterializationPrevented
+ _PLPlatformVisualIntelligenceSyncSupported
+ __104-[PLAssetsdLibraryInternalClient getSearchDonationProgressShouldCompute:shouldReport:completionHandler:]_block_invoke
+ __56-[PLAssetsdNonBindingDebugClient stateCaptureDictionary]_block_invoke
+ ___104-[PLAssetsdLibraryInternalClient getSearchDonationProgressShouldCompute:shouldReport:completionHandler:]_block_invoke
+ ___23-[PLLazyObject isValid]_block_invoke
+ ___30-[PLLazyObject wasInvalidated]_block_invoke
+ ___39-[PLLibraryServicesStateNode terminate]_block_invoke
+ ___52+[PLSecurity isEntitledForPrivatePhotosTCCForToken:]_block_invoke
+ ___56-[PLAssetsdNonBindingDebugClient stateCaptureDictionary]_block_invoke
+ ___block_descriptor_98_e8_32bs40n18_8_8_t0w1_s8_t16w32_e51_v16?0"<PLAssetsdLibraryInternalServiceProtocol>"8l
+ _fchmodat
+ _objc_msgSend$addOwnerWritePermissionIfNecessaryToFileAtPath:
+ _objc_msgSend$descriptionWithPath:
+ _objc_msgSend$getSearchDonationProgressShouldCompute:shouldReport:reply:
+ _objc_msgSend$getStateCaptureDictionaryWithReply:
+ _objc_msgSend$isEntitledForPrivatePhotosTCCForToken:
- -[PLPhotoLibraryPathManagerCore assetUUIDRecoveryMappingPath]
- -[PLPhotoLibraryPathManagerCore postInit]
- -[PLPhotoLibraryPathManagerCore setAssetUUIDRecoveryMappingPath:]
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
- GCC_except_table1794
- GCC_except_table1797
- GCC_except_table1800
- GCC_except_table1803
- GCC_except_table1806
- GCC_except_table1809
- GCC_except_table1812
- GCC_except_table1815
- GCC_except_table1817
- GCC_except_table1819
- GCC_except_table1822
- GCC_except_table1825
- GCC_except_table1828
- GCC_except_table1831
- GCC_except_table1833
- GCC_except_table1836
- GCC_except_table1839
- GCC_except_table1842
- GCC_except_table1845
- GCC_except_table1848
- GCC_except_table1851
- GCC_except_table1854
- GCC_except_table1857
- GCC_except_table1860
- GCC_except_table1863
- GCC_except_table1867
- GCC_except_table1871
- GCC_except_table1874
- GCC_except_table1877
- GCC_except_table1880
- GCC_except_table1883
- GCC_except_table1886
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
- GCC_except_table2259
- GCC_except_table2402
- GCC_except_table2482
- GCC_except_table2523
- GCC_except_table254
- GCC_except_table2557
- GCC_except_table2562
- GCC_except_table2565
- GCC_except_table2568
- GCC_except_table2573
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
- GCC_except_table265
- GCC_except_table2664
- GCC_except_table2668
- GCC_except_table267
- GCC_except_table2675
- GCC_except_table2686
- GCC_except_table2690
- GCC_except_table2701
- GCC_except_table2703
- GCC_except_table2707
- GCC_except_table272
- GCC_except_table2762
- GCC_except_table2766
- GCC_except_table278
- GCC_except_table2789
- GCC_except_table2792
- GCC_except_table2795
- GCC_except_table2798
- GCC_except_table2802
- GCC_except_table281
- GCC_except_table2837
- GCC_except_table2839
- GCC_except_table2844
- GCC_except_table2854
- GCC_except_table2856
- GCC_except_table2859
- GCC_except_table286
- GCC_except_table2865
- GCC_except_table2868
- GCC_except_table2871
- GCC_except_table2874
- GCC_except_table2877
- GCC_except_table2880
- GCC_except_table2883
- GCC_except_table2886
- GCC_except_table2889
- GCC_except_table289
- GCC_except_table2892
- GCC_except_table2895
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
- GCC_except_table317
- GCC_except_table3173
- GCC_except_table3187
- GCC_except_table325
- GCC_except_table328
- GCC_except_table331
- GCC_except_table334
- GCC_except_table3342
- GCC_except_table3344
- GCC_except_table3346
- GCC_except_table3355
- GCC_except_table3358
- GCC_except_table3361
- GCC_except_table3364
- GCC_except_table3367
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
- GCC_except_table3724
- GCC_except_table3728
- GCC_except_table3732
- GCC_except_table3736
- GCC_except_table3740
- GCC_except_table3761
- GCC_except_table3764
- GCC_except_table3773
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
- GCC_except_table3854
- GCC_except_table386
- GCC_except_table3862
- GCC_except_table3865
- GCC_except_table3869
- GCC_except_table3872
- GCC_except_table3881
- GCC_except_table3889
- GCC_except_table3903
- GCC_except_table3906
- GCC_except_table3950
- GCC_except_table3973
- GCC_except_table3974
- GCC_except_table3975
- GCC_except_table3977
- GCC_except_table3979
- GCC_except_table3981
- GCC_except_table3982
- GCC_except_table3984
- GCC_except_table4015
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
- OBJC_IVAR_$_PLPhotoLibraryPathManagerCore._assetUUIDRecoveryMappingPath
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
+ "PLCreateDirectoryIfNeededAndGetSandboxExtensionToken: failed to create directory=%@ error=%@"
+ "PLPhotosErrorCollectionShareNotEnabled"
+ "PLXPC Client: getSearchDonationProgressShouldCompute:shouldReport:completionHandler:"
+ "PLXPC Client: stateCaptureDictionary"
+ "Refusing to change permissions of symlink %@"
+ "Unable to open file %@ to save extended attributes (%{public}s)."
+ "\x83"
- "Unable to open file to save extended attributes (%{public}s)."
- "assetUUIDForPath.plist"
- "\x84"
```
