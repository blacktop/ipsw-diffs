## CascadeEngine

> `/System/Library/PrivateFrameworks/CascadeEngine.framework/Versions/A/CascadeEngine`

```diff

-166.17.1.0.0
-  __TEXT.__text: 0x1e864
-  __TEXT.__auth_stubs: 0x520
-  __TEXT.__objc_methlist: 0x160c
+166.20.0.0.0
+  __TEXT.__text: 0x1ef84
+  __TEXT.__auth_stubs: 0x560
+  __TEXT.__objc_methlist: 0x161c
   __TEXT.__const: 0xe0
-  __TEXT.__gcc_except_tab: 0x5e0
-  __TEXT.__cstring: 0xc94
-  __TEXT.__oslogstring: 0x344d
+  __TEXT.__gcc_except_tab: 0x5e8
+  __TEXT.__cstring: 0xca7
+  __TEXT.__oslogstring: 0x3456
   __TEXT.__dlopen_cstrs: 0x47
-  __TEXT.__unwind_info: 0x760
+  __TEXT.__unwind_info: 0x770
   __TEXT.__objc_classname: 0x46d
-  __TEXT.__objc_methname: 0x4a2d
-  __TEXT.__objc_methtype: 0x10a7
-  __TEXT.__objc_stubs: 0x3de0
+  __TEXT.__objc_methname: 0x4b06
+  __TEXT.__objc_methtype: 0x10ba
+  __TEXT.__objc_stubs: 0x3e00
   __DATA_CONST.__got: 0x280
-  __DATA_CONST.__const: 0x100
+  __DATA_CONST.__const: 0xe0
   __DATA_CONST.__objc_classlist: 0xd8
   __DATA_CONST.__objc_catlist: 0x10
   __DATA_CONST.__objc_protolist: 0x98
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x11d8
+  __DATA_CONST.__objc_selrefs: 0x11e8
   __DATA_CONST.__objc_protorefs: 0x10
   __DATA_CONST.__objc_superrefs: 0xc8
   __DATA_CONST.__objc_arraydata: 0xb0
-  __AUTH_CONST.__auth_got: 0x2a8
-  __AUTH_CONST.__const: 0xb00
+  __AUTH_CONST.__auth_got: 0x2c8
+  __AUTH_CONST.__const: 0xb70
   __AUTH_CONST.__cfstring: 0xa20
-  __AUTH_CONST.__objc_const: 0x3090
+  __AUTH_CONST.__objc_const: 0x30c0
   __AUTH_CONST.__objc_arrayobj: 0x18
   __AUTH_CONST.__objc_intobj: 0xa8
   __AUTH_CONST.__objc_dictobj: 0x28
   __AUTH_CONST.__objc_doubleobj: 0x10
   __AUTH.__objc_data: 0x870
-  __DATA.__objc_ivar: 0x24c
+  __DATA.__objc_ivar: 0x250
   __DATA.__data: 0x720
   __DATA.__bss: 0x24
   - /System/Library/Frameworks/CloudKit.framework/Versions/A/CloudKit

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libc++.1.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 673
-  Symbols:   1908
-  CStrings:  1337
+  Functions: 679
+  Symbols:   1921
+  CStrings:  1344
 
Symbols:
+ -[CCRapportManager registerRequestID:requestHandler:completionHandler:]
+ -[CCRapportManager registeredRequestsCompletionHandlers]
+ -[CCRapportManager setRegisteredRequestsCompletionHandlers:]
+ -[CCRapportManager startWithCompletion:]
+ -[CCRapportSyncEngine registerRequestsWithCompletionHandler:]
+ GCC_except_table17
+ GCC_except_table31
+ GCC_except_table42
+ GCC_except_table52
+ GCC_except_table62
+ GCC_except_table69
+ GCC_except_table88
+ OBJC_IVAR_$_CCRapportManager._registeredRequestsCompletionHandlers
+ __49-[CCRapportSyncEngine setDiscoveryRequestHandler]_block_invoke.185
+ __57-[CCRapportSyncEngine fetchMergeableDeltasRequestHandler]_block_invoke.195
+ __58-[CCRapportManager createDiscoveryClientWithControlFlags:]_block_invoke_2.15
+ __61-[CCRapportSyncEngine registerRequestsWithCompletionHandler:]_block_invoke.114
+ __61-[CCRapportSyncEngine registerRequestsWithCompletionHandler:]_block_invoke.118
+ __61-[CCRapportSyncEngine registerRequestsWithCompletionHandler:]_block_invoke.119
+ __61-[CCRapportSyncEngine registerRequestsWithCompletionHandler:]_block_invoke.120
+ __63-[CCRapportManager sendEvent:event:toDevice:completionHandler:]_block_invoke.33
+ __64-[CCRapportSyncEngine doneFetchingMergeableDeltasRequestHandler]_block_invoke.196
+ __65-[CCRapportManager activateDirectLinkToDevice:completionHandler:]_block_invoke.35
+ __71-[CCRapportManager sendRequest:request:device:options:responseHandler:]_block_invoke.30
+ __82-[CCRapportSyncEngine addOperationsToFetchMergeableDeltasFromDevice:isReciprocal:]_block_invoke.130
+ __82-[CCRapportSyncEngine addOperationsToFetchMergeableDeltasFromDevice:isReciprocal:]_block_invoke.144
+ __82-[CCRapportSyncEngine addOperationsToFetchMergeableDeltasFromDevice:isReciprocal:]_block_invoke.145
+ __82-[CCRapportSyncEngine addOperationsToFetchMergeableDeltasFromDevice:isReciprocal:]_block_invoke.146
+ __82-[CCRapportSyncEngine addOperationsToFetchMergeableDeltasFromDevice:isReciprocal:]_block_invoke.147
+ __82-[CCRapportSyncEngine addOperationsToFetchMergeableDeltasFromDevice:isReciprocal:]_block_invoke.150
+ __82-[CCRapportSyncEngine addOperationsToFetchMergeableDeltasFromDevice:isReciprocal:]_block_invoke.151
+ __82-[CCRapportSyncEngine fetchReciprocalMergeableDeltasFromDevice:completionHandler:]_block_invoke.128
+ __82-[CCRapportSyncEngine sendFetchMergeableDeltasRequest:toDevice:completionHandler:]_block_invoke.162
+ __82-[CCRapportSyncEngine sendFetchMergeableDeltasRequest:toDevice:completionHandler:]_block_invoke.162.cold.1
+ __82-[CCRapportSyncEngine sendFetchMergeableDeltasRequest:toDevice:completionHandler:]_block_invoke.163
+ __82-[CCRapportSyncEngine sendFetchMergeableDeltasRequest:toDevice:completionHandler:]_block_invoke.165
+ __82-[CCRapportSyncEngine sendFetchMergeableDeltasRequest:toDevice:completionHandler:]_block_invoke.165.cold.1
+ __82-[CCRapportSyncEngine sendFetchMergeableDeltasRequest:toDevice:completionHandler:]_block_invoke.165.cold.2
+ ___49-[CCRapportSyncEngine startServerWithCompletion:]_block_invoke_2
+ ___61-[CCRapportSyncEngine registerRequestsWithCompletionHandler:]_block_invoke
+ ___block_descriptor_40_e8_32bs_e8_v12?0B8l
+ ___block_descriptor_40_e8_32w_e18_v16?0"NSString"8l
+ ___block_descriptor_48_e8_32s40s_e18_v16?0"NSString"8l
+ _dispatch_group_create
+ _dispatch_group_enter
+ _dispatch_group_leave
+ _dispatch_group_notify
+ _objc_msgSend$registerRequestID:requestHandler:completionHandler:
+ _objc_msgSend$registerRequestsWithCompletionHandler:
+ _objc_msgSend$setRequestIDRegistrationCompletion:
+ _objc_msgSend$startWithCompletion:
- -[CCRapportManager registerEventID:eventHandler:]
- -[CCRapportManager registerEventID:eventHandler:].cold.1
- -[CCRapportManager registerRequestID:requestHandler:]
- -[CCRapportManager start]
- -[CCRapportSyncEngine registerRequests]
- GCC_except_table16
- GCC_except_table43
- GCC_except_table53
- GCC_except_table54
- GCC_except_table59
- GCC_except_table61
- GCC_except_table81
- __49-[CCRapportSyncEngine setDiscoveryRequestHandler]_block_invoke.175
- __57-[CCRapportSyncEngine fetchMergeableDeltasRequestHandler]_block_invoke.185
- __63-[CCRapportManager sendEvent:event:toDevice:completionHandler:]_block_invoke.30
- __64-[CCRapportSyncEngine doneFetchingMergeableDeltasRequestHandler]_block_invoke.186
- __65-[CCRapportManager activateDirectLinkToDevice:completionHandler:]_block_invoke.32
- __71-[CCRapportManager sendRequest:request:device:options:responseHandler:]_block_invoke.27
- __82-[CCRapportSyncEngine addOperationsToFetchMergeableDeltasFromDevice:isReciprocal:]_block_invoke.120
- __82-[CCRapportSyncEngine addOperationsToFetchMergeableDeltasFromDevice:isReciprocal:]_block_invoke.127
- __82-[CCRapportSyncEngine addOperationsToFetchMergeableDeltasFromDevice:isReciprocal:]_block_invoke.134
- __82-[CCRapportSyncEngine addOperationsToFetchMergeableDeltasFromDevice:isReciprocal:]_block_invoke.135
- __82-[CCRapportSyncEngine addOperationsToFetchMergeableDeltasFromDevice:isReciprocal:]_block_invoke.136
- __82-[CCRapportSyncEngine addOperationsToFetchMergeableDeltasFromDevice:isReciprocal:]_block_invoke.140
- __82-[CCRapportSyncEngine addOperationsToFetchMergeableDeltasFromDevice:isReciprocal:]_block_invoke.141
- __82-[CCRapportSyncEngine fetchReciprocalMergeableDeltasFromDevice:completionHandler:]_block_invoke.118
- __82-[CCRapportSyncEngine sendFetchMergeableDeltasRequest:toDevice:completionHandler:]_block_invoke.151
- __82-[CCRapportSyncEngine sendFetchMergeableDeltasRequest:toDevice:completionHandler:]_block_invoke.151.cold.1
- __82-[CCRapportSyncEngine sendFetchMergeableDeltasRequest:toDevice:completionHandler:]_block_invoke.152
- __82-[CCRapportSyncEngine sendFetchMergeableDeltasRequest:toDevice:completionHandler:]_block_invoke.155
- __82-[CCRapportSyncEngine sendFetchMergeableDeltasRequest:toDevice:completionHandler:]_block_invoke.155.cold.1
- __82-[CCRapportSyncEngine sendFetchMergeableDeltasRequest:toDevice:completionHandler:]_block_invoke.155.cold.2
- ___25-[CCRapportManager start]_block_invoke
- ___block_descriptor_32_e8_v12?0B8l
- _objc_msgSend$registerEventID:options:handler:
- _objc_msgSend$registerRequestID:requestHandler:
- _objc_msgSend$registerRequests
CStrings:
+ "\x01\x13\x11\x13"
+ "%@: %@ registered"
+ "%@: all requests registered"
+ "T@\"NSMutableDictionary\",&,N,V_registeredRequestsCompletionHandlers"
+ "_registeredRequestsCompletionHandlers"
+ "registerRequestID:requestHandler:completionHandler:"
+ "registerRequestsWithCompletionHandler:"
+ "registeredRequestsCompletionHandlers"
+ "setRegisteredRequestsCompletionHandlers:"
+ "setRequestIDRegistrationCompletion:"
+ "startWithCompletion:"
+ "v16@?0@\"NSString\"8"
+ "v40@0:8@16@?24@?32"
- "\x01\x13\x11\x12"
- "CCRapportManager: registerEventID %@"
- "registerEventID:eventHandler:"
- "registerEventID:options:handler:"
- "registerRequestID:requestHandler:"
- "registerRequests"

```
