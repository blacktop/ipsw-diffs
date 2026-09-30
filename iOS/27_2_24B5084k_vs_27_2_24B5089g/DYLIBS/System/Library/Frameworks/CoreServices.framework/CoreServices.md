## CoreServices

> `/System/Library/Frameworks/CoreServices.framework/CoreServices`

```diff

-1517.1.8.0.0
-  __TEXT.__text: 0x1c61c8
+1517.1.9.0.0
+  __TEXT.__text: 0x1c7a88
   __TEXT.__delay_helper: 0x1b8
   __TEXT.__lazy_helpers: 0xa8
-  __TEXT.__objc_methlist: 0xe2e4
+  __TEXT.__objc_methlist: 0xe334
   __TEXT.__const: 0x9c0
-  __TEXT.__cstring: 0x29500
-  __TEXT.__oslogstring: 0x16b4b
-  __TEXT.__gcc_except_tab: 0x2a0f4
+  __TEXT.__cstring: 0x29633
+  __TEXT.__oslogstring: 0x16d55
+  __TEXT.__gcc_except_tab: 0x2a3dc
   __TEXT.__ustring: 0x23c
-  __TEXT.__unwind_info: 0xdc78
+  __TEXT.__unwind_info: 0xdce0
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0
   __TEXT.__objc_classname: 0x0
   __TEXT.__objc_methname: 0x0
   __TEXT.__objc_methtype: 0x0
-  __DATA_CONST.__const: 0x75b0
+  __DATA_CONST.__const: 0x75d8
   __DATA_CONST.__objc_classlist: 0x7b0
   __DATA_CONST.__objc_catlist: 0x78
   __DATA_CONST.__objc_protolist: 0x180
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x65e0
+  __DATA_CONST.__objc_selrefs: 0x6608
   __DATA_CONST.__objc_protorefs: 0x90
   __DATA_CONST.__objc_superrefs: 0x640
   __DATA_CONST.__objc_arraydata: 0x990
   __DATA_CONST.__got: 0xbb8
   __AUTH_CONST.__const: 0x3be8
-  __AUTH_CONST.__cfstring: 0x17d20
-  __AUTH_CONST.__objc_const: 0x15748
+  __AUTH_CONST.__cfstring: 0x17d60
+  __AUTH_CONST.__objc_const: 0x15760
   __AUTH_CONST.__weak_auth_got: 0x18
   __AUTH_CONST.__lazy_load_got: 0x10
   __AUTH_CONST.__objc_intobj: 0x7e0

   - /usr/lib/libicucore.A.dylib
   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libsqlite3.dylib
-  Functions: 9604
-  Symbols:   16564
-  CStrings:  6105
+  Functions: 9619
+  Symbols:   16580
+  CStrings:  6119
 
Symbols:
+ -[LSApplicationRecord(MobileInstall) isInstallationHoldActive]
+ -[LSApplicationWorkspace setInstallationHoldActive:onApplicationWithBundleIdentifier:operationUUID:requestContext:saveObserver:error:]
+ -[LSBundleRecordUpdater rollPluginUUIDs]
+ -[LSBundleRecordUpdater setInstallationHoldActive:]
+ -[_LSDModifyClient setInstallationHoldActive:onApplicationWithBundleIdentifier:operationUUID:reply:]
+ GCC_except_table132
+ GCC_except_table223
+ GCC_except_table241
+ GCC_except_table258
+ GCC_except_table260
+ GCC_except_table262
+ GCC_except_table298
+ GCC_except_table305
+ GCC_except_table320
+ GCC_except_table326
+ GCC_except_table364
+ GCC_except_table370
+ GCC_except_table384
+ GCC_except_table386
+ GCC_except_table392
+ GCC_except_table395
+ GCC_except_table401
+ GCC_except_table406
+ GCC_except_table407
+ GCC_except_table408
+ GCC_except_table418
+ GCC_except_table424
+ GCC_except_table429
+ GCC_except_table433
+ GCC_except_table463
+ GCC_except_table471
+ GCC_except_table477
+ GCC_except_table481
+ GCC_except_table483
+ GCC_except_table487
+ GCC_except_table488
+ GCC_except_table492
+ GCC_except_table504
+ GCC_except_table524
+ GCC_except_table533
+ GCC_except_table534
+ GCC_except_table544
+ GCC_except_table568
+ __ZL35appAndPlaceholderUnitsForIdentifierP9LSContextP8NSString
+ ___100-[_LSDModifyClient setInstallationHoldActive:onApplicationWithBundleIdentifier:operationUUID:reply:]_block_invoke
+ ___134-[LSApplicationWorkspace setInstallationHoldActive:onApplicationWithBundleIdentifier:operationUUID:requestContext:saveObserver:error:]_block_invoke
+ ___134-[LSApplicationWorkspace setInstallationHoldActive:onApplicationWithBundleIdentifier:operationUUID:requestContext:saveObserver:error:]_block_invoke_2
+ ___40-[LSBundleRecordUpdater rollPluginUUIDs]_block_invoke
+ ____ZL24pluginUnitsForBundleDataP9LSContextPK12LSBundleData_block_invoke
+ ___block_descriptor_244_ea8_32r48c40_ZTSN14LaunchServices16BindingEvaluatorE_e379_v28?0I8r^{LSBundleData={LSBundleBaseData=IIIIIIIIii{LSVersionNumber=[32C]}{LSVersionNumber=[32C]}IIIIIIIIIIIICCIII{LSBundleBaseFlags=b1b1b1b1b1b1b1}}IQIIC{LSBundleMoreFlags=b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1}II{LSVersionNumber=[32C]}{LSVersionNumber=[32C]}IQQQIIIIIIIIIIIQIIQQQQIQQIIIQIQQIIIQIIIIIIIIIIIIIIIICCC[1I]II{LSAppClipFields=I}iIIIIIIIiIII}12*20l
+ ___block_descriptor_32_e392_B28?0^{LSContext=}8I16r^{LSBundleData={LSBundleBaseData=IIIIIIIIii{LSVersionNumber=[32C]}{LSVersionNumber=[32C]}IIIIIIIIIIIICCIII{LSBundleBaseFlags=b1b1b1b1b1b1b1}}IQIIC{LSBundleMoreFlags=b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1}II{LSVersionNumber=[32C]}{LSVersionNumber=[32C]}IQQQIIIIIIIIIIIQIIQQQQIQQIIIQIQQIIIQIIIIIIIIIIIIIIIICCC[1I]II{LSAppClipFields=I}iIIIIIIIiIII}20l
+ ___block_descriptor_40_ea8_32s_e392_B28?0"_LSDatabase"8I16r^{LSBundleData={LSBundleBaseData=IIIIIIIIii{LSVersionNumber=[32C]}{LSVersionNumber=[32C]}IIIIIIIIIIIICCIII{LSBundleBaseFlags=b1b1b1b1b1b1b1}}IQIIC{LSBundleMoreFlags=b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1}II{LSVersionNumber=[32C]}{LSVersionNumber=[32C]}IQQQIIIIIIIIIIIQIIQQQQIQQIIIQIQQIIIQIIIIIIIIIIIIIIIICCC[1I]II{LSAppClipFields=I}iIIIIIIIiIII}20ls32l8
+ ___block_descriptor_40_ea8_32s_e392_B28?0^{LSContext=}8I16r^{LSBundleData={LSBundleBaseData=IIIIIIIIii{LSVersionNumber=[32C]}{LSVersionNumber=[32C]}IIIIIIIIIIIICCIII{LSBundleBaseFlags=b1b1b1b1b1b1b1}}IQIIC{LSBundleMoreFlags=b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1}II{LSVersionNumber=[32C]}{LSVersionNumber=[32C]}IQQQIIIIIIIIIIIQIIQQQQIQQIIIQIQQIIIQIIIIIIIIIIIIIIIICCC[1I]II{LSAppClipFields=I}iIIIIIIIiIII}20ls32l8
+ ___block_descriptor_44_e392_B28?0"_LSDatabase"8I16r^{LSBundleData={LSBundleBaseData=IIIIIIIIii{LSVersionNumber=[32C]}{LSVersionNumber=[32C]}IIIIIIIIIIIICCIII{LSBundleBaseFlags=b1b1b1b1b1b1b1}}IQIIC{LSBundleMoreFlags=b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1}II{LSVersionNumber=[32C]}{LSVersionNumber=[32C]}IQQQIIIIIIIIIIIQIIQQQQIQQIIIQIQQIIIQIIIIIIIIIIIIIIIICCC[1I]II{LSAppClipFields=I}iIIIIIIIiIII}20l
+ ___block_descriptor_48_e8_32s40s_e392_v28?0"_LSDatabase"8I16r^{LSBundleData={LSBundleBaseData=IIIIIIIIii{LSVersionNumber=[32C]}{LSVersionNumber=[32C]}IIIIIIIIIIIICCIII{LSBundleBaseFlags=b1b1b1b1b1b1b1}}IQIIC{LSBundleMoreFlags=b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1}II{LSVersionNumber=[32C]}{LSVersionNumber=[32C]}IQQQIIIIIIIIIIIQIIQQQQIQQIIIQIQQIIIQIIIIIIIIIIIIIIIICCC[1I]II{LSAppClipFields=I}iIIIIIIIiIII}20ls32l8s40l8
+ ___block_descriptor_48_ea8_32bs_e389_v28?0"NSString"8I16r^{LSBundleData={LSBundleBaseData=IIIIIIIIii{LSVersionNumber=[32C]}{LSVersionNumber=[32C]}IIIIIIIIIIIICCIII{LSBundleBaseFlags=b1b1b1b1b1b1b1}}IQIIC{LSBundleMoreFlags=b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1}II{LSVersionNumber=[32C]}{LSVersionNumber=[32C]}IQQQIIIIIIIIIIIQIIQQQQIQQIIIQIQQIIIQIIIIIIIIIIIIIIIICCC[1I]II{LSAppClipFields=I}iIIIIIIIiIII}20ls32l8
+ ___block_descriptor_52_e8_32s40n6_8_8_s0_e392_v28?0"_LSDatabase"8I16r^{LSBundleData={LSBundleBaseData=IIIIIIIIii{LSVersionNumber=[32C]}{LSVersionNumber=[32C]}IIIIIIIIIIIICCIII{LSBundleBaseFlags=b1b1b1b1b1b1b1}}IQIIC{LSBundleMoreFlags=b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1}II{LSVersionNumber=[32C]}{LSVersionNumber=[32C]}IQQQIIIIIIIIIIIQIIQQQQIQQIIIQIQQIIIQIIIIIIIIIIIIIIIICCC[1I]II{LSAppClipFields=I}iIIIIIIIiIII}20l
+ ___block_descriptor_56_ea8_32bs40bs_e379_v28?0I8r^{LSBundleData={LSBundleBaseData=IIIIIIIIii{LSVersionNumber=[32C]}{LSVersionNumber=[32C]}IIIIIIIIIIIICCIII{LSBundleBaseFlags=b1b1b1b1b1b1b1}}IQIIC{LSBundleMoreFlags=b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1}II{LSVersionNumber=[32C]}{LSVersionNumber=[32C]}IQQQIIIIIIIIIIIQIIQQQQIQQIIIQIQQIIIQIIIIIIIIIIIIIIIICCC[1I]II{LSAppClipFields=I}iIIIIIIIiIII}12*20ls32l8s40l8
+ ___block_descriptor_56_ea8_32r40r_e379_v28?0I8r^{LSBundleData={LSBundleBaseData=IIIIIIIIii{LSVersionNumber=[32C]}{LSVersionNumber=[32C]}IIIIIIIIIIIICCIII{LSBundleBaseFlags=b1b1b1b1b1b1b1}}IQIIC{LSBundleMoreFlags=b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1}II{LSVersionNumber=[32C]}{LSVersionNumber=[32C]}IQQQIIIIIIIIIIIQIIQQQQIQQIIIQIQQIIIQIIIIIIIIIIIIIIIICCC[1I]II{LSAppClipFields=I}iIIIIIIIiIII}12*20lr32l8r40l8
+ ___block_descriptor_56_ea8_32s40bs_e379_v28?0I8r^{LSBundleData={LSBundleBaseData=IIIIIIIIii{LSVersionNumber=[32C]}{LSVersionNumber=[32C]}IIIIIIIIIIIICCIII{LSBundleBaseFlags=b1b1b1b1b1b1b1}}IQIIC{LSBundleMoreFlags=b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1}II{LSVersionNumber=[32C]}{LSVersionNumber=[32C]}IQQQIIIIIIIIIIIQIIQQQQIQQIIIQIQQIIIQIIIIIIIIIIIIIIIICCC[1I]II{LSAppClipFields=I}iIIIIIIIiIII}12*20ls32l8s40l8
+ ___block_descriptor_68_ea8_32s40s48s_e379_v28?0I8r^{LSBundleData={LSBundleBaseData=IIIIIIIIii{LSVersionNumber=[32C]}{LSVersionNumber=[32C]}IIIIIIIIIIIICCIII{LSBundleBaseFlags=b1b1b1b1b1b1b1}}IQIIC{LSBundleMoreFlags=b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1}II{LSVersionNumber=[32C]}{LSVersionNumber=[32C]}IQQQIIIIIIIIIIIQIIQQQQIQQIIIQIQQIIIQIIIIIIIIIIIIIIIICCC[1I]II{LSAppClipFields=I}iIIIIIIIiIII}12*20ls32l8s40l8s48l8
+ ___block_descriptor_72_e8_32bs40r48r_e379_v28?0I8r^{LSBundleData={LSBundleBaseData=IIIIIIIIii{LSVersionNumber=[32C]}{LSVersionNumber=[32C]}IIIIIIIIIIIICCIII{LSBundleBaseFlags=b1b1b1b1b1b1b1}}IQIIC{LSBundleMoreFlags=b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1}II{LSVersionNumber=[32C]}{LSVersionNumber=[32C]}IQQQIIIIIIIIIIIQIIQQQQIQQIIIQIQQIIIQIIIIIIIIIIIIIIIICCC[1I]II{LSAppClipFields=I}iIIIIIIIiIII}12*20ls32l8r40l8r48l8
+ ___block_descriptor_72_ea8_32s40s48r_e379_v28?0I8r^{LSBundleData={LSBundleBaseData=IIIIIIIIii{LSVersionNumber=[32C]}{LSVersionNumber=[32C]}IIIIIIIIIIIICCIII{LSBundleBaseFlags=b1b1b1b1b1b1b1}}IQIIC{LSBundleMoreFlags=b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1}II{LSVersionNumber=[32C]}{LSVersionNumber=[32C]}IQQQIIIIIIIIIIIQIIQQQQIQQIIIQIQQIIIQIIIIIIIIIIIIIIIICCC[1I]II{LSAppClipFields=I}iIIIIIIIiIII}12*20ls32l8s40l8r48l8
+ ___block_descriptor_73_ea8_32s40s48s56r64r_e42_v24?0"LSDBExecutionContext"8"NSError"16ls32l8s40l8s48l8r56l8r64l8
+ ___block_descriptor_80_e8_32s40s48s56s64n6_8_8_s0_e392_v28?0"_LSDatabase"8I16r^{LSBundleData={LSBundleBaseData=IIIIIIIIii{LSVersionNumber=[32C]}{LSVersionNumber=[32C]}IIIIIIIIIIIICCIII{LSBundleBaseFlags=b1b1b1b1b1b1b1}}IQIIC{LSBundleMoreFlags=b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1}II{LSVersionNumber=[32C]}{LSVersionNumber=[32C]}IQQQIIIIIIIIIIIQIIQQQQIQQIIIQIQQIIIQIIIIIIIIIIIIIIIICCC[1I]II{LSAppClipFields=I}iIIIIIIIiIII}20l
+ _objc_msgSend$isInstallationHoldActive
+ _objc_msgSend$rollPluginUUIDs
+ _objc_msgSend$setInstallationHoldActive:
+ _objc_msgSend$setInstallationHoldActive:onApplicationWithBundleIdentifier:operationUUID:reply:
- GCC_except_table220
- GCC_except_table230
- GCC_except_table235
- GCC_except_table239
- GCC_except_table257
- GCC_except_table287
- GCC_except_table295
- GCC_except_table300
- GCC_except_table302
- GCC_except_table314
- GCC_except_table323
- GCC_except_table328
- GCC_except_table363
- GCC_except_table367
- GCC_except_table374
- GCC_except_table382
- GCC_except_table389
- GCC_except_table397
- GCC_except_table402
- GCC_except_table417
- GCC_except_table423
- GCC_except_table428
- GCC_except_table432
- GCC_except_table460
- GCC_except_table468
- GCC_except_table474
- GCC_except_table478
- GCC_except_table480
- GCC_except_table484
- GCC_except_table485
- GCC_except_table486
- GCC_except_table501
- GCC_except_table521
- GCC_except_table522
- GCC_except_table530
- GCC_except_table541
- GCC_except_table565
- ___45-[LSBundleRecordUpdater parsePersonas:error:]_block_invoke
- ___block_descriptor_244_ea8_32r48c40_ZTSN14LaunchServices16BindingEvaluatorE_e377_v28?0I8r^{LSBundleData={LSBundleBaseData=IIIIIIIIii{LSVersionNumber=[32C]}{LSVersionNumber=[32C]}IIIIIIIIIIIICCIII{LSBundleBaseFlags=b1b1b1b1b1b1b1}}IQIIC{LSBundleMoreFlags=b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1}II{LSVersionNumber=[32C]}{LSVersionNumber=[32C]}IQQQIIIIIIIIIIIQIIQQQQIQQIIIQIQQIIIQIIIIIIIIIIIIIIIICCC[1I]II{LSAppClipFields=I}iIIIIIIIiIII}12*20l
- ___block_descriptor_32_e390_B28?0^{LSContext=}8I16r^{LSBundleData={LSBundleBaseData=IIIIIIIIii{LSVersionNumber=[32C]}{LSVersionNumber=[32C]}IIIIIIIIIIIICCIII{LSBundleBaseFlags=b1b1b1b1b1b1b1}}IQIIC{LSBundleMoreFlags=b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1}II{LSVersionNumber=[32C]}{LSVersionNumber=[32C]}IQQQIIIIIIIIIIIQIIQQQQIQQIIIQIQQIIIQIIIIIIIIIIIIIIIICCC[1I]II{LSAppClipFields=I}iIIIIIIIiIII}20l
- ___block_descriptor_40_ea8_32s_e390_B28?0"_LSDatabase"8I16r^{LSBundleData={LSBundleBaseData=IIIIIIIIii{LSVersionNumber=[32C]}{LSVersionNumber=[32C]}IIIIIIIIIIIICCIII{LSBundleBaseFlags=b1b1b1b1b1b1b1}}IQIIC{LSBundleMoreFlags=b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1}II{LSVersionNumber=[32C]}{LSVersionNumber=[32C]}IQQQIIIIIIIIIIIQIIQQQQIQQIIIQIQQIIIQIIIIIIIIIIIIIIIICCC[1I]II{LSAppClipFields=I}iIIIIIIIiIII}20ls32l8
- ___block_descriptor_40_ea8_32s_e390_B28?0^{LSContext=}8I16r^{LSBundleData={LSBundleBaseData=IIIIIIIIii{LSVersionNumber=[32C]}{LSVersionNumber=[32C]}IIIIIIIIIIIICCIII{LSBundleBaseFlags=b1b1b1b1b1b1b1}}IQIIC{LSBundleMoreFlags=b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1}II{LSVersionNumber=[32C]}{LSVersionNumber=[32C]}IQQQIIIIIIIIIIIQIIQQQQIQQIIIQIQQIIIQIIIIIIIIIIIIIIIICCC[1I]II{LSAppClipFields=I}iIIIIIIIiIII}20ls32l8
- ___block_descriptor_44_e390_B28?0"_LSDatabase"8I16r^{LSBundleData={LSBundleBaseData=IIIIIIIIii{LSVersionNumber=[32C]}{LSVersionNumber=[32C]}IIIIIIIIIIIICCIII{LSBundleBaseFlags=b1b1b1b1b1b1b1}}IQIIC{LSBundleMoreFlags=b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1}II{LSVersionNumber=[32C]}{LSVersionNumber=[32C]}IQQQIIIIIIIIIIIQIIQQQQIQQIIIQIQQIIIQIIIIIIIIIIIIIIIICCC[1I]II{LSAppClipFields=I}iIIIIIIIiIII}20l
- ___block_descriptor_48_e8_32s40s_e390_v28?0"_LSDatabase"8I16r^{LSBundleData={LSBundleBaseData=IIIIIIIIii{LSVersionNumber=[32C]}{LSVersionNumber=[32C]}IIIIIIIIIIIICCIII{LSBundleBaseFlags=b1b1b1b1b1b1b1}}IQIIC{LSBundleMoreFlags=b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1}II{LSVersionNumber=[32C]}{LSVersionNumber=[32C]}IQQQIIIIIIIIIIIQIIQQQQIQQIIIQIQQIIIQIIIIIIIIIIIIIIIICCC[1I]II{LSAppClipFields=I}iIIIIIIIiIII}20ls32l8s40l8
- ___block_descriptor_48_ea8_32bs_e387_v28?0"NSString"8I16r^{LSBundleData={LSBundleBaseData=IIIIIIIIii{LSVersionNumber=[32C]}{LSVersionNumber=[32C]}IIIIIIIIIIIICCIII{LSBundleBaseFlags=b1b1b1b1b1b1b1}}IQIIC{LSBundleMoreFlags=b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1}II{LSVersionNumber=[32C]}{LSVersionNumber=[32C]}IQQQIIIIIIIIIIIQIIQQQQIQQIIIQIQQIIIQIIIIIIIIIIIIIIIICCC[1I]II{LSAppClipFields=I}iIIIIIIIiIII}20ls32l8
- ___block_descriptor_52_e8_32s40n6_8_8_s0_e390_v28?0"_LSDatabase"8I16r^{LSBundleData={LSBundleBaseData=IIIIIIIIii{LSVersionNumber=[32C]}{LSVersionNumber=[32C]}IIIIIIIIIIIICCIII{LSBundleBaseFlags=b1b1b1b1b1b1b1}}IQIIC{LSBundleMoreFlags=b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1}II{LSVersionNumber=[32C]}{LSVersionNumber=[32C]}IQQQIIIIIIIIIIIQIIQQQQIQQIIIQIQQIIIQIIIIIIIIIIIIIIIICCC[1I]II{LSAppClipFields=I}iIIIIIIIiIII}20l
- ___block_descriptor_56_ea8_32bs40bs_e377_v28?0I8r^{LSBundleData={LSBundleBaseData=IIIIIIIIii{LSVersionNumber=[32C]}{LSVersionNumber=[32C]}IIIIIIIIIIIICCIII{LSBundleBaseFlags=b1b1b1b1b1b1b1}}IQIIC{LSBundleMoreFlags=b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1}II{LSVersionNumber=[32C]}{LSVersionNumber=[32C]}IQQQIIIIIIIIIIIQIIQQQQIQQIIIQIQQIIIQIIIIIIIIIIIIIIIICCC[1I]II{LSAppClipFields=I}iIIIIIIIiIII}12*20ls32l8s40l8
- ___block_descriptor_56_ea8_32r40r_e377_v28?0I8r^{LSBundleData={LSBundleBaseData=IIIIIIIIii{LSVersionNumber=[32C]}{LSVersionNumber=[32C]}IIIIIIIIIIIICCIII{LSBundleBaseFlags=b1b1b1b1b1b1b1}}IQIIC{LSBundleMoreFlags=b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1}II{LSVersionNumber=[32C]}{LSVersionNumber=[32C]}IQQQIIIIIIIIIIIQIIQQQQIQQIIIQIQQIIIQIIIIIIIIIIIIIIIICCC[1I]II{LSAppClipFields=I}iIIIIIIIiIII}12*20lr32l8r40l8
- ___block_descriptor_56_ea8_32s40bs_e377_v28?0I8r^{LSBundleData={LSBundleBaseData=IIIIIIIIii{LSVersionNumber=[32C]}{LSVersionNumber=[32C]}IIIIIIIIIIIICCIII{LSBundleBaseFlags=b1b1b1b1b1b1b1}}IQIIC{LSBundleMoreFlags=b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1}II{LSVersionNumber=[32C]}{LSVersionNumber=[32C]}IQQQIIIIIIIIIIIQIIQQQQIQQIIIQIQQIIIQIIIIIIIIIIIIIIIICCC[1I]II{LSAppClipFields=I}iIIIIIIIiIII}12*20ls32l8s40l8
- ___block_descriptor_68_ea8_32s40s48s_e377_v28?0I8r^{LSBundleData={LSBundleBaseData=IIIIIIIIii{LSVersionNumber=[32C]}{LSVersionNumber=[32C]}IIIIIIIIIIIICCIII{LSBundleBaseFlags=b1b1b1b1b1b1b1}}IQIIC{LSBundleMoreFlags=b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1}II{LSVersionNumber=[32C]}{LSVersionNumber=[32C]}IQQQIIIIIIIIIIIQIIQQQQIQQIIIQIQQIIIQIIIIIIIIIIIIIIIICCC[1I]II{LSAppClipFields=I}iIIIIIIIiIII}12*20ls32l8s40l8s48l8
- ___block_descriptor_72_e8_32bs40r48r_e377_v28?0I8r^{LSBundleData={LSBundleBaseData=IIIIIIIIii{LSVersionNumber=[32C]}{LSVersionNumber=[32C]}IIIIIIIIIIIICCIII{LSBundleBaseFlags=b1b1b1b1b1b1b1}}IQIIC{LSBundleMoreFlags=b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1}II{LSVersionNumber=[32C]}{LSVersionNumber=[32C]}IQQQIIIIIIIIIIIQIIQQQQIQQIIIQIQQIIIQIIIIIIIIIIIIIIIICCC[1I]II{LSAppClipFields=I}iIIIIIIIiIII}12*20ls32l8r40l8r48l8
- ___block_descriptor_72_ea8_32s40s48r_e377_v28?0I8r^{LSBundleData={LSBundleBaseData=IIIIIIIIii{LSVersionNumber=[32C]}{LSVersionNumber=[32C]}IIIIIIIIIIIICCIII{LSBundleBaseFlags=b1b1b1b1b1b1b1}}IQIIC{LSBundleMoreFlags=b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1}II{LSVersionNumber=[32C]}{LSVersionNumber=[32C]}IQQQIIIIIIIIIIIQIIQQQQIQQIIIQIQQIIIQIIIIIIIIIIIIIIIICCC[1I]II{LSAppClipFields=I}iIIIIIIIiIII}12*20ls32l8s40l8r48l8
- ___block_descriptor_80_e8_32s40s48s56s64n6_8_8_s0_e390_v28?0"_LSDatabase"8I16r^{LSBundleData={LSBundleBaseData=IIIIIIIIii{LSVersionNumber=[32C]}{LSVersionNumber=[32C]}IIIIIIIIIIIICCIII{LSBundleBaseFlags=b1b1b1b1b1b1b1}}IQIIC{LSBundleMoreFlags=b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1}II{LSVersionNumber=[32C]}{LSVersionNumber=[32C]}IQQQIIIIIIIIIIIQIIQQQQIQQIIIQIQQIIIQIIIIIIIIIIIIIIIICCC[1I]II{LSAppClipFields=I}iIIIIIIIiIII}20l
CStrings:
+ "-[_LSDModifyClient setInstallationHoldActive:onApplicationWithBundleIdentifier:operationUUID:reply:]"
+ "-[_LSDModifyClient setInstallationHoldActive:onApplicationWithBundleIdentifier:operationUUID:reply:]_block_invoke"
+ "B28@?0@\"_LSDatabase\"8I16r^{LSBundleData={LSBundleBaseData=IIIIIIIIii{LSVersionNumber=[32C]}{LSVersionNumber=[32C]}IIIIIIIIIIIICCIII{LSBundleBaseFlags=b1b1b1b1b1b1b1}}IQIIC{LSBundleMoreFlags=b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1}II{LSVersionNumber=[32C]}{LSVersionNumber=[32C]}IQQQIIIIIIIIIIIQIIQQQQIQQIIIQIQQIIIQIIIIIIIIIIIIIIIICCC[1I]II{LSAppClipFields=I}iIIIIIIIiIII}20"
+ "B28@?0^{LSContext=@}8I16r^{LSBundleData={LSBundleBaseData=IIIIIIIIii{LSVersionNumber=[32C]}{LSVersionNumber=[32C]}IIIIIIIIIIIICCIII{LSBundleBaseFlags=b1b1b1b1b1b1b1}}IQIIC{LSBundleMoreFlags=b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1}II{LSVersionNumber=[32C]}{LSVersionNumber=[32C]}IQQQIIIIIIIIIIIQIIQQQQIQQIIIQIQQIIIQIIIIIIIIIIIIIIIICCC[1I]II{LSAppClipFields=I}iIIIIIIIiIII}20"
+ "Parent app has an active installation hold"
+ "couldn't find parent app %#llx for plugin unit %#llx"
+ "installation-hold"
+ "operation %@ attempting to %{public}s installation hold on %@ from pid %ld"
+ "operation %@: Not all installation-hold updates were successful, but some were, so arming save timer"
+ "operation %@: Save after updating installation hold on %@ attempted: %d save error: %@"
+ "operation %@: could not %{public}s installation hold on %@ (bundle unit %llx): %@"
+ "operation %@: installation hold on %@ is already %{public}s; nothing to do"
+ "operation %@: installation-hold update succeeded"
+ "release"
+ "released"
+ "set"
+ "v28@?0@\"NSString\"8I16r^{LSBundleData={LSBundleBaseData=IIIIIIIIii{LSVersionNumber=[32C]}{LSVersionNumber=[32C]}IIIIIIIIIIIICCIII{LSBundleBaseFlags=b1b1b1b1b1b1b1}}IQIIC{LSBundleMoreFlags=b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1}II{LSVersionNumber=[32C]}{LSVersionNumber=[32C]}IQQQIIIIIIIIIIIQIIQQQQIQQIIIQIQQIIIQIIIIIIIIIIIIIIIICCC[1I]II{LSAppClipFields=I}iIIIIIIIiIII}20"
+ "v28@?0@\"_LSDatabase\"8I16r^{LSBundleData={LSBundleBaseData=IIIIIIIIii{LSVersionNumber=[32C]}{LSVersionNumber=[32C]}IIIIIIIIIIIICCIII{LSBundleBaseFlags=b1b1b1b1b1b1b1}}IQIIC{LSBundleMoreFlags=b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1}II{LSVersionNumber=[32C]}{LSVersionNumber=[32C]}IQQQIIIIIIIIIIIQIIQQQQIQQIIIQIQQIIIQIIIIIIIIIIIIIIIICCC[1I]II{LSAppClipFields=I}iIIIIIIIiIII}20"
+ "v28@?0I8r^{LSBundleData={LSBundleBaseData=IIIIIIIIii{LSVersionNumber=[32C]}{LSVersionNumber=[32C]}IIIIIIIIIIIICCIII{LSBundleBaseFlags=b1b1b1b1b1b1b1}}IQIIC{LSBundleMoreFlags=b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1}II{LSVersionNumber=[32C]}{LSVersionNumber=[32C]}IQQQIIIIIIIIIIIQIIQQQQIQQIIIQIQQIIIQIIIIIIIIIIIIIIIICCC[1I]II{LSAppClipFields=I}iIIIIIIIiIII}12*20"
- "B28@?0@\"_LSDatabase\"8I16r^{LSBundleData={LSBundleBaseData=IIIIIIIIii{LSVersionNumber=[32C]}{LSVersionNumber=[32C]}IIIIIIIIIIIICCIII{LSBundleBaseFlags=b1b1b1b1b1b1b1}}IQIIC{LSBundleMoreFlags=b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1}II{LSVersionNumber=[32C]}{LSVersionNumber=[32C]}IQQQIIIIIIIIIIIQIIQQQQIQQIIIQIQQIIIQIIIIIIIIIIIIIIIICCC[1I]II{LSAppClipFields=I}iIIIIIIIiIII}20"
- "B28@?0^{LSContext=@}8I16r^{LSBundleData={LSBundleBaseData=IIIIIIIIii{LSVersionNumber=[32C]}{LSVersionNumber=[32C]}IIIIIIIIIIIICCIII{LSBundleBaseFlags=b1b1b1b1b1b1b1}}IQIIC{LSBundleMoreFlags=b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1}II{LSVersionNumber=[32C]}{LSVersionNumber=[32C]}IQQQIIIIIIIIIIIQIIQQQQIQQIIIQIQQIIIQIIIIIIIIIIIIIIIICCC[1I]II{LSAppClipFields=I}iIIIIIIIiIII}20"
- "v28@?0@\"NSString\"8I16r^{LSBundleData={LSBundleBaseData=IIIIIIIIii{LSVersionNumber=[32C]}{LSVersionNumber=[32C]}IIIIIIIIIIIICCIII{LSBundleBaseFlags=b1b1b1b1b1b1b1}}IQIIC{LSBundleMoreFlags=b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1}II{LSVersionNumber=[32C]}{LSVersionNumber=[32C]}IQQQIIIIIIIIIIIQIIQQQQIQQIIIQIQQIIIQIIIIIIIIIIIIIIIICCC[1I]II{LSAppClipFields=I}iIIIIIIIiIII}20"
- "v28@?0@\"_LSDatabase\"8I16r^{LSBundleData={LSBundleBaseData=IIIIIIIIii{LSVersionNumber=[32C]}{LSVersionNumber=[32C]}IIIIIIIIIIIICCIII{LSBundleBaseFlags=b1b1b1b1b1b1b1}}IQIIC{LSBundleMoreFlags=b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1}II{LSVersionNumber=[32C]}{LSVersionNumber=[32C]}IQQQIIIIIIIIIIIQIIQQQQIQQIIIQIQQIIIQIIIIIIIIIIIIIIIICCC[1I]II{LSAppClipFields=I}iIIIIIIIiIII}20"
- "v28@?0I8r^{LSBundleData={LSBundleBaseData=IIIIIIIIii{LSVersionNumber=[32C]}{LSVersionNumber=[32C]}IIIIIIIIIIIICCIII{LSBundleBaseFlags=b1b1b1b1b1b1b1}}IQIIC{LSBundleMoreFlags=b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1}II{LSVersionNumber=[32C]}{LSVersionNumber=[32C]}IQQQIIIIIIIIIIIQIIQQQQIQQIIIQIQQIIIQIIIIIIIIIIIIIIIICCC[1I]II{LSAppClipFields=I}iIIIIIIIiIII}12*20"
```
