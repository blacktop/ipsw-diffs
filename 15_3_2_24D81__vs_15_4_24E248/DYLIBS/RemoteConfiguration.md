## RemoteConfiguration

> `/System/Library/PrivateFrameworks/RemoteConfiguration.framework/Versions/A/RemoteConfiguration`

```diff

-253.0.0.0.0
-  __TEXT.__text: 0x2ecc8
-  __TEXT.__auth_stubs: 0x5a0
-  __TEXT.__objc_methlist: 0x2ae0
-  __TEXT.__const: 0x1a8
-  __TEXT.__cstring: 0x491d
+260.0.0.0.0
+  __TEXT.__text: 0x2f5dc
+  __TEXT.__auth_stubs: 0x5b0
+  __TEXT.__objc_methlist: 0x2e8c
+  __TEXT.__const: 0x1a0
+  __TEXT.__cstring: 0x490c
   __TEXT.__gcc_except_tab: 0x4f0
-  __TEXT.__oslogstring: 0x1997
-  __TEXT.__unwind_info: 0xb68
+  __TEXT.__oslogstring: 0x1b4d
+  __TEXT.__unwind_info: 0xc18
   __TEXT.__objc_classname: 0x564
   __TEXT.__objc_methname: 0x8199
   __TEXT.__objc_methtype: 0x13a5

   __DATA_CONST.__objc_catlist: 0x88
   __DATA_CONST.__objc_protolist: 0x90
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x19c0
+  __DATA_CONST.__objc_selrefs: 0x1ab0
   __DATA_CONST.__objc_protorefs: 0x10
   __DATA_CONST.__objc_superrefs: 0x118
-  __AUTH_CONST.__auth_got: 0x2e0
+  __AUTH_CONST.__auth_got: 0x2e8
   __AUTH_CONST.__const: 0xd20
   __AUTH_CONST.__cfstring: 0x1fa0
-  __AUTH_CONST.__objc_const: 0x5cc0
+  __AUTH_CONST.__objc_const: 0x5658
   __AUTH_CONST.__objc_intobj: 0x18
   __AUTH.__objc_data: 0x780
   __DATA.__objc_ivar: 0x3b0

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libz.1.dylib
-  UUID: 030113C2-166E-39C0-A366-847866B2CC36
-  Functions: 1268
-  Symbols:   3056
-  CStrings:  2285
+  UUID: 37C8BC6C-A754-33AD-82B0-1B25F635CB1B
+  Functions: 1314
+  Symbols:   3108
+  CStrings:  2288
 
Symbols:
+ +[NSDate(RCAdditions) _fr_sharedYearAndMonthDateFormatter].cold.1
+ +[NSLocale(RCAdditions) rc_preferredLanguageCodes].cold.1
+ +[RCCachePolicy defaultCachePolicy].cold.1
+ +[RCCachePolicy ignoreCachePolicy].cold.1
+ +[RCEndpointResponseProcessing parseEndpointResponse:configurationSettings:maxAge:loggingPrefix:completion:].cold.1
+ +[RCKeyValueStore persistenceQueue].cold.1
+ +[RCURLSession _sharedSession].cold.1
+ -[RCConfigurationManager _endpointURLForEndpointConfig:].cold.1
+ -[RCConfigurationManager _endpointURLForEndpointConfig:].cold.2
+ -[RCConfigurationManager _endpointURLForEnvironment:requestKey:].cold.1
+ -[RCConfigurationManager _isAllowedToReachEndpointWithSettings:configurationResource:endpointURL:].cold.1
+ -[RCDeviceInfo dictionaryRepresentation].cold.1
+ -[RCFallbackOperation _parseFallbackResponse:fallbackURL:requestKey:enableExtraLogs:maxAge:etag:lastModifiedString:completion:].cold.1
+ -[RCKeyValueStore _logCacheStatus].cold.1
+ -[RCNetworkOperationURLSessionDelegate URLSession:didBecomeInvalidWithError:].cold.1
+ -[RCNetworkOperationURLSessionDelegate URLSession:didBecomeInvalidWithError:].cold.2
+ -[RCNetworkOperationURLSessionDelegate URLSession:downloadTask:didFinishDownloadingToURL:].cold.1
+ -[RCNetworkOperationURLSessionDelegate URLSession:task:didCompleteWithError:].cold.1
+ -[RCNetworkOperationURLSessionDelegate URLSession:task:didCompleteWithError:].cold.2
+ -[RCNetworkOperationURLSessionDelegate URLSession:task:didFinishCollectingMetrics:].cold.1
+ -[RCNetworkOperationURLSessionDelegate _existingNetworkTaskForURLSessionTask:].cold.1
+ -[RCOperation _finishOperationWithError:].cold.2
+ -[RCOperation _handleThrottlingFromError:delay:].cold.2
+ -[RCURLFetchOperation operationWillFinishWithError:].cold.1
+ -[RCURLFetchOperation operationWillFinishWithError:].cold.2
+ RCIsInternalBuild.cold.1
+ RCJSONArrayValue.cold.1
+ RCJSONBoolValue.cold.1
+ RCJSONDictionaryValue.cold.1
+ RCJSONDoubleValue.cold.1
+ RCJSONIntegerValue.cold.1
+ RCJSONStringValue.cold.1
+ RCSharedLog.cold.1
+ __110-[RCConfigurationManager fetchMultiConfigurationWithSettings:networkActivityBlock:completionQueue:completion:]_block_invoke_2.115.cold.1
+ __110-[RCConfigurationManager fetchMultiConfigurationWithSettings:networkActivityBlock:completionQueue:completion:]_block_invoke_2.cold.1
+ __51-[RCKeyValueStore _saveAsyncWithCompletionHandler:]_block_invoke.cold.2
+ __51-[RCKeyValueStore _saveAsyncWithCompletionHandler:]_block_invoke.cold.3
+ __66-[RCBackgroundURLSessionHandler networkSessionDidFinishWithTasks:]_block_invoke.cold.1
+ __75-[RCNetworkOperationURLSessionDelegate URLSession:dataTask:didReceiveData:]_block_invoke.cold.1
+ __77-[RCNetworkOperationURLSessionDelegate URLSession:task:didCompleteWithError:]_block_invoke.cold.1
+ __84-[RCConfigurationManager _fetchConfigurationFromFallbackURLWithSettings:completion:]_block_invoke.169
+ __84-[RCConfigurationManager _fetchConfigurationFromFallbackURLWithSettings:completion:]_block_invoke.173
+ __84-[RCConfigurationManager _fetchConfigurationFromFallbackURLWithSettings:completion:]_block_invoke_2.167.cold.1
+ __90-[RCNetworkOperationURLSessionDelegate URLSession:downloadTask:didFinishDownloadingToURL:]_block_invoke.cold.1
+ __os_log_debug_impl
- __84-[RCConfigurationManager _fetchConfigurationFromFallbackURLWithSettings:completion:]_block_invoke.172
- ___84-[RCConfigurationManager _fetchConfigurationFromFallbackURLWithSettings:completion:]_block_invoke_5
CStrings:
+ "%{public}@ Endpoint JSON HTTP response status code: %ld (%{public}@)"
+ "%{public}@ Endpoint JSON request: %{public}@"
+ "%{public}@ fallback: received configuration with requestKey: %{public}@ lastFetchedDate: %{public}@ maxAge: %{public}@ etag: %{public}@ lastModified: %{public}@ treatmentIDs: %{public}@ segmentSetIDs: %{public}@"
+ "%{public}@ successfully received configuration %{public}@ with size: %@, total time: %f"
+ "%{public}@ will perform operation to fetch config with settings %{public}@"
+ "/AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/RemoteConfiguration/RemoteConfiguration/BackgroundURLSessionSupport/RCBackgroundFetchConfiguration.m"
+ "/AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/RemoteConfiguration/RemoteConfiguration/BackgroundURLSessionSupport/RCURLSession.m"
+ "/AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/RemoteConfiguration/RemoteConfiguration/Categories/NSArray+RCAdditions.m"
+ "/AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/RemoteConfiguration/RemoteConfiguration/Categories/NSDate+RCAdditions.m"
+ "/AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/RemoteConfiguration/RemoteConfiguration/Categories/NSDateFormatter+RCAdditions.m"
+ "/AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/RemoteConfiguration/RemoteConfiguration/Categories/NSDictionary+RCAdditions.m"
+ "/AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/RemoteConfiguration/RemoteConfiguration/Categories/NSEnumerator+RCAdditions.m"
+ "/AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/RemoteConfiguration/RemoteConfiguration/Operations/RCBlockUtilities.m"
+ "/AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/RemoteConfiguration/RemoteConfiguration/Operations/RCOnce.m"
+ "/AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/RemoteConfiguration/RemoteConfiguration/Operations/RCOperation.m"
+ "/AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/RemoteConfiguration/RemoteConfiguration/Operations/RCOperationThrottler.m"
+ "/AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/RemoteConfiguration/RemoteConfiguration/Persistence/RCKeyValueStore.m"
+ "/AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/RemoteConfiguration/RemoteConfiguration/RCConfigurationFetchResult.m"
+ "/AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/RemoteConfiguration/RemoteConfiguration/RCConfigurationManager.m"
+ "/AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/RemoteConfiguration/RemoteConfiguration/RCConfigurationSettings.m"
+ "/AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/RemoteConfiguration/RemoteConfiguration/RCEndpointOperation.m"
+ "/AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/RemoteConfiguration/RemoteConfiguration/RCFallbackOperation.m"
+ "/AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/RemoteConfiguration/RemoteConfiguration/RCRequestInfo+News.m"
+ "/AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/RemoteConfiguration/RemoteConfiguration/RCRequestInfo.m"
+ "/AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/RemoteConfiguration/RemoteConfiguration/RCURLFetchOperation.m"
+ "/AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/RemoteConfiguration/RemoteConfiguration/Utilities/RCAsyncBlockOperation.m"
+ "/AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/RemoteConfiguration/RemoteConfiguration/Utilities/RCAsyncSerialQueue.m"
+ "/AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/RemoteConfiguration/RemoteConfiguration/Utilities/RCCast.m"
+ "/AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/RemoteConfiguration/RemoteConfiguration/Utilities/RCMath.m"
+ "<%@: %p; requestKey: %@ configurationID: %@ lastModified: %@ lastModifiedFallback: %@ lastFetched: %@ fallbackMaxAge: %@ endpointMaxAge: %@ etag: %@ userSegmentationConfig: %@>"
+ "cached configuration not available for requestKey: %{public}@, skip updating last fetch date, treatmentIDs and segmentSetIDs"
+ "checking if configuration is valid with resource: %{public}@ maxTTL: %lu isValid: %d useBackgroundRefreshRate: %d"
+ "configuration resource no longer valid because the storefrontID changed: %{public}@"
+ "configuration resource no longer valid because the userID changed: %{public}@"
+ "configuration resource not valid due to ignore cache policy: %{public}@"
+ "creating endpoint error with code: %{public}@ message: %{public}@ stacktrace: %@"
+ "endpoint operation failed with error: %{public}@"
+ "endpoint: missing data in configuration resource %{public}@"
+ "enqueuing configuration fetch from endpoint with settings: %{public}@"
+ "fallback operation failed with error: %{public}@"
+ "fallback: missing data in configuration resource %{public}@"
+ "fetching configuration from endpoint with settings: %{public}@"
+ "fetching configuration from fallback with settings: %{public}@"
+ "loaded configuration resource: %{public}@ size: %lu"
+ "matched contentHash, returning cached configuration for requestKey: %{public}@ treatmentIDs: %{public}@ segmentSetIDs: %{public}@ contentHash: %{public}@"
+ "missing data when loading configuration resource: %{public}@"
+ "returning the cached configuration for requestKeys: %{public}@ treatmentIDs: %{public}@ segmentSetIDs: %{public}@"
- "%{public}@ Endpoint JSON HTTP response status code: %ld (%@)"
- "%{public}@ Endpoint JSON request: %@"
- "%{public}@ fallback: received configuration with requestKey: %@ lastFetchedDate: %@ maxAge: %@ etag: %@ lastModified: %@ treatmentIDs: %@ segmentSetIDs: %@"
- "%{public}@ successfully received configuration %@ with size: %@, total time: %f"
- "%{public}@ will perform operation to fetch config with settings %@"
- "/AppleInternal/Library/BuildRoots/d187755d-b9a3-11ef-83e5-aabfac210453/Library/Caches/com.apple.xbs/Sources/RemoteConfiguration/RemoteConfiguration/BackgroundURLSessionSupport/RCBackgroundFetchConfiguration.m"
- "/AppleInternal/Library/BuildRoots/d187755d-b9a3-11ef-83e5-aabfac210453/Library/Caches/com.apple.xbs/Sources/RemoteConfiguration/RemoteConfiguration/BackgroundURLSessionSupport/RCURLSession.m"
- "/AppleInternal/Library/BuildRoots/d187755d-b9a3-11ef-83e5-aabfac210453/Library/Caches/com.apple.xbs/Sources/RemoteConfiguration/RemoteConfiguration/Categories/NSArray+RCAdditions.m"
- "/AppleInternal/Library/BuildRoots/d187755d-b9a3-11ef-83e5-aabfac210453/Library/Caches/com.apple.xbs/Sources/RemoteConfiguration/RemoteConfiguration/Categories/NSDate+RCAdditions.m"
- "/AppleInternal/Library/BuildRoots/d187755d-b9a3-11ef-83e5-aabfac210453/Library/Caches/com.apple.xbs/Sources/RemoteConfiguration/RemoteConfiguration/Categories/NSDateFormatter+RCAdditions.m"
- "/AppleInternal/Library/BuildRoots/d187755d-b9a3-11ef-83e5-aabfac210453/Library/Caches/com.apple.xbs/Sources/RemoteConfiguration/RemoteConfiguration/Categories/NSDictionary+RCAdditions.m"
- "/AppleInternal/Library/BuildRoots/d187755d-b9a3-11ef-83e5-aabfac210453/Library/Caches/com.apple.xbs/Sources/RemoteConfiguration/RemoteConfiguration/Categories/NSEnumerator+RCAdditions.m"
- "/AppleInternal/Library/BuildRoots/d187755d-b9a3-11ef-83e5-aabfac210453/Library/Caches/com.apple.xbs/Sources/RemoteConfiguration/RemoteConfiguration/Operations/RCBlockUtilities.m"
- "/AppleInternal/Library/BuildRoots/d187755d-b9a3-11ef-83e5-aabfac210453/Library/Caches/com.apple.xbs/Sources/RemoteConfiguration/RemoteConfiguration/Operations/RCOnce.m"
- "/AppleInternal/Library/BuildRoots/d187755d-b9a3-11ef-83e5-aabfac210453/Library/Caches/com.apple.xbs/Sources/RemoteConfiguration/RemoteConfiguration/Operations/RCOperation.m"
- "/AppleInternal/Library/BuildRoots/d187755d-b9a3-11ef-83e5-aabfac210453/Library/Caches/com.apple.xbs/Sources/RemoteConfiguration/RemoteConfiguration/Operations/RCOperationThrottler.m"
- "/AppleInternal/Library/BuildRoots/d187755d-b9a3-11ef-83e5-aabfac210453/Library/Caches/com.apple.xbs/Sources/RemoteConfiguration/RemoteConfiguration/Persistence/RCKeyValueStore.m"
- "/AppleInternal/Library/BuildRoots/d187755d-b9a3-11ef-83e5-aabfac210453/Library/Caches/com.apple.xbs/Sources/RemoteConfiguration/RemoteConfiguration/RCConfigurationFetchResult.m"
- "/AppleInternal/Library/BuildRoots/d187755d-b9a3-11ef-83e5-aabfac210453/Library/Caches/com.apple.xbs/Sources/RemoteConfiguration/RemoteConfiguration/RCConfigurationManager.m"
- "/AppleInternal/Library/BuildRoots/d187755d-b9a3-11ef-83e5-aabfac210453/Library/Caches/com.apple.xbs/Sources/RemoteConfiguration/RemoteConfiguration/RCConfigurationSettings.m"
- "/AppleInternal/Library/BuildRoots/d187755d-b9a3-11ef-83e5-aabfac210453/Library/Caches/com.apple.xbs/Sources/RemoteConfiguration/RemoteConfiguration/RCEndpointOperation.m"
- "/AppleInternal/Library/BuildRoots/d187755d-b9a3-11ef-83e5-aabfac210453/Library/Caches/com.apple.xbs/Sources/RemoteConfiguration/RemoteConfiguration/RCFallbackOperation.m"
- "/AppleInternal/Library/BuildRoots/d187755d-b9a3-11ef-83e5-aabfac210453/Library/Caches/com.apple.xbs/Sources/RemoteConfiguration/RemoteConfiguration/RCRequestInfo+News.m"
- "/AppleInternal/Library/BuildRoots/d187755d-b9a3-11ef-83e5-aabfac210453/Library/Caches/com.apple.xbs/Sources/RemoteConfiguration/RemoteConfiguration/RCRequestInfo.m"
- "/AppleInternal/Library/BuildRoots/d187755d-b9a3-11ef-83e5-aabfac210453/Library/Caches/com.apple.xbs/Sources/RemoteConfiguration/RemoteConfiguration/RCURLFetchOperation.m"
- "/AppleInternal/Library/BuildRoots/d187755d-b9a3-11ef-83e5-aabfac210453/Library/Caches/com.apple.xbs/Sources/RemoteConfiguration/RemoteConfiguration/Utilities/RCAsyncBlockOperation.m"
- "/AppleInternal/Library/BuildRoots/d187755d-b9a3-11ef-83e5-aabfac210453/Library/Caches/com.apple.xbs/Sources/RemoteConfiguration/RemoteConfiguration/Utilities/RCAsyncSerialQueue.m"
- "/AppleInternal/Library/BuildRoots/d187755d-b9a3-11ef-83e5-aabfac210453/Library/Caches/com.apple.xbs/Sources/RemoteConfiguration/RemoteConfiguration/Utilities/RCCast.m"
- "/AppleInternal/Library/BuildRoots/d187755d-b9a3-11ef-83e5-aabfac210453/Library/Caches/com.apple.xbs/Sources/RemoteConfiguration/RemoteConfiguration/Utilities/RCMath.m"
- "<%@: %p; requestKey: %@ configurationID: %@ contentHash: %@ lastModified: %@, etag: %@ lastModifiedFallback: %@ lastFetched: %@ fallbackMaxAge: %@ endpointMaxAge: %@ userSegmentationConfig: %@>"
- "cached configuration not available for requestKey: %@, skip updating last fetch date, treatmentIDs and segmentSetIDs"
- "checking if configuration is valid with resource: %@ maxTTL: %lu isValid: %d useBackgroundRefreshRate: %d"
- "configuration resource no longer valid because the storefrontID changed: %@"
- "configuration resource no longer valid because the userID changed: %@"
- "configuration resource not valid due to ignore cache policy: %@"
- "creating endpoint error with code: %@ message: %@ stacktrace: %@"
- "endpoint operation failed with error: %@"
- "enqueuing configuration fetch from endpoint with settings: %@"
- "fallback operation failed with error: %@"
- "fetching configuration from endpoint with settings: %@"
- "fetching configuration from fallback with settings: %@"
- "loaded configuration resource: %@"
- "matched contentHash, returning cached configuration for requestKey: %@ treatmentIDs: %@ segmentSetIDs: %@ contentHash: %@ "
- "returning the cached configuration for requestKeys: %@ treatmentIDs: %@ segmentSetIDs: %@"

```
