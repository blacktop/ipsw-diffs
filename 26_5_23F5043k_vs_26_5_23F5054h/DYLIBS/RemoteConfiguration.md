## RemoteConfiguration

> `/System/Library/PrivateFrameworks/RemoteConfiguration.framework/RemoteConfiguration`

```diff

-371.0.0.0.0
-  __TEXT.__text: 0x2e238
+400.0.0.0.0
+  __TEXT.__text: 0x2e9e8
   __TEXT.__auth_stubs: 0x970
-  __TEXT.__objc_methlist: 0x2f1c
-  __TEXT.__const: 0x1f2
-  __TEXT.__cstring: 0x49a3
+  __TEXT.__objc_methlist: 0x2f7c
+  __TEXT.__const: 0x200
   __TEXT.__gcc_except_tab: 0x4f4
-  __TEXT.__oslogstring: 0x1cd3
+  __TEXT.__oslogstring: 0x1d1d
+  __TEXT.__cstring: 0x4b23
   __TEXT.__swift5_typeref: 0x180
   __TEXT.__swift5_capture: 0x20
   __TEXT.__swift_as_entry: 0xc
   __TEXT.__swift_as_ret: 0xc
-  __TEXT.__unwind_info: 0xe78
+  __TEXT.__unwind_info: 0xe80
   __TEXT.__eh_frame: 0x138
-  __TEXT.__objc_classname: 0x565
-  __TEXT.__objc_methname: 0x834e
+  __TEXT.__objc_classname: 0x566
+  __TEXT.__objc_methname: 0x83c7
   __TEXT.__objc_methtype: 0x1465
-  __TEXT.__objc_stubs: 0x4fe0
+  __TEXT.__objc_stubs: 0x5060
   __DATA_CONST.__got: 0x318
-  __DATA_CONST.__const: 0xfc0
+  __DATA_CONST.__const: 0xff0
   __DATA_CONST.__objc_classlist: 0x148
   __DATA_CONST.__objc_catlist: 0x88
   __DATA_CONST.__objc_protolist: 0x90
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x1b00
+  __DATA_CONST.__objc_selrefs: 0x1b18
   __DATA_CONST.__objc_protorefs: 0x10
   __DATA_CONST.__objc_superrefs: 0x118
   __AUTH_CONST.__auth_got: 0x4c8
   __AUTH_CONST.__const: 0x3d0
-  __AUTH_CONST.__cfstring: 0x2120
-  __AUTH_CONST.__objc_const: 0x5718
+  __AUTH_CONST.__cfstring: 0x2280
+  __AUTH_CONST.__objc_const: 0x5798
   __AUTH_CONST.__objc_intobj: 0x18
   __AUTH.__objc_data: 0x550
-  __DATA.__objc_ivar: 0x3c0
+  __DATA.__objc_ivar: 0x3c8
   __DATA.__data: 0x708
   __DATA.__bss: 0x60
   __DATA_DIRTY.__objc_data: 0x780

   - /usr/lib/swift/libswiftXPC.dylib
   - /usr/lib/swift/libswift_Builtin_float.dylib
   - /usr/lib/swift/libswift_Concurrency.dylib
-  UUID: F1952F3E-1B8A-34CE-83F5-667E67ABBF0F
-  Functions: 1384
-  Symbols:   4558
-  CStrings:  2336
+  UUID: 319C65EF-EC1F-37CE-9860-606D03D5D357
+  Functions: 1393
+  Symbols:   4576
+  CStrings:  2364
 
Symbols:
+ +[RCDebugOverrides supportsSecureCoding]
+ -[RCConfigurationResource debugOverrides]
+ -[RCConfigurationResource setDebugOverrides:]
+ -[RCDebugOverrides encodeWithCoder:]
+ -[RCDebugOverrides hasSameFetchParametersAs:]
+ -[RCDebugOverrides initWithCoder:]
+ -[RCFallbackOperation debugOverrides]
+ -[RCFallbackOperation setDebugOverrides:]
+ _OBJC_IVAR_$_RCConfigurationResource._debugOverrides
+ _OBJC_IVAR_$_RCFallbackOperation._debugOverrides
+ _RCConfigurationResourceDebugOverridesKey
+ __OBJC_$_CATEGORY_NSURLSessionTask_$_RCAdditions
+ __OBJC_$_CLASS_PROP_LIST_RCDebugOverrides
+ __OBJC_$_INSTANCE_METHODS_NSURLSessionTask(RCAdditions|RCOperationIdentifyingSupport|RCOperationPrioritizingSupport)
+ __OBJC_CLASS_PROTOCOLS_$_NSURLSessionTask(RCAdditions|RCOperationIdentifyingSupport|RCOperationPrioritizingSupport)
+ ___110-[RCConfigurationManager fetchMultiConfigurationWithSettings:networkActivityBlock:completionQueue:completion:]_block_invoke.123
+ ___110-[RCConfigurationManager fetchMultiConfigurationWithSettings:networkActivityBlock:completionQueue:completion:]_block_invoke.124
+ ___110-[RCConfigurationManager fetchMultiConfigurationWithSettings:networkActivityBlock:completionQueue:completion:]_block_invoke.126
+ ___110-[RCConfigurationManager fetchMultiConfigurationWithSettings:networkActivityBlock:completionQueue:completion:]_block_invoke.127
+ ___110-[RCConfigurationManager fetchMultiConfigurationWithSettings:networkActivityBlock:completionQueue:completion:]_block_invoke.128
+ ___110-[RCConfigurationManager fetchMultiConfigurationWithSettings:networkActivityBlock:completionQueue:completion:]_block_invoke.134
+ ___110-[RCConfigurationManager fetchMultiConfigurationWithSettings:networkActivityBlock:completionQueue:completion:]_block_invoke.99
+ ___110-[RCConfigurationManager fetchMultiConfigurationWithSettings:networkActivityBlock:completionQueue:completion:]_block_invoke_2.103
+ ___110-[RCConfigurationManager fetchMultiConfigurationWithSettings:networkActivityBlock:completionQueue:completion:]_block_invoke_2.125
+ ___110-[RCConfigurationManager fetchMultiConfigurationWithSettings:networkActivityBlock:completionQueue:completion:]_block_invoke_2.133
+ ___110-[RCConfigurationManager fetchMultiConfigurationWithSettings:networkActivityBlock:completionQueue:completion:]_block_invoke_2.133.cold.1
+ ___110-[RCConfigurationManager fetchMultiConfigurationWithSettings:networkActivityBlock:completionQueue:completion:]_block_invoke_2.135
+ ___130-[RCConfigurationManager _fetchMultiConfigurationFromEndpointURL:settings:networkActivityBlock:changeTagsByRequestKey:completion:]_block_invoke.158
+ ___84-[RCConfigurationManager _fetchConfigurationFromFallbackURLWithSettings:completion:]_block_invoke.161
+ ___84-[RCConfigurationManager _fetchConfigurationFromFallbackURLWithSettings:completion:]_block_invoke.165
+ ___84-[RCConfigurationManager _fetchConfigurationFromFallbackURLWithSettings:completion:]_block_invoke.168
+ ___84-[RCConfigurationManager _fetchConfigurationFromFallbackURLWithSettings:completion:]_block_invoke_2.166
+ ___84-[RCConfigurationManager _fetchConfigurationFromFallbackURLWithSettings:completion:]_block_invoke_2.166.cold.1
+ ___84-[RCConfigurationManager _fetchConfigurationFromFallbackURLWithSettings:completion:]_block_invoke_2.170
+ ___98-[RCConfigurationManager _isAllowedToReachEndpointWithSettings:configurationResource:endpointURL:]_block_invoke.153
+ ___98-[RCConfigurationManager _isAllowedToReachEndpointWithSettings:configurationResource:endpointURL:]_block_invoke.156
+ ___block_literal_global.106
+ ___block_literal_global.109
+ ___block_literal_global.112
+ ___block_literal_global.114
+ ___block_literal_global.119
+ ___block_literal_global.122
+ ___block_literal_global.131
+ ___block_literal_global.163
+ ___block_literal_global.98
+ _objc_msgSend$decodeBoolForKey:
+ _objc_msgSend$encodeBool:forKey:
+ _objc_msgSend$hasSameFetchParametersAs:
+ _objc_msgSend$setDebugOverrides:
- -[RCConfigurationManager _endpointURLForEnvironment:requestKey:].cold.1
- __OBJC_$_CATEGORY_NSURLSessionTask_$_RCOperationPrioritizingSupport
- __OBJC_$_INSTANCE_METHODS_NSURLSessionTask(RCOperationPrioritizingSupport|RCOperationIdentifyingSupport|RCAdditions)
- __OBJC_CLASS_PROTOCOLS_$_NSURLSessionTask(RCOperationPrioritizingSupport|RCOperationIdentifyingSupport|RCAdditions)
- ___110-[RCConfigurationManager fetchMultiConfigurationWithSettings:networkActivityBlock:completionQueue:completion:]_block_invoke.108
- ___110-[RCConfigurationManager fetchMultiConfigurationWithSettings:networkActivityBlock:completionQueue:completion:]_block_invoke.109
- ___110-[RCConfigurationManager fetchMultiConfigurationWithSettings:networkActivityBlock:completionQueue:completion:]_block_invoke.111
- ___110-[RCConfigurationManager fetchMultiConfigurationWithSettings:networkActivityBlock:completionQueue:completion:]_block_invoke.112
- ___110-[RCConfigurationManager fetchMultiConfigurationWithSettings:networkActivityBlock:completionQueue:completion:]_block_invoke.113
- ___110-[RCConfigurationManager fetchMultiConfigurationWithSettings:networkActivityBlock:completionQueue:completion:]_block_invoke.119
- ___110-[RCConfigurationManager fetchMultiConfigurationWithSettings:networkActivityBlock:completionQueue:completion:]_block_invoke.84
- ___110-[RCConfigurationManager fetchMultiConfigurationWithSettings:networkActivityBlock:completionQueue:completion:]_block_invoke_2.110
- ___110-[RCConfigurationManager fetchMultiConfigurationWithSettings:networkActivityBlock:completionQueue:completion:]_block_invoke_2.118
- ___110-[RCConfigurationManager fetchMultiConfigurationWithSettings:networkActivityBlock:completionQueue:completion:]_block_invoke_2.118.cold.1
- ___110-[RCConfigurationManager fetchMultiConfigurationWithSettings:networkActivityBlock:completionQueue:completion:]_block_invoke_2.120
- ___110-[RCConfigurationManager fetchMultiConfigurationWithSettings:networkActivityBlock:completionQueue:completion:]_block_invoke_2.88
- ___130-[RCConfigurationManager _fetchMultiConfigurationFromEndpointURL:settings:networkActivityBlock:changeTagsByRequestKey:completion:]_block_invoke.143
- ___84-[RCConfigurationManager _fetchConfigurationFromFallbackURLWithSettings:completion:]_block_invoke.146
- ___84-[RCConfigurationManager _fetchConfigurationFromFallbackURLWithSettings:completion:]_block_invoke.150
- ___84-[RCConfigurationManager _fetchConfigurationFromFallbackURLWithSettings:completion:]_block_invoke.153
- ___84-[RCConfigurationManager _fetchConfigurationFromFallbackURLWithSettings:completion:]_block_invoke_2.151
- ___84-[RCConfigurationManager _fetchConfigurationFromFallbackURLWithSettings:completion:]_block_invoke_2.151.cold.1
- ___84-[RCConfigurationManager _fetchConfigurationFromFallbackURLWithSettings:completion:]_block_invoke_2.155
- ___98-[RCConfigurationManager _isAllowedToReachEndpointWithSettings:configurationResource:endpointURL:]_block_invoke.138
- ___98-[RCConfigurationManager _isAllowedToReachEndpointWithSettings:configurationResource:endpointURL:]_block_invoke.141
- ___block_literal_global.104
- ___block_literal_global.107
- ___block_literal_global.116
- ___block_literal_global.148
- ___block_literal_global.83
- ___block_literal_global.91
- ___block_literal_global.94
- ___block_literal_global.97
- ___block_literal_global.99
CStrings:
+ "No endpoint URL available for requestKey: %{public}@ falling back to generic-edge"
+ "T@\"RCDebugOverrides\",&,N,V_debugOverrides"
+ "_debugOverrides"
+ "configuration resource no longer valid because debug overrides changed"
+ "decodeBoolForKey:"
+ "encodeBool:forKey:"
+ "hasSameFetchParametersAs:"
+ "https://devel-generic-edge.newsapps.apple.com/v1/configs"
+ "https://generic-edge.infoapps.apple.com/v1/configs"
+ "https://qa-generic-edge.newsapps.apple.com/v1/configs"
+ "https://staging-generic-edge.newsapps.apple.com/v1/configs"
+ "https://test-generic-edge.newsapps.apple.com/v1/configs"
- "No endpoint URL available for requestKey: %{public}@ falling back to news-edge"

```
