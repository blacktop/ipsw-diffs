## PhotoLibraryServicesCore

> `/System/Library/PrivateFrameworks/PhotoLibraryServicesCore.framework/PhotoLibraryServicesCore`

```diff

-  __TEXT.__text: 0xca10c
-  __TEXT.__objc_methlist: 0x8264
+  __TEXT.__text: 0xcaf98
+  __TEXT.__objc_methlist: 0x8304
   __TEXT.__const: 0x2324
   __TEXT.__dlopen_cstrs: 0x19c
-  __TEXT.__gcc_except_tab: 0x570c
-  __TEXT.__cstring: 0x15b77
-  __TEXT.__oslogstring: 0xb142
+  __TEXT.__gcc_except_tab: 0x56fc
+  __TEXT.__cstring: 0x15d0f
+  __TEXT.__oslogstring: 0xb0b9
   __TEXT.__ustring: 0x4
-  __TEXT.__unwind_info: 0x3430
+  __TEXT.__unwind_info: 0x3468
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0
   __TEXT.__objc_classname: 0x0
   __TEXT.__objc_methname: 0x0
   __TEXT.__objc_methtype: 0x0
-  __DATA_CONST.__const: 0x3c20
+  __DATA_CONST.__const: 0x3c50
   __DATA_CONST.__objc_classlist: 0x408
   __DATA_CONST.__objc_catlist: 0x10
   __DATA_CONST.__objc_protolist: 0x160
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x4c18
+  __DATA_CONST.__objc_selrefs: 0x4c80
   __DATA_CONST.__objc_protorefs: 0xc8
   __DATA_CONST.__objc_superrefs: 0x268
   __DATA_CONST.__objc_arraydata: 0x420
-  __DATA_CONST.__got: 0xa50
+  __DATA_CONST.__got: 0xa48
   __AUTH_CONST.__const: 0x35e8
-  __AUTH_CONST.__cfstring: 0x11d80
-  __AUTH_CONST.__objc_const: 0xa900
-  __AUTH_CONST.__objc_intobj: 0x900
+  __AUTH_CONST.__cfstring: 0x11e80
+  __AUTH_CONST.__objc_const: 0xaa00
+  __AUTH_CONST.__objc_intobj: 0x918
   __AUTH_CONST.__objc_floatobj: 0x10
   __AUTH_CONST.__objc_dictobj: 0x50
   __AUTH_CONST.__objc_arrayobj: 0x288
-  __AUTH_CONST.__auth_got: 0xe40
-  __AUTH.__objc_data: 0x320
-  __DATA.__objc_ivar: 0x660
+  __AUTH_CONST.__auth_got: 0xe48
+  __AUTH.__objc_data: 0x370
+  __DATA.__objc_ivar: 0x678
   __DATA.__data: 0x10e0
-  __DATA.__bss: 0xdc0
-  __DATA_DIRTY.__objc_data: 0x2530
+  __DATA.__bss: 0xdb0
+  __DATA_DIRTY.__objc_data: 0x24e0
   __DATA_DIRTY.__data: 0x8
-  __DATA_DIRTY.__bss: 0x3f8
+  __DATA_DIRTY.__bss: 0x408
   - /System/Library/Frameworks/AVFoundation.framework/AVFoundation
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/CoreGraphics.framework/CoreGraphics

   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libperfcheck.dylib
   - /usr/lib/libsqlite3.dylib
-  Functions: 3945
-  Symbols:   13373
-  CStrings:  5935
+  Functions: 3961
+  Symbols:   13428
+  CStrings:  5951
 
Sections:
~ __DATA_CONST.__objc_classlist : content changed
~ __DATA_CONST.__objc_catlist : content changed
~ __DATA_CONST.__objc_protolist : content changed
~ __DATA_CONST.__objc_protorefs : content changed
~ __DATA_CONST.__objc_superrefs : content changed
~ __DATA_CONST.__objc_arraydata : content changed
~ __AUTH_CONST.__const : content changed
~ __AUTH_CONST.__objc_floatobj : content changed
~ __AUTH_CONST.__objc_dictobj : content changed
~ __AUTH_CONST.__objc_arrayobj : content changed
~ __DATA.__data : content changed
Symbols:
+ +[PLPhotoLibraryPathManagerCore photolibrarydPrivateGroupContainerName]
+ +[PLPhotoLibraryPathManagerCore systemLibraryPathDefaultsKey]
+ -[PLAppPrivateData _writeThroughGeneration:error:]
+ -[PLAppPrivateData dirtyGeneration]
+ -[PLAppPrivateData ioQueue]
+ -[PLAppPrivateData setDirtyGeneration:]
+ -[PLAppPrivateData setIoQueue:]
+ -[PLAppPrivateData setWrittenGeneration:]
+ -[PLAppPrivateData writtenGeneration]
+ -[PLAssetsdClient invalidateClientSandboxExtensions]
+ -[PLAssetsdClientSandboxExtensions invalidate]
+ -[PLAssetsdClientState invalidate]
+ -[PLFileSystemPersistenceAttributes UUIDStringsForKey:]
+ -[PLFileSystemPersistenceBatchItem setUUIDStrings:forKey:]
+ -[PLPhotoLibraryFileIdentifier initWithAssetUuid:bundleScope:uti:resourceVersion:resourceType:recipeID:storageAccessTier:originalFilename:customSuffix:]
+ -[PLPhotoLibraryFileIdentifier storageAccessTier]
+ GCC_except_table1017
+ GCC_except_table1052
+ GCC_except_table1116
+ GCC_except_table1119
+ GCC_except_table1450
+ GCC_except_table1465
+ GCC_except_table1474
+ GCC_except_table1591
+ GCC_except_table1614
+ GCC_except_table1619
+ GCC_except_table1656
+ GCC_except_table1672
+ GCC_except_table1698
+ GCC_except_table1703
+ GCC_except_table1706
+ GCC_except_table1709
+ GCC_except_table1712
+ GCC_except_table1715
+ GCC_except_table1718
+ GCC_except_table1721
+ GCC_except_table1724
+ GCC_except_table1727
+ GCC_except_table1730
+ GCC_except_table1732
+ GCC_except_table1734
+ GCC_except_table1737
+ GCC_except_table1740
+ GCC_except_table1743
+ GCC_except_table1746
+ GCC_except_table1748
+ GCC_except_table1751
+ GCC_except_table1754
+ GCC_except_table1757
+ GCC_except_table1760
+ GCC_except_table1763
+ GCC_except_table1766
+ GCC_except_table1769
+ GCC_except_table1772
+ GCC_except_table1775
+ GCC_except_table1778
+ GCC_except_table1782
+ GCC_except_table1786
+ GCC_except_table1789
+ GCC_except_table1792
+ GCC_except_table1795
+ GCC_except_table1798
+ GCC_except_table1801
+ GCC_except_table1803
+ GCC_except_table1806
+ GCC_except_table1809
+ GCC_except_table1812
+ GCC_except_table1822
+ GCC_except_table1830
+ GCC_except_table1838
+ GCC_except_table1935
+ GCC_except_table1954
+ GCC_except_table1958
+ GCC_except_table2116
+ GCC_except_table2166
+ GCC_except_table2172
+ GCC_except_table2174
+ GCC_except_table2177
+ GCC_except_table2316
+ GCC_except_table2404
+ GCC_except_table2444
+ GCC_except_table2478
+ GCC_except_table2483
+ GCC_except_table2486
+ GCC_except_table2489
+ GCC_except_table2492
+ GCC_except_table2495
+ GCC_except_table2498
+ GCC_except_table2501
+ GCC_except_table2504
+ GCC_except_table2507
+ GCC_except_table2510
+ GCC_except_table2513
+ GCC_except_table2527
+ GCC_except_table2534
+ GCC_except_table2569
+ GCC_except_table2573
+ GCC_except_table2580
+ GCC_except_table2591
+ GCC_except_table2595
+ GCC_except_table2599
+ GCC_except_table2606
+ GCC_except_table2608
+ GCC_except_table2612
+ GCC_except_table2616
+ GCC_except_table2620
+ GCC_except_table2624
+ GCC_except_table2628
+ GCC_except_table2632
+ GCC_except_table2636
+ GCC_except_table2640
+ GCC_except_table2644
+ GCC_except_table2648
+ GCC_except_table2652
+ GCC_except_table2656
+ GCC_except_table2660
+ GCC_except_table2667
+ GCC_except_table2671
+ GCC_except_table2675
+ GCC_except_table2679
+ GCC_except_table2683
+ GCC_except_table2687
+ GCC_except_table2703
+ GCC_except_table2707
+ GCC_except_table2711
+ GCC_except_table2715
+ GCC_except_table2719
+ GCC_except_table2723
+ GCC_except_table2727
+ GCC_except_table2731
+ GCC_except_table2735
+ GCC_except_table2742
+ GCC_except_table2750
+ GCC_except_table2755
+ GCC_except_table2759
+ GCC_except_table2800
+ GCC_except_table2802
+ GCC_except_table2858
+ GCC_except_table2925
+ GCC_except_table2928
+ GCC_except_table2985
+ GCC_except_table3039
+ GCC_except_table3050
+ GCC_except_table3056
+ GCC_except_table3058
+ GCC_except_table3078
+ GCC_except_table3084
+ GCC_except_table3235
+ GCC_except_table3237
+ GCC_except_table3239
+ GCC_except_table3243
+ GCC_except_table3248
+ GCC_except_table3251
+ GCC_except_table3254
+ GCC_except_table3257
+ GCC_except_table3260
+ GCC_except_table3345
+ GCC_except_table3469
+ GCC_except_table3536
+ GCC_except_table3540
+ GCC_except_table3547
+ GCC_except_table3600
+ GCC_except_table3615
+ GCC_except_table3630
+ GCC_except_table3634
+ GCC_except_table3638
+ GCC_except_table3642
+ GCC_except_table3646
+ GCC_except_table3667
+ GCC_except_table3670
+ GCC_except_table3679
+ GCC_except_table3692
+ GCC_except_table3710
+ GCC_except_table3718
+ GCC_except_table3720
+ GCC_except_table3725
+ GCC_except_table3735
+ GCC_except_table3743
+ GCC_except_table3746
+ GCC_except_table3750
+ GCC_except_table3753
+ GCC_except_table3766
+ GCC_except_table3769
+ GCC_except_table3782
+ GCC_except_table3785
+ GCC_except_table3789
+ GCC_except_table3793
+ GCC_except_table3807
+ GCC_except_table3810
+ GCC_except_table3854
+ GCC_except_table3877
+ GCC_except_table3878
+ GCC_except_table3879
+ GCC_except_table3881
+ GCC_except_table3883
+ GCC_except_table3886
+ GCC_except_table3888
+ GCC_except_table3891
+ GCC_except_table3892
+ GCC_except_table3901
+ GCC_except_table3914
+ GCC_except_table3919
+ GCC_except_table3926
+ GCC_except_table3931
+ GCC_except_table683
+ GCC_except_table715
+ GCC_except_table720
+ GCC_except_table723
+ GCC_except_table726
+ GCC_except_table732
+ GCC_except_table735
+ GCC_except_table738
+ GCC_except_table741
+ GCC_except_table745
+ GCC_except_table748
+ GCC_except_table781
+ GCC_except_table786
+ GCC_except_table790
+ GCC_except_table793
+ GCC_except_table796
+ GCC_except_table799
+ GCC_except_table802
+ GCC_except_table805
+ GCC_except_table808
+ GCC_except_table811
+ GCC_except_table814
+ GCC_except_table817
+ GCC_except_table823
+ GCC_except_table826
+ GCC_except_table829
+ GCC_except_table832
+ GCC_except_table835
+ GCC_except_table838
+ GCC_except_table841
+ GCC_except_table844
+ GCC_except_table847
+ GCC_except_table851
+ GCC_except_table855
+ GCC_except_table858
+ GCC_except_table861
+ GCC_except_table864
+ GCC_except_table867
+ GCC_except_table870
+ GCC_except_table873
+ GCC_except_table876
+ GCC_except_table879
+ GCC_except_table882
+ GCC_except_table885
+ GCC_except_table888
+ GCC_except_table891
+ GCC_except_table894
+ GCC_except_table896
+ GCC_except_table898
+ GCC_except_table901
+ GCC_except_table904
+ GCC_except_table907
+ GCC_except_table910
+ GCC_except_table913
+ GCC_except_table915
+ GCC_except_table918
+ GCC_except_table921
+ GCC_except_table924
+ GCC_except_table927
+ GCC_except_table930
+ GCC_except_table933
+ GCC_except_table937
+ GCC_except_table941
+ GCC_except_table944
+ GCC_except_table947
+ GCC_except_table950
+ GCC_except_table953
+ GCC_except_table956
+ GCC_except_table958
+ _OBJC_IVAR_$_PLAppPrivateData._dirtyGeneration
+ _OBJC_IVAR_$_PLAppPrivateData._ioQueue
+ _OBJC_IVAR_$_PLAppPrivateData._writtenGeneration
+ _OBJC_IVAR_$_PLPhotoLibraryFileIdentifier._storageAccessTier
+ _OBJC_IVAR_$_PLPhotoLibraryPathManagerUBF._resourcesRestrictedDerivativesDirectory
+ _OBJC_IVAR_$_PLPhotoLibraryPathManagerUBF._resourcesRestrictedDirectory
+ _OBJC_IVAR_$_PLPhotoLibraryPathManagerUBF._resourcesRestrictedOriginalsDirectory
+ _PFIsErrorEqualToCode
+ _PLFileSystemPersistenceKeywordsKey
+ _PLFilesAppBundleID
+ _PLResourceStorageTierForResourceType
+ _PLResourcesRestrictedDerivativesDirectoryName
+ _PLResourcesRestrictedDirectoryName
+ _PLResourcesRestrictedOriginalsDirectoryName
+ _PhotoLibraryServicesEntitlementAllowRestrictedResourcesRead
+ ___50-[PLAppPrivateData _writeThroughGeneration:error:]_block_invoke
+ ___block_descriptor_64_e8_32s40r48r_e5_v8?0ls32l8r40l8r48l8
+ _objc_msgSend$UUIDStringsForKey:
+ _objc_msgSend$_writeThroughGeneration:error:
+ _objc_msgSend$dictionaryWithContentsOfURL:
+ _objc_msgSend$dirtyGeneration
+ _objc_msgSend$initWithAssetUuid:bundleScope:uti:resourceVersion:resourceType:recipeID:storageAccessTier:originalFilename:customSuffix:
+ _objc_msgSend$initWithBytesNoCopy:length:freeWhenDone:
+ _objc_msgSend$ioQueue
+ _objc_msgSend$restrictedResourcesAccessAuthorized
+ _objc_msgSend$setDirtyGeneration:
+ _objc_msgSend$setWrittenGeneration:
+ _objc_msgSend$storageAccessTier
+ _objc_msgSend$writtenGeneration
- +[PLPhotoLibraryPathManagerCore _constructLegacySystemPhotoLibraryURLFromUnresolvableBookmark:]
- +[PLPhotoLibraryPathManagerCore _legacySystemLibraryBookmarkData]
- +[PLPhotoLibraryPathManagerCore _legacySystemLibraryPath]
- GCC_except_table1016
- GCC_except_table1051
- GCC_except_table1115
- GCC_except_table1117
- GCC_except_table1449
- GCC_except_table1464
- GCC_except_table1473
- GCC_except_table1590
- GCC_except_table1613
- GCC_except_table1618
- GCC_except_table1655
- GCC_except_table1671
- GCC_except_table1697
- GCC_except_table1702
- GCC_except_table1705
- GCC_except_table1708
- GCC_except_table1711
- GCC_except_table1714
- GCC_except_table1717
- GCC_except_table1720
- GCC_except_table1723
- GCC_except_table1726
- GCC_except_table1729
- GCC_except_table1731
- GCC_except_table1733
- GCC_except_table1736
- GCC_except_table1739
- GCC_except_table1742
- GCC_except_table1745
- GCC_except_table1747
- GCC_except_table1750
- GCC_except_table1753
- GCC_except_table1756
- GCC_except_table1759
- GCC_except_table1762
- GCC_except_table1765
- GCC_except_table1768
- GCC_except_table1771
- GCC_except_table1774
- GCC_except_table1777
- GCC_except_table1781
- GCC_except_table1785
- GCC_except_table1788
- GCC_except_table1791
- GCC_except_table1794
- GCC_except_table1797
- GCC_except_table1800
- GCC_except_table1802
- GCC_except_table1805
- GCC_except_table1808
- GCC_except_table1811
- GCC_except_table1821
- GCC_except_table1829
- GCC_except_table1837
- GCC_except_table1934
- GCC_except_table1953
- GCC_except_table1957
- GCC_except_table2115
- GCC_except_table2165
- GCC_except_table2170
- GCC_except_table2173
- GCC_except_table2176
- GCC_except_table2315
- GCC_except_table2403
- GCC_except_table2442
- GCC_except_table2476
- GCC_except_table2481
- GCC_except_table2484
- GCC_except_table2487
- GCC_except_table2490
- GCC_except_table2493
- GCC_except_table2496
- GCC_except_table2499
- GCC_except_table2502
- GCC_except_table2505
- GCC_except_table2508
- GCC_except_table2511
- GCC_except_table2525
- GCC_except_table2532
- GCC_except_table2566
- GCC_except_table2570
- GCC_except_table2574
- GCC_except_table2582
- GCC_except_table2592
- GCC_except_table2596
- GCC_except_table2600
- GCC_except_table2605
- GCC_except_table2609
- GCC_except_table2613
- GCC_except_table2617
- GCC_except_table2621
- GCC_except_table2625
- GCC_except_table2629
- GCC_except_table2633
- GCC_except_table2637
- GCC_except_table2641
- GCC_except_table2645
- GCC_except_table2649
- GCC_except_table2653
- GCC_except_table2657
- GCC_except_table2661
- GCC_except_table2668
- GCC_except_table2672
- GCC_except_table2676
- GCC_except_table2680
- GCC_except_table2684
- GCC_except_table2688
- GCC_except_table2704
- GCC_except_table2708
- GCC_except_table2712
- GCC_except_table2716
- GCC_except_table2720
- GCC_except_table2724
- GCC_except_table2728
- GCC_except_table2732
- GCC_except_table2736
- GCC_except_table2741
- GCC_except_table2746
- GCC_except_table2756
- GCC_except_table2758
- GCC_except_table2799
- GCC_except_table2855
- GCC_except_table2921
- GCC_except_table2924
- GCC_except_table2981
- GCC_except_table3035
- GCC_except_table3046
- GCC_except_table3048
- GCC_except_table3054
- GCC_except_table3074
- GCC_except_table3080
- GCC_except_table3228
- GCC_except_table3230
- GCC_except_table3232
- GCC_except_table3236
- GCC_except_table3241
- GCC_except_table3244
- GCC_except_table3247
- GCC_except_table3250
- GCC_except_table3253
- GCC_except_table3338
- GCC_except_table3462
- GCC_except_table3530
- GCC_except_table3534
- GCC_except_table3541
- GCC_except_table3594
- GCC_except_table3597
- GCC_except_table3606
- GCC_except_table3628
- GCC_except_table3632
- GCC_except_table3636
- GCC_except_table3640
- GCC_except_table3661
- GCC_except_table3664
- GCC_except_table3673
- GCC_except_table3686
- GCC_except_table3704
- GCC_except_table3712
- GCC_except_table3714
- GCC_except_table3719
- GCC_except_table3723
- GCC_except_table3734
- GCC_except_table3737
- GCC_except_table3744
- GCC_except_table3747
- GCC_except_table3754
- GCC_except_table3757
- GCC_except_table3767
- GCC_except_table3770
- GCC_except_table3783
- GCC_except_table3787
- GCC_except_table3801
- GCC_except_table3804
- GCC_except_table3848
- GCC_except_table3865
- GCC_except_table3866
- GCC_except_table3867
- GCC_except_table3869
- GCC_except_table3871
- GCC_except_table3873
- GCC_except_table3874
- GCC_except_table3876
- GCC_except_table3898
- GCC_except_table3903
- GCC_except_table3910
- GCC_except_table3915
- GCC_except_table682
- GCC_except_table714
- GCC_except_table719
- GCC_except_table722
- GCC_except_table725
- GCC_except_table731
- GCC_except_table734
- GCC_except_table737
- GCC_except_table740
- GCC_except_table743
- GCC_except_table747
- GCC_except_table780
- GCC_except_table785
- GCC_except_table789
- GCC_except_table792
- GCC_except_table795
- GCC_except_table798
- GCC_except_table801
- GCC_except_table804
- GCC_except_table807
- GCC_except_table810
- GCC_except_table813
- GCC_except_table816
- GCC_except_table822
- GCC_except_table825
- GCC_except_table828
- GCC_except_table831
- GCC_except_table834
- GCC_except_table837
- GCC_except_table840
- GCC_except_table843
- GCC_except_table846
- GCC_except_table850
- GCC_except_table854
- GCC_except_table857
- GCC_except_table860
- GCC_except_table863
- GCC_except_table866
- GCC_except_table869
- GCC_except_table872
- GCC_except_table875
- GCC_except_table878
- GCC_except_table881
- GCC_except_table884
- GCC_except_table887
- GCC_except_table890
- GCC_except_table893
- GCC_except_table895
- GCC_except_table897
- GCC_except_table900
- GCC_except_table903
- GCC_except_table906
- GCC_except_table909
- GCC_except_table912
- GCC_except_table914
- GCC_except_table917
- GCC_except_table920
- GCC_except_table923
- GCC_except_table926
- GCC_except_table929
- GCC_except_table932
- GCC_except_table936
- GCC_except_table940
- GCC_except_table943
- GCC_except_table946
- GCC_except_table949
- GCC_except_table952
- GCC_except_table955
- GCC_except_table957
- _NSURLPathKey
- _OBJC_IVAR_$_PLPrimitiveAssetsdClient._sandboxExtensions
- _PLURLForResourceProperties
- ___block_descriptor_64_e8_32s40r48r_e5_v8?0lr40l8s32l8r48l8
- _objc_msgSend$_constructLegacySystemPhotoLibraryURLFromUnresolvableBookmark:
- _objc_msgSend$_legacySystemLibraryBookmarkData
- _objc_msgSend$resourceValuesForKeys:fromBookmarkData:
CStrings:
+ "4"
+ "Error removing old SPL group plist: %@"
+ "Found SPL path in group plist in container prefs location"
+ "Library/Preferences/group.com.apple.photolibraryd.private.plist"
+ "NSString *_pathForResourceProperties(const char *, const char *, PLResourceType, PLResourceVersion, PLResourceRecipeID, BOOL, const char *, const char *, const char *, const char *, const char *, const char *, const char * _Nullable, PLResourceStorageTier, const char *)"
+ "PLPhotosErrorCollectionShareMigrationOriginatingShareModified"
+ "Removed old SPL group plist"
+ "com.apple.DocumentsApp"
+ "com.apple.assetsd.keywords"
+ "com.apple.photos.PLAppPrivateData.io"
+ "com.apple.private.photos.restrictedresources.read"
+ "resources/restricted"
+ "resources/restricted/derivatives"
+ "resources/restricted/originals"
+ "restrictedBase != NULL"
- "$"
- "/Volumes/"
- "Constructed legacy SPL URL based on unresolvable bookmark: %@"
- "Constructed legacy SPL URL from unresolvable bookmark: %@"
- "Legacy system photo library URL exists but it is not resolvable. Returning bogus URL: %@"
- "NSString *_pathForResourceProperties(const char *, const char *, PLResourceType, PLResourceVersion, PLResourceRecipeID, BOOL, const char *, const char *, const char *, const char *, const char *, const char *, const char *)"
- "No NSURLPathKey available from unresolvable bookmark"

```
