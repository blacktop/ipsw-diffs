## CoreServices

> `/System/Library/Frameworks/CoreServices.framework/CoreServices`

```diff

-1444.1.3.100.0
-  __TEXT.__text: 0x1aa3a8
-  __TEXT.__auth_stubs: 0x3080
+1444.2.8.0.0
+  __TEXT.__text: 0x1ac6fc
+  __TEXT.__auth_stubs: 0x30e0
   __TEXT.__delay_stubs: 0x2c
   __TEXT.__delay_helper: 0x16c
-  __TEXT.__objc_methlist: 0xccb4
+  __TEXT.__objc_methlist: 0xcd1c
   __TEXT.__const: 0x910
-  __TEXT.__cstring: 0x2479f
-  __TEXT.__oslogstring: 0x13623
-  __TEXT.__gcc_except_tab: 0x26ebc
+  __TEXT.__cstring: 0x249cd
+  __TEXT.__oslogstring: 0x137a8
+  __TEXT.__gcc_except_tab: 0x27304
   __TEXT.__ustring: 0x23c
-  __TEXT.__unwind_info: 0xb028
+  __TEXT.__unwind_info: 0xb1c0
   __TEXT.__eh_frame: 0x60
-  __TEXT.__objc_classname: 0x1ea9
-  __TEXT.__objc_methname: 0x1d02e
-  __TEXT.__objc_methtype: 0xa6a4
-  __TEXT.__objc_stubs: 0x10300
+  __TEXT.__objc_classname: 0x1f0e
+  __TEXT.__objc_methname: 0x1d1d8
+  __TEXT.__objc_methtype: 0xa9b6
+  __TEXT.__objc_stubs: 0x10380
   __DATA_CONST.__got: 0xa90
-  __DATA_CONST.__const: 0x6c58
-  __DATA_CONST.__objc_classlist: 0x6b0
+  __DATA_CONST.__const: 0x6d00
+  __DATA_CONST.__objc_classlist: 0x6b8
   __DATA_CONST.__objc_catlist: 0x50
-  __DATA_CONST.__objc_protolist: 0x138
+  __DATA_CONST.__objc_protolist: 0x140
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x5e90
+  __DATA_CONST.__objc_selrefs: 0x5ea0
   __DATA_CONST.__objc_protorefs: 0x90
-  __DATA_CONST.__objc_superrefs: 0x568
+  __DATA_CONST.__objc_superrefs: 0x570
   __DATA_CONST.__objc_arraydata: 0x180
-  __AUTH_CONST.__auth_got: 0x1860
-  __AUTH_CONST.__const: 0x35f0
-  __AUTH_CONST.__cfstring: 0x169e0
-  __AUTH_CONST.__objc_const: 0x12f08
-  __AUTH_CONST.__objc_intobj: 0x810
+  __AUTH_CONST.__auth_got: 0x1890
+  __AUTH_CONST.__const: 0x3690
+  __AUTH_CONST.__cfstring: 0x16aa0
+  __AUTH_CONST.__objc_const: 0x13130
+  __AUTH_CONST.__objc_intobj: 0x828
   __AUTH_CONST.__objc_dictobj: 0x50
   __AUTH_CONST.__objc_arrayobj: 0x120
-  __AUTH.__objc_data: 0x2b70
+  __AUTH.__objc_data: 0x2bc0
   __AUTH.__data: 0x318
-  __DATA.__objc_ivar: 0xa94
-  __DATA.__data: 0x1264
-  __DATA.__bss: 0xe80
+  __DATA.__objc_ivar: 0xab8
+  __DATA.__data: 0x12c4
+  __DATA.__bss: 0xe90
   __DATA.__common: 0x40
   __DATA_DIRTY.__objc_data: 0x1770
   __DATA_DIRTY.__data: 0x50

   - /usr/lib/libicucore.A.dylib
   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libsqlite3.dylib
-  UUID: C28F44CA-1E64-3EE8-9990-D036B2CED8C5
-  Functions: 8624
-  Symbols:   28030
-  CStrings:  13616
+  UUID: 076BFAA1-9250-30F3-94FD-CC909AFC0CD4
+  Functions: 8674
+  Symbols:   28204
+  CStrings:  13661
 
Symbols:
+ +[LSRatingRankEligibilityMonitor sharedServerInstance]
+ +[LSRatingRankEligibilityMonitor sharedServerInstance].cold.1
+ +[_LSStringLocalizer(Private) addContextualUsageDescriptionValuesToLocalizedKeys:fromInfoDictionary:]
+ -[LSApplicationRestrictionsManager(RatingRankMonitorDelegate) bundlesWithIdentifiers:ratingRankEligibilityChanged:monitor:]
+ -[LSBundleRecord _LSRecord_resolve__contextualFeatureUsageDescriptions]
+ -[LSBundleRecord _contextualFeatureUsageDescriptionLocStrRecordForFeature:contextKey:]
+ -[LSBundleRecord _contextualFeatureUsageDescriptionMapKeyForFeature:contextKey:]
+ -[LSBundleRecord _contextualFeatureUsageDescriptionsWithContext:tableID:unitID:unitBytes:]
+ -[LSBundleRecord _contextualFeatureUsageDescriptions]
+ -[LSBundleRecord(LocalizedName) hasLocalizedUsageDescriptionForFeature:contextKey:]
+ -[LSBundleRecord(LocalizedName) localizedUsageDescriptionForFeature:contextKey:]
+ -[LSBundleRecord(LocalizedName) localizedUsageDescriptionForFeature:contextKey:preferredLocalizations:]
+ -[LSBundleRecordBuilder ratingRankEligibilityDomain]
+ -[LSRatingRankEligibilityMonitor .cxx_construct]
+ -[LSRatingRankEligibilityMonitor .cxx_destruct]
+ -[LSRatingRankEligibilityMonitor _queue_domainNotificationFired:]
+ -[LSRatingRankEligibilityMonitor dealloc]
+ -[LSRatingRankEligibilityMonitor ensureMonitoringDomain:]
+ -[LSRatingRankEligibilityMonitor ensureMonitoringDomain:].cold.1
+ -[LSRatingRankEligibilityMonitor initWithTargetQueue:stateProvider:]
+ -[LSRatingRankEligibilityMonitor initWithTargetQueue:stateProvider:].cold.1
+ -[LSRatingRankEligibilityMonitor resume]
+ -[LSRatingRankEligibilityMonitor scanForDomainsInDatabase:]
+ -[_LSApplicationState _isApplicationInRatingRankExceptionListWithStateProvider:]
+ -[_LSApplicationState _isRatingRankActive]
+ -[_LSApplicationState initWithBundleIdentifier:stateFlags:ratingRank:ratingRankEligibilityDomain:installType:]
+ GCC_except_table160
+ GCC_except_table165
+ GCC_except_table248
+ GCC_except_table253
+ _OBJC_CLASS_$_LSRatingRankEligibilityMonitor
+ _OBJC_IVAR_$_LSBundleRecordBuilder._contextualIdentityUsageDescriptions
+ _OBJC_IVAR_$_LSBundleRecordBuilder._localizedContextualIdentityUsageDescriptions
+ _OBJC_IVAR_$_LSBundleRecordBuilder._ratingRankEligibilityDomain
+ _OBJC_IVAR_$_LSRatingRankEligibilityMonitor._activeTokens
+ _OBJC_IVAR_$_LSRatingRankEligibilityMonitor._delegate
+ _OBJC_IVAR_$_LSRatingRankEligibilityMonitor._flags
+ _OBJC_IVAR_$_LSRatingRankEligibilityMonitor._lock
+ _OBJC_IVAR_$_LSRatingRankEligibilityMonitor._queue
+ _OBJC_IVAR_$__LSApplicationState._ratingRankEligibilityDomain
+ _OBJC_METACLASS_$_LSRatingRankEligibilityMonitor
+ __CSDictionaryCreateWithKeysAndValues
+ __CSDictionaryDispose
+ __CSDictionaryEnumerateAllValues
+ __LSBundleBaseDataDisposeMembers
+ __LSBundleBaseDataWriteDescription
+ __OBJC_$_INSTANCE_METHODS_LSApplicationRestrictionsManager(RatingRankMonitorDelegate)
+ __OBJC_$_INSTANCE_METHODS_LSRatingRankEligibilityMonitor
+ __OBJC_$_INSTANCE_VARIABLES_LSRatingRankEligibilityMonitor
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_LSRatingRankEligibilityMonitorDelegate
+ __OBJC_$_PROTOCOL_METHOD_TYPES_LSRatingRankEligibilityMonitorDelegate
+ __OBJC_$_PROTOCOL_REFS_LSRatingRankEligibilityMonitorDelegate
+ __OBJC_CLASS_PROTOCOLS_$_LSApplicationRestrictionsManager(RatingRankMonitorDelegate)
+ __OBJC_CLASS_RO_$_LSRatingRankEligibilityMonitor
+ __OBJC_LABEL_PROTOCOL_$_LSRatingRankEligibilityMonitorDelegate
+ __OBJC_METACLASS_RO_$_LSRatingRankEligibilityMonitor
+ __OBJC_PROTOCOL_$_LSRatingRankEligibilityMonitorDelegate
+ __ZN14LaunchServices10BaseBundle43ContextualUsageDescriptionDictionaryBuilder16createDictionaryEP11_LSDatabase
+ __ZN14LaunchServices10BaseBundle43ContextualUsageDescriptionDictionaryBuilder16createDictionaryEP11_LSDatabase.cold.1
+ __ZN14LaunchServices10BaseBundle43ContextualUsageDescriptionDictionaryBuilder18addContextualUsageEP8NSStringS3_P12NSDictionaryIS3_S3_E
+ __ZN14LaunchServices7notifyd11NotifyTokenC1EOS1_
+ __ZNSt3__110unique_ptrINS_11__tree_nodeINS_12__value_typeI23os_eligibility_domain_tN14LaunchServices7notifyd11NotifyTokenEEEPvEENS_22__tree_node_destructorINS_9allocatorIS9_EEEEED1B8nn200100Ev
+ __ZNSt3__114__split_bufferINS_4pairIU8__strongP8NSStringN14LaunchServices10BaseBundle43ContextualUsageDescriptionDictionaryBuilder20ProtoLocalizedStringEEERNS_9allocatorIS9_EEED2Ev
+ __ZNSt3__134__uninitialized_allocator_relocateB8nn200100INS_9allocatorINS_4pairIU8__strongP8NSStringN14LaunchServices10BaseBundle43ContextualUsageDescriptionDictionaryBuilder20ProtoLocalizedStringEEEEEPSA_EEvRT_T0_SF_SF_
+ __ZNSt3__14pairIU8__strongP8NSStringN14LaunchServices10BaseBundle43ContextualUsageDescriptionDictionaryBuilder20ProtoLocalizedStringEED2Ev
+ __ZNSt3__16__treeINS_12__value_typeI23os_eligibility_domain_tN14LaunchServices7notifyd11NotifyTokenEEENS_19__map_value_compareIS2_S6_NS_4lessIS2_EELb1EEENS_9allocatorIS6_EEE16__construct_nodeIJNS_4pairIS2_S5_EEEEENS_10unique_ptrINS_11__tree_nodeIS6_PvEENS_22__tree_node_destructorINSB_ISK_EEEEEEDpOT_
+ __ZNSt3__16__treeINS_12__value_typeI23os_eligibility_domain_tN14LaunchServices7notifyd11NotifyTokenEEENS_19__map_value_compareIS2_S6_NS_4lessIS2_EELb1EEENS_9allocatorIS6_EEE16__insert_node_atEPNS_15__tree_end_nodeIPNS_16__tree_node_baseIPvEEEERSI_SI_
+ __ZNSt3__16__treeINS_12__value_typeI23os_eligibility_domain_tN14LaunchServices7notifyd11NotifyTokenEEENS_19__map_value_compareIS2_S6_NS_4lessIS2_EELb1EEENS_9allocatorIS6_EEE25__emplace_unique_key_argsIS2_JNS_4pairIS2_S5_EEEEENSF_INS_15__tree_iteratorIS6_PNS_11__tree_nodeIS6_PvEElEEbEERKT_DpOT0_
+ __ZNSt3__16__treeINS_12__value_typeI23os_eligibility_domain_tN14LaunchServices7notifyd11NotifyTokenEEENS_19__map_value_compareIS2_S6_NS_4lessIS2_EELb1EEENS_9allocatorIS6_EEE7destroyEPNS_11__tree_nodeIS6_PvEE
+ __ZNSt3__16vectorINS_4pairIU8__strongP8NSStringN14LaunchServices10BaseBundle43ContextualUsageDescriptionDictionaryBuilder20ProtoLocalizedStringEEENS_9allocatorIS9_EEE16__destroy_vectorclB8nn200100Ev
+ __ZNSt3__16vectorINS_4pairIU8__strongP8NSStringN14LaunchServices10BaseBundle43ContextualUsageDescriptionDictionaryBuilder20ProtoLocalizedStringEEENS_9allocatorIS9_EEE20__throw_length_errorB8nn200100Ev
+ __ZNSt3__16vectorINS_4pairIU8__strongP8NSStringN14LaunchServices10BaseBundle43ContextualUsageDescriptionDictionaryBuilder20ProtoLocalizedStringEEENS_9allocatorIS9_EEE24__emplace_back_slow_pathIJS9_EEEPS9_DpOT_
+ __ZNSt3__16vectorINS_4pairIU8__strongP8NSStringN14LaunchServices10BaseBundle43ContextualUsageDescriptionDictionaryBuilder20ProtoLocalizedStringEEENS_9allocatorIS9_EEE5clearB8nn200100Ev
+ __ZNSt3__16vectorINS_4pairIU8__strongP8NSStringN14LaunchServices10BaseBundle43ContextualUsageDescriptionDictionaryBuilder20ProtoLocalizedStringEEENS_9allocatorIS9_EEE9push_backB8nn200100EOS9_
+ __ZNSt3__19allocatorINS_4pairIU8__strongP8NSStringN14LaunchServices10BaseBundle43ContextualUsageDescriptionDictionaryBuilder20ProtoLocalizedStringEEEE17allocate_at_leastB8nn200100Em
+ __ZZ54+[LSRatingRankEligibilityMonitor sharedServerInstance]E14sharedInstance
+ __ZZ54+[LSRatingRankEligibilityMonitor sharedServerInstance]E9onceToken
+ ___123-[LSApplicationRestrictionsManager(RatingRankMonitorDelegate) bundlesWithIdentifiers:ratingRankEligibilityChanged:monitor:]_block_invoke
+ ___47-[LSBundleRecordBuilder buildBundleData:error:]_block_invoke.712
+ ___54+[LSRatingRankEligibilityMonitor sharedServerInstance]_block_invoke
+ ___57-[LSRatingRankEligibilityMonitor ensureMonitoringDomain:]_block_invoke
+ ___59-[LSRatingRankEligibilityMonitor scanForDomainsInDatabase:]_block_invoke
+ ___65-[LSRatingRankEligibilityMonitor _queue_domainNotificationFired:]_block_invoke
+ ___65-[LSRatingRankEligibilityMonitor _queue_domainNotificationFired:]_block_invoke_2
+ ___65-[LSRatingRankEligibilityMonitor _queue_domainNotificationFired:]_block_invoke_2.cold.1
+ ___90-[LSBundleRecord _contextualFeatureUsageDescriptionsWithContext:tableID:unitID:unitBytes:]_block_invoke
+ ___Block_byref_object_copy_.623
+ ___Block_byref_object_dispose_.624
+ ____LSBundleBaseDataDisposeMembers_block_invoke
+ ____LSBundleBaseDataWriteDescription_block_invoke
+ ____LSBundleFindWithNode_block_invoke.64
+ ____LSBundleRemove_block_invoke.83
+ ____LSBundleRemove_block_invoke_2.84
+ ___block_descriptor_32_e379_B28?0^{LSContext=}8I16r^{LSBundleData={LSBundleBaseData=IIIIIIi{LSVersionNumber=[32C]}{LSVersionNumber=[32C]}IIIIIIIIIIIIICCISI{LSBundleBaseFlags=b1b1b1b1b1b1b1}}IQIIC{LSBundleMoreFlags=b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1}IiI{LSVersionNumber=[32C]}{LSVersionNumber=[32C]}IQQQIIIIIIIIIIQIIQQQQIQQIIIQIQIIQIIIIIIIIIIIIIIIICCCI[1I]II{LSAppClipFields=I}iIIIIIII}20l
+ ___block_descriptor_40_ea8_32s_e379_B28?0"_LSDatabase"8I16r^{LSBundleData={LSBundleBaseData=IIIIIIi{LSVersionNumber=[32C]}{LSVersionNumber=[32C]}IIIIIIIIIIIIICCISI{LSBundleBaseFlags=b1b1b1b1b1b1b1}}IQIIC{LSBundleMoreFlags=b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1}IiI{LSVersionNumber=[32C]}{LSVersionNumber=[32C]}IQQQIIIIIIIIIIQIIQQQQIQQIIIQIQIIQIIIIIIIIIIIIIIIICCCI[1I]II{LSAppClipFields=I}iIIIIIII}20ls32l8
+ ___block_descriptor_40_ea8_32s_e379_B28?0^{LSContext=}8I16r^{LSBundleData={LSBundleBaseData=IIIIIIi{LSVersionNumber=[32C]}{LSVersionNumber=[32C]}IIIIIIIIIIIIICCISI{LSBundleBaseFlags=b1b1b1b1b1b1b1}}IQIIC{LSBundleMoreFlags=b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1}IiI{LSVersionNumber=[32C]}{LSVersionNumber=[32C]}IQQQIIIIIIIIIIQIIQQQQIQQIIIQIQIIQIIIIIIIIIIIIIIIICCCI[1I]II{LSAppClipFields=I}iIIIIIII}20ls32l8
+ ___block_descriptor_44_e379_B28?0"_LSDatabase"8I16r^{LSBundleData={LSBundleBaseData=IIIIIIi{LSVersionNumber=[32C]}{LSVersionNumber=[32C]}IIIIIIIIIIIIICCISI{LSBundleBaseFlags=b1b1b1b1b1b1b1}}IQIIC{LSBundleMoreFlags=b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1}IiI{LSVersionNumber=[32C]}{LSVersionNumber=[32C]}IQQQIIIIIIIIIIQIIQQQQIQQIIIQIQIIQIIIIIIIIIIIIIIIICCCI[1I]II{LSAppClipFields=I}iIIIIIII}20l
+ ___block_descriptor_48_ea8_32bs_e196_v28?0"NSString"8I16r^{LSPluginData={LSBundleBaseData=IIIIIIi{LSVersionNumber=[32C]}{LSVersionNumber=[32C]}IIIIIIIIIIIIICCISI{LSBundleBaseFlags=b1b1b1b1b1b1b1}}IIIII{LSVersionNumber=[32C]}IIII}20ls32l8
+ ___block_descriptor_48_ea8_32bs_e376_v28?0"NSString"8I16r^{LSBundleData={LSBundleBaseData=IIIIIIi{LSVersionNumber=[32C]}{LSVersionNumber=[32C]}IIIIIIIIIIIIICCISI{LSBundleBaseFlags=b1b1b1b1b1b1b1}}IQIIC{LSBundleMoreFlags=b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1}IiI{LSVersionNumber=[32C]}{LSVersionNumber=[32C]}IQQQIIIIIIIIIIQIIQQQQIQQIIIQIQIIQIIIIIIIIIIIIIIIICCCI[1I]II{LSAppClipFields=I}iIIIIIII}20ls32l8
+ ___block_descriptor_48_ea8_32s_e39_v32?0"NSString"8"NSDictionary"16^B24ls32l8
+ ___block_descriptor_48_ea8_32s_e42_v24?0"LSDBExecutionContext"8"NSError"16ls32l8
+ ___block_descriptor_48_ea8_32w_e5_v8?0lw32l8
+ ___block_descriptor_52_ea8_32s_e366_v28?0I8r^{LSBundleData={LSBundleBaseData=IIIIIIi{LSVersionNumber=[32C]}{LSVersionNumber=[32C]}IIIIIIIIIIIIICCISI{LSBundleBaseFlags=b1b1b1b1b1b1b1}}IQIIC{LSBundleMoreFlags=b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1}IiI{LSVersionNumber=[32C]}{LSVersionNumber=[32C]}IQQQIIIIIIIIIIQIIQQQQIQQIIIQIQIIQIIIIIIIIIIIIIIIICCCI[1I]II{LSAppClipFields=I}iIIIIIII}12*20ls32l8
+ ___block_descriptor_56_ea8_32bs40bs_e366_v28?0I8r^{LSBundleData={LSBundleBaseData=IIIIIIi{LSVersionNumber=[32C]}{LSVersionNumber=[32C]}IIIIIIIIIIIIICCISI{LSBundleBaseFlags=b1b1b1b1b1b1b1}}IQIIC{LSBundleMoreFlags=b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1}IiI{LSVersionNumber=[32C]}{LSVersionNumber=[32C]}IQQQIIIIIIIIIIQIIQQQQIQQIIIQIQIIQIIIIIIIIIIIIIIIICCCI[1I]II{LSAppClipFields=I}iIIIIIII}12*20ls32l8s40l8
+ ___block_descriptor_56_ea8_32r40r_e366_v28?0I8r^{LSBundleData={LSBundleBaseData=IIIIIIi{LSVersionNumber=[32C]}{LSVersionNumber=[32C]}IIIIIIIIIIIIICCISI{LSBundleBaseFlags=b1b1b1b1b1b1b1}}IQIIC{LSBundleMoreFlags=b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1}IiI{LSVersionNumber=[32C]}{LSVersionNumber=[32C]}IQQQIIIIIIIIIIQIIQQQQIQQIIIQIQIIQIIIIIIIIIIIIIIIICCCI[1I]II{LSAppClipFields=I}iIIIIIII}12*20lr32l8r40l8
+ ___block_descriptor_56_ea8_32s40bs_e366_v28?0I8r^{LSBundleData={LSBundleBaseData=IIIIIIi{LSVersionNumber=[32C]}{LSVersionNumber=[32C]}IIIIIIIIIIIIICCISI{LSBundleBaseFlags=b1b1b1b1b1b1b1}}IQIIC{LSBundleMoreFlags=b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1}IiI{LSVersionNumber=[32C]}{LSVersionNumber=[32C]}IQQQIIIIIIIIIIQIIQQQQIQQIIIQIQIIQIIIIIIIIIIIIIIIICCCI[1I]II{LSAppClipFields=I}iIIIIIII}12*20ls32l8s40l8
+ ___block_descriptor_56_ea8_32s_e19_v32?0I8r^v12I20*24ls32l8
+ ___block_descriptor_612_ea8_32s_e19_v32?0I8r^v12I20*24ls32l8
+ ___block_descriptor_612_ea8_32s_e37_v40?0q8"NSString"16"NSString"24*32ls32l8
+ ___block_descriptor_72_e8_32bs40r48r_e366_v28?0I8r^{LSBundleData={LSBundleBaseData=IIIIIIi{LSVersionNumber=[32C]}{LSVersionNumber=[32C]}IIIIIIIIIIIIICCISI{LSBundleBaseFlags=b1b1b1b1b1b1b1}}IQIIC{LSBundleMoreFlags=b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1}IiI{LSVersionNumber=[32C]}{LSVersionNumber=[32C]}IQQQIIIIIIIIIIQIIQQQQIQQIIIQIQIIQIIIIIIIIIIIIIIIICCCI[1I]II{LSAppClipFields=I}iIIIIIII}12*20ls32l8r40l8r48l8
+ ___block_descriptor_72_ea8_32s40s48r_e366_v28?0I8r^{LSBundleData={LSBundleBaseData=IIIIIIi{LSVersionNumber=[32C]}{LSVersionNumber=[32C]}IIIIIIIIIIIIICCISI{LSBundleBaseFlags=b1b1b1b1b1b1b1}}IQIIC{LSBundleMoreFlags=b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1}IiI{LSVersionNumber=[32C]}{LSVersionNumber=[32C]}IQQQIIIIIIIIIIQIIQQQQIQQIIIQIQIIQIIIIIIIIIIIIIIIICCCI[1I]II{LSAppClipFields=I}iIIIIIII}12*20ls32l8s40l8r48l8
+ ___block_literal_global.173
+ ___block_literal_global.175
+ ___block_literal_global.210
+ ___block_literal_global.296
+ ___block_literal_global.437
+ ___block_literal_global.448
+ ___block_literal_global.451
+ ___block_literal_global.469
+ ___block_literal_global.527
+ ___block_literal_global.557
+ ___block_literal_global.586
+ ___startRatingRankEligibilityMonitor_block_invoke
+ _dispatch_queue_attr_make_initially_inactive
+ _dispatch_set_target_queue
+ _objc_msgSend$_contextualFeatureUsageDescriptions
+ _objc_msgSend$addContextualUsageDescriptionValuesToLocalizedKeys:fromInfoDictionary:
+ _objc_msgSend$bundlesWithIdentifiers:ratingRankEligibilityChanged:monitor:
+ _objc_msgSend$initWithBundleIdentifier:stateFlags:ratingRank:ratingRankEligibilityDomain:installType:
+ _objc_msgSend$localizedUsageDescriptionForFeature:contextKey:
+ _objc_msgSend$localizedUsageDescriptionForFeature:contextKey:preferredLocalizations:
+ _objc_msgSend$ratingRankEligibilityDomain
+ _os_eligibility_get_domain_notification_name
- -[LSBundleRecord _LSRecord_resolve__localizedIdentityUsageDescription]
- -[LSBundleRecord _LSRecord_resolve__localizedMicrophoneUsageDescription]
- -[LSBundleRecord _localizedIdentityUsageDescriptionWithContext:tableID:unitID:unitBytes:]
- -[LSBundleRecord _localizedIdentityUsageDescription]
- -[LSBundleRecord _localizedMicrophoneUsageDescriptionWithContext:tableID:unitID:unitBytes:]
- -[LSBundleRecord _localizedMicrophoneUsageDescription]
- -[_LSApplicationState addStateFlag:]
- -[_LSApplicationState initWithBundleIdentifier:stateFlags:ratingRank:installType:]
- GCC_except_table156
- GCC_except_table175
- GCC_except_table245
- __OBJC_$_INSTANCE_METHODS_LSApplicationRestrictionsManager
- __OBJC_$_PROP_LIST_LSApplicationRestrictionsManager
- ___Block_byref_object_copy_.619
- ___Block_byref_object_dispose_.620
- ____LSBundleFindWithNode_block_invoke.137
- ____LSBundleRemove_block_invoke.156
- ____LSBundleRemove_block_invoke_2.157
- ___block_descriptor_32_e379_B28?0^{LSContext=}8I16r^{LSBundleData={LSBundleBaseData=IIIIIIi{LSVersionNumber=[32C]}{LSVersionNumber=[32C]}IIIIIIIIIIIIIICCISI{LSBundleBaseFlags=b1b1b1b1b1b1b1}}IQIIC{LSBundleMoreFlags=b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1}IiI{LSVersionNumber=[32C]}{LSVersionNumber=[32C]}IQQQIIIIIIIIIIQIIQQQQIQQIIIQIQIIIIIIIIIIIIIIIIIICCCI[1I]II{LSAppClipFields=I}iIIIIIII}20l
- ___block_descriptor_40_ea8_32s_e379_B28?0"_LSDatabase"8I16r^{LSBundleData={LSBundleBaseData=IIIIIIi{LSVersionNumber=[32C]}{LSVersionNumber=[32C]}IIIIIIIIIIIIIICCISI{LSBundleBaseFlags=b1b1b1b1b1b1b1}}IQIIC{LSBundleMoreFlags=b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1}IiI{LSVersionNumber=[32C]}{LSVersionNumber=[32C]}IQQQIIIIIIIIIIQIIQQQQIQQIIIQIQIIIIIIIIIIIIIIIIIICCCI[1I]II{LSAppClipFields=I}iIIIIIII}20ls32l8
- ___block_descriptor_40_ea8_32s_e379_B28?0^{LSContext=}8I16r^{LSBundleData={LSBundleBaseData=IIIIIIi{LSVersionNumber=[32C]}{LSVersionNumber=[32C]}IIIIIIIIIIIIIICCISI{LSBundleBaseFlags=b1b1b1b1b1b1b1}}IQIIC{LSBundleMoreFlags=b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1}IiI{LSVersionNumber=[32C]}{LSVersionNumber=[32C]}IQQQIIIIIIIIIIQIIQQQQIQQIIIQIQIIIIIIIIIIIIIIIIIICCCI[1I]II{LSAppClipFields=I}iIIIIIII}20ls32l8
- ___block_descriptor_44_e379_B28?0"_LSDatabase"8I16r^{LSBundleData={LSBundleBaseData=IIIIIIi{LSVersionNumber=[32C]}{LSVersionNumber=[32C]}IIIIIIIIIIIIIICCISI{LSBundleBaseFlags=b1b1b1b1b1b1b1}}IQIIC{LSBundleMoreFlags=b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1}IiI{LSVersionNumber=[32C]}{LSVersionNumber=[32C]}IQQQIIIIIIIIIIQIIQQQQIQQIIIQIQIIIIIIIIIIIIIIIIIICCCI[1I]II{LSAppClipFields=I}iIIIIIII}20l
- ___block_descriptor_48_ea8_32bs_e197_v28?0"NSString"8I16r^{LSPluginData={LSBundleBaseData=IIIIIIi{LSVersionNumber=[32C]}{LSVersionNumber=[32C]}IIIIIIIIIIIIIICCISI{LSBundleBaseFlags=b1b1b1b1b1b1b1}}IIIII{LSVersionNumber=[32C]}IIII}20ls32l8
- ___block_descriptor_48_ea8_32bs_e376_v28?0"NSString"8I16r^{LSBundleData={LSBundleBaseData=IIIIIIi{LSVersionNumber=[32C]}{LSVersionNumber=[32C]}IIIIIIIIIIIIIICCISI{LSBundleBaseFlags=b1b1b1b1b1b1b1}}IQIIC{LSBundleMoreFlags=b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1}IiI{LSVersionNumber=[32C]}{LSVersionNumber=[32C]}IQQQIIIIIIIIIIQIIQQQQIQQIIIQIQIIIIIIIIIIIIIIIIIICCCI[1I]II{LSAppClipFields=I}iIIIIIII}20ls32l8
- ___block_descriptor_52_ea8_32s_e366_v28?0I8r^{LSBundleData={LSBundleBaseData=IIIIIIi{LSVersionNumber=[32C]}{LSVersionNumber=[32C]}IIIIIIIIIIIIIICCISI{LSBundleBaseFlags=b1b1b1b1b1b1b1}}IQIIC{LSBundleMoreFlags=b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1}IiI{LSVersionNumber=[32C]}{LSVersionNumber=[32C]}IQQQIIIIIIIIIIQIIQQQQIQQIIIQIQIIIIIIIIIIIIIIIIIICCCI[1I]II{LSAppClipFields=I}iIIIIIII}12*20ls32l8
- ___block_descriptor_56_ea8_32bs40bs_e366_v28?0I8r^{LSBundleData={LSBundleBaseData=IIIIIIi{LSVersionNumber=[32C]}{LSVersionNumber=[32C]}IIIIIIIIIIIIIICCISI{LSBundleBaseFlags=b1b1b1b1b1b1b1}}IQIIC{LSBundleMoreFlags=b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1}IiI{LSVersionNumber=[32C]}{LSVersionNumber=[32C]}IQQQIIIIIIIIIIQIIQQQQIQQIIIQIQIIIIIIIIIIIIIIIIIICCCI[1I]II{LSAppClipFields=I}iIIIIIII}12*20ls32l8s40l8
- ___block_descriptor_56_ea8_32r40r_e366_v28?0I8r^{LSBundleData={LSBundleBaseData=IIIIIIi{LSVersionNumber=[32C]}{LSVersionNumber=[32C]}IIIIIIIIIIIIIICCISI{LSBundleBaseFlags=b1b1b1b1b1b1b1}}IQIIC{LSBundleMoreFlags=b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1}IiI{LSVersionNumber=[32C]}{LSVersionNumber=[32C]}IQQQIIIIIIIIIIQIIQQQQIQQIIIQIQIIIIIIIIIIIIIIIIIICCCI[1I]II{LSAppClipFields=I}iIIIIIII}12*20lr32l8r40l8
- ___block_descriptor_56_ea8_32s40bs_e366_v28?0I8r^{LSBundleData={LSBundleBaseData=IIIIIIi{LSVersionNumber=[32C]}{LSVersionNumber=[32C]}IIIIIIIIIIIIIICCISI{LSBundleBaseFlags=b1b1b1b1b1b1b1}}IQIIC{LSBundleMoreFlags=b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1}IiI{LSVersionNumber=[32C]}{LSVersionNumber=[32C]}IQQQIIIIIIIIIIQIIQQQQIQQIIIQIQIIIIIIIIIIIIIIIIIICCCI[1I]II{LSAppClipFields=I}iIIIIIII}12*20ls32l8s40l8
- ___block_descriptor_608_ea8_32s_e19_v32?0I8r^v12I20*24ls32l8
- ___block_descriptor_608_ea8_32s_e37_v40?0q8"NSString"16"NSString"24*32ls32l8
- ___block_descriptor_72_e8_32bs40r48r_e366_v28?0I8r^{LSBundleData={LSBundleBaseData=IIIIIIi{LSVersionNumber=[32C]}{LSVersionNumber=[32C]}IIIIIIIIIIIIIICCISI{LSBundleBaseFlags=b1b1b1b1b1b1b1}}IQIIC{LSBundleMoreFlags=b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1}IiI{LSVersionNumber=[32C]}{LSVersionNumber=[32C]}IQQQIIIIIIIIIIQIIQQQQIQQIIIQIQIIIIIIIIIIIIIIIIIICCCI[1I]II{LSAppClipFields=I}iIIIIIII}12*20ls32l8r40l8r48l8
- ___block_descriptor_72_ea8_32s40s48r_e366_v28?0I8r^{LSBundleData={LSBundleBaseData=IIIIIIi{LSVersionNumber=[32C]}{LSVersionNumber=[32C]}IIIIIIIIIIIIIICCISI{LSBundleBaseFlags=b1b1b1b1b1b1b1}}IQIIC{LSBundleMoreFlags=b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1}IiI{LSVersionNumber=[32C]}{LSVersionNumber=[32C]}IQQQIIIIIIIIIIQIIQQQQIQQIIIQIQIIIIIIIIIIIIIIIIIICCCI[1I]II{LSAppClipFields=I}iIIIIIII}12*20ls32l8s40l8r48l8
- ___block_literal_global.168
- ___block_literal_global.209
- ___block_literal_global.211
- ___block_literal_global.295
- ___block_literal_global.302
- ___block_literal_global.429
- ___block_literal_global.440
- ___block_literal_global.443
- ___block_literal_global.461
- ___block_literal_global.519
- ___block_literal_global.554
- ___block_literal_global.582
- _objc_msgSend$_localizedIdentityUsageDescription
- _objc_msgSend$_localizedMicrophoneUsageDescription
- _objc_msgSend$initWithBundleIdentifier:stateFlags:ratingRank:installType:
CStrings:
+ "#LSRatingRankEligibilityMonitor Coulnd't get to database in %s: %@"
+ "#LSRatingRankEligibilityMonitor No identifier for bundle unit %llx?"
+ "#LSRatingRankEligibilityMonitor begin monitoring domain %llu"
+ "#LSRatingRankEligibilityMonitor domain %llu already being monitored"
+ "#LSRatingRankEligibilityMonitor monitored domain %llu changed"
+ "+[LSRatingRankEligibilityMonitor sharedServerInstance]"
+ "-[LSRatingRankEligibilityMonitor _queue_domainNotificationFired:]_block_invoke"
+ "-[LSRatingRankEligibilityMonitor dealloc]"
+ "-[LSRatingRankEligibilityMonitor ensureMonitoringDomain:]"
+ "/Library/Caches/com.apple.xbs/Sources/CoreServices/LaunchServices.subprj/Source/LaunchServices/Workspace/LSApplicationState.mm"
+ "@\"<LSRatingRankEligibilityMonitorDelegate>\""
+ "@32@0:8^{LSContext=@}16r^{LSBundleData={LSBundleBaseData=IIIIIIi{LSVersionNumber=[32C]}{LSVersionNumber=[32C]}IIIIIIIIIIIIICCISI{LSBundleBaseFlags=b1b1b1b1b1b1b1}}IQIIC{LSBundleMoreFlags=b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1}IiI{LSVersionNumber=[32C]}{LSVersionNumber=[32C]}IQQQIIIIIIIIIIQIIQQQQIQQIIIQIQIIQIIIIIIIIIIIIIIIICCCI[1I]II{LSAppClipFields=I}iIIIIIII}24"
+ "@36@0:8@16I24r^{LSBundleData={LSBundleBaseData=IIIIIIi{LSVersionNumber=[32C]}{LSVersionNumber=[32C]}IIIIIIIIIIIIICCISI{LSBundleBaseFlags=b1b1b1b1b1b1b1}}IQIIC{LSBundleMoreFlags=b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1}IiI{LSVersionNumber=[32C]}{LSVersionNumber=[32C]}IQQQIIIIIIIIIIQIIQQQQIQQIIIQIQIIQIIIIIIIIIIIIIIIICCCI[1I]II{LSAppClipFields=I}iIIIIIII}28"
+ "@36@0:8^{LSContext=@}16I24r^{LSBundleData={LSBundleBaseData=IIIIIIi{LSVersionNumber=[32C]}{LSVersionNumber=[32C]}IIIIIIIIIIIIICCISI{LSBundleBaseFlags=b1b1b1b1b1b1b1}}IQIIC{LSBundleMoreFlags=b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1}IiI{LSVersionNumber=[32C]}{LSVersionNumber=[32C]}IQQQIIIIIIIIIIQIIQQQQIQQIIIQIQIIQIIIIIIIIIIIIIIIICCCI[1I]II{LSAppClipFields=I}iIIIIIII}28"
+ "@40@0:8Q16@24@32"
+ "@40@0:8^{LSContext=@}16I24I28r^{LSBundleBaseData=IIIIIIi{LSVersionNumber=[32C]}{LSVersionNumber=[32C]}IIIIIIIIIIIIICCISI{LSBundleBaseFlags=b1b1b1b1b1b1b1}}32"
+ "@40@0:8^{LSContext=@}16I24I28r^{LSBundleData={LSBundleBaseData=IIIIIIi{LSVersionNumber=[32C]}{LSVersionNumber=[32C]}IIIIIIIIIIIIICCISI{LSBundleBaseFlags=b1b1b1b1b1b1b1}}IQIIC{LSBundleMoreFlags=b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1}IiI{LSVersionNumber=[32C]}{LSVersionNumber=[32C]}IQQQIIIIIIIIIIQIIQQQQIQQIIIQIQIIQIIIIIIIIIIIIIIIICCCI[1I]II{LSAppClipFields=I}iIIIIIII}32"
+ "@40@0:8^{LSContext=@}16I24I28r^{LSPluginData={LSBundleBaseData=IIIIIIi{LSVersionNumber=[32C]}{LSVersionNumber=[32C]}IIIIIIIIIIIIICCISI{LSBundleBaseFlags=b1b1b1b1b1b1b1}}IIIII{LSVersionNumber=[32C]}IIII}32"
+ "@44@0:8B16^{LSContext=@}20I28I32r^{LSBundleBaseData=IIIIIIi{LSVersionNumber=[32C]}{LSVersionNumber=[32C]}IIIIIIIIIIIIICCISI{LSBundleBaseFlags=b1b1b1b1b1b1b1}}36"
+ "@44@0:8B16^{LSContext=@}20I28I32r^{LSBundleData={LSBundleBaseData=IIIIIIi{LSVersionNumber=[32C]}{LSVersionNumber=[32C]}IIIIIIIIIIIIICCISI{LSBundleBaseFlags=b1b1b1b1b1b1b1}}IQIIC{LSBundleMoreFlags=b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1}IiI{LSVersionNumber=[32C]}{LSVersionNumber=[32C]}IQQQIIIIIIIIIIQIIQQQQIQQIIIQIQIIQIIIIIIIIIIIIIIIICCCI[1I]II{LSAppClipFields=I}iIIIIIII}36"
+ "@44@0:8I16r^{LSBundleData={LSBundleBaseData=IIIIIIi{LSVersionNumber=[32C]}{LSVersionNumber=[32C]}IIIIIIIIIIIIICCISI{LSBundleBaseFlags=b1b1b1b1b1b1b1}}IQIIC{LSBundleMoreFlags=b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1}IiI{LSVersionNumber=[32C]}{LSVersionNumber=[32C]}IQQQIIIIIIIIIIQIIQQQQIQQIIIQIQIIQIIIIIIIIIIIIIIIICCCI[1I]II{LSAppClipFields=I}iIIIIIII}20@28^@36"
+ "@44@0:8^{LSContext=@}16I24r^{LSBundleData={LSBundleBaseData=IIIIIIi{LSVersionNumber=[32C]}{LSVersionNumber=[32C]}IIIIIIIIIIIIICCISI{LSBundleBaseFlags=b1b1b1b1b1b1b1}}IQIIC{LSBundleMoreFlags=b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1}IiI{LSVersionNumber=[32C]}{LSVersionNumber=[32C]}IQQQIIIIIIIIIIQIIQQQQIQQIIIQIQIIQIIIIIIIIIIIIIIIICCCI[1I]II{LSAppClipFields=I}iIIIIIII}28^@36"
+ "@44@0:8^{LSContext=@}16I24r^{LSPluginData={LSBundleBaseData=IIIIIIi{LSVersionNumber=[32C]}{LSVersionNumber=[32C]}IIIIIIIIIIIIICCISI{LSBundleBaseFlags=b1b1b1b1b1b1b1}}IIIII{LSVersionNumber=[32C]}IIII}28^@36"
+ "@52@0:8@16Q24i32Q36Q44"
+ "@52@0:8^{LSContext=@}16I24r^{LSPluginData={LSBundleBaseData=IIIIIIi{LSVersionNumber=[32C]}{LSVersionNumber=[32C]}IIIIIIIIIIIIICCISI{LSBundleBaseFlags=b1b1b1b1b1b1b1}}IIIII{LSVersionNumber=[32C]}IIII}28@36^@44"
+ "@64@0:8@16@24^{LSContext=@}32I40I44r^{LSBundleBaseData=IIIIIIi{LSVersionNumber=[32C]}{LSVersionNumber=[32C]}IIIIIIIIIIIIICCISI{LSBundleBaseFlags=b1b1b1b1b1b1b1}}48^@56"
+ "A"
+ "B28@?0@\"_LSDatabase\"8I16r^{LSBundleData={LSBundleBaseData=IIIIIIi{LSVersionNumber=[32C]}{LSVersionNumber=[32C]}IIIIIIIIIIIIICCISI{LSBundleBaseFlags=b1b1b1b1b1b1b1}}IQIIC{LSBundleMoreFlags=b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1}IiI{LSVersionNumber=[32C]}{LSVersionNumber=[32C]}IQQQIIIIIIIIIIQIIQQQQIQQIIIQIQIIQIIIIIIIIIIIIIIIICCCI[1I]II{LSAppClipFields=I}iIIIIIII}20"
+ "B28@?0^{LSContext=@}8I16r^{LSBundleData={LSBundleBaseData=IIIIIIi{LSVersionNumber=[32C]}{LSVersionNumber=[32C]}IIIIIIIIIIIIICCISI{LSBundleBaseFlags=b1b1b1b1b1b1b1}}IQIIC{LSBundleMoreFlags=b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1}IiI{LSVersionNumber=[32C]}{LSVersionNumber=[32C]}IQQQIIIIIIIIIIQIIQQQQIQQIIIQIQIIQIIIIIIIIIIIIIIIICCCI[1I]II{LSAppClipFields=I}iIIIIIII}20"
+ "B32@0:8Q16@24"
+ "B36@0:8I16r^{LSBundleData={LSBundleBaseData=IIIIIIi{LSVersionNumber=[32C]}{LSVersionNumber=[32C]}IIIIIIIIIIIIICCISI{LSBundleBaseFlags=b1b1b1b1b1b1b1}}IQIIC{LSBundleMoreFlags=b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1}IiI{LSVersionNumber=[32C]}{LSVersionNumber=[32C]}IQQQIIIIIIIIIIQIIQQQQIQQIIIQIQIIQIIIIIIIIIIIIIIIICCCI[1I]II{LSAppClipFields=I}iIIIIIII}20^{LSContext=@}28"
+ "B36@0:8I16r^{LSPluginData={LSBundleBaseData=IIIIIIi{LSVersionNumber=[32C]}{LSVersionNumber=[32C]}IIIIIIIIIIIIICCISI{LSBundleBaseFlags=b1b1b1b1b1b1b1}}IIIII{LSVersionNumber=[32C]}IIII}20@28"
+ "B36@0:8^{LSContext=@}16I24r^{LSBundleData={LSBundleBaseData=IIIIIIi{LSVersionNumber=[32C]}{LSVersionNumber=[32C]}IIIIIIIIIIIIICCISI{LSBundleBaseFlags=b1b1b1b1b1b1b1}}IQIIC{LSBundleMoreFlags=b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1}IiI{LSVersionNumber=[32C]}{LSVersionNumber=[32C]}IQQQIIIIIIIIIIQIIQQQQIQQIIIQIQIIQIIIIIIIIIIIIIIIICCCI[1I]II{LSAppClipFields=I}iIIIIIII}28"
+ "B40@0:8I16r^{LSPluginData={LSBundleBaseData=IIIIIIi{LSVersionNumber=[32C]}{LSVersionNumber=[32C]}IIIIIIIIIIIIICCISI{LSBundleBaseFlags=b1b1b1b1b1b1b1}}IIIII{LSVersionNumber=[32C]}IIII}20I28^{LSContext=@}32"
+ "B40@0:8^{LSContext=@}16I24I28r^{LSBundleData={LSBundleBaseData=IIIIIIi{LSVersionNumber=[32C]}{LSVersionNumber=[32C]}IIIIIIIIIIIIICCISI{LSBundleBaseFlags=b1b1b1b1b1b1b1}}IQIIC{LSBundleMoreFlags=b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1}IiI{LSVersionNumber=[32C]}{LSVersionNumber=[32C]}IQQQIIIIIIIIIIQIIQQQQIQQIIIQIQIIQIIIIIIIIIIIIIIIICCCI[1I]II{LSAppClipFields=I}iIIIIIII}32"
+ "B52@0:8I16r^{LSBundleData={LSBundleBaseData=IIIIIIi{LSVersionNumber=[32C]}{LSVersionNumber=[32C]}IIIIIIIIIIIIICCISI{LSBundleBaseFlags=b1b1b1b1b1b1b1}}IQIIC{LSBundleMoreFlags=b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1}IiI{LSVersionNumber=[32C]}{LSVersionNumber=[32C]}IQQQIIIIIIIIIIQIIQQQQIQQIIIQIQIIQIIIIIIIIIIIIIIIICCCI[1I]II{LSAppClipFields=I}iIIIIIII}20^{LSContext=@}28@36^@44"
+ "B60@0:8^@16^@24I32r^{LSBundleData={LSBundleBaseData=IIIIIIi{LSVersionNumber=[32C]}{LSVersionNumber=[32C]}IIIIIIIIIIIIICCISI{LSBundleBaseFlags=b1b1b1b1b1b1b1}}IQIIC{LSBundleMoreFlags=b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1}IiI{LSVersionNumber=[32C]}{LSVersionNumber=[32C]}IQQQIIIIIIIIIIQIIQQQQIQQIIIQIQIIQIIIIIIIIIIIIIIIICCCI[1I]II{LSAppClipFields=I}iIIIIIII}36@44^@52"
+ "C40@0:8^{LSContext=@}16I24I28r^{LSBundleBaseData=IIIIIIi{LSVersionNumber=[32C]}{LSVersionNumber=[32C]}IIIIIIIIIIIIICCISI{LSBundleBaseFlags=b1b1b1b1b1b1b1}}32"
+ "C40@0:8^{LSContext=@}16I24I28r^{LSBundleData={LSBundleBaseData=IIIIIIi{LSVersionNumber=[32C]}{LSVersionNumber=[32C]}IIIIIIIIIIIIICCISI{LSBundleBaseFlags=b1b1b1b1b1b1b1}}IQIIC{LSBundleMoreFlags=b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1}IiI{LSVersionNumber=[32C]}{LSVersionNumber=[32C]}IQQQIIIIIIIIIIQIIQQQQIQQIIIQIQIIQIIIIIIIIIIIIIIIICCCI[1I]II{LSAppClipFields=I}iIIIIIII}32"
+ "I40@0:8^{LSContext=@}16I24I28r^{LSBundleBaseData=IIIIIIi{LSVersionNumber=[32C]}{LSVersionNumber=[32C]}IIIIIIIIIIIIICCISI{LSBundleBaseFlags=b1b1b1b1b1b1b1}}32"
+ "I40@0:8^{LSContext=@}16I24I28r^{LSBundleData={LSBundleBaseData=IIIIIIi{LSVersionNumber=[32C]}{LSVersionNumber=[32C]}IIIIIIIIIIIIICCISI{LSBundleBaseFlags=b1b1b1b1b1b1b1}}IQIIC{LSBundleMoreFlags=b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1}IiI{LSVersionNumber=[32C]}{LSVersionNumber=[32C]}IQQQIIIIIIIIIIQIIQQQQIQQIIIQIQIIQIIIIIIIIIIIIIIIICCCI[1I]II{LSAppClipFields=I}iIIIIIII}32"
+ "I40@0:8^{LSContext=@}16I24I28r^{LSPluginData={LSBundleBaseData=IIIIIIi{LSVersionNumber=[32C]}{LSVersionNumber=[32C]}IIIIIIIIIIIIICCISI{LSBundleBaseFlags=b1b1b1b1b1b1b1}}IIIII{LSVersionNumber=[32C]}IIII}32"
+ "IdentityUsage"
+ "IdentityUsage."
+ "LSDefaultAppCategoryInvalidPlaceholder2"
+ "LSRatingRankEligibilityMonitor"
+ "LSRatingRankEligibilityMonitor.mm"
+ "LSRatingRankEligibilityMonitorDelegate"
+ "MicUsage"
+ "NSIdentityUsageDescriptionDictionary"
+ "Q40@0:8^{LSContext=@}16I24I28r^{LSBundleData={LSBundleBaseData=IIIIIIi{LSVersionNumber=[32C]}{LSVersionNumber=[32C]}IIIIIIIIIIIIICCISI{LSBundleBaseFlags=b1b1b1b1b1b1b1}}IQIIC{LSBundleMoreFlags=b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1}IiI{LSVersionNumber=[32C]}{LSVersionNumber=[32C]}IQQQIIIIIIIIIIQIIQQQQIQQIIIQIQIIQIIIIIIIIIIIIIIIICCCI[1I]II{LSAppClipFields=I}iIIIIIII}32"
+ "RatingRankEligibilityDomain"
+ "RatingRankMonitorDelegate"
+ "T@\"NSNumber\",R,N,V_ratingRankEligibilityDomain"
+ "Unsetting redactable for unit %llx"
+ "_LSRecord_resolve__contextualFeatureUsageDescriptions"
+ "_activeTokens"
+ "_contextualFeatureUsageDescriptions"
+ "_contextualFeatureUsageDescriptionsWithContext:tableID:unitID:unitBytes:"
+ "_contextualIdentityUsageDescriptions"
+ "_localizedContextualIdentityUsageDescriptions"
+ "_ratingRankEligibilityDomain"
+ "addContextualUsageDescriptionValuesToLocalizedKeys:fromInfoDictionary:"
+ "bundles for domain %llu changed: %@"
+ "bundlesWithIdentifiers:ratingRankEligibilityChanged:monitor:"
+ "c40@0:8^{LSContext=@}16I24I28r^{LSBundleData={LSBundleBaseData=IIIIIIi{LSVersionNumber=[32C]}{LSVersionNumber=[32C]}IIIIIIIIIIIIICCISI{LSBundleBaseFlags=b1b1b1b1b1b1b1}}IQIIC{LSBundleMoreFlags=b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1}IiI{LSVersionNumber=[32C]}{LSVersionNumber=[32C]}IQQQIIIIIIIIIIQIIQQQQIQQIIIQIQIIQIIIIIIIIIIIIIIIICCCI[1I]II{LSAppClipFields=I}iIIIIIII}32"
+ "com.apple.default-app.inactivecategory2"
+ "com.apple.launchservices.LSRatingRankEligibilityMonitor"
+ "couldn't create dictionary for contextual usage descriptions: %@"
+ "deallocating resumed but uninvalidated monitor"
+ "ensure monitoring for invalidated monitor"
+ "force_safari_rating_rank"
+ "hasLocalizedUsageDescriptionForFeature:contextKey:"
+ "i32@0:8@16^{LSBundleData={LSBundleBaseData=IIIIIIi{LSVersionNumber=[32C]}{LSVersionNumber=[32C]}IIIIIIIIIIIIICCISI{LSBundleBaseFlags=b1b1b1b1b1b1b1}}IQIIC{LSBundleMoreFlags=b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1}IiI{LSVersionNumber=[32C]}{LSVersionNumber=[32C]}IQQQIIIIIIIIIIQIIQQQQIQQIIIQIQIIQIIIIIIIIIIIIIIIICCCI[1I]II{LSAppClipFields=I}iIIIIIII}24"
+ "i36@0:8@16I24r^{LSBundleData={LSBundleBaseData=IIIIIIi{LSVersionNumber=[32C]}{LSVersionNumber=[32C]}IIIIIIIIIIIIICCISI{LSBundleBaseFlags=b1b1b1b1b1b1b1}}IQIIC{LSBundleMoreFlags=b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1}IiI{LSVersionNumber=[32C]}{LSVersionNumber=[32C]}IQQQIIIIIIIIIIQIIQQQQIQQIIIQIQIIQIIIIIIIIIIIIIIIICCCI[1I]II{LSAppClipFields=I}iIIIIIII}28"
+ "i40@0:8^{LSContext=@}16I24I28r^{LSBundleData={LSBundleBaseData=IIIIIIi{LSVersionNumber=[32C]}{LSVersionNumber=[32C]}IIIIIIIIIIIIICCISI{LSBundleBaseFlags=b1b1b1b1b1b1b1}}IQIIC{LSBundleMoreFlags=b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1}IiI{LSVersionNumber=[32C]}{LSVersionNumber=[32C]}IQQQIIIIIIIIIIQIIQQQQIQQIIIQIQIIQIIIIIIIIIIIIIIIICCCI[1I]II{LSAppClipFields=I}iIIIIIII}32"
+ "initWithBundleIdentifier:stateFlags:ratingRank:ratingRankEligibilityDomain:installType:"
+ "localizedUsageDescriptionForFeature:contextKey:"
+ "localizedUsageDescriptionForFeature:contextKey:preferredLocalizations:"
+ "r^{LSPluginData={LSBundleBaseData=IIIIIIi{LSVersionNumber=[32C]}{LSVersionNumber=[32C]}IIIIIIIIIIIIICCISI{LSBundleBaseFlags=b1b1b1b1b1b1b1}}IIIII{LSVersionNumber=[32C]}IIII}20@0:8I16"
+ "ratingRankEligibilityDomain"
+ "redactable"
+ "v28@?0@\"NSString\"8I16r^{LSBundleData={LSBundleBaseData=IIIIIIi{LSVersionNumber=[32C]}{LSVersionNumber=[32C]}IIIIIIIIIIIIICCISI{LSBundleBaseFlags=b1b1b1b1b1b1b1}}IQIIC{LSBundleMoreFlags=b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1}IiI{LSVersionNumber=[32C]}{LSVersionNumber=[32C]}IQQQIIIIIIIIIIQIIQQQQIQQIIIQIQIIQIIIIIIIIIIIIIIIICCCI[1I]II{LSAppClipFields=I}iIIIIIII}20"
+ "v28@?0@\"NSString\"8I16r^{LSPluginData={LSBundleBaseData=IIIIIIi{LSVersionNumber=[32C]}{LSVersionNumber=[32C]}IIIIIIIIIIIIICCISI{LSBundleBaseFlags=b1b1b1b1b1b1b1}}IIIII{LSVersionNumber=[32C]}IIII}20"
+ "v28@?0I8r^{LSBundleData={LSBundleBaseData=IIIIIIi{LSVersionNumber=[32C]}{LSVersionNumber=[32C]}IIIIIIIIIIIIICCISI{LSBundleBaseFlags=b1b1b1b1b1b1b1}}IQIIC{LSBundleMoreFlags=b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1}IiI{LSVersionNumber=[32C]}{LSVersionNumber=[32C]}IQQQIIIIIIIIIIQIIQQQQIQQIIIQIQIIQIIIIIIIIIIIIIIIICCCI[1I]II{LSAppClipFields=I}iIIIIIII}12*20"
+ "v36@0:8^{LSContext=@}16I24r^{LSBundleData={LSBundleBaseData=IIIIIIi{LSVersionNumber=[32C]}{LSVersionNumber=[32C]}IIIIIIIIIIIIICCISI{LSBundleBaseFlags=b1b1b1b1b1b1b1}}IQIIC{LSBundleMoreFlags=b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1}IiI{LSVersionNumber=[32C]}{LSVersionNumber=[32C]}IQQQIIIIIIIIIIQIIQQQQIQQIIIQIQIIQIIIIIIIIIIIIIIIICCCI[1I]II{LSAppClipFields=I}iIIIIIII}28"
+ "v40@0:8@\"NSSet\"16Q24@\"LSRatingRankEligibilityMonitor\"32"
+ "v40@0:8@16Q24@32"
+ "{?=\"wasResumed\"b1\"wasInvalidated\"b1}"
+ "{LSBundleBaseFlags=\"appleInternal\"b1\"requiresObjCGarbageCollection\"b1\"builtWithTSan\"b1\"isLinkEnabled\"b1\"isSecuredSystemContent\"b1\"redactable\"b1\"_reserved\"b1}"
+ "{LSBundleBaseFlags=b1b1b1b1b1b1b1}40@0:8^{LSContext=@}16I24I28r^{LSBundleBaseData=IIIIIIi{LSVersionNumber=[32C]}{LSVersionNumber=[32C]}IIIIIIIIIIIIICCISI{LSBundleBaseFlags=b1b1b1b1b1b1b1}}32"
+ "{LSBundleData=\"base\"{LSBundleBaseData=\"bookmark\"I\"container\"I\"execPath\"I\"exactIdentifier\"I\"teamID\"I\"platform\"I\"registrationTime\"i\"version\"{LSVersionNumber=\"_opaque\"[32C]}\"execSDKVersion\"{LSVersionNumber=\"_opaque\"[32C]}\"machOUUIDs\"I\"dataContainerAlias\"I\"bundleName\"I\"localizedShortDisplayName\"I\"displayName\"I\"localizedDisplayName\"I\"contextualUsageDescriptions\"I\"codeInfoIdentifier\"I\"signerOrganization\"I\"signerIdentity\"I\"infoDictionary\"I\"entitlements\"I\"groupContainers\"I\"containingDirectoryClass\"C\"profileValidationState\"C\"intentDefinitionURLs\"I\"_sliceMask\"S\"signatureVersion\"I\"flags\"{LSBundleBaseFlags=\"appleInternal\"b1\"requiresObjCGarbageCollection\"b1\"builtWithTSan\"b1\"isLinkEnabled\"b1\"isSecuredSystemContent\"b1\"redactable\"b1\"_reserved\"b1}}\"_clas\"I\"_bundleFlags\"Q\"_plistContentFlags\"I\"_itemFlags\"I\"_iconFlags\"C\"moreFlags\"{LSBundleMoreFlags=\"isWebBrowser\"b1\"isMailClient\"b1\"supportsControllerUserInteraction\"b1\"supportsSpotlightQueryContinuation\"b1\"supportsSpotlightActions\"b1\"isCodeSigningInfoNotAuthoritative\"b1\"applicationQueriesSchemesTooBig\"b1\"isUpdateAvailable\"b1\"isPlaygroundsApp\"b1\"supportsAlwaysOnDisplay\"b1\"defaultsToPrivateAlwaysOnDisplayTreatment\"b1\"supportsLiveActivities\"b1\"supportsLiveActivitiesFrequentUpdates\"b1\"requiresPostprocessing\"b1\"hasShellRole\"b1\"requiresSecureLaunch\"b1\"eligibleForWatchAppInstall\"b1\"isEligibilityCheckedBrowser\"b1\"isEligibilityCheckedBrowserEngineEmbedder\"b1\"isManagedAppDistributor\"b1\"isHiddenByAppProtection\"b1\"isLockedByAppProtection\"b1\"supportsDataExport\"b1\"hasSupportsGameModeKey\"b1\"supportsGameMode\"b1\"isOnCryptex\"b1}\"_hfsType\"I\"_mtime\"i\"minSystemVersionPlatform\"I\"_minSystemVersion\"{LSVersionNumber=\"_opaque\"[32C]}\"_maxSystemVersion\"{LSVersionNumber=\"_opaque\"[32C]}\"appStoreToolsBuildVersion\"I\"sequenceNumber\"Q\"compatibilityState\"Q\"itemID\"Q\"deviceFamilies\"I\"identifier\"I\"counterpartIdentifiers\"I\"equivalentBundleIdentifiers\"I\"categoryType\"I\"secondaryCategoryType\"I\"filename\"I\"bundleVersion\"I\"shortVersionString\"I\"installType\"I\"installFailureReason\"Q\"vendorName\"I\"appType\"I\"staticDiskUsage\"Q\"purchaserDSID\"Q\"downloaderDSID\"Q\"familyID\"Q\"itemName\"I\"storefront\"Q\"versionIdentifier\"Q\"sourceAppBundleID\"I\"appVariant\"I\"managementDeclarationIdentifier\"I\"ratingRank\"Q\"ratingLabel\"I\"genreID\"Q\"genre\"I\"distributorInfo\"I\"ratingRankEligibilityDomain\"Q\"primaryIconName\"I\"alternatePrimaryIconName\"I\"iconsDict\"I\"iconFileNames\"I\"libraryPath\"I\"libraryItems\"I\"claims\"I\"types\"I\"plugins\"I\"driverExtensions\"I\"extensionPoints\"I\"activityTypes\"I\"queriableSchemes\"I\"bgPermittedIDs\"I\"carPlayInstrumentClusterURLSchemes\"I\"appContainerAlias\"I\"revision\"C\"retries\"C\"_reserved4\"C\"sandboxEnvironmentVariables\"I\"localizedNameWithContext\"[1I]\"bundlePersonas\"I\"bundlePersonaTypes\"I\"appClipFields\"{LSAppClipFields=\"parentAppIDs\"I}\"recordModificationTime\"i\"supportedGameControllers\"I\"mobileInstallIDs\"I\"applicationManagementDomain\"I\"stashedAppDict\"I\"linkedParentBundleIdentifier\"I\"serializedPlaceholderPath\"I\"_reserved5\"I}"
+ "{LSBundleData={LSBundleBaseData=IIIIIIi{LSVersionNumber=[32C]}{LSVersionNumber=[32C]}IIIIIIIIIIIIICCISI{LSBundleBaseFlags=b1b1b1b1b1b1b1}}IQIIC{LSBundleMoreFlags=b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1}IiI{LSVersionNumber=[32C]}{LSVersionNumber=[32C]}IQQQIIIIIIIIIIQIIQQQQIQQIIIQIQIIQIIIIIIIIIIIIIIIICCCI[1I]II{LSAppClipFields=I}iIIIIIII}32@0:8@16^@24"
+ "{LSBundleMoreFlags=b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1}40@0:8^{LSContext=@}16I24I28r^{LSBundleData={LSBundleBaseData=IIIIIIi{LSVersionNumber=[32C]}{LSVersionNumber=[32C]}IIIIIIIIIIIIICCISI{LSBundleBaseFlags=b1b1b1b1b1b1b1}}IQIIC{LSBundleMoreFlags=b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1}IiI{LSVersionNumber=[32C]}{LSVersionNumber=[32C]}IQQQIIIIIIIIIIQIIQQQQIQQIIIQIQIIQIIIIIIIIIIIIIIIICCCI[1I]II{LSAppClipFields=I}iIIIIIII}32"
+ "{LSVersionNumber=[32C]}40@0:8^{LSContext=@}16I24I28r^{LSBundleBaseData=IIIIIIi{LSVersionNumber=[32C]}{LSVersionNumber=[32C]}IIIIIIIIIIIIICCISI{LSBundleBaseFlags=b1b1b1b1b1b1b1}}32"
+ "{expected<LSApplicationRecord *, NSError *>={__conditional_no_unique_address<true, std::__expected_base<LSApplicationRecord *, NSError *>::__repr>={__repr={__conditional_no_unique_address<false, std::__expected_base<LSApplicationRecord *, NSError *>::__union_t>=(__union_t=@@)}B}}}36@0:8^{LSContext=@}16I24r^{LSBundleData={LSBundleBaseData=IIIIIIi{LSVersionNumber=[32C]}{LSVersionNumber=[32C]}IIIIIIIIIIIIICCISI{LSBundleBaseFlags=b1b1b1b1b1b1b1}}IQIIC{LSBundleMoreFlags=b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1}IiI{LSVersionNumber=[32C]}{LSVersionNumber=[32C]}IQQQIIIIIIIIIIQIIQQQQIQQIIIQIQIIQIIIIIIIIIIIIIIIICCCI[1I]II{LSAppClipFields=I}iIIIIIII}28"
+ "{map<os_eligibility_domain_t, LaunchServices::NotifyToken, std::less<os_eligibility_domain_t>, std::allocator<std::pair<const os_eligibility_domain_t, LaunchServices::NotifyToken>>>=\"__tree_\"{__tree<std::__value_type<os_eligibility_domain_t, LaunchServices::NotifyToken>, std::__map_value_compare<os_eligibility_domain_t, std::__value_type<os_eligibility_domain_t, LaunchServices::NotifyToken>, std::less<os_eligibility_domain_t>>, std::allocator<std::__value_type<os_eligibility_domain_t, LaunchServices::NotifyToken>>>=\"__begin_node_\"^v\"__end_node_\"{__tree_end_node<std::__tree_node_base<void *> *>=\"__left_\"^v}\"__size_\"Q}}"
- "/Library/Caches/com.apple.xbs/Sources/CoreServices/LaunchServices.subprj/Source/LaunchServices/Workspace/LSApplicationState.m"
- "@32@0:8^{LSContext=@}16r^{LSBundleData={LSBundleBaseData=IIIIIIi{LSVersionNumber=[32C]}{LSVersionNumber=[32C]}IIIIIIIIIIIIIICCISI{LSBundleBaseFlags=b1b1b1b1b1b1b1}}IQIIC{LSBundleMoreFlags=b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1}IiI{LSVersionNumber=[32C]}{LSVersionNumber=[32C]}IQQQIIIIIIIIIIQIIQQQQIQQIIIQIQIIIIIIIIIIIIIIIIIICCCI[1I]II{LSAppClipFields=I}iIIIIIII}24"
- "@36@0:8@16I24r^{LSBundleData={LSBundleBaseData=IIIIIIi{LSVersionNumber=[32C]}{LSVersionNumber=[32C]}IIIIIIIIIIIIIICCISI{LSBundleBaseFlags=b1b1b1b1b1b1b1}}IQIIC{LSBundleMoreFlags=b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1}IiI{LSVersionNumber=[32C]}{LSVersionNumber=[32C]}IQQQIIIIIIIIIIQIIQQQQIQQIIIQIQIIIIIIIIIIIIIIIIIICCCI[1I]II{LSAppClipFields=I}iIIIIIII}28"
- "@36@0:8^{LSContext=@}16I24r^{LSBundleData={LSBundleBaseData=IIIIIIi{LSVersionNumber=[32C]}{LSVersionNumber=[32C]}IIIIIIIIIIIIIICCISI{LSBundleBaseFlags=b1b1b1b1b1b1b1}}IQIIC{LSBundleMoreFlags=b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1}IiI{LSVersionNumber=[32C]}{LSVersionNumber=[32C]}IQQQIIIIIIIIIIQIIQQQQIQQIIIQIQIIIIIIIIIIIIIIIIIICCCI[1I]II{LSAppClipFields=I}iIIIIIII}28"
- "@40@0:8^{LSContext=@}16I24I28r^{LSBundleBaseData=IIIIIIi{LSVersionNumber=[32C]}{LSVersionNumber=[32C]}IIIIIIIIIIIIIICCISI{LSBundleBaseFlags=b1b1b1b1b1b1b1}}32"
- "@40@0:8^{LSContext=@}16I24I28r^{LSBundleData={LSBundleBaseData=IIIIIIi{LSVersionNumber=[32C]}{LSVersionNumber=[32C]}IIIIIIIIIIIIIICCISI{LSBundleBaseFlags=b1b1b1b1b1b1b1}}IQIIC{LSBundleMoreFlags=b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1}IiI{LSVersionNumber=[32C]}{LSVersionNumber=[32C]}IQQQIIIIIIIIIIQIIQQQQIQQIIIQIQIIIIIIIIIIIIIIIIIICCCI[1I]II{LSAppClipFields=I}iIIIIIII}32"
- "@40@0:8^{LSContext=@}16I24I28r^{LSPluginData={LSBundleBaseData=IIIIIIi{LSVersionNumber=[32C]}{LSVersionNumber=[32C]}IIIIIIIIIIIIIICCISI{LSBundleBaseFlags=b1b1b1b1b1b1b1}}IIIII{LSVersionNumber=[32C]}IIII}32"
- "@44@0:8@16Q24i32Q36"
- "@44@0:8B16^{LSContext=@}20I28I32r^{LSBundleBaseData=IIIIIIi{LSVersionNumber=[32C]}{LSVersionNumber=[32C]}IIIIIIIIIIIIIICCISI{LSBundleBaseFlags=b1b1b1b1b1b1b1}}36"
- "@44@0:8B16^{LSContext=@}20I28I32r^{LSBundleData={LSBundleBaseData=IIIIIIi{LSVersionNumber=[32C]}{LSVersionNumber=[32C]}IIIIIIIIIIIIIICCISI{LSBundleBaseFlags=b1b1b1b1b1b1b1}}IQIIC{LSBundleMoreFlags=b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1}IiI{LSVersionNumber=[32C]}{LSVersionNumber=[32C]}IQQQIIIIIIIIIIQIIQQQQIQQIIIQIQIIIIIIIIIIIIIIIIIICCCI[1I]II{LSAppClipFields=I}iIIIIIII}36"
- "@44@0:8I16r^{LSBundleData={LSBundleBaseData=IIIIIIi{LSVersionNumber=[32C]}{LSVersionNumber=[32C]}IIIIIIIIIIIIIICCISI{LSBundleBaseFlags=b1b1b1b1b1b1b1}}IQIIC{LSBundleMoreFlags=b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1}IiI{LSVersionNumber=[32C]}{LSVersionNumber=[32C]}IQQQIIIIIIIIIIQIIQQQQIQQIIIQIQIIIIIIIIIIIIIIIIIICCCI[1I]II{LSAppClipFields=I}iIIIIIII}20@28^@36"
- "@44@0:8^{LSContext=@}16I24r^{LSBundleData={LSBundleBaseData=IIIIIIi{LSVersionNumber=[32C]}{LSVersionNumber=[32C]}IIIIIIIIIIIIIICCISI{LSBundleBaseFlags=b1b1b1b1b1b1b1}}IQIIC{LSBundleMoreFlags=b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1}IiI{LSVersionNumber=[32C]}{LSVersionNumber=[32C]}IQQQIIIIIIIIIIQIIQQQQIQQIIIQIQIIIIIIIIIIIIIIIIIICCCI[1I]II{LSAppClipFields=I}iIIIIIII}28^@36"
- "@44@0:8^{LSContext=@}16I24r^{LSPluginData={LSBundleBaseData=IIIIIIi{LSVersionNumber=[32C]}{LSVersionNumber=[32C]}IIIIIIIIIIIIIICCISI{LSBundleBaseFlags=b1b1b1b1b1b1b1}}IIIII{LSVersionNumber=[32C]}IIII}28^@36"
- "@52@0:8^{LSContext=@}16I24r^{LSPluginData={LSBundleBaseData=IIIIIIi{LSVersionNumber=[32C]}{LSVersionNumber=[32C]}IIIIIIIIIIIIIICCISI{LSBundleBaseFlags=b1b1b1b1b1b1b1}}IIIII{LSVersionNumber=[32C]}IIII}28@36^@44"
- "@64@0:8@16@24^{LSContext=@}32I40I44r^{LSBundleBaseData=IIIIIIi{LSVersionNumber=[32C]}{LSVersionNumber=[32C]}IIIIIIIIIIIIIICCISI{LSBundleBaseFlags=b1b1b1b1b1b1b1}}48^@56"
- "B28@?0@\"_LSDatabase\"8I16r^{LSBundleData={LSBundleBaseData=IIIIIIi{LSVersionNumber=[32C]}{LSVersionNumber=[32C]}IIIIIIIIIIIIIICCISI{LSBundleBaseFlags=b1b1b1b1b1b1b1}}IQIIC{LSBundleMoreFlags=b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1}IiI{LSVersionNumber=[32C]}{LSVersionNumber=[32C]}IQQQIIIIIIIIIIQIIQQQQIQQIIIQIQIIIIIIIIIIIIIIIIIICCCI[1I]II{LSAppClipFields=I}iIIIIIII}20"
- "B28@?0^{LSContext=@}8I16r^{LSBundleData={LSBundleBaseData=IIIIIIi{LSVersionNumber=[32C]}{LSVersionNumber=[32C]}IIIIIIIIIIIIIICCISI{LSBundleBaseFlags=b1b1b1b1b1b1b1}}IQIIC{LSBundleMoreFlags=b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1}IiI{LSVersionNumber=[32C]}{LSVersionNumber=[32C]}IQQQIIIIIIIIIIQIIQQQQIQQIIIQIQIIIIIIIIIIIIIIIIIICCCI[1I]II{LSAppClipFields=I}iIIIIIII}20"
- "B36@0:8I16r^{LSBundleData={LSBundleBaseData=IIIIIIi{LSVersionNumber=[32C]}{LSVersionNumber=[32C]}IIIIIIIIIIIIIICCISI{LSBundleBaseFlags=b1b1b1b1b1b1b1}}IQIIC{LSBundleMoreFlags=b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1}IiI{LSVersionNumber=[32C]}{LSVersionNumber=[32C]}IQQQIIIIIIIIIIQIIQQQQIQQIIIQIQIIIIIIIIIIIIIIIIIICCCI[1I]II{LSAppClipFields=I}iIIIIIII}20^{LSContext=@}28"
- "B36@0:8I16r^{LSPluginData={LSBundleBaseData=IIIIIIi{LSVersionNumber=[32C]}{LSVersionNumber=[32C]}IIIIIIIIIIIIIICCISI{LSBundleBaseFlags=b1b1b1b1b1b1b1}}IIIII{LSVersionNumber=[32C]}IIII}20@28"
- "B36@0:8^{LSContext=@}16I24r^{LSBundleData={LSBundleBaseData=IIIIIIi{LSVersionNumber=[32C]}{LSVersionNumber=[32C]}IIIIIIIIIIIIIICCISI{LSBundleBaseFlags=b1b1b1b1b1b1b1}}IQIIC{LSBundleMoreFlags=b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1}IiI{LSVersionNumber=[32C]}{LSVersionNumber=[32C]}IQQQIIIIIIIIIIQIIQQQQIQQIIIQIQIIIIIIIIIIIIIIIIIICCCI[1I]II{LSAppClipFields=I}iIIIIIII}28"
- "B40@0:8I16r^{LSPluginData={LSBundleBaseData=IIIIIIi{LSVersionNumber=[32C]}{LSVersionNumber=[32C]}IIIIIIIIIIIIIICCISI{LSBundleBaseFlags=b1b1b1b1b1b1b1}}IIIII{LSVersionNumber=[32C]}IIII}20I28^{LSContext=@}32"
- "B40@0:8^{LSContext=@}16I24I28r^{LSBundleData={LSBundleBaseData=IIIIIIi{LSVersionNumber=[32C]}{LSVersionNumber=[32C]}IIIIIIIIIIIIIICCISI{LSBundleBaseFlags=b1b1b1b1b1b1b1}}IQIIC{LSBundleMoreFlags=b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1}IiI{LSVersionNumber=[32C]}{LSVersionNumber=[32C]}IQQQIIIIIIIIIIQIIQQQQIQQIIIQIQIIIIIIIIIIIIIIIIIICCCI[1I]II{LSAppClipFields=I}iIIIIIII}32"
- "B52@0:8I16r^{LSBundleData={LSBundleBaseData=IIIIIIi{LSVersionNumber=[32C]}{LSVersionNumber=[32C]}IIIIIIIIIIIIIICCISI{LSBundleBaseFlags=b1b1b1b1b1b1b1}}IQIIC{LSBundleMoreFlags=b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1}IiI{LSVersionNumber=[32C]}{LSVersionNumber=[32C]}IQQQIIIIIIIIIIQIIQQQQIQQIIIQIQIIIIIIIIIIIIIIIIIICCCI[1I]II{LSAppClipFields=I}iIIIIIII}20^{LSContext=@}28@36^@44"
- "B60@0:8^@16^@24I32r^{LSBundleData={LSBundleBaseData=IIIIIIi{LSVersionNumber=[32C]}{LSVersionNumber=[32C]}IIIIIIIIIIIIIICCISI{LSBundleBaseFlags=b1b1b1b1b1b1b1}}IQIIC{LSBundleMoreFlags=b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1}IiI{LSVersionNumber=[32C]}{LSVersionNumber=[32C]}IQQQIIIIIIIIIIQIIQQQQIQQIIIQIQIIIIIIIIIIIIIIIIIICCCI[1I]II{LSAppClipFields=I}iIIIIIII}36@44^@52"
- "C40@0:8^{LSContext=@}16I24I28r^{LSBundleBaseData=IIIIIIi{LSVersionNumber=[32C]}{LSVersionNumber=[32C]}IIIIIIIIIIIIIICCISI{LSBundleBaseFlags=b1b1b1b1b1b1b1}}32"
- "C40@0:8^{LSContext=@}16I24I28r^{LSBundleData={LSBundleBaseData=IIIIIIi{LSVersionNumber=[32C]}{LSVersionNumber=[32C]}IIIIIIIIIIIIIICCISI{LSBundleBaseFlags=b1b1b1b1b1b1b1}}IQIIC{LSBundleMoreFlags=b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1}IiI{LSVersionNumber=[32C]}{LSVersionNumber=[32C]}IQQQIIIIIIIIIIQIIQQQQIQQIIIQIQIIIIIIIIIIIIIIIIIICCCI[1I]II{LSAppClipFields=I}iIIIIIII}32"
- "CodeInfoID"
- "I40@0:8^{LSContext=@}16I24I28r^{LSBundleBaseData=IIIIIIi{LSVersionNumber=[32C]}{LSVersionNumber=[32C]}IIIIIIIIIIIIIICCISI{LSBundleBaseFlags=b1b1b1b1b1b1b1}}32"
- "I40@0:8^{LSContext=@}16I24I28r^{LSBundleData={LSBundleBaseData=IIIIIIi{LSVersionNumber=[32C]}{LSVersionNumber=[32C]}IIIIIIIIIIIIIICCISI{LSBundleBaseFlags=b1b1b1b1b1b1b1}}IQIIC{LSBundleMoreFlags=b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1}IiI{LSVersionNumber=[32C]}{LSVersionNumber=[32C]}IQQQIIIIIIIIIIQIIQQQQIQQIIIQIQIIIIIIIIIIIIIIIIIICCCI[1I]II{LSAppClipFields=I}iIIIIIII}32"
- "I40@0:8^{LSContext=@}16I24I28r^{LSPluginData={LSBundleBaseData=IIIIIIi{LSVersionNumber=[32C]}{LSVersionNumber=[32C]}IIIIIIIIIIIIIICCISI{LSBundleBaseFlags=b1b1b1b1b1b1b1}}IIIII{LSVersionNumber=[32C]}IIII}32"
- "PKDict"
- "Q40@0:8^{LSContext=@}16I24I28r^{LSBundleData={LSBundleBaseData=IIIIIIi{LSVersionNumber=[32C]}{LSVersionNumber=[32C]}IIIIIIIIIIIIIICCISI{LSBundleBaseFlags=b1b1b1b1b1b1b1}}IQIIC{LSBundleMoreFlags=b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1}IiI{LSVersionNumber=[32C]}{LSVersionNumber=[32C]}IQQQIIIIIIIIIIQIIQQQQIQQIIIQIQIIIIIIIIIIIIIIIIIICCCI[1I]II{LSAppClipFields=I}iIIIIIII}32"
- "Unknown usage description feature %lu"
- "Unsetting redactible for unit %llx"
- "_LSRecord_resolve__localizedIdentityUsageDescription"
- "_LSRecord_resolve__localizedMicrophoneUsageDescription"
- "_localizedIdentityUsageDescriptionWithContext:tableID:unitID:unitBytes:"
- "_localizedMicrophoneUsageDescriptionWithContext:tableID:unitID:unitBytes:"
- "addStateFlag:"
- "c40@0:8^{LSContext=@}16I24I28r^{LSBundleData={LSBundleBaseData=IIIIIIi{LSVersionNumber=[32C]}{LSVersionNumber=[32C]}IIIIIIIIIIIIIICCISI{LSBundleBaseFlags=b1b1b1b1b1b1b1}}IQIIC{LSBundleMoreFlags=b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1}IiI{LSVersionNumber=[32C]}{LSVersionNumber=[32C]}IQQQIIIIIIIIIIQIIQQQQIQQIIIQIQIIIIIIIIIIIIIIIIIICCCI[1I]II{LSAppClipFields=I}iIIIIIII}32"
- "grpContainers"
- "i32@0:8@16^{LSBundleData={LSBundleBaseData=IIIIIIi{LSVersionNumber=[32C]}{LSVersionNumber=[32C]}IIIIIIIIIIIIIICCISI{LSBundleBaseFlags=b1b1b1b1b1b1b1}}IQIIC{LSBundleMoreFlags=b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1}IiI{LSVersionNumber=[32C]}{LSVersionNumber=[32C]}IQQQIIIIIIIIIIQIIQQQQIQQIIIQIQIIIIIIIIIIIIIIIIIICCCI[1I]II{LSAppClipFields=I}iIIIIIII}24"
- "i36@0:8@16I24r^{LSBundleData={LSBundleBaseData=IIIIIIi{LSVersionNumber=[32C]}{LSVersionNumber=[32C]}IIIIIIIIIIIIIICCISI{LSBundleBaseFlags=b1b1b1b1b1b1b1}}IQIIC{LSBundleMoreFlags=b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1}IiI{LSVersionNumber=[32C]}{LSVersionNumber=[32C]}IQQQIIIIIIIIIIQIIQQQQIQQIIIQIQIIIIIIIIIIIIIIIIIICCCI[1I]II{LSAppClipFields=I}iIIIIIII}28"
- "i40@0:8^{LSContext=@}16I24I28r^{LSBundleData={LSBundleBaseData=IIIIIIi{LSVersionNumber=[32C]}{LSVersionNumber=[32C]}IIIIIIIIIIIIIICCISI{LSBundleBaseFlags=b1b1b1b1b1b1b1}}IQIIC{LSBundleMoreFlags=b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1}IiI{LSVersionNumber=[32C]}{LSVersionNumber=[32C]}IQQQIIIIIIIIIIQIIQQQQIQQIIIQIQIIIIIIIIIIIIIIIIIICCCI[1I]II{LSAppClipFields=I}iIIIIIII}32"
- "initWithBundleIdentifier:stateFlags:ratingRank:installType:"
- "localizedMicrophoneUsage"
- "r^{LSPluginData={LSBundleBaseData=IIIIIIi{LSVersionNumber=[32C]}{LSVersionNumber=[32C]}IIIIIIIIIIIIIICCISI{LSBundleBaseFlags=b1b1b1b1b1b1b1}}IIIII{LSVersionNumber=[32C]}IIII}20@0:8I16"
- "redactible"
- "v28@?0@\"NSString\"8I16r^{LSBundleData={LSBundleBaseData=IIIIIIi{LSVersionNumber=[32C]}{LSVersionNumber=[32C]}IIIIIIIIIIIIIICCISI{LSBundleBaseFlags=b1b1b1b1b1b1b1}}IQIIC{LSBundleMoreFlags=b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1}IiI{LSVersionNumber=[32C]}{LSVersionNumber=[32C]}IQQQIIIIIIIIIIQIIQQQQIQQIIIQIQIIIIIIIIIIIIIIIIIICCCI[1I]II{LSAppClipFields=I}iIIIIIII}20"
- "v28@?0@\"NSString\"8I16r^{LSPluginData={LSBundleBaseData=IIIIIIi{LSVersionNumber=[32C]}{LSVersionNumber=[32C]}IIIIIIIIIIIIIICCISI{LSBundleBaseFlags=b1b1b1b1b1b1b1}}IIIII{LSVersionNumber=[32C]}IIII}20"
- "v28@?0I8r^{LSBundleData={LSBundleBaseData=IIIIIIi{LSVersionNumber=[32C]}{LSVersionNumber=[32C]}IIIIIIIIIIIIIICCISI{LSBundleBaseFlags=b1b1b1b1b1b1b1}}IQIIC{LSBundleMoreFlags=b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1}IiI{LSVersionNumber=[32C]}{LSVersionNumber=[32C]}IQQQIIIIIIIIIIQIIQQQQIQQIIIQIQIIIIIIIIIIIIIIIIIICCCI[1I]II{LSAppClipFields=I}iIIIIIII}12*20"
- "v36@0:8^{LSContext=@}16I24r^{LSBundleData={LSBundleBaseData=IIIIIIi{LSVersionNumber=[32C]}{LSVersionNumber=[32C]}IIIIIIIIIIIIIICCISI{LSBundleBaseFlags=b1b1b1b1b1b1b1}}IQIIC{LSBundleMoreFlags=b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1}IiI{LSVersionNumber=[32C]}{LSVersionNumber=[32C]}IQQQIIIIIIIIIIQIIQQQQIQQIIIQIQIIIIIIIIIIIIIIIIIICCCI[1I]II{LSAppClipFields=I}iIIIIIII}28"
- "{LSBundleBaseFlags=\"appleInternal\"b1\"requiresObjCGarbageCollection\"b1\"builtWithTSan\"b1\"isLinkEnabled\"b1\"isSecuredSystemContent\"b1\"redactible\"b1\"_reserved\"b1}"
- "{LSBundleBaseFlags=b1b1b1b1b1b1b1}40@0:8^{LSContext=@}16I24I28r^{LSBundleBaseData=IIIIIIi{LSVersionNumber=[32C]}{LSVersionNumber=[32C]}IIIIIIIIIIIIIICCISI{LSBundleBaseFlags=b1b1b1b1b1b1b1}}32"
- "{LSBundleData=\"base\"{LSBundleBaseData=\"bookmark\"I\"container\"I\"execPath\"I\"exactIdentifier\"I\"teamID\"I\"platform\"I\"registrationTime\"i\"version\"{LSVersionNumber=\"_opaque\"[32C]}\"execSDKVersion\"{LSVersionNumber=\"_opaque\"[32C]}\"machOUUIDs\"I\"dataContainerAlias\"I\"bundleName\"I\"localizedShortDisplayName\"I\"displayName\"I\"localizedDisplayName\"I\"localizedMicrophoneUsageDescription\"I\"localizedIdentityUsageDescription\"I\"codeInfoIdentifier\"I\"signerOrganization\"I\"signerIdentity\"I\"infoDictionary\"I\"entitlements\"I\"groupContainers\"I\"containingDirectoryClass\"C\"profileValidationState\"C\"intentDefinitionURLs\"I\"_sliceMask\"S\"signatureVersion\"I\"flags\"{LSBundleBaseFlags=\"appleInternal\"b1\"requiresObjCGarbageCollection\"b1\"builtWithTSan\"b1\"isLinkEnabled\"b1\"isSecuredSystemContent\"b1\"redactible\"b1\"_reserved\"b1}}\"_clas\"I\"_bundleFlags\"Q\"_plistContentFlags\"I\"_itemFlags\"I\"_iconFlags\"C\"moreFlags\"{LSBundleMoreFlags=\"isWebBrowser\"b1\"isMailClient\"b1\"supportsControllerUserInteraction\"b1\"supportsSpotlightQueryContinuation\"b1\"supportsSpotlightActions\"b1\"isCodeSigningInfoNotAuthoritative\"b1\"applicationQueriesSchemesTooBig\"b1\"isUpdateAvailable\"b1\"isPlaygroundsApp\"b1\"supportsAlwaysOnDisplay\"b1\"defaultsToPrivateAlwaysOnDisplayTreatment\"b1\"supportsLiveActivities\"b1\"supportsLiveActivitiesFrequentUpdates\"b1\"requiresPostprocessing\"b1\"hasShellRole\"b1\"requiresSecureLaunch\"b1\"eligibleForWatchAppInstall\"b1\"isEligibilityCheckedBrowser\"b1\"isEligibilityCheckedBrowserEngineEmbedder\"b1\"isManagedAppDistributor\"b1\"isHiddenByAppProtection\"b1\"isLockedByAppProtection\"b1\"supportsDataExport\"b1\"hasSupportsGameModeKey\"b1\"supportsGameMode\"b1\"isOnCryptex\"b1}\"_hfsType\"I\"_mtime\"i\"minSystemVersionPlatform\"I\"_minSystemVersion\"{LSVersionNumber=\"_opaque\"[32C]}\"_maxSystemVersion\"{LSVersionNumber=\"_opaque\"[32C]}\"appStoreToolsBuildVersion\"I\"sequenceNumber\"Q\"compatibilityState\"Q\"itemID\"Q\"deviceFamilies\"I\"identifier\"I\"counterpartIdentifiers\"I\"equivalentBundleIdentifiers\"I\"categoryType\"I\"secondaryCategoryType\"I\"filename\"I\"bundleVersion\"I\"shortVersionString\"I\"installType\"I\"installFailureReason\"Q\"vendorName\"I\"appType\"I\"staticDiskUsage\"Q\"purchaserDSID\"Q\"downloaderDSID\"Q\"familyID\"Q\"itemName\"I\"storefront\"Q\"versionIdentifier\"Q\"sourceAppBundleID\"I\"appVariant\"I\"managementDeclarationIdentifier\"I\"ratingRank\"Q\"ratingLabel\"I\"genreID\"Q\"genre\"I\"distributorInfo\"I\"primaryIconName\"I\"alternatePrimaryIconName\"I\"iconsDict\"I\"iconFileNames\"I\"libraryPath\"I\"libraryItems\"I\"claims\"I\"types\"I\"plugins\"I\"driverExtensions\"I\"extensionPoints\"I\"activityTypes\"I\"queriableSchemes\"I\"bgPermittedIDs\"I\"carPlayInstrumentClusterURLSchemes\"I\"appContainerAlias\"I\"revision\"C\"retries\"C\"_reserved4\"C\"sandboxEnvironmentVariables\"I\"localizedNameWithContext\"[1I]\"bundlePersonas\"I\"bundlePersonaTypes\"I\"appClipFields\"{LSAppClipFields=\"parentAppIDs\"I}\"recordModificationTime\"i\"supportedGameControllers\"I\"mobileInstallIDs\"I\"applicationManagementDomain\"I\"stashedAppDict\"I\"linkedParentBundleIdentifier\"I\"serializedPlaceholderPath\"I\"_reserved5\"I}"
- "{LSBundleData={LSBundleBaseData=IIIIIIi{LSVersionNumber=[32C]}{LSVersionNumber=[32C]}IIIIIIIIIIIIIICCISI{LSBundleBaseFlags=b1b1b1b1b1b1b1}}IQIIC{LSBundleMoreFlags=b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1}IiI{LSVersionNumber=[32C]}{LSVersionNumber=[32C]}IQQQIIIIIIIIIIQIIQQQQIQQIIIQIQIIIIIIIIIIIIIIIIIICCCI[1I]II{LSAppClipFields=I}iIIIIIII}32@0:8@16^@24"
- "{LSBundleMoreFlags=b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1}40@0:8^{LSContext=@}16I24I28r^{LSBundleData={LSBundleBaseData=IIIIIIi{LSVersionNumber=[32C]}{LSVersionNumber=[32C]}IIIIIIIIIIIIIICCISI{LSBundleBaseFlags=b1b1b1b1b1b1b1}}IQIIC{LSBundleMoreFlags=b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1}IiI{LSVersionNumber=[32C]}{LSVersionNumber=[32C]}IQQQIIIIIIIIIIQIIQQQQIQQIIIQIQIIIIIIIIIIIIIIIIIICCCI[1I]II{LSAppClipFields=I}iIIIIIII}32"
- "{LSVersionNumber=[32C]}40@0:8^{LSContext=@}16I24I28r^{LSBundleBaseData=IIIIIIi{LSVersionNumber=[32C]}{LSVersionNumber=[32C]}IIIIIIIIIIIIIICCISI{LSBundleBaseFlags=b1b1b1b1b1b1b1}}32"
- "{expected<LSApplicationRecord *, NSError *>={__conditional_no_unique_address<true, std::__expected_base<LSApplicationRecord *, NSError *>::__repr>={__repr={__conditional_no_unique_address<false, std::__expected_base<LSApplicationRecord *, NSError *>::__union_t>=(__union_t=@@)}B}}}36@0:8^{LSContext=@}16I24r^{LSBundleData={LSBundleBaseData=IIIIIIi{LSVersionNumber=[32C]}{LSVersionNumber=[32C]}IIIIIIIIIIIIIICCISI{LSBundleBaseFlags=b1b1b1b1b1b1b1}}IQIIC{LSBundleMoreFlags=b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1}IiI{LSVersionNumber=[32C]}{LSVersionNumber=[32C]}IQQQIIIIIIIIIIQIIQQQQIQQIIIQIQIIIIIIIIIIIIIIIIIICCCI[1I]II{LSAppClipFields=I}iIIIIIII}28"

```
