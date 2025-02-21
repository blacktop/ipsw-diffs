## BoardServices

> `/System/Library/PrivateFrameworks/BoardServices.framework/BoardServices`

```diff

-694.3.4.0.0
-  __TEXT.__text: 0x47a58
-  __TEXT.__auth_stubs: 0xaa0
-  __TEXT.__objc_methlist: 0x11b4
+694.5.5.0.0
+  __TEXT.__text: 0x49cd8
+  __TEXT.__auth_stubs: 0xac0
+  __TEXT.__objc_methlist: 0x1a04
   __TEXT.__const: 0xd8
-  __TEXT.__gcc_except_tab: 0x8ae4
-  __TEXT.__cstring: 0x55ab
-  __TEXT.__oslogstring: 0x1fb9
+  __TEXT.__gcc_except_tab: 0x8f68
+  __TEXT.__cstring: 0x5903
+  __TEXT.__oslogstring: 0x2005
   __TEXT.__dlopen_cstrs: 0x2ca
-  __TEXT.__unwind_info: 0x1700
-  __TEXT.__objc_classname: 0x786
-  __TEXT.__objc_methname: 0x3af7
+  __TEXT.__unwind_info: 0x1748
+  __TEXT.__objc_classname: 0x79a
+  __TEXT.__objc_methname: 0x3c15
   __TEXT.__objc_methtype: 0x12f5
-  __TEXT.__objc_stubs: 0x2300
+  __TEXT.__objc_stubs: 0x2340
   __DATA_CONST.__got: 0x338
-  __DATA_CONST.__const: 0xff8
+  __DATA_CONST.__const: 0x1000
   __DATA_CONST.__objc_classlist: 0x118
   __DATA_CONST.__objc_catlist: 0x10
   __DATA_CONST.__objc_protolist: 0x110
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0xe48
+  __DATA_CONST.__objc_selrefs: 0xf58
   __DATA_CONST.__objc_protorefs: 0x48
   __DATA_CONST.__objc_superrefs: 0xe0
   __DATA_CONST.__objc_arraydata: 0x20
-  __AUTH_CONST.__auth_got: 0x560
+  __AUTH_CONST.__auth_got: 0x570
   __AUTH_CONST.__const: 0x3c0
-  __AUTH_CONST.__cfstring: 0x4280
-  __AUTH_CONST.__objc_const: 0x5690
+  __AUTH_CONST.__cfstring: 0x4500
+  __AUTH_CONST.__objc_const: 0x4888
   __AUTH_CONST.__objc_arrayobj: 0x18
   __AUTH.__objc_data: 0x50
-  __DATA.__objc_ivar: 0x3e4
+  __DATA.__objc_ivar: 0x3e8
   __DATA.__data: 0xcc0
   __DATA.__bss: 0x8
   __DATA.__common: 0x10

   - /System/Library/PrivateFrameworks/SoftLinking.framework/SoftLinking
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 712
-  Symbols:   1038
-  CStrings:  1729
+  Functions: 719
+  Symbols:   1050
+  CStrings:  1760
 
Symbols:
+ _os_unfair_lock_assert_not_owner
+ _xpc_connection_bs_seal_listener
+ _xpc_connection_copy_bundle_id
- _xpc_endpoint_create
CStrings:
+ "\x02\x11%\x12"
+ "ViewService backstop"
+ "ViewService domain cannot be activated via this call"
+ "[_bs_assert_object isKindOfClass:BSServiceDomainClass]"
+ "_UIViewServiceConfiguration"
+ "_configurationFromPlist:isViewService:postfixBlock:"
+ "_endpointForDomain:service:instance:"
+ "_lock_registerDomain:"
+ "_lock_viewServiceConfiguration"
+ "_underlyingServerPeer can only be called on a server peer : context = %@"
+ "_underlyingServerPeerConnection"
+ "_xpcConnection"
+ "activateViewServiceConfiguration"
+ "asked for endpoint before sealing the listener configuration"
+ "asked for non-launching status before sealing the listener configuration"
+ "bs_fetchBundleIdentifierFromXPCConnection"
+ "cannot process domain %@ with unknown start type %@"
+ "connection and lastKnownConnection must be the same for server peers"
+ "could not find underlying xpcConnection"
+ "could not resolve class _UIViewServiceConfiguration"
+ "domainsDictionary"
+ "extended automatic bootstrap complete"
+ "forViewServicesOnly"
+ "initializing automatic domain %@"
+ "initializing view-service domain %@"
+ "invalid viewServiceConfiguration returned for %@"
+ "lastKnownConnection must be the same as the parent's lastKnownConnection for child server peers"
+ "manual bootstrap activation"
+ "manual session activation"
+ "manual session reactivation"
+ "manually activating session for domain %@"
+ "must be configured before resume"
+ "only manual session domains can deactivate"
+ "registerViewServiceConfiguration"
+ "server peer is somehow missing its underlying connection"
+ "view-serv"
+ "view-service config cannot contain XPCService domains : %@"
+ "view-service domains must specify Start to be ViewService : %@"
+ "viewServiceConfiguration"
+ "viewServiceConfigurationRegisteringIfNecessary:"
+ "viewServiceDomains"
- "\x01\x11%\x12"
- "_configurationFromPlist:postfixBlock:"
- "_dynamicConfigWithPlist:"
- "_lock_ensureEndpoint"
- "activateSuspended"
- "activation endpoint is not equivalent to previous sealing endpoint : new=%@ old=%@"
- "activation endpoint is not the same bs_type as the previous sealing endpoint : new=%{bool}i old=%{bool}i"
- "failed to retrieve an endpoint from listener=%@"
- "initializing session for domain %@"
- "manual activation"
- "must be activated before resume"

```
