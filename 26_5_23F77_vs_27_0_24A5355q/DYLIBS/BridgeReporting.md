## BridgeReporting

> `/System/Library/PrivateFrameworks/BridgeReporting.framework/BridgeReporting`

```diff

-1310.13.0.0.0
-  __TEXT.__text: 0x7e0c
-  __TEXT.__auth_stubs: 0x370
+1350.1.0.0.0
+  __TEXT.__text: 0x7008
   __TEXT.__objc_methlist: 0x9fc
   __TEXT.__const: 0xf8
-  __TEXT.__gcc_except_tab: 0xec
-  __TEXT.__cstring: 0x1083
+  __TEXT.__gcc_except_tab: 0xdc
+  __TEXT.__cstring: 0x1098
   __TEXT.__oslogstring: 0x648
-  __TEXT.__unwind_info: 0x320
-  __TEXT.__objc_classname: 0xf9
-  __TEXT.__objc_methname: 0x2108
-  __TEXT.__objc_methtype: 0x2d0
-  __TEXT.__objc_stubs: 0x15c0
-  __DATA_CONST.__got: 0x120
+  __TEXT.__unwind_info: 0x258
+  __TEXT.__objc_stubs: 0x0
+  __TEXT.__auth_stubs: 0x0
+  __TEXT.__objc_classname: 0x0
+  __TEXT.__objc_methname: 0x0
+  __TEXT.__objc_methtype: 0x0
   __DATA_CONST.__const: 0x6b8
   __DATA_CONST.__objc_classlist: 0x48
   __DATA_CONST.__objc_protolist: 0x10
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_selrefs: 0x7c8
   __DATA_CONST.__objc_superrefs: 0x30
-  __AUTH_CONST.__auth_got: 0x1c8
+  __DATA_CONST.__got: 0x120
   __AUTH_CONST.__const: 0xa0
   __AUTH_CONST.__cfstring: 0x1460
   __AUTH_CONST.__objc_const: 0x1130
   __AUTH_CONST.__objc_intobj: 0x90
+  __AUTH_CONST.__auth_got: 0x0
   __AUTH.__objc_data: 0x2d0
   __DATA.__objc_ivar: 0xd0
   __DATA.__data: 0xc0

   - /usr/lib/libMobileGestalt.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 3C3EF8A0-5F03-37C7-96DF-1B9DC5986E92
+  UUID: 91DFDF5A-9CAD-3B2D-AB5A-65F69D4B5871
   Functions: 225
-  Symbols:   994
-  CStrings:  808
+  Symbols:   999
+  CStrings:  390
 
Symbols:
+ _objc_claimAutoreleasedReturnValue
+ _objc_retain
+ _objc_retainAutoreleaseReturnValue
+ _objc_retain_x23
+ _objc_retain_x26
+ _objc_retain_x3
+ _objc_retain_x8
- _objc_retainAutoreleasedReturnValue
- _objc_retain_x28
Functions:
~ -[BRSetupControllerDetails setTimeStamp:] : 64 -> 12
~ -[BRSetupControllerDetails setControllerName:] : 64 -> 12
~ -[BRSetupControllerDetails setControllerOrder:] : 64 -> 12
~ -[BRSetupControllerTracker addSetupController:action:] : 212 -> 204
~ -[BRSetupControllerTracker lastPushedSetupController] : 216 -> 196
~ -[BRSetupControllerTracker setSetupControllers:] : 64 -> 12
~ -[BRSetupControllerTracker setHoldControllerDetails:] : 64 -> 12
~ -[BRRTCPairingReportManager initWithPairingBeginsType:] : 244 -> 240
~ -[BRRTCPairingReportManager _addEvent:withValue:withError:] : 548 -> 488
~ -[BRRTCPairingReportManager checkInWithOpenPairingTimeEvent:] : 252 -> 248
~ ___61-[BRRTCPairingReportManager checkInWithOpenPairingTimeEvent:]_block_invoke : 88 -> 84
~ -[BRRTCPairingReportManager checkInWithClosingPairingTimeEvent:] : 152 -> 148
~ ___64-[BRRTCPairingReportManager checkInWithClosingPairingTimeEvent:]_block_invoke : 672 -> 584
~ -[BRRTCPairingReportManager checkInWithController:action:] : 96 -> 92
~ -[BRRTCPairingReportManager checkInWithRUIController:] : 540 -> 448
~ -[BRRTCPairingReportManager recordSetupController:action:] : 212 -> 204
~ -[BRRTCPairingReportManager writeDeltasForSetupControllerActions:action:] : 804 -> 708
~ -[BRRTCPairingReportManager deltaForControllerAction:] : 160 -> 152
~ ___66-[BRRTCPairingReportManager writePushOrHoldToPairingPlist:action:]_block_invoke : 348 -> 328
~ -[BRRTCPairingReportManager _writeToPairingPlist:withValue:] : 732 -> 696
~ -[BRRTCPairingReportManager truncateSetupControllerClassName:] : 172 -> 168
~ -[BRRTCPairingReportManager _eventClearedForRecord:] : 416 -> 344
~ -[BRRTCPairingReportManager completePairingMetricWithSuccess:] : 196 -> 192
~ ___62-[BRRTCPairingReportManager completePairingMetricWithSuccess:]_block_invoke_2 : 200 -> 152
~ -[BRRTCPairingReportManager completeMetricForAppTermination] : 140 -> 136
~ ___60-[BRRTCPairingReportManager completeMetricForAppTermination]_block_invoke : 356 -> 308
~ ___60-[BRRTCPairingReportManager completeMetricForAppTermination]_block_invoke_2 : 376 -> 320
~ -[BRRTCPairingReportManager submitAnyPendingMetrics] : 228 -> 224
~ ___52-[BRRTCPairingReportManager submitAnyPendingMetrics]_block_invoke : 156 -> 152
~ -[BRRTCPairingReportManager setupPairingMetric:] : 316 -> 308
~ ___48-[BRRTCPairingReportManager setupPairingMetric:]_block_invoke_2 : 336 -> 288
~ -[BRRTCPairingReportManager addMetaKeys] : 464 -> 456
~ ___40-[BRRTCPairingReportManager addMetaKeys]_block_invoke : 316 -> 296
~ ___40-[BRRTCPairingReportManager addMetaKeys]_block_invoke_2 : 308 -> 292
~ -[BRRTCPairingReportManager createPairingReportPlistWithPairingType:] : 1084 -> 1032
~ -[BRRTCPairingReportManager cleanUpMetricDirectoryWithCompletion:] : 1172 -> 1136
~ ___66-[BRRTCPairingReportManager cleanUpMetricDirectoryWithCompletion:]_block_invoke : 272 -> 268
~ ___66-[BRRTCPairingReportManager cleanUpMetricDirectoryWithCompletion:]_block_invoke_3 : 272 -> 268
~ -[BRRTCPairingReportManager archivePairingMetric:withCompletion:] : 1100 -> 1068
~ -[BRRTCPairingReportManager combineMetricPlistsForArchive:] : 248 -> 228
~ -[BRRTCPairingReportManager completeRTCPairingMetricForMetricID:withSuccess:] : 460 -> 404
~ -[BRRTCPairingReportManager _addEventToPendingQueue:withValue:] : 452 -> 436
~ ___63-[BRRTCPairingReportManager _addEventToPendingQueue:withValue:]_block_invoke : 176 -> 168
~ -[BRRTCPairingReportManager addPendingEventToMetric] : 140 -> 136
~ ___52-[BRRTCPairingReportManager addPendingEventToMetric]_block_invoke : 360 -> 352
~ -[BRRTCPairingReportManager setPairingMetric:] : 64 -> 12
~ -[BRRTCPairingReportManager setOpenPairingTimeEvents:] : 64 -> 12
~ -[BRRTCPairingReportManager setSetupControllerTracker:] : 64 -> 12
~ -[BRRTCPairingReportManager setCurrentPairingMetricBridgePlistPath:] : 64 -> 12
~ -[BRRTCPairingReportManager setQueue:] : 64 -> 12
~ -[BRRTCPairingReportManager setPendingEvents:] : 64 -> 12
~ _BRGetCurrentMetricIDFromMetricDir : 404 -> 408
~ _BRGetAllMetricKeysAndValues : 572 -> 528
~ _BRStaleOrNoPairingMetric : 432 -> 396
~ _BRSignInPairingTimeEventForAccountType : 252 -> 248
~ _BRSignInFailureErrorForAccountType : 172 -> 168
~ _BRPairingTimeEventToString : 1036 -> 1024
~ +[BRRTCSession reportingSession] : 84 -> 68
~ +[BRRTCSession startRTCReportingSessionWithConfiguration:andComplection:] : 208 -> 220
~ ___73+[BRRTCSession startRTCReportingSessionWithConfiguration:andComplection:]_block_invoke : 276 -> 264
~ ___73+[BRRTCSession startRTCReportingSessionWithConfiguration:andComplection:]_block_invoke_2 : 228 -> 180
~ +[BRRTCSession _parentRTCReportingSession:] : 448 -> 436
~ ____utilityQueue_block_invoke : 108 -> 104
~ -[BRRTCPairingMetric dictionaryRepresentation] : 220 -> 204
~ -[BRRTCPairingMetric setMetricDict:] : 64 -> 12
~ _br_metriccollection_log : 84 -> 68
~ -[BRRTCMigrationReportManager initWithPairingID:] : 132 -> 140
~ -[BRRTCMigrationReportManager addTransactionPhase:withSuccess:withPairingID:] : 452 -> 380
~ -[BRRTCMigrationReportManager addDeviceDetails:] : 100 -> 96
~ -[BRRTCMigrationReportManager setIsAutomation:] : 84 -> 80
~ -[BRRTCMigrationReportManager setErrorCode:domain:description:] : 328 -> 276
~ -[BRRTCMigrationReportManager setMigrationFailedBTKeysNotSynced:] : 256 -> 204
~ -[BRRTCMigrationReportManager setMigrationDeviceUnpairedBecauseKeychainIsOff:] : 256 -> 204
~ -[BRRTCMigrationReportManager setMigrationDeviceUnpairedBecauseStale:] : 256 -> 204
~ -[BRRTCMigrationReportManager setMigrationDeviceUnpairedByUserAction:] : 256 -> 204
~ -[BRRTCMigrationReportManager setMigrationSucceeded:] : 256 -> 204
~ -[BRRTCMigrationReportManager setMigrationBegan:] : 144 -> 132
~ -[BRRTCMigrationReportManager setLastActiveDate:] : 108 -> 100
~ -[BRRTCMigrationReportManager setSessionID:] : 100 -> 96
~ -[BRRTCMigrationReportManager submitMetic] : 376 -> 304
~ -[BRRTCMigrationReportManager _transactionNameFromKey:] : 132 -> 124
~ -[BRRTCMigrationReportManager _likelyOffendingTransaction] : 468 -> 408
~ ___58-[BRRTCMigrationReportManager _likelyOffendingTransaction]_block_invoke : 228 -> 220
~ -[BRRTCMigrationReportManager formatDate:] : 152 -> 148
~ -[BRRTCMigrationReportManager setMigrationMetric:] : 64 -> 12
~ -[BRReportManager initWithCategory:] : 260 -> 208
~ -[BRReportManager reportRTCMetric:] : 732 -> 716
~ ___35-[BRReportManager reportRTCMetric:]_block_invoke : 300 -> 252
~ -[BRReportManager categortyToConfiguration:] : 248 -> 236
~ -[BRRTCMigrationMetricDeviceDetails dictionaryOfMetricKeysWithRecordedValues] : 684 -> 620
~ -[BRRTCMigrationMetricDeviceDetails setGizmoBuild:] : 64 -> 12
~ -[BRRTCMigrationMetricDeviceDetails setGizmoHardware:] : 64 -> 12
~ -[BRRTCMigrationMetricDeviceDetails setGizmoBuildType:] : 64 -> 12
~ -[BRRTCMigrationMetricDeviceDetails setPairedDeviceCount:] : 64 -> 12
~ -[BRRTCMigrationMetricDeviceDetails setGizmoMaxPairingVersion:] : 64 -> 12
~ -[BRRTCMigrationMetricDeviceDetails setGizmoEnclosureMaterial:] : 64 -> 12
~ -[BRRTCMigrationMetricDeviceDetails setSwitchCounter:] : 64 -> 12
~ -[BRRTCMigrationMetricDeviceDetails setMigratingDeviceId:] : 64 -> 12
~ -[BRRTCMigrationMetric dictionaryRepresentation] : 756 -> 728
~ -[BRRTCMigrationMetric setMigrationBeganTime:] : 64 -> 12
~ -[BRRTCMigrationMetric setSessionID:] : 64 -> 12
~ -[BRRTCMigrationMetric setDeviceDetails:] : 64 -> 12
~ -[BRRTCMigrationMetric setTransactionPhases:] : 64 -> 12
~ -[BRRTCMigrationMetric setMigrationFailureCode:] : 64 -> 12
~ -[BRRTCMigrationMetric setMigrationFailureDescription:] : 64 -> 12
~ -[BRRTCMigrationMetric setMigrationFailureDomain:] : 64 -> 12
~ -[BRRTCMigrationMetric setSuspectTransaction:] : 64 -> 12
~ -[BRRTCMigrationMetric setLastActiveDate:] : 64 -> 12
CStrings:
- "#16@0:8"
- ".cxx_destruct"
- "@\"BRRTCMigrationMetric\""
- "@\"BRRTCMigrationMetricDeviceDetails\""
- "@\"BRRTCPairingMetric\""
- "@\"BRRTCPairingReportManager\""
- "@\"BRSetupControllerDetails\""
- "@\"BRSetupControllerTracker\""
- "@\"NSDictionary\"16@0:8"
- "@\"NSMutableArray\""
- "@\"NSMutableDictionary\""
- "@\"NSNumber\""
- "@\"NSObject<OS_dispatch_queue>\""
- "@\"NSString\""
- "@\"NSString\"16@0:8"
- "@\"NSURL\""
- "@\"NSUUID\""
- "@16@0:8"
- "@20@0:8S16"
- "@24@0:8:16"
- "@24@0:8@16"
- "@24@0:8Q16"
- "@32@0:8:16@24"
- "@40@0:8:16@24@32"
- "@?"
- "@?16@0:8"
- "B"
- "B16@0:8"
- "B24@0:8#16"
- "B24@0:8:16"
- "B24@0:8@\"Protocol\"16"
- "B24@0:8@16"
- "B24@0:8Q16"
- "BRRTCMetric"
- "BRRTCMigrationMetric"
- "BRRTCMigrationMetricDeviceDetails"
- "BRRTCMigrationReportManager"
- "BRRTCPairingMetric"
- "BRRTCPairingReportManager"
- "BRRTCSession"
- "BRReportManager"
- "BRSetupControllerDetails"
- "BRSetupControllerTracker"
- "NSObject"
- "Q"
- "Q16@0:8"
- "S16@0:8"
- "T#,R"
- "T@\"BRRTCMigrationMetric\",&,N,V_migrationMetric"
- "T@\"BRRTCMigrationMetricDeviceDetails\",&,N,V_deviceDetails"
- "T@\"BRRTCPairingMetric\",&,N,V_pairingMetric"
- "T@\"BRRTCPairingReportManager\",W,N,V_pairingReportManager"
- "T@\"BRSetupControllerDetails\",&,N,V_holdControllerDetails"
- "T@\"BRSetupControllerTracker\",&,N,V_setupControllerTracker"
- "T@\"NSMutableArray\",&,N,V_pendingEvents"
- "T@\"NSMutableArray\",&,N,V_setupControllers"
- "T@\"NSMutableDictionary\",&,N,V_metricDict"
- "T@\"NSMutableDictionary\",&,N,V_openPairingTimeEvents"
- "T@\"NSMutableDictionary\",&,N,V_transactionPhases"
- "T@\"NSNumber\",&,N,V_controllerOrder"
- "T@\"NSNumber\",&,N,V_gizmoEnclosureMaterial"
- "T@\"NSNumber\",&,N,V_gizmoMaxPairingVersion"
- "T@\"NSNumber\",&,N,V_migratingDeviceId"
- "T@\"NSNumber\",&,N,V_migrationFailureCode"
- "T@\"NSNumber\",&,N,V_pairedDeviceCount"
- "T@\"NSNumber\",&,N,V_switchCounter"
- "T@\"NSNumber\",&,N,V_timeStamp"
- "T@\"NSNumber\",N,V_subreasonCode"
- "T@\"NSObject<OS_dispatch_queue>\",&,N,V_queue"
- "T@\"NSString\",&,N,V_controllerName"
- "T@\"NSString\",&,N,V_gizmoBuild"
- "T@\"NSString\",&,N,V_gizmoBuildType"
- "T@\"NSString\",&,N,V_gizmoHardware"
- "T@\"NSString\",&,N,V_lastActiveDate"
- "T@\"NSString\",&,N,V_migrationBeganTime"
- "T@\"NSString\",&,N,V_migrationFailureDescription"
- "T@\"NSString\",&,N,V_migrationFailureDomain"
- "T@\"NSString\",&,N,V_sessionID"
- "T@\"NSString\",&,N,V_suspectTransaction"
- "T@\"NSString\",?,R,C"
- "T@\"NSString\",C,N,V_configuration"
- "T@\"NSString\",R,C"
- "T@\"NSString\",W,N,V_currentPairingMetricID"
- "T@\"NSURL\",&,N,V_currentPairingMetricBridgePlistPath"
- "T@\"NSUUID\",R,N,V_pairingID"
- "T@?,C,N,V_archivePairingMetric"
- "T@?,C,N,V_pendingMetricSubmission"
- "TB,N,V_isAutomation"
- "TB,N,V_metricBusy"
- "TB,N,V_metricSubmitted"
- "TB,N,V_migrationBegan"
- "TB,N,V_migrationDeviceUnpairedBecauseKeychainIsOff"
- "TB,N,V_migrationDeviceUnpairedBecauseStale"
- "TB,N,V_migrationDeviceUnpairedByUserAction"
- "TB,N,V_migrationFailedBTKeysNotSynced"
- "TB,N,V_migrationSucceeded"
- "TB,N,V_pairingMetricSetup"
- "TB,N,V_pairingReportUnderway"
- "TQ,N,V_pairingBeginsType"
- "TQ,R"
- "TS,N"
- "TS,N,V_category"
- "TS,N,V_rtcType"
- "URLByAppendingPathComponent:"
- "UUIDString"
- "Vv16@0:8"
- "^{_NSZone=}16@0:8"
- "_addEvent:withValue:withError:"
- "_addEventToPendingQueue:withValue:"
- "_archivePairingMetric"
- "_category"
- "_cleanupAfterWrite"
- "_configuration"
- "_controllerName"
- "_controllerOrder"
- "_currentPairingMetricBridgePlistPath"
- "_currentPairingMetricID"
- "_deviceDetails"
- "_eventClearedForRecord:"
- "_gizmoBuild"
- "_gizmoBuildType"
- "_gizmoEnclosureMaterial"
- "_gizmoHardware"
- "_gizmoMaxPairingVersion"
- "_holdControllerDetails"
- "_isAutomation"
- "_lastActiveDate"
- "_likelyOffendingTransaction"
- "_metricBusy"
- "_metricDict"
- "_metricSubmitted"
- "_migratingDeviceId"
- "_migrationBegan"
- "_migrationBeganTime"
- "_migrationDeviceUnpairedBecauseKeychainIsOff"
- "_migrationDeviceUnpairedBecauseStale"
- "_migrationDeviceUnpairedByUserAction"
- "_migrationFailedBTKeysNotSynced"
- "_migrationFailureCode"
- "_migrationFailureDescription"
- "_migrationFailureDomain"
- "_migrationMetric"
- "_migrationSucceeded"
- "_openPairingTimeEvents"
- "_pairedDeviceCount"
- "_pairingBeginsType"
- "_pairingID"
- "_pairingMetric"
- "_pairingMetricSetup"
- "_pairingReportManager"
- "_pairingReportUnderway"
- "_parentRTCReportingSession:"
- "_pendingEvents"
- "_pendingMetricSubmission"
- "_queue"
- "_rtcType"
- "_sessionID"
- "_setupControllerTracker"
- "_setupControllers"
- "_subreasonCode"
- "_suspectTransaction"
- "_switchCounter"
- "_timeStamp"
- "_transactionNameFromKey:"
- "_transactionPhases"
- "_trimPrecision:"
- "_writeToPairingPlist:withValue:"
- "absoluteString"
- "addDeviceDetails:"
- "addEntriesFromDictionary:"
- "addMetaKeys"
- "addObject:"
- "addPairingTimeEventStringToPairingReportPlist:withValue:withError:"
- "addPairingTimeEventToMetricDict:withValue:"
- "addPairingTimeEventToPairingReportPlist:withValue:withError:"
- "addPairingTimePerformanceEventToMetricDict:withTime:"
- "addPendingEventToMetric"
- "addSetupController:action:"
- "addTransactionPhase:withSuccess:withPairingID:"
- "allValues"
- "archivePairingMetric"
- "archivePairingMetric:withCompletion:"
- "arrayWithObjects:count:"
- "autorelease"
- "boolValue"
- "categortyToConfiguration:"
- "category"
- "checkInWithClosingPairingTimeEvent:"
- "checkInWithController:action:"
- "checkInWithOpenPairingTimeEvent:"
- "checkInWithRUIController:"
- "class"
- "cleanUpMetricDirectoryWithCompletion:"
- "clearControllerHold"
- "clearPendingEventQueue"
- "combineMetricPlistsForArchive:"
- "completeMetricForAppTermination"
- "completePairingMetricWithSuccess:"
- "completeRTCPairingMetricForMetricID:withSuccess:"
- "configuration"
- "conformsToProtocol:"
- "containsString:"
- "contentsOfDirectoryAtPath:error:"
- "controllerName"
- "controllerOrder"
- "count"
- "countByEnumeratingWithState:objects:count:"
- "createDirectoryAtPath:withIntermediateDirectories:attributes:error:"
- "createPairingReportPlistWithPairingType:"
- "currentPairingMetricBridgePlistPath"
- "currentPairingMetricID"
- "date"
- "debugDescription"
- "defaultCenter"
- "defaultManager"
- "deltaForControllerAction:"
- "description"
- "deviceDetails"
- "dictionaryOfMetricKeysWithRecordedValues"
- "dictionaryRepresentation"
- "dictionaryWithContentsOfURL:"
- "dictionaryWithObjects:forKeys:count:"
- "doubleValue"
- "enumerateKeysAndObjectsUsingBlock:"
- "errorWithDomain:code:userInfo:"
- "fileExistsAtPath:"
- "fileURLWithPath:"
- "flagForAutomation"
- "formatDate:"
- "getAllDevicesWithArchivedAltAccountDevicesMatching:"
- "gizmoBuild"
- "gizmoBuildType"
- "gizmoEnclosureMaterial"
- "gizmoHardware"
- "gizmoMaxPairingVersion"
- "hash"
- "holdControllerDetails"
- "host"
- "init"
- "initWithCategory:"
- "initWithObjects:"
- "initWithPairingBeginsType:"
- "initWithPairingID:"
- "initWithSessionInfo:userInfo:frameworksToCheck:"
- "initWithUUIDString:"
- "initializeEndToEndMetric"
- "intValue"
- "integerValue"
- "isAutomation"
- "isEqual:"
- "isEqualToNumber:"
- "isEqualToString:"
- "isKindOfClass:"
- "isMemberOfClass:"
- "isProxy"
- "lastActiveDate"
- "lastObject"
- "lastPushedSetupController"
- "length"
- "metricBusy"
- "metricDict"
- "metricSubmitted"
- "migratingDeviceId"
- "migrationBegan"
- "migrationBeganTime"
- "migrationDeviceUnpairedBecauseKeychainIsOff"
- "migrationDeviceUnpairedBecauseStale"
- "migrationDeviceUnpairedByUserAction"
- "migrationFailedBTKeysNotSynced"
- "migrationFailureCode"
- "migrationFailureDescription"
- "migrationFailureDomain"
- "migrationMetric"
- "migrationSucceeded"
- "moveItemAtURL:toURL:error:"
- "numberWithBool:"
- "numberWithDouble:"
- "numberWithInt:"
- "numberWithInteger:"
- "numberWithLong:"
- "numberWithUnsignedInteger:"
- "numberWithUnsignedShort:"
- "objectAtIndex:"
- "objectForKey:"
- "objectForKeyedSubscript:"
- "objectModel"
- "openPairingTimeEvents"
- "pageElement"
- "pairedDeviceCount"
- "pairingBeginsType"
- "pairingID"
- "pairingMetric"
- "pairingMetricSetup"
- "pairingReportManager"
- "pairingReportUnderway"
- "path"
- "pathWithComponents:"
- "pendingEvents"
- "pendingMetricSubmission"
- "performSelector:"
- "performSelector:withObject:"
- "performSelector:withObject:withObject:"
- "postNotificationName:object:userInfo:"
- "queue"
- "recordSetupController:action:"
- "relativePath"
- "release"
- "removeItemAtURL:error:"
- "removeObjectForKey:"
- "reportRTCMetric:"
- "reporterWithCatergory:"
- "reportingSession"
- "respondsToSelector:"
- "retain"
- "retainCount"
- "retrieveMigrationMetric"
- "rtcType"
- "self"
- "sendMessageWithCategory:type:payload:error:"
- "sessionID"
- "setArchivePairingMetric:"
- "setCategory:"
- "setConfiguration:"
- "setControllerName:"
- "setControllerOrder:"
- "setCurrentPairingMetricBridgePlistPath:"
- "setCurrentPairingMetricID:"
- "setDateFormat:"
- "setDeviceDetails:"
- "setErrorCode:domain:description:"
- "setGizmoBuild:"
- "setGizmoBuildType:"
- "setGizmoEnclosureMaterial:"
- "setGizmoHardware:"
- "setGizmoMaxPairingVersion:"
- "setHoldControllerDetails:"
- "setIsAutomation:"
- "setLastActiveDate:"
- "setMetricBusy:"
- "setMetricDict:"
- "setMetricSubmitted:"
- "setMigratingDeviceId:"
- "setMigrationBegan:"
- "setMigrationBeganTime:"
- "setMigrationDeviceUnpairedBecauseKeychainIsOff:"
- "setMigrationDeviceUnpairedBecauseStale:"
- "setMigrationDeviceUnpairedByUserAction:"
- "setMigrationFailedBTKeysNotSynced:"
- "setMigrationFailureCode:"
- "setMigrationFailureDescription:"
- "setMigrationFailureDomain:"
- "setMigrationMetric:"
- "setMigrationSucceeded:"
- "setObject:forKey:"
- "setOpenPairingTimeEvents:"
- "setPairedDeviceCount:"
- "setPairingBeginsType:"
- "setPairingMetric:"
- "setPairingMetricSetup:"
- "setPairingReportManager:"
- "setPairingReportUnderway:"
- "setPendingEvents:"
- "setPendingMetricSubmission:"
- "setQueue:"
- "setRtcType:"
- "setSessionID:"
- "setSetupControllerTracker:"
- "setSetupControllers:"
- "setSubreasonCode:"
- "setSuspectTransaction:"
- "setSwitchCounter:"
- "setTimeStamp:"
- "setTransactionPhases:"
- "setValue:forKey:"
- "setupControllerTracker"
- "setupControllers"
- "setupPairingMetric:"
- "sharedInstance"
- "sourceURL"
- "startConfigurationWithCompletionHandler:"
- "startRTCReportingSessionWithConfiguration:andComplection:"
- "stringByReplacingOccurrencesOfString:withString:"
- "stringFromDate:"
- "stringWithFormat:"
- "submitAnyPendingMetrics"
- "submitMetic"
- "subreasonCode"
- "substringFromIndex:"
- "substringToIndex:"
- "superclass"
- "suspectTransaction"
- "switchCounter"
- "timeStamp"
- "title"
- "transactionPhases"
- "truncateSetupControllerClassName:"
- "unsignedIntegerValue"
- "v16@0:8"
- "v20@0:8B16"
- "v20@0:8S16"
- "v24@0:8@16"
- "v24@0:8@?16"
- "v24@0:8Q16"
- "v32@0:8@16@24"
- "v32@0:8@16@?24"
- "v32@0:8@16Q24"
- "v32@0:8Q16@24"
- "v36@0:8@16B24@28"
- "v40@0:8@16@24@32"
- "v40@0:8Q16@24@32"
- "valueForProperty:"
- "writeDeltasForSetupControllerActions:action:"
- "writePushOrHoldToPairingPlist:action:"
- "writeToFile:atomically:"
- "writeToURL:atomically:"
- "writeToURL:error:"
- "zone"

```
