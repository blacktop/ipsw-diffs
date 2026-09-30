## spaceattributiond

> `/System/Library/PrivateFrameworks/SpaceAttribution.framework/spaceattributiond`

```diff

-437.0.0.0.0
-  __TEXT.__text: 0x3f200
-  __TEXT.__auth_stubs: 0x950
-  __TEXT.__objc_stubs: 0x6c40
-  __TEXT.__objc_methlist: 0x2c18
-  __TEXT.__const: 0x1e8
-  __TEXT.__oslogstring: 0x4ec6
-  __TEXT.__cstring: 0x3241
-  __TEXT.__objc_classname: 0x308
-  __TEXT.__objc_methtype: 0x10ca
-  __TEXT.__objc_methname: 0x8093
-  __TEXT.__gcc_except_tab: 0x17d8
-  __TEXT.__unwind_info: 0xdb8
-  __DATA_CONST.__auth_got: 0x4b8
-  __DATA_CONST.__got: 0x200
-  __DATA_CONST.__const: 0x14d0
-  __DATA_CONST.__cfstring: 0x28a0
-  __DATA_CONST.__objc_classlist: 0x148
+444.0.0.0.0
+  __TEXT.__text: 0x40594
+  __TEXT.__auth_stubs: 0x980
+  __TEXT.__objc_stubs: 0x6e60
+  __TEXT.__objc_methlist: 0x2d58
+  __TEXT.__const: 0x208
+  __TEXT.__gcc_except_tab: 0x1930
+  __TEXT.__cstring: 0x33c6
+  __TEXT.__objc_methname: 0x84ca
+  __TEXT.__oslogstring: 0x50e7
+  __TEXT.__objc_classname: 0x31b
+  __TEXT.__objc_methtype: 0x1126
+  __TEXT.__unwind_info: 0xe40
+  __DATA_CONST.__auth_got: 0x4d0
+  __DATA_CONST.__got: 0x210
+  __DATA_CONST.__const: 0x1638
+  __DATA_CONST.__cfstring: 0x2920
+  __DATA_CONST.__objc_classlist: 0x150
   __DATA_CONST.__objc_protolist: 0x30
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_protorefs: 0x10
-  __DATA_CONST.__objc_superrefs: 0xb8
+  __DATA_CONST.__objc_superrefs: 0xc0
   __DATA_CONST.__objc_intobj: 0x5a0
   __DATA_CONST.__objc_arraydata: 0x168
   __DATA_CONST.__objc_arrayobj: 0xa8
   __DATA_CONST.__objc_dictobj: 0x50
-  __DATA.__objc_const: 0x4080
-  __DATA.__objc_selrefs: 0x2080
-  __DATA.__objc_ivar: 0x31c
-  __DATA.__objc_data: 0xcd0
+  __DATA.__objc_const: 0x4270
+  __DATA.__objc_selrefs: 0x2128
+  __DATA.__objc_ivar: 0x338
+  __DATA.__objc_data: 0xd20
   __DATA.__data: 0x250
   __DATA.__bss: 0x1e8
   - /AppleInternal/Library/Frameworks/TapToRadarKit.framework/TapToRadarKit

   - /usr/lib/libMobileGestalt.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: E156B02D-C644-3F1B-A3B1-502AB3143A9B
-  Functions: 1350
-  Symbols:   225
-  CStrings:  2891
+  UUID: 46F3CBCD-515F-329B-A55A-B36E4B9D8451
+  Functions: 1392
+  Symbols:   230
+  CStrings:  2954
 
Symbols:
+ _NSLocalizedDescriptionKey
+ __dispatch_main_q
+ _dispatch_group_enter
+ _dispatch_group_leave
+ _dispatch_sync
CStrings:
+ "%s: Get the %@ purgeable data from CD for the %@"
+ "%s: Get the up-to-date purgeable data of the call made on the main run"
+ "%s: Synchronous purgeable data retrieval failed: %@. Falling back to cached results."
+ "%s: Synchronous purgeable data retrieval successful."
+ "-[SAVolumeScanner getPurgeableDataInfo]"
+ "-[SAVolumesInfo addSUPurgeableClone:size:volumePath:]"
+ "-[SAVolumesInfo getSUPurgeableCloneSize:volumePath:]"
+ "@\"NSError\""
+ "@\"SACacheDeleteClient\""
+ "A non-cached purgeable data call is already in progress."
+ "APFSIOC_CLONEGROUP_ITERATE returned with unexpected error %s"
+ "B40@0:8Q16^@24^@32"
+ "CDClient"
+ "Initiating asynchronous non-cached CD query on the main run"
+ "No async call has been made yet."
+ "Removing binary path %@ for %@ from app path list on disk"
+ "SACacheDeleteClient"
+ "SACacheDeleteClientErrorDomain"
+ "SU Size %llu for bundleIDs %@ overflowed (record size %llu clone groups size %llu)"
+ "T@\"NSDictionary\",&,N,V_asyncPurgeableInfo"
+ "T@\"NSError\",&,N,V_asyncPurgeableInfoError"
+ "T@\"NSMutableDictionary\",&,V_purgeableSUCloneSize"
+ "T@\"NSObject<OS_dispatch_group>\",&,N,V_dataGroup"
+ "T@\"NSObject<OS_dispatch_queue>\",&,N,V_purgeableInfoQueue"
+ "T@\"SACacheDeleteClient\",&,V_CDClient"
+ "TB,N,V_nonCachedPurgeableDataCallInProgress"
+ "TB,V_queriedNonCachedPurgeable"
+ "Timeout getting CD purgeable info"
+ "Timeout waiting for async purgeable info."
+ "Unable to get %@, purgeable size is set to 0. %@"
+ "Unable to get FS purgeable info"
+ "Unable to get total FS purgeable info"
+ "_CDClient"
+ "_asyncPurgeableInfo"
+ "_asyncPurgeableInfoError"
+ "_dataGroup"
+ "_initiateAsyncNonCachedCDQuery"
+ "_isRerun"
+ "_nonCachedPurgeableDataCallInProgress"
+ "_purgeableInfoQueue"
+ "_purgeableSUCloneSize"
+ "_queriedNonCachedPurgeable"
+ "accountForCDPluginSize:"
+ "addSUPurgeableClone:size:"
+ "addSUPurgeableClone:size:volumePath:"
+ "asyncPurgeableInfo"
+ "asyncPurgeableInfoError"
+ "cached"
+ "com.apple.SACacheDeleteClient.purgeableInfoQueue"
+ "dataGroup"
+ "getAsyncPurgeableInfoWithTimeout:results:error:"
+ "getPurgeableInfo:cached:timeout:completionHandler:"
+ "getPurgeableInfoAsync:cached:completionHandler:"
+ "getSUPurgeableCloneSize:"
+ "getSUPurgeableCloneSize:volumePath:"
+ "lastNonCachedCDQueryDateKey"
+ "main run"
+ "non-cached (run options: %zu)"
+ "nonCachedPurgeableDataCallInProgress"
+ "purgeableInfoQueue"
+ "purgeableSUCloneSize"
+ "queriedNonCachedPurgeable"
+ "re-run"
+ "setAsyncPurgeableInfo:"
+ "setAsyncPurgeableInfoError:"
+ "setCDClient:"
+ "setDataGroup:"
+ "setNonCachedPurgeableDataCallInProgress:"
+ "setPurgeableInfoQueue:"
+ "setPurgeableSUCloneSize:"
+ "setQueriedNonCachedPurgeable:"
+ "v36@0:8@16B24@?28"
+ "v44@0:8@16B24Q28@?36"
+ "volumeSupportsCloneGroups:"
- "TQ,N,V_cacheDeletePluginSize"
- "URLWithString:"
- "Unable to get %@, purgeable size is set to 0: %@"
- "_cacheDeletePluginSize"
- "accountForCDPluginSize"
- "applicationState"
- "cacheDeletePluginSize"
- "isRestricted"
- "purgeable size: %llu is greater than existing data size: %llu for bundleSet %@"
- "setCacheDeletePluginSize:"

```
