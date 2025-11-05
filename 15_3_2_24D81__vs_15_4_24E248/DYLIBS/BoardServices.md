## BoardServices

> `/System/Library/PrivateFrameworks/BoardServices.framework/Versions/A/BoardServices`

```diff

-694.3.4.0.0
-  __TEXT.__text: 0x4f0a4
-  __TEXT.__auth_stubs: 0x8d0
-  __TEXT.__objc_methlist: 0x11b4
+694.5.5.0.0
+  __TEXT.__text: 0x51750
+  __TEXT.__auth_stubs: 0x8f0
+  __TEXT.__objc_methlist: 0x1a04
   __TEXT.__const: 0xe0
-  __TEXT.__gcc_except_tab: 0x8b94
-  __TEXT.__cstring: 0x55e1
-  __TEXT.__oslogstring: 0x1fb9
+  __TEXT.__gcc_except_tab: 0x903c
+  __TEXT.__cstring: 0x5939
+  __TEXT.__oslogstring: 0x2005
   __TEXT.__dlopen_cstrs: 0x2ca
-  __TEXT.__unwind_info: 0x1760
-  __TEXT.__objc_classname: 0x786
-  __TEXT.__objc_methname: 0x3af7
+  __TEXT.__unwind_info: 0x17c0
+  __TEXT.__objc_classname: 0x79a
+  __TEXT.__objc_methname: 0x3c15
   __TEXT.__objc_methtype: 0x12f5
-  __TEXT.__objc_stubs: 0x2300
+  __TEXT.__objc_stubs: 0x2340
   __DATA_CONST.__got: 0x338
-  __DATA_CONST.__const: 0x378
+  __DATA_CONST.__const: 0x380
   __DATA_CONST.__objc_classlist: 0x118
   __DATA_CONST.__objc_catlist: 0x10
   __DATA_CONST.__objc_protolist: 0x110
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0xe48
+  __DATA_CONST.__objc_selrefs: 0xf58
   __DATA_CONST.__objc_protorefs: 0x48
   __DATA_CONST.__objc_superrefs: 0xe0
   __DATA_CONST.__objc_arraydata: 0x20
-  __AUTH_CONST.__auth_got: 0x478
+  __AUTH_CONST.__auth_got: 0x488
   __AUTH_CONST.__const: 0x1260
-  __AUTH_CONST.__cfstring: 0x4280
-  __AUTH_CONST.__objc_const: 0x5690
+  __AUTH_CONST.__cfstring: 0x4500
+  __AUTH_CONST.__objc_const: 0x4888
   __AUTH_CONST.__objc_arrayobj: 0x18
   __AUTH.__objc_data: 0x190
-  __DATA.__objc_ivar: 0x3e4
+  __DATA.__objc_ivar: 0x3e8
   __DATA.__data: 0xcc0
   __DATA.__bss: 0x50
   __DATA.__common: 0x50

   - /System/Library/PrivateFrameworks/SoftLinking.framework/Versions/A/SoftLinking
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 859D3BCA-4A5C-3A3E-A698-65A540D84A1A
-  Functions: 756
-  Symbols:   2512
-  CStrings:  2240
+  UUID: 3A8007A6-248E-375F-BFB9-734AB048A881
+  Functions: 765
+  Symbols:   2541
+  CStrings:  2291
 
Symbols:
+ +[BSServicesConfiguration _configurationFromPlist:isViewService:postfixBlock:]
+ +[BSServicesConfiguration _viewServiceConfigWithDomainsDictionary:]
+ +[BSServicesConfiguration activateViewServiceConfiguration]
+ +[BSServicesConfiguration registerViewServiceConfiguration]
+ +[BSServicesConfiguration viewServiceConfiguration]
+ -[BSNSXPCTransport _underlyingServerPeerConnection]
+ -[BSServiceManager _lock_registerDomain:]
+ -[BSServiceManager activateViewServiceConfiguration]
+ -[BSServiceManager viewServiceConfigurationRegisteringIfNecessary:]
+ -[BSXPCServiceConnection _underlyingServerPeerConnection]
+ -[NSXPCConnection(forViewServicesOnly) bs_fetchBundleIdentifierFromXPCConnection]
+ GCC_except_table57
+ GCC_except_table61
+ GCC_except_table66
+ GCC_except_table68
+ GCC_except_table72
+ GCC_except_table75
+ GCC_except_table80
+ GCC_except_table82
+ OBJC_IVAR_$_BSServiceManager._lock_viewServiceConfiguration
+ __36-[BSServiceManager debugDescription]_block_invoke.68
+ __36-[BSServiceManager debugDescription]_block_invoke.70
+ __36-[BSServiceManager debugDescription]_block_invoke.77
+ __36-[BSServiceManager debugDescription]_block_invoke_2.69
+ __36-[BSServiceManager debugDescription]_block_invoke_2.71
+ __36-[BSServiceManager debugDescription]_block_invoke_2.84
+ __42-[BSServiceDomain _initWithSpecification:]_block_invoke.106
+ __42-[BSServiceDomain _initWithSpecification:]_block_invoke.116
+ __42-[BSServiceDomain _initWithSpecification:]_block_invoke.126
+ __42-[BSServiceDomain _initWithSpecification:]_block_invoke_2.110
+ __54-[BSServiceManager extendAutomaticBootstrapCompletion]_block_invoke.106
+ __55-[BSXPCServiceConnection _lock_activateNowOrWhenReady:]_block_invoke.178
+ __55-[BSXPCServiceConnection _lock_activateNowOrWhenReady:]_block_invoke.185
+ __55-[BSXPCServiceConnection _lock_activateNowOrWhenReady:]_block_invoke.196
+ __55-[BSXPCServiceConnection _lock_activateNowOrWhenReady:]_block_invoke.200
+ __55-[BSXPCServiceConnection _lock_activateNowOrWhenReady:]_block_invoke.202
+ __78+[BSServicesConfiguration _configurationFromPlist:isViewService:postfixBlock:]_block_invoke.103
+ __78+[BSServicesConfiguration _configurationFromPlist:isViewService:postfixBlock:]_block_invoke.14
+ __78+[BSServicesConfiguration _configurationFromPlist:isViewService:postfixBlock:]_block_invoke.83
+ __96-[BSServiceManager _lock_rootConnectionWithEndpoint:oneshot:nonLaunching:targetPID:description:]_block_invoke.217
+ __96-[BSServiceManager _lock_rootConnectionWithEndpoint:oneshot:nonLaunching:targetPID:description:]_block_invoke.223
+ __96-[BSServiceManager _lock_rootConnectionWithEndpoint:oneshot:nonLaunching:targetPID:description:]_block_invoke_2.218
+ __96-[BSServiceManager _lock_rootConnectionWithEndpoint:oneshot:nonLaunching:targetPID:description:]_block_invoke_2.227
+ __OBJC_$_INSTANCE_METHODS_NSXPCConnection(BSServiceConnection|forViewServicesOnly)
+ __OBJC_$_PROP_LIST_NSXPCConnection_$_BSServiceConnection
+ __OBJC_CATEGORY_PROTOCOLS_$_NSXPCConnection_$_BSServiceConnection
+ ___28-[BSServiceDomain _activate]_block_invoke_2
+ ___36-[BSServiceManager debugDescription]_block_invoke_3
+ ___44-[BSXPCServiceConnectionListener configure:]_block_invoke
+ ___78+[BSServicesConfiguration _configurationFromPlist:isViewService:postfixBlock:]_block_invoke
+ ___KeyForIndex_block_invoke
+ ____handleEvent_block_invoke.216
+ ___block_descriptor_64_ea8_32s40s48s56s_e42_v32?0"NSString"8"BSServiceDomain"16^B24l
+ ___block_descriptor_72_ea8_32s40s48s56s64s_e5_v8?0l
+ ___block_descriptor_73_ea8_32s40s48bs_e39_v32?0"NSString"8"NSDictionary"16^B24l
+ ___copy_helper_block_ea8_32s40s48s56s64s
+ ___destroy_helper_block_ea8_32s40s48s56s64s
+ __block_literal_global.108
+ __block_literal_global.115
+ __block_literal_global.139
+ __block_literal_global.177
+ __block_literal_global.180
+ __block_literal_global.187
+ __block_literal_global.189
+ __block_literal_global.204
+ __block_literal_global.216
+ __block_literal_global.237
+ __block_literal_global.80
+ _objc_msgSend$_xpcConnection
+ _objc_msgSend$domainsDictionary
+ _os_unfair_lock_assert_not_owner
+ _xpc_connection_bs_seal_listener
+ _xpc_connection_copy_bundle_id
- +[BSServicesConfiguration _configurationFromPlist:postfixBlock:]
- -[BSXPCServiceConnectionListener _lock_ensureEndpoint]
- -[BSXPCServiceConnectionListener activateSuspended]
- GCC_except_table58
- GCC_except_table63
- GCC_except_table67
- GCC_except_table71
- GCC_except_table73
- GCC_except_table78
- GCC_except_table81
- __28-[BSServiceDomain _activate]_block_invoke.167
- __36-[BSServiceManager debugDescription]_block_invoke.65
- __36-[BSServiceManager debugDescription]_block_invoke.67
- __36-[BSServiceManager debugDescription]_block_invoke.76
- __36-[BSServiceManager debugDescription]_block_invoke_2.66
- __36-[BSServiceManager debugDescription]_block_invoke_2.73
- __36-[BSServiceManager debugDescription]_block_invoke_2.83
- __42-[BSServiceDomain _initWithSpecification:]_block_invoke.105
- __42-[BSServiceDomain _initWithSpecification:]_block_invoke.115
- __42-[BSServiceDomain _initWithSpecification:]_block_invoke.125
- __42-[BSServiceDomain _initWithSpecification:]_block_invoke_2.109
- __54-[BSServiceManager extendAutomaticBootstrapCompletion]_block_invoke.105
- __55-[BSXPCServiceConnection _lock_activateNowOrWhenReady:]_block_invoke.167
- __55-[BSXPCServiceConnection _lock_activateNowOrWhenReady:]_block_invoke.171
- __55-[BSXPCServiceConnection _lock_activateNowOrWhenReady:]_block_invoke.174
- __55-[BSXPCServiceConnection _lock_activateNowOrWhenReady:]_block_invoke.182
- __55-[BSXPCServiceConnection _lock_activateNowOrWhenReady:]_block_invoke.186
- __64+[BSServicesConfiguration _configurationFromPlist:postfixBlock:]_block_invoke.118
- __64+[BSServicesConfiguration _configurationFromPlist:postfixBlock:]_block_invoke.33
- __64+[BSServicesConfiguration _configurationFromPlist:postfixBlock:]_block_invoke.98
- __96-[BSServiceManager _lock_rootConnectionWithEndpoint:oneshot:nonLaunching:targetPID:description:]_block_invoke.189
- __96-[BSServiceManager _lock_rootConnectionWithEndpoint:oneshot:nonLaunching:targetPID:description:]_block_invoke.195
- __96-[BSServiceManager _lock_rootConnectionWithEndpoint:oneshot:nonLaunching:targetPID:description:]_block_invoke_2.190
- __96-[BSServiceManager _lock_rootConnectionWithEndpoint:oneshot:nonLaunching:targetPID:description:]_block_invoke_2.199
- __OBJC_$_CATEGORY_INSTANCE_METHODS_NSXPCConnection_$_BSServiceConnection
- ___51-[BSXPCServiceConnectionListener activateSuspended]_block_invoke
- ___64+[BSServicesConfiguration _configurationFromPlist:postfixBlock:]_block_invoke
- ____handleEvent_block_invoke.219
- ___block_descriptor_56_ea8_32s40s48s_e42_v32?0"NSString"8"BSServiceDomain"16^B24l
- ___block_descriptor_64_ea8_32s40s48s56s_e5_v8?0l
- ___block_descriptor_72_ea8_32s40s48bs_e39_v32?0"NSString"8"NSDictionary"16^B24l
- __block_literal_global.107
- __block_literal_global.118
- __block_literal_global.136
- __block_literal_global.161
- __block_literal_global.172
- __block_literal_global.175
- __block_literal_global.188
- __block_literal_global.190
- __block_literal_global.198
- __block_literal_global.79
- _xpc_endpoint_create
CStrings:
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
