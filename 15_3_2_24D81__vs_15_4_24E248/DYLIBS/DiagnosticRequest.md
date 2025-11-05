## DiagnosticRequest

> `/System/Library/PrivateFrameworks/DiagnosticRequest.framework/Versions/A/DiagnosticRequest`

```diff

-383.80.2.0.0
-  __TEXT.__text: 0x11430
+383.101.1.0.0
+  __TEXT.__text: 0x11778
   __TEXT.__auth_stubs: 0x450
-  __TEXT.__objc_methlist: 0x438
+  __TEXT.__objc_methlist: 0x470
   __TEXT.__const: 0xd8
-  __TEXT.__cstring: 0x13fe
+  __TEXT.__cstring: 0x1460
   __TEXT.__gcc_except_tab: 0xac
-  __TEXT.__oslogstring: 0x1f3d
-  __TEXT.__unwind_info: 0x298
+  __TEXT.__oslogstring: 0x1ff2
+  __TEXT.__unwind_info: 0x2a0
   __TEXT.__objc_classname: 0x8c
   __TEXT.__objc_methname: 0xf31
   __TEXT.__objc_methtype: 0x1fb
   __TEXT.__objc_stubs: 0xd80
   __DATA_CONST.__got: 0xf8
-  __DATA_CONST.__const: 0x340
+  __DATA_CONST.__const: 0x348
   __DATA_CONST.__objc_classlist: 0x30
   __DATA_CONST.__objc_protolist: 0x10
   __DATA_CONST.__objc_imageinfo: 0x8

   __DATA_CONST.__objc_superrefs: 0x30
   __AUTH_CONST.__auth_got: 0x238
   __AUTH_CONST.__const: 0xb30
-  __AUTH_CONST.__cfstring: 0xa00
-  __AUTH_CONST.__objc_const: 0x9e0
+  __AUTH_CONST.__cfstring: 0xa60
+  __AUTH_CONST.__objc_const: 0x988
   __AUTH.__objc_data: 0x1e0
   __DATA.__objc_ivar: 0x70
   __DATA.__data: 0xd8

   - /System/Library/Frameworks/Foundation.framework/Versions/C/Foundation
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: F70A0743-25A8-3D38-903E-D907FE2E5722
-  Functions: 328
-  Symbols:   975
-  CStrings:  722
+  UUID: 7D31493F-6C3D-3C4C-9EC2-7CEE7A2AE0B2
+  Functions: 402
+  Symbols:   1050
+  CStrings:  731
 
Symbols:
+ +[DRSubscriptionManager sharedInstance].cold.1
+ +[_DRCConnectionState sharedConnectionState].cold.1
+ +[_DRCTaskingConnectionState sharedConnectionState].cold.1
+ DPLogHandle_AdminError.cold.1
+ DPLogHandle_CKCFUpload.cold.1
+ DPLogHandle_CKCFUploadError.cold.1
+ DPLogHandle_CKConfig.cold.1
+ DPLogHandle_CKConfigError.cold.1
+ DPLogHandle_CKInverness.cold.1
+ DPLogHandle_CKInvernessError.cold.1
+ DPLogHandle_CKRecord.cold.1
+ DPLogHandle_CKRecordError.cold.1
+ DPLogHandle_CKRecordUpload.cold.1
+ DPLogHandle_ClientAPI.cold.1
+ DPLogHandle_ClientAPIError.cold.1
+ DPLogHandle_ClientError.cold.1
+ DPLogHandle_ClientTaskingXPC.cold.1
+ DPLogHandle_ClientTaskingXPCError.cold.1
+ DPLogHandle_ClientXPC.cold.1
+ DPLogHandle_ClientXPCError.cold.1
+ DPLogHandle_ConfigMonitor.cold.1
+ DPLogHandle_ConfigMonitorError.cold.1
+ DPLogHandle_ConfigPersistedStore.cold.1
+ DPLogHandle_ConfigPersistedStoreError.cold.1
+ DPLogHandle_CoreData.cold.1
+ DPLogHandle_CoreDataError.cold.1
+ DPLogHandle_DAReporting.cold.1
+ DPLogHandle_DAReportingError.cold.1
+ DPLogHandle_DPConfig.cold.1
+ DPLogHandle_DPConfigError.cold.1
+ DPLogHandle_DRSConfig.cold.1
+ DPLogHandle_DRSConfigError.cold.1
+ DPLogHandle_DampeningManager.cold.1
+ DPLogHandle_DampeningManagerError.cold.1
+ DPLogHandle_EnableDataGatheringQuery.cold.1
+ DPLogHandle_EnableDataGatheringQueryError.cold.1
+ DPLogHandle_LogManagement.cold.1
+ DPLogHandle_LogManagementError.cold.1
+ DPLogHandle_PermissiveUploadActivity.cold.1
+ DPLogHandle_Request.cold.1
+ DPLogHandle_RequestError.cold.1
+ DPLogHandle_ServiceEventPublisher.cold.1
+ DPLogHandle_ServiceEventPublisherError.cold.1
+ DPLogHandle_ServiceLifecycle.cold.1
+ DPLogHandle_ServiceLifecycleError.cold.1
+ DPLogHandle_ServiceTasking.cold.1
+ DPLogHandle_ServiceTaskingError.cold.1
+ DPLogHandle_ServiceTaskingXPC.cold.1
+ DPLogHandle_ServiceTaskingXPCError.cold.1
+ DPLogHandle_ServiceXPC.cold.1
+ DPLogHandle_ServiceXPCError.cold.1
+ DPLogHandle_SubmitLog.cold.1
+ DPLogHandle_SubmitLogError.cold.1
+ DPLogHandle_SubmitLogToCKContainer.cold.1
+ DPLogHandle_SubmitLogToCKContainerError.cold.1
+ DPLogHandle_SystemProfile.cold.1
+ DPLogHandle_SystemProfileError.cold.1
+ DPLogHandle_Tailspin.cold.1
+ DPLogHandle_TailspinError.cold.1
+ DPLogHandle_TaskingDSTelemetry.cold.1
+ DPLogHandle_TaskingDecisionMaker.cold.1
+ DPLogHandle_TaskingDecisionMakerError.cold.1
+ DPLogHandle_TaskingManager.cold.1
+ DPLogHandle_TaskingManagerError.cold.1
+ DPLogHandle_TaskingMessage.cold.1
+ DPLogHandle_TaskingMessageChannel.cold.1
+ DPLogHandle_TaskingMessageChannelError.cold.1
+ DPLogHandle_TaskingMessageError.cold.1
+ DPLogHandle_Telemetry.cold.1
+ DPLogHandle_UploadSessionDate.cold.1
+ DPLogHandle_UploadSessionDateError.cold.1
+ __block_literal_global.34
+ _doesPassHysteresis.cold.1
+ _hysteresisDict.cold.1
+ _hysteresisQueue.cold.1
+ _kDRTailspinRequestMessageKey_maxMAT
Functions:
~ +[_DRCTaskingConnectionState sharedConnectionState] : 84 -> 68
~ -[_DRCTaskingConnectionState sendMessageWithReplySync:] : 404 -> 408
~ __DPCSendTaskingSystemJSONDataMessage : 940 -> 936
~ __DPCGetConfigStateForUUID : 992 -> 984
~ __DPCMarkConfigUUIDCompletedOrRejected : 1228 -> 1224
~ __DPCRequestTeamIDBroadcast : 968 -> 964
~ -[DRClientLog _checkPath] : 1000 -> 1004
~ _DPLogHandle_ClientError : 84 -> 68
~ _DPLogHandle_AdminError : 84 -> 68
~ _DPLogHandle_ClientXPCError : 84 -> 68
~ _DPLogHandle_ClientXPC : 84 -> 68
~ _DPLogHandle_ClientAPI : 84 -> 68
~ _DPLogHandle_ClientAPIError : 84 -> 68
~ _DPLogHandle_CKRecordError : 84 -> 68
~ _DPLogHandle_CKRecord : 84 -> 68
~ _DPLogHandle_CKRecordUpload : 84 -> 68
~ _DPLogHandle_CKInverness : 84 -> 68
~ _DPLogHandle_CKInvernessError : 84 -> 68
~ _DPLogHandle_CKCFUpload : 84 -> 68
~ _DPLogHandle_CKCFUploadError : 84 -> 68
~ _DPLogHandle_ServiceXPCError : 84 -> 68
~ _DPLogHandle_ServiceXPC : 84 -> 68
~ _DPLogHandle_ServiceLifecycle : 84 -> 68
~ _DPLogHandle_ServiceLifecycleError : 84 -> 68
~ _DPLogHandle_PermissiveUploadActivity : 84 -> 68
~ _DPLogHandle_LogManagement : 84 -> 68
~ _DPLogHandle_LogManagementError : 84 -> 68
~ _DPLogHandle_DAReporting : 84 -> 68
~ _DPLogHandle_DAReportingError : 84 -> 68
~ _DPLogHandle_RequestError : 84 -> 68
~ _DPLogHandle_Request : 84 -> 68
~ _DPLogHandle_TailspinError : 84 -> 68
~ _DPLogHandle_Tailspin : 84 -> 68
~ _DPLogHandle_SubmitLogError : 84 -> 68
~ _DPLogHandle_SubmitLog : 84 -> 68
~ _DPLogHandle_SubmitLogToCKContainerError : 84 -> 68
~ _DPLogHandle_SubmitLogToCKContainer : 84 -> 68
~ _DPLogHandle_EnableDataGatheringQueryError : 84 -> 68
~ _DPLogHandle_EnableDataGatheringQuery : 84 -> 68
~ _DPLogHandle_CoreDataError : 84 -> 68
~ _DPLogHandle_CoreData : 84 -> 68
~ _DPLogHandle_SystemProfileError : 84 -> 68
~ _DPLogHandle_SystemProfile : 84 -> 68
~ _DPLogHandle_DampeningManager : 84 -> 68
~ _DPLogHandle_DampeningManagerError : 84 -> 68
~ _DPLogHandle_TaskingMessage : 84 -> 68
~ _DPLogHandle_TaskingMessageError : 84 -> 68
~ _DPLogHandle_TaskingDecisionMaker : 84 -> 68
~ _DPLogHandle_TaskingDecisionMakerError : 84 -> 68
~ _DPLogHandle_ConfigPersistedStore : 84 -> 68
~ _DPLogHandle_ConfigPersistedStoreError : 84 -> 68
~ _DPLogHandle_TaskingManager : 84 -> 68
~ _DPLogHandle_TaskingManagerError : 84 -> 68
~ _DPLogHandle_TaskingMessageChannel : 84 -> 68
~ _DPLogHandle_TaskingMessageChannelError : 84 -> 68
~ _DPLogHandle_ClientTaskingXPC : 84 -> 68
~ _DPLogHandle_ClientTaskingXPCError : 84 -> 68
~ _DPLogHandle_ConfigMonitor : 84 -> 68
~ _DPLogHandle_ConfigMonitorError : 84 -> 68
~ _DPLogHandle_ServiceTasking : 84 -> 68
~ _DPLogHandle_ServiceTaskingError : 84 -> 68
~ _DPLogHandle_ServiceTaskingXPC : 84 -> 68
~ _DPLogHandle_ServiceTaskingXPCError : 84 -> 68
~ _DPLogHandle_ServiceEventPublisher : 84 -> 68
~ _DPLogHandle_ServiceEventPublisherError : 84 -> 68
~ _DPLogHandle_Telemetry : 84 -> 68
~ _DPLogHandle_TaskingDSTelemetry : 84 -> 68
~ _DPLogHandle_CKConfig : 84 -> 68
~ _DPLogHandle_CKConfigError : 84 -> 68
~ _DPLogHandle_UploadSessionDate : 84 -> 68
~ _DPLogHandle_UploadSessionDateError : 84 -> 68
~ _DPLogHandle_DPConfig : 84 -> 68
~ _DPLogHandle_DPConfigError : 84 -> 68
~ _DPLogHandle_DRSConfig : 84 -> 68
~ _DPLogHandle_DRSConfigError : 84 -> 68
~ __hysteresisQueue : 84 -> 68
~ __doesPassHysteresis : 140 -> 124
~ __tailspinRequestShared : 768 -> 824
~ _DRSubmitLog : 416 -> 420
~ _DRSubmitLogs : 376 -> 388
~ _DRSubmitLogToCKContainer : 1104 -> 1120
~ _DRSubmitRapidLog : 416 -> 420
~ _DRCheckRapidLogSize : 716 -> 720
~ __hysteresisDict : 84 -> 68
~ _DRRequestPassesTimeHysteresis : 320 -> 312
~ ___DRRequestPassesTimeHysteresis_block_invoke : 296 -> 300
~ +[DRSubscriptionManager sharedInstance] : 84 -> 68
~ -[DRSubscriptionManager init] : 424 -> 420
~ -[DRSubscriptionManager _requestSubscriptionToTeamIDStream:] : 968 -> 940
~ -[DRSubscriptionManager _unsubscribeFromStreamWithTeamID:] : 368 -> 364
~ ___61-[DRConfigMonitor _handleCurrentConfig:error:forceBroadcast:]_block_invoke : 1088 -> 1092
~ -[DRConfig initWithBuild:teamID:configDescription:configUUID:receivedDate:startDate:endDate:payload:payloadIsJSON:skipHysteresis:] : 1048 -> 1044
~ -[DRConfig initWithJSONDict:receivedDate:] : 1392 -> 1396
~ _DRConfigStringForState : 40 -> 36
~ +[_DRCConnectionState sharedConnectionState] : 84 -> 68
~ __DPCTailspinRequestMessage : 656 -> 960
~ __DPCSubmitLogToCKContainerRequestMessage : 2204 -> 2196
~ __DPClientBaseMessage : 1520 -> 1724
+ +[_DRCTaskingConnectionState sharedConnectionState].cold.1
CStrings:
+ "Client requested max timestamp less than the min timestamp (requested: %{public}llu current: %{public}llu"
+ "Context dictionary contains a value for reserved private key: '%{public}@'"
+ "Context dictionary is using reserved key'__DPMD__'"
+ "Max timestamp <= min timestamp"
+ "MaxMAT"
+ "__DPMD__"

```
