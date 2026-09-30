## VoiceShortcuts

> `/System/iOSSupport/System/Library/PrivateFrameworks/VoiceShortcuts.framework/Versions/A/VoiceShortcuts`

```diff

-5037.0.17.0.0
-  __TEXT.__text: 0x11bdbc
-  __TEXT.__objc_methlist: 0x4974
-  __TEXT.__const: 0x5fc8
+5110.0.8.0.0
+  __TEXT.__text: 0x112cf4
+  __TEXT.__objc_methlist: 0x46b4
+  __TEXT.__const: 0x6308
   __TEXT.__dlopen_cstrs: 0x12d
-  __TEXT.__constg_swiftt: 0x1ee0
-  __TEXT.__swift5_typeref: 0x2f7f
-  __TEXT.__swift5_builtin: 0x12c
-  __TEXT.__swift5_reflstr: 0x12e1
-  __TEXT.__swift5_fieldmd: 0x1634
-  __TEXT.__swift5_assocty: 0x5a0
-  __TEXT.__swift5_proto: 0x3b0
-  __TEXT.__swift5_types: 0x1d0
-  __TEXT.__cstring: 0xcc6f
-  __TEXT.__swift5_capture: 0x2960
-  __TEXT.__oslogstring: 0xdba5
-  __TEXT.__swift_as_entry: 0x2c8
-  __TEXT.__swift_as_ret: 0x314
-  __TEXT.__swift_as_cont: 0x6f4
+  __TEXT.__constg_swiftt: 0x1f58
+  __TEXT.__swift5_typeref: 0x3021
+  __TEXT.__swift5_builtin: 0x140
+  __TEXT.__swift5_reflstr: 0x1301
+  __TEXT.__swift5_fieldmd: 0x1688
+  __TEXT.__swift5_assocty: 0x618
+  __TEXT.__swift5_proto: 0x3e8
+  __TEXT.__swift5_types: 0x1e0
+  __TEXT.__cstring: 0xc3cd
+  __TEXT.__swift5_capture: 0x2bd4
+  __TEXT.__oslogstring: 0xc876
+  __TEXT.__swift_as_entry: 0x2c4
+  __TEXT.__swift_as_ret: 0x2f4
+  __TEXT.__swift_as_cont: 0x6a4
   __TEXT.__swift5_protos: 0x4c
   __TEXT.__swift5_mpenum: 0x28
-  __TEXT.__gcc_except_tab: 0x848
+  __TEXT.__gcc_except_tab: 0x760
   __TEXT.__ustring: 0x44
-  __TEXT.__unwind_info: 0x54a8
-  __TEXT.__eh_frame: 0x8498
+  __TEXT.__unwind_info: 0x5398
+  __TEXT.__eh_frame: 0x7fd8
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0
   __TEXT.__objc_classname: 0x0
   __TEXT.__objc_methname: 0x0
   __TEXT.__objc_methtype: 0x0
-  __DATA_CONST.__const: 0x1bf8
-  __DATA_CONST.__objc_classlist: 0x280
-  __DATA_CONST.__objc_catlist: 0xf0
+  __DATA_CONST.__const: 0x1aa0
+  __DATA_CONST.__objc_classlist: 0x290
+  __DATA_CONST.__objc_catlist: 0x68
   __DATA_CONST.__objc_protolist: 0x230
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x4058
+  __DATA_CONST.__objc_selrefs: 0x3c48
   __DATA_CONST.__objc_protorefs: 0xb0
-  __DATA_CONST.__objc_superrefs: 0x130
+  __DATA_CONST.__objc_superrefs: 0x140
   __DATA_CONST.__objc_arraydata: 0x40
-  __DATA_CONST.__got: 0x1700
-  __AUTH_CONST.__const: 0x9688
-  __AUTH_CONST.__cfstring: 0x38c0
-  __AUTH_CONST.__objc_const: 0x8410
+  __DATA_CONST.__got: 0x15a8
+  __AUTH_CONST.__const: 0x9be8
+  __AUTH_CONST.__cfstring: 0x37e0
+  __AUTH_CONST.__objc_const: 0x81a0
   __AUTH_CONST.__objc_intobj: 0xa8
   __AUTH_CONST.__objc_dictobj: 0x28
-  __AUTH_CONST.__auth_got: 0x1ee8
-  __AUTH.__objc_data: 0x458
-  __AUTH.__data: 0xba0
-  __DATA.__objc_ivar: 0x2f4
-  __DATA.__data: 0x1fc0
+  __AUTH_CONST.__auth_got: 0x1eb8
+  __AUTH.__objc_data: 0x4a8
+  __AUTH.__data: 0xc50
+  __DATA.__objc_ivar: 0x300
+  __DATA.__data: 0x2020
   __DATA_DIRTY.__objc_data: 0x1270
-  __DATA_DIRTY.__data: 0x2730
+  __DATA_DIRTY.__data: 0x26f0
   __DATA_DIRTY.__crash_info: 0x148
   __DATA_DIRTY.__bss: 0x2f80
-  __DATA_DIRTY.__common: 0x30
+  __DATA_DIRTY.__common: 0x38
   - /System/Library/Frameworks/AppIntents.framework/Versions/A/AppIntents
   - /System/Library/Frameworks/CloudKit.framework/Versions/A/CloudKit
   - /System/Library/Frameworks/Combine.framework/Versions/A/Combine

   - /usr/lib/swift/libswift_DarwinFoundation3.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  Functions: 7327
-  Symbols:   6504
-  CStrings:  1988
+  Functions: 7309
+  Symbols:   6261
+  CStrings:  1896
 
Symbols:
+ -[WFTriggerEventRunner completeInFlightRunForTestingWithClient:error:cancelled:]
+ -[WFTriggerEventRunner handleFinishedRunForClient:error:cancelled:]
+ -[WFTriggerEventRunner init]
+ -[WFTriggerEventRunner numberOfRunsInFlight]
+ -[WFTriggerEventRunner registerInFlightRunForTestingWithClient:triggerKey:workflowIdentifier:startDate:]
+ -[WFTriggerEventRunner takeInFlightRunForClient:]
+ -[WFTriggerInFlightRun .cxx_destruct]
+ -[WFTriggerInFlightRun client]
+ -[WFTriggerInFlightRun eventInfo]
+ -[WFTriggerInFlightRun initWithClient:triggerKey:workflowIdentifier:eventInfo:runEvent:startDate:]
+ -[WFTriggerInFlightRun runEvent]
+ -[WFTriggerInFlightRun startDate]
+ -[WFTriggerInFlightRun triggerKey]
+ -[WFTriggerInFlightRun workflowIdentifier]
+ GCC_except_table1043
+ GCC_except_table1049
+ GCC_except_table1051
+ GCC_except_table1101
+ GCC_except_table1137
+ GCC_except_table1141
+ GCC_except_table1155
+ GCC_except_table1160
+ GCC_except_table1170
+ GCC_except_table1176
+ GCC_except_table1190
+ GCC_except_table1194
+ GCC_except_table1212
+ GCC_except_table1216
+ GCC_except_table1232
+ GCC_except_table1257
+ GCC_except_table1271
+ GCC_except_table221
+ GCC_except_table293
+ GCC_except_table356
+ GCC_except_table375
+ GCC_except_table458
+ GCC_except_table539
+ GCC_except_table540
+ GCC_except_table553
+ GCC_except_table564
+ GCC_except_table578
+ GCC_except_table735
+ GCC_except_table859
+ GCC_except_table875
+ GCC_except_table88
+ GCC_except_table881
+ GCC_except_table883
+ GCC_except_table89
+ GCC_except_table901
+ GCC_except_table941
+ GCC_except_table958
+ GCC_except_table962
+ OBJC_IVAR_$_WFTriggerEventRunner._inFlightRuns
+ OBJC_IVAR_$_WFTriggerEventRunner._lock
+ OBJC_IVAR_$_WFTriggerInFlightRun._client
+ OBJC_IVAR_$_WFTriggerInFlightRun._eventInfo
+ OBJC_IVAR_$_WFTriggerInFlightRun._runEvent
+ OBJC_IVAR_$_WFTriggerInFlightRun._startDate
+ OBJC_IVAR_$_WFTriggerInFlightRun._triggerKey
+ OBJC_IVAR_$_WFTriggerInFlightRun._workflowIdentifier
+ _OBJC_CLASS_$_WFTriggerInFlightRun
+ _OBJC_METACLASS_$_WFTriggerInFlightRun
+ _OUTLINED_FUNCTION_351
+ _OUTLINED_FUNCTION_352
+ _OUTLINED_FUNCTION_353
+ _OUTLINED_FUNCTION_354
+ _OUTLINED_FUNCTION_355
+ _OUTLINED_FUNCTION_356
+ _OUTLINED_FUNCTION_357
+ _WFRunnerDefaultMaxRunTimeSeconds
+ _WFWorkflowRunOutcomeForRunError
+ __DATA__TtCC14VoiceShortcuts18WFTriggerRegistrar31ResourceAvailabilityEventSource
+ __INSTANCE_METHODS__TtCC14VoiceShortcuts18WFTriggerRegistrar31ResourceAvailabilityEventSource
+ __IVARS__TtCC14VoiceShortcuts18WFTriggerRegistrar31ResourceAvailabilityEventSource
+ __METACLASS_DATA__TtCC14VoiceShortcuts18WFTriggerRegistrar31ResourceAvailabilityEventSource
+ __OBJC_$_INSTANCE_METHODS_WFTriggerInFlightRun
+ __OBJC_$_INSTANCE_VARIABLES_WFTriggerInFlightRun
+ __OBJC_$_PROP_LIST_WFTriggerInFlightRun
+ __OBJC_CLASS_RO_$_WFTriggerInFlightRun
+ __OBJC_METACLASS_RO_$_WFTriggerInFlightRun
+ __swift_closure_destructor.168Tm
+ _associated conformance 14VoiceShortcuts18WFTriggerRegistrarC31ResourceAvailabilityEventSourceCAA06DaemongH0AA0G0AaFP_AA0iG0
+ _associated conformance 14VoiceShortcuts18WFTriggerRegistrarC42ResourceAvailabilityChangedEventDescriptorVAA06DaemonhI0AA0H0AaFP_AA0jH0
+ _associated conformance 14VoiceShortcuts18WFTriggerRegistrarC42ResourceAvailabilityChangedEventDescriptorVSHAASQ
+ _associated conformance SC11VCErrorCodeLeV10Foundation13CustomNSErrorSCs5Error
+ _associated conformance SC11VCErrorCodeLeV10Foundation21_BridgedStoredNSErrorSC0B0AcDP_8RawValueSYs17FixedWidthInteger
+ _associated conformance SC11VCErrorCodeLeV10Foundation21_BridgedStoredNSErrorSC0B0AcDP_AC06_ErrorB8Protocol
+ _associated conformance SC11VCErrorCodeLeV10Foundation21_BridgedStoredNSErrorSC0B0AcDP_SY
+ _associated conformance SC11VCErrorCodeLeV10Foundation21_BridgedStoredNSErrorSCAC06CustomF0
+ _associated conformance SC11VCErrorCodeLeV10Foundation21_BridgedStoredNSErrorSCAC26_ObjectiveCBridgeableError
+ _associated conformance SC11VCErrorCodeLeV10Foundation21_BridgedStoredNSErrorSCSH
+ _associated conformance SC11VCErrorCodeLeV10Foundation26_ObjectiveCBridgeableErrorSCs0F0
+ _associated conformance SC11VCErrorCodeLeVSHSCSQ
+ _associated conformance So11VCErrorCodeV10Foundation06_ErrorB8ProtocolSC01_D4TypeAcDP_AC21_BridgedStoredNSError
+ _associated conformance So11VCErrorCodeV10Foundation06_ErrorB8ProtocolSCSQ
+ _objc_msgSend$addTarget:selector:
+ _objc_msgSend$client
+ _objc_msgSend$handleFinishedRunForClient:error:cancelled:
+ _objc_msgSend$hasUnifiedAutomationTriggers
+ _objc_msgSend$initWithClient:triggerKey:workflowIdentifier:eventInfo:runEvent:startDate:
+ _objc_msgSend$isTombstoned
+ _objc_msgSend$numberOfEnabledUnifiedAutomationTriggers
+ _objc_msgSend$removeTarget:selector:
+ _objc_msgSend$resetTriggerNotificationLevels
+ _objc_msgSend$runEvent
+ _objc_msgSend$sortedValidRunEventsForTriggerKey:error:
+ _objc_msgSend$startDate
+ _objc_msgSend$takeInFlightRunForClient:
+ _swift_initStaticObject
+ _symbolic SDySo19WFUnifiedTriggerKeyC_____G 11WorkflowKit12WFNewTriggerC
+ _symbolic Say_____G 11WorkflowKit36WFUnifiedAutomationTriggerDescriptorC
+ _symbolic SbIegd_
+ _symbolic _____ 11WorkflowKit31TriggerRegistrationUpdateReasonO
+ _symbolic _____ 11WorkflowKit36WFUnifiedAutomationTriggerDescriptorC
+ _symbolic _____ 14VoiceShortcuts18WFTriggerRegistrarC31ResourceAvailabilityEventSourceC
+ _symbolic _____ 14VoiceShortcuts18WFTriggerRegistrarC32ResourceAvailabilityChangedEventV
+ _symbolic _____ 14VoiceShortcuts18WFTriggerRegistrarC42ResourceAvailabilityChangedEventDescriptorV
+ _symbolic _____ SC11VCErrorCodeLeV
+ _symbolic _____ So11VCErrorCodeV
+ _symbolic _____Iegd_ s5Int32V
+ _symbolic _____Ieghn_ 14VoiceShortcuts18WFTriggerRegistrarC32ResourceAvailabilityChangedEventV
+ _symbolic _____Iegr_ 11WorkflowKit31TriggerRegistrationUpdateReasonO
+ _symbolic _____Iegr_ s5Int32V
+ _symbolic __________Iegnr_ 14VoiceShortcuts18WFTriggerRegistrarC32ResourceAvailabilityChangedEventV AA05EmptyH0V
+ _symbolic _____ySo19WFUnifiedTriggerKeyC_____G s17_NativeDictionaryV 11WorkflowKit12WFNewTriggerC
+ _symbolic _____ySo19WFUnifiedTriggerKeyC_____G s18_DictionaryStorageC 11WorkflowKit12WFNewTriggerC
+ _symbolic _____y______G 14VoiceShortcuts17DaemonEventStreamV0D6SourceC AA18WFTriggerRegistrarC027ResourceAvailabilityChangedD10DescriptorV
+ _symbolic _____y______GSgXw 14VoiceShortcuts17DaemonEventStreamV0D6SourceC AA18WFTriggerRegistrarC027ResourceAvailabilityChangedD10DescriptorV
+ _symbolic _____y_____y______GG 14VoiceShortcuts14EventDebouncerC AA06DaemonC6StreamV0C6SourceC AA18WFTriggerRegistrarC027ResourceAvailabilityChangedC10DescriptorV
+ _symbolic _____y_____y______GGSgXw 14VoiceShortcuts14EventDebouncerC AA06DaemonC6StreamV0C6SourceC AA18WFTriggerRegistrarC027ResourceAvailabilityChangedC10DescriptorV
+ _type_layout_string 14VoiceShortcuts18WFTriggerRegistrarC42ResourceAvailabilityChangedEventDescriptorV
- +[WFBluetoothTrigger(BiomeContext) stream]
- +[WFTrigger(BiomeContext) unregisterContextSyncClient]
- +[WFWalletTransactionTrigger(BiomeContext) registerContextSyncClient]
- +[WFWalletTransactionTrigger(BiomeContext) unregisterContextSyncClient]
- +[WFWorkoutTrigger(BiomeContext) registerContextSyncClient]
- +[WFWorkoutTrigger(BiomeContext) unregisterContextSyncClient]
- -[VCVoiceShortcutManagerAccessWrapper getConfiguredTriggerForTriggerID:completion:]
- -[VCVoiceShortcutManagerAccessWrapper getConfiguredTriggersForWorkflowID:completion:]
- -[VCXPCServer triggerManager]
- -[WFAirplaneModeTrigger(BiomeContext) publisherWithScheduler:]
- -[WFAirplaneModeTrigger(BiomeContext) shouldFireInResponseToEvent:triggerIdentifier:completion:]
- -[WFAlarmTrigger(BiomeContext) alarmEventForCurrentAlarmState]
- -[WFAlarmTrigger(BiomeContext) publisherWithScheduler:]
- -[WFAlarmTrigger(BiomeContext) shouldFireInResponseToEvent:triggerIdentifier:completion:]
- -[WFAppInFocusTrigger(BiomeContext) publisherWithScheduler:]
- -[WFAppInFocusTrigger(BiomeContext) shouldFireInResponseToEvent:triggerIdentifier:completion:]
- -[WFBatteryLevelTrigger(BiomeConext) publisherWithScheduler:]
- -[WFBatteryLevelTrigger(BiomeConext) shouldFireInResponseToEvent:triggerIdentifier:completion:]
- -[WFBluetoothTrigger(BiomeContext) getPreviousStateWithDeviceName:currentStateEvent:completionHandler:]
- -[WFBluetoothTrigger(BiomeContext) publisherWithScheduler:]
- -[WFBluetoothTrigger(BiomeContext) shouldFireInResponseToEvent:triggerIdentifier:completion:]
- -[WFCarPlayConnectionTrigger(BiomeContext) publisherWithScheduler:]
- -[WFCarPlayConnectionTrigger(BiomeContext) shouldFireInResponseToEvent:triggerIdentifier:completion:]
- -[WFExternalDisplayTrigger(BiomeContext) publisherWithScheduler:]
- -[WFExternalDisplayTrigger(BiomeContext) shouldFireInResponseToEvent:triggerIdentifier:completion:]
- -[WFLowPowerModeTrigger(BiomeContext) publisherWithScheduler:]
- -[WFLowPowerModeTrigger(BiomeContext) shouldFireInResponseToEvent:triggerIdentifier:completion:]
- -[WFNFCTrigger(BiomeContext) publisherWithScheduler:]
- -[WFNFCTrigger(BiomeContext) shouldFireInResponseToEvent:triggerIdentifier:completion:]
- -[WFPlugInTrigger(BiomeContext) publisherWithScheduler:]
- -[WFPlugInTrigger(BiomeContext) shouldFireInResponseToEvent:triggerIdentifier:completion:]
- -[WFSoundRecognitionTrigger(BiomeContext) publisherWithScheduler:]
- -[WFSoundRecognitionTrigger(BiomeContext) shouldFireInResponseToEvent:triggerIdentifier:completion:]
- -[WFStageManagerTrigger(BiomeContext) publisherWithScheduler:]
- -[WFStageManagerTrigger(BiomeContext) shouldFireInResponseToEvent:triggerIdentifier:completion:]
- -[WFTrigger(BiomeContext) hasRemotePublisher]
- -[WFTrigger(BiomeContext) publisherWithScheduler:]
- -[WFTrigger(BiomeContext) remotePublisherWithScheduler:]
- -[WFTrigger(BiomeContext) shouldFireInResponseToEvent:triggerIdentifier:completion:]
- -[WFTriggerEventRunner inProgressEventInfo]
- -[WFTriggerEventRunner inProgressRunEvent]
- -[WFTriggerEventRunner inProgressRunnerClient]
- -[WFTriggerEventRunner inProgressTriggerKey]
- -[WFTriggerEventRunner setInProgressEventInfo:]
- -[WFTriggerEventRunner setInProgressRunEvent:]
- -[WFTriggerEventRunner setInProgressRunnerClient:]
- -[WFTriggerEventRunner setInProgressTriggerKey:]
- -[WFUserFocusActivityTrigger(BiomeContext) publisherWithScheduler:]
- -[WFUserFocusActivityTrigger(BiomeContext) shouldFireInResponseToEvent:triggerIdentifier:completion:]
- -[WFWalletTransactionTrigger(BiomeContext) hasRemotePublisher]
- -[WFWalletTransactionTrigger(BiomeContext) isPassIdentifierValid:]
- -[WFWalletTransactionTrigger(BiomeContext) publisherWithScheduler:]
- -[WFWalletTransactionTrigger(BiomeContext) remotePublisherWithScheduler:]
- -[WFWalletTransactionTrigger(BiomeContext) shouldFireInResponseToEvent:triggerIdentifier:completion:]
- -[WFWalletTransactionTrigger(BiomeContext) transactionIdentifierWithEvent:]
- -[WFWifiTrigger(BiomeContext) publisherWithScheduler:]
- -[WFWifiTrigger(BiomeContext) shouldFireInResponseToEvent:triggerIdentifier:completion:]
- -[WFWorkoutTrigger(BiomeContext) hasRemotePublisher]
- -[WFWorkoutTrigger(BiomeContext) publisherWithScheduler:]
- -[WFWorkoutTrigger(BiomeContext) remotePublisherWithScheduler:]
- -[WFWorkoutTrigger(BiomeContext) shouldFireInResponseToEvent:triggerIdentifier:completion:]
- GCC_except_table1015
- GCC_except_table1019
- GCC_except_table1103
- GCC_except_table1109
- GCC_except_table1111
- GCC_except_table1161
- GCC_except_table1197
- GCC_except_table1201
- GCC_except_table1215
- GCC_except_table1220
- GCC_except_table1250
- GCC_except_table1272
- GCC_except_table1276
- GCC_except_table1290
- GCC_except_table1292
- GCC_except_table1296
- GCC_except_table1314
- GCC_except_table1317
- GCC_except_table1331
- GCC_except_table215
- GCC_except_table286
- GCC_except_table300
- GCC_except_table313
- GCC_except_table321
- GCC_except_table348
- GCC_except_table411
- GCC_except_table430
- GCC_except_table513
- GCC_except_table524
- GCC_except_table595
- GCC_except_table596
- GCC_except_table609
- GCC_except_table620
- GCC_except_table634
- GCC_except_table77
- GCC_except_table791
- GCC_except_table82
- GCC_except_table915
- GCC_except_table931
- GCC_except_table937
- GCC_except_table939
- GCC_except_table957
- GCC_except_table998
- HealthKitLibrary.sLib
- HealthKitLibrary.sOnce
- OBJC_IVAR_$_VCXPCServer._triggerManager
- OBJC_IVAR_$_WFTriggerEventRunner._inProgressEventInfo
- OBJC_IVAR_$_WFTriggerEventRunner._inProgressRunEvent
- OBJC_IVAR_$_WFTriggerEventRunner._inProgressRunnerClient
- OBJC_IVAR_$_WFTriggerEventRunner._inProgressTriggerKey
- _BiomeLibrary
- _OBJC_CLASS_$_BMAccessibilitySoundDetection
- _OBJC_CLASS_$_BMAppInFocus
- _OBJC_CLASS_$_BMCarPlayConnected
- _OBJC_CLASS_$_BMClockAlarm
- _OBJC_CLASS_$_BMContextSyncWalletTransaction
- _OBJC_CLASS_$_BMContextSyncWorkout
- _OBJC_CLASS_$_BMDeviceAirplaneMode
- _OBJC_CLASS_$_BMDeviceBatteryLevel
- _OBJC_CLASS_$_BMDeviceBluetooth
- _OBJC_CLASS_$_BMDeviceLowPowerMode
- _OBJC_CLASS_$_BMDeviceNFCTag
- _OBJC_CLASS_$_BMDevicePluggedIn
- _OBJC_CLASS_$_BMDeviceWiFi
- _OBJC_CLASS_$_BMHealthWorkout
- _OBJC_CLASS_$_BMPublisherOptions
- _OBJC_CLASS_$_BMSpringBoardDisplayConnected
- _OBJC_CLASS_$_BMUserFocusModeComputed
- _OBJC_CLASS_$_BMWalletTransaction
- _OBJC_CLASS_$_ContextSyncClient
- _OBJC_CLASS_$_WFAXSDSettings
- _OBJC_CLASS_$_WFAirplaneModeTrigger
- _OBJC_CLASS_$_WFAlarmTrigger
- _OBJC_CLASS_$_WFAppInFocusTrigger
- _OBJC_CLASS_$_WFArriveLocationTrigger
- _OBJC_CLASS_$_WFBatteryLevelTrigger
- _OBJC_CLASS_$_WFBluetoothTrigger
- _OBJC_CLASS_$_WFCarPlayConnectionTrigger
- _OBJC_CLASS_$_WFConfiguredTrigger
- _OBJC_CLASS_$_WFConfiguredTriggerRecord
- _OBJC_CLASS_$_WFExternalDisplayTrigger
- _OBJC_CLASS_$_WFLeaveLocationTrigger
- _OBJC_CLASS_$_WFLocationTrigger
- _OBJC_CLASS_$_WFLowPowerModeTrigger
- _OBJC_CLASS_$_WFNFCTrigger
- _OBJC_CLASS_$_WFPlugInTrigger
- _OBJC_CLASS_$_WFSoundRecognitionTrigger
- _OBJC_CLASS_$_WFStageManagerTrigger
- _OBJC_CLASS_$_WFTimeOfDayTrigger
- _OBJC_CLASS_$_WFTriggerManager
- _OBJC_CLASS_$_WFUserFocusActivityTrigger
- _OBJC_CLASS_$_WFWalletTransactionTrigger
- _OBJC_CLASS_$_WFWifiTrigger
- _OBJC_CLASS_$_WFWorkoutTrigger
- _WFAllWalletTransactionMerchantTypes
- _WFTriggerIDsToDisableNotificationUserInfoFromTriggers
- __OBJC_$_CATEGORY_CLASS_METHODS_WFBluetoothTrigger_$_BiomeContext
- __OBJC_$_CATEGORY_CLASS_METHODS_WFTrigger_$_BiomeContext
- __OBJC_$_CATEGORY_CLASS_METHODS_WFWalletTransactionTrigger_$_BiomeContext
- __OBJC_$_CATEGORY_CLASS_METHODS_WFWorkoutTrigger_$_BiomeContext
- __OBJC_$_CATEGORY_INSTANCE_METHODS_WFAirplaneModeTrigger_$_BiomeContext
- __OBJC_$_CATEGORY_INSTANCE_METHODS_WFAlarmTrigger_$_BiomeContext
- __OBJC_$_CATEGORY_INSTANCE_METHODS_WFAppInFocusTrigger_$_BiomeContext
- __OBJC_$_CATEGORY_INSTANCE_METHODS_WFBatteryLevelTrigger_$_BiomeConext
- __OBJC_$_CATEGORY_INSTANCE_METHODS_WFBluetoothTrigger_$_BiomeContext
- __OBJC_$_CATEGORY_INSTANCE_METHODS_WFCarPlayConnectionTrigger_$_BiomeContext
- __OBJC_$_CATEGORY_INSTANCE_METHODS_WFExternalDisplayTrigger_$_BiomeContext
- __OBJC_$_CATEGORY_INSTANCE_METHODS_WFLowPowerModeTrigger_$_BiomeContext
- __OBJC_$_CATEGORY_INSTANCE_METHODS_WFNFCTrigger_$_BiomeContext
- __OBJC_$_CATEGORY_INSTANCE_METHODS_WFPlugInTrigger_$_BiomeContext
- __OBJC_$_CATEGORY_INSTANCE_METHODS_WFSoundRecognitionTrigger_$_BiomeContext
- __OBJC_$_CATEGORY_INSTANCE_METHODS_WFStageManagerTrigger_$_BiomeContext
- __OBJC_$_CATEGORY_INSTANCE_METHODS_WFTrigger_$_BiomeContext
- __OBJC_$_CATEGORY_INSTANCE_METHODS_WFUserFocusActivityTrigger_$_BiomeContext
- __OBJC_$_CATEGORY_INSTANCE_METHODS_WFWalletTransactionTrigger_$_BiomeContext
- __OBJC_$_CATEGORY_INSTANCE_METHODS_WFWifiTrigger_$_BiomeContext
- __OBJC_$_CATEGORY_INSTANCE_METHODS_WFWorkoutTrigger_$_BiomeContext
- __OBJC_$_CATEGORY_WFAirplaneModeTrigger_$_BiomeContext
- __OBJC_$_CATEGORY_WFAlarmTrigger_$_BiomeContext
- __OBJC_$_CATEGORY_WFAppInFocusTrigger_$_BiomeContext
- __OBJC_$_CATEGORY_WFBatteryLevelTrigger_$_BiomeConext
- __OBJC_$_CATEGORY_WFBluetoothTrigger_$_BiomeContext
- __OBJC_$_CATEGORY_WFCarPlayConnectionTrigger_$_BiomeContext
- __OBJC_$_CATEGORY_WFExternalDisplayTrigger_$_BiomeContext
- __OBJC_$_CATEGORY_WFLowPowerModeTrigger_$_BiomeContext
- __OBJC_$_CATEGORY_WFNFCTrigger_$_BiomeContext
- __OBJC_$_CATEGORY_WFPlugInTrigger_$_BiomeContext
- __OBJC_$_CATEGORY_WFSoundRecognitionTrigger_$_BiomeContext
- __OBJC_$_CATEGORY_WFStageManagerTrigger_$_BiomeContext
- __OBJC_$_CATEGORY_WFTrigger_$_BiomeContext
- __OBJC_$_CATEGORY_WFUserFocusActivityTrigger_$_BiomeContext
- __OBJC_$_CATEGORY_WFWalletTransactionTrigger_$_BiomeContext
- __OBJC_$_CATEGORY_WFWifiTrigger_$_BiomeContext
- __OBJC_$_CATEGORY_WFWorkoutTrigger_$_BiomeContext
- ___100-[WFSoundRecognitionTrigger(BiomeContext) shouldFireInResponseToEvent:triggerIdentifier:completion:]_block_invoke
- ___101-[WFWalletTransactionTrigger(BiomeContext) shouldFireInResponseToEvent:triggerIdentifier:completion:]_block_invoke
- ___103-[WFBluetoothTrigger(BiomeContext) getPreviousStateWithDeviceName:currentStateEvent:completionHandler:]_block_invoke
- ___103-[WFBluetoothTrigger(BiomeContext) getPreviousStateWithDeviceName:currentStateEvent:completionHandler:]_block_invoke_2
- ___56-[VCMetricSubmitter numberOfPersonalAutomationsEnabled:]_block_invoke
- ___87-[VCVoiceShortcutManagerAccessWrapper resetAutomationConfirmationStatusWithCompletion:]_block_invoke
- ___93-[WFBluetoothTrigger(BiomeContext) shouldFireInResponseToEvent:triggerIdentifier:completion:]_block_invoke
- ___95-[WFBatteryLevelTrigger(BiomeConext) shouldFireInResponseToEvent:triggerIdentifier:completion:]_block_invoke
- ___95-[WFBatteryLevelTrigger(BiomeConext) shouldFireInResponseToEvent:triggerIdentifier:completion:]_block_invoke_2
- ___HealthKitLibrary_block_invoke
- ___block_descriptor_32_e23_v16?0"BPSCompletion"8l
- ___block_descriptor_32_e40_v24?0"BPSCompletion"8"<BMBookmark>"16l
- ___block_descriptor_40_e8_32r_e18_16?0"NSString"8lr32l8
- ___block_descriptor_40_e8_32r_e22_v16?0"BMStoreEvent"8lr32l8
- ___block_descriptor_40_e8_32r_e36_v32?0"WFConfiguredTrigger"8Q16^B24lr32l8
- ___block_descriptor_48_e8_32s40s_e36_v32?0"WFConfiguredTrigger"8Q16^B24ls32l8s40l8
- ___block_descriptor_56_e8_32s40s48bs_e27_v16?0"BMDeviceBluetooth"8ls32l8s48l8s40l8
- ___block_descriptor_64_e8_32s40s48r56r_e22_B16?0"BMStoreEvent"8lr48l8s32l8r56l8s40l8
- ___block_descriptor_67_e8_32s40bs48r56r_e22_v16?0"NSDictionary"8ls40l8r48l8s32l8r56l8
- ___kCFBooleanFalse
- ___swift_project_boxed_opaque_existential_0Tm
- __swift_closure_destructor.146Tm
- _associated conformance 14VoiceShortcuts22TriggerConversionErrorO10Foundation09LocalizedE0AAs0E0
- _init_HKWorkoutActivityNameForActivityType
- _objc_msgSend$Accessibility
- _objc_msgSend$AirplaneMode
- _objc_msgSend$Alarm
- _objc_msgSend$App
- _objc_msgSend$BatteryLevel
- _objc_msgSend$Bluetooth
- _objc_msgSend$CarPlay
- _objc_msgSend$Clock
- _objc_msgSend$ComputedMode
- _objc_msgSend$Connected
- _objc_msgSend$ContextSync
- _objc_msgSend$DSLPublisher
- _objc_msgSend$DSLPublisherWithUseCase:
- _objc_msgSend$Device
- _objc_msgSend$DisplayConnected
- _objc_msgSend$ExternalDisplay
- _objc_msgSend$Health
- _objc_msgSend$InFocus
- _objc_msgSend$LowPowerMode
- _objc_msgSend$NFCTag
- _objc_msgSend$PluggedIn
- _objc_msgSend$Power
- _objc_msgSend$SSID
- _objc_msgSend$SoundDetection
- _objc_msgSend$SpringBoard
- _objc_msgSend$StageManagerMode
- _objc_msgSend$Transaction
- _objc_msgSend$UserFocus
- _objc_msgSend$Wallet
- _objc_msgSend$WalletTransaction
- _objc_msgSend$WiFi
- _objc_msgSend$WindowManagement
- _objc_msgSend$Wireless
- _objc_msgSend$Workout
- _objc_msgSend$activitySemanticIdentifier
- _objc_msgSend$activityType
- _objc_msgSend$activityUniqueIdentifier
- _objc_msgSend$alarmEventForCurrentAlarmState
- _objc_msgSend$alarmIDs
- _objc_msgSend$alarmState
- _objc_msgSend$alarmType
- _objc_msgSend$allBMApplianceTypes
- _objc_msgSend$allConfiguredTriggers
- _objc_msgSend$associateWorkflowToTriggerID:deletingExistingReference:notifyDaemon:workflowReference:completion:
- _objc_msgSend$batteryPercentage
- _objc_msgSend$bmTypeForAXSDSoundDetectionType:
- _objc_msgSend$bundleID
- _objc_msgSend$configuredTriggerForTriggerID:
- _objc_msgSend$configuredTriggersForWorkflowID:
- _objc_msgSend$dateWithTimeIntervalSinceReferenceDate:
- _objc_msgSend$dayOfMonth
- _objc_msgSend$daysOfWeek
- _objc_msgSend$deleteTriggerWithIdentifier:notifyDaemon:completion:
- _objc_msgSend$descriptor
- _objc_msgSend$drivableSinkWithBookmark:completion:shouldContinue:
- _objc_msgSend$endTime
- _objc_msgSend$eventBody
- _objc_msgSend$eventInfoForEvent:completion:
- _objc_msgSend$eventType
- _objc_msgSend$getPreviousStateWithDeviceName:currentStateEvent:completionHandler:
- _objc_msgSend$inProgressEventInfo
- _objc_msgSend$inProgressRunEvent
- _objc_msgSend$inProgressRunnerClient
- _objc_msgSend$inProgressTriggerKey
- _objc_msgSend$initWithClientName:
- _objc_msgSend$initWithPassUniqueID:passLocalizedDescription:transactionType:transactionID:merchantType:poiCategory:
- _objc_msgSend$initWithStartDate:endDate:maxEvents:lastN:reversed:
- _objc_msgSend$isApplianceSoundDetectionType:
- _objc_msgSend$isDeleted
- _objc_msgSend$isEnabled
- _objc_msgSend$isFirstPartyDonation
- _objc_msgSend$isPassIdentifierValid:
- _objc_msgSend$isSleepAlarm
- _objc_msgSend$latestRunEventForLegacyTriggerIdentifier:
- _objc_msgSend$launchReason
- _objc_msgSend$merchant
- _objc_msgSend$merchantType
- _objc_msgSend$onBackground
- _objc_msgSend$onConnect
- _objc_msgSend$onDisable
- _objc_msgSend$onDisconnect
- _objc_msgSend$onEnable
- _objc_msgSend$onEnd
- _objc_msgSend$onFocus
- _objc_msgSend$onStart
- _objc_msgSend$passLocalizedDescription
- _objc_msgSend$passUniqueID
- _objc_msgSend$poiCategory
- _objc_msgSend$publisherWithOptions:
- _objc_msgSend$publisherWithUseCase:options:
- _objc_msgSend$region
- _objc_msgSend$registerContextSyncClient
- _objc_msgSend$registerForUpdates:withIdentifier:shouldWake:forDeviceTypes:withError:
- _objc_msgSend$runAfterConnectionInterruption
- _objc_msgSend$saveNewConfiguredTrigger:notifyDaemon:completion:
- _objc_msgSend$saveNewConfiguredTrigger:workflow:notifyDaemon:completion:
- _objc_msgSend$selectedBundleIdentifiers
- _objc_msgSend$selectedDevices
- _objc_msgSend$selectedMerchantTypes
- _objc_msgSend$selectedMerchants
- _objc_msgSend$selectedNetworks
- _objc_msgSend$selectedPassUniqueIDs
- _objc_msgSend$selectedWorkoutTypes
- _objc_msgSend$selection
- _objc_msgSend$semanticModeIdentifier
- _objc_msgSend$serializedData
- _objc_msgSend$setEditableShortcut:
- _objc_msgSend$setEnabled:
- _objc_msgSend$setEndTime:
- _objc_msgSend$setInProgressEventInfo:
- _objc_msgSend$setInProgressRunEvent:
- _objc_msgSend$setInProgressRunnerClient:
- _objc_msgSend$setInProgressTriggerKey:
- _objc_msgSend$setMode:
- _objc_msgSend$setRegion:
- _objc_msgSend$setShouldPrompt:
- _objc_msgSend$setShouldRecur:
- _objc_msgSend$setStartTime:
- _objc_msgSend$setTime:
- _objc_msgSend$setTriggerData:
- _objc_msgSend$setWithSet:
- _objc_msgSend$sinkWithCompletion:receiveInput:
- _objc_msgSend$soundDetectionType
- _objc_msgSend$soundDetectionTypes
- _objc_msgSend$startTime
- _objc_msgSend$starting
- _objc_msgSend$stream
- _objc_msgSend$stringValue
- _objc_msgSend$subscribeOn:
- _objc_msgSend$tagID
- _objc_msgSend$tagIdentifier
- _objc_msgSend$time
- _objc_msgSend$timestamp
- _objc_msgSend$transactionID
- _objc_msgSend$transactionType
- _objc_msgSend$trigger
- _objc_msgSend$unregisterForUpdates:withIdentifier:forDeviceTypes:withError:
- _objc_msgSend$unsignedIntegerValue
- _objc_msgSend$updateNotificationLevel:forConfiguredTrigger:error:
- _softLink_HKWorkoutActivityNameForActivityType
- _symbolic SccySo19WFConfiguredTriggerC_So19WFWorkflowReferenceCt______pG s5ErrorP
- _symbolic SccySo19WFConfiguredTriggerC______pG s5ErrorP
- _symbolic So16WFTriggerManagerCSgSg
- _symbolic _____ 14VoiceShortcuts22TriggerConversionErrorO
- _symbolic _____ 19VoiceShortcutClient20ActionParameterValueV
- _symbolic _____Sg 19VoiceShortcutClient16ScheduledTriggerV
- _symbolic _____Sg 19VoiceShortcutClient16TimeOfDayTriggerV
- _symbolic _____Sg 19VoiceShortcutClient21LegacyLocationTriggerV9TimeRangeV
- _symbolic ___________t 19VoiceShortcutClient11TriggerTypeO AA013LegacyCodableD6ActionO
- _symbolic _____ySay_____GG 19VoiceShortcutClient0aB17ResponseWithValueO AA16ScheduledTriggerV
- _symbolic _____ySiG s23_ContiguousArrayStorageC
- _symbolic _____y_____G 19VoiceShortcutClient0aB17ResponseWithValueO AA16ScheduledTriggerV
- _symbolic _____y_____G s23_ContiguousArrayStorageC 19VoiceShortcutClient16ScheduledTriggerV
- _symbolic _____y_____SgG 19VoiceShortcutClient0aB17ResponseWithValueO AA16ScheduledTriggerV
- _type_layout_string 14VoiceShortcuts22TriggerConversionErrorO
CStrings:
+ "%s Received completion for an untracked workflow runner client (cancelled: %{public}d, error: %{public}@). Ignoring."
+ "%s This automation is already running, so we can't run this newly-triggered one (%{public}@) (%{public}@)."
+ "%s 🤖 Started workflow run for trigger (%{public}@) of type (%{public}@), workflow id (%{public}@), presentationMode (%{public}ld), needsConfirmation (%{public}d), runs in flight (%{public}lu)"
+ "-[WFTriggerEventRunner handleFinishedRunForClient:error:cancelled:]"
+ "<Trigger Resource Availability Changed Event>"
+ "Create Key Points Action"
+ "Excluding %{public}ld run event(s) dated after now for trigger %{public}@; newest is %{public}s, so the clock moved backwards since they were recorded"
+ "Name for Dark Mode"
+ "Name for Toggle Accessibility Keyboard"
+ "Name for Toggle Alternate Pointer Actions"
+ "Name for Toggle Full Keyboard Access"
+ "Name for Toggle Head Pointer"
+ "Name for Toggle Hover Text action"
+ "Name for Toggle Hover Typing action"
+ "Name for Toggle Live Captions"
+ "Name for Toggle Live Captions action"
+ "Name for Toggle Live Speech"
+ "Name for Toggle Mono Audio"
+ "Name for Toggle Motion Cues"
+ "Name for Toggle Motion Keys action"
+ "Name for Toggle Slow Keys"
+ "Name for Toggle Stage Manager"
+ "Name for Toggle Sticky Keys"
+ "Name for Toggle Switch Control"
+ "Name for Toggle WLAN action used inside China (WAPI-capable devices)"
+ "Name for Toggle Wi-Fi action"
+ "Name for the Call action"
+ "Name for the FaceTime call action"
+ "Name for the Toggle Audio Descriptions action"
+ "Name for the Toggle Background Sounds action"
+ "Not running trigger %{public}s %{public}@, it is rate limited: %{public}@"
+ "TriggerResourceAvailabilityChanged"
+ "startup shortcut sync"
+ "startup stored value sync"
- " when attempting to convert to WFLocationTrigger."
- "$"
- "%s ***WFWorkoutTrigger publisherWithScheduler reached. Candidate for deprecation"
- "%s ***WFWorkoutTrigger registerContextSyncClient reached. Candidate for deprecation"
- "%s ***WFWorkoutTrigger remotePublisherWithScheduler reached. Candidate for deprecation"
- "%s ***WFWorkoutTrigger shouldFireInResponseToEvent reached. Candidate for deprecation"
- "%s ***WFWorkoutTrigger unregisterContextSyncClient reached. Candidate for deprecation"
- "%s Alarm event alarmID string was not valid UUID"
- "%s An automation is already running (%{public}@), so we can't run this newly-triggered one (%{public}@) (%{public}@)."
- "%s App.InFocus: BundleID: %{public}@, isStarting: %d, launchReason: %{public}@"
- "%s App.InFocus: Trigger firing. bundleID: %{public}@, isStarting: %d"
- "%s App.InFocus: Trigger not firing - ignoring launch reason on focus: %{public}@"
- "%s App.InFocus: Trigger not firing: ignoring launch reason on background: %{public}@"
- "%s Could not fetch transaction for wallet transaction event, ignoring merchant filtering."
- "%s Could not reset automation confirmation status for trigger: %{public}@ with error: %{public}@"
- "%s Event device not contained in trigger devices, not firing"
- "%s Event in stream was not of BMDeviceBluetooth event type."
- "%s Failed register for updates from context sync client with error: %@"
- "%s Failed to register workout for updates from context sync client with error: %@"
- "%s Failed to unregister client with error: %@"
- "%s Failed to unregister workout client with error: %@"
- "%s Found last event for device name: %@"
- "%s Found remote event converting to BMWalletTransaction"
- "%s Found remote workout event from ContextSync"
- "%s Hit the event we are recieved for the trigger, which has timestamp %f"
- "%s Ignoring third-party workout event; not firing."
- "%s Invalid case hit for WFBatteryLevelTrigger"
- "%s Last Bluetooth connection event was same as current event, not firing"
- "%s No Airplane Mode event received for trigger; not firing."
- "%s No Alarm event received for trigger; not firing."
- "%s No App.InFocus ezvent received for trigger; not firing."
- "%s No Bluetooth event received for trigger; not firing."
- "%s No CarPlay event received for trigger; not firing."
- "%s No NFC event received for trigger; not firing."
- "%s No WiFi event received for trigger; not firing."
- "%s No display event received for trigger; not firing."
- "%s No wallet transaction event received for trigger; not firing."
- "%s No workout event received for trigger; not firing."
- "%s Processed previous event with different device: %@"
- "%s Received Airplane Mode connection event %@ for trigger with setting"
- "%s Received Bluetooth connection event %@ for trigger with setting; trigger has onConnect %d and onDisconnect %d and event has starting %d"
- "%s Received CarPlay connection event %@ for trigger with setting"
- "%s Received Kettle mode change and the trigger has no semantic mode identifier. The unique identifier didn't match the trigger's unique identifier, not firing"
- "%s Received Kettle mode change, but the semantic mode identifier didn't match the trigger's semantic mode identifier, not firing"
- "%s Received NFC connection event %@ for trigger with setting"
- "%s Received WiFi connection event %@ for trigger with setting"
- "%s Received alarm event %@ for trigger"
- "%s Received change for Kettle mode (%{public}@) — incoming change (uuid: %{public}@, id: %{public}@, starting: %i), trigger (uuid: %{public}@, id: %{public}@, onEnable: %i, onDisable: %i)"
- "%s Received completion for an unexpected workflow runner client (in-progress trigger: %{public}@, cancelled: %{public}d, error: %{public}@). Ignoring."
- "%s Received sound detection event %{public}@ for trigger containing sound detection types %{public}@"
- "%s Received wallet transaction event %@ for trigger. pass unique id: %@; transactionType: %lu"
- "%s Received workout event for trigger. activityType: %@; eventType: %d; trigger onStart: %d, onEnd: %d"
- "%s Recieved alarm event"
- "%s Successfully registered for updates with context sync client"
- "%s Successfully registered workout for updates with context sync client"
- "%s Successfully unregistered from context sync client"
- "%s Successfully unregistered workout from context sync client"
- "%s Trigger set with onConnect: %d and onDisconnect: %d and event had starting: %d, not firing"
- "%s Walking back through bluetooth event with timestamp %f"
- "%s 🤖 Started workflow run for trigger (%{public}@) of type (%{public}@), workflow id (%{public}@), presentationMode (%{public}ld), needsConfirmation (%{public}d)"
- "+[WFWalletTransactionTrigger(BiomeContext) registerContextSyncClient]"
- "+[WFWalletTransactionTrigger(BiomeContext) unregisterContextSyncClient]"
- "+[WFWorkoutTrigger(BiomeContext) registerContextSyncClient]"
- "+[WFWorkoutTrigger(BiomeContext) unregisterContextSyncClient]"
- "-[VCVoiceShortcutManagerAccessWrapper resetAutomationConfirmationStatusWithCompletion:]_block_invoke"
- "-[WFAirplaneModeTrigger(BiomeContext) shouldFireInResponseToEvent:triggerIdentifier:completion:]"
- "-[WFAlarmTrigger(BiomeContext) shouldFireInResponseToEvent:triggerIdentifier:completion:]"
- "-[WFAppInFocusTrigger(BiomeContext) shouldFireInResponseToEvent:triggerIdentifier:completion:]"
- "-[WFBatteryLevelTrigger(BiomeConext) shouldFireInResponseToEvent:triggerIdentifier:completion:]"
- "-[WFBluetoothTrigger(BiomeContext) getPreviousStateWithDeviceName:currentStateEvent:completionHandler:]_block_invoke"
- "-[WFBluetoothTrigger(BiomeContext) getPreviousStateWithDeviceName:currentStateEvent:completionHandler:]_block_invoke_2"
- "-[WFBluetoothTrigger(BiomeContext) shouldFireInResponseToEvent:triggerIdentifier:completion:]"
- "-[WFBluetoothTrigger(BiomeContext) shouldFireInResponseToEvent:triggerIdentifier:completion:]_block_invoke"
- "-[WFCarPlayConnectionTrigger(BiomeContext) shouldFireInResponseToEvent:triggerIdentifier:completion:]"
- "-[WFExternalDisplayTrigger(BiomeContext) shouldFireInResponseToEvent:triggerIdentifier:completion:]"
- "-[WFNFCTrigger(BiomeContext) shouldFireInResponseToEvent:triggerIdentifier:completion:]"
- "-[WFSoundRecognitionTrigger(BiomeContext) shouldFireInResponseToEvent:triggerIdentifier:completion:]"
- "-[WFTrigger shouldFireInResponseToEvent:] must be overridden"
- "-[WFTriggerEventRunner workflowRunnerClient:didFinishRunningWorkflowWithOutput:error:cancelled:]"
- "-[WFUserFocusActivityTrigger(BiomeContext) shouldFireInResponseToEvent:triggerIdentifier:completion:]"
- "-[WFWalletTransactionTrigger(BiomeContext) shouldFireInResponseToEvent:triggerIdentifier:completion:]"
- "-[WFWalletTransactionTrigger(BiomeContext) shouldFireInResponseToEvent:triggerIdentifier:completion:]_block_invoke"
- "-[WFWifiTrigger(BiomeContext) shouldFireInResponseToEvent:triggerIdentifier:completion:]"
- "-[WFWorkoutTrigger(BiomeContext) publisherWithScheduler:]"
- "-[WFWorkoutTrigger(BiomeContext) remotePublisherWithScheduler:]"
- "-[WFWorkoutTrigger(BiomeContext) shouldFireInResponseToEvent:triggerIdentifier:completion:]"
- "/System/Library/Frameworks/HealthKit.framework/HealthKit"
- "/System/iOSSupport/System/Library/Frameworks/HealthKit.framework/HealthKit"
- "1"
- "@16@?0@\"NSString\"8"
- "Attempted to convert WFTimeOfDayTrigger %{public}@ to TimeOfDayTrigger but did not find a time!"
- "Attempted to convert WFTimeOfDayTrigger to TimeOfDayTrigger but did not find a time!"
- "Automation.Trigger"
- "B16@?0@\"BMStoreEvent\"8"
- "Case not handled"
- "Could not convert trigger with reason: "
- "Could not create time of day trigger"
- "Failed to build background running notification user info for %{public}ld trigger(s): database unavailable."
- "Failed to convert location trigger %{public}@: no region found"
- "Failed to convert time-of-day trigger %{public}@: could not create TimeOfDayTrigger"
- "Failed to convert trigger %{public}@: unsupported trigger type"
- "Failed to create WFTriggerManager: database unavailable."
- "Failed to create intent trigger: saveNewConfiguredTrigger returned nil (trigger manager unavailable?)"
- "Failed to create shortcut trigger for workflow %{public}s: saveNewConfiguredTrigger returned nil"
- "Failed to create template trigger for %{public}s: saveNewConfiguredTrigger returned nil"
- "Failed to create template trigger: could not load template %{public}s.wflow"
- "Failed to create trigger: no LN action metadata found for %{public}s/%{public}s"
- "Failed to create trigger: no workflow found for id %{public}s"
- "No region found for location trigger."
- "SBFullScreenSwitcherSceneLiveContentOverlay"
- "SHORTCUTS_AUTOMATIONS"
- "Skipping template parameter override for %{public}s: invalid action index %{public}ld or missing parameters"
- "Unsupported trigger type"
- "VoiceShortcuts/Trigger+Convertible.swift"
- "_HKWorkoutActivityNameForActivityType"
- "com.apple.SpringBoard.backlight.transitionReason.idleTimer"
- "com.apple.SpringBoard.backlight.transitionReason.lockButton"
- "nil"
- "transaction"
- "unfinished attempts in run history"
- "v16@?0@\"BMDeviceBluetooth\"8"
- "v16@?0@\"BMStoreEvent\"8"
- "v16@?0@\"BPSCompletion\"8"
- "v16@?0@\"NSDictionary\"8"
- "v24@?0@\"BPSCompletion\"8@\"<BMBookmark>\"16"
- "v32@?0@\"WFConfiguredTrigger\"8Q16^B24"
```
