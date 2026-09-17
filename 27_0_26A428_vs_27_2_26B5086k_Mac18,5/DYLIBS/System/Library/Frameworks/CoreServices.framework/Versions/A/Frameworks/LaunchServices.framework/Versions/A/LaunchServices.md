## LaunchServices

> `/System/Library/Frameworks/CoreServices.framework/Versions/A/Frameworks/LaunchServices.framework/Versions/A/LaunchServices`

```diff

-1517.0.1.402.0
-  __TEXT.__text: 0x24d014
+1517.1.8.0.0
+  __TEXT.__text: 0x2506e8
   __TEXT.__lazy_helpers: 0xa8
-  __TEXT.__objc_methlist: 0xee14
-  __TEXT.__const: 0xac8
-  __TEXT.__cstring: 0x3383b
-  __TEXT.__oslogstring: 0x2262f
-  __TEXT.__gcc_except_tab: 0x347d8
+  __TEXT.__objc_methlist: 0xee84
+  __TEXT.__const: 0xad8
+  __TEXT.__cstring: 0x33e16
+  __TEXT.__oslogstring: 0x229f9
+  __TEXT.__gcc_except_tab: 0x34e2c
   __TEXT.__ustring: 0x1be
   __TEXT.__dof_LSFSNode: 0x2b6
-  __TEXT.__unwind_info: 0x101e8
+  __TEXT.__unwind_info: 0x10310
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0
   __TEXT.__objc_classname: 0x0
   __TEXT.__objc_methname: 0x0
   __TEXT.__objc_methtype: 0x0
-  __DATA_CONST.__const: 0x3ee0
+  __DATA_CONST.__const: 0x3f48
   __DATA_CONST.__objc_classlist: 0x7a8
   __DATA_CONST.__objc_catlist: 0x88
   __DATA_CONST.__objc_protolist: 0x190
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x6e80
+  __DATA_CONST.__objc_selrefs: 0x6ed0
   __DATA_CONST.__objc_protorefs: 0x98
   __DATA_CONST.__objc_superrefs: 0x638
   __DATA_CONST.__objc_arraydata: 0xa10
   __DATA_CONST.__got: 0xe40
-  __AUTH_CONST.__const: 0xab88
-  __AUTH_CONST.__cfstring: 0x1e020
-  __AUTH_CONST.__objc_const: 0x16688
+  __AUTH_CONST.__const: 0xabe8
+  __AUTH_CONST.__cfstring: 0x1e1e0
+  __AUTH_CONST.__objc_const: 0x166a8
   __AUTH_CONST.__weak_auth_got: 0x30
   __AUTH_CONST.__lazy_load_got: 0x10
-  __AUTH_CONST.__objc_intobj: 0x750
+  __AUTH_CONST.__objc_intobj: 0x738
   __AUTH_CONST.__objc_arrayobj: 0x138
   __AUTH_CONST.__objc_dictobj: 0x78
   __AUTH_CONST.__auth_got: 0x1ec8
   __AUTH.__objc_data: 0x3b60
   __AUTH.__data: 0x248
-  __DATA.__objc_ivar: 0xc68
+  __DATA.__objc_ivar: 0xc6c
   __DATA.__data: 0x15ec
   __DATA.__common: 0x5
   __DATA_DIRTY.__objc_data: 0x1130

   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libsqlite3.dylib
   - /usr/lib/system/libxpc.dylib
-  Functions: 11180
-  Symbols:   19557
-  CStrings:  7948
+  Functions: 11222
+  Symbols:   19612
+  CStrings:  7985
 
Symbols:
+ +[LSApplicationIdentity(Conveniences) applicationIdentityForJobLabel:error:]
+ +[LSApplicationRecord(AppReplacement) applicationRecordForPotentiallyReplacedBundleIdentifier:fetchingPlaceholder:error:]
+ +[LSBundleRecord _bundleRecordForApplicationIdentifier:context:pluginFindOptions:error:]
+ +[LSBundleRecord bundleRecordForApplicationIdentifier:error:]
+ -[LSApplicationRecord _LSRecord_resolve_jobLabel]
+ -[LSApplicationRecord initWithJobLabel:error:]
+ -[LSApplicationRecord jobLabelWithContext:tableID:unitID:unitBytes:]
+ -[LSApplicationRestrictionsManager clearCachedValues]
+ -[LSApplicationWorkspace setAppReplacementSourceBundleIdentifier:forApplicationWithBundleIdentifier:operationUUID:requestContext:saveObserver:error:]
+ -[LSApplicationWorkspace(Migration) migrateApplicationPreferencesFromIdentity:toIdentity:error:]
+ -[LSBundleRecordBuilder launchDLabel]
+ -[_LSDModifyClient migratePreferencesFromBundleIdentifier:toBundleIdentifier:destinationBundleVersion:completionHandler:]
+ GCC_except_table181
+ GCC_except_table188
+ GCC_except_table189
+ GCC_except_table191
+ GCC_except_table210
+ GCC_except_table221
+ GCC_except_table238
+ GCC_except_table254
+ GCC_except_table258
+ GCC_except_table267
+ GCC_except_table271
+ GCC_except_table273
+ GCC_except_table277
+ GCC_except_table280
+ GCC_except_table285
+ GCC_except_table286
+ GCC_except_table287
+ GCC_except_table288
+ GCC_except_table297
+ GCC_except_table298
+ GCC_except_table307
+ GCC_except_table324
+ GCC_except_table327
+ GCC_except_table328
+ GCC_except_table329
+ GCC_except_table331
+ GCC_except_table332
+ GCC_except_table339
+ GCC_except_table340
+ GCC_except_table341
+ GCC_except_table342
+ GCC_except_table348
+ GCC_except_table350
+ GCC_except_table353
+ GCC_except_table357
+ GCC_except_table358
+ GCC_except_table364
+ GCC_except_table374
+ GCC_except_table397
+ OBJC_IVAR_$_LSBundleRecordBuilder._launchDLabel
+ _LSGetApplicationIdentifierEntitlementKeys
+ _LSServer_LSHandlerPrefMigrateBundleID
+ _ZNSt3__116__if_likely_elseB9nqn220106IZNS_6vectorINS_4pairIjhEENS_9allocatorIS3_EEE12emplace_backIJRjS8_EEERS3_DpOT_EUlvE_ZNS7_IJS8_S8_EEES9_SC_EUlvE0_EEvbT_T0_
+ __LSBundleFindWithJobLabel
+ __LSGetApplicationIdentifierEntitlementKeys
+ __LSGetApplicationIdentifierFromEntitlements
+ __LSServer_LSHandlerPrefMigrateBundleID
+ __OBJC_$_CATEGORY_INSTANCE_METHODS_ICLBundleRecord_$_LSExtensions
+ __OBJC_$_CLASS_METHODS_LSApplicationRecord(Containers|iTunesMetadata|UniqueIdentifiers|InfoPlistRarities|Localization|AlternateIconsInternal|AlternateIcons|IconServices|Intents|UserActivity|Gaming|AppWrappers|MobileInstall|watchOS|InstallMachineryPrivate|Transitional|Identities|DefaultApps|BUIPrivate|ForRunningBoardOnly|JournalApp|AppReplacement|Redaction|Diagnostic|Enumeration)
+ __OBJC_$_CLASS_METHODS_LSApplicationWorkspace(PersonaNiceties|DeprecatedEnumeration|DefaultApps|Migration|URLQueries|DeprecatedURLQueries|OpenAdditions|PersonaAssociation|LSURLOverride)
+ __OBJC_$_INSTANCE_METHODS_LSApplicationRecord(Containers|iTunesMetadata|UniqueIdentifiers|InfoPlistRarities|Localization|AlternateIconsInternal|AlternateIcons|IconServices|Intents|UserActivity|Gaming|AppWrappers|MobileInstall|watchOS|InstallMachineryPrivate|Transitional|Identities|DefaultApps|BUIPrivate|ForRunningBoardOnly|JournalApp|AppReplacement|Redaction|Diagnostic|Enumeration)
+ __OBJC_$_INSTANCE_METHODS_LSApplicationWorkspace(PersonaNiceties|DeprecatedEnumeration|DefaultApps|Migration|URLQueries|DeprecatedURLQueries|OpenAdditions|PersonaAssociation|LSURLOverride)
+ __ZN13LSHandlerPref35MigrateRoleHandlersMatchingBundleIDEP11_LSDatabasejj15LSVersionNumber
+ __ZN14LaunchServices16BindingEvaluator18CreateWithJobLabelEP8NSStringb
+ __ZN14LaunchServices16BindingEvaluator31CreateWithApplicationIdentifierEP8NSStringbb
+ __ZN14LaunchServices16BundleCapability26getForBundleAndURLPropertyEP11_LSDatabaseP6FSNodePK12LSBundleDataPK10__CFString
+ __ZN14LaunchServices16BundleCapability26getForBundleAndURLPropertyEP11_LSDatabaseP6FSNodePK12LSBundleDataRKNS_21BundleCapabilityState14BundleInfoHintEPK10__CFString
+ __ZN14LaunchServices16BundleCapabilityC1EP11_LSDatabaseP6FSNodePK12LSBundleDataNS_10CapabilityE
+ __ZN14LaunchServices16BundleCapabilityC1EP11_LSDatabaseP6FSNodePK12LSBundleDataRKNS_21BundleCapabilityState14BundleInfoHintENS_10CapabilityE
+ __ZN14LaunchServices16BundleCapabilityC2EP11_LSDatabaseP6FSNodePK12LSBundleDataRKNS_21BundleCapabilityState14BundleInfoHintENS_10CapabilityE
+ __ZN14LaunchServices16BundleCapabilityD1Ev
+ __ZN14LaunchServices16BundleCapabilityD2Ev
+ __ZN14LaunchServices19URLPropertyProviderL40setNodeResourceValueUnlessSystemEnforcedEP6FSNodePK10__CFStringP11objc_objectPU15__autoreleasingP7NSError
+ __ZN14LaunchServices21BundleCapabilityState14BundleInfoHintC1EP11_LSDatabasePK12LSBundleData
+ __ZN14LaunchServices21BundleCapabilityState14BundleInfoHintC2EP11_LSDatabasePK12LSBundleData
+ __ZN14LaunchServices21BundleCapabilityStateC1EP11_LSDatabasePK12LSBundleDataPKNS_19PrefsCapabilityInfoE
+ __ZN14LaunchServices21BundleCapabilityStateC2EP11_LSDatabasePK12LSBundleDataPKNS_19PrefsCapabilityInfoERKNS0_14BundleInfoHintE
+ __ZNK14LaunchServices10Capability33getValueForBundleWithOptionalNodeEP11_LSDatabasePK12LSBundleDataRKNS_21BundleCapabilityStateEP6FSNodePU15__autoreleasingP7NSError
+ __ZNK14LaunchServices16BundleCapability17hardOverrideValueEv
+ __ZNK14LaunchServices16BundleCapability17softOverrideValueEv
+ __ZNK14LaunchServices16BundleCapability8getValueEv
+ __ZNK14LaunchServices21BundleCapabilityState13userCanChangeEv
+ __ZNSt3__116__if_likely_elseB9nqn220106IZNS_6vectorINS_4pairIjhEENS_9allocatorIS3_EEE12emplace_backIJRjS8_EEERS3_DpOT_EUlvE_ZNS7_IJS8_S8_EEES9_SC_EUlvE0_EEvbT_T0_
+ __ZNSt3__16vectorINS_4pairIjhEENS_9allocatorIS2_EEE20__throw_length_errorB9nqn220106Ev
+ __ZNSt3__16vectorINS_4pairIjhEENS_9allocatorIS2_EEE24__emplace_back_slow_pathIJRjS7_EEEPS2_DpOT_
+ __ZNSt3__18optionalIN14LaunchServices16BundleCapabilityEED2Ev
+ __ZNSt3__19allocatorINS_4pairIjhEEE17allocate_at_leastB9nqn220106Em
+ __ZZ42_LSGetApplicationIdentifierEntitlementKeysE5sOnce
+ __ZZ42_LSGetApplicationIdentifierEntitlementKeysE7sResult
+ ___121-[_LSDModifyClient migratePreferencesFromBundleIdentifier:toBundleIdentifier:destinationBundleVersion:completionHandler:]_block_invoke
+ ___46-[LSApplicationRecord initWithJobLabel:error:]_block_invoke
+ ___88+[LSBundleRecord _bundleRecordForApplicationIdentifier:context:pluginFindOptions:error:]_block_invoke
+ ___96-[LSApplicationWorkspace(Migration) migrateApplicationPreferencesFromIdentity:toIdentity:error:]_block_invoke
+ ___96-[LSApplicationWorkspace(Migration) migrateApplicationPreferencesFromIdentity:toIdentity:error:]_block_invoke_2
+ ___LSASNHash
+ ____LSGetApplicationIdentifierEntitlementKeys_block_invoke
+ ____ZN13LSHandlerPref35MigrateRoleHandlersMatchingBundleIDEP11_LSDatabasejj15LSVersionNumber_block_invoke
+ ___block_descriptor_32_e380_B28?0"_LSDatabase"8I16r^{LSBundleData={LSBundleBaseData=IIIIIIIIii{LSVersionNumber=[32C]}{LSVersionNumber=[32C]}IIIIIIIIIICCII{LSBundleBaseFlags=b1b1b1b1b1b1b1}}IQIICCCCCCCCCC{LSBundleMoreFlags=b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1}IIQQI{LSVersionNumber=[32C]}{LSVersionNumber=[32C]}Ii{LSVersionNumber=[32C]}QQIIIIIIIIIIIQIQQQIQQIIIQIQQIIIQIIIIIIIIIIIIIIIICCC[0I]IIiIIIIII}20l
+ ___block_descriptor_32_e380_B28?0^{LSContext=}8I16r^{LSBundleData={LSBundleBaseData=IIIIIIIIii{LSVersionNumber=[32C]}{LSVersionNumber=[32C]}IIIIIIIIIICCII{LSBundleBaseFlags=b1b1b1b1b1b1b1}}IQIICCCCCCCCCC{LSBundleMoreFlags=b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1}IIQQI{LSVersionNumber=[32C]}{LSVersionNumber=[32C]}Ii{LSVersionNumber=[32C]}QQIIIIIIIIIIIQIQQQIQQIIIQIQQIIIQIIIIIIIIIIIIIIIICCC[0I]IIiIIIIII}20l
+ ___block_descriptor_32_e383_B36?0^{LSContext=}8I16r^{LSBundleData={LSBundleBaseData=IIIIIIIIii{LSVersionNumber=[32C]}{LSVersionNumber=[32C]}IIIIIIIIIICCII{LSBundleBaseFlags=b1b1b1b1b1b1b1}}IQIICCCCCCCCCC{LSBundleMoreFlags=b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1}IIQQI{LSVersionNumber=[32C]}{LSVersionNumber=[32C]}Ii{LSVersionNumber=[32C]}QQIIIIIIIIIIIQIQQQIQQIIIQIQQIIIQIIIIIIIIIIIIIIIICCC[0I]IIiIIIIII}20*28l
+ ___block_descriptor_368_ea8_32r_e367_v28?0I8r^{LSBundleData={LSBundleBaseData=IIIIIIIIii{LSVersionNumber=[32C]}{LSVersionNumber=[32C]}IIIIIIIIIICCII{LSBundleBaseFlags=b1b1b1b1b1b1b1}}IQIICCCCCCCCCC{LSBundleMoreFlags=b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1}IIQQI{LSVersionNumber=[32C]}{LSVersionNumber=[32C]}Ii{LSVersionNumber=[32C]}QQIIIIIIIIIIIQIQQQIQQIIIQIQQIIIQIIIIIIIIIIIIIIIICCC[0I]IIiIIIIII}12*20l
+ ___block_descriptor_40_e383_B36?0^{LSContext=}8I16r^{LSBundleData={LSBundleBaseData=IIIIIIIIii{LSVersionNumber=[32C]}{LSVersionNumber=[32C]}IIIIIIIIIICCII{LSBundleBaseFlags=b1b1b1b1b1b1b1}}IQIICCCCCCCCCC{LSBundleMoreFlags=b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1}IIQQI{LSVersionNumber=[32C]}{LSVersionNumber=[32C]}Ii{LSVersionNumber=[32C]}QQIIIIIIIIIIIQIQQQIQQIIIQIQQIIIQIIIIIIIIIIIIIIIICCC[0I]IIiIIIIII}20*28l
+ ___block_descriptor_40_ea8_32s_e380_B28?0^{LSContext=}8I16r^{LSBundleData={LSBundleBaseData=IIIIIIIIii{LSVersionNumber=[32C]}{LSVersionNumber=[32C]}IIIIIIIIIICCII{LSBundleBaseFlags=b1b1b1b1b1b1b1}}IQIICCCCCCCCCC{LSBundleMoreFlags=b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1}IIQQI{LSVersionNumber=[32C]}{LSVersionNumber=[32C]}Ii{LSVersionNumber=[32C]}QQIIIIIIIIIIIQIQQQIQQIIIQIQQIIIQIIIIIIIIIIIIIIIICCC[0I]IIiIIIIII}20l
+ ___block_descriptor_44_e380_B28?0"_LSDatabase"8I16r^{LSBundleData={LSBundleBaseData=IIIIIIIIii{LSVersionNumber=[32C]}{LSVersionNumber=[32C]}IIIIIIIIIICCII{LSBundleBaseFlags=b1b1b1b1b1b1b1}}IQIICCCCCCCCCC{LSBundleMoreFlags=b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1}IIQQI{LSVersionNumber=[32C]}{LSVersionNumber=[32C]}Ii{LSVersionNumber=[32C]}QQIIIIIIIIIIIQIQQQIQQIIIQIQQIIIQIIIIIIIIIIIIIIIICCC[0I]IIiIIIIII}20l
+ ___block_descriptor_48_ea8_32bs_e194_v28?0"NSString"8I16r^{LSPluginData={LSBundleBaseData=IIIIIIIIii{LSVersionNumber=[32C]}{LSVersionNumber=[32C]}IIIIIIIIIICCII{LSBundleBaseFlags=b1b1b1b1b1b1b1}}IIIII{LSVersionNumber=[32C]}III}20l
+ ___block_descriptor_48_ea8_32bs_e377_v28?0"NSString"8I16r^{LSBundleData={LSBundleBaseData=IIIIIIIIii{LSVersionNumber=[32C]}{LSVersionNumber=[32C]}IIIIIIIIIICCII{LSBundleBaseFlags=b1b1b1b1b1b1b1}}IQIICCCCCCCCCC{LSBundleMoreFlags=b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1}IIQQI{LSVersionNumber=[32C]}{LSVersionNumber=[32C]}Ii{LSVersionNumber=[32C]}QQIIIIIIIIIIIQIQQQIQQIIIQIQQIIIQIIIIIIIIIIIIIIIICCC[0I]IIiIIIIII}20l
+ ___block_descriptor_56_ea8_32bs40bs_e367_v28?0I8r^{LSBundleData={LSBundleBaseData=IIIIIIIIii{LSVersionNumber=[32C]}{LSVersionNumber=[32C]}IIIIIIIIIICCII{LSBundleBaseFlags=b1b1b1b1b1b1b1}}IQIICCCCCCCCCC{LSBundleMoreFlags=b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1}IIQQI{LSVersionNumber=[32C]}{LSVersionNumber=[32C]}Ii{LSVersionNumber=[32C]}QQIIIIIIIIIIIQIQQQIQQIIIQIQQIIIQIIIIIIIIIIIIIIIICCC[0I]IIiIIIIII}12*20l
+ ___block_descriptor_56_ea8_32bs40rc_e367_v28?0I8r^{LSBundleData={LSBundleBaseData=IIIIIIIIii{LSVersionNumber=[32C]}{LSVersionNumber=[32C]}IIIIIIIIIICCII{LSBundleBaseFlags=b1b1b1b1b1b1b1}}IQIICCCCCCCCCC{LSBundleMoreFlags=b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1}IIQQI{LSVersionNumber=[32C]}{LSVersionNumber=[32C]}Ii{LSVersionNumber=[32C]}QQIIIIIIIIIIIQIQQQIQQIIIQIQQIIIQIIIIIIIIIIIIIIIICCC[0I]IIiIIIIII}12*20l
+ ___block_descriptor_56_ea8_32r40r_e367_v28?0I8r^{LSBundleData={LSBundleBaseData=IIIIIIIIii{LSVersionNumber=[32C]}{LSVersionNumber=[32C]}IIIIIIIIIICCII{LSBundleBaseFlags=b1b1b1b1b1b1b1}}IQIICCCCCCCCCC{LSBundleMoreFlags=b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1}IIQQI{LSVersionNumber=[32C]}{LSVersionNumber=[32C]}Ii{LSVersionNumber=[32C]}QQIIIIIIIIIIIQIQQQIQQIIIQIQQIIIQIIIIIIIIIIIIIIIICCC[0I]IIiIIIIII}12*20l
+ ___block_descriptor_56_ea8_32s40bs_e367_v28?0I8r^{LSBundleData={LSBundleBaseData=IIIIIIIIii{LSVersionNumber=[32C]}{LSVersionNumber=[32C]}IIIIIIIIIICCII{LSBundleBaseFlags=b1b1b1b1b1b1b1}}IQIICCCCCCCCCC{LSBundleMoreFlags=b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1}IIQQI{LSVersionNumber=[32C]}{LSVersionNumber=[32C]}Ii{LSVersionNumber=[32C]}QQIIIIIIIIIIIQIQQQIQQIIIQIQQIIIQIIIIIIIIIIIIIIIICCC[0I]IIiIIIIII}12*20l
+ ___block_descriptor_56_ea8_32s40s_e367_v28?0I8r^{LSBundleData={LSBundleBaseData=IIIIIIIIii{LSVersionNumber=[32C]}{LSVersionNumber=[32C]}IIIIIIIIIICCII{LSBundleBaseFlags=b1b1b1b1b1b1b1}}IQIICCCCCCCCCC{LSBundleMoreFlags=b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1}IIQQI{LSVersionNumber=[32C]}{LSVersionNumber=[32C]}Ii{LSVersionNumber=[32C]}QQIIIIIIIIIIIQIQQQIQQIIIQIQQIIIQIIIIIIIIIIIIIIIICCC[0I]IIiIIIIII}12*20l
+ ___block_descriptor_579_ea8_32s40r48r56r64r72r_e14_v24?0I8I12*16l
+ ___block_descriptor_648_ea8_32s_e37_v40?0q8"NSString"16"NSString"24*32l
+ ___block_descriptor_72_e8_32bs40r48r_e367_v28?0I8r^{LSBundleData={LSBundleBaseData=IIIIIIIIii{LSVersionNumber=[32C]}{LSVersionNumber=[32C]}IIIIIIIIIICCII{LSBundleBaseFlags=b1b1b1b1b1b1b1}}IQIICCCCCCCCCC{LSBundleMoreFlags=b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1}IIQQI{LSVersionNumber=[32C]}{LSVersionNumber=[32C]}Ii{LSVersionNumber=[32C]}QQIIIIIIIIIIIQIQQQIQQIIIQIQQIIIQIIIIIIIIIIIIIIIICCC[0I]IIiIIIIII}12*20l
+ ___block_descriptor_72_ea8_32s40s48r_e367_v28?0I8r^{LSBundleData={LSBundleBaseData=IIIIIIIIii{LSVersionNumber=[32C]}{LSVersionNumber=[32C]}IIIIIIIIIICCII{LSBundleBaseFlags=b1b1b1b1b1b1b1}}IQIICCCCCCCCCC{LSBundleMoreFlags=b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1}IIQQI{LSVersionNumber=[32C]}{LSVersionNumber=[32C]}Ii{LSVersionNumber=[32C]}QQIIIIIIIIIIIQIQQQIQQIIIQIQQIIIQIIIIIIIIIIIIIIIICCC[0I]IIiIIIIII}12*20l
+ ___block_descriptor_73_ea8_32s40r48r56r_e5_v8?0l
+ ___block_descriptor_96_ea8_32s40s48r56r_e42_v24?0"LSDBExecutionContext"8"NSError"16l
+ ___block_descriptor_97_ea8_40c45_ZTSN14LaunchServices21BundleCapabilityStateE_e5_v8?0l
+ ___copy_helper_block_ea8_40c45_ZTSN14LaunchServices21BundleCapabilityStateE
+ ___destroy_helper_block_ea8_40c45_ZTSN14LaunchServices21BundleCapabilityStateE
+ _kLSCanMigrateApplicationPreferencesEntitlement
+ _objc_msgSend$_bundleRecordForApplicationIdentifier:context:pluginFindOptions:error:
+ _objc_msgSend$findApplicationRecordWithError:
+ _objc_msgSend$initWithJobLabel:error:
+ _objc_msgSend$jobLabel
+ _objc_msgSend$migratePreferencesFromBundleIdentifier:toBundleIdentifier:destinationBundleVersion:completionHandler:
- -[ICLBundleRecord(LSTransitional) ls_associatedPersonasIfAvailable]
- GCC_except_table194
- GCC_except_table196
- GCC_except_table217
- GCC_except_table225
- GCC_except_table232
- GCC_except_table240
- GCC_except_table243
- GCC_except_table250
- GCC_except_table257
- GCC_except_table266
- GCC_except_table269
- GCC_except_table272
- GCC_except_table283
- GCC_except_table284
- GCC_except_table291
- GCC_except_table292
- GCC_except_table295
- GCC_except_table318
- GCC_except_table321
- GCC_except_table322
- GCC_except_table323
- GCC_except_table325
- GCC_except_table326
- GCC_except_table333
- GCC_except_table334
- GCC_except_table335
- GCC_except_table337
- GCC_except_table338
- GCC_except_table346
- GCC_except_table352
- GCC_except_table354
- GCC_except_table360
- GCC_except_table370
- GCC_except_table393
- __OBJC_$_CLASS_METHODS_LSApplicationRecord(Containers|iTunesMetadata|UniqueIdentifiers|InfoPlistRarities|Localization|AlternateIconsInternal|AlternateIcons|IconServices|Intents|UserActivity|Gaming|AppWrappers|MobileInstall|watchOS|InstallMachineryPrivate|Transitional|Identities|DefaultApps|BUIPrivate|ForRunningBoardOnly|JournalApp|Redaction|Diagnostic|Enumeration)
- __OBJC_$_CLASS_METHODS_LSApplicationWorkspace(PersonaNiceties|DeprecatedEnumeration|DefaultApps|URLQueries|DeprecatedURLQueries|OpenAdditions|PersonaAssociation|LSURLOverride)
- __OBJC_$_INSTANCE_METHODS_ICLBundleRecord(LSExtensions|LSTransitional)
- __OBJC_$_INSTANCE_METHODS_LSApplicationRecord(Containers|iTunesMetadata|UniqueIdentifiers|InfoPlistRarities|Localization|AlternateIconsInternal|AlternateIcons|IconServices|Intents|UserActivity|Gaming|AppWrappers|MobileInstall|watchOS|InstallMachineryPrivate|Transitional|Identities|DefaultApps|BUIPrivate|ForRunningBoardOnly|JournalApp|Redaction|Diagnostic|Enumeration)
- __OBJC_$_INSTANCE_METHODS_LSApplicationWorkspace(PersonaNiceties|DeprecatedEnumeration|DefaultApps|URLQueries|DeprecatedURLQueries|OpenAdditions|PersonaAssociation|LSURLOverride)
- __ZN14LaunchServices16BindingEvaluator31CreateWithApplicationIdentifierEP8NSStringb
- __ZN14LaunchServices19URLPropertyProviderL33systemEnforcedValueForURLPropertyEPK10__CFString
- __ZN21BundleCapabilityStateC2EP11_LSDatabasePK12LSBundleDataPKN14LaunchServices19PrefsCapabilityInfoE
- __ZNK14LaunchServices10Capability17getValueForBundleEP11_LSDatabasePK12LSBundleDatajPU15__autoreleasingP7NSError
- __ZNK14LaunchServices10Capability25getValueForBundleWithNodeEP11_LSDatabasePK12LSBundleDatajP6FSNodePU15__autoreleasingP7NSError
- __ZNK14LaunchServices10Capability33getValueForBundleWithOptionalNodeEP11_LSDatabasePK12LSBundleDataP6FSNodePU15__autoreleasingP7NSError
- __ZNK21BundleCapabilityState13userCanChangeEv
- __ZZN14LaunchServices19URLPropertyProviderL45overrideFlagsForApplicationInfoAndURLPropertyEP8NSString15LSVersionNumberP13_LSExceptionsPK10__CFStringE5flags
- ___67-[ICLBundleRecord(LSTransitional) ls_associatedPersonasIfAvailable]_block_invoke
- ___block_descriptor_32_e378_B28?0"_LSDatabase"8I16r^{LSBundleData={LSBundleBaseData=IIIIIIIii{LSVersionNumber=[32C]}{LSVersionNumber=[32C]}IIIIIIIIIICCII{LSBundleBaseFlags=b1b1b1b1b1b1b1}}IQIICCCCCCCCCC{LSBundleMoreFlags=b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1}IIQQI{LSVersionNumber=[32C]}{LSVersionNumber=[32C]}Ii{LSVersionNumber=[32C]}QQIIIIIIIIIIQIQQQIQQIIIQIQQIIIQIIIIIIIIIIIIIIIICCC[0I]IIiIIIIII}20l
- ___block_descriptor_32_e378_B28?0^{LSContext=}8I16r^{LSBundleData={LSBundleBaseData=IIIIIIIii{LSVersionNumber=[32C]}{LSVersionNumber=[32C]}IIIIIIIIIICCII{LSBundleBaseFlags=b1b1b1b1b1b1b1}}IQIICCCCCCCCCC{LSBundleMoreFlags=b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1}IIQQI{LSVersionNumber=[32C]}{LSVersionNumber=[32C]}Ii{LSVersionNumber=[32C]}QQIIIIIIIIIIQIQQQIQQIIIQIQQIIIQIIIIIIIIIIIIIIIICCC[0I]IIiIIIIII}20l
- ___block_descriptor_32_e381_B36?0^{LSContext=}8I16r^{LSBundleData={LSBundleBaseData=IIIIIIIii{LSVersionNumber=[32C]}{LSVersionNumber=[32C]}IIIIIIIIIICCII{LSBundleBaseFlags=b1b1b1b1b1b1b1}}IQIICCCCCCCCCC{LSBundleMoreFlags=b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1}IIQQI{LSVersionNumber=[32C]}{LSVersionNumber=[32C]}Ii{LSVersionNumber=[32C]}QQIIIIIIIIIIQIQQQIQQIIIQIQQIIIQIIIIIIIIIIIIIIIICCC[0I]IIiIIIIII}20*28l
- ___block_descriptor_368_ea8_32r_e365_v28?0I8r^{LSBundleData={LSBundleBaseData=IIIIIIIii{LSVersionNumber=[32C]}{LSVersionNumber=[32C]}IIIIIIIIIICCII{LSBundleBaseFlags=b1b1b1b1b1b1b1}}IQIICCCCCCCCCC{LSBundleMoreFlags=b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1}IIQQI{LSVersionNumber=[32C]}{LSVersionNumber=[32C]}Ii{LSVersionNumber=[32C]}QQIIIIIIIIIIQIQQQIQQIIIQIQQIIIQIIIIIIIIIIIIIIIICCC[0I]IIiIIIIII}12*20l
- ___block_descriptor_40_e381_B36?0^{LSContext=}8I16r^{LSBundleData={LSBundleBaseData=IIIIIIIii{LSVersionNumber=[32C]}{LSVersionNumber=[32C]}IIIIIIIIIICCII{LSBundleBaseFlags=b1b1b1b1b1b1b1}}IQIICCCCCCCCCC{LSBundleMoreFlags=b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1}IIQQI{LSVersionNumber=[32C]}{LSVersionNumber=[32C]}Ii{LSVersionNumber=[32C]}QQIIIIIIIIIIQIQQQIQQIIIQIQQIIIQIIIIIIIIIIIIIIIICCC[0I]IIiIIIIII}20*28l
- ___block_descriptor_40_ea8_32s_e378_B28?0^{LSContext=}8I16r^{LSBundleData={LSBundleBaseData=IIIIIIIii{LSVersionNumber=[32C]}{LSVersionNumber=[32C]}IIIIIIIIIICCII{LSBundleBaseFlags=b1b1b1b1b1b1b1}}IQIICCCCCCCCCC{LSBundleMoreFlags=b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1}IIQQI{LSVersionNumber=[32C]}{LSVersionNumber=[32C]}Ii{LSVersionNumber=[32C]}QQIIIIIIIIIIQIQQQIQQIIIQIQQIIIQIIIIIIIIIIIIIIIICCC[0I]IIiIIIIII}20l
- ___block_descriptor_415_ea8_32s40r48r56r64r72r_e14_v24?0I8I12*16l
- ___block_descriptor_44_e378_B28?0"_LSDatabase"8I16r^{LSBundleData={LSBundleBaseData=IIIIIIIii{LSVersionNumber=[32C]}{LSVersionNumber=[32C]}IIIIIIIIIICCII{LSBundleBaseFlags=b1b1b1b1b1b1b1}}IQIICCCCCCCCCC{LSBundleMoreFlags=b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1}IIQQI{LSVersionNumber=[32C]}{LSVersionNumber=[32C]}Ii{LSVersionNumber=[32C]}QQIIIIIIIIIIQIQQQIQQIIIQIQQIIIQIIIIIIIIIIIIIIIICCC[0I]IIiIIIIII}20l
- ___block_descriptor_48_ea8_32bs_e193_v28?0"NSString"8I16r^{LSPluginData={LSBundleBaseData=IIIIIIIii{LSVersionNumber=[32C]}{LSVersionNumber=[32C]}IIIIIIIIIICCII{LSBundleBaseFlags=b1b1b1b1b1b1b1}}IIIII{LSVersionNumber=[32C]}III}20l
- ___block_descriptor_48_ea8_32bs_e375_v28?0"NSString"8I16r^{LSBundleData={LSBundleBaseData=IIIIIIIii{LSVersionNumber=[32C]}{LSVersionNumber=[32C]}IIIIIIIIIICCII{LSBundleBaseFlags=b1b1b1b1b1b1b1}}IQIICCCCCCCCCC{LSBundleMoreFlags=b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1}IIQQI{LSVersionNumber=[32C]}{LSVersionNumber=[32C]}Ii{LSVersionNumber=[32C]}QQIIIIIIIIIIQIQQQIQQIIIQIQQIIIQIIIIIIIIIIIIIIIICCC[0I]IIiIIIIII}20l
- ___block_descriptor_56_ea8_32bs40bs_e365_v28?0I8r^{LSBundleData={LSBundleBaseData=IIIIIIIii{LSVersionNumber=[32C]}{LSVersionNumber=[32C]}IIIIIIIIIICCII{LSBundleBaseFlags=b1b1b1b1b1b1b1}}IQIICCCCCCCCCC{LSBundleMoreFlags=b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1}IIQQI{LSVersionNumber=[32C]}{LSVersionNumber=[32C]}Ii{LSVersionNumber=[32C]}QQIIIIIIIIIIQIQQQIQQIIIQIQQIIIQIIIIIIIIIIIIIIIICCC[0I]IIiIIIIII}12*20l
- ___block_descriptor_56_ea8_32bs40rc_e365_v28?0I8r^{LSBundleData={LSBundleBaseData=IIIIIIIii{LSVersionNumber=[32C]}{LSVersionNumber=[32C]}IIIIIIIIIICCII{LSBundleBaseFlags=b1b1b1b1b1b1b1}}IQIICCCCCCCCCC{LSBundleMoreFlags=b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1}IIQQI{LSVersionNumber=[32C]}{LSVersionNumber=[32C]}Ii{LSVersionNumber=[32C]}QQIIIIIIIIIIQIQQQIQQIIIQIQQIIIQIIIIIIIIIIIIIIIICCC[0I]IIiIIIIII}12*20l
- ___block_descriptor_56_ea8_32r40r_e365_v28?0I8r^{LSBundleData={LSBundleBaseData=IIIIIIIii{LSVersionNumber=[32C]}{LSVersionNumber=[32C]}IIIIIIIIIICCII{LSBundleBaseFlags=b1b1b1b1b1b1b1}}IQIICCCCCCCCCC{LSBundleMoreFlags=b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1}IIQQI{LSVersionNumber=[32C]}{LSVersionNumber=[32C]}Ii{LSVersionNumber=[32C]}QQIIIIIIIIIIQIQQQIQQIIIQIQQIIIQIIIIIIIIIIIIIIIICCC[0I]IIiIIIIII}12*20l
- ___block_descriptor_56_ea8_32s40bs_e365_v28?0I8r^{LSBundleData={LSBundleBaseData=IIIIIIIii{LSVersionNumber=[32C]}{LSVersionNumber=[32C]}IIIIIIIIIICCII{LSBundleBaseFlags=b1b1b1b1b1b1b1}}IQIICCCCCCCCCC{LSBundleMoreFlags=b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1}IIQQI{LSVersionNumber=[32C]}{LSVersionNumber=[32C]}Ii{LSVersionNumber=[32C]}QQIIIIIIIIIIQIQQQIQQIIIQIQQIIIQIIIIIIIIIIIIIIIICCC[0I]IIiIIIIII}12*20l
- ___block_descriptor_56_ea8_32s40s_e365_v28?0I8r^{LSBundleData={LSBundleBaseData=IIIIIIIii{LSVersionNumber=[32C]}{LSVersionNumber=[32C]}IIIIIIIIIICCII{LSBundleBaseFlags=b1b1b1b1b1b1b1}}IQIICCCCCCCCCC{LSBundleMoreFlags=b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1}IIQQI{LSVersionNumber=[32C]}{LSVersionNumber=[32C]}Ii{LSVersionNumber=[32C]}QQIIIIIIIIIIQIQQQIQQIIIQIQQIIIQIIIIIIIIIIIIIIIICCC[0I]IIiIIIIII}12*20l
- ___block_descriptor_640_ea8_32s_e37_v40?0q8"NSString"16"NSString"24*32l
- ___block_descriptor_72_e8_32bs40r48r_e365_v28?0I8r^{LSBundleData={LSBundleBaseData=IIIIIIIii{LSVersionNumber=[32C]}{LSVersionNumber=[32C]}IIIIIIIIIICCII{LSBundleBaseFlags=b1b1b1b1b1b1b1}}IQIICCCCCCCCCC{LSBundleMoreFlags=b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1}IIQQI{LSVersionNumber=[32C]}{LSVersionNumber=[32C]}Ii{LSVersionNumber=[32C]}QQIIIIIIIIIIQIQQQIQQIIIQIQQIIIQIIIIIIIIIIIIIIIICCC[0I]IIiIIIIII}12*20l
- ___block_descriptor_72_ea8_32s40s48r_e365_v28?0I8r^{LSBundleData={LSBundleBaseData=IIIIIIIii{LSVersionNumber=[32C]}{LSVersionNumber=[32C]}IIIIIIIIIICCII{LSBundleBaseFlags=b1b1b1b1b1b1b1}}IQIICCCCCCCCCC{LSBundleMoreFlags=b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1}IIQQI{LSVersionNumber=[32C]}{LSVersionNumber=[32C]}Ii{LSVersionNumber=[32C]}QQIIIIIIIIIIQIQQQIQQIIIQIQQIIIQIIIIIIIIIIIIIIIICCC[0I]IIiIIIIII}12*20l
- ___block_descriptor_97_ea8_40c27_ZTS21BundleCapabilityState_e5_v8?0l
- ___copy_helper_block_ea8_40c27_ZTS21BundleCapabilityState
- ___destroy_helper_block_ea8_40c27_ZTS21BundleCapabilityState
- _objc_msgSend$ls_associatedPersonasIfAvailable
- ls_associatedPersonasIfAvailable.onceToken
- ls_associatedPersonasIfAvailable.responds
CStrings:
+ " 4 0#1%4#0\"0"
+ "%{public}s: alias %#x bookmark was stale (relative to %{public}s); stored file 0x%llx at %{private}@; resolved %{public}s to volume 0x%llx file 0x%llx at %{private}@"
+ "%{public}s: bundle %#x changed; container %#x, resolved node volume 0x%llx file 0x%llx"
+ "%{public}s: bundle %#x existence check failed for its recorded path; container %#x, stored file 0x%llx at %{private}@; falling back to alias resolution"
+ "%{public}s: bundle %#x has no recorded path for alias %#x; falling back to alias resolution"
+ "%{public}s: cached node not found, registering new node for bundle %#x; container %#x, volume 0x%llx file 0x%llx, node %{private}@"
+ "%{public}s: node changed, re-registering bundle %#x; container %#x, volume 0x%llx file 0x%llx, node %{private}@"
+ "+[LSApplicationIdentity(Conveniences) applicationIdentityForJobLabel:error:]"
+ "+[LSApplicationRecord(AppReplacement) applicationRecordForPotentiallyReplacedBundleIdentifier:fetchingPlaceholder:error:]"
+ "+[LSBundleRecord _bundleRecordForApplicationIdentifier:context:pluginFindOptions:error:]"
+ "-[LSApplicationRecord initWithJobLabel:error:]"
+ "-[LSApplicationWorkspace setAppReplacementSourceBundleIdentifier:forApplicationWithBundleIdentifier:operationUUID:requestContext:saveObserver:error:]"
+ "-[LSApplicationWorkspace(Migration) migrateApplicationPreferencesFromIdentity:toIdentity:error:]"
+ "-[_LSDModifyClient migratePreferencesFromBundleIdentifier:toBundleIdentifier:destinationBundleVersion:completionHandler:]"
+ "AppID"
+ "AppIDBinding"
+ "B28@?0@\"_LSDatabase\"8I16r^{LSBundleData={LSBundleBaseData=IIIIIIIIii{LSVersionNumber=[32C]}{LSVersionNumber=[32C]}IIIIIIIIIICCII{LSBundleBaseFlags=b1b1b1b1b1b1b1}}IQIICCCCCCCCCC{LSBundleMoreFlags=b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1}IIQQI{LSVersionNumber=[32C]}{LSVersionNumber=[32C]}Ii{LSVersionNumber=[32C]}QQIIIIIIIIIIIQIQQQIQQIIIQIQQIIIQIIIIIIIIIIIIIIIICCC[0I]IIiIIIIII}20"
+ "B28@?0^{LSContext=@}8I16r^{LSBundleData={LSBundleBaseData=IIIIIIIIii{LSVersionNumber=[32C]}{LSVersionNumber=[32C]}IIIIIIIIIICCII{LSBundleBaseFlags=b1b1b1b1b1b1b1}}IQIICCCCCCCCCC{LSBundleMoreFlags=b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1}IIQQI{LSVersionNumber=[32C]}{LSVersionNumber=[32C]}Ii{LSVersionNumber=[32C]}QQIIIIIIIIIIIQIQQQIQQIIIQIQQIIIQIIIIIIIIIIIIIIIICCC[0I]IIiIIIIII}20"
+ "B36@?0^{LSContext=@}8I16r^{LSBundleData={LSBundleBaseData=IIIIIIIIii{LSVersionNumber=[32C]}{LSVersionNumber=[32C]}IIIIIIIIIICCII{LSBundleBaseFlags=b1b1b1b1b1b1b1}}IQIICCCCCCCCCC{LSBundleMoreFlags=b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1}IIQQI{LSVersionNumber=[32C]}{LSVersionNumber=[32C]}Ii{LSVersionNumber=[32C]}QQIIIIIIIIIIIQIQQQIQQIIIQIQQIIIQIIIIIIIIIIIIIIIICCC[0I]IIiIIIIII}20*28"
+ "BOOL _LSServer_LSHandlerPrefMigrateBundleID(LSContext *, NSString *__strong, NSString *__strong, LSVersionNumber, NSError *__autoreleasing *)"
+ "Couldn't get capability for should be hidden by system pref: %@"
+ "Creating binding evaluator for job label %@"
+ "Found unit %llx for job label %@ but found no bundle data for it"
+ "JobLabelBinding"
+ "PluginAppIDBinding"
+ "Unable to create string for bundleID %{public}@ while migrating handler prefs from %@"
+ "_LSServer_LSHandlerPrefMigrateBundleID"
+ "another node"
+ "appID"
+ "com.apple.private.coreservices.appmigration.write"
+ "const LSPluginData *_LSPluginFindWithPlatformInfo(__strong LSDatabaseRef, CFStringRef, CFStringRef, CFStringRef, LSPluginFindOptions, FSNode *__strong, dyld_platform_t, LSPluginID *, NSError *__autoreleasing *)"
+ "jobLabel"
+ "jobLabel != nil"
+ "need bundleID"
+ "need job label to bind by job label"
+ "nil"
+ "no version available for destination %@ while migrating preferences: %@"
+ "pid %ld error migrating preferences from %@ to %@: %@"
+ "pid %ld migrated preferences from %@ to %@"
+ "source %@ and destination %@ mapped to the same bundleID, nothing to do"
+ "sourceBundleID and destBundleID must differ"
+ "sourceBundleID/destBundleID"
+ "sourceIdentity and destinationIdentity must have different bundle identifiers"
+ "static BindingEvaluator LaunchServices::BindingEvaluator::CreateWithJobLabel(NSString *const __strong _Nonnull, BOOL)"
+ "static NSInteger LaunchServices::PrefsStorage::_GetIndexOfValueInPrefsArrayWithPredicate(NSArray *__strong, const Pred &) [Pred = (lambda at /AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.<TMP>/Sources/CoreServicesSubFrameworks/LaunchServices.subprj/Source/LaunchServices/Info/LSPrefs.mm:1587:63)]"
+ "static NSInteger LaunchServices::PrefsStorage::_GetIndexOfValueInPrefsArrayWithPredicate(NSArray *__strong, const Pred &) [Pred = (lambda at /AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.<TMP>/Sources/CoreServicesSubFrameworks/LaunchServices.subprj/Source/LaunchServices/Info/LSPrefs.mm:1618:65)]"
+ "static NSInteger LaunchServices::PrefsStorage::_GetIndexOfValueInPrefsArrayWithPredicate(NSArray *__strong, const Pred &) [Pred = (lambda at /AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.<TMP>/Sources/CoreServicesSubFrameworks/LaunchServices.subprj/Source/LaunchServices/Info/LSPrefs.mm:1625:65)]"
+ "static id LaunchServices::PrefsStorage::_GetValueInPrefsArrayWithPredicate(NSArray *__strong, __unsafe_unretained Class, const Pred &) [Pred = (lambda at /AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.<TMP>/Sources/CoreServicesSubFrameworks/LaunchServices.subprj/Source/LaunchServices/Info/LSPrefs.mm:1618:65)]"
+ "static id LaunchServices::PrefsStorage::_GetValueInPrefsArrayWithPredicate(NSArray *__strong, __unsafe_unretained Class, const Pred &) [Pred = (lambda at /AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.<TMP>/Sources/CoreServicesSubFrameworks/LaunchServices.subprj/Source/LaunchServices/Info/LSPrefs.mm:1625:65)]"
+ "successfully"
+ "unsuccessfully"
+ "v28@?0@\"NSString\"8I16r^{LSBundleData={LSBundleBaseData=IIIIIIIIii{LSVersionNumber=[32C]}{LSVersionNumber=[32C]}IIIIIIIIIICCII{LSBundleBaseFlags=b1b1b1b1b1b1b1}}IQIICCCCCCCCCC{LSBundleMoreFlags=b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1}IIQQI{LSVersionNumber=[32C]}{LSVersionNumber=[32C]}Ii{LSVersionNumber=[32C]}QQIIIIIIIIIIIQIQQQIQQIIIQIQQIIIQIIIIIIIIIIIIIIIICCC[0I]IIiIIIIII}20"
+ "v28@?0@\"NSString\"8I16r^{LSPluginData={LSBundleBaseData=IIIIIIIIii{LSVersionNumber=[32C]}{LSVersionNumber=[32C]}IIIIIIIIIICCII{LSBundleBaseFlags=b1b1b1b1b1b1b1}}IIIII{LSVersionNumber=[32C]}III}20"
+ "v28@?0I8r^{LSBundleData={LSBundleBaseData=IIIIIIIIii{LSVersionNumber=[32C]}{LSVersionNumber=[32C]}IIIIIIIIIICCII{LSBundleBaseFlags=b1b1b1b1b1b1b1}}IQIICCCCCCCCCC{LSBundleMoreFlags=b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1}IIQQI{LSVersionNumber=[32C]}{LSVersionNumber=[32C]}Ii{LSVersionNumber=[32C]}QQIIIIIIIIIIIQIQQQIQQIIIQIQQIIIQIIIIIIIIIIIIIIIICCC[0I]IIiIIIIII}12*20"
- " 4 0#0%4#0\"0"
- "%s: cached node not found, registering new node %@"
- "%s: node changed, re-registering %{private}@"
- "B28@?0@\"_LSDatabase\"8I16r^{LSBundleData={LSBundleBaseData=IIIIIIIii{LSVersionNumber=[32C]}{LSVersionNumber=[32C]}IIIIIIIIIICCII{LSBundleBaseFlags=b1b1b1b1b1b1b1}}IQIICCCCCCCCCC{LSBundleMoreFlags=b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1}IIQQI{LSVersionNumber=[32C]}{LSVersionNumber=[32C]}Ii{LSVersionNumber=[32C]}QQIIIIIIIIIIQIQQQIQQIIIQIQQIIIQIIIIIIIIIIIIIIIICCC[0I]IIiIIIIII}20"
- "B28@?0^{LSContext=@}8I16r^{LSBundleData={LSBundleBaseData=IIIIIIIii{LSVersionNumber=[32C]}{LSVersionNumber=[32C]}IIIIIIIIIICCII{LSBundleBaseFlags=b1b1b1b1b1b1b1}}IQIICCCCCCCCCC{LSBundleMoreFlags=b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1}IIQQI{LSVersionNumber=[32C]}{LSVersionNumber=[32C]}Ii{LSVersionNumber=[32C]}QQIIIIIIIIIIQIQQQIQQIIIQIQQIIIQIIIIIIIIIIIIIIIICCC[0I]IIiIIIIII}20"
- "B36@?0^{LSContext=@}8I16r^{LSBundleData={LSBundleBaseData=IIIIIIIii{LSVersionNumber=[32C]}{LSVersionNumber=[32C]}IIIIIIIIIICCII{LSBundleBaseFlags=b1b1b1b1b1b1b1}}IQIICCCCCCCCCC{LSBundleMoreFlags=b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1}IIQQI{LSVersionNumber=[32C]}{LSVersionNumber=[32C]}Ii{LSVersionNumber=[32C]}QQIIIIIIIIIIQIQQQIQQIIIQIQQIIIQIIIIIIIIIIIIIIIICCC[0I]IIiIIIIII}20*28"
- "Couldn't get capaibility for should be hidden by system pref: %@"
- "const LSPluginData *_LSPluginFindWithPlatformInfo(__strong LSDatabaseRef, CFStringRef, CFStringRef, LSPluginFindOptions, FSNode *__strong, dyld_platform_t, LSPluginID *, NSError *__autoreleasing *)"
- "launch-with-label"
- "static NSInteger LaunchServices::PrefsStorage::_GetIndexOfValueInPrefsArrayWithPredicate(NSArray *__strong, const Pred &) [Pred = (lambda at /AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.<TMP>/Sources/CoreServicesSubFrameworks/LaunchServices.subprj/Source/LaunchServices/Info/LSPrefs.mm:1498:63)]"
- "static NSInteger LaunchServices::PrefsStorage::_GetIndexOfValueInPrefsArrayWithPredicate(NSArray *__strong, const Pred &) [Pred = (lambda at /AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.<TMP>/Sources/CoreServicesSubFrameworks/LaunchServices.subprj/Source/LaunchServices/Info/LSPrefs.mm:1529:65)]"
- "static NSInteger LaunchServices::PrefsStorage::_GetIndexOfValueInPrefsArrayWithPredicate(NSArray *__strong, const Pred &) [Pred = (lambda at /AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.<TMP>/Sources/CoreServicesSubFrameworks/LaunchServices.subprj/Source/LaunchServices/Info/LSPrefs.mm:1536:65)]"
- "static id LaunchServices::PrefsStorage::_GetValueInPrefsArrayWithPredicate(NSArray *__strong, __unsafe_unretained Class, const Pred &) [Pred = (lambda at /AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.<TMP>/Sources/CoreServicesSubFrameworks/LaunchServices.subprj/Source/LaunchServices/Info/LSPrefs.mm:1529:65)]"
- "static id LaunchServices::PrefsStorage::_GetValueInPrefsArrayWithPredicate(NSArray *__strong, __unsafe_unretained Class, const Pred &) [Pred = (lambda at /AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.<TMP>/Sources/CoreServicesSubFrameworks/LaunchServices.subprj/Source/LaunchServices/Info/LSPrefs.mm:1536:65)]"
- "v28@?0@\"NSString\"8I16r^{LSBundleData={LSBundleBaseData=IIIIIIIii{LSVersionNumber=[32C]}{LSVersionNumber=[32C]}IIIIIIIIIICCII{LSBundleBaseFlags=b1b1b1b1b1b1b1}}IQIICCCCCCCCCC{LSBundleMoreFlags=b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1}IIQQI{LSVersionNumber=[32C]}{LSVersionNumber=[32C]}Ii{LSVersionNumber=[32C]}QQIIIIIIIIIIQIQQQIQQIIIQIQQIIIQIIIIIIIIIIIIIIIICCC[0I]IIiIIIIII}20"
- "v28@?0@\"NSString\"8I16r^{LSPluginData={LSBundleBaseData=IIIIIIIii{LSVersionNumber=[32C]}{LSVersionNumber=[32C]}IIIIIIIIIICCII{LSBundleBaseFlags=b1b1b1b1b1b1b1}}IIIII{LSVersionNumber=[32C]}III}20"
- "v28@?0I8r^{LSBundleData={LSBundleBaseData=IIIIIIIii{LSVersionNumber=[32C]}{LSVersionNumber=[32C]}IIIIIIIIIICCII{LSBundleBaseFlags=b1b1b1b1b1b1b1}}IQIICCCCCCCCCC{LSBundleMoreFlags=b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1}IIQQI{LSVersionNumber=[32C]}{LSVersionNumber=[32C]}Ii{LSVersionNumber=[32C]}QQIIIIIIIIIIQIQQQIQQIIIQIQQIIIQIIIIIIIIIIIIIIIICCC[0I]IIiIIIIII}12*20"
```
