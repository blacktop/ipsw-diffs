## NetworkInfo

> `/System/Library/PrivateFrameworks/NetworkInfo.framework/NetworkInfo`

```diff

-194.80.3.0.0
-  __TEXT.__text: 0xec670
-  __TEXT.__auth_stubs: 0x2440
+194.100.9.0.0
+  __TEXT.__text: 0xebbe4
+  __TEXT.__auth_stubs: 0x23a0
   __TEXT.__objc_methlist: 0x8f4
   __TEXT.__const: 0x35d0
-  __TEXT.__cstring: 0x45e7
+  __TEXT.__cstring: 0x3ebf
   __TEXT.__oslogstring: 0x2234
   __TEXT.__gcc_except_tab: 0x14
   __TEXT.__swift5_typeref: 0xf85

   __TEXT.__swift5_types: 0x154
   __TEXT.__swift_as_entry: 0x8c
   __TEXT.__swift_as_ret: 0xd8
-  __TEXT.__unwind_info: 0x1600
-  __TEXT.__eh_frame: 0x22b8
-  __TEXT.__objc_classname: 0x8f
-  __TEXT.__objc_methname: 0x16e2
-  __TEXT.__objc_methtype: 0x8a3
-  __TEXT.__objc_stubs: 0xae0
-  __DATA_CONST.__got: 0x530
+  __TEXT.__unwind_info: 0x1608
+  __TEXT.__eh_frame: 0x2248
+  __TEXT.__objc_classname: 0x4bc
+  __TEXT.__objc_methname: 0x1db5
+  __TEXT.__objc_methtype: 0x9f6
+  __TEXT.__objc_stubs: 0xf60
+  __DATA_CONST.__got: 0x520
   __DATA_CONST.__const: 0x840
   __DATA_CONST.__objc_classlist: 0xf0
   __DATA_CONST.__objc_protolist: 0x40

   __DATA_CONST.__objc_selrefs: 0x5e0
   __DATA_CONST.__objc_protorefs: 0x20
   __DATA_CONST.__objc_superrefs: 0x20
-  __AUTH_CONST.__auth_got: 0x1230
+  __AUTH_CONST.__auth_got: 0x11e0
   __AUTH_CONST.__const: 0x8660
   __AUTH_CONST.__cfstring: 0x320
   __AUTH_CONST.__objc_const: 0x2518

   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswift_DarwinFoundation1.dylib
   - /usr/lib/swift/libswiftos.dylib
-  UUID: 5A719D64-1A88-3390-807B-F97310E7296F
-  Functions: 3488
-  Symbols:   1937
-  CStrings:  1271
+  UUID: E6D80F58-BA06-3A53-8DDC-4C640770F0D3
+  Functions: 3496
+  Symbols:   1980
+  CStrings:  1331
 
Symbols:
+ _OUTLINED_FUNCTION_20
+ _OUTLINED_FUNCTION_21
+ _OUTLINED_FUNCTION_22
+ _OUTLINED_FUNCTION_23
+ ___swift_assign_boxed_opaque_existential_1
+ _block_copy_helper.383
+ _block_copy_helper.432
+ _block_copy_helper.520
+ _block_copy_helper.523
+ _block_descriptor.385
+ _block_descriptor.434
+ _block_descriptor.522
+ _block_descriptor.525
+ _block_destroy_helper.384
+ _block_destroy_helper.433
+ _block_destroy_helper.521
+ _block_destroy_helper.524
+ _objc_msgSend$connectEndDate
+ _objc_msgSend$connectStartDate
+ _objc_msgSend$countOfResponseBodyBytesAfterDecoding
+ _objc_msgSend$countOfResponseBodyBytesReceived
+ _objc_msgSend$createDirectoryAtPath:withIntermediateDirectories:attributes:error:
+ _objc_msgSend$defaultManager
+ _objc_msgSend$defaultSessionConfiguration
+ _objc_msgSend$domainLookupEndDate
+ _objc_msgSend$domainLookupStartDate
+ _objc_msgSend$fetchStartDate
+ _objc_msgSend$init
+ _objc_msgSend$initWithQueue:
+ _objc_msgSend$initWithQueue:service:
+ _objc_msgSend$integerValue
+ _objc_msgSend$invalidateAndCancel
+ _objc_msgSend$invalidateConnections
+ _objc_msgSend$localAddress
+ _objc_msgSend$networkProtocolName
+ _objc_msgSend$remoteAddress
+ _objc_msgSend$requestEndDate
+ _objc_msgSend$requestStartDate
+ _objc_msgSend$resolveHostname:withCompletion:
+ _objc_msgSend$responseEndDate
+ _objc_msgSend$responseStartDate
+ _objc_msgSend$secureConnectionEndDate
+ _objc_msgSend$secureConnectionStartDate
+ _objc_msgSend$sessionWithConfiguration:delegate:delegateQueue:
+ _objc_msgSend$setDelegate:
+ _objc_msgSend$setRequestCachePolicy:
+ _objc_msgSend$setTimeoutIntervalForRequest:
+ _objc_msgSend$setTimeoutIntervalForResource:
+ _objc_msgSend$startPing:hostName:interface:pingCount:interPingInterval:burstCount:interBurstInterval:timeout:stopTestOnFirstSuccess:withCompletion:
+ _objc_msgSend$startTask:destination:withCompletion:
+ _objc_msgSend$statusCode
+ _objc_msgSend$stopTask:withCompletion:
+ _objc_msgSend$transactionMetrics
+ _traceroute4_run.cold.2
- _block_copy_helper.373
- _block_copy_helper.422
- _block_copy_helper.510
- _block_copy_helper.513
- _block_descriptor.375
- _block_descriptor.424
- _block_descriptor.512
- _block_descriptor.515
- _block_destroy_helper.374
- _block_destroy_helper.423
- _block_destroy_helper.511
- _block_destroy_helper.514
- _ifaddrlist
- _ifaddrlist_free
- _ioctl
- _objc_claimAutoreleasedReturnValue
- _objc_retain_x1
- _objc_retain_x2
- _objc_retain_x26
- _objc_retain_x3
- _objc_retain_x4
CStrings:
+ "%s: getifaddrs: %s\n"
+ "NetworkInfo"
+ "NetworkInfoAssessment"
+ "NetworkInfoConfiguration"
+ "NetworkInfoResults"
+ "NetworkInfoSnapshotter"
+ "StaticString should have Unicode scalar representation"
+ "TraceRoute"
- "%s: ifaddrlist: %s\n"
- "Buffer must contain a whole number of Element instances"
- "Division by zero"
- "Division results in an overflow"
- "SIOCGIFADDR: %s: %s"
- "SIOCGIFCONF: %s"
- "SIOCGIFCONF: ifreq struct too small (%d bytes)"
- "SIOCGIFFLAGS: %.*s: %s"
- "Too many interfaces (%d)"
- "socket: %s"

```
