## libBKDM2.dylib

> `/usr/lib/libBKDM2.dylib`

```diff

-754.120.4.0.0
-  __TEXT.__text: 0x737ac
-  __TEXT.__auth_stubs: 0xd50
-  __TEXT.__objc_methlist: 0x5984
-  __TEXT.__const: 0x69d7
-  __TEXT.__cstring: 0x5f60
-  __TEXT.__oslogstring: 0x3993
-  __TEXT.__gcc_except_tab: 0x13b8
+859.0.0.0.0
+  __TEXT.__text: 0x7c4cc
+  __TEXT.__auth_stubs: 0xda0
+  __TEXT.__objc_methlist: 0x5a64
+  __TEXT.__const: 0x7677
+  __TEXT.__cstring: 0x648d
+  __TEXT.__oslogstring: 0x3e59
+  __TEXT.__gcc_except_tab: 0x15a0
   __TEXT.__ustring: 0x11c
-  __TEXT.__unwind_info: 0xc80
+  __TEXT.__unwind_info: 0xd10
   __TEXT.__eh_frame: 0x50
-  __TEXT.__objc_classname: 0x357
-  __TEXT.__objc_methname: 0x13ef0
-  __TEXT.__objc_methtype: 0x285f
-  __TEXT.__objc_stubs: 0x75e0
-  __DATA_CONST.__got: 0x430
-  __DATA_CONST.__const: 0x12b0
-  __DATA_CONST.__objc_classlist: 0xc8
+  __TEXT.__objc_classname: 0x374
+  __TEXT.__objc_methname: 0x142b0
+  __TEXT.__objc_methtype: 0x2903
+  __TEXT.__objc_stubs: 0x79a0
+  __DATA_CONST.__got: 0x450
+  __DATA_CONST.__const: 0x1368
+  __DATA_CONST.__objc_classlist: 0xd0
   __DATA_CONST.__objc_protolist: 0x28
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x3a28
-  __DATA_CONST.__objc_superrefs: 0xb0
-  __DATA_CONST.__objc_arraydata: 0x2f0
-  __AUTH_CONST.__auth_got: 0x6b8
-  __AUTH_CONST.__const: 0x708
-  __AUTH_CONST.__cfstring: 0x5640
-  __AUTH_CONST.__objc_const: 0x8ca0
-  __AUTH_CONST.__objc_intobj: 0x318
+  __DATA_CONST.__objc_selrefs: 0x3b30
+  __DATA_CONST.__objc_superrefs: 0xb8
+  __DATA_CONST.__objc_arraydata: 0x318
+  __AUTH_CONST.__auth_got: 0x6e0
+  __AUTH_CONST.__const: 0x890
+  __AUTH_CONST.__cfstring: 0x5c60
+  __AUTH_CONST.__objc_const: 0x8fb0
+  __AUTH_CONST.__objc_intobj: 0x348
   __AUTH_CONST.__objc_dictobj: 0xa0
   __AUTH_CONST.__objc_arrayobj: 0xc0
   __AUTH.__objc_data: 0x410
-  __DATA.__objc_ivar: 0x998
+  __DATA.__objc_ivar: 0x9e0
   __DATA.__data: 0x890
   __DATA.__bss: 0x80
-  __DATA_DIRTY.__objc_data: 0x3c0
-  __DATA_DIRTY.__common: 0x30
-  __DATA_DIRTY.__bss: 0x5a
+  __DATA_DIRTY.__objc_data: 0x410
+  __DATA_DIRTY.__common: 0x40
+  __DATA_DIRTY.__bss: 0x63
   - /System/Library/Frameworks/AVFoundation.framework/AVFoundation
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/CoreMotion.framework/CoreMotion

   - /System/Library/PrivateFrameworks/BaseBoard.framework/BaseBoard
   - /System/Library/PrivateFrameworks/BiomeStreams.framework/BiomeStreams
   - /System/Library/PrivateFrameworks/BiometricSupport.framework/BiometricSupport
+  - /System/Library/PrivateFrameworks/DiagnosticRequest.framework/DiagnosticRequest
   - /System/Library/PrivateFrameworks/MSUDataAccessor.framework/MSUDataAccessor
   - /System/Library/PrivateFrameworks/ManagedConfiguration.framework/ManagedConfiguration
   - /System/Library/PrivateFrameworks/MobileKeyBag.framework/MobileKeyBag

   - /usr/lib/libc++.1.dylib
   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libtailspin.dylib
-  UUID: 72747D5C-3B53-3CB1-AD44-6EB9C9638E12
-  Functions: 2656
-  Symbols:   8001
-  CStrings:  5077
+  UUID: B5E0A7D3-F33B-3C22-AE11-819F085769EE
+  Functions: 2715
+  Symbols:   8203
+  CStrings:  5287
 
Symbols:
+ +[BLHelper buildVersionString]
+ +[BLHelper buildVersionString].cold.1
+ +[BLHelper deviceSerialNumberString]
+ +[BLHelper deviceSerialNumberString].cold.1
+ +[BLHelper median:count:queue:completionBlock:]
+ +[BLHelper median:count:queue:completionBlock:].cold.1
+ +[BLHelper median:count:queue:completionBlock:].cold.2
+ +[BioLogDiagnosticPipeline initialize]
+ +[BioLogDiagnosticPipeline initialize].cold.1
+ -[BioLog extractFrameDebug:data:]
+ -[BioLog initForInternalLogging:].cold.5
+ -[BioLog initForInternalLogging:].cold.6
+ -[BioLogDiagnosticPipeline .cxx_destruct]
+ -[BioLogDiagnosticPipeline environment]
+ -[BioLogDiagnosticPipeline init]
+ -[BioLogDiagnosticPipeline init].cold.1
+ -[BioLogDiagnosticPipeline init].cold.2
+ -[BioLogDiagnosticPipeline init].cold.3
+ -[BioLogDiagnosticPipeline scheduleDelay]
+ -[BioLogDiagnosticPipeline scheduleSubmit]
+ -[BioLogDiagnosticPipeline setEnvironment:]
+ -[BioLogDiagnosticPipeline setScheduleDelay:]
+ -[BioLogDiagnosticPipeline setSubmitPeriod:]
+ -[BioLogDiagnosticPipeline submitPeriod]
+ -[BioLogDiagnosticPipeline submit]
+ -[BiometricKitXPCServerPearl captureOutput:didOutputMetadataObjects:fromConnection:].cold.1
+ -[BiometricKitXPCServerPearl getSensorFamily:]
+ -[BiometricKitXPCServerPearl getSensorFamily:].cold.1
+ -[BiometricKitXPCServerPearl getSensorFamily:].cold.2
+ -[BiometricKitXPCServerPearl getSensorFamily:].cold.3
+ -[BiometricKitXPCServerPearl getSensorFamily:].cold.4
+ -[BiometricKitXPCServerPearl getSensorFamily:].cold.5
+ -[BiometricKitXPCServerPearl init].cold.13
+ -[BiometricKitXPCServerPearl performGetDeviceHardwareStateCommand:].cold.3
+ -[BiometricKitXPCServerPearl prewarmCamera:withClient:]
+ -[BiometricKitXPCServerPearl prewarmCamera:withClient:].cold.1
+ -[PearlCoreAnalytics lockStateUpdated:forUser:]
+ -[PearlCoreAnalytics serviceMatchWithServer:]
+ -[PearlCoreAnalyticsDailyUpdateEvent postEventExtendedBy:]
+ -[PearlCoreAnalyticsEvent postEventExtendedBy:]
+ -[PearlCoreAnalyticsEvent postEventExtendedBy:].cold.1
+ -[PearlCoreAnalyticsSecureFaceDetectEvent postEventExtendedBy:]
+ GCC_except_table114
+ GCC_except_table13
+ GCC_except_table14
+ GCC_except_table204
+ GCC_except_table229
+ GCC_except_table235
+ GCC_except_table236
+ GCC_except_table244
+ GCC_except_table245
+ GCC_except_table38
+ GCC_except_table51
+ GCC_except_table52
+ GCC_except_table53
+ GCC_except_table55
+ GCC_except_table89
+ GCC_except_table90
+ _AVGQKYDMKTE2UUKHJCGGZGQNYH5GDE
+ _AVPSecureBootG2Rsa4kSha384IM4C
+ _AVPSecureBootG2Rsa4kSha384IM4C_len
+ _CryptexG1Rsa4kSha384IM4C
+ _CryptexG1Rsa4kSha384IM4C_len
+ _CryptexGlobalG1Rsa4kSha384IM4C
+ _CryptexGlobalG1Rsa4kSha384IM4C_len
+ _DERParseInteger64Signed
+ _DERParseIntegerSigned
+ _DRSubmitLog
+ _Img4DecodeAVPSecureBootG2Rsa4kSha384IM4C
+ _Img4DecodeCryptexG1Rsa4kSha384IM4C
+ _Img4DecodeCryptexGlobalG1Rsa4kSha384IM4C
+ _Img4DecodeLocalPolicyTatsuG8Rsa4kSha384IM4C
+ _Img4DecodeRepairG1Rsa4kSha384IM4C
+ _Img4DecodeSecureBootG7Rsa4kSha384IM4C
+ _Img4DecodeSecureBootGlobalG1Rsa4kSha384IM4C
+ _LocalPolicyTatsuG8Rsa4kSha384IM4C
+ _LocalPolicyTatsuG8Rsa4kSha384IM4C_len
+ _LocalRsa4kSha384IM4C
+ _LocalRsa4kSha384IM4C_len
+ _NSFileCreationDate
+ _NSTemporaryDirectory
+ _OBJC_CLASS_$_BioLogDiagnosticPipeline
+ _OBJC_CLASS_$_BiometricKitCoreAnalyticsLockState
+ _OBJC_CLASS_$_NSPipe
+ _OBJC_CLASS_$_NSTask
+ _OBJC_EHTYPE_$_NSException
+ _OBJC_IVAR_$_BioLog._diagnosticPipeline
+ _OBJC_IVAR_$_BioLog._frameDebugExtraArray
+ _OBJC_IVAR_$_BioLog._frameDebugExtraFrameCount
+ _OBJC_IVAR_$_BioLog._frameDebugExtraFrameCountExpected
+ _OBJC_IVAR_$_BioLog._frameDebugExtraQueue
+ _OBJC_IVAR_$_BioLog._frameDebugExtraSemaphore
+ _OBJC_IVAR_$_BioLog._frameDebugExtraSequenceNumber
+ _OBJC_IVAR_$_BioLogDiagnosticPipeline._environment
+ _OBJC_IVAR_$_BioLogDiagnosticPipeline._lastSubmitTry
+ _OBJC_IVAR_$_BioLogDiagnosticPipeline._queue
+ _OBJC_IVAR_$_BioLogDiagnosticPipeline._running
+ _OBJC_IVAR_$_BioLogDiagnosticPipeline._scheduleDelay
+ _OBJC_IVAR_$_BioLogDiagnosticPipeline._submitFromDate
+ _OBJC_IVAR_$_BioLogDiagnosticPipeline._submitPeriod
+ _OBJC_IVAR_$_BioLogDiagnosticPipeline._submitPostponeHours
+ _OBJC_IVAR_$_BioLogDiagnosticPipeline._timerSource
+ _OBJC_IVAR_$_BioLogDiagnosticPipeline._userDefaults
+ _OBJC_IVAR_$_BiometricKitXPCServerPearl._avcSessionState
+ _OBJC_IVAR_$_BiometricKitXPCServerPearl._avcStartStopQueue
+ _OBJC_IVAR_$_PearlCoreAnalytics._lockState
+ _OBJC_METACLASS_$_BioLogDiagnosticPipeline
+ _OUTLINED_FUNCTION_50
+ _RepairG1Rsa4kSha384IM4C
+ _RepairG1Rsa4kSha384IM4C_len
+ _SecureBootG7Rsa4kSha384IM4C
+ _SecureBootG7Rsa4kSha384IM4C_len
+ _SecureBootGlobalG1Rsa4kSha384IM4C
+ _SecureBootGlobalG1Rsa4kSha384IM4C_len
+ _ShamRsa4kSha384IM4C
+ _ShamRsa4kSha384IM4C_len
+ __OBJC_$_CLASS_METHODS_BioLogDiagnosticPipeline
+ __OBJC_$_INSTANCE_METHODS_BioLogDiagnosticPipeline
+ __OBJC_$_INSTANCE_VARIABLES_BioLogDiagnosticPipeline
+ __OBJC_$_PROP_LIST_BioLogDiagnosticPipeline
+ __OBJC_CLASS_RO_$_BioLogDiagnosticPipeline
+ __OBJC_METACLASS_RO_$_BioLogDiagnosticPipeline
+ ___30+[BLHelper buildVersionString]_block_invoke
+ ___32-[BioLogDiagnosticPipeline init]_block_invoke
+ ___33-[BioLog extractFrameDebug:data:]_block_invoke
+ ___33-[BioLog extractFrameDebug:data:]_block_invoke_2
+ ___34-[BiometricKitXPCServerPearl init]_block_invoke.218
+ ___34-[BiometricKitXPCServerPearl init]_block_invoke.221
+ ___35-[BioLog logFrameDebug:withBuffer:]_block_invoke
+ ___36+[BLHelper deviceSerialNumberString]_block_invoke
+ ___43-[BiometricKitXPCServerPearl serviceMatch:]_block_invoke.258
+ ___47+[BLHelper median:count:queue:completionBlock:]_block_invoke
+ ___47+[BLHelper median:count:queue:completionBlock:]_block_invoke.cold.1
+ ___47+[BLHelper median:count:queue:completionBlock:]_block_invoke.cold.2
+ ___47+[BLHelper median:count:queue:completionBlock:]_block_invoke.cold.3
+ ___50-[BiometricKitXPCServerPearl initSecureFaceDetect]_block_invoke.828
+ ___50-[BiometricKitXPCServerPearl initSecureFaceDetect]_block_invoke.831
+ ___50-[BiometricKitXPCServerPearl initSecureFaceDetect]_block_invoke.834
+ ___50-[BiometricKitXPCServerPearl initSecureFaceDetect]_block_invoke.837
+ ___50-[BiometricKitXPCServerPearl stopSecureFaceDetect]_block_invoke
+ ___51-[BiometricKitXPCServerPearl startSecureFaceDetect]_block_invoke
+ ___51-[BiometricKitXPCServerPearl startSecureFaceDetect]_block_invoke.cold.1
+ ___61-[BioLog logSequenceInfo:withContext:orientation:identities:]_block_invoke.709
+ ___61-[BioLog logSequenceInfo:withContext:orientation:identities:]_block_invoke.751
+ ___75-[BiometricKitXPCServerPearl serviceStatus:version:ordinal:data:timestamp:]_block_invoke.263
+ ___block_descriptor_40_e8_32s_e8_v12?0S8ls32l8
+ ___block_descriptor_56_e8_32s40r_e5_v8?0ls32l8r40l8
+ ___block_descriptor_56_e8_32s40s_e5_v8?0ls32l8s40l8
+ ___block_descriptor_64_e8_32s40r48r_e5_v8?0ls32l8r40l8r48l8
+ ___block_literal_global.158
+ ___block_literal_global.204
+ ___block_literal_global.242
+ ___block_literal_global.489
+ ___block_literal_global.830
+ ___block_literal_global.833
+ ___block_literal_global.836
+ ___block_literal_global.839
+ ___block_literal_global.879
+ ___block_literal_global.881
+ ___osLogTrace_BioLogDiagnosticPipeline
+ ___osLog_BioLogDiagnosticPipeline
+ __dispatch_queue_attr_concurrent
+ _buildVersionString.buildVersionString
+ _buildVersionString.onceToken
+ _captureOutput:didOutputMetadataObjects:fromConnection:.abcEventSent
+ _captureOutput:didOutputMetadataObjects:fromConnection:.unexpectedCallsCount
+ _deviceSerialNumberString.onceToken
+ _deviceSerialNumberString.serialNumberString
+ _dispatch_time
+ _getSensorFamily:.sensorFamily
+ _kBiometricKitCoreAnalyticsLockStateEventName
+ _kImg4DecodeAVPSecureBootG2Rsa4kSha384IM4C
+ _kImg4DecodeCryptexG1Rsa4kSha384IM4C
+ _kImg4DecodeCryptexGlobalG1Rsa4kSha384IM4C
+ _kImg4DecodeLocalPolicyTatsuG8Rsa4kSha384IM4C
+ _kImg4DecodeRepairG1Rsa4kSha384IM4C
+ _kImg4DecodeSecureBootG7Rsa4kSha384IM4C
+ _kImg4DecodeSecureBootGlobalG1Rsa4kSha384IM4C
+ _kPearlAbcTypeAVCaptureIssue
+ _objc_begin_catch
+ _objc_end_catch
+ _objc_msgSend$UUID
+ _objc_msgSend$_setError
+ _objc_msgSend$buildVersionString
+ _objc_msgSend$description
+ _objc_msgSend$deviceSerialNumberString
+ _objc_msgSend$extractFrameDebug:data:
+ _objc_msgSend$getBytes:range:
+ _objc_msgSend$hasError
+ _objc_msgSend$initWithPersistedDataWithName:
+ _objc_msgSend$launchAndReturnError:
+ _objc_msgSend$lockStateUpdated:forUser:
+ _objc_msgSend$median:count:queue:completionBlock:
+ _objc_msgSend$pipe
+ _objc_msgSend$position
+ _objc_msgSend$postEventExtendedBy:
+ _objc_msgSend$scheduleSubmit
+ _objc_msgSend$serviceMatchWithServer:
+ _objc_msgSend$setArguments:
+ _objc_msgSend$setCurrentDirectoryURL:
+ _objc_msgSend$setEnvironment:
+ _objc_msgSend$setLaunchPath:
+ _objc_msgSend$setPosition:
+ _objc_msgSend$setScheduleDelay:
+ _objc_msgSend$setStandardInput:
+ _objc_msgSend$setStandardOutput:
+ _objc_msgSend$setSubmitPeriod:
+ _objc_msgSend$stringForKey:
+ _objc_msgSend$submit
+ _objc_msgSend$terminationReason
+ _objc_msgSend$terminationStatus
+ _objc_msgSend$unsignedIntegerForKey:
+ _objc_msgSend$waitUntilExit
+ _objc_msgSend$writeToFile:atomically:
+ _objc_retainAutoreleasedReturnValue
- +[BLHelper buildVersion]
- +[BLHelper buildVersion].cold.1
- +[BLHelper deviceSerialNumber]
- +[BLHelper deviceSerialNumber].cold.1
- -[PearlCoreAnalyticsDailyUpdateEvent postEvent]
- -[PearlCoreAnalyticsEvent postEvent]
- -[PearlCoreAnalyticsEvent postEvent].cold.1
- -[PearlCoreAnalyticsSecureFaceDetectEvent postEvent]
- GCC_except_table203
- GCC_except_table220
- GCC_except_table232
- GCC_except_table233
- GCC_except_table239
- GCC_except_table241
- GCC_except_table4
- GCC_except_table43
- GCC_except_table44
- GCC_except_table45
- GCC_except_table47
- OBJC_IVAR_$_PBDataReader._bytes
- OBJC_IVAR_$_PBDataReader._error
- OBJC_IVAR_$_PBDataReader._length
- OBJC_IVAR_$_PBDataReader._pos
- _AVGQCaptureAttentionDetectionSupported
- _Local_root_rsa4k_pub
- _OBJC_IVAR_$_BiometricKitXPCServerPearl._avcSessionInitialized
- _OBJC_IVAR_$_BiometricKitXPCServerPearl._avcSessionStarted
- _SecureBoot_root_rsa4k_pub
- _SecureBoot_root_rsa4k_pub_len
- _Sham_root_rsa4k_pub
- ___24+[BLHelper buildVersion]_block_invoke
- ___24+[BLHelper buildVersion]_block_invoke.cold.1
- ___30+[BLHelper deviceSerialNumber]_block_invoke
- ___34-[BiometricKitXPCServerPearl init]_block_invoke.217
- ___34-[BiometricKitXPCServerPearl init]_block_invoke.220
- ___43-[BiometricKitXPCServerPearl serviceMatch:]_block_invoke.257
- ___50-[BiometricKitXPCServerPearl initSecureFaceDetect]_block_invoke.826
- ___50-[BiometricKitXPCServerPearl initSecureFaceDetect]_block_invoke.830
- ___50-[BiometricKitXPCServerPearl initSecureFaceDetect]_block_invoke.833
- ___50-[BiometricKitXPCServerPearl initSecureFaceDetect]_block_invoke.836
- ___75-[BiometricKitXPCServerPearl serviceStatus:version:ordinal:data:timestamp:]_block_invoke.262
- ___block_literal_global.133
- ___block_literal_global.179
- ___block_literal_global.241
- ___block_literal_global.487
- ___block_literal_global.829
- ___block_literal_global.832
- ___block_literal_global.835
- ___block_literal_global.838
- ___block_literal_global.878
- ___block_literal_global.880
- _buildVersion.onceToken
- _buildVersion.version
- _deviceSerialNumber.onceToken
- _deviceSerialNumber.serialNumberString
- _objc_msgSend$arrayByAddingObject:
- _objc_msgSend$buildVersion
- _objc_msgSend$deviceSerialNumber
- _sysctl
CStrings:
+ "!_inDiagnosticMode"
+ "%lds"
+ "("
+ ")"
+ "-"
+ "--auto-compress"
+ "--cd"
+ "--create"
+ "--file"
+ "--files-from"
+ "--null"
+ "-Btime"
+ "-f"
+ "-name"
+ "-or"
+ "-print0"
+ "/Library/Caches/com.apple.xbs/Sources/Pearl/BioLog/BioLogDiagnosticPipeline.m"
+ "/usr/bin/find"
+ "/usr/bin/login"
+ "@\"BioLogDiagnosticPipeline\""
+ "@\"BioUserDefaults\""
+ "@\"BiometricKitCoreAnalyticsLockState\""
+ "AVCaptureIssue"
+ "BioLogDiagnosticPipeline"
+ "BioLogMeta_%@_%lu_%@.zip"
+ "BuildVersion"
+ "Couldn't create OS Log for 'com.apple.BiometricKit.BioLogDiagnosticPipeline'!\n"
+ "DRContext.json"
+ "ERROR: DRSubmitLog -> %@\n"
+ "ERROR: dataWithJSONObject(contextDictionary) -> nil (%@)\n"
+ "ERROR: findTask -> %@\n"
+ "ERROR: tarTask -> %@\n"
+ "ERROR: tarTask threw exception: %@\n"
+ "ERROR: tarTask(find) -> %d (terminationReason:%ld)\n"
+ "ERROR: tarTask(find) failed to create log bundle file: %@\n"
+ "ERROR: writeToFile(DRContext.json) -> NO\n"
+ "Note: Delayed _frameDebugExtraArray collected: %u\n"
+ "PearlAFileBundle"
+ "PearlCoreAnalytics lockStateUpdated: %u forUser: %u\n"
+ "PearlCoreAnalytics serviceMatch\n"
+ "SerialNumber"
+ "T@\"NSString\",&,V_environment"
+ "TQ,N,V_scheduleDelay"
+ "TQ,V_submitPeriod"
+ "UUID"
+ "UnstoppedAVCaptureSession"
+ "WARNING: _frameDebugExtraSequenceNumber != sequenceInfo->sequenceId.number (%lu != %u)\n"
+ "[_dailyEvent postEventExtendedBy:[_lockState dictionaryRepresentation]]"
+ "[self.biometricABC sendAutoBugCaptureEvent:kPearlAbcUnstoppedAVCaptureSession]"
+ "_avcSessionState"
+ "_avcSessionState == kAVCSessionStateUninitialized"
+ "_avcStartStopQueue"
+ "_diagnosticPipeline"
+ "_environment"
+ "_frameDebugExtraArray"
+ "_frameDebugExtraFrameCount"
+ "_frameDebugExtraFrameCountExpected"
+ "_frameDebugExtraQueue"
+ "_frameDebugExtraSemaphore"
+ "_frameDebugExtraSequenceNumber"
+ "_lastSubmitTry"
+ "_lockState"
+ "_queue"
+ "_running"
+ "_scheduleDelay"
+ "_setError"
+ "_submitFromDate"
+ "_submitFromDate: %@ (Last submit)\n"
+ "_submitFromDate: %@ (Never submitted)\n"
+ "_submitPeriod"
+ "_submitPostponeHours"
+ "_timerSource"
+ "_userDefaults"
+ "bioLogDiagnosticPipelineEnvironment"
+ "bioLogDiagnosticPipelineSubmitPeriod"
+ "bioLogDiagnosticPipelineSubmitted"
+ "buildVersionString"
+ "build_version"
+ "bundle"
+ "bundle_id"
+ "bundle_type"
+ "bundle_version"
+ "com.apple.BioLog.DiagnosticPipeline"
+ "com.apple.BioLog.frameDebugExtra"
+ "com.apple.pearl"
+ "com.apple.pearl.biolog_meta"
+ "com.apple.pearld.avcStartStop"
+ "creation_time_seconds"
+ "development"
+ "deviceSerialNumberString"
+ "device_category"
+ "device_serial"
+ "endOffset <= [debugData length]"
+ "end_time_seconds"
+ "environment"
+ "extractFrameDebug:data:"
+ "fid_resized_data_median_value"
+ "first"
+ "first <= nth"
+ "frame_debug_extra_array"
+ "getBytes:range:"
+ "getSensorFamily\n"
+ "getSensorFamily -> 0x%x\n"
+ "getSensorFamily:"
+ "hasError"
+ "i24@0:8^C16"
+ "i32@0:8Q16@24"
+ "iOS"
+ "last_frame_glasses_score"
+ "last_frame_has_glasses"
+ "launchAndReturnError:"
+ "lockStateUpdated:forUser:"
+ "median:count:queue:completionBlock:"
+ "nth <= last"
+ "pipe"
+ "pose_bin_count"
+ "position"
+ "postEventExtendedBy:"
+ "prewarmCamera: %lu %@\n"
+ "prewarmCamera: -> (%{errno}d)\n"
+ "prewarmCamera:withClient:"
+ "processSecureFaceDetectRequestMessage: request:%u, flags:0x%x, sessionID:%u (_avcSessionState:%u)\n"
+ "production"
+ "response.sensorFamily != kSensorFamilyNotSet"
+ "response.sensorFamily < kSensorFamilyCount"
+ "responseSize == sizeof(response)"
+ "scheduleDelay"
+ "scheduleSubmit"
+ "sec-*.json"
+ "sensorFamilyOut"
+ "seq-*.json"
+ "serviceMatchWithServer:"
+ "setArguments:"
+ "setCurrentDirectoryURL:"
+ "setEnvironment:"
+ "setLaunchPath:"
+ "setPosition:"
+ "setScheduleDelay:"
+ "setStandardInput:"
+ "setStandardOutput:"
+ "setSubmitPeriod:"
+ "sizeof(*debugInfo) <= [debugData length]"
+ "startSecureFaceDetect: calling startRunning (%p)\n"
+ "startSecureFaceDetect: dispatch startRunning (%p)\n"
+ "startSecureFaceDetect: session abandoned, calling stopRunning (%p)\n"
+ "startSecureFaceDetect: startRunning (%p) (dt = %f ms), running:%u, interrupted:%u\n"
+ "start_time_seconds"
+ "stopSecureFaceDetect: calling stopRunning (%p)\n"
+ "stopSecureFaceDetect: dispatch stopRunning (%p)\n"
+ "stopSecureFaceDetect: stopRunning (%p) (dt = %f ms)\n"
+ "stringForKey:"
+ "submit"
+ "submit -> DONE (_submitFromDate: %@)\n"
+ "submit -> FAILED: Will retry in %lu hours.\n"
+ "submit <- (submitFromDate: %@, submitToDate: %@)\n"
+ "submitPeriod"
+ "tar"
+ "terminationReason"
+ "terminationStatus"
+ "unsignedIntegerForKey:"
+ "v12@?0S8"
+ "v32@0:8^{?=QSSSCC{?=QSC}}16@24"
+ "v48@0:8^S16Q24@32@?40"
+ "waitUntilExit"
+ "writeToFile:atomically:"
- "!_avcSessionInitialized"
- "/System/Library/Pearl/DCNKernels/DCNKernelsa_H11_iPhone.bin"
- "/System/Library/Pearl/DCNKernels/DCNKernelsb_H11_iPhone.bin"
- "VasUgeSzVyHdB27g2XpN0g"
- "[_dailyEvent postEvent]"
- "_avcSessionInitialized"
- "_avcSessionStarted"
- "arrayByAddingObject:"
- "buildVersion"
- "deviceSerialNumber"
- "processSecureFaceDetectRequestMessage: request:%u, flags:0x%x, sessionID:%u\n"
- "startSecureFaceDetect: startRunning (dt = %f ms), running:%u, interrupted:%u\n"
- "stopSecureFaceDetect: stopRunning (dt = %f ms)\n"

```
