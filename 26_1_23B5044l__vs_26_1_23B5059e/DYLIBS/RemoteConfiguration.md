## RemoteConfiguration

> `/System/Library/PrivateFrameworks/RemoteConfiguration.framework/RemoteConfiguration`

```diff

-354.0.0.0.0
-  __TEXT.__text: 0x2d328
-  __TEXT.__auth_stubs: 0x9b0
-  __TEXT.__objc_methlist: 0x2edc
+356.0.0.0.0
+  __TEXT.__text: 0x2daa8
+  __TEXT.__auth_stubs: 0x9e0
+  __TEXT.__objc_methlist: 0x2eec
   __TEXT.__const: 0x1ba
-  __TEXT.__cstring: 0x43f5
-  __TEXT.__gcc_except_tab: 0x4e8
-  __TEXT.__oslogstring: 0x1b9f
+  __TEXT.__cstring: 0x4425
+  __TEXT.__gcc_except_tab: 0x554
+  __TEXT.__oslogstring: 0x1c7d
   __TEXT.__swift5_typeref: 0x180
   __TEXT.__swift5_capture: 0x20
   __TEXT.__swift_as_entry: 0xc
   __TEXT.__swift_as_ret: 0xc
-  __TEXT.__unwind_info: 0xba0
+  __TEXT.__unwind_info: 0xbc0
   __TEXT.__eh_frame: 0x138
   __TEXT.__objc_classname: 0x564
-  __TEXT.__objc_methname: 0x82f2
+  __TEXT.__objc_methname: 0x8302
   __TEXT.__objc_methtype: 0x13c1
-  __TEXT.__objc_stubs: 0x4f60
-  __DATA_CONST.__got: 0x310
+  __TEXT.__objc_stubs: 0x4f80
+  __DATA_CONST.__got: 0x318
   __DATA_CONST.__const: 0xfb8
   __DATA_CONST.__objc_classlist: 0x148
   __DATA_CONST.__objc_catlist: 0x88
   __DATA_CONST.__objc_protolist: 0x90
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x1ae8
+  __DATA_CONST.__objc_selrefs: 0x1af0
   __DATA_CONST.__objc_protorefs: 0x10
   __DATA_CONST.__objc_superrefs: 0x118
-  __AUTH_CONST.__auth_got: 0x4e8
-  __AUTH_CONST.__const: 0x390
-  __AUTH_CONST.__cfstring: 0x20c0
+  __AUTH_CONST.__auth_got: 0x500
+  __AUTH_CONST.__const: 0x3d0
+  __AUTH_CONST.__cfstring: 0x2120
   __AUTH_CONST.__objc_const: 0x56b8
   __AUTH_CONST.__objc_intobj: 0x18
   __AUTH.__objc_data: 0x550
   __DATA.__objc_ivar: 0x3b8
   __DATA.__data: 0x708
-  __DATA.__bss: 0x50
+  __DATA.__bss: 0x60
   __DATA_DIRTY.__objc_data: 0x780
   __DATA_DIRTY.__bss: 0x50
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation

   - /usr/lib/swift/libswiftXPC.dylib
   - /usr/lib/swift/libswift_Builtin_float.dylib
   - /usr/lib/swift/libswift_Concurrency.dylib
-  UUID: C356F7C7-12B2-3037-807F-66A5248F9334
-  Functions: 1331
-  Symbols:   4380
-  CStrings:  2322
+  UUID: CDBFE537-6940-3551-8C1D-7D615E4BDDDD
+  Functions: 1339
+  Symbols:   4406
+  CStrings:  2331
 
Symbols:
+ +[RCCachePolicy cacheOnlyPolicy]
+ +[RCCachePolicy cacheOnlyPolicy].cold.1
+ -[RCConfigurationManager fetchMultiConfigurationWithSettings:networkActivityBlock:completionQueue:completion:].cold.1
+ GCC_except_table45
+ GCC_except_table6
+ _OBJC_EHTYPE_$_NSException
+ ___110-[RCConfigurationManager fetchMultiConfigurationWithSettings:networkActivityBlock:completionQueue:completion:]_block_invoke.108
+ ___110-[RCConfigurationManager fetchMultiConfigurationWithSettings:networkActivityBlock:completionQueue:completion:]_block_invoke.109
+ ___110-[RCConfigurationManager fetchMultiConfigurationWithSettings:networkActivityBlock:completionQueue:completion:]_block_invoke.111
+ ___110-[RCConfigurationManager fetchMultiConfigurationWithSettings:networkActivityBlock:completionQueue:completion:]_block_invoke.112
+ ___110-[RCConfigurationManager fetchMultiConfigurationWithSettings:networkActivityBlock:completionQueue:completion:]_block_invoke.119
+ ___110-[RCConfigurationManager fetchMultiConfigurationWithSettings:networkActivityBlock:completionQueue:completion:]_block_invoke_2.110
+ ___110-[RCConfigurationManager fetchMultiConfigurationWithSettings:networkActivityBlock:completionQueue:completion:]_block_invoke_2.118
+ ___110-[RCConfigurationManager fetchMultiConfigurationWithSettings:networkActivityBlock:completionQueue:completion:]_block_invoke_2.118.cold.1
+ ___110-[RCConfigurationManager fetchMultiConfigurationWithSettings:networkActivityBlock:completionQueue:completion:]_block_invoke_2.120
+ ___130-[RCConfigurationManager _fetchMultiConfigurationFromEndpointURL:settings:networkActivityBlock:changeTagsByRequestKey:completion:]_block_invoke.143
+ ___32+[RCCachePolicy cacheOnlyPolicy]_block_invoke
+ ___84-[RCConfigurationManager _fetchConfigurationFromFallbackURLWithSettings:completion:]_block_invoke.146
+ ___84-[RCConfigurationManager _fetchConfigurationFromFallbackURLWithSettings:completion:]_block_invoke.150
+ ___84-[RCConfigurationManager _fetchConfigurationFromFallbackURLWithSettings:completion:]_block_invoke.153
+ ___84-[RCConfigurationManager _fetchConfigurationFromFallbackURLWithSettings:completion:]_block_invoke_2.151
+ ___84-[RCConfigurationManager _fetchConfigurationFromFallbackURLWithSettings:completion:]_block_invoke_2.151.cold.1
+ ___84-[RCConfigurationManager _fetchConfigurationFromFallbackURLWithSettings:completion:]_block_invoke_2.155
+ ___98-[RCConfigurationManager _isAllowedToReachEndpointWithSettings:configurationResource:endpointURL:]_block_invoke.138
+ ___98-[RCConfigurationManager _isAllowedToReachEndpointWithSettings:configurationResource:endpointURL:]_block_invoke.141
+ ___block_literal_global.107
+ ___block_literal_global.116
+ ___block_literal_global.148
+ ___block_literal_global.4
+ _cacheOnlyPolicy.onceToken
+ _cacheOnlyPolicy.result
+ _objc_begin_catch
+ _objc_end_catch
+ _objc_msgSend$rc_notCachedError
+ _objc_retainAutoreleasedReturnValue
- GCC_except_table52
- ___110-[RCConfigurationManager fetchMultiConfigurationWithSettings:networkActivityBlock:completionQueue:completion:]_block_invoke.105
- ___110-[RCConfigurationManager fetchMultiConfigurationWithSettings:networkActivityBlock:completionQueue:completion:]_block_invoke.106
- ___110-[RCConfigurationManager fetchMultiConfigurationWithSettings:networkActivityBlock:completionQueue:completion:]_block_invoke.107
- ___110-[RCConfigurationManager fetchMultiConfigurationWithSettings:networkActivityBlock:completionQueue:completion:]_block_invoke_2.112
- ___110-[RCConfigurationManager fetchMultiConfigurationWithSettings:networkActivityBlock:completionQueue:completion:]_block_invoke_2.112.cold.1
- ___110-[RCConfigurationManager fetchMultiConfigurationWithSettings:networkActivityBlock:completionQueue:completion:]_block_invoke_2.114
- ___130-[RCConfigurationManager _fetchMultiConfigurationFromEndpointURL:settings:networkActivityBlock:changeTagsByRequestKey:completion:]_block_invoke.138
- ___84-[RCConfigurationManager _fetchConfigurationFromFallbackURLWithSettings:completion:]_block_invoke.141
- ___84-[RCConfigurationManager _fetchConfigurationFromFallbackURLWithSettings:completion:]_block_invoke.145
- ___84-[RCConfigurationManager _fetchConfigurationFromFallbackURLWithSettings:completion:]_block_invoke.148
- ___84-[RCConfigurationManager _fetchConfigurationFromFallbackURLWithSettings:completion:]_block_invoke_2.146
- ___84-[RCConfigurationManager _fetchConfigurationFromFallbackURLWithSettings:completion:]_block_invoke_2.146.cold.1
- ___84-[RCConfigurationManager _fetchConfigurationFromFallbackURLWithSettings:completion:]_block_invoke_2.150
- ___98-[RCConfigurationManager _isAllowedToReachEndpointWithSettings:configurationResource:endpointURL:]_block_invoke.133
- ___98-[RCConfigurationManager _isAllowedToReachEndpointWithSettings:configurationResource:endpointURL:]_block_invoke.136
- ___block_literal_global.110
- ___block_literal_global.143
CStrings:
+ "<exception: %@>"
+ "<nil description>"
+ "<null>"
+ "cache-only policy: cached configuration not available or invalid for requestKeys: %{public}@"
+ "cache-only policy: returning cached configuration for requestKeys: %{public}@ treatmentIDs: %{public}@ segmentSetIDs: %{public}@"
+ "cacheOnlyPolicy"

```
