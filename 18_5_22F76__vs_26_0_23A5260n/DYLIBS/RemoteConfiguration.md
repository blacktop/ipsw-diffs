## RemoteConfiguration

> `/System/Library/PrivateFrameworks/RemoteConfiguration.framework/RemoteConfiguration`

```diff

-270.0.0.0.0
-  __TEXT.__text: 0x2ac10
+350.0.0.0.0
+  __TEXT.__text: 0x2b1f8
   __TEXT.__auth_stubs: 0x790
-  __TEXT.__objc_methlist: 0x2e8c
+  __TEXT.__objc_methlist: 0x2ecc
   __TEXT.__const: 0x198
-  __TEXT.__cstring: 0x427c
+  __TEXT.__cstring: 0x4319
   __TEXT.__gcc_except_tab: 0x4e8
-  __TEXT.__oslogstring: 0x1b4d
-  __TEXT.__unwind_info: 0xb00
+  __TEXT.__oslogstring: 0x1b9d
+  __TEXT.__unwind_info: 0xad8
   __TEXT.__objc_classname: 0x564
-  __TEXT.__objc_methname: 0x8199
-  __TEXT.__objc_methtype: 0x13a5
-  __TEXT.__objc_stubs: 0x4ec0
+  __TEXT.__objc_methname: 0x8297
+  __TEXT.__objc_methtype: 0x13b0
+  __TEXT.__objc_stubs: 0x4f60
   __DATA_CONST.__got: 0x2e0
-  __DATA_CONST.__const: 0xf20
+  __DATA_CONST.__const: 0xf88
   __DATA_CONST.__objc_classlist: 0x148
   __DATA_CONST.__objc_catlist: 0x88
   __DATA_CONST.__objc_protolist: 0x90
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x1ab0
+  __DATA_CONST.__objc_selrefs: 0x1ad8
   __DATA_CONST.__objc_protorefs: 0x10
   __DATA_CONST.__objc_superrefs: 0x118
   __AUTH_CONST.__auth_got: 0x3d8
   __AUTH_CONST.__const: 0x2a0
-  __AUTH_CONST.__cfstring: 0x1fa0
-  __AUTH_CONST.__objc_const: 0x5658
+  __AUTH_CONST.__cfstring: 0x20c0
+  __AUTH_CONST.__objc_const: 0x56b8
   __AUTH_CONST.__objc_intobj: 0x18
-  __AUTH.__objc_data: 0x50
-  __DATA.__objc_ivar: 0x3b0
+  __AUTH.__objc_data: 0x550
+  __DATA.__objc_ivar: 0x3b8
   __DATA.__data: 0x6c8
   __DATA.__bss: 0x50
-  __DATA_DIRTY.__objc_data: 0xc80
+  __DATA_DIRTY.__objc_data: 0x780
   __DATA_DIRTY.__bss: 0x50
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/Foundation.framework/Foundation

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libz.1.dylib
-  UUID: FC8F1465-8638-303A-9251-368A4F0F8263
-  Functions: 1273
-  Symbols:   4360
-  CStrings:  2288
+  UUID: 1FADD142-4806-3E35-A487-E72D9B79A00D
+  Functions: 1282
+  Symbols:   4386
+  CStrings:  2315
 
Symbols:
+ +[NSError(RCErrorAdditions) rc_endpointURLNotAvailableError]
+ -[RCConfigurationManager _areAllConfigurationResourcesExpired:allowedToReachEndpoint:configurationSettings:requestKeys:]
+ -[RCConfigurationManager _areAllConfigurationResourcesInvalid:configurationSettings:allowedToReachEndpoint:requestKeys:]
+ -[RCConfigurationManager _isUnexpiredConfigurationResource:allowedToReachEndpoint:useBackgroundRefreshRate:]
+ -[RCConfigurationManager _isValidConfigurationResource:configurationSettings:allowedToReachEndpoint:cachePolicy:]
+ -[RCConfigurationResource environment]
+ -[RCConfigurationResource setEnvironment:]
+ -[RCDeviceInfo deviceClass]
+ GCC_except_table52
+ _OBJC_IVAR_$_RCConfigurationResource._environment
+ _OBJC_IVAR_$_RCDeviceInfo._deviceClass
+ _RCConfigurationResourceEndpointConfigEnvironment
+ _RCDeviceClassString
+ _RCDeviceInfoDeviceClassKey
+ ___110-[RCConfigurationManager fetchMultiConfigurationWithSettings:networkActivityBlock:completionQueue:completion:]_block_invoke.107
+ ___110-[RCConfigurationManager fetchMultiConfigurationWithSettings:networkActivityBlock:completionQueue:completion:]_block_invoke.113
+ ___110-[RCConfigurationManager fetchMultiConfigurationWithSettings:networkActivityBlock:completionQueue:completion:]_block_invoke_2.112
+ ___110-[RCConfigurationManager fetchMultiConfigurationWithSettings:networkActivityBlock:completionQueue:completion:]_block_invoke_2.112.cold.1
+ ___110-[RCConfigurationManager fetchMultiConfigurationWithSettings:networkActivityBlock:completionQueue:completion:]_block_invoke_2.114
+ ___110-[RCConfigurationManager fetchMultiConfigurationWithSettings:networkActivityBlock:completionQueue:completion:]_block_invoke_8
+ ___120-[RCConfigurationManager _areAllConfigurationResourcesExpired:allowedToReachEndpoint:configurationSettings:requestKeys:]_block_invoke
+ ___120-[RCConfigurationManager _areAllConfigurationResourcesInvalid:configurationSettings:allowedToReachEndpoint:requestKeys:]_block_invoke
+ ___block_literal_global.104
+ ___block_literal_global.110
+ _objc_msgSend$_areAllConfigurationResourcesExpired:allowedToReachEndpoint:configurationSettings:requestKeys:
+ _objc_msgSend$_areAllConfigurationResourcesInvalid:configurationSettings:allowedToReachEndpoint:requestKeys:
+ _objc_msgSend$_isUnexpiredConfigurationResource:allowedToReachEndpoint:useBackgroundRefreshRate:
+ _objc_msgSend$_isValidConfigurationResource:configurationSettings:allowedToReachEndpoint:cachePolicy:
+ _objc_msgSend$deviceClass
+ _objc_msgSend$intValue
+ _objc_msgSend$rc_endpointURLNotAvailableError
- -[RCConfigurationManager _areAllConfigurationResourcesInvalid:allowedToReachEndpoint:configurationSettings:requestKeys:]
- -[RCConfigurationManager _isValidConfigurationResource:allowedToReachEndpoint:useBackgroundRefreshRate:userID:storefrontID:cachePolicy:]
- GCC_except_table38
- GCC_except_table48
- ___110-[RCConfigurationManager fetchMultiConfigurationWithSettings:networkActivityBlock:completionQueue:completion:]_block_invoke.104
- ___110-[RCConfigurationManager fetchMultiConfigurationWithSettings:networkActivityBlock:completionQueue:completion:]_block_invoke.112
- ___110-[RCConfigurationManager fetchMultiConfigurationWithSettings:networkActivityBlock:completionQueue:completion:]_block_invoke_2.111
- ___110-[RCConfigurationManager fetchMultiConfigurationWithSettings:networkActivityBlock:completionQueue:completion:]_block_invoke_2.111.cold.1
- ___110-[RCConfigurationManager fetchMultiConfigurationWithSettings:networkActivityBlock:completionQueue:completion:]_block_invoke_2.113
- ___120-[RCConfigurationManager _areAllConfigurationResourcesInvalid:allowedToReachEndpoint:configurationSettings:requestKeys:]_block_invoke
- ___block_literal_global.103
- ___block_literal_global.109
- _objc_msgSend$_areAllConfigurationResourcesInvalid:allowedToReachEndpoint:configurationSettings:requestKeys:
- _objc_msgSend$_isValidConfigurationResource:allowedToReachEndpoint:useBackgroundRefreshRate:userID:storefrontID:cachePolicy:
CStrings:
+ "<%@: %p; preferredLanguages: %@\n deviceType: %@\n deviceClass: %@\n utcOffset: %ld\n dstOffset: %ld\n appVersion: %@\n osVersion: %@\n formatVersion: %@\n seedNumber: %@\n buildNumber: %@>"
+ "<%@: %p; requestKey:%@ configurationID:%@ lastModified:%@ lastModifiedFallback:%@ lastFetched:%@ fallbackMaxAge:%@ endpointMaxAge:%@ environment:%@ etag:%@ userSegmentationConfig:%@>"
+ "B32@0:8@16B24B28"
+ "B44@0:8@16@24B32@36"
+ "DeviceClassNumber"
+ "T@\"NSString\",R,C,N,V_deviceClass"
+ "The endpoint URL for the requested environment is not available."
+ "_areAllConfigurationResourcesExpired:allowedToReachEndpoint:configurationSettings:requestKeys:"
+ "_areAllConfigurationResourcesInvalid:configurationSettings:allowedToReachEndpoint:requestKeys:"
+ "_deviceClass"
+ "_isUnexpiredConfigurationResource:allowedToReachEndpoint:useBackgroundRefreshRate:"
+ "_isValidConfigurationResource:configurationSettings:allowedToReachEndpoint:cachePolicy:"
+ "checking if configuration is valid with resource: %{public}@ maxTTL: %lu isUnexpired: %d useBackgroundRefreshRate: %d"
+ "configuration resource not valid due to mismatched environments: %{public}@"
+ "deviceClass"
+ "intValue"
+ "ipad"
+ "iphone"
+ "mac"
+ "rc_endpointURLNotAvailableError"
+ "realityDevice"
+ "tv"
+ "watch"
- "<%@: %p; preferredLanguages: %@\n deviceType: %@\n utcOffset: %ld\n dstOffset: %ld\n appVersion: %@\n osVersion: %@\n formatVersion: %@\n seedNumber: %@\n buildNumber: %@>"
- "<%@: %p; requestKey: %@ configurationID: %@ lastModified: %@ lastModifiedFallback: %@ lastFetched: %@ fallbackMaxAge: %@ endpointMaxAge: %@ etag: %@ userSegmentationConfig: %@>"
- "B56@0:8@16B24B28@32@40@48"
- "_areAllConfigurationResourcesInvalid:allowedToReachEndpoint:configurationSettings:requestKeys:"
- "_isValidConfigurationResource:allowedToReachEndpoint:useBackgroundRefreshRate:userID:storefrontID:cachePolicy:"
- "checking if configuration is valid with resource: %{public}@ maxTTL: %lu isValid: %d useBackgroundRefreshRate: %d"

```
