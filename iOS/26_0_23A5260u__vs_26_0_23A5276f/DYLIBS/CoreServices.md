## CoreServices

> `/System/Library/Frameworks/CoreServices.framework/CoreServices`

```diff

-1420.0.0.0.0
-  __TEXT.__text: 0x1a5b0c
+1429.0.0.0.0
+  __TEXT.__text: 0x1a6744
   __TEXT.__auth_stubs: 0x2fe0
   __TEXT.__delay_stubs: 0x2c
   __TEXT.__delay_helper: 0xa4
-  __TEXT.__objc_methlist: 0xcafc
+  __TEXT.__objc_methlist: 0xcb24
   __TEXT.__const: 0x910
-  __TEXT.__cstring: 0x23f19
-  __TEXT.__oslogstring: 0x130be
-  __TEXT.__gcc_except_tab: 0x266d4
+  __TEXT.__cstring: 0x24088
+  __TEXT.__oslogstring: 0x13177
+  __TEXT.__gcc_except_tab: 0x26860
   __TEXT.__ustring: 0x23c
-  __TEXT.__unwind_info: 0xac18
+  __TEXT.__unwind_info: 0xac38
   __TEXT.__eh_frame: 0x60
-  __TEXT.__objc_classname: 0x1e62
-  __TEXT.__objc_methname: 0x1cac8
-  __TEXT.__objc_methtype: 0x9ec2
-  __TEXT.__objc_stubs: 0x100e0
+  __TEXT.__objc_classname: 0x1e6e
+  __TEXT.__objc_methname: 0x1cb1d
+  __TEXT.__objc_methtype: 0x9f7a
+  __TEXT.__objc_stubs: 0x10120
   __DATA_CONST.__got: 0xa78
   __DATA_CONST.__const: 0x6b80
   __DATA_CONST.__objc_classlist: 0x6a0
   __DATA_CONST.__objc_catlist: 0x50
   __DATA_CONST.__objc_protolist: 0x140
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x5dc8
+  __DATA_CONST.__objc_selrefs: 0x5dd8
   __DATA_CONST.__objc_protorefs: 0x98
   __DATA_CONST.__objc_superrefs: 0x548
   __DATA_CONST.__objc_arraydata: 0x1c0
   __AUTH_CONST.__auth_got: 0x1810
   __AUTH_CONST.__const: 0x3680
-  __AUTH_CONST.__cfstring: 0x16720
-  __AUTH_CONST.__objc_const: 0x12ce8
+  __AUTH_CONST.__cfstring: 0x167c0
+  __AUTH_CONST.__objc_const: 0x12d38
   __AUTH_CONST.__objc_intobj: 0x810
   __AUTH_CONST.__objc_dictobj: 0xf0
   __AUTH_CONST.__objc_arrayobj: 0x120
   __AUTH.__objc_data: 0x2b20
   __AUTH.__data: 0x330
-  __DATA.__objc_ivar: 0xa58
+  __DATA.__objc_ivar: 0xa60
   __DATA.__data: 0x12b4
   __DATA.__bss: 0xeb0
   __DATA.__common: 0x40

   - /usr/lib/libicucore.A.dylib
   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libsqlite3.dylib
-  UUID: FAFAFEEC-83C1-37F0-9AAA-C2CEC61E25A3
-  Functions: 8562
-  Symbols:   27805
-  CStrings:  13481
+  UUID: 7A88E160-DFD7-367D-B0B5-BBBB2A78C5E5
+  Functions: 8573
+  Symbols:   27833
+  CStrings:  13504
 
Symbols:
+ -[LSApplicationRecord(Gaming) supportsGameMode]
+ -[LSApplicationRestrictionsManager willRestrictedStateOfBundleWithRatingRank:changeOnUpdateToRatingRank:]
+ -[NSArray(LSAdditions) ls_caseInsensitiveContainsString:]
+ GCC_except_table302
+ GCC_except_table305
+ GCC_except_table309
+ GCC_except_table311
+ GCC_except_table321
+ GCC_except_table327
+ GCC_except_table340
+ GCC_except_table343
+ GCC_except_table349
+ GCC_except_table370
+ GCC_except_table373
+ GCC_except_table379
+ GCC_except_table383
+ GCC_except_table386
+ GCC_except_table399
+ GCC_except_table402
+ GCC_except_table406
+ GCC_except_table444
+ GCC_except_table450
+ GCC_except_table454
+ GCC_except_table458
+ GCC_except_table460
+ GCC_except_table465
+ GCC_except_table478
+ GCC_except_table498
+ GCC_except_table501
+ GCC_except_table504
+ GCC_except_table507
+ _OBJC_IVAR_$_LSBundleRecordUpdater._newRatingRank
+ _OBJC_IVAR_$_LSBundleRecordUpdater._oldRatingRank
+ __LSBundleIdentifierIsPlatformWebBrowser
+ __LSCopyApplicationCategoriesForApplicationNode
+ __LSServer_SendStateChangedNotificationsForBundlesWithIdentifiers
+ __OBJC_$_INSTANCE_METHODS_NSArray(LSObserverAdditions|LSAdditions)
+ ___68-[LSApplicationWorkspaceRemoteObserver applicationInstallsDidStart:]_block_invoke.762
+ ___95-[LSApplicationWorkspace sendApplicationStateChangedNotificationsFor:stateProvider:completion:]_block_invoke_2.cold.1
+ ___Block_byref_object_copy_.1017
+ ___Block_byref_object_dispose_.1018
+ ____LSServer_LSEnumerateAndRegisterAllBundles_block_invoke.945
+ ____LSServer_LSEnumerateAndRegisterAllBundles_block_invoke.945.cold.1
+ ____LSServer_LSEnumerateAndRegisterAllBundles_block_invoke.949
+ ____LSServer_LSEnumerateAndRegisterAllBundles_block_invoke.949.cold.1
+ ____LSServer_LSEnumerateAndRegisterAllBundles_block_invoke.951
+ ____LSServer_LSEnumerateAndRegisterAllBundles_block_invoke.952
+ ____LSServer_LSEnumerateAndRegisterAllBundles_block_invoke_2.947
+ ____LSServer_LSEnumerateAndRegisterAllBundles_block_invoke_2.950
+ ____LSServer_LSEnumerateAndRegisterAllBundles_block_invoke_2.954
+ ____LSServer_LSEnumerateAndRegisterAllBundles_block_invoke_2.954.cold.1
+ ____LSServer_PerformOpenOperation_block_invoke.81.cold.2
+ ____LSServer_PerformOpenOperation_block_invoke.81.cold.3
+ ____LSServer_PerformOpenOperation_block_invoke.81.cold.4
+ ____LSServer_PerformOpenOperation_block_invoke.81.cold.5
+ ____LSServer_SyncWithMobileInstallation_block_invoke.1019
+ ____LSServer_SyncWithMobileInstallation_block_invoke_2.1020
+ ___block_descriptor_32_e378_B28?0^{LSContext=}8I16r^{LSBundleData={LSBundleBaseData=IIIIIIi{LSVersionNumber=[32C]}{LSVersionNumber=[32C]}IIIIIIIIIIIIIICCISI{LSBundleBaseFlags=b1b1b1b1b1b1b1}}IQIIC{LSBundleMoreFlags=b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1}IiI{LSVersionNumber=[32C]}{LSVersionNumber=[32C]}IQQQIIIIIIIIIIQIIQQQQIQQIIIQIQIIIIIIIIIIIIIIIIIICCCI[1I]II{LSAppClipFields=I}iIIIIII}20l
+ ___block_descriptor_40_ea8_32s_e378_B28?0"_LSDatabase"8I16r^{LSBundleData={LSBundleBaseData=IIIIIIi{LSVersionNumber=[32C]}{LSVersionNumber=[32C]}IIIIIIIIIIIIIICCISI{LSBundleBaseFlags=b1b1b1b1b1b1b1}}IQIIC{LSBundleMoreFlags=b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1}IiI{LSVersionNumber=[32C]}{LSVersionNumber=[32C]}IQQQIIIIIIIIIIQIIQQQQIQQIIIQIQIIIIIIIIIIIIIIIIIICCCI[1I]II{LSAppClipFields=I}iIIIIII}20ls32l8
+ ___block_descriptor_40_ea8_32s_e378_B28?0^{LSContext=}8I16r^{LSBundleData={LSBundleBaseData=IIIIIIi{LSVersionNumber=[32C]}{LSVersionNumber=[32C]}IIIIIIIIIIIIIICCISI{LSBundleBaseFlags=b1b1b1b1b1b1b1}}IQIIC{LSBundleMoreFlags=b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1}IiI{LSVersionNumber=[32C]}{LSVersionNumber=[32C]}IQQQIIIIIIIIIIQIIQQQQIQQIIIQIQIIIIIIIIIIIIIIIIIICCCI[1I]II{LSAppClipFields=I}iIIIIII}20ls32l8
+ ___block_descriptor_44_e378_B28?0"_LSDatabase"8I16r^{LSBundleData={LSBundleBaseData=IIIIIIi{LSVersionNumber=[32C]}{LSVersionNumber=[32C]}IIIIIIIIIIIIIICCISI{LSBundleBaseFlags=b1b1b1b1b1b1b1}}IQIIC{LSBundleMoreFlags=b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1}IiI{LSVersionNumber=[32C]}{LSVersionNumber=[32C]}IQQQIIIIIIIIIIQIIQQQQIQQIIIQIQIIIIIIIIIIIIIIIIIICCCI[1I]II{LSAppClipFields=I}iIIIIII}20l
+ ___block_descriptor_48_ea8_32bs_e375_v28?0"NSString"8I16r^{LSBundleData={LSBundleBaseData=IIIIIIi{LSVersionNumber=[32C]}{LSVersionNumber=[32C]}IIIIIIIIIIIIIICCISI{LSBundleBaseFlags=b1b1b1b1b1b1b1}}IQIIC{LSBundleMoreFlags=b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1}IiI{LSVersionNumber=[32C]}{LSVersionNumber=[32C]}IQQQIIIIIIIIIIQIIQQQQIQQIIIQIQIIIIIIIIIIIIIIIIIICCCI[1I]II{LSAppClipFields=I}iIIIIII}20ls32l8
+ ___block_descriptor_52_ea8_32s_e365_v28?0I8r^{LSBundleData={LSBundleBaseData=IIIIIIi{LSVersionNumber=[32C]}{LSVersionNumber=[32C]}IIIIIIIIIIIIIICCISI{LSBundleBaseFlags=b1b1b1b1b1b1b1}}IQIIC{LSBundleMoreFlags=b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1}IiI{LSVersionNumber=[32C]}{LSVersionNumber=[32C]}IQQQIIIIIIIIIIQIIQQQQIQQIIIQIQIIIIIIIIIIIIIIIIIICCCI[1I]II{LSAppClipFields=I}iIIIIII}12*20ls32l8
+ ___block_descriptor_56_ea8_32bs40bs_e365_v28?0I8r^{LSBundleData={LSBundleBaseData=IIIIIIi{LSVersionNumber=[32C]}{LSVersionNumber=[32C]}IIIIIIIIIIIIIICCISI{LSBundleBaseFlags=b1b1b1b1b1b1b1}}IQIIC{LSBundleMoreFlags=b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1}IiI{LSVersionNumber=[32C]}{LSVersionNumber=[32C]}IQQQIIIIIIIIIIQIIQQQQIQQIIIQIQIIIIIIIIIIIIIIIIIICCCI[1I]II{LSAppClipFields=I}iIIIIII}12*20ls32l8s40l8
+ ___block_descriptor_56_ea8_32r40r_e365_v28?0I8r^{LSBundleData={LSBundleBaseData=IIIIIIi{LSVersionNumber=[32C]}{LSVersionNumber=[32C]}IIIIIIIIIIIIIICCISI{LSBundleBaseFlags=b1b1b1b1b1b1b1}}IQIIC{LSBundleMoreFlags=b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1}IiI{LSVersionNumber=[32C]}{LSVersionNumber=[32C]}IQQQIIIIIIIIIIQIIQQQQIQQIIIQIQIIIIIIIIIIIIIIIIIICCCI[1I]II{LSAppClipFields=I}iIIIIII}12*20lr32l8r40l8
+ ___block_descriptor_56_ea8_32s40bs_e365_v28?0I8r^{LSBundleData={LSBundleBaseData=IIIIIIi{LSVersionNumber=[32C]}{LSVersionNumber=[32C]}IIIIIIIIIIIIIICCISI{LSBundleBaseFlags=b1b1b1b1b1b1b1}}IQIIC{LSBundleMoreFlags=b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1}IiI{LSVersionNumber=[32C]}{LSVersionNumber=[32C]}IQQQIIIIIIIIIIQIIQQQQIQQIIIQIQIIIIIIIIIIIIIIIIIICCCI[1I]II{LSAppClipFields=I}iIIIIII}12*20ls32l8s40l8
+ ___block_descriptor_604_ea8_32s_e19_v32?0I8r^v12I20*24ls32l8
+ ___block_descriptor_604_ea8_32s_e37_v40?0q8"NSString"16"NSString"24*32ls32l8
+ ___block_descriptor_72_e8_32bs40r48r_e365_v28?0I8r^{LSBundleData={LSBundleBaseData=IIIIIIi{LSVersionNumber=[32C]}{LSVersionNumber=[32C]}IIIIIIIIIIIIIICCISI{LSBundleBaseFlags=b1b1b1b1b1b1b1}}IQIIC{LSBundleMoreFlags=b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1}IiI{LSVersionNumber=[32C]}{LSVersionNumber=[32C]}IQQQIIIIIIIIIIQIIQQQQIQQIIIQIQIIIIIIIIIIIIIIIIIICCCI[1I]II{LSAppClipFields=I}iIIIIII}12*20ls32l8r40l8r48l8
+ ___block_descriptor_72_ea8_32s40s48r_e365_v28?0I8r^{LSBundleData={LSBundleBaseData=IIIIIIi{LSVersionNumber=[32C]}{LSVersionNumber=[32C]}IIIIIIIIIIIIIICCISI{LSBundleBaseFlags=b1b1b1b1b1b1b1}}IQIIC{LSBundleMoreFlags=b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1}IiI{LSVersionNumber=[32C]}{LSVersionNumber=[32C]}IQQQIIIIIIIIIIQIIQQQQIQQIIIQIQIIIIIIIIIIIIIIIIIICCCI[1I]II{LSAppClipFields=I}iIIIIII}12*20ls32l8s40l8r48l8
+ ___block_literal_global.551
+ ___block_literal_global.650
+ ___block_literal_global.664
+ ___block_literal_global.681
+ ___block_literal_global.683
+ ___block_literal_global.924
+ ___block_literal_global.942
+ ___block_literal_global.981
+ _objc_msgSend$claimBindingsWithURL:error:
+ _objc_msgSend$ls_caseInsensitiveContainsString:
- GCC_except_table299
- GCC_except_table304
- GCC_except_table308
- GCC_except_table310
- GCC_except_table320
- GCC_except_table324
- GCC_except_table339
- GCC_except_table342
- GCC_except_table348
- GCC_except_table367
- GCC_except_table372
- GCC_except_table374
- GCC_except_table378
- GCC_except_table380
- GCC_except_table384
- GCC_except_table398
- GCC_except_table401
- GCC_except_table405
- GCC_except_table443
- GCC_except_table449
- GCC_except_table453
- GCC_except_table457
- GCC_except_table459
- GCC_except_table463
- GCC_except_table477
- GCC_except_table496
- GCC_except_table500
- GCC_except_table503
- GCC_except_table505
- __LSBundleIdentifierIsWebBrowser
- __LSCopyApplicationCategoriesForNodeWithDefaultIdentifierProvider
- ___68-[LSApplicationWorkspaceRemoteObserver applicationInstallsDidStart:]_block_invoke.774
- ___Block_byref_object_copy_.1029
- ___Block_byref_object_dispose_.1030
- ____LSServer_LSEnumerateAndRegisterAllBundles_block_invoke.957
- ____LSServer_LSEnumerateAndRegisterAllBundles_block_invoke.957.cold.1
- ____LSServer_LSEnumerateAndRegisterAllBundles_block_invoke.961
- ____LSServer_LSEnumerateAndRegisterAllBundles_block_invoke.961.cold.1
- ____LSServer_LSEnumerateAndRegisterAllBundles_block_invoke.963
- ____LSServer_LSEnumerateAndRegisterAllBundles_block_invoke.964
- ____LSServer_LSEnumerateAndRegisterAllBundles_block_invoke_2.959
- ____LSServer_LSEnumerateAndRegisterAllBundles_block_invoke_2.962
- ____LSServer_LSEnumerateAndRegisterAllBundles_block_invoke_2.966
- ____LSServer_LSEnumerateAndRegisterAllBundles_block_invoke_2.966.cold.1
- ____LSServer_SyncWithMobileInstallation_block_invoke.1031
- ____LSServer_SyncWithMobileInstallation_block_invoke_2.1032
- ___block_descriptor_32_e374_B28?0^{LSContext=}8I16r^{LSBundleData={LSBundleBaseData=IIIIIIi{LSVersionNumber=[32C]}{LSVersionNumber=[32C]}IIIIIIIIIIIIIICCISI{LSBundleBaseFlags=b1b1b1b1b1b1b1}}IQIIC{LSBundleMoreFlags=b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1}IiI{LSVersionNumber=[32C]}{LSVersionNumber=[32C]}IQQQIIIIIIIIIIQIIQQQQIQQIIIQIQIIIIIIIIIIIIIIIIIICCCI[1I]II{LSAppClipFields=I}iIIIIII}20l
- ___block_descriptor_40_ea8_32s_e374_B28?0"_LSDatabase"8I16r^{LSBundleData={LSBundleBaseData=IIIIIIi{LSVersionNumber=[32C]}{LSVersionNumber=[32C]}IIIIIIIIIIIIIICCISI{LSBundleBaseFlags=b1b1b1b1b1b1b1}}IQIIC{LSBundleMoreFlags=b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1}IiI{LSVersionNumber=[32C]}{LSVersionNumber=[32C]}IQQQIIIIIIIIIIQIIQQQQIQQIIIQIQIIIIIIIIIIIIIIIIIICCCI[1I]II{LSAppClipFields=I}iIIIIII}20ls32l8
- ___block_descriptor_40_ea8_32s_e374_B28?0^{LSContext=}8I16r^{LSBundleData={LSBundleBaseData=IIIIIIi{LSVersionNumber=[32C]}{LSVersionNumber=[32C]}IIIIIIIIIIIIIICCISI{LSBundleBaseFlags=b1b1b1b1b1b1b1}}IQIIC{LSBundleMoreFlags=b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1}IiI{LSVersionNumber=[32C]}{LSVersionNumber=[32C]}IQQQIIIIIIIIIIQIIQQQQIQQIIIQIQIIIIIIIIIIIIIIIIIICCCI[1I]II{LSAppClipFields=I}iIIIIII}20ls32l8
- ___block_descriptor_44_e374_B28?0"_LSDatabase"8I16r^{LSBundleData={LSBundleBaseData=IIIIIIi{LSVersionNumber=[32C]}{LSVersionNumber=[32C]}IIIIIIIIIIIIIICCISI{LSBundleBaseFlags=b1b1b1b1b1b1b1}}IQIIC{LSBundleMoreFlags=b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1}IiI{LSVersionNumber=[32C]}{LSVersionNumber=[32C]}IQQQIIIIIIIIIIQIIQQQQIQQIIIQIQIIIIIIIIIIIIIIIIIICCCI[1I]II{LSAppClipFields=I}iIIIIII}20l
- ___block_descriptor_48_ea8_32bs_e371_v28?0"NSString"8I16r^{LSBundleData={LSBundleBaseData=IIIIIIi{LSVersionNumber=[32C]}{LSVersionNumber=[32C]}IIIIIIIIIIIIIICCISI{LSBundleBaseFlags=b1b1b1b1b1b1b1}}IQIIC{LSBundleMoreFlags=b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1}IiI{LSVersionNumber=[32C]}{LSVersionNumber=[32C]}IQQQIIIIIIIIIIQIIQQQQIQQIIIQIQIIIIIIIIIIIIIIIIIICCCI[1I]II{LSAppClipFields=I}iIIIIII}20ls32l8
- ___block_descriptor_52_ea8_32s_e361_v28?0I8r^{LSBundleData={LSBundleBaseData=IIIIIIi{LSVersionNumber=[32C]}{LSVersionNumber=[32C]}IIIIIIIIIIIIIICCISI{LSBundleBaseFlags=b1b1b1b1b1b1b1}}IQIIC{LSBundleMoreFlags=b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1}IiI{LSVersionNumber=[32C]}{LSVersionNumber=[32C]}IQQQIIIIIIIIIIQIIQQQQIQQIIIQIQIIIIIIIIIIIIIIIIIICCCI[1I]II{LSAppClipFields=I}iIIIIII}12*20ls32l8
- ___block_descriptor_56_ea8_32bs40bs_e361_v28?0I8r^{LSBundleData={LSBundleBaseData=IIIIIIi{LSVersionNumber=[32C]}{LSVersionNumber=[32C]}IIIIIIIIIIIIIICCISI{LSBundleBaseFlags=b1b1b1b1b1b1b1}}IQIIC{LSBundleMoreFlags=b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1}IiI{LSVersionNumber=[32C]}{LSVersionNumber=[32C]}IQQQIIIIIIIIIIQIIQQQQIQQIIIQIQIIIIIIIIIIIIIIIIIICCCI[1I]II{LSAppClipFields=I}iIIIIII}12*20ls32l8s40l8
- ___block_descriptor_56_ea8_32r40r_e361_v28?0I8r^{LSBundleData={LSBundleBaseData=IIIIIIi{LSVersionNumber=[32C]}{LSVersionNumber=[32C]}IIIIIIIIIIIIIICCISI{LSBundleBaseFlags=b1b1b1b1b1b1b1}}IQIIC{LSBundleMoreFlags=b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1}IiI{LSVersionNumber=[32C]}{LSVersionNumber=[32C]}IQQQIIIIIIIIIIQIIQQQQIQQIIIQIQIIIIIIIIIIIIIIIIIICCCI[1I]II{LSAppClipFields=I}iIIIIII}12*20lr32l8r40l8
- ___block_descriptor_56_ea8_32s40bs_e361_v28?0I8r^{LSBundleData={LSBundleBaseData=IIIIIIi{LSVersionNumber=[32C]}{LSVersionNumber=[32C]}IIIIIIIIIIIIIICCISI{LSBundleBaseFlags=b1b1b1b1b1b1b1}}IQIIC{LSBundleMoreFlags=b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1}IiI{LSVersionNumber=[32C]}{LSVersionNumber=[32C]}IQQQIIIIIIIIIIQIIQQQQIQQIIIQIQIIIIIIIIIIIIIIIIIICCCI[1I]II{LSAppClipFields=I}iIIIIII}12*20ls32l8s40l8
- ___block_descriptor_600_ea8_32s_e19_v32?0I8r^v12I20*24ls32l8
- ___block_descriptor_600_ea8_32s_e37_v40?0q8"NSString"16"NSString"24*32ls32l8
- ___block_descriptor_72_e8_32bs40r48r_e361_v28?0I8r^{LSBundleData={LSBundleBaseData=IIIIIIi{LSVersionNumber=[32C]}{LSVersionNumber=[32C]}IIIIIIIIIIIIIICCISI{LSBundleBaseFlags=b1b1b1b1b1b1b1}}IQIIC{LSBundleMoreFlags=b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1}IiI{LSVersionNumber=[32C]}{LSVersionNumber=[32C]}IQQQIIIIIIIIIIQIIQQQQIQQIIIQIQIIIIIIIIIIIIIIIIIICCCI[1I]II{LSAppClipFields=I}iIIIIII}12*20ls32l8r40l8r48l8
- ___block_descriptor_72_ea8_32s40s48r_e361_v28?0I8r^{LSBundleData={LSBundleBaseData=IIIIIIi{LSVersionNumber=[32C]}{LSVersionNumber=[32C]}IIIIIIIIIIIIIICCISI{LSBundleBaseFlags=b1b1b1b1b1b1b1}}IQIIC{LSBundleMoreFlags=b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1}IiI{LSVersionNumber=[32C]}{LSVersionNumber=[32C]}IQQQIIIIIIIIIIQIIQQQQIQQIIIQIQIIIIIIIIIIIIIIIIIICCCI[1I]II{LSAppClipFields=I}iIIIIII}12*20ls32l8s40l8r48l8
- ___block_literal_global.545
- ___block_literal_global.662
- ___block_literal_global.676
- ___block_literal_global.693
- ___block_literal_global.695
- ___block_literal_global.936
- ___block_literal_global.940
- ___block_literal_global.979
CStrings:
+ "@32@0:8^{LSContext=@}16r^{LSBundleData={LSBundleBaseData=IIIIIIi{LSVersionNumber=[32C]}{LSVersionNumber=[32C]}IIIIIIIIIIIIIICCISI{LSBundleBaseFlags=b1b1b1b1b1b1b1}}IQIIC{LSBundleMoreFlags=b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1}IiI{LSVersionNumber=[32C]}{LSVersionNumber=[32C]}IQQQIIIIIIIIIIQIIQQQQIQQIIIQIQIIIIIIIIIIIIIIIIIICCCI[1I]II{LSAppClipFields=I}iIIIIII}24"
+ "@36@0:8@16I24r^{LSBundleData={LSBundleBaseData=IIIIIIi{LSVersionNumber=[32C]}{LSVersionNumber=[32C]}IIIIIIIIIIIIIICCISI{LSBundleBaseFlags=b1b1b1b1b1b1b1}}IQIIC{LSBundleMoreFlags=b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1}IiI{LSVersionNumber=[32C]}{LSVersionNumber=[32C]}IQQQIIIIIIIIIIQIIQQQQIQQIIIQIQIIIIIIIIIIIIIIIIIICCCI[1I]II{LSAppClipFields=I}iIIIIII}28"
+ "@36@0:8^{LSContext=@}16I24r^{LSBundleData={LSBundleBaseData=IIIIIIi{LSVersionNumber=[32C]}{LSVersionNumber=[32C]}IIIIIIIIIIIIIICCISI{LSBundleBaseFlags=b1b1b1b1b1b1b1}}IQIIC{LSBundleMoreFlags=b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1}IiI{LSVersionNumber=[32C]}{LSVersionNumber=[32C]}IQQQIIIIIIIIIIQIIQQQQIQQIIIQIQIIIIIIIIIIIIIIIIIICCCI[1I]II{LSAppClipFields=I}iIIIIII}28"
+ "@40@0:8^{LSContext=@}16I24I28r^{LSBundleData={LSBundleBaseData=IIIIIIi{LSVersionNumber=[32C]}{LSVersionNumber=[32C]}IIIIIIIIIIIIIICCISI{LSBundleBaseFlags=b1b1b1b1b1b1b1}}IQIIC{LSBundleMoreFlags=b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1}IiI{LSVersionNumber=[32C]}{LSVersionNumber=[32C]}IQQQIIIIIIIIIIQIIQQQQIQQIIIQIQIIIIIIIIIIIIIIIIIICCCI[1I]II{LSAppClipFields=I}iIIIIII}32"
+ "@44@0:8B16^{LSContext=@}20I28I32r^{LSBundleData={LSBundleBaseData=IIIIIIi{LSVersionNumber=[32C]}{LSVersionNumber=[32C]}IIIIIIIIIIIIIICCISI{LSBundleBaseFlags=b1b1b1b1b1b1b1}}IQIIC{LSBundleMoreFlags=b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1}IiI{LSVersionNumber=[32C]}{LSVersionNumber=[32C]}IQQQIIIIIIIIIIQIIQQQQIQQIIIQIQIIIIIIIIIIIIIIIIIICCCI[1I]II{LSAppClipFields=I}iIIIIII}36"
+ "@44@0:8I16r^{LSBundleData={LSBundleBaseData=IIIIIIi{LSVersionNumber=[32C]}{LSVersionNumber=[32C]}IIIIIIIIIIIIIICCISI{LSBundleBaseFlags=b1b1b1b1b1b1b1}}IQIIC{LSBundleMoreFlags=b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1}IiI{LSVersionNumber=[32C]}{LSVersionNumber=[32C]}IQQQIIIIIIIIIIQIIQQQQIQQIIIQIQIIIIIIIIIIIIIIIIIICCCI[1I]II{LSAppClipFields=I}iIIIIII}20@28^@36"
+ "@44@0:8^{LSContext=@}16I24r^{LSBundleData={LSBundleBaseData=IIIIIIi{LSVersionNumber=[32C]}{LSVersionNumber=[32C]}IIIIIIIIIIIIIICCISI{LSBundleBaseFlags=b1b1b1b1b1b1b1}}IQIIC{LSBundleMoreFlags=b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1}IiI{LSVersionNumber=[32C]}{LSVersionNumber=[32C]}IQQQIIIIIIIIIIQIIQQQQIQQIIIQIQIIIIIIIIIIIIIIIIIICCCI[1I]II{LSAppClipFields=I}iIIIIII}28^@36"
+ "B28@?0@\"_LSDatabase\"8I16r^{LSBundleData={LSBundleBaseData=IIIIIIi{LSVersionNumber=[32C]}{LSVersionNumber=[32C]}IIIIIIIIIIIIIICCISI{LSBundleBaseFlags=b1b1b1b1b1b1b1}}IQIIC{LSBundleMoreFlags=b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1}IiI{LSVersionNumber=[32C]}{LSVersionNumber=[32C]}IQQQIIIIIIIIIIQIIQQQQIQQIIIQIQIIIIIIIIIIIIIIIIIICCCI[1I]II{LSAppClipFields=I}iIIIIII}20"
+ "B28@?0^{LSContext=@}8I16r^{LSBundleData={LSBundleBaseData=IIIIIIi{LSVersionNumber=[32C]}{LSVersionNumber=[32C]}IIIIIIIIIIIIIICCISI{LSBundleBaseFlags=b1b1b1b1b1b1b1}}IQIIC{LSBundleMoreFlags=b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1}IiI{LSVersionNumber=[32C]}{LSVersionNumber=[32C]}IQQQIIIIIIIIIIQIIQQQQIQQIIIQIQIIIIIIIIIIIIIIIIIICCCI[1I]II{LSAppClipFields=I}iIIIIII}20"
+ "B36@0:8I16r^{LSBundleData={LSBundleBaseData=IIIIIIi{LSVersionNumber=[32C]}{LSVersionNumber=[32C]}IIIIIIIIIIIIIICCISI{LSBundleBaseFlags=b1b1b1b1b1b1b1}}IQIIC{LSBundleMoreFlags=b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1}IiI{LSVersionNumber=[32C]}{LSVersionNumber=[32C]}IQQQIIIIIIIIIIQIIQQQQIQQIIIQIQIIIIIIIIIIIIIIIIIICCCI[1I]II{LSAppClipFields=I}iIIIIII}20^{LSContext=@}28"
+ "B40@0:8^{LSContext=@}16I24I28r^{LSBundleData={LSBundleBaseData=IIIIIIi{LSVersionNumber=[32C]}{LSVersionNumber=[32C]}IIIIIIIIIIIIIICCISI{LSBundleBaseFlags=b1b1b1b1b1b1b1}}IQIIC{LSBundleMoreFlags=b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1}IiI{LSVersionNumber=[32C]}{LSVersionNumber=[32C]}IQQQIIIIIIIIIIQIIQQQQIQQIIIQIQIIIIIIIIIIIIIIIIIICCCI[1I]II{LSAppClipFields=I}iIIIIII}32"
+ "B52@0:8I16r^{LSBundleData={LSBundleBaseData=IIIIIIi{LSVersionNumber=[32C]}{LSVersionNumber=[32C]}IIIIIIIIIIIIIICCISI{LSBundleBaseFlags=b1b1b1b1b1b1b1}}IQIIC{LSBundleMoreFlags=b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1}IiI{LSVersionNumber=[32C]}{LSVersionNumber=[32C]}IQQQIIIIIIIIIIQIIQQQQIQQIIIQIQIIIIIIIIIIIIIIIIIICCCI[1I]II{LSAppClipFields=I}iIIIIII}20^{LSContext=@}28@36^@44"
+ "B60@0:8^@16^@24I32r^{LSBundleData={LSBundleBaseData=IIIIIIi{LSVersionNumber=[32C]}{LSVersionNumber=[32C]}IIIIIIIIIIIIIICCISI{LSBundleBaseFlags=b1b1b1b1b1b1b1}}IQIIC{LSBundleMoreFlags=b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1}IiI{LSVersionNumber=[32C]}{LSVersionNumber=[32C]}IQQQIIIIIIIIIIQIIQQQQIQQIIIQIQIIIIIIIIIIIIIIIIIICCCI[1I]II{LSAppClipFields=I}iIIIIII}36@44^@52"
+ "C40@0:8^{LSContext=@}16I24I28r^{LSBundleData={LSBundleBaseData=IIIIIIi{LSVersionNumber=[32C]}{LSVersionNumber=[32C]}IIIIIIIIIIIIIICCISI{LSBundleBaseFlags=b1b1b1b1b1b1b1}}IQIIC{LSBundleMoreFlags=b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1}IiI{LSVersionNumber=[32C]}{LSVersionNumber=[32C]}IQQQIIIIIIIIIIQIIQQQQIQQIIIQIQIIIIIIIIIIIIIIIIIICCCI[1I]II{LSAppClipFields=I}iIIIIII}32"
+ "GCSupportsGameMode"
+ "I40@0:8^{LSContext=@}16I24I28r^{LSBundleData={LSBundleBaseData=IIIIIIi{LSVersionNumber=[32C]}{LSVersionNumber=[32C]}IIIIIIIIIIIIIICCISI{LSBundleBaseFlags=b1b1b1b1b1b1b1}}IQIIC{LSBundleMoreFlags=b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1}IiI{LSVersionNumber=[32C]}{LSVersionNumber=[32C]}IQQQIIIIIIIIIIQIIQQQQIQQIIIQIQIIIIIIIIIIIIIIIIIICCCI[1I]II{LSAppClipFields=I}iIIIIII}32"
+ "LSAdditions"
+ "LSSupportsGameMode"
+ "Q40@0:8^{LSContext=@}16I24I28r^{LSBundleData={LSBundleBaseData=IIIIIIi{LSVersionNumber=[32C]}{LSVersionNumber=[32C]}IIIIIIIIIIIIIICCISI{LSBundleBaseFlags=b1b1b1b1b1b1b1}}IQIIC{LSBundleMoreFlags=b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1}IiI{LSVersionNumber=[32C]}{LSVersionNumber=[32C]}IQQQIIIIIIIIIIQIIQQQQIQQIIIQIQIIIIIIIIIIIIIIIIIICCCI[1I]II{LSAppClipFields=I}iIIIIII}32"
+ "SELF !=[c] %@"
+ "T{LSBundleMoreFlags=b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1},R"
+ "_LSIsDocumentOpenRequestValid"
+ "_LSIsRequestAllowed"
+ "_LSServer_SendStateChangedNotificationsForBundlesWithIdentifiers"
+ "_newRatingRank"
+ "_oldRatingRank"
+ "c40@0:8^{LSContext=@}16I24I28r^{LSBundleData={LSBundleBaseData=IIIIIIi{LSVersionNumber=[32C]}{LSVersionNumber=[32C]}IIIIIIIIIIIIIICCISI{LSBundleBaseFlags=b1b1b1b1b1b1b1}}IQIIC{LSBundleMoreFlags=b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1}IiI{LSVersionNumber=[32C]}{LSVersionNumber=[32C]}IQQQIIIIIIIIIIQIIQQQQIQQIIIQIQIIIIIIIIIIIIIIIIIICCCI[1I]II{LSAppClipFields=I}iIIIIII}32"
+ "com.apple.keyboard-service"
+ "couldn't get context in %s! %@"
+ "has-supports-game-mode"
+ "i32@0:8@16^{LSBundleData={LSBundleBaseData=IIIIIIi{LSVersionNumber=[32C]}{LSVersionNumber=[32C]}IIIIIIIIIIIIIICCISI{LSBundleBaseFlags=b1b1b1b1b1b1b1}}IQIIC{LSBundleMoreFlags=b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1}IiI{LSVersionNumber=[32C]}{LSVersionNumber=[32C]}IQQQIIIIIIIIIIQIIQQQQIQQIIIQIQIIIIIIIIIIIIIIIIIICCCI[1I]II{LSAppClipFields=I}iIIIIII}24"
+ "i36@0:8@16I24r^{LSBundleData={LSBundleBaseData=IIIIIIi{LSVersionNumber=[32C]}{LSVersionNumber=[32C]}IIIIIIIIIIIIIICCISI{LSBundleBaseFlags=b1b1b1b1b1b1b1}}IQIIC{LSBundleMoreFlags=b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1}IiI{LSVersionNumber=[32C]}{LSVersionNumber=[32C]}IQQQIIIIIIIIIIQIIQQQQIQQIIIQIQIIIIIIIIIIIIIIIIIICCCI[1I]II{LSAppClipFields=I}iIIIIII}28"
+ "i40@0:8^{LSContext=@}16I24I28r^{LSBundleData={LSBundleBaseData=IIIIIIi{LSVersionNumber=[32C]}{LSVersionNumber=[32C]}IIIIIIIIIIIIIICCISI{LSBundleBaseFlags=b1b1b1b1b1b1b1}}IQIIC{LSBundleMoreFlags=b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1}IiI{LSVersionNumber=[32C]}{LSVersionNumber=[32C]}IQQQIIIIIIIIIIQIIQQQQIQQIIIQIQIIIIIIIIIIIIIIIIIICCCI[1I]II{LSAppClipFields=I}iIIIIII}32"
+ "ls_caseInsensitiveContainsString:"
+ "pid %d cannot open URL with scheme %@"
+ "pid %d cannot open URL with scheme %@ (no claimants)"
+ "pid %d cannot open file URLs."
+ "pid %d cannot specify an opener."
+ "supports-game-mode"
+ "supportsGameMode"
+ "v28@?0@\"NSString\"8I16r^{LSBundleData={LSBundleBaseData=IIIIIIi{LSVersionNumber=[32C]}{LSVersionNumber=[32C]}IIIIIIIIIIIIIICCISI{LSBundleBaseFlags=b1b1b1b1b1b1b1}}IQIIC{LSBundleMoreFlags=b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1}IiI{LSVersionNumber=[32C]}{LSVersionNumber=[32C]}IQQQIIIIIIIIIIQIIQQQQIQQIIIQIQIIIIIIIIIIIIIIIIIICCCI[1I]II{LSAppClipFields=I}iIIIIII}20"
+ "v28@?0I8r^{LSBundleData={LSBundleBaseData=IIIIIIi{LSVersionNumber=[32C]}{LSVersionNumber=[32C]}IIIIIIIIIIIIIICCISI{LSBundleBaseFlags=b1b1b1b1b1b1b1}}IQIIC{LSBundleMoreFlags=b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1}IiI{LSVersionNumber=[32C]}{LSVersionNumber=[32C]}IQQQIIIIIIIIIIQIIQQQQIQQIIIQIQIIIIIIIIIIIIIIIIIICCCI[1I]II{LSAppClipFields=I}iIIIIII}12*20"
+ "v36@0:8^{LSContext=@}16I24r^{LSBundleData={LSBundleBaseData=IIIIIIi{LSVersionNumber=[32C]}{LSVersionNumber=[32C]}IIIIIIIIIIIIIICCISI{LSBundleBaseFlags=b1b1b1b1b1b1b1}}IQIIC{LSBundleMoreFlags=b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1}IiI{LSVersionNumber=[32C]}{LSVersionNumber=[32C]}IQQQIIIIIIIIIIQIIQQQQIQQIIIQIQIIIIIIIIIIIIIIIIIICCCI[1I]II{LSAppClipFields=I}iIIIIII}28"
+ "void _LSServer_SendStateChangedNotificationsForBundlesWithIdentifiers(LSContext *, NSSet<NSString *> *__strong, __strong id<LSMCStateProvider>)"
+ "{LSBundleData=\"base\"{LSBundleBaseData=\"bookmark\"I\"container\"I\"execPath\"I\"exactIdentifier\"I\"teamID\"I\"platform\"I\"registrationTime\"i\"version\"{LSVersionNumber=\"_opaque\"[32C]}\"execSDKVersion\"{LSVersionNumber=\"_opaque\"[32C]}\"machOUUIDs\"I\"dataContainerAlias\"I\"bundleName\"I\"localizedShortDisplayName\"I\"displayName\"I\"localizedDisplayName\"I\"localizedMicrophoneUsageDescription\"I\"localizedIdentityUsageDescription\"I\"codeInfoIdentifier\"I\"signerOrganization\"I\"signerIdentity\"I\"infoDictionary\"I\"entitlements\"I\"groupContainers\"I\"containingDirectoryClass\"C\"profileValidationState\"C\"intentDefinitionURLs\"I\"_sliceMask\"S\"signatureVersion\"I\"flags\"{LSBundleBaseFlags=\"appleInternal\"b1\"requiresObjCGarbageCollection\"b1\"builtWithTSan\"b1\"isLinkEnabled\"b1\"isSecuredSystemContent\"b1\"redactible\"b1\"_reserved\"b1}}\"_clas\"I\"_bundleFlags\"Q\"_plistContentFlags\"I\"_itemFlags\"I\"_iconFlags\"C\"moreFlags\"{LSBundleMoreFlags=\"isWebBrowser\"b1\"isMailClient\"b1\"supportsControllerUserInteraction\"b1\"supportsSpotlightQueryContinuation\"b1\"supportsSpotlightActions\"b1\"isCodeSigningInfoNotAuthoritative\"b1\"applicationQueriesSchemesTooBig\"b1\"isUpdateAvailable\"b1\"isPlaygroundsApp\"b1\"supportsAlwaysOnDisplay\"b1\"defaultsToPrivateAlwaysOnDisplayTreatment\"b1\"supportsLiveActivities\"b1\"supportsLiveActivitiesFrequentUpdates\"b1\"requiresPostprocessing\"b1\"hasShellRole\"b1\"requiresSecureLaunch\"b1\"eligibleForWatchAppInstall\"b1\"isEligibilityCheckedBrowser\"b1\"isEligibilityCheckedBrowserEngineEmbedder\"b1\"isManagedAppDistributor\"b1\"isHiddenByAppProtection\"b1\"isLockedByAppProtection\"b1\"supportsDataExport\"b1\"hasSupportsGameModeKey\"b1\"supportsGameMode\"b1\"_reserved\"b1}\"_hfsType\"I\"_mtime\"i\"minSystemVersionPlatform\"I\"_minSystemVersion\"{LSVersionNumber=\"_opaque\"[32C]}\"_maxSystemVersion\"{LSVersionNumber=\"_opaque\"[32C]}\"appStoreToolsBuildVersion\"I\"sequenceNumber\"Q\"compatibilityState\"Q\"itemID\"Q\"deviceFamilies\"I\"identifier\"I\"counterpartIdentifiers\"I\"equivalentBundleIdentifiers\"I\"categoryType\"I\"secondaryCategoryType\"I\"filename\"I\"bundleVersion\"I\"shortVersionString\"I\"installType\"I\"installFailureReason\"Q\"vendorName\"I\"appType\"I\"staticDiskUsage\"Q\"purchaserDSID\"Q\"downloaderDSID\"Q\"familyID\"Q\"itemName\"I\"storefront\"Q\"versionIdentifier\"Q\"sourceAppBundleID\"I\"appVariant\"I\"managementDeclarationIdentifier\"I\"ratingRank\"Q\"ratingLabel\"I\"genreID\"Q\"genre\"I\"distributorInfo\"I\"primaryIconName\"I\"alternatePrimaryIconName\"I\"iconsDict\"I\"iconFileNames\"I\"libraryPath\"I\"libraryItems\"I\"claims\"I\"types\"I\"plugins\"I\"driverExtensions\"I\"extensionPoints\"I\"activityTypes\"I\"queriableSchemes\"I\"bgPermittedIDs\"I\"carPlayInstrumentClusterURLSchemes\"I\"appContainerAlias\"I\"revision\"C\"retries\"C\"_reserved4\"C\"sandboxEnvironmentVariables\"I\"localizedNameWithContext\"[1I]\"bundlePersonas\"I\"bundlePersonaTypes\"I\"appClipFields\"{LSAppClipFields=\"parentAppIDs\"I}\"recordModificationTime\"i\"supportedGameControllers\"I\"mobileInstallIDs\"I\"applicationManagementDomain\"I\"stashedAppDict\"I\"linkedParentBundleIdentifier\"I\"_reserved5\"I}"
+ "{LSBundleData={LSBundleBaseData=IIIIIIi{LSVersionNumber=[32C]}{LSVersionNumber=[32C]}IIIIIIIIIIIIIICCISI{LSBundleBaseFlags=b1b1b1b1b1b1b1}}IQIIC{LSBundleMoreFlags=b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1}IiI{LSVersionNumber=[32C]}{LSVersionNumber=[32C]}IQQQIIIIIIIIIIQIIQQQQIQQIIIQIQIIIIIIIIIIIIIIIIIICCCI[1I]II{LSAppClipFields=I}iIIIIII}32@0:8@16^@24"
+ "{LSBundleMoreFlags=\"isWebBrowser\"b1\"isMailClient\"b1\"supportsControllerUserInteraction\"b1\"supportsSpotlightQueryContinuation\"b1\"supportsSpotlightActions\"b1\"isCodeSigningInfoNotAuthoritative\"b1\"applicationQueriesSchemesTooBig\"b1\"isUpdateAvailable\"b1\"isPlaygroundsApp\"b1\"supportsAlwaysOnDisplay\"b1\"defaultsToPrivateAlwaysOnDisplayTreatment\"b1\"supportsLiveActivities\"b1\"supportsLiveActivitiesFrequentUpdates\"b1\"requiresPostprocessing\"b1\"hasShellRole\"b1\"requiresSecureLaunch\"b1\"eligibleForWatchAppInstall\"b1\"isEligibilityCheckedBrowser\"b1\"isEligibilityCheckedBrowserEngineEmbedder\"b1\"isManagedAppDistributor\"b1\"isHiddenByAppProtection\"b1\"isLockedByAppProtection\"b1\"supportsDataExport\"b1\"hasSupportsGameModeKey\"b1\"supportsGameMode\"b1\"_reserved\"b1}"
+ "{LSBundleMoreFlags=b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1}16@0:8"
+ "{LSBundleMoreFlags=b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1}40@0:8^{LSContext=@}16I24I28r^{LSBundleData={LSBundleBaseData=IIIIIIi{LSVersionNumber=[32C]}{LSVersionNumber=[32C]}IIIIIIIIIIIIIICCISI{LSBundleBaseFlags=b1b1b1b1b1b1b1}}IQIIC{LSBundleMoreFlags=b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1}IiI{LSVersionNumber=[32C]}{LSVersionNumber=[32C]}IQQQIIIIIIIIIIQIIQQQQIQQIIIQIQIIIIIIIIIIIIIIIIIICCCI[1I]II{LSAppClipFields=I}iIIIIII}32"
- "@32@0:8^{LSContext=@}16r^{LSBundleData={LSBundleBaseData=IIIIIIi{LSVersionNumber=[32C]}{LSVersionNumber=[32C]}IIIIIIIIIIIIIICCISI{LSBundleBaseFlags=b1b1b1b1b1b1b1}}IQIIC{LSBundleMoreFlags=b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1}IiI{LSVersionNumber=[32C]}{LSVersionNumber=[32C]}IQQQIIIIIIIIIIQIIQQQQIQQIIIQIQIIIIIIIIIIIIIIIIIICCCI[1I]II{LSAppClipFields=I}iIIIIII}24"
- "@36@0:8@16I24r^{LSBundleData={LSBundleBaseData=IIIIIIi{LSVersionNumber=[32C]}{LSVersionNumber=[32C]}IIIIIIIIIIIIIICCISI{LSBundleBaseFlags=b1b1b1b1b1b1b1}}IQIIC{LSBundleMoreFlags=b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1}IiI{LSVersionNumber=[32C]}{LSVersionNumber=[32C]}IQQQIIIIIIIIIIQIIQQQQIQQIIIQIQIIIIIIIIIIIIIIIIIICCCI[1I]II{LSAppClipFields=I}iIIIIII}28"
- "@36@0:8^{LSContext=@}16I24r^{LSBundleData={LSBundleBaseData=IIIIIIi{LSVersionNumber=[32C]}{LSVersionNumber=[32C]}IIIIIIIIIIIIIICCISI{LSBundleBaseFlags=b1b1b1b1b1b1b1}}IQIIC{LSBundleMoreFlags=b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1}IiI{LSVersionNumber=[32C]}{LSVersionNumber=[32C]}IQQQIIIIIIIIIIQIIQQQQIQQIIIQIQIIIIIIIIIIIIIIIIIICCCI[1I]II{LSAppClipFields=I}iIIIIII}28"
- "@40@0:8^{LSContext=@}16I24I28r^{LSBundleData={LSBundleBaseData=IIIIIIi{LSVersionNumber=[32C]}{LSVersionNumber=[32C]}IIIIIIIIIIIIIICCISI{LSBundleBaseFlags=b1b1b1b1b1b1b1}}IQIIC{LSBundleMoreFlags=b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1}IiI{LSVersionNumber=[32C]}{LSVersionNumber=[32C]}IQQQIIIIIIIIIIQIIQQQQIQQIIIQIQIIIIIIIIIIIIIIIIIICCCI[1I]II{LSAppClipFields=I}iIIIIII}32"
- "@44@0:8B16^{LSContext=@}20I28I32r^{LSBundleData={LSBundleBaseData=IIIIIIi{LSVersionNumber=[32C]}{LSVersionNumber=[32C]}IIIIIIIIIIIIIICCISI{LSBundleBaseFlags=b1b1b1b1b1b1b1}}IQIIC{LSBundleMoreFlags=b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1}IiI{LSVersionNumber=[32C]}{LSVersionNumber=[32C]}IQQQIIIIIIIIIIQIIQQQQIQQIIIQIQIIIIIIIIIIIIIIIIIICCCI[1I]II{LSAppClipFields=I}iIIIIII}36"
- "@44@0:8I16r^{LSBundleData={LSBundleBaseData=IIIIIIi{LSVersionNumber=[32C]}{LSVersionNumber=[32C]}IIIIIIIIIIIIIICCISI{LSBundleBaseFlags=b1b1b1b1b1b1b1}}IQIIC{LSBundleMoreFlags=b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1}IiI{LSVersionNumber=[32C]}{LSVersionNumber=[32C]}IQQQIIIIIIIIIIQIIQQQQIQQIIIQIQIIIIIIIIIIIIIIIIIICCCI[1I]II{LSAppClipFields=I}iIIIIII}20@28^@36"
- "@44@0:8^{LSContext=@}16I24r^{LSBundleData={LSBundleBaseData=IIIIIIi{LSVersionNumber=[32C]}{LSVersionNumber=[32C]}IIIIIIIIIIIIIICCISI{LSBundleBaseFlags=b1b1b1b1b1b1b1}}IQIIC{LSBundleMoreFlags=b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1}IiI{LSVersionNumber=[32C]}{LSVersionNumber=[32C]}IQQQIIIIIIIIIIQIIQQQQIQQIIIQIQIIIIIIIIIIIIIIIIIICCCI[1I]II{LSAppClipFields=I}iIIIIII}28^@36"
- "B28@?0@\"_LSDatabase\"8I16r^{LSBundleData={LSBundleBaseData=IIIIIIi{LSVersionNumber=[32C]}{LSVersionNumber=[32C]}IIIIIIIIIIIIIICCISI{LSBundleBaseFlags=b1b1b1b1b1b1b1}}IQIIC{LSBundleMoreFlags=b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1}IiI{LSVersionNumber=[32C]}{LSVersionNumber=[32C]}IQQQIIIIIIIIIIQIIQQQQIQQIIIQIQIIIIIIIIIIIIIIIIIICCCI[1I]II{LSAppClipFields=I}iIIIIII}20"
- "B28@?0^{LSContext=@}8I16r^{LSBundleData={LSBundleBaseData=IIIIIIi{LSVersionNumber=[32C]}{LSVersionNumber=[32C]}IIIIIIIIIIIIIICCISI{LSBundleBaseFlags=b1b1b1b1b1b1b1}}IQIIC{LSBundleMoreFlags=b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1}IiI{LSVersionNumber=[32C]}{LSVersionNumber=[32C]}IQQQIIIIIIIIIIQIIQQQQIQQIIIQIQIIIIIIIIIIIIIIIIIICCCI[1I]II{LSAppClipFields=I}iIIIIII}20"
- "B36@0:8I16r^{LSBundleData={LSBundleBaseData=IIIIIIi{LSVersionNumber=[32C]}{LSVersionNumber=[32C]}IIIIIIIIIIIIIICCISI{LSBundleBaseFlags=b1b1b1b1b1b1b1}}IQIIC{LSBundleMoreFlags=b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1}IiI{LSVersionNumber=[32C]}{LSVersionNumber=[32C]}IQQQIIIIIIIIIIQIIQQQQIQQIIIQIQIIIIIIIIIIIIIIIIIICCCI[1I]II{LSAppClipFields=I}iIIIIII}20^{LSContext=@}28"
- "B40@0:8^{LSContext=@}16I24I28r^{LSBundleData={LSBundleBaseData=IIIIIIi{LSVersionNumber=[32C]}{LSVersionNumber=[32C]}IIIIIIIIIIIIIICCISI{LSBundleBaseFlags=b1b1b1b1b1b1b1}}IQIIC{LSBundleMoreFlags=b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1}IiI{LSVersionNumber=[32C]}{LSVersionNumber=[32C]}IQQQIIIIIIIIIIQIIQQQQIQQIIIQIQIIIIIIIIIIIIIIIIIICCCI[1I]II{LSAppClipFields=I}iIIIIII}32"
- "B52@0:8I16r^{LSBundleData={LSBundleBaseData=IIIIIIi{LSVersionNumber=[32C]}{LSVersionNumber=[32C]}IIIIIIIIIIIIIICCISI{LSBundleBaseFlags=b1b1b1b1b1b1b1}}IQIIC{LSBundleMoreFlags=b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1}IiI{LSVersionNumber=[32C]}{LSVersionNumber=[32C]}IQQQIIIIIIIIIIQIIQQQQIQQIIIQIQIIIIIIIIIIIIIIIIIICCCI[1I]II{LSAppClipFields=I}iIIIIII}20^{LSContext=@}28@36^@44"
- "B60@0:8^@16^@24I32r^{LSBundleData={LSBundleBaseData=IIIIIIi{LSVersionNumber=[32C]}{LSVersionNumber=[32C]}IIIIIIIIIIIIIICCISI{LSBundleBaseFlags=b1b1b1b1b1b1b1}}IQIIC{LSBundleMoreFlags=b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1}IiI{LSVersionNumber=[32C]}{LSVersionNumber=[32C]}IQQQIIIIIIIIIIQIIQQQQIQQIIIQIQIIIIIIIIIIIIIIIIIICCCI[1I]II{LSAppClipFields=I}iIIIIII}36@44^@52"
- "C40@0:8^{LSContext=@}16I24I28r^{LSBundleData={LSBundleBaseData=IIIIIIi{LSVersionNumber=[32C]}{LSVersionNumber=[32C]}IIIIIIIIIIIIIICCISI{LSBundleBaseFlags=b1b1b1b1b1b1b1}}IQIIC{LSBundleMoreFlags=b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1}IiI{LSVersionNumber=[32C]}{LSVersionNumber=[32C]}IQQQIIIIIIIIIIQIIQQQQIQQIIIQIQIIIIIIIIIIIIIIIIIICCCI[1I]II{LSAppClipFields=I}iIIIIII}32"
- "I40@0:8^{LSContext=@}16I24I28r^{LSBundleData={LSBundleBaseData=IIIIIIi{LSVersionNumber=[32C]}{LSVersionNumber=[32C]}IIIIIIIIIIIIIICCISI{LSBundleBaseFlags=b1b1b1b1b1b1b1}}IQIIC{LSBundleMoreFlags=b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1}IiI{LSVersionNumber=[32C]}{LSVersionNumber=[32C]}IQQQIIIIIIIIIIQIIQQQQIQQIIIQIQIIIIIIIIIIIIIIIIIICCCI[1I]II{LSAppClipFields=I}iIIIIII}32"
- "Q40@0:8^{LSContext=@}16I24I28r^{LSBundleData={LSBundleBaseData=IIIIIIi{LSVersionNumber=[32C]}{LSVersionNumber=[32C]}IIIIIIIIIIIIIICCISI{LSBundleBaseFlags=b1b1b1b1b1b1b1}}IQIIC{LSBundleMoreFlags=b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1}IiI{LSVersionNumber=[32C]}{LSVersionNumber=[32C]}IQQQIIIIIIIIIIQIIQQQQIQQIIIQIQIIIIIIIIIIIIIIIIIICCCI[1I]II{LSAppClipFields=I}iIIIIII}32"
- "SELF != %@"
- "T{LSBundleMoreFlags=b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1},R"
- "_LSIsRequestValid"
- "c40@0:8^{LSContext=@}16I24I28r^{LSBundleData={LSBundleBaseData=IIIIIIi{LSVersionNumber=[32C]}{LSVersionNumber=[32C]}IIIIIIIIIIIIIICCISI{LSBundleBaseFlags=b1b1b1b1b1b1b1}}IQIIC{LSBundleMoreFlags=b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1}IiI{LSVersionNumber=[32C]}{LSVersionNumber=[32C]}IQQQIIIIIIIIIIQIIQQQQIQQIIIQIQIIIIIIIIIIIIIIIIIICCCI[1I]II{LSAppClipFields=I}iIIIIII}32"
- "i32@0:8@16^{LSBundleData={LSBundleBaseData=IIIIIIi{LSVersionNumber=[32C]}{LSVersionNumber=[32C]}IIIIIIIIIIIIIICCISI{LSBundleBaseFlags=b1b1b1b1b1b1b1}}IQIIC{LSBundleMoreFlags=b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1}IiI{LSVersionNumber=[32C]}{LSVersionNumber=[32C]}IQQQIIIIIIIIIIQIIQQQQIQQIIIQIQIIIIIIIIIIIIIIIIIICCCI[1I]II{LSAppClipFields=I}iIIIIII}24"
- "i36@0:8@16I24r^{LSBundleData={LSBundleBaseData=IIIIIIi{LSVersionNumber=[32C]}{LSVersionNumber=[32C]}IIIIIIIIIIIIIICCISI{LSBundleBaseFlags=b1b1b1b1b1b1b1}}IQIIC{LSBundleMoreFlags=b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1}IiI{LSVersionNumber=[32C]}{LSVersionNumber=[32C]}IQQQIIIIIIIIIIQIIQQQQIQQIIIQIQIIIIIIIIIIIIIIIIIICCCI[1I]II{LSAppClipFields=I}iIIIIII}28"
- "i40@0:8^{LSContext=@}16I24I28r^{LSBundleData={LSBundleBaseData=IIIIIIi{LSVersionNumber=[32C]}{LSVersionNumber=[32C]}IIIIIIIIIIIIIICCISI{LSBundleBaseFlags=b1b1b1b1b1b1b1}}IQIIC{LSBundleMoreFlags=b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1}IiI{LSVersionNumber=[32C]}{LSVersionNumber=[32C]}IQQQIIIIIIIIIIQIIQQQQIQQIIIQIQIIIIIIIIIIIIIIIIIICCCI[1I]II{LSAppClipFields=I}iIIIIII}32"
- "v28@?0@\"NSString\"8I16r^{LSBundleData={LSBundleBaseData=IIIIIIi{LSVersionNumber=[32C]}{LSVersionNumber=[32C]}IIIIIIIIIIIIIICCISI{LSBundleBaseFlags=b1b1b1b1b1b1b1}}IQIIC{LSBundleMoreFlags=b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1}IiI{LSVersionNumber=[32C]}{LSVersionNumber=[32C]}IQQQIIIIIIIIIIQIIQQQQIQQIIIQIQIIIIIIIIIIIIIIIIIICCCI[1I]II{LSAppClipFields=I}iIIIIII}20"
- "v28@?0I8r^{LSBundleData={LSBundleBaseData=IIIIIIi{LSVersionNumber=[32C]}{LSVersionNumber=[32C]}IIIIIIIIIIIIIICCISI{LSBundleBaseFlags=b1b1b1b1b1b1b1}}IQIIC{LSBundleMoreFlags=b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1}IiI{LSVersionNumber=[32C]}{LSVersionNumber=[32C]}IQQQIIIIIIIIIIQIIQQQQIQQIIIQIQIIIIIIIIIIIIIIIIIICCCI[1I]II{LSAppClipFields=I}iIIIIII}12*20"
- "v36@0:8^{LSContext=@}16I24r^{LSBundleData={LSBundleBaseData=IIIIIIi{LSVersionNumber=[32C]}{LSVersionNumber=[32C]}IIIIIIIIIIIIIICCISI{LSBundleBaseFlags=b1b1b1b1b1b1b1}}IQIIC{LSBundleMoreFlags=b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1}IiI{LSVersionNumber=[32C]}{LSVersionNumber=[32C]}IQQQIIIIIIIIIIQIIQQQQIQQIIIQIQIIIIIIIIIIIIIIIIIICCCI[1I]II{LSAppClipFields=I}iIIIIII}28"
- "{LSBundleData=\"base\"{LSBundleBaseData=\"bookmark\"I\"container\"I\"execPath\"I\"exactIdentifier\"I\"teamID\"I\"platform\"I\"registrationTime\"i\"version\"{LSVersionNumber=\"_opaque\"[32C]}\"execSDKVersion\"{LSVersionNumber=\"_opaque\"[32C]}\"machOUUIDs\"I\"dataContainerAlias\"I\"bundleName\"I\"localizedShortDisplayName\"I\"displayName\"I\"localizedDisplayName\"I\"localizedMicrophoneUsageDescription\"I\"localizedIdentityUsageDescription\"I\"codeInfoIdentifier\"I\"signerOrganization\"I\"signerIdentity\"I\"infoDictionary\"I\"entitlements\"I\"groupContainers\"I\"containingDirectoryClass\"C\"profileValidationState\"C\"intentDefinitionURLs\"I\"_sliceMask\"S\"signatureVersion\"I\"flags\"{LSBundleBaseFlags=\"appleInternal\"b1\"requiresObjCGarbageCollection\"b1\"builtWithTSan\"b1\"isLinkEnabled\"b1\"isSecuredSystemContent\"b1\"redactible\"b1\"_reserved\"b1}}\"_clas\"I\"_bundleFlags\"Q\"_plistContentFlags\"I\"_itemFlags\"I\"_iconFlags\"C\"moreFlags\"{LSBundleMoreFlags=\"isWebBrowser\"b1\"isMailClient\"b1\"supportsControllerUserInteraction\"b1\"supportsSpotlightQueryContinuation\"b1\"supportsSpotlightActions\"b1\"isCodeSigningInfoNotAuthoritative\"b1\"applicationQueriesSchemesTooBig\"b1\"isUpdateAvailable\"b1\"isPlaygroundsApp\"b1\"supportsAlwaysOnDisplay\"b1\"defaultsToPrivateAlwaysOnDisplayTreatment\"b1\"supportsLiveActivities\"b1\"supportsLiveActivitiesFrequentUpdates\"b1\"requiresPostprocessing\"b1\"hasShellRole\"b1\"requiresSecureLaunch\"b1\"eligibleForWatchAppInstall\"b1\"isEligibilityCheckedBrowser\"b1\"isEligibilityCheckedBrowserEngineEmbedder\"b1\"isManagedAppDistributor\"b1\"isHiddenByAppProtection\"b1\"isLockedByAppProtection\"b1\"supportsDataExport\"b1\"_reserved\"b1}\"_hfsType\"I\"_mtime\"i\"minSystemVersionPlatform\"I\"_minSystemVersion\"{LSVersionNumber=\"_opaque\"[32C]}\"_maxSystemVersion\"{LSVersionNumber=\"_opaque\"[32C]}\"appStoreToolsBuildVersion\"I\"sequenceNumber\"Q\"compatibilityState\"Q\"itemID\"Q\"deviceFamilies\"I\"identifier\"I\"counterpartIdentifiers\"I\"equivalentBundleIdentifiers\"I\"categoryType\"I\"secondaryCategoryType\"I\"filename\"I\"bundleVersion\"I\"shortVersionString\"I\"installType\"I\"installFailureReason\"Q\"vendorName\"I\"appType\"I\"staticDiskUsage\"Q\"purchaserDSID\"Q\"downloaderDSID\"Q\"familyID\"Q\"itemName\"I\"storefront\"Q\"versionIdentifier\"Q\"sourceAppBundleID\"I\"appVariant\"I\"managementDeclarationIdentifier\"I\"ratingRank\"Q\"ratingLabel\"I\"genreID\"Q\"genre\"I\"distributorInfo\"I\"primaryIconName\"I\"alternatePrimaryIconName\"I\"iconsDict\"I\"iconFileNames\"I\"libraryPath\"I\"libraryItems\"I\"claims\"I\"types\"I\"plugins\"I\"driverExtensions\"I\"extensionPoints\"I\"activityTypes\"I\"queriableSchemes\"I\"bgPermittedIDs\"I\"carPlayInstrumentClusterURLSchemes\"I\"appContainerAlias\"I\"revision\"C\"retries\"C\"_reserved4\"C\"sandboxEnvironmentVariables\"I\"localizedNameWithContext\"[1I]\"bundlePersonas\"I\"bundlePersonaTypes\"I\"appClipFields\"{LSAppClipFields=\"parentAppIDs\"I}\"recordModificationTime\"i\"supportedGameControllers\"I\"mobileInstallIDs\"I\"applicationManagementDomain\"I\"stashedAppDict\"I\"linkedParentBundleIdentifier\"I\"_reserved5\"I}"
- "{LSBundleData={LSBundleBaseData=IIIIIIi{LSVersionNumber=[32C]}{LSVersionNumber=[32C]}IIIIIIIIIIIIIICCISI{LSBundleBaseFlags=b1b1b1b1b1b1b1}}IQIIC{LSBundleMoreFlags=b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1}IiI{LSVersionNumber=[32C]}{LSVersionNumber=[32C]}IQQQIIIIIIIIIIQIIQQQQIQQIIIQIQIIIIIIIIIIIIIIIIIICCCI[1I]II{LSAppClipFields=I}iIIIIII}32@0:8@16^@24"
- "{LSBundleMoreFlags=\"isWebBrowser\"b1\"isMailClient\"b1\"supportsControllerUserInteraction\"b1\"supportsSpotlightQueryContinuation\"b1\"supportsSpotlightActions\"b1\"isCodeSigningInfoNotAuthoritative\"b1\"applicationQueriesSchemesTooBig\"b1\"isUpdateAvailable\"b1\"isPlaygroundsApp\"b1\"supportsAlwaysOnDisplay\"b1\"defaultsToPrivateAlwaysOnDisplayTreatment\"b1\"supportsLiveActivities\"b1\"supportsLiveActivitiesFrequentUpdates\"b1\"requiresPostprocessing\"b1\"hasShellRole\"b1\"requiresSecureLaunch\"b1\"eligibleForWatchAppInstall\"b1\"isEligibilityCheckedBrowser\"b1\"isEligibilityCheckedBrowserEngineEmbedder\"b1\"isManagedAppDistributor\"b1\"isHiddenByAppProtection\"b1\"isLockedByAppProtection\"b1\"supportsDataExport\"b1\"_reserved\"b1}"
- "{LSBundleMoreFlags=b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1}16@0:8"
- "{LSBundleMoreFlags=b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1}40@0:8^{LSContext=@}16I24I28r^{LSBundleData={LSBundleBaseData=IIIIIIi{LSVersionNumber=[32C]}{LSVersionNumber=[32C]}IIIIIIIIIIIIIICCISI{LSBundleBaseFlags=b1b1b1b1b1b1b1}}IQIIC{LSBundleMoreFlags=b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1}IiI{LSVersionNumber=[32C]}{LSVersionNumber=[32C]}IQQQIIIIIIIIIIQIIQQQQIQQIIIQIQIIIIIIIIIIIIIIIIIICCCI[1I]II{LSAppClipFields=I}iIIIIII}32"

```
