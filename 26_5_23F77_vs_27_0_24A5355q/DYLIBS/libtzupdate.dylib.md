## libtzupdate.dylib

> `/usr/lib/libtzupdate.dylib`

```diff

-88.0.0.0.0
-  __TEXT.__text: 0x3124
-  __TEXT.__auth_stubs: 0x330
+89.0.0.0.0
+  __TEXT.__text: 0x2eec
   __TEXT.__objc_methlist: 0x418
   __TEXT.__const: 0x48
-  __TEXT.__cstring: 0xe70
+  __TEXT.__cstring: 0xe76
   __TEXT.__unwind_info: 0x120
-  __TEXT.__objc_classname: 0x96
-  __TEXT.__objc_methname: 0xe8e
-  __TEXT.__objc_methtype: 0x127
-  __TEXT.__objc_stubs: 0x9a0
-  __DATA_CONST.__got: 0xd0
+  __TEXT.__objc_stubs: 0x0
+  __TEXT.__auth_stubs: 0x0
+  __TEXT.__objc_classname: 0x0
+  __TEXT.__objc_methname: 0x0
+  __TEXT.__objc_methtype: 0x0
   __DATA_CONST.__const: 0xe8
   __DATA_CONST.__objc_classlist: 0x40
   __DATA_CONST.__objc_protolist: 0x8

   __DATA_CONST.__objc_selrefs: 0x3a0
   __DATA_CONST.__objc_protorefs: 0x8
   __DATA_CONST.__objc_superrefs: 0x20
-  __AUTH_CONST.__auth_got: 0x1a0
+  __DATA_CONST.__got: 0xd0
   __AUTH_CONST.__const: 0x80
   __AUTH_CONST.__cfstring: 0x940
   __AUTH_CONST.__objc_const: 0x8f8
+  __AUTH_CONST.__auth_got: 0x0
   __AUTH.__objc_data: 0xa0
   __DATA.__objc_ivar: 0x50
   __DATA.__data: 0x60

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libicucore.A.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 2BE37679-FBC3-3B67-AEAC-0B30E057923F
+  UUID: 44C5557A-11B0-32B9-AA6C-FFCC471FA5BF
   Functions: 88
-  Symbols:   429
-  CStrings:  369
+  Symbols:   430
+  CStrings:  178
 
Symbols:
+ _objc_claimAutoreleasedReturnValue
+ _objc_retainAutoreleaseReturnValue
+ _objc_retain_x27
+ _objc_retain_x8
- _objc_retainAutoreleasedReturnValue
- _objc_retain_x19
- _objc_retain_x22
Functions:
~ +[TZDeviceInfoHelper icuVersion] : 204 -> 200
~ +[TZDeviceInfoHelper zoneinfoVersion] : 176 -> 168
~ +[TZFileSystemInterface sharedInstance] : 84 -> 68
~ -[TZFileSystemInterface systemICUSchemaVersionURL] : 212 -> 196
~ -[TZFileSystemInterface cacheTZLatestDestination] : 108 -> 100
~ -[TZFileSystemInterface systemVersionInfo] : 100 -> 88
~ -[TZFileSystemInterface latestVersionInfo] : 192 -> 180
~ -[TZFileSystemInterface currentVersionInfo] : 480 -> 448
~ -[TZFileSystemInterface lastInstalledVersionInfo] : 168 -> 156
~ -[TZFileSystemInterface systemICUTZSchemaVersion] : 316 -> 292
~ -[TZFileSystemInterface obtainDestinationOfLinkAtURL:] : 324 -> 312
~ +[TZUtilities stringWithContentsOfFileAtURL:error:] : 276 -> 264
~ +[TZUtilities fileExistsAndIsSymbolicLinkAtURL:] : 368 -> 360
~ +[TZVersionInfo versionInfoFromContainerDirectory:] : 560 -> 532
~ +[TZVersionInfo versionInfoFromDefaultSystem] : 244 -> 232
~ -[TZVersionInfo _initWithVersionInfoDictionary:isPartial:] : 408 -> 388
~ -[TZVersionInfo versionString] : 308 -> 276
~ +[TZVersionInfo _verifyVersionInfoDictionary:] : 1756 -> 1688
~ +[TZVersionInfo _tzDataVersionFromZoneinfoDirectory:withError:] : 364 -> 348
~ -[TZVersionInfo compare:] : 124 -> 116
~ -[TZVersionInfo description] : 180 -> 164
~ -[TZVersionInfo isBlank] : 336 -> 304
~ +[TZDLogging canLogMessageAtLevel:] : 84 -> 80
~ +[TZUpdate sharedInstance] : 84 -> 68
~ -[TZUpdate init] : 108 -> 104
~ -[TZUpdate createNewXPCConnection] : 140 -> 136
~ -[TZUpdate isUpdateWaitingWithCompletion:] : 400 -> 404
~ ___42-[TZUpdate isUpdateWaitingWithCompletion:]_block_invoke : 172 -> 168
~ ___42-[TZUpdate isUpdateWaitingWithCompletion:]_block_invoke_2 : 164 -> 160
~ -[TZUpdate purgeAllAssetsWithCompletion:] : 400 -> 404
~ ___41-[TZUpdate purgeAllAssetsWithCompletion:]_block_invoke : 176 -> 172
~ ___41-[TZUpdate purgeAllAssetsWithCompletion:]_block_invoke_2 : 188 -> 184
~ -[TZUpdate affectedZones] : 272 -> 244
~ -[TZUpdate currentTZDataVersion] : 112 -> 100
~ -[TZUpdate alertForAllZones] : 124 -> 112
~ -[TZUpdate updateTZDataVersion] : 136 -> 124
~ -[TZUpdate isUpdateWaiting] : 284 -> 248
~ +[TZPreferencesController sharedPreferencesController] : 176 -> 160
~ -[TZPreferencesController init] : 192 -> 184
CStrings:
- ".cxx_destruct"
- "@\"NSArray\""
- "@\"NSDictionary\""
- "@\"NSNumber\""
- "@\"NSString\""
- "@\"NSURL\""
- "@\"NSXPCConnection\""
- "@\"TZFileSystemInterface\""
- "@\"TZVersionInfo\""
- "@16@0:8"
- "@24@0:8@16"
- "@28@0:8@16B24"
- "@32@0:8@16^@24"
- "B16@0:8"
- "B24@0:8@16"
- "B24@0:8q16"
- "T@\"NSArray\",&,V_changedFiles"
- "T@\"NSDictionary\",&,V_alertZones"
- "T@\"NSNumber\",&,V_shouldAlertAll"
- "T@\"NSString\",&,V_bundleVersion"
- "T@\"NSString\",&,V_icuTZSchemaVersion"
- "T@\"NSString\",&,V_tzDataVersion"
- "T@\"NSString\",R"
- "T@\"NSString\",R,V_systemICUTZSchemaVersion"
- "T@\"NSURL\",&,V_cachedTZDataLocation"
- "T@\"NSURL\",&,V_dataExpansionVersionDirectory"
- "T@\"NSURL\",&,V_diskLocation"
- "T@\"NSURL\",&,V_latestTZDataLink"
- "T@\"NSURL\",&,V_temporaryDirectory"
- "T@\"NSURL\",R"
- "T@\"NSURL\",R,V_latestLinkDestinationAtStartup"
- "T@\"NSURL\",R,V_systemICUSchemaVersionURL"
- "T@\"NSXPCConnection\",&,V_connectionToService"
- "T@\"TZFileSystemInterface\",&,V_fileSystemInterface"
- "T@\"TZVersionInfo\",R,V_currentVersionInfo"
- "T@\"TZVersionInfo\",R,V_lastInstalledVersionInfo"
- "T@\"TZVersionInfo\",R,V_latestVersionInfo"
- "T@\"TZVersionInfo\",R,V_systemVersionInfo"
- "TB,R,N"
- "TZDLogging"
- "TZDeviceInfoHelper"
- "TZFileSystemInterface"
- "TZPreferencesController"
- "TZUpdate"
- "TZUpdateProtocol"
- "TZUtilities"
- "TZVersionInfo"
- "TZXPCConstants"
- "Tq,R,N"
- "URLByAppendingPathComponent:"
- "_alertZones"
- "_bundleVersion"
- "_cachedTZDataLocation"
- "_changedFiles"
- "_connectionToService"
- "_currentVersionInfo"
- "_dataExpansionVersionDirectory"
- "_diskLocation"
- "_fileSystemInterface"
- "_icuTZSchemaVersion"
- "_initWithVersionInfoDictionary:isPartial:"
- "_lastInstalledVersionInfo"
- "_latestLinkDestinationAtStartup"
- "_latestTZDataLink"
- "_latestVersionInfo"
- "_shouldAlertAll"
- "_systemICUSchemaVersionURL"
- "_systemICUTZSchemaVersion"
- "_systemVersionInfo"
- "_temporaryDirectory"
- "_tzDataVersion"
- "_tzDataVersionFromZoneinfoDirectory:withError:"
- "_verifyVersionInfoDictionary:"
- "addObserver:selector:name:object:"
- "affectedZones"
- "alertForAllZones"
- "alertZones"
- "allKeys"
- "allObjects"
- "allValues"
- "arrayWithObjects:count:"
- "blankVersionInfo"
- "boolValue"
- "bundleVersion"
- "cacheTZLatestDestination"
- "cachedTZDataLocation"
- "canLogMessageAtLevel:"
- "changedFiles"
- "compare:"
- "compare:options:"
- "connectionToService"
- "countByEnumeratingWithState:objects:count:"
- "createNewXPCConnection"
- "currentTZDataVersion"
- "currentVersionInfo"
- "currentZoneinfoLinkURL"
- "dataExpansionParentURL"
- "dataExpansionVersionDirectory"
- "defaultCenter"
- "defaultManager"
- "description"
- "destinationOfSymbolicLinkAtPath:error:"
- "dictionary"
- "dictionaryWithContentsOfURL:"
- "dictionaryWithObjects:forKeys:count:"
- "diskLocation"
- "fileExistsAndIsSymbolicLinkAtURL:"
- "fileExistsAtPath:"
- "fileSystemInterface"
- "fileSystemRepresentationWithPath:"
- "fileURLWithPath:"
- "fileURLWithPath:isDirectory:"
- "icuTZSchemaVersion"
- "icuVersion"
- "indexOfObjectPassingTest:"
- "init"
- "initWithContentsOfFile:"
- "initWithMachServiceName:options:"
- "interfaceWithProtocol:"
- "intersectSet:"
- "invalidate"
- "isBlank"
- "isEqualToSet:"
- "isEqualToString:"
- "isUpdateWaiting"
- "isUpdateWaitingWithCompletion:"
- "isUpdateWaitingWithReply:"
- "knownTimeZoneNames"
- "lastInstalledVersionInfo"
- "latestLinkDestinationAtStartup"
- "latestTZDataLink"
- "latestTZLinkURL"
- "latestVersionInfo"
- "loggingLevel"
- "newlineCharacterSet"
- "objectForKeyedSubscript:"
- "obtainDestinationOfLinkAtURL:"
- "path"
- "preferencesChanged:"
- "purgeAllAssetsWithCompletion:"
- "purgeAllAssetsWithReply:"
- "q16@0:8"
- "q24@0:8@16"
- "remoteObjectProxyWithErrorHandler:"
- "resetTemporaryDirectory"
- "resume"
- "setAlertZones:"
- "setBundleVersion:"
- "setByAddingObjectsFromSet:"
- "setCachedTZDataLocation:"
- "setChangedFiles:"
- "setConnectionToService:"
- "setDataExpansionVersionDirectory:"
- "setDiskLocation:"
- "setFileSystemInterface:"
- "setIcuTZSchemaVersion:"
- "setLatestTZDataLink:"
- "setObject:forKeyedSubscript:"
- "setRemoteObjectInterface:"
- "setShouldAlertAll:"
- "setTemporaryDirectory:"
- "setTzDataVersion:"
- "setWithArray:"
- "sharedInstance"
- "sharedPreferencesController"
- "shouldAlertAll"
- "stringByDeletingLastPathComponent"
- "stringByTrimmingCharactersInSet:"
- "stringWithContentsOfFileAtURL:error:"
- "stringWithContentsOfURL:encoding:error:"
- "stringWithFormat:"
- "stringWithUTF8String:"
- "systemICUDirectoryURL"
- "systemICUSchemaVersionURL"
- "systemICUTZSchemaVersion"
- "systemVersionInfo"
- "temporaryDirectory"
- "timeZoneDataVersion"
- "tzDataVersion"
- "updateTZDataVersion"
- "updatesEnabled"
- "v16@0:8"
- "v24@0:8@16"
- "v24@0:8@?16"
- "v24@0:8@?<v@?B>16"
- "v24@0:8@?<v@?B@\"NSError\">16"
- "versionInfoFromContainerDirectory:"
- "versionInfoFromDefaultSystem"
- "versionInfoWithDictionary:isPartial:"
- "versionString"
- "zoneinfoVersion"

```
