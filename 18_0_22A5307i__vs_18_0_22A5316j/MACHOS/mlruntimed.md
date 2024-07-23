## mlruntimed

> `/usr/libexec/mlruntimed`

```diff

-107.0.0.0.0
-  __TEXT.__text: 0x1385c
-  __TEXT.__auth_stubs: 0x780
-  __TEXT.__objc_stubs: 0x2a40
-  __TEXT.__objc_methlist: 0xc58
-  __TEXT.__const: 0xc8
-  __TEXT.__oslogstring: 0x1517
-  __TEXT.__cstring: 0xbf5
-  __TEXT.__objc_classname: 0x2d4
-  __TEXT.__objc_methname: 0x2fa6
-  __TEXT.__objc_methtype: 0xd28
-  __TEXT.__gcc_except_tab: 0x1ac
+108.0.0.0.0
+  __TEXT.__text: 0xc464
+  __TEXT.__auth_stubs: 0x6f0
+  __TEXT.__objc_stubs: 0x1de0
+  __TEXT.__objc_methlist: 0x9d0
+  __TEXT.__const: 0xa8
+  __TEXT.__oslogstring: 0xcb0
+  __TEXT.__cstring: 0x702
+  __TEXT.__objc_classname: 0x287
+  __TEXT.__objc_methname: 0x227c
+  __TEXT.__objc_methtype: 0xb05
+  __TEXT.__gcc_except_tab: 0x174
   __TEXT.__info_plist: 0x63f
-  __TEXT.__unwind_info: 0x548
-  __DATA_CONST.__auth_got: 0x3d0
-  __DATA_CONST.__got: 0x2b8
-  __DATA_CONST.__const: 0xa00
-  __DATA_CONST.__cfstring: 0x880
-  __DATA_CONST.__objc_classlist: 0x98
+  __TEXT.__unwind_info: 0x3f8
+  __DATA_CONST.__auth_got: 0x388
+  __DATA_CONST.__got: 0x240
+  __DATA_CONST.__const: 0x5c8
+  __DATA_CONST.__cfstring: 0x500
+  __DATA_CONST.__objc_classlist: 0x80
   __DATA_CONST.__objc_catlist: 0x10
   __DATA_CONST.__objc_protolist: 0x58
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_protorefs: 0x10
-  __DATA_CONST.__objc_superrefs: 0x78
-  __DATA.__objc_const: 0x29d0
-  __DATA.__objc_selrefs: 0xb88
-  __DATA.__objc_ivar: 0x164
-  __DATA.__objc_data: 0x5f0
+  __DATA_CONST.__objc_superrefs: 0x60
+  __DATA.__objc_const: 0x2370
+  __DATA.__objc_selrefs: 0x870
+  __DATA.__objc_ivar: 0x114
+  __DATA.__objc_data: 0x500
   __DATA.__data: 0x420
-  __DATA.__bss: 0x38
+  __DATA.__bss: 0x28
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/Foundation.framework/Foundation
   - /System/Library/PrivateFrameworks/CoreAnalytics.framework/CoreAnalytics

   - /System/Library/PrivateFrameworks/TrialProto.framework/TrialProto
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 426
-  Symbols:   218
-  CStrings:  881
+  Functions: 304
+  Symbols:   194
+  CStrings:  647
 
Symbols:
+ _DESLogAndReturnSunsetError
+ _objc_retain_x6
- _DESGetDeviceType
- _DESGetOSVersion
- _NSInternalInconsistencyException
- _NSLocalizedFailureReasonErrorKey
- _OBJC_CLASS_$_DESBundlePluginManager
- _OBJC_CLASS_$_DESDodMLServer
- _OBJC_CLASS_$_DESDodMLTaskSchedulingPolicy
- _OBJC_CLASS_$_DESInternalDodMLTask
- _OBJC_CLASS_$_DESInternalDodMLTaskResult
- _OBJC_CLASS_$_DESRecipe
- _OBJC_CLASS_$_DESRecordSet
- _OBJC_CLASS_$_DESUploadTransport
- _OBJC_CLASS_$_NSBundle
- _OBJC_CLASS_$_NSSet
- _OBJC_CLASS_$_NSURL
- _OBJC_CLASS_$_NSUUID
- _OBJC_CLASS_$_NSUserDefaults
- _RecordInfoForUUID
- __os_signpost_emit_with_name_impl
- _abort
- _arc4random
- _objc_retain_x28
- _objc_retain_x5
- _objc_retain_x9
- _os_signpost_enabled
- _os_signpost_id_generate
CStrings:
+ "%!@(MISSING)"
- "\x03\x11\x16"
- "\x05"
- "%!@(MISSING)\n%!@(MISSING)"
- "%!@(MISSING) returns result=%!@(MISSING), resultCarrier=%!@(MISSING)."
- "%!@(MISSING)(%!@(MISSING), %!l(MISSING)d, %!f(MISSING), %!@(MISSING), %!@(MISSING), %!@(MISSING))"
- "%!s(MISSING) die roll for recipeID=%!@(MISSING), matchingRecordSet=%!@(MISSING)"
- "-"
- "@\"DESDodMLServer\""
- "@\"DESDodMLTaskSchedulingPolicy\""
- "@\"DESInternalDodMLTaskResult\"32@0:8@\"DESInternalDodMLTask\"16^@24"
- "@\"DESRecordSet\""
- "@\"MLRLocalDebugSchedulingTask\""
- "@\"MLRPluginSchedulingRecord\""
- "@\"NSArray\""
- "@\"NSDictionary\"24@0:8@\"DESRecordSet\"16"
- "@24@0:8^@16"
- "@40@0:8@16@24@32"
- "@56@0:8@16@24@32@40@48"
- "@64@0:8@16@24@32@40@48#56"
- "@64@0:8@16q24d32@40@48@56"
- "@68@0:8@16@24@32@40@48#56B64"
- "B32@0:8@\"NSURL\"16@\"DESInternalDodMLTask\"24"
- "B8@?0"
- "Continuing recipe evaluations because limits not reached (%!t(MISSING)u/%!t(MISSING)u, %!f(MISSING)s/%!f(MISSING)s)"
- "Continuing recipe evaluations because override enabled"
- "Could not load plugin for %!@(MISSING): with error:%!@(MISSING)"
- "Created worker=%!@(MISSING) for pluginID=%!@(MISSING) with %!@(MISSING) records."
- "Evaluating recipe."
- "Evaluation has been deferred by DAS"
- "Expected MLRLocalDebugSchedulingTask"
- "Fail to commit debug record with error=%!@(MISSING)"
- "Fail to fetch policy."
- "Fail to find matched records with error=%!{(MISSING)public}@"
- "Fail to load plugin with error = %!@(MISSING)."
- "Fail to perform dodML task."
- "Fail to retrieve task result for %!@(MISSING) with error=%!@(MISSING)."
- "Fail to roll die with error=%!{(MISSING)public}@"
- "Fail to run task, bundleID=%!@(MISSING), recipeID=%!@(MISSING), deferred=%!d(MISSING), error=%!@(MISSING)"
- "Fail to send results for recipe=%!@(MISSING), with error=%!@(MISSING)"
- "Fail to send telemetry"
- "Fail to send telemetry with error = %!@(MISSING)."
- "Fail to update task record for plugin=%!@(MISSING), error=%!@(MISSING)"
- "Federated Buffer staleness is too large"
- "Federated Buffer staleness is too large for recipe=%!@(MISSING)."
- "FetchTelemetry"
- "Fetching Telemetry."
- "Finished evaluating recipe."
- "Finished fetching Telemetry."
- "InfoKeys-%!@(MISSING)"
- "JSONResult"
- "Last successful run was < 6 hours ago with bundleID=%!@(MISSING)"
- "Lost die roll; not doing evalution for recipe %!@(MISSING)"
- "Lost die roll; not doing telemetry callback to %!@(MISSING)"
- "MLRDodMLTaskWorker"
- "MLRDodMLTaskWorker"
- "MLRLocalDebugSchedulingTask"
- "MLRLocalDebugTaskWorker"
- "Missing record info in %!@(MISSING)"
- "Nil completionDate"
- "No FiDES records for bundleId=%!@(MISSING), no need to check with server"
- "No evaluator for custom telemetry: %!@(MISSING)"
- "No matching and winning recipes, all done."
- "No valid upload transport"
- "No valid upload transport for recipe=%!@(MISSING)."
- "NonPFLPlugins"
- "Not downloading attachment %!@(MISSING)"
- "Plugin %!@(MISSING) is skipped because the last successful run was < %!l(MISSING)u seconds ago."
- "Reaching out to plugin to start compute, sessionID=%!@(MISSING), remoteObjectProxy=%!@(MISSING)."
- "Recipe %!@(MISSING) has no matching records, skipping"
- "Recipe attachment download failed"
- "RecipeEvaluation"
- "Returning result=%!@(MISSING)"
- "Skipping die roll for %!@(MISSING)"
- "Skipping die roll; doing telemetry callback to %!@(MISSING)"
- "Skipping recipe evaluation due to attachment download error"
- "Skipping result post-back for empty or deferred evaluation result for recipe %!@(MISSING), recordSet %!@(MISSING)"
- "Skipping telemetry because none valid was found in the policy"
- "Stopping recipe evaluations because limit reached (%!t(MISSING)u)"
- "Stopping recipe evaluations because time limit reached (%!f(MISSING)s/%!f(MISSING)s)"
- "T@\"<DESPluginManaging>\",R,N,V_plugin"
- "T@\"DESDodMLServer\",R,N,V_server"
- "T@\"DESRecordSet\",R,N,V_recordSet"
- "T@\"MLRLocalDebugSchedulingTask\",R,N,V_task"
- "T@\"MLRPluginSchedulingRecord\",R,N,V_schedulingRecord"
- "T@\"NSArray\",R,N,V_attachments"
- "T@\"NSArray\",R,N,V_recordUUIDs"
- "T@\"NSString\",R,N,V_localeIdentifier"
- "T@\"NSURL\",R,N,V_recipePath"
- "Task is completed without error or defer, bundleID=%!@(MISSING), recipeID=%!@(MISSING),."
- "Task is deferred by plugin, bundleID=%!@(MISSING), recipeID=%!@(MISSING),."
- "Telemetry failed: %!@(MISSING)/%!@(MISSING)"
- "Throttling PFL plugin sampling rate to %!f(MISSING)"
- "URLForResource:withExtension:"
- "UUID"
- "UUIDString"
- "Unexpected task result returned"
- "Win"
- "Won die roll; doing telemetry callback to %!@(MISSING)"
- "_"
- "_addDebugRecordAfterExecutingRecipe:withError:result:"
- "_addDebugRecordErrorForRecipeID:description:"
- "_attachments"
- "_attemptRecipeMatchWithRecipeIDs:keepGoing:completion:"
- "_downloadAttachments:recipe:completion:"
- "_ensureEvaluatorWithError:"
- "_fetchRecipe:matchingRecordSet:completion:"
- "_handleRecipe:matchingRecordSet:completion:"
- "_handleTelemetryInPolicy:completion:"
- "_inithWithContentsOfFile:recipeID:bundleIdentifier:error:"
- "_matchedRecordSetforRecipeID:error:"
- "_nativeRecordInfoWithError:"
- "_policy"
- "_recipePath"
- "_recipeWithError:"
- "_recordSet"
- "_recordUUIDs"
- "_results"
- "_rollDieWithRecipeID:error:"
- "_runEvaluationForBundleId:task:completion:"
- "_schedulingRecord"
- "_server"
- "_task"
- "_taskDeferByDASError"
- "absoluteString"
- "addPFLSchedulingTaskToTasks:withBundleID:"
- "allKeys"
- "allRecipeIDs"
- "arrayByAddingObjectsFromArray:"
- "attachmentPaths"
- "attachmentSignatures"
- "baseURL"
- "binaryResult"
- "bundle identifier should not be nil."
- "bundleForClass:"
- "canRun"
- "certificate"
- "com.apple.MLRuntime.MLRLocalDebugTaskWorker"
- "containsObject:"
- "createTaskWorkerForDodMLTask:completion:"
- "createTaskWorkerForLocalDebugTask:completion:"
- "custom"
- "dediscoRoute"
- "deferralURL"
- "deferred"
- "device_os"
- "device_type"
- "dictionaryForKey:"
- "dictionaryWithContentsOfURL:"
- "downloadAttachments:signatures:certificate:relativePaths:completion:"
- "duration"
- "fetchCoreDuetEventsForBundleId:completion:"
- "fetchPolicyForBundleIdentifier:completion:"
- "fetchRecipe:bundleIdentifier:completion:"
- "fetchRecordSetForBundleId:completion:"
- "fetchSavedRecordInfoForBundleId:completion:"
- "fileURLWithPath:"
- "filteredRecordSetWithJSONPredicate:"
- "initWithBaseURL:localeIdentifier:protocolClass:"
- "initWithBaseURL:recordSet:bundleIdentifier:localeIdentifier:pluginOverride:"
- "initWithBaseURL:recordSet:bundleIdentifier:localeIdentifier:pluginOverride:protocolClass:"
- "initWithBaseURL:recordSet:bundleIdentifier:localeIdentifier:pluginOverride:protocolClass:alwaysRun:"
- "initWithBundleIdentifier:taskSource:maxTimeLimit:recipePath:recordUUIDs:attachments:"
- "initWithDediscoRoute:originRoute:parsecRoute:postBackBaseURL:"
- "initWithNativeRecords:nativeRecordInfo:coreDuetEvents:"
- "initWithPolicy:recipe:"
- "initWithRecipe:matchingRecordSet:baseURL:localIdentifier:recipePath:uploadTransport:"
- "initWithTask:plugin:dodMLServer:"
- "invalid arguments passed to service; programmer error!"
- "invalid task.recipePath"
- "isFederatedBufferStaled"
- "isFileURL"
- "isPFLPlugin"
- "locale"
- "localeIdentifier"
- "lose"
- "maxTimeLimitInSeconds"
- "nil plugin"
- "path"
- "performDodMLTask:outError:"
- "performDodMLTask:sandBoxExtensions:completion:"
- "period"
- "plist"
- "plugin"
- "pluginManagerForBundleId:error:"
- "plugins"
- "predicate"
- "predicateForRecipeID:error:"
- "recipeCountLimit"
- "recipeID"
- "recipePath"
- "recordSet"
- "recordUUIDs"
- "record_count"
- "result = %!@(MISSING)"
- "runJSONPOSTRequest:URL:completion:"
- "samplingRateForRecipeID:error:"
- "schedulingRecord"
- "sendEventAttachmentDownloadsBundleID:duration:success:downloadedAttachmentCount:"
- "sendEventRecordsMatchedForBundleID:"
- "sendRecipeResponseWithResult:recipe:uploadTransport:error:completion:"
- "server"
- "setAttachments:"
- "setObject:forKey:"
- "setValue:forKey:"
- "setWithArray:"
- "shouldDownloadURL:forTask:"
- "standardUserDefaults"
- "start local debug task=%!@(MISSING)"
- "stringByReplacingOccurrencesOfString:withString:"
- "task"
- "taskResultWithError:"
- "telemetrySamplingRate"
- "telemetryURL"
- "telemetryWithRecordSet:"
- "timeLimit"
- "transportIsDedisco"
- "updateTaskAfterCompletion:error:"
- "uploadViaDediscoWithResult:recipe:error:"
- "v20@?0B8@\"NSError\"12"
- "v24@?0@\"DESDodMLTaskResultContainer\"8@\"NSError\"16"
- "v24@?0@\"DESDodMLTaskSchedulingPolicy\"8@\"NSError\"16"
- "v24@?0@\"DESInternalDodMLTaskResult\"8@\"NSError\"16"
- "v24@?0@\"DESRecipe\"8@\"NSError\"16"
- "v24@?0@\"DESRecordSet\"8@\"NSError\"16"
- "v24@?0@\"NSArray\"8@\"NSError\"16"
- "v24@?0@\"NSData\"8@\"NSError\"16"
- "v24@?0@\"NSDictionary\"8@\"NSError\"16"
- "v24@?0@\"NSUUID\"8@\"NSError\"16"
- "v32@?0@\"DESInternalDodMLTaskResult\"8@\"DESRecipe\"16@\"NSError\"24"
- "v32@?0@\"NSArray\"8@\"NSError\"16^B24"
- "v32@?0@\"NSData\"8@\"NSURLResponse\"16@\"NSError\"24"
- "v40@0:8@\"DESInternalDodMLTask\"16@\"NSArray\"24@?<v@?@\"DESDodMLTaskResultContainer\"@\"NSError\">32"
- "v40@0:8@16@24@32"
- "v40@0:8@16@?24@?32"
- "v40@?0@\"NSDictionary\"8@\"NSDictionary\"16@\"NSArray\"24@\"NSError\"32"

```
