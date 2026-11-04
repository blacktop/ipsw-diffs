## AttentionAwareness

> `/System/Library/PrivateFrameworks/AttentionAwareness.framework/AttentionAwareness`

```diff

-265.40.4.0.0
-  __TEXT.__text: 0x36944
-  __TEXT.__objc_methlist: 0x281c
-  __TEXT.__const: 0x200
-  __TEXT.__gcc_except_tab: 0x884
-  __TEXT.__oslogstring: 0x5832
-  __TEXT.__cstring: 0x4186
-  __TEXT.__unwind_info: 0xf00
+265.60.1.0.2
+  __TEXT.__text: 0x3cca0
+  __TEXT.__objc_methlist: 0x2a2c
+  __TEXT.__const: 0x5f4
+  __TEXT.__cstring: 0x452c
+  __TEXT.__swift5_typeref: 0x13c
+  __TEXT.__swift5_capture: 0xf0
+  __TEXT.__swift5_reflstr: 0x8a
+  __TEXT.__swift5_assocty: 0x30
+  __TEXT.__constg_swiftt: 0x14c
+  __TEXT.__swift5_builtin: 0x28
+  __TEXT.__swift5_fieldmd: 0x5c
+  __TEXT.__swift5_proto: 0x28
+  __TEXT.__swift5_types: 0x10
+  __TEXT.__swift_as_entry: 0x24
+  __TEXT.__swift_as_ret: 0x18
+  __TEXT.__swift_as_cont: 0x18
+  __TEXT.__gcc_except_tab: 0x8dc
+  __TEXT.__oslogstring: 0x5d3f
+  __TEXT.__unwind_info: 0x11b8
+  __TEXT.__eh_frame: 0x2f0
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0
   __TEXT.__objc_classname: 0x0
   __TEXT.__objc_methname: 0x0
   __TEXT.__objc_methtype: 0x0
-  __DATA_CONST.__const: 0xe48
-  __DATA_CONST.__objc_classlist: 0x128
+  __DATA_CONST.__const: 0xef0
+  __DATA_CONST.__objc_classlist: 0x148
   __DATA_CONST.__objc_catlist: 0x8
   __DATA_CONST.__objc_protolist: 0xe8
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x1450
+  __DATA_CONST.__objc_selrefs: 0x1540
   __DATA_CONST.__objc_protorefs: 0x20
-  __DATA_CONST.__objc_superrefs: 0x110
+  __DATA_CONST.__objc_superrefs: 0x120
   __DATA_CONST.__objc_arraydata: 0x40
-  __DATA_CONST.__got: 0x228
-  __AUTH_CONST.__const: 0x448
-  __AUTH_CONST.__cfstring: 0x1da0
-  __AUTH_CONST.__objc_const: 0x5270
+  __DATA_CONST.__got: 0x2c0
+  __AUTH_CONST.__const: 0x6f0
+  __AUTH_CONST.__cfstring: 0x1ee0
+  __AUTH_CONST.__objc_const: 0x5758
   __AUTH_CONST.__weak_auth_got: 0x8
   __AUTH_CONST.__objc_intobj: 0xd8
   __AUTH_CONST.__objc_arrayobj: 0x18
-  __AUTH_CONST.__auth_got: 0x0
-  __AUTH.__objc_data: 0x50
-  __DATA.__objc_ivar: 0x54c
-  __DATA.__data: 0xae0
-  __DATA_DIRTY.__objc_data: 0xb40
-  __DATA_DIRTY.__data: 0x8
-  __DATA_DIRTY.__bss: 0x138
+  __AUTH_CONST.__auth_got: 0x758
+  __AUTH.__objc_data: 0x130
+  __DATA.__objc_ivar: 0x580
+  __DATA.__data: 0xb70
+  __DATA_DIRTY.__objc_data: 0xd28
+  __DATA_DIRTY.__data: 0x68
+  __DATA_DIRTY.__bss: 0x160
   - /System/Library/Frameworks/AVFoundation.framework/AVFoundation
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/CoreMotion.framework/CoreMotion

   - /System/Library/PrivateFrameworks/BiometricKit.framework/BiometricKit
   - /System/Library/PrivateFrameworks/CoreAnalytics.framework/CoreAnalytics
   - /System/Library/PrivateFrameworks/PowerLog.framework/PowerLog
+  - /System/Library/PrivateFrameworks/WirelessPerception.framework/WirelessPerception
+  - /System/Library/PrivateFrameworks/WirelessPerceptionRuntime.framework/WirelessPerceptionRuntime
   - /usr/lib/libAccessibility.dylib
   - /usr/lib/libMobileGestalt.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libbsm.0.dylib
   - /usr/lib/libc++.1.dylib
   - /usr/lib/libobjc.A.dylib
+  - /usr/lib/swift/libswiftCore.dylib
   - /usr/lib/swift/libswiftCoreFoundation.dylib
   - /usr/lib/swift/libswiftDispatch.dylib
   - /usr/lib/swift/libswiftObjectiveC.dylib
   - /usr/lib/swift/libswiftXPC.dylib
   - /usr/lib/swift/libswift_Builtin_float.dylib
+  - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
-  Functions: 973
-  Symbols:   2134
-  CStrings:  857
+  Functions: 1164
+  Symbols:   2310
+  CStrings:  905
 
Symbols:
+ +[AWWifiMotionDetectAttentionEvent supportsSecureCoding]
+ +[WirelessPerceptionEngine isWirelessPerceptionSupported]
+ +[WirelessPerceptionEngine sharedEngine]
+ -[AWFaceDetectAttentionEvent eyeWearConfidence]
+ -[AWFaceDetectAttentionEvent eyesClosedConfidence]
+ -[AWFaceDetectAttentionEvent eyesOccludedConfidence]
+ -[AWFaceDetectAttentionEvent eyesOpenConfidence]
+ -[AWFaceDetectAttentionEvent maskConfidence]
+ -[AWRemoteClient isWifiMotionDetectClient]
+ -[AWRemoteClient notifyWifiMotionDetectEvent:motionDetected:timestamp:]
+ -[AWScheduler handleWirelessPerceptionEvent:]
+ -[AWScheduler shouldActivateWifiMotionDetect]
+ -[AWWifiMotionDetectAttentionEvent description]
+ -[AWWifiMotionDetectAttentionEvent encodeWithCoder:]
+ -[AWWifiMotionDetectAttentionEvent initWithCoder:]
+ -[AWWifiMotionDetectAttentionEvent initWithTimestamp:tagIndex:motionDetected:]
+ -[AWWifiMotionDetectAttentionEvent motionDetected]
+ -[AWWifiMotionDetectAttentionEvent validateMask]
+ -[WirelessPerceptionEngine .cxx_destruct]
+ -[WirelessPerceptionEngine cancelRetryTimer]
+ -[WirelessPerceptionEngine dealloc]
+ -[WirelessPerceptionEngine initWithQueue:]
+ -[WirelessPerceptionEngine registerCallbackBlock:]
+ -[WirelessPerceptionEngine scheduleRetry]
+ -[WirelessPerceptionEngine setupAndStartWirelessPerception]
+ -[WirelessPerceptionEngine stopWirelessPerception]
+ GCC_except_table122
+ GCC_except_table123
+ GCC_except_table169
+ GCC_except_table174
+ GCC_except_table189
+ GCC_except_table208
+ GCC_except_table214
+ GCC_except_table239
+ GCC_except_table273
+ GCC_except_table297
+ GCC_except_table351
+ GCC_except_table363
+ GCC_except_table382
+ GCC_except_table446
+ GCC_except_table447
+ GCC_except_table515
+ GCC_except_table519
+ GCC_except_table533
+ GCC_except_table544
+ GCC_except_table548
+ GCC_except_table552
+ GCC_except_table557
+ GCC_except_table56
+ GCC_except_table561
+ GCC_except_table565
+ GCC_except_table632
+ GCC_except_table656
+ GCC_except_table728
+ GCC_except_table84
+ GCC_except_table882
+ GCC_except_table914
+ GCC_except_table918
+ GCC_except_table922
+ GCC_except_table925
+ GCC_except_table927
+ GCC_except_table929
+ GCC_except_table930
+ GCC_except_table940
+ GCC_except_table942
+ GCC_except_table947
+ GCC_except_table953
+ GCC_except_table955
+ _CFPreferencesGetAppBooleanValue
+ _MGIsDeviceOfType
+ _OBJC_CLASS_$_AWWifiMotionDetectAttentionEvent
+ _OBJC_CLASS_$_WirelessPerceptionEngine
+ _OBJC_CLASS_$__TtC18AttentionAwareness24WirelessPerceptionHelper
+ _OBJC_CLASS_$__TtC18AttentionAwareness24WirelessPerceptionOutput
+ _OBJC_IVAR_$_AWFaceDetectAttentionEvent._eyeWearConfidence
+ _OBJC_IVAR_$_AWFaceDetectAttentionEvent._eyesClosedConfidence
+ _OBJC_IVAR_$_AWFaceDetectAttentionEvent._eyesOccludedConfidence
+ _OBJC_IVAR_$_AWFaceDetectAttentionEvent._eyesOpenConfidence
+ _OBJC_IVAR_$_AWFaceDetectAttentionEvent._maskConfidence
+ _OBJC_IVAR_$_AWRemoteClient._firstWifiMotionEventDelivered
+ _OBJC_IVAR_$_AWScheduler._wifiMotionDetectStarted
+ _OBJC_IVAR_$_AWScheduler._wirelessPerceptionEngine
+ _OBJC_IVAR_$_AWWifiMotionDetectAttentionEvent._motionDetected
+ _OBJC_IVAR_$_WirelessPerceptionEngine._callbackBlock
+ _OBJC_IVAR_$_WirelessPerceptionEngine._lastOutput
+ _OBJC_IVAR_$_WirelessPerceptionEngine._queue
+ _OBJC_IVAR_$_WirelessPerceptionEngine._retryTimer
+ _OBJC_IVAR_$_WirelessPerceptionEngine._wirelessPerceptionHelper
+ _OBJC_METACLASS_$_AWWifiMotionDetectAttentionEvent
+ _OBJC_METACLASS_$_WirelessPerceptionEngine
+ _OBJC_METACLASS_$__TtC18AttentionAwareness24WirelessPerceptionHelper
+ _OBJC_METACLASS_$__TtC18AttentionAwareness24WirelessPerceptionOutput
+ _WirelessPerceptionHelperErrorDomain_block_invoke.onceToken
+ __Block_copy
+ __Block_release
+ __CLASS_METHODS__TtC18AttentionAwareness24WirelessPerceptionHelper
+ __CLASS_PROPERTIES__TtC18AttentionAwareness24WirelessPerceptionHelper
+ __DATA__TtC18AttentionAwareness24WirelessPerceptionHelper
+ __DATA__TtC18AttentionAwareness24WirelessPerceptionOutput
+ __INSTANCE_METHODS__TtC18AttentionAwareness24WirelessPerceptionHelper
+ __INSTANCE_METHODS__TtC18AttentionAwareness24WirelessPerceptionOutput
+ __IVARS__TtC18AttentionAwareness24WirelessPerceptionHelper
+ __IVARS__TtC18AttentionAwareness24WirelessPerceptionOutput
+ __METACLASS_DATA__TtC18AttentionAwareness24WirelessPerceptionHelper
+ __METACLASS_DATA__TtC18AttentionAwareness24WirelessPerceptionOutput
+ __OBJC_$_CLASS_METHODS_AWWifiMotionDetectAttentionEvent
+ __OBJC_$_CLASS_METHODS_WirelessPerceptionEngine
+ __OBJC_$_CLASS_PROP_LIST_AWWifiMotionDetectAttentionEvent
+ __OBJC_$_INSTANCE_METHODS_AWWifiMotionDetectAttentionEvent
+ __OBJC_$_INSTANCE_METHODS_WirelessPerceptionEngine
+ __OBJC_$_INSTANCE_VARIABLES_AWWifiMotionDetectAttentionEvent
+ __OBJC_$_INSTANCE_VARIABLES_WirelessPerceptionEngine
+ __OBJC_$_PROP_LIST_AWWifiMotionDetectAttentionEvent
+ __OBJC_CLASS_PROTOCOLS_$_AWWifiMotionDetectAttentionEvent
+ __OBJC_CLASS_RO_$_AWWifiMotionDetectAttentionEvent
+ __OBJC_CLASS_RO_$_WirelessPerceptionEngine
+ __OBJC_METACLASS_RO_$_AWWifiMotionDetectAttentionEvent
+ __OBJC_METACLASS_RO_$_WirelessPerceptionEngine
+ __PROPERTIES__TtC18AttentionAwareness24WirelessPerceptionOutput
+ ___40+[WirelessPerceptionEngine sharedEngine]_block_invoke
+ ___41-[WirelessPerceptionEngine scheduleRetry]_block_invoke
+ ___45-[AWScheduler handleWirelessPerceptionEvent:]_block_invoke
+ ___45-[AWScheduler shouldActivateWifiMotionDetect]_block_invoke
+ ___50-[WirelessPerceptionEngine stopWirelessPerception]_block_invoke
+ ___59-[WirelessPerceptionEngine setupAndStartWirelessPerception]_block_invoke
+ ___block_descriptor_32_e17_v16?0"NSError"8l
+ ___block_descriptor_40_e8_32w_e17_v16?0"NSError"8lw32l8
+ ___block_descriptor_40_e8_32w_e60_v16?0"_TtC18AttentionAwareness24WirelessPerceptionOutput"8lw32l8
+ ___block_descriptor_40_e8_32w_e8_v16?0q8lw32l8
+ ___chkstk_darwin
+ ___isRGBFaceDetectFeatureEnabled_block_invoke
+ ___swift__destructor
+ ___swift_async_cont_functlets
+ ___swift_async_entry_functlets
+ ___swift_async_ret_functlets
+ ___swift_closure_destructor
+ ___swift_closure_destructor.20Tm
+ ___swift_closure_destructor.24Tm
+ ___swift_instantiateConcreteTypeFromMangledNameV2
+ __os_feature_enabled_impl
+ __swift_stdlib_reportUnimplementedInitializer
+ _associated conformance 18AttentionAwareness29WirelessPerceptionHelperErrorO10Foundation021_ObjectiveCBridgeableF0AAs0F0
+ _associated conformance 18AttentionAwareness29WirelessPerceptionHelperErrorO10Foundation15_BridgedNSErrorAA8RawValueSY_s17FixedWidthInteger
+ _associated conformance 18AttentionAwareness29WirelessPerceptionHelperErrorO10Foundation15_BridgedNSErrorAASH
+ _associated conformance 18AttentionAwareness29WirelessPerceptionHelperErrorO10Foundation15_BridgedNSErrorAASY
+ _associated conformance 18AttentionAwareness29WirelessPerceptionHelperErrorO10Foundation15_BridgedNSErrorAaD021_ObjectiveCBridgeableF0
+ _associated conformance 18AttentionAwareness29WirelessPerceptionHelperErrorOSHAASQ
+ _associated conformance 18AttentionAwareness30WirelessPerceptionNotificationOSHAASQ
+ _doesPlatformSupportFaceDetectEvent
+ _doesPlatformSupportRGBFaceDetect.supported
+ _isRGBFaceDetectFeatureEnabled.enabled
+ _isRGBFaceDetectFeatureEnabled.onceToken
+ _objc_allocWithZone
+ _objc_opt_self
+ _swift_allocError
+ _swift_allocObject
+ _swift_beginAccess
+ _swift_bridgeObjectRelease
+ _swift_deallocObject
+ _swift_dynamicCast
+ _swift_endAccess
+ _swift_errorRelease
+ _swift_errorRetain
+ _swift_getObjectType
+ _swift_getTypeByMangledNameInContext2
+ _swift_getWitnessTable
+ _swift_isaMask
+ _swift_lookUpClassMethod
+ _swift_once
+ _swift_release
+ _swift_release_x1
+ _swift_release_x19
+ _swift_release_x20
+ _swift_release_x21
+ _swift_release_x25
+ _swift_release_x8
+ _swift_retain
+ _swift_retain_x1
+ _swift_retain_x19
+ _swift_retain_x20
+ _swift_retain_x21
+ _swift_retain_x22
+ _swift_task_alloc
+ _swift_task_create
+ _swift_task_dealloc
+ _swift_task_switch
+ _swift_unknownObjectRelease
+ _swift_unknownObjectRetain
+ _swift_unknownObjectWeakDestroy
+ _swift_unknownObjectWeakInit
+ _swift_unknownObjectWeakLoadStrong
+ _swift_willThrow
+ _symbolic $sSY
+ _symbolic IeAgH_
+ _symbolic IeghH_
+ _symbolic Sb
+ _symbolic ScA_pSg
+ _symbolic ScPSg
+ _symbolic ScTyyt_____GSg s5NeverO
+ _symbolic Scsy___________pG 25WirelessPerceptionRuntime11MotionEventV s5ErrorP
+ _symbolic Si
+ _symbolic So7NSErrorCSgIeyBy_
+ _symbolic So8NSObjectC
+ _symbolic _____ 18AttentionAwareness24WirelessPerceptionHelperC
+ _symbolic _____ 18AttentionAwareness24WirelessPerceptionOutputC
+ _symbolic _____ 18AttentionAwareness29WirelessPerceptionHelperErrorO
+ _symbolic _____ 18AttentionAwareness30WirelessPerceptionNotificationO
+ _symbolic _____IeyBy_ 18AttentionAwareness24WirelessPerceptionOutputC
+ _symbolic _____IeyBy_ 18AttentionAwareness30WirelessPerceptionNotificationO
+ _symbolic _____Sg 18WirelessPerception0aB6MotionC
+ _symbolic _____Sg 25WirelessPerceptionRuntime11MotionEventV
+ _symbolic _____SgXw 18AttentionAwareness24WirelessPerceptionHelperC
+ _symbolic _____SgXwz_Xx 18AttentionAwareness24WirelessPerceptionHelperC
+ _symbolic ______p s5ErrorP
+ _symbolic _____y___________p_G Scs8IteratorV 25WirelessPerceptionRuntime11MotionEventV s5ErrorP
+ _symbolic y_____cSg 18AttentionAwareness24WirelessPerceptionOutputC
+ _symbolic y_____cSg 18AttentionAwareness30WirelessPerceptionNotificationO
+ _symbolic ytIeAgHr_
- GCC_except_table118
- GCC_except_table119
- GCC_except_table165
- GCC_except_table166
- GCC_except_table185
- GCC_except_table204
- GCC_except_table206
- GCC_except_table231
- GCC_except_table267
- GCC_except_table291
- GCC_except_table345
- GCC_except_table357
- GCC_except_table376
- GCC_except_table440
- GCC_except_table441
- GCC_except_table511
- GCC_except_table517
- GCC_except_table522
- GCC_except_table526
- GCC_except_table530
- GCC_except_table535
- GCC_except_table543
- GCC_except_table610
- GCC_except_table634
- GCC_except_table706
- GCC_except_table80
- GCC_except_table848
- GCC_except_table854
- GCC_except_table880
- GCC_except_table884
- GCC_except_table891
- GCC_except_table893
- GCC_except_table895
- GCC_except_table896
- GCC_except_table906
- GCC_except_table908
- GCC_except_table913
- GCC_except_table919
- GCC_except_table921
- _CARColorFilterIntensityBlueYellowKey_block_invoke.onceToken
- _OBJC_IVAR_$_AWScheduler._useAVFoundation
- _doesPlatformSupportRGBFaceDetect.answer
CStrings:
+ "%13.5f: Activating WifiMotionDetect"
+ "%13.5f: Attention detection %s"
+ "%13.5f: Callback block not configured for WirelessPerceptionEngine"
+ "%13.5f: Deactivating WifiMotionDetect"
+ "%13.5f: Error %@ when trying to stop WirelessPerception"
+ "%13.5f: Using AVFoundation for RGB Face detect operations (allowRGBFaceDetect=%s, hasPearl=%s)"
+ "%13.5f: WirelessPerception error %@ received, retrying in %.0f seconds"
+ "%13.5f: WirelessPerception event received: %@"
+ "%13.5f: WirelessPerception interrupted, retrying in %.0f seconds"
+ "%13.5f: WirelessPerception not supported on this device"
+ "%13.5f: WirelessPerception not supported on this device: %@"
+ "%13.5f: WirelessPerception notification %ld received"
+ "%30s:%-4d: %13.5f: %d active WifiMotion clients"
+ "%30s:%-4d: %13.5f: Activating WifiMotionDetect"
+ "%30s:%-4d: %13.5f: Attention detection %s"
+ "%30s:%-4d: %13.5f: Deactivating WifiMotionDetect"
+ "%30s:%-4d: %13.5f: Error %@ when trying to stop WirelessPerception"
+ "%30s:%-4d: %13.5f: Received event %@ from WirelessPerceptionEngine"
+ "%30s:%-4d: %13.5f: Using AVFoundation for RGB Face detect operations (allowRGBFaceDetect=%s, hasPearl=%s)"
+ "%30s:%-4d: %13.5f: WirelessPerception error %@ received, retrying in %.0f seconds"
+ "%30s:%-4d: %13.5f: WirelessPerception event received: %@"
+ "%30s:%-4d: %13.5f: WirelessPerception interrupted, retrying in %.0f seconds"
+ "%30s:%-4d: %13.5f: WirelessPerception not supported on this device"
+ "%30s:%-4d: %13.5f: WirelessPerception not supported on this device: %@"
+ "%30s:%-4d: %13.5f: WirelessPerception notification %ld received"
+ "-[AWRemoteClient notifyWifiMotionDetectEvent:motionDetected:timestamp:]"
+ "-[AWWifiMotionDetectAttentionEvent validateMask]"
+ "/Library/Caches/com.apple.xbs/<UUID>/TemporaryDirectory.<TMP>/Sources/AttentionAwareness/Framework/XPCService/WirelessPerception/WirelessPerceptionEngine.m"
+ "<%@: %p> (timestamp: %13.5f motionDetected: %u %@)"
+ "AttentionAwareness.WirelessPerceptionHelperError"
+ "AttentionAwareness.WirelessPerceptionOutput"
+ "NO"
+ "RGBFaceDetect"
+ "RGBFaceDetectEnabled"
+ "WifiMotionDetect|"
+ "WirelessPerception motionDetected: "
+ "WirelessPerceptionErrorDomain"
+ "WirelessPerceptionNotSupported"
+ "YES"
+ "enabled"
+ "eyeWearConfidence"
+ "eyesClosedConfidence"
+ "eyesOccludedConfidence"
+ "eyesOpenConfidence"
+ "init()"
+ "mask == AWAttentionEventMaskWifiMotionDetect"
+ "maskConfidence"
+ "motionDetected"
+ "not supported"
+ "self.eventMask == AWAttentionEventMaskWifiMotionDetect"
+ "v16@?0@\"_TtC18AttentionAwareness24WirelessPerceptionOutput\"8"
+ "v16@?0q8"
+ "\xc1"
- "%13.5f: RGB metadata received on a AWFaceDetectAttentionEvent class, not passing it to client %@"
- "%13.5f: Using AVFoundation for RGB Face detect operations"
- "%30s:%-4d: %13.5f: Using AVFoundation for RGB Face detect operations"
- "AVFoundation"
- "\x81"
```
