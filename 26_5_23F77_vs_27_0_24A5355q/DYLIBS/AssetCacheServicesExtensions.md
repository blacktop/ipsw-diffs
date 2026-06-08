## AssetCacheServicesExtensions

> `/System/Library/PrivateFrameworks/AssetCacheServicesExtensions.framework/AssetCacheServicesExtensions`

```diff

-140.120.2.0.0
-  __TEXT.__text: 0x3c5c
-  __TEXT.__auth_stubs: 0x3d0
+151.0.0.0.0
+  __TEXT.__text: 0x3a34
   __TEXT.__objc_methlist: 0x188
   __TEXT.__const: 0x98
-  __TEXT.__gcc_except_tab: 0x130
-  __TEXT.__cstring: 0x307
+  __TEXT.__gcc_except_tab: 0x134
+  __TEXT.__cstring: 0x30b
   __TEXT.__oslogstring: 0x9b
   __TEXT.__unwind_info: 0x140
-  __TEXT.__objc_classname: 0x1f
-  __TEXT.__objc_methname: 0x90b
-  __TEXT.__objc_methtype: 0xf6
-  __TEXT.__objc_stubs: 0xa80
-  __DATA_CONST.__got: 0x110
+  __TEXT.__objc_stubs: 0x0
+  __TEXT.__auth_stubs: 0x0
+  __TEXT.__objc_classname: 0x0
+  __TEXT.__objc_methname: 0x0
+  __TEXT.__objc_methtype: 0x0
   __DATA_CONST.__const: 0x228
   __DATA_CONST.__objc_classlist: 0x8
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_selrefs: 0x2d8
   __DATA_CONST.__objc_superrefs: 0x8
-  __AUTH_CONST.__auth_got: 0x1f8
+  __DATA_CONST.__got: 0x0
   __AUTH_CONST.__const: 0x60
   __AUTH_CONST.__cfstring: 0x500
   __AUTH_CONST.__objc_const: 0x190
   __AUTH_CONST.__objc_intobj: 0x18
-  __AUTH.__objc_data: 0x50
+  __AUTH_CONST.__auth_got: 0x0
   __DATA.__objc_ivar: 0x14
+  __DATA_DIRTY.__objc_data: 0x50
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/Foundation.framework/Foundation
   - /System/Library/PrivateFrameworks/AssetCacheServices.framework/AssetCacheServices
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: CE0BE9E1-EF8E-30F6-B419-ABF123783C21
-  Functions: 51
-  Symbols:   337
-  CStrings:  211
+  UUID: 9DDBF6B3-C4A9-34D8-8F55-D0833675386A
+  Functions: 50
+  Symbols:   338
+  CStrings:  95
 
Symbols:
+ _objc_claimAutoreleasedReturnValue
+ _objc_retain
+ _objc_retain_x1
+ _objc_retain_x2
+ _objc_retain_x3
+ _objc_retain_x8
- _OUTLINED_FUNCTION_0
- _objc_retainAutoreleasedReturnValue
- _objc_retain_x27
- _objc_retain_x28
CStrings:
- ".cxx_destruct"
- "@\"<AssetCacheServicesReporterDelegate>\""
- "@\"NSMutableDictionary\""
- "@\"NSMutableSet\""
- "@\"NSObject<OS_dispatch_queue>\""
- "@\"NSObject<OS_os_log>\""
- "@16@0:8"
- "@24@0:8@16"
- "@32@0:8@16@24"
- "AssetCacheServicesReporter"
- "B32@0:8@16@24"
- "JSONObjectWithData:options:error:"
- "T@\"<AssetCacheServicesReporterDelegate>\",W,V_weakDelegate"
- "T@\"NSMutableDictionary\",&,V_results"
- "T@\"NSMutableSet\",&,V_allServerHostPorts"
- "T@\"NSObject<OS_dispatch_queue>\",W,V_weakDelegateQueue"
- "T@\"NSObject<OS_os_log>\",&,V_logHandle"
- "URLWithString:"
- "UTF8String"
- "_allServerHostPorts"
- "_logHandle"
- "_results"
- "_weakDelegate"
- "_weakDelegateQueue"
- "addEntriesFromDictionary:"
- "addObject:"
- "allKeys"
- "allServerHostPorts"
- "appendString:"
- "array"
- "bytes"
- "code"
- "compare:"
- "count"
- "countByEnumeratingWithState:objects:count:"
- "dataTaskWithRequest:completionHandler:"
- "dataWithBytes:length:"
- "dictionary"
- "dictionaryWithCapacity:"
- "dictionaryWithObjects:forKeys:count:"
- "didFinishWithResults:"
- "didGatherResults:forKeyPath:"
- "doRanges:containAddress:"
- "domain"
- "ephemeralSessionConfiguration"
- "errorWithDomain:code:userInfo:"
- "hasPrefix:"
- "hasSuffix:"
- "init"
- "initWithDelegate:delegateQueue:"
- "intValue"
- "invalidateAndCancel"
- "isEqual:"
- "isEqualToString:"
- "keyPath:byAppendingKey:"
- "length"
- "locateServersWithOptions:"
- "logHandle"
- "mutableCopy"
- "null"
- "numberWithBool:"
- "numberWithUnsignedShort:"
- "objectForKey:"
- "prettyRanges:"
- "rangeOfString:"
- "rangeOfString:options:"
- "reportCachedPublicIPAddressRangesAndFavoredServerRangesWithKeyPath:"
- "reportCachedServersWithKeyPath:"
- "reportFreshPublicIPAddressRangesAndFavoredServerRangesWithKeyPath:"
- "reportFreshServersWithKeyPath:"
- "reportMightHaveWithKeyPath:"
- "reportPublicIPAddress"
- "reportPublicIPAddressRangesWithKeyPath:andFavoredServerRangesWithKeyPath:generateOptions:"
- "reportReachability"
- "reportServersWithKeyPath:generateOptions:"
- "reporter:didFinishWithResults:"
- "reporter:didGatherResults:forKeyPath:"
- "reporter:willStartGatheringResultsForKeyPath:"
- "requestWithURL:cachePolicy:timeoutInterval:"
- "results"
- "resume"
- "serverSortInfoForHostPort:rank:"
- "sessionWithConfiguration:canUseCachingServer:locateOptions:"
- "set"
- "setAllServerHostPorts:"
- "setAllowsCellularAccess:"
- "setHTTPCookieStorage:"
- "setHTTPMethod:"
- "setHTTPShouldHandleCookies:"
- "setLogHandle:"
- "setObject:forKey:"
- "setResults:"
- "setURLCache:"
- "setURLCredentialStorage:"
- "setValue:forHTTPHeaderField:"
- "setValue:forKeyPath:"
- "setWeakDelegate:"
- "setWeakDelegateQueue:"
- "setWithCapacity:"
- "sortedArrayUsingComparator:"
- "sortedHostPorts:"
- "sortedHostPorts:usingSortInfo:"
- "start"
- "statusCode"
- "stringWithFormat:"
- "substringFromIndex:"
- "substringToIndex:"
- "substringWithRange:"
- "v16@0:8"
- "v24@0:8@16"
- "v32@0:8@16@24"
- "v32@0:8@16@?24"
- "v40@0:8@16@24@?32"
- "weakDelegate"
- "weakDelegateQueue"
- "willStartGatheringResultsForKeyPath:"

```
