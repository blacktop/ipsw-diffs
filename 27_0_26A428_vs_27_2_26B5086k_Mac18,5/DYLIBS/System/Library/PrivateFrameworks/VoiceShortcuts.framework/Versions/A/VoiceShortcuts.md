## VoiceShortcuts

> `/System/Library/PrivateFrameworks/VoiceShortcuts.framework/Versions/A/VoiceShortcuts`

```diff

-5037.0.17.0.0
-  __TEXT.__text: 0x1385f0
-  __TEXT.__objc_methlist: 0x4c7c
-  __TEXT.__const: 0x64e0
+5110.0.8.0.0
+  __TEXT.__text: 0x12ef68
+  __TEXT.__objc_methlist: 0x49bc
+  __TEXT.__const: 0x6820
   __TEXT.__dlopen_cstrs: 0x25a
-  __TEXT.__constg_swiftt: 0x2138
-  __TEXT.__swift5_typeref: 0x328f
-  __TEXT.__swift5_builtin: 0x140
-  __TEXT.__swift5_reflstr: 0x14d1
-  __TEXT.__swift5_fieldmd: 0x1794
-  __TEXT.__swift5_assocty: 0x5d0
-  __TEXT.__swift5_proto: 0x3e0
-  __TEXT.__swift5_types: 0x1ec
-  __TEXT.__cstring: 0xd963
-  __TEXT.__swift5_capture: 0x2bec
-  __TEXT.__oslogstring: 0xf8b6
-  __TEXT.__swift_as_entry: 0x2f0
-  __TEXT.__swift_as_ret: 0x320
-  __TEXT.__swift_as_cont: 0x720
+  __TEXT.__constg_swiftt: 0x21b0
+  __TEXT.__swift5_typeref: 0x333d
+  __TEXT.__swift5_builtin: 0x154
+  __TEXT.__swift5_reflstr: 0x14e1
+  __TEXT.__swift5_fieldmd: 0x17e8
+  __TEXT.__swift5_assocty: 0x648
+  __TEXT.__swift5_proto: 0x418
+  __TEXT.__swift5_types: 0x1fc
+  __TEXT.__cstring: 0xd240
+  __TEXT.__swift5_capture: 0x2e60
+  __TEXT.__oslogstring: 0xe57d
+  __TEXT.__swift_as_entry: 0x2ec
+  __TEXT.__swift_as_ret: 0x300
+  __TEXT.__swift_as_cont: 0x6d0
   __TEXT.__swift5_protos: 0x4c
   __TEXT.__swift5_mpenum: 0x28
-  __TEXT.__gcc_except_tab: 0x8f0
+  __TEXT.__gcc_except_tab: 0x840
   __TEXT.__ustring: 0xf0
-  __TEXT.__unwind_info: 0x59a8
-  __TEXT.__eh_frame: 0x873c
+  __TEXT.__unwind_info: 0x5898
+  __TEXT.__eh_frame: 0x829c
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0
   __TEXT.__objc_classname: 0x0
   __TEXT.__objc_methname: 0x0
   __TEXT.__objc_methtype: 0x0
-  __DATA_CONST.__const: 0x8c8
-  __DATA_CONST.__objc_classlist: 0x2c0
-  __DATA_CONST.__objc_catlist: 0x100
+  __DATA_CONST.__const: 0x888
+  __DATA_CONST.__objc_classlist: 0x2d0
+  __DATA_CONST.__objc_catlist: 0x78
   __DATA_CONST.__objc_protolist: 0x218
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x42f0
+  __DATA_CONST.__objc_selrefs: 0x3f48
   __DATA_CONST.__objc_protorefs: 0xa8
-  __DATA_CONST.__objc_superrefs: 0x148
+  __DATA_CONST.__objc_superrefs: 0x158
   __DATA_CONST.__objc_arraydata: 0x88
-  __DATA_CONST.__got: 0x1890
-  __AUTH_CONST.__const: 0xb738
-  __AUTH_CONST.__cfstring: 0x3d80
-  __AUTH_CONST.__objc_const: 0x8c50
+  __DATA_CONST.__got: 0x1738
+  __AUTH_CONST.__const: 0xbb98
+  __AUTH_CONST.__cfstring: 0x3d20
+  __AUTH_CONST.__objc_const: 0x89e0
   __AUTH_CONST.__objc_intobj: 0xa8
   __AUTH_CONST.__objc_arrayobj: 0xa8
   __AUTH_CONST.__objc_dictobj: 0x50
-  __AUTH_CONST.__auth_got: 0x1ef0
-  __AUTH.__objc_data: 0x628
-  __AUTH.__data: 0xbe0
-  __DATA.__objc_ivar: 0x31c
-  __DATA.__data: 0x1ef0
+  __AUTH_CONST.__auth_got: 0x1ec0
+  __AUTH.__objc_data: 0x678
+  __AUTH.__data: 0xc90
+  __DATA.__objc_ivar: 0x328
+  __DATA.__data: 0x1f50
   __DATA_DIRTY.__objc_data: 0x13b0
-  __DATA_DIRTY.__data: 0x2d08
+  __DATA_DIRTY.__data: 0x2d18
   __DATA_DIRTY.__crash_info: 0x148
   __DATA_DIRTY.__bss: 0x3200
-  __DATA_DIRTY.__common: 0x30
+  __DATA_DIRTY.__common: 0x38
   - /System/Library/Frameworks/AppIntents.framework/Versions/A/AppIntents
   - /System/Library/Frameworks/ApplicationServices.framework/Versions/A/ApplicationServices
   - /System/Library/Frameworks/CloudKit.framework/Versions/A/CloudKit

   - /usr/lib/swift/libswift_DarwinFoundation3.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  Functions: 7687
-  Symbols:   6714
-  CStrings:  2192
+  Functions: 7664
+  Symbols:   6490
+  CStrings:  2107
 
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
+ GCC_except_table100
+ GCC_except_table101
+ GCC_except_table1018
+ GCC_except_table1037
+ GCC_except_table1043
+ GCC_except_table1065
+ GCC_except_table1136
+ GCC_except_table1144
+ GCC_except_table1148
+ GCC_except_table1173
+ GCC_except_table1201
+ GCC_except_table1219
+ GCC_except_table1224
+ GCC_except_table1227
+ GCC_except_table1229
+ GCC_except_table1257
+ GCC_except_table1261
+ GCC_except_table1275
+ GCC_except_table1281
+ GCC_except_table1293
+ GCC_except_table1299
+ GCC_except_table1320
+ GCC_except_table1324
+ GCC_except_table1342
+ GCC_except_table1346
+ GCC_except_table1360
+ GCC_except_table1362
+ GCC_except_table1366
+ GCC_except_table1386
+ GCC_except_table1389
+ GCC_except_table236
+ GCC_except_table293
+ GCC_except_table378
+ GCC_except_table397
+ GCC_except_table482
+ GCC_except_table561
+ GCC_except_table562
+ GCC_except_table576
+ GCC_except_table587
+ GCC_except_table605
+ GCC_except_table800
+ GCC_except_table922
+ GCC_except_table948
+ GCC_except_table954
+ GCC_except_table956
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
+ _OUTLINED_FUNCTION_245
+ _OUTLINED_FUNCTION_246
+ _OUTLINED_FUNCTION_247
+ _OUTLINED_FUNCTION_248
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
+ __swift_closure_destructor.198Tm
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
- -[WFNotificationTrigger(BiomeContext) publisherWithScheduler:]
- -[WFNotificationTrigger(BiomeContext) shouldFireInResponseToEvent:triggerIdentifier:completion:]
- -[WFPlugInTrigger(BiomeContext) publisherWithScheduler:]
- -[WFPlugInTrigger(BiomeContext) shouldFireInResponseToEvent:triggerIdentifier:completion:]
- -[WFScreenshotTrigger(BiomeContext) publisherWithScheduler:]
- -[WFScreenshotTrigger(BiomeContext) shouldFireInResponseToEvent:triggerIdentifier:completion:]
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
- GCC_except_table1004
- GCC_except_table1010
- GCC_except_table1012
- GCC_except_table1034
- GCC_except_table1075
- GCC_except_table1094
- GCC_except_table1100
- GCC_except_table1122
- GCC_except_table1196
- GCC_except_table1204
- GCC_except_table1206
- GCC_except_table1231
- GCC_except_table1259
- GCC_except_table1277
- GCC_except_table1282
- GCC_except_table1285
- GCC_except_table1287
- GCC_except_table1315
- GCC_except_table1319
- GCC_except_table1333
- GCC_except_table1338
- GCC_except_table1350
- GCC_except_table1356
- GCC_except_table1377
- GCC_except_table1381
- GCC_except_table1399
- GCC_except_table1417
- GCC_except_table1419
- GCC_except_table1423
- GCC_except_table1443
- GCC_except_table1446
- GCC_except_table1460
- GCC_except_table230
- GCC_except_table287
- GCC_except_table307
- GCC_except_table337
- GCC_except_table346
- GCC_except_table433
- GCC_except_table452
- GCC_except_table537
- GCC_except_table545
- GCC_except_table617
- GCC_except_table618
- GCC_except_table632
- GCC_except_table643
- GCC_except_table661
- GCC_except_table856
- GCC_except_table89
- GCC_except_table94
- OBJC_IVAR_$_VCXPCServer._triggerManager
- OBJC_IVAR_$_WFTriggerEventRunner._inProgressEventInfo
- OBJC_IVAR_$_WFTriggerEventRunner._inProgressRunEvent
- OBJC_IVAR_$_WFTriggerEventRunner._inProgressRunnerClient
- OBJC_IVAR_$_WFTriggerEventRunner._inProgressTriggerKey
- _OBJC_CLASS_$_BMCarPlayConnected
- _OBJC_CLASS_$_BMClockAlarm
- _OBJC_CLASS_$_BMContextSyncWalletTransaction
- _OBJC_CLASS_$_BMContextSyncWorkout
- _OBJC_CLASS_$_BMDeviceAirplaneMode
- _OBJC_CLASS_$_BMDeviceBatteryLevel
- _OBJC_CLASS_$_BMDeviceBluetooth
- _OBJC_CLASS_$_BMDeviceDisplayConnected
- _OBJC_CLASS_$_BMDeviceLowPowerMode
- _OBJC_CLASS_$_BMDeviceNFCTag
- _OBJC_CLASS_$_BMDevicePluggedIn
- _OBJC_CLASS_$_BMDeviceWiFi
- _OBJC_CLASS_$_BMHealthWorkout
- _OBJC_CLASS_$_BMNotificationDelivery
- _OBJC_CLASS_$_BMPublisherOptions
- _OBJC_CLASS_$_BMScreenshotsScreenshot
- _OBJC_CLASS_$_BMUserFocusModeComputed
- _OBJC_CLASS_$_BMWalletTransaction
- _OBJC_CLASS_$_ContextSyncClient
- _OBJC_CLASS_$_WFAirplaneModeTrigger
- _OBJC_CLASS_$_WFAlarmTrigger
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
- _OBJC_CLASS_$_WFNotificationTrigger
- _OBJC_CLASS_$_WFPlugInTrigger
- _OBJC_CLASS_$_WFScreenshotTrigger
- _OBJC_CLASS_$_WFStageManagerTrigger
- _OBJC_CLASS_$_WFTimeOfDayTrigger
- _OBJC_CLASS_$_WFTriggerManager
- _OBJC_CLASS_$_WFUserFocusActivityTrigger
- _OBJC_CLASS_$_WFWalletTransactionTrigger
- _OBJC_CLASS_$_WFWifiTrigger
- _OBJC_CLASS_$_WFWorkoutTrigger
- _WFAllWalletTransactionMerchantTypes
- _WFSystemNotificationIdentifierIsForTrigger
- _WFTriggerIDsToDisableNotificationUserInfoFromTriggers
- __OBJC_$_CATEGORY_CLASS_METHODS_WFBluetoothTrigger_$_BiomeContext
- __OBJC_$_CATEGORY_CLASS_METHODS_WFTrigger_$_BiomeContext
- __OBJC_$_CATEGORY_CLASS_METHODS_WFWalletTransactionTrigger_$_BiomeContext
- __OBJC_$_CATEGORY_CLASS_METHODS_WFWorkoutTrigger_$_BiomeContext
- __OBJC_$_CATEGORY_INSTANCE_METHODS_WFAirplaneModeTrigger_$_BiomeContext
- __OBJC_$_CATEGORY_INSTANCE_METHODS_WFAlarmTrigger_$_BiomeContext
- __OBJC_$_CATEGORY_INSTANCE_METHODS_WFBatteryLevelTrigger_$_BiomeConext
- __OBJC_$_CATEGORY_INSTANCE_METHODS_WFBluetoothTrigger_$_BiomeContext
- __OBJC_$_CATEGORY_INSTANCE_METHODS_WFCarPlayConnectionTrigger_$_BiomeContext
- __OBJC_$_CATEGORY_INSTANCE_METHODS_WFExternalDisplayTrigger_$_BiomeContext
- __OBJC_$_CATEGORY_INSTANCE_METHODS_WFLowPowerModeTrigger_$_BiomeContext
- __OBJC_$_CATEGORY_INSTANCE_METHODS_WFNFCTrigger_$_BiomeContext
- __OBJC_$_CATEGORY_INSTANCE_METHODS_WFNotificationTrigger_$_BiomeContext
- __OBJC_$_CATEGORY_INSTANCE_METHODS_WFPlugInTrigger_$_BiomeContext
- __OBJC_$_CATEGORY_INSTANCE_METHODS_WFScreenshotTrigger_$_BiomeContext
- __OBJC_$_CATEGORY_INSTANCE_METHODS_WFStageManagerTrigger_$_BiomeContext
- __OBJC_$_CATEGORY_INSTANCE_METHODS_WFTrigger_$_BiomeContext
- __OBJC_$_CATEGORY_INSTANCE_METHODS_WFUserFocusActivityTrigger_$_BiomeContext
- __OBJC_$_CATEGORY_INSTANCE_METHODS_WFWalletTransactionTrigger_$_BiomeContext
- __OBJC_$_CATEGORY_INSTANCE_METHODS_WFWifiTrigger_$_BiomeContext
- __OBJC_$_CATEGORY_INSTANCE_METHODS_WFWorkoutTrigger_$_BiomeContext
- __OBJC_$_CATEGORY_WFAirplaneModeTrigger_$_BiomeContext
- __OBJC_$_CATEGORY_WFAlarmTrigger_$_BiomeContext
- __OBJC_$_CATEGORY_WFBatteryLevelTrigger_$_BiomeConext
- __OBJC_$_CATEGORY_WFBluetoothTrigger_$_BiomeContext
- __OBJC_$_CATEGORY_WFCarPlayConnectionTrigger_$_BiomeContext
- __OBJC_$_CATEGORY_WFExternalDisplayTrigger_$_BiomeContext
- __OBJC_$_CATEGORY_WFLowPowerModeTrigger_$_BiomeContext
- __OBJC_$_CATEGORY_WFNFCTrigger_$_BiomeContext
- __OBJC_$_CATEGORY_WFNotificationTrigger_$_BiomeContext
- __OBJC_$_CATEGORY_WFPlugInTrigger_$_BiomeContext
- __OBJC_$_CATEGORY_WFScreenshotTrigger_$_BiomeContext
- __OBJC_$_CATEGORY_WFStageManagerTrigger_$_BiomeContext
- __OBJC_$_CATEGORY_WFTrigger_$_BiomeContext
- __OBJC_$_CATEGORY_WFUserFocusActivityTrigger_$_BiomeContext
- __OBJC_$_CATEGORY_WFWalletTransactionTrigger_$_BiomeContext
- __OBJC_$_CATEGORY_WFWifiTrigger_$_BiomeContext
- __OBJC_$_CATEGORY_WFWorkoutTrigger_$_BiomeContext
- ___101-[WFWalletTransactionTrigger(BiomeContext) shouldFireInResponseToEvent:triggerIdentifier:completion:]_block_invoke
- ___103-[WFBluetoothTrigger(BiomeContext) getPreviousStateWithDeviceName:currentStateEvent:completionHandler:]_block_invoke
- ___103-[WFBluetoothTrigger(BiomeContext) getPreviousStateWithDeviceName:currentStateEvent:completionHandler:]_block_invoke_2
- ___56-[VCMetricSubmitter numberOfPersonalAutomationsEnabled:]_block_invoke
- ___87-[VCVoiceShortcutManagerAccessWrapper resetAutomationConfirmationStatusWithCompletion:]_block_invoke
- ___93-[WFBluetoothTrigger(BiomeContext) shouldFireInResponseToEvent:triggerIdentifier:completion:]_block_invoke
- ___95-[WFBatteryLevelTrigger(BiomeConext) shouldFireInResponseToEvent:triggerIdentifier:completion:]_block_invoke
- ___95-[WFBatteryLevelTrigger(BiomeConext) shouldFireInResponseToEvent:triggerIdentifier:completion:]_block_invoke_2
- ___block_descriptor_32_e23_v16?0"BPSCompletion"8l
- ___block_descriptor_32_e40_v24?0"BPSCompletion"8"<BMBookmark>"16l
- ___block_descriptor_40_e8_32r_e22_v16?0"BMStoreEvent"8l
- ___block_descriptor_40_e8_32r_e36_v32?0"WFConfiguredTrigger"8Q16^B24l
- ___block_descriptor_48_e8_32s40s_e36_v32?0"WFConfiguredTrigger"8Q16^B24l
- ___block_descriptor_56_e8_32s40s48bs_e27_v16?0"BMDeviceBluetooth"8l
- ___block_descriptor_64_e8_32s40s48r56r_e22_B16?0"BMStoreEvent"8l
- ___block_descriptor_67_e8_32s40bs48r56r_e22_v16?0"NSDictionary"8l
- ___kCFBooleanFalse
- ___swift_project_boxed_opaque_existential_0Tm
- __swift_closure_destructor.155Tm
- _associated conformance 14VoiceShortcuts22TriggerConversionErrorO10Foundation09LocalizedE0AAs0E0
- _objc_msgSend$AirplaneMode
- _objc_msgSend$Alarm
- _objc_msgSend$BatteryLevel
- _objc_msgSend$Bluetooth
- _objc_msgSend$CarPlay
- _objc_msgSend$Clock
- _objc_msgSend$ComputedMode
- _objc_msgSend$Connected
- _objc_msgSend$ContextSync
- _objc_msgSend$DSLPublisher
- _objc_msgSend$DSLPublisherWithUseCase:
- _objc_msgSend$Delivery
- _objc_msgSend$Device
- _objc_msgSend$DisplayConnected
- _objc_msgSend$ExternalDisplay
- _objc_msgSend$Health
- _objc_msgSend$LowPowerMode
- _objc_msgSend$NFCTag
- _objc_msgSend$Notification
- _objc_msgSend$PluggedIn
- _objc_msgSend$Power
- _objc_msgSend$SSID
- _objc_msgSend$Screenshot
- _objc_msgSend$Screenshots
- _objc_msgSend$StageManager
- _objc_msgSend$Toggled
- _objc_msgSend$Transaction
- _objc_msgSend$UserFocus
- _objc_msgSend$Wallet
- _objc_msgSend$WalletTransaction
- _objc_msgSend$WiFi
- _objc_msgSend$WindowManager
- _objc_msgSend$Wireless
- _objc_msgSend$Workout
- _objc_msgSend$activitySemanticIdentifier
- _objc_msgSend$activityType
- _objc_msgSend$activityUniqueIdentifier
- _objc_msgSend$alarmEventForCurrentAlarmState
- _objc_msgSend$alarmIDs
- _objc_msgSend$alarmState
- _objc_msgSend$alarmType
- _objc_msgSend$allConfiguredTriggers
- _objc_msgSend$associateWorkflowToTriggerID:deletingExistingReference:notifyDaemon:workflowReference:completion:
- _objc_msgSend$batteryPercentage
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
- _objc_msgSend$eventDisplayFilter
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
- _objc_msgSend$isDeleted
- _objc_msgSend$isEnabled
- _objc_msgSend$isFirstPartyDonation
- _objc_msgSend$isPassIdentifierValid:
- _objc_msgSend$isSleepAlarm
- _objc_msgSend$latestRunEventForLegacyTriggerIdentifier:
- _objc_msgSend$level
- _objc_msgSend$merchant
- _objc_msgSend$merchantType
- _objc_msgSend$onDisable
- _objc_msgSend$onEnable
- _objc_msgSend$onEnd
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
- _objc_msgSend$semanticModeIdentifier
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
- _objc_msgSend$sinkWithCompletion:receiveInput:
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
- _objc_msgSend$uniqueId
- _objc_msgSend$unregisterForUpdates:withIdentifier:forDeviceTypes:withError:
- _objc_msgSend$updateNotificationLevel:forConfiguredTrigger:error:
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
- "%s Could not fetch transaction for wallet transaction event, ignoring merchant filtering."
- "%s Could not reset automation confirmation status for trigger: %{public}@ with error: %{public}@"
- "%s Event device not contained in trigger devices, not firing"
- "%s Event in stream was not of BMDeviceBluetooth event type."
- "%s Event received was not screenshot event, not firing."
- "%s Failed register for updates from context sync client with error: %@"
- "%s Failed to register workout for updates from context sync client with error: %@"
- "%s Failed to unregister client with error: %@"
- "%s Failed to unregister workout client with error: %@"
- "%s Found last event for device name: %@"
- "%s Found remote event converting to BMWalletTransaction"
- "%s Found remote workout event from ContextSync"
- "%s Hit the event we are recieved for the trigger, which has timestamp %f"
- "%s Ignoring filtered display event with UUID: %@"
- "%s Ignoring third-party workout event; not firing."
- "%s Invalid case hit for WFBatteryLevelTrigger"
- "%s Last Bluetooth connection event was same as current event, not firing"
- "%s No Airplane Mode event received for trigger; not firing."
- "%s No Alarm event received for trigger; not firing."
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
- "%s Received event from screenshot stream: %@"
- "%s Received wallet transaction event %@ for trigger. pass unique id: %@; transactionType: %lu"
- "%s Received workout event for trigger. activityType: %@; eventType: %d; trigger onStart: %d, onEnd: %d"
- "%s Recieved alarm event"
- "%s Specific workout type matching unavailable without HealthKit; not firing."
- "%s Successfully registered for updates with context sync client"
- "%s Successfully registered workout for updates with context sync client"
- "%s Successfully unregistered from context sync client"
- "%s Successfully unregistered workout from context sync client"
- "%s Trigger set with onConnect: %d and onDisconnect: %d and event had starting: %d, not firing"
- "%s Walking back through bluetooth event with timestamp %f"
- "%s 🤖 - No Notification event received for trigger; not firing."
- "%s 🤖 - Notification trigger not firing: no app configured"
- "%s 🤖 - Received possible notification event"
- "%s 🤖 - Skipping notification produced by this trigger (%{public}@); not firing."
- "%s 🤖 Started workflow run for trigger (%{public}@) of type (%{public}@), workflow id (%{public}@), presentationMode (%{public}ld), needsConfirmation (%{public}d)"
- "+[WFWalletTransactionTrigger(BiomeContext) registerContextSyncClient]"
- "+[WFWalletTransactionTrigger(BiomeContext) unregisterContextSyncClient]"
- "+[WFWorkoutTrigger(BiomeContext) registerContextSyncClient]"
- "+[WFWorkoutTrigger(BiomeContext) unregisterContextSyncClient]"
- "-[VCVoiceShortcutManagerAccessWrapper resetAutomationConfirmationStatusWithCompletion:]_block_invoke"
- "-[WFAirplaneModeTrigger(BiomeContext) shouldFireInResponseToEvent:triggerIdentifier:completion:]"
- "-[WFAlarmTrigger(BiomeContext) shouldFireInResponseToEvent:triggerIdentifier:completion:]"
- "-[WFBatteryLevelTrigger(BiomeConext) shouldFireInResponseToEvent:triggerIdentifier:completion:]"
- "-[WFBluetoothTrigger(BiomeContext) getPreviousStateWithDeviceName:currentStateEvent:completionHandler:]_block_invoke"
- "-[WFBluetoothTrigger(BiomeContext) getPreviousStateWithDeviceName:currentStateEvent:completionHandler:]_block_invoke_2"
- "-[WFBluetoothTrigger(BiomeContext) shouldFireInResponseToEvent:triggerIdentifier:completion:]"
- "-[WFBluetoothTrigger(BiomeContext) shouldFireInResponseToEvent:triggerIdentifier:completion:]_block_invoke"
- "-[WFCarPlayConnectionTrigger(BiomeContext) shouldFireInResponseToEvent:triggerIdentifier:completion:]"
- "-[WFExternalDisplayTrigger(BiomeContext) shouldFireInResponseToEvent:triggerIdentifier:completion:]"
- "-[WFNFCTrigger(BiomeContext) shouldFireInResponseToEvent:triggerIdentifier:completion:]"
- "-[WFNotificationTrigger(BiomeContext) shouldFireInResponseToEvent:triggerIdentifier:completion:]"
- "-[WFScreenshotTrigger(BiomeContext) shouldFireInResponseToEvent:triggerIdentifier:completion:]"
- "-[WFTrigger shouldFireInResponseToEvent:] must be overridden"
- "-[WFTriggerEventRunner workflowRunnerClient:didFinishRunningWorkflowWithOutput:error:cancelled:]"
- "-[WFUserFocusActivityTrigger(BiomeContext) shouldFireInResponseToEvent:triggerIdentifier:completion:]"
- "-[WFWalletTransactionTrigger(BiomeContext) shouldFireInResponseToEvent:triggerIdentifier:completion:]"
- "-[WFWalletTransactionTrigger(BiomeContext) shouldFireInResponseToEvent:triggerIdentifier:completion:]_block_invoke"
- "-[WFWifiTrigger(BiomeContext) shouldFireInResponseToEvent:triggerIdentifier:completion:]"
- "-[WFWorkoutTrigger(BiomeContext) publisherWithScheduler:]"
- "-[WFWorkoutTrigger(BiomeContext) remotePublisherWithScheduler:]"
- "-[WFWorkoutTrigger(BiomeContext) shouldFireInResponseToEvent:triggerIdentifier:completion:]"
- "1"
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
- "SHORTCUTS_AUTOMATIONS"
- "Skipping template parameter override for %{public}s: invalid action index %{public}ld or missing parameters"
- "Unsupported trigger type"
- "VoiceShortcuts/Trigger+Convertible.swift"
- "transaction"
- "unfinished attempts in run history"
- "v16@?0@\"BMDeviceBluetooth\"8"
- "v16@?0@\"BMStoreEvent\"8"
- "v16@?0@\"BPSCompletion\"8"
- "v24@?0@\"BPSCompletion\"8@\"<BMBookmark>\"16"
- "v32@?0@\"WFConfiguredTrigger\"8Q16^B24"
```
