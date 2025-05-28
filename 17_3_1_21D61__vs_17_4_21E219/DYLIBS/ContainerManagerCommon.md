## ContainerManagerCommon

> `/System/Library/PrivateFrameworks/ContainerManagerCommon.framework/ContainerManagerCommon`

```diff

-582.80.2.0.0
-  __TEXT.__text: 0xb315c
+582.100.15.0.0
+  __TEXT.__text: 0xb3814
   __TEXT.__auth_stubs: 0x19f0
-  __TEXT.__objc_methlist: 0x6950
+  __TEXT.__objc_methlist: 0x6990
   __TEXT.__const: 0x530
-  __TEXT.__oslogstring: 0xd405
-  __TEXT.__cstring: 0xd1e2
-  __TEXT.__gcc_except_tab: 0x1e00
+  __TEXT.__oslogstring: 0xd431
+  __TEXT.__cstring: 0xd1d1
+  __TEXT.__gcc_except_tab: 0x1e38
   __TEXT.__ustring: 0x43c
   __TEXT.__dlopen_cstrs: 0x66
-  __TEXT.__unwind_info: 0x1944
+  __TEXT.__unwind_info: 0x194c
   __TEXT.__objc_classname: 0x17f3
-  __TEXT.__objc_methname: 0xf4ce
-  __TEXT.__objc_methtype: 0x3304
-  __TEXT.__objc_stubs: 0x9c80
-  __DATA_CONST.__got: 0x138
+  __TEXT.__objc_methname: 0xf64c
+  __TEXT.__objc_methtype: 0x3307
+  __TEXT.__objc_stubs: 0x9ce0
+  __DATA_CONST.__got: 0x140
   __DATA_CONST.__const: 0x15c0
   __DATA_CONST.__objc_classlist: 0x528
   __DATA_CONST.__objc_catlist: 0x20
   __DATA_CONST.__objc_protolist: 0x280
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_const: 0xf1e0
-  __DATA_CONST.__objc_selrefs: 0x2ad0
-  __DATA_CONST.__objc_arraydata: 0x250
-  __AUTH_CONST.__const: 0x600
-  __AUTH_CONST.__cfstring: 0x6200
+  __DATA_CONST.__objc_const: 0xf290
+  __DATA_CONST.__objc_selrefs: 0x2af8
+  __DATA_CONST.__objc_protorefs: 0x18
+  __DATA_CONST.__objc_classrefs: 0x5c8
+  __DATA_CONST.__objc_superrefs: 0x480
+  __DATA_CONST.__objc_arraydata: 0x260
+  __AUTH_CONST.__const: 0x620
+  __AUTH_CONST.__cfstring: 0x6220
   __AUTH_CONST.__objc_const: 0x4480
   __AUTH_CONST.__objc_dictobj: 0xc8
-  __AUTH_CONST.__objc_intobj: 0xf0
+  __AUTH_CONST.__objc_intobj: 0x1b0
   __AUTH_CONST.__objc_arrayobj: 0xa8
   __AUTH_CONST.__auth_got: 0xd08
-  __AUTH.__objc_data: 0x730
-  __DATA.__objc_protorefs: 0x18
-  __DATA.__objc_classrefs: 0x5c8
-  __DATA.__objc_superrefs: 0x480
-  __DATA.__objc_ivar: 0x908
+  __AUTH.__objc_data: 0x6e0
+  __DATA.__objc_ivar: 0x914
   __DATA.__data: 0x1f28
   __DATA.__crash_info: 0x40
   __DATA.__bss: 0x108
-  __DATA_DIRTY.__objc_data: 0x2c60
+  __DATA_DIRTY.__objc_data: 0x2cb0
   __DATA_DIRTY.__data: 0x8
-  __DATA_DIRTY.__bss: 0x2f0
+  __DATA_DIRTY.__bss: 0x300
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/Foundation.framework/Foundation
   - /System/Library/Frameworks/IOKit.framework/Versions/A/IOKit

   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libsandbox.1.dylib
   - /usr/lib/libsqlite3.dylib
-  Functions: 2393
-  Symbols:   9219
-  CStrings:  4993
+  Functions: 2399
+  Symbols:   9241
+  CStrings:  5005
 
Symbols:
+ -[MCMCodeSigningMapping _onQueue_iterateGroupIdsWithKey:fallBackKey:noReferenceKey:forAllIdentifiersUsingBlock:]
+ -[MCMEntitlements _arrayOfStringsFromArray:]
+ -[MCMEntitlements _dataProtectionClassFromString:]
+ -[MCMEntitlements dataProtectionClassIfAvailable]
+ -[MCMManagedUserPathRegistry containermanagerUserCaches]
+ -[MCMManagedUserPathRegistry containermanagerUserDeathrow]
+ -[MCMManagedUserPathRegistry userCaches]
+ GCC_except_table1029
+ GCC_except_table1031
+ GCC_except_table1035
+ GCC_except_table1036
+ GCC_except_table1187
+ GCC_except_table1213
+ GCC_except_table1269
+ GCC_except_table1407
+ GCC_except_table1445
+ GCC_except_table1457
+ GCC_except_table1471
+ GCC_except_table1478
+ GCC_except_table1514
+ GCC_except_table1520
+ GCC_except_table1656
+ GCC_except_table1669
+ GCC_except_table1789
+ GCC_except_table1806
+ GCC_except_table1807
+ GCC_except_table1884
+ GCC_except_table1936
+ GCC_except_table1962
+ GCC_except_table1983
+ GCC_except_table1987
+ GCC_except_table2011
+ GCC_except_table2021
+ GCC_except_table2045
+ GCC_except_table2074
+ GCC_except_table2092
+ GCC_except_table2096
+ GCC_except_table2098
+ GCC_except_table2102
+ GCC_except_table2157
+ GCC_except_table2238
+ GCC_except_table2289
+ GCC_except_table2353
+ GCC_except_table597
+ GCC_except_table598
+ GCC_except_table613
+ GCC_except_table664
+ GCC_except_table673
+ GCC_except_table677
+ GCC_except_table679
+ GCC_except_table691
+ GCC_except_table720
+ GCC_except_table746
+ GCC_except_table748
+ GCC_except_table793
+ GCC_except_table801
+ GCC_except_table805
+ GCC_except_table841
+ GCC_except_table842
+ GCC_except_table854
+ GCC_except_table856
+ GCC_except_table860
+ GCC_except_table868
+ GCC_except_table870
+ GCC_except_table876
+ GCC_except_table878
+ GCC_except_table880
+ GCC_except_table885
+ GCC_except_table887
+ GCC_except_table892
+ GCC_except_table894
+ GCC_except_table903
+ GCC_except_table905
+ GCC_except_table913
+ GCC_except_table927
+ GCC_except_table937
+ GCC_except_table942
+ GCC_except_table946
+ GCC_except_table948
+ GCC_except_table981
+ _MCMDataProtectionClassCompare.dataProtectionClassPrecedence
+ _MCMDataProtectionClassCompare.onceToken
+ _NSFileProtectionCompleteWhenUserInactive
+ _OBJC_IVAR_$_MCMManagedUserPathRegistry._containermanagerUserCaches
+ _OBJC_IVAR_$_MCMManagedUserPathRegistry._containermanagerUserDeathrow
+ _OBJC_IVAR_$_MCMManagedUserPathRegistry._userCaches
+ __OBJC_$_PROP_LIST_MCMClientCodeSignInfo.90
+ __OBJC_$_PROP_LIST_MCMClientMessageContext.86
+ __OBJC_$_PROP_LIST_MCMCommandContext.83
+ __OBJC_$_PROP_LIST_MCMContainerCache.152
+ __OBJC_$_PROP_LIST_MCMContainerClassCache.166
+ __OBJC_$_PROP_LIST_MCMDeleteManifest.122
+ __OBJC_$_PROP_LIST_MCMFSNode.88
+ __OBJC_$_PROP_LIST_MCMFileHandle.198
+ __OBJC_$_PROP_LIST_MCMManagedPath.112
+ __OBJC_$_PROP_LIST_MCMMetadata.243
+ __OBJC_$_PROP_LIST_MCMMetadataMinimal.204
+ __OBJC_$_PROP_LIST_MCMReply.96
+ __OBJC_$_PROP_LIST_MCMResultPromise.70
+ __OBJC_$_PROP_LIST_MCMVolumeChangeMonitor.102
+ ___112-[MCMCodeSigningMapping _onQueue_iterateGroupIdsWithKey:fallBackKey:noReferenceKey:forAllIdentifiersUsingBlock:]_block_invoke
+ ___126-[MCMCodeSigningMapping _onQueue_handleChangeFromOldGroupContainerIds:toNewGroupContainerIds:containerClass:reconcileHandler:]_block_invoke.246
+ ___44-[MCMEntitlements _arrayOfStringsFromArray:]_block_invoke
+ ___84-[MCMCodeSigningMapping _onQueue_removeReferenceForGroupIdentifiers:containerClass:]_block_invoke.257
+ ___Block_byref_object_copy_.10972
+ ___Block_byref_object_copy_.11509
+ ___Block_byref_object_copy_.12316
+ ___Block_byref_object_copy_.12885
+ ___Block_byref_object_copy_.2116
+ ___Block_byref_object_copy_.2741
+ ___Block_byref_object_copy_.3334
+ ___Block_byref_object_copy_.3639
+ ___Block_byref_object_copy_.4355
+ ___Block_byref_object_copy_.5881
+ ___Block_byref_object_copy_.6234
+ ___Block_byref_object_copy_.7291
+ ___Block_byref_object_copy_.7421
+ ___Block_byref_object_copy_.7586
+ ___Block_byref_object_copy_.8152
+ ___Block_byref_object_copy_.966
+ ___Block_byref_object_copy_.9841
+ ___Block_byref_object_dispose_.10973
+ ___Block_byref_object_dispose_.11510
+ ___Block_byref_object_dispose_.12317
+ ___Block_byref_object_dispose_.12886
+ ___Block_byref_object_dispose_.2117
+ ___Block_byref_object_dispose_.2742
+ ___Block_byref_object_dispose_.3335
+ ___Block_byref_object_dispose_.3640
+ ___Block_byref_object_dispose_.4356
+ ___Block_byref_object_dispose_.5882
+ ___Block_byref_object_dispose_.6235
+ ___Block_byref_object_dispose_.7292
+ ___Block_byref_object_dispose_.7422
+ ___Block_byref_object_dispose_.7587
+ ___Block_byref_object_dispose_.8153
+ ___Block_byref_object_dispose_.967
+ ___Block_byref_object_dispose_.9842
+ ___MCMDataProtectionClassCompare_block_invoke
+ ____containermanagerd_perform_launch_tasks_block_invoke.208
+ ____containermanagerd_perform_launch_tasks_block_invoke.214
+ ____containermanagerd_start_xpc_block_invoke.158
+ ___block_descriptor_72_e8_32s40s48s56s64bs_e42_v24?0"NSString"8"MCMCodeSigningEntry"16ls32l8s40l8s48l8s56l8s64l8
+ ___block_literal_global.10141
+ ___block_literal_global.10981
+ ___block_literal_global.11322
+ ___block_literal_global.11754
+ ___block_literal_global.11973
+ ___block_literal_global.1209
+ ___block_literal_global.12635
+ ___block_literal_global.1267
+ ___block_literal_global.12720
+ ___block_literal_global.12741
+ ___block_literal_global.1365
+ ___block_literal_global.1695
+ ___block_literal_global.204
+ ___block_literal_global.210
+ ___block_literal_global.216
+ ___block_literal_global.2226
+ ___block_literal_global.237
+ ___block_literal_global.239
+ ___block_literal_global.2577
+ ___block_literal_global.4390
+ ___block_literal_global.5414
+ ___block_literal_global.6138
+ ___block_literal_global.6715
+ ___block_literal_global.6983
+ ___block_literal_global.7590
+ ___block_literal_global.7794
+ ___block_literal_global.7902
+ ___block_literal_global.884
+ ___block_literal_global.8974
+ ___block_literal_global.972
+ ___block_literal_global.9885
+ __unnamed_array_storage.1412
+ __unnamed_array_storage.1668
+ __unnamed_array_storage.2129
+ __unnamed_array_storage.3693
+ __unnamed_array_storage.8868
+ _defaultManager.onceToken.7783
+ _objc_msgSend$_arrayOfStringsFromArray:
+ _objc_msgSend$_dataProtectionClassFromString:
+ _objc_msgSend$_onQueue_iterateGroupIdsWithKey:fallBackKey:noReferenceKey:forAllIdentifiersUsingBlock:
+ _objc_msgSend$containermanagerUserDeathrow
+ _objc_msgSend$dataProtectionClassIfAvailable
+ _sharedInstance.instance.10483
+ _sharedInstance.onceToken.10482
+ _sharedInstance.onceToken.8551
- +[MCMContainerClassDeletedPath _deletedComponent]
- -[MCMCodeSigningMapping _onQueue_iterateGroupIdsWithKey:fallBackKey:forAllIdentifiersUsingBlock:]
- GCC_except_table1026
- GCC_except_table1028
- GCC_except_table1032
- GCC_except_table1033
- GCC_except_table1184
- GCC_except_table1210
- GCC_except_table1266
- GCC_except_table1404
- GCC_except_table1442
- GCC_except_table1448
- GCC_except_table1468
- GCC_except_table1474
- GCC_except_table1510
- GCC_except_table1516
- GCC_except_table1649
- GCC_except_table1661
- GCC_except_table1781
- GCC_except_table1798
- GCC_except_table1799
- GCC_except_table1876
- GCC_except_table1928
- GCC_except_table1954
- GCC_except_table1975
- GCC_except_table1979
- GCC_except_table2003
- GCC_except_table2013
- GCC_except_table2037
- GCC_except_table2066
- GCC_except_table2084
- GCC_except_table2088
- GCC_except_table2090
- GCC_except_table2094
- GCC_except_table2149
- GCC_except_table2232
- GCC_except_table2283
- GCC_except_table2347
- GCC_except_table594
- GCC_except_table595
- GCC_except_table610
- GCC_except_table661
- GCC_except_table670
- GCC_except_table674
- GCC_except_table676
- GCC_except_table682
- GCC_except_table717
- GCC_except_table743
- GCC_except_table745
- GCC_except_table790
- GCC_except_table798
- GCC_except_table802
- GCC_except_table838
- GCC_except_table839
- GCC_except_table851
- GCC_except_table853
- GCC_except_table857
- GCC_except_table862
- GCC_except_table867
- GCC_except_table873
- GCC_except_table875
- GCC_except_table877
- GCC_except_table879
- GCC_except_table884
- GCC_except_table886
- GCC_except_table891
- GCC_except_table897
- GCC_except_table902
- GCC_except_table910
- GCC_except_table924
- GCC_except_table934
- GCC_except_table939
- GCC_except_table943
- GCC_except_table945
- GCC_except_table978
- __OBJC_$_PROP_LIST_MCMClientCodeSignInfo.89
- __OBJC_$_PROP_LIST_MCMClientMessageContext.85
- __OBJC_$_PROP_LIST_MCMCommandContext.82
- __OBJC_$_PROP_LIST_MCMContainerCache.151
- __OBJC_$_PROP_LIST_MCMContainerClassCache.165
- __OBJC_$_PROP_LIST_MCMDeleteManifest.121
- __OBJC_$_PROP_LIST_MCMFSNode.87
- __OBJC_$_PROP_LIST_MCMFileHandle.195
- __OBJC_$_PROP_LIST_MCMManagedPath.111
- __OBJC_$_PROP_LIST_MCMMetadata.242
- __OBJC_$_PROP_LIST_MCMMetadataMinimal.203
- __OBJC_$_PROP_LIST_MCMReply.95
- __OBJC_$_PROP_LIST_MCMResultPromise.69
- __OBJC_$_PROP_LIST_MCMVolumeChangeMonitor.101
- ___126-[MCMCodeSigningMapping _onQueue_handleChangeFromOldGroupContainerIds:toNewGroupContainerIds:containerClass:reconcileHandler:]_block_invoke.243
- ___59+[MCMContainerClassDeletedPath deletedURLWithUserIdentity:]_block_invoke
- ___84-[MCMCodeSigningMapping _onQueue_removeReferenceForGroupIdentifiers:containerClass:]_block_invoke.254
- ___97-[MCMCodeSigningMapping _onQueue_iterateGroupIdsWithKey:fallBackKey:forAllIdentifiersUsingBlock:]_block_invoke
- ___Block_byref_object_copy_.10903
- ___Block_byref_object_copy_.11439
- ___Block_byref_object_copy_.12245
- ___Block_byref_object_copy_.12818
- ___Block_byref_object_copy_.2103
- ___Block_byref_object_copy_.2717
- ___Block_byref_object_copy_.3305
- ___Block_byref_object_copy_.3606
- ___Block_byref_object_copy_.4315
- ___Block_byref_object_copy_.5837
- ___Block_byref_object_copy_.6188
- ___Block_byref_object_copy_.7242
- ___Block_byref_object_copy_.7364
- ___Block_byref_object_copy_.7526
- ___Block_byref_object_copy_.8082
- ___Block_byref_object_copy_.968
- ___Block_byref_object_copy_.9766
- ___Block_byref_object_dispose_.10904
- ___Block_byref_object_dispose_.11440
- ___Block_byref_object_dispose_.12246
- ___Block_byref_object_dispose_.12819
- ___Block_byref_object_dispose_.2104
- ___Block_byref_object_dispose_.2718
- ___Block_byref_object_dispose_.3306
- ___Block_byref_object_dispose_.3607
- ___Block_byref_object_dispose_.4316
- ___Block_byref_object_dispose_.5838
- ___Block_byref_object_dispose_.6189
- ___Block_byref_object_dispose_.7243
- ___Block_byref_object_dispose_.7365
- ___Block_byref_object_dispose_.7527
- ___Block_byref_object_dispose_.8083
- ___Block_byref_object_dispose_.969
- ___Block_byref_object_dispose_.9767
- ____containermanagerd_perform_launch_tasks_block_invoke.207
- ____containermanagerd_perform_launch_tasks_block_invoke.213
- ____containermanagerd_start_xpc_block_invoke.157
- ___block_descriptor_64_e8_32s40s48s56bs_e42_v24?0"NSString"8"MCMCodeSigningEntry"16ls32l8s40l8s48l8s56l8
- ___block_literal_global.10067
- ___block_literal_global.10912
- ___block_literal_global.11253
- ___block_literal_global.11683
- ___block_literal_global.11897
- ___block_literal_global.1203
- ___block_literal_global.12564
- ___block_literal_global.1261
- ___block_literal_global.12650
- ___block_literal_global.12671
- ___block_literal_global.1358
- ___block_literal_global.1681
- ___block_literal_global.203
- ___block_literal_global.209
- ___block_literal_global.215
- ___block_literal_global.2213
- ___block_literal_global.236
- ___block_literal_global.238
- ___block_literal_global.2548
- ___block_literal_global.4350
- ___block_literal_global.5371
- ___block_literal_global.6092
- ___block_literal_global.6669
- ___block_literal_global.6935
- ___block_literal_global.7726
- ___block_literal_global.7833
- ___block_literal_global.885
- ___block_literal_global.8896
- ___block_literal_global.976
- ___block_literal_global.9811
- __unnamed_array_storage.1399
- __unnamed_array_storage.1654
- __unnamed_array_storage.2116
- __unnamed_array_storage.3659
- __unnamed_array_storage.8792
- _defaultManager.onceToken.7715
- _objc_msgSend$_deletedComponent
- _objc_msgSend$_onQueue_iterateGroupIdsWithKey:fallBackKey:forAllIdentifiersUsingBlock:
- _sharedInstance.instance.10410
- _sharedInstance.onceToken.10409
- _sharedInstance.onceToken.8480
CStrings:
+ "-[MCMCodeSigningMapping _onQueue_iterateGroupIdsWithKey:fallBackKey:noReferenceKey:forAllIdentifiersUsingBlock:]"
+ "21:03:46"
+ "Feb 16 2024"
+ "MobileContainerManager-582.100.15~640"
+ "Set directory [%s] with mode: 0%o, w/intermediates: %d, DP class: %d, owner: %@"
+ "T@\"MCMManagedPath\",R,N,V_containermanagerUserCaches"
+ "T@\"MCMManagedPath\",R,N,V_containermanagerUserDeathrow"
+ "T@\"MCMManagedPath\",R,N,V_userCaches"
+ "T@\"NSString\",?,R,C"
+ "Unable to determine precedence of data protection; desired = %d, original = %d"
+ "Unrecognized value for data protection entitlement: [%@]"
+ "_arrayOfStringsFromArray:"
+ "_containermanagerUserCaches"
+ "_containermanagerUserDeathrow"
+ "_dataProtectionClassFromString:"
+ "_onQueue_iterateGroupIdsWithKey:fallBackKey:noReferenceKey:forAllIdentifiersUsingBlock:"
+ "_userCaches"
+ "com.apple.developer.default-data-protection-if-available"
+ "com.apple.private.MobileContainerManager.appGroup.noReference"
+ "containermanagerUserCaches"
+ "containermanagerUserDeathrow"
+ "dataProtectionClassIfAvailable"
+ "userCaches"
+ "v48@0:8@16@24@32@?40"
- "\a"
- "%{public}s(%d) Unknown value for DataProtectionClass entitlement: %@; defaulting to class %d"
- "+[MCMContainerClassDeletedPath deletedURLWithUserIdentity:]"
- "-[MCMCodeSigningMapping _onQueue_iterateGroupIdsWithKey:fallBackKey:forAllIdentifiersUsingBlock:]"
- "-[MCMEntitlements intendedDataProtectionClass]"
- "18:12:58"
- "Dec 20 2023"
- "Library/Caches/com.apple.containermanagerd/Dead"
- "MobileContainerManager-582.80.2~58"
- "Unknown value for DataProtectionClass entitlement: %@; defaulting to class %d"
- "_deletedComponent"
- "_onQueue_iterateGroupIdsWithKey:fallBackKey:forAllIdentifiersUsingBlock:"
- "v40@0:8@16@24@?32"

```
