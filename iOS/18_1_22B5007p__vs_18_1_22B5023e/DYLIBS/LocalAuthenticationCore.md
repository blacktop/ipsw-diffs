## LocalAuthenticationCore

> `/System/Library/PrivateFrameworks/LocalAuthenticationCore.framework/LocalAuthenticationCore`

```diff

-1656.0.83.0.0
-  __TEXT.__text: 0xa753c
-  __TEXT.__auth_stubs: 0x1e30
-  __TEXT.__objc_methlist: 0x4f70
-  __TEXT.__const: 0x30f4
-  __TEXT.__cstring: 0xa94a
-  __TEXT.__oslogstring: 0x2cb5
-  __TEXT.__gcc_except_tab: 0x1208
-  __TEXT.__dlopen_cstrs: 0x2f8
-  __TEXT.__swift5_typeref: 0xfc8
+1656.40.15.0.0
+  __TEXT.__text: 0xa8bf8
+  __TEXT.__auth_stubs: 0x1e70
+  __TEXT.__objc_methlist: 0x50a0
+  __TEXT.__const: 0x3124
+  __TEXT.__cstring: 0xa98a
+  __TEXT.__oslogstring: 0x2d6b
+  __TEXT.__gcc_except_tab: 0x122c
+  __TEXT.__dlopen_cstrs: 0x352
+  __TEXT.__swift5_typeref: 0xfc6
   __TEXT.__constg_swiftt: 0xa84
   __TEXT.__swift5_reflstr: 0x617
   __TEXT.__swift5_fieldmd: 0x740
   __TEXT.__swift5_builtin: 0xa0
   __TEXT.__swift5_assocty: 0x108
-  __TEXT.__swift5_capture: 0x778
+  __TEXT.__swift5_capture: 0x868
   __TEXT.__swift5_proto: 0xd0
   __TEXT.__swift5_types: 0x90
   __TEXT.__swift5_protos: 0x18
   __TEXT.__swift5_mpenum: 0x8
-  __TEXT.__unwind_info: 0x2fb0
-  __TEXT.__eh_frame: 0x17a8
-  __TEXT.__objc_classname: 0x17e7
-  __TEXT.__objc_methname: 0xa063
-  __TEXT.__objc_methtype: 0x2d2e
-  __TEXT.__objc_stubs: 0x7540
-  __DATA_CONST.__got: 0x818
-  __DATA_CONST.__const: 0x3740
-  __DATA_CONST.__objc_classlist: 0x5a8
-  __DATA_CONST.__objc_protolist: 0x408
+  __TEXT.__unwind_info: 0x3018
+  __TEXT.__eh_frame: 0x17d0
+  __TEXT.__objc_classname: 0x185b
+  __TEXT.__objc_methname: 0xa1c7
+  __TEXT.__objc_methtype: 0x2d6c
+  __TEXT.__objc_stubs: 0x75e0
+  __DATA_CONST.__got: 0x830
+  __DATA_CONST.__const: 0x37f8
+  __DATA_CONST.__objc_classlist: 0x5c8
+  __DATA_CONST.__objc_protolist: 0x410
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x25d0
+  __DATA_CONST.__objc_selrefs: 0x2618
   __DATA_CONST.__objc_protorefs: 0x168
-  __DATA_CONST.__objc_superrefs: 0x390
-  __DATA_CONST.__objc_arraydata: 0x48
-  __AUTH_CONST.__auth_got: 0xf28
-  __AUTH_CONST.__auth_ptr: 0x380
-  __AUTH_CONST.__const: 0x2110
-  __AUTH_CONST.__cfstring: 0x3980
-  __AUTH_CONST.__objc_const: 0x294e8
+  __DATA_CONST.__objc_superrefs: 0x3a0
+  __DATA_CONST.__objc_arraydata: 0x40
+  __AUTH_CONST.__auth_got: 0xf48
+  __AUTH_CONST.__auth_ptr: 0x388
+  __AUTH_CONST.__const: 0x2310
+  __AUTH_CONST.__cfstring: 0x39a0
+  __AUTH_CONST.__objc_const: 0x2a690
   __AUTH_CONST.__objc_intobj: 0x1c8
   __AUTH_CONST.__objc_arrayobj: 0x78
-  __AUTH.__objc_data: 0xae8
-  __AUTH.__data: 0x138
-  __DATA.__objc_ivar: 0x5f8
-  __DATA.__data: 0x3430
-  __DATA.__bss: 0x15d9
-  __DATA.__common: 0x48
-  __DATA_DIRTY.__objc_data: 0x3308
-  __DATA_DIRTY.__data: 0xde0
-  __DATA_DIRTY.__bss: 0x4d8
-  __DATA_DIRTY.__common: 0x68
+  __AUTH.__objc_data: 0x228
+  __DATA.__objc_ivar: 0x614
+  __DATA.__data: 0x3740
+  __DATA.__bss: 0x1a11
+  __DATA.__common: 0x40
+  __DATA_DIRTY.__objc_data: 0x3d08
+  __DATA_DIRTY.__data: 0xc98
+  __DATA_DIRTY.__bss: 0xc0
+  __DATA_DIRTY.__common: 0x70
   - /System/Library/Frameworks/Combine.framework/Combine
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/CoreServices.framework/CoreServices

   - /usr/lib/swift/libswiftOSLog.dylib
   - /usr/lib/swift/libswiftObjectiveC.dylib
   - /usr/lib/swift/libswiftXPC.dylib
+  - /usr/lib/swift/libswift_Builtin_float.dylib
   - /usr/lib/swift/libswift_Concurrency.dylib
+  - /usr/lib/swift/libswift_errno.dylib
+  - /usr/lib/swift/libswift_math.dylib
+  - /usr/lib/swift/libswift_signal.dylib
+  - /usr/lib/swift/libswift_stdio.dylib
+  - /usr/lib/swift/libswift_time.dylib
   - /usr/lib/swift/libswiftos.dylib
-  Functions: 4044
-  Symbols:   5714
-  CStrings:  4028
+  - /usr/lib/swift/libswiftsys_time.dylib
+  - /usr/lib/swift/libswiftunistd.dylib
+  Functions: 4086
+  Symbols:   5797
+  CStrings:  4060
 
Symbols:
+ _LACErrorCodeTimeout
+ _LACErrorSubcodeBiometryFailedToStart
+ _LACErrorSubcodeCompanionSessionActive
+ _LACErrorSubcodeFaceIDLowPower
+ _LACErrorSubcodeUnknown
+ _OBJC_CLASS_$_LACDTOFailureProcessor
+ _OBJC_CLASS_$_LACDTOSensorRepairStateProviderFactory
+ _OBJC_CLASS_$_LACSetUpStateProvider
+ _OBJC_CLASS_$_LACUNManagerProvider
+ _OBJC_CLASS_$_LACUNManagerSetUpDecorator
+ _OBJC_METACLASS_$_LACDTOFailureProcessor
+ _OBJC_METACLASS_$_LACDTOSensorRepairStateProviderFactory
+ _OBJC_METACLASS_$_LACSetUpStateProvider
+ _OBJC_METACLASS_$_LACUNManagerProvider
+ _OBJC_METACLASS_$_LACUNManagerSetUpDecorator
+ __swift_FORCE_LOAD_$_swift_Builtin_float
+ __swift_FORCE_LOAD_$_swift_errno
+ __swift_FORCE_LOAD_$_swift_math
+ __swift_FORCE_LOAD_$_swift_signal
+ __swift_FORCE_LOAD_$_swift_stdio
+ __swift_FORCE_LOAD_$_swift_time
+ __swift_FORCE_LOAD_$_swiftsys_time
+ __swift_FORCE_LOAD_$_swiftunistd
+ _abort_report_np
+ _dispatch_get_global_queue
+ _dlerror
+ _dlsym
- _OBJC_CLASS_$_LACUNManagerPool
- _OBJC_METACLASS_$_LACUNManagerPool
CStrings:
+ "\"\x14!"
+ "@\"<LACSetUpStateProvider>\""
+ "@\"LACUNManager\"8@?0"
+ "@\"LACUNManagerSetUpDecorator\"8@?0"
+ "@32@0:8@?16@24"
+ "BYSetupAssistantNeedsToRun"
+ "BiometryRequired"
+ "Cannot interact with UserNotifications at the moment."
+ "Failure alert did disappear (err: %!@(MISSING))"
+ "Failure alert will appear."
+ "LACDTOFailureProcessor"
+ "LACDTOSensorRepairStateProviderFactory"
+ "LACSetUpStateProvider"
+ "LACUNManagerProvider"
+ "LACUNManagerSetUpDecorator"
+ "Sensor trust alert with id: %!@(MISSING) will appear."
+ "SensorNotTrustedStrictMode"
+ "Service not available in Setup"
+ "Setup checks are not available due to missing dependencies"
+ "T@\"NSError\",&,N"
+ "T@\"NSError\",&,N,VretryingForError"
+ "TB,R,N,VisRecoveringFromBiolockout"
+ "_checkErrorRequiresUI:"
+ "_responder"
+ "_responderBuilder"
+ "_setupStateProvider"
+ "globalUserInitiatedConcurrentQueue"
+ "hasCompletedSetup: %!@(MISSING)"
+ "initWithManagerBuilder:"
+ "initWithManagerBuilder:setupStateProvider:"
+ "initWithReplyQueue:ui:"
+ "isFeatureAvailable = isFeatureEnabled = YES"
+ "isRecoveringFromBiolockout"
+ "repairStateProviderWithReplyQueue:flags:"
+ "responder"
+ "retryingForError"
+ "setRetryingForError:"
+ "softlink:o:path:/System/Library/PrivateFrameworks/SetupAssistant.framework/SetupAssistant"
+ "v24@0:8@\"NSError\"16"
- "\"\x14"
- "@\"LACUNManagerQueueDecorator\"8@?0"
- "LACUNManagerPool"
- "Mapping unapproved sensor error %!{(MISSING)public}@ to success for excepted client"
- "Sensor trust alert will appear."
- "_shouldAllowUnapprovedSensorForOperation:"
- "com.apple.Preferences:FaceID"
- "com.apple.Preferences:TouchID"

```
