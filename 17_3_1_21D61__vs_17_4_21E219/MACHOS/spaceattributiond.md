## spaceattributiond

> `/System/Library/PrivateFrameworks/SpaceAttribution.framework/spaceattributiond`

```diff

-180.60.4.0.0
-  __TEXT.__text: 0x26074
-  __TEXT.__auth_stubs: 0x820
-  __TEXT.__objc_stubs: 0x3cc0
-  __TEXT.__objc_methlist: 0x16c0
-  __TEXT.__gcc_except_tab: 0x114c
-  __TEXT.__oslogstring: 0x2d4a
-  __TEXT.__cstring: 0x2256
-  __TEXT.__objc_methname: 0x4637
-  __TEXT.__objc_classname: 0x213
-  __TEXT.__objc_methtype: 0xc1d
-  __TEXT.__const: 0x90
-  __TEXT.__unwind_info: 0x82c
-  __DATA_CONST.__auth_got: 0x420
-  __DATA_CONST.__got: 0x68
-  __DATA_CONST.__const: 0xca0
-  __DATA_CONST.__cfstring: 0x1a60
-  __DATA_CONST.__objc_classlist: 0xd8
+180.102.1.0.0
+  __TEXT.__text: 0x2a7c4
+  __TEXT.__auth_stubs: 0x8f0
+  __TEXT.__objc_stubs: 0x4400
+  __TEXT.__objc_methlist: 0x1b0c
+  __TEXT.__const: 0x88
+  __TEXT.__gcc_except_tab: 0x1280
+  __TEXT.__cstring: 0x25d9
+  __TEXT.__oslogstring: 0x335e
+  __TEXT.__objc_classname: 0x28a
+  __TEXT.__objc_methname: 0x4ee3
+  __TEXT.__objc_methtype: 0xcd7
+  __TEXT.__unwind_info: 0x918
+  __DATA_CONST.__auth_got: 0x488
+  __DATA_CONST.__got: 0x70
+  __DATA_CONST.__const: 0xe08
+  __DATA_CONST.__cfstring: 0x1f40
+  __DATA_CONST.__objc_classlist: 0x108
   __DATA_CONST.__objc_protolist: 0x30
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_arraydata: 0xd8
-  __DATA_CONST.__objc_arrayobj: 0xa8
-  __DATA_CONST.__objc_intobj: 0x2e8
+  __DATA_CONST.__objc_protorefs: 0x10
+  __DATA_CONST.__objc_classrefs: 0x238
+  __DATA_CONST.__objc_superrefs: 0x80
+  __DATA_CONST.__objc_intobj: 0x4c8
+  __DATA_CONST.__objc_arraydata: 0x168
+  __DATA_CONST.__objc_arrayobj: 0xf0
   __DATA_CONST.__objc_dictobj: 0x28
-  __DATA.__objc_const: 0x2b88
-  __DATA.__objc_selrefs: 0x12d0
-  __DATA.__objc_protorefs: 0x10
-  __DATA.__objc_classrefs: 0x208
-  __DATA.__objc_superrefs: 0x70
-  __DATA.__objc_ivar: 0x1b8
-  __DATA.__objc_data: 0x870
+  __DATA.__objc_const: 0x3368
+  __DATA.__objc_selrefs: 0x1540
+  __DATA.__objc_ivar: 0x20c
+  __DATA.__objc_data: 0xa50
   __DATA.__data: 0x248
-  __DATA.__bss: 0xf0
+  __DATA.__bss: 0x148
   __DATA.__common: 0x1
   - /AppleInternal/Library/Frameworks/TapToRadarKit.framework/TapToRadarKit
   - /System/Library/Frameworks/Accounts.framework/Accounts

   - /usr/lib/libMobileGestalt.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 7BC71DFD-0019-3074-B2E2-425F720BC5E1
-  Functions: 854
-  Symbols:   193
-  CStrings:  1771
+  UUID: FECC6734-8521-3F5E-B49F-1C508D9F82C9
+  Functions: 975
+  Symbols:   207
+  CStrings:  2034
 
Symbols:
+ _CFArrayCreate
+ _FSEventStreamCreateRelativeToDevice
+ _FSEventStreamInvalidate
+ _FSEventStreamRelease
+ _FSEventStreamSetDispatchQueue
+ _FSEventStreamStart
+ _FSEventStreamStop
+ _FSEventsGetCurrentEventId
+ __os_feature_enabled_impl
+ _dispatch_queue_create
+ _kCFTypeArrayCallBacks
+ _memcpy
+ _objc_retain_x7
+ _os_transaction_create
CStrings:
+ "\x01"
+ "!"
+ "%"
+ "%@%d"
+ "%s: No LSApplicationRecord was found for app %@. Assuming invisible app by default."
+ "%s: merging writer %@ appPath with it's greater ancestor %@"
+ "%s: removing writer %@ from appPathList"
+ "%s:importing plist from %@"
+ "-[SAAppPath isAppUserVisible]"
+ "-[SAAppPathList MergeWritersAppPaths]_block_invoke"
+ "-[SAHelper importFromPlist:reply:]"
+ "/.activity"
+ "@\"NSObject<OS_os_transaction>\""
+ "@32@0:8Q16Q24"
+ "@44@0:8i16i20i24Q28Q36"
+ "@60@0:8@16@24@32@40B48B52B56"
+ "@64@0:8q16q24q32Q40Q48@56"
+ "ACCESS"
+ "APFSIOC_GET_VOLUME_ROLE returned %d (errno = %d)"
+ "App Sizer Deferred before SDA"
+ "App Sizer: Daily Activity"
+ "App Sizer: User Initiated"
+ "Bundle (%@) shared paths are invalid"
+ "Bundle (%@) unique paths are invalid"
+ "BundleID: %@, volType %u, urgency: %u, state %u"
+ "C52@0:8i16Q20@28Q36^@44"
+ "CLEAR_PURGEABILITY"
+ "END: Speculative Download Analytics"
+ "FAILED to log speculative download telemetry using AnalyticsSendEventLazy\n"
+ "FP_DISCARDED"
+ "FSEventStreamCreate:"
+ "FSEventStreamStart failed for %@"
+ "Failed to get application record for app %@ with error %@"
+ "HIGH"
+ "Histogram Begin:"
+ "Histogram End (%zu)."
+ "Incorrect event.urgency (%@), ignoring"
+ "Initial run. Set initial lastEventId and abort."
+ "Inside processEvents with %lu events"
+ "Inside processEvents with kFSEventStreamEventFlagHistoryDone"
+ "Invalid path (%@) - '~' is not resolved."
+ "Invalid path (%@) - the provided path is relative, must provide an absolute path."
+ "LAST"
+ "LOW"
+ "MAX"
+ "MED"
+ "MergeWritersAppPaths"
+ "Options"
+ "Path %@ is already claimed by another bundles-set"
+ "SAFSEEvent"
+ "SASpeculativeDownloadAnalytics"
+ "SDA: Send telemetry"
+ "SDAHistogramElement"
+ "SDAHistogramMatrix"
+ "SDAPerBundleHistogram"
+ "SDAState"
+ "SDTelStateKeysTranslationTable"
+ "SDTelUrgencyKeysTranslationTable"
+ "SDTelVolumeKeysTranslationTable"
+ "SOFTWARE_UPDATE"
+ "START: Speculative Download Analytics"
+ "SYSTEM_DISCARDED"
+ "SdaStateFilePath"
+ "Speculative Download is disabled"
+ "SpeculativeDownload"
+ "SpeculativeDownload.db"
+ "Start SDA for %@"
+ "T@\"NSMutableArray\",&,V_ageGroupCount"
+ "T@\"NSMutableArray\",&,V_perBundle"
+ "T@\"NSMutableArray\",&,V_sizeGroupCount"
+ "T@\"NSMutableDictionary\",&,V_histogram"
+ "T@\"NSNumber\",&,V__isUserVisible"
+ "T@\"NSObject<OS_os_transaction>\",&,V_scanOSTransaction"
+ "T@\"NSString\",&,V_SdaStateFilePath"
+ "T@\"NSString\",&,V_eventType"
+ "T@\"NSString\",&,V_pathToDisk"
+ "T@\"NSString\",?,R,C"
+ "TB,R,N"
+ "TQ,V_Options"
+ "TQ,V_dirstatKey"
+ "TQ,V_inode"
+ "TQ,V_lastEventId"
+ "TQ,V_purgeableATime"
+ "TQ,V_size"
+ "TQ,V_version"
+ "TYPE_DATA"
+ "TYPE_ENTERPRISE"
+ "TYPE_LAST"
+ "TYPE_USER"
+ "Ti,V_dev"
+ "Ti,V_urgency"
+ "Ti,V_useState"
+ "Tq,V_attributionTagID"
+ "Tq,V_dirStatKey"
+ "Tq,V_lastEventTime"
+ "UNKNOWN"
+ "USER_DISCARDED"
+ "\\!"
+ "_Options"
+ "_SdaStateFilePath"
+ "__isUserVisible"
+ "_ageGroupCount"
+ "_attributionTagID"
+ "_dev"
+ "_dirStatKey"
+ "_dirstatKey"
+ "_eventType"
+ "_histogram"
+ "_inode"
+ "_lastEventId"
+ "_lastEventTime"
+ "_pathToDisk"
+ "_perBundle"
+ "_purgeableATime"
+ "_scanOSTransaction"
+ "_size"
+ "_sizeGroupCount"
+ "_urgency"
+ "_useState"
+ "_version"
+ "addClonePathOfCloneID:FSId:dataSize:purgeableSize:dirStatKey:attributionTag:bundleSet:cloneData:"
+ "addPaths:ToBundleSets:"
+ "addWriterId:"
+ "adjAge:andSize:"
+ "age:  %@ %@ %@ %@ %@ %@ %@ %@"
+ "ageGroupCount"
+ "age_"
+ "analyzeVolPath:pathList:dirKeyCache:appSizerResults:"
+ "appPathWithRecords:identifier:dataContainerURL:personaUniqueString:isDataSeparated:isPlugin:isGroup:"
+ "appRecord"
+ "appsList"
+ "arrayWithCapacity:"
+ "attributionTag"
+ "attributionTagID"
+ "bundle set %@ for dir-stat key %llu contains multiple bundle ids. Taking %@"
+ "can't find dir for dir-key %llu"
+ "can't parse eventStr"
+ "can't read SDAState with %@"
+ "can't write to file %@"
+ "com.apple.fakeapp.Environments"
+ "com.apple.journal"
+ "com.apple.massStorage.spaceAttribution.speculativeDownloads"
+ "com.apple.spaceattributiond.appSizerScan"
+ "dev"
+ "dirStatKey"
+ "dirStatsKey"
+ "dirstatKey"
+ "disk_free_space"
+ "enumerateBundleHistogram:"
+ "evennt.dev (%llu) is not equal to fsid (%llu"
+ "eventType"
+ "forceHidden"
+ "forceVisible"
+ "fse que"
+ "getGreaterAncestorOfBundle:"
+ "getLSAppRecordForBundle:reply:"
+ "histogram"
+ "importFromPlist:reply:"
+ "initWithBundleRecords:identifier:dataContainerURL:personaUniqueString:isDataSeparated:isPlugin:isGroup:"
+ "initWithDataSize:cloneSize:purgeableSize:dirStatKey:attributionTag:clonePath:"
+ "initWithFSEventString:"
+ "inode"
+ "invalid eventString %@"
+ "isAppUserVisible"
+ "lastEventId"
+ "lastEventTime"
+ "lastSpeculativeDownloadSentTelemetryDate"
+ "loadFromDiskWithPathsResolving:"
+ "loadFromFileAtPath:"
+ "newElement"
+ "newWithAge:andSize:"
+ "newWithDataSize:cloneSize:purgeableSize:dirStatKey:attributionTag:clonePath:"
+ "newWithVolType:Urgency:state:age:size:"
+ "null event string for event number %llu"
+ "numberWithUnsignedInt:"
+ "perBundle"
+ "processCloneMapOnVol:withPathList:andDirKeyCache:collectClonesPaths:reply:"
+ "purgeableATime"
+ "purgeable_size"
+ "removeAppPath:"
+ "runAppSizerWithAsyncBlocksNum:withRunMode:withActivity:withScanOptions:error:"
+ "saveToFile"
+ "scanOSTransaction"
+ "sendTelemetry:withHistogramMatrix:"
+ "setAgeGroupCount:"
+ "setAttributionTagID:"
+ "setDev:"
+ "setDirStatKey:"
+ "setDirstatKey:"
+ "setEventType:"
+ "setHistogram:"
+ "setInode:"
+ "setLastEventId:"
+ "setLastEventTime:"
+ "setLastFSEventId:"
+ "setObject:atIndexedSubscript:"
+ "setOptions:"
+ "setPathToDisk:"
+ "setPerBundle:"
+ "setPurgeableATime:"
+ "setScanOSTransaction:"
+ "setSdaStateFilePath:"
+ "setSize:"
+ "setSizeGroupCount:"
+ "setSystemDataSize:"
+ "setTotalCDAvailable:"
+ "setTotalPurgeableClones:"
+ "setUrgency:"
+ "setUseState:"
+ "setVersion:"
+ "set_isUserVisible:"
+ "size"
+ "size: %@ %@ %@ %@ %@ %@ %@ %@"
+ "sizeGroupCount"
+ "size_"
+ "state"
+ "stringWithCString:encoding:"
+ "timeout processing fsEvents"
+ "totalCDAvailable"
+ "totalCDAvailable (%llu) is greater than device diskUsed (%llu)"
+ "totalPurgeableClones"
+ "totalPurgeableDataSize (%llu: totalCDAvailable(%llu) + purgeableClonesSize(%llu)) is greater than diskUsed (%llu). Ignoring totalPurgeableDataSize value"
+ "total_purgeable_size"
+ "total_size"
+ "updateTotalsInfo:totalPurgeable:"
+ "updateVolType:Urgency:state:age:size:"
+ "upsertBundleID:volType:urgency:state:age:size:"
+ "useState"
+ "v24@?0@\"NSError\"8@\"LSApplicationRecord\"16"
+ "v32@0:8@\"NSString\"16@?<v@?@\"NSError\">24"
+ "v32@?0@\"NSString\"8@\"SDAPerBundleHistogram\"16^B24"
+ "v32@?0@\"NSString\"8Q16^B24"
+ "v44@0:8i16i20i24Q28Q36"
+ "v44@?0@\"NSString\"8i16i20i24@\"SDAHistogramElement\"28^B36"
+ "v48@0:8@16@24@32@40"
+ "v52@0:8@16@24@32B40@?44"
+ "v52@0:8@16i24i28i32Q36Q44"
+ "v80@0:8Q16^{fsid=[2i]}24Q32Q40Q48Q56@64@72"
+ "validatePaths:"
+ "version"
+ "volume_role"
+ "writersBundles"
+ "~"
- "$"
- "%s: The provided SAAppPath's bundleID must be equal to the instance bundleId (%@)"
- "-[SAAppPath extendWithPropertiesFromAppPath:]"
- "@48@0:8q16q24q32@40"
- "@64@0:8@16@24@32@40B48B52B56B60"
- "Bundle %@ ParentBundle %@"
- "C56@0:8i16Q20@28Q36B44^@48"
- "Path %@ claimed by %@ already exists for bundles-set %@"
- "TB,N,V_isUserVisible"
- "\\"
- "addClonePathOfCloneID:FSId:dataSize:purgeableSize:bundleSet:cloneData:"
- "addSystemDataVolumeWithUsed:systemData:"
- "appPathWithRecords:identifier:dataContainerURL:personaUniqueString:isDataSeparated:isPlugin:isUserVisible:isGroup:"
- "getLSAppRecordForBundle:"
- "initWithBundleRecords:identifier:dataContainerURL:personaUniqueString:isDataSeparated:isPlugin:isUserVisible:isGroup:"
- "initWithDataSize:cloneSize:purgeableSize:clonePath:"
- "isAppUserVisible:"
- "isAppsSetUserVisible:"
- "newWithDataSize:cloneSize:purgeableSize:clonePath:"
- "processCloneMapOnVol:withPathList:collectClonesPaths:reply:"
- "runAppSizerWithAsyncBlocksNum:withRunMode:withActivity:withScanOptions:withSendTelemetry:error:"
- "setIsUserVisible:"
- "v44@0:8@16@24B32@?36"
- "v64@0:8Q16^{fsid=[2i]}24Q32Q40@48@56"

```
