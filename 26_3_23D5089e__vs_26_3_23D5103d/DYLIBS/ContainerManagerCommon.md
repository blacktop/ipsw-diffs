## ContainerManagerCommon

> `/System/Library/PrivateFrameworks/ContainerManagerCommon.framework/ContainerManagerCommon`

```diff

-725.80.4.0.0
-  __TEXT.__text: 0xeda4c
+725.80.5.0.0
+  __TEXT.__text: 0xee534
   __TEXT.__auth_stubs: 0x2290
-  __TEXT.__objc_methlist: 0xa4fc
+  __TEXT.__objc_methlist: 0xa524
   __TEXT.__const: 0x11a0
-  __TEXT.__cstring: 0x9b92
+  __TEXT.__cstring: 0x9bf6
   __TEXT.__swift5_typeref: 0x5b7
-  __TEXT.__oslogstring: 0xefc2
+  __TEXT.__oslogstring: 0xf1d0
   __TEXT.__constg_swiftt: 0x5a8
   __TEXT.__swift5_reflstr: 0x38a
   __TEXT.__swift5_fieldmd: 0x420

   __TEXT.__unwind_info: 0x2268
   __TEXT.__eh_frame: 0x4a0
   __TEXT.__objc_classname: 0x1dec
-  __TEXT.__objc_methname: 0x1396e
+  __TEXT.__objc_methname: 0x13a7b
   __TEXT.__objc_methtype: 0x41ae
-  __TEXT.__objc_stubs: 0xbba0
+  __TEXT.__objc_stubs: 0xbc00
   __DATA_CONST.__got: 0x398
-  __DATA_CONST.__const: 0x19c8
+  __DATA_CONST.__const: 0x19d0
   __DATA_CONST.__objc_classlist: 0x5d0
   __DATA_CONST.__objc_catlist: 0x28
   __DATA_CONST.__objc_protolist: 0x4a8
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x3588
+  __DATA_CONST.__objc_selrefs: 0x35a0
   __DATA_CONST.__objc_protorefs: 0x78
   __DATA_CONST.__objc_superrefs: 0x4e8
   __DATA_CONST.__objc_arraydata: 0x2d0
   __AUTH_CONST.__auth_got: 0x1158
   __AUTH_CONST.__const: 0x1228
-  __AUTH_CONST.__cfstring: 0x46e0
-  __AUTH_CONST.__objc_const: 0x16440
+  __AUTH_CONST.__cfstring: 0x4740
+  __AUTH_CONST.__objc_const: 0x16488
   __AUTH_CONST.__objc_dictobj: 0x140
   __AUTH_CONST.__objc_intobj: 0x14d0
   __AUTH_CONST.__objc_arrayobj: 0xc0
   __AUTH.__objc_data: 0xb50
   __AUTH.__data: 0x168
-  __DATA.__objc_ivar: 0xbe0
+  __DATA.__objc_ivar: 0xbe4
   __DATA.__data: 0x3930
   __DATA.__crash_info: 0x148
   __DATA.__bss: 0xf78

   - /usr/lib/swift/libswiftXPC.dylib
   - /usr/lib/swift/libswift_Builtin_float.dylib
   - /usr/lib/swift/libswiftos.dylib
-  UUID: EDC4F5D9-A723-3306-A502-5821E41DCC4D
-  Functions: 3453
-  Symbols:   11649
-  CStrings:  6228
+  UUID: 8A42A5A2-BB93-3478-8643-B8BB2A6FD2DD
+  Functions: 3456
+  Symbols:   11660
+  CStrings:  6245
 
Symbols:
+ -[MCMCommandUserDataMigration _migrateContainersWithIdentifierMap:parentMap:containerConfig:]
+ -[MCMCommandUserDataMigration _replaceContainer:withContainer:changingParentIdentifier:]
+ -[MCMContainerMigrator _fixParentsOnMigratedIdentitiesWithContext:]
+ -[MCMContainerMigrator _updateMigratedContainerParentsFromMap:containerConfig:context:]
+ -[MCMStaticConfiguration containerIdentityMigrationParents]
+ GCC_except_table1627
+ GCC_except_table1716
+ GCC_except_table1861
+ GCC_except_table1899
+ GCC_except_table1903
+ GCC_except_table1906
+ GCC_except_table1909
+ GCC_except_table1924
+ GCC_except_table1928
+ GCC_except_table1964
+ GCC_except_table1970
+ GCC_except_table2042
+ GCC_except_table2045
+ GCC_except_table2156
+ GCC_except_table2293
+ GCC_except_table2311
+ GCC_except_table2389
+ GCC_except_table2448
+ GCC_except_table2463
+ GCC_except_table2523
+ GCC_except_table2535
+ GCC_except_table2595
+ GCC_except_table2605
+ GCC_except_table2630
+ GCC_except_table2659
+ GCC_except_table2681
+ GCC_except_table2688
+ GCC_except_table2692
+ GCC_except_table2748
+ GCC_except_table2837
+ GCC_except_table2888
+ GCC_except_table2959
+ _MCMMigrationTypeParentBundleIDUpdate
+ _OBJC_IVAR_$_MCMStaticConfiguration._containerIdentityMigrationParents
+ ___Block_byref_object_copy_.10070
+ ___Block_byref_object_copy_.11866
+ ___Block_byref_object_copy_.12589
+ ___Block_byref_object_copy_.12937
+ ___Block_byref_object_copy_.13498
+ ___Block_byref_object_copy_.14354
+ ___Block_byref_object_copy_.14710
+ ___Block_byref_object_copy_.14971
+ ___Block_byref_object_copy_.4382
+ ___Block_byref_object_copy_.5120
+ ___Block_byref_object_copy_.5390
+ ___Block_byref_object_copy_.7357
+ ___Block_byref_object_copy_.7889
+ ___Block_byref_object_copy_.9045
+ ___Block_byref_object_copy_.9237
+ ___Block_byref_object_copy_.9371
+ ___Block_byref_object_copy_.9839
+ ___Block_byref_object_dispose_.10071
+ ___Block_byref_object_dispose_.11867
+ ___Block_byref_object_dispose_.12590
+ ___Block_byref_object_dispose_.12938
+ ___Block_byref_object_dispose_.13499
+ ___Block_byref_object_dispose_.14355
+ ___Block_byref_object_dispose_.14711
+ ___Block_byref_object_dispose_.14972
+ ___Block_byref_object_dispose_.4383
+ ___Block_byref_object_dispose_.5121
+ ___Block_byref_object_dispose_.5391
+ ___Block_byref_object_dispose_.7358
+ ___Block_byref_object_dispose_.7890
+ ___Block_byref_object_dispose_.9046
+ ___Block_byref_object_dispose_.9238
+ ___Block_byref_object_dispose_.9372
+ ___Block_byref_object_dispose_.9840
+ ___block_literal_global.10967
+ ___block_literal_global.11908
+ ___block_literal_global.12.11906
+ ___block_literal_global.12127
+ ___block_literal_global.12946
+ ___block_literal_global.13297
+ ___block_literal_global.13480
+ ___block_literal_global.13760
+ ___block_literal_global.13963
+ ___block_literal_global.14702
+ ___block_literal_global.14791
+ ___block_literal_global.14811
+ ___block_literal_global.5097
+ ___block_literal_global.5436
+ ___block_literal_global.6611
+ ___block_literal_global.67
+ ___block_literal_global.7251
+ ___block_literal_global.7793
+ ___block_literal_global.8402
+ ___block_literal_global.8673
+ ___block_literal_global.9496
+ ___block_literal_global.9593
+ _defaultManager.onceToken.9485
+ _objc_msgSend$_fixParentsOnMigratedIdentitiesWithContext:
+ _objc_msgSend$_migrateContainersWithIdentifierMap:parentMap:containerConfig:
+ _objc_msgSend$_replaceContainer:withContainer:changingParentIdentifier:
+ _objc_msgSend$_updateMigratedContainerParentsFromMap:containerConfig:context:
+ _objc_msgSend$containerIdentityMigrationParents
+ _sharedInstance.instance.12453
+ _sharedInstance.onceToken.10373
+ _sharedInstance.onceToken.12452
- -[MCMCommandUserDataMigration _migrateContainersWithIdentifierMap:containerConfig:]
- -[MCMCommandUserDataMigration _replaceContainer:withContainer:]
- GCC_except_table1626
- GCC_except_table1715
- GCC_except_table1860
- GCC_except_table1898
- GCC_except_table1902
- GCC_except_table1905
- GCC_except_table1908
- GCC_except_table1923
- GCC_except_table1927
- GCC_except_table1963
- GCC_except_table1969
- GCC_except_table2041
- GCC_except_table2044
- GCC_except_table2155
- GCC_except_table2292
- GCC_except_table2309
- GCC_except_table2388
- GCC_except_table2445
- GCC_except_table2460
- GCC_except_table2520
- GCC_except_table2532
- GCC_except_table2592
- GCC_except_table2602
- GCC_except_table2627
- GCC_except_table2656
- GCC_except_table2678
- GCC_except_table2682
- GCC_except_table2689
- GCC_except_table2745
- GCC_except_table2834
- GCC_except_table2882
- GCC_except_table2956
- ___Block_byref_object_copy_.10058
- ___Block_byref_object_copy_.11856
- ___Block_byref_object_copy_.12564
- ___Block_byref_object_copy_.12914
- ___Block_byref_object_copy_.13474
- ___Block_byref_object_copy_.14331
- ___Block_byref_object_copy_.14687
- ___Block_byref_object_copy_.14948
- ___Block_byref_object_copy_.4381
- ___Block_byref_object_copy_.5119
- ___Block_byref_object_copy_.5389
- ___Block_byref_object_copy_.7347
- ___Block_byref_object_copy_.7879
- ___Block_byref_object_copy_.9035
- ___Block_byref_object_copy_.9227
- ___Block_byref_object_copy_.9361
- ___Block_byref_object_copy_.9829
- ___Block_byref_object_dispose_.10059
- ___Block_byref_object_dispose_.11857
- ___Block_byref_object_dispose_.12565
- ___Block_byref_object_dispose_.12915
- ___Block_byref_object_dispose_.13475
- ___Block_byref_object_dispose_.14332
- ___Block_byref_object_dispose_.14688
- ___Block_byref_object_dispose_.14949
- ___Block_byref_object_dispose_.4382
- ___Block_byref_object_dispose_.5120
- ___Block_byref_object_dispose_.5390
- ___Block_byref_object_dispose_.7348
- ___Block_byref_object_dispose_.7880
- ___Block_byref_object_dispose_.9036
- ___Block_byref_object_dispose_.9228
- ___Block_byref_object_dispose_.9362
- ___Block_byref_object_dispose_.9830
- ___block_literal_global.10958
- ___block_literal_global.11898
- ___block_literal_global.12.11896
- ___block_literal_global.12115
- ___block_literal_global.12923
- ___block_literal_global.13273
- ___block_literal_global.13456
- ___block_literal_global.13736
- ___block_literal_global.13939
- ___block_literal_global.14679
- ___block_literal_global.14768
- ___block_literal_global.14788
- ___block_literal_global.5096
- ___block_literal_global.5435
- ___block_literal_global.64
- ___block_literal_global.6610
- ___block_literal_global.7238
- ___block_literal_global.7783
- ___block_literal_global.8392
- ___block_literal_global.8663
- ___block_literal_global.9486
- ___block_literal_global.9583
- _defaultManager.onceToken.9475
- _objc_msgSend$_migrateContainersWithIdentifierMap:containerConfig:
- _objc_msgSend$_replaceContainer:withContainer:
- _sharedInstance.instance.12428
- _sharedInstance.onceToken.10361
- _sharedInstance.onceToken.12427
CStrings:
+ "20:19:52"
+ "Completed Container Identity Parent Fixup Migration on %@"
+ "Jan  5 2026"
+ "MobileContainerManager-725.80.5~308"
+ "ParentBundleIDUpdate"
+ "Performing Container Identity Parent Fixup Migration on %@"
+ "T@\"NSDictionary\",R,N,V_containerIdentityMigrationParents"
+ "Unable to construct container identity for migration; identifier = [%@], userIdentity = %@, error = (%llu) %s"
+ "Unable to fetch container for migration; identifier = [%@], userIdentity = %@, error = %@"
+ "Unable to fetch metadata for container for migration; identifier = [%@], userIdentity = %@, error = %@"
+ "Unable to write new metadata to container for migration; identifier = [%@], userIdentity = %@, error = %@"
+ "_containerIdentityMigrationParents"
+ "_fixParentsOnMigratedIdentitiesWithContext:"
+ "_migrateContainersWithIdentifierMap:parentMap:containerConfig:"
+ "_replaceContainer:withContainer:changingParentIdentifier:"
+ "_updateMigratedContainerParentsFromMap:containerConfig:context:"
+ "com.apple.MobileInstallation.ParentBundleID"
+ "containerIdentityMigrationParents"
- "20:18:54"
- "Dec 10 2025"
- "MobileContainerManager-725.80.4~36"
- "_migrateContainersWithIdentifierMap:containerConfig:"
- "_replaceContainer:withContainer:"

```
