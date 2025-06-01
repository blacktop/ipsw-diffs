## RemoteConfiguration

> `/System/Library/PrivateFrameworks/RemoteConfiguration.framework/RemoteConfiguration`

```diff

-212.0.0.0.0
-  __TEXT.__text: 0x25108
+221.0.0.0.0
+  __TEXT.__text: 0x25a20
   __TEXT.__auth_stubs: 0x750
-  __TEXT.__objc_methlist: 0x261c
+  __TEXT.__objc_methlist: 0x26b8
   __TEXT.__const: 0x120
-  __TEXT.__cstring: 0x3e47
+  __TEXT.__cstring: 0x3f6b
   __TEXT.__gcc_except_tab: 0x2b8
-  __TEXT.__oslogstring: 0x15d3
-  __TEXT.__unwind_info: 0x88c
-  __TEXT.__objc_classname: 0x529
-  __TEXT.__objc_methname: 0x73cc
-  __TEXT.__objc_methtype: 0x1212
-  __TEXT.__objc_stubs: 0x4a20
+  __TEXT.__oslogstring: 0x160b
+  __TEXT.__unwind_info: 0x990
+  __TEXT.__objc_classname: 0x53b
+  __TEXT.__objc_methname: 0x759c
+  __TEXT.__objc_methtype: 0x127a
+  __TEXT.__objc_stubs: 0x4b00
   __DATA_CONST.__got: 0x88
-  __DATA_CONST.__const: 0xe60
-  __DATA_CONST.__objc_classlist: 0x130
+  __DATA_CONST.__const: 0xe90
+  __DATA_CONST.__objc_classlist: 0x138
   __DATA_CONST.__objc_catlist: 0x88
   __DATA_CONST.__objc_protolist: 0x90
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_const: 0x4328
-  __DATA_CONST.__objc_selrefs: 0x1780
+  __DATA_CONST.__objc_const: 0x4380
+  __DATA_CONST.__objc_selrefs: 0x17c0
   __DATA_CONST.__objc_protorefs: 0x10
-  __DATA_CONST.__objc_classrefs: 0x240
+  __DATA_CONST.__objc_classrefs: 0x248
   __DATA_CONST.__objc_superrefs: 0x108
-  __AUTH_CONST.__cfstring: 0x1da0
-  __AUTH_CONST.__objc_const: 0x1208
-  __AUTH_CONST.__const: 0x260
+  __AUTH_CONST.__cfstring: 0x1de0
+  __AUTH_CONST.__objc_const: 0x1298
+  __AUTH_CONST.__const: 0x2a0
   __AUTH_CONST.__objc_intobj: 0x18
   __AUTH_CONST.__auth_got: 0x3b8
-  __AUTH.__objc_data: 0x4b0
-  __DATA.__objc_ivar: 0x354
-  __DATA.__data: 0x6c8
-  __DATA.__bss: 0x49
+  __AUTH.__objc_data: 0x500
+  __DATA.__objc_ivar: 0x358
+  __DATA.__data: 0x6e8
+  __DATA.__bss: 0x50
   __DATA_DIRTY.__objc_data: 0x730
   __DATA_DIRTY.__bss: 0x30
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libz.1.dylib
-  UUID: EAEF820E-AD96-39C6-BEC3-D46CA4009074
-  Functions: 1135
-  Symbols:   3865
-  CStrings:  2122
+  UUID: 92635275-A2EB-3A16-BFF1-83814913B1F3
+  Functions: 1154
+  Symbols:   3928
+  CStrings:  2145
 
Symbols:
+ +[RCCachePolicy defaultCachePolicy]
+ +[RCCachePolicy ignoreCachePolicy]
+ -[RCCachePolicy copyWithZone:]
+ -[RCCachePolicy description]
+ -[RCCachePolicy hash]
+ -[RCCachePolicy isEqual:]
+ -[RCCachePolicy requestCachePolicy]
+ -[RCCachePolicy setRequestCachePolicy:]
+ -[RCConfigurationManager _isValidConfigurationResource:allowedToReachEndpoint:useBackgroundRefreshRate:userID:cachePolicy:]
+ -[RCConfigurationSettings requestInfoForRequestCacheKey:]
+ -[RCRequestInfo cachePolicy]
+ -[RCRequestInfo initWithRequestKey:responseKey:fallbackURL:requestType:additionalChangeTags:requestCacheKey:]
+ -[RCRequestInfo initWithRequestKey:responseKey:fallbackURL:requestType:additionalChangeTags:requestCacheKey:cachePolicy:]
+ -[RCRequestInfo initWithRequestKey:responseKey:fallbackURL:requestType:additionalChangeTags:requestCacheKey:cachePolicy:].cold.1
+ -[RCRequestInfo initWithRequestKey:responseKey:fallbackURL:requestType:additionalChangeTags:requestCacheKey:cachePolicy:].cold.2
+ -[RCRequestInfo(News) initWithRequestKey:responseKey:fallbackURL:requestType:additionalChangeTags:requestFeedType:]
+ -[RCRequestInfo(News) initWithRequestKey:responseKey:fallbackURL:requestType:additionalChangeTags:requestFeedType:cachePolicy:]
+ -[RCRequestInfo(News) initWithRequestKey:responseKey:fallbackURL:requestType:additionalChangeTags:requestFeedType:cachePolicy:].cold.1
+ -[RCRequestInfo(News) initWithRequestKey:responseKey:fallbackURL:requestType:additionalChangeTags:requestFeedType:cachePolicy:].cold.2
+ _OBJC_CLASS_$_RCCachePolicy
+ _OBJC_IVAR_$_RCCachePolicy._requestCachePolicy
+ _OBJC_IVAR_$_RCRequestInfo._cachePolicy
+ _OBJC_METACLASS_$_RCCachePolicy
+ _RCRequestFeedTypePremiumLiteKey
+ __OBJC_$_CLASS_METHODS_RCCachePolicy
+ __OBJC_$_INSTANCE_METHODS_RCCachePolicy
+ __OBJC_$_INSTANCE_METHODS_RCRequestInfo(News)
+ __OBJC_$_INSTANCE_VARIABLES_RCCachePolicy
+ __OBJC_$_PROP_LIST_RCCachePolicy
+ __OBJC_CLASS_PROTOCOLS_$_RCCachePolicy
+ __OBJC_CLASS_RO_$_RCCachePolicy
+ __OBJC_METACLASS_RO_$_RCCachePolicy
+ ___109-[RCConfigurationManager _fetchMultiConfigurationFromEndpointURL:settings:changeTagsByRequestKey:completion:]_block_invoke.138
+ ___34+[RCCachePolicy ignoreCachePolicy]_block_invoke
+ ___35+[RCCachePolicy defaultCachePolicy]_block_invoke
+ ___57-[RCConfigurationSettings requestInfoForRequestCacheKey:]_block_invoke
+ ___84-[RCConfigurationManager _fetchConfigurationFromFallbackURLWithSettings:completion:]_block_invoke.141
+ ___84-[RCConfigurationManager _fetchConfigurationFromFallbackURLWithSettings:completion:]_block_invoke.145
+ ___84-[RCConfigurationManager _fetchConfigurationFromFallbackURLWithSettings:completion:]_block_invoke_2.146
+ ___98-[RCConfigurationManager _isAllowedToReachEndpointWithSettings:configurationResource:endpointURL:]_block_invoke.133
+ ___98-[RCConfigurationManager _isAllowedToReachEndpointWithSettings:configurationResource:endpointURL:]_block_invoke.136
+ ___block_descriptor_40_e8_32s_e23_B16?0"RCRequestInfo"8ls32l8
+ ___block_literal_global.143
+ ___block_literal_global.2
+ _defaultCachePolicy.onceToken
+ _defaultCachePolicy.result
+ _ignoreCachePolicy.onceToken
+ _ignoreCachePolicy.result
+ _objc_msgSend$_isValidConfigurationResource:allowedToReachEndpoint:useBackgroundRefreshRate:userID:cachePolicy:
+ _objc_msgSend$allocWithZone:
+ _objc_msgSend$cachePolicy
+ _objc_msgSend$defaultCachePolicy
+ _objc_msgSend$initWithRequestKey:responseKey:fallbackURL:requestType:additionalChangeTags:requestCacheKey:
+ _objc_msgSend$initWithRequestKey:responseKey:fallbackURL:requestType:additionalChangeTags:requestCacheKey:cachePolicy:
+ _objc_msgSend$initWithRequestKey:responseKey:fallbackURL:requestType:additionalChangeTags:requestFeedType:cachePolicy:
+ _objc_msgSend$requestCachePolicy
+ _objc_msgSend$requestInfoForRequestCacheKey:
+ _objc_msgSend$setValue:forAdditionalField:
- -[RCConfigurationManager _isValidConfigurationResource:allowedToReachEndpoint:useBackgroundRefreshRate:userID:]
- -[RCRequestInfo initWithRequestKey:responseKey:fallbackURL:requestType:additionalChangeTags:requestFeedType:]
- -[RCRequestInfo initWithRequestKey:responseKey:fallbackURL:requestType:additionalChangeTags:requestFeedType:].cold.1
- -[RCRequestInfo initWithRequestKey:responseKey:fallbackURL:requestType:additionalChangeTags:requestFeedType:].cold.2
- -[RCRequestInfo requestFeedType]
- _OBJC_IVAR_$_RCRequestInfo._requestFeedType
- __OBJC_$_INSTANCE_METHODS_RCRequestInfo
- ___109-[RCConfigurationManager _fetchMultiConfigurationFromEndpointURL:settings:changeTagsByRequestKey:completion:]_block_invoke.137
- ___84-[RCConfigurationManager _fetchConfigurationFromFallbackURLWithSettings:completion:]_block_invoke.140
- ___84-[RCConfigurationManager _fetchConfigurationFromFallbackURLWithSettings:completion:]_block_invoke.144
- ___84-[RCConfigurationManager _fetchConfigurationFromFallbackURLWithSettings:completion:]_block_invoke_2.145
- ___98-[RCConfigurationManager _isAllowedToReachEndpointWithSettings:configurationResource:endpointURL:]_block_invoke.132
- ___98-[RCConfigurationManager _isAllowedToReachEndpointWithSettings:configurationResource:endpointURL:]_block_invoke.135
- ___block_literal_global.142
- _objc_msgSend$_isValidConfigurationResource:allowedToReachEndpoint:useBackgroundRefreshRate:userID:
- _objc_msgSend$initWithRequestKey:responseKey:fallbackURL:requestType:additionalChangeTags:requestFeedType:
- _objc_msgSend$requestFeedType
CStrings:
+ "\x03\x14"
+ "-[RCRequestInfo initWithRequestKey:responseKey:fallbackURL:requestType:additionalChangeTags:requestCacheKey:cachePolicy:]"
+ "-[RCRequestInfo(News) initWithRequestKey:responseKey:fallbackURL:requestType:additionalChangeTags:requestFeedType:cachePolicy:]"
+ "/Library/Caches/com.apple.xbs/Sources/RemoteConfiguration/RemoteConfiguration/RCRequestInfo+News.m"
+ "<%@: %p; requestKey: %@ responseKey: %@ fallbackURL: %@ requestType: %lu, additionalChangeTags: %@, cacheKey: %@, additionalFields: %@ cachePolicy: %@>"
+ "<%@: requestCachePolicy: %lu>"
+ "@\"RCCachePolicy\""
+ "@64@0:8@16@24@32Q40@48@56"
+ "@72@0:8@16@24@32Q40@48@56@64"
+ "@72@0:8@16@24@32Q40@48Q56@64"
+ "B48@0:8@16B24B28@32@40"
+ "News"
+ "RCCachePolicy"
+ "T@\"RCCachePolicy\",R,N,V_cachePolicy"
+ "TQ,N,V_requestCachePolicy"
+ "_cachePolicy"
+ "_isValidConfigurationResource:allowedToReachEndpoint:useBackgroundRefreshRate:userID:cachePolicy:"
+ "_requestCachePolicy"
+ "allocWithZone:"
+ "cachePolicy"
+ "configuration resource no longer valid because the userID changed: %@"
+ "configuration resource not valid due to ignore cache policy: %@"
+ "defaultCachePolicy"
+ "ignoreCachePolicy"
+ "initWithRequestKey:responseKey:fallbackURL:requestType:additionalChangeTags:requestCacheKey:"
+ "initWithRequestKey:responseKey:fallbackURL:requestType:additionalChangeTags:requestCacheKey:cachePolicy:"
+ "initWithRequestKey:responseKey:fallbackURL:requestType:additionalChangeTags:requestFeedType:cachePolicy:"
+ "premium_lite"
+ "requestCachePolicy"
+ "requestInfoForRequestCacheKey:"
- "\x03\x11\x12"
- "-[RCRequestInfo initWithRequestKey:responseKey:fallbackURL:requestType:additionalChangeTags:requestFeedType:]"
- "<%@: %p; requestKey: %@ responseKey: %@ fallbackURL: %@ requestType: %lu requestFeedType: %lu additionalChangeTags: %@, additionalFields: %@>"
- "B40@0:8@16B24B28@32"
- "TQ,R,N,V_requestFeedType"
- "_isValidConfigurationResource:allowedToReachEndpoint:useBackgroundRefreshRate:userID:"
- "_requestFeedType"
- "configuration with resource: %@ is no longer valid because the userID changed"
- "requestFeedType"

```
