## RemoteConfiguration

> `/System/Library/PrivateFrameworks/RemoteConfiguration.framework/RemoteConfiguration`

```diff

-253.0.0.0.0
-  __TEXT.__text: 0x2a30c
-  __TEXT.__auth_stubs: 0x780
-  __TEXT.__objc_methlist: 0x2ae0
-  __TEXT.__const: 0x1a0
-  __TEXT.__cstring: 0x428d
+258.0.0.0.0
+  __TEXT.__text: 0x2abe8
+  __TEXT.__auth_stubs: 0x790
+  __TEXT.__objc_methlist: 0x2e8c
+  __TEXT.__const: 0x198
+  __TEXT.__cstring: 0x427c
   __TEXT.__gcc_except_tab: 0x4e8
-  __TEXT.__oslogstring: 0x1997
-  __TEXT.__unwind_info: 0xa50
+  __TEXT.__oslogstring: 0x1b4d
+  __TEXT.__unwind_info: 0xaf8
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
-  __AUTH_CONST.__auth_got: 0x3d0
+  __AUTH_CONST.__auth_got: 0x3d8
   __AUTH_CONST.__const: 0x2a0
   __AUTH_CONST.__cfstring: 0x1fa0
-  __AUTH_CONST.__objc_const: 0x5cc0
+  __AUTH_CONST.__objc_const: 0x5658
   __AUTH_CONST.__objc_intobj: 0x18
   __AUTH.__objc_data: 0x50
   __DATA.__objc_ivar: 0x3b0

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libz.1.dylib
-  Functions: 1227
-  Symbols:   1669
-  CStrings:  2052
+  Functions: 1273
+  Symbols:   1721
+  CStrings:  2055
 
Symbols:
+ __os_log_debug_impl
CStrings:
+ "%{public}@ Endpoint JSON HTTP response status code: %ld (%{public}@)"
+ "%{public}@ Endpoint JSON request: %{public}@"
+ "%{public}@ fallback: received configuration with requestKey: %{public}@ lastFetchedDate: %{public}@ maxAge: %{public}@ etag: %{public}@ lastModified: %{public}@ treatmentIDs: %{public}@ segmentSetIDs: %{public}@"
+ "%{public}@ successfully received configuration %{public}@ with size: %@, total time: %f"
+ "%{public}@ will perform operation to fetch config with settings %{public}@"
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
