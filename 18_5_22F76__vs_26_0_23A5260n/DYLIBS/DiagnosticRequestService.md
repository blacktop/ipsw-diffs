## DiagnosticRequestService

> `/System/Library/PrivateFrameworks/DiagnosticRequestService.framework/DiagnosticRequestService`

```diff

-383.120.2.0.0
-  __TEXT.__text: 0x69630
-  __TEXT.__auth_stubs: 0xf20
-  __TEXT.__objc_methlist: 0x4ca4
+411.0.5.0.0
+  __TEXT.__text: 0x6b93c
+  __TEXT.__auth_stubs: 0xf60
+  __TEXT.__objc_methlist: 0x4d44
   __TEXT.__const: 0xd86
-  __TEXT.__gcc_except_tab: 0xbd8
-  __TEXT.__cstring: 0x54ff
-  __TEXT.__oslogstring: 0xb8c9
+  __TEXT.__gcc_except_tab: 0xc00
+  __TEXT.__cstring: 0x565f
+  __TEXT.__oslogstring: 0xbd2a
   __TEXT.__swift5_typeref: 0x278
   __TEXT.__constg_swiftt: 0x24c
   __TEXT.__swift5_fieldmd: 0x240

   __TEXT.__swift5_capture: 0x20
   __TEXT.__swift5_assocty: 0x30
   __TEXT.__swift5_builtin: 0x14
-  __TEXT.__unwind_info: 0x1708
+  __TEXT.__unwind_info: 0x1728
   __TEXT.__eh_frame: 0x4b0
-  __TEXT.__objc_classname: 0x975
-  __TEXT.__objc_methname: 0xb262
-  __TEXT.__objc_methtype: 0x110c
-  __TEXT.__objc_stubs: 0x82c0
-  __DATA_CONST.__got: 0x448
-  __DATA_CONST.__const: 0x1388
+  __TEXT.__objc_classname: 0x978
+  __TEXT.__objc_methname: 0xb4f7
+  __TEXT.__objc_methtype: 0x111d
+  __TEXT.__objc_stubs: 0x8540
+  __DATA_CONST.__got: 0x430
+  __DATA_CONST.__const: 0x13b8
   __DATA_CONST.__objc_classlist: 0x2b8
   __DATA_CONST.__objc_catlist: 0x8
   __DATA_CONST.__objc_protolist: 0x38
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x25d0
+  __DATA_CONST.__objc_selrefs: 0x2678
   __DATA_CONST.__objc_superrefs: 0x1f8
-  __AUTH_CONST.__auth_got: 0x7a0
-  __AUTH_CONST.__const: 0xf10
-  __AUTH_CONST.__cfstring: 0x53e0
-  __AUTH_CONST.__objc_const: 0x8a38
+  __AUTH_CONST.__auth_got: 0x7c0
+  __AUTH_CONST.__const: 0xf30
+  __AUTH_CONST.__cfstring: 0x5580
+  __AUTH_CONST.__objc_const: 0x8a58
   __AUTH_CONST.__objc_intobj: 0x108
   __AUTH_CONST.__objc_doubleobj: 0x20
-  __AUTH.__objc_data: 0x630
-  __AUTH.__data: 0x300
+  __AUTH.__objc_data: 0x598
+  __AUTH.__data: 0x18
   __DATA.__objc_ivar: 0x454
-  __DATA.__data: 0x788
+  __DATA.__data: 0x708
   __DATA.__objc_stublist: 0x8
-  __DATA.__bss: 0x15f0
-  __DATA.__common: 0x88
-  __DATA_DIRTY.__objc_data: 0x1580
-  __DATA_DIRTY.__data: 0xe0
-  __DATA_DIRTY.__bss: 0x3a8
+  __DATA.__bss: 0x1070
+  __DATA.__common: 0x78
+  __DATA_DIRTY.__objc_data: 0x1618
+  __DATA_DIRTY.__data: 0x478
+  __DATA_DIRTY.__bss: 0x940
+  __DATA_DIRTY.__common: 0x10
   - /System/Library/Frameworks/CloudKit.framework/CloudKit
   - /System/Library/Frameworks/CoreData.framework/CoreData
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation

   - /usr/lib/swift/libswiftCore.dylib
   - /usr/lib/swift/libswiftCoreAudio.dylib
   - /usr/lib/swift/libswiftCoreFoundation.dylib
+  - /usr/lib/swift/libswiftCoreImage.dylib
   - /usr/lib/swift/libswiftCoreLocation.dylib
   - /usr/lib/swift/libswiftCoreMIDI.dylib
   - /usr/lib/swift/libswiftCoreMedia.dylib

   - /usr/lib/swift/libswiftUniformTypeIdentifiers.dylib
   - /usr/lib/swift/libswiftXPC.dylib
   - /usr/lib/swift/libswift_Builtin_float.dylib
-  - /usr/lib/swift/libswift_errno.dylib
-  - /usr/lib/swift/libswift_math.dylib
-  - /usr/lib/swift/libswift_signal.dylib
-  - /usr/lib/swift/libswift_stdio.dylib
-  - /usr/lib/swift/libswift_time.dylib
+  - /usr/lib/swift/libswift_DarwinFoundation1.dylib
+  - /usr/lib/swift/libswift_DarwinFoundation2.dylib
+  - /usr/lib/swift/libswift_DarwinFoundation3.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  - /usr/lib/swift/libswiftsys_time.dylib
-  - /usr/lib/swift/libswiftunistd.dylib
-  UUID: 1AA0B6AA-1438-36AD-A371-7CDD619BF5FA
-  Functions: 2444
-  Symbols:   7113
-  CStrings:  4642
+  UUID: 08C617BF-FD5A-3EDE-B4CC-D8AED8EBF2D0
+  Functions: 2462
+  Symbols:   7181
+  CStrings:  4718
 
Symbols:
+ +[DRSDampeningConfiguration backlightServicesFlipboookHangConfiguration]
+ +[DRSDampeningConfiguration mssLostBeforeThisDrainConfiguration]
+ +[DRSDampeningConfiguration mssLostThisDrainConfiguration]
+ +[DRSDampeningManager _backlightServicesTeamConfiguration:isSeed:isCarrier:platform:]
+ +[DRSDampeningManager _mssTeamConfiguration:isSeed:isCarrier:platform:]
+ +[DRSRequest unblockStrandedUploadingRecordsFromPersistentContainer:errorOut:]
+ +[DRSService defaultServiceIsEnabled]
+ +[DRSService defaultServiceIsEnabled].cold.1
+ -[DRSDecisionServerRequestReply acceptedNum]
+ -[DRSDecisionServerRequestReply errorString]
+ -[DRSDecisionServerRequestReply initWithOriginalRequest:errorString:]
+ -[DRSRequest uploadCompleteWithError:ckOperationID:ckRecordID:]
+ -[DRSRequest uploadFailedDueToReason:ckOperationID:]
+ -[DRSService _handleGetUploadServiceEnabled:state:]
+ -[DRSService _handleSetUploadServiceEnabled:state:]
+ -[DRSService _sendCurrentUploadServiceEnabledReply:state:]
+ -[DRSService _setConfigValue:forKey:expectedClass:]
+ -[DRSService isEnabledOverride]
+ -[DRSService setIsEnabledOverride:]
+ GCC_except_table111
+ GCC_except_table114
+ GCC_except_table116
+ GCC_except_table118
+ GCC_except_table128
+ GCC_except_table130
+ GCC_except_table136
+ GCC_except_table167
+ GCC_except_table176
+ GCC_except_table178
+ GCC_except_table182
+ GCC_except_table185
+ GCC_except_table83
+ GCC_except_table87
+ _DPLogHandle_CKCodeServer
+ _DPLogHandle_CKCodeServer.cold.1
+ _DPLogHandle_CKCodeServer.handle
+ _DPLogHandle_CKCodeServer.onceToken
+ _DPLogHandle_CKCodeServerError
+ _DPLogHandle_CKCodeServerError.cold.1
+ _DPLogHandle_CKCodeServerError.handle
+ _DPLogHandle_CKCodeServerError.onceToken
+ _DRSDeviceFormattedForContentProtection.formatted
+ _DRSDeviceFormattedForContentProtection.once
+ _DRSDeviceIsUnlocked.cold.1
+ _MKBDeviceFormattedForContentProtection
+ _MobileGestalt_copy_productTypeDescForPowerPerf_obj
+ _MobileGestalt_get_current_device
+ _OBJC_IVAR_$_DRSDecisionServerRequestReply._acceptedNum
+ _OBJC_IVAR_$_DRSDecisionServerRequestReply._errorString
+ ___116-[DRSService _ckQueueDownstreamOnly_uploadInFlightWithTransaction:xpcActivity:ckHelper:isExpedited:completionBlock:]_block_invoke.120
+ ___125-[DRSService _ckQueueOnly_submitOutstandingEnableDataGatheringQueriesWithTransaction:xpcActivity:ckHelper:followupWorkBlock:]_block_invoke.146
+ ___136-[DRSCloudKitHelper uploadRequests:contactDecisionServer:xpcActivity:remainingUploadQuota:backingPersistentContainer:completionHandler:]_block_invoke.239
+ ___136-[DRSCloudKitHelper uploadRequests:contactDecisionServer:xpcActivity:remainingUploadQuota:backingPersistentContainer:completionHandler:]_block_invoke.243
+ ___31-[DRSService isEnabledOverride]_block_invoke
+ ___37+[DRSService defaultServiceIsEnabled]_block_invoke
+ ___40-[DRSSystemProfile automatedDeviceGroup]_block_invoke.120
+ ___51-[DRSService _setConfigValue:forKey:expectedClass:]_block_invoke
+ ___51-[DRSTeamDampeningConfiguration initWithPlistDict:]_block_invoke.420
+ ___60-[DRSService _registerPermissiveExpeditedUploadXPCActivity:]_block_invoke.208
+ ___63-[DRSDampeningManager _ON_MOC_QUEUE_moRepresentationInContext:]_block_invoke.550
+ ___78+[DRSRequest unblockStrandedUploadingRecordsFromPersistentContainer:errorOut:]_block_invoke
+ ___87+[DRSDampeningManager dampeningManagerFromPersistentContainer:deleteBadState:errorOut:]_block_invoke.545
+ ___DPLogHandle_CKCodeServerError_block_invoke
+ ___DPLogHandle_CKCodeServer_block_invoke
+ ___DRSDeviceFormattedForContentProtection_block_invoke
+ ___DRSRegisterForDeviceUnlockNotification_block_invoke.9
+ ___DRSRegisterForDeviceUnlockNotification_block_invoke.cold.1
+ ___DRSWaitForDeviceUnlock_block_invoke.cold.2
+ ___block_descriptor_48_e8_32s40bs_e47_v32?0"NSDictionary"8"NSString"16"NSError"24ls32l8s40l8
+ ___block_descriptor_56_e8_32s40s48bs_e47_v32?0"NSDictionary"8"NSString"16"NSError"24ls32l8s40l8s48l8
+ ___block_descriptor_56_e8_32s40s48s_e36_v32?0"CKRecordID"8"NSError"16^B24ls32l8s40l8s48l8
+ ___block_descriptor_64_e8_32s40s48s56s_e42_v32?0"NSArray"8"NSError"16"NSString"24ls32l8s40l8s48l8s56l8
+ ___block_descriptor_64_e8_32s40s48s_e5_v8?0ls32l8s40l8s48l8u56l8
+ ___block_descriptor_72_e8_32s40s48s56s64bs_e47_v32?0"NSDictionary"8"NSString"16"NSError"24ls32l8s40l8s64l8s48l8s56l8
+ ___block_descriptor_72_e8_32s40s48s56s64bs_e63_v24?0"PBCodable<CKCodeOperationMessageMutation>"8"NSError"16ls32l8s40l8s48l8s64l8s56l8
+ ___block_literal_global.118
+ ___block_literal_global.14
+ ___block_literal_global.222
+ ___block_literal_global.232
+ ___block_literal_global.32
+ ___block_literal_global.34
+ ___block_literal_global.386
+ ___block_literal_global.817
+ ___block_literal_global.832
+ ___block_literal_global.886
+ __swift_FORCE_LOAD_$_swiftCoreImage
+ __swift_FORCE_LOAD_$_swiftCoreImage_$_DiagnosticRequestService
+ __swift_FORCE_LOAD_$_swift_DarwinFoundation1
+ __swift_FORCE_LOAD_$_swift_DarwinFoundation1_$_DiagnosticRequestService
+ __swift_FORCE_LOAD_$_swift_DarwinFoundation2
+ __swift_FORCE_LOAD_$_swift_DarwinFoundation2_$_DiagnosticRequestService
+ __swift_FORCE_LOAD_$_swift_DarwinFoundation3
+ __swift_FORCE_LOAD_$_swift_DarwinFoundation3_$_DiagnosticRequestService
+ _defaultServiceIsEnabled.isEnabled
+ _defaultServiceIsEnabled.onceToken
+ _kDRSDMBacklightServicesFlipbookHangIssueCategory
+ _kDRSDMBacklightServicesTeamID
+ _kDRSDMMicrostackLostMSSBeforeThisDrain
+ _kDRSDMMicrostackLostMSSInThisDrain
+ _kDRSDMMicrostackshotsTeamID
+ _kDRSUploadServiceEnabledKey
+ _kDRSUploadServiceEnabled_CurrentValue
+ _kDRSUploadServiceEnabled_HasOverride
+ _objc_msgSend$_backlightServicesTeamConfiguration:isSeed:isCarrier:platform:
+ _objc_msgSend$_handleGetUploadServiceEnabled:state:
+ _objc_msgSend$_handleSetUploadServiceEnabled:state:
+ _objc_msgSend$_mssTeamConfiguration:isSeed:isCarrier:platform:
+ _objc_msgSend$_sendCurrentUploadServiceEnabledReply:state:
+ _objc_msgSend$_setConfigValue:forKey:expectedClass:
+ _objc_msgSend$_setError
+ _objc_msgSend$acceptedNum
+ _objc_msgSend$backlightServicesFlipboookHangConfiguration
+ _objc_msgSend$data
+ _objc_msgSend$defaultServiceIsEnabled
+ _objc_msgSend$errorString
+ _objc_msgSend$getBytes:range:
+ _objc_msgSend$hasError
+ _objc_msgSend$initWithOriginalRequest:errorString:
+ _objc_msgSend$isEnabledOverride
+ _objc_msgSend$mssLostBeforeThisDrainConfiguration
+ _objc_msgSend$mssLostThisDrainConfiguration
+ _objc_msgSend$position
+ _objc_msgSend$setIsEnabledOverride:
+ _objc_msgSend$setPosition:
+ _objc_msgSend$unblockStrandedUploadingRecordsFromPersistentContainer:errorOut:
+ _objc_msgSend$uploadCompleteWithError:ckOperationID:ckRecordID:
+ _objc_msgSend$uploadFailedDueToReason:ckOperationID:
+ _swift_coroFrameAlloc
+ _symbolic _____y___________pG s6ResultOsRi_zRi0_zrlE 24DiagnosticRequestService17RapidPayloadReplyV s5ErrorP
- +[DRSService serviceIsEnabled]
- +[DRSService serviceIsEnabled].cold.1
- -[DRSDecisionServerRequestReply requestAccepted]
- -[DRSRequest uploadCompleteWithError:ckRecordID:]
- -[DRSRequest uploadFailedDueToReason:]
- GCC_except_table112
- GCC_except_table113
- GCC_except_table115
- GCC_except_table125
- GCC_except_table127
- GCC_except_table162
- GCC_except_table171
- GCC_except_table173
- GCC_except_table177
- GCC_except_table180
- GCC_except_table55
- GCC_except_table78
- GCC_except_table94
- OBJC_IVAR_$_PBDataReader._bytes
- OBJC_IVAR_$_PBDataReader._error
- OBJC_IVAR_$_PBDataReader._length
- OBJC_IVAR_$_PBDataReader._pos
- _DPLogHandle_CKInverness
- _DPLogHandle_CKInverness.cold.1
- _DPLogHandle_CKInverness.handle
- _DPLogHandle_CKInverness.onceToken
- _DPLogHandle_CKInvernessError
- _DPLogHandle_CKInvernessError.cold.1
- _DPLogHandle_CKInvernessError.handle
- _DPLogHandle_CKInvernessError.onceToken
- _OBJC_IVAR_$_DRSDecisionServerRequestReply._requestAccepted
- _OBJC_IVAR_$_DRSService._isEnabled
- ___116-[DRSService _ckQueueDownstreamOnly_uploadInFlightWithTransaction:xpcActivity:ckHelper:isExpedited:completionBlock:]_block_invoke_3
- ___125-[DRSService _ckQueueOnly_submitOutstandingEnableDataGatheringQueriesWithTransaction:xpcActivity:ckHelper:followupWorkBlock:]_block_invoke.145
- ___136-[DRSCloudKitHelper uploadRequests:contactDecisionServer:xpcActivity:remainingUploadQuota:backingPersistentContainer:completionHandler:]_block_invoke.228
- ___136-[DRSCloudKitHelper uploadRequests:contactDecisionServer:xpcActivity:remainingUploadQuota:backingPersistentContainer:completionHandler:]_block_invoke.234
- ___30+[DRSService serviceIsEnabled]_block_invoke
- ___40-[DRSSystemProfile automatedDeviceGroup]_block_invoke.114
- ___44-[DRSService setIgnoreAutomatedDeviceGroup:]_block_invoke
- ___51-[DRSTeamDampeningConfiguration initWithPlistDict:]_block_invoke.402
- ___60-[DRSService _registerPermissiveExpeditedUploadXPCActivity:]_block_invoke.207
- ___63-[DRSDampeningManager _ON_MOC_QUEUE_moRepresentationInContext:]_block_invoke.532
- ___87+[DRSDampeningManager dampeningManagerFromPersistentContainer:deleteBadState:errorOut:]_block_invoke.527
- ___DPLogHandle_CKInvernessError_block_invoke
- ___DPLogHandle_CKInverness_block_invoke
- ___DRSRegisterForDeviceUnlockNotification_block_invoke_2
- ___block_descriptor_48_e8_32s40bs_e34_v24?0"NSDictionary"8"NSError"16ls32l8s40l8
- ___block_descriptor_48_e8_32s40s_e36_v32?0"CKRecordID"8"NSError"16^B24ls32l8s40l8
- ___block_descriptor_56_e8_32s40s48bs_e34_v24?0"NSDictionary"8"NSError"16ls32l8s40l8s48l8
- ___block_descriptor_64_e8_32s40s48s56bs_e63_v24?0"PBCodable<CKCodeOperationMessageMutation>"8"NSError"16ls32l8s40l8s48l8s56l8
- ___block_descriptor_64_e8_32s40s48s56s_e29_v24?0"NSArray"8"NSError"16ls32l8s40l8s48l8s56l8
- ___block_descriptor_72_e8_32s40s48s56s64bs_e34_v24?0"NSDictionary"8"NSError"16ls32l8s40l8s64l8s48l8s56l8
- ___block_literal_global.11
- ___block_literal_global.112
- ___block_literal_global.13
- ___block_literal_global.140
- ___block_literal_global.214
- ___block_literal_global.216
- ___block_literal_global.31
- ___block_literal_global.374
- ___block_literal_global.808
- ___block_literal_global.823
- ___block_literal_global.877
- __swift_FORCE_LOAD_$_swift_errno
- __swift_FORCE_LOAD_$_swift_errno_$_DiagnosticRequestService
- __swift_FORCE_LOAD_$_swift_math
- __swift_FORCE_LOAD_$_swift_math_$_DiagnosticRequestService
- __swift_FORCE_LOAD_$_swift_signal
- __swift_FORCE_LOAD_$_swift_signal_$_DiagnosticRequestService
- __swift_FORCE_LOAD_$_swift_stdio
- __swift_FORCE_LOAD_$_swift_stdio_$_DiagnosticRequestService
- __swift_FORCE_LOAD_$_swift_time
- __swift_FORCE_LOAD_$_swift_time_$_DiagnosticRequestService
- __swift_FORCE_LOAD_$_swiftsys_time
- __swift_FORCE_LOAD_$_swiftsys_time_$_DiagnosticRequestService
- __swift_FORCE_LOAD_$_swiftunistd
- __swift_FORCE_LOAD_$_swiftunistd_$_DiagnosticRequestService
- _objc_msgSend$requestAccepted
- _objc_msgSend$serviceIsEnabled
- _objc_msgSend$uploadCompleteWithError:ckRecordID:
- _objc_msgSend$uploadFailedDueToReason:
- _symbolic _____y___________pG s6ResultOsRi_zrlE 24DiagnosticRequestService17RapidPayloadReplyV s5ErrorP
CStrings:
+ "2`"
+ "Avoiding purgeable to non-purgeable transition"
+ "BLSFlipbookHang"
+ "CKCS error for 'reportDiagnosticRequestStatsBatch': %{public}@"
+ "CKCodeOperationCreation"
+ "CKCodeServer"
+ "CKCodeServerDecisionServerError"
+ "CKCodeServerError"
+ "Cannot set '%{public}@' to unexpected non-%{public}@ value: %{public}@"
+ "Cleared '%{public}@'"
+ "ComputeModule"
+ "DRSServiceConfigKeyClear"
+ "DRSServiceConfigUpdate"
+ "DRSServiceConfigUpdateFailure"
+ "DeviceNotFormattedForContentProtection"
+ "Do not wait for a notification that will never come since the device is not formatted for content protection"
+ "Falling back to using `kMGQProductType` to populate device model since `kMGQSubProductType` is not available"
+ "Get 'Upload Service Enabled' setting"
+ "GetUploadServiceEnabled_Rejected"
+ "HasOverride"
+ "Hysteresis: %.1fs, cap: %lu, acceptance rate: %.3f"
+ "LogStateTransitionEdgeCase"
+ "LostMicrostackshotsBeforeThisDrain"
+ "LostMicrostackshotsInThisDrain"
+ "MGQProductTypeFallback"
+ "Moved record back to awaiting upload: %{public}@"
+ "RealityDevice"
+ "Rejecting request for current 'Upload Service Enabled' setting [%d] due to missing entitlement"
+ "RequestStateTransition"
+ "Server: %{public}@, function: %{public}@, CKOperationID: %{public}@"
+ "Set '%{public}@' to %{public}@"
+ "Set 'Upload Service Enabled' setting"
+ "SetUploadServiceEnablement"
+ "Short circuiting waiting for device unlock since the device is not formatted for content protection"
+ "Short-circuiting upload since the upload service is not enabled"
+ "SkippingUnlockRegistration"
+ "T@\"NSNumber\",R,N,V_acceptedNum"
+ "T@\"NSString\",R,N,V_errorString"
+ "Transitioning from %{public}@ to %{public}@\n%{public}@"
+ "UnblockUploadingRecordsFailure"
+ "UnblockUploadingRecordsSuccess"
+ "Unblocked %llu stuck requests"
+ "UnblockingRecord"
+ "UnblockingUploadingLogsFailure"
+ "UnblockingUploadingLogsSuccess"
+ "Unknown decision server error"
+ "Upload cancelled due to DPDS error: %@"
+ "Upload failed. Will retry. CKOperationID: %{public}@, Error: %{public}@"
+ "Upload failure. CKOperationID: %{public}@, Error: %{public}@"
+ "UploadServiceEnabled"
+ "UploadServiceEnabledRequestReply"
+ "UploadSessionShortCircuit"
+ "_acceptedNum"
+ "_backlightServicesTeamConfiguration:isSeed:isCarrier:platform:"
+ "_errorString"
+ "_handleGetUploadServiceEnabled:state:"
+ "_handleSetUploadServiceEnabled:state:"
+ "_mssTeamConfiguration:isSeed:isCarrier:platform:"
+ "_sendCurrentUploadServiceEnabledReply:state:"
+ "_setConfigValue:forKey:expectedClass:"
+ "_setError"
+ "acceptedNum"
+ "backlightServicesFlipboookHangConfiguration"
+ "com.apple.backlightservices"
+ "com.apple.microstackshots"
+ "data"
+ "defaultServiceIsEnabled"
+ "errorString"
+ "getBytes:range:"
+ "hasError"
+ "initWithOriginalRequest:errorString:"
+ "isEnabledOverride"
+ "mssLostBeforeThisDrainConfiguration"
+ "mssLostThisDrainConfiguration"
+ "position"
+ "requestDate < %@"
+ "setIsEnabledOverride:"
+ "setPosition:"
+ "unblockStrandedUploadingRecordsFromPersistentContainer:errorOut:"
+ "uploadCompleteWithError:ckOperationID:ckRecordID:"
+ "uploadFailedDueToReason:ckOperationID:"
+ "v32@?0@\"NSArray\"8@\"NSError\"16@\"NSString\"24"
+ "v32@?0@\"NSDictionary\"8@\"NSString\"16@\"NSError\"24"
+ "v40@0:8@16@24#32"
- "CKInverness"
- "CKInvernessError"
- "Cannot set 'ignoreAutomatedDeviceGroup' to unexpected non-NSNumber value: %{public}@"
- "DRSServiceSetIgnoreAutomatedDeviceGroup"
- "DRSServiceSetIgnoreAutomatedDeviceGroupFailure"
- "DiagnosticPipelineInvernessError"
- "Hysteresis window: %.1fs\nCap: %lu\nAcceptance rate: %.3f\n"
- "Inverness error for 'reportDiagnosticRequestStatsBatch': %{public}@"
- "InvernessDecisionServerError"
- "Set 'ignoreAutomatedDeviceGroup' to %{public}@"
- "TB,R,N,V_isEnabled"
- "TB,R,N,V_requestAccepted"
- "Upload failed. Will retry. %{public, name=uploadSuccess}u Error: %{public}@"
- "Upload failure. %{public, name=uploadSuccess}u Error: %{public}@"
- "_isEnabled"
- "_requestAccepted"
- "requestAccepted"
- "uploadCompleteWithError:ckRecordID:"
- "uploadFailedDueToReason:"
- "v24@?0@\"NSArray\"8@\"NSError\"16"
- "v24@?0@\"NSDictionary\"8@\"NSError\"16"

```
