## FileProviderDaemon

> `/System/Library/PrivateFrameworks/FileProviderDaemon.framework/FileProviderDaemon`

```diff

-2732.42.1.0.0
-  __TEXT.__text: 0xcca28
-  __TEXT.__auth_stubs: 0x11e0
-  __TEXT.__objc_methlist: 0x5350
+2732.60.87.502.1
+  __TEXT.__text: 0xceea0
+  __TEXT.__auth_stubs: 0x11f0
+  __TEXT.__objc_methlist: 0x5488
   __TEXT.__const: 0x1f8
-  __TEXT.__cstring: 0xcd62
-  __TEXT.__oslogstring: 0xde1a
-  __TEXT.__gcc_except_tab: 0xd250
-  __TEXT.__ustring: 0x1972
+  __TEXT.__cstring: 0xcf6e
+  __TEXT.__oslogstring: 0xdfad
+  __TEXT.__gcc_except_tab: 0xd35c
+  __TEXT.__ustring: 0x1922
   __TEXT.__dlopen_cstrs: 0x50
-  __TEXT.__unwind_info: 0x3938
-  __TEXT.__objc_classname: 0xa2d
-  __TEXT.__objc_methname: 0x1549a
-  __TEXT.__objc_methtype: 0x53b5
-  __TEXT.__objc_stubs: 0xdea0
-  __DATA_CONST.__got: 0x810
-  __DATA_CONST.__const: 0x3990
-  __DATA_CONST.__objc_classlist: 0x258
+  __TEXT.__unwind_info: 0x39c0
+  __TEXT.__objc_classname: 0xa71
+  __TEXT.__objc_methname: 0x159a2
+  __TEXT.__objc_methtype: 0x547b
+  __TEXT.__objc_stubs: 0xe300
+  __DATA_CONST.__got: 0x828
+  __DATA_CONST.__const: 0x39e0
+  __DATA_CONST.__objc_classlist: 0x268
   __DATA_CONST.__objc_catlist: 0x30
-  __DATA_CONST.__objc_protolist: 0x138
+  __DATA_CONST.__objc_protolist: 0x140
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x4288
+  __DATA_CONST.__objc_selrefs: 0x43c8
   __DATA_CONST.__objc_protorefs: 0x38
-  __DATA_CONST.__objc_superrefs: 0x1f0
+  __DATA_CONST.__objc_superrefs: 0x208
   __DATA_CONST.__objc_arraydata: 0xc8
-  __AUTH_CONST.__auth_got: 0x900
+  __AUTH_CONST.__auth_got: 0x908
   __AUTH_CONST.__auth_ptr: 0x8
-  __AUTH_CONST.__const: 0xa00
-  __AUTH_CONST.__cfstring: 0x5c40
-  __AUTH_CONST.__objc_const: 0x12330
+  __AUTH_CONST.__const: 0xa40
+  __AUTH_CONST.__cfstring: 0x5e20
+  __AUTH_CONST.__objc_const: 0x12600
   __AUTH_CONST.__objc_arrayobj: 0x90
-  __AUTH_CONST.__objc_intobj: 0xc0
+  __AUTH_CONST.__objc_intobj: 0xf0
   __AUTH_CONST.__objc_dictobj: 0x50
-  __AUTH.__objc_data: 0x9b0
-  __DATA.__objc_ivar: 0x944
-  __DATA.__data: 0xeb0
-  __DATA.__bss: 0xd0
+  __AUTH.__objc_data: 0xa50
+  __DATA.__objc_ivar: 0x950
+  __DATA.__data: 0xf10
+  __DATA.__bss: 0xe8
   __DATA_DIRTY.__objc_data: 0xdc0
   __DATA_DIRTY.__data: 0x8
   __DATA_DIRTY.__bss: 0x140

   - /System/Library/PrivateFrameworks/CacheDelete.framework/CacheDelete
   - /System/Library/PrivateFrameworks/CrashReporterSupport.framework/CrashReporterSupport
   - /System/Library/PrivateFrameworks/DuetActivityScheduler.framework/DuetActivityScheduler
+  - /System/Library/PrivateFrameworks/EmojiFoundation.framework/EmojiFoundation
   - /System/Library/PrivateFrameworks/FileProviderTelemetry.framework/FileProviderTelemetry
   - /System/Library/PrivateFrameworks/GenerationalStorage.framework/GenerationalStorage
   - /System/Library/PrivateFrameworks/IconServices.framework/IconServices

   - /usr/lib/libbsm.0.dylib
   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libprequelite.dylib
-  Functions: 3496
-  Symbols:   4380
-  CStrings:  5906
+  Functions: 3533
+  Symbols:   4423
+  CStrings:  5983
 
Symbols:
+ _FPIgnoresForcedKeyChecks
+ _FPStatVFS
+ _NSFileProviderErrorDomainDisconnectionStateKey
+ _OBJC_CLASS_$_FPDTapToRadarManager
+ _OBJC_CLASS_$_NSCalendar
+ _OBJC_CLASS_$_NSJSONSerialization
+ _OBJC_METACLASS_$_FPDTapToRadarManager
- _OBJC_CLASS_$_FPFSTapToRadarManager
- _statfs
CStrings:
+ "-[FPDDeadEndExtensionSession init]"
+ "-[FPDXPCServicer dumpTelemetryTo:providerFilter:completionHandler:]"
+ "-[FPDXPCServicer dumpTelemetryTo:providerFilter:completionHandler:]_block_invoke"
+ "All"
+ "FPCKOnDemandUpdateReceiver"
+ "FPCKUpdateReceiving"
+ "FPDTapToRadarManager"
+ "Failed to adopt persona"
+ "Failed to adopt persona %!@(MISSING) for role %!d(MISSING)\nError: %!@(MISSING)"
+ "FileProvider"
+ "ManagementAllowsKnownFolderSyncing"
+ "ManagementKnownFolderSyncingAllowList"
+ "ORGANIZATION_DISALLOWS_KNOWN_FOLDER_OPERATION"
+ "RadarComponent"
+ "RadarDraft"
+ "T@\"NSError\",R,C,N"
+ "TapToRadarService"
+ "[DEBUG] 📡  Creating a radar draft request"
+ "[DEBUG] 📡  Not internal build, ignoring tap to radar request"
+ "[DEBUG] 📡  Tap to radar returned successfuly"
+ "[DEBUG] 🧹 No backend for sendTTRForItemIDs"
+ "[ERROR] Failed adopting %!@(MISSING) for role %!d(MISSING) but generation changed in-between, bailing out"
+ "[ERROR] Management Disallows claiming known folders %!@(MISSING) by %!{(MISSING)public}@ for %!{(MISSING)public}@"
+ "[ERROR] Unable to getattrlist for enterprise path '%!{(MISSING)public}@': %!{(MISSING)errno}d"
+ "[INFO] 🧹 Saving FPCK report"
+ "[INFO] 🧹 Update recevier received a telemetry update: %!@(MISSING)"
+ "[WARNING] 📡  Tap to radar returned error: (%!@(MISSING))"
+ "_backend"
+ "_domainsWithFilter:"
+ "_executionQueue"
+ "_replaceFPCKTelemetryValuesInTelemetryReport:"
+ "a problem bringing up a domain occured"
+ "com.apple.fileprovider.ttr-queue"
+ "components:fromDate:toDate:options:"
+ "createDraft:forProcessNamed:withDisplayReason:completionHandler:"
+ "currentCalendar"
+ "dataWithJSONObject:options:error:"
+ "day"
+ "disconnection_state"
+ "dumpPlistTelemetryForProviders:result:providerFilter:completionHandler:"
+ "dumpTelemetryTo:providerFilter:completionHandler:"
+ "enabled"
+ "errorReflectingDisconnectionState"
+ "fetchFPCKTelemetryWithCompletionHandler:"
+ "fetchTelemetryReportForAllDomains:resultDictionary:completionHandler:"
+ "fetchTelemetryReportWithCompletionHandler:"
+ "fetchTelemetryReportWithProviderFilter:completionHandler:"
+ "fp_disallowedByManagement:"
+ "initWithData:encoding:"
+ "initWithDictionary:"
+ "initWithDomainBackend:"
+ "initWithError:"
+ "initWithInteger:"
+ "initWithName:version:identifier:"
+ "initWithTimeIntervalSince1970:"
+ "isDisallowedByOrganization"
+ "isKnownFolderSyncingAllowedByManagement"
+ "postMultipleReports:type:userinfo:session:observer:"
+ "prettyNameForNsDomain:provider:"
+ "put:"
+ "reportAge"
+ "requestTapToRadarWithTitle:description:componentName:componentVersion:componentID:keywords:attachments:displayReason:"
+ "saveCheckpointWithReport:"
+ "saveFPCKTelemetryReport:completionHandler:"
+ "scheduleFPCKRun:domainUserInfo:domainRootURL:databaseBackupPath:urls:volumeRole:options:reason:fpfs:iCDPackageDetection:launchType:updateReceiver:shouldPause:proxy:completionHandler:"
+ "sendTTRForItemIDs:"
+ "setAttachments:"
+ "setAutoDiagnostics:"
+ "setClassification:"
+ "setComponent:"
+ "setDeleteOnAttach:"
+ "setKeywords:"
+ "setProblemDescription:"
+ "setReproducibility:"
+ "setTitle:"
+ "shared"
+ "shouldPauseWithCompletion:"
+ "shouldn't be called"
+ "startTime"
+ "stringArrayForKey:"
+ "v24@0:8@\"FPCKTelemetryUpdate\"16"
+ "v24@0:8@?<v@?@\"NSDictionary\"@\"NSError\">16"
+ "v32@0:8@\"NSDictionary\"16@?<v@?@\"NSError\">24"
+ "v40@0:8@\"NSFileHandle\"16@\"NSString\"24@?<v@?@\"NSError\">32"
+ "v56@0:8@16@24@32@40@48"
+ "v80@0:8@16@24@32@40q48@56@64@72"
- "-[FPDVolume _computeKnownPathsForRole:]_block_invoke"
- "[ERROR] FPDRTCReportingSession Failed to start"
- "[ERROR] FPDRTCReportingSession failed to flush messages : %!{(MISSING)public}@"
- "[ERROR] Unable to statfs for enterprise path '%!{(MISSING)public}@': %!{(MISSING)errno}d"
- "flushMessagesSynchronouslyWithError:"
- "scheduleFPCKRun:domainUserInfo:domainRootURL:databaseBackupPath:urls:volumeRole:options:reason:fpfs:iCDPackageDetection:launchType:pauseChecker:shouldPause:proxy:completionHandler:"
- "sessionWithCommonProperties:"
- "telemetryReportWithCompletionHandler:"
- "v24@0:8@?<v@?@\"NSDictionary\">16"

```
