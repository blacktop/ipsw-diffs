## PowerlogHelperdOperators

> `/System/Library/PrivateFrameworks/PowerlogHelperdOperators.framework/PowerlogHelperdOperators`

```diff

-2964.0.40.502.1
-  __TEXT.__text: 0x1c100c
-  __TEXT.__auth_stubs: 0x1b60
-  __TEXT.__objc_methlist: 0xe6c8
+2964.0.64.0.0
+  __TEXT.__text: 0x1c22ec
+  __TEXT.__auth_stubs: 0x1b70
+  __TEXT.__objc_methlist: 0xe810
   __TEXT.__const: 0x6a8
-  __TEXT.__cstring: 0x232a2
-  __TEXT.__oslogstring: 0x11d6a
-  __TEXT.__gcc_except_tab: 0x25fc
+  __TEXT.__cstring: 0x232d2
+  __TEXT.__oslogstring: 0x11dd4
+  __TEXT.__gcc_except_tab: 0x2620
   __TEXT.__ustring: 0x10
-  __TEXT.__unwind_info: 0x3670
-  __TEXT.__objc_classname: 0xb7b
-  __TEXT.__objc_methname: 0x30dfa
-  __TEXT.__objc_methtype: 0x275c
-  __TEXT.__objc_stubs: 0x1e880
-  __DATA_CONST.__got: 0xe68
+  __TEXT.__unwind_info: 0x3690
+  __TEXT.__objc_classname: 0xbae
+  __TEXT.__objc_methname: 0x31145
+  __TEXT.__objc_methtype: 0x276d
+  __TEXT.__objc_stubs: 0x1e9c0
+  __DATA_CONST.__got: 0xe80
   __DATA_CONST.__const: 0x4380
-  __DATA_CONST.__objc_classlist: 0x308
+  __DATA_CONST.__objc_classlist: 0x310
   __DATA_CONST.__objc_nlclslist: 0x108
   __DATA_CONST.__objc_protolist: 0x50
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x9780
+  __DATA_CONST.__objc_selrefs: 0x97f0
   __DATA_CONST.__objc_protorefs: 0x8
   __DATA_CONST.__objc_superrefs: 0x288
-  __DATA_CONST.__objc_arraydata: 0x14928
-  __AUTH_CONST.__auth_got: 0xdc8
-  __AUTH_CONST.__const: 0x18a0
-  __AUTH_CONST.__cfstring: 0x31600
-  __AUTH_CONST.__objc_const: 0x12100
-  __AUTH_CONST.__objc_intobj: 0x25c8
-  __AUTH_CONST.__objc_dictobj: 0x33e0
-  __AUTH_CONST.__objc_doubleobj: 0xb50
-  __AUTH_CONST.__objc_arrayobj: 0x2aa8
-  __AUTH.__objc_data: 0x8c0
-  __DATA.__objc_ivar: 0x1214
+  __DATA_CONST.__objc_arraydata: 0x14998
+  __AUTH_CONST.__auth_got: 0xdd0
+  __AUTH_CONST.__const: 0x18c0
+  __AUTH_CONST.__cfstring: 0x316e0
+  __AUTH_CONST.__objc_const: 0x12378
+  __AUTH_CONST.__objc_intobj: 0x2688
+  __AUTH_CONST.__objc_dictobj: 0x34d0
+  __AUTH_CONST.__objc_doubleobj: 0xb60
+  __AUTH_CONST.__objc_arrayobj: 0x2ad8
+  __AUTH.__objc_data: 0x910
+  __DATA.__objc_ivar: 0x1234
   __DATA.__data: 0x400
-  __DATA.__bss: 0x2350
+  __DATA.__bss: 0x2368
   __DATA.__common: 0x74
   __DATA_DIRTY.__objc_data: 0x1590
   __DATA_DIRTY.__data: 0x10
-  __DATA_DIRTY.__bss: 0x3c0
+  __DATA_DIRTY.__bss: 0x398
   __DATA_DIRTY.__common: 0x8
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/CoreLocation.framework/CoreLocation

   - /usr/lib/libc++.1.dylib
   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libz.1.dylib
-  UUID: 8C4813AC-B638-39C4-B284-F50C1ADEE235
-  Functions: 7698
-  Symbols:   26141
-  CStrings:  22235
+  UUID: 76209B7B-BD6A-37D6-96EA-F9FC8EF2586F
+  Functions: 7733
+  Symbols:   26239
+  CStrings:  22274
 
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
+ -[PLBatteryUINotificationService ursaTTRContent:].cold.5
+ -[PLBatteryUIResponseTypeDrainComparisonSummary getEnergyForAppWithBundleID:inDateInterval:forRootNodes:]
+ -[PLBatteryUIResponseTypeOngoingDeviceSetupInsight .cxx_destruct]
+ -[PLBatteryUIResponseTypeOngoingDeviceSetupInsight coalesce]
+ -[PLBatteryUIResponseTypeOngoingDeviceSetupInsight configure:]
+ -[PLBatteryUIResponseTypeOngoingDeviceSetupInsight dependencies]
+ -[PLBatteryUIResponseTypeOngoingDeviceSetupInsight didUpgradeInLast:]
+ -[PLBatteryUIResponseTypeOngoingDeviceSetupInsight end]
+ -[PLBatteryUIResponseTypeOngoingDeviceSetupInsight lastUpgradeTimestamp]
+ -[PLBatteryUIResponseTypeOngoingDeviceSetupInsight responderService]
+ -[PLBatteryUIResponseTypeOngoingDeviceSetupInsight result]
+ -[PLBatteryUIResponseTypeOngoingDeviceSetupInsight run]
+ -[PLBatteryUIResponseTypeOngoingDeviceSetupInsight setEnd:]
+ -[PLBatteryUIResponseTypeOngoingDeviceSetupInsight setLastUpgradeTimestamp:]
+ -[PLBatteryUIResponseTypeOngoingDeviceSetupInsight setResponderService:]
+ -[PLBatteryUIResponseTypeOngoingDeviceSetupInsight setSuggest:]
+ -[PLBatteryUIResponseTypeOngoingDeviceSetupInsight shouldShowSuggestionThroughOverrides]
+ -[PLBatteryUIResponseTypeOngoingDeviceSetupInsight suggest]
+ -[PLXPCService handlePeerListenerEvent:withMessage:withClientID:withProcessName:withKey:withPayload:withPeer:]
+ -[PLXPCService handlePeerListenerEvent:withMessage:withClientID:withProcessName:withKey:withPayload:withPeer:].cold.1
+ -[PLXPCService handlePeerListenerEvent:withMessage:withClientID:withProcessName:withKey:withPayload:withPeer:].cold.2
+ -[PLXPCService handlePeerResponderEvent:withMessage:withClientID:withProcessName:withKey:withPayload:withPeer:]
+ -[PLXPCService handlePeerResponderEvent:withMessage:withClientID:withProcessName:withKey:withPayload:withPeer:].cold.1
+ -[PLXPCService handlePeerResponderEvent:withMessage:withClientID:withProcessName:withKey:withPayload:withPeer:].cold.2
+ -[PLXPCService handlePeerResponderEvent:withMessage:withClientID:withProcessName:withKey:withPayload:withPeer:].cold.3
+ -[PLXPCService handlePeerShouldLogEvent:withMessage:withClientID:withProcessName:withKey:withPeer:]
+ -[PLXPCService handlePeerShouldLogEvent:withMessage:withClientID:withProcessName:withKey:withPeer:].cold.1
+ -[PLXPCService handlePeerShouldLogEvent:withMessage:withClientID:withProcessName:withKey:withPeer:].cold.2
+ -[PLXPCService handlePeerShouldLogEvent:withMessage:withClientID:withProcessName:withKey:withPeer:].cold.3
+ -[PLXPCService init].cold.6
+ -[PLXPCService localeResponder]
+ -[PLXPCService setLocaleResponder:]
+ GCC_except_table197
+ GCC_except_table260
+ GCC_except_table274
+ GCC_except_table275
+ GCC_except_table323
+ GCC_except_table327
+ GCC_except_table432
+ GCC_except_table67
+ _NSLocaleIdentifier
+ _OBJC_CLASS_$_PLBatteryUIResponseTypeOngoingDeviceSetupInsight
+ _OBJC_CLASS_$_PLXPCRelay
+ _OBJC_IVAR_$_PLBatteryAgent._batteryAppDetailVisitNotification
+ _OBJC_IVAR_$_PLBatteryAgent._batteryDetailVisitNotification
+ _OBJC_IVAR_$_PLBatteryAgent._batteryUIInsightsListener
+ _OBJC_IVAR_$_PLBatteryAgent._batteryUIVisitsListener
+ _OBJC_IVAR_$_PLBatteryUIResponseTypeOngoingDeviceSetupInsight._end
+ _OBJC_IVAR_$_PLBatteryUIResponseTypeOngoingDeviceSetupInsight._lastUpgradeTimestamp
+ _OBJC_IVAR_$_PLBatteryUIResponseTypeOngoingDeviceSetupInsight._responderService
+ _OBJC_IVAR_$_PLBatteryUIResponseTypeOngoingDeviceSetupInsight._suggest
+ _OBJC_IVAR_$_PLXPCService._localeResponder
+ _OBJC_METACLASS_$_PLBatteryUIResponseTypeOngoingDeviceSetupInsight
+ _PLLogRelay
+ __OBJC_$_INSTANCE_METHODS_PLBatteryUIResponseTypeOngoingDeviceSetupInsight
+ __OBJC_$_INSTANCE_VARIABLES_PLBatteryUIResponseTypeOngoingDeviceSetupInsight
+ __OBJC_$_PROP_LIST_PLBatteryUIResponseTypeOngoingDeviceSetupInsight
+ __OBJC_CLASS_PROTOCOLS_$_PLBatteryUIResponseTypeOngoingDeviceSetupInsight
+ __OBJC_CLASS_RO_$_PLBatteryUIResponseTypeOngoingDeviceSetupInsight
+ __OBJC_METACLASS_RO_$_PLBatteryUIResponseTypeOngoingDeviceSetupInsight
+ ___110-[PLXPCService handlePeerListenerEvent:withMessage:withClientID:withProcessName:withKey:withPayload:withPeer:]_block_invoke
+ ___110-[PLXPCService handlePeerListenerEvent:withMessage:withClientID:withProcessName:withKey:withPayload:withPeer:]_block_invoke.880
+ ___111-[PLXPCService handlePeerResponderEvent:withMessage:withClientID:withProcessName:withKey:withPayload:withPeer:]_block_invoke
+ ___111-[PLXPCService handlePeerResponderEvent:withMessage:withClientID:withProcessName:withKey:withPayload:withPeer:]_block_invoke.811
+ ___111-[PLXPCService handlePeerResponderEvent:withMessage:withClientID:withProcessName:withKey:withPayload:withPeer:]_block_invoke.823
+ ___111-[PLXPCService handlePeerResponderEvent:withMessage:withClientID:withProcessName:withKey:withPayload:withPeer:]_block_invoke.827
+ ___111-[PLXPCService handlePeerResponderEvent:withMessage:withClientID:withProcessName:withKey:withPayload:withPeer:]_block_invoke.827.cold.1
+ ___111-[PLXPCService handlePeerResponderEvent:withMessage:withClientID:withProcessName:withKey:withPayload:withPeer:]_block_invoke.827.cold.2
+ ___111-[PLXPCService handlePeerResponderEvent:withMessage:withClientID:withProcessName:withKey:withPayload:withPeer:]_block_invoke.849
+ ___111-[PLXPCService handlePeerResponderEvent:withMessage:withClientID:withProcessName:withKey:withPayload:withPeer:]_block_invoke.856
+ ___111-[PLXPCService handlePeerResponderEvent:withMessage:withClientID:withProcessName:withKey:withPayload:withPeer:]_block_invoke.863
+ ___111-[PLXPCService handlePeerResponderEvent:withMessage:withClientID:withProcessName:withKey:withPayload:withPeer:]_block_invoke.863.cold.1
+ ___111-[PLXPCService handlePeerResponderEvent:withMessage:withClientID:withProcessName:withKey:withPayload:withPeer:]_block_invoke.870
+ ___111-[PLXPCService handlePeerResponderEvent:withMessage:withClientID:withProcessName:withKey:withPayload:withPeer:]_block_invoke.874
+ ___111-[PLXPCService handlePeerResponderEvent:withMessage:withClientID:withProcessName:withKey:withPayload:withPeer:]_block_invoke_2
+ ___111-[PLXPCService handlePeerResponderEvent:withMessage:withClientID:withProcessName:withKey:withPayload:withPeer:]_block_invoke_2.864
+ ___20-[PLXPCService init]_block_invoke.612
+ ___20-[PLXPCService init]_block_invoke.612.cold.1
+ ___22-[PLBatteryAgent init]_block_invoke.3262
+ ___22-[PLBatteryAgent init]_block_invoke.3262.cold.1
+ ___22-[PLBatteryAgent init]_block_invoke.3262.cold.10
+ ___22-[PLBatteryAgent init]_block_invoke.3262.cold.11
+ ___22-[PLBatteryAgent init]_block_invoke.3262.cold.2
+ ___22-[PLBatteryAgent init]_block_invoke.3262.cold.3
+ ___22-[PLBatteryAgent init]_block_invoke.3262.cold.4
+ ___22-[PLBatteryAgent init]_block_invoke.3262.cold.5
+ ___22-[PLBatteryAgent init]_block_invoke.3262.cold.6
+ ___22-[PLBatteryAgent init]_block_invoke.3262.cold.7
+ ___22-[PLBatteryAgent init]_block_invoke.3262.cold.8
+ ___22-[PLBatteryAgent init]_block_invoke.3262.cold.9
+ ___22-[PLBatteryAgent init]_block_invoke.3274
+ ___22-[PLBatteryAgent init]_block_invoke.3276
+ ___22-[PLBatteryAgent init]_block_invoke.3305
+ ___22-[PLBatteryAgent init]_block_invoke.3313
+ ___22-[PLBatteryAgent init]_block_invoke.3313.cold.1
+ ___22-[PLBatteryAgent init]_block_invoke.3313.cold.2
+ ___22-[PLBatteryAgent init]_block_invoke.3319
+ ___22-[PLBatteryAgent init]_block_invoke.3323
+ ___22-[PLBatteryAgent init]_block_invoke_2.3345
+ ___24-[PLBatteryAgent xFlags]_block_invoke.5073
+ ___24-[PLBatteryAgent xFlags]_block_invoke.5082
+ ___24-[PLBatteryAgent xFlags]_block_invoke.5097
+ ___24-[PLBatteryAgent xFlags]_block_invoke.5103
+ ___24-[PLBatteryAgent xFlags]_block_invoke.5109
+ ___24-[PLBatteryAgent xFlags]_block_invoke.5118
+ ___24-[PLBatteryAgent xFlags]_block_invoke.5124
+ ___24-[PLBatteryAgent xFlags]_block_invoke.5130
+ ___32-[PLBatteryAgent aggdTimerFired]_block_invoke.4751
+ ___32-[PLBatteryAgent getIOPSDevices]_block_invoke.3443
+ ___32-[PLBatteryAgent getIOPSDevices]_block_invoke.3449
+ ___33-[PLBatteryAgent cancelEALogging]_block_invoke.3434
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
+ ___42-[PLBatteryAgent initOperatorDependancies]_block_invoke.3521
+ ___42-[PLBatteryAgent initOperatorDependancies]_block_invoke.3527
+ ___42-[PLBatteryAgent initOperatorDependancies]_block_invoke.3527.cold.1
+ ___42-[PLBatteryAgent initOperatorDependancies]_block_invoke.3543
+ ___42-[PLBatteryAgent initOperatorDependancies]_block_invoke.3576
+ ___42-[PLBatteryAgent initOperatorDependancies]_block_invoke.3636
+ ___42-[PLBatteryAgent initOperatorDependancies]_block_invoke.3636.cold.1
+ ___42-[PLBatteryAgent initOperatorDependancies]_block_invoke.3636.cold.2
+ ___42-[PLBatteryAgent initOperatorDependancies]_block_invoke.3636.cold.3
+ ___42-[PLBatteryAgent initOperatorDependancies]_block_invoke.3653.cold.1
+ ___42-[PLBatteryAgent initOperatorDependancies]_block_invoke.3664
+ ___42-[PLBatteryAgent initOperatorDependancies]_block_invoke.3668
+ ___42-[PLBatteryAgent initOperatorDependancies]_block_invoke.3668.cold.1
+ ___42-[PLBatteryAgent initOperatorDependancies]_block_invoke.3676
+ ___42-[PLBatteryAgent initOperatorDependancies]_block_invoke.3676.cold.1
+ ___42-[PLBatteryAgent initOperatorDependancies]_block_invoke.3683
+ ___42-[PLBatteryAgent initOperatorDependancies]_block_invoke.3692
+ ___42-[PLBatteryAgent initOperatorDependancies]_block_invoke.3698
+ ___42-[PLBatteryAgent initOperatorDependancies]_block_invoke.3705
+ ___42-[PLBatteryAgent initOperatorDependancies]_block_invoke.3705.cold.1
+ ___42-[PLBatteryAgent initOperatorDependancies]_block_invoke.3712
+ ___42-[PLBatteryAgent initOperatorDependancies]_block_invoke.3712.cold.1
+ ___42-[PLBatteryAgent initOperatorDependancies]_block_invoke.3726
+ ___42-[PLBatteryAgent initOperatorDependancies]_block_invoke.3726.cold.1
+ ___42-[PLBatteryAgent initOperatorDependancies]_block_invoke.3731
+ ___42-[PLBatteryAgent initOperatorDependancies]_block_invoke.3731.cold.1
+ ___42-[PLBatteryAgent initOperatorDependancies]_block_invoke.3738
+ ___42-[PLBatteryAgent initOperatorDependancies]_block_invoke.3761
+ ___42-[PLBatteryAgent initOperatorDependancies]_block_invoke_2.3528
+ ___42-[PLBatteryAgent initOperatorDependancies]_block_invoke_2.3573
+ ___42-[PLBatteryAgent initOperatorDependancies]_block_invoke_2.3588
+ ___42-[PLBatteryAgent initOperatorDependancies]_block_invoke_2.3660
+ ___42-[PLBatteryAgent initOperatorDependancies]_block_invoke_2.3677
+ ___42-[PLBatteryAgent initOperatorDependancies]_block_invoke_2.3687
+ ___42-[PLBatteryAgent initOperatorDependancies]_block_invoke_2.3706
+ ___42-[PLBatteryAgent initOperatorDependancies]_block_invoke_2.3713
+ ___42-[PLBatteryAgent initOperatorDependancies]_block_invoke_2.3769
+ ___42-[PLBatteryAgent initOperatorDependancies]_block_invoke_3.3777
+ ___42-[PLBatteryAgent initOperatorDependancies]_block_invoke_4.3785
+ ___42-[PLBatteryAgent initOperatorDependancies]_block_invoke_5.3789
+ ___42-[PLBatteryAgent initOperatorDependancies]_block_invoke_6.3793
+ ___42-[PLBatteryAgent initOperatorDependancies]_block_invoke_7.3797
+ ___42-[PLBatteryAgent initOperatorDependancies]_block_invoke_8
+ ___42-[PLBatteryAgent initOperatorDependancies]_block_invoke_9
+ ___42-[PLBatteryAgent initSmartChargingLogging]_block_invoke.5294
+ ___42-[PLBatteryAgent initSmartChargingLogging]_block_invoke.5294.cold.1
+ ___42-[PLBatteryAgent initSmartChargingLogging]_block_invoke.5294.cold.2
+ ___42-[PLBatteryAgent initSmartChargingLogging]_block_invoke.5302
+ ___42-[PLBatteryAgent initSmartChargingLogging]_block_invoke_2.5296
+ ___42-[PLBatteryAgent logEventIntervalGasGauge]_block_invoke.4016
+ ___42-[PLXPCService resetPermissionsForClients]_block_invoke.687
+ ___42-[PLXPCService resetPermissionsForClients]_block_invoke.697
+ ___44-[PLXPCService respondToEvent:withResponse:]_block_invoke.651
+ ___44-[PLXPCService respondToEvent:withResponse:]_block_invoke.657
+ ___45-[PLBatteryAgent logCPMSSnapshotWithTrigger:]_block_invoke.5330
+ ___45-[PLBatteryAgent logCPMSSnapshotWithTrigger:]_block_invoke.5331
+ ___45-[PLBatteryAgent logCPMSSnapshotWithTrigger:]_block_invoke.5332
+ ___45-[PLBatteryAgent logCPMSSnapshotWithTrigger:]_block_invoke.5333
+ ___45-[PLBatteryAgent logCPMSSnapshotWithTrigger:]_block_invoke.5334
+ ___45-[PLBatteryAgent logCPMSSnapshotWithTrigger:]_block_invoke.5334.cold.1
+ ___45-[PLBatteryAgent logCPMSSnapshotWithTrigger:]_block_invoke.5335
+ ___45-[PLBatteryAgent logCPMSSnapshotWithTrigger:]_block_invoke.5335.cold.1
+ ___45-[PLBatteryAgent logCPMSSnapshotWithTrigger:]_block_invoke.5336
+ ___45-[PLBatteryAgent logCPMSSnapshotWithTrigger:]_block_invoke.5336.cold.1
+ ___45-[PLBatteryAgent logCPMSSnapshotWithTrigger:]_block_invoke.5377
+ ___46-[PLApplicationAgent initOperatorDependancies]_block_invoke.417
+ ___46-[PLApplicationAgent initOperatorDependancies]_block_invoke.446
+ ___46-[PLApplicationAgent initOperatorDependancies]_block_invoke.446.cold.1
+ ___46-[PLApplicationAgent initOperatorDependancies]_block_invoke.452
+ ___46-[PLApplicationAgent initOperatorDependancies]_block_invoke.452.cold.1
+ ___46-[PLApplicationAgent initOperatorDependancies]_block_invoke.457
+ ___46-[PLApplicationAgent initOperatorDependancies]_block_invoke.457.cold.1
+ ___46-[PLApplicationAgent initOperatorDependancies]_block_invoke.464
+ ___46-[PLApplicationAgent initOperatorDependancies]_block_invoke.464.cold.1
+ ___46-[PLApplicationAgent initOperatorDependancies]_block_invoke.474
+ ___46-[PLApplicationAgent initOperatorDependancies]_block_invoke.474.cold.1
+ ___46-[PLApplicationAgent initOperatorDependancies]_block_invoke.481
+ ___46-[PLApplicationAgent initOperatorDependancies]_block_invoke.481.cold.1
+ ___46-[PLApplicationAgent initOperatorDependancies]_block_invoke.488
+ ___46-[PLApplicationAgent initOperatorDependancies]_block_invoke.488.cold.1
+ ___46-[PLApplicationAgent initOperatorDependancies]_block_invoke.493
+ ___46-[PLApplicationAgent initOperatorDependancies]_block_invoke.493.cold.1
+ ___46-[PLApplicationAgent initOperatorDependancies]_block_invoke.498
+ ___46-[PLApplicationAgent initOperatorDependancies]_block_invoke.498.cold.1
+ ___46-[PLApplicationAgent initOperatorDependancies]_block_invoke.506
+ ___46-[PLApplicationAgent initOperatorDependancies]_block_invoke.506.cold.1
+ ___46-[PLApplicationAgent initOperatorDependancies]_block_invoke.514
+ ___46-[PLApplicationAgent initOperatorDependancies]_block_invoke.514.cold.1
+ ___46-[PLApplicationAgent initOperatorDependancies]_block_invoke.519
+ ___46-[PLApplicationAgent initOperatorDependancies]_block_invoke.519.cold.1
+ ___46-[PLApplicationAgent initOperatorDependancies]_block_invoke.524
+ ___46-[PLApplicationAgent initOperatorDependancies]_block_invoke.524.cold.1
+ ___46-[PLApplicationAgent initOperatorDependancies]_block_invoke.539
+ ___46-[PLApplicationAgent initOperatorDependancies]_block_invoke.539.cold.1
+ ___46-[PLApplicationAgent initOperatorDependancies]_block_invoke.547
+ ___46-[PLApplicationAgent initOperatorDependancies]_block_invoke.547.cold.1
+ ___46-[PLApplicationAgent initOperatorDependancies]_block_invoke_2.420
+ ___46-[PLApplicationAgent initOperatorDependancies]_block_invoke_2.526
+ ___46-[PLApplicationAgent initOperatorDependancies]_block_invoke_2.526.cold.1
+ ___46-[PLApplicationAgent initOperatorDependancies]_block_invoke_2.526.cold.2
+ ___50-[PLBatteryAgent initializeChargingStateIntervals]_block_invoke.5319
+ ___50-[PLBatteryAgent initializeChargingStateIntervals]_block_invoke.5320
+ ___50-[PLBatteryAgent initializeChargingStateIntervals]_block_invoke.5324
+ ___50-[PLBatteryAgent initializeChargingStateIntervals]_block_invoke.5324.cold.1
+ ___50-[PLBatteryAgent initializeChargingStateIntervals]_block_invoke.5324.cold.2
+ ___54-[PLXPCService handleSingleMessage:fromPeer:forEvent:]_block_invoke.760
+ ___54-[PLXPCService handleSingleMessage:fromPeer:forEvent:]_block_invoke.763
+ ___54-[PLXPCService handleSingleMessage:fromPeer:forEvent:]_block_invoke.769
+ ___54-[PLXPCService handleSingleMessage:fromPeer:forEvent:]_block_invoke.775
+ ___54-[PLXPCService handleSingleMessage:fromPeer:forEvent:]_block_invoke.781
+ ___54-[PLXPCService handleSingleMessage:fromPeer:forEvent:]_block_invoke.787
+ ___55-[PLBatteryAgent logEventNoneBatteryConfigWithRawData:]_block_invoke.5007
+ ___55-[PLBatteryAgent logEventNoneBatteryConfigWithRawData:]_block_invoke.5007.cold.1
+ ___55-[PLBatteryAgent logEventNoneBatteryConfigWithRawData:]_block_invoke.5011
+ ___55-[PLBatteryAgent logEventNoneBatteryConfigWithRawData:]_block_invoke.5011.cold.1
+ ___55-[PLBatteryAgent logEventNoneBatteryConfigWithRawData:]_block_invoke.5016
+ ___55-[PLBatteryAgent logEventNoneBatteryConfigWithRawData:]_block_invoke.5020
+ ___55-[PLBatteryAgent logEventNoneBatteryConfigWithRawData:]_block_invoke_2.5012
+ ___55-[PLBatteryAgent logEventNoneBatteryConfigWithRawData:]_block_invoke_2.5017
+ ___56-[PLApplicationAgent createWidgetStatsAccountingEvents:]_block_invoke.577
+ ___58-[PLBatteryUIResponseTypeOngoingDeviceSetupInsight result]_block_invoke
+ ___58-[PLBatteryUIResponseTypeOngoingDeviceSetupInsight result]_block_invoke_2
+ ___59-[PLBatteryAgent setupEALoggingTriggeredByConnectionEvent:]_block_invoke.3414
+ ___61-[PLBatteryBreakdownService mapDeletedAppsWithEnergyEntries:]_block_invoke.1810
+ ___61-[PLBatteryUIResponderService convertResponseToLegacyFormat:]_block_invoke.225
+ ___61-[PLBatteryUIResponderService convertResponseToLegacyFormat:]_block_invoke.269
+ ___63-[PLBatteryBreakdownService mapPluginsToAppsWithEnergyEntries:]_block_invoke.1819
+ ___64-[PLBatteryBreakdownService combineDuplicatesWithEnergyEntries:]_block_invoke.1883
+ ___64-[PLBatteryBreakdownService combineDuplicatesWithEnergyEntries:]_block_invoke.1887
+ ___65-[PLBatteryAgent logEventBackwardHeatMapCallback:andHeatMapType:]_block_invoke.4414
+ ___65-[PLBatteryUIResponseTypeBatteryBreakdown collapseEnergyEntries:]_block_invoke.575
+ ___66-[PLBatteryUIResponseTypeBatteryBreakdown reaccountBackupRestore:]_block_invoke.607
+ ___67-[PLBatteryBreakdownService filterWithEnergyEntries:withQueryType:]_block_invoke.1904
+ ___68-[PLBatteryBreakdownService determineDisplayNamesWithEnergyEntries:]_block_invoke.1898
+ ___69-[PLBatteryBreakdownService reaccountBackupRestoreWithEnergyEntries:]_block_invoke.1872
+ ___71-[PLBatteryUIResponseTypeBatteryBreakdown transformPlugins:withBucket:]_block_invoke.621
+ ___73-[PLBatteryBreakdownService populateRootNodeEnergyKeysWithEnergyEntries:]_block_invoke.1603
+ ___74-[PLBatteryBreakdownService filterEnergyEntriesBasedOnTime:withQueryType:]_block_invoke.1736
+ ___74-[PLBatteryBreakdownService filterEnergyEntriesBasedOnTime:withQueryType:]_block_invoke.1748
+ ___74-[PLBatteryBreakdownService filterEnergyEntriesBasedOnTime:withQueryType:]_block_invoke.1756
+ ___75-[PLBatteryAgent showOrHideTLCNotification:meetsTLCNotificationConditions:]_block_invoke.3386
+ ___75-[PLBatteryBreakdownService addNotificationValues:withRange:withQueryType:]_block_invoke.1726
+ ___76-[PLBatteryUIResponseTypeDrainComparisonSummary getBundleIDToDisplayNameMap]_block_invoke.192
+ ___77-[PLBatteryBreakdownService applyStaticNameTransformationsWithEnergyEntries:]_block_invoke.1777
+ ___77-[PLBatteryBreakdownService applyStaticNameTransformationsWithEnergyEntries:]_block_invoke.1791
+ ___81-[PLApplicationAgent logInstalledAppWithRecord:withBundleID:shouldMaskTimestamp:]_block_invoke.617
+ ___81-[PLBatteryBreakdownService qualifiersWithEnergyEntry:bucketSize:andTotalEnergy:]_block_invoke.1939
+ ___81-[PLBatteryBreakdownService qualifiersWithEnergyEntry:bucketSize:andTotalEnergy:]_block_invoke.1956
+ ___81-[PLBatteryBreakdownService qualifiersWithEnergyEntry:bucketSize:andTotalEnergy:]_block_invoke.1964
+ ___81-[PLBatteryBreakdownService qualifiersWithEnergyEntry:bucketSize:andTotalEnergy:]_block_invoke.1972
+ ___81-[PLBatteryBreakdownService qualifiersWithEnergyEntry:bucketSize:andTotalEnergy:]_block_invoke.2014
+ ___81-[PLBatteryBreakdownService qualifiersWithEnergyEntry:bucketSize:andTotalEnergy:]_block_invoke.2024
+ ___84+[PLBatteryUIResponseTypeUtilities getBundleIDToDisplayNameMapWithResponderService:]_block_invoke.472
+ ___84+[PLBatteryUIResponseTypeUtilities getPluginBundleIDToEntryMapWithResponderService:]_block_invoke.444
+ ___84+[PLBatteryUIResponseTypeUtilities getPluginBundleIDToEntryMapWithResponderService:]_block_invoke.450
+ ___88-[PLBatteryBreakdownService energyEntriesWithRange:withEntryTimeInterval:withQueryType:]_block_invoke.1528
+ ___99-[PLXPCService handlePeerShouldLogEvent:withMessage:withClientID:withProcessName:withKey:withPeer:]_block_invoke
+ ___99-[PLXPCService handlePeerShouldLogEvent:withMessage:withClientID:withProcessName:withKey:withPeer:]_block_invoke.802
+ ___block_literal_global.2094
+ ___block_literal_global.218
+ ___block_literal_global.259
+ ___block_literal_global.3249
+ ___block_literal_global.3360
+ ___block_literal_global.3373
+ ___block_literal_global.3388
+ ___block_literal_global.3489
+ ___block_literal_global.351
+ ___block_literal_global.3546
+ ___block_literal_global.3590
+ ___block_literal_global.3599
+ ___block_literal_global.3608
+ ___block_literal_global.3620
+ ___block_literal_global.3733
+ ___block_literal_global.3803
+ ___block_literal_global.3809
+ ___block_literal_global.3819
+ ___block_literal_global.4463
+ ___block_literal_global.4707
+ ___block_literal_global.4719
+ ___block_literal_global.4769
+ ___block_literal_global.526
+ ___block_literal_global.5268
+ ___block_literal_global.5329
+ ___block_literal_global.543
+ ___block_literal_global.550
+ _applyStaticNameTransformationsWithEnergyEntries:.classDebugEnabled.1776
+ _applyStaticNameTransformationsWithEnergyEntries:.classDebugEnabled.1790
+ _applyStaticNameTransformationsWithEnergyEntries:.defaultOnce.1775
+ _applyStaticNameTransformationsWithEnergyEntries:.defaultOnce.1789
+ _cancelEALogging.classDebugEnabled.3433
+ _cancelEALogging.defaultOnce.3432
+ _combineDuplicatesWithEnergyEntries:.classDebugEnabled.1882
+ _combineDuplicatesWithEnergyEntries:.classDebugEnabled.1889
+ _combineDuplicatesWithEnergyEntries:.defaultOnce.1881
+ _combineDuplicatesWithEnergyEntries:.defaultOnce.1888
+ _dailyTasks.defaultOnce.630
+ _determineDisplayNamesWithEnergyEntries:.classDebugEnabled.1897
+ _determineDisplayNamesWithEnergyEntries:.defaultOnce.1896
+ _energyEntriesWithRange:withEntryTimeInterval:withQueryType:.classDebugEnabled.1527
+ _energyEntriesWithRange:withEntryTimeInterval:withQueryType:.defaultOnce.1526
+ _filterEnergyEntriesBasedOnTime:withQueryType:.classDebugEnabled.1735
+ _filterEnergyEntriesBasedOnTime:withQueryType:.classDebugEnabled.1747
+ _filterEnergyEntriesBasedOnTime:withQueryType:.classDebugEnabled.1755
+ _filterEnergyEntriesBasedOnTime:withQueryType:.defaultOnce.1734
+ _filterEnergyEntriesBasedOnTime:withQueryType:.defaultOnce.1746
+ _filterEnergyEntriesBasedOnTime:withQueryType:.defaultOnce.1754
+ _filterWithEnergyEntries:withQueryType:.classDebugEnabled.1903
+ _filterWithEnergyEntries:withQueryType:.defaultOnce.1902
+ _getBundleIDToDisplayNameMap.classDebugEnabled.191
+ _getBundleIDToDisplayNameMap.defaultOnce.190
+ _getBundleIDToDisplayNameMapWithResponderService:.classDebugEnabled.471
+ _getBundleIDToDisplayNameMapWithResponderService:.defaultOnce.470
+ _getIOPSDevices.classDebugEnabled.3442
+ _getIOPSDevices.classDebugEnabled.3448
+ _getIOPSDevices.defaultOnce.3441
+ _getIOPSDevices.defaultOnce.3447
+ _getPluginBundleIDToEntryMapWithResponderService:.classDebugEnabled.443
+ _getPluginBundleIDToEntryMapWithResponderService:.classDebugEnabled.449
+ _getPluginBundleIDToEntryMapWithResponderService:.defaultOnce.442
+ _getPluginBundleIDToEntryMapWithResponderService:.defaultOnce.448
+ _handlePeer:forEvent:.classDebugEnabled.705
+ _handlePeer:forEvent:.classDebugEnabled.711
+ _handlePeer:forEvent:.classDebugEnabled.717
+ _handlePeer:forEvent:.classDebugEnabled.723
+ _handlePeer:forEvent:.classDebugEnabled.732
+ _handlePeer:forEvent:.classDebugEnabled.742
+ _handlePeer:forEvent:.defaultOnce.704
+ _handlePeer:forEvent:.defaultOnce.710
+ _handlePeer:forEvent:.defaultOnce.716
+ _handlePeer:forEvent:.defaultOnce.722
+ _handlePeer:forEvent:.defaultOnce.731
+ _handlePeer:forEvent:.defaultOnce.741
+ _handlePeerListenerEvent:withMessage:withClientID:withProcessName:withKey:withPayload:withPeer:.classDebugEnabled
+ _handlePeerListenerEvent:withMessage:withClientID:withProcessName:withKey:withPayload:withPeer:.classDebugEnabled.879
+ _handlePeerListenerEvent:withMessage:withClientID:withProcessName:withKey:withPayload:withPeer:.defaultOnce
+ _handlePeerListenerEvent:withMessage:withClientID:withProcessName:withKey:withPayload:withPeer:.defaultOnce.878
+ _handlePeerResponderEvent:withMessage:withClientID:withProcessName:withKey:withPayload:withPeer:.classDebugEnabled
+ _handlePeerResponderEvent:withMessage:withClientID:withProcessName:withKey:withPayload:withPeer:.classDebugEnabled.810
+ _handlePeerResponderEvent:withMessage:withClientID:withProcessName:withKey:withPayload:withPeer:.classDebugEnabled.822
+ _handlePeerResponderEvent:withMessage:withClientID:withProcessName:withKey:withPayload:withPeer:.classDebugEnabled.869
+ _handlePeerResponderEvent:withMessage:withClientID:withProcessName:withKey:withPayload:withPeer:.defaultOnce
+ _handlePeerResponderEvent:withMessage:withClientID:withProcessName:withKey:withPayload:withPeer:.defaultOnce.809
+ _handlePeerResponderEvent:withMessage:withClientID:withProcessName:withKey:withPayload:withPeer:.defaultOnce.821
+ _handlePeerResponderEvent:withMessage:withClientID:withProcessName:withKey:withPayload:withPeer:.defaultOnce.868
+ _handlePeerShouldLogEvent:withMessage:withClientID:withProcessName:withKey:withPeer:.classDebugEnabled
+ _handlePeerShouldLogEvent:withMessage:withClientID:withProcessName:withKey:withPeer:.classDebugEnabled.801
+ _handlePeerShouldLogEvent:withMessage:withClientID:withProcessName:withKey:withPeer:.defaultOnce
+ _handlePeerShouldLogEvent:withMessage:withClientID:withProcessName:withKey:withPeer:.defaultOnce.800
+ _handleSingleMessage:fromPeer:forEvent:.classDebugEnabled.759
+ _handleSingleMessage:fromPeer:forEvent:.classDebugEnabled.762
+ _handleSingleMessage:fromPeer:forEvent:.classDebugEnabled.768
+ _handleSingleMessage:fromPeer:forEvent:.classDebugEnabled.774
+ _handleSingleMessage:fromPeer:forEvent:.classDebugEnabled.780
+ _handleSingleMessage:fromPeer:forEvent:.classDebugEnabled.786
+ _handleSingleMessage:fromPeer:forEvent:.defaultOnce.758
+ _handleSingleMessage:fromPeer:forEvent:.defaultOnce.761
+ _handleSingleMessage:fromPeer:forEvent:.defaultOnce.767
+ _handleSingleMessage:fromPeer:forEvent:.defaultOnce.773
+ _handleSingleMessage:fromPeer:forEvent:.defaultOnce.779
+ _handleSingleMessage:fromPeer:forEvent:.defaultOnce.785
+ _initOperatorDependancies.classDebugEnabled.3694
+ _initOperatorDependancies.classDebugEnabled.3697
+ _initOperatorDependancies.defaultOnce.3693
+ _initOperatorDependancies.defaultOnce.3696
+ _kPLBatteryAgentStringUserType_block_invoke.classDebugEnabled.3304
+ _kPLBatteryAgentStringUserType_block_invoke.classDebugEnabled.3318
+ _kPLBatteryAgentStringUserType_block_invoke.defaultOnce.3264
+ _kPLBatteryAgentStringUserType_block_invoke.defaultOnce.3300
+ _kPLBatteryAgentStringUserType_block_invoke.defaultOnce.3303
+ _kPLBatteryAgentStringUserType_block_invoke.defaultOnce.3317
+ _kPLBatteryAgentStringUserType_block_invoke.objectForKey.3301
+ _kPLBatteryAgentStringUserType_block_invoke_12.classDebugEnabled.5301
+ _kPLBatteryAgentStringUserType_block_invoke_12.defaultOnce.5300
+ _kPLBatteryAgentStringUserType_block_invoke_2.classDebugEnabled.3520
+ _kPLBatteryAgentStringUserType_block_invoke_2.defaultOnce.3519
+ _kPLXPCServiceEventPointNameClientLoggingDrops_block_invoke_6.classDebugEnabled.848
+ _kPLXPCServiceEventPointNameClientLoggingDrops_block_invoke_6.classDebugEnabled.855
+ _kPLXPCServiceEventPointNameClientLoggingDrops_block_invoke_6.defaultOnce.847
+ _kPLXPCServiceEventPointNameClientLoggingDrops_block_invoke_6.defaultOnce.854
+ _logEventBackwardHeatMap.classDebugEnabled.4153
+ _logEventBackwardHeatMap.classDebugEnabled.4160
+ _logEventBackwardHeatMap.defaultOnce.4152
+ _logEventBackwardHeatMap.defaultOnce.4159
+ _logEventIntervalGasGauge.classDebugEnabled.4015
+ _logEventIntervalGasGauge.defaultOnce.4014
+ _logEventNoneBatteryConfigWithRawData:.classDebugEnabled.5019
+ _logEventNoneBatteryConfigWithRawData:.defaultOnce.5018
+ _logMessage:withPayload:.classDebugEnabled.674
+ _logMessage:withPayload:.defaultOnce.671
+ _logMessage:withPayload:.defaultOnce.673
+ _mapDeletedAppsWithEnergyEntries:.classDebugEnabled.1809
+ _mapDeletedAppsWithEnergyEntries:.defaultOnce.1808
+ _mapPluginsToAppsWithEnergyEntries:.classDebugEnabled.1818
+ _mapPluginsToAppsWithEnergyEntries:.defaultOnce.1817
+ _objc_msgSend$didUpgradeInLast:
+ _objc_msgSend$getEnergyForAppWithBundleID:inDateInterval:forRootNodes:
+ _objc_msgSend$handlePeerListenerEvent:withMessage:withClientID:withProcessName:withKey:withPayload:withPeer:
+ _objc_msgSend$handlePeerResponderEvent:withMessage:withClientID:withProcessName:withKey:withPayload:withPeer:
+ _objc_msgSend$handlePeerShouldLogEvent:withMessage:withClientID:withProcessName:withKey:withPeer:
+ _objc_msgSend$localeIdentifier
+ _objc_msgSend$logEventPointBatteryUIAppDetailVisit
+ _objc_msgSend$logEventPointBatteryUIDetailVisit
+ _objc_msgSend$logEventPointBatteryUIInsightsAndSuggestionsWithPayload:
+ _objc_msgSend$logEventPointBatteryUIVisitWithPayload:
+ _objc_msgSend$relayActive
+ _objc_msgSend$setBatteryAppDetailVisitNotification:
+ _objc_msgSend$setBatteryDetailVisitNotification:
+ _objc_msgSend$setBatteryUIInsightsListener:
+ _objc_msgSend$setBatteryUIVisitsListener:
+ _populateRootNodeEnergyKeysWithEnergyEntries:.classDebugEnabled.1602
+ _populateRootNodeEnergyKeysWithEnergyEntries:.defaultOnce.1601
+ _qualifiersWithEnergyEntry:bucketSize:andTotalEnergy:.classDebugEnabled.1938
+ _qualifiersWithEnergyEntry:bucketSize:andTotalEnergy:.classDebugEnabled.1955
+ _qualifiersWithEnergyEntry:bucketSize:andTotalEnergy:.classDebugEnabled.1963
+ _qualifiersWithEnergyEntry:bucketSize:andTotalEnergy:.defaultOnce.1937
+ _qualifiersWithEnergyEntry:bucketSize:andTotalEnergy:.defaultOnce.1954
+ _qualifiersWithEnergyEntry:bucketSize:andTotalEnergy:.defaultOnce.1962
+ _qualifiersWithEnergyEntry:bucketSize:andTotalEnergy:.defaultOnce.1971
+ _qualifiersWithEnergyEntry:bucketSize:andTotalEnergy:.defaultOnce.2012
+ _qualifiersWithEnergyEntry:bucketSize:andTotalEnergy:.defaultOnce.2022
+ _qualifiersWithEnergyEntry:bucketSize:andTotalEnergy:.defaultOnce.2025
+ _qualifiersWithEnergyEntry:bucketSize:andTotalEnergy:.objectForKey.2013
+ _qualifiersWithEnergyEntry:bucketSize:andTotalEnergy:.objectForKey.2023
+ _qualifiersWithEnergyEntry:bucketSize:andTotalEnergy:.objectForKey.2026
+ _reaccountBackupRestore:.classDebugEnabled.609
+ _reaccountBackupRestore:.defaultOnce.608
+ _reaccountBackupRestoreWithEnergyEntries:.classDebugEnabled.1874
+ _reaccountBackupRestoreWithEnergyEntries:.defaultOnce.1873
+ _resetPermissionsForClients.classDebugEnabled.696
+ _resetPermissionsForClients.defaultOnce.695
+ _respondToEvent:withResponse:.classDebugEnabled.650
+ _respondToEvent:withResponse:.classDebugEnabled.656
+ _respondToEvent:withResponse:.defaultOnce.649
+ _respondToEvent:withResponse:.defaultOnce.655
+ _setupEALoggingTriggeredByConnectionEvent:.classDebugEnabled.3425
+ _setupEALoggingTriggeredByConnectionEvent:.defaultOnce.3424
+ _transformPlugins:withBucket:.classDebugEnabled.620
+ _transformPlugins:withBucket:.defaultOnce.619
+ _xFlags.classDebugEnabled.5072
+ _xFlags.classDebugEnabled.5081
+ _xFlags.classDebugEnabled.5096
+ _xFlags.classDebugEnabled.5102
+ _xFlags.classDebugEnabled.5108
+ _xFlags.classDebugEnabled.5117
+ _xFlags.classDebugEnabled.5123
+ _xFlags.classDebugEnabled.5129
+ _xFlags.defaultOnce.5071
+ _xFlags.defaultOnce.5080
+ _xFlags.defaultOnce.5095
+ _xFlags.defaultOnce.5101
+ _xFlags.defaultOnce.5107
+ _xFlags.defaultOnce.5116
+ _xFlags.defaultOnce.5122
+ _xFlags.defaultOnce.5128
- -[PLBatteryAgent batteryUIVisitNotification]
- -[PLBatteryAgent logEventPointBatteryUIVisit]
- -[PLBatteryAgent setBatteryUIVisitNotification:]
- -[PLBatteryBreakdownService shouldShowOngoingRestoreInsight]
- -[PLBatteryBreakdownService shouldShowOngoingRestoreInsight].cold.1
- -[PLXPCService handlePeerListenerEvent:withMessage:withClientID:withProcessName:withKey:withPayload:]
- -[PLXPCService handlePeerListenerEvent:withMessage:withClientID:withProcessName:withKey:withPayload:].cold.1
- -[PLXPCService handlePeerListenerEvent:withMessage:withClientID:withProcessName:withKey:withPayload:].cold.2
- -[PLXPCService handlePeerResponderEvent:withMessage:withClientID:withProcessName:withKey:withPayload:]
- -[PLXPCService handlePeerResponderEvent:withMessage:withClientID:withProcessName:withKey:withPayload:].cold.1
- -[PLXPCService handlePeerResponderEvent:withMessage:withClientID:withProcessName:withKey:withPayload:].cold.2
- -[PLXPCService handlePeerResponderEvent:withMessage:withClientID:withProcessName:withKey:withPayload:].cold.3
- -[PLXPCService handlePeerShouldLogEvent:withMessage:withClientID:withProcessName:withKey:]
- -[PLXPCService handlePeerShouldLogEvent:withMessage:withClientID:withProcessName:withKey:].cold.1
- -[PLXPCService handlePeerShouldLogEvent:withMessage:withClientID:withProcessName:withKey:].cold.2
- -[PLXPCService handlePeerShouldLogEvent:withMessage:withClientID:withProcessName:withKey:].cold.3
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
- _OBJC_IVAR_$_PLBatteryAgent._batteryUIVisitNotification
- ___101-[PLXPCService handlePeerListenerEvent:withMessage:withClientID:withProcessName:withKey:withPayload:]_block_invoke
- ___101-[PLXPCService handlePeerListenerEvent:withMessage:withClientID:withProcessName:withKey:withPayload:]_block_invoke.862
- ___102-[PLXPCService handlePeerResponderEvent:withMessage:withClientID:withProcessName:withKey:withPayload:]_block_invoke
- ___102-[PLXPCService handlePeerResponderEvent:withMessage:withClientID:withProcessName:withKey:withPayload:]_block_invoke.793
- ___102-[PLXPCService handlePeerResponderEvent:withMessage:withClientID:withProcessName:withKey:withPayload:]_block_invoke.805
- ___102-[PLXPCService handlePeerResponderEvent:withMessage:withClientID:withProcessName:withKey:withPayload:]_block_invoke.809
- ___102-[PLXPCService handlePeerResponderEvent:withMessage:withClientID:withProcessName:withKey:withPayload:]_block_invoke.809.cold.1
- ___102-[PLXPCService handlePeerResponderEvent:withMessage:withClientID:withProcessName:withKey:withPayload:]_block_invoke.809.cold.2
- ___102-[PLXPCService handlePeerResponderEvent:withMessage:withClientID:withProcessName:withKey:withPayload:]_block_invoke.831
- ___102-[PLXPCService handlePeerResponderEvent:withMessage:withClientID:withProcessName:withKey:withPayload:]_block_invoke.838
- ___102-[PLXPCService handlePeerResponderEvent:withMessage:withClientID:withProcessName:withKey:withPayload:]_block_invoke.845
- ___102-[PLXPCService handlePeerResponderEvent:withMessage:withClientID:withProcessName:withKey:withPayload:]_block_invoke.845.cold.1
- ___102-[PLXPCService handlePeerResponderEvent:withMessage:withClientID:withProcessName:withKey:withPayload:]_block_invoke.852
- ___102-[PLXPCService handlePeerResponderEvent:withMessage:withClientID:withProcessName:withKey:withPayload:]_block_invoke.856
- ___102-[PLXPCService handlePeerResponderEvent:withMessage:withClientID:withProcessName:withKey:withPayload:]_block_invoke_2
- ___102-[PLXPCService handlePeerResponderEvent:withMessage:withClientID:withProcessName:withKey:withPayload:]_block_invoke_2.846
- ___22-[PLBatteryAgent init]_block_invoke.3251
- ___22-[PLBatteryAgent init]_block_invoke.3251.cold.1
- ___22-[PLBatteryAgent init]_block_invoke.3251.cold.10
- ___22-[PLBatteryAgent init]_block_invoke.3251.cold.11
- ___22-[PLBatteryAgent init]_block_invoke.3251.cold.2
- ___22-[PLBatteryAgent init]_block_invoke.3251.cold.3
- ___22-[PLBatteryAgent init]_block_invoke.3251.cold.4
- ___22-[PLBatteryAgent init]_block_invoke.3251.cold.5
- ___22-[PLBatteryAgent init]_block_invoke.3251.cold.6
- ___22-[PLBatteryAgent init]_block_invoke.3251.cold.7
- ___22-[PLBatteryAgent init]_block_invoke.3251.cold.8
- ___22-[PLBatteryAgent init]_block_invoke.3251.cold.9
- ___22-[PLBatteryAgent init]_block_invoke.3263
- ___22-[PLBatteryAgent init]_block_invoke.3265
- ___22-[PLBatteryAgent init]_block_invoke.3291
- ___22-[PLBatteryAgent init]_block_invoke.3294
- ___22-[PLBatteryAgent init]_block_invoke.3302.cold.1
- ___22-[PLBatteryAgent init]_block_invoke.3302.cold.2
- ___22-[PLBatteryAgent init]_block_invoke.3308
- ___22-[PLBatteryAgent init]_block_invoke.3312
- ___22-[PLBatteryAgent init]_block_invoke_2.3334
- ___24-[PLBatteryAgent xFlags]_block_invoke.5025
- ___24-[PLBatteryAgent xFlags]_block_invoke.5034
- ___24-[PLBatteryAgent xFlags]_block_invoke.5043
- ___24-[PLBatteryAgent xFlags]_block_invoke.5052
- ___24-[PLBatteryAgent xFlags]_block_invoke.5058
- ___24-[PLBatteryAgent xFlags]_block_invoke.5070
- ___24-[PLBatteryAgent xFlags]_block_invoke.5079
- ___24-[PLBatteryAgent xFlags]_block_invoke.5085
- ___32-[PLBatteryAgent aggdTimerFired]_block_invoke.4712
- ___32-[PLBatteryAgent getIOPSDevices]_block_invoke.3432
- ___32-[PLBatteryAgent getIOPSDevices]_block_invoke.3438
- ___33-[PLBatteryAgent cancelEALogging]_block_invoke.3423
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
- ___42-[PLBatteryAgent initOperatorDependancies]_block_invoke.3510
- ___42-[PLBatteryAgent initOperatorDependancies]_block_invoke.3516
- ___42-[PLBatteryAgent initOperatorDependancies]_block_invoke.3516.cold.1
- ___42-[PLBatteryAgent initOperatorDependancies]_block_invoke.3532
- ___42-[PLBatteryAgent initOperatorDependancies]_block_invoke.3565
- ___42-[PLBatteryAgent initOperatorDependancies]_block_invoke.3625
- ___42-[PLBatteryAgent initOperatorDependancies]_block_invoke.3625.cold.1
- ___42-[PLBatteryAgent initOperatorDependancies]_block_invoke.3625.cold.2
- ___42-[PLBatteryAgent initOperatorDependancies]_block_invoke.3625.cold.3
- ___42-[PLBatteryAgent initOperatorDependancies]_block_invoke.3642
- ___42-[PLBatteryAgent initOperatorDependancies]_block_invoke.3642.cold.1
- ___42-[PLBatteryAgent initOperatorDependancies]_block_invoke.3657
- ___42-[PLBatteryAgent initOperatorDependancies]_block_invoke.3657.cold.1
- ___42-[PLBatteryAgent initOperatorDependancies]_block_invoke.3665
- ___42-[PLBatteryAgent initOperatorDependancies]_block_invoke.3665.cold.1
- ___42-[PLBatteryAgent initOperatorDependancies]_block_invoke.3672
- ___42-[PLBatteryAgent initOperatorDependancies]_block_invoke.3681
- ___42-[PLBatteryAgent initOperatorDependancies]_block_invoke.3687
- ___42-[PLBatteryAgent initOperatorDependancies]_block_invoke.3694
- ___42-[PLBatteryAgent initOperatorDependancies]_block_invoke.3694.cold.1
- ___42-[PLBatteryAgent initOperatorDependancies]_block_invoke.3701
- ___42-[PLBatteryAgent initOperatorDependancies]_block_invoke.3701.cold.1
- ___42-[PLBatteryAgent initOperatorDependancies]_block_invoke.3715
- ___42-[PLBatteryAgent initOperatorDependancies]_block_invoke.3715.cold.1
- ___42-[PLBatteryAgent initOperatorDependancies]_block_invoke.3720
- ___42-[PLBatteryAgent initOperatorDependancies]_block_invoke.3720.cold.1
- ___42-[PLBatteryAgent initOperatorDependancies]_block_invoke.3727
- ___42-[PLBatteryAgent initOperatorDependancies]_block_invoke.3750
- ___42-[PLBatteryAgent initOperatorDependancies]_block_invoke_2.3517
- ___42-[PLBatteryAgent initOperatorDependancies]_block_invoke_2.3562
- ___42-[PLBatteryAgent initOperatorDependancies]_block_invoke_2.3577
- ___42-[PLBatteryAgent initOperatorDependancies]_block_invoke_2.3649
- ___42-[PLBatteryAgent initOperatorDependancies]_block_invoke_2.3666
- ___42-[PLBatteryAgent initOperatorDependancies]_block_invoke_2.3676
- ___42-[PLBatteryAgent initOperatorDependancies]_block_invoke_2.3684
- ___42-[PLBatteryAgent initOperatorDependancies]_block_invoke_2.3702
- ___42-[PLBatteryAgent initOperatorDependancies]_block_invoke_2.3758
- ___42-[PLBatteryAgent initOperatorDependancies]_block_invoke_3.3762
- ___42-[PLBatteryAgent initOperatorDependancies]_block_invoke_4.3766
- ___42-[PLBatteryAgent initOperatorDependancies]_block_invoke_5.3770
- ___42-[PLBatteryAgent initOperatorDependancies]_block_invoke_6.3772
- ___42-[PLBatteryAgent initSmartChargingLogging]_block_invoke.5255
- ___42-[PLBatteryAgent initSmartChargingLogging]_block_invoke.5255.cold.1
- ___42-[PLBatteryAgent initSmartChargingLogging]_block_invoke.5255.cold.2
- ___42-[PLBatteryAgent initSmartChargingLogging]_block_invoke.5263
- ___42-[PLBatteryAgent initSmartChargingLogging]_block_invoke_2.5257
- ___42-[PLBatteryAgent logEventIntervalGasGauge]_block_invoke.3977
- ___42-[PLXPCService resetPermissionsForClients]_block_invoke.670
- ___42-[PLXPCService resetPermissionsForClients]_block_invoke.680
- ___44-[PLXPCService respondToEvent:withResponse:]_block_invoke.634
- ___44-[PLXPCService respondToEvent:withResponse:]_block_invoke.640
- ___45-[PLBatteryAgent logCPMSSnapshotWithTrigger:]_block_invoke.5291
- ___45-[PLBatteryAgent logCPMSSnapshotWithTrigger:]_block_invoke.5292
- ___45-[PLBatteryAgent logCPMSSnapshotWithTrigger:]_block_invoke.5293
- ___45-[PLBatteryAgent logCPMSSnapshotWithTrigger:]_block_invoke.5294
- ___45-[PLBatteryAgent logCPMSSnapshotWithTrigger:]_block_invoke.5295
- ___45-[PLBatteryAgent logCPMSSnapshotWithTrigger:]_block_invoke.5295.cold.1
- ___45-[PLBatteryAgent logCPMSSnapshotWithTrigger:]_block_invoke.5296
- ___45-[PLBatteryAgent logCPMSSnapshotWithTrigger:]_block_invoke.5296.cold.1
- ___45-[PLBatteryAgent logCPMSSnapshotWithTrigger:]_block_invoke.5297
- ___45-[PLBatteryAgent logCPMSSnapshotWithTrigger:]_block_invoke.5297.cold.1
- ___45-[PLBatteryAgent logCPMSSnapshotWithTrigger:]_block_invoke.5338
- ___46-[PLApplicationAgent initOperatorDependancies]_block_invoke.418
- ___46-[PLApplicationAgent initOperatorDependancies]_block_invoke.447
- ___46-[PLApplicationAgent initOperatorDependancies]_block_invoke.447.cold.1
- ___46-[PLApplicationAgent initOperatorDependancies]_block_invoke.453
- ___46-[PLApplicationAgent initOperatorDependancies]_block_invoke.453.cold.1
- ___46-[PLApplicationAgent initOperatorDependancies]_block_invoke.458
- ___46-[PLApplicationAgent initOperatorDependancies]_block_invoke.458.cold.1
- ___46-[PLApplicationAgent initOperatorDependancies]_block_invoke.465
- ___46-[PLApplicationAgent initOperatorDependancies]_block_invoke.465.cold.1
- ___46-[PLApplicationAgent initOperatorDependancies]_block_invoke.475
- ___46-[PLApplicationAgent initOperatorDependancies]_block_invoke.475.cold.1
- ___46-[PLApplicationAgent initOperatorDependancies]_block_invoke.482
- ___46-[PLApplicationAgent initOperatorDependancies]_block_invoke.482.cold.1
- ___46-[PLApplicationAgent initOperatorDependancies]_block_invoke.489
- ___46-[PLApplicationAgent initOperatorDependancies]_block_invoke.489.cold.1
- ___46-[PLApplicationAgent initOperatorDependancies]_block_invoke.494
- ___46-[PLApplicationAgent initOperatorDependancies]_block_invoke.494.cold.1
- ___46-[PLApplicationAgent initOperatorDependancies]_block_invoke.499
- ___46-[PLApplicationAgent initOperatorDependancies]_block_invoke.499.cold.1
- ___46-[PLApplicationAgent initOperatorDependancies]_block_invoke.507
- ___46-[PLApplicationAgent initOperatorDependancies]_block_invoke.507.cold.1
- ___46-[PLApplicationAgent initOperatorDependancies]_block_invoke.515
- ___46-[PLApplicationAgent initOperatorDependancies]_block_invoke.515.cold.1
- ___46-[PLApplicationAgent initOperatorDependancies]_block_invoke.520
- ___46-[PLApplicationAgent initOperatorDependancies]_block_invoke.520.cold.1
- ___46-[PLApplicationAgent initOperatorDependancies]_block_invoke.525.cold.1
- ___46-[PLApplicationAgent initOperatorDependancies]_block_invoke.526
- ___46-[PLApplicationAgent initOperatorDependancies]_block_invoke.540
- ___46-[PLApplicationAgent initOperatorDependancies]_block_invoke.540.cold.1
- ___46-[PLApplicationAgent initOperatorDependancies]_block_invoke.548
- ___46-[PLApplicationAgent initOperatorDependancies]_block_invoke.548.cold.1
- ___46-[PLApplicationAgent initOperatorDependancies]_block_invoke_2.421
- ___46-[PLApplicationAgent initOperatorDependancies]_block_invoke_2.527
- ___46-[PLApplicationAgent initOperatorDependancies]_block_invoke_2.527.cold.1
- ___46-[PLApplicationAgent initOperatorDependancies]_block_invoke_2.527.cold.2
- ___50-[PLBatteryAgent initializeChargingStateIntervals]_block_invoke.5280
- ___50-[PLBatteryAgent initializeChargingStateIntervals]_block_invoke.5281
- ___50-[PLBatteryAgent initializeChargingStateIntervals]_block_invoke.5285
- ___50-[PLBatteryAgent initializeChargingStateIntervals]_block_invoke.5285.cold.1
- ___50-[PLBatteryAgent initializeChargingStateIntervals]_block_invoke.5285.cold.2
- ___54-[PLXPCService handleSingleMessage:fromPeer:forEvent:]_block_invoke.743
- ___54-[PLXPCService handleSingleMessage:fromPeer:forEvent:]_block_invoke.746
- ___54-[PLXPCService handleSingleMessage:fromPeer:forEvent:]_block_invoke.752
- ___54-[PLXPCService handleSingleMessage:fromPeer:forEvent:]_block_invoke.758
- ___54-[PLXPCService handleSingleMessage:fromPeer:forEvent:]_block_invoke.764
- ___54-[PLXPCService handleSingleMessage:fromPeer:forEvent:]_block_invoke.770
- ___55-[PLBatteryAgent logEventNoneBatteryConfigWithRawData:]_block_invoke.4968
- ___55-[PLBatteryAgent logEventNoneBatteryConfigWithRawData:]_block_invoke.4968.cold.1
- ___55-[PLBatteryAgent logEventNoneBatteryConfigWithRawData:]_block_invoke.4972
- ___55-[PLBatteryAgent logEventNoneBatteryConfigWithRawData:]_block_invoke.4972.cold.1
- ___55-[PLBatteryAgent logEventNoneBatteryConfigWithRawData:]_block_invoke.4977
- ___55-[PLBatteryAgent logEventNoneBatteryConfigWithRawData:]_block_invoke.4981
- ___55-[PLBatteryAgent logEventNoneBatteryConfigWithRawData:]_block_invoke_2.4973
- ___55-[PLBatteryAgent logEventNoneBatteryConfigWithRawData:]_block_invoke_2.4978
- ___56-[PLApplicationAgent createWidgetStatsAccountingEvents:]_block_invoke.578
- ___59-[PLBatteryAgent setupEALoggingTriggeredByConnectionEvent:]_block_invoke.3403
- ___60-[PLBatteryBreakdownService shouldShowOngoingRestoreInsight]_block_invoke
- ___61-[PLBatteryBreakdownService mapDeletedAppsWithEnergyEntries:]_block_invoke.1816
- ___61-[PLBatteryUIResponderService convertResponseToLegacyFormat:]_block_invoke.222
- ___61-[PLBatteryUIResponderService convertResponseToLegacyFormat:]_block_invoke.266
- ___63-[PLBatteryBreakdownService mapPluginsToAppsWithEnergyEntries:]_block_invoke.1825
- ___64-[PLBatteryBreakdownService combineDuplicatesWithEnergyEntries:]_block_invoke.1889
- ___64-[PLBatteryBreakdownService combineDuplicatesWithEnergyEntries:]_block_invoke.1893
- ___65-[PLBatteryAgent logEventBackwardHeatMapCallback:andHeatMapType:]_block_invoke.4375
- ___65-[PLBatteryUIResponseTypeBatteryBreakdown collapseEnergyEntries:]_block_invoke.576
- ___66-[PLBatteryUIResponseTypeBatteryBreakdown reaccountBackupRestore:]_block_invoke.608
- ___67-[PLBatteryBreakdownService filterWithEnergyEntries:withQueryType:]_block_invoke.1922
- ___68-[PLBatteryBreakdownService determineDisplayNamesWithEnergyEntries:]_block_invoke.1904
- ___69-[PLBatteryBreakdownService reaccountBackupRestoreWithEnergyEntries:]_block_invoke.1878
- ___71-[PLBatteryUIResponseTypeBatteryBreakdown transformPlugins:withBucket:]_block_invoke.622
- ___73-[PLBatteryBreakdownService populateRootNodeEnergyKeysWithEnergyEntries:]_block_invoke.1615
- ___74-[PLBatteryBreakdownService filterEnergyEntriesBasedOnTime:withQueryType:]_block_invoke.1742
- ___74-[PLBatteryBreakdownService filterEnergyEntriesBasedOnTime:withQueryType:]_block_invoke.1754
- ___74-[PLBatteryBreakdownService filterEnergyEntriesBasedOnTime:withQueryType:]_block_invoke.1768
- ___75-[PLBatteryAgent showOrHideTLCNotification:meetsTLCNotificationConditions:]_block_invoke.3375
- ___75-[PLBatteryBreakdownService addNotificationValues:withRange:withQueryType:]_block_invoke.1732
- ___76-[PLBatteryUIResponseTypeDrainComparisonSummary getBundleIDToDisplayNameMap]_block_invoke.174
- ___77-[PLBatteryBreakdownService applyStaticNameTransformationsWithEnergyEntries:]_block_invoke.1789
- ___77-[PLBatteryBreakdownService applyStaticNameTransformationsWithEnergyEntries:]_block_invoke.1797
- ___81-[PLApplicationAgent logInstalledAppWithRecord:withBundleID:shouldMaskTimestamp:]_block_invoke.618
- ___81-[PLBatteryBreakdownService qualifiersWithEnergyEntry:bucketSize:andTotalEnergy:]_block_invoke.1945
- ___81-[PLBatteryBreakdownService qualifiersWithEnergyEntry:bucketSize:andTotalEnergy:]_block_invoke.1962
- ___81-[PLBatteryBreakdownService qualifiersWithEnergyEntry:bucketSize:andTotalEnergy:]_block_invoke.1970
- ___81-[PLBatteryBreakdownService qualifiersWithEnergyEntry:bucketSize:andTotalEnergy:]_block_invoke.1978
- ___81-[PLBatteryBreakdownService qualifiersWithEnergyEntry:bucketSize:andTotalEnergy:]_block_invoke.2020
- ___81-[PLBatteryBreakdownService qualifiersWithEnergyEntry:bucketSize:andTotalEnergy:]_block_invoke.2030
- ___84+[PLBatteryUIResponseTypeUtilities getBundleIDToDisplayNameMapWithResponderService:]_block_invoke.469
- ___84+[PLBatteryUIResponseTypeUtilities getPluginBundleIDToEntryMapWithResponderService:]_block_invoke.441
- ___84+[PLBatteryUIResponseTypeUtilities getPluginBundleIDToEntryMapWithResponderService:]_block_invoke.447
- ___88-[PLBatteryBreakdownService energyEntriesWithRange:withEntryTimeInterval:withQueryType:]_block_invoke.1558
- ___90-[PLXPCService handlePeerShouldLogEvent:withMessage:withClientID:withProcessName:withKey:]_block_invoke
- ___90-[PLXPCService handlePeerShouldLogEvent:withMessage:withClientID:withProcessName:withKey:]_block_invoke.784
- ___block_literal_global.2100
- ___block_literal_global.238
- ___block_literal_global.3238
- ___block_literal_global.3349
- ___block_literal_global.3362
- ___block_literal_global.3377
- ___block_literal_global.3478
- ___block_literal_global.348
- ___block_literal_global.3535
- ___block_literal_global.3579
- ___block_literal_global.3588
- ___block_literal_global.3597
- ___block_literal_global.3609
- ___block_literal_global.3722
- ___block_literal_global.3774
- ___block_literal_global.3780
- ___block_literal_global.3790
- ___block_literal_global.4424
- ___block_literal_global.4668
- ___block_literal_global.4680
- ___block_literal_global.4730
- ___block_literal_global.520
- ___block_literal_global.5229
- ___block_literal_global.5290
- ___block_literal_global.534
- ___block_literal_global.547
- _applyStaticNameTransformationsWithEnergyEntries:.classDebugEnabled.1788
- _applyStaticNameTransformationsWithEnergyEntries:.classDebugEnabled.1796
- _applyStaticNameTransformationsWithEnergyEntries:.defaultOnce.1787
- _applyStaticNameTransformationsWithEnergyEntries:.defaultOnce.1795
- _cancelEALogging.classDebugEnabled.3422
- _cancelEALogging.defaultOnce.3421
- _combineDuplicatesWithEnergyEntries:.classDebugEnabled.1888
- _combineDuplicatesWithEnergyEntries:.classDebugEnabled.1895
- _combineDuplicatesWithEnergyEntries:.defaultOnce.1887
- _combineDuplicatesWithEnergyEntries:.defaultOnce.1894
- _dailyTasks.defaultOnce.613
- _determineDisplayNamesWithEnergyEntries:.classDebugEnabled.1903
- _determineDisplayNamesWithEnergyEntries:.defaultOnce.1902
- _energyEntriesWithRange:withEntryTimeInterval:withQueryType:.classDebugEnabled.1557
- _energyEntriesWithRange:withEntryTimeInterval:withQueryType:.defaultOnce.1556
- _filterEnergyEntriesBasedOnTime:withQueryType:.classDebugEnabled.1741
- _filterEnergyEntriesBasedOnTime:withQueryType:.classDebugEnabled.1753
- _filterEnergyEntriesBasedOnTime:withQueryType:.classDebugEnabled.1767
- _filterEnergyEntriesBasedOnTime:withQueryType:.defaultOnce.1740
- _filterEnergyEntriesBasedOnTime:withQueryType:.defaultOnce.1752
- _filterEnergyEntriesBasedOnTime:withQueryType:.defaultOnce.1766
- _filterWithEnergyEntries:withQueryType:.classDebugEnabled.1921
- _filterWithEnergyEntries:withQueryType:.defaultOnce.1920
- _getBundleIDToDisplayNameMap.classDebugEnabled.173
- _getBundleIDToDisplayNameMap.defaultOnce.172
- _getBundleIDToDisplayNameMapWithResponderService:.classDebugEnabled.468
- _getBundleIDToDisplayNameMapWithResponderService:.defaultOnce.467
- _getIOPSDevices.classDebugEnabled.3431
- _getIOPSDevices.classDebugEnabled.3437
- _getIOPSDevices.defaultOnce.3430
- _getIOPSDevices.defaultOnce.3436
- _getPluginBundleIDToEntryMapWithResponderService:.classDebugEnabled.440
- _getPluginBundleIDToEntryMapWithResponderService:.classDebugEnabled.446
- _getPluginBundleIDToEntryMapWithResponderService:.defaultOnce.439
- _getPluginBundleIDToEntryMapWithResponderService:.defaultOnce.445
- _handlePeer:forEvent:.classDebugEnabled.688
- _handlePeer:forEvent:.classDebugEnabled.694
- _handlePeer:forEvent:.classDebugEnabled.700
- _handlePeer:forEvent:.classDebugEnabled.706
- _handlePeer:forEvent:.classDebugEnabled.715
- _handlePeer:forEvent:.classDebugEnabled.725
- _handlePeer:forEvent:.defaultOnce.687
- _handlePeer:forEvent:.defaultOnce.693
- _handlePeer:forEvent:.defaultOnce.699
- _handlePeer:forEvent:.defaultOnce.705
- _handlePeer:forEvent:.defaultOnce.714
- _handlePeer:forEvent:.defaultOnce.724
- _handlePeerListenerEvent:withMessage:withClientID:withProcessName:withKey:withPayload:.classDebugEnabled
- _handlePeerListenerEvent:withMessage:withClientID:withProcessName:withKey:withPayload:.classDebugEnabled.861
- _handlePeerListenerEvent:withMessage:withClientID:withProcessName:withKey:withPayload:.defaultOnce
- _handlePeerListenerEvent:withMessage:withClientID:withProcessName:withKey:withPayload:.defaultOnce.860
- _handlePeerResponderEvent:withMessage:withClientID:withProcessName:withKey:withPayload:.classDebugEnabled
- _handlePeerResponderEvent:withMessage:withClientID:withProcessName:withKey:withPayload:.classDebugEnabled.792
- _handlePeerResponderEvent:withMessage:withClientID:withProcessName:withKey:withPayload:.classDebugEnabled.804
- _handlePeerResponderEvent:withMessage:withClientID:withProcessName:withKey:withPayload:.classDebugEnabled.851
- _handlePeerResponderEvent:withMessage:withClientID:withProcessName:withKey:withPayload:.defaultOnce
- _handlePeerResponderEvent:withMessage:withClientID:withProcessName:withKey:withPayload:.defaultOnce.791
- _handlePeerResponderEvent:withMessage:withClientID:withProcessName:withKey:withPayload:.defaultOnce.803
- _handlePeerResponderEvent:withMessage:withClientID:withProcessName:withKey:withPayload:.defaultOnce.850
- _handlePeerShouldLogEvent:withMessage:withClientID:withProcessName:withKey:.classDebugEnabled
- _handlePeerShouldLogEvent:withMessage:withClientID:withProcessName:withKey:.classDebugEnabled.783
- _handlePeerShouldLogEvent:withMessage:withClientID:withProcessName:withKey:.defaultOnce
- _handlePeerShouldLogEvent:withMessage:withClientID:withProcessName:withKey:.defaultOnce.782
- _handleSingleMessage:fromPeer:forEvent:.classDebugEnabled.742
- _handleSingleMessage:fromPeer:forEvent:.classDebugEnabled.745
- _handleSingleMessage:fromPeer:forEvent:.classDebugEnabled.751
- _handleSingleMessage:fromPeer:forEvent:.classDebugEnabled.757
- _handleSingleMessage:fromPeer:forEvent:.classDebugEnabled.763
- _handleSingleMessage:fromPeer:forEvent:.classDebugEnabled.769
- _handleSingleMessage:fromPeer:forEvent:.defaultOnce.741
- _handleSingleMessage:fromPeer:forEvent:.defaultOnce.744
- _handleSingleMessage:fromPeer:forEvent:.defaultOnce.750
- _handleSingleMessage:fromPeer:forEvent:.defaultOnce.756
- _handleSingleMessage:fromPeer:forEvent:.defaultOnce.762
- _handleSingleMessage:fromPeer:forEvent:.defaultOnce.768
- _initOperatorDependancies.classDebugEnabled.3675
- _initOperatorDependancies.classDebugEnabled.3683
- _initOperatorDependancies.defaultOnce.3674
- _initOperatorDependancies.defaultOnce.3682
- _kPLBatteryAgentStringUserType_block_invoke.classDebugEnabled.3293
- _kPLBatteryAgentStringUserType_block_invoke.classDebugEnabled.3307
- _kPLBatteryAgentStringUserType_block_invoke.defaultOnce.3253
- _kPLBatteryAgentStringUserType_block_invoke.defaultOnce.3289
- _kPLBatteryAgentStringUserType_block_invoke.defaultOnce.3292
- _kPLBatteryAgentStringUserType_block_invoke.defaultOnce.3306
- _kPLBatteryAgentStringUserType_block_invoke.objectForKey.3290
- _kPLBatteryAgentStringUserType_block_invoke_12.classDebugEnabled.5262
- _kPLBatteryAgentStringUserType_block_invoke_12.defaultOnce.5261
- _kPLBatteryAgentStringUserType_block_invoke_2.classDebugEnabled.3509
- _kPLBatteryAgentStringUserType_block_invoke_2.defaultOnce.3508
- _kPLXPCServiceEventPointNameClientLoggingDrops_block_invoke_6.classDebugEnabled.830
- _kPLXPCServiceEventPointNameClientLoggingDrops_block_invoke_6.classDebugEnabled.837
- _kPLXPCServiceEventPointNameClientLoggingDrops_block_invoke_6.defaultOnce.829
- _kPLXPCServiceEventPointNameClientLoggingDrops_block_invoke_6.defaultOnce.836
- _logEventBackwardHeatMap.classDebugEnabled.4114
- _logEventBackwardHeatMap.classDebugEnabled.4121
- _logEventBackwardHeatMap.defaultOnce.4113
- _logEventBackwardHeatMap.defaultOnce.4120
- _logEventIntervalGasGauge.classDebugEnabled.3976
- _logEventIntervalGasGauge.defaultOnce.3975
- _logEventNoneBatteryConfigWithRawData:.classDebugEnabled.4980
- _logEventNoneBatteryConfigWithRawData:.defaultOnce.4979
- _logMessage:withPayload:.classDebugEnabled.657
- _logMessage:withPayload:.defaultOnce.654
- _logMessage:withPayload:.defaultOnce.656
- _mapDeletedAppsWithEnergyEntries:.classDebugEnabled.1815
- _mapDeletedAppsWithEnergyEntries:.defaultOnce.1814
- _mapPluginsToAppsWithEnergyEntries:.classDebugEnabled.1824
- _mapPluginsToAppsWithEnergyEntries:.defaultOnce.1823
- _objc_msgSend$handlePeerListenerEvent:withMessage:withClientID:withProcessName:withKey:withPayload:
- _objc_msgSend$handlePeerResponderEvent:withMessage:withClientID:withProcessName:withKey:withPayload:
- _objc_msgSend$handlePeerShouldLogEvent:withMessage:withClientID:withProcessName:withKey:
- _objc_msgSend$logEventPointBatteryUIVisit
- _objc_msgSend$setBatteryUIVisitNotification:
- _populateRootNodeEnergyKeysWithEnergyEntries:.classDebugEnabled.1614
- _populateRootNodeEnergyKeysWithEnergyEntries:.defaultOnce.1613
- _qualifiersWithEnergyEntry:bucketSize:andTotalEnergy:.classDebugEnabled.1944
- _qualifiersWithEnergyEntry:bucketSize:andTotalEnergy:.classDebugEnabled.1961
- _qualifiersWithEnergyEntry:bucketSize:andTotalEnergy:.classDebugEnabled.1969
- _qualifiersWithEnergyEntry:bucketSize:andTotalEnergy:.defaultOnce.1943
- _qualifiersWithEnergyEntry:bucketSize:andTotalEnergy:.defaultOnce.1960
- _qualifiersWithEnergyEntry:bucketSize:andTotalEnergy:.defaultOnce.1968
- _qualifiersWithEnergyEntry:bucketSize:andTotalEnergy:.defaultOnce.1977
- _qualifiersWithEnergyEntry:bucketSize:andTotalEnergy:.defaultOnce.2018
- _qualifiersWithEnergyEntry:bucketSize:andTotalEnergy:.defaultOnce.2028
- _qualifiersWithEnergyEntry:bucketSize:andTotalEnergy:.defaultOnce.2031
- _qualifiersWithEnergyEntry:bucketSize:andTotalEnergy:.objectForKey.2019
- _qualifiersWithEnergyEntry:bucketSize:andTotalEnergy:.objectForKey.2029
- _qualifiersWithEnergyEntry:bucketSize:andTotalEnergy:.objectForKey.2032
- _reaccountBackupRestore:.classDebugEnabled.610
- _reaccountBackupRestore:.defaultOnce.609
- _reaccountBackupRestoreWithEnergyEntries:.classDebugEnabled.1880
- _reaccountBackupRestoreWithEnergyEntries:.defaultOnce.1879
- _resetPermissionsForClients.classDebugEnabled.679
- _resetPermissionsForClients.defaultOnce.678
- _respondToEvent:withResponse:.classDebugEnabled.633
- _respondToEvent:withResponse:.classDebugEnabled.639
- _respondToEvent:withResponse:.defaultOnce.632
- _respondToEvent:withResponse:.defaultOnce.638
- _setupEALoggingTriggeredByConnectionEvent:.classDebugEnabled.3414
- _setupEALoggingTriggeredByConnectionEvent:.defaultOnce.3413
- _shouldShowOngoingRestoreInsight.classDebugEnabled
- _shouldShowOngoingRestoreInsight.defaultOnce
- _transformPlugins:withBucket:.classDebugEnabled.621
- _transformPlugins:withBucket:.defaultOnce.620
- _xFlags.classDebugEnabled.5024
- _xFlags.classDebugEnabled.5033
- _xFlags.classDebugEnabled.5042
- _xFlags.classDebugEnabled.5051
- _xFlags.classDebugEnabled.5057
- _xFlags.classDebugEnabled.5069
- _xFlags.classDebugEnabled.5078
- _xFlags.classDebugEnabled.5084
- _xFlags.defaultOnce.5023
- _xFlags.defaultOnce.5032
- _xFlags.defaultOnce.5041
- _xFlags.defaultOnce.5050
- _xFlags.defaultOnce.5056
- _xFlags.defaultOnce.5068
- _xFlags.defaultOnce.5077
- _xFlags.defaultOnce.5083
CStrings:
+ "-[PLXPCService handlePeerListenerEvent:withMessage:withClientID:withProcessName:withKey:withPayload:withPeer:]"
+ "-[PLXPCService handlePeerResponderEvent:withMessage:withClientID:withProcessName:withKey:withPayload:withPeer:]"
+ "-[PLXPCService handlePeerResponderEvent:withMessage:withClientID:withProcessName:withKey:withPayload:withPeer:]_block_invoke"
+ "-[PLXPCService handlePeerResponderEvent:withMessage:withClientID:withProcessName:withKey:withPayload:withPeer:]_block_invoke_2"
+ "-[PLXPCService handlePeerShouldLogEvent:withMessage:withClientID:withProcessName:withKey:withPeer:]"
+ "AlwaysOnDisplay"
+ "AppDetailVisit"
+ "B24@0:8d16"
+ "BUI_DEVICESETUP_SUGGESTION_SHOW"
+ "DailyUsageSummary"
+ "DetailVisit"
+ "Insights"
+ "InsightsAndSuggestions"
+ "Locale"
+ "PLBatteryUIResponseTypeOngoingDeviceSetupInsight"
+ "Qualifiers"
+ "Relay: locale requested"
+ "SELECT %@,SUM(%@/1000.0) AS %@ FROM %@ RNE JOIN %@ N ON RNE.NodeID = N.ID WHERE %@ LIKE \"%@\" AND RNE.timestamp >= %f AND RNE.timestamp <= %f %@ IN (%@) AND timeInterval = 3600.0 GROUP BY %@"
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
+ "com.apple.batteryui.deviceSetupInsightDuration"
+ "com.apple.batteryui.insights.deviceSetup"
+ "com.apple.powerlog.AppDetailViewVisit"
+ "com.apple.powerlog.ShowAllUsageViewVisit"
+ "com.apple.powerlog.locale"
+ "deviceSetup"
+ "didUpgradeInLast:"
+ "getEnergyForAppWithBundleID:inDateInterval:forRootNodes:"
+ "handlePeerListenerEvent:withMessage:withClientID:withProcessName:withKey:withPayload:withPeer:"
+ "handlePeerResponderEvent:withMessage:withClientID:withProcessName:withKey:withPayload:withPeer:"
+ "handlePeerShouldLogEvent:withMessage:withClientID:withProcessName:withKey:withPeer:"
+ "invalid violation time, using current time instead"
+ "localeIdentifier"
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
+ "totalAppEnergyToday"
+ "totalAudioEnergy"
+ "v68@0:8@16@24s32@36@44@52@60"
- "-[PLBatteryBreakdownService shouldShowOngoingRestoreInsight]"
- "-[PLXPCService handlePeerListenerEvent:withMessage:withClientID:withProcessName:withKey:withPayload:]"
- "-[PLXPCService handlePeerResponderEvent:withMessage:withClientID:withProcessName:withKey:withPayload:]"
- "-[PLXPCService handlePeerResponderEvent:withMessage:withClientID:withProcessName:withKey:withPayload:]_block_invoke"
- "-[PLXPCService handlePeerResponderEvent:withMessage:withClientID:withProcessName:withKey:withPayload:]_block_invoke_2"
- "-[PLXPCService handlePeerShouldLogEvent:withMessage:withClientID:withProcessName:withKey:]"
- "Auto-Brightness is currently turned off. You can save battery by turning it on."
- "Auto-Lock is currently turned off. You can save battery by turning it on."
- "Enable Auto-Brightness"
- "Enable Auto-Lock"
- "High display brightness consumes large amounts of energy. Consider reducing brightness to improve battery life."
- "Recent Usage"
- "Reduce Brightness"
- "T@\"PLCFNotificationOperatorComposition\",&,V_batteryUIVisitNotification"
- "Text"
- "Your %@ has been used more than usual since upgrading iOS, which may affect battery life."
- "_batteryUIVisitNotification"
- "batteryUIVisitNotification"
- "bui_device_setup"
- "com.apple.powerlogd.logBatteryUIVisit"
- "handlePeerListenerEvent:withMessage:withClientID:withProcessName:withKey:withPayload:"
- "handlePeerResponderEvent:withMessage:withClientID:withProcessName:withKey:withPayload:"
- "handlePeerShouldLogEvent:withMessage:withClientID:withProcessName:withKey:"
- "iPad"
- "iPhone"
- "logEventPointBatteryUIVisit"
- "setBatteryUIVisitNotification:"
- "shouldShowOngoingRestoreInsight"
- "shouldShowOngoingRestoreInsight = %@"
- "v52@0:8@16@24s32@36@44"

```
