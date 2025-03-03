## SafetyKit

> `/System/Library/Frameworks/SafetyKit.framework/SafetyKit`

```diff

-121.0.1.0.0
-  __TEXT.__text: 0xe434
-  __TEXT.__auth_stubs: 0x650
-  __TEXT.__objc_methlist: 0xa28
-  __TEXT.__const: 0x88
-  __TEXT.__cstring: 0x15eb
-  __TEXT.__oslogstring: 0x1969
-  __TEXT.__gcc_except_tab: 0x2ec
-  __TEXT.__unwind_info: 0x440
-  __TEXT.__objc_classname: 0x2c8
-  __TEXT.__objc_methname: 0x295a
-  __TEXT.__objc_methtype: 0xa61
-  __TEXT.__objc_stubs: 0x22c0
-  __DATA_CONST.__got: 0x250
-  __DATA_CONST.__const: 0x5c0
-  __DATA_CONST.__objc_classlist: 0x88
+125.0.13.0.0
+  __TEXT.__text: 0x1073c
+  __TEXT.__auth_stubs: 0x7e0
+  __TEXT.__objc_methlist: 0xe2c
+  __TEXT.__const: 0xe0
+  __TEXT.__cstring: 0x18f6
+  __TEXT.__oslogstring: 0x1ce3
+  __TEXT.__gcc_except_tab: 0x6ec
+  __TEXT.__unwind_info: 0x5b8
+  __TEXT.__objc_classname: 0x2da
+  __TEXT.__objc_methname: 0x2aae
+  __TEXT.__objc_methtype: 0xaee
+  __TEXT.__objc_stubs: 0x2380
+  __DATA_CONST.__got: 0x268
+  __DATA_CONST.__const: 0x6c8
+  __DATA_CONST.__objc_classlist: 0x90
   __DATA_CONST.__objc_catlist: 0x8
   __DATA_CONST.__objc_protolist: 0x80
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x968
+  __DATA_CONST.__objc_selrefs: 0xb20
   __DATA_CONST.__objc_protorefs: 0x10
-  __DATA_CONST.__objc_superrefs: 0x60
-  __AUTH_CONST.__auth_got: 0x338
-  __AUTH_CONST.__const: 0x120
-  __AUTH_CONST.__cfstring: 0x7c0
-  __AUTH_CONST.__objc_const: 0x2b60
+  __DATA_CONST.__objc_superrefs: 0x68
+  __AUTH_CONST.__auth_got: 0x408
+  __AUTH_CONST.__const: 0x1b0
+  __AUTH_CONST.__cfstring: 0x9e0
+  __AUTH_CONST.__objc_const: 0x2680
   __AUTH_CONST.__objc_intobj: 0x18
-  __AUTH.__objc_data: 0x370
-  __DATA.__objc_ivar: 0xbc
-  __DATA.__data: 0x608
+  __AUTH.__objc_data: 0x3c0
+  __DATA.__objc_ivar: 0xc4
+  __DATA.__data: 0x818
   __DATA.__bss: 0x20
   __DATA_DIRTY.__objc_data: 0x1e0
   __DATA_DIRTY.__bss: 0x50

   - /System/Library/Frameworks/UIKit.framework/UIKit
   - /System/Library/Frameworks/UserNotifications.framework/UserNotifications
   - /System/Library/PrivateFrameworks/AppConduit.framework/AppConduit
+  - /System/Library/PrivateFrameworks/LocationSupport.framework/LocationSupport
   - /System/Library/PrivateFrameworks/NanoPreferencesSync.framework/NanoPreferencesSync
   - /System/Library/PrivateFrameworks/NanoRegistry.framework/NanoRegistry
   - /System/Library/PrivateFrameworks/RunningBoardServices.framework/RunningBoardServices

   - /System/Library/PrivateFrameworks/TCC.framework/TCC
   - /System/Library/PrivateFrameworks/TelephonyUtilities.framework/TelephonyUtilities
   - /usr/lib/libSystem.B.dylib
+  - /usr/lib/libc++.1.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 371
-  Symbols:   595
-  CStrings:  853
+  Functions: 415
+  Symbols:   698
+  CStrings:  910
 
Symbols:
+ _CSKappaConnectionBringupFeedbackAssistantMessage
+ _CSKappaConnectionCommandKey
+ _CSKappaConnectionFeedbackAssistantConsentKey
+ _CSKappaConnectionFeedbackAssistantConsentResponse
+ _CSKappaConnectionFeedbackAssistantUUIDKey
+ _CSKappaConnectionReturn
+ _CSKappaConnectionSendCommandName
+ _CSKappaConnectionServiceName
+ _CSKappaConnectionTestMessageName
+ _CSKappaConnectionTestPowerAssertionName
+ _CSKappaConnectionTestSOSName
+ _CSKappaConnectionTestSignalName
+ _CSKappaConnectionTestTTRName
+ _CSKappaConnectionTestTriggerName
+ _CSKappaConnectionValueKey
+ _OBJC_CLASS_$_CSKappaConnection
+ _OBJC_METACLASS_$_CSKappaConnection
+ __ZN18CLConnectionClient11sendMessageENSt3__110shared_ptrI19CLConnectionMessageEEU13block_pointerFvS3_E
+ __ZN18CLConnectionClient11sendMessageENSt3__110shared_ptrI19CLConnectionMessageEEb
+ __ZN18CLConnectionClient22setInterruptionHandlerEU13block_pointerFvvE
+ __ZN18CLConnectionClient24setDefaultMessageHandlerEU13block_pointerFvNSt3__110shared_ptrI19CLConnectionMessageEEE
+ __ZN18CLConnectionClient5startEv
+ __ZN18CLConnectionClientC1ENSt3__112basic_stringIcNS0_11char_traitsIcEENS0_9allocatorIcEEEEPU28objcproto17OS_dispatch_queue8NSObject
+ __ZN19CLConnectionMessageC1ERKNSt3__112basic_stringIcNS0_11char_traitsIcEENS0_9allocatorIcEEEE
+ __ZN19CLConnectionMessageC1ERKNSt3__112basic_stringIcNS0_11char_traitsIcEENS0_9allocatorIcEEEEPU25objcproto14NSSecureCoding11objc_object
+ __ZN19CLConnectionMessageD1Ev
+ __ZNK19CLConnectionMessage13getDictionaryEv
+ __ZNK19CLConnectionMessage22getDictionaryOfClassesEP5NSSet
+ __ZNK19CLConnectionMessage4nameEv
+ __ZNKSt3__119__shared_weak_count13__get_deleterERKSt9type_info
+ __ZNSt11logic_errorC2EPKc
+ __ZNSt12length_errorD1Ev
+ __ZNSt3__119__shared_weak_count14__release_weakEv
+ __ZNSt3__119__shared_weak_countD2Ev
+ __ZTINSt3__119__shared_weak_countE
+ __ZTISt12length_error
+ __ZTVN10__cxxabiv120__si_class_type_infoE
+ __ZTVSt12length_error
+ __ZdlPv
+ __ZdlPvSt19__type_descriptor_t
+ __Znwm
+ __ZnwmSt19__type_descriptor_t
+ ___cxa_allocate_exception
+ ___cxa_free_exception
+ ___cxa_throw
+ ___gxx_personality_v0
+ _memmove
+ _objc_retainAutoreleasedReturnValue
+ _objc_retain_x27
+ _strlen
- _objc_retain_x28
CStrings:
+ "CSConnection"
+ "CSKappaCommandKey"
+ "CSKappaConnection"
+ "CSKappaConnectionBringupFeedbackAssistantMessage"
+ "CSKappaConnectionQueue"
+ "CSKappaFeedbackAssistantConsentKey"
+ "CSKappaFeedbackAssistantUUIDKey"
+ "CSKappaReturnKey"
+ "CSKappaValueKey"
+ "Connection Interrupted"
+ "UTF8String"
+ "^v"
+ "_internalQueue"
+ "basic_string"
+ "bringupFeedbackAssistantWithUUID:"
+ "com.apple.anomalydetectiond"
+ "com.apple.anomalydetectiond.kappa"
+ "com.apple.anomalydetectiond.kappa.command"
+ "com.apple.anomalydetectiond.kappa.feedbackConsentResponse"
+ "com.apple.anomalydetectiond.kappa.message.test"
+ "com.apple.anomalydetectiond.kappa.powerassertion.test"
+ "com.apple.anomalydetectiond.kappa.signal.test"
+ "com.apple.anomalydetectiond.kappa.sos.test"
+ "com.apple.anomalydetectiond.kappa.trigger.test"
+ "com.apple.anomalydetectiond.kappa.ttr.test"
+ "defaultMessageHandler:"
+ "interruptionHandler"
+ "numberWithBool:"
+ "numberWithDouble:"
+ "response is nil"
+ "sendCommand:"
+ "sendCommand:withValue:"
+ "sendFeedbackConsent:andUUID:"
+ "sendTestCachedMessage:"
+ "sendTestMessage:"
+ "sendTestPowerAssertion:"
+ "sendTestSMSignal:"
+ "sendTestSOS"
+ "sendTestTTR"
+ "sendTestTrigger"
+ "setWithObjects:"
+ "testPowerAssertionCmd"
+ "testSMSignal"
+ "v20@0:8i16"
+ "v24@0:8d16"
+ "v24@0:8i16i20"
+ "v24@?0{shared_ptr<CLConnectionMessage>=^{CLConnectionMessage}^{__shared_weak_count}}8"
+ "v28@0:8B16@20"
+ "v32@0:8{shared_ptr<CLConnectionMessage>=^{CLConnectionMessage}^{__shared_weak_count}}16"
+ "{\"msg%{public}.0s\":\"defaultMessageHandler\", \"name\":%{public, location:escape_only}s, \"value\":%{public, location:escape_only}@}"
+ "{\"msg%{public}.0s\":\"sendCommand\", \"name\":%{public, location:escape_only}s, \"value\":%{public, location:escape_only}@}"
+ "{\"msg%{public}.0s\":\"sendTestMessage\", \"name\":%{public, location:escape_only}s, \"value\":%{public, location:escape_only}@}"
+ "{\"msg%{public}.0s\":\"sendTestSMSignal\", \"name\":%{public, location:escape_only}s, \"value\":%{public, location:escape_only}@}"
+ "{\"msg%{public}.0s\":\"sendTestSOS\", \"name\":%{public, location:escape_only}s, \"value\":%{public, location:escape_only}@}"
+ "{\"msg%{public}.0s\":\"sendTestTTR\", \"name\":%{public, location:escape_only}s, \"value\":%{public, location:escape_only}@}"
+ "{\"msg%{public}.0s\":\"sendTestTrigger\", \"name\":%{public, location:escape_only}s, \"value\":%{public, location:escape_only}@}"

```
