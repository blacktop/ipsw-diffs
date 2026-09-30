## WiFiAnalytics

> `/System/Library/PrivateFrameworks/WiFiAnalytics.framework/WiFiAnalytics`

```diff

-776.70.0.0.0
-  __TEXT.__text: 0x125a90
-  __TEXT.__auth_stubs: 0x1010
-  __TEXT.__objc_methlist: 0xeb50
-  __TEXT.__const: 0x300
+776.79.0.0.0
+  __TEXT.__text: 0x12b224
+  __TEXT.__auth_stubs: 0x1030
+  __TEXT.__objc_methlist: 0xef98
+  __TEXT.__const: 0x310
   __TEXT.__dlopen_cstrs: 0x56
-  __TEXT.__cstring: 0x11c28
-  __TEXT.__oslogstring: 0xdfa8
-  __TEXT.__constg_swiftt: 0x190
-  __TEXT.__swift5_typeref: 0x107
-  __TEXT.__swift5_reflstr: 0x61
-  __TEXT.__swift5_fieldmd: 0x70
+  __TEXT.__cstring: 0x11f87
+  __TEXT.__oslogstring: 0xe36b
+  __TEXT.__constg_swiftt: 0x1e0
+  __TEXT.__swift5_typeref: 0x14b
+  __TEXT.__swift5_reflstr: 0xb1
+  __TEXT.__swift5_fieldmd: 0x88
   __TEXT.__swift5_capture: 0x2d0
   __TEXT.__swift5_types: 0x4
-  __TEXT.__gcc_except_tab: 0x2b60
-  __TEXT.__unwind_info: 0x2648
-  __TEXT.__eh_frame: 0x578
-  __TEXT.__objc_classname: 0xe31
-  __TEXT.__objc_methname: 0x1e92e
-  __TEXT.__objc_methtype: 0x3c42
-  __TEXT.__objc_stubs: 0xc8e0
-  __DATA_CONST.__got: 0x720
-  __DATA_CONST.__const: 0x1ec8
-  __DATA_CONST.__objc_classlist: 0x3d8
+  __TEXT.__gcc_except_tab: 0x2c28
+  __TEXT.__unwind_info: 0x2698
+  __TEXT.__eh_frame: 0x548
+  __TEXT.__objc_classname: 0xe69
+  __TEXT.__objc_methname: 0x1f0f5
+  __TEXT.__objc_methtype: 0x3d8a
+  __TEXT.__objc_stubs: 0xcae0
+  __DATA_CONST.__got: 0x730
+  __DATA_CONST.__const: 0x1eb0
+  __DATA_CONST.__objc_classlist: 0x3e0
   __DATA_CONST.__objc_catlist: 0x8
-  __DATA_CONST.__objc_protolist: 0x38
+  __DATA_CONST.__objc_protolist: 0x40
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x7e90
+  __DATA_CONST.__objc_selrefs: 0x80d8
   __DATA_CONST.__objc_protorefs: 0x8
-  __DATA_CONST.__objc_superrefs: 0x2b8
-  __DATA_CONST.__objc_arraydata: 0x488
-  __AUTH_CONST.__auth_got: 0x818
+  __DATA_CONST.__objc_superrefs: 0x2c0
+  __DATA_CONST.__objc_arraydata: 0x490
+  __AUTH_CONST.__auth_got: 0x828
   __AUTH_CONST.__const: 0x1670
-  __AUTH_CONST.__cfstring: 0xcf00
-  __AUTH_CONST.__objc_const: 0x14690
-  __AUTH_CONST.__objc_intobj: 0x240
-  __AUTH_CONST.__objc_arrayobj: 0x5b8
+  __AUTH_CONST.__cfstring: 0xd1c0
+  __AUTH_CONST.__objc_const: 0x14bf8
+  __AUTH_CONST.__objc_intobj: 0x258
+  __AUTH_CONST.__objc_arrayobj: 0x5d0
   __AUTH_CONST.__objc_dictobj: 0x28
-  __AUTH.__objc_data: 0x4f8
-  __DATA.__objc_ivar: 0xf08
-  __DATA.__data: 0x318
+  __AUTH.__objc_data: 0x548
+  __DATA.__objc_ivar: 0xf4c
+  __DATA.__data: 0x3a8
   __DATA.__bss: 0x1c
   __DATA.__common: 0x11d0
-  __DATA_DIRTY.__objc_data: 0x2368
+  __DATA_DIRTY.__objc_data: 0x23c8
   __DATA_DIRTY.__data: 0x90
   __DATA_DIRTY.__bss: 0x150
   __DATA_DIRTY.__common: 0x28

   - /usr/lib/libobjc.A.dylib
   - /usr/lib/swift/libswiftCore.dylib
   - /usr/lib/swift/libswiftCoreFoundation.dylib
-  - /usr/lib/swift/libswiftDarwin.dylib
   - /usr/lib/swift/libswiftDispatch.dylib
   - /usr/lib/swift/libswiftObjectiveC.dylib
   - /usr/lib/swift/libswiftXPC.dylib
   - /usr/lib/swift/libswift_Builtin_float.dylib
-  - /usr/lib/swift/libswift_DarwinFoundation1.dylib
-  - /usr/lib/swift/libswift_DarwinFoundation2.dylib
-  - /usr/lib/swift/libswift_DarwinFoundation3.dylib
   - /usr/lib/swift/libswiftos.dylib
-  UUID: E255517D-3CD0-3C4A-8E49-C3897389EA58
-  Functions: 5472
-  Symbols:   15023
-  CStrings:  11549
+  UUID: EC900E6E-0C82-328A-A2B1-5887DA0B1171
+  Functions: 5570
+  Symbols:   15238
+  CStrings:  11727
 
Symbols:
+ +[RoamPolicyStore neighborChannelsAsArrayOfChanInfo:]
+ +[RoamPolicyStore neighborChannelsOf:]
+ +[UniqueMO aggregateName]
+ +[UsageHelper aggregateNameFor:withError:]
+ +[UsageMO aggregateName]
+ +[WADeviceAnalyticsClient aggregateNameFor:withError:]
+ +[WADeviceAnalyticsUsageDimension dimensionsUsedAsFilterIn:]
+ +[WADeviceAnalyticsUsageDimension dimensionsUsedAsGroupBy:]
+ +[WAUtil filterArray:usingPredicate:]
+ +[WAUtil filterSet:usingPredicate:]
+ -[AnalyticsProcessor performPruneTestEntity:since:withPredicate:withError:]
+ -[LANMO isEnterprise]
+ -[LANMO isPublic]
+ -[NetworkMO isEnterprise]
+ -[UsagePoliciesHandler checkMissingBandsIn:from:to:]
+ -[UsagePoliciesHandler updateUniqueMO:withConstraints:fromStats:aggregatedOn:withTotal:timespan:prevPercentile:]
+ -[WADeploymentAnalyzer updateHomeNetworksForDeploymentIssuesWithReason:withError:]
+ -[WADeploymentAnalyzer updateNetworksForCoverageIssues:withReason:withError:]
+ -[WADeploymentIssuesMetric secondsSinceLastRun]
+ -[WADeploymentIssuesMetric setSecondsSinceLastRun:]
+ -[WADeviceAnalyticsClient performPruneTestBSSes:networks:lans:withError:]
+ -[WADeviceAnalyticsClient performPruneTestEntity:since:withPredicate:withError:]
+ -[WADeviceAnalytics_DHCPServerInfo hash]
+ -[WALQM description]
+ -[WAPersistentContainer batchDelete:newerThanDate:andPredicate:withError:]
+ -[WAPersistentContainer espressionWithAggregateFunction:overField:called:]
+ -[WiFiAnalyticsAWDWiFiNWActivityInterfaceStats hasRxStall]
+ -[WiFiAnalyticsAWDWiFiNWActivityInterfaceStats rxStall]
+ -[WiFiAnalyticsAWDWiFiNWActivityInterfaceStats setRxStall:]
+ -[WiFiAnalyticsAWDWiFiRxDataStallStats copyTo:]
+ -[WiFiAnalyticsAWDWiFiRxDataStallStats copyWithZone:]
+ -[WiFiAnalyticsAWDWiFiRxDataStallStats description]
+ -[WiFiAnalyticsAWDWiFiRxDataStallStats dictionaryRepresentation]
+ -[WiFiAnalyticsAWDWiFiRxDataStallStats hasHealthcheckFaultsRtscts]
+ -[WiFiAnalyticsAWDWiFiRxDataStallStats hasHealthcheckFaults]
+ -[WiFiAnalyticsAWDWiFiRxDataStallStats hasRxMuPpdu]
+ -[WiFiAnalyticsAWDWiFiRxDataStallStats hasRxMuRts]
+ -[WiFiAnalyticsAWDWiFiRxDataStallStats hasRxTotalPpdu]
+ -[WiFiAnalyticsAWDWiFiRxDataStallStats hasSrMuRtsNoUcast]
+ -[WiFiAnalyticsAWDWiFiRxDataStallStats hasSrRtsCtsNoUcast]
+ -[WiFiAnalyticsAWDWiFiRxDataStallStats hasSrStallInProgress]
+ -[WiFiAnalyticsAWDWiFiRxDataStallStats hasSrTimNoUcast]
+ -[WiFiAnalyticsAWDWiFiRxDataStallStats hasSrTxBlanking]
+ -[WiFiAnalyticsAWDWiFiRxDataStallStats hasStallAge]
+ -[WiFiAnalyticsAWDWiFiRxDataStallStats hasStallElapsedDur]
+ -[WiFiAnalyticsAWDWiFiRxDataStallStats hasTxCtsNoUcast]
+ -[WiFiAnalyticsAWDWiFiRxDataStallStats hasTxCtsRxUcast]
+ -[WiFiAnalyticsAWDWiFiRxDataStallStats hash]
+ -[WiFiAnalyticsAWDWiFiRxDataStallStats healthcheckFaultsRtscts]
+ -[WiFiAnalyticsAWDWiFiRxDataStallStats healthcheckFaults]
+ -[WiFiAnalyticsAWDWiFiRxDataStallStats isEqual:]
+ -[WiFiAnalyticsAWDWiFiRxDataStallStats mergeFrom:]
+ -[WiFiAnalyticsAWDWiFiRxDataStallStats readFrom:]
+ -[WiFiAnalyticsAWDWiFiRxDataStallStats rxMuPpdu]
+ -[WiFiAnalyticsAWDWiFiRxDataStallStats rxMuRts]
+ -[WiFiAnalyticsAWDWiFiRxDataStallStats rxTotalPpdu]
+ -[WiFiAnalyticsAWDWiFiRxDataStallStats setHasHealthcheckFaults:]
+ -[WiFiAnalyticsAWDWiFiRxDataStallStats setHasHealthcheckFaultsRtscts:]
+ -[WiFiAnalyticsAWDWiFiRxDataStallStats setHasRxMuPpdu:]
+ -[WiFiAnalyticsAWDWiFiRxDataStallStats setHasRxMuRts:]
+ -[WiFiAnalyticsAWDWiFiRxDataStallStats setHasRxTotalPpdu:]
+ -[WiFiAnalyticsAWDWiFiRxDataStallStats setHasSrMuRtsNoUcast:]
+ -[WiFiAnalyticsAWDWiFiRxDataStallStats setHasSrRtsCtsNoUcast:]
+ -[WiFiAnalyticsAWDWiFiRxDataStallStats setHasSrStallInProgress:]
+ -[WiFiAnalyticsAWDWiFiRxDataStallStats setHasSrTimNoUcast:]
+ -[WiFiAnalyticsAWDWiFiRxDataStallStats setHasSrTxBlanking:]
+ -[WiFiAnalyticsAWDWiFiRxDataStallStats setHasStallAge:]
+ -[WiFiAnalyticsAWDWiFiRxDataStallStats setHasStallElapsedDur:]
+ -[WiFiAnalyticsAWDWiFiRxDataStallStats setHasTxCtsNoUcast:]
+ -[WiFiAnalyticsAWDWiFiRxDataStallStats setHasTxCtsRxUcast:]
+ -[WiFiAnalyticsAWDWiFiRxDataStallStats setHealthcheckFaults:]
+ -[WiFiAnalyticsAWDWiFiRxDataStallStats setHealthcheckFaultsRtscts:]
+ -[WiFiAnalyticsAWDWiFiRxDataStallStats setRxMuPpdu:]
+ -[WiFiAnalyticsAWDWiFiRxDataStallStats setRxMuRts:]
+ -[WiFiAnalyticsAWDWiFiRxDataStallStats setRxTotalPpdu:]
+ -[WiFiAnalyticsAWDWiFiRxDataStallStats setSrMuRtsNoUcast:]
+ -[WiFiAnalyticsAWDWiFiRxDataStallStats setSrRtsCtsNoUcast:]
+ -[WiFiAnalyticsAWDWiFiRxDataStallStats setSrStallInProgress:]
+ -[WiFiAnalyticsAWDWiFiRxDataStallStats setSrTimNoUcast:]
+ -[WiFiAnalyticsAWDWiFiRxDataStallStats setSrTxBlanking:]
+ -[WiFiAnalyticsAWDWiFiRxDataStallStats setStallAge:]
+ -[WiFiAnalyticsAWDWiFiRxDataStallStats setStallElapsedDur:]
+ -[WiFiAnalyticsAWDWiFiRxDataStallStats setTxCtsNoUcast:]
+ -[WiFiAnalyticsAWDWiFiRxDataStallStats setTxCtsRxUcast:]
+ -[WiFiAnalyticsAWDWiFiRxDataStallStats srMuRtsNoUcast]
+ -[WiFiAnalyticsAWDWiFiRxDataStallStats srRtsCtsNoUcast]
+ -[WiFiAnalyticsAWDWiFiRxDataStallStats srStallInProgress]
+ -[WiFiAnalyticsAWDWiFiRxDataStallStats srTimNoUcast]
+ -[WiFiAnalyticsAWDWiFiRxDataStallStats srTxBlanking]
+ -[WiFiAnalyticsAWDWiFiRxDataStallStats stallAge]
+ -[WiFiAnalyticsAWDWiFiRxDataStallStats stallElapsedDur]
+ -[WiFiAnalyticsAWDWiFiRxDataStallStats txCtsNoUcast]
+ -[WiFiAnalyticsAWDWiFiRxDataStallStats txCtsRxUcast]
+ -[WiFiAnalyticsAWDWiFiRxDataStallStats writeTo:]
+ GCC_except_table101
+ GCC_except_table103
+ GCC_except_table140
+ GCC_except_table142
+ GCC_except_table154
+ GCC_except_table160
+ GCC_except_table166
+ GCC_except_table172
+ GCC_except_table178
+ GCC_except_table252
+ GCC_except_table74
+ GCC_except_table80
+ GCC_except_table82
+ GCC_except_table86
+ GCC_except_table89
+ GCC_except_table91
+ GCC_except_table93
+ GCC_except_table95
+ GCC_except_table97
+ GCC_except_table99
+ OBJC_IVAR_$_WiFiAnalyticsAWDWiFiNWActivityInterfaceStats._rxStall
+ OBJC_IVAR_$_WiFiAnalyticsAWDWiFiRxDataStallStats._has
+ OBJC_IVAR_$_WiFiAnalyticsAWDWiFiRxDataStallStats._healthcheckFaults
+ OBJC_IVAR_$_WiFiAnalyticsAWDWiFiRxDataStallStats._healthcheckFaultsRtscts
+ OBJC_IVAR_$_WiFiAnalyticsAWDWiFiRxDataStallStats._rxMuPpdu
+ OBJC_IVAR_$_WiFiAnalyticsAWDWiFiRxDataStallStats._rxMuRts
+ OBJC_IVAR_$_WiFiAnalyticsAWDWiFiRxDataStallStats._rxTotalPpdu
+ OBJC_IVAR_$_WiFiAnalyticsAWDWiFiRxDataStallStats._srMuRtsNoUcast
+ OBJC_IVAR_$_WiFiAnalyticsAWDWiFiRxDataStallStats._srRtsCtsNoUcast
+ OBJC_IVAR_$_WiFiAnalyticsAWDWiFiRxDataStallStats._srStallInProgress
+ OBJC_IVAR_$_WiFiAnalyticsAWDWiFiRxDataStallStats._srTimNoUcast
+ OBJC_IVAR_$_WiFiAnalyticsAWDWiFiRxDataStallStats._srTxBlanking
+ OBJC_IVAR_$_WiFiAnalyticsAWDWiFiRxDataStallStats._stallAge
+ OBJC_IVAR_$_WiFiAnalyticsAWDWiFiRxDataStallStats._stallElapsedDur
+ OBJC_IVAR_$_WiFiAnalyticsAWDWiFiRxDataStallStats._txCtsNoUcast
+ OBJC_IVAR_$_WiFiAnalyticsAWDWiFiRxDataStallStats._txCtsRxUcast
+ _OBJC_CLASS_$_WiFiAnalyticsAWDWiFiRxDataStallStats
+ _OBJC_IVAR_$_WADeploymentIssuesMetric._secondsSinceLastRun
+ _OBJC_METACLASS_$_WiFiAnalyticsAWDWiFiRxDataStallStats
+ _WiFiAnalyticsAWDWiFiRxDataStallStatsReadFrom
+ __OBJC_$_INSTANCE_METHODS_LANMO
+ __OBJC_$_INSTANCE_METHODS_WiFiAnalyticsAWDWiFiRxDataStallStats
+ __OBJC_$_INSTANCE_VARIABLES_WiFiAnalyticsAWDWiFiRxDataStallStats
+ __OBJC_$_PROP_LIST_WiFiAnalyticsAWDWiFiRxDataStallStats
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_DeploymentProtocol
+ __OBJC_$_PROTOCOL_METHOD_TYPES_DeploymentProtocol
+ __OBJC_$_PROTOCOL_REFS_DeploymentProtocol
+ __OBJC_CLASS_PROTOCOLS_$_WiFiAnalyticsAWDWiFiRxDataStallStats
+ __OBJC_CLASS_RO_$_WiFiAnalyticsAWDWiFiRxDataStallStats
+ __OBJC_LABEL_PROTOCOL_$_DeploymentProtocol
+ __OBJC_METACLASS_RO_$_WiFiAnalyticsAWDWiFiRxDataStallStats
+ __OBJC_PROTOCOL_$_DeploymentProtocol
+ ___47-[WAPersistentContainer batchDelete:withError:]_block_invoke.260
+ ___73-[WADeviceAnalyticsClient performPruneTestBSSes:networks:lans:withError:]_block_invoke
+ ___80-[WADeviceAnalyticsClient performPruneTestEntity:since:withPredicate:withError:]_block_invoke
+ ___NSArray0__struct
+ ___block_descriptor_56_e8_32s40s48r_e19_"NSDictionary"8?0lr48l8s32l8s40l8
+ ___block_descriptor_80_e8_32s40s48s56s64r72r_e5_v8?0lr64l8s32l8s40l8s48l8s56l8r72l8
+ ___block_literal_global.228
+ __swiftEmptySetSingleton
+ _kWAMessageMetricNameCarPlayJoinFailureMetrics
+ _objc_msgSend$aggregateName
+ _objc_msgSend$aggregateNameFor:withError:
+ _objc_msgSend$anyObject
+ _objc_msgSend$batchDelete:newerThanDate:andPredicate:withError:
+ _objc_msgSend$checkMissingBandsIn:from:to:
+ _objc_msgSend$dimensionsUsedAsFilterIn:
+ _objc_msgSend$dimensionsUsedAsGroupBy:
+ _objc_msgSend$espressionWithAggregateFunction:overField:called:
+ _objc_msgSend$filterArray:usingPredicate:
+ _objc_msgSend$filterSet:usingPredicate:
+ _objc_msgSend$isEnterprise
+ _objc_msgSend$isPublic
+ _objc_msgSend$neighborChannelsAsArrayOfChanInfo:
+ _objc_msgSend$neighborChannelsOf:
+ _objc_msgSend$networkFlags
+ _objc_msgSend$performPruneTestEntity:since:withPredicate:withError:
+ _objc_msgSend$secondsSinceLastRun
+ _objc_msgSend$setIsPublic:
+ _objc_msgSend$setRxStall:
+ _objc_msgSend$setSecondsSinceLastRun:
+ _objc_msgSend$unionSet:
+ _objc_msgSend$updateHomeNetworksForDeploymentIssuesWithReason:withError:
+ _objc_msgSend$updateNetworksForCoverageIssues:withReason:withError:
+ _objc_msgSend$updateUniqueMO:withConstraints:fromStats:aggregatedOn:withTotal:timespan:prevPercentile:
+ _swift_bridgeObjectRetain_n
+ _symbolic SS6prefix_SS6suffixt
+ _symbolic _____Sg 10Foundation6LocaleV
+ _symbolic _____ySS6prefix_SS6suffixtG s23_ContiguousArrayStorageC
+ _symbolic _____ySSG s11_SetStorageC
- +[RoamPolicyStore neighborChannelsAsArray:]
- -[AnalyticsProcessor performPruneTestEntity:since:withError:]
- -[UsagePoliciesHandler updateUniqueMO:withConstraints:fromStats:withTotal:timespan:prevPercentile:]
- -[WADeploymentAnalyzer updateHomeNetworksForDeploymentIssuesWithError:]
- -[WADeploymentAnalyzer updateNetworksForCoverageIssues:withError:]
- -[WADeviceAnalyticsClient performPruneTestBSSes:withError:]
- -[WADeviceAnalyticsClient performPruneTestEntity:since:withError:]
- -[WAPersistentContainer batchDelete:newerThanDate:withError:]
- -[WAPersistentContainer espressionWithAggregateFunction:overField:]
- GCC_except_table100
- GCC_except_table102
- GCC_except_table104
- GCC_except_table124
- GCC_except_table137
- GCC_except_table139
- GCC_except_table141
- GCC_except_table153
- GCC_except_table159
- GCC_except_table165
- GCC_except_table171
- GCC_except_table177
- GCC_except_table65
- GCC_except_table73
- GCC_except_table79
- GCC_except_table81
- GCC_except_table83
- GCC_except_table85
- GCC_except_table92
- GCC_except_table94
- _OBJC_CLASS_$_NSRegularExpression
- ___47-[WAPersistentContainer batchDelete:withError:]_block_invoke.261
- ___53-[AnalyticsProcessor poorCoverageAnalysisWithReason:]_block_invoke
- ___59-[WADeviceAnalyticsClient performPruneTestBSSes:withError:]_block_invoke
- ___66-[WADeviceAnalyticsClient performPruneTestEntity:since:withError:]_block_invoke
- ___block_descriptor_40_e8_32r_e19_"NSDictionary"8?0lr32l8
- ___block_descriptor_72_e8_32s40s48s56r64r_e5_v8?0lr56l8s32l8s40l8s48l8r64l8
- ___block_literal_global.242
- __swift_FORCE_LOAD_$_swiftDarwin
- __swift_FORCE_LOAD_$_swiftDarwin_$_WiFiAnalytics
- __swift_FORCE_LOAD_$_swift_DarwinFoundation1
- __swift_FORCE_LOAD_$_swift_DarwinFoundation1_$_WiFiAnalytics
- __swift_FORCE_LOAD_$_swift_DarwinFoundation2
- __swift_FORCE_LOAD_$_swift_DarwinFoundation2_$_WiFiAnalytics
- __swift_FORCE_LOAD_$_swift_DarwinFoundation3
- __swift_FORCE_LOAD_$_swift_DarwinFoundation3_$_WiFiAnalytics
- _objc_msgSend$batchDelete:newerThanDate:withError:
- _objc_msgSend$bssesCount
- _objc_msgSend$espressionWithAggregateFunction:overField:
- _objc_msgSend$neighborChannelsAsArray:
- _objc_msgSend$performPruneTestEntity:since:withError:
- _objc_msgSend$updateHomeNetworksForDeploymentIssuesWithError:
- _objc_msgSend$updateNetworksForCoverageIssues:withError:
- _objc_msgSend$updateUniqueMO:withConstraints:fromStats:withTotal:timespan:prevPercentile:
- _objc_retain_x28
CStrings:
+ "%@(%u) %lus"
+ "%{public}s::%d:%@ is %@ %@ %@ -- ignoring for telemetry"
+ "%{public}s::%d:%@ most recently seen at %@ (%@) earlier than lastClassifyTrains run (%@) -- skipping"
+ "%{public}s::%d:%s - Pruning %@"
+ "%{public}s::%d:Class %@ does not implement aggregateName"
+ "%{public}s::%d:Class %@ for %@ does not implement aggregateName"
+ "%{public}s::%d:Failed to get WAClient sharedClient instance"
+ "%{public}s::%d:Last Complete %@ has already been used to update %@ - skipping"
+ "%{public}s::%d:This function runs on entities whose class adopts DeploymentProtocol"
+ "%{public}s::%d:Unable to fetch agrgegateName for Weekly Usage Table"
+ "%{public}s::%d:Unable to filter array %@ on %@: %@"
+ "%{public}s::%d:Unable to filter set %@ on %@: %@"
+ "%{public}s::%d:Updated LAN for %@ (networksCount:%lu bsses.count:%lu)"
+ "%{public}s::%d:no recent roams from %@"
+ "%{public}s::%d:no roams from %@"
+ "%{public}s::%d:object:%@(%@) prefix:%@ --> %@"
+ "%{public}s::%d:submitting %@: %@"
+ "%{public}s::%d:unable to fetch all BSSes in Networks %@: %@"
+ "+[UsageHelper aggregateNameFor:withError:]"
+ "+[WAClient sharedClientWithIdentifier:]"
+ "+[WAUtil filterArray:usingPredicate:]"
+ "+[WAUtil filterSet:usingPredicate:]"
+ "-[UsagePoliciesHandler updateUniqueMO:withConstraints:fromStats:aggregatedOn:withTotal:timespan:prevPercentile:]"
+ "-[WAClient submitWiFiAnalytics:data:]"
+ "-[WAClient submitWiFiAnalytics:data:]_block_invoke"
+ "-[WADeploymentAnalyzer updateHomeNetworksForDeploymentIssuesWithReason:withError:]"
+ "-[WADeploymentAnalyzer updateNetworksForCoverageIssues:withReason:withError:]"
+ "-[WADeviceAnalyticsClient performPruneTestBSSes:networks:lans:withError:]_block_invoke"
+ "-[WADeviceAnalyticsClient performPruneTestEntity:since:withPredicate:withError:]"
+ "-[WAPersistentContainer batchDelete:newerThanDate:andPredicate:withError:]"
+ "@\"WiFiAnalyticsAWDWiFiRxDataStallStats\""
+ "@72@0:8@16@24@32@40Q48Q56^Q64"
+ "Calculated timeOffset between samples is negative %f"
+ "DeploymentProtocol"
+ "Enterprise"
+ "Public"
+ "Q48@0:8@16@24@32^@40"
+ "SELF.network.authFlags != nil && (SELF.network.authFlags & %u) != 0"
+ "SELF.network.isPublic = YES"
+ "Setting allowSingleFragmentDeltaCalculations true due to negative timeOffset %f or growth in metrics from early %ld to late %ld, rerunning diff"
+ "Setting allowSingleFragmentDeltaCalculations true due to singleFragment"
+ "T@\"WiFiAnalyticsAWDWiFiRxDataStallStats\",&,N,V_rxStall"
+ "TQ,N,V_healthcheckFaults"
+ "TQ,N,V_healthcheckFaultsRtscts"
+ "TQ,N,V_rxMuPpdu"
+ "TQ,N,V_rxMuRts"
+ "TQ,N,V_rxTotalPpdu"
+ "TQ,N,V_secondsSinceLastRun"
+ "TQ,N,V_srMuRtsNoUcast"
+ "TQ,N,V_srRtsCtsNoUcast"
+ "TQ,N,V_srStallInProgress"
+ "TQ,N,V_srTimNoUcast"
+ "TQ,N,V_srTxBlanking"
+ "TQ,N,V_stallAge"
+ "TQ,N,V_stallElapsedDur"
+ "TQ,N,V_txCtsNoUcast"
+ "TQ,N,V_txCtsRxUcast"
+ "WADeploymentAnalyzer updateNetworksForCoverageIssues:"
+ "WiFiAnalytics-776.79 Jun 18 2025 20:51:35"
+ "WiFiAnalytics-776.79 Jun 18 2025 20:51:36"
+ "WiFiAnalyticsAWDWiFiRxDataStallStats"
+ "_XX:XX:XX:XX:XX:XX_"
+ "_[0-9A-Fa-f]{2}(?::[0-9A-Fa-f]{2}){5}_"
+ "_healthcheckFaults"
+ "_healthcheckFaultsRtscts"
+ "_rxMuPpdu"
+ "_rxMuRts"
+ "_rxStall"
+ "_rxTotalPpdu"
+ "_secondsSinceLastRun"
+ "_srMuRtsNoUcast"
+ "_srRtsCtsNoUcast"
+ "_srStallInProgress"
+ "_srTimNoUcast"
+ "_srTxBlanking"
+ "_stallAge"
+ "_stallElapsedDur"
+ "_txCtsNoUcast"
+ "_txCtsRxUcast"
+ "aggregateName"
+ "aggregateNameFor:withError:"
+ "allowSingleFragmentDeltaCalculations"
+ "anyObject"
+ "batchDelete:newerThanDate:andPredicate:withError:"
+ "checkMissingBandsIn:from:to:"
+ "com.apple.wifi.CarPlayJoinFailureMetrics"
+ "dimensionsUsedAsFilterIn:"
+ "dimensionsUsedAsGroupBy:"
+ "espressionWithAggregateFunction:overField:called:"
+ "filterArray:usingPredicate:"
+ "filterSet:usingPredicate:"
+ "has more than MaxBssInDeployment bss"
+ "hasHealthcheckFaults"
+ "hasHealthcheckFaultsRtscts"
+ "hasRxMuPpdu"
+ "hasRxMuRts"
+ "hasRxStall"
+ "hasRxTotalPpdu"
+ "hasSrMuRtsNoUcast"
+ "hasSrRtsCtsNoUcast"
+ "hasSrStallInProgress"
+ "hasSrTimNoUcast"
+ "hasSrTxBlanking"
+ "hasStallAge"
+ "hasStallElapsedDur"
+ "hasTxCtsNoUcast"
+ "hasTxCtsRxUcast"
+ "healthcheckFaults"
+ "healthcheckFaultsRtscts"
+ "healthcheck_faults"
+ "healthcheck_faults_rtscts"
+ "i32@0:8[3B]16i24i28"
+ "ignoreEnterpriseNetworks"
+ "ignorePublicNetworks"
+ "isEnterprise"
+ "isPublic"
+ "neighborChannelsAsArrayOfChanInfo:"
+ "neighborChannelsOf:"
+ "network.ssid IN %@"
+ "performPerPeerCalculations"
+ "performPruneTestBSSes:networks:lans:withError:"
+ "performPruneTestEntity:since:withPredicate:withError:"
+ "rxMuPpdu"
+ "rxMuRts"
+ "rxStall"
+ "rxTotalPpdu"
+ "rx_mu_ppdu"
+ "rx_mu_rts"
+ "rx_total_ppdu"
+ "secondsSinceLastRun"
+ "setHasHealthcheckFaults:"
+ "setHasHealthcheckFaultsRtscts:"
+ "setHasRxMuPpdu:"
+ "setHasRxMuRts:"
+ "setHasRxTotalPpdu:"
+ "setHasSrMuRtsNoUcast:"
+ "setHasSrRtsCtsNoUcast:"
+ "setHasSrStallInProgress:"
+ "setHasSrTimNoUcast:"
+ "setHasSrTxBlanking:"
+ "setHasStallAge:"
+ "setHasStallElapsedDur:"
+ "setHasTxCtsNoUcast:"
+ "setHasTxCtsRxUcast:"
+ "setHealthcheckFaults:"
+ "setHealthcheckFaultsRtscts:"
+ "setIsPublic:"
+ "setRxMuPpdu:"
+ "setRxMuRts:"
+ "setRxStall:"
+ "setRxTotalPpdu:"
+ "setSecondsSinceLastRun:"
+ "setSrMuRtsNoUcast:"
+ "setSrRtsCtsNoUcast:"
+ "setSrStallInProgress:"
+ "setSrTimNoUcast:"
+ "setSrTxBlanking:"
+ "setStallAge:"
+ "setStallElapsedDur:"
+ "setTxCtsNoUcast:"
+ "setTxCtsRxUcast:"
+ "srMuRtsNoUcast"
+ "srRtsCtsNoUcast"
+ "srStallInProgress"
+ "srTimNoUcast"
+ "srTxBlanking"
+ "sr_mu_rts_no_ucast"
+ "sr_rts_cts_no_ucast"
+ "sr_stall_in_progress"
+ "sr_tim_no_ucast"
+ "sr_tx_blanking"
+ "stallAge"
+ "stallElapsedDur"
+ "stall_age"
+ "stall_elapsed_dur"
+ "txCtsNoUcast"
+ "txCtsRxUcast"
+ "tx_cts_no_ucast"
+ "tx_cts_rx_ucast"
+ "unionSet:"
+ "updateHomeNetworksForDeploymentIssuesWithReason:withError:"
+ "updateNetworksForCoverageIssues:withReason:withError:"
+ "updateUniqueMO:withConstraints:fromStats:aggregatedOn:withTotal:timespan:prevPercentile:"
+ "{?=\"healthcheckFaults\"b1\"healthcheckFaultsRtscts\"b1\"rxMuPpdu\"b1\"rxMuRts\"b1\"rxTotalPpdu\"b1\"srMuRtsNoUcast\"b1\"srRtsCtsNoUcast\"b1\"srStallInProgress\"b1\"srTimNoUcast\"b1\"srTxBlanking\"b1\"stallAge\"b1\"stallElapsedDur\"b1\"txCtsNoUcast\"b1\"txCtsRxUcast\"b1}"
- "%@ > %@"
- "%{public}s::%d:Last Complete %@ has already been used to update %@"
- "%{public}s::%d:NSExpression threw exception: %@"
- "%{public}s::%d:Updated LAN for %@ (networksCount:%lu bssesCount:%lu)"
- "%{public}s::%d:roamManagedObject is nil"
- "+[UsageMO usageOf:timeSpan:around:onContainer:withError:]"
- "-[AnalyticsProcessor poorCoverageAnalysisWithReason:]_block_invoke"
- "-[UsagePoliciesHandler updateUniqueMO:withConstraints:fromStats:withTotal:timespan:prevPercentile:]"
- "-[WADeploymentAnalyzer updateHomeNetworksForDeploymentIssuesWithError:]"
- "-[WADeploymentAnalyzer updateNetworksForCoverageIssues:withError:]"
- "-[WADeviceAnalyticsClient performPruneTestEntity:since:withError:]"
- "-[WAPersistentContainer batchDelete:newerThanDate:withError:]"
- "@64@0:8@16@24@32Q40Q48^Q56"
- "Either early or later dictionaries must contain at least one entry"
- "WADeploymentAnalyzer updateHomeNetworksForLowSignal"
- "WiFiAnalytics-776.70 May 30 2025 19:19:33"
- "WiFiAnalytics-776.70 May 30 2025 19:19:34"
- "WiFiAnalytics/WANWActivityTransform.swift"
- "batchDelete:newerThanDate:withError:"
- "bss.lastSeen"
- "bssesCount"
- "espressionWithAggregateFunction:overField:"
- "firstMatchInString:options:range:"
- "initWithPattern:options:error:"
- "max:"
- "mostRecentChannelFlags"
- "neighborChannelsAsArray:"
- "performPruneTestEntity:since:withError:"
- "updateHomeNetworksForDeploymentIssuesWithError:"
- "updateNetworksForCoverageIssues:withError:"
- "updateUniqueMO:withConstraints:fromStats:withTotal:timespan:prevPercentile:"

```
