## ContainerManagerCommon

> `/System/Library/PrivateFrameworks/ContainerManagerCommon.framework/ContainerManagerCommon`

```diff

-725.60.3.0.0
-  __TEXT.__text: 0xec014
+725.60.3.502.1
+  __TEXT.__text: 0xeda4c
   __TEXT.__auth_stubs: 0x2290
-  __TEXT.__objc_methlist: 0xa4ac
+  __TEXT.__objc_methlist: 0xa4fc
   __TEXT.__const: 0x11a0
-  __TEXT.__cstring: 0x9b6b
+  __TEXT.__cstring: 0x9b97
   __TEXT.__swift5_typeref: 0x5b7
-  __TEXT.__oslogstring: 0xe8bd
+  __TEXT.__oslogstring: 0xefc1
   __TEXT.__constg_swiftt: 0x5a8
   __TEXT.__swift5_reflstr: 0x38a
   __TEXT.__swift5_fieldmd: 0x420

   __TEXT.__swift5_mpenum: 0x10
   __TEXT.__swift5_capture: 0x48
   __TEXT.__swift5_protos: 0x18
-  __TEXT.__gcc_except_tab: 0x2b14
+  __TEXT.__gcc_except_tab: 0x2b1c
   __TEXT.__ustring: 0x16c
   __TEXT.__unwind_info: 0x2268
   __TEXT.__eh_frame: 0x4a0
   __TEXT.__objc_classname: 0x1dec
-  __TEXT.__objc_methname: 0x1385e
+  __TEXT.__objc_methname: 0x1396e
   __TEXT.__objc_methtype: 0x41ae
-  __TEXT.__objc_stubs: 0xbb00
+  __TEXT.__objc_stubs: 0xbba0
   __DATA_CONST.__got: 0x398
   __DATA_CONST.__const: 0x19c8
   __DATA_CONST.__objc_classlist: 0x5d0
   __DATA_CONST.__objc_catlist: 0x28
   __DATA_CONST.__objc_protolist: 0x4a8
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x3560
+  __DATA_CONST.__objc_selrefs: 0x3588
   __DATA_CONST.__objc_protorefs: 0x78
   __DATA_CONST.__objc_superrefs: 0x4e8
   __DATA_CONST.__objc_arraydata: 0x2d0
   __AUTH_CONST.__auth_got: 0x1158
   __AUTH_CONST.__const: 0x1228
-  __AUTH_CONST.__cfstring: 0x46a0
-  __AUTH_CONST.__objc_const: 0x163f8
+  __AUTH_CONST.__cfstring: 0x46e0
+  __AUTH_CONST.__objc_const: 0x16440
   __AUTH_CONST.__objc_dictobj: 0x140
   __AUTH_CONST.__objc_intobj: 0x14d0
   __AUTH_CONST.__objc_arrayobj: 0xc0
   __AUTH.__objc_data: 0xb50
   __AUTH.__data: 0x168
-  __DATA.__objc_ivar: 0xbdc
+  __DATA.__objc_ivar: 0xbe0
   __DATA.__data: 0x3930
   __DATA.__crash_info: 0x148
   __DATA.__bss: 0xf78

   - /usr/lib/swift/libswiftXPC.dylib
   - /usr/lib/swift/libswift_Builtin_float.dylib
   - /usr/lib/swift/libswiftos.dylib
-  UUID: 4BE8CC05-06C8-33D1-A4AF-7DB2466AC475
-  Functions: 3448
-  Symbols:   11633
-  CStrings:  6199
+  UUID: A20CC5F7-BF3C-320B-AAB1-99788F0485EB
+  Functions: 3453
+  Symbols:   11649
+  CStrings:  6228
 
Symbols:
+ -[MCMCommandUserDataMigration _migrateContainerIdentities]
+ -[MCMCommandUserDataMigration _migrateContainersWithIdentifierMap:containerConfig:]
+ -[MCMCommandUserDataMigration _replaceContainer:withContainer:]
+ -[MCMStaticConfiguration _containerIdentityMigrationsFromPlistValue:error:]
+ -[MCMStaticConfiguration containerIdentityMigrations]
+ GCC_except_table1046
+ GCC_except_table1055
+ GCC_except_table1059
+ GCC_except_table1097
+ GCC_except_table1098
+ GCC_except_table1110
+ GCC_except_table1112
+ GCC_except_table1116
+ GCC_except_table1124
+ GCC_except_table1126
+ GCC_except_table1132
+ GCC_except_table1134
+ GCC_except_table1136
+ GCC_except_table1141
+ GCC_except_table1143
+ GCC_except_table1150
+ GCC_except_table1152
+ GCC_except_table1161
+ GCC_except_table1163
+ GCC_except_table1171
+ GCC_except_table1187
+ GCC_except_table1197
+ GCC_except_table1202
+ GCC_except_table1206
+ GCC_except_table1208
+ GCC_except_table1260
+ GCC_except_table1270
+ GCC_except_table1301
+ GCC_except_table1349
+ GCC_except_table1351
+ GCC_except_table1355
+ GCC_except_table1356
+ GCC_except_table1575
+ GCC_except_table1626
+ GCC_except_table1715
+ GCC_except_table1860
+ GCC_except_table1898
+ GCC_except_table1902
+ GCC_except_table1905
+ GCC_except_table1908
+ GCC_except_table1923
+ GCC_except_table1927
+ GCC_except_table1963
+ GCC_except_table1969
+ GCC_except_table2041
+ GCC_except_table2044
+ GCC_except_table2155
+ GCC_except_table2292
+ GCC_except_table2309
+ GCC_except_table2310
+ GCC_except_table2388
+ GCC_except_table2445
+ GCC_except_table2460
+ GCC_except_table2520
+ GCC_except_table2532
+ GCC_except_table2592
+ GCC_except_table2602
+ GCC_except_table2627
+ GCC_except_table2656
+ GCC_except_table2678
+ GCC_except_table2682
+ GCC_except_table2685
+ GCC_except_table2689
+ GCC_except_table2745
+ GCC_except_table2834
+ GCC_except_table2882
+ GCC_except_table2885
+ GCC_except_table2956
+ GCC_except_table839
+ GCC_except_table914
+ GCC_except_table959
+ GCC_except_table990
+ GCC_except_table992
+ _OBJC_IVAR_$_MCMStaticConfiguration._containerIdentityMigrations
+ ___Block_byref_object_copy_.10058
+ ___Block_byref_object_copy_.11856
+ ___Block_byref_object_copy_.12564
+ ___Block_byref_object_copy_.12914
+ ___Block_byref_object_copy_.13474
+ ___Block_byref_object_copy_.14331
+ ___Block_byref_object_copy_.14687
+ ___Block_byref_object_copy_.14948
+ ___Block_byref_object_copy_.2567
+ ___Block_byref_object_copy_.3309
+ ___Block_byref_object_copy_.3983
+ ___Block_byref_object_copy_.4381
+ ___Block_byref_object_copy_.5119
+ ___Block_byref_object_copy_.5389
+ ___Block_byref_object_copy_.7347
+ ___Block_byref_object_copy_.7879
+ ___Block_byref_object_copy_.9035
+ ___Block_byref_object_copy_.9227
+ ___Block_byref_object_copy_.9361
+ ___Block_byref_object_copy_.9829
+ ___Block_byref_object_dispose_.10059
+ ___Block_byref_object_dispose_.11857
+ ___Block_byref_object_dispose_.12565
+ ___Block_byref_object_dispose_.12915
+ ___Block_byref_object_dispose_.13475
+ ___Block_byref_object_dispose_.14332
+ ___Block_byref_object_dispose_.14688
+ ___Block_byref_object_dispose_.14949
+ ___Block_byref_object_dispose_.2568
+ ___Block_byref_object_dispose_.3310
+ ___Block_byref_object_dispose_.3984
+ ___Block_byref_object_dispose_.4382
+ ___Block_byref_object_dispose_.5120
+ ___Block_byref_object_dispose_.5390
+ ___Block_byref_object_dispose_.7348
+ ___Block_byref_object_dispose_.7880
+ ___Block_byref_object_dispose_.9036
+ ___Block_byref_object_dispose_.9228
+ ___Block_byref_object_dispose_.9362
+ ___Block_byref_object_dispose_.9830
+ ___block_literal_global.10958
+ ___block_literal_global.11898
+ ___block_literal_global.12.11896
+ ___block_literal_global.12115
+ ___block_literal_global.12923
+ ___block_literal_global.13273
+ ___block_literal_global.13456
+ ___block_literal_global.13736
+ ___block_literal_global.13939
+ ___block_literal_global.14679
+ ___block_literal_global.14768
+ ___block_literal_global.14788
+ ___block_literal_global.2672
+ ___block_literal_global.5096
+ ___block_literal_global.5435
+ ___block_literal_global.6610
+ ___block_literal_global.7238
+ ___block_literal_global.7783
+ ___block_literal_global.8392
+ ___block_literal_global.8663
+ ___block_literal_global.9486
+ ___block_literal_global.9583
+ _defaultManager.onceToken.9475
+ _objc_msgSend$_containerIdentityMigrationsFromPlistValue:error:
+ _objc_msgSend$_migrateContainerIdentities
+ _objc_msgSend$_migrateContainersWithIdentifierMap:containerConfig:
+ _objc_msgSend$_replaceContainer:withContainer:
+ _objc_msgSend$containerIdentityMigrations
+ _sharedInstance.instance.12428
+ _sharedInstance.onceToken.10361
+ _sharedInstance.onceToken.12427
- GCC_except_table1043
- GCC_except_table1052
- GCC_except_table1056
- GCC_except_table1094
- GCC_except_table1095
- GCC_except_table1107
- GCC_except_table1109
- GCC_except_table1113
- GCC_except_table1118
- GCC_except_table1123
- GCC_except_table1129
- GCC_except_table1131
- GCC_except_table1133
- GCC_except_table1135
- GCC_except_table1140
- GCC_except_table1144
- GCC_except_table1149
- GCC_except_table1155
- GCC_except_table1160
- GCC_except_table1168
- GCC_except_table1184
- GCC_except_table1194
- GCC_except_table1199
- GCC_except_table1203
- GCC_except_table1205
- GCC_except_table1257
- GCC_except_table1267
- GCC_except_table1298
- GCC_except_table1346
- GCC_except_table1348
- GCC_except_table1352
- GCC_except_table1353
- GCC_except_table1572
- GCC_except_table1621
- GCC_except_table1710
- GCC_except_table1855
- GCC_except_table1893
- GCC_except_table1897
- GCC_except_table1900
- GCC_except_table1903
- GCC_except_table1918
- GCC_except_table1922
- GCC_except_table1958
- GCC_except_table1964
- GCC_except_table2036
- GCC_except_table2039
- GCC_except_table2150
- GCC_except_table2287
- GCC_except_table2304
- GCC_except_table2305
- GCC_except_table2383
- GCC_except_table2440
- GCC_except_table2455
- GCC_except_table2515
- GCC_except_table2527
- GCC_except_table2587
- GCC_except_table2597
- GCC_except_table2622
- GCC_except_table2651
- GCC_except_table2673
- GCC_except_table2677
- GCC_except_table2680
- GCC_except_table2684
- GCC_except_table2740
- GCC_except_table2829
- GCC_except_table2877
- GCC_except_table2880
- GCC_except_table2951
- GCC_except_table836
- GCC_except_table911
- GCC_except_table956
- GCC_except_table987
- GCC_except_table989
- ___Block_byref_object_copy_.10026
- ___Block_byref_object_copy_.11821
- ___Block_byref_object_copy_.12529
- ___Block_byref_object_copy_.12874
- ___Block_byref_object_copy_.13434
- ___Block_byref_object_copy_.14291
- ___Block_byref_object_copy_.14647
- ___Block_byref_object_copy_.14908
- ___Block_byref_object_copy_.2545
- ___Block_byref_object_copy_.3288
- ___Block_byref_object_copy_.3962
- ___Block_byref_object_copy_.4357
- ___Block_byref_object_copy_.5095
- ___Block_byref_object_copy_.5365
- ___Block_byref_object_copy_.7315
- ___Block_byref_object_copy_.7847
- ___Block_byref_object_copy_.9003
- ___Block_byref_object_copy_.9195
- ___Block_byref_object_copy_.9329
- ___Block_byref_object_copy_.9797
- ___Block_byref_object_dispose_.10027
- ___Block_byref_object_dispose_.11822
- ___Block_byref_object_dispose_.12530
- ___Block_byref_object_dispose_.12875
- ___Block_byref_object_dispose_.13435
- ___Block_byref_object_dispose_.14292
- ___Block_byref_object_dispose_.14648
- ___Block_byref_object_dispose_.14909
- ___Block_byref_object_dispose_.2546
- ___Block_byref_object_dispose_.3289
- ___Block_byref_object_dispose_.3963
- ___Block_byref_object_dispose_.4358
- ___Block_byref_object_dispose_.5096
- ___Block_byref_object_dispose_.5366
- ___Block_byref_object_dispose_.7316
- ___Block_byref_object_dispose_.7848
- ___Block_byref_object_dispose_.9004
- ___Block_byref_object_dispose_.9196
- ___Block_byref_object_dispose_.9330
- ___Block_byref_object_dispose_.9798
- ___block_literal_global.10923
- ___block_literal_global.11863
- ___block_literal_global.12.11861
- ___block_literal_global.12080
- ___block_literal_global.12883
- ___block_literal_global.13233
- ___block_literal_global.13416
- ___block_literal_global.13696
- ___block_literal_global.13899
- ___block_literal_global.14639
- ___block_literal_global.14728
- ___block_literal_global.14748
- ___block_literal_global.2650
- ___block_literal_global.5072
- ___block_literal_global.5411
- ___block_literal_global.6582
- ___block_literal_global.7207
- ___block_literal_global.7751
- ___block_literal_global.8360
- ___block_literal_global.8631
- ___block_literal_global.9454
- ___block_literal_global.9551
- _defaultManager.onceToken.9443
- _sharedInstance.instance.12393
- _sharedInstance.onceToken.10329
- _sharedInstance.onceToken.12392
CStrings:
+ "21:02:37"
+ "Completed Container Identity Migration on %@"
+ "Container identity migration map identifier is not in a valid format; expected = NSString, got = %@, value = %@"
+ "Container identity migration map is not in a valid format; expected = NSDictionary, got = %@, value = %@"
+ "Container identity migration map value is not in a valid format; expected = NSDictionary, got = %@, value = %@"
+ "Encountered container identity migration entry with unknown container class: %@"
+ "Failed to readd container to cache for migration; metadata = %@, error = %@"
+ "MobileContainerManager-725.60.3.502.1~1"
+ "Nov  3 2025"
+ "Performing Container Identity Migration on %@"
+ "Preferences"
+ "T@\"NSDictionary\",R,N,V_containerIdentityMigrations"
+ "Unable to construct (from) container identity for migration; identifier = [%@], userIdentity = %@, error = (%llu) %s"
+ "Unable to construct (to) container identity for migration; identifier = [%@], userIdentity = %@, error = (%llu) %s"
+ "Unable to delete old container for migration; fromIdentifier = [%@], toIdentifier = [%@], userIdentity = %@, error = %@"
+ "Unable to fetch (from) container for migration; identifier = [%@], userIdentity = %@, error = %@"
+ "Unable to fetch (to) container for migration; identifier = [%@], userIdentity = %@, error = %@"
+ "Unable to fetch metadata for (from) container for migration; identifier = [%@], userIdentity = %@, error = %@"
+ "Unable to remove (from) container from cache for migration; identifier = [%@], userIdentity = %@, error = %@"
+ "Unable to remove (to) container from cache for migration; identifier = [%@], userIdentity = %@, error = %@"
+ "Unable to rename prefs for migration; fromPreferencesURL = [%@], toPreferencesURL = [%@], userIdentity = %@, error = %@"
+ "Unable to replace containers for migration; fromIdentifier = [%@], toIdentifier = [%@], userIdentity = %@, error = %@"
+ "Unable to write new metadata to (from) container for migration; identifier = [%@], userIdentity = %@, error = %@"
+ "_containerIdentityMigrations"
+ "_containerIdentityMigrationsFromPlistValue:error:"
+ "_migrateContainerIdentities"
+ "_migrateContainersWithIdentifierMap:containerConfig:"
+ "_replaceContainer:withContainer:"
+ "containerIdentityMigrations"
- "20:52:55"
- "MobileContainerManager-725.60.3~566"
- "Oct 28 2025"

```
