## ManagedSettingsUI

> `/System/Library/Frameworks/ManagedSettingsUI.framework/ManagedSettingsUI`

```diff

-214.0.0.0.0
-  __TEXT.__text: 0x5510
+215.0.0.0.0
+  __TEXT.__text: 0x5544
   __TEXT.__auth_stubs: 0x6f0
   __TEXT.__objc_methlist: 0xac
   __TEXT.__const: 0x24e

   __TEXT.__unwind_info: 0x158
   __TEXT.__objc_methname: 0x369
   __DATA_CONST.__got: 0x98
-  __DATA_CONST.__const: 0x88
+  __DATA_CONST.__const: 0xc8
   __DATA_CONST.__objc_classlist: 0x10
   __DATA_CONST.__objc_protolist: 0x10
   __DATA_CONST.__objc_imageinfo: 0x8

   - /usr/lib/swift/libswiftQuartzCore.dylib
   - /usr/lib/swift/libswiftUniformTypeIdentifiers.dylib
   - /usr/lib/swift/libswiftXPC.dylib
+  - /usr/lib/swift/libswift_Builtin_float.dylib
+  - /usr/lib/swift/libswift_errno.dylib
+  - /usr/lib/swift/libswift_math.dylib
+  - /usr/lib/swift/libswift_signal.dylib
+  - /usr/lib/swift/libswift_stdio.dylib
+  - /usr/lib/swift/libswift_time.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
+  - /usr/lib/swift/libswiftsys_time.dylib
+  - /usr/lib/swift/libswiftunistd.dylib
   Functions: 129
-  Symbols:   118
-  CStrings:  0
+  Symbols:   126
+  CStrings:  62
 
Symbols:
+ __swift_FORCE_LOAD_$_swift_Builtin_float
+ __swift_FORCE_LOAD_$_swift_errno
+ __swift_FORCE_LOAD_$_swift_math
+ __swift_FORCE_LOAD_$_swift_signal
+ __swift_FORCE_LOAD_$_swift_stdio
+ __swift_FORCE_LOAD_$_swift_time
+ __swift_FORCE_LOAD_$_swiftsys_time
+ __swift_FORCE_LOAD_$_swiftunistd
CStrings:
+ "ServiceMsgEEE"
+ "TraceMessageEvent"
+ "_OBJC_CLASS_$_OSLogEventLiveSource"
+ "_OBJC_CLASS_$_OSLogEventLiveStore"
+ "_OBJC_CLASS_$_OSLogEventLiveStream"
+ "_OBJC_CLASS_$_OSLogEventSource"
+ "_OBJC_CLASS_$_OSLogEventStreamPosition"
+ "_OBJC_CLASS_$_OSLogPreferencesManager"
+ "_OBJC_CLASS_$_OSLogPreferencesSubsystem"
+ "_OBJC_CLASS_$_OSLogTermDumper"
+ "_OBJC_METACLASS_$_OSActivityTransitionEvent"
+ "_OBJC_METACLASS_$_OSActivityUserActionEvent"
+ "_OBJC_METACLASS_$_OSLogDeserializedEventStream"
+ "_OBJC_METACLASS_$_OSLogEventLiveSource"
+ "_OBJC_METACLASS_$_OSLogEventLiveStore"
+ "_OBJC_METACLASS_$_OSLogEventLiveStream"
+ "_OBJC_METACLASS_$_OSLogEventSerializer"
+ "_OBJC_METACLASS_$_OSLogPersistence"
+ "_OBJC_METACLASS_$_OSLogPreferencesCategory"
+ "_OBJC_METACLASS_$_OSLogPreferencesManager"
+ "_OBJC_METACLASS_$_OSLogPreferencesProcess"
+ "_OBJC_METACLASS_$_OSLogPreferencesSubsystem"
+ "_OBJC_METACLASS_$_OSLogTermDumper"
+ "_OBJC_METACLASS_$__OSLogVersioning"
+ "__ZN14_ATCSException19setExceptionHandlerEPFvRS_E"
+ "__ZN19ATCSRouterIPCDriver15resetErrorStateEv"
+ "__ZN19ATCSRouterIPCDriver6createERKNS_10ParametersE"
+ "__ZN19QMIServerConnectionC1Ev"
+ "__ZN3ctu9SingletonI26ATCSExceptionHandlerGlobalS1_NS_23PthreadMutexGuardPolicyIS1_EEE9sInstanceE"
+ "__ZN3ctu9SingletonINS_7GestaltES1_NS_23PthreadMutexGuardPolicyIS1_EEE9sInstanceE"
+ "__ZN3qmi10kClientSimE"
+ "__ZN3qmi11kClientNameE"
+ "__ZN3qmi12ClientRouter5resetEv"
+ "__ZN3qmi12ClientRouter9addClientENS_16SubscriptionTypeENS_6ClientE"
+ "__ZN3qmi12ClientRouterC1EP8os_log_s"
+ "__ZN3qmi14kClientSvcTypeE"
+ "__ZN3qmi17kClientSendWindowE"
+ "__ZN3qmi18QMuxServerAccepter21setValidationStrategyENSt3__18functionIFbPvEEE"
+ "__ZN3qmi18QMuxServerAccepterC1ERK4QMuxRKP16dispatch_queue_sRKNSt3__112basic_stringIcNS8_11char_traitsIcEENS8_9allocatorIcEEEE"
+ "__ZN3qmi21kClientRemoteLogLevelE"
+ "__ZN3qmi8asStringENS_16SubscriptionTypeE"
+ "__ZN4QMux11invokeResetERKNSt3__112basic_stringIcNS0_11char_traitsIcEENS0_9allocatorIcEEEEb"
+ "__ZN4QMux14enterPowerModeEP16dispatch_group_sN3qmi12PowerProfileE"
+ "__ZN4QMux18setDriverAndCookieEP13ATCSIPCDriverPv"
+ "__ZN4QMux23getQMIPowerDownMessagesEv"
+ "__ZN4QMux4stopEv"
+ "__ZN4QMux5startEv"
+ "__ZN4QMux8shutdownEv"
+ "__ZN4QMuxC1EP13ATCSIPCDriverPvRKNSt3__112basic_stringIcNS3_11char_traitsIcEENS3_9allocatorIcEEEENS3_8weak_ptrI16ATCSResetInvokerEEbb"
+ "__ZN4QMuxC1Ev"
+ "__ZN4QMuxD1Ev"
+ "__ZNK13QMIServiceMsg11getNewErrorEv"
+ "__ZNK3qmi12ClientRouter10setHandlerENS_6Client5EventENSt3__18functionIFvNS_16SubscriptionTypeEEEE"
+ "__ZNK3qmi12ClientRouter16setIndShouldWakeEtb"
+ "__ZNK3qmi12ClientRouter3hasENS_16SubscriptionTypeE"
+ "__ZNK3qmi12ClientRouter4stopENS_16SubscriptionTypeE"
+ "__ZNK3qmi12ClientRouter5startENS_16SubscriptionTypeE"
+ "__ZNK4QMux13isPoweredDownEv"
+ "__ZNK4QMux7getNameEv"
+ "__ZNK4QMux9dumpStateEv"
+ "__ZNK4QMux9isRunningEv"
+ "nt10getSvcTypeEv"

```
