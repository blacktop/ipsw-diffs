## pcapd

> `/usr/libexec/pcapd`

```diff

-66.0.0.0.0
-  __TEXT.__text: 0xc048
-  __TEXT.__auth_stubs: 0x820
-  __TEXT.__const: 0xd0
-  __TEXT.__cstring: 0xce7
-  __TEXT.__oslogstring: 0x24f8
-  __TEXT.__unwind_info: 0x178
-  __DATA_CONST.__auth_got: 0x410
-  __DATA_CONST.__got: 0xb0
-  __DATA_CONST.__const: 0x2f8
-  __DATA.__data: 0x290
-  __DATA.__crash_info: 0x40
-  __DATA.__bss: 0x1058
+73.0.0.0.0
+  __TEXT.__text: 0xe7a0
+  __TEXT.__auth_stubs: 0xc80
+  __TEXT.__objc_stubs: 0x20
+  __TEXT.__objc_methlist: 0x2c
+  __TEXT.__const: 0x182
+  __TEXT.__cstring: 0xe34
+  __TEXT.__oslogstring: 0x2644
+  __TEXT.__swift5_typeref: 0xca
+  __TEXT.__swift5_capture: 0x5c
+  __TEXT.__objc_methname: 0x2d
+  __TEXT.__constg_swiftt: 0xe0
+  __TEXT.__swift5_reflstr: 0xe
+  __TEXT.__swift5_fieldmd: 0x38
+  __TEXT.__swift5_types: 0x8
+  __TEXT.__swift_as_entry: 0xc
+  __TEXT.__swift_as_ret: 0xc
+  __TEXT.__unwind_info: 0x238
+  __TEXT.__eh_frame: 0x110
+  __DATA_CONST.__auth_got: 0x648
+  __DATA_CONST.__got: 0xf0
+  __DATA_CONST.__auth_ptr: 0x40
+  __DATA_CONST.__const: 0x4d8
+  __DATA_CONST.__objc_classlist: 0x8
+  __DATA_CONST.__objc_imageinfo: 0x8
+  __DATA.__objc_const: 0x98
+  __DATA.__objc_selrefs: 0x20
+  __DATA.__objc_data: 0xd8
+  __DATA.__data: 0x318
+  __DATA.__crash_info: 0x148
+  __DATA.__bss: 0x10f0
   __DATA.__common: 0x14
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
+  - /System/Library/Frameworks/Foundation.framework/Foundation
+  - /System/Library/PrivateFrameworks/NetworkInfo.framework/NetworkInfo
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/liblockdown.dylib
+  - /usr/lib/libobjc.A.dylib
   - /usr/lib/libpcap.A.dylib
-  UUID: 45D21BC4-9529-3386-8730-ABC459F4A9A6
-  Functions: 160
-  Symbols:   166
-  CStrings:  350
+  - /usr/lib/swift/libswiftCore.dylib
+  - /usr/lib/swift/libswiftCoreFoundation.dylib
+  - /usr/lib/swift/libswiftDarwin.dylib
+  - /usr/lib/swift/libswiftDispatch.dylib
+  - /usr/lib/swift/libswiftOSLog.dylib
+  - /usr/lib/swift/libswiftObjectiveC.dylib
+  - /usr/lib/swift/libswiftXPC.dylib
+  - /usr/lib/swift/libswift_Builtin_float.dylib
+  - /usr/lib/swift/libswift_Concurrency.dylib
+  - /usr/lib/swift/libswift_DarwinFoundation1.dylib
+  - /usr/lib/swift/libswift_DarwinFoundation2.dylib
+  - /usr/lib/swift/libswift_DarwinFoundation3.dylib
+  - /usr/lib/swift/libswiftos.dylib
+  UUID: 55154CEA-70B4-34FB-9366-8CE2DDA84090
+  Functions: 214
+  Symbols:   267
+  CStrings:  375
 
Symbols:
+ _$s11NetworkInfo10TraceRouteC5trace7domainsSayAA0cD9ResultSetVGSaySSG_tYaFZ
+ _$s11NetworkInfo10TraceRouteC5trace7domainsSayAA0cD9ResultSetVGSaySSG_tYaFZTu
+ _$s11NetworkInfo10TraceRouteCMa
+ _$s11NetworkInfo17TraceRouteOptionsC6targetSSvgTj
+ _$s11NetworkInfo17TracerouteRequestV7optionsAA17TraceRouteOptionsCvg
+ _$s11NetworkInfo17TracerouteRequestVMa
+ _$s11NetworkInfo17TracerouteRequestVMn
+ _$s11NetworkInfo17TracerouteRequestVSeAAMc
+ _$s11NetworkInfo18TracerouteResponseV7resultsACSayAA19TraceRouteResultSetVG_tcfC
+ _$s11NetworkInfo18TracerouteResponseVMa
+ _$s11NetworkInfo18TracerouteResponseVMn
+ _$s11NetworkInfo18TracerouteResponseVSEAAMc
+ _$s11NetworkInfo19TraceRouteResultSetVMn
+ _$s2os6LoggerV9logObjectSo03OS_a1_C0Cvg
+ _$s2os6LoggerV9subsystem8categoryACSS_SStcfC
+ _$s2os6LoggerVMa
+ _$s2os6LoggerVMn
+ _$s3XPC11XPCListenerC21InitializationOptionsV4noneAEvgZ
+ _$s3XPC11XPCListenerC21InitializationOptionsVMa
+ _$s3XPC11XPCListenerC22IncomingSessionRequestC6accept22incomingMessageHandler012cancellationI0AE8DecisionVSE_pSgAA011XPCReceivedH0Vc_yAA12XPCRichErrorVcSgtFTj
+ _$s3XPC11XPCListenerC7service11targetQueue7options11requirement22incomingSessionHandlerACSS_So17OS_dispatch_queueCSgAC21InitializationOptionsVAA18XPCPeerRequirementVAC08IncomingI7RequestC8DecisionVAQctKcfC
+ _$s3XPC11XPCListenerCMa
+ _$s3XPC18XPCPeerRequirementV14hasEntitlementyACSSFZ
+ _$s3XPC18XPCPeerRequirementV14isPlatformCode27andMatchesSigningIdentifierACSSSg_tFZ
+ _$s3XPC18XPCPeerRequirementVMa
+ _$s3XPC18XPCReceivedMessageV15senderSatisfiesySbAA18XPCPeerRequirementVF
+ _$s3XPC18XPCReceivedMessageV6decode2asxxm_tKSeRzlF
+ _$sBOWV
+ _$sScA15unownedExecutorScevgTj
+ _$sScP8rawValues5UInt8Vvg
+ _$sScPMa
+ _$sSo13os_log_type_ta0A0E5debugABvgZ
+ _$sSo13os_log_type_ta0A0E5errorABvgZ
+ _$sSo21OS_dispatch_semaphoreC8DispatchE4waityyF
+ _$sSo21OS_dispatch_semaphoreC8DispatchE6signalSiyF
+ _$sSqMa
+ _$ss23_ContiguousArrayStorageCMn
+ _$ss5ErrorMp
+ _$ss5ErrorWS
+ _$ss6ResultOMa
+ _$ss6ResultOMn
+ _$sytN
+ _OBJC_CLASS_$_NSObject
+ _OBJC_METACLASS_$_NSObject
+ _OBJC_METACLASS_$__TtCs12_SwiftObject
+ ___chkstk_darwin
+ __objc_empty_cache
+ __swift_FORCE_LOAD_$_swiftCoreFoundation
+ __swift_FORCE_LOAD_$_swiftDarwin
+ __swift_FORCE_LOAD_$_swiftDispatch
+ __swift_FORCE_LOAD_$_swiftFoundation
+ __swift_FORCE_LOAD_$_swiftOSLog
+ __swift_FORCE_LOAD_$_swiftObjectiveC
+ __swift_FORCE_LOAD_$_swiftXPC
+ __swift_FORCE_LOAD_$_swift_Builtin_float
+ __swift_FORCE_LOAD_$_swift_DarwinFoundation1
+ __swift_FORCE_LOAD_$_swift_DarwinFoundation2
+ __swift_FORCE_LOAD_$_swift_DarwinFoundation3
+ __swift_FORCE_LOAD_$_swiftos
+ __swift_stdlib_bridgeErrorToNSError
+ _dispatch_semaphore_create
+ _fsctl
+ _objc_allocWithZone
+ _objc_alloc_init
+ _objc_msgSend
+ _objc_msgSendSuper2
+ _objc_release
+ _objc_release_x20
+ _objc_release_x8
+ _objc_retain
+ _objc_retain_x20
+ _objc_retain_x24
+ _swift_allocBox
+ _swift_allocObject
+ _swift_allocateGenericClassMetadata
+ _swift_bridgeObjectRelease
+ _swift_bridgeObjectRetain
+ _swift_deallocClassInstance
+ _swift_deallocObject
+ _swift_deletedMethodError
+ _swift_errorRelease
+ _swift_errorRetain
+ _swift_getGenericMetadata
+ _swift_getObjectType
+ _swift_getSingletonMetadata
+ _swift_getTypeByMangledNameInContext2
+ _swift_getTypeByMangledNameInContextInMetadataState2
+ _swift_getWitnessTable
+ _swift_initClassMetadata2
+ _swift_release
+ _swift_retain
+ _swift_slowAlloc
+ _swift_slowDealloc
+ _swift_task_alloc
+ _swift_task_create
+ _swift_task_dealloc
+ _swift_task_switch
+ _swift_unknownObjectRelease
+ _swift_unknownObjectRetain
+ _swift_updateClassMetadata2
+ _swift_willThrowTypedImpl
CStrings:
+ "%s:%d %s pktap_filters are full"
+ "%s:%d Marking %s as purgeable\n"
+ "%s:%d Setting filter_param_if_name to %s"
+ "%s:%d Setting filter_param_if_name to %s\n"
+ "%s:%d ioctl(SIOCGDRVSPEC, %s): errno=%d"
+ "%s:%d ioctl(SIOCGDRVSPEC, %s): errno=%d\n"
+ "%s:%d ioctl(SIOCSDRVSPEC, %s), errno=%d"
+ "%s:%d ioctl(SIOCSDRVSPEC, %s), errno=%d\n"
+ "%s:%d socket(PF_INET, SOCK_DGRAM) failed, errno=%d"
+ "%s:%d socket(PF_INET, SOCK_DGRAM) failed, errno=%d\n"
+ "%{public}s:%d Failed to mark pcap as purgeable at %{public}s\n"
+ "%{public}s:%d Invalid NULL command\n"
+ ".cxx_destruct"
+ "@16@0:8"
+ "Problem setting up listener %@"
+ "com.apple.pcapd-traceroute"
+ "com.apple.private.traceroute-client"
+ "could not traceroute: %@"
+ "createXPCListener"
+ "dealloc"
+ "enable_pktap_filter"
+ "init"
+ "logger"
+ "missing entitlement"
+ "purgeable"
+ "result"
+ "v16@0:8"
- "%{public}s:%d pcc or ppc_temp_file_path is NULL\n"
- "%{public}s:%d ppc_final_file_path is NULL\n"
- "move_pcap_files"

```
