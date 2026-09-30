## SearchAssets

> `/System/Library/PrivateFrameworks/SearchAssets.framework/SearchAssets`

```diff

-3400.140.1.0.0
-  __TEXT.__text: 0x221b0
-  __TEXT.__auth_stubs: 0x1190
-  __TEXT.__objc_methlist: 0x1b0
-  __TEXT.__const: 0x161c
-  __TEXT.__cstring: 0x178f
-  __TEXT.__constg_swiftt: 0xf8c
-  __TEXT.__swift5_typeref: 0x9a9
-  __TEXT.__swift5_reflstr: 0x121b
-  __TEXT.__swift5_fieldmd: 0xc5c
-  __TEXT.__swift5_builtin: 0x14
-  __TEXT.__oslogstring: 0x1ac9
-  __TEXT.__swift5_capture: 0xf8
-  __TEXT.__swift5_proto: 0xc4
-  __TEXT.__swift5_types: 0x60
-  __TEXT.__swift5_protos: 0x50
-  __TEXT.__swift5_assocty: 0x60
-  __TEXT.__unwind_info: 0x980
-  __TEXT.__eh_frame: 0xdb4
+3401.2.1.1.1
+  __TEXT.__text: 0x278f0
+  __TEXT.__auth_stubs: 0x1200
+  __TEXT.__objc_methlist: 0x1c8
+  __TEXT.__const: 0x19ec
+  __TEXT.__cstring: 0x18af
+  __TEXT.__constg_swiftt: 0x1268
+  __TEXT.__swift5_typeref: 0xb4e
+  __TEXT.__swift5_reflstr: 0x13b4
+  __TEXT.__swift5_fieldmd: 0xe68
+  __TEXT.__swift5_builtin: 0x3c
+  __TEXT.__oslogstring: 0x2057
+  __TEXT.__swift5_capture: 0x130
+  __TEXT.__swift5_proto: 0xec
+  __TEXT.__swift5_types: 0x84
+  __TEXT.__swift5_protos: 0x58
+  __TEXT.__swift5_assocty: 0x90
+  __TEXT.__unwind_info: 0xb28
+  __TEXT.__eh_frame: 0xf5c
   __TEXT.__objc_classname: 0x99
-  __TEXT.__objc_methname: 0x6ab
-  __TEXT.__objc_methtype: 0x19e
-  __DATA_CONST.__got: 0x210
-  __DATA_CONST.__const: 0x70
-  __DATA_CONST.__objc_classlist: 0x58
+  __TEXT.__objc_methname: 0x734
+  __TEXT.__objc_methtype: 0x1f0
+  __DATA_CONST.__got: 0x248
+  __DATA_CONST.__const: 0x100
+  __DATA_CONST.__objc_classlist: 0x60
   __DATA_CONST.__objc_protolist: 0x60
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x1c0
+  __DATA_CONST.__objc_selrefs: 0x1e0
   __DATA_CONST.__objc_protorefs: 0x30
-  __AUTH_CONST.__auth_got: 0x8c8
-  __AUTH_CONST.__auth_ptr: 0x390
-  __AUTH_CONST.__const: 0xd68
-  __AUTH_CONST.__objc_const: 0x1140
-  __AUTH.__objc_data: 0x428
-  __AUTH.__data: 0xca8
-  __DATA.__data: 0xa08
-  __DATA.__bss: 0x1000
-  __DATA.__common: 0x60
+  __AUTH_CONST.__auth_got: 0x900
+  __AUTH_CONST.__auth_ptr: 0x3f0
+  __AUTH_CONST.__const: 0x1308
+  __AUTH_CONST.__objc_const: 0x1408
+  __AUTH.__objc_data: 0x448
+  __AUTH.__data: 0xe20
+  __DATA.__data: 0xbc8
+  __DATA.__common: 0x138
+  __DATA.__bss: 0x1400
   - /System/Library/Frameworks/CFNetwork.framework/CFNetwork
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
-  - /System/Library/Frameworks/CryptoKit.framework/CryptoKit
   - /System/Library/Frameworks/Foundation.framework/Foundation
   - /System/Library/Frameworks/Network.framework/Network
   - /System/Library/PrivateFrameworks/CoreAnalytics.framework/CoreAnalytics

   - /usr/lib/swift/libswiftOSLog.dylib
   - /usr/lib/swift/libswiftObjectiveC.dylib
   - /usr/lib/swift/libswiftXPC.dylib
+  - /usr/lib/swift/libswift_Builtin_float.dylib
   - /usr/lib/swift/libswift_Concurrency.dylib
+  - /usr/lib/swift/libswift_errno.dylib
+  - /usr/lib/swift/libswift_math.dylib
+  - /usr/lib/swift/libswift_signal.dylib
+  - /usr/lib/swift/libswift_stdio.dylib
+  - /usr/lib/swift/libswift_time.dylib
   - /usr/lib/swift/libswiftos.dylib
-  Functions: 878
-  Symbols:   406
-  CStrings:  353
+  - /usr/lib/swift/libswiftsys_time.dylib
+  - /usr/lib/swift/libswiftunistd.dylib
+  Functions: 1016
+  Symbols:   436
+  CStrings:  384
 
Symbols:
+ _OBJC_CLASS_$_NSNotificationCenter
+ __swift_FORCE_LOAD_$_swift_Builtin_float
+ __swift_FORCE_LOAD_$_swift_errno
+ __swift_FORCE_LOAD_$_swift_math
+ __swift_FORCE_LOAD_$_swift_signal
+ __swift_FORCE_LOAD_$_swift_stdio
+ __swift_FORCE_LOAD_$_swift_time
+ __swift_FORCE_LOAD_$_swiftsys_time
+ __swift_FORCE_LOAD_$_swiftunistd
+ _gettimeofday
+ _objc_retain_x27
+ _pthread_cond_broadcast
+ _pthread_cond_init
+ _pthread_cond_timedwait
+ _pthread_cond_wait
+ _pthread_mutex_init
+ _pthread_mutex_lock
+ _pthread_mutex_unlock
+ _swift_lookUpClassMethod
+ _swift_stdlib_random
- _objc_retain_x25
- _objc_retain_x28
CStrings:
+ " when calling pthread_cond_timedwait"
+ "@\"<PrefilterSafariSummarizationPrefetchModelProtocol>\"24@0:8@\"NSString\"16"
+ "SafariSummarizationPrefetch - After delegate.didNotFindAssetAfterThrottlingPeriodExpired hasUrlRedactMap %!{(MISSING)bool}d"
+ "SafariSummarizationPrefetch - After delegate.didNotFindAssetAfterThrottlingPeriodExpired, no urlRedactPatterns"
+ "SafariSummarizationPrefetch - Call delegate.didNotFindAssetAfterThrottlingPeriodExpired for locale %!{(MISSING)sensitive}s. No loaded assets. Next check at %!f(MISSING)"
+ "SafariSummarizationPrefetch - Canceling task if needed"
+ "SafariSummarizationPrefetch - Failed to find %!s(MISSING) key in metadata dictionary for hash: %!{(MISSING)sensitive}llu, numShards: %!l(MISSING)lu, version: %!s(MISSING)"
+ "SafariSummarizationPrefetch - Failed to find path filter hash at path: %!{(MISSING)sensitive}s, version: %!s(MISSING)"
+ "SafariSummarizationPrefetch - Failed to get asset location for asset: %!@(MISSING), countryCode: %!{(MISSING)sensitive}s, locale: %!{(MISSING)sensitive}s"
+ "SafariSummarizationPrefetch - Failed to get asset metadata version for asset: %!@(MISSING), countryCode: %!{(MISSING)sensitive}s, locale: %!{(MISSING)sensitive}s"
+ "SafariSummarizationPrefetch - Failed to get reachable asset location for asset: %!@(MISSING), countryCode: %!{(MISSING)sensitive}s, locale: %!{(MISSING)sensitive}s"
+ "SafariSummarizationPrefetch - Failed to retrieve AssetSet: %!s(MISSING), with name: %!s(MISSING), countryCode: %!{(MISSING)sensitive}s, locale: %!{(MISSING)sensitive}s"
+ "SafariSummarizationPrefetch - Failed while scanning url path filter jsonl file at path: %!{(MISSING)sensitive}s, with error: %!@(MISSING)"
+ "SafariSummarizationPrefetch - Finish loading the url path filter data"
+ "SafariSummarizationPrefetch - Made UrlRedactMap with %!l(MISSING)d entries"
+ "SafariSummarizationPrefetch - Posting notification SafariAssistantFilterDataLoaded"
+ "SafariSummarizationPrefetch - Skip processing for Url Path Filter, already loaded hash %!s(MISSING)"
+ "SafariSummarizationPrefetch - Skipping update to loadedAssets, already updated to asset version: %!s(MISSING), asset: %!@(MISSING), countryCode: %!{(MISSING)sensitive}s, locale: %!{(MISSING)sensitive}s"
+ "SafariSummarizationPrefetch - Skipping, assets unavailable. Consider request eligible. Next check at %!f(MISSING)"
+ "SafariSummarizationPrefetch - Start loading the url path filter data"
+ "SafariSummarizationPrefetch - Successfully reset filter"
+ "SafariSummarizationPrefetch - Successfully retrieved reachable asset location for asset: %!@(MISSING), countryCode: %!{(MISSING)sensitive}s, locale: %!{(MISSING)sensitive}s"
+ "SafariSummarizationPrefetch - Task cancelled, skip updating urlRedactPatterns"
+ "SafariSummarizationPrefetch - Throttling new submission. Loading the url path filter data is already in progress"
+ "SafariSummarizationPrefetch - Unsupported countryCode %!{(MISSING)sensitive}s or locale %!{(MISSING)sensitive}s"
+ "SearchAssets/lock.swift"
+ "_TtC12SearchAssets4Lock"
+ "_isAssetFound"
+ "_loadFilterDataTask"
+ "_urlRedactPatterns"
+ "_value"
+ "assetDeliveryBloomFilter"
+ "assetDeliveryGetPreloadedData"
+ "assetDeliveryPrefilterPrefetch"
+ "assetDeliveryPreloadAsset"
+ "assetDeliveryRedact"
+ "assetDeliveryRetrieveAsset"
+ "assetSpeciferHandler"
+ "common"
+ "cond"
+ "defaultCenter"
+ "isProcessingUrlRedactPatterns"
+ "mutex"
+ "nextTimeToCheckForAsset"
+ "path_filter_file_hash"
+ "postNotificationName:object:"
+ "prefilterSafariSummarizationPrefetchRequestModelWithUrlString:"
+ "resetSafariSummarizationAssets"
+ "searchAssets.safariAssistant.filterLoaded"
+ "shouldReportAnalytics"
- "SafariSummarizationPrefetch - Failed didUpdateLoadedAssets, countryCode %!{(MISSING)sensitive}s does not match deviceContext.country %!{(MISSING)sensitive}s"
- "SafariSummarizationPrefetch - Failed to find %!s(MISSING) key in metadata dictionary for hash: %!{(MISSING)sensitive}u, numShards: %!u(MISSING), version: %!s(MISSING)"
- "SafariSummarizationPrefetch - Failed to get asset location for asset: %!@(MISSING), countryCode: %!s(MISSING), locale: %!s(MISSING)"
- "SafariSummarizationPrefetch - Failed to get asset metadata version for asset: %!@(MISSING), countryCode: %!s(MISSING), locale: %!s(MISSING)"
- "SafariSummarizationPrefetch - Failed to get reachable asset location for asset: %!@(MISSING), countryCode: %!s(MISSING), locale: %!s(MISSING)"
- "SafariSummarizationPrefetch - Failed to retrieve AssetSet: %!s(MISSING), countryCode: %!{(MISSING)sensitive}s, locale: %!{(MISSING)sensitive}s"
- "SafariSummarizationPrefetch - Failed while scanning url path filter jsonl file at path: %!s(MISSING), with error: %!@(MISSING)"
- "SafariSummarizationPrefetch - Loading data for filter completed"
- "SafariSummarizationPrefetch - Loading data for filter completed unsuccessfully"
- "SafariSummarizationPrefetch - Successfully made UrlRedactMap with %!l(MISSING)d entries"
- "SafariSummarizationPrefetch - Successfully retrieved reachable asset location for asset: %!@(MISSING), countryCode: %!s(MISSING), locale: %!s(MISSING)"
- "_urlRedactMap"
- "assetDeliveryAssetAccessBloomFilter"
- "assetDeliveryAssetAccessPathFilter"
- "assetDeliveryAssetRedactPath"
- "assetDeliveryFetchAssetsSafariSummarization"
- "assetDeliveryFetchAssetsUAF"
- "assetDeliveryPreinstalledAssetsSafariSummarization"
- "assetDeliverySanitizeSafariSummarization"
- "loadFilterDataTask"

```
