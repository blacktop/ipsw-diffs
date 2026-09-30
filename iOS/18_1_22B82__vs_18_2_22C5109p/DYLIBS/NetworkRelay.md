## NetworkRelay

> `/System/Library/PrivateFrameworks/NetworkRelay.framework/NetworkRelay`

```diff

-563.40.6.0.0
-  __TEXT.__text: 0x5f0f0
-  __TEXT.__auth_stubs: 0xd20
-  __TEXT.__objc_methlist: 0x150c
+563.60.13.0.0
+  __TEXT.__text: 0x60a84
+  __TEXT.__auth_stubs: 0xd80
+  __TEXT.__objc_methlist: 0x156c
   __TEXT.__const: 0x1f0
-  __TEXT.__gcc_except_tab: 0x7ec
-  __TEXT.__cstring: 0xcffc
-  __TEXT.__oslogstring: 0x12cc
-  __TEXT.__unwind_info: 0x870
-  __TEXT.__objc_classname: 0x30b
-  __TEXT.__objc_methname: 0x3ea4
-  __TEXT.__objc_methtype: 0x733
-  __TEXT.__objc_stubs: 0x2560
-  __DATA_CONST.__got: 0x1f0
-  __DATA_CONST.__const: 0xd48
-  __DATA_CONST.__objc_classlist: 0xe8
+  __TEXT.__gcc_except_tab: 0x850
+  __TEXT.__cstring: 0xd47d
+  __TEXT.__oslogstring: 0x130a
+  __TEXT.__unwind_info: 0x8a8
+  __TEXT.__objc_classname: 0x323
+  __TEXT.__objc_methname: 0x3fad
+  __TEXT.__objc_methtype: 0x742
+  __TEXT.__objc_stubs: 0x25c0
+  __DATA_CONST.__got: 0x220
+  __DATA_CONST.__const: 0xd90
+  __DATA_CONST.__objc_classlist: 0xf0
   __DATA_CONST.__objc_protolist: 0x28
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0xc00
-  __DATA_CONST.__objc_superrefs: 0xe8
-  __DATA_CONST.__objc_arraydata: 0x168
-  __AUTH_CONST.__auth_got: 0x6a0
+  __DATA_CONST.__objc_selrefs: 0xc38
+  __DATA_CONST.__objc_superrefs: 0xf0
+  __DATA_CONST.__objc_arraydata: 0x170
+  __AUTH_CONST.__auth_got: 0x6d0
   __AUTH_CONST.__auth_ptr: 0x8
-  __AUTH_CONST.__const: 0x490
-  __AUTH_CONST.__cfstring: 0x4180
-  __AUTH_CONST.__objc_const: 0x4130
+  __AUTH_CONST.__const: 0x4f0
+  __AUTH_CONST.__cfstring: 0x4280
+  __AUTH_CONST.__objc_const: 0x42c8
   __AUTH_CONST.__objc_intobj: 0x228
   __AUTH_CONST.__objc_arrayobj: 0x90
   __AUTH_CONST.__objc_dictobj: 0x50
-  __AUTH.__objc_data: 0x870
-  __DATA.__objc_ivar: 0x430
-  __DATA.__data: 0x208
+  __AUTH.__objc_data: 0x8c0
+  __DATA.__objc_ivar: 0x450
+  __DATA.__data: 0x218
   __DATA.__crash_info: 0x40
-  __DATA.__bss: 0x1f8
+  __DATA.__bss: 0x238
   __DATA_DIRTY.__objc_data: 0xa0
-  __DATA_DIRTY.__bss: 0xa8
+  __DATA_DIRTY.__bss: 0xa0
   __DATA_DIRTY.__common: 0x2
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/Foundation.framework/Foundation
   - /System/Library/Frameworks/Network.framework/Network
+  - /System/Library/Frameworks/Security.framework/Security
   - /System/Library/Frameworks/SystemConfiguration.framework/SystemConfiguration
   - /System/Library/PrivateFrameworks/CoreWiFi.framework/CoreWiFi
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libnetwork.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 793
-  Symbols:   1194
-  CStrings:  2483
+  Functions: 810
+  Symbols:   1228
+  CStrings:  2533
 
Symbols:
+ _CFDictionaryGetTypeID
+ _CFGetTypeID
+ _OBJC_CLASS_$_NRIdentityProxyClient
+ _OBJC_CLASS_$_SecKeyProxy
+ _OBJC_METACLASS_$_NRIdentityProxyClient
+ _SecItemCopyMatching
+ _dispatch_group_async
+ _dispatch_group_wait
+ _dispatch_queue_attr_make_with_qos_class
+ _kCFBooleanTrue
+ _kNRIPCOptionPID
+ _kSecClass
+ _kSecClassIdentity
+ _kSecReturnRef
+ _kSecValuePersistentRef
+ _nrXPCEntitlementIdentityProxy
+ _nrXPCKeyIdentityProxyReferences
CStrings:
+ "%!"(MISSING)
+ "%!s(MISSING) called with null certificateReference"
+ "%!s(MISSING) called with null identityReference"
+ "%!s(MISSING)%!s(MISSING):%!d(MISSING) %!@(MISSING) SecItemCopyMatching for identity failed %!d(MISSING)"
+ "%!s(MISSING)%!s(MISSING):%!d(MISSING) %!@(MISSING) created new key proxy for %!@(MISSING)"
+ "%!s(MISSING)%!s(MISSING):%!d(MISSING) %!@(MISSING) dealloc"
+ "%!s(MISSING)%!s(MISSING):%!d(MISSING) %!@(MISSING) key proxy creation failed "
+ "%!s(MISSING)%!s(MISSING):%!d(MISSING) ABORTING: dispatch_queue_attr_make_with_qos_class(%!u(MISSING)) failed"
+ "%!s(MISSING)%!s(MISSING):%!d(MISSING) fetching identity references"
+ "%!s(MISSING)%!s(MISSING):%!d(MISSING) identity cache valid"
+ "%!s(MISSING)%!s(MISSING):%!d(MISSING) starting validation for pid %!@(MISSING)"
+ "%!s(MISSING)%!s(MISSING):%!d(MISSING) timed out waiting for identity proxy resolution"
+ "%!{(MISSING)public}s dispatch_queue_attr_make_with_qos_class(%!u(MISSING)) failed"
+ "-[NRIdentityProxyClient dealloc]"
+ "-[NRIdentityProxyClient fetchSecKeyProxyFromKeychainLocked]"
+ "-[NRIdentityProxyClient initInternal:options:]"
+ "-[NRIdentityProxyClient initWithCertificateReference:options:]"
+ "-[NRIdentityProxyClient initWithIdentityReference:options:]"
+ "-[NRIdentityProxyClient validateLocked]"
+ "@\"SecKeyProxy\""
+ "IdentityProxyReferences"
+ "NRIPCFetchReferencesLocked"
+ "NRIdentityProxyClient"
+ "NRIdentityProxyClient[%!l(MISSING)lu, %!@(MISSING)]"
+ "ResolveIdentityProxyMessage"
+ "_certificateData"
+ "_isCertificateReference"
+ "_isIdentityReference"
+ "_keyProxy"
+ "_options"
+ "_persistentReference"
+ "_references"
+ "cert"
+ "cert-ref"
+ "com.apple.networkrelay.identityProxy"
+ "com.apple.networkrelay.queue.identity-proxy-client"
+ "com.apple.networkrelay.referencesChanged"
+ "copyCertificateData"
+ "copySecKeyProxy"
+ "endpoint"
+ "id"
+ "id-ref"
+ "initWithCertificateReference:options:"
+ "initWithIdentity:"
+ "initWithIdentityReference:options:"
+ "isEqualToData:"
+ "nrXPCCopyIdentityReferences"
+ "nr_dispatch_queue_create_with_qos"
+ "pid"
+ "streaming-9001"

```
