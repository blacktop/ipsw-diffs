## SiriCrossDeviceArbitration

> `/System/Library/PrivateFrameworks/SiriCrossDeviceArbitration.framework/SiriCrossDeviceArbitration`

```diff

-3405.12.1.0.0
-  __TEXT.__text: 0x311dc
-  __TEXT.__auth_stubs: 0x850
-  __TEXT.__objc_methlist: 0x302c
-  __TEXT.__dlopen_cstrs: 0x164
+3500.47.1.0.0
+  __TEXT.__text: 0x2fba8
+  __TEXT.__auth_stubs: 0x830
+  __TEXT.__objc_methlist: 0x2f14
+  __TEXT.__dlopen_cstrs: 0x118
   __TEXT.__const: 0x1e8
-  __TEXT.__gcc_except_tab: 0x490
-  __TEXT.__oslogstring: 0x5397
-  __TEXT.__cstring: 0x5ad9
-  __TEXT.__unwind_info: 0xcf0
-  __TEXT.__objc_classname: 0x6aa
-  __TEXT.__objc_methname: 0x7cc2
-  __TEXT.__objc_methtype: 0x193f
-  __TEXT.__objc_stubs: 0x5b80
-  __DATA_CONST.__got: 0x320
-  __DATA_CONST.__const: 0x1120
-  __DATA_CONST.__objc_classlist: 0x170
-  __DATA_CONST.__objc_protolist: 0x88
+  __TEXT.__gcc_except_tab: 0x498
+  __TEXT.__oslogstring: 0x52ae
+  __TEXT.__cstring: 0x59d2
+  __TEXT.__unwind_info: 0xc80
+  __TEXT.__objc_classname: 0x5f5
+  __TEXT.__objc_methname: 0x7bcb
+  __TEXT.__objc_methtype: 0x1897
+  __TEXT.__objc_stubs: 0x5a60
+  __DATA_CONST.__got: 0x2f8
+  __DATA_CONST.__const: 0x10f8
+  __DATA_CONST.__objc_classlist: 0x150
+  __DATA_CONST.__objc_protolist: 0x78
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x1d38
-  __DATA_CONST.__objc_superrefs: 0x150
+  __DATA_CONST.__objc_selrefs: 0x1cf8
+  __DATA_CONST.__objc_superrefs: 0x138
   __DATA_CONST.__objc_arraydata: 0xa8
-  __AUTH_CONST.__auth_got: 0x438
+  __AUTH_CONST.__auth_got: 0x428
   __AUTH_CONST.__const: 0x300
-  __AUTH_CONST.__cfstring: 0x26c0
-  __AUTH_CONST.__objc_const: 0x58a0
-  __AUTH_CONST.__objc_intobj: 0x1c8
+  __AUTH_CONST.__cfstring: 0x2700
+  __AUTH_CONST.__objc_const: 0x53d8
+  __AUTH_CONST.__objc_intobj: 0x1e0
   __AUTH_CONST.__objc_dictobj: 0x78
   __AUTH_CONST.__objc_arrayobj: 0xd8
-  __AUTH.__objc_data: 0xa0
-  __DATA.__objc_ivar: 0x53c
-  __DATA.__data: 0x6a8
-  __DATA.__bss: 0x190
-  __DATA_DIRTY.__objc_data: 0xdc0
+  __AUTH.__objc_data: 0x140
+  __DATA.__objc_ivar: 0x4f8
+  __DATA.__data: 0x5d0
+  __DATA.__bss: 0x180
+  __DATA_DIRTY.__objc_data: 0xbe0
   __DATA_DIRTY.__bss: 0x8
   __DATA_DIRTY.__common: 0x10
   - /System/Library/Frameworks/CoreBluetooth.framework/CoreBluetooth

   - /usr/lib/swift/libswiftAccelerate.dylib
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
-  UUID: 1DF21EEC-AEA7-3686-A4EF-DB6482B026C7
-  Functions: 1177
-  Symbols:   4241
-  CStrings:  2939
+  UUID: AA119DAC-A6C1-3E75-BD6B-32B78814CAE0
+  Functions: 1157
+  Symbols:   4124
+  CStrings:  2888
 
Symbols:
+ +[SCDAPerceptualAudioHash _audioHashFileBaseDirectory]
+ +[SCDAPerceptualAudioHash _audioHashFilePath]
+ +[SCDAPerceptualAudioHash tryToRetrieveAudioHashFromFile]
+ +[SCDARecord _generateRandomHash]
+ -[SCDAAssistantPreferences disableRecencyBoost]
+ -[SCDAAssistantPreferences recencyBoostDecayInterval]
+ -[SCDAAssistantPreferences recencyBoostInitialInterval]
+ -[SCDACoordinator rtsTriggerRecord]
+ -[SCDAGoodnessScoreContext adjustedScoreOverride]
+ -[SCDAGoodnessScoreContext setAdjustedScoreOverride:]
+ -[SCDAMonitor beginObserver]
+ -[SCDAMonitor lostObserver]
+ -[SCDAMonitor repostedWonObserver]
+ -[SCDAMonitor setBeginObserver:]
+ -[SCDAMonitor setLostObserver:]
+ -[SCDAMonitor setRepostedWonObserver:]
+ -[SCDAMonitor setWonObserver:]
+ -[SCDAMonitor wonObserver]
+ -[SCDAPerceptualAudioHash _initWithPhash:scoreAudioIntensity:userConfidence:voiceTriggerTime:frac:]
+ -[SCDAPerceptualAudioHash frac]
+ -[SCDAPerceptualAudioHash pHash]
+ -[SCDAPerceptualAudioHash scoreAudioIntensity]
+ -[SCDAPerceptualAudioHash setData:]
+ -[SCDAPerceptualAudioHash setFrac:]
+ -[SCDAPerceptualAudioHash setPHash:]
+ -[SCDAPerceptualAudioHash setScoreAudioIntensity:]
+ -[SCDAPerceptualAudioHash setUserConfidence:]
+ -[SCDAPerceptualAudioHash setVoiceTriggerTime:]
+ -[SCDAPerceptualAudioHash userConfidence]
+ -[SCDAPerceptualAudioHash voiceTriggerTime]
+ -[SCDAPreferences disableRecencyBoost]
+ -[SCDAPreferences recencyBoostDecayInterval]
+ -[SCDARecord context]
+ -[SCDARecord initWithPerceptualAudioHash:]
+ -[SCDARecord isSetup]
+ -[SCDARecord setContext:]
+ -[SCDARecord updateVoiceTriggerTime:]
+ -[SCDARecord voiceTriggerMachTime]
+ GCC_except_table1002
+ GCC_except_table1064
+ GCC_except_table217
+ GCC_except_table223
+ GCC_except_table450
+ GCC_except_table499
+ GCC_except_table500
+ GCC_except_table506
+ GCC_except_table601
+ GCC_except_table709
+ GCC_except_table816
+ GCC_except_table831
+ GCC_except_table881
+ GCC_except_table885
+ GCC_except_table912
+ GCC_except_table961
+ GCC_except_table982
+ _OBJC_IVAR_$_SCDAGoodnessScoreContext._adjustedScoreOverride
+ _OBJC_IVAR_$_SCDAPerceptualAudioHash._frac
+ _OBJC_IVAR_$_SCDAPerceptualAudioHash._pHash
+ _OBJC_IVAR_$_SCDAPerceptualAudioHash._scoreAudioIntensity
+ _OBJC_IVAR_$_SCDAPerceptualAudioHash._userConfidence
+ _OBJC_IVAR_$_SCDAPerceptualAudioHash._voiceTriggerTime
+ _OBJC_IVAR_$_SCDARecord._context
+ _OBJC_IVAR_$_SCDARecord._voiceTriggerMachTime
+ _SCDANextActionWindow
+ __OBJC_$_CLASS_METHODS_SCDARecord
+ __OBJC_$_INSTANCE_METHODS_SCDAPerceptualAudioHash
+ __OBJC_$_PROP_LIST_SCDAAssistantPreferences
+ ___31-[SCDACoordinator _enterState:]_block_invoke.224
+ ___36-[SCDACoordinator _advertiseTrigger]_block_invoke.319
+ ___36-[SCDACoordinator _advertiseTrigger]_block_invoke.322
+ ___36-[SCDACoordinator _advertiseTrigger]_block_invoke.323
+ ___41-[SCDACoordinator _deviceShouldContinue:]_block_invoke
+ ___41-[SCDACoordinator endWaitingForEmergency]_block_invoke
+ ___42-[SCDACoordinator _waitWiProx:andExecute:]_block_invoke.352
+ ___51-[SCDACoordinator _endAdvertisingAnalyticsContext:]_block_invoke.189
+ ___52-[SCDACoordinator _createWaitWiProxTimer:waitBlock:]_block_invoke.351
+ ___56-[SCDAEmergencyCallPunchout initiateEmergencyCallMyriad]_block_invoke.24
+ ___62-[SCDAMonitor notifyObserver:didReceiveNotificationWithToken:]_block_invoke
+ ___89-[SCDACoordinator _advertiseWith:afterDelay:maxInterval:voiceTriggerLatency:thenExecute:]_block_invoke.330
+ ___89-[SCDACoordinator _advertiseWith:afterDelay:maxInterval:voiceTriggerLatency:thenExecute:]_block_invoke.339
+ ___Block_byref_object_copy_.1088
+ ___Block_byref_object_copy_.1620
+ ___Block_byref_object_copy_.2286
+ ___Block_byref_object_dispose_.1089
+ ___Block_byref_object_dispose_.1621
+ ___Block_byref_object_dispose_.2287
+ ___block_descriptor_40_e8_32r_e27_v32?08"SCDARecord"16^B24lr32l8
+ ___block_literal_global.1042
+ ___block_literal_global.1103
+ ___block_literal_global.1137
+ ___block_literal_global.1161
+ ___block_literal_global.1205
+ ___block_literal_global.1498
+ ___block_literal_global.1698
+ ___block_literal_global.216
+ ___block_literal_global.218
+ ___block_literal_global.2278
+ ___block_literal_global.2567
+ ___block_literal_global.343
+ ___block_literal_global.346
+ ___block_literal_global.350
+ ___block_literal_global.443
+ ___block_literal_global.499
+ ___block_literal_global.744
+ __swift_FORCE_LOAD_$_swiftCoreImage
+ __swift_FORCE_LOAD_$_swiftCoreImage_$_SiriCrossDeviceArbitration
+ __swift_FORCE_LOAD_$_swift_DarwinFoundation1
+ __swift_FORCE_LOAD_$_swift_DarwinFoundation1_$_SiriCrossDeviceArbitration
+ __swift_FORCE_LOAD_$_swift_DarwinFoundation2
+ __swift_FORCE_LOAD_$_swift_DarwinFoundation2_$_SiriCrossDeviceArbitration
+ __swift_FORCE_LOAD_$_swift_DarwinFoundation3
+ __swift_FORCE_LOAD_$_swift_DarwinFoundation3_$_SiriCrossDeviceArbitration
+ _objc_msgSend$_audioHashFileBaseDirectory
+ _objc_msgSend$_audioHashFilePath
+ _objc_msgSend$_generateRandomHash
+ _objc_msgSend$adjustedScoreOverride
+ _objc_msgSend$disableRecencyBoost
+ _objc_msgSend$frac
+ _objc_msgSend$initWithPerceptualAudioHash:
+ _objc_msgSend$isSetup
+ _objc_msgSend$numberWithChar:
+ _objc_msgSend$recencyBoostDecayInterval
+ _objc_msgSend$recencyBoostInitialInterval
+ _objc_msgSend$removeAllObjects
+ _objc_msgSend$rtsTriggerRecord
+ _objc_msgSend$scoreAudioIntensity
+ _objc_msgSend$setAdjustedScoreOverride:
+ _objc_msgSend$setContext:
+ _objc_msgSend$setFrac:
+ _objc_msgSend$setScoreAudioIntensity:
+ _objc_msgSend$setVoiceTriggerTime:
+ _objc_msgSend$timeIntervalSinceDate:
+ _objc_msgSend$tryToRetrieveAudioHashFromFile
+ _objc_msgSend$unsignedCharValue
+ _objc_msgSend$updateVoiceTriggerTime:
+ _objc_msgSend$voiceTriggerMachTime
+ _objc_msgSend$voiceTriggerTime
- +[SCDACoordinator audioHashFileBaseDirectory]
- +[SCDACoordinator audioHashFilePath]
- +[SCDACoordinator safelyGetAudioData]
- +[SCDAPerceptualAudioHash newWithBuilder:]
- -[SCDACoordinator _enterBLEDiagnosticMode]
- -[SCDACoordinator _initDeviceClassAndAdjustments]
- -[SCDACoordinator _leaveBLEDiagnosticMode]
- -[SCDACoordinator _resetAudioData]
- -[SCDACoordinator _startListenTimer]
- -[SCDACoordinator _updateVoiceTriggerTimeFromFile]
- -[SCDAGoodnessScoreContext getOverridingContext]
- -[SCDAGoodnessScoreContext setOverridingContext:]
- -[SCDAGoodnessScoreOverrideContext overriddenAdjustedScore]
- -[SCDAGoodnessScoreOverrideContext overrideContext]
- -[SCDAGoodnessScoreOverrideContext setOverriddenAdjustedScore:]
- -[SCDAGoodnessScoreOverrideContext setOverrideContext:]
- -[SCDALinkedListItem .cxx_destruct]
- -[SCDALinkedListItem initWithObject:]
- -[SCDALinkedListItem insertAfterItem:]
- -[SCDALinkedListItem insertBeforeItem:]
- -[SCDALinkedListItem nextItem]
- -[SCDALinkedListItem object]
- -[SCDALinkedListItem previousItem]
- -[SCDALinkedListItem removeFromList]
- -[SCDALinkedListItem setNextItem:]
- -[SCDALinkedListItem setPreviousItem:]
- -[SCDAMonitor _ignoreRepostMyriadNotification:]
- -[SCDAMonitor startMonitoringWithTimeoutInterval:]
- -[SCDAMonitor waitForMyriadDecisionWithCompletion:]
- -[SCDAPerceptualAudioHash _descriptionWithIndent:]
- -[SCDAPerceptualAudioHash initWithBuilder:]
- -[SCDAPerceptualAudioHash init]
- -[SCDAPerceptualAudioHash(SCDAPerceptualAudioHashMutability) mutatedCopyWithMutator:]
- -[SCDAQueue .cxx_destruct]
- -[SCDAQueue _objects]
- -[SCDAQueue countByEnumeratingWithState:objects:count:]
- -[SCDAQueue count]
- -[SCDAQueue dealloc]
- -[SCDAQueue delegate]
- -[SCDAQueue dequeueAllObjects]
- -[SCDAQueue dequeueObject]
- -[SCDAQueue description]
- -[SCDAQueue enqueueObject:]
- -[SCDAQueue enqueueObjects:]
- -[SCDAQueue frontObject]
- -[SCDAQueue objectAtIndex:]
- -[SCDAQueue setDelegate:]
- -[SCDARecord initWithAudioData:]
- -[SCDARecord init]
- -[_SCDAPerceptualAudioHashMutation .cxx_destruct]
- -[_SCDAPerceptualAudioHashMutation getData]
- -[_SCDAPerceptualAudioHashMutation initWithBase:]
- -[_SCDAPerceptualAudioHashMutation isDirty]
- -[_SCDAPerceptualAudioHashMutation setData:]
- GCC_except_table1021
- GCC_except_table1085
- GCC_except_table213
- GCC_except_table219
- GCC_except_table439
- GCC_except_table502
- GCC_except_table503
- GCC_except_table509
- GCC_except_table608
- GCC_except_table716
- GCC_except_table829
- GCC_except_table844
- GCC_except_table851
- GCC_except_table899
- GCC_except_table903
- GCC_except_table930
- GCC_except_table980
- _OBJC_CLASS_$_SCDAGoodnessScoreOverrideContext
- _OBJC_CLASS_$_SCDALinkedListItem
- _OBJC_CLASS_$_SCDAQueue
- _OBJC_CLASS_$__SCDAPerceptualAudioHashMutation
- _OBJC_IVAR_$_SCDACoordinator._center
- _OBJC_IVAR_$_SCDACoordinator._clientIsListeningAfterRecentWin
- _OBJC_IVAR_$_SCDACoordinator._clientIsWatchTrumpPromote
- _OBJC_IVAR_$_SCDACoordinator._clientLostDueToTrumping
- _OBJC_IVAR_$_SCDACoordinator._clientRecentlyLostElection
- _OBJC_IVAR_$_SCDACoordinator._listenTimerIsRunning
- _OBJC_IVAR_$_SCDACoordinator._nDeltaTs
- _OBJC_IVAR_$_SCDACoordinator._sfDiagnosticsTimer
- _OBJC_IVAR_$_SCDACoordinator._sfdiagnostics
- _OBJC_IVAR_$_SCDACoordinator._timerSource
- _OBJC_IVAR_$_SCDACoordinator._voiceTriggerTime
- _OBJC_IVAR_$_SCDAGoodnessScoreContext._overriddenContext
- _OBJC_IVAR_$_SCDAGoodnessScoreOverrideContext._overriddenAdjustedScore
- _OBJC_IVAR_$_SCDAGoodnessScoreOverrideContext._overrideContext
- _OBJC_IVAR_$_SCDALinkedListItem._nextItem
- _OBJC_IVAR_$_SCDALinkedListItem._object
- _OBJC_IVAR_$_SCDALinkedListItem._previousItem
- _OBJC_IVAR_$_SCDAMonitor._ignoreRepostMyriadNotification
- _OBJC_IVAR_$_SCDAQueue._count
- _OBJC_IVAR_$_SCDAQueue._delegate
- _OBJC_IVAR_$_SCDAQueue._head
- _OBJC_IVAR_$_SCDAQueue._tail
- _OBJC_IVAR_$__SCDAPerceptualAudioHashMutation._base
- _OBJC_IVAR_$__SCDAPerceptualAudioHashMutation._data
- _OBJC_IVAR_$__SCDAPerceptualAudioHashMutation._mutationFlags
- _OBJC_METACLASS_$_SCDAGoodnessScoreOverrideContext
- _OBJC_METACLASS_$_SCDALinkedListItem
- _OBJC_METACLASS_$_SCDAQueue
- _OBJC_METACLASS_$__SCDAPerceptualAudioHashMutation
- _SharingLibraryCore.frameworkLibrary
- __OBJC_$_INSTANCE_METHODS_SCDAGoodnessScoreOverrideContext
- __OBJC_$_INSTANCE_METHODS_SCDALinkedListItem
- __OBJC_$_INSTANCE_METHODS_SCDAPerceptualAudioHash(SCDAPerceptualAudioHashMutability)
- __OBJC_$_INSTANCE_METHODS_SCDAQueue
- __OBJC_$_INSTANCE_METHODS__SCDAPerceptualAudioHashMutation
- __OBJC_$_INSTANCE_VARIABLES_SCDAGoodnessScoreOverrideContext
- __OBJC_$_INSTANCE_VARIABLES_SCDALinkedListItem
- __OBJC_$_INSTANCE_VARIABLES_SCDAQueue
- __OBJC_$_INSTANCE_VARIABLES__SCDAPerceptualAudioHashMutation
- __OBJC_$_PROP_LIST_SCDAGoodnessScoreOverrideContext
- __OBJC_$_PROP_LIST_SCDALinkedListItem
- __OBJC_$_PROP_LIST_SCDAQueue
- __OBJC_$_PROP_LIST__SCDAPerceptualAudioHashMutation
- __OBJC_$_PROTOCOL_INSTANCE_METHODS_NSFastEnumeration
- __OBJC_$_PROTOCOL_INSTANCE_METHODS_SCDAPerceptualAudioHashMutating
- __OBJC_$_PROTOCOL_METHOD_TYPES_NSFastEnumeration
- __OBJC_$_PROTOCOL_METHOD_TYPES_SCDAPerceptualAudioHashMutating
- __OBJC_$_PROTOCOL_REFS_SCDAPerceptualAudioHashMutating
- __OBJC_CLASS_PROTOCOLS_$_SCDAQueue
- __OBJC_CLASS_PROTOCOLS_$__SCDAPerceptualAudioHashMutation
- __OBJC_CLASS_RO_$_SCDAGoodnessScoreOverrideContext
- __OBJC_CLASS_RO_$_SCDALinkedListItem
- __OBJC_CLASS_RO_$_SCDAQueue
- __OBJC_CLASS_RO_$__SCDAPerceptualAudioHashMutation
- __OBJC_LABEL_PROTOCOL_$_NSFastEnumeration
- __OBJC_LABEL_PROTOCOL_$_SCDAPerceptualAudioHashMutating
- __OBJC_METACLASS_RO_$_SCDAGoodnessScoreOverrideContext
- __OBJC_METACLASS_RO_$_SCDALinkedListItem
- __OBJC_METACLASS_RO_$_SCDAQueue
- __OBJC_METACLASS_RO_$__SCDAPerceptualAudioHashMutation
- __OBJC_PROTOCOL_$_NSFastEnumeration
- __OBJC_PROTOCOL_$_SCDAPerceptualAudioHashMutating
- ___31-[SCDACoordinator _enterState:]_block_invoke.239
- ___36-[SCDACoordinator _advertiseTrigger]_block_invoke.335
- ___36-[SCDACoordinator _advertiseTrigger]_block_invoke.338
- ___36-[SCDACoordinator _advertiseTrigger]_block_invoke.339
- ___40-[SCDAPerceptualAudioHash initWithData:]_block_invoke
- ___42-[SCDACoordinator _enterBLEDiagnosticMode]_block_invoke
- ___42-[SCDACoordinator _enterBLEDiagnosticMode]_block_invoke.375
- ___42-[SCDACoordinator _waitWiProx:andExecute:]_block_invoke.369
- ___47-[SCDAMonitor _ignoreRepostMyriadNotification:]_block_invoke
- ___51-[SCDACoordinator _endAdvertisingAnalyticsContext:]_block_invoke.202
- ___51-[SCDAMonitor waitForMyriadDecisionWithCompletion:]_block_invoke
- ___52-[SCDACoordinator _createWaitWiProxTimer:waitBlock:]_block_invoke.368
- ___56-[SCDAEmergencyCallPunchout initiateEmergencyCallMyriad]_block_invoke.6
- ___89-[SCDACoordinator _advertiseWith:afterDelay:maxInterval:voiceTriggerLatency:thenExecute:]_block_invoke.346
- ___89-[SCDACoordinator _advertiseWith:afterDelay:maxInterval:voiceTriggerLatency:thenExecute:]_block_invoke.355
- ___Block_byref_object_copy_.1095
- ___Block_byref_object_copy_.1670
- ___Block_byref_object_copy_.2378
- ___Block_byref_object_dispose_.1096
- ___Block_byref_object_dispose_.1671
- ___Block_byref_object_dispose_.2379
- ___SharingLibraryCore_block_invoke
- ___assert_rtn
- ___block_descriptor_40_e8_32s_e43_v16?0"<SCDAPerceptualAudioHashMutating>"8ls32l8
- ___block_literal_global.1046
- ___block_literal_global.1129
- ___block_literal_global.1211
- ___block_literal_global.1236
- ___block_literal_global.1276
- ___block_literal_global.1543
- ___block_literal_global.1748
- ___block_literal_global.228
- ___block_literal_global.230
- ___block_literal_global.2370
- ___block_literal_global.2660
- ___block_literal_global.360
- ___block_literal_global.363
- ___block_literal_global.367
- ___block_literal_global.453
- ___block_literal_global.511
- ___block_literal_global.750
- ___getSFDiagnosticsClass_block_invoke
- __swift_FORCE_LOAD_$_swift_errno
- __swift_FORCE_LOAD_$_swift_errno_$_SiriCrossDeviceArbitration
- __swift_FORCE_LOAD_$_swift_math
- __swift_FORCE_LOAD_$_swift_math_$_SiriCrossDeviceArbitration
- __swift_FORCE_LOAD_$_swift_signal
- __swift_FORCE_LOAD_$_swift_signal_$_SiriCrossDeviceArbitration
- __swift_FORCE_LOAD_$_swift_stdio
- __swift_FORCE_LOAD_$_swift_stdio_$_SiriCrossDeviceArbitration
- __swift_FORCE_LOAD_$_swift_time
- __swift_FORCE_LOAD_$_swift_time_$_SiriCrossDeviceArbitration
- __swift_FORCE_LOAD_$_swiftsys_time
- __swift_FORCE_LOAD_$_swiftsys_time_$_SiriCrossDeviceArbitration
- __swift_FORCE_LOAD_$_swiftunistd
- __swift_FORCE_LOAD_$_swiftunistd_$_SiriCrossDeviceArbitration
- _audit_stringSharing
- _extractMyriadDataFromAudioContext
- _getSFDiagnosticsClass.softClass
- _objc_msgSend$_enterBLEDiagnosticMode
- _objc_msgSend$_initDeviceClassAndAdjustments
- _objc_msgSend$_leaveBLEDiagnosticMode
- _objc_msgSend$_objects
- _objc_msgSend$_resetAudioData
- _objc_msgSend$_updateVoiceTriggerTimeFromFile
- _objc_msgSend$audioHashFileBaseDirectory
- _objc_msgSend$audioHashFilePath
- _objc_msgSend$compare:
- _objc_msgSend$dateWithTimeInterval:sinceDate:
- _objc_msgSend$delegate
- _objc_msgSend$dequeueAllObjects
- _objc_msgSend$diagnosticBLEModeWithCompletion:
- _objc_msgSend$enqueueObject:
- _objc_msgSend$enqueueObjects:
- _objc_msgSend$getData
- _objc_msgSend$getOverridingContext
- _objc_msgSend$initWithAudioData:
- _objc_msgSend$initWithObject:
- _objc_msgSend$insertAfterItem:
- _objc_msgSend$nextItem
- _objc_msgSend$object
- _objc_msgSend$overriddenAdjustedScore
- _objc_msgSend$previousItem
- _objc_msgSend$queue:didEnqueueObjects:
- _objc_msgSend$removeFromList
- _objc_msgSend$safelyGetAudioData
- _objc_msgSend$setDispatchQueue:
- _objc_msgSend$setNextItem:
- _objc_msgSend$setOverriddenAdjustedScore:
- _objc_msgSend$setOverrideContext:
- _objc_msgSend$setOverridingContext:
- _objc_msgSend$setPreviousItem:
- _objc_msgSend$startMonitoringWithTimeoutInterval:instanceContext:
- _objc_unsafeClaimAutoreleasedReturnValue
- _scda_attention_queue_label
- _scda_readiness_queue_label
- _scda_timer_mgmt_queue_label
CStrings:
+ "%s #scda BTLE could open audio data file, MYR_EXT_FINGERPRINT_LEN: %zd"
+ "%s #scda adjustedScoreOverride: %@, _incomingAdjustment %d"
+ "%s #scda recency boost disabled, clearing it %f -> 0"
+ "%s #scda voice trigger is invalid, resetting: %f"
+ "%s Attempting to end emergency while in no activity state, ignoring."
+ "%s BTLE deviceShouldContinue:%ld coordinationDisabled:%ld, isDirectlyActivating:%ld, isInEarTrigger:%ld, suppressLateTrigger:%ld setupRecordSuppression:%ld."
+ "%s Configured RAISE_TO_SPEAK record"
+ "%s Data Length: %d"
+ "%s Ending Emergency Flow Early"
+ "%s Invalid perceptual audio hash: %{public}@"
+ "%s Perceptual Audio hash with no VT time, trying to read from file."
+ "%s Perceptual audio hash was missing, trying to update from file with result: %@"
+ "%s Received notification of unregistered observer"
+ "%s Setting Emergency Continuation to End Early"
+ "%s Setup record found while detecting attention, losing election"
+ "+[SCDAPerceptualAudioHash _audioHashFileBaseDirectory]"
+ "+[SCDAPerceptualAudioHash _audioHashFilePath]"
+ "+[SCDAPerceptualAudioHash tryToRetrieveAudioHashFromFile]"
+ "+[SCDARecord _generateRandomHash]"
+ "-[SCDACoordinator _deviceShouldContinue:]_block_invoke"
+ "-[SCDACoordinator endWaitingForEmergency]_block_invoke"
+ "-[SCDAMonitor notifyObserver:didReceiveNotificationWithToken:]_block_invoke"
+ "-[SCDAPerceptualAudioHash initWithData:]"
+ "-[SCDARecord updateVoiceTriggerTime:]"
+ "@\"NSMutableArray\""
+ "@40@0:8S16C20C24Q28C36"
+ "Myriad Disable Recency Boost"
+ "Myriad Recency Boost Decay Interval"
+ "Myriad Recency Boost Initial Interval"
+ "Overridden Device"
+ "Overridden Product"
+ "T@\"NSData\",C,N,V_data"
+ "T@\"NSNumber\",&,N,V_adjustedScoreOverride"
+ "T@\"SCDANotifyObserver\",&,N,V_beginObserver"
+ "T@\"SCDANotifyObserver\",&,N,V_lostObserver"
+ "T@\"SCDANotifyObserver\",&,N,V_repostedWonObserver"
+ "T@\"SCDANotifyObserver\",&,N,V_wonObserver"
+ "TC,N,V_frac"
+ "TC,N,V_scoreAudioIntensity"
+ "TQ,N,V_context"
+ "TQ,N,V_voiceTriggerTime"
+ "TQ,R,N,V_voiceTriggerMachTime"
+ "_adjustedScoreOverride"
+ "_audioHashFileBaseDirectory"
+ "_audioHashFilePath"
+ "_frac"
+ "_initWithPhash:scoreAudioIntensity:userConfidence:voiceTriggerTime:frac:"
+ "_scoreAudioIntensity"
+ "_voiceTriggerMachTime"
+ "adjustedScoreOverride"
+ "beginObserver"
+ "disableRecencyBoost"
+ "frac"
+ "hash:%hu, audio:%d, uc:%d, frac:%d, vtt:%llu, remaining:%f"
+ "initWithPerceptualAudioHash:"
+ "isSetup"
+ "lostObserver"
+ "numberWithChar:"
+ "raiseToSpeak"
+ "recencyBoostDecayInterval"
+ "recencyBoostInitialInterval"
+ "removeAllObjects"
+ "repostedWonObserver"
+ "rtsTriggerRecord"
+ "scoreAudioIntensity"
+ "setAdjustedScoreOverride:"
+ "setBeginObserver:"
+ "setContext:"
+ "setFrac:"
+ "setLostObserver:"
+ "setRepostedWonObserver:"
+ "setScoreAudioIntensity:"
+ "setVoiceTriggerTime:"
+ "setWonObserver:"
+ "timeIntervalSinceDate:"
+ "tryToRetrieveAudioHashFromFile"
+ "unsignedCharValue"
+ "updateVoiceTriggerTime:"
+ "voiceTriggerMachTime"
+ "voiceTriggerTime"
+ "wonObserver"
- " %@"
- "#"
- "%@ {data = (%llu bytes)}"
- "%s #scda BTLE could not open audio data file"
- "%s #scda BTLE could open audio data file, MYR_EXT_FINGERPRINT_LEN: %d"
- "%s #scda election time remaining from a file is too old, Siri might respond from multiple devices"
- "%s #scda endTime from a file is good, electionTimeRemaining=%f"
- "%s #scda overrideContext: %@, _incomingAdjustment %d"
- "%s BTLE added diagnostic mode timer for %f seconds %@"
- "%s BTLE cancelling diagnostic mode timer for %f seconds %@"
- "%s BTLE deviceShouldContinue:%ld (coordinationDisabled:%ld, isDirectlyActivating:%ld, isInEarTrigger:%ld, suppressLateTrigger:%ld."
- "%s BTLE diagnostic mode timer fired"
- "%s BTLE entering diagnostic mode"
- "%s BTLE failed to enter diagnostic mode %@"
- "%s BTLE leaving diagnostic mode"
- "%s Dropping stale VT: %f"
- "%s Ending Continuation Early"
- "%s Myriad Delay Monitor: Ignoring Myriad repost notifications."
- "%s SCDARecord initfrom: <THISDEVICE> - %@"
- "%s SCDARecord invalid data during init: %@"
- "%s Voice trigger time not found in file."
- "%s currentTime=%llu timeSinceActivationInSeconds=%f"
- "%s data=%@, hash=%hu, good=%hu, conf=%hu, absTime=%llu, frac=%hu"
- "%s endWaitingForEmergency called from invalid state: %@"
- "+[SCDACoordinator audioHashFileBaseDirectory]"
- "+[SCDACoordinator audioHashFilePath]"
- "+[SCDACoordinator safelyGetAudioData]"
- "-[SCDACoordinator _enterBLEDiagnosticMode]"
- "-[SCDACoordinator _enterBLEDiagnosticMode]_block_invoke"
- "-[SCDACoordinator _initDeviceClassAndAdjustments]"
- "-[SCDACoordinator _leaveBLEDiagnosticMode]"
- "-[SCDACoordinator _updateVoiceTriggerTimeFromFile]"
- "-[SCDACoordinator directTriggerRecord]"
- "-[SCDACoordinator endWaitingForEmergency]"
- "-[SCDACoordinator voiceTriggerRecord]"
- "-[SCDAMonitor _fetchCurrentMyriadDecisionWithWaitTime:]"
- "-[SCDAMonitor notifyObserver:didReceiveNotificationWithToken:]"
- "-[SCDARecord initWithAudioData:]"
- "1"
- "@\"<SCDAQueueDelegate>\""
- "@\"SCDAGoodnessScoreOverrideContext\""
- "@\"SCDALinkedListItem\""
- "@\"SCDAQueue\""
- "@\"SFDiagnostics\""
- "NSFastEnumeration"
- "Overriden Device"
- "Overriden Product"
- "Q40@0:8^{?=Q^@^Q[5Q]}16^@24Q32"
- "SCDACoordinator.m"
- "SCDAGoodnessScoreOverrideContext"
- "SCDALinkedListItem"
- "SCDAPerceptualAudioHashMutability"
- "SCDAPerceptualAudioHashMutating"
- "SCDAQueue"
- "SFDiagnostics"
- "T@\"<SCDAQueueDelegate>\",W,N,V_delegate"
- "T@\"NSData\",R,C,N,V_data"
- "T@\"SCDALinkedListItem\",&,N,V_nextItem"
- "T@\"SCDALinkedListItem\",&,N,V_previousItem"
- "T@,R,N"
- "T@,R,N,V_object"
- "TB,N,V_overrideContext"
- "TC,N,V_overriddenAdjustedScore"
- "^{__CFNotificationCenter=}"
- "_SCDAPerceptualAudioHashMutation"
- "_center"
- "_clientIsListeningAfterRecentWin"
- "_clientIsWatchTrumpPromote"
- "_clientLostDueToTrumping"
- "_clientRecentlyLostElection"
- "_count"
- "_enterBLEDiagnosticMode"
- "_head"
- "_ignoreRepostMyriadNotification"
- "_ignoreRepostMyriadNotification:"
- "_initDeviceClassAndAdjustments"
- "_leaveBLEDiagnosticMode"
- "_listenTimerIsRunning"
- "_nDeltaTs"
- "_nextItem"
- "_object"
- "_objects"
- "_overriddenAdjustedScore"
- "_overriddenContext"
- "_overrideContext"
- "_previousItem"
- "_resetAudioData"
- "_sfDiagnosticsTimer"
- "_sfdiagnostics"
- "_startListenTimer"
- "_tail"
- "_updateVoiceTriggerTimeFromFile"
- "audioHashFileBaseDirectory"
- "audioHashFilePath"
- "com.apple.myriad_attention"
- "com.apple.myriad_readiness"
- "com.apple.myriad_timer_mgmt"
- "compare:"
- "dateWithTimeInterval:sinceDate:"
- "delegate"
- "dequeueAllObjects"
- "dequeueObject"
- "diagnosticBLEModeWithCompletion:"
- "enqueueObject:"
- "enqueueObjects:"
- "extractMyriadDataFromAudioContext"
- "frontObject"
- "getData"
- "getOverridingContext"
- "initWithAudioData:"
- "initWithObject:"
- "insertAfterItem:"
- "insertBeforeItem:"
- "listen"
- "nextItem"
- "object"
- "overriddenAdjustedScore"
- "overrideContext"
- "previousItem"
- "queue:didEnqueueObjects:"
- "removeFromList"
- "safelyGetAudioData"
- "setDelegate:"
- "setDispatchQueue:"
- "setNextItem:"
- "setOverriddenAdjustedScore:"
- "setOverrideContext:"
- "setOverridingContext:"
- "setPreviousItem:"
- "softlink:r:path:/System/Library/PrivateFrameworks/Sharing.framework/Sharing"
- "startMonitoringWithTimeoutInterval:"
- "v16@?0@\"<SCDAPerceptualAudioHashMutating>\"8"
- "waitForMyriadDecisionWithCompletion:"
- "{_mutationFlags=\"isDirty\"b1\"hasData\"b1}"

```
