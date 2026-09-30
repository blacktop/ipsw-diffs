## powerexperienced

> `/usr/libexec/powerexperienced`

```diff

-44.60.10.0.0
-  __TEXT.__text: 0xc508
-  __TEXT.__auth_stubs: 0x3c0
-  __TEXT.__objc_stubs: 0x1900
-  __TEXT.__objc_methlist: 0xcf4
-  __TEXT.__const: 0xc8
-  __TEXT.__cstring: 0x64b
-  __TEXT.__objc_methname: 0x1bfb
-  __TEXT.__oslogstring: 0xef3
-  __TEXT.__objc_classname: 0x1e9
-  __TEXT.__objc_methtype: 0x4f2
-  __TEXT.__unwind_info: 0x2e0
-  __DATA_CONST.__auth_got: 0x1e8
-  __DATA_CONST.__got: 0xa0
-  __DATA_CONST.__const: 0x568
-  __DATA_CONST.__cfstring: 0x700
-  __DATA_CONST.__objc_classlist: 0x80
-  __DATA_CONST.__objc_protolist: 0x38
+57.100.8.0.0
+  __TEXT.__text: 0xd7e0
+  __TEXT.__auth_stubs: 0x500
+  __TEXT.__objc_stubs: 0x1c40
+  __TEXT.__objc_methlist: 0x11a4
+  __TEXT.__const: 0xd8
+  __TEXT.__cstring: 0x89a
+  __TEXT.__objc_methname: 0x203c
+  __TEXT.__oslogstring: 0x10c1
+  __TEXT.__objc_classname: 0x214
+  __TEXT.__objc_methtype: 0x54a
+  __TEXT.__gcc_except_tab: 0x48
+  __TEXT.__dlopen_cstrs: 0x8d
+  __TEXT.__unwind_info: 0x398
+  __DATA_CONST.__auth_got: 0x290
+  __DATA_CONST.__got: 0xa8
+  __DATA_CONST.__const: 0x648
+  __DATA_CONST.__cfstring: 0x7a0
+  __DATA_CONST.__objc_classlist: 0x88
+  __DATA_CONST.__objc_protolist: 0x40
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_protorefs: 0x20
-  __DATA_CONST.__objc_superrefs: 0x70
+  __DATA_CONST.__objc_superrefs: 0x78
   __DATA_CONST.__objc_intobj: 0x48
-  __DATA.__objc_const: 0x2698
-  __DATA.__objc_selrefs: 0x768
-  __DATA.__objc_ivar: 0xe4
-  __DATA.__objc_data: 0x500
-  __DATA.__data: 0x2a0
-  __DATA.__bss: 0x130
+  __DATA.__objc_const: 0x26f0
+  __DATA.__objc_selrefs: 0x928
+  __DATA.__objc_ivar: 0x10c
+  __DATA.__objc_data: 0x550
+  __DATA.__data: 0x300
+  __DATA.__bss: 0x160
   __DATA.__common: 0x80
   - /System/Library/Frameworks/CoreFoundation.framework/Versions/A/CoreFoundation
   - /System/Library/Frameworks/Foundation.framework/Versions/C/Foundation

   - /System/Library/PrivateFrameworks/PerformanceControlKit.framework/Versions/A/PerformanceControlKit
   - /System/Library/PrivateFrameworks/PowerExperience.framework/Versions/A/PowerExperience
   - /System/Library/PrivateFrameworks/PowerLog.framework/Versions/A/PowerLog
+  - /System/Library/PrivateFrameworks/SoftLinking.framework/Versions/A/SoftLinking
+  - /System/Library/PrivateFrameworks/Trial.framework/Versions/A/Trial
   - /usr/lib/libMobileGestalt.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 7761B0BB-0B88-313C-9D0D-270932E00FA1
-  Functions: 335
-  Symbols:   92
-  CStrings:  685
+  UUID: 455DA173-A6C4-3A90-84B8-9375B5DFA2E4
+  Functions: 403
+  Symbols:   114
+  CStrings:  778
 
Symbols:
+ _IOPMConnectionAcknowledgeEvent
+ _IOPMConnectionCreate
+ _IOPMConnectionGetSystemCapabilities
+ _IOPMConnectionSetDispatchQueue
+ _IOPMConnectionSetNotification
+ _IOPMIsADarkWake
+ _OBJC_CLASS_$_TRIClient
+ __Block_object_dispose
+ __Unwind_Resume
+ ___objc_personality_v0
+ __sl_dlopen
+ _abort_report_np
+ _dlopen_preflight
+ _free
+ _objc_copyWeak
+ _objc_destroyWeak
+ _objc_getClass
+ _objc_initWeak
+ _objc_loadWeakRetained
+ _objc_sync_enter
+ _objc_sync_exit
+ _objc_unsafeClaimAutoreleasedReturnValue
CStrings:
+ "%s"
+ "/AppleInternal/Library/Frameworks/PerformanceControlKitInternal.framework/PerformanceControlKitInternal"
+ "/System/Library/../../AppleInternal/Library/Frameworks/PerformanceControlKitInternal.framework/Contents/MacOS/PerformanceControlKitInternal"
+ "@\"<CLPCInternalAccess>\""
+ "@\"TRIClient\""
+ "AppleCLPC"
+ "AppleCLPC kext not present"
+ "CLPCInternalInterface"
+ "CLPC_TuningOption"
+ "COREOS_POWER_EXPERIENCE_POWER_TUNING"
+ "CPMTrialManager"
+ "CPMTrialManagerDelegate"
+ "Calling trial delegates"
+ "EarlyWakeInProgress"
+ "Error 0x%08x from IOPMConnectionCreate.\n"
+ "Error 0x%08x from IOPMConnectionSetNotification.\n"
+ "Error creating CLPC Internal User Client %@"
+ "Error setting clpc trial value %@"
+ "Failed to register for clamshell state update"
+ "HotInBackpackMode"
+ "Initialized internal CLPC Policy Interface"
+ "InternalBuild"
+ "Mac"
+ "PerformanceControlKitInternal not available"
+ "PowerExperience"
+ "SleepFromDarkWakeInProgress"
+ "T@\"<CLPCInternalAccess>\",&,V_clpcInternalAccessClient"
+ "T@\"NSMutableArray\",&,V_delegates"
+ "T@\"NSString\",&,V_experimentID"
+ "T@\"NSString\",&,V_namespace"
+ "T@\"NSString\",&,V_treatmentID"
+ "T@\"TRIClient\",&,V_trialClient"
+ "TB,V_isInternal"
+ "Ti,V_deploymentID"
+ "Trial experiment status. treatmentID %@, rolloutID %@, experimentID %@"
+ "Trial:CLPC tuning factor %lld"
+ "Trial:No trial value for CLPC tuning option"
+ "Unable to find class %s"
+ "Updating CLPCInternal client RPC buffer size tp 16k"
+ "_clpcInternalAccessClient"
+ "_delegates"
+ "_deploymentID"
+ "_experimentID"
+ "_isInternal"
+ "_namespace"
+ "_treatmentID"
+ "_trialClient"
+ "addDelegate:"
+ "addUpdateHandlerForNamespaceName:usingBlock:"
+ "clientWithIdentifier:"
+ "clpcInternalAccessClient"
+ "com.apple.powerexperienced.trialmanager"
+ "com.apple.system.powermanagement.clamshellstate"
+ "cpmTrialManager:hasUpdatedParametersForNamespace:"
+ "delegates"
+ "deploymentID"
+ "evaluatePowerMode: %@: %d isPluggedIn %d, isClamshelled %d, isDarkWake %d, sleepS0InProgress %d, earlyWakeInProgress %d, (allowOnCharger: %d)"
+ "experimentID"
+ "experimentIdentifiersWithNamespaceName:"
+ "factorWithName:"
+ "handleClamshellStateChange"
+ "i"
+ "i16@0:8"
+ "initClamshellStateChange"
+ "initPowerStateChange"
+ "isInternal"
+ "kClamshellStateContext"
+ "kDarkWakeStateContext"
+ "levelForFactor:withNamespaceName:"
+ "longValue"
+ "namespace"
+ "numberWithUnsignedInt:"
+ "refresh"
+ "registerForTrial"
+ "rolloutIdentifiersWithNamespaceName:"
+ "setCLPCTrialID:error:"
+ "setClpcInternalAccessClient:"
+ "setDelegates:"
+ "setDeploymentID:"
+ "setExperimentID:"
+ "setIsInternal:"
+ "setNamespace:"
+ "setRPCBufferSize:"
+ "setTreatmentID:"
+ "setTrialClient:"
+ "softlink:o:path:/System/Library/../../AppleInternal/Library/Frameworks/PerformanceControlKitInternal.framework/PerformanceControlKitInternal"
+ "treatmentID"
+ "treatmentIdWithNamespaceName:"
+ "trialClient"
+ "trialmanager"
+ "updateFactors"
+ "updateTrialParameters"
+ "v16@?0@\"<TRINamespaceUpdateProtocol>\"8"
+ "v32@0:8@\"CPMTrialManager\"16@\"NSString\"24"
- "NFCSession"
- "SiriAudio"
- "SleepInProgress"
- "Updating SMC with debug mode %@:%d"
- "WakeInProgress"
- "evaluatePowerMode: %@: %d display %d, carPlaySession %d, nFCSession %d, audioSession %d, sleepInProgress %d, wakeInProgress %d, onenessSession %d, siriAudio %d, pluggedIn %d (allowOnCharger: %d)"

```
