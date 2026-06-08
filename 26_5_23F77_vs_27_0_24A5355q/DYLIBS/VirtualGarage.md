## VirtualGarage

> `/System/Library/PrivateFrameworks/VirtualGarage.framework/VirtualGarage`

```diff

-2391.35.2.9.4
-  __TEXT.__text: 0x31260
-  __TEXT.__auth_stubs: 0x6b0
-  __TEXT.__objc_methlist: 0x1f14
-  __TEXT.__const: 0x1a0
-  __TEXT.__gcc_except_tab: 0x124c
-  __TEXT.__cstring: 0x3b14
-  __TEXT.__oslogstring: 0x4c25
-  __TEXT.__unwind_info: 0xae8
-  __TEXT.__objc_classname: 0x3ea
-  __TEXT.__objc_methname: 0x4c80
-  __TEXT.__objc_methtype: 0xc1c
-  __TEXT.__objc_stubs: 0x3ce0
-  __DATA_CONST.__got: 0x370
-  __DATA_CONST.__const: 0x1170
-  __DATA_CONST.__objc_classlist: 0xa8
+2429.30.5.14.3
+  __TEXT.__text: 0x3a60c
+  __TEXT.__objc_methlist: 0x1f7c
+  __TEXT.__const: 0x2c0
+  __TEXT.__swift5_typeref: 0xc2
+  __TEXT.__cstring: 0x3cac
+  __TEXT.__swift5_reflstr: 0x1d
+  __TEXT.__swift5_assocty: 0x18
+  __TEXT.__constg_swiftt: 0x68
+  __TEXT.__swift5_fieldmd: 0x2c
+  __TEXT.__swift5_protos: 0x4
+  __TEXT.__swift5_proto: 0x4
+  __TEXT.__swift5_types: 0x4
+  __TEXT.__gcc_except_tab: 0xee0
+  __TEXT.__oslogstring: 0x4f21
+  __TEXT.__unwind_info: 0xbc8
+  __TEXT.__objc_stubs: 0x0
+  __TEXT.__auth_stubs: 0x0
+  __TEXT.__objc_classname: 0x0
+  __TEXT.__objc_methname: 0x0
+  __TEXT.__objc_methtype: 0x0
+  __DATA_CONST.__const: 0x9f8
+  __DATA_CONST.__objc_classlist: 0xb0
   __DATA_CONST.__objc_catlist: 0x10
   __DATA_CONST.__objc_protolist: 0xa8
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x1350
+  __DATA_CONST.__objc_selrefs: 0x1380
   __DATA_CONST.__objc_protorefs: 0x18
   __DATA_CONST.__objc_superrefs: 0xa0
   __DATA_CONST.__objc_arraydata: 0x48
-  __AUTH_CONST.__auth_got: 0x370
-  __AUTH_CONST.__const: 0x6a0
-  __AUTH_CONST.__cfstring: 0x13e0
-  __AUTH_CONST.__objc_const: 0x3248
-  __AUTH_CONST.__objc_doubleobj: 0x40
+  __DATA_CONST.__got: 0x410
+  __AUTH_CONST.__const: 0x530
+  __AUTH_CONST.__cfstring: 0xf60
+  __AUTH_CONST.__objc_const: 0x33a0
   __AUTH_CONST.__objc_intobj: 0x288
   __AUTH_CONST.__objc_arrayobj: 0x18
+  __AUTH_CONST.__auth_got: 0x500
   __AUTH.__objc_data: 0xf0
-  __DATA.__objc_ivar: 0x270
-  __DATA.__data: 0x7e0
-  __DATA.__bss: 0x90
+  __AUTH.__data: 0xa8
+  __DATA.__objc_ivar: 0x27c
+  __DATA.__data: 0x808
+  __DATA.__bss: 0x6f8
   __DATA_DIRTY.__objc_data: 0x5a0
-  __DATA_DIRTY.__data: 0x10
-  __DATA_DIRTY.__bss: 0x80
+  __DATA_DIRTY.__data: 0x20
+  __DATA_DIRTY.__bss: 0x240
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/CoreGraphics.framework/CoreGraphics
   - /System/Library/Frameworks/CoreServices.framework/CoreServices

   - /System/Library/Frameworks/Foundation.framework/Foundation
   - /System/Library/Frameworks/Intents.framework/Intents
   - /System/Library/PrivateFrameworks/GeoServices.framework/GeoServices
+  - /System/Library/PrivateFrameworks/GeoServicesCore.framework/GeoServicesCore
   - /System/Library/PrivateFrameworks/IntentsCore.framework/IntentsCore
   - /System/Library/PrivateFrameworks/ProtocolBuffer.framework/ProtocolBuffer
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libc++.1.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 8486024E-0208-348C-BD21-7A591D21F3EF
-  Functions: 752
-  Symbols:   2893
-  CStrings:  1862
+  - /usr/lib/swift/libswiftCore.dylib
+  - /usr/lib/swift/libswiftCoreFoundation.dylib
+  - /usr/lib/swift/libswiftDispatch.dylib
+  - /usr/lib/swift/libswiftOSLog.dylib
+  - /usr/lib/swift/libswiftObjectiveC.dylib
+  - /usr/lib/swift/libswiftXPC.dylib
+  - /usr/lib/swift/libswift_Builtin_float.dylib
+  - /usr/lib/swift/libswiftos.dylib
+  UUID: 332B8DF2-8DED-360D-A61F-788F2EE9837C
+  Functions: 882
+  Symbols:   2884
+  CStrings:  829
 
Symbols:
+ +[VGVehicle _vehicleStateHistoryRetention]
+ -[VGChargingNetwork _initWithGlobalBrandID:name:]
+ -[VGVehicle _pruneStaleVehicleStates]
+ -[VGVehicle setVehicleStateHistory:]
+ -[VGVehicle vehicleStateHistory]
+ -[VGVehicleState initWithIdentifier:pairedAppIdentifier:dateOfUpdate:origin:batteryPercentage:currentEVRange:maxEVRange:minBatteryCapacity:currentBatteryCapacity:maxBatteryCapacity:consumptionArguments:chargingArguments:isCharging:activeConnector:]
+ -[VGVehicleState pairedAppIdentifier]
+ -[VGVehicleStateStorage hasPairedAppIdentifier]
+ -[VGVehicleStateStorage pairedAppIdentifier]
+ -[VGVehicleStateStorage setPairedAppIdentifier:]
+ GCC_except_table113
+ GCC_except_table116
+ GCC_except_table122
+ GCC_except_table201
+ GCC_except_table222
+ GCC_except_table250
+ GCC_except_table327
+ GCC_except_table364
+ GCC_except_table400
+ GCC_except_table443
+ GCC_except_table457
+ GCC_except_table458
+ GCC_except_table460
+ GCC_except_table462
+ GCC_except_table463
+ GCC_except_table464
+ GCC_except_table465
+ GCC_except_table466
+ GCC_except_table468
+ GCC_except_table470
+ GCC_except_table472
+ GCC_except_table474
+ GCC_except_table485
+ GCC_except_table487
+ GCC_except_table493
+ GCC_except_table497
+ GCC_except_table504
+ GCC_except_table506
+ GCC_except_table507
+ GCC_except_table509
+ GCC_except_table510
+ GCC_except_table513
+ GCC_except_table514
+ GCC_except_table518
+ GCC_except_table520
+ GCC_except_table526
+ GCC_except_table588
+ GCC_except_table592
+ GCC_except_table595
+ GCC_except_table600
+ GCC_except_table607
+ GCC_except_table650
+ GCC_except_table654
+ GCC_except_table659
+ GCC_except_table715
+ GCC_except_table72
+ GCC_except_table720
+ GCC_except_table723
+ GCC_except_table725
+ GCC_except_table82
+ GCC_except_table83
+ GCC_except_table84
+ GCC_except_table87
+ _CFAbsoluteTimeGetCurrent
+ _OBJC_CLASS_$__TtCs12_SwiftObject
+ _OBJC_IVAR_$_VGVehicle._vehicleStateHistory
+ _OBJC_IVAR_$_VGVehicleState._pairedAppIdentifier
+ _OBJC_IVAR_$_VGVehicleStateStorage._pairedAppIdentifier
+ _OBJC_METACLASS_$__TtCs12_SwiftObject
+ _VirtualGarageConfig_BatteryChargeThresholdForVehicleStateComparison
+ _VirtualGarageConfig_EVRoutingVehicleStateHistoryRetention
+ __DATA__TtC13VirtualGarage20VirtualGarageConfigs
+ __IVARS__TtC13VirtualGarage20VirtualGarageConfigs
+ __METACLASS_DATA__TtC13VirtualGarage20VirtualGarageConfigs
+ __OBJC_$_PROP_LIST_VGOEMApplication.199
+ __VirtualGarageConfig_MetadataForIdentifier
+ ___35-[VGDataCoordinator unpairVehicle:]_block_invoke.76
+ ___36-[VGDataCoordinator OEMAppsUpdated:]_block_invoke.90
+ ___36-[VGDataCoordinator OEMAppsUpdated:]_block_invoke.91
+ ___37-[VGVehicle initWithMapsSyncVehicle:]_block_invoke.19
+ ___40-[VGVirtualGarageService openForClient:]_block_invoke.29
+ ___41-[VGDataCoordinator vehicleStateUpdated:]_block_invoke.89
+ ___41-[VGVirtualGarageService _openConnection]_block_invoke.69
+ ___42+[VGVehicle _vehicleStateHistoryRetention]_block_invoke
+ ___42-[VGDataCoordinator forceFetchAllVehicles]_block_invoke.14
+ ___43-[VGOEMApplication listCarsWithCompletion:]_block_invoke.39
+ ___43-[VGOEMApplication listCarsWithCompletion:]_block_invoke.40
+ ___43-[VGOEMApplication listCarsWithCompletion:]_block_invoke.42
+ ___43-[VGOEMApplication listCarsWithCompletion:]_block_invoke.43
+ ___45-[VGDataCoordinator finishOnboardingVehicle:]_block_invoke.74
+ ___46-[VGVirtualGarage virtualGarageSelectVehicle:]_block_invoke.36
+ ___50-[_VGOEMExtensionConnection resumeWithCompletion:]_block_invoke.27
+ ___55-[VGDataCoordinator getLatestStateOfVehicle:withReply:]_block_invoke.101
+ ___55-[VGDataCoordinator getLatestStateOfVehicle:withReply:]_block_invoke.102
+ ___55-[VGOEMApplication stopSendingChargeUpdatesForVehicle:]_block_invoke.71
+ ___56-[VGChargingNetworkAvailabilityProvider _reloadNetworks]_block_invoke.21
+ ___56-[VGOEMApplication startSendingChargeUpdatesForVehicle:]_block_invoke.69
+ ___58-[VGOEMApplication getStateOfChargeForVehicle:completion:]_block_invoke.47
+ ___58-[VGOEMApplication getStateOfChargeForVehicle:completion:]_block_invoke.48
+ ___58-[VGOEMApplication getStateOfChargeForVehicle:completion:]_block_invoke.49
+ ___58-[VGOEMApplication getStateOfChargeForVehicle:completion:]_block_invoke.50
+ ___58-[VGOEMApplication getStateOfChargeForVehicle:completion:]_block_invoke.62
+ ___58-[VGOEMApplication tearDownStreamingConnectionForVehicle:]_block_invoke.72
+ ___58-[VGOEMApplication tearDownStreamingConnectionForVehicle:]_block_invoke.73
+ ___59-[VGDataCoordinator _loadAllOEMVehiclesForApps:completion:]_block_invoke.86
+ ___59-[VGDataCoordinator _loadAllOEMVehiclesForApps:completion:]_block_invoke.87
+ ___60-[VGVirtualGarageServer listener:shouldAcceptNewConnection:]_block_invoke.56
+ ___60-[VGVirtualGarageServer listener:shouldAcceptNewConnection:]_block_invoke.57
+ ___62-[VGExternalAccessoryModelFilter _initializeAllowAndDenylists]_block_invoke.39
+ ___62-[VGExternalAccessoryModelFilter _initializeAllowAndDenylists]_block_invoke.41
+ ___64-[VGDataCoordinator _updateGarageWithVehicle:syncAcrossDevices:]_block_invoke.17
+ ___64-[VGDataCoordinator _updateGarageWithVehicle:syncAcrossDevices:]_block_invoke.19
+ ___81-[VGDataCoordinator _updateStateOfChargeForVehicle:syncAcrossDevices:completion:]_block_invoke.22
+ ___81-[VGDataCoordinator _updateStateOfChargeForVehicle:syncAcrossDevices:completion:]_block_invoke.23
+ ___81-[VGExternalAccessoryModelFilter allowsVehicleWithModelId:firmwareId:year:model:]_block_invoke.46
+ ___98-[VGVirtualGarage virtualGarageGetLatestStateOfVehicleWithIdentifier:syncAcrossDevices:withReply:]_block_invoke.44
+ ___98-[VGVirtualGarage virtualGarageGetLatestStateOfVehicleWithIdentifier:syncAcrossDevices:withReply:]_block_invoke.53
+ ___98-[VGVirtualGarage virtualGarageGetLatestStateOfVehicleWithIdentifier:syncAcrossDevices:withReply:]_block_invoke.54
+ ___Block_byref_object_copy_.634
+ ___Block_byref_object_copy_.769
+ ___Block_byref_object_dispose_.635
+ ___Block_byref_object_dispose_.770
+ ___NSStringFromVGChargingConnectorTypeOptions_block_invoke.55
+ ___block_literal_global.102
+ ___block_literal_global.1153
+ ___block_literal_global.1647
+ ___block_literal_global.1869
+ ___block_literal_global.2014
+ ___block_literal_global.21
+ ___block_literal_global.24
+ ___block_literal_global.310
+ ___block_literal_global.39
+ ___block_literal_global.400
+ ___block_literal_global.55
+ ___block_literal_global.69
+ ___block_literal_global.71
+ ___block_literal_global.712
+ ___block_literal_global.759
+ ___block_literal_global.82
+ ___block_literal_global.85
+ ___block_literal_global.881
+ ___chkstk_darwin
+ ___swift_allocate_value_buffer
+ ___swift_instantiateConcreteTypeFromMangledNameAbstractV2
+ ___swift_instantiateConcreteTypeFromMangledNameV2
+ ___swift_project_value_buffer
+ ___swift_reflection_version
+ __swift_FORCE_LOAD_$_swiftCoreFoundation
+ __swift_FORCE_LOAD_$_swiftCoreFoundation_$_VirtualGarage
+ __swift_FORCE_LOAD_$_swiftDispatch
+ __swift_FORCE_LOAD_$_swiftDispatch_$_VirtualGarage
+ __swift_FORCE_LOAD_$_swiftFoundation
+ __swift_FORCE_LOAD_$_swiftFoundation_$_VirtualGarage
+ __swift_FORCE_LOAD_$_swiftOSLog
+ __swift_FORCE_LOAD_$_swiftOSLog_$_VirtualGarage
+ __swift_FORCE_LOAD_$_swiftObjectiveC
+ __swift_FORCE_LOAD_$_swiftObjectiveC_$_VirtualGarage
+ __swift_FORCE_LOAD_$_swiftXPC
+ __swift_FORCE_LOAD_$_swiftXPC_$_VirtualGarage
+ __swift_FORCE_LOAD_$_swift_Builtin_float
+ __swift_FORCE_LOAD_$_swift_Builtin_float_$_VirtualGarage
+ __swift_FORCE_LOAD_$_swiftos
+ __swift_FORCE_LOAD_$_swiftos_$_VirtualGarage
+ __vehicleStateHistoryRetention.onceToken
+ __vehicleStateHistoryRetention.retentionInterval
+ _free
+ _objc_claimAutoreleasedReturnValue
+ _objc_msgSend$_initWithGlobalBrandID:name:
+ _objc_msgSend$_pruneStaleVehicleStates
+ _objc_msgSend$_storage
+ _objc_msgSend$_vehicleStateHistoryRetention
+ _objc_msgSend$hasDateOfUpdate
+ _objc_msgSend$initWithIdentifier:pairedAppIdentifier:dateOfUpdate:origin:batteryPercentage:currentEVRange:maxEVRange:minBatteryCapacity:currentBatteryCapacity:maxBatteryCapacity:consumptionArguments:chargingArguments:isCharging:activeConnector:
+ _objc_msgSend$setVehicleStateHistory:
+ _objc_opt_self
+ _objc_retainAutoreleaseReturnValue
+ _objc_retain_x1
+ _objc_retain_x3
+ _objc_retain_x4
+ _swift_allocObject
+ _swift_beginAccess
+ _swift_bridgeObjectRelease
+ _swift_coroFrameAlloc
+ _swift_deallocClassInstance
+ _swift_deletedMethodError
+ _swift_endAccess
+ _swift_getTypeByMangledNameInContext2
+ _swift_getTypeByMangledNameInContextInMetadataState2
+ _swift_getWitnessTable
+ _swift_lookUpClassMethod
+ _swift_once
+ _swift_release_x1
+ _swift_release_x8
+ _swift_retain
+ _swift_retain_x19
+ _swift_slowAlloc
+ _swift_unknownObjectRelease
+ _swift_unknownObjectRetain
+ _symbolic $s11GeoServices9GEOConfigV9NamespaceP
+ _symbolic $s13VirtualGarage0aB7ConfigsC13_KeyNamespaceP
+ _symbolic Say_____G 11GeoServices9GEOConfigV7OptionsV
+ _symbolic _____ 13VirtualGarage0aB7ConfigsC
+ _symbolic _____Sg 11GeoServices10_GEOConfigV8MetadataV
+ _symbolic ______p 13VirtualGarage0aB7ConfigsC13_KeyNamespaceP
+ _symbolic ______pSg 11GeoServices9GEOConfigV14StoreProvidingP
+ _symbolic _____y_SS______pG 11GeoServices9GEOConfigV3KeyV 13VirtualGarage0eF7ConfigsC01_D9NamespaceP
+ _symbolic _____y_Sb______pG 11GeoServices9GEOConfigV3KeyV 13VirtualGarage0eF7ConfigsC01_D9NamespaceP
+ _symbolic _____y_Sd______pG 11GeoServices9GEOConfigV3KeyV 13VirtualGarage0eF7ConfigsC01_D9NamespaceP
+ _symbolic _____y_____G s23_ContiguousArrayStorageC 11GeoServices9GEOConfigV7OptionsV
- -[VGVehicleState initWithIdentifier:dateOfUpdate:origin:batteryPercentage:currentEVRange:maxEVRange:minBatteryCapacity:currentBatteryCapacity:maxBatteryCapacity:consumptionArguments:chargingArguments:isCharging:activeConnector:]
- GCC_except_table109
- GCC_except_table135
- GCC_except_table136
- GCC_except_table139
- GCC_except_table145
- GCC_except_table221
- GCC_except_table242
- GCC_except_table270
- GCC_except_table347
- GCC_except_table383
- GCC_except_table419
- GCC_except_table475
- GCC_except_table479
- GCC_except_table480
- GCC_except_table484
- GCC_except_table486
- GCC_except_table488
- GCC_except_table490
- GCC_except_table492
- GCC_except_table496
- GCC_except_table500
- GCC_except_table501
- GCC_except_table512
- GCC_except_table515
- GCC_except_table523
- GCC_except_table524
- GCC_except_table527
- GCC_except_table528
- GCC_except_table529
- GCC_except_table531
- GCC_except_table532
- GCC_except_table535
- GCC_except_table536
- GCC_except_table538
- GCC_except_table539
- GCC_except_table540
- GCC_except_table543
- GCC_except_table544
- GCC_except_table606
- GCC_except_table610
- GCC_except_table613
- GCC_except_table618
- GCC_except_table625
- GCC_except_table668
- GCC_except_table672
- GCC_except_table677
- GCC_except_table733
- GCC_except_table738
- GCC_except_table741
- GCC_except_table743
- GCC_except_table99
- _OBJC_CLASS_$_NSConstantDoubleNumber
- _VirtualGarageConfig_AutomaticallyDeselectMissingVehicles_Metadata
- _VirtualGarageConfig_AutomaticallyDeselectMissingVehicles_Metadata_block_invoke_22
- _VirtualGarageConfig_CapacityThresholdForVehicleStateComparison_Metadata
- _VirtualGarageConfig_CapacityThresholdForVehicleStateComparison_Metadata_block_invoke_23
- _VirtualGarageConfig_EVRoutingAllowSteppingRoutes_Metadata
- _VirtualGarageConfig_EVRoutingAllowSteppingRoutes_Metadata_block_invoke_27
- _VirtualGarageConfig_EVRoutingDisabledApplications_Metadata
- _VirtualGarageConfig_EVRoutingDisabledApplications_Metadata_block_invoke_17
- _VirtualGarageConfig_EVRoutingEnableAutomaticVehicleDeselection_Metadata
- _VirtualGarageConfig_EVRoutingEnableAutomaticVehicleDeselection_Metadata_block_invoke_21
- _VirtualGarageConfig_EVRoutingEnableIAP2Onboarding_Metadata
- _VirtualGarageConfig_EVRoutingEnableIAP2Onboarding_Metadata_block_invoke_19
- _VirtualGarageConfig_EVRoutingForceShowLastSyncDate_Metadata
- _VirtualGarageConfig_EVRoutingForceShowLastSyncDate_Metadata_block_invoke_13
- _VirtualGarageConfig_EVRoutingIntentsRequestTimeout_Metadata
- _VirtualGarageConfig_EVRoutingIntentsRequestTimeout_Metadata_block_invoke_15
- _VirtualGarageConfig_EVRoutingKeyNameForModelID_Metadata
- _VirtualGarageConfig_EVRoutingKeyNameForModelID_Metadata_block_invoke_2
- _VirtualGarageConfig_EVRoutingManifestKeyNameForIApAllowlist_Metadata
- _VirtualGarageConfig_EVRoutingManifestKeyNameForIApAllowlist_Metadata_block_invoke_6
- _VirtualGarageConfig_EVRoutingManifestKeyNameForIApDenyListedFirmwareID_Metadata
- _VirtualGarageConfig_EVRoutingManifestKeyNameForIApDenyListedFirmwareID_Metadata_block_invoke_9
- _VirtualGarageConfig_EVRoutingManifestKeyNameForIApDenyListedModelID_Metadata
- _VirtualGarageConfig_EVRoutingManifestKeyNameForIApDenyListedModelID_Metadata_block_invoke_8
- _VirtualGarageConfig_EVRoutingManifestKeyNameForIApDenyListedModel_Metadata
- _VirtualGarageConfig_EVRoutingManifestKeyNameForIApDenyListedModel_Metadata_block_invoke_10
- _VirtualGarageConfig_EVRoutingManifestKeyNameForIApDenyListedYear_Metadata
- _VirtualGarageConfig_EVRoutingManifestKeyNameForIApDenyListedYear_Metadata_block_invoke_11
- _VirtualGarageConfig_EVRoutingManifestKeyNameForIApDenylist_Metadata
- _VirtualGarageConfig_EVRoutingManifestKeyNameForIApDenylist_Metadata_block_invoke_7
- _VirtualGarageConfig_EVRoutingManifestKeyNameForSiriAllowListedModelIDs_Metadata
- _VirtualGarageConfig_EVRoutingManifestKeyNameForSiriAllowListedModelIDs_Metadata_block_invoke_5
- _VirtualGarageConfig_EVRoutingManifestKeyNameForSiriAllowlist_Metadata
- _VirtualGarageConfig_EVRoutingManifestKeyNameForSiriAllowlist_Metadata_block_invoke_3
- _VirtualGarageConfig_EVRoutingManifestKeyNameForSiriBundleID_Metadata
- _VirtualGarageConfig_EVRoutingManifestKeyNameForSiriBundleID_Metadata_block_invoke_4
- _VirtualGarageConfig_EVRoutingOEMAppPullInterval_Metadata
- _VirtualGarageConfig_EVRoutingOEMAppPullInterval_Metadata_block_invoke_14
- _VirtualGarageConfig_EVRoutingResourceNameForAllowAndDenylists_Metadata
- _VirtualGarageConfig_EVRoutingResourceNameForAllowAndDenylists_Metadata_block_invoke_12
- _VirtualGarageConfig_EVRoutingResourceNameForPreferredNetworksList_Metadata
- _VirtualGarageConfig_EVRoutingResourceNameForPreferredNetworksList_Metadata_block_invoke_25
- _VirtualGarageConfig_EVRoutingStreamUpdatesDuringNav_Metadata
- _VirtualGarageConfig_EVRoutingStreamUpdatesDuringNav_Metadata_block_invoke_16
- _VirtualGarageConfig_EVRoutingSynchronousVehicleStateUpdate_Metadata
- _VirtualGarageConfig_EVRoutingSynchronousVehicleStateUpdate_Metadata_block_invoke_18
- _VirtualGarageConfig_EVRoutingUseCarDisplaySimIdentifier_Metadata
- _VirtualGarageConfig_EVRoutingUseCarDisplaySimIdentifier_Metadata_block_invoke_20
- _VirtualGarageConfig_EVRoutingUseMapsSyncLiveUpdates_Metadata
- _VirtualGarageConfig_EVRoutingUseMapsSyncLiveUpdates_Metadata_block_invoke
- _VirtualGarageConfig_EnableAutomaticVehicleUnpairing_Metadata
- _VirtualGarageConfig_EnableAutomaticVehicleUnpairing_Metadata_block_invoke_26
- _VirtualGarageConfig_TimeThresholdForVehicleStateComparison_Metadata
- _VirtualGarageConfig_TimeThresholdForVehicleStateComparison_Metadata_block_invoke_24
- __OBJC_$_PROP_LIST_VGOEMApplication.194
- ___35-[VGDataCoordinator unpairVehicle:]_block_invoke.72
- ___36-[VGDataCoordinator OEMAppsUpdated:]_block_invoke.86
- ___36-[VGDataCoordinator OEMAppsUpdated:]_block_invoke.87
- ___37-[VGVehicle initWithMapsSyncVehicle:]_block_invoke.13
- ___40-[VGVirtualGarageService openForClient:]_block_invoke.23
- ___41-[VGDataCoordinator vehicleStateUpdated:]_block_invoke.85
- ___41-[VGVirtualGarageService _openConnection]_block_invoke.63
- ___42-[VGDataCoordinator forceFetchAllVehicles]_block_invoke.10
- ___43-[VGOEMApplication listCarsWithCompletion:]_block_invoke.31
- ___43-[VGOEMApplication listCarsWithCompletion:]_block_invoke.33
- ___43-[VGOEMApplication listCarsWithCompletion:]_block_invoke.34
- ___43-[VGOEMApplication listCarsWithCompletion:]_block_invoke.36
- ___45-[VGDataCoordinator finishOnboardingVehicle:]_block_invoke.70
- ___46-[VGVirtualGarage virtualGarageSelectVehicle:]_block_invoke.30
- ___50-[_VGOEMExtensionConnection resumeWithCompletion:]_block_invoke.22
- ___55-[VGDataCoordinator getLatestStateOfVehicle:withReply:]_block_invoke.95
- ___55-[VGDataCoordinator getLatestStateOfVehicle:withReply:]_block_invoke.96
- ___55-[VGOEMApplication stopSendingChargeUpdatesForVehicle:]_block_invoke.65
- ___56-[VGChargingNetworkAvailabilityProvider _reloadNetworks]_block_invoke.15
- ___56-[VGOEMApplication startSendingChargeUpdatesForVehicle:]_block_invoke.63
- ___58-[VGOEMApplication getStateOfChargeForVehicle:completion:]_block_invoke.41
- ___58-[VGOEMApplication getStateOfChargeForVehicle:completion:]_block_invoke.42
- ___58-[VGOEMApplication getStateOfChargeForVehicle:completion:]_block_invoke.43
- ___58-[VGOEMApplication getStateOfChargeForVehicle:completion:]_block_invoke.44
- ___58-[VGOEMApplication getStateOfChargeForVehicle:completion:]_block_invoke.56
- ___58-[VGOEMApplication tearDownStreamingConnectionForVehicle:]_block_invoke.66
- ___58-[VGOEMApplication tearDownStreamingConnectionForVehicle:]_block_invoke.67
- ___59-[VGDataCoordinator _loadAllOEMVehiclesForApps:completion:]_block_invoke.82
- ___59-[VGDataCoordinator _loadAllOEMVehiclesForApps:completion:]_block_invoke.83
- ___60-[VGVirtualGarageServer listener:shouldAcceptNewConnection:]_block_invoke.50
- ___60-[VGVirtualGarageServer listener:shouldAcceptNewConnection:]_block_invoke.51
- ___62-[VGExternalAccessoryModelFilter _initializeAllowAndDenylists]_block_invoke.34
- ___62-[VGExternalAccessoryModelFilter _initializeAllowAndDenylists]_block_invoke.36
- ___64-[VGDataCoordinator _updateGarageWithVehicle:syncAcrossDevices:]_block_invoke.13
- ___64-[VGDataCoordinator _updateGarageWithVehicle:syncAcrossDevices:]_block_invoke.15
- ___81-[VGDataCoordinator _updateStateOfChargeForVehicle:syncAcrossDevices:completion:]_block_invoke.18
- ___81-[VGDataCoordinator _updateStateOfChargeForVehicle:syncAcrossDevices:completion:]_block_invoke.19
- ___81-[VGExternalAccessoryModelFilter allowsVehicleWithModelId:firmwareId:year:model:]_block_invoke.41
- ___98-[VGVirtualGarage virtualGarageGetLatestStateOfVehicleWithIdentifier:syncAcrossDevices:withReply:]_block_invoke.38
- ___98-[VGVirtualGarage virtualGarageGetLatestStateOfVehicleWithIdentifier:syncAcrossDevices:withReply:]_block_invoke.47
- ___98-[VGVirtualGarage virtualGarageGetLatestStateOfVehicleWithIdentifier:syncAcrossDevices:withReply:]_block_invoke.48
- ___Block_byref_object_copy_.671
- ___Block_byref_object_copy_.815
- ___Block_byref_object_dispose_.672
- ___Block_byref_object_dispose_.816
- ___NSStringFromVGChargingConnectorTypeOptions_block_invoke.49
- ___block_descriptor_32_e5_8?0l
- ___block_literal_global.104
- ___block_literal_global.106
- ___block_literal_global.110
- ___block_literal_global.116
- ___block_literal_global.1223
- ___block_literal_global.124
- ___block_literal_global.130
- ___block_literal_global.139
- ___block_literal_global.145
- ___block_literal_global.151
- ___block_literal_global.157
- ___block_literal_global.163
- ___block_literal_global.169
- ___block_literal_global.17
- ___block_literal_global.17.344
- ___block_literal_global.1734
- ___block_literal_global.177
- ___block_literal_global.18
- ___block_literal_global.185
- ___block_literal_global.194
- ___block_literal_global.1959
- ___block_literal_global.200
- ___block_literal_global.2097
- ___block_literal_global.26
- ___block_literal_global.33
- ___block_literal_global.35
- ___block_literal_global.367
- ___block_literal_global.44
- ___block_literal_global.457
- ___block_literal_global.49
- ___block_literal_global.53
- ___block_literal_global.60
- ___block_literal_global.62
- ___block_literal_global.65
- ___block_literal_global.68
- ___block_literal_global.760
- ___block_literal_global.77
- ___block_literal_global.77.130
- ___block_literal_global.8
- ___block_literal_global.805
- ___block_literal_global.81
- ___block_literal_global.86
- ___block_literal_global.925
- ___block_literal_global.95
- ___kCFBooleanFalse
- ___kCFBooleanTrue
- __registerStateCaptureCallbacks
- __stateCaptureCallbackRegistration
- _objc_msgSend$initWithIdentifier:dateOfUpdate:origin:batteryPercentage:currentEVRange:maxEVRange:minBatteryCapacity:currentBatteryCapacity:maxBatteryCapacity:consumptionArguments:chargingArguments:isCharging:activeConnector:
CStrings:
+ "-[VGDataCoordinator _removeUnpairedIapVehicleIfNeeded]_block_invoke"
+ "<%@:%p, identifier: %@, pairedAppIdentifier: %@, dateOfUpdate: %@, origin: %@, batteryCharge: %@, currentEVRange: %@, maxEVRange: %@, minBatteryCapacity: %@, currentBatteryCapacity: %@, maxBatteryCapacity: %@, consumptionArguments: %@, chargingArguments: %@, isCharging: %@, activeConnector: %@>"
+ "BatteryChargeThresholdForVehicleStateComparison"
+ "EVRoutingVehicleStateHistoryRetention"
+ "Fatal error"
+ "Invalid VirtualGarageConfig GEOConfig key id "
+ "VirtualGarage/VirtualGarageConfigs.swift"
+ "[%{public}p] _currentStatePassesEVRoutingRequirements: accessoryState is nil"
+ "[%{public}p] _currentStatePassesEVRoutingRequirements: identifier is nil"
+ "[%{public}p] _currentStatePassesEVRoutingRequirements: not connected to electric vehicle"
+ "[%{public}p] _isConnectedToElectricVehicle: chargingArguments is empty"
+ "[%{public}p] _isConnectedToElectricVehicle: consumptionArguments is empty"
+ "[%{public}p] _isConnectedToElectricVehicle: not connected to CarPlay accessory"
+ "_onboardVehicle will onboard vehicle, but it wasn't in the list of unpaired vehicles (%@)"
+ "_onboardVehicle will onboard vehicle, but we didn't find exactly one match in (%@) unpairedVehicles: %@"
+ "_onboardVehicle: will onboard vehicle (%@)"
+ "_vehicleStateHistory"
+ "identifierMatches && appMatches"
+ "isSignificantlyDifferentFromVehicleState: -> YES. Battery charge percentage has changed. current: %@, new: %@"
+ "isSignificantlyDifferentFromVehicleState: -> YES. Battery charge percentage presence has changed."
- "#16@0:8"
- ".cxx_destruct"
- "<%@:%p, identifier: %@, dateOfUpdate: %@, origin: %@, batteryCharge: %@, currentEVRange: %@, maxEVRange: %@, minBatteryCapacity: %@, currentBatteryCapacity: %@, maxBatteryCapacity: %@, consumptionArguments: %@, chargingArguments: %@, isCharging: %@, activeConnector: %@>"
- "@\"<VGChargingNetworkAvailabilityProviderDelegate>\""
- "@\"<VGDataCoordinatorDelegate>\""
- "@\"<VGExternalAccessoryUpdating>\""
- "@\"<VGOEMAppSOCStreaming>\""
- "@\"<VGOEMAppSOCStreaming>\"16@0:8"
- "@\"<VGOEMApplicationFinderUpdates>\""
- "@\"<VGOEMApplicationFinderUpdates>\"16@0:8"
- "@\"<VGOEMApplicationFinding>\""
- "@\"<VGVirtualGarageDelegate>\""
- "@\"<VGVirtualGarageObserver>\""
- "@\"<VGVirtualGaragePersisting>\""
- "@\"GEOObserverHashTable\""
- "@\"GEOPerformanceEventLogger\""
- "@\"INCExtensionConnection\""
- "@\"INIntent\""
- "@\"LSApplicationRecord\""
- "@\"LSApplicationRecord\"16@0:8"
- "@\"NSArray\""
- "@\"NSArray\"16@0:8"
- "@\"NSData\""
- "@\"NSDate\""
- "@\"NSDictionary\""
- "@\"NSHashTable\""
- "@\"NSMapTable\""
- "@\"NSMeasurement\""
- "@\"NSMutableArray\""
- "@\"NSMutableDictionary\""
- "@\"NSMutableSet\""
- "@\"NSNumber\""
- "@\"NSObject<OS_dispatch_queue>\""
- "@\"NSSet\""
- "@\"NSString\""
- "@\"NSString\"16@0:8"
- "@\"NSTimer\""
- "@\"NSXPCConnection\""
- "@\"NSXPCListener\""
- "@\"VGDataCoordinator\""
- "@\"VGExternalAccessory\""
- "@\"VGExternalAccessoryModelFilter\""
- "@\"VGExternalAccessoryState\""
- "@\"VGVehicle\""
- "@\"VGVehicle\"16@0:8"
- "@\"VGVehicle\"24@0:8@\"NSString\"16"
- "@\"VGVehicleState\""
- "@\"VGVirtualGarage\""
- "@\"geo_isolater\""
- "@116@0:8@16@24q32@40@48@56@64@72@80@88@96B104Q108"
- "@16@0:8"
- "@20@0:8B16"
- "@20@0:8i16"
- "@24@0:8:16"
- "@24@0:8@\"NSCoder\"16"
- "@24@0:8@16"
- "@24@0:8@?16"
- "@24@0:8Q16"
- "@24@0:8^{_NSZone=}16"
- "@24@0:8q16"
- "@32@0:8:16@24"
- "@32@0:8@\"NSString\"16@\"LSApplicationRecord\"24"
- "@32@0:8@16@24"
- "@32@0:8@16^@24"
- "@40@0:8:16@24@32"
- "@40@0:8@16@24@32"
- "@48@0:8@16@24@32@40"
- "@88@0:8@16@24@32@40@48@56@64@72@80"
- "@88@0:8@16@24@32@40@48@56@64Q72@80"
- "@8@?0"
- "@?"
- "B"
- "B16@0:8"
- "B24@0:8#16"
- "B24@0:8:16"
- "B24@0:8@\"NSString\"16"
- "B24@0:8@\"Protocol\"16"
- "B24@0:8@\"VGVehicle\"16"
- "B24@0:8@16"
- "B32@0:8@\"NSXPCListener\"16@\"NSXPCConnection\"24"
- "B32@0:8@16@24"
- "B48@0:8@16@24@32@40"
- "CarPlaySupport"
- "GEOConfigChangeListenerDelegate"
- "GEOResourceManifestTileGroupObserver"
- "INIntentResponseObserver"
- "JSONObjectWithData:options:error:"
- "LSApplicationWorkspaceObserverProtocol"
- "NSCoding"
- "NSCopying"
- "NSObject"
- "NSSecureCoding"
- "NSXPCListenerDelegate"
- "OEMAppsUpdated:"
- "Onboarding vehicle: %@ in virtual garage."
- "Q16@0:8"
- "Q24@0:8@16"
- "StringAsActiveConnector:"
- "StringAsOrigin:"
- "T#,R"
- "T@\"<VGExternalAccessoryUpdating>\",W,N,V_accessoryUpdateDelegate"
- "T@\"<VGOEMAppSOCStreaming>\",W,N"
- "T@\"<VGOEMAppSOCStreaming>\",W,N,V_chargeStreamingDelegate"
- "T@\"<VGOEMApplicationFinderUpdates>\",W,N"
- "T@\"<VGOEMApplicationFinderUpdates>\",W,N,V_delegate"
- "T@\"<VGVirtualGarageDelegate>\",W,N,V_delegate"
- "T@\"<VGVirtualGarageObserver>\",W,N,V_observer"
- "T@\"LSApplicationRecord\",R,N"
- "T@\"LSApplicationRecord\",R,N,V_applicationRecord"
- "T@\"NSArray\",&,N,V_allowedFormulaIDs"
- "T@\"NSArray\",&,N,V_denylist"
- "T@\"NSArray\",&,N,V_modelIdAllowlist"
- "T@\"NSArray\",R,C,N"
- "T@\"NSArray\",R,N"
- "T@\"NSData\",&,N,V_pairedAppInstallSessionIdentifier"
- "T@\"NSDate\",R,C,N,V_creationDate"
- "T@\"NSDate\",R,C,N,V_lastStateUpdateDate"
- "T@\"NSDate\",R,N,V_dateOfUpdate"
- "T@\"NSDictionary\",&,N,V_allowlist"
- "T@\"NSDictionary\",R,C,N,V_powerByConnector"
- "T@\"NSDictionary\",R,N,V_powerByConnector"
- "T@\"NSMeasurement\",&,N,V_currentBatteryCapacity"
- "T@\"NSMeasurement\",&,N,V_currentEVRange"
- "T@\"NSMeasurement\",&,N,V_maxBatteryCapacity"
- "T@\"NSMeasurement\",&,N,V_maxEVRange"
- "T@\"NSMeasurement\",&,N,V_minBatteryCapacity"
- "T@\"NSMeasurement\",R,N,V_currentBatteryCapacity"
- "T@\"NSMeasurement\",R,N,V_currentEVRange"
- "T@\"NSMeasurement\",R,N,V_maxBatteryCapacity"
- "T@\"NSMeasurement\",R,N,V_maxEVRange"
- "T@\"NSMeasurement\",R,N,V_minBatteryCapacity"
- "T@\"NSMutableArray\",&,N,V_activeConnections"
- "T@\"NSMutableArray\",&,N,V_networks"
- "T@\"NSMutableDictionary\",&,N,V_applications"
- "T@\"NSNumber\",&,N,V_batteryCharge"
- "T@\"NSNumber\",N,V_supportedConnectors"
- "T@\"NSNumber\",R,N,V_activeConnector"
- "T@\"NSNumber\",R,N,V_batteryPercentage"
- "T@\"NSObject<OS_dispatch_queue>\",&,N,V_observerQueue"
- "T@\"NSSet\",&,N,V_disabledAppIdentifiers"
- "T@\"NSSet\",&,N,V_preferredChargingNetworks"
- "T@\"NSString\",&,N,V_chargingArguments"
- "T@\"NSString\",&,N,V_colorHex"
- "T@\"NSString\",&,N,V_consumptionArguments"
- "T@\"NSString\",&,N,V_iapIdentifier"
- "T@\"NSString\",&,N,V_identifier"
- "T@\"NSString\",&,N,V_manufacturer"
- "T@\"NSString\",&,N,V_model"
- "T@\"NSString\",&,N,V_name"
- "T@\"NSString\",&,N,V_pairedAppIdentifier"
- "T@\"NSString\",&,N,V_pairedAppInstallDeviceIdentifier"
- "T@\"NSString\",&,N,V_siriIntentsIdentifier"
- "T@\"NSString\",&,N,V_year"
- "T@\"NSString\",?,R,C"
- "T@\"NSString\",C,N,V_colorHex"
- "T@\"NSString\",C,N,V_displayName"
- "T@\"NSString\",C,N,V_licensePlate"
- "T@\"NSString\",C,N,V_lprPowerType"
- "T@\"NSString\",C,N,V_lprVehicleType"
- "T@\"NSString\",C,V_activeVehicleIdentifier"
- "T@\"NSString\",R,C"
- "T@\"NSString\",R,C,N,V_headUnitBluetoothIdentifier"
- "T@\"NSString\",R,C,N,V_headUnitIdentifier"
- "T@\"NSString\",R,C,N,V_identifier"
- "T@\"NSString\",R,C,N,V_manufacturer"
- "T@\"NSString\",R,C,N,V_model"
- "T@\"NSString\",R,C,N,V_year"
- "T@\"NSString\",R,N"
- "T@\"NSString\",R,N,V_chargingArguments"
- "T@\"NSString\",R,N,V_consumptionArguments"
- "T@\"NSString\",R,N,V_identifier"
- "T@\"NSString\",R,N,V_name"
- "T@\"NSXPCConnection\",&,N,V_connection"
- "T@\"NSXPCListener\",&,N,V_listener"
- "T@\"VGOEMExtensionConnectionBroker\",R,N"
- "T@\"VGVehicle\",R,N"
- "T@\"VGVehicleState\",R,N,V_currentVehicleState"
- "T@\"VGVirtualGarage\",&,N,V_garage"
- "TB,N"
- "TB,N,GisEnabled"
- "TB,N,GisEnabled,V_enabled"
- "TB,N,V_hostsVirtualGarage"
- "TB,N,V_isCharging"
- "TB,N,V_shouldAssumeFullCharge"
- "TB,N,V_usesPreferredNetworksForRouting"
- "TB,R"
- "TB,R,N"
- "TB,R,N,V_isCharging"
- "TQ,N,V_identifier"
- "TQ,N,V_supportedConnectors"
- "TQ,R"
- "TQ,R,N,V_activeConnector"
- "TQ,R,N,V_globalBrandID"
- "Td,N,V_batteryPercentage"
- "Td,N,V_currentBatteryCapacity"
- "Td,N,V_currentEVRange"
- "Td,N,V_dateOfUpdate"
- "Td,N,V_maxBatteryCapacity"
- "Td,N,V_maxEVRange"
- "Td,N,V_minBatteryCapacity"
- "Ti,N,V_activeConnector"
- "Ti,N,V_origin"
- "Tq,R,N,V_origin"
- "UTF8String"
- "UUID"
- "UUIDString"
- "VGChargingNetwork"
- "VGChargingNetworkAvailabilityProvider"
- "VGChargingNetworkStorage"
- "VGChargingNetworksStorage"
- "VGDataCoordinator"
- "VGDataCoordinatorDelegate"
- "VGDenylistEntry"
- "VGExternalAccessory"
- "VGExternalAccessoryModelFilter"
- "VGExternalAccessoryState"
- "VGExternalAccessoryUpdating"
- "VGExtras"
- "VGOEMAppSOCStreaming"
- "VGOEMApplication"
- "VGOEMApplicationFinder"
- "VGOEMApplicationFinderUpdates"
- "VGOEMApplicationFinding"
- "VGVehicle"
- "VGVehicleDeduper"
- "VGVehicleState"
- "VGVehicleStateProviding"
- "VGVehicleStateStorage"
- "VGVirtualGarage"
- "VGVirtualGarageActions"
- "VGVirtualGarageDelegate"
- "VGVirtualGarageObserver"
- "VGVirtualGaragePersistingDelegate"
- "VGVirtualGarageService"
- "Vv16@0:8"
- "[state.identifier isEqualToString:vehicle.siriIntentsIdentifier]"
- "^{_NSZone=}16@0:8"
- "_VGChargingConnectorTypeOptionFromINCarChargingConnectorType:"
- "_VGChargingConnectorTypeOptionsFromINCarChargingConnectorTypes:"
- "_VGOEMExtensionConnection"
- "_VGOEMExtensionConnectionKey"
- "_accessory"
- "_accessoryDidConnect:"
- "_accessoryDidDisconnect:"
- "_accessoryDidUpdateVehicle:"
- "_accessoryState"
- "_accessoryUpdateDelegate"
- "_activeConnections"
- "_activeVehicleIdentifier"
- "_addNewCarPlayAccessory:"
- "_addOEMApplicationForApplicationRecordIfNeeded:"
- "_addVehicle:"
- "_allowedFormulaIDs"
- "_allowlist"
- "_allowlistPayload"
- "_applicationFinder"
- "_applicationForVehicle:"
- "_applicationRecord"
- "_applicationRecordForBundleIdentifier:"
- "_applicationRecordForVehicle:"
- "_applications"
- "_batteryCharge"
- "_bluetoothIdentifier"
- "_callbackQueue"
- "_canBeUpdatedFromState:"
- "_chargeStreamingConnection"
- "_chargeStreamingDelegate"
- "_checkAvailableAccessoriesAndAttachIfNeeded"
- "_cleanUp"
- "_clearActiveVehicleIdentifierIfNeeded:"
- "_clients"
- "_clientsIsolater"
- "_closeConnection"
- "_complete"
- "_completion"
- "_completionLock"
- "_connection"
- "_connectionErrorHandlers"
- "_connectionQueue"
- "_connectionTimeoutHandlers"
- "_connectionWithIntent:"
- "_createChargeStreamingConnectionIfNeededForVehicle:"
- "_currentStatePassesEVRoutingRequirements"
- "_currentVehicle"
- "_dataCoordinator"
- "_delegate"
- "_delegateQueue"
- "_denylist"
- "_deviceIdentifier"
- "_disabledAppIdentifiers"
- "_enabled"
- "_endContinuousUpdates"
- "_executeQueuedCompletionHandlersIfNeeded"
- "_extensionMap"
- "_finishedLoadingVehicles"
- "_firmwareId"
- "_firmwareIds"
- "_forceUpdateWithVehicles:"
- "_garage"
- "_garageCopy"
- "_handlersLock"
- "_has"
- "_hostsVirtualGarage"
- "_identifierForVehicleStateOrigin:"
- "_indexOfVehicleInUnpairedVehicles:"
- "_initializeAllowAndDenylists"
- "_intent"
- "_intentCompletionHandlers"
- "_invalidateRefreshTimer"
- "_isAccessoryTracked:"
- "_isConnectedToCarPlayAccessory"
- "_isConnectedToElectricVehicle"
- "_isConnectedVehicleAllowlisted"
- "_isDataCoordinatorRunning"
- "_isValidConsumptionModelForResponse:"
- "_isolationQueue"
- "_listener"
- "_loadAllOEMVehiclesForApps:completion:"
- "_loadIapVehicles"
- "_lock"
- "_mapsDisplayName"
- "_modelFilter"
- "_modelId"
- "_modelIdAllowlist"
- "_modelIdFromArguments:"
- "_models"
- "_networks"
- "_notifyDelegateWithCurrentVehicle"
- "_notifyObserversGarageDidUpdateVehicles"
- "_observedVehicles"
- "_observer"
- "_observerQueue"
- "_observers"
- "_oemAppForChargeStreamForVehicle:"
- "_onboardVehicle will onboard vehicle %@, but we didn't find exactly one match in unpairedVehicles: %@"
- "_onboardVehicle:"
- "_openConnection"
- "_otherNetworks"
- "_performanceEventLogger"
- "_persister"
- "_persisterHasStaleStateForVehicle:"
- "_powerByConnectorDictionaryFromCar:"
- "_queue"
- "_queuedGetGarageCompletionHandlers"
- "_refreshStateForTrackedVehicles"
- "_reloadNetworks"
- "_removeCarPlayAccessory:"
- "_removeOEMApplicationForBundleIdentifier:"
- "_removeUnpairedIapVehicleIfNeeded"
- "_removeVehicleWithIdentifier:"
- "_removeVehiclesWithUninstalledAppsIfNeeded"
- "_requiredIntents"
- "_saveOnboardingInfoForVehicle:"
- "_saveVehicle:syncAcrossDevices:"
- "_selectVehicleWithIdentifier:"
- "_setDataCoordintorRunning:"
- "_setError"
- "_setLaunchId:"
- "_setQueue:"
- "_setShouldUsePreferredNetworks:forVehicle:"
- "_setVehicleState:"
- "_setupTimerIfNeeded"
- "_setupVirtualGarageHostingIfNeeded"
- "_shouldAssumeFullCharge"
- "_startChargeStreamForVehicle:"
- "_startContinuousUpdatesIfNeeded"
- "_stopChargeStreamForVehicle:"
- "_storage"
- "_suggestedNetworks"
- "_trackedAccessoriesByConnectionId"
- "_unpairVehicle:"
- "_unpairedOEMVehicles"
- "_unpairedVehicles"
- "_updateDataCoordinatorAvailability"
- "_updateFromVehicleInfo:"
- "_updateGarageWithVehicle:syncAcrossDevices:"
- "_updateStateOfChargeForVehicle:syncAcrossDevices:completion:"
- "_updateWithVehicleInfo:"
- "_updateWithVehicleState:"
- "_vehicleByUpdatingUsesPreferredNetworksForRouting:"
- "_vehicleByUpdatingWithVehicle:"
- "_vehicleForCurrentState"
- "_vehicleMatchingVehicle:inArray:"
- "_vehicleStateForCurrentState"
- "_vehicleStateFromResponse:error:"
- "_vehicleStateFromStorage:"
- "_vehicleStateProviderForVehicle:"
- "_vehicleStateRefreshInterval"
- "_vehicleStateRefreshTimer"
- "_vehicleWithIdentifier:"
- "_vehiclesFromListCarsIntentResponse:"
- "_vg_supportsCarPlay"
- "_waitForGarageUpdateIfNecessary:"
- "_workQueue"
- "_years"
- "accessoryUpdateDelegate"
- "accessoryUpdatedWithVehicle:"
- "actionForAddingNewVehicle:withExistingGarageVehicles:andUnpairedVehicles:"
- "activeConnections"
- "activeConnectorAsString:"
- "activeVehicleIdentifier"
- "addConnectionErrorHandler:"
- "addConnectionTimeoutHandler:"
- "addIntentCompletionHandler:"
- "addNetworks:"
- "addObject:"
- "addObserver:"
- "addObserver:selector:name:object:"
- "addTileGroupObserver:queue:"
- "addVehicle:"
- "allKeys"
- "allObjects"
- "allValues"
- "allocWithZone:"
- "allowedFormulaIDs"
- "allowlist"
- "allowsVehicleWithModelId:firmwareId:year:model:"
- "appInfoWithApplicationRecord:"
- "app_bundle_id"
- "appendFormat:"
- "appendString:"
- "applicationIconDidChange:"
- "applicationInstallsArePrioritized:arePaused:"
- "applicationInstallsDidCancel:"
- "applicationInstallsDidChange:"
- "applicationInstallsDidPause:"
- "applicationInstallsDidPrioritize:"
- "applicationInstallsDidResume:"
- "applicationInstallsDidStart:"
- "applicationInstallsDidUpdateIcon:"
- "applicationRecord"
- "applicationStateDidChange:"
- "applications"
- "applicationsDidChangePersonas:"
- "applicationsDidFailToInstall:"
- "applicationsDidFailToUninstall:"
- "applicationsDidInstall:"
- "applicationsDidUninstall:"
- "applicationsDidUpdateMetadata:"
- "applicationsWillInstall:"
- "applicationsWillUninstall:"
- "array"
- "arrayWithCapacity:"
- "arrayWithObjects:count:"
- "autorelease"
- "availableNetworksDidChangeForProvider:"
- "batteryCharge"
- "batteryPercentageBasedOfCapacity"
- "bestStringForCurrentLocale:fallbackToFirstAvailable:"
- "bluetoothIdentifier"
- "boolValue"
- "brandInfoMappings"
- "bundleIdentifier"
- "calendar"
- "callStackSymbols"
- "canUseVirtualGarageXPCService"
- "carIdentifier"
- "carName"
- "cars"
- "caseInsensitiveCompare:"
- "chargePercentRemaining"
- "chargeStreamingDelegate"
- "charging"
- "chargingFormulaArguments"
- "chargingNetworkInfo"
- "class"
- "clearNetworks"
- "closeForClient:"
- "code"
- "color"
- "colorHex"
- "combinedDisplayName"
- "compare:"
- "componentsJoinedByString:"
- "componentsSeparatedByString:"
- "conformsToProtocol:"
- "connectedAccessories"
- "connection"
- "connectionID"
- "consumptionFormulaArguments"
- "containsObject:"
- "copy"
- "copyTo:"
- "copyWithZone:"
- "count"
- "countByEnumeratingWithState:objects:count:"
- "countryCode"
- "countryCodeDidChange:"
- "creationDate"
- "currentCalendar"
- "currentCountrySupportsElectricVehicleRouting"
- "currentLocale"
- "currentVehicleState"
- "d"
- "d16@0:8"
- "data"
- "dataCoordinator:didUpdateUnpairedVehicles:"
- "dataCoordinator:wantsToUpdateVehicle:syncAcrossDevices:"
- "dataCoordinatorDidUpdateInstalledApps:"
- "dataForResourceWithName:fallbackBundle:"
- "dataUsingEncoding:"
- "dataWithJSONObject:options:error:"
- "databaseWasRebuilt"
- "date"
- "dateFromComponents:"
- "dateOfLastStateUpdate"
- "dateOfVehicleIngestion"
- "dateWithTimeIntervalSinceReferenceDate:"
- "dealloc"
- "debugDescription"
- "decodeBoolForKey:"
- "decodeInt64ForKey:"
- "decodeIntegerForKey:"
- "decodeObjectOfClass:forKey:"
- "decodeObjectOfClasses:forKey:"
- "defaultCenter"
- "defaultWorkspace"
- "delegate"
- "denylist"
- "description"
- "deviceIdentifier"
- "deviceIdentifierForVendor"
- "deviceManagementPolicyDidChange:"
- "dictionary"
- "dictionaryRepresentation"
- "dictionaryWithObjects:forKeys:count:"
- "disabledAppIdentifiers"
- "displayName"
- "displayedBatteryPercentage"
- "distanceRemainingElectric"
- "doubleValue"
- "enabled"
- "encodeBool:forKey:"
- "encodeInt64:forKey:"
- "encodeInteger:forKey:"
- "encodeObject:forKey:"
- "encodeWithCoder:"
- "endAllContinuousUpdates"
- "enumerateObjectsUsingBlock:"
- "enumeratorWithOptions:"
- "errorCode"
- "errorWithDomain:code:userInfo:"
- "filteredArrayUsingPredicate:"
- "findOEMApplications"
- "finishOnboardingVehicle:"
- "firmwareRevision"
- "firmware_id"
- "firstObject"
- "forceFetchAllVehicles"
- "garage"
- "garagePersister:wantsToUpdateVehicles:"
- "getBytes:range:"
- "getLatestStateOfVehicle:withReply:"
- "getStateOfChargeForVehicle:completion:"
- "getVehicleInfoData"
- "globalBrandID"
- "globalBrandId"
- "handleIntentWithCompletionHandler:"
- "hasActiveConnector"
- "hasBatteryPercentage"
- "hasChargingArguments"
- "hasConsumptionArguments"
- "hasCurrentBatteryCapacity"
- "hasCurrentEVRange"
- "hasDateOfUpdate"
- "hasError"
- "hasIdentifier"
- "hasIsCharging"
- "hasMaxBatteryCapacity"
- "hasMaxEVRange"
- "hasMinBatteryCapacity"
- "hasName"
- "hasOrigin"
- "hasPairedAppInstallDeviceIdentifier"
- "hasPairedAppInstallSessionIdentifier"
- "hasUsesPreferredNetworksForRouting"
- "hash"
- "headUnit"
- "headUnitBluetoothIdentifier"
- "headUnitIdentifier"
- "headUnitMacAddress"
- "helperPlaceholdersInstalled:"
- "helperPlaceholdersUninstalled:"
- "hostsVirtualGarage"
- "i"
- "i16@0:8"
- "i24@0:8@16"
- "iAP2Identifier"
- "iap2_allowlist"
- "iap2_denylist"
- "iapIdentifier"
- "indexOfObject:"
- "indexOfObjectPassingTest:"
- "init"
- "initWithApplicationFinder:externalAccessory:delegate:"
- "initWithArray:"
- "initWithBrandInfoMapping:"
- "initWithBundleIdentifier:allowPlaceholder:error:"
- "initWithCapacity:"
- "initWithCarName:"
- "initWithChargingNetworkStorage:"
- "initWithClassName:"
- "initWithCoder:"
- "initWithConnection:"
- "initWithData:"
- "initWithData:encoding:"
- "initWithDelegate:"
- "initWithDisplayName:year:manufacturer:model:colorHex:headUnitIdentifier:headUnitBluetoothIdentifier:supportedConnectors:powerByConnector:"
- "initWithDoubleValue:unit:"
- "initWithFormat:"
- "initWithGaragePersister:"
- "initWithIdentifier:applicationRecord:"
- "initWithIdentifier:dateOfUpdate:origin:batteryPercentage:currentEVRange:maxEVRange:minBatteryCapacity:currentBatteryCapacity:maxBatteryCapacity:consumptionArguments:chargingArguments:isCharging:activeConnector:"
- "initWithIdentifier:displayName:year:manufacturer:model:colorHex:licensePlate:lprVehicleType:lprPowerType:"
- "initWithIntent:"
- "initWithKeyOptions:valueOptions:capacity:"
- "initWithLicensePlate:lprVehicleType:lprPowerType:"
- "initWithMachServiceName:"
- "initWithMachServiceName:options:"
- "initWithMapsSyncVehicle:"
- "initWithModelId:firmwareIds:years:models:"
- "initWithObjects:"
- "initWithOptions:capacity:"
- "initWithProtocol:queue:"
- "initWithVehicle:"
- "initWithVocabularyIdentifier:spokenPhrase:pronunciationHint:"
- "installSessionIdentifier"
- "intent"
- "intentResponseDidUpdate:"
- "intentResponseDidUpdate:withSerializedCacheItems:"
- "interfaceWithProtocol:"
- "invalidate"
- "isConnected"
- "isConnectedToAccessoryWithIdentifier:"
- "isConnectedToVehicle:"
- "isEnabled"
- "isEqual:"
- "isEqualToMeasurement:"
- "isEqualToNumber:"
- "isEqualToString:"
- "isGreaterThanMeasurement:"
- "isGreaterThanOrEqualToMeasurement:"
- "isInternalInstall"
- "isKindOfClass:"
- "isLessThanMeasurement:"
- "isLessThanOrEqualToMeasurement:"
- "isMemberOfClass:"
- "isNetworkReachable"
- "isProxy"
- "isPureElectricVehicle"
- "isSignificantlyDifferentFromVehicleState:"
- "isSubsetOfSet:"
- "isSuggesteds"
- "isSuggestedsCount"
- "isSupersetOfEntry:"
- "isoCountryCode"
- "isoCountryCodes"
- "isoCountryCodesCount"
- "kilometers"
- "kilowattHours"
- "lastStateUpdateDate"
- "launchId"
- "length"
- "licensePlate"
- "listCarsWithCompletion:"
- "listener"
- "listener:shouldAcceptNewConnection:"
- "loadVehiclesWithCompletion:"
- "localizedDescription"
- "localizedNames"
- "logPerformanceEvent:"
- "lowercaseString"
- "lprPowerType"
- "lprVehicleType"
- "macAddress"
- "make"
- "manufacturer"
- "maximumBatteryCapacity"
- "maximumDistanceElectric"
- "maximumPowerForChargingConnectorType:"
- "measurementByConvertingToUnit:"
- "mergeFrom:"
- "messageTargetWithErrorReply:"
- "minimumBatteryCapacity"
- "model"
- "modelIdAllowlist"
- "model_id"
- "model_ids"
- "modernManager"
- "mutableCopy"
- "mutableCopyWithZone:"
- "networkUsageChanged:"
- "networksAtIndex:"
- "networksCount"
- "networksType"
- "new"
- "nextObject"
- "numberWithBool:"
- "numberWithDouble:"
- "numberWithUnsignedInteger:"
- "numberWithUnsignedLongLong:"
- "objectAtIndex:"
- "objectAtIndexedSubscript:"
- "objectForKey:"
- "objectForKeyedSubscript:"
- "observeLaunchProhibitedApps"
- "observer"
- "observerQueue"
- "openForClient:"
- "originAsString:"
- "otherNetworks"
- "pairToIapIdentifier:bluetoothIdentifier:"
- "performSelector:"
- "performSelector:withObject:"
- "performSelector:withObject:withObject:"
- "persistedVehicleForVehicle:"
- "pluginsDidInstall:"
- "pluginsDidUninstall:"
- "pluginsWillUninstall:"
- "position"
- "powerByConnector"
- "powerPerConnectors"
- "predicateWithBlock:"
- "preferredChargingNetworks"
- "processIdentifier"
- "q16@0:8"
- "q24@0:8@16"
- "q40@0:8^@16@24@32"
- "readFrom:"
- "registerForLocalNotifications"
- "registerObserver:"
- "release"
- "remoteObjectProxyWithErrorHandler:"
- "removeAllObjects"
- "removeObject:"
- "removeObjectAtIndex:"
- "removeObjectForKey:"
- "removeObjectsInArray:"
- "removeObserver:"
- "removeTileGroupObserver:"
- "removeVehicle:"
- "replaceObjectAtIndex:withObject:"
- "reset"
- "resetStreamingConnection"
- "resourceManifestManager:didChangeActiveTileGroup:fromOldTileGroup:"
- "resourceManifestManagerDidChangeActiveTileGroup:"
- "resourceManifestManagerWillChangeActiveTileGroup:"
- "respondsToSelector:"
- "resume"
- "resumeConnectionWithIntent:connectionTimeoutHandler:connectionErrorHandler:intentCompletionHandler:"
- "resumeWithCompletion:"
- "resumeWithCompletionHandler:"
- "retain"
- "retainCount"
- "saveVehicle:syncAcrossDevices:"
- "scheduledTimerWithTimeInterval:target:selector:userInfo:repeats:"
- "scopedBrandInfos"
- "selectedVehicle"
- "selectedVehicleIdentifier"
- "self"
- "serialNumber"
- "set"
- "setAccessoryUpdateDelegate:"
- "setActiveConnections:"
- "setActiveConnector:"
- "setActiveVehicleIdentifier:"
- "setAllowedFormulaIDs:"
- "setAllowlist:"
- "setApplications:"
- "setBatteryCharge:"
- "setBatteryPercentage:"
- "setChargeStreamingDelegate:"
- "setChargingArguments:"
- "setClasses:forSelector:argumentIndex:ofReply:"
- "setColorHex:"
- "setConnection:"
- "setConsumptionArguments:"
- "setCurrentBatteryCapacity:"
- "setCurrentEVRange:"
- "setDateOfUpdate:"
- "setDelegate:"
- "setDenylist:"
- "setDisabledAppIdentifiers:"
- "setDisplayName:"
- "setEnabled:"
- "setExportedInterface:"
- "setExportedObject:"
- "setGarage:"
- "setHasActiveConnector:"
- "setHasBatteryPercentage:"
- "setHasCurrentBatteryCapacity:"
- "setHasCurrentEVRange:"
- "setHasDateOfUpdate:"
- "setHasIdentifier:"
- "setHasIsCharging:"
- "setHasMaxBatteryCapacity:"
- "setHasMaxEVRange:"
- "setHasMinBatteryCapacity:"
- "setHasOrigin:"
- "setHasUsesPreferredNetworksForRouting:"
- "setHostsVirtualGarage:"
- "setIapIdentifier:"
- "setIdentifier:"
- "setInterruptionHandler:"
- "setInvalidationHandler:"
- "setIsCharging:"
- "setLicensePlate:"
- "setListener:"
- "setLprPowerType:"
- "setLprVehicleType:"
- "setManufacturer:"
- "setMaxBatteryCapacity:"
- "setMaxEVRange:"
- "setMinBatteryCapacity:"
- "setModel:"
- "setModelIdAllowlist:"
- "setName:"
- "setNetworks:"
- "setObject:forKey:"
- "setObject:forKeyedSubscript:"
- "setObserver:"
- "setObserverQueue:"
- "setOrigin:"
- "setPairedAppIdentifier:"
- "setPairedAppInstallDeviceIdentifier:"
- "setPairedAppInstallSessionIdentifier:"
- "setPosition:"
- "setPreferredChargingNetworks:"
- "setRemoteObjectInterface:"
- "setRequestTimeoutInterval:"
- "setRequiresTCC:"
- "setRequiresTrustCheck:"
- "setSelectedVehicleIdentifier:"
- "setShouldAssumeFullCharge:"
- "setSiriIntentsIdentifier:"
- "setSupportedConnectors:"
- "setTimeoutHandler:"
- "setUsesPreferredNetworksForRouting:"
- "setWithArray:"
- "setWithObjects:"
- "setYear:"
- "sharedAccessoryManager"
- "sharedConfiguration"
- "sharedInstance"
- "sharedManager"
- "sharedNetworkObserver"
- "sharedPlatform"
- "sharedServer"
- "sharedService"
- "shouldAssumeFullCharge"
- "shouldUnpairVehicle:"
- "siriIntentsIdentifier"
- "siri_allowlist"
- "sortedArrayUsingComparator:"
- "startContinuousUpdatesForVehicle:"
- "startSendingChargeUpdatesForVehicle:"
- "startSendingUpdatesToObserver:"
- "startWithPersister:"
- "stop"
- "stopSendingChargeUpdatesForVehicle:"
- "stopSendingUpdates"
- "stringByAppendingString:"
- "stringByReplacingOccurrencesOfString:withString:"
- "stringValue"
- "stringWithFormat:"
- "suggestedNetworks"
- "superclass"
- "supportedChargingConnectors"
- "supportedConnectors"
- "supportedIntents"
- "supportsCarPlay"
- "supportsSecureCoding"
- "supportsUSBCarPlay"
- "supportsWirelessCarPlay"
- "tearDownStreamingConnectionForVehicle:"
- "timeIntervalSinceDate:"
- "timeIntervalSinceReferenceDate"
- "unarchivedObjectOfClasses:fromData:error:"
- "underlyingError"
- "unit"
- "unpairVehicle:"
- "unpairedVehicles"
- "unregisterForLocalNotifications"
- "unregisterObserver:"
- "unsignedIntegerValue"
- "userInfo"
- "v16@0:8"
- "v20@0:8B16"
- "v20@0:8i16"
- "v24@0:8@\"<VGOEMAppSOCStreaming>\"16"
- "v24@0:8@\"<VGOEMApplicationFinderUpdates>\"16"
- "v24@0:8@\"GEOResourceManifestManager\"16"
- "v24@0:8@\"INIntentResponse\"16"
- "v24@0:8@\"NSArray\"16"
- "v24@0:8@\"NSCoder\"16"
- "v24@0:8@\"VGDataCoordinator\"16"
- "v24@0:8@\"VGVehicle\"16"
- "v24@0:8@\"VGVehicleState\"16"
- "v24@0:8@\"VGVirtualGarage\"16"
- "v24@0:8@16"
- "v24@0:8@?16"
- "v24@0:8@?<v@?@\"NSArray\"@\"NSError\">16"
- "v24@0:8@?<v@?@\"VGVirtualGarage\"@\"NSError\">16"
- "v24@0:8Q16"
- "v24@0:8d16"
- "v28@0:8@16B24"
- "v28@0:8B16@\"VGVehicle\"20"
- "v28@0:8B16@20"
- "v32@0:8@\"<VGVirtualGaragePersisting>\"16@\"NSArray\"24"
- "v32@0:8@\"INIntentResponse\"16@\"NSSet\"24"
- "v32@0:8@\"NSArray\"16@\"NSArray\"24"
- "v32@0:8@\"VGDataCoordinator\"16@\"NSArray\"24"
- "v32@0:8@\"VGVehicle\"16@?<v@?@\"VGVehicleState\"@\"NSError\">24"
- "v32@0:8@\"VGVirtualGarage\"16@\"NSArray\"24"
- "v32@0:8@16@24"
- "v32@0:8@16@?24"
- "v32@0:8{?=I^v}16"
- "v36@0:8@\"NSString\"16B24@?<v@?@\"VGVehicle\"@\"NSError\">28"
- "v36@0:8@\"VGDataCoordinator\"16@\"VGVehicle\"24B32"
- "v36@0:8@16@24B32"
- "v36@0:8@16B24@?28"
- "v40@0:8@\"GEOResourceManifestManager\"16@\"GEOActiveTileGroup\"24@\"GEOActiveTileGroup\"32"
- "v40@0:8@16@24@32"
- "v48@0:8@16@?24@?32@?40"
- "valueChangedForGEOConfigKey:"
- "valueForEntitlement:"
- "vehicleIdentifier"
- "vehicleInfoInitialData"
- "vehicleStateUpdated:"
- "vehicleWithIdentifier:"
- "vehicles"
- "virtualGarage:didUpdateUnpairedVehicles:"
- "virtualGarageAddVehicle:"
- "virtualGarageDidUpdate:"
- "virtualGarageEndContinuousUpdates"
- "virtualGarageForceFetchAllVehicles"
- "virtualGarageGetGarageWithReply:"
- "virtualGarageGetLatestStateOfVehicleWithIdentifier:syncAcrossDevices:withReply:"
- "virtualGarageGetListOfUnpairedVehiclesWithReply:"
- "virtualGarageOnboardVehicle:"
- "virtualGarageRemoveVehicle:"
- "virtualGarageSaveVehicle:"
- "virtualGarageSelectVehicle:"
- "virtualGarageSetAssumesFullCharge:"
- "virtualGarageSetShouldUsePreferredNetworks:forVehicle:"
- "virtualGarageStartContinuousUpdatesIfNeeded"
- "watts"
- "writeTo:"
- "year"
- "zone"
- "{?=\"batteryPercentage\"b1\"currentBatteryCapacity\"b1\"currentEVRange\"b1\"dateOfUpdate\"b1\"maxBatteryCapacity\"b1\"maxEVRange\"b1\"minBatteryCapacity\"b1\"activeConnector\"b1\"origin\"b1\"isCharging\"b1}"
- "{?=\"identifier\"b1}"
- "{?=\"usesPreferredNetworksForRouting\"b1}"
- "{os_unfair_lock_s=\"_os_unfair_lock_opaque\"I}"

```
