## assessmentagent

> `/usr/libexec/assessmentagent`

```diff

-14.2.9.0.0
-  __TEXT.__text: 0x727c4
-  __TEXT.__auth_stubs: 0x1be0
+16.0.0.0.0
+  __TEXT.__text: 0x715b4
+  __TEXT.__auth_stubs: 0x1cf0
   __TEXT.__objc_stubs: 0x700
-  __TEXT.__objc_methlist: 0xc30
-  __TEXT.__const: 0x53e4
-  __TEXT.__objc_methname: 0x1aa2
-  __TEXT.__cstring: 0x395b
+  __TEXT.__objc_methlist: 0xc40
+  __TEXT.__const: 0x5b34
+  __TEXT.__objc_methname: 0x1b1f
+  __TEXT.__cstring: 0x39fb
   __TEXT.__objc_classname: 0x52f
   __TEXT.__objc_methtype: 0x990
   __TEXT.__gcc_except_tab: 0x20
-  __TEXT.__swift5_typeref: 0x2ade
+  __TEXT.__swift5_typeref: 0x2d36
   __TEXT.__swift5_entry: 0x8
-  __TEXT.__constg_swiftt: 0x38e0
+  __TEXT.__constg_swiftt: 0x3a48
   __TEXT.__swift5_builtin: 0xb4
-  __TEXT.__swift5_reflstr: 0x24dd
-  __TEXT.__swift5_fieldmd: 0x2508
-  __TEXT.__swift5_assocty: 0x228
-  __TEXT.__swift5_proto: 0x38c
-  __TEXT.__swift5_types: 0x278
-  __TEXT.__swift5_capture: 0xab0
-  __TEXT.__swift5_protos: 0x98
-  __TEXT.__oslogstring: 0x1364
-  __TEXT.__swift_as_entry: 0x148
-  __TEXT.__swift_as_ret: 0x100
+  __TEXT.__swift5_reflstr: 0x26cd
+  __TEXT.__swift5_fieldmd: 0x2674
+  __TEXT.__swift5_assocty: 0x270
+  __TEXT.__swift5_proto: 0x3b4
+  __TEXT.__swift5_types: 0x290
+  __TEXT.__swift5_capture: 0xb9c
+  __TEXT.__swift5_protos: 0xa0
+  __TEXT.__oslogstring: 0x1404
+  __TEXT.__swift_as_entry: 0x14c
+  __TEXT.__swift_as_ret: 0x104
   __TEXT.__swift5_mpenum: 0x38
-  __TEXT.__unwind_info: 0x1b20
-  __TEXT.__eh_frame: 0x2890
-  __DATA_CONST.__auth_got: 0xe00
-  __DATA_CONST.__got: 0x7a0
-  __DATA_CONST.__auth_ptr: 0xa50
-  __DATA_CONST.__const: 0x56e8
+  __TEXT.__unwind_info: 0x1c50
+  __TEXT.__eh_frame: 0x29e0
+  __DATA_CONST.__auth_got: 0xe88
+  __DATA_CONST.__got: 0x7e8
+  __DATA_CONST.__auth_ptr: 0x880
+  __DATA_CONST.__const: 0x5bf8
   __DATA_CONST.__cfstring: 0x1c0
-  __DATA_CONST.__objc_classlist: 0x220
+  __DATA_CONST.__objc_classlist: 0x228
   __DATA_CONST.__objc_protolist: 0x2c0
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_protorefs: 0x160
   __DATA_CONST.__objc_superrefs: 0x28
-  __DATA.__objc_const: 0x4978
-  __DATA.__objc_selrefs: 0x868
+  __DATA.__objc_const: 0x4ab8
+  __DATA.__objc_selrefs: 0x890
   __DATA.__objc_ivar: 0x2c
-  __DATA.__objc_data: 0xd68
-  __DATA.__data: 0x6028
+  __DATA.__objc_data: 0xd88
+  __DATA.__data: 0x5f20
   __DATA.__common: 0x288
-  __DATA.__bss: 0x42c0
+  __DATA.__bss: 0x4740
   - /System/Library/Frameworks/AVFoundation.framework/AVFoundation
+  - /System/Library/Frameworks/AVRouting.framework/AVRouting
   - /System/Library/Frameworks/Combine.framework/Combine
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/CoreServices.framework/CoreServices

   - /System/Library/Frameworks/Network.framework/Network
   - /System/Library/Frameworks/NetworkExtension.framework/NetworkExtension
   - /System/Library/Frameworks/Security.framework/Security
+  - /System/Library/Frameworks/UIKit.framework/UIKit
   - /System/Library/PrivateFrameworks/AACCore.framework/AACCore
   - /System/Library/PrivateFrameworks/Catalyst.framework/Catalyst
   - /System/Library/PrivateFrameworks/FrontBoardServices.framework/FrontBoardServices

   - /System/Library/PrivateFrameworks/MobileKeyBag.framework/MobileKeyBag
   - /System/Library/PrivateFrameworks/RunningBoardServices.framework/RunningBoardServices
   - /System/Library/PrivateFrameworks/SpringBoardServices.framework/SpringBoardServices
-  - /System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libbsm.0.dylib
   - /usr/lib/libobjc.A.dylib

   - /usr/lib/swift/libswiftCoreFoundation.dylib
   - /usr/lib/swift/libswiftCoreImage.dylib
   - /usr/lib/swift/libswiftDarwin.dylib
-  - /usr/lib/swift/libswiftDataDetection.dylib
   - /usr/lib/swift/libswiftDispatch.dylib
   - /usr/lib/swift/libswiftMetal.dylib
   - /usr/lib/swift/libswiftOSLog.dylib

   - /usr/lib/swift/libswiftXPC.dylib
   - /usr/lib/swift/libswift_Builtin_float.dylib
   - /usr/lib/swift/libswift_Concurrency.dylib
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
-  UUID: 2BEEBA22-5C61-384D-8603-D0DB7D84A39D
-  Functions: 2265
-  Symbols:   833
-  CStrings:  927
+  UUID: A3970264-BAF1-3DFB-AAB1-9DF731C70B3D
+  Functions: 2347
+  Symbols:   866
+  CStrings:  940
 
Symbols:
+ _$s7Combine10PublishersO0A7Latest3VMn
+ _$s7Combine10PublishersO0A7Latest3VyAEy_xq_q0_Gx_q_q0_tcfC
+ _$s7Combine10PublishersO0A7Latest3Vy_xq_q0_GAA9PublisherAAMc
+ _$s7Combine10PublishersO10CompactMapVMa
+ _$s7Combine14AnyCancellableCyACxcAA0C0RzlufC
+ _$s7Combine14AnyCancellableCyACyyccfc
+ _$s7Combine18PassthroughSubjectCACyxq_GycfC
+ _$s7Combine19CurrentValueSubjectCMa
+ _$s7Combine19CurrentValueSubjectCyACyxq_GxcfC
+ _$s9ActorTypes06GlobalA0PTl
+ _$sSL1goiySbx_xtFZTq
+ _$sSL1loiySbx_xtFZTq
+ _$sSL2geoiySbx_xtFZTq
+ _$sSL2leoiySbx_xtFZTq
+ _$sSLMp
+ _$sSLSQTb
+ _$sSS10FoundationE18StandardComparatorV09localizedB0ACvgZ
+ _$sSS10FoundationE18StandardComparatorV7compareySo18NSComparisonResultVSS_SStF
+ _$sSS10FoundationE18StandardComparatorVMa
+ _$sSo17OS_dispatch_queueC8DispatchE20AutoreleaseFrequencyO8workItemyA2EmFWC
+ _$sSo24OS_dispatch_queue_serialC8DispatchE10AttributesVMa
+ _$sSo24OS_dispatch_queue_serialC8DispatchE10AttributesVMn
+ _$sSo24OS_dispatch_queue_serialC8DispatchE10AttributesVs10SetAlgebraACMc
+ _$sSo24OS_dispatch_queue_serialC8DispatchE5label3qos10attributes20autoreleaseFrequency6targetABSS_AC0E3QoSVAbCE10AttributesVSo0a1_b1_C0CACE011AutoreleaseJ0OANSgtcfC
+ _$sSo33OS_dispatch_queue_serial_executorC8DispatchE23asUnownedSerialExecutorSceyF
+ _$ss11GlobalActorMp
+ _$ss11GlobalActorP0B4TypeAB_ScATn
+ _$ss11GlobalActorP21sharedUnownedExecutorScevgZTq
+ _$ss11GlobalActorP6shared0B4TypeQzvgZTq
+ _$ss11GlobalActorPsE21sharedUnownedExecutorScevgZ
+ _$ss11_StringGutsV16_foreignCopyUTF84intoSiSgSrys5UInt8VG_tF
+ _AEAssessmentModePrivateConfigurationSPIEntitlement
+ _AECoreError
+ _AECoreErrorDomain
+ _AECoreNotInstalledParticipantsKey
+ _AECoreRestrictedSystemParticipantsKey
+ _OBJC_CLASS_$_NSError
+ _OBJC_CLASS_$_OS_dispatch_queue_serial
+ __swift_FORCE_LOAD_$_swift_DarwinFoundation1
+ __swift_FORCE_LOAD_$_swift_DarwinFoundation2
+ __swift_FORCE_LOAD_$_swift_DarwinFoundation3
+ _swift_coroFrameAlloc
+ _swift_getExtendedExistentialTypeMetadata_unique
+ _swift_initStaticObject
- _$s7Combine14AnyCancellableCyACxcAA0C0Rzlufc
- _$ss10_HashTableV8nextHole9atOrAfterAB6BucketVAF_tF
- _$ss11_StringGutsV8copyUTF84intoSiSgSrys5UInt8VG_tF
- __swift_FORCE_LOAD_$_swiftDataDetection
- __swift_FORCE_LOAD_$_swift_errno
- __swift_FORCE_LOAD_$_swift_math
- __swift_FORCE_LOAD_$_swift_signal
- __swift_FORCE_LOAD_$_swift_stdio
- __swift_FORCE_LOAD_$_swift_time
- __swift_FORCE_LOAD_$_swiftsys_time
- __swift_FORCE_LOAD_$_swiftunistd
CStrings:
+ "Missing participants (restricted system applications): %{public}s"
+ "Not applying network restrictions because the config allows network access"
+ "Removing PID %{public}d from exclusive frontmost list"
+ "_TtC15assessmentagent10AgentActor"
+ "_TtC15assessmentagent42AEAAssessmentSessionConfigurationValidator"
+ "_allowsContentCapture"
+ "_allowsNetworkAccess"
+ "allowsNetworkAntiphony"
+ "allowsNetworkSubscription"
+ "base"
+ "canUsePrivateConfigurationSPI"
+ "configurationValidator"
+ "connectionCanUsePrivateConfigurationSPI:"
+ "initWithDomain:code:userInfo:"
+ "isRequired"
+ "transform"
- "$__lazy_storage_$_missingParticipantLogger"
- "Missing participants (system restricted): %{public}s"
- "_TtC15assessmentagent27AEAMissingParticipantLogger"

```
