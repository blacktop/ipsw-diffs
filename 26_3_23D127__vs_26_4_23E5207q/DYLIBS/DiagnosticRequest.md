## DiagnosticRequest

> `/System/Library/PrivateFrameworks/DiagnosticRequest.framework/DiagnosticRequest`

```diff

-411.80.3.0.0
-  __TEXT.__text: 0x10448
-  __TEXT.__auth_stubs: 0x620
+411.100.13.0.0
+  __TEXT.__text: 0x11028
+  __TEXT.__auth_stubs: 0x5b0
   __TEXT.__objc_methlist: 0x470
   __TEXT.__const: 0xd8
   __TEXT.__cstring: 0x14c3
   __TEXT.__gcc_except_tab: 0xac
   __TEXT.__oslogstring: 0x1ff2
-  __TEXT.__unwind_info: 0x290
+  __TEXT.__unwind_info: 0x4d0
   __TEXT.__objc_classname: 0x8c
   __TEXT.__objc_methname: 0xf31
   __TEXT.__objc_methtype: 0x1fb
   __TEXT.__objc_stubs: 0xd80
   __DATA_CONST.__got: 0xf8
-  __DATA_CONST.__const: 0x4c0
+  __DATA_CONST.__const: 0x4b8
   __DATA_CONST.__objc_classlist: 0x30
   __DATA_CONST.__objc_protolist: 0x10
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_selrefs: 0x3d8
   __DATA_CONST.__objc_superrefs: 0x30
-  __AUTH_CONST.__auth_got: 0x320
+  __AUTH_CONST.__auth_got: 0x2e8
   __AUTH_CONST.__const: 0x980
   __AUTH_CONST.__cfstring: 0xa80
   __AUTH_CONST.__objc_const: 0x988

   - /System/Library/Frameworks/Foundation.framework/Foundation
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 90FD327E-F3C7-389D-A79C-07B1E8DDE7B4
+  UUID: 8C91B029-0676-3C3E-B0B1-23718CB3EFFA
   Functions: 392
-  Symbols:   1417
+  Symbols:   1410
   CStrings:  735
 
Symbols:
- _objc_claimAutoreleasedReturnValue
- _objc_retainAutoreleaseReturnValue
- _objc_retain_x1
- _objc_retain_x2
- _objc_retain_x3
- _objc_retain_x4
- _objc_retain_x7
Functions:
~ _DRValidateCKRecordDictionary : 1128 -> 1176
~ +[_DRCTaskingConnectionState sharedConnectionState] : 68 -> 84
~ -[_DRCTaskingConnectionState cleanupState] : 108 -> 112
~ -[_DRCTaskingConnectionState init] : 412 -> 432
~ ___34-[_DRCTaskingConnectionState init]_block_invoke : 520 -> 536
~ __DRCTaskingConnectionStateFinalizer : 84 -> 88
~ ___42-[_DRCTaskingConnectionState sendMessage:]_block_invoke : 128 -> 132
~ -[_DRCTaskingConnectionState sendMessageWithReplySync:] : 380 -> 392
~ __DPCSendTaskingSystemJSONDataMessage : 872 -> 908
~ __replyObjectForRequestMessage : 420 -> 440
~ __DPCGetConfigStateForUUID : 904 -> 936
~ __DPCSendClearTaskingStateMessage : 836 -> 872
~ __DPCMarkConfigUUIDCompletedOrRejected : 1140 -> 1176
~ __DPCRequestTeamIDBroadcast : 900 -> 936
~ __DPCGetCloudChannelConfig : 1336 -> 1392
~ __DPCSetCloudChannelConfig : 1016 -> 1052
~ __DPCResetToDefaultCloudChannelConfig : 844 -> 880
~ -[DRClientLog _checkPath] : 904 -> 960
~ +[DRClientLog sandboxExtensionForLog:transferOwnership:] : 356 -> 368
~ -[DRClientLog initWithPath:transferOwnership:errorOut:] : 508 -> 540
~ __dateFromJSONDict : 356 -> 364
~ _DPLogHandle_ClientError : 68 -> 84
~ _DPLogHandle_AdminError : 68 -> 84
~ _DPLogHandle_ClientXPCError : 68 -> 84
~ _DPLogHandle_ClientXPC : 68 -> 84
~ _DPLogHandle_ClientAPI : 68 -> 84
~ _DPLogHandle_ClientAPIError : 68 -> 84
~ _DPLogHandle_CKRecordError : 68 -> 84
~ _DPLogHandle_CKRecord : 68 -> 84
~ _DPLogHandle_CKRecordUpload : 68 -> 84
~ _DPLogHandle_CKCodeServer : 68 -> 84
~ _DPLogHandle_CKCodeServerError : 68 -> 84
~ _DPLogHandle_CKCFUpload : 68 -> 84
~ _DPLogHandle_CKCFUploadError : 68 -> 84
~ _DPLogHandle_ServiceXPCError : 68 -> 84
~ _DPLogHandle_ServiceXPC : 68 -> 84
~ _DPLogHandle_ServiceLifecycle : 68 -> 84
~ _DPLogHandle_ServiceLifecycleError : 68 -> 84
~ _DPLogHandle_PermissiveUploadActivity : 68 -> 84
~ _DPLogHandle_LogManagement : 68 -> 84
~ _DPLogHandle_LogManagementError : 68 -> 84
~ _DPLogHandle_DAReporting : 68 -> 84
~ _DPLogHandle_DAReportingError : 68 -> 84
~ _DPLogHandle_RequestError : 68 -> 84
~ _DPLogHandle_Request : 68 -> 84
~ _DPLogHandle_TailspinError : 68 -> 84
~ _DPLogHandle_Tailspin : 68 -> 84
~ _DPLogHandle_SubmitLogError : 68 -> 84
~ _DPLogHandle_SubmitLog : 68 -> 84
~ _DPLogHandle_SubmitLogToCKContainerError : 68 -> 84
~ _DPLogHandle_SubmitLogToCKContainer : 68 -> 84
~ _DPLogHandle_EnableDataGatheringQueryError : 68 -> 84
~ _DPLogHandle_EnableDataGatheringQuery : 68 -> 84
~ _DPLogHandle_CoreDataError : 68 -> 84
~ _DPLogHandle_CoreData : 68 -> 84
~ _DPLogHandle_SystemProfileError : 68 -> 84
~ _DPLogHandle_SystemProfile : 68 -> 84
~ _DPLogHandle_DampeningManager : 68 -> 84
~ _DPLogHandle_DampeningManagerError : 68 -> 84
~ _DPLogHandle_TaskingMessage : 68 -> 84
~ _DPLogHandle_TaskingMessageError : 68 -> 84
~ _DPLogHandle_TaskingDecisionMaker : 68 -> 84
~ _DPLogHandle_TaskingDecisionMakerError : 68 -> 84
~ _DPLogHandle_ConfigPersistedStore : 68 -> 84
~ _DPLogHandle_ConfigPersistedStoreError : 68 -> 84
~ _DPLogHandle_TaskingManager : 68 -> 84
~ _DPLogHandle_TaskingManagerError : 68 -> 84
~ _DPLogHandle_TaskingMessageChannel : 68 -> 84
~ _DPLogHandle_TaskingMessageChannelError : 68 -> 84
~ _DPLogHandle_ClientTaskingXPC : 68 -> 84
~ _DPLogHandle_ClientTaskingXPCError : 68 -> 84
~ _DPLogHandle_ConfigMonitor : 68 -> 84
~ _DPLogHandle_ConfigMonitorError : 68 -> 84
~ _DPLogHandle_ServiceTasking : 68 -> 84
~ _DPLogHandle_ServiceTaskingError : 68 -> 84
~ _DPLogHandle_ServiceTaskingXPC : 68 -> 84
~ _DPLogHandle_ServiceTaskingXPCError : 68 -> 84
~ _DPLogHandle_ServiceEventPublisher : 68 -> 84
~ _DPLogHandle_ServiceEventPublisherError : 68 -> 84
~ _DPLogHandle_Telemetry : 68 -> 84
~ _DPLogHandle_TaskingDSTelemetry : 68 -> 84
~ _DPLogHandle_CKConfig : 68 -> 84
~ _DPLogHandle_CKConfigError : 68 -> 84
~ _DPLogHandle_UploadSessionDate : 68 -> 84
~ _DPLogHandle_UploadSessionDateError : 68 -> 84
~ _DPLogHandle_DPConfig : 68 -> 84
~ _DPLogHandle_DPConfigError : 68 -> 84
~ _DPLogHandle_DRSConfig : 68 -> 84
~ _DPLogHandle_DRSConfigError : 68 -> 84
~ __DRRequestResetTailspinHysteresis : 72 -> 76
~ __hysteresisQueue : 68 -> 84
~ __DRRequestPassesTailspinHysteresis : 200 -> 204
~ __tailspinRequestShared : 736 -> 772
~ _DRTailspinRequest : 280 -> 248
~ _DRTailspinRequestWithLogs : 408 -> 396
~ __clientError : 220 -> 228
~ __sendSubmitLogMessageAndHandleReply : 664 -> 684
~ _DRSubmitLog : 364 -> 372
~ _DRSubmitLogs : 340 -> 304
~ _DRSubmitLogToCKContainer : 988 -> 992
~ _DRSubmitRapidLog : 364 -> 372
~ _DRShouldEnableLogGathering : 1220 -> 1260
~ __unexpectedReplyError : 212 -> 220
~ _DRGetAllLogFileURLs : 612 -> 632
~ _DRCheckRapidLogSize : 668 -> 688
~ __DRRequestResetHysteresisDict : 72 -> 76
~ ____DRRequestResetHysteresisDict_block_invoke : 64 -> 68
~ __hysteresisDict : 68 -> 84
~ ___DRRequestPassesTimeHysteresis_block_invoke : 268 -> 284
~ +[DRSubscriptionManager sharedInstance] : 68 -> 84
~ ___39+[DRSubscriptionManager sharedInstance]_block_invoke : 148 -> 152
~ -[DRSubscriptionManager _configFromEvent:teamIdOut:] : 1048 -> 1088
~ -[DRSubscriptionManager _processNewEvent:] : 752 -> 772
~ -[DRSubscriptionManager init] : 384 -> 400
~ -[DRSubscriptionManager _broadcastErrorForTeamID:error:] : 316 -> 320
~ -[DRSubscriptionManager _requestSubscriptionToTeamIDStream:] : 864 -> 892
~ -[DRSubscriptionManager _completeSubscriptionRequestForTeamID:config:event:] : 516 -> 540
~ -[DRSubscriptionManager _hasInitializedSubscriptionForTeamID:cachedConfigOut:errorOut:] : 244 -> 256
~ ___36-[DRSubscriptionManager addMonitor:]_block_invoke : 608 -> 648
~ -[DRSubscriptionManager _unsubscribeFromStreamWithTeamID:] : 324 -> 340
~ ___39-[DRSubscriptionManager removeMonitor:]_block_invoke : 620 -> 664
~ -[DRConfigMonitor startMonitoring] : 88 -> 92
~ -[DRConfigMonitor stopMonitoring] : 88 -> 92
~ ___47-[DRConfigMonitor _notifyClientOfConfig:error:]_block_invoke : 120 -> 128
~ -[DRConfigMonitor _handleCurrentConfig:error:forceBroadcast:] : 232 -> 224
~ ___61-[DRConfigMonitor _handleCurrentConfig:error:forceBroadcast:]_block_invoke : 1000 -> 1052
~ ___55-[DRConfigMonitor _markConfigUUID:isRejected:errorOut:]_block_invoke : 228 -> 236
~ ___53-[DRConfigMonitor currentConfigSnapshotWithErrorOut:]_block_invoke : 76 -> 80
~ -[DRConfigMonitor setCurrentConfig:] : 12 -> 64
~ -[DRConfig encodeWithCoder:] : 452 -> 484
~ -[DRConfig initWithCoder:] : 516 -> 548
~ -[DRConfig initWithBuild:teamID:configDescription:configUUID:receivedDate:startDate:endDate:payload:payloadIsJSON:skipHysteresis:] : 956 -> 972
~ __argIsNonNil : 204 -> 208
~ -[DRConfig isEqualToConfig:] : 644 -> 708
~ -[DRConfig initWithJSONDict:receivedDate:] : 1276 -> 1332
~ -[DRConfig jsonDictRepresentation] : 704 -> 768
~ -[DRConfig setBuild:] : 12 -> 64
~ _DRConfigStringForState : 36 -> 44
~ +[_DRCConnectionState sharedConnectionState] : 68 -> 84
~ -[_DRCConnectionState hasConnection] : 52 -> 56
~ -[_DRCConnectionState init] : 408 -> 428
~ ___27-[_DRCConnectionState init]_block_invoke : 700 -> 724
~ __DRCConnectionStateFinalizer : 68 -> 72
~ ___35-[_DRCConnectionState sendMessage:]_block_invoke : 128 -> 132
~ -[_DRCConnectionState sendMessageWithReplySync:] : 316 -> 320
~ ___48-[_DRCConnectionState sendMessageWithReplySync:]_block_invoke : 76 -> 80
~ -[_DRCConnectionState setConnection:] : 12 -> 64
~ __DPClientXPCSendMessage : 92 -> 96
~ __DPClientXPCSendMessageWithReplySync : 252 -> 264
~ __xpcArrayForStringArray : 316 -> 312
~ __DPCTailspinRequestMessage : 904 -> 920
~ __DPClientLogRequestBaseMessage : 1400 -> 1444
~ __DPCSubmitLogsRequestMessage : 520 -> 524
~ __DPCSubmitLogToCKContainerRequestMessage : 2092 -> 2184
~ __DPCConvertDictionaryToPlistData : 864 -> 884
~ __DPCSubmitRapidLogRequestMessage : 112 -> 116
~ __DPCEnableLogGatheringQueryMessage : 108 -> 112
~ __DPClientBaseMessage : 1596 -> 1628
~ __DPCEnableLogGatheringQueryResultInjectionMessage : 140 -> 144
~ __sendAdminRequestMessage_WaitForReply : 648 -> 680
~ __DRCSetDampeningConfigurationDefaults : 788 -> 776
~ __DPCRefreshDampeningConfiguration : 292 -> 300
~ __DPCInjectEnableLogGatheringQueryResult : 392 -> 388
~ __sendCKConfigMessageAndHandleReply : 724 -> 752
~ __DPCSchedulePermissiveExpeditedUploadActivity : 324 -> 332
~ __DPCCancelPermissiveExpeditedUploadActivity : 296 -> 304
~ __DPCSetIgnoreAutomatedDeviceGroup : 356 -> 364
~ __sendIgnoreADGMessage : 164 -> 176
~ __DPCGetIgnoreAutomatedDeviceGroup : 304 -> 312
~ __DPCGetUploadServiceEnablement : 164 -> 168
~ __xpcError : 216 -> 224
~ __sendUploadServiceEnabledMessage : 248 -> 264
~ __DPCSetUploadServiceEnablement : 224 -> 228
~ __sendAdminRequestMessage_GetReply : 672 -> 704

```
