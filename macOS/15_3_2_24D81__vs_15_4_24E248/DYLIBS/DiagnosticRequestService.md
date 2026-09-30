## DiagnosticRequestService

> `/System/Library/PrivateFrameworks/DiagnosticRequestService.framework/Versions/A/DiagnosticRequestService`

```diff

-383.80.2.0.0
-  __TEXT.__text: 0x74afc
-  __TEXT.__auth_stubs: 0xce0
-  __TEXT.__objc_methlist: 0x48fc
+383.101.1.0.0
+  __TEXT.__text: 0x75ac0
+  __TEXT.__auth_stubs: 0xcd0
+  __TEXT.__objc_methlist: 0x4ca4
   __TEXT.__const: 0xe08
   __TEXT.__gcc_except_tab: 0xbdc
-  __TEXT.__cstring: 0x531f
-  __TEXT.__oslogstring: 0xb387
+  __TEXT.__cstring: 0x53ef
+  __TEXT.__oslogstring: 0xb7ec
   __TEXT.__swift5_typeref: 0x278
   __TEXT.__constg_swiftt: 0x24c
   __TEXT.__swift5_fieldmd: 0x240

   __TEXT.__swift5_capture: 0x20
   __TEXT.__swift5_assocty: 0x30
   __TEXT.__swift5_builtin: 0x14
-  __TEXT.__unwind_info: 0x17b8
-  __TEXT.__eh_frame: 0x420
+  __TEXT.__unwind_info: 0x17b0
+  __TEXT.__eh_frame: 0x4b0
   __TEXT.__objc_classname: 0x975
-  __TEXT.__objc_methname: 0xaf71
-  __TEXT.__objc_methtype: 0x10f7
-  __TEXT.__objc_stubs: 0x8020
-  __DATA_CONST.__got: 0x410
-  __DATA_CONST.__const: 0x648
+  __TEXT.__objc_methname: 0xb233
+  __TEXT.__objc_methtype: 0x110c
+  __TEXT.__objc_stubs: 0x8260
+  __DATA_CONST.__got: 0x418
+  __DATA_CONST.__const: 0x670
   __DATA_CONST.__objc_classlist: 0x2b8
   __DATA_CONST.__objc_catlist: 0x8
   __DATA_CONST.__objc_protolist: 0x38
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x2458
+  __DATA_CONST.__objc_selrefs: 0x25b8
   __DATA_CONST.__objc_superrefs: 0x1f8
-  __AUTH_CONST.__auth_got: 0x680
+  __AUTH_CONST.__auth_got: 0x678
   __AUTH_CONST.__const: 0x1d00
-  __AUTH_CONST.__cfstring: 0x5020
-  __AUTH_CONST.__objc_const: 0x8e18
+  __AUTH_CONST.__cfstring: 0x5160
+  __AUTH_CONST.__objc_const: 0x8a38
   __AUTH_CONST.__objc_intobj: 0x108
   __AUTH_CONST.__objc_doubleobj: 0x20
   __AUTH.__objc_data: 0x1bb0
   __AUTH.__data: 0x3d0
-  __DATA.__objc_ivar: 0x448
-  __DATA.__data: 0x750
+  __DATA.__objc_ivar: 0x454
+  __DATA.__data: 0x770
   __DATA.__objc_stublist: 0x8
   __DATA.__bss: 0x1980
   __DATA.__common: 0x88

   - /usr/lib/swift/libswiftsimd.dylib
   - /usr/lib/swift/libswiftsys_time.dylib
   - /usr/lib/swift/libswiftunistd.dylib
-  UUID: 4708F33D-6418-3235-B05D-7DDD422B11F1
-  Functions: 2414
-  Symbols:   4986
-  CStrings:  4521
+  UUID: 0868015A-0C76-3C59-B668-3E8134D77215
+  Functions: 2519
+  Symbols:   5139
+  CStrings:  4595
 
Symbols:
+ +[DRSCKConfig defaultConfig].cold.1
+ +[DRSCloudChannelConfig _iOSSliceCountDict].cold.1
+ +[DRSCloudChannelConfig _smallPopulationCountDict].cold.1
+ +[DRSCloudKitHelper prodContainerHelper].cold.1
+ +[DRSCloudKitHelper sandboxContainerHelper].cold.1
+ +[DRSDampeningConfiguration pearlAFileBundleConfiguration]
+ +[DRSDampeningConfiguration shareSheetMadRequestTimeoutConfiguration]
+ +[DRSDampeningConfiguration shareSheetTimeoutConfiguration]
+ +[DRSDampeningManager _coreDuetPeopleSuggesterTeamConfiguration:isSeed:isCarrier:platform:]
+ +[DRSDampeningManager _pearlTeamConfiguration:isSeed:isCarrier:platform:]
+ +[DRSEnableDataGatheringQuery leastRecentDateFirstSortDescriptor].cold.1
+ +[DRSEnableDataGatheringQuery mostRecentDateFirstSortDescriptor].cold.1
+ +[DRSRapidCloudKitHelper devHelper].cold.1
+ +[DRSRapidCloudKitHelper prodHelper].cold.1
+ +[DRSRequest leastRecentDateFirstSortDescriptor].cold.1
+ +[DRSRequest maxUploadAttemptCount]
+ +[DRSRequest mostRecentDateFirstSortDescriptor].cold.1
+ +[DRSService serviceIsEnabled].cold.1
+ +[DRSService sharedInstance].cold.1
+ +[DRSSubmitLogToCKContainerRequest(CKRecord_Private) safeguardArchiveZoneID].cold.1
+ +[DRSSubmitLogToCKContainerRequest(CKRecord_Private) xcRecordZoneID].cold.1
+ +[DRSSubmitRapidLogRequest maxUploadAttemptCount]
+ +[DRSSystemProfile sharedInstance].cold.1
+ +[DRSTailspinRequest _shouldScrub].cold.1
+ +[DRSTaskingCloudKitHelper prodContainerHelper].cold.1
+ +[DRSTaskingCloudKitHelper sandboxContainerHelper].cold.1
+ +[DRSTaskingCloudKitHelper taskingDeviceMetadata].cold.1
+ +[DRSTaskingLimitingParameters _customerParameters].cold.1
+ +[DRSTaskingLimitingParameters _disabledParameters].cold.1
+ +[DRSTaskingLimitingParameters _internalParameters].cold.1
+ +[DRSTaskingLimitingParameters _seedParameters].cold.1
+ +[DRSTaskingService serviceIsEnabled].cold.1
+ +[DRSTaskingService sharedInstance].cold.1
+ -[DRSRequest _addContextMetadataKey:value:expectedClass:errorOut:]
+ -[DRSRequest addContextMetadataKey:numberValue:errorOut:]
+ -[DRSRequest addContextMetadataKey:stringValue:errorOut:]
+ -[DRSRequest addHWModelContextMetadata]
+ -[DRSRequest addIsLikelyCarryContextMetadata]
+ -[DRSRequest automatedDeviceGroup]
+ -[DRSRequest hwModel]
+ -[DRSRequest isLikeCarryDevice]
+ -[DRSRequest metadataDictionary]
+ -[DRSService _ckQueueOnly_submitOutstandingEnableDataGatheringQueriesWithTransaction:xpcActivity:ckHelper:followupWorkBlock:].cold.1
+ -[DRSSystemProfile _populateHWModel]
+ -[DRSSystemProfile _populateIsCarry]
+ -[DRSSystemProfile automatedDeviceGroup].cold.1
+ -[DRSSystemProfile hwModel]
+ -[DRSSystemProfile isLikelyCarryGroupNum]
+ -[DRSTailspinRequest maxMAT]
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
+ DRSDeviceMetadata.cold.1
+ DRSProductionContainer.cold.1
+ DRSRapidProdContainer.cold.1
+ DRSRapidSandboxContainer.cold.1
+ DRSRegisterForDeviceUnlockNotification.cold.1
+ DRSSandboxContainer.cold.1
+ DRSWaitForDeviceUnlock.cold.1
+ GCC_except_table100
+ GCC_except_table105
+ GCC_except_table113
+ GCC_except_table118
+ GCC_except_table133
+ GCC_except_table172
+ GCC_except_table183
+ GCC_except_table187
+ GCC_except_table193
+ GCC_except_table196
+ GCC_except_table63
+ OBJC_IVAR_$_DRSSystemProfile._hwModel
+ OBJC_IVAR_$_DRSSystemProfile._isLikelyCarryGroupNum
+ OBJC_IVAR_$_DRSTailspinRequest._maxMAT
+ _TSPDumpOptions_EndTimestamp
+ __116-[DRSService _ckQueueDownstreamOnly_uploadInFlightWithTransaction:xpcActivity:ckHelper:isExpedited:completionBlock:]_block_invoke.cold.1
+ __39-[DRSDampeningManager debugDescription]_block_invoke.471
+ __40-[DRSSystemProfile automatedDeviceGroup]_block_invoke.53
+ __51-[DRSTeamDampeningConfiguration initWithPlistDict:]_block_invoke.404
+ __63-[DRSDampeningManager _ON_MOC_QUEUE_moRepresentationInContext:]_block_invoke.541
+ __87+[DRSDampeningManager dampeningManagerFromPersistentContainer:deleteBadState:errorOut:]_block_invoke.532
+ __block_literal_global.464
+ __block_literal_global.810
+ __block_literal_global.825
+ __block_literal_global.879
+ _configAccessQueue.cold.1
+ _kDRSDMCoreDuetPeopleSuggesterShareSheetMadRequestTimeoutCategory
+ _kDRSDMCoreDuetPeopleSuggesterShareSheetTimeoutCategory
+ _kDRSDMCoreDuetPeopleSuggesterTeamID
+ _kDRSDMPearlAFileBundleCategory
+ _kDRSDMPearlTeamID
+ _kDRTailspinRequestMessageKey_maxMAT
+ _minBufferDurationQueue.cold.1
+ _objc_msgSend$_addContextMetadataKey:value:expectedClass:errorOut:
+ _objc_msgSend$_coreDuetPeopleSuggesterTeamConfiguration:isSeed:isCarrier:platform:
+ _objc_msgSend$_pearlTeamConfiguration:isSeed:isCarrier:platform:
+ _objc_msgSend$_populateHWModel
+ _objc_msgSend$_populateIsCarry
+ _objc_msgSend$addContextMetadataKey:numberValue:errorOut:
+ _objc_msgSend$addContextMetadataKey:stringValue:errorOut:
+ _objc_msgSend$addHWModelContextMetadata
+ _objc_msgSend$addIsLikelyCarryContextMetadata
+ _objc_msgSend$hwModel
+ _objc_msgSend$isLikelyCarryGroupNum
+ _objc_msgSend$maxMAT
+ _objc_msgSend$maxUploadAttemptCount
+ _objc_msgSend$metadataDictionary
+ _objc_msgSend$pearlAFileBundleConfiguration
+ _objc_msgSend$setMaxMAT:
+ _objc_msgSend$shareSheetMadRequestTimeoutConfiguration
+ _objc_msgSend$shareSheetTimeoutConfiguration
- GCC_except_table104
- GCC_except_table109
- GCC_except_table130
- GCC_except_table167
- GCC_except_table178
- GCC_except_table182
- GCC_except_table188
- GCC_except_table191
- GCC_except_table85
- GCC_except_table96
- __39-[DRSDampeningManager debugDescription]_block_invoke.453
- __40-[DRSSystemProfile automatedDeviceGroup]_block_invoke.50
- __51-[DRSTeamDampeningConfiguration initWithPlistDict:]_block_invoke.386
- __63-[DRSDampeningManager _ON_MOC_QUEUE_moRepresentationInContext:]_block_invoke.523
- __87+[DRSDampeningManager dampeningManagerFromPersistentContainer:deleteBadState:errorOut:]_block_invoke.514
- __block_literal_global.443
- __block_literal_global.775
- __block_literal_global.790
- __block_literal_global.840
- _fmodf
- _kDRSRequestADGContextDictKey
CStrings:
+ "ADG"
+ "Added 'isLikelyCarry': '%{public}@' to context metadata"
+ "Added ADG %{public}@ to context metadata for request %{public}@"
+ "Added HW model '%{public}@' to context metadata"
+ "AutomatedDeviceGroupMetadataContextUpdated"
+ "B48@0:8@16@24#32^@40"
+ "Collided on context metadata key '%{public}@'. Overwriting..."
+ "ContextDictionaryUpdateFailure"
+ "ContextDictionaryUpdateSuccess"
+ "ContextMetadataADGFailure"
+ "ContextMetadataHWModelAddition"
+ "ContextMetadataHWModelFailure"
+ "ContextMetadataIsLikelyCarryAddition"
+ "ContextMetadataIsLikelyCarryNumFailure"
+ "Could not add 'IsLikelyCarry' value (nil number)"
+ "Could not add HW model string (nil string)"
+ "Could not serialized updated context as plist"
+ "DRSRequestContextMetadataError"
+ "Failed to add 'isLikelyCarry' value to context metadata due to error: %{public}@"
+ "Failed to add ADG to context metadata due to error: %{public}@"
+ "Failed to add HW model to context metadata due to error: %{public}@"
+ "Failed to lookup hw.model: %d %{public}s"
+ "Failed to serialize to plist when adding context metadata key '%{public}@'"
+ "HWModel"
+ "HWModelLookupFailure"
+ "HWModelLookupSuccess"
+ "IsLikelyCarryLookupSkipped"
+ "LikelyCarry"
+ "MAT[%@, %@]"
+ "MaxMAT"
+ "NilHWModel"
+ "NilLikelyCarry"
+ "OverwritingContextMetadataKey"
+ "PearlAFileBundle"
+ "ShareSheetMadRequestTimeout"
+ "ShareSheetTimeout"
+ "Skipping due to non-Internal device"
+ "SkippingHWModel"
+ "SkippingIsLikelyCarry"
+ "Stopped trying to upload after %u attempts. Upload error: %@"
+ "T@\"NSNumber\",R,N"
+ "T@\"NSNumber\",R,N,V_isLikelyCarryGroupNum"
+ "T@\"NSNumber\",R,N,V_maxMAT"
+ "T@\"NSString\",R,N,V_hwModel"
+ "Updated context metadata with new key: '%{public}@'"
+ "__DPMD__"
+ "_addContextMetadataKey:value:expectedClass:errorOut:"
+ "_coreDuetPeopleSuggesterTeamConfiguration:isSeed:isCarrier:platform:"
+ "_hwModel"
+ "_isLikelyCarryGroupNum"
+ "_maxMAT"
+ "_pearlTeamConfiguration:isSeed:isCarrier:platform:"
+ "_populateHWModel"
+ "_populateIsCarry"
+ "addContextMetadataKey:numberValue:errorOut:"
+ "addContextMetadataKey:stringValue:errorOut:"
+ "addHWModelContextMetadata"
+ "addIsLikelyCarryContextMetadata"
+ "build                       = %{public}@\nbuildVariant                = %{public}@\ndeviceCategory              = %{public}@\ndeviceModel                 = %{public}@\nplatformString              = %{public}@\ndeviceHash                  = %{public}#llx\nisInternal                  = %{public}u\nisSeed                      = %{public}u\nisCarrier                   = %{public}u\ncustomerApprovesAnalytics   = %{public}u\nisLogUploadEnabled          = %{public}u\nisTaskingEnabled            = %{public}u\nuploadSessionUploadCapBytes = %{public}llu\nhwModel                     = %{public}@n\nisLikelyCarry               = %{public}@n\n"
+ "com.apple.CoreDuet.PeopleSuggester"
+ "com.apple.pearl"
+ "hw.model: '%{public}@'"
+ "hwModel"
+ "isLikeCarryDevice"
+ "isLikelyCarryGroupNum"
+ "macOS does not have a sense of carry"
+ "maxUploadAttemptCount"
+ "metadataDictionary"
+ "pearlAFileBundleConfiguration"
+ "setMaxMAT:"
+ "shareSheetMadRequestTimeoutConfiguration"
+ "shareSheetTimeoutConfiguration"
- "Added ADG %{public}@ for request %{public}@"
- "AutomatedDeviceGroupContextUpdateFailure"
- "AutomatedDeviceGroupContextUpdated"
- "Failed to update context dictionary with ADG for request %{public}@"
- "MAT[%@, -)"
- "Stopped trying to upload after %llu attempts. Upload error: %@"
- "__AutomatedDeviceGroup__"
- "build                       = %{public}@\nbuildVariant                = %{public}@\ndeviceCategory              = %{public}@\ndeviceModel                 = %{public}@\nplatformString              = %{public}@\ndeviceHash                  = %{public}#llx\nisInternal                  = %{public}u\nisSeed                      = %{public}u\nisCarrier                   = %{public}u\ncustomerApprovesAnalytics   = %{public}u\nisLogUploadEnabled          = %{public}u\nisTaskingEnabled            = %{public}u\nuploadSessionUploadCapBytes = %{public}llu\n"

```
