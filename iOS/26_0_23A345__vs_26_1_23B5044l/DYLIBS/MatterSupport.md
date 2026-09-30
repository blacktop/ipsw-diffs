## MatterSupport

> `/System/Library/Frameworks/MatterSupport.framework/MatterSupport`

```diff

-1349.1.3.1.1
-  __TEXT.__text: 0x30514
-  __TEXT.__auth_stubs: 0x10d0
-  __TEXT.__objc_methlist: 0x1ea0
+1368.1.0.1.2
+  __TEXT.__text: 0x30bcc
+  __TEXT.__auth_stubs: 0x10f0
+  __TEXT.__objc_methlist: 0x1eb8
   __TEXT.__const: 0x2fa0
-  __TEXT.__cstring: 0x17b5
+  __TEXT.__cstring: 0x181e
   __TEXT.__swift5_typeref: 0x979
   __TEXT.__constg_swiftt: 0x74c
   __TEXT.__swift5_reflstr: 0x2ea

   __TEXT.__swift5_proto: 0x2b8
   __TEXT.__swift5_types: 0xb8
   __TEXT.__swift5_capture: 0x254
-  __TEXT.__oslogstring: 0x2173
+  __TEXT.__oslogstring: 0x22b5
   __TEXT.__swift_as_entry: 0x68
   __TEXT.__swift_as_ret: 0x48
   __TEXT.__gcc_except_tab: 0x170
-  __TEXT.__unwind_info: 0x1060
+  __TEXT.__unwind_info: 0x1068
   __TEXT.__eh_frame: 0x1120
   __TEXT.__objc_classname: 0x694
-  __TEXT.__objc_methname: 0x2fbb
-  __TEXT.__objc_methtype: 0xeee
-  __TEXT.__objc_stubs: 0x1ec0
+  __TEXT.__objc_methname: 0x3056
+  __TEXT.__objc_methtype: 0xeec
+  __TEXT.__objc_stubs: 0x1f00
   __DATA_CONST.__got: 0x370
-  __DATA_CONST.__const: 0x330
+  __DATA_CONST.__const: 0x350
   __DATA_CONST.__objc_classlist: 0x120
   __DATA_CONST.__objc_catlist: 0x20
   __DATA_CONST.__objc_protolist: 0x140
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x9b0
+  __DATA_CONST.__objc_selrefs: 0x9c0
   __DATA_CONST.__objc_protorefs: 0x40
   __DATA_CONST.__objc_superrefs: 0xe8
-  __AUTH_CONST.__auth_got: 0x878
+  __AUTH_CONST.__auth_got: 0x888
   __AUTH_CONST.__const: 0x1a20
-  __AUTH_CONST.__cfstring: 0x1380
-  __AUTH_CONST.__objc_const: 0x3a78
+  __AUTH_CONST.__cfstring: 0x13e0
+  __AUTH_CONST.__objc_const: 0x3aa8
   __AUTH_CONST.__objc_intobj: 0x78
   __AUTH.__objc_data: 0x9d8
   __AUTH.__data: 0x358
-  __DATA.__objc_ivar: 0x154
+  __DATA.__objc_ivar: 0x158
   __DATA.__data: 0x14e8
-  __DATA.__bss: 0x5760
+  __DATA.__bss: 0x5770
   __DATA.__common: 0x18
   __DATA_DIRTY.__objc_data: 0x370
-  __DATA_DIRTY.__bss: 0x30
+  __DATA_DIRTY.__bss: 0x20
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/ExtensionFoundation.framework/ExtensionFoundation
   - /System/Library/Frameworks/Foundation.framework/Foundation

   - /usr/lib/swift/libswiftAccelerate.dylib
   - /usr/lib/swift/libswiftCore.dylib
   - /usr/lib/swift/libswiftCoreFoundation.dylib
-  - /usr/lib/swift/libswiftCoreImage.dylib
   - /usr/lib/swift/libswiftDispatch.dylib
   - /usr/lib/swift/libswiftMetal.dylib
   - /usr/lib/swift/libswiftOSLog.dylib

   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  UUID: 8CF94D2F-787C-3DB8-BF3D-E3E848FF2501
-  Functions: 1414
-  Symbols:   2418
-  CStrings:  1182
+  UUID: F33FB75D-76EE-3B44-BCD3-3B4BA7C31AA5
+  Functions: 1418
+  Symbols:   2430
+  CStrings:  1195
 
Symbols:
+ -[MTSNetworkCredentialManager retrievePreferredThreadCredentialsOrCreateWithDataset:completionHandler:]
+ -[MTSThreadNetworkCredential borderAgentID]
+ -[MTSThreadNetworkCredential initWithDataset:borderAgentEUI:borderAgentID:]
+ -[MTSXPCClientProxy retrievePreferredThreadCredentialsOrCreateWithDataset:completionHandler:]
+ -[MTSXPCServer clientProxy:retrievePreferredThreadCredentialsOrCreateWithDataset:completionHandler:]
+ -[MTSXPCServerProxy retrievePreferredThreadCredentialsOrCreateWithDataset:completionHandler:]
+ GCC_except_table367
+ GCC_except_table441
+ GCC_except_table442
+ GCC_except_table480
+ GCC_except_table481
+ GCC_except_table482
+ _OBJC_IVAR_$_MTSThreadNetworkCredential._borderAgentID
+ ___103-[MTSNetworkCredentialManager retrievePreferredThreadCredentialsOrCreateWithDataset:completionHandler:]_block_invoke
+ ___87-[MTSNetworkCredentialManager retrievePreferredThreadCredentialsWithCompletionHandler:]_block_invoke
+ ___93-[MTSXPCServerProxy retrievePreferredThreadCredentialsOrCreateWithDataset:completionHandler:]_block_invoke
+ ___block_descriptor_40_e8_32bs_e5_v8?0ls32l8
+ ___block_literal_global.1434
+ ___block_literal_global.1954
+ ___block_literal_global.2403
+ ___block_literal_global.2538
+ ___block_literal_global.406
+ ___block_literal_global.483
+ ___block_literal_global.573
+ ___block_literal_global.824
+ _dispatch_async
+ _dispatch_get_global_queue
+ _logCategory._hmf_once_t15.2409
+ _logCategory._hmf_once_t9
+ _logCategory._hmf_once_v10
+ _logCategory._hmf_once_v16.2410
+ _objc_msgSend$borderAgentID
+ _objc_msgSend$clientProxy:retrievePreferredThreadCredentialsOrCreateWithDataset:completionHandler:
+ _objc_msgSend$retrievePreferredThreadCredentialsOrCreateWithDataset:completionHandler:
+ _objc_msgSend$retrievePreferredThreadCredentialsWithCompletionHandler:
- -[MTSThreadNetworkCredential initWithDataset:borderAgentEUI:]
- -[MTSXPCClientProxy retrievePreferredThreadCredentialsWithOptions:completionHandler:]
- -[MTSXPCServer clientProxy:retrievePreferredThreadCredentialsWithOptions:completionHandler:]
- -[MTSXPCServerProxy retrievePreferredThreadCredentialsWithOptions:completionHandler:]
- GCC_except_table363
- GCC_except_table437
- GCC_except_table438
- GCC_except_table474
- GCC_except_table476
- GCC_except_table477
- ___85-[MTSXPCServerProxy retrievePreferredThreadCredentialsWithOptions:completionHandler:]_block_invoke
- ___block_literal_global.1415
- ___block_literal_global.1938
- ___block_literal_global.2389
- ___block_literal_global.2525
- ___block_literal_global.401
- ___block_literal_global.479
- ___block_literal_global.568
- ___block_literal_global.821
- __swift_FORCE_LOAD_$_swiftCoreImage
- __swift_FORCE_LOAD_$_swiftCoreImage_$_MatterSupport
- _logCategory._hmf_once_t15.2395
- _logCategory._hmf_once_t6.1414
- _logCategory._hmf_once_v16.2396
- _logCategory._hmf_once_v7.1416
- _objc_msgSend$clientProxy:retrievePreferredThreadCredentialsWithOptions:completionHandler:
- _objc_msgSend$retrievePreferredThreadCredentialsWithOptions:completionHandler:
CStrings:
+ "!borderAgentID || isValidBorderAgentID(borderAgentID)"
+ "%{public}@Failed to decode MTSThreadNetworkCredentialBorderAgentIDCodingKey"
+ "%{public}@[%{public}@] Failed to retrieve or create preferred Thread credentials: %@"
+ "%{public}@[%{public}@] Retrieving or creating preferred Thread credentials"
+ "%{public}@[%{public}@] Successfully retrieved or created preferred Thread credentials"
+ "Retrieve or create preferred Thread credentials"
+ "T@\"NSData\",R,C,V_borderAgentID"
+ "_borderAgentID"
+ "borderAgentID"
+ "clientProxy:retrievePreferredThreadCredentialsOrCreateWithDataset:completionHandler:"
+ "id"
+ "initWithDataset:borderAgentEUI:borderAgentID:"
+ "retrievePreferredThreadCredentialsOrCreateWithDataset:completionHandler:"
+ "v32@0:8@\"NSData\"16@?<v@?@\"MTSThreadNetworkCredential\"@\"NSError\">24"
+ "v40@0:8@\"MTSXPCClientProxy\"16@\"NSData\"24@?<v@?@\"MTSThreadNetworkCredential\"@\"NSError\">32"
- "clientProxy:retrievePreferredThreadCredentialsWithOptions:completionHandler:"
- "initWithDataset:borderAgentEUI:"
- "v32@0:8Q16@?<v@?@\"MTSThreadNetworkCredential\"@\"NSError\">24"
- "v40@0:8@\"MTSXPCClientProxy\"16Q24@?<v@?@\"MTSThreadNetworkCredential\"@\"NSError\">32"
- "v40@0:8@16Q24@?32"

```
