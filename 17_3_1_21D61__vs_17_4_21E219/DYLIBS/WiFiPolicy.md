## WiFiPolicy

> `/System/Library/PrivateFrameworks/WiFiPolicy.framework/WiFiPolicy`

```diff

-753.9.0.0.0
-  __TEXT.__text: 0xab0e8
-  __TEXT.__auth_stubs: 0x15d0
-  __TEXT.__objc_methlist: 0xeee4
-  __TEXT.__const: 0x4e8
-  __TEXT.__cstring: 0x1aaab
-  __TEXT.__gcc_except_tab: 0x1358
-  __TEXT.__oslogstring: 0x3217
+760.19.3.1.0
+  __TEXT.__text: 0xad570
+  __TEXT.__auth_stubs: 0x15b0
+  __TEXT.__objc_methlist: 0xf224
+  __TEXT.__const: 0x510
+  __TEXT.__cstring: 0x1a7a8
+  __TEXT.__gcc_except_tab: 0x1344
+  __TEXT.__oslogstring: 0x36b2
   __TEXT.__dlopen_cstrs: 0x56
-  __TEXT.__unwind_info: 0x1f34
+  __TEXT.__unwind_info: 0x1f74
   __TEXT.__eh_frame: 0x38
-  __TEXT.__objc_classname: 0x124f
-  __TEXT.__objc_methname: 0x2c962
-  __TEXT.__objc_methtype: 0x2f6b
-  __TEXT.__objc_stubs: 0x161a0
-  __DATA_CONST.__got: 0x2b0
-  __DATA_CONST.__const: 0x1f88
+  __TEXT.__objc_classname: 0x1250
+  __TEXT.__objc_methname: 0x2d53c
+  __TEXT.__objc_methtype: 0x3025
+  __TEXT.__objc_stubs: 0x16680
+  __DATA_CONST.__got: 0x2b8
+  __DATA_CONST.__const: 0x2008
   __DATA_CONST.__objc_classlist: 0x4e8
   __DATA_CONST.__objc_catlist: 0x58
   __DATA_CONST.__objc_protolist: 0xe0
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_const: 0x1aeb8
-  __DATA_CONST.__objc_selrefs: 0x8750
-  __DATA_CONST.__objc_arraydata: 0xa58
-  __AUTH_CONST.__cfstring: 0x17060
+  __DATA_CONST.__objc_const: 0x1b398
+  __DATA_CONST.__objc_selrefs: 0x8938
+  __DATA_CONST.__objc_protorefs: 0x20
+  __DATA_CONST.__objc_classrefs: 0x6f8
+  __DATA_CONST.__objc_superrefs: 0x408
+  __DATA_CONST.__objc_arraydata: 0xa98
+  __AUTH_CONST.__cfstring: 0x17020
   __AUTH_CONST.__objc_const: 0x42e0
   __AUTH_CONST.__objc_intobj: 0x1680
-  __AUTH_CONST.__objc_arrayobj: 0x390
-  __AUTH_CONST.__const: 0x320
+  __AUTH_CONST.__objc_arrayobj: 0x3a8
+  __AUTH_CONST.__const: 0x380
   __AUTH_CONST.__objc_dictobj: 0x78
   __AUTH_CONST.__objc_doubleobj: 0x20
-  __AUTH_CONST.__auth_got: 0xb00
-  __AUTH.__objc_data: 0x960
-  __DATA.__objc_protorefs: 0x20
-  __DATA.__objc_classrefs: 0x6e0
-  __DATA.__objc_superrefs: 0x400
-  __DATA.__objc_ivar: 0x1d74
-  __DATA.__data: 0x1a48
-  __DATA.__bss: 0x40
-  __DATA_DIRTY.__objc_data: 0x27b0
-  __DATA_DIRTY.__bss: 0x240
+  __AUTH_CONST.__auth_got: 0xaf0
+  __AUTH.__objc_data: 0x780
+  __DATA.__objc_ivar: 0x1ddc
+  __DATA.__data: 0x1a40
+  __DATA.__bss: 0x2a
+  __DATA_DIRTY.__objc_data: 0x2990
+  __DATA_DIRTY.__bss: 0x260
   __DATA_DIRTY.__common: 0x20
   - /System/Library/Frameworks/CFNetwork.framework/CFNetwork
   - /System/Library/Frameworks/CoreData.framework/CoreData

   - /System/Library/PrivateFrameworks/CoreAnalytics.framework/CoreAnalytics
   - /System/Library/PrivateFrameworks/CoreRoutine.framework/CoreRoutine
   - /System/Library/PrivateFrameworks/CrashReporterSupport.framework/CrashReporterSupport
+  - /System/Library/PrivateFrameworks/FrontBoardServices.framework/FrontBoardServices
   - /System/Library/PrivateFrameworks/GeoServices.framework/GeoServices
   - /System/Library/PrivateFrameworks/IO80211.framework/IO80211
   - /System/Library/PrivateFrameworks/Lexicon.framework/Lexicon

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libc++.1.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 75D3385A-5188-344B-AFDC-2C997D6649D2
-  Functions: 5431
-  Symbols:   17891
-  CStrings:  15006
+  UUID: 79ACFDCC-5797-3626-AF4C-4FE4A005FCA1
+  Functions: 5515
+  Symbols:   18135
+  CStrings:  15138
 
Symbols:
+ +[WiFiSoftError _updateHUDWithMessage:].cold.1
+ +[WiFiSoftError _updateHUDWithMessage:].cold.2
+ +[WiFiSoftError _updateHUDWithMessage:].cold.3
+ +[WiFiUsageChannel channelWithBssDetails:]
+ +[WiFiUsageChannel channelWithChannelInfo:]
+ +[WiFiUsageChannel channelWithScanChannel:]
+ +[WiFiUsageInterfaceStats _statsFromMIB:]
+ +[WiFiUsageInterfaceStats _statsFromMIB:].cold.1
+ +[WiFiUsageInterfaceStats _statsFromMIB:].cold.2
+ +[WiFiUsageInterfaceStats _statsFromMIB:].cold.3
+ +[WiFiUsageInterfaceStats _statsFromNetIF:]
+ +[WiFiUsageInterfaceStats netIFStatsForInterfaceName:]
+ +[WiFiUsageInterfaceStats statsForInterfaceName:].cold.1
+ +[WiFiUsageLQMTriggerCriteria initialize]
+ +[WiFiUsageMonitor getTDEvalCompleteEventStringForDisplay:]
+ +[WiFiUsagePrivacyFilter bandFromChanInfo:]
+ +[WiFiUsagePrivacyFilter bandFromChannel:]
+ +[WiFiUsagePrivacyFilter bandFromFlags:]
+ +[WiFiUsagePrivacyFilter channelWidthFromFlags:]
+ +[WiFiUsagePrivacyFilter subBandForBSPAsStringFromChannel:andBand:]
+ -[WiFiUsageChannel initWithChannel:flags:]
+ -[WiFiUsageChannel initWithChannel:flags:band:width:isDFS:]
+ -[WiFiUsageChannel initWithChannel:flags:isDFS:]
+ -[WiFiUsageChannel updateDFSInfoFromSupportedChannels:]
+ -[WiFiUsageInterfaceStats description]
+ -[WiFiUsageInterfaceStats isEqual:]
+ -[WiFiUsageInterfaceStats isEqualToInterfaceStats:]
+ -[WiFiUsageLQMSample allDimensionsIntoDict:]
+ -[WiFiUsageLQMUserSample allDimensionsIntoDict:]
+ -[WiFiUsageLQMUserSample band]
+ -[WiFiUsageLQMUserSample bspAvgMuteMS]
+ -[WiFiUsageLQMUserSample bspErrorPercentage]
+ -[WiFiUsageLQMUserSample bspMaxConsecutiveFails]
+ -[WiFiUsageLQMUserSample bspMaxMuteMS]
+ -[WiFiUsageLQMUserSample bspMutePercentage]
+ -[WiFiUsageLQMUserSample bspRejectOrFailPercentageOfTriggers]
+ -[WiFiUsageLQMUserSample bspTimeOutPercentageOfTriggers]
+ -[WiFiUsageLQMUserSample bspTimeToTST]
+ -[WiFiUsageLQMUserSample bspTriggerCount]
+ -[WiFiUsageLQMUserSample channelWidth]
+ -[WiFiUsageLQMUserSample channel]
+ -[WiFiUsageLQMUserSample isBSPActive]
+ -[WiFiUsageLQMUserSample isBspSampleDurationExpected:]
+ -[WiFiUsageLQMUserSample isP2PActiveBSP]
+ -[WiFiUsageLQMUserSample isScanActiveBSP]
+ -[WiFiUsageLQMUserSample phyMode]
+ -[WiFiUsageLQMUserSample populateWithBspOverflowed:IsBSPActive:BspTimeToTST:BspSampleDurationMS:IsScanActiveBSP:IsP2PActiveBSP:BspTriggerCount:BspMutePercentage:BspMaxMuteMS:BspAvgMuteMS:BspErrorPercentage:BspTimeOutPercentageOfTriggers:BspRejectOrFailPercentageOfTriggers:BspMaxConsecutiveFails:]
+ -[WiFiUsageLQMUserSample rxBytesSecondary]
+ -[WiFiUsageLQMUserSample rxBytes]
+ -[WiFiUsageLQMUserSample setBand:]
+ -[WiFiUsageLQMUserSample setBspAvgMuteMS:]
+ -[WiFiUsageLQMUserSample setBspErrorPercentage:]
+ -[WiFiUsageLQMUserSample setBspMaxConsecutiveFails:]
+ -[WiFiUsageLQMUserSample setBspMaxMuteMS:]
+ -[WiFiUsageLQMUserSample setBspMutePercentage:]
+ -[WiFiUsageLQMUserSample setBspRejectOrFailPercentageOfTriggers:]
+ -[WiFiUsageLQMUserSample setBspTimeOutPercentageOfTriggers:]
+ -[WiFiUsageLQMUserSample setBspTimeToTST:]
+ -[WiFiUsageLQMUserSample setBspTriggerCount:]
+ -[WiFiUsageLQMUserSample setChannel:]
+ -[WiFiUsageLQMUserSample setChannelWidth:]
+ -[WiFiUsageLQMUserSample setIsBSPActive:]
+ -[WiFiUsageLQMUserSample setIsP2PActiveBSP:]
+ -[WiFiUsageLQMUserSample setIsScanActiveBSP:]
+ -[WiFiUsageLQMUserSample setPhyMode:]
+ -[WiFiUsageLQMUserSample setRxBytes:]
+ -[WiFiUsageLQMUserSample setRxBytesSecondary:]
+ -[WiFiUsageLQMUserSample setTxBytes:]
+ -[WiFiUsageLQMUserSample setTxBytesSecondary:]
+ -[WiFiUsageLQMUserSample txBytesSecondary]
+ -[WiFiUsageLQMUserSample txBytes]
+ -[WiFiUsageLQMUserSample updateWithTxBytes:RxBytes:TxL3Packets:RxL3Packets:txBytesSecondary:rxBytesSecondary:]
+ -[WiFiUsageMonitor isBSPActive]
+ -[WiFiUsageMonitor lastScanRequest]
+ -[WiFiUsageMonitor secondaryIfStatsAtLastLqmUpdate]
+ -[WiFiUsageMonitor setIsBSPActive:]
+ -[WiFiUsageMonitor setLastScanRequest:]
+ -[WiFiUsageMonitor setScanningState:client:neighborBSS:otherBSS:withChannelInfoList:withRequest:forInterface:]
+ -[WiFiUsageMonitor setSecondaryIfStatsAtLastLqmUpdate:]
+ -[WiFiUsageMonitor submitScanResultWithNeighborBSS:withOtherBSS:withChannelInfoList:]
+ -[WiFiUsageMonitor updateIsBSPActive:]
+ -[WiFiUsageMonitor updateWithBspOverflowed:IsBSPActive:BspTimeToTST:BspSampleDurationMS:IsScanActiveBSP:IsP2PActiveBSP:BspTriggerCount:BspMutePercentage:BspMaxMuteMS:BspAvgMuteMS:BspErrorPercentage:BspTimeOutPercentageOfTriggers:BspRejectOrFailPercentageOfTriggers:bspMaxConsecutiveFails:supportsLinkRecommendation:forInterface:]
+ -[WiFiUsageParsedBeacon hasColocatedMLD2G]
+ -[WiFiUsageParsedBeacon hasColocatedMLD5G]
+ -[WiFiUsageParsedBeacon hasColocatedMLD6G]
+ -[WiFiUsageParsedBeacon hasEHT]
+ -[WiFiUsageParsedBeacon setHasColocatedMLD2G:]
+ -[WiFiUsageParsedBeacon setHasColocatedMLD5G:]
+ -[WiFiUsageParsedBeacon setHasColocatedMLD6G:]
+ -[WiFiUsageParsedBeacon setHasEHT:]
+ GCC_except_table213
+ GCC_except_table85
+ _FBSOpenApplicationOptionKeyActivateSuspended
+ _OBJC_CLASS_$_NSURLComponents
+ _OBJC_CLASS_$_NSURLQueryItem
+ _OBJC_CLASS_$__LSOpenConfiguration
+ _OBJC_IVAR_$_WiFiUsageLQMUserSample._band
+ _OBJC_IVAR_$_WiFiUsageLQMUserSample._bspAvgMuteMS
+ _OBJC_IVAR_$_WiFiUsageLQMUserSample._bspErrorPercentage
+ _OBJC_IVAR_$_WiFiUsageLQMUserSample._bspMaxConsecutiveFails
+ _OBJC_IVAR_$_WiFiUsageLQMUserSample._bspMaxMuteMS
+ _OBJC_IVAR_$_WiFiUsageLQMUserSample._bspMutePercentage
+ _OBJC_IVAR_$_WiFiUsageLQMUserSample._bspRejectOrFailPercentageOfTriggers
+ _OBJC_IVAR_$_WiFiUsageLQMUserSample._bspTimeOutPercentageOfTriggers
+ _OBJC_IVAR_$_WiFiUsageLQMUserSample._bspTimeToTST
+ _OBJC_IVAR_$_WiFiUsageLQMUserSample._bspTriggerCount
+ _OBJC_IVAR_$_WiFiUsageLQMUserSample._channel
+ _OBJC_IVAR_$_WiFiUsageLQMUserSample._channelWidth
+ _OBJC_IVAR_$_WiFiUsageLQMUserSample._isBSPActive
+ _OBJC_IVAR_$_WiFiUsageLQMUserSample._isP2PActiveBSP
+ _OBJC_IVAR_$_WiFiUsageLQMUserSample._isScanActiveBSP
+ _OBJC_IVAR_$_WiFiUsageLQMUserSample._phyMode
+ _OBJC_IVAR_$_WiFiUsageLQMUserSample._rxBytes
+ _OBJC_IVAR_$_WiFiUsageLQMUserSample._rxBytesSecondary
+ _OBJC_IVAR_$_WiFiUsageLQMUserSample._txBytes
+ _OBJC_IVAR_$_WiFiUsageLQMUserSample._txBytesSecondary
+ _OBJC_IVAR_$_WiFiUsageMonitor._isBSPActive
+ _OBJC_IVAR_$_WiFiUsageMonitor._lastScanRequest
+ _OBJC_IVAR_$_WiFiUsageMonitor._secondaryIfStatsAtLastLqmUpdate
+ _OBJC_IVAR_$_WiFiUsageParsedBeacon._hasColocatedMLD2G
+ _OBJC_IVAR_$_WiFiUsageParsedBeacon._hasColocatedMLD5G
+ _OBJC_IVAR_$_WiFiUsageParsedBeacon._hasColocatedMLD6G
+ _OBJC_IVAR_$_WiFiUsageParsedBeacon._hasEHT
+ __ZNKSt3__112basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEE20__throw_length_errorB8ue170006Ev
+ __ZNKSt3__16vectorIN6gloria6TileIdENS_9allocatorIS2_EEE20__throw_length_errorB8ue170006Ev
+ __ZNSt12length_errorC1B8ue170006EPKc
+ __ZNSt3__112basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEEC2B8ue170006Emc
+ __ZNSt3__116__pad_and_outputB8ue170006IcNS_11char_traitsIcEEEENS_19ostreambuf_iteratorIT_T0_EES6_PKS4_S8_S8_RNS_8ios_baseES4_
+ __ZNSt3__119__allocate_at_leastB8ue170006INS_9allocatorIN6gloria6TileIdEEEEENS_19__allocation_resultINS_16allocator_traitsIT_E7pointerEEERS7_m
+ __ZNSt3__119basic_ostringstreamIcNS_11char_traitsIcEENS_9allocatorIcEEEC1B8ue170006Ev
+ __ZNSt3__120__throw_length_errorB8ue170006EPKc
+ __ZNSt3__124__put_character_sequenceB8ue170006IcNS_11char_traitsIcEEEERNS_13basic_ostreamIT_T0_EES7_PKS4_m
+ __ZNSt3__127__tree_balance_after_insertB8ue170006IPNS_16__tree_node_baseIPvEEEEvT_S5_
+ __ZSt28__throw_bad_array_new_lengthB8ue170006v
+ ___110-[WiFiUsageMonitor setScanningState:client:neighborBSS:otherBSS:withChannelInfoList:withRequest:forInterface:]_block_invoke
+ ___329-[WiFiUsageMonitor updateWithBspOverflowed:IsBSPActive:BspTimeToTST:BspSampleDurationMS:IsScanActiveBSP:IsP2PActiveBSP:BspTriggerCount:BspMutePercentage:BspMaxMuteMS:BspAvgMuteMS:BspErrorPercentage:BspTimeOutPercentageOfTriggers:BspRejectOrFailPercentageOfTriggers:bspMaxConsecutiveFails:supportsLinkRecommendation:forInterface:]_block_invoke
+ ___36-[WiFiUsageMonitor submitAnalytics:]_block_invoke.597
+ ___38-[WiFiSoftError updateHUDWithMessage:]_block_invoke.114
+ ___38-[WiFiSoftError updateHUDWithMessage:]_block_invoke.114.cold.1
+ ___38-[WiFiUsageMonitor updateIsBSPActive:]_block_invoke
+ ___48-[WiFiUsageNetworkSession processForgetNetwork:]_block_invoke.23
+ ___53-[WiFiSoftError tapToRadarWithURL:completionHandler:]_block_invoke.130
+ ___53-[WiFiSoftError tapToRadarWithURL:completionHandler:]_block_invoke.130.cold.1
+ ___85-[WiFiUsageMonitor submitScanResultWithNeighborBSS:withOtherBSS:withChannelInfoList:]_block_invoke
+ ___85-[WiFiUsageMonitor submitScanResultWithNeighborBSS:withOtherBSS:withChannelInfoList:]_block_invoke_2
+ ___85-[WiFiUsageMonitor updateKnownNetworksSupportingSeamless:forBSS:andSSID:beaconCache:]_block_invoke.641
+ ___85-[WiFiUsageMonitor updateKnownNetworksSupportingSeamless:forBSS:andSSID:beaconCache:]_block_invoke.652
+ ___85-[WiFiUsageMonitor updateKnownNetworksSupportingSeamless:forBSS:andSSID:beaconCache:]_block_invoke_2
+ ___85-[WiFiUsageMonitor updateKnownNetworksSupportingSeamless:forBSS:andSSID:beaconCache:]_block_invoke_3
+ ___85-[WiFiUsageMonitor updateKnownNetworksSupportingSeamless:forBSS:andSSID:beaconCache:]_block_invoke_4
+ ___block_descriptor_133_e8_32s40s_e5_v8?0ls32l8s40l8
+ ___block_descriptor_32_e47_B32?0"WiFiUsageChannel"8"NSMutableSet"16^B24l
+ ___block_descriptor_48_e8_32s40s_e19_"NSDictionary"8?0ls32l8s40l8
+ ___block_descriptor_89_e8_32s40s48s56s64s72s_e5_v8?0ls32l8s40l8s48l8s56l8s64l8s72l8
+ ___block_literal_global.644
+ ___block_literal_global.655
+ ___block_literal_global.657
+ ___block_literal_global.659
+ ___block_literal_global.98
+ __unnamed_array_storage.128
+ __unnamed_array_storage.153
+ __unnamed_array_storage.176
+ __unnamed_array_storage.196
+ __unnamed_array_storage.199
+ _if_nametoindex
+ _objc_msgSend$URL
+ _objc_msgSend$_statsFromMIB:
+ _objc_msgSend$_statsFromNetIF:
+ _objc_msgSend$absoluteString
+ _objc_msgSend$allDimensionsIntoDict:
+ _objc_msgSend$bandFromChanInfo:
+ _objc_msgSend$channelWithBssDetails:
+ _objc_msgSend$channelWithChannelInfo:
+ _objc_msgSend$channelWithScanChannel:
+ _objc_msgSend$getTDEvalCompleteEventStringForDisplay:
+ _objc_msgSend$initWithChannel:flags:
+ _objc_msgSend$initWithChannel:flags:band:width:isDFS:
+ _objc_msgSend$initWithName:value:
+ _objc_msgSend$isBSPActive
+ _objc_msgSend$isBspSampleDurationExpected:
+ _objc_msgSend$isEqualToInterfaceStats:
+ _objc_msgSend$member:
+ _objc_msgSend$openURL:configuration:error:
+ _objc_msgSend$populateWithBspOverflowed:IsBSPActive:BspTimeToTST:BspSampleDurationMS:IsScanActiveBSP:IsP2PActiveBSP:BspTriggerCount:BspMutePercentage:BspMaxMuteMS:BspAvgMuteMS:BspErrorPercentage:BspTimeOutPercentageOfTriggers:BspRejectOrFailPercentageOfTriggers:BspMaxConsecutiveFails:
+ _objc_msgSend$redactedDescription
+ _objc_msgSend$setBspAvgMuteMS:
+ _objc_msgSend$setBspErrorPercentage:
+ _objc_msgSend$setBspMaxConsecutiveFails:
+ _objc_msgSend$setBspMaxMuteMS:
+ _objc_msgSend$setBspMutePercentage:
+ _objc_msgSend$setBspRejectOrFailPercentageOfTriggers:
+ _objc_msgSend$setBspTimeOutPercentageOfTriggers:
+ _objc_msgSend$setBspTimeToTST:
+ _objc_msgSend$setBspTriggerCount:
+ _objc_msgSend$setFrontBoardOptions:
+ _objc_msgSend$setHasColocatedMLD2G:
+ _objc_msgSend$setHasColocatedMLD5G:
+ _objc_msgSend$setHasColocatedMLD6G:
+ _objc_msgSend$setHasEHT:
+ _objc_msgSend$setHost:
+ _objc_msgSend$setIsBSPActive:
+ _objc_msgSend$setIsP2PActiveBSP:
+ _objc_msgSend$setIsScanActiveBSP:
+ _objc_msgSend$setQueryItems:
+ _objc_msgSend$setRxBytesSecondary:
+ _objc_msgSend$setScheme:
+ _objc_msgSend$setTxBytesSecondary:
+ _objc_msgSend$subBandForBSPAsStringFromChannel:andBand:
+ _objc_msgSend$submitScanResultWithNeighborBSS:withOtherBSS:withChannelInfoList:
+ _objc_msgSend$updateDFSInfoFromSupportedChannels:
+ _objc_msgSend$updateWithTxBytes:RxBytes:TxL3Packets:RxL3Packets:txBytesSecondary:rxBytesSecondary:
- +[WiFiUsageBssDetails bandFromChannel:]
- +[WiFiUsageBssDetails bandFromFlags:]
- +[WiFiUsageBssDetails channelWidthFromFlags:]
- +[WiFiUsageChannel channelWithBssDetails:andChannelInfoList:]
- +[WiFiUsageMonitor appendChannelInfoToDict:from:]
- +[WiFiUsageMonitor getTDExecutionStateEventStringForDisplay:]
- -[WiFiSoftError hudOffset]
- -[WiFiSoftError setHudOffset:]
- -[WiFiUsageChannel dfsChannel:]
- -[WiFiUsageInterfaceCapabilities currentLinkPHYRate]
- -[WiFiUsageInterfaceCapabilities maxLinkPHYRate]
- -[WiFiUsageLQMUserSample updateWithTxBytes:RxBytes:TxL3Packets:RxL3Packets:]
- -[WiFiUsageMonitor setScanningState:client:neighborBSS:otherBSS:withChannelInfoList:forInterface:]
- GCC_except_table206
- GCC_except_table86
- _CARenderServerGetServerPort
- _OBJC_IVAR_$_WiFiSoftError._hudOffset
- _OUTLINED_FUNCTION_13
- __ZNKSt3__112basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEE20__throw_length_errorB7v160006Ev
- __ZNKSt3__16vectorIN6gloria6TileIdENS_9allocatorIS2_EEE20__throw_length_errorB7v160006Ev
- __ZNSt12length_errorC1B7v160006EPKc
- __ZNSt3__112basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEEC2B7v160006Emc
- __ZNSt3__116__pad_and_outputB7v160006IcNS_11char_traitsIcEEEENS_19ostreambuf_iteratorIT_T0_EES6_PKS4_S8_S8_RNS_8ios_baseES4_
- __ZNSt3__119__allocate_at_leastB7v160006INS_9allocatorIN6gloria6TileIdEEEEENS_19__allocation_resultINS_16allocator_traitsIT_E7pointerEEERS7_m
- __ZNSt3__119basic_ostringstreamIcNS_11char_traitsIcEENS_9allocatorIcEEEC1B7v160006Ev
- __ZNSt3__120__throw_length_errorB7v160006EPKc
- __ZNSt3__124__put_character_sequenceB7v160006IcNS_11char_traitsIcEEEERNS_13basic_ostreamIT_T0_EES7_PKS4_m
- __ZNSt3__127__tree_balance_after_insertB7v160006IPNS_16__tree_node_baseIPvEEEEvT_S5_
- __ZSt28__throw_bad_array_new_lengthB7v160006v
- ___36-[WiFiUsageMonitor submitAnalytics:]_block_invoke.598
- ___38-[WiFiSoftError updateHUDWithMessage:]_block_invoke.126
- ___38-[WiFiSoftError updateHUDWithMessage:]_block_invoke.126.cold.1
- ___48-[WiFiUsageNetworkSession processForgetNetwork:]_block_invoke_2
- ___53-[WiFiSoftError tapToRadarWithURL:completionHandler:]_block_invoke.145
- ___53-[WiFiSoftError tapToRadarWithURL:completionHandler:]_block_invoke.145.cold.1
- ___85-[WiFiUsageMonitor updateKnownNetworksSupportingSeamless:forBSS:andSSID:beaconCache:]_block_invoke.636
- ___85-[WiFiUsageMonitor updateKnownNetworksSupportingSeamless:forBSS:andSSID:beaconCache:]_block_invoke.692
- ___98-[WiFiUsageMonitor setScanningState:client:neighborBSS:otherBSS:withChannelInfoList:forInterface:]_block_invoke
- ___98-[WiFiUsageMonitor setScanningState:client:neighborBSS:otherBSS:withChannelInfoList:forInterface:]_block_invoke.555
- ___98-[WiFiUsageMonitor setScanningState:client:neighborBSS:otherBSS:withChannelInfoList:forInterface:]_block_invoke_2
- ___block_descriptor_81_e8_32s40s48s56s64s_e5_v8?0ls32l8s40l8s48l8s56l8s64l8
- ___block_literal_global.110
- ___block_literal_global.639
- __unnamed_array_storage.138
- __unnamed_array_storage.163
- __unnamed_array_storage.186
- __unnamed_array_storage.206
- __unnamed_array_storage.209
- _mach_port_deallocate
- _objc_msgSend$appendChannelInfoToDict:from:
- _objc_msgSend$channelWithBssDetails:andChannelInfoList:
- _objc_msgSend$currentLinkPHYRate
- _objc_msgSend$dfsChannel:
- _objc_msgSend$getTDExecutionStateEventStringForDisplay:
- _objc_msgSend$maxLinkPHYRate
- _objc_msgSend$updateWithTxBytes:RxBytes:TxL3Packets:RxL3Packets:
CStrings:
+ "#\x12\xf0\xf0\xf0\xf0A"
+ "%@: maxPHYRate:%d maxNSS:%d"
+ "%Xu_%lu"
+ "%s -  SSIDTransitionCandidates(excluding %{mask.hash}@):%{private}@\n"
+ "%s - bssid:%{mask.hash}@ %@Ghz rssi:%@dBm %@"
+ "%s - channel:%lu flags:%lu (band enum:%u band:%@)"
+ "%s - currentBSSID (%{mask.hash}@) not in beaconCache"
+ "%s - currentBSSID (%{mask.hash}@) too short"
+ "%s - isUp:%@ details:%{private}@"
+ "%s Begin capturing metric for %{mask.hash}@[%{mask.hash}@] - {oui:%@ blacklistedReason:%@ blacklistedSubreason:%@}"
+ "%s Clearing trigger %@ (%@) for '%{mask.hash}@[%{mask.hash}@]'"
+ "%s Clearing(for interval exceeded) trigger %@ (%@) for '%{mask.hash}@[%{mask.hash}@] (diff:%lu)'"
+ "%s Clearing(for interval exceeded) trigger %@ (%@) for '%{mask.hash}@[%{mask.hash}@]'"
+ "%s Finish capturing metric for %{mask.hash}@[%{mask.hash}@] - {duration:%@ unblacklistReason:%@ prunedCount:%@}"
+ "%s Metric for %{mask.hash}@[%{mask.hash}@] not found!"
+ "%s Trigger %@ for [%{mask.hash}@] was %f seconds ago and outside window. Will not consider for WoW blacklist"
+ "%s Unblacklisting BSS '%{mask.hash}@[%{mask.hash}@]' for autojoin "
+ "%s Unblacklisting and removing '%{mask.hash}@[%{mask.hash}@]' from Autojoin blacklist"
+ "%s Unblacklisting and removing '%{mask.hash}@[%{mask.hash}@]' from BSS blacklist"
+ "%s Unblacklisting and removing '%{mask.hash}@[%{mask.hash}@]' from WoW blacklist"
+ "%s blacklistedNode %{mask.hash}@[%{mask.hash}@]"
+ "%s bssid '%{mask.hash}@' %s thresholds. CurrentCount:%d ThresholdCount:%d"
+ "%s metric ssid:%{mask.hash}@ bssid:%{mask.hash}@ doesnt match with node ssid:%{mask.hash}@ bssid:%{mask.hash}@"
+ "%s network %{mask.hash}@[%{mask.hash}@]"
+ "%s node not found with ssid:%{mask.hash}@ bssid:%{mask.hash}@"
+ "%s: %@: roamed from BSSID %{mask.hash}@ on channel %d(%@Ghz) to BSSID %{mask.hash}@ on channel %d(%@Ghz)"
+ "%s: (%{mask.hash}@) contains PersonalHotspotIEs:%@ -- skip"
+ "%s: (%{mask.hash}@) parsingSuccessful: %@ invalidElements:%@ invalidExtElements:%@ -- skip"
+ "%s: BMDeviceWiFi Allocation failed SSID:%{mask.hash}@ linkstate:%d "
+ "%s: BMPruner NUll - SSID:%{mask.hash}@ "
+ "%s: BMSource NUll - SSID:%{mask.hash}@ linkstate:%d "
+ "%s: BMStream NUll - SSID:%{mask.hash}@ "
+ "%s: BMStream NUll - SSID:%{mask.hash}@ linkstate:%d "
+ "%s: Do Nothing as WiFiDirectDonation Feature Flag Disabled! details:%{private}@ linkWentUp:%d linkWentDown:%d "
+ "%s: Fetching tile key at key: %@ zoom: %hhu"
+ "%s: InValid inputs details:%{private}@ linkWentUp:%d linkWentDown:%d"
+ "%s: Invalid tileKey at zoom: %hhu"
+ "%s: Trigger '%@' for '%{mask.hash}@ [%{mask.hash}@]' (reason=%lu reasonData=%ld state=%lu)"
+ "%s: bssid %{mask.hash}@ has not been derived from a beacon retrieved after the current association (last updated: %@)"
+ "%s: failed to create match for candidate %{private}@, scanned %{private}@"
+ "%s: failed to get mib length."
+ "%s: falling back to NetIF"
+ "%s: fetching 3bars network for %{mask.hash}@"
+ "%s: link session ended for %{private}@"
+ "%s: link session started for %{private}@"
+ "%s: missing scan match for bssid %{mask.hash}@, candidate %{private}@"
+ "%s: null reqBuf"
+ "%s: performing LQM window analysis for reason %@ (ending this analysis early because the BSSID has changed (%{mask.hash}@ -> %{mask.hash}@)"
+ "%s: profile for %{mask.hash}@ is valid: %{mask.hash}@"
+ "%s: removed %{mask.hash}@ from defaults: %@"
+ "%s: sysctl failed"
+ "%s: visit is a depature, not using for fetching"
+ "'%{mask.hash}@[%{mask.hash}@]' was already %@. Would have blacklisted again due to %@(%lu)"
+ "+[WiFiUsageBssDetails bssWithIdentifier:apProfile:apMode:phyMode:channel:channelFlags:channelWidth:rssi:latitude:longitude:isEdgeBss:]"
+ "+[WiFiUsageInterfaceStats _statsFromMIB:]"
+ "+[WiFiUsageInterfaceStats statsForInterfaceName:]"
+ ","
+ "-[WiFiUsageMonitor setScanningState:client:neighborBSS:otherBSS:withChannelInfoList:withRequest:forInterface:]_block_invoke"
+ "2G"
+ "5G"
+ "5high"
+ "5low"
+ "6G"
+ "<%@:%p "
+ "@28@0:8Q16i24"
+ "@36@0:8Q16Q24B32"
+ "@48@0:8Q16Q24i32Q36B44"
+ "AssertMacros: %s, %s file: %s, line: %d, value: %lld\n"
+ "B32@?0@\"WiFiUsageChannel\"8@\"NSMutableSet\"16^B24"
+ "B:\x1d\x13"
+ "BSS '%{mask.hash}@[%{mask.hash}@]' is due for unblacklisting"
+ "Beacon PER"
+ "Blacklisting and adding '%{mask.hash}@[%{mask.hash}@]' to %@ due to %@(%lu)"
+ "Bytes=%lu "
+ "CHANNELINFO_BAND_NUM"
+ "FW Tx PER"
+ "Gateway ARP Failures"
+ "JoinReasonSetupCount"
+ "JoinReasonSharingCount"
+ "LQM_RW - LQM window analysis for %@ (%@: %@ - %@ ; %@: %@ - %@)\n Network at trigger        : %{private}@\n Network at end of analysis: %{private}@\n Context:\n%@\n Features: %@"
+ "Link down"
+ "Network '%{mask.hash}@' BSSID \"%{mask.hash}@\" isBlacklisted:%s "
+ "RSSI improved"
+ "Roamed"
+ "Rx: Packets=%lu "
+ "SCAN_CHANNELS"
+ "SCAN_TYPE"
+ "Setup"
+ "Sharing"
+ "Skip unblacklisting BSS '%{mask.hash}@[%{mask.hash}@]' - not due."
+ "Symptoms DNS Errors"
+ "T@\"NSDate\",?,R,C,N"
+ "T@\"NSDictionary\",&,N,V_lastScanRequest"
+ "T@\"NSDictionary\",?,&,N"
+ "T@\"NSDictionary\",?,&,N,VuserInfo"
+ "T@\"NSDictionary\",?,R,N"
+ "T@\"NSDictionary\",?,R,N,VresultsByBSSID"
+ "T@\"NSSet\",?,R,N"
+ "T@\"NSString\",?,&,N"
+ "T@\"NSString\",?,&,N,V_etag"
+ "T@\"NSString\",?,R,C"
+ "T@\"NSString\",?,R,C,N"
+ "T@\"TBLocalFetchRequestDescriptor\",?,R,N"
+ "T@\"WiFiUsageInterfaceStats\",&,V_secondaryIfStatsAtLastLqmUpdate"
+ "TB,N,V_colocated6Ghz"
+ "TB,N,V_colocated6GhzIsPSC"
+ "TB,N,V_hasColocatedMLD2G"
+ "TB,N,V_hasColocatedMLD5G"
+ "TB,N,V_hasColocatedMLD6G"
+ "TB,N,V_hasEHT"
+ "TB,N,V_isBSPActive"
+ "TB,N,V_isP2PActiveBSP"
+ "TB,N,V_isScanActiveBSP"
+ "TB,V_isBSPActive"
+ "TD evaluation complete: disconnected the link"
+ "TD evaluation complete: outcome %@"
+ "TD evaluation in progress: high %@ detected"
+ "TQ,?,R,D,N"
+ "TQ,?,R,N"
+ "TQ,N,V_bspAvgMuteMS"
+ "TQ,N,V_bspErrorPercentage"
+ "TQ,N,V_bspMaxConsecutiveFails"
+ "TQ,N,V_bspMaxMuteMS"
+ "TQ,N,V_bspMutePercentage"
+ "TQ,N,V_bspRejectOrFailPercentageOfTriggers"
+ "TQ,N,V_bspTimeOutPercentageOfTriggers"
+ "TQ,N,V_bspTimeToTST"
+ "TQ,N,V_bspTriggerCount"
+ "TQ,N,V_channelWidth"
+ "TQ,N,V_phyMode"
+ "TQ,N,V_rxBytesSecondary"
+ "TQ,N,V_txBytesSecondary"
+ "Td,?,R,N"
+ "Ts: %@>"
+ "Tx PER"
+ "Tx: Packets=%lu "
+ "URL"
+ "Wi-Fi Assist: cellular fallback is active"
+ "Wi-Fi Assist: cellular fallback is inactive"
+ "WiFiNetworkJoinResult"
+ "[15Q]"
+ "[26Q]"
+ "[HUD]: HUD message info: %@"
+ "[HUD]: Missing required class symbols for posting banner, early return with no operation"
+ "[HUD]: attempted to open url: %@"
+ "[HUD]: ignoring empty HUD message info"
+ "[HUD]: open url error: %@"
+ "[TrafficEngineering] (%{mask.hash}s:%{mask.hash}d) active peers %lu, requested peers %lu,  responses %lu, diagnostics log %@"
+ "_bspAvgMuteMS"
+ "_bspErrorPercentage"
+ "_bspMaxConsecutiveFails"
+ "_bspMaxMuteMS"
+ "_bspMutePercentage"
+ "_bspRejectOrFailPercentageOfTriggers"
+ "_bspTimeOutPercentageOfTriggers"
+ "_bspTimeToTST"
+ "_bspTriggerCount"
+ "_hasColocatedMLD2G"
+ "_hasColocatedMLD5G"
+ "_hasColocatedMLD6G"
+ "_hasEHT"
+ "_isBSPActive"
+ "_isP2PActiveBSP"
+ "_isScanActiveBSP"
+ "_lastScanRequest"
+ "_rxBytesSecondary"
+ "_secondaryIfStatsAtLastLqmUpdate"
+ "_statsFromMIB:"
+ "_statsFromNetIF:"
+ "_txBytesSecondary"
+ "absoluteString"
+ "allDimensionsIntoDict:"
+ "bandForBSP"
+ "bandFromChanInfo:"
+ "banner"
+ "bspAvgMuteMS"
+ "bspErrorPercentage"
+ "bspMaxConsecutiveFails"
+ "bspMaxMuteMS"
+ "bspMutePercentage"
+ "bspRejectOrFailPercentageOfTriggers"
+ "bspTimeOutPercentageOfTriggers"
+ "bspTimeToTST"
+ "bspTriggerCount"
+ "channelWithBssDetails:"
+ "channelWithChannelInfo:"
+ "channelWithScanChannel:"
+ "content"
+ "getTDEvalCompleteEventStringForDisplay:"
+ "hasColocatedMLD2G"
+ "hasColocatedMLD5G"
+ "hasColocatedMLD6G"
+ "hasColocatedMLOs"
+ "hasEHT"
+ "i24@0:8@16"
+ "initWithChannel:flags:"
+ "initWithChannel:flags:band:width:isDFS:"
+ "initWithChannel:flags:isDFS:"
+ "initWithName:value:"
+ "isActive"
+ "isBSPActive"
+ "isBspSampleDurationExpected:"
+ "isEHT"
+ "isEqualToInterfaceStats:"
+ "isP2PActiveBSP"
+ "isScanActiveBSP"
+ "lastScanRequest"
+ "member:"
+ "netIFStatsForInterfaceName:"
+ "openURL:configuration:error:"
+ "populateWithBspOverflowed:IsBSPActive:BspTimeToTST:BspSampleDurationMS:IsScanActiveBSP:IsP2PActiveBSP:BspTriggerCount:BspMutePercentage:BspMaxMuteMS:BspAvgMuteMS:BspErrorPercentage:BspTimeOutPercentageOfTriggers:BspRejectOrFailPercentageOfTriggers:BspMaxConsecutiveFails:"
+ "q:"
+ "rxBytesSecondary"
+ "scannedChannels"
+ "secondaryIfStatsAtLastLqmUpdate"
+ "setBspAvgMuteMS:"
+ "setBspErrorPercentage:"
+ "setBspMaxConsecutiveFails:"
+ "setBspMaxMuteMS:"
+ "setBspMutePercentage:"
+ "setBspRejectOrFailPercentageOfTriggers:"
+ "setBspTimeOutPercentageOfTriggers:"
+ "setBspTimeToTST:"
+ "setBspTriggerCount:"
+ "setFrontBoardOptions:"
+ "setHasColocatedMLD2G:"
+ "setHasColocatedMLD5G:"
+ "setHasColocatedMLD6G:"
+ "setHasEHT:"
+ "setHost:"
+ "setIsBSPActive:"
+ "setIsP2PActiveBSP:"
+ "setIsScanActiveBSP:"
+ "setLastScanRequest:"
+ "setQueryItems:"
+ "setRxBytesSecondary:"
+ "setScanningState:client:neighborBSS:otherBSS:withChannelInfoList:withRequest:forInterface:"
+ "setScheme:"
+ "setSecondaryIfStatsAtLastLqmUpdate:"
+ "setTxBytesSecondary:"
+ "subBandForBSPAsStringFromChannel:andBand:"
+ "submitScanResultWithNeighborBSS:withOtherBSS:withChannelInfoList:"
+ "txBytesSecondary"
+ "updateDFSInfoFromSupportedChannels:"
+ "updateIsBSPActive:"
+ "updateWithBspOverflowed:IsBSPActive:BspTimeToTST:BspSampleDurationMS:IsScanActiveBSP:IsP2PActiveBSP:BspTriggerCount:BspMutePercentage:BspMaxMuteMS:BspAvgMuteMS:BspErrorPercentage:BspTimeOutPercentageOfTriggers:BspRejectOrFailPercentageOfTriggers:bspMaxConsecutiveFails:supportsLinkRecommendation:forInterface:"
+ "updateWithTxBytes:RxBytes:TxL3Packets:RxL3Packets:txBytesSecondary:rxBytesSecondary:"
+ "v112@0:8B16B20Q24Q32B40B44Q48Q56Q64Q72Q80Q88Q96Q104"
+ "v124@0:8B16B20Q24Q32B40B44Q48Q56Q64Q72Q80Q88Q96Q104B112@116"
+ "v64@0:8Q16Q24Q32Q40Q48Q56"
+ "v68@0:8B16Q20@28@36@44@52@60"
+ "wifiapp"
+ "\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf01s\x11#\x11\x8f\x0f\x03\xf0\xf0\xf0\x91s\xf0\xf0\xf0\x91\xb2t\xb2S'\x11\xa1\xf0\xa1\x11\xa3"
- "\n\n"
- "\x13\x12\xf0\xf0\xf0a"
- "%@%@%@%@%@%@%@%@%@"
- "%@: maxPHYRate:%d maxNSS:%d linkPHYRate:(max: %d, current: %d)"
- "%s -  SSIDTransitionCandidates(excluding %{public}@):%{public}@\n"
- "%s - bssid:%{public}@ %@Ghz rssi:%@dBm %@"
- "%s - currentBSSID (%{public}@) not in beaconCache"
- "%s - currentBSSID (%{public}@) too short"
- "%s - isUp:%@ details:%@"
- "%s Begin capturing metric for %{public}@[%{public}@] - {oui:%@ blacklistedReason:%@ blacklistedSubreason:%@}"
- "%s Clearing trigger %@ (%@) for '%{public}@[%{public}@]'"
- "%s Clearing(for interval exceeded) trigger %@ (%@) for '%{public}@[%{public}@] (diff:%lu)'"
- "%s Clearing(for interval exceeded) trigger %@ (%@) for '%{public}@[%{public}@]'"
- "%s Finish capturing metric for %{public}@[%{public}@] - {duration:%@ unblacklistReason:%@ prunedCount:%@}"
- "%s Metric for %{public}@[%{public}@] not found!"
- "%s Trigger %@ for [%{public}@] was %f seconds ago and outside window. Will not consider for WoW blacklist"
- "%s Unblacklisting BSS '%{public}@[%{public}@]' for autojoin "
- "%s Unblacklisting and removing '%{public}@[%{public}@]' from Autojoin blacklist"
- "%s Unblacklisting and removing '%{public}@[%{public}@]' from BSS blacklist"
- "%s Unblacklisting and removing '%{public}@[%{public}@]' from WoW blacklist"
- "%s blacklistedNode %{public}@[%{public}@]"
- "%s bssid '%{public}@' %s thresholds. CurrentCount:%d ThresholdCount:%d"
- "%s metric ssid:%{public}@ bssid:%{public}@ doesnt match with node ssid:%{public}@ bssid:%{public}@"
- "%s network %{public}@[%{public}@]"
- "%s node not found with ssid:%{public}@ bssid:%{public}@"
- "%s: %@: roamed from BSSID %{public}@ on channel %d(%@Ghz) to BSSID %{public}@ on channel %d(%@Ghz)"
- "%s: (%{public}@) contains PersonalHotspotIEs:%@ -- skip"
- "%s: (%{public}@) parsingSuccessful: %@ invalidElements:%@ invalidExtElements:%@ -- skip"
- "%s: Apple80211Get returned err %d"
- "%s: BMDeviceWiFi Allocation failed SSID:%@ linkstate:%d "
- "%s: BMPruner NUll - SSID:%@ "
- "%s: BMSource NUll - SSID:%@ linkstate:%d "
- "%s: BMStream NUll - SSID:%@ "
- "%s: BMStream NUll - SSID:%@ linkstate:%d "
- "%s: Do Nothing as WiFiDirectDonation Feature Flag Disabled! details:%@ linkWentUp:%d linkWentDown:%d "
- "%s: Fetching tile key at location=%@, key: %@ zoom: %hhu"
- "%s: InValid inputs details:%@ linkWentUp:%d linkWentDown:%d"
- "%s: Invalid tileKey at location=%@ zoom: %hhu"
- "%s: Trigger '%@' for '%{public}@ [%{public}@]' (reason=%lu reasonData=%ld state=%lu)"
- "%s: Unable to get render server port"
- "%s: bssid %{public}@ has not been derived from a beacon retrieved after the current association (last updated: %@)"
- "%s: failed to create match for candidate %{public}@, scanned %{public}@"
- "%s: fetching 3bars network for %{public}@"
- "%s: link session ended for %@"
- "%s: link session started for %@"
- "%s: mcsIndex %d nss %d bandwidth %d gi %d"
- "%s: missing scan match for bssid %{public}@, candidate %{public}@"
- "%s: performing LQM window analysis for reason %@ (ending this analysis early because the BSSID has changed (%{public}@ -> %{public}@)"
- "%s: poor location accuracy %@"
- "%s: profile for %{public}@ is valid: %{public}@"
- "%s: removed %{public}@ from defaults: %@"
- "%s: visit %@ is a depature, not using for fetching"
- "%s: visit: %@"
- "'%{public}@[%{public}@]' was already %@. Would have blacklisted again due to %@(%lu)"
- "+[WiFiSoftError _updateHUDWithMessage:]"
- "-[WiFiUsageInterfaceCapabilities currentLinkPHYRate]"
- "-[WiFiUsageInterfaceCapabilities maxLinkPHYRate]"
- "-[WiFiUsageMonitor setScanningState:client:neighborBSS:otherBSS:withChannelInfoList:forInterface:]_block_invoke"
- ". Will trigger roaming."
- "2:\x1b\x13"
- "2dB RSSI guard."
- "8S7ydMJ4DlCUF38/hI/fJA"
- "AssertMacros: %s, %s file: %s, line: %d, value: %ld\n"
- "BANDWIDTH"
- "BSS '%{public}@[%{public}@]' is due for unblacklisting"
- "Beacon PER "
- "Blacklisting and adding '%{public}@[%{public}@]' to %@ due to %@(%lu)"
- "FW Tx PER "
- "GI"
- "Gateway ARP Failures "
- "LQM_RW - LQM window analysis for %@ (%@: %@ - %@ ; %@: %@ - %@)\n Network at trigger        : %@\n Network at end of analysis: %@\n Context:\n%@\n Features: %@"
- "MCS_INDEX"
- "MIMOSTATUS_BSSBW"
- "MIMOSTATUS_BSSRXCHAIN"
- "NSS"
- "Network '%{public}@' BSSID \"%{public}@\" isBlacklisted:%s "
- "Skip unblacklisting BSS '%{public}@[%{public}@]' - not due."
- "Starting trigger disconnect evaluation due to: %@"
- "Suppressing Trigger Disconnect due to %@"
- "Symptoms DNS Errors "
- "T@\"NSDate\",R,C,N"
- "T@\"NSDictionary\",&,N"
- "T@\"NSDictionary\",&,N,VuserInfo"
- "T@\"NSDictionary\",R,N,VresultsByBSSID"
- "T@\"NSString\",&,N"
- "T@\"NSString\",&,N,V_etag"
- "T@\"NSString\",N,V_hudOffset"
- "TC,N,V_colocated6Ghz"
- "TC,N,V_colocated6GhzIsPSC"
- "Trigger Disconnect: Disconnected the link due to continued poor quality."
- "Trigger Disconnect: Ending evaluation after : %@"
- "Trigger Disconnect: Observing high %@"
- "Tx PER "
- "WiFi link conditions improved, WiFi icon is back!"
- "WiFi-assist kicked-in due to bad link conditions, WiFi icon is taken away!"
- "[13Q]"
- "[22Q]"
- "[TrafficEngineering] (%{public}s:%{public}d) active peers %lu, requested peers %lu,  responses %lu, diagnostics log %@"
- "_hudOffset"
- "active probing."
- "appendChannelInfoToDict:from:"
- "band = %lu"
- "better app policy score from Symptoms."
- "channelWithBssDetails:andChannelInfoList:"
- "currentLinkPHYRate"
- "dfsChannel:"
- "getTDExecutionStateEventStringForDisplay:"
- "good datastall score from Symptoms."
- "hudOffset"
- "improved TxPER."
- "maxLinkPHYRate"
- "no FG networking app."
- "no availability of cheap cellular data."
- "q5\x15"
- "setHudOffset:"
- "setScanningState:client:neighborBSS:otherBSS:withChannelInfoList:forInterface:"
- "updateWithTxBytes:RxBytes:TxL3Packets:RxL3Packets:"
- "user's input."
- "user's previous input on TapToRadar."
- "v48@0:8Q16Q24Q32Q40"
- "v60@0:8B16Q20@28@36@44@52"
- "\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xa1s\x11#\x11\x8f\x0f\x03\xf0\xf0\xf0\x91s\xf0\xf0\xf0\x91\xb2t\xb2S'\x11\xa1\xf0\xa1\x11\xa3"

```
