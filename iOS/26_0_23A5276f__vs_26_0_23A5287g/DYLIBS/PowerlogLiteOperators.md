## PowerlogLiteOperators

> `/System/Library/PrivateFrameworks/PowerlogLiteOperators.framework/PowerlogLiteOperators`

```diff

-2964.0.40.502.1
-  __TEXT.__text: 0x50d58c
-  __TEXT.__auth_stubs: 0x2d90
-  __TEXT.__objc_methlist: 0x301c4
-  __TEXT.__const: 0x1e98
+2964.0.64.0.0
+  __TEXT.__text: 0x50e6ac
+  __TEXT.__auth_stubs: 0x2db0
+  __TEXT.__objc_methlist: 0x3024c
+  __TEXT.__const: 0x1ea8
   __TEXT.__swift5_typeref: 0x4fa
   __TEXT.__constg_swiftt: 0x364
   __TEXT.__swift5_reflstr: 0x2be
   __TEXT.__swift5_fieldmd: 0x51c
-  __TEXT.__cstring: 0x83c5e
+  __TEXT.__cstring: 0x83d79
   __TEXT.__swift5_proto: 0x108
   __TEXT.__swift5_types: 0x34
-  __TEXT.__oslogstring: 0x11bc7
-  __TEXT.__swift5_capture: 0x4e4
+  __TEXT.__oslogstring: 0x11cdd
+  __TEXT.__swift5_capture: 0x4f4
   __TEXT.__swift5_builtin: 0x14
   __TEXT.__swift5_mpenum: 0x8
   __TEXT.__swift5_protos: 0x8
   __TEXT.__swift_as_entry: 0x50
   __TEXT.__swift_as_ret: 0x58
-  __TEXT.__gcc_except_tab: 0x2d08
+  __TEXT.__gcc_except_tab: 0x2d34
   __TEXT.__ustring: 0x22
-  __TEXT.__unwind_info: 0x80d0
+  __TEXT.__unwind_info: 0x81b0
   __TEXT.__eh_frame: 0x10f0
   __TEXT.__objc_classname: 0x2845
-  __TEXT.__objc_methname: 0x66be1
-  __TEXT.__objc_methtype: 0x8304
-  __TEXT.__objc_stubs: 0x355e0
-  __DATA_CONST.__got: 0x1b00
-  __DATA_CONST.__const: 0xa620
+  __TEXT.__objc_methname: 0x66f36
+  __TEXT.__objc_methtype: 0x830a
+  __TEXT.__objc_stubs: 0x35720
+  __DATA_CONST.__got: 0x1b10
+  __DATA_CONST.__const: 0xa648
   __DATA_CONST.__objc_classlist: 0xa68
   __DATA_CONST.__objc_nlclslist: 0x260
   __DATA_CONST.__objc_catlist: 0x8
   __DATA_CONST.__objc_protolist: 0x88
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x14ec0
+  __DATA_CONST.__objc_selrefs: 0x14f30
   __DATA_CONST.__objc_protorefs: 0x8
   __DATA_CONST.__objc_superrefs: 0xb58
-  __DATA_CONST.__objc_arraydata: 0x15f38
-  __AUTH_CONST.__auth_got: 0x16e0
-  __AUTH_CONST.__const: 0x2470
-  __AUTH_CONST.__cfstring: 0x74bc0
-  __AUTH_CONST.__objc_const: 0x3a7d0
-  __AUTH_CONST.__objc_intobj: 0x74d0
+  __DATA_CONST.__objc_arraydata: 0x15f88
+  __AUTH_CONST.__auth_got: 0x16f0
+  __AUTH_CONST.__const: 0x24b8
+  __AUTH_CONST.__cfstring: 0x74dc0
+  __AUTH_CONST.__objc_const: 0x3a890
+  __AUTH_CONST.__objc_intobj: 0x7500
   __AUTH_CONST.__objc_arrayobj: 0x2cd0
-  __AUTH_CONST.__objc_dictobj: 0x4e98
-  __AUTH_CONST.__objc_doubleobj: 0x1420
+  __AUTH_CONST.__objc_dictobj: 0x4f10
+  __AUTH_CONST.__objc_doubleobj: 0x1440
   __AUTH.__objc_data: 0x2cf8
   __AUTH.__data: 0x760
   __DATA.__objc_ivar: 0x1f18
   __DATA.__data: 0xf08
   __DATA.__bss: 0x1ff8
   __DATA.__common: 0x228
-  __DATA_DIRTY.__objc_ivar: 0x170c
+  __DATA_DIRTY.__objc_ivar: 0x171c
   __DATA_DIRTY.__objc_data: 0x3c98
   __DATA_DIRTY.__data: 0x2a0
-  __DATA_DIRTY.__bss: 0x56b0
+  __DATA_DIRTY.__bss: 0x56a8
   __DATA_DIRTY.__common: 0x90
   - /System/Library/Frameworks/Accounts.framework/Accounts
   - /System/Library/Frameworks/CloudKit.framework/CloudKit

   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  UUID: 5D352F26-6E12-331A-A5AC-4C7CB07B375F
-  Functions: 20353
-  Symbols:   54958
-  CStrings:  52702
+  UUID: 5997D9D3-D85C-3385-9AB8-F78947C6AC0E
+  Functions: 20368
+  Symbols:   55001
+  CStrings:  52766
 
Symbols:
+ -[PLBatteryAgent batteryAppDetailVisitNotification]
+ -[PLBatteryAgent batteryDetailVisitNotification]
+ -[PLBatteryAgent batteryUIInsightsListener]
+ -[PLBatteryAgent batteryUIVisitsListener]
+ -[PLBatteryAgent logEventPointBatteryUIAppDetailVisit]
+ -[PLBatteryAgent logEventPointBatteryUIDetailVisit]
+ -[PLBatteryAgent logEventPointBatteryUIInsightsAndSuggestionsWithPayload:]
+ -[PLBatteryAgent logEventPointBatteryUIVisitWithPayload:]
+ -[PLBatteryAgent setBatteryAppDetailVisitNotification:]
+ -[PLBatteryAgent setBatteryDetailVisitNotification:]
+ -[PLBatteryAgent setBatteryUIInsightsListener:]
+ -[PLBatteryAgent setBatteryUIVisitsListener:]
+ -[PLEnergyIssuesService handlePE:withImpact:withTimestamp:]
+ -[PLEnergyIssuesService insertSystemTime:fromPLEntry:]
+ -[PLXPCService handlePeerListenerEvent:withMessage:withClientID:withProcessName:withKey:withPayload:withPeer:]
+ -[PLXPCService handlePeerResponderEvent:withMessage:withClientID:withProcessName:withKey:withPayload:withPeer:]
+ -[PLXPCService handlePeerShouldLogEvent:withMessage:withClientID:withProcessName:withKey:withPeer:]
+ -[PLXPCService localeResponder]
+ -[PLXPCService setLocaleResponder:]
+ GCC_except_table197
+ GCC_except_table260
+ GCC_except_table274
+ GCC_except_table275
+ GCC_except_table323
+ GCC_except_table327
+ GCC_except_table432
+ _NSLocaleIdentifier
+ _OBJC_CLASS_$_PLXPCRelay
+ _PLLogRelay
+ ___110-[PLXPCService handlePeerListenerEvent:withMessage:withClientID:withProcessName:withKey:withPayload:withPeer:]_block_invoke
+ ___110-[PLXPCService handlePeerListenerEvent:withMessage:withClientID:withProcessName:withKey:withPayload:withPeer:]_block_invoke.880
+ ___111-[PLXPCService handlePeerResponderEvent:withMessage:withClientID:withProcessName:withKey:withPayload:withPeer:]_block_invoke
+ ___111-[PLXPCService handlePeerResponderEvent:withMessage:withClientID:withProcessName:withKey:withPayload:withPeer:]_block_invoke.811
+ ___111-[PLXPCService handlePeerResponderEvent:withMessage:withClientID:withProcessName:withKey:withPayload:withPeer:]_block_invoke.823
+ ___111-[PLXPCService handlePeerResponderEvent:withMessage:withClientID:withProcessName:withKey:withPayload:withPeer:]_block_invoke.827
+ ___111-[PLXPCService handlePeerResponderEvent:withMessage:withClientID:withProcessName:withKey:withPayload:withPeer:]_block_invoke.849
+ ___111-[PLXPCService handlePeerResponderEvent:withMessage:withClientID:withProcessName:withKey:withPayload:withPeer:]_block_invoke.856
+ ___111-[PLXPCService handlePeerResponderEvent:withMessage:withClientID:withProcessName:withKey:withPayload:withPeer:]_block_invoke.863
+ ___111-[PLXPCService handlePeerResponderEvent:withMessage:withClientID:withProcessName:withKey:withPayload:withPeer:]_block_invoke.870
+ ___111-[PLXPCService handlePeerResponderEvent:withMessage:withClientID:withProcessName:withKey:withPayload:withPeer:]_block_invoke.874
+ ___111-[PLXPCService handlePeerResponderEvent:withMessage:withClientID:withProcessName:withKey:withPayload:withPeer:]_block_invoke_2
+ ___111-[PLXPCService handlePeerResponderEvent:withMessage:withClientID:withProcessName:withKey:withPayload:withPeer:]_block_invoke_2.864
+ ___20-[PLXPCService init]_block_invoke.612
+ ___22-[PLBatteryAgent init]_block_invoke.3262
+ ___22-[PLBatteryAgent init]_block_invoke.3274
+ ___22-[PLBatteryAgent init]_block_invoke.3276
+ ___22-[PLBatteryAgent init]_block_invoke.3303
+ ___22-[PLBatteryAgent init]_block_invoke.3311
+ ___22-[PLBatteryAgent init]_block_invoke.3317
+ ___22-[PLBatteryAgent init]_block_invoke.3321
+ ___22-[PLBatteryAgent init]_block_invoke_2.3343
+ ___24-[PLBatteryAgent xFlags]_block_invoke.5073
+ ___24-[PLBatteryAgent xFlags]_block_invoke.5082
+ ___24-[PLBatteryAgent xFlags]_block_invoke.5097
+ ___24-[PLBatteryAgent xFlags]_block_invoke.5103
+ ___24-[PLBatteryAgent xFlags]_block_invoke.5109
+ ___24-[PLBatteryAgent xFlags]_block_invoke.5118
+ ___24-[PLBatteryAgent xFlags]_block_invoke.5124
+ ___24-[PLBatteryAgent xFlags]_block_invoke.5130
+ ___28-[PLBackupRestoreAgent init]_block_invoke.41
+ ___32-[PLBatteryAgent aggdTimerFired]_block_invoke.4751
+ ___32-[PLBatteryAgent getIOPSDevices]_block_invoke.3442
+ ___32-[PLBatteryAgent getIOPSDevices]_block_invoke.3448
+ ___33-[PLBatteryAgent cancelEALogging]_block_invoke.3433
+ ___33-[PLBatteryAgent setupCSMLogging]_block_invoke.5143
+ ___36-[PLXPCService handlePeer:forEvent:]_block_invoke.706
+ ___36-[PLXPCService handlePeer:forEvent:]_block_invoke.712
+ ___36-[PLXPCService handlePeer:forEvent:]_block_invoke.718
+ ___36-[PLXPCService handlePeer:forEvent:]_block_invoke.724
+ ___36-[PLXPCService handlePeer:forEvent:]_block_invoke.733
+ ___36-[PLXPCService handlePeer:forEvent:]_block_invoke.743
+ ___36-[PLXPCService handlePeer:forEvent:]_block_invoke.747
+ ___38-[PLBatteryAgent handleBDCAMALogging:]_block_invoke.3810
+ ___39-[PLXPCService logMessage:withPayload:]_block_invoke.672
+ ___41-[PLBatteryAgent logEventBackwardHeatMap]_block_invoke.4151
+ ___41-[PLBatteryAgent logEventBackwardHeatMap]_block_invoke.4158
+ ___41-[PLBatteryAgent logEventBackwardHeatMap]_block_invoke_2.4154
+ ___41-[PLBatteryAgent logEventBackwardHeatMap]_block_invoke_2.4161
+ ___42-[PLBatteryAgent initOperatorDependancies]_block_invoke.3520
+ ___42-[PLBatteryAgent initOperatorDependancies]_block_invoke.3526
+ ___42-[PLBatteryAgent initOperatorDependancies]_block_invoke.3542
+ ___42-[PLBatteryAgent initOperatorDependancies]_block_invoke.3575
+ ___42-[PLBatteryAgent initOperatorDependancies]_block_invoke.3635
+ ___42-[PLBatteryAgent initOperatorDependancies]_block_invoke.3663
+ ___42-[PLBatteryAgent initOperatorDependancies]_block_invoke.3667
+ ___42-[PLBatteryAgent initOperatorDependancies]_block_invoke.3675
+ ___42-[PLBatteryAgent initOperatorDependancies]_block_invoke.3682
+ ___42-[PLBatteryAgent initOperatorDependancies]_block_invoke.3691
+ ___42-[PLBatteryAgent initOperatorDependancies]_block_invoke.3697
+ ___42-[PLBatteryAgent initOperatorDependancies]_block_invoke.3704
+ ___42-[PLBatteryAgent initOperatorDependancies]_block_invoke.3711
+ ___42-[PLBatteryAgent initOperatorDependancies]_block_invoke.3725
+ ___42-[PLBatteryAgent initOperatorDependancies]_block_invoke.3730
+ ___42-[PLBatteryAgent initOperatorDependancies]_block_invoke.3737
+ ___42-[PLBatteryAgent initOperatorDependancies]_block_invoke.3761
+ ___42-[PLBatteryAgent initOperatorDependancies]_block_invoke_2.3527
+ ___42-[PLBatteryAgent initOperatorDependancies]_block_invoke_2.3572
+ ___42-[PLBatteryAgent initOperatorDependancies]_block_invoke_2.3587
+ ___42-[PLBatteryAgent initOperatorDependancies]_block_invoke_2.3659
+ ___42-[PLBatteryAgent initOperatorDependancies]_block_invoke_2.3676
+ ___42-[PLBatteryAgent initOperatorDependancies]_block_invoke_2.3686
+ ___42-[PLBatteryAgent initOperatorDependancies]_block_invoke_2.3705
+ ___42-[PLBatteryAgent initOperatorDependancies]_block_invoke_2.3712
+ ___42-[PLBatteryAgent initOperatorDependancies]_block_invoke_2.3769
+ ___42-[PLBatteryAgent initOperatorDependancies]_block_invoke_3.3777
+ ___42-[PLBatteryAgent initOperatorDependancies]_block_invoke_4.3785
+ ___42-[PLBatteryAgent initOperatorDependancies]_block_invoke_5.3789
+ ___42-[PLBatteryAgent initOperatorDependancies]_block_invoke_6.3793
+ ___42-[PLBatteryAgent initOperatorDependancies]_block_invoke_7.3797
+ ___42-[PLBatteryAgent initOperatorDependancies]_block_invoke_8
+ ___42-[PLBatteryAgent initOperatorDependancies]_block_invoke_9
+ ___42-[PLBatteryAgent initSmartChargingLogging]_block_invoke.5294
+ ___42-[PLBatteryAgent initSmartChargingLogging]_block_invoke.5302
+ ___42-[PLBatteryAgent initSmartChargingLogging]_block_invoke_2.5296
+ ___42-[PLBatteryAgent logEventIntervalGasGauge]_block_invoke.4016
+ ___42-[PLXPCService resetPermissionsForClients]_block_invoke.687
+ ___42-[PLXPCService resetPermissionsForClients]_block_invoke.697
+ ___43-[PLIOReportAgent initOperatorDependancies]_block_invoke.8741
+ ___43-[PLIOReportAgent initOperatorDependancies]_block_invoke.8743
+ ___43-[PLIOReportAgent initOperatorDependancies]_block_invoke.8748
+ ___43-[PLIOReportAgent initOperatorDependancies]_block_invoke.8749
+ ___43-[PLIOReportAgent initOperatorDependancies]_block_invoke.8750
+ ___43-[PLIOReportAgent initOperatorDependancies]_block_invoke.8751
+ ___43-[PLIOReportAgent initOperatorDependancies]_block_invoke_2.8744
+ ___43-[PLIOReportAgent initOperatorDependancies]_block_invoke_2.8752
+ ___43-[PLIOReportAgent initOperatorDependancies]_block_invoke_3.8756
+ ___43-[PLIOReportAgent logEventBackwardMTRAging]_block_invoke.9648
+ ___43-[PLIOReportAgent logEventBackwardMTRAging]_block_invoke.9654
+ ___43-[PLIOReportAgent logEventBackwardMTRAging]_block_invoke.9661
+ ___44-[PLXPCService respondToEvent:withResponse:]_block_invoke.651
+ ___44-[PLXPCService respondToEvent:withResponse:]_block_invoke.657
+ ___45-[PLBatteryAgent logCPMSSnapshotWithTrigger:]_block_invoke.5330
+ ___45-[PLBatteryAgent logCPMSSnapshotWithTrigger:]_block_invoke.5331
+ ___45-[PLBatteryAgent logCPMSSnapshotWithTrigger:]_block_invoke.5332
+ ___45-[PLBatteryAgent logCPMSSnapshotWithTrigger:]_block_invoke.5333
+ ___45-[PLBatteryAgent logCPMSSnapshotWithTrigger:]_block_invoke.5334
+ ___45-[PLBatteryAgent logCPMSSnapshotWithTrigger:]_block_invoke.5335
+ ___45-[PLBatteryAgent logCPMSSnapshotWithTrigger:]_block_invoke.5336
+ ___45-[PLBatteryAgent logCPMSSnapshotWithTrigger:]_block_invoke.5377
+ ___46-[PLApplicationAgent initOperatorDependancies]_block_invoke.417
+ ___46-[PLApplicationAgent initOperatorDependancies]_block_invoke.446
+ ___46-[PLApplicationAgent initOperatorDependancies]_block_invoke.452
+ ___46-[PLApplicationAgent initOperatorDependancies]_block_invoke.457
+ ___46-[PLApplicationAgent initOperatorDependancies]_block_invoke.464
+ ___46-[PLApplicationAgent initOperatorDependancies]_block_invoke.474
+ ___46-[PLApplicationAgent initOperatorDependancies]_block_invoke.481
+ ___46-[PLApplicationAgent initOperatorDependancies]_block_invoke.488
+ ___46-[PLApplicationAgent initOperatorDependancies]_block_invoke.493
+ ___46-[PLApplicationAgent initOperatorDependancies]_block_invoke.498
+ ___46-[PLApplicationAgent initOperatorDependancies]_block_invoke.506
+ ___46-[PLApplicationAgent initOperatorDependancies]_block_invoke.514
+ ___46-[PLApplicationAgent initOperatorDependancies]_block_invoke.519
+ ___46-[PLApplicationAgent initOperatorDependancies]_block_invoke.524
+ ___46-[PLApplicationAgent initOperatorDependancies]_block_invoke.539
+ ___46-[PLApplicationAgent initOperatorDependancies]_block_invoke.547
+ ___46-[PLApplicationAgent initOperatorDependancies]_block_invoke_2.420
+ ___46-[PLApplicationAgent initOperatorDependancies]_block_invoke_2.526
+ ___50-[PLBatteryAgent initializeChargingStateIntervals]_block_invoke.5319
+ ___50-[PLBatteryAgent initializeChargingStateIntervals]_block_invoke.5320
+ ___50-[PLBatteryAgent initializeChargingStateIntervals]_block_invoke.5324
+ ___54-[PLXPCService handleSingleMessage:fromPeer:forEvent:]_block_invoke.760
+ ___54-[PLXPCService handleSingleMessage:fromPeer:forEvent:]_block_invoke.763
+ ___54-[PLXPCService handleSingleMessage:fromPeer:forEvent:]_block_invoke.769
+ ___54-[PLXPCService handleSingleMessage:fromPeer:forEvent:]_block_invoke.775
+ ___54-[PLXPCService handleSingleMessage:fromPeer:forEvent:]_block_invoke.781
+ ___54-[PLXPCService handleSingleMessage:fromPeer:forEvent:]_block_invoke.787
+ ___55-[PLBatteryAgent logEventNoneBatteryConfigWithRawData:]_block_invoke.5007
+ ___55-[PLBatteryAgent logEventNoneBatteryConfigWithRawData:]_block_invoke.5011
+ ___55-[PLBatteryAgent logEventNoneBatteryConfigWithRawData:]_block_invoke.5016
+ ___55-[PLBatteryAgent logEventNoneBatteryConfigWithRawData:]_block_invoke.5020
+ ___55-[PLBatteryAgent logEventNoneBatteryConfigWithRawData:]_block_invoke_2.5012
+ ___55-[PLBatteryAgent logEventNoneBatteryConfigWithRawData:]_block_invoke_2.5017
+ ___56-[PLApplicationAgent createWidgetStatsAccountingEvents:]_block_invoke.577
+ ___59-[PLBatteryAgent setupEALoggingTriggeredByConnectionEvent:]_block_invoke.3413
+ ___59-[PLEnergyIssuesService handlePE:withImpact:withTimestamp:]_block_invoke
+ ___61-[PLBatteryBreakdownService mapDeletedAppsWithEnergyEntries:]_block_invoke.1810
+ ___63-[PLBatteryBreakdownService mapPluginsToAppsWithEnergyEntries:]_block_invoke.1819
+ ___64-[PLBatteryBreakdownService combineDuplicatesWithEnergyEntries:]_block_invoke.1883
+ ___64-[PLBatteryBreakdownService combineDuplicatesWithEnergyEntries:]_block_invoke.1887
+ ___65-[PLBatteryAgent logEventBackwardHeatMapCallback:andHeatMapType:]_block_invoke.4414
+ ___67-[PLBatteryBreakdownService filterWithEnergyEntries:withQueryType:]_block_invoke.1904
+ ___68-[PLBatteryBreakdownService determineDisplayNamesWithEnergyEntries:]_block_invoke.1898
+ ___69-[PLBatteryBreakdownService reaccountBackupRestoreWithEnergyEntries:]_block_invoke.1872
+ ___69-[PLIOReportAgent logEventBackwardIOReportWithDelta:forChannelGroup:]_block_invoke.9612
+ ___70-[PLIOReportAgent channelDictionaryWithChannelSet:withMinProcessTime:]_block_invoke.8346
+ ___70-[PLIOReportAgent channelDictionaryWithChannelSet:withMinProcessTime:]_block_invoke.8352
+ ___73-[PLBatteryBreakdownService populateRootNodeEnergyKeysWithEnergyEntries:]_block_invoke.1603
+ ___74-[PLBatteryBreakdownService filterEnergyEntriesBasedOnTime:withQueryType:]_block_invoke.1736
+ ___74-[PLBatteryBreakdownService filterEnergyEntriesBasedOnTime:withQueryType:]_block_invoke.1748
+ ___74-[PLBatteryBreakdownService filterEnergyEntriesBasedOnTime:withQueryType:]_block_invoke.1756
+ ___75-[PLBatteryAgent showOrHideTLCNotification:meetsTLCNotificationConditions:]_block_invoke.3385
+ ___75-[PLBatteryBreakdownService addNotificationValues:withRange:withQueryType:]_block_invoke.1726
+ ___77-[PLBatteryBreakdownService applyStaticNameTransformationsWithEnergyEntries:]_block_invoke.1777
+ ___77-[PLBatteryBreakdownService applyStaticNameTransformationsWithEnergyEntries:]_block_invoke.1791
+ ___81-[PLApplicationAgent logInstalledAppWithRecord:withBundleID:shouldMaskTimestamp:]_block_invoke.617
+ ___81-[PLBatteryBreakdownService qualifiersWithEnergyEntry:bucketSize:andTotalEnergy:]_block_invoke.1939
+ ___81-[PLBatteryBreakdownService qualifiersWithEnergyEntry:bucketSize:andTotalEnergy:]_block_invoke.1956
+ ___81-[PLBatteryBreakdownService qualifiersWithEnergyEntry:bucketSize:andTotalEnergy:]_block_invoke.1964
+ ___81-[PLBatteryBreakdownService qualifiersWithEnergyEntry:bucketSize:andTotalEnergy:]_block_invoke.1972
+ ___81-[PLBatteryBreakdownService qualifiersWithEnergyEntry:bucketSize:andTotalEnergy:]_block_invoke.2014
+ ___81-[PLBatteryBreakdownService qualifiersWithEnergyEntry:bucketSize:andTotalEnergy:]_block_invoke.2024
+ ___88-[PLBatteryBreakdownService energyEntriesWithRange:withEntryTimeInterval:withQueryType:]_block_invoke.1528
+ ___99-[PLXPCService handlePeerShouldLogEvent:withMessage:withClientID:withProcessName:withKey:withPeer:]_block_invoke
+ ___99-[PLXPCService handlePeerShouldLogEvent:withMessage:withClientID:withProcessName:withKey:withPeer:]_block_invoke.802
+ ___block_descriptor_48_e8_32s40s_e47_v32?0"NSError"8"NSString"16"NSDictionary"24ls32l8s40l8
+ ___block_literal_global.176
+ ___block_literal_global.2094
+ ___block_literal_global.3249
+ ___block_literal_global.3359
+ ___block_literal_global.3372
+ ___block_literal_global.3387
+ ___block_literal_global.3488
+ ___block_literal_global.3545
+ ___block_literal_global.3589
+ ___block_literal_global.3598
+ ___block_literal_global.3607
+ ___block_literal_global.3619
+ ___block_literal_global.3732
+ ___block_literal_global.3803
+ ___block_literal_global.3809
+ ___block_literal_global.3819
+ ___block_literal_global.429
+ ___block_literal_global.4463
+ ___block_literal_global.4707
+ ___block_literal_global.4719
+ ___block_literal_global.4769
+ ___block_literal_global.492
+ ___block_literal_global.5268
+ ___block_literal_global.5329
+ ___block_literal_global.5860
+ ___block_literal_global.7270
+ ___block_literal_global.7281
+ ___block_literal_global.8327
+ ___block_literal_global.8692
+ ___block_literal_global.8747
+ ___block_literal_global.8842
+ ___block_literal_global.8857
+ ___block_literal_global.9133
+ ___block_literal_global.9744
+ ___block_literal_global.9772
+ _objc_msgSend$handlePE:withImpact:withTimestamp:
+ _objc_msgSend$handlePeerListenerEvent:withMessage:withClientID:withProcessName:withKey:withPayload:withPeer:
+ _objc_msgSend$handlePeerResponderEvent:withMessage:withClientID:withProcessName:withKey:withPayload:withPeer:
+ _objc_msgSend$handlePeerShouldLogEvent:withMessage:withClientID:withProcessName:withKey:withPeer:
+ _objc_msgSend$insertSystemTime:fromPLEntry:
+ _objc_msgSend$isBasebandMavToAllowSysdiagnoseTrigger
+ _objc_msgSend$isPowerexceptionsd
+ _objc_msgSend$logEventPointBatteryUIAppDetailVisit
+ _objc_msgSend$logEventPointBatteryUIDetailVisit
+ _objc_msgSend$logEventPointBatteryUIInsightsAndSuggestionsWithPayload:
+ _objc_msgSend$logEventPointBatteryUIVisitWithPayload:
+ _objc_msgSend$relayActive
+ _objc_msgSend$setBatteryAppDetailVisitNotification:
+ _objc_msgSend$setBatteryDetailVisitNotification:
+ _objc_msgSend$setBatteryUIInsightsListener:
+ _objc_msgSend$setBatteryUIVisitsListener:
- -[PLBatteryAgent batteryUIVisitNotification]
- -[PLBatteryAgent logEventPointBatteryUIVisit]
- -[PLBatteryAgent setBatteryUIVisitNotification:]
- -[PLBatteryBreakdownService shouldShowOngoingRestoreInsight]
- -[PLEnergyIssuesService handlePE:withImpact:]
- -[PLXPCService handlePeerListenerEvent:withMessage:withClientID:withProcessName:withKey:withPayload:]
- -[PLXPCService handlePeerResponderEvent:withMessage:withClientID:withProcessName:withKey:withPayload:]
- -[PLXPCService handlePeerShouldLogEvent:withMessage:withClientID:withProcessName:withKey:]
- GCC_except_table191
- GCC_except_table254
- GCC_except_table256
- GCC_except_table261
- GCC_except_table269
- GCC_except_table29
- GCC_except_table315
- GCC_except_table317
- GCC_except_table426
- GCC_except_table66
- ___101-[PLXPCService handlePeerListenerEvent:withMessage:withClientID:withProcessName:withKey:withPayload:]_block_invoke
- ___101-[PLXPCService handlePeerListenerEvent:withMessage:withClientID:withProcessName:withKey:withPayload:]_block_invoke.862
- ___102-[PLXPCService handlePeerResponderEvent:withMessage:withClientID:withProcessName:withKey:withPayload:]_block_invoke
- ___102-[PLXPCService handlePeerResponderEvent:withMessage:withClientID:withProcessName:withKey:withPayload:]_block_invoke.793
- ___102-[PLXPCService handlePeerResponderEvent:withMessage:withClientID:withProcessName:withKey:withPayload:]_block_invoke.805
- ___102-[PLXPCService handlePeerResponderEvent:withMessage:withClientID:withProcessName:withKey:withPayload:]_block_invoke.809
- ___102-[PLXPCService handlePeerResponderEvent:withMessage:withClientID:withProcessName:withKey:withPayload:]_block_invoke.831
- ___102-[PLXPCService handlePeerResponderEvent:withMessage:withClientID:withProcessName:withKey:withPayload:]_block_invoke.838
- ___102-[PLXPCService handlePeerResponderEvent:withMessage:withClientID:withProcessName:withKey:withPayload:]_block_invoke.845
- ___102-[PLXPCService handlePeerResponderEvent:withMessage:withClientID:withProcessName:withKey:withPayload:]_block_invoke.852
- ___102-[PLXPCService handlePeerResponderEvent:withMessage:withClientID:withProcessName:withKey:withPayload:]_block_invoke.856
- ___102-[PLXPCService handlePeerResponderEvent:withMessage:withClientID:withProcessName:withKey:withPayload:]_block_invoke_2
- ___102-[PLXPCService handlePeerResponderEvent:withMessage:withClientID:withProcessName:withKey:withPayload:]_block_invoke_2.846
- ___22-[PLBatteryAgent init]_block_invoke.3251
- ___22-[PLBatteryAgent init]_block_invoke.3263
- ___22-[PLBatteryAgent init]_block_invoke.3265
- ___22-[PLBatteryAgent init]_block_invoke.3289
- ___22-[PLBatteryAgent init]_block_invoke.3292
- ___22-[PLBatteryAgent init]_block_invoke.3306
- ___22-[PLBatteryAgent init]_block_invoke.3310
- ___22-[PLBatteryAgent init]_block_invoke_2.3332
- ___24-[PLBatteryAgent xFlags]_block_invoke.5025
- ___24-[PLBatteryAgent xFlags]_block_invoke.5034
- ___24-[PLBatteryAgent xFlags]_block_invoke.5043
- ___24-[PLBatteryAgent xFlags]_block_invoke.5052
- ___24-[PLBatteryAgent xFlags]_block_invoke.5058
- ___24-[PLBatteryAgent xFlags]_block_invoke.5070
- ___24-[PLBatteryAgent xFlags]_block_invoke.5079
- ___24-[PLBatteryAgent xFlags]_block_invoke.5085
- ___28-[PLBackupRestoreAgent init]_block_invoke.43
- ___32-[PLBatteryAgent aggdTimerFired]_block_invoke.4712
- ___32-[PLBatteryAgent getIOPSDevices]_block_invoke.3431
- ___32-[PLBatteryAgent getIOPSDevices]_block_invoke.3437
- ___33-[PLBatteryAgent cancelEALogging]_block_invoke.3422
- ___33-[PLBatteryAgent setupCSMLogging]_block_invoke.5104
- ___36-[PLXPCService handlePeer:forEvent:]_block_invoke.689
- ___36-[PLXPCService handlePeer:forEvent:]_block_invoke.695
- ___36-[PLXPCService handlePeer:forEvent:]_block_invoke.701
- ___36-[PLXPCService handlePeer:forEvent:]_block_invoke.707
- ___36-[PLXPCService handlePeer:forEvent:]_block_invoke.716
- ___36-[PLXPCService handlePeer:forEvent:]_block_invoke.726
- ___36-[PLXPCService handlePeer:forEvent:]_block_invoke.730
- ___38-[PLBatteryAgent handleBDCAMALogging:]_block_invoke.3781
- ___39-[PLXPCService logMessage:withPayload:]_block_invoke.655
- ___41-[PLBatteryAgent logEventBackwardHeatMap]_block_invoke.4112
- ___41-[PLBatteryAgent logEventBackwardHeatMap]_block_invoke.4119
- ___41-[PLBatteryAgent logEventBackwardHeatMap]_block_invoke_2.4115
- ___41-[PLBatteryAgent logEventBackwardHeatMap]_block_invoke_2.4122
- ___42-[PLBatteryAgent initOperatorDependancies]_block_invoke.3509
- ___42-[PLBatteryAgent initOperatorDependancies]_block_invoke.3515
- ___42-[PLBatteryAgent initOperatorDependancies]_block_invoke.3531
- ___42-[PLBatteryAgent initOperatorDependancies]_block_invoke.3564
- ___42-[PLBatteryAgent initOperatorDependancies]_block_invoke.3624
- ___42-[PLBatteryAgent initOperatorDependancies]_block_invoke.3641
- ___42-[PLBatteryAgent initOperatorDependancies]_block_invoke.3656
- ___42-[PLBatteryAgent initOperatorDependancies]_block_invoke.3664
- ___42-[PLBatteryAgent initOperatorDependancies]_block_invoke.3671
- ___42-[PLBatteryAgent initOperatorDependancies]_block_invoke.3680
- ___42-[PLBatteryAgent initOperatorDependancies]_block_invoke.3686
- ___42-[PLBatteryAgent initOperatorDependancies]_block_invoke.3693
- ___42-[PLBatteryAgent initOperatorDependancies]_block_invoke.3700
- ___42-[PLBatteryAgent initOperatorDependancies]_block_invoke.3714
- ___42-[PLBatteryAgent initOperatorDependancies]_block_invoke.3719
- ___42-[PLBatteryAgent initOperatorDependancies]_block_invoke.3726
- ___42-[PLBatteryAgent initOperatorDependancies]_block_invoke.3750
- ___42-[PLBatteryAgent initOperatorDependancies]_block_invoke_2.3516
- ___42-[PLBatteryAgent initOperatorDependancies]_block_invoke_2.3561
- ___42-[PLBatteryAgent initOperatorDependancies]_block_invoke_2.3576
- ___42-[PLBatteryAgent initOperatorDependancies]_block_invoke_2.3648
- ___42-[PLBatteryAgent initOperatorDependancies]_block_invoke_2.3665
- ___42-[PLBatteryAgent initOperatorDependancies]_block_invoke_2.3675
- ___42-[PLBatteryAgent initOperatorDependancies]_block_invoke_2.3683
- ___42-[PLBatteryAgent initOperatorDependancies]_block_invoke_2.3701
- ___42-[PLBatteryAgent initOperatorDependancies]_block_invoke_2.3758
- ___42-[PLBatteryAgent initOperatorDependancies]_block_invoke_3.3762
- ___42-[PLBatteryAgent initOperatorDependancies]_block_invoke_4.3766
- ___42-[PLBatteryAgent initOperatorDependancies]_block_invoke_5.3770
- ___42-[PLBatteryAgent initOperatorDependancies]_block_invoke_6.3772
- ___42-[PLBatteryAgent initSmartChargingLogging]_block_invoke.5255
- ___42-[PLBatteryAgent initSmartChargingLogging]_block_invoke.5263
- ___42-[PLBatteryAgent initSmartChargingLogging]_block_invoke_2.5257
- ___42-[PLBatteryAgent logEventIntervalGasGauge]_block_invoke.3977
- ___42-[PLXPCService resetPermissionsForClients]_block_invoke.670
- ___42-[PLXPCService resetPermissionsForClients]_block_invoke.680
- ___43-[PLIOReportAgent initOperatorDependancies]_block_invoke.8715
- ___43-[PLIOReportAgent initOperatorDependancies]_block_invoke.8724
- ___43-[PLIOReportAgent initOperatorDependancies]_block_invoke.8726
- ___43-[PLIOReportAgent initOperatorDependancies]_block_invoke.8731
- ___43-[PLIOReportAgent initOperatorDependancies]_block_invoke.8733
- ___43-[PLIOReportAgent initOperatorDependancies]_block_invoke.8734
- ___43-[PLIOReportAgent initOperatorDependancies]_block_invoke_2.8727
- ___43-[PLIOReportAgent initOperatorDependancies]_block_invoke_2.8735
- ___43-[PLIOReportAgent initOperatorDependancies]_block_invoke_3.8739
- ___43-[PLIOReportAgent logEventBackwardMTRAging]_block_invoke.9631
- ___43-[PLIOReportAgent logEventBackwardMTRAging]_block_invoke.9637
- ___43-[PLIOReportAgent logEventBackwardMTRAging]_block_invoke.9644
- ___44-[PLXPCService respondToEvent:withResponse:]_block_invoke.634
- ___44-[PLXPCService respondToEvent:withResponse:]_block_invoke.640
- ___45-[PLBatteryAgent logCPMSSnapshotWithTrigger:]_block_invoke.5291
- ___45-[PLBatteryAgent logCPMSSnapshotWithTrigger:]_block_invoke.5292
- ___45-[PLBatteryAgent logCPMSSnapshotWithTrigger:]_block_invoke.5293
- ___45-[PLBatteryAgent logCPMSSnapshotWithTrigger:]_block_invoke.5294
- ___45-[PLBatteryAgent logCPMSSnapshotWithTrigger:]_block_invoke.5295
- ___45-[PLBatteryAgent logCPMSSnapshotWithTrigger:]_block_invoke.5296
- ___45-[PLBatteryAgent logCPMSSnapshotWithTrigger:]_block_invoke.5297
- ___45-[PLBatteryAgent logCPMSSnapshotWithTrigger:]_block_invoke.5338
- ___45-[PLEnergyIssuesService handlePE:withImpact:]_block_invoke
- ___46-[PLApplicationAgent initOperatorDependancies]_block_invoke.418
- ___46-[PLApplicationAgent initOperatorDependancies]_block_invoke.447
- ___46-[PLApplicationAgent initOperatorDependancies]_block_invoke.453
- ___46-[PLApplicationAgent initOperatorDependancies]_block_invoke.458
- ___46-[PLApplicationAgent initOperatorDependancies]_block_invoke.465
- ___46-[PLApplicationAgent initOperatorDependancies]_block_invoke.475
- ___46-[PLApplicationAgent initOperatorDependancies]_block_invoke.482
- ___46-[PLApplicationAgent initOperatorDependancies]_block_invoke.489
- ___46-[PLApplicationAgent initOperatorDependancies]_block_invoke.494
- ___46-[PLApplicationAgent initOperatorDependancies]_block_invoke.499
- ___46-[PLApplicationAgent initOperatorDependancies]_block_invoke.507
- ___46-[PLApplicationAgent initOperatorDependancies]_block_invoke.515
- ___46-[PLApplicationAgent initOperatorDependancies]_block_invoke.520
- ___46-[PLApplicationAgent initOperatorDependancies]_block_invoke.526
- ___46-[PLApplicationAgent initOperatorDependancies]_block_invoke.540
- ___46-[PLApplicationAgent initOperatorDependancies]_block_invoke.548
- ___46-[PLApplicationAgent initOperatorDependancies]_block_invoke_2.421
- ___46-[PLApplicationAgent initOperatorDependancies]_block_invoke_2.527
- ___50-[PLBatteryAgent initializeChargingStateIntervals]_block_invoke.5280
- ___50-[PLBatteryAgent initializeChargingStateIntervals]_block_invoke.5281
- ___50-[PLBatteryAgent initializeChargingStateIntervals]_block_invoke.5285
- ___54-[PLXPCService handleSingleMessage:fromPeer:forEvent:]_block_invoke.743
- ___54-[PLXPCService handleSingleMessage:fromPeer:forEvent:]_block_invoke.746
- ___54-[PLXPCService handleSingleMessage:fromPeer:forEvent:]_block_invoke.752
- ___54-[PLXPCService handleSingleMessage:fromPeer:forEvent:]_block_invoke.758
- ___54-[PLXPCService handleSingleMessage:fromPeer:forEvent:]_block_invoke.764
- ___54-[PLXPCService handleSingleMessage:fromPeer:forEvent:]_block_invoke.770
- ___55-[PLBatteryAgent logEventNoneBatteryConfigWithRawData:]_block_invoke.4968
- ___55-[PLBatteryAgent logEventNoneBatteryConfigWithRawData:]_block_invoke.4972
- ___55-[PLBatteryAgent logEventNoneBatteryConfigWithRawData:]_block_invoke.4977
- ___55-[PLBatteryAgent logEventNoneBatteryConfigWithRawData:]_block_invoke.4981
- ___55-[PLBatteryAgent logEventNoneBatteryConfigWithRawData:]_block_invoke_2.4973
- ___55-[PLBatteryAgent logEventNoneBatteryConfigWithRawData:]_block_invoke_2.4978
- ___56-[PLApplicationAgent createWidgetStatsAccountingEvents:]_block_invoke.578
- ___59-[PLBatteryAgent setupEALoggingTriggeredByConnectionEvent:]_block_invoke.3402
- ___60-[PLBatteryBreakdownService shouldShowOngoingRestoreInsight]_block_invoke
- ___61-[PLBatteryBreakdownService mapDeletedAppsWithEnergyEntries:]_block_invoke.1816
- ___63-[PLBatteryBreakdownService mapPluginsToAppsWithEnergyEntries:]_block_invoke.1825
- ___64-[PLBatteryBreakdownService combineDuplicatesWithEnergyEntries:]_block_invoke.1889
- ___64-[PLBatteryBreakdownService combineDuplicatesWithEnergyEntries:]_block_invoke.1893
- ___65-[PLBatteryAgent logEventBackwardHeatMapCallback:andHeatMapType:]_block_invoke.4375
- ___67-[PLBatteryBreakdownService filterWithEnergyEntries:withQueryType:]_block_invoke.1922
- ___68-[PLBatteryBreakdownService determineDisplayNamesWithEnergyEntries:]_block_invoke.1904
- ___69-[PLBatteryBreakdownService reaccountBackupRestoreWithEnergyEntries:]_block_invoke.1878
- ___69-[PLIOReportAgent logEventBackwardIOReportWithDelta:forChannelGroup:]_block_invoke.9595
- ___70-[PLIOReportAgent channelDictionaryWithChannelSet:withMinProcessTime:]_block_invoke.8329
- ___70-[PLIOReportAgent channelDictionaryWithChannelSet:withMinProcessTime:]_block_invoke.8335
- ___73-[PLBatteryBreakdownService populateRootNodeEnergyKeysWithEnergyEntries:]_block_invoke.1615
- ___74-[PLBatteryBreakdownService filterEnergyEntriesBasedOnTime:withQueryType:]_block_invoke.1742
- ___74-[PLBatteryBreakdownService filterEnergyEntriesBasedOnTime:withQueryType:]_block_invoke.1754
- ___74-[PLBatteryBreakdownService filterEnergyEntriesBasedOnTime:withQueryType:]_block_invoke.1768
- ___75-[PLBatteryAgent showOrHideTLCNotification:meetsTLCNotificationConditions:]_block_invoke.3374
- ___75-[PLBatteryBreakdownService addNotificationValues:withRange:withQueryType:]_block_invoke.1732
- ___77-[PLBatteryBreakdownService applyStaticNameTransformationsWithEnergyEntries:]_block_invoke.1789
- ___77-[PLBatteryBreakdownService applyStaticNameTransformationsWithEnergyEntries:]_block_invoke.1797
- ___81-[PLApplicationAgent logInstalledAppWithRecord:withBundleID:shouldMaskTimestamp:]_block_invoke.618
- ___81-[PLBatteryBreakdownService qualifiersWithEnergyEntry:bucketSize:andTotalEnergy:]_block_invoke.1945
- ___81-[PLBatteryBreakdownService qualifiersWithEnergyEntry:bucketSize:andTotalEnergy:]_block_invoke.1962
- ___81-[PLBatteryBreakdownService qualifiersWithEnergyEntry:bucketSize:andTotalEnergy:]_block_invoke.1970
- ___81-[PLBatteryBreakdownService qualifiersWithEnergyEntry:bucketSize:andTotalEnergy:]_block_invoke.1978
- ___81-[PLBatteryBreakdownService qualifiersWithEnergyEntry:bucketSize:andTotalEnergy:]_block_invoke.2020
- ___81-[PLBatteryBreakdownService qualifiersWithEnergyEntry:bucketSize:andTotalEnergy:]_block_invoke.2030
- ___88-[PLBatteryBreakdownService energyEntriesWithRange:withEntryTimeInterval:withQueryType:]_block_invoke.1558
- ___90-[PLXPCService handlePeerShouldLogEvent:withMessage:withClientID:withProcessName:withKey:]_block_invoke
- ___90-[PLXPCService handlePeerShouldLogEvent:withMessage:withClientID:withProcessName:withKey:]_block_invoke.784
- ___block_literal_global.164
- ___block_literal_global.2100
- ___block_literal_global.3238
- ___block_literal_global.3348
- ___block_literal_global.3361
- ___block_literal_global.3376
- ___block_literal_global.3477
- ___block_literal_global.3534
- ___block_literal_global.3578
- ___block_literal_global.3587
- ___block_literal_global.3596
- ___block_literal_global.3608
- ___block_literal_global.3721
- ___block_literal_global.3774
- ___block_literal_global.3780
- ___block_literal_global.3790
- ___block_literal_global.426
- ___block_literal_global.4424
- ___block_literal_global.4668
- ___block_literal_global.4680
- ___block_literal_global.4730
- ___block_literal_global.489
- ___block_literal_global.5229
- ___block_literal_global.5290
- ___block_literal_global.5843
- ___block_literal_global.7253
- ___block_literal_global.7264
- ___block_literal_global.8310
- ___block_literal_global.8675
- ___block_literal_global.8730
- ___block_literal_global.8825
- ___block_literal_global.8840
- ___block_literal_global.9116
- ___block_literal_global.9727
- ___block_literal_global.9755
- _objc_msgSend$handlePE:withImpact:
- _objc_msgSend$handlePeerListenerEvent:withMessage:withClientID:withProcessName:withKey:withPayload:
- _objc_msgSend$handlePeerResponderEvent:withMessage:withClientID:withProcessName:withKey:withPayload:
- _objc_msgSend$handlePeerShouldLogEvent:withMessage:withClientID:withProcessName:withKey:
- _objc_msgSend$logEventPointBatteryUIVisit
- _objc_msgSend$setBatteryUIVisitNotification:
CStrings:
+ "-[PLXPCService handlePeerListenerEvent:withMessage:withClientID:withProcessName:withKey:withPayload:withPeer:]"
+ "-[PLXPCService handlePeerResponderEvent:withMessage:withClientID:withProcessName:withKey:withPayload:withPeer:]"
+ "-[PLXPCService handlePeerResponderEvent:withMessage:withClientID:withProcessName:withKey:withPayload:withPeer:]_block_invoke"
+ "-[PLXPCService handlePeerResponderEvent:withMessage:withClientID:withProcessName:withKey:withPayload:withPeer:]_block_invoke_2"
+ "-[PLXPCService handlePeerShouldLogEvent:withMessage:withClientID:withProcessName:withKey:withPeer:]"
+ "AppDetailVisit"
+ "DailyUsageSummary"
+ "DetailVisit"
+ "ISP,IOP State"
+ "Insights"
+ "InsightsAndSuggestions"
+ "PCPUDTL012"
+ "PCPUDTL112"
+ "PCPUDTL212"
+ "PCPUDTL311"
+ "PCPUDTL312"
+ "PMP,DCS Ceiling"
+ "Qualifiers"
+ "Relay: locale requested"
+ "Setting up locale responder..."
+ "T@\"PLCFNotificationOperatorComposition\",&,V_batteryAppDetailVisitNotification"
+ "T@\"PLCFNotificationOperatorComposition\",&,V_batteryDetailVisitNotification"
+ "T@\"PLXPCListenerOperatorComposition\",&,V_batteryUIInsightsListener"
+ "T@\"PLXPCListenerOperatorComposition\",&,V_batteryUIVisitsListener"
+ "T@\"PLXPCResponderOperatorComposition\",&,V_localeResponder"
+ "UsageSummary"
+ "_batteryAppDetailVisitNotification"
+ "_batteryDetailVisitNotification"
+ "_batteryUIInsightsListener"
+ "_batteryUIVisitsListener"
+ "_localeResponder"
+ "batteryAppDetailVisitNotification"
+ "batteryDetailVisitNotification"
+ "batteryUIInsightsListener"
+ "batteryUIVisitsListener"
+ "com.apple.powerlog.AppDetailViewVisit"
+ "com.apple.powerlog.ShowAllUsageViewVisit"
+ "com.apple.powerlog.locale"
+ "failed to convert exception monotonic time to system time"
+ "failed to copy payload dictionary"
+ "handlePE:withImpact:withTimestamp:"
+ "handlePeerListenerEvent:withMessage:withClientID:withProcessName:withKey:withPayload:withPeer:"
+ "handlePeerResponderEvent:withMessage:withClientID:withProcessName:withKey:withPayload:withPeer:"
+ "handlePeerShouldLogEvent:withMessage:withClientID:withProcessName:withKey:withPeer:"
+ "insertSystemTime:fromPLEntry:"
+ "invalid payload for timestamp"
+ "invalid violation monotonic time for exception"
+ "isBasebandMavToAllowSysdiagnoseTrigger"
+ "isPowerexceptionsd"
+ "localeResponder"
+ "logEventPointBatteryUIAppDetailVisit"
+ "logEventPointBatteryUIDetailVisit"
+ "logEventPointBatteryUIInsightsAndSuggestionsWithPayload:"
+ "logEventPointBatteryUIVisitWithPayload:"
+ "peTimestamp"
+ "relayActive"
+ "setBatteryAppDetailVisitNotification:"
+ "setBatteryDetailVisitNotification:"
+ "setBatteryUIInsightsListener:"
+ "setBatteryUIVisitsListener:"
+ "setLocaleResponder:"
+ "v68@0:8@16@24s32@36@44@52@60"
+ "violation end time is neither NSNumber nor NSDate: %@"
+ "wcacheOverWrLogSizeCnts"
+ "wcacheOverWrSizeByFlow"
+ "wcacheWr"
+ "wcache_Mbytes"
+ "wcache_Reads"
+ "wcache_segsSortedLogSize"
- "-[PLBatteryBreakdownService shouldShowOngoingRestoreInsight]"
- "-[PLXPCService handlePeerListenerEvent:withMessage:withClientID:withProcessName:withKey:withPayload:]"
- "-[PLXPCService handlePeerResponderEvent:withMessage:withClientID:withProcessName:withKey:withPayload:]"
- "-[PLXPCService handlePeerResponderEvent:withMessage:withClientID:withProcessName:withKey:withPayload:]_block_invoke"
- "-[PLXPCService handlePeerResponderEvent:withMessage:withClientID:withProcessName:withKey:withPayload:]_block_invoke_2"
- "-[PLXPCService handlePeerShouldLogEvent:withMessage:withClientID:withProcessName:withKey:]"
- "T@\"PLCFNotificationOperatorComposition\",&,V_batteryUIVisitNotification"
- "_batteryUIVisitNotification"
- "batteryUIVisitNotification"
- "bui_device_setup"
- "com.apple.batteryui"
- "com.apple.powerlogd.logBatteryUIVisit"
- "handlePE:withImpact:"
- "handlePeerListenerEvent:withMessage:withClientID:withProcessName:withKey:withPayload:"
- "handlePeerResponderEvent:withMessage:withClientID:withProcessName:withKey:withPayload:"
- "handlePeerShouldLogEvent:withMessage:withClientID:withProcessName:withKey:"
- "logEventPointBatteryUIVisit"
- "setBatteryUIVisitNotification:"
- "shouldShowOngoingRestoreInsight"
- "shouldShowOngoingRestoreInsight = %@"
- "v52@0:8@16@24s32@36@44"

```
