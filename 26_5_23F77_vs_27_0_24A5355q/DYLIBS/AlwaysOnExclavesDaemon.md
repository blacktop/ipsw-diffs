## AlwaysOnExclavesDaemon

> `/System/Library/PrivateFrameworks/AlwaysOnExclavesDaemon.framework/AlwaysOnExclavesDaemon`

```diff

-40.100.10.0.0
-  __TEXT.__text: 0x4558
-  __TEXT.__auth_stubs: 0x790
+60.0.0.0.1
+  __TEXT.__text: 0x8534
   __TEXT.__objc_methlist: 0x104
-  __TEXT.__const: 0x212
-  __TEXT.__oslogstring: 0x3fc
-  __TEXT.__constg_swiftt: 0x214
-  __TEXT.__swift5_typeref: 0xc8
-  __TEXT.__swift5_reflstr: 0xc2
-  __TEXT.__swift5_fieldmd: 0x128
-  __TEXT.__cstring: 0x1c9
+  __TEXT.__const: 0x4f0
+  __TEXT.__oslogstring: 0x4df
+  __TEXT.__constg_swiftt: 0x36c
+  __TEXT.__swift5_typeref: 0x10e
+  __TEXT.__swift5_reflstr: 0x152
+  __TEXT.__swift5_fieldmd: 0x220
+  __TEXT.__cstring: 0x757
   __TEXT.__swift5_builtin: 0x14
-  __TEXT.__swift5_types: 0x14
-  __TEXT.__swift5_proto: 0x4
+  __TEXT.__swift5_types: 0x28
+  __TEXT.__swift5_proto: 0x1c
   __TEXT.__swift5_capture: 0x14
-  __TEXT.__unwind_info: 0x170
-  __TEXT.__eh_frame: 0x80
-  __TEXT.__objc_classname: 0xb1
-  __TEXT.__objc_methname: 0x213
-  __TEXT.__objc_methtype: 0xf5
-  __DATA_CONST.__got: 0xc0
-  __DATA_CONST.__const: 0x40
-  __DATA_CONST.__objc_classlist: 0x18
+  __TEXT.__unwind_info: 0x1e8
+  __TEXT.__eh_frame: 0xc8
+  __TEXT.__objc_stubs: 0x0
+  __TEXT.__auth_stubs: 0x0
+  __TEXT.__objc_classname: 0x0
+  __TEXT.__objc_methname: 0x0
+  __TEXT.__objc_methtype: 0x0
+  __DATA_CONST.__const: 0x50
+  __DATA_CONST.__objc_classlist: 0x30
   __DATA_CONST.__objc_protolist: 0x20
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0xa0
+  __DATA_CONST.__objc_selrefs: 0x110
   __DATA_CONST.__objc_protorefs: 0x10
-  __AUTH_CONST.__auth_got: 0x3c8
-  __AUTH_CONST.__const: 0x1d0
-  __AUTH_CONST.__objc_const: 0x390
+  __DATA_CONST.__got: 0x0
+  __AUTH_CONST.__const: 0x2c8
+  __AUTH_CONST.__objc_const: 0x5e0
+  __AUTH_CONST.__auth_got: 0x540
   __AUTH.__objc_data: 0xf0
-  __AUTH.__data: 0x318
-  __DATA.__data: 0x190
-  __DATA.__common: 0x28
-  __DATA.__bss: 0x80
+  __AUTH.__data: 0x238
+  __DATA.__data: 0x1c0
+  __DATA.__common: 0x10
+  __DATA.__bss: 0x300
+  __DATA_DIRTY.__objc_data: 0xf0
+  __DATA_DIRTY.__data: 0x3f0
+  __DATA_DIRTY.__common: 0x10
+  __DATA_DIRTY.__bss: 0x80
+  - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/Foundation.framework/Foundation
   - /System/Library/PrivateFrameworks/AlwaysOnExclavesServices.framework/AlwaysOnExclavesServices
+  - /System/Library/PrivateFrameworks/FeatureFlags.framework/FeatureFlags
   - /System/Library/PrivateFrameworks/Tightbeam.framework/Tightbeam
+  - /System/Library/PrivateFrameworks/TrustedClockingServices.framework/TrustedClockingServices
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
   - /usr/lib/swift/libswiftCore.dylib

   - /usr/lib/swift/libswiftXPC.dylib
   - /usr/lib/swift/libswift_Builtin_float.dylib
   - /usr/lib/swift/libswiftos.dylib
-  UUID: C6977329-6B58-3F6D-922E-79CFFBA1F23F
-  Functions: 87
-  Symbols:   179
-  CStrings:  92
+  UUID: 988A2A34-221F-3D09-A025-167CC8D12D6F
+  Functions: 152
+  Symbols:   246
+  CStrings:  70
 
Symbols:
+ _OBJC_CLASS_$_NSLock
+ _OBJC_CLASS_$_NSString
+ _OBJC_CLASS_$_NSUserDefaults
+ _OBJC_CLASS_$_TrustedClockingManager
+ __DATA__TtC22AlwaysOnExclavesDaemon13EnableTracker
+ __DATA__TtC22AlwaysOnExclavesDaemon16WorkerThreadPool
+ __DATA__TtC22AlwaysOnExclavesDaemon24CrossConclaveIpcReceiver
+ __IVARS__TtC22AlwaysOnExclavesDaemon13EnableTracker
+ __IVARS__TtC22AlwaysOnExclavesDaemon16WorkerThreadPool
+ __IVARS__TtC22AlwaysOnExclavesDaemon24CrossConclaveIpcReceiver
+ __METACLASS_DATA__TtC22AlwaysOnExclavesDaemon13EnableTracker
+ __METACLASS_DATA__TtC22AlwaysOnExclavesDaemon16WorkerThreadPool
+ __METACLASS_DATA__TtC22AlwaysOnExclavesDaemon24CrossConclaveIpcReceiver
+ ___swift_closure_destructor
+ ___swift_destroy_boxed_opaque_existential_0Tm
+ ___swift_destroy_boxed_opaque_existential_1
+ ___swift_memcpy0_1
+ ___swift_memcpy1_1
+ _associated conformance 22AlwaysOnExclavesDaemon0abC0OSHAASQ
+ _associated conformance 22AlwaysOnExclavesDaemon29CrossConclaveIpcReceiverErrorOSHAASQ
+ _block_copy_helper.26
+ _block_descriptor.28
+ _block_destroy_helper.27
+ _exclaves_c2cc_recv_loop
+ _exclaves_conclave_enable_c2cc_recv
+ _objc_allocWithZone
+ _objc_msgSend
+ _objc_msgSend$boolForKey:
+ _objc_msgSend$dictionaryRepresentation
+ _objc_msgSend$init
+ _objc_msgSend$initWithBytes:length:encoding:
+ _objc_msgSend$initialize:
+ _objc_msgSend$integerForKey:
+ _objc_msgSend$lock
+ _objc_msgSend$removeObjectForKey:
+ _objc_msgSend$setBool:forKey:
+ _objc_msgSend$setInteger:forKey:
+ _objc_msgSend$setObject:forKey:
+ _objc_msgSend$sharedInstance
+ _objc_msgSend$stringForKey:
+ _objc_msgSend$unlock
+ _objc_release_x21
+ _objc_release_x22
+ _objc_release_x23
+ _objc_release_x24
+ _objc_release_x26
+ _objc_release_x27
+ _pthread_attr_setdetachstate
+ _swift_allocError
+ _swift_bridgeObjectRetain_n
+ _swift_once
+ _swift_release_x19
+ _swift_release_x20
+ _swift_release_x21
+ _swift_release_x22
+ _swift_release_x26
+ _swift_release_x8
+ _swift_retain_x12
+ _swift_retain_x19
+ _swift_retain_x2
+ _swift_retain_x20
+ _swift_retain_x22
+ _swift_retain_x23
+ _swift_retain_x26
+ _swift_retain_x8
+ _swift_willThrow
+ _symbolic SSSg
+ _symbolic Sb
+ _symbolic So14NSUserDefaultsC
+ _symbolic _____ 22AlwaysOnExclavesDaemon0abC0O
+ _symbolic _____ 22AlwaysOnExclavesDaemon13EnableTrackerC
+ _symbolic _____ 22AlwaysOnExclavesDaemon16WorkerThreadPoolC
+ _symbolic _____ 22AlwaysOnExclavesDaemon24CrossConclaveIpcReceiverC
+ _symbolic _____ 22AlwaysOnExclavesDaemon29CrossConclaveIpcReceiverErrorO
+ _symbolic _____Sg 10Foundation6LocaleV
- _block_copy_helper.15
- _block_copy_helper.18
- _block_descriptor.17
- _block_descriptor.20
- _block_destroy_helper.16
- _block_destroy_helper.19
- _exclaves_lookup_service
- _swift_retain
- _symbolic Say_____G 8Dispatch0A13WorkItemFlagsV
- _symbolic Si
- _sysctlbyname
CStrings:
+ " has previously enabled AOE but enable count is zero"
+ "%s created %d IPC receiver threads"
+ "%s is feature-flag disabled, refusing to start conclave"
+ "%s: no conclave present, cannot setup IPC receiver"
+ "%s: xpcService: bootuuid is %s"
+ "%s: xpcService: new boot detected, old bootuuid was %s, resetting to clean defaults"
+ "): exclaves_aoe_enumerate_and_setup_services failed"
+ "): exclaves_aoe_enumerate_and_setup_services succeeded but returned zero services"
+ "): exclaves_aoe_get_all_service_infos failed"
+ "): failed pthread_setname_np for CrossConclaveIpcReceiver thread"
+ "): failed pthread_setname_np for message thread"
+ "): failed pthread_setname_np for worker thread"
+ "): failed to create pthread"
+ "): failed to create thread attribute"
+ "): failed to enable CrossConclaveIpcReceiver"
+ "): failed to mark thread as detached"
+ "): failed to set thread QoS"
+ "): failed to set thread attribute"
+ "): failed to set thread stacksize"
+ ", could not launch conclave for "
+ ": failed to parse conclave name"
+ ": xpcService: failed to parse bootuuid"
+ ": xpcService: sysctl kern.bootsessionuuid failed, size "
+ "AlwaysOnExclavesDaemon/crossConclaveIpcReceiver.swift"
+ "AlwaysOnExclavesDaemon/workerThreadPool.swift"
+ "Failed to initialize TrustedClockingServices"
+ "Foundation/arm64e-apple-ios.private.swiftinterface"
+ "[Forwarder] Service lookup failed for service %s with kr = %d"
+ "[XPCService] %s requested overdisablement of %s"
+ "[XPCService] %s requested overenablement of %s"
+ "[XPCService] %s successfully requested disablement of %s"
+ "[XPCService] %s successfully requested enablement of %s"
+ "[XPCService] AlwaysOnExclaves is not available, please enable the alwaysonexclavesd feature flag"
+ "[warn] daemon %s has no conclave"
+ "_aoe_enabled_by__"
+ "_message_thread_for_service_"
+ "_worker_thread_for_service_"
+ "alwaysonexclavesd"
+ "com.apple.alwaysonexclavesd"
+ "conclave for %s is not present, daemon.start() skipped"
+ "error: invalid EndpointSchedulingCategory "
+ "exclaves_c2cc_recv_loop unexpectedly returned"
+ "hasConclave"
+ "inited %s"
+ "input of String.init(cString:encoding:) must be null-terminated"
+ "kern.bootsessionuuid"
+ "lifecycle"
+ "started %s"
- "#16@0:8"
- "(error %d): exclaves_aoe_enumerate_and_setup_services failed"
- "(error %d): exclaves_aoe_enumerate_and_setup_services succeeded but returned zero services"
- "(error %d): exclaves_aoe_get_all_service_infos failed"
- "(error: %d): failed to create pthread"
- "(error: %d): failed to create thread attribute"
- "(error: %d): failed to set thread attribute"
- "(error: %d): failed to set thread stacksize"
- "@\"NSString\"16@0:8"
- "@16@0:8"
- "@24@0:8:16"
- "@32@0:8:16@24"
- "@40@0:8:16@24@32"
- "B16@0:8"
- "B24@0:8#16"
- "B24@0:8:16"
- "B24@0:8@\"Protocol\"16"
- "B24@0:8@16"
- "Failed to retrieve task conclave name"
- "NSObject"
- "OS_xpc_object"
- "Q16@0:8"
- "T#,R"
- "T@\"NSString\",?,R,C"
- "T@\"NSString\",R,C"
- "TQ,R"
- "Vv16@0:8"
- "[Forwarder] Service lookup failed"
- "[xpcService] AlwaysOnExclaves disabled by %s"
- "[xpcService] AlwaysOnExclaves enabled by %s"
- "^{_NSZone=}16@0:8"
- "_TtC22AlwaysOnExclavesDaemon18AlwaysOnXPCService"
- "_TtC22AlwaysOnExclavesDaemon25AlwaysOnExclavesForwarder"
- "_TtC22AlwaysOnExclavesDaemon6Daemon"
- "aoe_message_thread_for_service_"
- "aoe_worker_thread_for_service_"
- "autorelease"
- "class"
- "clientConnections"
- "conformsToProtocol:"
- "debugDescription"
- "description"
- "enabledCount"
- "error: invalid EndpointSchedulingCategory %llu"
- "exec_name"
- "exiting"
- "forwarder"
- "forwardingConnections"
- "hash"
- "isEqual:"
- "isKindOfClass:"
- "isMemberOfClass:"
- "isProxy"
- "label"
- "listener"
- "logger"
- "performSelector:"
- "performSelector:withObject:"
- "performSelector:withObject:withObject:"
- "release"
- "respondsToSelector:"
- "retain"
- "retainCount"
- "self"
- "superclass"
- "v16@?0@\"<OS_xpc_object>\"8"
- "v8@?0"
- "xpcConnectionQueue"
- "xpcService"
- "zone"

```
