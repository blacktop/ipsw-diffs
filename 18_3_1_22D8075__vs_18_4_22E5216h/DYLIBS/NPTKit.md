## NPTKit

> `/System/Library/PrivateFrameworks/NPTKit.framework/NPTKit`

```diff

-164.1.0.0.0
-  __TEXT.__text: 0x3c27c
-  __TEXT.__auth_stubs: 0xa50
-  __TEXT.__objc_methlist: 0x45d0
-  __TEXT.__const: 0xf8
-  __TEXT.__cstring: 0x3b79
-  __TEXT.__gcc_except_tab: 0xacc
-  __TEXT.__oslogstring: 0xb97
-  __TEXT.__unwind_info: 0x848
-  __TEXT.__objc_classname: 0x3eb
-  __TEXT.__objc_methname: 0xdcc1
-  __TEXT.__objc_methtype: 0x1a25
-  __TEXT.__objc_stubs: 0x85c0
-  __DATA_CONST.__got: 0x310
-  __DATA_CONST.__const: 0xa08
-  __DATA_CONST.__objc_classlist: 0xf0
+175.0.0.0.0
+  __TEXT.__text: 0x4e72c
+  __TEXT.__auth_stubs: 0x1190
+  __TEXT.__objc_methlist: 0x4c24
+  __TEXT.__const: 0x3f8
+  __TEXT.__cstring: 0x423a
+  __TEXT.__gcc_except_tab: 0xad4
+  __TEXT.__oslogstring: 0x10d5
+  __TEXT.__swift5_typeref: 0x681
+  __TEXT.__swift5_capture: 0x430
+  __TEXT.__constg_swiftt: 0x124
+  __TEXT.__swift5_reflstr: 0x24a
+  __TEXT.__swift5_fieldmd: 0x1c0
+  __TEXT.__swift5_builtin: 0x14
+  __TEXT.__swift5_types: 0x18
+  __TEXT.__swift_as_entry: 0x54
+  __TEXT.__swift_as_ret: 0x54
+  __TEXT.__swift5_assocty: 0x18
+  __TEXT.__swift5_proto: 0xc
+  __TEXT.__unwind_info: 0xd50
+  __TEXT.__eh_frame: 0x880
+  __TEXT.__objc_classname: 0x3b1
+  __TEXT.__objc_methname: 0xdf47
+  __TEXT.__objc_methtype: 0x1967
+  __TEXT.__objc_stubs: 0x8520
+  __DATA_CONST.__got: 0x3a8
+  __DATA_CONST.__const: 0xa88
+  __DATA_CONST.__objc_classlist: 0xf8
   __DATA_CONST.__objc_catlist: 0x70
   __DATA_CONST.__objc_protolist: 0x80
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x32a8
+  __DATA_CONST.__objc_selrefs: 0x3578
   __DATA_CONST.__objc_protorefs: 0x10
   __DATA_CONST.__objc_superrefs: 0x80
   __DATA_CONST.__objc_arraydata: 0x2c8
-  __AUTH_CONST.__auth_got: 0x538
-  __AUTH_CONST.__const: 0xe0
-  __AUTH_CONST.__cfstring: 0x5e00
-  __AUTH_CONST.__objc_const: 0xcb38
+  __AUTH_CONST.__auth_got: 0x8d8
+  __AUTH_CONST.__auth_ptr: 0xc0
+  __AUTH_CONST.__const: 0xe88
+  __AUTH_CONST.__cfstring: 0x5fc0
+  __AUTH_CONST.__objc_const: 0xc4a8
   __AUTH_CONST.__objc_intobj: 0x2e8
   __AUTH_CONST.__objc_dictobj: 0x28
   __AUTH_CONST.__objc_arrayobj: 0xc0
-  __AUTH.__objc_data: 0x1e0
-  __DATA.__objc_ivar: 0x744
-  __DATA.__data: 0x600
-  __DATA.__bss: 0x10
+  __AUTH.__objc_data: 0x140
+  __AUTH.__data: 0x260
+  __DATA.__objc_ivar: 0x73c
+  __DATA.__data: 0x838
+  __DATA.__bss: 0x180
+  __DATA.__common: 0x30
   __DATA_DIRTY.__objc_data: 0x780
   - /System/Library/Frameworks/CFNetwork.framework/CFNetwork
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation

   - /System/Library/PrivateFrameworks/CoreAnalytics.framework/CoreAnalytics
   - /System/Library/PrivateFrameworks/CoreWiFi.framework/CoreWiFi
   - /System/Library/PrivateFrameworks/ProtocolBuffer.framework/ProtocolBuffer
+  - /System/Library/PrivateFrameworks/Rapport.framework/Rapport
   - /System/Library/PrivateFrameworks/WiFiVelocity.framework/WiFiVelocity
   - /System/Library/PrivateFrameworks/WirelessCoexManager.framework/WirelessCoexManager
   - /System/Library/PrivateFrameworks/WirelessInsights.framework/WirelessInsights

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libnetquality.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 1559
-  Symbols:   2125
-  CStrings:  3643
+  - /usr/lib/swift/libswiftCore.dylib
+  - /usr/lib/swift/libswiftCoreAudio.dylib
+  - /usr/lib/swift/libswiftCoreFoundation.dylib
+  - /usr/lib/swift/libswiftDarwin.dylib
+  - /usr/lib/swift/libswiftDispatch.dylib
+  - /usr/lib/swift/libswiftMetal.dylib
+  - /usr/lib/swift/libswiftOSLog.dylib
+  - /usr/lib/swift/libswiftObjectiveC.dylib
+  - /usr/lib/swift/libswiftQuartzCore.dylib
+  - /usr/lib/swift/libswiftXPC.dylib
+  - /usr/lib/swift/libswift_Builtin_float.dylib
+  - /usr/lib/swift/libswift_Concurrency.dylib
+  - /usr/lib/swift/libswift_errno.dylib
+  - /usr/lib/swift/libswift_math.dylib
+  - /usr/lib/swift/libswift_signal.dylib
+  - /usr/lib/swift/libswift_stdio.dylib
+  - /usr/lib/swift/libswift_time.dylib
+  - /usr/lib/swift/libswiftos.dylib
+  - /usr/lib/swift/libswiftsys_time.dylib
+  - /usr/lib/swift/libswiftunistd.dylib
+  Functions: 2035
+  Symbols:   2272
+  CStrings:  3735
 
Symbols:
+ _NSClassFromString
+ _NSStringFromClass
+ _OBJC_CLASS_$_NSKeyedArchiver
+ _OBJC_CLASS_$_NSKeyedUnarchiver
+ _OBJC_CLASS_$_RPCompanionLinkClient
+ _OBJC_CLASS_$_RPCompanionLinkDevice
+ _OBJC_CLASS_$__TtCs12_SwiftObject
+ _OBJC_METACLASS_$__TtCs12_SwiftObject
+ __Block_copy
+ __Block_release
+ ___chkstk_darwin
+ __swiftEmptyArrayStorage
+ __swiftEmptyDictionarySingleton
+ __swiftEmptySetSingleton
+ __swiftImmortalRefCount
+ __swift_FORCE_LOAD_$_swiftCoreAudio
+ __swift_FORCE_LOAD_$_swiftCoreFoundation
+ __swift_FORCE_LOAD_$_swiftDarwin
+ __swift_FORCE_LOAD_$_swiftDispatch
+ __swift_FORCE_LOAD_$_swiftFoundation
+ __swift_FORCE_LOAD_$_swiftMetal
+ __swift_FORCE_LOAD_$_swiftOSLog
+ __swift_FORCE_LOAD_$_swiftObjectiveC
+ __swift_FORCE_LOAD_$_swiftQuartzCore
+ __swift_FORCE_LOAD_$_swiftXPC
+ __swift_FORCE_LOAD_$_swift_Builtin_float
+ __swift_FORCE_LOAD_$_swift_errno
+ __swift_FORCE_LOAD_$_swift_math
+ __swift_FORCE_LOAD_$_swift_signal
+ __swift_FORCE_LOAD_$_swift_stdio
+ __swift_FORCE_LOAD_$_swift_time
+ __swift_FORCE_LOAD_$_swiftos
+ __swift_FORCE_LOAD_$_swiftsys_time
+ __swift_FORCE_LOAD_$_swiftunistd
+ __swift_stdlib_bridgeErrorToNSError
+ _bzero
+ _malloc_size
+ _memmove
+ _objc_allocWithZone
+ _objc_opt_self
+ _objc_retainAutoreleasedReturnValue
+ _swift_allocError
+ _swift_allocObject
+ _swift_arrayDestroy
+ _swift_arrayInitWithCopy
+ _swift_beginAccess
+ _swift_bridgeObjectRelease
+ _swift_bridgeObjectRelease_n
+ _swift_bridgeObjectRetain
+ _swift_bridgeObjectRetain_n
+ _swift_continuation_await
+ _swift_continuation_init
+ _swift_continuation_resume
+ _swift_continuation_throwingResume
+ _swift_continuation_throwingResumeWithError
+ _swift_deallocClassInstance
+ _swift_deallocObject
+ _swift_deletedMethodError
+ _swift_dynamicCast
+ _swift_endAccess
+ _swift_errorRelease
+ _swift_errorRetain
+ _swift_getForeignTypeMetadata
+ _swift_getObjCClassMetadata
+ _swift_getObjectType
+ _swift_getTypeByMangledNameInContext2
+ _swift_getWitnessTable
+ _swift_initStackObject
+ _swift_isUniquelyReferenced_nonNull_native
+ _swift_lookUpClassMethod
+ _swift_once
+ _swift_release
+ _swift_release_n
+ _swift_retain
+ _swift_retain_n
+ _swift_slowAlloc
+ _swift_slowDealloc
+ _swift_task_alloc
+ _swift_task_create
+ _swift_task_dealloc
+ _swift_task_switch
+ _swift_unknownObjectRelease
+ _swift_unknownObjectRetain
+ _swift_weakDestroy
+ _swift_weakInit
+ _swift_weakLoadStrong
+ _swift_willThrow
- _OBJC_CLASS_$_NPTDLogger
- _OBJC_CLASS_$_NetworkPerformanceTesterDClient
- _OBJC_METACLASS_$_NPTDLogger
- _OBJC_METACLASS_$_NetworkPerformanceTesterDClient
- _dispatch_once
- _objc_release_x1
CStrings:
+ "Activated send client to %@"
+ "Activated send client to %@ with error %@"
+ "Error on remote object proxy: %s %s"
+ "Event Response from %@ contains error %@"
+ "Event sent to %@"
+ "Identifier received does not match remote device identifier for this object"
+ "NPTDRemoteClient received a request %s - this is not currently supported"
+ "NetworkPerformanceTesterDRemoteClient activated with error: %@"
+ "NetworkPerformanceTesterDRemoteClient disconnected from remote"
+ "NetworkPerformanceTesterDRemoteClient found device %@"
+ "NetworkPerformanceTesterDRemoteClient lost device %@"
+ "Rapport client Found device %@"
+ "Rapport client Lost device %@"
+ "Rapport client activated"
+ "Rapport client activated with error: %@"
+ "Rapport received event %s"
+ "Rapport received request %@"
+ "Received response error: %@"
+ "Received response from %@"
+ "Received response from %s"
+ "Response from %@ contains error %@"
+ "Sending request %s to %@, device count %ld"
+ "Will send event to %@, device count %ld, event %@"
+ "Will send request to %@, device count %ld"
+ "_TtC6NPTKit18NPTDRapportManager"
+ "_TtC6NPTKit31NetworkPerformanceTesterDClient"
+ "_TtC6NPTKit37NetworkPerformanceTesterDRemoteClient"
+ "_TtP6NPTKit12NPTDServices_"
+ "activateWithCompletion:"
+ "activeDevices"
+ "archivedDataWithRootObject:requiringSecureCoding:error:"
+ "classForCoder"
+ "com.apple.networkperformancetesterd.rapportWake"
+ "com.apple.nptkit"
+ "decodeInt32ForKey:"
+ "decodeInt64ForKey:"
+ "destinationDeviceDisconnected"
+ "destinationDeviceDiscoveredHandler"
+ "destinationDeviceLostHandler"
+ "deviceFoundHandler"
+ "deviceLostHandler"
+ "encodeInt32:forKey:"
+ "encodeInt64:forKey:"
+ "eventHandler"
+ "eventHandler dropping event %@"
+ "eventHandler dropping requestType %ld"
+ "eventHandler triggered in NPTDRemoteClient for event %@"
+ "eventHandler triggered in NPTDRemoteClient for sender event from %s"
+ "getPrivilegedFileHandleForPacketCaptureWithCompletionHandler:"
+ "idsDeviceIdentifier"
+ "initWithDictionary:"
+ "metadataCompletionHandler"
+ "metadataUpdateHandler"
+ "registerEventID:options:handler:"
+ "registerRequestID:options:handler:"
+ "remoteDevice"
+ "requestHandler"
+ "responseHandler"
+ "sendClients"
+ "sendEventID:event:options:completion:"
+ "sendRequestID:request:options:responseHandler:"
+ "setClasses:forSelector:argumentIndex:ofReply:"
+ "setControlFlags:"
+ "setDestinationDevice:"
+ "setDeviceChangedHandler:"
+ "setDeviceFoundHandler:"
+ "setDeviceLostHandler:"
+ "setDisconnectHandler:"
+ "setServiceType:"
+ "startLocalPerformanceTestWith:completionHandler:"
+ "startMetadataCollection(updateHandler:)"
+ "startPerformanceTest(with:updateHandler:)"
+ "stopLocalPerformanceTest:"
+ "stopMetadataCollection()"
+ "stopPerformanceTest()"
+ "testCompletionHandler"
+ "testUpdateHandler"
+ "v16@?0@\"RPCompanionLinkDevice\"8"
+ "v20@?0@\"RPCompanionLinkDevice\"8I16"
+ "v24@0:8@?<v@?@\"NSError\">16"
+ "v24@?0@\"NPTResults\"8@\"NSArray\"16"
+ "v24@?0@\"NSDictionary\"8@\"NSDictionary\"16"
+ "v32@0:8@\"NPTPerformanceTestConfiguration\"16@?<v@?@\"NPTResults\"@\"NSArray\">24"
+ "v32@?0@\"NSDictionary\"8@\"NSDictionary\"16@\"NSError\"24"
+ "v32@?0@\"NSDictionary\"8@\"NSDictionary\"16@?<v@?@\"NSDictionary\"@\"NSDictionary\"@\"NSError\">24"
- "\x02"
- "%@: %@ %@\n"
- "@\"<NPTDServices>\""
- "@\"NSXPCConnection\""
- "Error on remote object proxy"
- "Interrupted"
- "Invalidated"
- "NPTDLogger"
- "NPTDServices"
- "NetworkPerformanceTesterDClient"
- "daemon"
- "getPrivilegedFileHandleForPacketCapture:"
- "sharedInstance"

```
