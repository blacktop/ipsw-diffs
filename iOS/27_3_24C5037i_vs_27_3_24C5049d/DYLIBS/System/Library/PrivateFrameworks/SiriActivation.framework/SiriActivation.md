## SiriActivation

> `/System/Library/PrivateFrameworks/SiriActivation.framework/SiriActivation`

```diff

-3610.10.1.0.0
-  __TEXT.__text: 0x75d64
-  __TEXT.__objc_methlist: 0x75c4
-  __TEXT.__const: 0x124c
-  __TEXT.__cstring: 0xd522
-  __TEXT.__oslogstring: 0x9e27
-  __TEXT.__gcc_except_tab: 0xd90
+3610.17.2.0.0
+  __TEXT.__text: 0x79330
+  __TEXT.__objc_methlist: 0x777c
+  __TEXT.__const: 0x1328
+  __TEXT.__cstring: 0xdaa6
+  __TEXT.__oslogstring: 0x9f95
+  __TEXT.__gcc_except_tab: 0xdf0
   __TEXT.__dlopen_cstrs: 0x1bc
-  __TEXT.__swift5_typeref: 0x77a
-  __TEXT.__constg_swiftt: 0x42c
-  __TEXT.__swift5_reflstr: 0x241
-  __TEXT.__swift5_fieldmd: 0x1b0
-  __TEXT.__swift5_builtin: 0x50
-  __TEXT.__swift5_types: 0x28
+  __TEXT.__swift5_typeref: 0x822
+  __TEXT.__constg_swiftt: 0x49c
+  __TEXT.__swift5_reflstr: 0x290
+  __TEXT.__swift5_fieldmd: 0x21c
+  __TEXT.__swift5_builtin: 0x64
+  __TEXT.__swift5_types: 0x34
   __TEXT.__swift5_assocty: 0x30
-  __TEXT.__swift5_capture: 0x508
+  __TEXT.__swift5_capture: 0x534
   __TEXT.__swift5_proto: 0x2c
   __TEXT.__swift_as_entry: 0x78
   __TEXT.__swift_as_ret: 0x6c
   __TEXT.__swift5_protos: 0xc
   __TEXT.__swift5_mpenum: 0x14
   __TEXT.__swift_as_cont: 0x8c
-  __TEXT.__unwind_info: 0x2808
+  __TEXT.__unwind_info: 0x2930
   __TEXT.__eh_frame: 0xf58
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0
   __TEXT.__objc_classname: 0x0
   __TEXT.__objc_methname: 0x0
   __TEXT.__objc_methtype: 0x0
-  __DATA_CONST.__const: 0x1978
-  __DATA_CONST.__objc_classlist: 0x3b8
+  __DATA_CONST.__const: 0x19f0
+  __DATA_CONST.__objc_classlist: 0x3c0
   __DATA_CONST.__objc_catlist: 0x18
-  __DATA_CONST.__objc_protolist: 0x1e0
+  __DATA_CONST.__objc_protolist: 0x1f0
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x3790
-  __DATA_CONST.__objc_protorefs: 0x68
+  __DATA_CONST.__objc_selrefs: 0x3988
+  __DATA_CONST.__objc_protorefs: 0x70
   __DATA_CONST.__objc_superrefs: 0x2f8
   __DATA_CONST.__objc_arraydata: 0x510
-  __DATA_CONST.__got: 0xac0
-  __AUTH_CONST.__const: 0x14f0
-  __AUTH_CONST.__cfstring: 0x52c0
-  __AUTH_CONST.__objc_const: 0xbbb0
+  __DATA_CONST.__got: 0xb00
+  __AUTH_CONST.__const: 0x16b0
+  __AUTH_CONST.__cfstring: 0x5560
+  __AUTH_CONST.__objc_const: 0xbef8
   __AUTH_CONST.__objc_intobj: 0x978
   __AUTH_CONST.__objc_dictobj: 0x118
-  __AUTH_CONST.__auth_got: 0xc08
-  __AUTH.__objc_data: 0x2230
-  __AUTH.__data: 0x118
-  __DATA.__objc_ivar: 0x7a4
-  __DATA.__data: 0x1710
+  __AUTH_CONST.__auth_got: 0xc60
+  __AUTH.__objc_data: 0x22e8
+  __AUTH.__data: 0x148
+  __DATA.__objc_ivar: 0x7c4
+  __DATA.__data: 0x17e0
   __DATA.__common: 0x270
   __DATA_DIRTY.__objc_data: 0x5f0
   __DATA_DIRTY.__bss: 0x10

   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  Functions: 3057
-  Symbols:   4876
-  CStrings:  1903
+  Functions: 3129
+  Symbols:   4972
+  CStrings:  1949
 
Symbols:
+ +[SASDeviceSelectionShadowController comparisonOutcomeWhenAsked:hasAnswered:hasError:isWin:]
+ +[SRUIFIntelligenceFlowFeatureFlag(SWEFeatureFlags) isIntercomPlannerToolsEnabled]
+ +[SiriDirectActionContext isIntercomPlannerToolsEnabled]
+ -[SASDeviceSelectionController _isDeviceSelectionParticipating]
+ -[SASDeviceSelectionController activateForRequest:withTimeout:visible:idleAndQuiet:electionGeneration:]
+ -[SASDeviceSelectionController lastAnsweredElectionGeneration]
+ -[SASDeviceSelectionController lastAnsweredElectionIsWin]
+ -[SASDeviceSelectionController lastLocalScore]
+ -[SASDeviceSelectionController lastSelectionError]
+ -[SASDeviceSelectionShadowController _askDeviceSelection:withTimeout:visible:idleAndQuiet:generation:]
+ -[SASDeviceSelectionShadowController _logShadowComparison]
+ -[SASDeviceSelectionShadowController _shadowScoreBoostsFrom:]
+ -[SASMyriadController _applyFetchedAlarms:]
+ -[SASMyriadController _applyFetchedTimers:]
+ -[SASMyriadController _fetchAlarms]
+ -[SASMyriadController _fetchTimers]
+ -[SASMyriadController _forgetRemovedAlarms:]
+ -[SASMyriadController _forgetRemovedTimers:]
+ -[SASMyriadController _refetchFiringAlarms]
+ -[SASMyriadController _refetchFiringTimers]
+ -[SASMyriadController alarmsRemoved:]
+ -[SASMyriadController myriadCdaId]
+ -[SASMyriadController scdaWillStartWithSession:]
+ -[SASMyriadController timersRemoved:]
+ -[SASSystemState hasMultipleLogicalDisplays]
+ GCC_except_table23
+ GCC_except_table30
+ GCC_except_table31
+ GCC_except_table36
+ GCC_except_table37
+ GCC_except_table46
+ GCC_except_table47
+ GCC_except_table52
+ GCC_except_table60
+ GCC_except_table61
+ GCC_except_table62
+ GCC_except_table66
+ GCC_except_table70
+ GCC_except_table77
+ _MGGetLogicalDeviceDisplayCount
+ _OBJC_CLASS_$_CDASchemaCDAClientEvent
+ _OBJC_CLASS_$_CDASchemaCDAClientEventMetadata
+ _OBJC_CLASS_$_CDASchemaCDADeviceSelectionDecisionMade
+ _OBJC_CLASS_$_CDASchemaCDADeviceSelectionScoreBoosts
+ _OBJC_CLASS_$_SASRequestTransactionController
+ _OBJC_CLASS_$_SCDADevice
+ _OBJC_CLASS_$_SISchemaErrorInfo
+ _OBJC_IVAR_$_SASDeviceSelectionController._lastAnsweredElectionGeneration
+ _OBJC_IVAR_$_SASDeviceSelectionController._lastAnsweredElectionIsWin
+ _OBJC_IVAR_$_SASDeviceSelectionController._lastLocalScore
+ _OBJC_IVAR_$_SASDeviceSelectionController._lastSelectionError
+ _OBJC_IVAR_$_SASDeviceSelectionShadowController._activationGeneration
+ _OBJC_IVAR_$_SASDeviceSelectionShadowController._deviceSelectionAskedGeneration
+ _OBJC_IVAR_$_SASDeviceSelectionShadowController._generationLock
+ _OBJC_IVAR_$_SASDeviceSelectionShadowController._loggedGeneration
+ _OBJC_IVAR_$_SASMyriadController._myriadCdaId
+ _OBJC_METACLASS_$_SASRequestTransactionController
+ _SCDAToSISchemaUUID
+ __DATA_SASRequestTransactionController
+ __INSTANCE_METHODS_SASRequestTransactionController
+ __IVARS_SASRequestTransactionController
+ __METACLASS_DATA_SASRequestTransactionController
+ __OBJC_$_CLASS_METHODS_SASDeviceSelectionShadowController
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_OPT_SASMyriadControlling
+ __OBJC_$_PROTOCOL_REFS_OS_os_transaction
+ __OBJC_LABEL_PROTOCOL_$_OS_os_transaction
+ __OBJC_PROTOCOL_$_OS_os_transaction
+ ___103-[SASDeviceSelectionController activateForRequest:withTimeout:visible:idleAndQuiet:electionGeneration:]_block_invoke
+ ___103-[SASDeviceSelectionController activateForRequest:withTimeout:visible:idleAndQuiet:electionGeneration:]_block_invoke_2
+ ___37-[SASMyriadController alarmsRemoved:]_block_invoke
+ ___37-[SASMyriadController timersRemoved:]_block_invoke
+ ___43-[SASMyriadController _refetchFiringAlarms]_block_invoke
+ ___43-[SASMyriadController _refetchFiringAlarms]_block_invoke_2
+ ___43-[SASMyriadController _refetchFiringTimers]_block_invoke
+ ___43-[SASMyriadController _refetchFiringTimers]_block_invoke_2
+ ___48-[SASMyriadController scdaWillStartWithSession:]_block_invoke
+ ___block_descriptor_32_e29_v16?0"SASMyriadController"8l
+ ___block_descriptor_48_e8_32w_e29_v24?0"NSArray"8"NSError"16lw32l8
+ ___block_descriptor_48_e8_32w_e73_v32?0"DeviceSelectionDevice"8"DeviceSelectionLocalScore"16"NSError"24lw32l8
+ ___block_descriptor_56_e8_32s40s_e29_v16?0"SASMyriadController"8ls32l8s40l8
+ ___block_descriptor_72_e8_32s40s48s56w_e5_v8?0lw56l8s32l8s40l8s48l8
+ ___destructor_8_s0_s8_s16_s24_s32_s40_s48_s56
+ ___getMTAlarmManagerAlarmsRemovedSymbolLoc_block_invoke
+ ___getMTTimerManagerTimersRemovedSymbolLoc_block_invoke
+ ___swift_memcpy24_8
+ ___swift_memcpy4_4
+ ___swift_noop_void_return
+ _flat unique So17OS_os_transaction_p
+ _getMTAlarmManagerAlarmsKey
+ _getMTAlarmManagerAlarmsRemoved
+ _getMTAlarmManagerAlarmsRemovedSymbolLoc.ptr
+ _getMTTimerManagerTimersKey
+ _getMTTimerManagerTimersRemoved
+ _getMTTimerManagerTimersRemovedSymbolLoc.ptr
+ _os_transaction_create
+ _swift_getObjCClassFromMetadata
+ _symbolic SDySSSuG
+ _symbolic Su
+ _symbolic _____ 14SiriActivation28RequestTransactionControllerC
+ _symbolic _____ 14SiriActivation28RequestTransactionControllerC5State33_D28766290E5C2D6875A33E455727B990LLV
+ _symbolic _____ So16os_unfair_lock_sV
+ _symbolic _____ s6UInt32V
+ _symbolic _____SgXw 14SiriActivation28RequestTransactionControllerC
+ _symbolic _____SgXwz_Xx 14SiriActivation28RequestTransactionControllerC
+ _symbolic _____XDXMT 14SiriActivation28RequestTransactionControllerC
+ _symbolic ______pSg So17OS_os_transactionP
+ _symbolic _____ySSSuG s18_DictionaryStorageC
+ _symbolic _____y_____G 2os21OSAllocatedUnfairLockV 14SiriActivation28RequestTransactionControllerC5State33_D28766290E5C2D6875A33E455727B990LLV
+ _symbolic _____y__________G s13ManagedBufferCsRi__rlE 14SiriActivation28RequestTransactionControllerC5State33_D28766290E5C2D6875A33E455727B990LLV So16os_unfair_lock_sV
+ _symbolic _____y______pG s23_ContiguousArrayStorageC s7CVarArgP
+ _type_layout_string 14SiriActivation28RequestTransactionControllerC5State33_D28766290E5C2D6875A33E455727B990LLV
+ _type_layout_string So16os_unfair_lock_sV
- -[SASSystemState isV68]
- GCC_except_table24
- GCC_except_table27
- GCC_except_table33
- GCC_except_table35
- GCC_except_table44
- _MGGetProductType
- _OBJC_IVAR_$_SASDeviceSelectionShadowController._lastDeviceSelectionOutcome
- ___48-[SASMyriadController _primeMTAlarmManagerState]_block_invoke_2
- ___48-[SASMyriadController _primeMTTimerManagerState]_block_invoke_2
- ___84-[SASDeviceSelectionController activateForRequest:withTimeout:visible:idleAndQuiet:]_block_invoke
- ___84-[SASDeviceSelectionController activateForRequest:withTimeout:visible:idleAndQuiet:]_block_invoke_2
- ___block_descriptor_40_e8_32s_e29_v16?0"SASMyriadController"8ls32l8
- ___block_descriptor_40_e8_32w_e17_v16?0"NSArray"8lw32l8
- ___block_descriptor_40_e8_32w_e43_v24?0"DeviceSelectionDevice"8"NSError"16lw32l8
- ___destructor_8_s0_s8_s16_s24_s32_s40
CStrings:
+ "#activation holding request transaction (%{public}@)"
+ "#activation released request transaction (%{public}@)"
+ "%s #deviceSelection #shadow Logged %{public}@ under cdaId %@."
+ "%s #deviceSelection #shadow Myriad %{public}@."
+ "%s #deviceSelection #shadow No cdaId for this election; not logging the comparison."
+ "%s #deviceSelection #shadow No column for boost %{public}@; omitted."
+ "%s #myriad alarms fetch failed, keeping firing state: %@"
+ "%s #myriad ignoring alarm notifications %@, %@, %@"
+ "%s #myriad ignoring stale alarms fetch"
+ "%s #myriad ignoring stale timers fetch"
+ "%s #myriad ignoring timer notifications %@, %@, %@"
+ "%s #myriad observing alarm notifications: %@, %@, %@"
+ "%s #myriad observing timer notifications: %@, %@, %@"
+ "%s #myriad priming MTAlarmManager"
+ "%s #myriad priming MTTimerManager"
+ "%s #myriad timers fetch failed, keeping firing state: %@"
+ "-[SASDeviceSelectionController activateForRequest:withTimeout:visible:idleAndQuiet:electionGeneration:]"
+ "-[SASDeviceSelectionController activateForRequest:withTimeout:visible:idleAndQuiet:electionGeneration:]_block_invoke"
+ "-[SASDeviceSelectionController activateForRequest:withTimeout:visible:idleAndQuiet:electionGeneration:]_block_invoke_2"
+ "-[SASDeviceSelectionShadowController _logShadowComparison]"
+ "-[SASDeviceSelectionShadowController _shadowScoreBoostsFrom:]"
+ "-[SASMyriadController _primeMTAlarmManagerState]_block_invoke"
+ "-[SASMyriadController _primeMTTimerManagerState]_block_invoke"
+ "-[SASMyriadController _refetchFiringAlarms]_block_invoke"
+ "-[SASMyriadController _refetchFiringAlarms]_block_invoke_2"
+ "-[SASMyriadController _refetchFiringTimers]_block_invoke"
+ "-[SASMyriadController _refetchFiringTimers]_block_invoke_2"
+ "-[SASMyriadController alarmsRemoved:]"
+ "-[SASMyriadController timersRemoved:]"
+ "CDADEVICESELECTIONOUTCOME_CANCELED"
+ "CDADEVICESELECTIONOUTCOME_DECIDED"
+ "CDADEVICESELECTIONOUTCOME_ERRORED"
+ "CDADEVICESELECTIONOUTCOME_NOT_RUN"
+ "CDADEVICESELECTIONOUTCOME_TIMED_OUT"
+ "CDADEVICESELECTIONOUTCOME_UNKNOWN"
+ "Created Intercom Read PrescribedAction with tool ID: "
+ "Intercom.ReadAnnouncement"
+ "IntercomPlannerTools"
+ "MTAlarmManagerAlarmsRemoved"
+ "MTTimerManagerTimersRemoved"
+ "SiriPresentationActivationCancelReasonSiriNotReady"
+ "alarmOrTimerFiring"
+ "attention"
+ "com.apple.announced"
+ "com.apple.siri.activation.request"
+ "deviceAdjustment"
+ "inEar"
+ "intercomReadAction()"
+ "liftTimeBoost"
+ "mediaPlaybackActive"
+ "mediaPlaybackRecentPlayback"
+ "perception"
+ "platformBoost"
+ "raiseToWake"
+ "recencyBoost"
+ "unlockTimeBoost"
+ "v24@?0@\"NSArray\"8@\"NSError\"16"
+ "v32@?0@\"DeviceSelectionDevice\"8@\"DeviceSelectionLocalScore\"16@\"NSError\"24"
+ "watchGesture"
+ "watchLoudnessThreshold"
- "%s #deviceSelection #shadow Myriad %{public}@, Device Selection %{public}@."
- "%s #myriad ignoring alarm notifications %@, %@"
- "%s #myriad ignoring timer notifications %@, %@"
- "%s #myriad observing alarm notifications: %@, %@"
- "%s #myriad observing timer notifications: %@, %@"
- "%s #myriad priming MTAlarmManager: %lu alarm(s)"
- "%s #myriad priming MTTimerManager: %lu timer(s)"
- "-[SASDeviceSelectionController activateForRequest:withTimeout:visible:idleAndQuiet:]"
- "-[SASDeviceSelectionController activateForRequest:withTimeout:visible:idleAndQuiet:]_block_invoke"
- "-[SASDeviceSelectionController activateForRequest:withTimeout:visible:idleAndQuiet:]_block_invoke_2"
- "-[SASMyriadController _primeMTAlarmManagerState]_block_invoke_2"
- "-[SASMyriadController _primeMTTimerManagerState]_block_invoke_2"
- "v16@?0@\"NSArray\"8"
- "v24@?0@\"DeviceSelectionDevice\"8@\"NSError\"16"
```
