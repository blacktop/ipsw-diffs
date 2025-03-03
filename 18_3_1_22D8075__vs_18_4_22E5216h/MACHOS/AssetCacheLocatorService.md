## AssetCacheLocatorService

> `/System/Library/PrivateFrameworks/AssetCacheServices.framework/XPCServices/AssetCacheLocatorService.xpc/AssetCacheLocatorService`

```diff

-135.0.0.0.0
-  __TEXT.__text: 0x21018
+135.1.0.0.0
+  __TEXT.__text: 0x1fda0
   __TEXT.__auth_stubs: 0xd60
   __TEXT.__objc_stubs: 0x3140
-  __TEXT.__objc_methlist: 0xdfc
+  __TEXT.__objc_methlist: 0xfc4
   __TEXT.__const: 0x1df
-  __TEXT.__gcc_except_tab: 0x38c
-  __TEXT.__cstring: 0x22f4
+  __TEXT.__gcc_except_tab: 0x354
+  __TEXT.__cstring: 0x2383
   __TEXT.__objc_methname: 0x39c1
-  __TEXT.__oslogstring: 0x298f
+  __TEXT.__oslogstring: 0x2393
   __TEXT.__objc_classname: 0xfe
   __TEXT.__objc_methtype: 0xf1f
-  __TEXT.__unwind_info: 0x480
+  __TEXT.__unwind_info: 0x4b8
   __DATA_CONST.__auth_got: 0x6c0
   __DATA_CONST.__got: 0x318
   __DATA_CONST.__const: 0xbe0

   __DATA_CONST.__objc_arraydata: 0x18
   __DATA_CONST.__objc_arrayobj: 0x18
   __DATA_CONST.__objc_doubleobj: 0x10
-  __DATA.__objc_const: 0x1d40
-  __DATA.__objc_selrefs: 0xd18
+  __DATA.__objc_const: 0x19e8
+  __DATA.__objc_selrefs: 0xde0
   __DATA.__objc_ivar: 0x124
   __DATA.__objc_data: 0x280
   __DATA.__data: 0x190

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libresolv.9.dylib
-  Functions: 497
+  Functions: 492
   Symbols:   359
-  CStrings:  1289
+  CStrings:  1270
 
CStrings:
+ "#%08x [%s] XPC response to pid %d uid %d: success: servers=redacted-1003 validityInterval=%.3f elapsed=%.3f"
+ "#%08x [%s] cache refresh finished, validityInterval=%.3f, error=%@)"
+ "#%08x [%s] loadDiskCache: discarding %@ %@ entry redacted-2217"
+ "-[AssetCacheLocatorService slowcateCachingServerWithTimeout:capabilities:affinityID:forceRefresh:forceDNSRefresh:callback:tag:]_block_invoke_4"
- "#%08x [%s] %@ cached servers=%@ %@ hit=%{BOOL}d"
- "#%08x [%s] XPC response to pid %d uid %d: success: servers=%@ validityInterval=%.3f elapsed=%.3f"
- "#%08x [%s] cache refresh finished (servers=%@, sorted=%{BOOL}d, other=%@, validityInterval=%.3f, error=%@)"
- "#%08x [%s] cacheServers:%@ forAffinityID:%@ hostports=%@"
- "#%08x [%s] cacheServers:%@ forNetworkIdentifiers:[%ld]%{private}@ validityInterval:%.3f"
- "#%08x [%s] cached%@ForNetworkIdentifiers -> %@ validityInterval=%.3f"
- "#%08x [%s] cachedServers:%@ forAffinityID:%@ hostports=%@ -> %@"
- "#%08x [%s] choose:%d fromArray:%@ sorted:%{BOOL}d other:%@ -> %@"
- "#%08x [%s] doesServer:%@ haveCapabilities:%@"
- "#%08x [%s] handleLocateEvent callback(servers=%@, sorted=%{BOOL}d, other=%@, validityInterval=%.3f, error=%@)"
- "#%08x [%s] in response from %@, server entry is invalid: %@"
- "#%08x [%s] locateLocalCachingServers callback(locateServers=%@, sorted=%{BOOL}d, other=%@, locateValidityInterval=%.3f, locateError=%@)"
- "#%08x [%s] locateTetheredCachingServers -> %@"
- "#%08x [%s] parseLocateResponse -> servers=%@, validityInterval=%.3f, error=%@"
- "#%08x [%s] parseLocateResponse response=%@"
- "#%08x [%s] queryServersFromArray:%@ forReachabilityOrAffinityID:%@ withTimeout:%.3f"
- "#%08x [%s] refineServers -> best=%@ other=%@"
- "#%08x [%s] refineServers:%@"
- "#%08x [%s] serversFromArray -> %@"
- "#%08x [%s] serversFromArray:%@ withCapabilities:%@"
- "#%08x [%s] slowcateCachingServer callback(localServers=%@, sorted=%{BOOL}d, other=%@, localValidityInterval=%.3f, localError=%@)"
- "#%08x [%s] slowcateCachingServer callback(localhostServers=%@, sorted=%{BOOL}d, other=%@, localhostValidityInterval=%.3f, localhostError=%@)"
- "#%08x [%s] slowcateCachingServer finishSingleLocateAndCallBackWithServers(servers=%@, sorted=%{BOOL}d, other=%@, validityInterval=%.3f, error=%@)"

```
