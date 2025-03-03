## powerexperienced

> `/usr/libexec/powerexperienced`

```diff

-44.60.10.0.0
-  __TEXT.__text: 0xb794
-  __TEXT.__auth_stubs: 0x580
-  __TEXT.__objc_stubs: 0x19e0
-  __TEXT.__objc_methlist: 0xda4
-  __TEXT.__const: 0xc8
-  __TEXT.__cstring: 0x659
-  __TEXT.__objc_methname: 0x1e98
-  __TEXT.__oslogstring: 0xf3a
-  __TEXT.__objc_classname: 0x238
-  __TEXT.__objc_methtype: 0x601
-  __TEXT.__unwind_info: 0x2e0
-  __DATA_CONST.__auth_got: 0x2c8
-  __DATA_CONST.__got: 0xa8
-  __DATA_CONST.__const: 0x4e8
-  __DATA_CONST.__cfstring: 0x700
-  __DATA_CONST.__objc_classlist: 0x88
-  __DATA_CONST.__objc_protolist: 0x48
+57.100.8.0.0
+  __TEXT.__text: 0xcbc0
+  __TEXT.__auth_stubs: 0x690
+  __TEXT.__objc_stubs: 0x1d20
+  __TEXT.__objc_methlist: 0x12d4
+  __TEXT.__const: 0xd8
+  __TEXT.__cstring: 0x831
+  __TEXT.__objc_methname: 0x22d9
+  __TEXT.__oslogstring: 0x1155
+  __TEXT.__objc_classname: 0x263
+  __TEXT.__objc_methtype: 0x659
+  __TEXT.__gcc_except_tab: 0x48
+  __TEXT.__dlopen_cstrs: 0x8d
+  __TEXT.__unwind_info: 0x3a8
+  __DATA_CONST.__auth_got: 0x358
+  __DATA_CONST.__got: 0xb0
+  __DATA_CONST.__const: 0x5d0
+  __DATA_CONST.__cfstring: 0x7a0
+  __DATA_CONST.__objc_classlist: 0x90
+  __DATA_CONST.__objc_protolist: 0x50
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_protorefs: 0x20
-  __DATA_CONST.__objc_superrefs: 0x78
+  __DATA_CONST.__objc_superrefs: 0x80
   __DATA_CONST.__objc_intobj: 0x48
-  __DATA.__objc_const: 0x2c78
-  __DATA.__objc_selrefs: 0x7c0
-  __DATA.__objc_ivar: 0xf4
-  __DATA.__objc_data: 0x550
-  __DATA.__data: 0x360
-  __DATA.__bss: 0x140
+  __DATA.__objc_const: 0x2bf8
+  __DATA.__objc_selrefs: 0x9b0
+  __DATA.__objc_ivar: 0x11c
+  __DATA.__objc_data: 0x5a0
+  __DATA.__data: 0x3c0
+  __DATA.__bss: 0x170
   __DATA.__common: 0x80
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/Foundation.framework/Foundation

   - /System/Library/PrivateFrameworks/PerformanceControlKit.framework/PerformanceControlKit
   - /System/Library/PrivateFrameworks/PowerExperience.framework/PowerExperience
   - /System/Library/PrivateFrameworks/PowerLog.framework/PowerLog
+  - /System/Library/PrivateFrameworks/SoftLinking.framework/SoftLinking
+  - /System/Library/PrivateFrameworks/Trial.framework/Trial
   - /usr/lib/libMobileGestalt.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 337
-  Symbols:   121
-  CStrings:  674
+  Functions: 402
+  Symbols:   140
+  CStrings:  765
 
Symbols:
+ _OBJC_CLASS_$_TRIClient
+ __Block_object_dispose
+ __Unwind_Resume
+ ___error
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
+ _objc_retain_x9
+ _objc_sync_enter
+ _objc_sync_exit
+ _posix_spawn
+ _strerror
CStrings:
+ "\x17"
+ "%s"
+ "/AppleInternal/Library/Frameworks/PerformanceControlKitInternal.framework/PerformanceControlKitInternal"
+ "/usr/local/bin/clpcctrl"
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
+ "Error creating CLPC Internal User Client %@"
+ "Error setting clpc trial value %@"
+ "Error setting lower HiP target %s"
+ "Failed to register for clamshell state update"
+ "Initialized internal CLPC Policy Interface"
+ "InternalBuild"
+ "Mac"
+ "PerformanceControlKitInternal not available"
+ "ReducedHiPTarget"
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
+ "Updating CLPC with power target 400mW for HiP"
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
+ "levelForFactor:withNamespaceName:"
+ "longValue"
+ "namespace"
+ "numberWithUnsignedInt:"
+ "pkg-hip-static-power-target=0.4"
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

```
