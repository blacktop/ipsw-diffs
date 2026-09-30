## libCommCenterBase.dylib

> `/System/Library/Frameworks/CoreTelephony.framework/Support/libCommCenterBase.dylib`

```diff

-12109.5.0.0.0
-  __TEXT.__text: 0xbae84
-  __TEXT.__auth_stubs: 0x1760
+12209.3.0.0.0
+  __TEXT.__text: 0xbb854
+  __TEXT.__auth_stubs: 0x1730
   __TEXT.__init_offsets: 0x30
   __TEXT.__objc_methlist: 0xf8
-  __TEXT.__const: 0xdf3e
-  __TEXT.__gcc_except_tab: 0x10b1c
-  __TEXT.__cstring: 0x11d49
-  __TEXT.__oslogstring: 0x2190
-  __TEXT.__unwind_info: 0x48c8
+  __TEXT.__const: 0xdf6e
+  __TEXT.__gcc_except_tab: 0x10c38
+  __TEXT.__cstring: 0x11dd7
+  __TEXT.__oslogstring: 0x229b
+  __TEXT.__unwind_info: 0x48e8
   __TEXT.__objc_classname: 0x2b
   __TEXT.__objc_methname: 0x3bc
   __TEXT.__objc_methtype: 0x354
   __TEXT.__objc_stubs: 0x360
-  __DATA_CONST.__got: 0x248
-  __DATA_CONST.__const: 0x6e58
+  __DATA_CONST.__got: 0x1f8
+  __DATA_CONST.__const: 0x6e60
   __DATA_CONST.__objc_classlist: 0x8
   __DATA_CONST.__objc_catlist: 0x20
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_selrefs: 0x140
   __DATA_CONST.__objc_superrefs: 0x8
-  __AUTH_CONST.__auth_got: 0xbc0
+  __AUTH_CONST.__auth_got: 0xba8
   __AUTH_CONST.__auth_ptr: 0x8
-  __AUTH_CONST.__const: 0x13440
+  __AUTH_CONST.__const: 0x13520
   __AUTH_CONST.__cfstring: 0x2b40
   __AUTH_CONST.__objc_const: 0x200
   __DATA.__objc_ivar: 0x8
-  __DATA.__data: 0x78
+  __DATA.__data: 0x80
   __DATA.__bss: 0x5
   __DATA_DIRTY.__objc_data: 0x50
   __DATA_DIRTY.__data: 0x18

   - /usr/lib/libTelephonyUtilDynamic.dylib
   - /usr/lib/libc++.1.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 5401
-  Symbols:   7794
-  CStrings:  4127
+  Functions: 5409
+  Symbols:   7793
+  CStrings:  4134
 
Symbols:
+ _DNSServiceGetAddrInfo
+ _DNSServiceRefDeallocate
+ _DNSServiceSetDispatchQueue
+ __Z15read_rest_valueR12CallKitEventRKN3xpc6objectE
+ __Z16write_rest_valueRK12CallKitEvent
+ __ZN11DNSResolver12startResolveERKNSt3__112basic_stringIcNS0_11char_traitsIcEENS0_9allocatorIcEEEENS0_8functionIFvRKNS0_6vectorIS6_NS4_IS6_EEEEEEEmS8_j
+ __ZN11DNSResolver19disposeService_syncEv
+ __ZN11DNSResolver19getAddrInfoCallbackEP16_DNSServiceRef_tjiPKcPK8sockaddr
+ __ZN11DNSResolver7resolveERKNSt3__110shared_ptrIK8RegistryEERKNS0_12basic_stringIcNS0_11char_traitsIcEENS0_9allocatorIcEEEENS0_8functionIFvRKNS0_6vectorISC_NSA_ISC_EEEEEEEN8dispatch5queueEmSE_j
+ __ZN11DNSResolverC1ERKNSt3__110shared_ptrIK8RegistryEENS1_I26DNSServiceWrapperInterfaceEERKN8dispatch5queueE
+ __ZN11DNSResolverC2ERKNSt3__110shared_ptrIK8RegistryEENS1_I26DNSServiceWrapperInterfaceEERKN8dispatch5queueE
+ __ZN17DNSServiceWrapper14disposeServiceEv
+ __ZN17DNSServiceWrapper21dnsServiceGetAddrInfoEjjjPKcPFvP16_DNSServiceRef_tjjiS1_PK8sockaddrjPvES7_
+ __ZN17DNSServiceWrapper26dnsServiceSetDispatchQueueEP16dispatch_queue_s
+ __ZN17DNSServiceWrapperD0Ev
+ __ZN17DNSServiceWrapperD1Ev
+ __ZN17DNSServiceWrapperD2Ev
+ __ZN26DNSServiceWrapperInterfaceD0Ev
+ __ZN26DNSServiceWrapperInterfaceD1Ev
+ __ZN26DNSServiceWrapperInterfaceD2Ev
+ __ZNK3xpc6object9to_stringEv
+ __ZNSt3__112basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEE5eraseEmm
+ __ZNSt3__113basic_istreamIcNS_11char_traitsIcEEErsERj
+ __ZTI17DNSServiceWrapper
+ __ZTI26DNSServiceWrapperInterface
+ __ZTS17DNSServiceWrapper
+ __ZTS26DNSServiceWrapperInterface
+ __ZTV17DNSServiceWrapper
+ __ZTV26DNSServiceWrapperInterface
+ __os_log_debug_impl
+ _if_nametoindex
+ _kDataActivateFailureSatelliteSystemKey
- _CFHostCreateWithName
- _CFHostGetAddressing
- _CFHostScheduleWithRunLoop
- _CFHostSetClient
- _CFHostStartInfoResolution
- _CFHostUnscheduleFromRunLoop
- _CFRunLoopGetMain
- __CFHostStartInfoResolutionForInterface
- __ZN11DNSResolver12hostCallbackEPK13CFStreamError
- __ZN11DNSResolver12startResolveERKNSt3__112basic_stringIcNS0_11char_traitsIcEENS0_9allocatorIcEEEENS0_8functionIFvRKNS0_6vectorIS6_NS4_IS6_EEEEEEEmS8_
- __ZN11DNSResolver16disposeHost_syncEv
- __ZN11DNSResolver19hostCallbackWrapperEP8__CFHost14CFHostInfoTypePK13CFStreamErrorPv
- __ZN11DNSResolver7resolveERKNSt3__110shared_ptrIK8RegistryEERKNS0_12basic_stringIcNS0_11char_traitsIcEENS0_9allocatorIcEEEENS0_8functionIFvRKNS0_6vectorISC_NSA_ISC_EEEEEEEN8dispatch5queueEmSE_
- __ZN11DNSResolverC1ERKNSt3__110shared_ptrIK8RegistryEERKN8dispatch5queueE
- __ZN11DNSResolverC2ERKNSt3__110shared_ptrIK8RegistryEERKN8dispatch5queueE
- __ZNSt3__113basic_istreamIcNS_11char_traitsIcEEErsERt
- __ZTVN10__cxxabiv119__pointer_type_infoE
- __ZTVN10__cxxabiv120__function_type_infoE
- ___TUAssertTrigger
- _getnameinfo
- _kCFHostAddressesString
- _kCFRunLoopCommonModes
- _kCFStreamErrorDomainFTP
- _kCFStreamErrorDomainHTTP
- _kCFStreamErrorDomainMach
- _kCFStreamErrorDomainNetDB
- _kCFStreamErrorDomainNetServices
- _kCFStreamErrorDomainSOCKS
- _kCFStreamErrorDomainSSL
- _kCFStreamErrorDomainSystemConfiguration
CStrings:
+ "#D DisplayStatus [isOn=%!s(MISSING), isLocked=%!s(MISSING), isCoversheetActive=%!s(MISSING), isPasscodeSet=%!s(MISSING)]"
+ "#D Getting main bundle"
+ "#D Input(%!s(MISSING)) = %!f(MISSING)"
+ "#D Personality Info: %!s(MISSING) - %!s(MISSING)"
+ "#D Resolver callback for name %!s(MISSING), flags: 0x%!x(MISSING)"
+ "#D Sending OTASP success dialogue to UI"
+ "#D ThumperID: %!s(MISSING), info: %!p(MISSING)"
+ "#D [conn %!p(MISSING)] Connection closed."
+ "#D [conn %!p(MISSING)] Got REST message: %!s(MISSING)"
+ "#I DNS resolution of %!s(MISSING) is already ongoing"
+ "#I Resolved address for name %!s(MISSING): %!s(MISSING)"
+ "#I start resolving domain name %!s(MISSING) over interface %!s(MISSING) (%!u(MISSING)), attempt #%!l(MISSING)u"
+ "#N Failed to resolve name %!s(MISSING) with error %!d(MISSING)."
+ "#N Resolving IPv4 for name %!s(MISSING) timed out."
+ "#N Resolving IPv6 for name %!s(MISSING) timed out."
+ "/Library/Caches/com.apple.xbs/Sources/CoreTelephony/CSI/Source/Common/SmsPduEncoder.cpp"
+ "/Library/Caches/com.apple.xbs/Sources/CoreTelephony/CommCenter/CommCenterCommandDrivers/Sim/SubscriberDefinitions.cpp"
+ "Assertion failure: ( %!s(MISSING) ), in file %!s(MISSING), line: %!d(MISSING)"
+ "Failed to assign dispatch queue for name resolution of %!s(MISSING), error: %!d(MISSING)"
+ "Failed to start name resolution for %!s(MISSING) over interface %!s(MISSING) (%!u(MISSING)) with error: %!d(MISSING)"
+ "callKitUdp:"
+ "ended"
+ "green tea"
+ "kCTRegistrationDataIndicatorStatus5G_CA"
+ "kDataActivateFailureSatelliteSystemKey"
+ "not active"
+ "starting"
+ "video"
- "#I          %!s(MISSING)"
- "#I Failed to create CFHost for %!s(MISSING)"
- "#I Failed to set host client for %!s(MISSING)"
- "#I Failed to start name reselution for %!s(MISSING) over interface %!s(MISSING) with error %!s(MISSING):%!d(MISSING)"
- "#I Failed to start name reselution for %!s(MISSING), attempt #%!l(MISSING)u"
- "#I Resolved %!d(MISSING) addresses for name %!s(MISSING):"
- "#I a dns resolving of %!s(MISSING) is already on going"
- "#I start resolving domain name %!s(MISSING)"
- "#I start resolving domain name %!s(MISSING) over interface %!s(MISSING), attempt #%!l(MISSING)u"
- "#N Failed to resolve name %!s(MISSING) with error %!s(MISSING)(%!d(MISSING):%!d(MISSING))."
- "#N got callback with nullptr fHost"
- "Unknown Domain"
- "kCFStreamErrorDomainFTP"
- "kCFStreamErrorDomainHTTP"
- "kCFStreamErrorDomainMach"
- "kCFStreamErrorDomainNetDB"
- "kCFStreamErrorDomainNetServices"
- "kCFStreamErrorDomainSOCKS"
- "kCFStreamErrorDomainSSL"
- "kCFStreamErrorDomainSystemConfiguration"
- "kUnkown"

```
