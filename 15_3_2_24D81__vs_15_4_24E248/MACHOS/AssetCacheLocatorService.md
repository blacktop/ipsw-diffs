## AssetCacheLocatorService

> `/System/Library/PrivateFrameworks/AssetCacheServices.framework/Versions/A/XPCServices/AssetCacheLocatorService.xpc/Contents/MacOS/AssetCacheLocatorService`

```diff

-135.0.0.0.0
-  __TEXT.__text: 0x289b4
+135.1.0.0.0
+  __TEXT.__text: 0x273ec
   __TEXT.__auth_stubs: 0xc40
   __TEXT.__objc_stubs: 0x33e0
-  __TEXT.__objc_methlist: 0xf00
+  __TEXT.__objc_methlist: 0x10c4
   __TEXT.__const: 0x1fd
-  __TEXT.__cstring: 0x251c
+  __TEXT.__cstring: 0x25ab
   __TEXT.__objc_classname: 0x10c
   __TEXT.__objc_methtype: 0xf81
-  __TEXT.__gcc_except_tab: 0x580
+  __TEXT.__gcc_except_tab: 0x534
   __TEXT.__objc_methname: 0x3da6
-  __TEXT.__oslogstring: 0x2f08
-  __TEXT.__unwind_info: 0x598
+  __TEXT.__oslogstring: 0x28b4
+  __TEXT.__unwind_info: 0x5b8
   __DATA_CONST.__auth_got: 0x630
   __DATA_CONST.__got: 0x2f8
   __DATA_CONST.__const: 0xf08

   __DATA_CONST.__objc_arraydata: 0x18
   __DATA_CONST.__objc_arrayobj: 0x18
   __DATA_CONST.__objc_doubleobj: 0x20
-  __DATA.__objc_const: 0x1e40
-  __DATA.__objc_selrefs: 0xdd8
+  __DATA.__objc_const: 0x1ae8
+  __DATA.__objc_selrefs: 0xea0
   __DATA.__objc_ivar: 0x134
   __DATA.__objc_data: 0x280
   __DATA.__data: 0x190

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libresolv.9.dylib
-  UUID: FF6E5774-2072-377B-AE8A-1393FA5C23B9
-  Functions: 597
+  UUID: AA9851B6-72D9-3690-B9BC-61BB1C19ECB1
+  Functions: 592
   Symbols:   337
-  CStrings:  1634
+  CStrings:  1614
 
CStrings:
+ "#%08x [%s] XPC response to pid %d uid %d: success: servers=redacted-1003 validityInterval=%.3f elapsed=%.3f"
+ "#%08x [%s] cache refresh finished, validityInterval=%.3f, error=%@)"
+ "#%08x [%s] loadDiskCache: discarding %@ %@ entry redacted-2217"
+ "-[AssetCacheLocatorService slowcateCachingServerWithTimeout:capabilities:affinityID:forceRefresh:forceDNSRefresh:callback:tag:]_block_invoke_2"
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
- "#%08x [%s] locateLocalhostCachingServers -> %@"
- "#%08x [%s] locateLocalhostCachingServers reply callback(object=%@) calledback=%{BOOL}d"
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
