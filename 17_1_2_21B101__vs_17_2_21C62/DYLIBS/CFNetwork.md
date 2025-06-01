## CFNetwork

> `/System/Library/Frameworks/CFNetwork.framework/CFNetwork`

```diff

-1485.0.0.0.0
-  __TEXT.__text: 0x2842a8
-  __TEXT.__auth_stubs: 0x55f0
-  __TEXT.__objc_methlist: 0x8e40
+1490.0.4.0.0
+  __TEXT.__text: 0x2863dc
+  __TEXT.__auth_stubs: 0x5600
+  __TEXT.__objc_methlist: 0x8e90
   __TEXT.__const: 0xc9a4c
-  __TEXT.__gcc_except_tab: 0x13e04
-  __TEXT.__cstring: 0x1aa1e
-  __TEXT.__oslogstring: 0x1014c
-  __TEXT.__dlopen_cstrs: 0xff3
+  __TEXT.__gcc_except_tab: 0x13f3c
+  __TEXT.__cstring: 0x1ab09
+  __TEXT.__oslogstring: 0x1036c
+  __TEXT.__dlopen_cstrs: 0x104b
   __TEXT.__dof_CFNetwork: 0xf3b
-  __TEXT.__unwind_info: 0xc778
+  __TEXT.__unwind_info: 0xc848
   __TEXT.__eh_frame: 0x38
   __TEXT.__objc_classname: 0x15ca
-  __TEXT.__objc_methname: 0x17eae
-  __TEXT.__objc_methtype: 0x6e02
-  __TEXT.__objc_stubs: 0xe9a0
+  __TEXT.__objc_methname: 0x17f94
+  __TEXT.__objc_methtype: 0x6e05
+  __TEXT.__objc_stubs: 0xe9e0
   __DATA_CONST.__got: 0x758
-  __DATA_CONST.__const: 0x9ec0
+  __DATA_CONST.__const: 0x9f48
   __DATA_CONST.__objc_classlist: 0x508
   __DATA_CONST.__objc_catlist: 0x10
   __DATA_CONST.__objc_protolist: 0x130
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_const: 0x122b8
-  __DATA_CONST.__objc_selrefs: 0x4c58
+  __DATA_CONST.__objc_const: 0x123b8
+  __DATA_CONST.__objc_selrefs: 0x4c80
   __DATA_CONST.__objc_arraydata: 0x58
-  __AUTH_CONST.__const: 0x13da8
-  __AUTH_CONST.__cfstring: 0xfb00
+  __AUTH_CONST.__const: 0x13f38
+  __AUTH_CONST.__cfstring: 0xfc00
   __AUTH_CONST.__objc_const: 0x39e0
   __AUTH_CONST.__objc_intobj: 0x180
   __AUTH_CONST.__objc_dictobj: 0x28
   __AUTH_CONST.__objc_arrayobj: 0x30
-  __AUTH_CONST.__auth_got: 0x2b10
+  __AUTH_CONST.__auth_got: 0x2b18
   __AUTH.__objc_data: 0x17c0
   __AUTH.__cfstring_CFN: 0x7b60
   __AUTH.__data: 0x358
   __DATA.__objc_protorefs: 0x20
   __DATA.__objc_classrefs: 0x5e8
   __DATA.__objc_superrefs: 0x410
-  __DATA.__objc_ivar: 0x13c0
+  __DATA.__objc_ivar: 0x13d4
   __DATA.__data: 0x1950
   __DATA.__crash_info: 0x40
-  __DATA.__bss: 0xd98
+  __DATA.__bss: 0xda8
   __DATA_DIRTY.__objc_data: 0x1a90
   __DATA_DIRTY.__data: 0x270
   __DATA_DIRTY.__bss: 0x9e0

   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libsqlite3.dylib
   - /usr/lib/libz.1.dylib
-  UUID: D0B06B1A-16BF-37D6-80FD-A783C24A8BF4
-  Functions: 13475
-  Symbols:   2545
-  CStrings:  11807
+  UUID: 707E82B7-49FC-31AA-A493-F47AAC5C7C41
+  Functions: 13521
+  Symbols:   2550
+  CStrings:  11840
 
Symbols:
+ __CFHTTPAuthenticationCopySortedAuthSchemes
+ __CFHTTPAuthenticationGetSchemesDict
+ __CFHTTPAuthenticationSetPreferredScheme
+ _estimatedPropertyListSize
+ _nw_tcp_options_set_enable_background_traffic_management
+ _setxattr
- _nw_parameters_set_background_traffic_management
CStrings:
+ "Dropping oversized protocol property key %@ in %@"
+ "Failed to set can-suspend-locked at %s: %{errno}d"
+ "HTTP/2 Connection %llu Stream %d ended. Connection considered operational %{bool}d"
+ "TB,V_canSuspendLocked"
+ "Task <%{public,uuid_t}.16P>.<%lu> summary for %{public}s {transaction_duration_ms=%u, response_status=%ld, connection=%llu, reused=1, reused_after_ms=%u, request_start_ms=%u, request_duration_ms=%u, response_start_ms=%u, response_duration_ms=%u, request_bytes=%lld, response_bytes=%lld, cache_hit=%{bool}d}"
+ "Task <%{public,uuid_t}.16P>.<%lu> summary for %{public}s {transaction_duration_ms=%u, response_status=%ld, connection=%llu, reused=1, reused_after_ms=%u, reused_after_sleep=%{bool}d, request_start_ms=%u, request_duration_ms=%u, response_start_ms=%u, response_duration_ms=%u, request_bytes=%lld, response_bytes=%lld, cache_hit=%{bool}d}"
+ "V\xf05"
+ "^{CFNetworkTaskMetrics_s=QQQqqqQQ[16C][16C]iBB[0{?=QQQQQQ[16C]qqqiBBBBqQB}]}24@0:8@16"
+ "_apSleepWakeMonitored"
+ "_canSuspendLocked"
+ "_idleAtTime"
+ "_onqueue_logConnectionsAtAPSleep"
+ "_onqueue_markConnectionsReusedAfterAPSleepWake"
+ "_reusedAfterAPSleepWake"
+ "_reusedAfterTime"
+ "apSleepWakeMonitored"
+ "canSuspendLocked"
+ "com.apple.CFNetwork.ConnectionIdleAtSleepEvent"
+ "com.apple.runningboard.can-suspend-locked"
+ "idleAtTime"
+ "idleDuration"
+ "logConnectionAtAPSleep: idleDuration=%u"
+ "preconnect"
+ "reusedAfterSleepWake"
+ "reusedAfterTime"
+ "setCanSuspendLocked:"
+ "setReusedAfterAPSleepWake"
+ "v32@?0@\"NSObject\"8@\"NSObject\"16^B24"
- "HTTP/2 Connection %llu Stream %d ended successfully %{bool}d"
- "Task <%{public,uuid_t}.16P>.<%lu> summary for %{public}s {transaction_duration_ms=%u, response_status=%ld, connection=%llu, reused=1, request_start_ms=%u, request_duration_ms=%u, response_start_ms=%u, response_duration_ms=%u, request_bytes=%lld, response_bytes=%lld, cache_hit=%{bool}d}"
- "V\xf0%"
- "^{CFNetworkTaskMetrics_s=QQQqqqQQ[16C][16C]iB[0{?=QQQQQQ[16C]qqqiBBBBq}]}24@0:8@16"

```
