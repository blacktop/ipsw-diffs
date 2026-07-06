## PhotoLibraryServicesCore

> `/System/Library/PrivateFrameworks/PhotoLibraryServicesCore.framework/Versions/A/PhotoLibraryServicesCore`

```diff

-  __TEXT.__text: 0xd1e00
-  __TEXT.__objc_methlist: 0x8384
+  __TEXT.__text: 0xd30f4
+  __TEXT.__objc_methlist: 0x8454
   __TEXT.__const: 0x2234
   __TEXT.__dlopen_cstrs: 0xe1
-  __TEXT.__gcc_except_tab: 0x56a0
-  __TEXT.__cstring: 0x151ee
-  __TEXT.__oslogstring: 0xb429
+  __TEXT.__gcc_except_tab: 0x5690
+  __TEXT.__cstring: 0x1539a
+  __TEXT.__oslogstring: 0xb4c7
   __TEXT.__ustring: 0x4
-  __TEXT.__unwind_info: 0x3248
+  __TEXT.__unwind_info: 0x3288
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0
   __TEXT.__objc_classname: 0x0
   __TEXT.__objc_methname: 0x0
   __TEXT.__objc_methtype: 0x0
-  __DATA_CONST.__const: 0x2260
+  __DATA_CONST.__const: 0x2290
   __DATA_CONST.__objc_classlist: 0x400
   __DATA_CONST.__objc_catlist: 0x10
   __DATA_CONST.__objc_protolist: 0x160
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x4fc8
+  __DATA_CONST.__objc_selrefs: 0x5058
   __DATA_CONST.__objc_protorefs: 0xc8
   __DATA_CONST.__objc_superrefs: 0x258
   __DATA_CONST.__objc_arraydata: 0x438
   __DATA_CONST.__got: 0xa08
   __AUTH_CONST.__const: 0x5240
-  __AUTH_CONST.__cfstring: 0x11660
-  __AUTH_CONST.__objc_const: 0xab28
-  __AUTH_CONST.__objc_intobj: 0x8e8
+  __AUTH_CONST.__cfstring: 0x117a0
+  __AUTH_CONST.__objc_const: 0xac28
+  __AUTH_CONST.__objc_intobj: 0x900
   __AUTH_CONST.__objc_dictobj: 0x50
   __AUTH_CONST.__objc_arrayobj: 0x2a0
-  __AUTH_CONST.__auth_got: 0xd00
-  __AUTH.__objc_data: 0x2a8
-  __DATA.__objc_ivar: 0x67c
+  __AUTH_CONST.__auth_got: 0xd08
+  __AUTH.__objc_data: 0x2f8
+  __DATA.__objc_ivar: 0x694
   __DATA.__data: 0x10e0
   __DATA.__bss: 0x868
-  __DATA_DIRTY.__objc_data: 0x2558
+  __DATA_DIRTY.__objc_data: 0x2508
   __DATA_DIRTY.__data: 0x8
   __DATA_DIRTY.__bss: 0x8c8
   - /System/Library/Frameworks/AVFoundation.framework/Versions/A/AVFoundation

   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libperfcheck.dylib
   - /usr/lib/libsqlite3.dylib
-  Functions: 4020
-  Symbols:   10119
-  CStrings:  5835
+  Functions: 4040
+  Symbols:   10167
+  CStrings:  5859
 
Sections:
~ __DATA_CONST.__objc_classlist : content changed
~ __DATA_CONST.__objc_catlist : content changed
~ __DATA_CONST.__objc_protolist : content changed
~ __DATA_CONST.__objc_protorefs : content changed
~ __DATA_CONST.__objc_superrefs : content changed
~ __DATA_CONST.__objc_arraydata : content changed
~ __DATA_CONST.__got : content changed
~ __AUTH_CONST.__const : content changed
~ __AUTH_CONST.__objc_dictobj : content changed
~ __AUTH_CONST.__objc_arrayobj : content changed
~ __DATA.__data : content changed
Symbols:
+ +[PLPhotoLibraryPathManagerCore _removeLegacySystemLibraryBookmarkData]
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
+ GCC_except_table1002
+ GCC_except_table1005
+ GCC_except_table1008
+ GCC_except_table1011
+ GCC_except_table1014
+ GCC_except_table1017
+ GCC_except_table1020
+ GCC_except_table1023
+ GCC_except_table1026
+ GCC_except_table1029
+ GCC_except_table1032
+ GCC_except_table1037
+ GCC_except_table1039
+ GCC_except_table1041
+ GCC_except_table1044
+ GCC_except_table1047
+ GCC_except_table1050
+ GCC_except_table1053
+ GCC_except_table1056
+ GCC_except_table1058
+ GCC_except_table1061
+ GCC_except_table1064
+ GCC_except_table1067
+ GCC_except_table1070
+ GCC_except_table1073
+ GCC_except_table1076
+ GCC_except_table1080
+ GCC_except_table1084
+ GCC_except_table1087
+ GCC_except_table1090
+ GCC_except_table1093
+ GCC_except_table1096
+ GCC_except_table1099
+ GCC_except_table1101
+ GCC_except_table1160
+ GCC_except_table1196
+ GCC_except_table1520
+ GCC_except_table1535
+ GCC_except_table1544
+ GCC_except_table1661
+ GCC_except_table1694
+ GCC_except_table1701
+ GCC_except_table1737
+ GCC_except_table1755
+ GCC_except_table1781
+ GCC_except_table1786
+ GCC_except_table1789
+ GCC_except_table1792
+ GCC_except_table1795
+ GCC_except_table1798
+ GCC_except_table1801
+ GCC_except_table1804
+ GCC_except_table1807
+ GCC_except_table1810
+ GCC_except_table1813
+ GCC_except_table1815
+ GCC_except_table1817
+ GCC_except_table1820
+ GCC_except_table1823
+ GCC_except_table1826
+ GCC_except_table1829
+ GCC_except_table1831
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
+ GCC_except_table1865
+ GCC_except_table1869
+ GCC_except_table1872
+ GCC_except_table1875
+ GCC_except_table1878
+ GCC_except_table1881
+ GCC_except_table1884
+ GCC_except_table1886
+ GCC_except_table1889
+ GCC_except_table1892
+ GCC_except_table1895
+ GCC_except_table1905
+ GCC_except_table1913
+ GCC_except_table1921
+ GCC_except_table2019
+ GCC_except_table2038
+ GCC_except_table2193
+ GCC_except_table2243
+ GCC_except_table2249
+ GCC_except_table2251
+ GCC_except_table2254
+ GCC_except_table2393
+ GCC_except_table2473
+ GCC_except_table2514
+ GCC_except_table2548
+ GCC_except_table2553
+ GCC_except_table2556
+ GCC_except_table2559
+ GCC_except_table2564
+ GCC_except_table2567
+ GCC_except_table2570
+ GCC_except_table2573
+ GCC_except_table2576
+ GCC_except_table2579
+ GCC_except_table2582
+ GCC_except_table2585
+ GCC_except_table2599
+ GCC_except_table2608
+ GCC_except_table2655
+ GCC_except_table2659
+ GCC_except_table2666
+ GCC_except_table2677
+ GCC_except_table2681
+ GCC_except_table2685
+ GCC_except_table2692
+ GCC_except_table2694
+ GCC_except_table2698
+ GCC_except_table2702
+ GCC_except_table2706
+ GCC_except_table2710
+ GCC_except_table2714
+ GCC_except_table2718
+ GCC_except_table2722
+ GCC_except_table2726
+ GCC_except_table2730
+ GCC_except_table2734
+ GCC_except_table2738
+ GCC_except_table2742
+ GCC_except_table2746
+ GCC_except_table2753
+ GCC_except_table2757
+ GCC_except_table2761
+ GCC_except_table2765
+ GCC_except_table2769
+ GCC_except_table2773
+ GCC_except_table2789
+ GCC_except_table2793
+ GCC_except_table2797
+ GCC_except_table2801
+ GCC_except_table2805
+ GCC_except_table2809
+ GCC_except_table2813
+ GCC_except_table2817
+ GCC_except_table2821
+ GCC_except_table2828
+ GCC_except_table2836
+ GCC_except_table2841
+ GCC_except_table2845
+ GCC_except_table2886
+ GCC_except_table2888
+ GCC_except_table2944
+ GCC_except_table3011
+ GCC_except_table3014
+ GCC_except_table3071
+ GCC_except_table3126
+ GCC_except_table3138
+ GCC_except_table3144
+ GCC_except_table3146
+ GCC_except_table3164
+ GCC_except_table3177
+ GCC_except_table3330
+ GCC_except_table3332
+ GCC_except_table3334
+ GCC_except_table3338
+ GCC_except_table3343
+ GCC_except_table3346
+ GCC_except_table3349
+ GCC_except_table3352
+ GCC_except_table3355
+ GCC_except_table3440
+ GCC_except_table3545
+ GCC_except_table3616
+ GCC_except_table3620
+ GCC_except_table3627
+ GCC_except_table3681
+ GCC_except_table3684
+ GCC_except_table3690
+ GCC_except_table3693
+ GCC_except_table3696
+ GCC_except_table3699
+ GCC_except_table3711
+ GCC_except_table3715
+ GCC_except_table3719
+ GCC_except_table3723
+ GCC_except_table3727
+ GCC_except_table3748
+ GCC_except_table3751
+ GCC_except_table3760
+ GCC_except_table3773
+ GCC_except_table3799
+ GCC_except_table3801
+ GCC_except_table3810
+ GCC_except_table3816
+ GCC_except_table3827
+ GCC_except_table3841
+ GCC_except_table3844
+ GCC_except_table3856
+ GCC_except_table3859
+ GCC_except_table3865
+ GCC_except_table3868
+ GCC_except_table3872
+ GCC_except_table3876
+ GCC_except_table3890
+ GCC_except_table3893
+ GCC_except_table3937
+ GCC_except_table3960
+ GCC_except_table3961
+ GCC_except_table3962
+ GCC_except_table3966
+ GCC_except_table3968
+ GCC_except_table3969
+ GCC_except_table3971
+ GCC_except_table3974
+ GCC_except_table3975
+ GCC_except_table3984
+ GCC_except_table3997
+ GCC_except_table4002
+ GCC_except_table4010
+ GCC_except_table4015
+ GCC_except_table697
+ GCC_except_table731
+ GCC_except_table736
+ GCC_except_table739
+ GCC_except_table742
+ GCC_except_table748
+ GCC_except_table752
+ GCC_except_table755
+ GCC_except_table758
+ GCC_except_table762
+ GCC_except_table765
+ GCC_except_table922
+ GCC_except_table927
+ GCC_except_table931
+ GCC_except_table934
+ GCC_except_table937
+ GCC_except_table940
+ GCC_except_table943
+ GCC_except_table946
+ GCC_except_table949
+ GCC_except_table952
+ GCC_except_table955
+ GCC_except_table958
+ GCC_except_table964
+ GCC_except_table967
+ GCC_except_table970
+ GCC_except_table973
+ GCC_except_table976
+ GCC_except_table979
+ GCC_except_table982
+ GCC_except_table985
+ GCC_except_table988
+ GCC_except_table992
+ GCC_except_table996
+ GCC_except_table999
+ OBJC_IVAR_$_PLAppPrivateData._dirtyGeneration
+ OBJC_IVAR_$_PLAppPrivateData._ioQueue
+ OBJC_IVAR_$_PLAppPrivateData._writtenGeneration
+ OBJC_IVAR_$_PLPhotoLibraryFileIdentifier._storageAccessTier
+ OBJC_IVAR_$_PLPhotoLibraryPathManagerUBF._resourcesRestrictedDerivativesDirectory
+ OBJC_IVAR_$_PLPhotoLibraryPathManagerUBF._resourcesRestrictedDirectory
+ OBJC_IVAR_$_PLPhotoLibraryPathManagerUBF._resourcesRestrictedOriginalsDirectory
+ _PFIsErrorEqualToCode
+ _PLFileSystemPersistenceKeywordsKey
+ _PLFilesAppBundleID
+ _PLResourceStorageTierForResourceType
+ _PLResourcesRestrictedDerivativesDirectoryName
+ _PLResourcesRestrictedDirectoryName
+ _PLResourcesRestrictedOriginalsDirectoryName
+ _PhotoLibraryServicesEntitlementAllowRestrictedResourcesRead
+ ___50-[PLAppPrivateData _writeThroughGeneration:error:]_block_invoke
+ _objc_msgSend$UUIDStringsForKey:
+ _objc_msgSend$_removeLegacySystemLibraryBookmarkData
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
- GCC_except_table1001
- GCC_except_table1004
- GCC_except_table1007
- GCC_except_table1010
- GCC_except_table1013
- GCC_except_table1016
- GCC_except_table1019
- GCC_except_table1022
- GCC_except_table1025
- GCC_except_table1028
- GCC_except_table1031
- GCC_except_table1036
- GCC_except_table1038
- GCC_except_table1040
- GCC_except_table1043
- GCC_except_table1046
- GCC_except_table1049
- GCC_except_table1052
- GCC_except_table1055
- GCC_except_table1057
- GCC_except_table1060
- GCC_except_table1063
- GCC_except_table1066
- GCC_except_table1069
- GCC_except_table1072
- GCC_except_table1075
- GCC_except_table1079
- GCC_except_table1083
- GCC_except_table1086
- GCC_except_table1089
- GCC_except_table1092
- GCC_except_table1095
- GCC_except_table1098
- GCC_except_table1100
- GCC_except_table1159
- GCC_except_table1195
- GCC_except_table1519
- GCC_except_table1534
- GCC_except_table1543
- GCC_except_table1660
- GCC_except_table1693
- GCC_except_table1700
- GCC_except_table1736
- GCC_except_table1754
- GCC_except_table1780
- GCC_except_table1785
- GCC_except_table1788
- GCC_except_table1791
- GCC_except_table1794
- GCC_except_table1797
- GCC_except_table1800
- GCC_except_table1803
- GCC_except_table1806
- GCC_except_table1809
- GCC_except_table1812
- GCC_except_table1814
- GCC_except_table1816
- GCC_except_table1819
- GCC_except_table1822
- GCC_except_table1825
- GCC_except_table1828
- GCC_except_table1830
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
- GCC_except_table1864
- GCC_except_table1868
- GCC_except_table1871
- GCC_except_table1874
- GCC_except_table1877
- GCC_except_table1880
- GCC_except_table1883
- GCC_except_table1885
- GCC_except_table1888
- GCC_except_table1891
- GCC_except_table1894
- GCC_except_table1904
- GCC_except_table1912
- GCC_except_table1920
- GCC_except_table2018
- GCC_except_table2037
- GCC_except_table2192
- GCC_except_table2242
- GCC_except_table2247
- GCC_except_table2250
- GCC_except_table2253
- GCC_except_table2392
- GCC_except_table2472
- GCC_except_table2512
- GCC_except_table2546
- GCC_except_table2551
- GCC_except_table2554
- GCC_except_table2557
- GCC_except_table2562
- GCC_except_table2565
- GCC_except_table2568
- GCC_except_table2571
- GCC_except_table2574
- GCC_except_table2577
- GCC_except_table2580
- GCC_except_table2583
- GCC_except_table2597
- GCC_except_table2606
- GCC_except_table2652
- GCC_except_table2656
- GCC_except_table2660
- GCC_except_table2668
- GCC_except_table2678
- GCC_except_table2682
- GCC_except_table2686
- GCC_except_table2691
- GCC_except_table2695
- GCC_except_table2699
- GCC_except_table2703
- GCC_except_table2707
- GCC_except_table2711
- GCC_except_table2715
- GCC_except_table2719
- GCC_except_table2723
- GCC_except_table2727
- GCC_except_table2731
- GCC_except_table2735
- GCC_except_table2739
- GCC_except_table2743
- GCC_except_table2747
- GCC_except_table2754
- GCC_except_table2758
- GCC_except_table2762
- GCC_except_table2766
- GCC_except_table2770
- GCC_except_table2774
- GCC_except_table2790
- GCC_except_table2794
- GCC_except_table2798
- GCC_except_table2802
- GCC_except_table2806
- GCC_except_table2810
- GCC_except_table2814
- GCC_except_table2818
- GCC_except_table2822
- GCC_except_table2827
- GCC_except_table2832
- GCC_except_table2842
- GCC_except_table2844
- GCC_except_table2885
- GCC_except_table2941
- GCC_except_table3007
- GCC_except_table3010
- GCC_except_table3067
- GCC_except_table3122
- GCC_except_table3134
- GCC_except_table3136
- GCC_except_table3142
- GCC_except_table3160
- GCC_except_table3169
- GCC_except_table3323
- GCC_except_table3325
- GCC_except_table3327
- GCC_except_table3331
- GCC_except_table3336
- GCC_except_table3339
- GCC_except_table3342
- GCC_except_table3345
- GCC_except_table3348
- GCC_except_table3433
- GCC_except_table3538
- GCC_except_table3606
- GCC_except_table3610
- GCC_except_table3617
- GCC_except_table3671
- GCC_except_table3674
- GCC_except_table3680
- GCC_except_table3683
- GCC_except_table3686
- GCC_except_table3689
- GCC_except_table3695
- GCC_except_table3701
- GCC_except_table3709
- GCC_except_table3713
- GCC_except_table3717
- GCC_except_table3738
- GCC_except_table3741
- GCC_except_table3750
- GCC_except_table3763
- GCC_except_table3781
- GCC_except_table3789
- GCC_except_table3796
- GCC_except_table3800
- GCC_except_table3811
- GCC_except_table3814
- GCC_except_table3817
- GCC_except_table3839
- GCC_except_table3842
- GCC_except_table3846
- GCC_except_table3855
- GCC_except_table3858
- GCC_except_table3866
- GCC_except_table3880
- GCC_except_table3883
- GCC_except_table3927
- GCC_except_table3944
- GCC_except_table3945
- GCC_except_table3946
- GCC_except_table3948
- GCC_except_table3950
- GCC_except_table3952
- GCC_except_table3953
- GCC_except_table3955
- GCC_except_table3977
- GCC_except_table3982
- GCC_except_table3990
- GCC_except_table3995
- GCC_except_table696
- GCC_except_table730
- GCC_except_table735
- GCC_except_table738
- GCC_except_table741
- GCC_except_table747
- GCC_except_table751
- GCC_except_table754
- GCC_except_table757
- GCC_except_table760
- GCC_except_table764
- GCC_except_table921
- GCC_except_table926
- GCC_except_table930
- GCC_except_table933
- GCC_except_table936
- GCC_except_table939
- GCC_except_table942
- GCC_except_table945
- GCC_except_table948
- GCC_except_table951
- GCC_except_table954
- GCC_except_table957
- GCC_except_table963
- GCC_except_table966
- GCC_except_table969
- GCC_except_table972
- GCC_except_table975
- GCC_except_table978
- GCC_except_table981
- GCC_except_table984
- GCC_except_table987
- GCC_except_table991
- GCC_except_table995
- GCC_except_table998
- OBJC_IVAR_$_PLPrimitiveAssetsdClient._sandboxExtensions
- _PLURLForResourceProperties
CStrings:
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.AnfnE8/Sources/Photos/Projects/PhotoLibraryServicesCore/Sources/PLTaggedPointer.m"
+ "Error removing old SPL group plist: %@"
+ "Found SPL path in group plist in container prefs location"
+ "Library/Preferences/group.com.apple.photolibraryd.private.plist"
+ "NSString *_pathForResourceProperties(const char *, const char *, PLResourceType, PLResourceVersion, PLResourceRecipeID, BOOL, const char *, const char *, const char *, const char *, const char *, const char *, const char * _Nullable, PLResourceStorageTier, const char *)"
+ "PLPhotosErrorCollectionShareMigrationOriginatingShareModified"
+ "Removed legacy SPL bookmark data"
+ "Removed old SPL group plist"
+ "com.apple.DocumentsApp"
+ "com.apple.assetsd.keywords"
+ "com.apple.photos.PLAppPrivateData.io"
+ "com.apple.private.photos.restrictedresources.read"
+ "derivatives"
+ "resources/restricted"
+ "resources/restricted/derivatives"
+ "resources/restricted/originals"
+ "restrictedBase != NULL"
- "$"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.c1NpFB/Sources/Photos/Projects/PhotoLibraryServicesCore/Sources/PLTaggedPointer.m"
- "NSString *_pathForResourceProperties(const char *, const char *, PLResourceType, PLResourceVersion, PLResourceRecipeID, BOOL, const char *, const char *, const char *, const char *, const char *, const char *, const char *)"

```
