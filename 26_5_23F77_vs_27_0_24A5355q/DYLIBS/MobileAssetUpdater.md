## MobileAssetUpdater

> `/System/Library/PrivateFrameworks/MobileAssetUpdater.framework/MobileAssetUpdater`

```diff

-1345.120.5.0.0
-  __TEXT.__text: 0x1614
-  __TEXT.__auth_stubs: 0x180
+1576.0.0.0.0
+  __TEXT.__text: 0x161c
   __TEXT.__objc_methlist: 0x200
   __TEXT.__const: 0x10
   __TEXT.__gcc_except_tab: 0x4c
   __TEXT.__cstring: 0x639
   __TEXT.__unwind_info: 0xd0
-  __TEXT.__objc_classname: 0x13
-  __TEXT.__objc_methname: 0x830
-  __TEXT.__objc_methtype: 0x108
-  __TEXT.__objc_stubs: 0x7c0
-  __DATA_CONST.__got: 0x70
+  __TEXT.__objc_stubs: 0x0
+  __TEXT.__auth_stubs: 0x0
+  __TEXT.__objc_classname: 0x0
+  __TEXT.__objc_methname: 0x0
+  __TEXT.__objc_methtype: 0x0
   __DATA_CONST.__const: 0xa0
   __DATA_CONST.__objc_classlist: 0x8
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x2a0
+  __DATA_CONST.__objc_selrefs: 0x298
   __DATA_CONST.__objc_superrefs: 0x8
-  __AUTH_CONST.__auth_got: 0xd0
+  __DATA_CONST.__got: 0x0
   __AUTH_CONST.__cfstring: 0x5c0
   __AUTH_CONST.__objc_const: 0x360
+  __AUTH_CONST.__auth_got: 0x0
   __DATA.__objc_ivar: 0x3c
   __DATA_DIRTY.__objc_data: 0x50
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation

   - /usr/lib/libMobileGestalt.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 8540258A-BBBF-3837-B234-75FD063AEEA9
+  UUID: C40F5ED3-8FF4-38A8-B2B1-76585EE2D8CD
   Functions: 54
-  Symbols:   241
-  CStrings:  238
+  Symbols:   240
+  CStrings:  101
 
Symbols:
+ _MANonUserInitiatedDownloadsAllowedForAssetType
- _OBJC_CLASS_$_ASAsset
- _objc_msgSend$nonUserInitiatedDownloadsAllowed
Functions:
~ -[MobileAssetUpdater findAsset:completion:] : 1440 -> 1448
CStrings:
- "@\"MAAsset\""
- "@\"MAAssetQuery\""
- "@\"NSLock\""
- "@\"NSMutableArray\""
- "@\"NSString\""
- "@\"NSURL\""
- "@16@0:8"
- "@24@0:8@16"
- "@24@0:8@?16"
- "@28@0:8B16@?20"
- "@?"
- "@?16@0:8"
- "B"
- "B16@0:8"
- "B24@0:8@16"
- "B40@0:8@16@24@32"
- "MobileAssetUpdater"
- "T@\"MAAsset\",&,V_asset"
- "T@\"MAAssetQuery\",&,V_query"
- "T@\"NSMutableArray\",C,N,V_alternateAssetTypes"
- "T@\"NSString\",&,V_overrideFile"
- "T@\"NSString\",&,V_purgeOverrideFile"
- "T@\"NSString\",C,V_assetType"
- "T@\"NSURL\",&,V_assetLocation"
- "T@\"NSURL\",&,V_assetLocationOverride"
- "T@?,C,V_logger"
- "TB,R"
- "TB,R,V_assetDownloaded"
- "TB,R,V_overrideApplied"
- "TB,V_downloadOnCellularAllowed"
- "TB,V_requireAssetMetadata"
- "_alternateAssetTypes"
- "_asset"
- "_assetDownloaded"
- "_assetLocation"
- "_assetLocationOverride"
- "_assetType"
- "_downloadOnCellularAllowed"
- "_lock"
- "_logger"
- "_overrideApplied"
- "_overrideFile"
- "_participateInSeed"
- "_purgeOverrideFile"
- "_query"
- "_requireAssetMetadata"
- "addKeyValuePair:with:"
- "alternateAssetTypes"
- "asset"
- "assetAvailable"
- "assetDownloaded"
- "assetId"
- "assetLocation"
- "assetLocationOverride"
- "assetType"
- "assetWithMaxVersion:"
- "attributes"
- "compare:"
- "copy"
- "count"
- "countByEnumeratingWithState:objects:count:"
- "dealloc"
- "defaultManager"
- "dictionaryWithCapacity:"
- "dictionaryWithContentsOfFile:"
- "doneWithAsset"
- "downloadAsset:"
- "downloadComplete:completion:"
- "downloadOnCellularAllowed"
- "errorWithDomain:code:userInfo:"
- "fileExistsAtPath:"
- "filterAsset:osBuild:osVersion:"
- "filterFoundAssets:"
- "filteredArrayUsingPredicate:"
- "findAsset:completion:"
- "firstObject"
- "indexesOfObjectsWithOptions:passingTest:"
- "init"
- "initWithAssetType:"
- "initWithFormat:"
- "initWithFormat:arguments:"
- "initWithType:"
- "isDeploymentAllowed:"
- "lock"
- "log:format:"
- "logger"
- "mutableCopy"
- "nonUserInitiatedDownloadsAllowed"
- "objectForKey:"
- "objectsAtIndexes:"
- "overrideApplied"
- "overrideFile"
- "overrideQueryPredicateFromDict:"
- "purge:"
- "purgeAsset"
- "purgeOverrideFile"
- "purgeSync"
- "query"
- "queryComplete:remote:status:completion:"
- "queryMetaData:"
- "queryPredicate"
- "refreshState"
- "removeItemAtPath:error:"
- "removeObjectAtIndex:"
- "requireAssetMetadata"
- "results"
- "returnTypes:"
- "setAllowsCellularAccess:"
- "setAlternateAssetTypes:"
- "setAsset:"
- "setAssetLocation:"
- "setAssetLocationOverride:"
- "setAssetType:"
- "setDiscretionary:"
- "setDownloadOnCellularAllowed:"
- "setLogger:"
- "setObject:forKey:"
- "setOverrideFile:"
- "setPurgeOverrideFile:"
- "setQuery:"
- "setRequireAssetMetadata:"
- "startCatalogDownload:options:then:"
- "startDownload:then:"
- "state"
- "stringValue"
- "unlock"
- "v16@0:8"
- "v20@0:8B16"
- "v24@0:8@16"
- "v24@0:8@?16"
- "v28@0:8i16@20"
- "v32@0:8q16@?24"
- "v44@0:8@16B24q28@?36"
- "validateAsset"
- "validateAssetAttributes:"
- "valueForKey:"
- "wasPurgeable"

```
