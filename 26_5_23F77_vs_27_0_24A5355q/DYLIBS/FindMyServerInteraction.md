## FindMyServerInteraction

> `/System/Library/PrivateFrameworks/FindMyServerInteraction.framework/FindMyServerInteraction`

```diff

-84.35.2.23.2
-  __TEXT.__text: 0xb7c0
-  __TEXT.__auth_stubs: 0x8e0
-  __TEXT.__objc_methlist: 0x1f4
-  __TEXT.__const: 0x6d0
-  __TEXT.__swift5_typeref: 0x35c
-  __TEXT.__constg_swiftt: 0x318
-  __TEXT.__swift5_reflstr: 0x16e
-  __TEXT.__swift5_fieldmd: 0x2a8
+104.30.5.3.4
+  __TEXT.__text: 0x18d70
+  __TEXT.__objc_methlist: 0x274
+  __TEXT.__const: 0xb10
+  __TEXT.__constg_swiftt: 0x47c
+  __TEXT.__swift5_typeref: 0x48a
   __TEXT.__swift5_builtin: 0x28
-  __TEXT.__swift5_proto: 0x2c
-  __TEXT.__swift5_types: 0x30
+  __TEXT.__swift5_proto: 0x40
+  __TEXT.__swift5_types: 0x3c
+  __TEXT.__oslogstring: 0x7c5
+  __TEXT.__cstring: 0x2bd
+  __TEXT.__swift5_reflstr: 0x272
+  __TEXT.__swift5_fieldmd: 0x374
+  __TEXT.__swift5_capture: 0x278
+  __TEXT.__swift_as_entry: 0x54
+  __TEXT.__swift_as_ret: 0x60
+  __TEXT.__swift_as_cont: 0x98
   __TEXT.__swift5_protos: 0x18
-  __TEXT.__cstring: 0xe3
   __TEXT.__swift5_mpenum: 0x8
-  __TEXT.__swift5_capture: 0x64
-  __TEXT.__oslogstring: 0x8e
-  __TEXT.__swift_as_entry: 0x2c
-  __TEXT.__swift_as_ret: 0x30
-  __TEXT.__unwind_info: 0x390
-  __TEXT.__eh_frame: 0x728
-  __TEXT.__objc_classname: 0xca
-  __TEXT.__objc_methname: 0x744
-  __TEXT.__objc_methtype: 0x4ea
-  __TEXT.__objc_stubs: 0x280
-  __DATA_CONST.__got: 0x108
-  __DATA_CONST.__const: 0x40
-  __DATA_CONST.__objc_classlist: 0x10
+  __TEXT.__unwind_info: 0x598
+  __TEXT.__eh_frame: 0xdf8
+  __TEXT.__objc_stubs: 0x0
+  __TEXT.__auth_stubs: 0x0
+  __TEXT.__objc_classname: 0x0
+  __TEXT.__objc_methname: 0x0
+  __TEXT.__objc_methtype: 0x0
+  __DATA_CONST.__const: 0x90
+  __DATA_CONST.__objc_classlist: 0x28
   __DATA_CONST.__objc_protolist: 0x30
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x1c8
+  __DATA_CONST.__objc_selrefs: 0x278
   __DATA_CONST.__objc_protorefs: 0x18
-  __AUTH_CONST.__auth_got: 0x478
-  __AUTH_CONST.__const: 0x470
-  __AUTH_CONST.__objc_const: 0x330
-  __AUTH.__objc_data: 0x48
-  __AUTH.__data: 0x90
-  __DATA.__data: 0x1a0
-  __DATA.__bss: 0x380
-  __DATA_DIRTY.__objc_data: 0x88
-  __DATA_DIRTY.__data: 0x3a0
-  __DATA_DIRTY.__bss: 0x80
+  __DATA_CONST.__objc_superrefs: 0x8
+  __DATA_CONST.__got: 0x0
+  __AUTH_CONST.__const: 0xa30
+  __AUTH_CONST.__objc_const: 0x5a8
+  __AUTH_CONST.__auth_got: 0x740
+  __AUTH.__objc_data: 0xe8
+  __AUTH.__data: 0x1a8
+  __DATA.__objc_ivar: 0x4
+  __DATA.__data: 0x260
+  __DATA.__bss: 0x580
+  __DATA_DIRTY.__objc_data: 0xd0
+  __DATA_DIRTY.__data: 0x508
+  __DATA_DIRTY.__bss: 0x100
   __DATA_DIRTY.__common: 0x30
+  - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
+  - /System/Library/Frameworks/CoreTelephony.framework/CoreTelephony
   - /System/Library/Frameworks/Foundation.framework/Foundation
+  - /System/Library/Frameworks/Network.framework/Network
   - /System/Library/PrivateFrameworks/AuthKit.framework/AuthKit
   - /System/Library/PrivateFrameworks/FindMyBase.framework/FindMyBase
   - /System/Library/PrivateFrameworks/FindMyCommon.framework/FindMyCommon

   - /usr/lib/swift/libswift_Builtin_float.dylib
   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
-  UUID: DB77A3C4-1BCD-3338-A60C-B65645C2F94B
-  Functions: 252
-  Symbols:   261
-  CStrings:  119
+  UUID: BE1F8FA6-5FC1-363F-B2F9-C4159C506D21
+  Functions: 404
+  Symbols:   515
+  CStrings:  58
 
Symbols:
+ -[FMCoreTelephonyWrapper .cxx_destruct]
+ -[FMCoreTelephonyWrapper carrierBundleValueForKey:completionHandler:]
+ -[FMCoreTelephonyWrapper carrierBundleValueForKey:error:]
+ -[FMCoreTelephonyWrapper getBootstrapStatus:]
+ -[FMCoreTelephonyWrapper init]
+ -[FMCoreTelephonyWrapper preferredDataSubscriptionUUIDStringAndReturnError:]
+ -[FMCoreTelephonyWrapper preferredDataSubscriptionUUIDStringWithCompletionHandler:]
+ -[FMCoreTelephonyWrapper releaseBootstrapService:]
+ -[FMCoreTelephonyWrapper releaseBootstrapServiceWithCompletionHandler:]
+ -[FMCoreTelephonyWrapper requestBootstrapService:completion:]
+ _NSSelectorFromString
+ _OBJC_CLASS_$_CTBundle
+ _OBJC_CLASS_$_CoreTelephonyClient
+ _OBJC_CLASS_$_FMCoreTelephonyWrapper
+ _OBJC_CLASS_$_NSBundle
+ _OBJC_CLASS_$_NSNumber
+ _OBJC_CLASS_$_NSString
+ _OBJC_CLASS_$_OS_dispatch_queue
+ _OBJC_IVAR_$_FMCoreTelephonyWrapper._client
+ _OBJC_METACLASS_$_FMCoreTelephonyWrapper
+ __CTServerConnectionCreate
+ __CTServerConnectionOTAActivationAssertionCreate
+ __DATA__TtC23FindMyServerInteraction25BootstrapAssertionManager
+ __DATA__TtC23FindMyServerInteraction26NetworkReachabilityMonitor
+ __IVARS__TtC23FindMyServerInteraction25BootstrapAssertionManager
+ __IVARS__TtC23FindMyServerInteraction26NetworkReachabilityMonitor
+ __METACLASS_DATA__TtC23FindMyServerInteraction25BootstrapAssertionManager
+ __METACLASS_DATA__TtC23FindMyServerInteraction26NetworkReachabilityMonitor
+ __NSConcreteStackBlock
+ __OBJC_$_INSTANCE_METHODS_FMCoreTelephonyWrapper
+ __OBJC_$_INSTANCE_VARIABLES_FMCoreTelephonyWrapper
+ __OBJC_CLASS_RO_$_FMCoreTelephonyWrapper
+ __OBJC_METACLASS_RO_$_FMCoreTelephonyWrapper
+ __PROTOCOLS__TtC23FindMyServerInteractionP33_C6B3C350C31B0B220EF4B9CE0C9359C115SessionDelegate.23
+ ___69-[FMCoreTelephonyWrapper carrierBundleValueForKey:completionHandler:]_block_invoke
+ ___71-[FMCoreTelephonyWrapper releaseBootstrapServiceWithCompletionHandler:]_block_invoke
+ ___83-[FMCoreTelephonyWrapper preferredDataSubscriptionUUIDStringWithCompletionHandler:]_block_invoke
+ ___block_descriptor_48_e8_32s40bs_e5_v8?0ls32l8s40l8
+ ___block_descriptor_56_e8_32s40s48bs_e5_v8?0ls32l8s40l8s48l8
+ ___swift__destructor
+ ___swift__destructor.63
+ ___swift_allocate_boxed_opaque_existential_0
+ ___swift_async_cont_functlets
+ ___swift_closure_destructor
+ ___swift_closure_destructor.100
+ ___swift_closure_destructor.106
+ ___swift_closure_destructor.111
+ ___swift_closure_destructor.120
+ ___swift_closure_destructor.124
+ ___swift_closure_destructor.129
+ ___swift_closure_destructor.13
+ ___swift_closure_destructor.134
+ ___swift_closure_destructor.140
+ ___swift_closure_destructor.145
+ ___swift_closure_destructor.150
+ ___swift_closure_destructor.155
+ ___swift_closure_destructor.161
+ ___swift_closure_destructor.166
+ ___swift_closure_destructor.172
+ ___swift_closure_destructor.177
+ ___swift_closure_destructor.28
+ ___swift_closure_destructor.28Tm
+ ___swift_closure_destructor.32
+ ___swift_closure_destructor.36
+ ___swift_closure_destructor.40
+ ___swift_closure_destructor.66
+ ___swift_closure_destructor.66Tm
+ ___swift_closure_destructor.70
+ ___swift_closure_destructor.74
+ ___swift_closure_destructor.79
+ ___swift_closure_destructor.85
+ ___swift_closure_destructor.90
+ ___swift_closure_destructor.95
+ ___swift_destroy_boxed_opaque_existential_0Tm
+ ___swift_memcpy17_8
+ ___swift_project_boxed_opaque_existential_0
+ ___swift_project_boxed_opaque_existential_1Tm
+ __objc_autoreleasePoolPop
+ __objc_autoreleasePoolPush
+ _associated conformance 23FindMyServerInteraction14BootstrapErrorOSHAASQ
+ _block_copy_helper
+ _block_copy_helper.15
+ _block_copy_helper.52
+ _block_copy_helper.55
+ _block_descriptor
+ _block_descriptor.17
+ _block_descriptor.54
+ _block_descriptor.57
+ _block_destroy_helper
+ _block_destroy_helper.16
+ _block_destroy_helper.53
+ _block_destroy_helper.56
+ _dispatch_async
+ _dispatch_get_global_queue
+ _kCFAllocatorDefault
+ _objc_alloc
+ _objc_autoreleaseReturnValue
+ _objc_claimAutoreleasedReturnValue
+ _objc_msgSend$UUIDString
+ _objc_msgSend$bootstrapStatus
+ _objc_msgSend$bundleIdentifier
+ _objc_msgSend$carrierBundleValueForKey:completionHandler:
+ _objc_msgSend$carrierBundleValueForKey:error:
+ _objc_msgSend$copyCarrierBundleValue:key:bundleType:error:
+ _objc_msgSend$getBootstrapState:
+ _objc_msgSend$getBootstrapStatus:
+ _objc_msgSend$getPreferredDataSubscriptionContextSync:
+ _objc_msgSend$init
+ _objc_msgSend$initWithBundleType:
+ _objc_msgSend$initWithQueue:
+ _objc_msgSend$localizedDescription
+ _objc_msgSend$mainBundle
+ _objc_msgSend$performSelector:withObject:
+ _objc_msgSend$preferredDataSubscriptionUUIDStringAndReturnError:
+ _objc_msgSend$preferredDataSubscriptionUUIDStringWithCompletionHandler:
+ _objc_msgSend$releaseBootstrapService:
+ _objc_msgSend$releaseBootstrapServiceWithCompletionHandler:
+ _objc_msgSend$requestBootstrapService:completion:
+ _objc_msgSend$respondsToSelector:
+ _objc_msgSend$setTimeoutIntervalForRequest:
+ _objc_msgSend$setTimeoutIntervalForResource:
+ _objc_msgSend$setWaitsForConnectivity:
+ _objc_msgSend$uuid
+ _objc_release
+ _objc_retainAutorelease
+ _objc_retain_x2
+ _objc_retain_x27
+ _objc_retain_x28
+ _objc_storeStrong
+ _swift_allocBox
+ _swift_beginAccess
+ _swift_continuation_await
+ _swift_continuation_init
+ _swift_endAccess
+ _swift_getErrorValue
+ _swift_release_n
+ _swift_release_x19
+ _swift_release_x20
+ _swift_release_x21
+ _swift_release_x22
+ _swift_release_x23
+ _swift_release_x24
+ _swift_release_x25
+ _swift_release_x26
+ _swift_release_x27
+ _swift_release_x28
+ _swift_release_x8
+ _swift_release_x9
+ _swift_retain_n
+ _swift_retain_x19
+ _swift_retain_x2
+ _swift_retain_x20
+ _swift_retain_x21
+ _swift_retain_x24
+ _swift_retain_x27
+ _swift_retain_x28
+ _swift_unknownObjectRetain_n
+ _swift_updateClassMetadata2
+ _swift_weakDestroy
+ _swift_weakInit
+ _swift_weakLoadStrong
+ _symbolic SS6reason_t
+ _symbolic SSSg
+ _symbolic Say_____G So17OS_dispatch_queueC8DispatchE10AttributesV
+ _symbolic ScCySS______pG s5ErrorP
+ _symbolic ScCyyp______pG s5ErrorP
+ _symbolic ScCyyt______pG s5ErrorP
+ _symbolic Si
+ _symbolic So12NSURLSessionCSg
+ _symbolic _____ 23FindMyServerInteraction14BootstrapErrorO
+ _symbolic _____ 23FindMyServerInteraction25BootstrapAssertionManagerC
+ _symbolic _____ 23FindMyServerInteraction26NetworkReachabilityMonitorC
+ _symbolic _____ 7Network13NWPathMonitorC
+ _symbolic _____ 7Network6NWPathV
+ _symbolic _____3key_yp5valuet s11AnyHashableV
+ _symbolic _____4host______4portt 7Network10NWEndpointO4HostO AC4PortV
+ _symbolic _____Sg 10Foundation4DateV
+ _symbolic _____Sg 7Network10NWEndpointO4PortV
+ _symbolic _____Sg 7Network6NWPathV
+ _symbolic _____SgXw 23FindMyServerInteraction25BootstrapAssertionManagerC
+ _symbolic _____SgXw 23FindMyServerInteraction26NetworkReachabilityMonitorC
+ _symbolic _____SgXwz_Xx 23FindMyServerInteraction26NetworkReachabilityMonitorC
+ _symbolic ______p s5ErrorP
+ _symbolic _____y_____G s23_ContiguousArrayStorageC 7Network18ProxyConfigurationV
+ _symbolic _____y______pG s23_ContiguousArrayStorageC s7CVarArgP
+ _symbolic _____yyXlGSg s9UnmanagedV
+ _symbolic ytSg
+ _symbolic ytSgIeAgHr_
- __PROTOCOLS__TtC23FindMyServerInteractionP33_C6B3C350C31B0B220EF4B9CE0C9359C115SessionDelegate.20
- ___swift_destroy_boxed_opaque_existential_1Tm
- ___swift_memcpy9_8
- _objectdestroy.24Tm
- _swift_deletedAsyncMethodErrorTu
- _symbolic _____Sg 23FindMyServerInteraction12MockEndpointV
CStrings:
+ "Bootstrap available: %{bool}d"
+ "Bootstrap service released successfully"
+ "Bootstrap service requested successfully"
+ "BootstrapAssertionManager deallocated with active assertion - releasing"
+ "Configured bootstrap proxy: %s:%ld, tls=%{bool}d"
+ "Creating OTA assertion for bootstrap"
+ "Error.tooManyAuthKitRetries"
+ "Extracted UUID successfully"
+ "Failed to create CT server connection"
+ "Failed to create OTA assertion"
+ "Failed to get preferred data subscription UUID: %s"
+ "Failed to get proxy host: %s"
+ "Failed to get proxy port: %s"
+ "Got carrier bundle proxy host: %s"
+ "Got carrier bundle proxy port: %@"
+ "Invalid proxy port: "
+ "Invalid proxy port: %ld"
+ "No OTA assertion to release"
+ "No carrier bundle proxy found, using fallback Apple proxy"
+ "No current network path available"
+ "No proxy settings available"
+ "No proxy settings for bootstrap connection after fallback"
+ "OTA assertion already enabled"
+ "OTA assertion created successfully"
+ "OTAActivationProxyHost"
+ "OTAActivationProxyPort"
+ "Releasing OTA assertion (lifetime: %ss)"
+ "Retry #%ld because AKAppleIDSession told us to retry"
+ "Set secondary identifier on config"
+ "URLSessionConfiguration does not respond to set_CTDataConnectionServiceType:"
+ "URLSessionConfiguration does not respond to set_CTDataConnectionServiceType: - API may have changed"
+ "URLSessionConfiguration does not respond to set_sourceApplicationSecondaryIdentifier: - API may have changed"
+ "WiFi reachability check: satisfied=%{bool}d, usesWiFi=%{bool}d"
+ "_createCheckedThrowingContinuation(_:)"
+ "com.apple.findmy.networkmonitor"
+ "getBootstrapStatus failed: %s"
+ "kCTDataConnectionServiceTypeOTAActivation"
+ "network_selected=Bootstrap (fallback), wifi_reachable=NO, endpoint=%{public}s"
+ "network_selected=WiFi (no connectivity), wifi_reachable=NO, bootstrap not allowed for endpoint, endpoint=%{public}s"
+ "network_selected=WiFi, wifi_reachable=YES, endpoint=%{public}s"
+ "releaseBootstrapService failed: %s"
+ "requestBootstrapService failed: %s"
+ "set_CTDataConnectionServiceType:"
+ "set_sourceApplicationSecondaryIdentifier:"
+ "sq-device-proxy.apple.com"
+ "v8@?0"
- "#16@0:8"
- "$defaultActor"
- ".cxx_destruct"
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
- "NSObject"
- "NSURLSessionDelegate"
- "NSURLSessionTaskDelegate"
- "Q16@0:8"
- "T#,R"
- "T@\"NSString\",?,R,C"
- "T@\"NSString\",R,C"
- "TQ,R"
- "URLSession:didBecomeInvalidWithError:"
- "URLSession:didCreateTask:"
- "URLSession:didReceiveChallenge:completionHandler:"
- "URLSession:task:didCompleteWithError:"
- "URLSession:task:didFinishCollectingMetrics:"
- "URLSession:task:didReceiveChallenge:completionHandler:"
- "URLSession:task:didReceiveInformationalResponse:"
- "URLSession:task:didSendBodyData:totalBytesSent:totalBytesExpectedToSend:"
- "URLSession:task:needNewBodyStream:"
- "URLSession:task:needNewBodyStreamFromOffset:completionHandler:"
- "URLSession:task:willBeginDelayedRequest:completionHandler:"
- "URLSession:task:willPerformHTTPRedirection:newRequest:completionHandler:"
- "URLSession:taskIsWaitingForConnectivity:"
- "URLSessionDidFinishEventsForBackgroundURLSession:"
- "Vv16@0:8"
- "^{_NSZone=}16@0:8"
- "_TtC23FindMyServerInteraction27ServerInteractionController"
- "_TtC23FindMyServerInteractionP33_C6B3C350C31B0B220EF4B9CE0C9359C115SessionDelegate"
- "allHeaderFields"
- "appleIDHeadersForRequest:"
- "authKitSession"
- "authenticationMethod"
- "autorelease"
- "class"
- "conformsToProtocol:"
- "credential"
- "currentDevice"
- "dealloc"
- "debugDescription"
- "description"
- "ephemeralSessionConfiguration"
- "handleResponse:forRequest:shouldRetry:"
- "hash"
- "host"
- "init"
- "initWithIdentifier:"
- "initWithUser:password:persistence:"
- "isEqual:"
- "isKindOfClass:"
- "isMemberOfClass:"
- "isProxy"
- "performSelector:"
- "performSelector:withObject:"
- "performSelector:withObject:withObject:"
- "pinningCredential"
- "protectionSpace"
- "release"
- "respondsToSelector:"
- "retain"
- "retainCount"
- "self"
- "serverFriendlyDescription"
- "serverTrust"
- "session"
- "sessionWithConfiguration:"
- "setHTTPCookieAcceptPolicy:"
- "setHTTPCookieStorage:"
- "setRequestCachePolicy:"
- "setURLCache:"
- "setURLCredentialStorage:"
- "statusCode"
- "superclass"
- "v16@0:8"
- "v24@0:8@\"NSURLSession\"16"
- "v24@0:8@16"
- "v32@0:8@\"NSURLSession\"16@\"NSError\"24"
- "v32@0:8@\"NSURLSession\"16@\"NSURLSessionTask\"24"
- "v32@0:8@16@24"
- "v40@0:8@\"NSURLSession\"16@\"NSURLAuthenticationChallenge\"24@?<v@?q@\"NSURLCredential\">32"
- "v40@0:8@\"NSURLSession\"16@\"NSURLSessionTask\"24@\"NSError\"32"
- "v40@0:8@\"NSURLSession\"16@\"NSURLSessionTask\"24@\"NSHTTPURLResponse\"32"
- "v40@0:8@\"NSURLSession\"16@\"NSURLSessionTask\"24@\"NSURLSessionTaskMetrics\"32"
- "v40@0:8@\"NSURLSession\"16@\"NSURLSessionTask\"24@?<v@?@\"NSInputStream\">32"
- "v40@0:8@16@24@32"
- "v40@0:8@16@24@?32"
- "v48@0:8@\"NSURLSession\"16@\"NSURLSessionTask\"24@\"NSURLAuthenticationChallenge\"32@?<v@?q@\"NSURLCredential\">40"
- "v48@0:8@\"NSURLSession\"16@\"NSURLSessionTask\"24@\"NSURLRequest\"32@?<v@?q@\"NSURLRequest\">40"
- "v48@0:8@\"NSURLSession\"16@\"NSURLSessionTask\"24q32@?<v@?@\"NSInputStream\">40"
- "v48@0:8@16@24@32@?40"
- "v48@0:8@16@24q32@?40"
- "v56@0:8@\"NSURLSession\"16@\"NSURLSessionTask\"24@\"NSHTTPURLResponse\"32@\"NSURLRequest\"40@?<v@?@\"NSURLRequest\">48"
- "v56@0:8@\"NSURLSession\"16@\"NSURLSessionTask\"24q32q40q48"
- "v56@0:8@16@24@32@40@?48"
- "v56@0:8@16@24q32q40q48"
- "valueForHTTPHeaderField:"
- "zone"

```
