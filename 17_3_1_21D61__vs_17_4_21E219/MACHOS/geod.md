## geod

> `/System/Library/PrivateFrameworks/GeoServices.framework/geod`

```diff

-1940.33.11.14.2
-  __TEXT.__text: 0x42278
-  __TEXT.__auth_stubs: 0xed0
-  __TEXT.__objc_stubs: 0x87e0
-  __TEXT.__objc_methlist: 0x2394
+1940.34.10.5.24
+  __TEXT.__text: 0x42c38
+  __TEXT.__auth_stubs: 0xf20
+  __TEXT.__objc_stubs: 0x89a0
+  __TEXT.__objc_methlist: 0x23f4
   __TEXT.__const: 0x130
   __TEXT.__gcc_except_tab: 0xaf8
-  __TEXT.__objc_methname: 0x85d1
-  __TEXT.__oslogstring: 0x285d
-  __TEXT.__cstring: 0x4b63
-  __TEXT.__objc_classname: 0x9a1
-  __TEXT.__objc_methtype: 0x1670
-  __TEXT.__unwind_info: 0x11ec
-  __DATA_CONST.__auth_got: 0x778
-  __DATA_CONST.__got: 0x390
-  __DATA_CONST.__const: 0x2148
-  __DATA_CONST.__cfstring: 0x32c0
+  __TEXT.__objc_methname: 0x878d
+  __TEXT.__oslogstring: 0x2831
+  __TEXT.__cstring: 0x4bc4
+  __TEXT.__objc_classname: 0x9c2
+  __TEXT.__objc_methtype: 0x17d9
+  __TEXT.__unwind_info: 0x1214
+  __DATA_CONST.__auth_got: 0x7a0
+  __DATA_CONST.__got: 0x378
+  __DATA_CONST.__const: 0x2198
+  __DATA_CONST.__cfstring: 0x3240
   __DATA_CONST.__objc_classlist: 0x218
   __DATA_CONST.__objc_catlist: 0x28
-  __DATA_CONST.__objc_protolist: 0xa8
+  __DATA_CONST.__objc_protolist: 0xb0
   __DATA_CONST.__objc_imageinfo: 0x8
+  __DATA_CONST.__objc_protorefs: 0x8
+  __DATA_CONST.__objc_classrefs: 0x958
+  __DATA_CONST.__objc_superrefs: 0x138
   __DATA_CONST.__objc_intobj: 0x90
-  __DATA_CONST.__objc_arraydata: 0x258
-  __DATA_CONST.__objc_arrayobj: 0x4b0
+  __DATA_CONST.__objc_arraydata: 0x278
+  __DATA_CONST.__objc_arrayobj: 0x4f8
   __DATA_CONST.__objc_dictobj: 0x78
-  __DATA.__objc_const: 0x7f38
-  __DATA.__objc_selrefs: 0x2478
-  __DATA.__objc_protorefs: 0x8
-  __DATA.__objc_classrefs: 0x8f0
-  __DATA.__objc_superrefs: 0x130
+  __DATA.__objc_const: 0x8000
+  __DATA.__objc_selrefs: 0x24f8
   __DATA.__objc_ivar: 0x204
   __DATA.__objc_data: 0x14f0
-  __DATA.__data: 0x7e0
+  __DATA.__data: 0x840
   __DATA.__bss: 0x240
   - /System/Library/Frameworks/CFNetwork.framework/CFNetwork
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation

   - /usr/lib/libcompression.dylib
   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libsqlite3.dylib
-  UUID: 995554E8-7056-3FD4-A876-6EAC327EBD0F
-  Functions: 1200
-  Symbols:   602
-  CStrings:  2888
+  UUID: 8C98F3A8-2ECA-3833-B956-93BD457EBAED
+  Functions: 1214
+  Symbols:   617
+  CStrings:  2903
 
Symbols:
+ _GEOBackgroundTaskReportReportTaskInitiated
+ _GEODataRequestTimeout
+ _GEOMapRectForMapRegion
+ _GEOMapRectIntersectsRect
+ _OBJC_CLASS_$_GEOLocationShiftingCacheItem
+ _OBJC_CLASS_$_GEOLocationShiftingCachedResponseFetchRequest
+ _OBJC_CLASS_$_GEOLocationShiftingCachedResponseFetchResponse
+ _OBJC_CLASS_$_GEOLocationShiftingEnabledRequest
+ _OBJC_CLASS_$_GEOLocationShiftingEnabledResponse
+ _OBJC_CLASS_$_GEOLocationShiftingFlushCacheRequest
+ _OBJC_CLASS_$_GEOLocationShiftingFunctionRequest
+ _OBJC_CLASS_$_GEOLocationShiftingFunctionResponse
+ _OBJC_CLASS_$_GEOLocationShiftingIsRequiredRequest
+ _OBJC_CLASS_$_GEOLocationShiftingIsRequiredResponse
+ _OBJC_CLASS_$_GEOLocationShiftingListCacheRequest
+ _OBJC_CLASS_$_GEOLocationShiftingListCacheResponse
+ _OBJC_CLASS_$_GEOLocationShiftingPruneCacheRequest
+ _OBJC_CLASS_$_GEOLocationShiftingVersionRequest
+ _OBJC_CLASS_$_GEOLocationShiftingVersionResponse
+ __GEOGetSharedTileDB
- _GEO_DEFAULT_PROTOBUF_REQUEST_TIMEOUT
- _GeoServicesConfig_LocationShiftMaxCacheAgeSeconds
- _GeoServicesConfig_LocationShiftMaxCacheCount
- _OBJC_CLASS_$_GEOLatLng
- _OBJC_CLASS_$_GEOLocationShifterPersistence
CStrings:
+ "B24@0:8@\"GEOMapRegion\"16"
+ "T@\"GEOTileDB\",R,N"
+ "T@\"NSString\",?,R,C"
+ "_GEOLocationShifterProxyInternal"
+ "_fetchCachedShiftFunctionResponseForLocation:callbackQueue:completionHandler:"
+ "_forceUpdateForUserInitiatedSubscriptionsForDataType:mode:auditToken:"
+ "_startDownloadForSubscriptionIdentifiers:mode:auditToken:"
+ "com.apple.geoservices.locationshift.cache-access"
+ "companionRequestType"
+ "deleteAllDBFilesFor:"
+ "fetchCachedFunctionWithRequest:"
+ "fetchCachedShiftFunctionResponseForLocation:callbackQueue:completionHandler:"
+ "findShiftResponseForCoordinate:reduceRadius:queue:completion:"
+ "flushDiskCacheWithRequest:"
+ "functionVersionWithRequest:"
+ "getAllShiftEntries:queue:handler:"
+ "isEnabledWithRequest:"
+ "isLocationShiftRequiredForRegion:"
+ "isRequiredForCoordinateWithRequest:"
+ "isRequiredForRegionWithRequest:"
+ "latLng"
+ "listDiskCacheWithRequest:"
+ "migrateDBFrom:to:"
+ "migrateFilesFrom:to:"
+ "pruneDiskCache"
+ "pruneDiskCacheWithRequest:"
+ "pruneShiftEntries"
+ "removeAllShiftEntries"
+ "removeAllShiftEntriesSync"
+ "setAddDate:"
+ "setCoordinate:"
+ "setEnabled:"
+ "setFunction:"
+ "setItems:"
+ "setRadiusMeters:"
+ "setRequired:"
+ "setVersion:"
+ "shiftCoordinateWithRequest:"
+ "storeShiftResponse:"
+ "v32@?0@\"GEOLocationShiftFunctionResponse\"8q16@\"NSError\"24"
+ "v40@0:8@\"GEOLatLng\"16@\"NSObject<OS_dispatch_queue>\"24@?<v@?@\"GEOLocationShiftFunctionResponse\"@\"NSError\">32"
+ "v40@0:8@\"NSObject<OS_dispatch_group>\"16@\"NSObject<OS_dispatch_queue>\"24@?<v@?@\"NSDate\"ddd>32"
+ "v40@?0@\"NSDate\"8d16d24d32"
+ "v60@0:8@\"GEOLatLng\"16d24@\"GEOMapServiceTraits\"32@\"GEOApplicationAuditToken\"40B48@?<v@?@\"GEOLocationShiftFunctionResponse\"@\"NSError\">52"
- "T@\"GEOLocationShifterPersistence\",R,N"
- "Unexpected length for 'coordinate' argument"
- "_prunePersistentCache"
- "answer"
- "coord"
- "dateWithTimeIntervalSinceNow:"
- "findResponseForCoordinate:reduceRadius:queue:completion:"
- "flushDiskCacheWithMessage:"
- "forceUpdateForUserInitiatedSubscriptionsForDataType:mode:"
- "function"
- "functionVersionWithMessage:"
- "gtLog"
- "initWithCoordinate:"
- "isEnabledWithMessage:"
- "isRequiredForCoordinateWithMessage:"
- "migrateFrom:to:"
- "pruneEntriesOlderThan:maximumEntriesToKeep:"
- "removeAllEntries"
- "removeAllEntriesSync"
- "setGtLog:"
- "sharedPersister"
- "shiftCoordinateWithMessage:"
- "startDownloadForSubscriptionIdentifiers:mode:"
- "storeResponse:"
- "version"

```
