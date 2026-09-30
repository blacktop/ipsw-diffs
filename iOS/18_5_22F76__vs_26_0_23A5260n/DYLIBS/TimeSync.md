## TimeSync

> `/System/Library/PrivateFrameworks/TimeSync.framework/TimeSync`

```diff

-1340.12.0.0.0
-  __TEXT.__text: 0x51894
-  __TEXT.__auth_stubs: 0x900
-  __TEXT.__objc_methlist: 0x5fe8
-  __TEXT.__const: 0x288
-  __TEXT.__oslogstring: 0x3b64
-  __TEXT.__cstring: 0x68d0
-  __TEXT.__gcc_except_tab: 0xb84
-  __TEXT.__unwind_info: 0x1650
-  __TEXT.__objc_classname: 0x9bf
-  __TEXT.__objc_methname: 0xaed0
-  __TEXT.__objc_methtype: 0x14fe
-  __TEXT.__objc_stubs: 0x68c0
-  __DATA_CONST.__got: 0x378
-  __DATA_CONST.__const: 0xbf0
-  __DATA_CONST.__objc_classlist: 0x320
-  __DATA_CONST.__objc_catlist: 0x8
+1400.53.0.0.0
+  __TEXT.__text: 0x57b44
+  __TEXT.__auth_stubs: 0x920
+  __TEXT.__objc_methlist: 0x63a0
+  __TEXT.__const: 0x298
+  __TEXT.__oslogstring: 0x3e8a
+  __TEXT.__cstring: 0x6fb7
+  __TEXT.__gcc_except_tab: 0xd24
+  __TEXT.__unwind_info: 0x1790
+  __TEXT.__objc_classname: 0x9f6
+  __TEXT.__objc_methname: 0xb671
+  __TEXT.__objc_methtype: 0x1839
+  __TEXT.__objc_stubs: 0x6ec0
+  __DATA_CONST.__got: 0x390
+  __DATA_CONST.__const: 0xc88
+  __DATA_CONST.__objc_classlist: 0x330
+  __DATA_CONST.__objc_catlist: 0x10
   __DATA_CONST.__objc_protolist: 0x60
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x2148
+  __DATA_CONST.__objc_selrefs: 0x22f0
   __DATA_CONST.__objc_protorefs: 0x20
-  __DATA_CONST.__objc_superrefs: 0x340
-  __AUTH_CONST.__auth_got: 0x498
-  __AUTH_CONST.__const: 0x220
-  __AUTH_CONST.__cfstring: 0x4f80
-  __AUTH_CONST.__objc_const: 0xb930
+  __DATA_CONST.__objc_superrefs: 0x348
+  __AUTH_CONST.__auth_got: 0x4a8
+  __AUTH_CONST.__const: 0x2a0
+  __AUTH_CONST.__cfstring: 0x5160
+  __AUTH_CONST.__objc_const: 0xbd38
   __AUTH_CONST.__objc_intobj: 0x30
-  __DATA.__objc_ivar: 0x830
+  __DATA.__objc_ivar: 0x860
   __DATA.__data: 0x488
   __DATA.__bss: 0xa0
-  __DATA_DIRTY.__objc_data: 0x1f40
-  __DATA_DIRTY.__bss: 0xe8
+  __DATA_DIRTY.__objc_data: 0x1fe0
+  __DATA_DIRTY.__bss: 0xf8
   __DATA_DIRTY.__common: 0x4
   - /System/Library/Frameworks/Accelerate.framework/Accelerate
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libc++.1.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: C52F69BA-30C3-38EE-896D-73529579185B
-  Functions: 2425
-  Symbols:   7624
-  CStrings:  3687
+  UUID: CA28FD9A-798E-3168-8396-B9423E067DE3
+  Functions: 2566
+  Symbols:   7899
+  CStrings:  3860
 
Symbols:
+ +[NSValue(TSMSGExternalSyncConfig) valuewithTSMSGExternalSyncConfig:]
+ +[TSMSGClockSession withSyncId:nominalSyncDuration:]
+ +[TSMSGService sharedMSGService]
+ +[TSMSGService sharedMSGService].cold.1
+ -[NSValue(TSMSGExternalSyncConfig) TSMSGExternalSyncConfigValue]
+ -[TSClockManager addPersistentUserFilteredClockRef:error:]
+ -[TSClockManager addPersistentUserFilteredClockWithMachInterval:domainInterval:usingFilterShift:isAdaptive:withUserID:error:]
+ -[TSClockManager getPersistentUserFilteredClockIdentifier:error:]
+ -[TSClockManager removePersistentUserFilteredClock:error:]
+ -[TSDCgPTPClock setPreferredGM:error:]
+ -[TSDCgPTPClock updateNtpAnchorOffset:isLocalClockSourceFromNTP:error:]
+ -[TSMSGClockSession nominalSyncDuration]
+ -[TSMSGClockSession refCnt]
+ -[TSMSGClockSession setRefCnt:]
+ -[TSMSGClockSession syncId]
+ -[TSMSGService .cxx_destruct]
+ -[TSMSGService addMSGClock:withNominalSyncDuration:error:]
+ -[TSMSGService addMSGClockRef:error:]
+ -[TSMSGService daemonClientRefresh]
+ -[TSMSGService dispatchMSGNotification:args:numArgs:]
+ -[TSMSGService dispatchMSGNotification:args:numArgs:].cold.1
+ -[TSMSGService dispatchMSGNotification:args:numArgs:].cold.2
+ -[TSMSGService dispatchMSGNotification:args:numArgs:].cold.3
+ -[TSMSGService dispatchMSGNotification:args:numArgs:].cold.4
+ -[TSMSGService dispatchMSGNotification:args:numArgs:].cold.5
+ -[TSMSGService getMSGClock:error:]
+ -[TSMSGService init]
+ -[TSMSGService removeMSGClock:error:]
+ -[TSMSGService startExternalSync:error:]
+ -[TSMSGService stopExternalSync:error:]
+ -[TSXDaemonServiceClient addMSGClock:withNominalSyncDuration:error:]
+ -[TSXDaemonServiceClient addMSGClockRef:error:]
+ -[TSXDaemonServiceClient getMSGClock:error:]
+ -[TSXDaemonServiceClient isMSGServiceAvailable]
+ -[TSXDaemonServiceClient removeMSGClock:error:]
+ -[TSXDaemonServiceClient restoreMSGClockSession:withNominalSyncDuration:refCnt:error:]
+ -[TSXDaemonServiceClient startMSGExternalSync:]
+ -[TSXDaemonServiceClient stopMSGExternalSync:]
+ -[TSXDaemonServiceClientExported msgServiceNotification:arguments:]
+ -[TSgPTPClock setPreferredGM:error:]
+ -[TSgPTPClock updateNtpAnchorOffset:isLocalClockSourceFromNTP:error:]
+ -[TSgPTPLocalClockPort hasLocalClockSourceFromNTP]
+ -[TSgPTPLocalClockPort hasNtpAnchorOffsetNsec]
+ -[TSgPTPLocalClockPort localClockSourceFromNTP]
+ -[TSgPTPLocalClockPort ntpAnchorOffsetNsec]
+ -[TSgPTPManager addCopresencePTPInstance:ntpAndUpTimeOffsetNsec:isLocalClockSourceFromNTP:error:]
+ -[TSgPTPManager addCopresencePTPInstanceRefWithError:]
+ -[TSgPTPManager dockReplayTimestamps:]
+ -[TSgPTPManager startReplayTimestamps:]
+ -[TSgPTPManager stopReplayTimestamps:]
+ -[_TSF_TSDClockManager addPersistentUserFilteredClockRef:error:]
+ -[_TSF_TSDClockManager addPersistentUserFilteredClockRef:error:].cold.1
+ -[_TSF_TSDClockManager addPersistentUserFilteredClockWithMachInterval:domainInterval:usingFilterShift:isAdaptive:withUserID:error:]
+ -[_TSF_TSDClockManager addPersistentUserFilteredClockWithMachInterval:domainInterval:usingFilterShift:isAdaptive:withUserID:error:].cold.1
+ -[_TSF_TSDClockManager getPersistentUserFilteredClockIdentifier:error:]
+ -[_TSF_TSDClockManager getPersistentUserFilteredClockIdentifier:error:].cold.1
+ -[_TSF_TSDClockManager removePersistentUserFilteredClock:error:]
+ -[_TSF_TSDClockManager removePersistentUserFilteredClock:error:].cold.1
+ -[_TSF_TSDgPTPClock setPreferredGM:error:]
+ -[_TSF_TSDgPTPClock updateNtpAnchorOffset:isLocalClockSourceFromNTP:error:]
+ -[_TSF_TSDgPTPLocalClockPort _hasLocalClockSourceFromNTP]
+ -[_TSF_TSDgPTPLocalClockPort _hasNtpAnchorOffsetNsec]
+ -[_TSF_TSDgPTPLocalClockPort _localClockSourceFromNTP]
+ -[_TSF_TSDgPTPLocalClockPort _ntpAnchorOffsetNsec]
+ -[_TSF_TSDgPTPLocalClockPort hasLocalClockSourceFromNTP]
+ -[_TSF_TSDgPTPLocalClockPort hasNtpAnchorOffsetNsec]
+ -[_TSF_TSDgPTPLocalClockPort localClockSourceFromNTP]
+ -[_TSF_TSDgPTPLocalClockPort ntpAnchorOffsetNsec]
+ -[_TSF_TSDgPTPLocalClockPort setHasLocalClockSourceFromNTP:]
+ -[_TSF_TSDgPTPLocalClockPort setHasNtpAnchorOffsetNsec:]
+ -[_TSF_TSDgPTPLocalClockPort setLocalClockSourceFromNTP:]
+ -[_TSF_TSDgPTPLocalClockPort setNtpAnchorOffsetNsec:]
+ -[_TSF_TSDgPTPManager addCopresencePTPInstance:ntpAndUpTimeOffsetNsec:isLocalClockSourceFromNTP:error:]
+ -[_TSF_TSDgPTPManager addCopresencePTPInstance:ntpAndUpTimeOffsetNsec:isLocalClockSourceFromNTP:error:].cold.1
+ -[_TSF_TSDgPTPManager addCopresencePTPInstanceRefWithError:]
+ -[_TSF_TSDgPTPManager addCopresencePTPInstanceRefWithError:].cold.1
+ -[_TSF_TSDgPTPManager dockReplayTimestamps:]
+ -[_TSF_TSDgPTPManager dockReplayTimestamps:].cold.1
+ -[_TSF_TSDgPTPManager startReplayTimestamps:]
+ -[_TSF_TSDgPTPManager startReplayTimestamps:].cold.1
+ -[_TSF_TSDgPTPManager stopReplayTimestamps:]
+ -[_TSF_TSDgPTPManager stopReplayTimestamps:].cold.1
+ GCC_except_table29
+ GCC_except_table33
+ GCC_except_table34
+ GCC_except_table35
+ GCC_except_table39
+ GCC_except_table42
+ GCC_except_table44
+ _OBJC_CLASS_$_NSValue
+ _OBJC_CLASS_$_TSMSGClockSession
+ _OBJC_CLASS_$_TSMSGService
+ _OBJC_IVAR_$_TSMSGClockSession._nominalSyncDuration
+ _OBJC_IVAR_$_TSMSGClockSession._refCnt
+ _OBJC_IVAR_$_TSMSGClockSession._syncId
+ _OBJC_IVAR_$_TSMSGService._activeClockSessionsBySyncId
+ _OBJC_IVAR_$_TSMSGService._activeExtSyncSessionsByTriggerId
+ _OBJC_IVAR_$_TSMSGService._clockSessionsLock
+ _OBJC_IVAR_$_TSMSGService._extSyncSessionsLock
+ _OBJC_IVAR_$_TSMSGService._msgDispatchQueue
+ _OBJC_IVAR_$__TSF_TSDgPTPLocalClockPort._hasLocalClockSourceFromNTP
+ _OBJC_IVAR_$__TSF_TSDgPTPLocalClockPort._hasNtpAnchorOffsetNsec
+ _OBJC_IVAR_$__TSF_TSDgPTPLocalClockPort._localClockSourceFromNTP
+ _OBJC_IVAR_$__TSF_TSDgPTPLocalClockPort._ntpAnchorOffsetNsec
+ _OBJC_METACLASS_$_TSMSGClockSession
+ _OBJC_METACLASS_$_TSMSGService
+ _OUTLINED_FUNCTION_16
+ _OUTLINED_FUNCTION_17
+ _OUTLINED_FUNCTION_18
+ _OUTLINED_FUNCTION_19
+ _OUTLINED_FUNCTION_20
+ _TSMSGNotifyTypeToString.TSMSGNotifyTypeStrings
+ _TimeSyncAddCopresencePTPInstanceRef
+ _TimeSyncAddCopresencePTPInstanceRef.cold.1
+ _TimeSyncGetCopresencePTPInstanceConfiguration
+ _TimeSyncGetCopresencePTPInstanceConfiguration.cold.1
+ _TimeSyncGetCopresencePTPInstanceConfiguration.cold.2
+ _TimeSyncGetCopresencePTPInstanceConfiguration.cold.3
+ _TimeSyncGetCopresencePTPInstanceConfiguration.cold.4
+ _TimeSyncGetCopresencePTPInstanceConfiguration.cold.5
+ _TimeSyncMSGAddClockInstance
+ _TimeSyncMSGAddClockInstanceRef
+ _TimeSyncMSGAddClockInstanceRef.cold.1
+ _TimeSyncMSGAddClockInstance_Rational
+ _TimeSyncMSGAddClockInstance_Rational.cold.1
+ _TimeSyncMSGClockInstanceIdentifier
+ _TimeSyncMSGClockInstanceIdentifier.cold.1
+ _TimeSyncMSGRemoveClockInstance
+ _TimeSyncMSGRemoveClockInstance.cold.1
+ _TimeSyncMSGStartExternalSync
+ _TimeSyncMSGStartExternalSync.cold.1
+ _TimeSyncMSGStopExternalSync
+ _TimeSyncMSGStopExternalSync.cold.1
+ _TimeSyncSetPreferredGM
+ _TimeSyncSetPreferredGM.cold.1
+ _TimeSyncSetPreferredGM.cold.2
+ _TimeSyncUpdateNtpAnchorOffset
+ _TimeSyncUpdateNtpAnchorOffset.cold.1
+ _TimeSyncUpdateNtpAnchorOffset.cold.2
+ __OBJC_$_CATEGORY_CLASS_METHODS_NSValue_$_TSMSGExternalSyncConfig
+ __OBJC_$_CATEGORY_INSTANCE_METHODS_NSValue_$_TSMSGExternalSyncConfig
+ __OBJC_$_CATEGORY_NSValue_$_TSMSGExternalSyncConfig
+ __OBJC_$_CLASS_METHODS_TSMSGClockSession
+ __OBJC_$_CLASS_METHODS_TSMSGService
+ __OBJC_$_INSTANCE_METHODS_TSMSGClockSession
+ __OBJC_$_INSTANCE_METHODS_TSMSGService
+ __OBJC_$_INSTANCE_VARIABLES_TSMSGClockSession
+ __OBJC_$_INSTANCE_VARIABLES_TSMSGService
+ __OBJC_$_PROP_LIST_NSValue_$_TSMSGExternalSyncConfig
+ __OBJC_$_PROP_LIST_TSMSGClockSession
+ __OBJC_CLASS_RO_$_TSMSGClockSession
+ __OBJC_CLASS_RO_$_TSMSGService
+ __OBJC_METACLASS_RO_$_TSMSGClockSession
+ __OBJC_METACLASS_RO_$_TSMSGService
+ ___169-[TSXDaemonServiceClient callMethodForDaemonClient:clientMethodSelector:scalarInputs:scalarInputCount:structInput:structInputSize:scalarOutputs:scalarOutputCount:error:]_block_invoke.97
+ ___30-[TSXDaemonServiceClient init]_block_invoke.88
+ ___32+[TSMSGService sharedMSGService]_block_invoke
+ ___35-[TSMSGService daemonClientRefresh]_block_invoke
+ ___35-[TSMSGService daemonClientRefresh]_block_invoke.cold.1
+ ___35-[TSMSGService daemonClientRefresh]_block_invoke.cold.2
+ ___44-[TSXDaemonServiceClient getMSGClock:error:]_block_invoke
+ ___44-[TSXDaemonServiceClient getMSGClock:error:]_block_invoke.119
+ ___44-[TSXDaemonServiceClient getMSGClock:error:]_block_invoke.cold.1
+ ___46-[TSXDaemonServiceClient stopMSGExternalSync:]_block_invoke
+ ___46-[TSXDaemonServiceClient stopMSGExternalSync:]_block_invoke.118
+ ___46-[TSXDaemonServiceClient stopMSGExternalSync:]_block_invoke.cold.1
+ ___47-[TSXDaemonServiceClient addMSGClockRef:error:]_block_invoke
+ ___47-[TSXDaemonServiceClient addMSGClockRef:error:]_block_invoke.122
+ ___47-[TSXDaemonServiceClient addMSGClockRef:error:]_block_invoke.cold.1
+ ___47-[TSXDaemonServiceClient isMSGServiceAvailable]_block_invoke
+ ___47-[TSXDaemonServiceClient isMSGServiceAvailable]_block_invoke.110
+ ___47-[TSXDaemonServiceClient isMSGServiceAvailable]_block_invoke.cold.1
+ ___47-[TSXDaemonServiceClient removeMSGClock:error:]_block_invoke
+ ___47-[TSXDaemonServiceClient removeMSGClock:error:]_block_invoke.123
+ ___47-[TSXDaemonServiceClient removeMSGClock:error:]_block_invoke.cold.1
+ ___47-[TSXDaemonServiceClient startMSGExternalSync:]_block_invoke
+ ___47-[TSXDaemonServiceClient startMSGExternalSync:]_block_invoke.114
+ ___47-[TSXDaemonServiceClient startMSGExternalSync:]_block_invoke.cold.1
+ ___50-[TSXDaemonServiceClient closeDaemonClient:error:]_block_invoke.94
+ ___55-[TSXDaemonServiceClient propertiesForRegistryEntryID:]_block_invoke.101
+ ___57-[TSXDaemonServiceClient propertyForRegistryEntryID:key:]_block_invoke.105
+ ___68-[TSXDaemonServiceClient addMSGClock:withNominalSyncDuration:error:]_block_invoke
+ ___68-[TSXDaemonServiceClient addMSGClock:withNominalSyncDuration:error:]_block_invoke.121
+ ___68-[TSXDaemonServiceClient addMSGClock:withNominalSyncDuration:error:]_block_invoke.cold.1
+ ___79-[TSXDaemonServiceClient openDaemonClientWithRegistryEntryID:clientType:error:]_block_invoke.91
+ ___86-[TSXDaemonServiceClient restoreMSGClockSession:withNominalSyncDuration:refCnt:error:]_block_invoke
+ ___86-[TSXDaemonServiceClient restoreMSGClockSession:withNominalSyncDuration:refCnt:error:]_block_invoke.124
+ ___86-[TSXDaemonServiceClient restoreMSGClockSession:withNominalSyncDuration:refCnt:error:]_block_invoke.cold.1
+ ___block_descriptor_40_e8_32r_e8_v12?0B8lr32l8
+ ___block_descriptor_40_e8_32r_e8_v12?0I8lr32l8
+ ___block_descriptor_48_e8_32r40r_e20_v24?0Q8"NSError"16lr32l8r40l8
+ ___block_literal_global.100
+ ___block_literal_global.104
+ ___block_literal_global.109
+ ___block_literal_global.113
+ ___block_literal_global.117
+ __os_feature_enabled_impl
+ __sharedMSGService
+ _objc_msgSend$TSMSGExternalSyncConfigValue
+ _objc_msgSend$_hasLocalClockSourceFromNTP
+ _objc_msgSend$_hasNtpAnchorOffsetNsec
+ _objc_msgSend$_localClockSourceFromNTP
+ _objc_msgSend$_ntpAnchorOffsetNsec
+ _objc_msgSend$addCopresencePTPInstance:ntpAndUpTimeOffsetNsec:isLocalClockSourceFromNTP:error:
+ _objc_msgSend$addCopresencePTPInstanceRefWithError:
+ _objc_msgSend$addMSGClock:withNominalSyncDuration:error:
+ _objc_msgSend$addMSGClock:withNominalSyncDuration:reply:
+ _objc_msgSend$addMSGClockRef:error:
+ _objc_msgSend$addMSGClockRef:reply:
+ _objc_msgSend$addPersistentUserFilteredClockRef:error:
+ _objc_msgSend$addPersistentUserFilteredClockWithMachInterval:domainInterval:usingFilterShift:isAdaptive:withUserID:error:
+ _objc_msgSend$dispatchMSGNotification:args:numArgs:
+ _objc_msgSend$dockReplayTimestamps:
+ _objc_msgSend$getMSGClock:error:
+ _objc_msgSend$getMSGClock:reply:
+ _objc_msgSend$getPersistentUserFilteredClockIdentifier:error:
+ _objc_msgSend$getValue:
+ _objc_msgSend$hasLocalClockSourceFromNTP
+ _objc_msgSend$hasNtpAnchorOffsetNsec
+ _objc_msgSend$isMSGServiceAvailable
+ _objc_msgSend$isMSGServiceAvailable:
+ _objc_msgSend$localClockSourceFromNTP
+ _objc_msgSend$longLongValue
+ _objc_msgSend$nominalSyncDuration
+ _objc_msgSend$ntpAnchorOffsetNsec
+ _objc_msgSend$refCnt
+ _objc_msgSend$removeMSGClock:error:
+ _objc_msgSend$removeMSGClock:reply:
+ _objc_msgSend$removePersistentUserFilteredClock:error:
+ _objc_msgSend$restoreMSGClockSession:nominalSyncDuration:refCnt:reply:
+ _objc_msgSend$restoreMSGClockSession:withNominalSyncDuration:refCnt:error:
+ _objc_msgSend$setPreferredGM:error:
+ _objc_msgSend$setRefCnt:
+ _objc_msgSend$sharedMSGService
+ _objc_msgSend$startExternalSync:error:
+ _objc_msgSend$startMSGExternalSync:
+ _objc_msgSend$startMSGExternalSync:reply:
+ _objc_msgSend$startReplayTimestamps:
+ _objc_msgSend$stopExternalSync:error:
+ _objc_msgSend$stopMSGExternalSync:
+ _objc_msgSend$stopMSGExternalSync:reply:
+ _objc_msgSend$stopReplayTimestamps:
+ _objc_msgSend$syncId
+ _objc_msgSend$updateNtpAnchorOffset:isLocalClockSourceFromNTP:error:
+ _objc_msgSend$valueWithBytes:objCType:
+ _objc_msgSend$valuewithTSMSGExternalSyncConfig:
+ _objc_msgSend$withSyncId:nominalSyncDuration:
+ _objc_retain_x6
+ _sharedMSGService.onceToken
- -[TSgPTPManager addCopresencePTPInstance:error:]
- -[_TSF_TSDgPTPManager addCopresencePTPInstance:error:]
- -[_TSF_TSDgPTPManager addCopresencePTPInstance:error:].cold.1
- GCC_except_table32
- GCC_except_table40
- GCC_except_table41
- GCC_except_table47
- GCC_except_table50
- ___169-[TSXDaemonServiceClient callMethodForDaemonClient:clientMethodSelector:scalarInputs:scalarInputCount:structInput:structInputSize:scalarOutputs:scalarOutputCount:error:]_block_invoke.77
- ___30-[TSXDaemonServiceClient init]_block_invoke.68
- ___50-[TSXDaemonServiceClient closeDaemonClient:error:]_block_invoke.74
- ___55-[TSXDaemonServiceClient propertiesForRegistryEntryID:]_block_invoke.81
- ___57-[TSXDaemonServiceClient propertyForRegistryEntryID:key:]_block_invoke.85
- ___79-[TSXDaemonServiceClient openDaemonClientWithRegistryEntryID:clientType:error:]_block_invoke.71
- ___block_literal_global.80
- ___block_literal_global.84
- _objc_msgSend$addCopresencePTPInstance:error:
CStrings:
+ "%@    Local clock source from NTP: "
+ "%@    Ntp anchor offsetNsec: "
+ "%d \n"
+ "%llu"
+ "(ntpAndUpTimeOffsetNsec != nil) && (isLocalClockSourceFromNTP != nil)"
+ ", "
+ "-[TSXDaemonServiceClient addMSGClock:withNominalSyncDuration:error:]_block_invoke"
+ "-[TSXDaemonServiceClient addMSGClockRef:error:]_block_invoke"
+ "-[TSXDaemonServiceClient callMethodForDaemonClient:clientMethodSelector:scalarInputs:scalarInputCount:structInput:structInputSize:scalarOutputs:scalarOutputCount:error:]_block_invoke"
+ "-[TSXDaemonServiceClient closeDaemonClient:error:]_block_invoke"
+ "-[TSXDaemonServiceClient getMSGClock:error:]_block_invoke"
+ "-[TSXDaemonServiceClient isMSGServiceAvailable]_block_invoke"
+ "-[TSXDaemonServiceClient openDaemonClientWithRegistryEntryID:clientType:error:]_block_invoke"
+ "-[TSXDaemonServiceClient propertiesForRegistryEntryID:]_block_invoke"
+ "-[TSXDaemonServiceClient propertyForRegistryEntryID:key:]_block_invoke"
+ "-[TSXDaemonServiceClient removeMSGClock:error:]_block_invoke"
+ "-[TSXDaemonServiceClient restoreMSGClockSession:withNominalSyncDuration:refCnt:error:]_block_invoke"
+ "-[TSXDaemonServiceClient startMSGExternalSync:]_block_invoke"
+ "-[TSXDaemonServiceClient stopMSGExternalSync:]_block_invoke"
+ "/Library/Caches/com.apple.xbs/Sources/TimeSync/TimeSync/API/TSMSGService.m"
+ "@120@0:8{?={?=II{?=QQ}{?=QQ}QQQ*}^?^?^?^?}16"
+ "@36@0:8I16{?=QQ}20"
+ "B24@0:8^v16"
+ "B24@0:8^{?={TSReplayTimestampsHeader=qQQ[13Q][16c]}^{TSReplayTimestampsTimestamp}}16"
+ "B32@0:8r^{?={?=II{?=QQ}{?=QQ}QQQ*}^?^?^?^?}16^@24"
+ "B36@0:8q16B24^@28"
+ "B44@0:8^Q16q24B32^@36"
+ "FAILED to restart MSG clock session for syncId: %u\n"
+ "FAILED to restart MSG external sync session for triggerId: %u\n"
+ "Failed to add Copresence PTP Instance reference count with error 0x%08x\n"
+ "I20@0:8I16"
+ "I24@0:8r^{?=II{?=QQ}{?=QQ}QQQ*}16"
+ "IOTimeSyncTimeOfDayAnchorPort"
+ "Invalid args for TSMSGLockState msg"
+ "Invalid args for TSMSGOutOfBounds msg"
+ "Invalid args for TSMSGSessionStopped msg"
+ "Invalid args for TSMSGTriggerPresent msg"
+ "LocalClockSourceFromNTP"
+ "LockState"
+ "NtpAnchorOffsetNsec"
+ "OutOfBounds"
+ "Q28@0:8I16^@20"
+ "Q32@0:8@16^@24"
+ "Q44@0:8I16{?=QQ}20^@36"
+ "Q52@0:8I16{?=QQ}20Q36^@44"
+ "Q56@0:8Q16Q24C32B36@40^@48"
+ "Received MSG notification: %s\n"
+ "Restarted MSG clock session for syncId: %u\n"
+ "Restarted MSG external sync session for triggerId: %u\n"
+ "SessionStopped"
+ "TB,N,V_hasLocalClockSourceFromNTP"
+ "TB,N,V_hasNtpAnchorOffsetNsec"
+ "TB,N,V_localClockSourceFromNTP"
+ "TI,R,N,V_syncId"
+ "TQ,N,V_refCnt"
+ "TSDgPTPClock setPreferredGm(%u) = %ld"
+ "TSDgPTPClock updateNtpAnchorOffset(%lld %d) = %ld"
+ "TSMSGClockSession"
+ "TSMSGExternalSyncConfig"
+ "TSMSGExternalSyncConfigValue"
+ "TSMSGService"
+ "TSXDaemonServiceClient %s error during call %s"
+ "TimeSyncAddCopresencePTPInstance() = 0x%016llx ntpAndUpTimeOffsetNsec:%lld"
+ "TimeSyncAddCopresencePTPInstanceRef() = %{public}s"
+ "TimeSyncGetCopresencePTPInstanceConfiguration(%p, %lld %d) = %#x"
+ "TimeSyncMSGAddClockInstance(%u, (%llu/%llu)) = 0x%016llx, err: 0x%x"
+ "TimeSyncMSGAddClockInstanceRef(%u) = 0x%016llx, err: 0x%x"
+ "TimeSyncMSGClockInstanceIdentifier(%u) = 0x%016llx, err: 0x%x"
+ "TimeSyncMSGRemoveClockInstance(%u) = %s, err: 0x%x"
+ "TimeSyncSetPreferredGM(%p, %u) = %#x"
+ "TimeSyncStartMSGExternalSync() = %#x"
+ "TimeSyncStopMSGExternalSync() = %#x"
+ "TimeSyncUpdateNtpAnchorOffset(%p, %lld %d) = %#x"
+ "Tq,N,V_ntpAnchorOffsetNsec"
+ "TriggerPresent"
+ "T{?=QQ},R,N,V_nominalSyncDuration"
+ "T{?={?=II{?=QQ}{?=QQ}QQQ*}^?^?^?^?},R"
+ "Unknown/Unsupported TSMSGNotifyType: %u"
+ "[port isKindOfClass:[TSgPTPLocalClockPort class]]"
+ "]\n"
+ "_activeClockSessionsBySyncId"
+ "_activeExtSyncSessionsByTriggerId"
+ "_clockSessionsLock"
+ "_extSyncSessionsLock"
+ "_hasLocalClockSourceFromNTP"
+ "_hasNtpAnchorOffsetNsec"
+ "_localClockSourceFromNTP"
+ "_msgDispatchQueue"
+ "_nominalSyncDuration"
+ "_ntpAnchorOffsetNsec"
+ "_refCnt"
+ "_syncId"
+ "addCopresencePTPInstance:ntpAndUpTimeOffsetNsec:isLocalClockSourceFromNTP:error:"
+ "addCopresencePTPInstanceRefWithError:"
+ "addMSGClock:withNominalSyncDuration:error:"
+ "addMSGClock:withNominalSyncDuration:reply:"
+ "addMSGClockRef:error:"
+ "addMSGClockRef:reply:"
+ "addPersistentUserFilteredClockRef:error:"
+ "addPersistentUserFilteredClockWithMachInterval:domainInterval:usingFilterShift:isAdaptive:withUserID:error:"
+ "args != ((void *)0) && numArgs == 2"
+ "com.apple.TimeSync.%@"
+ "dispatchMSGNotification:args:numArgs:"
+ "dockReplayTimestamps:"
+ "getMSGClock:error:"
+ "getMSGClock:reply:"
+ "getPersistentUserFilteredClockIdentifier:error:"
+ "getValue:"
+ "hasLocalClockSourceFromNTP"
+ "hasNtpAnchorOffsetNsec"
+ "isMSGServiceAvailable"
+ "isMSGServiceAvailable:"
+ "localClockSourceFromNTP"
+ "longLongValue"
+ "msgService"
+ "msgServiceNotification:arguments:"
+ "msgType: %@, args: ["
+ "msg_audio_clock"
+ "msg_ext_sync"
+ "nominalSyncDuration"
+ "ntpAnchorOffsetNsec"
+ "refCnt"
+ "removeMSGClock:error:"
+ "removeMSGClock:reply:"
+ "removePersistentUserFilteredClock:error:"
+ "restoreMSGClockSession:nominalSyncDuration:refCnt:reply:"
+ "restoreMSGClockSession:withNominalSyncDuration:refCnt:error:"
+ "setHasLocalClockSourceFromNTP:"
+ "setHasNtpAnchorOffsetNsec:"
+ "setLocalClockSourceFromNTP:"
+ "setNtpAnchorOffsetNsec:"
+ "setPreferredGM:error:"
+ "setRefCnt:"
+ "sharedMSGService"
+ "startExternalSync:error:"
+ "startMSGExternalSync:"
+ "startMSGExternalSync:reply:"
+ "startReplayTimestamps:"
+ "stopExternalSync:error:"
+ "stopMSGExternalSync:"
+ "stopMSGExternalSync:reply:"
+ "stopReplayTimestamps:"
+ "syncId"
+ "updateNtpAnchorOffset:isLocalClockSourceFromNTP:error:"
+ "v12@?0I8"
+ "v24@0:8@?<v@?B>16"
+ "v24@?0Q8@\"NSError\"16"
+ "v28@0:8I16@?<v@?I>20"
+ "v28@0:8I16@?<v@?Q@\"NSError\">20"
+ "v28@0:8S16r^{ScalarArgsArrayUserReference=[16Q]I}20"
+ "v32@0:8S16r^Q20I28"
+ "v32@0:8r^{?=II{?=QQ}{?=QQ}QQQ*}16@?24"
+ "v32@0:8r^{?=II{?=QQ}{?=QQ}QQQ*}16@?<v@?I>24"
+ "v44@0:8I16{?=QQ}20@?36"
+ "v44@0:8I16{?=QQ}20@?<v@?Q@\"NSError\">36"
+ "v52@0:8I16{?=QQ}20Q36@?44"
+ "v52@0:8I16{?=QQ}20Q36@?<v@?Q@\"NSError\">44"
+ "valueWithBytes:objCType:"
+ "valuewithTSMSGExternalSyncConfig:"
+ "withSyncId:nominalSyncDuration:"
+ "{?=\"numerator\"Q\"denominator\"Q}"
+ "{?={?=II{?=QQ}{?=QQ}QQQ*}^?^?^?^?}"
+ "{?={?=II{?=QQ}{?=QQ}QQQ*}^?^?^?^?}16@0:8"
- "TSXDaemonServiceClient callMethodForDaemonClient:daemonClassName: error during call %s"
- "TSXDaemonServiceClient closeDaemonClient error during call %s"
- "TSXDaemonServiceClient openDaemonClientWithRegistryEntryID error during call %s"
- "TimeSyncAddCopresencePTPInstance() = 0x%016llx"
- "addCopresencePTPInstance:error:"

```
