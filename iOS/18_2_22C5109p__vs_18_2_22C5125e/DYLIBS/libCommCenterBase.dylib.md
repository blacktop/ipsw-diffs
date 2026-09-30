## libCommCenterBase.dylib

> `/System/Library/Frameworks/CoreTelephony.framework/Support/libCommCenterBase.dylib`

```diff

-12209.3.0.0.0
-  __TEXT.__text: 0xbb854
-  __TEXT.__auth_stubs: 0x1730
+12212.4.0.0.0
+  __TEXT.__text: 0xba760
+  __TEXT.__auth_stubs: 0x1720
   __TEXT.__init_offsets: 0x30
   __TEXT.__objc_methlist: 0xf8
-  __TEXT.__const: 0xdf6e
-  __TEXT.__gcc_except_tab: 0x10c38
-  __TEXT.__cstring: 0x11dd7
-  __TEXT.__oslogstring: 0x229b
-  __TEXT.__unwind_info: 0x48e8
+  __TEXT.__const: 0xdd8e
+  __TEXT.__gcc_except_tab: 0x10bb8
+  __TEXT.__cstring: 0x11ee6
+  __TEXT.__oslogstring: 0x1fec
+  __TEXT.__unwind_info: 0x4850
   __TEXT.__objc_classname: 0x2b
   __TEXT.__objc_methname: 0x3bc
   __TEXT.__objc_methtype: 0x354

   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_selrefs: 0x140
   __DATA_CONST.__objc_superrefs: 0x8
-  __AUTH_CONST.__auth_got: 0xba8
+  __AUTH_CONST.__auth_got: 0xba0
   __AUTH_CONST.__auth_ptr: 0x8
-  __AUTH_CONST.__const: 0x13520
+  __AUTH_CONST.__const: 0x13418
   __AUTH_CONST.__cfstring: 0x2b40
   __AUTH_CONST.__objc_const: 0x200
   __DATA.__objc_ivar: 0x8

   - /usr/lib/libTelephonyUtilDynamic.dylib
   - /usr/lib/libc++.1.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 5409
-  Symbols:   7793
-  CStrings:  4134
+  Functions: 5391
+  Symbols:   7774
+  CStrings:  4138
 
Symbols:
+ __Z15read_rest_valueR15t_imsi_identityRKN3xpc6objectE
+ __Z16write_rest_valueRK15t_imsi_identity
+ __Z25getSingleSlotForEmergencyRKNSt3__16vectorI18EmergencySetupTypeNS_9allocatorIS1_EEEE
+ __Z8asStringRK15t_imsi_identity
+ __ZN27DNSResolverFactoryInterfaceD0Ev
+ __ZN27DNSResolverFactoryInterfaceD1Ev
+ __ZN27DNSResolverFactoryInterfaceD2Ev
+ __ZN27DNSResolverServiceInterfaceD0Ev
+ __ZN27DNSResolverServiceInterfaceD1Ev
+ __ZN27DNSResolverServiceInterfaceD2Ev
+ __ZN4rest8asStringERKNS_24ManagedConfigurationInfoE
+ __ZTI27DNSResolverFactoryInterface
+ __ZTI27DNSResolverServiceInterface
+ __ZTS27DNSResolverFactoryInterface
+ __ZTS27DNSResolverServiceInterface
+ __ZTV27DNSResolverFactoryInterface
+ __ZTV27DNSResolverServiceInterface
+ __ZeqRK15t_imsi_identityS1_
+ __ZneRK15t_imsi_identityS1_
- __ZN11DNSResolver12startResolveERKNSt3__112basic_stringIcNS0_11char_traitsIcEENS0_9allocatorIcEEEENS0_8functionIFvRKNS0_6vectorIS6_NS4_IS6_EEEEEEEmS8_j
- __ZN11DNSResolver15tryResolve_syncEv
- __ZN11DNSResolver19disposeService_syncEv
- __ZN11DNSResolver19getAddrInfoCallbackEP16_DNSServiceRef_tjiPKcPK8sockaddr
- __ZN11DNSResolver7resolveERKNSt3__110shared_ptrIK8RegistryEERKNS0_12basic_stringIcNS0_11char_traitsIcEENS0_9allocatorIcEEEENS0_8functionIFvRKNS0_6vectorISC_NSA_ISC_EEEEEEEN8dispatch5queueEmSE_j
- __ZN11DNSResolverC1ERKNSt3__110shared_ptrIK8RegistryEENS1_I26DNSServiceWrapperInterfaceEERKN8dispatch5queueE
- __ZN11DNSResolverC2ERKNSt3__110shared_ptrIK8RegistryEENS1_I26DNSServiceWrapperInterfaceEERKN8dispatch5queueE
- __ZN11DNSResolverD0Ev
- __ZN11DNSResolverD1Ev
- __ZN11DNSResolverD2Ev
- __ZTI11DNSResolver
- __ZTS11DNSResolver
- __ZTV11DNSResolver
- _if_nametoindex
CStrings:
+ " '"
+ " fBlockedBundleIds:["
+ " fIsESimModificationAllowed:"
+ " fIsESimOutgoingTransferAllowed:"
+ " fIsRCSMessagingAllowed:"
+ " fIsSatelliteConnectionAllowed:"
+ " fIsSupervised:"
+ "'"
+ "),"
+ ", home:"
+ "], fManagedBundleIds:["
+ "], fManagedSliceBundleIds:["
+ "]}"
+ "curr_imsi"
+ "home_imsi"
+ "home_mcc"
+ "home_mnc"
+ "isSatelliteConnectionAllowed"
+ "{ imsi curr:"
- "#D Resolver callback for name %!s(MISSING), flags: 0x%!x(MISSING)"
- "#I DNS resolution of %!s(MISSING) is already ongoing"
- "#I No Callback provided for name %!s(MISSING), cannot do DNS resolve."
- "#I Resolved address for name %!s(MISSING): %!s(MISSING)"
- "#I a dns resolving of %!s(MISSING) is already ongoing, cannot resolve %!s(MISSING) the meantime."
- "#I dns resolving of %!s(MISSING) is already ongoing."
- "#I start resolving domain name %!s(MISSING) over interface %!s(MISSING) (%!u(MISSING)), attempt #%!l(MISSING)u"
- "#N Failed to resolve name %!s(MISSING) with error %!d(MISSING)."
- "#N Resolving IPv4 for name %!s(MISSING) timed out."
- "#N Resolving IPv6 for name %!s(MISSING) timed out."
- "#N cannot resolve empty domain name."
- "DNSResolverRetryTimer"
- "Failed to assign dispatch queue for name resolution of %!s(MISSING), error: %!d(MISSING)"
- "Failed to start name resolution for %!s(MISSING) over interface %!s(MISSING) (%!u(MISSING)) with error: %!d(MISSING)"
- "dns.resolver"

```
