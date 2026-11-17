## VoiceShortcuts

> `/System/Library/PrivateFrameworks/VoiceShortcuts.framework/VoiceShortcuts`

```diff

-5203.0.1.0.0
-  __TEXT.__text: 0x1342a0
-  __TEXT.__objc_methlist: 0x54f4
-  __TEXT.__const: 0x6c50
-  __TEXT.__dlopen_cstrs: 0x1e1
-  __TEXT.__oslogstring: 0xea2b
-  __TEXT.__swift5_typeref: 0x35a1
-  __TEXT.__swift5_fieldmd: 0x1888
-  __TEXT.__constg_swiftt: 0x22bc
-  __TEXT.__swift5_reflstr: 0x1551
+5206.0.3.0.0
+  __TEXT.__text: 0x13e38c
+  __TEXT.__objc_methlist: 0x5534
+  __TEXT.__const: 0x6da0
+  __TEXT.__dlopen_cstrs: 0x181
+  __TEXT.__oslogstring: 0xf15d
+  __TEXT.__swift5_typeref: 0x376b
+  __TEXT.__swift5_fieldmd: 0x1920
+  __TEXT.__constg_swiftt: 0x2324
+  __TEXT.__swift5_reflstr: 0x1661
   __TEXT.__swift5_builtin: 0x154
   __TEXT.__swift5_assocty: 0x690
-  __TEXT.__swift5_capture: 0x3180
-  __TEXT.__cstring: 0xe36f
+  __TEXT.__swift5_capture: 0x33a0
+  __TEXT.__cstring: 0xe73b
   __TEXT.__swift5_proto: 0x448
-  __TEXT.__swift5_types: 0x208
-  __TEXT.__swift_as_entry: 0x328
-  __TEXT.__swift_as_ret: 0x324
-  __TEXT.__swift_as_cont: 0x750
+  __TEXT.__swift5_types: 0x210
+  __TEXT.__swift_as_entry: 0x340
+  __TEXT.__swift_as_ret: 0x340
+  __TEXT.__swift_as_cont: 0x778
   __TEXT.__swift5_protos: 0x4c
   __TEXT.__swift5_mpenum: 0x28
-  __TEXT.__gcc_except_tab: 0x998
+  __TEXT.__gcc_except_tab: 0x950
   __TEXT.__ustring: 0x44
-  __TEXT.__unwind_info: 0x5d88
-  __TEXT.__eh_frame: 0x8980
+  __TEXT.__unwind_info: 0x5fb0
+  __TEXT.__eh_frame: 0x8e68
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0
   __TEXT.__objc_classname: 0x0
   __TEXT.__objc_methname: 0x0
   __TEXT.__objc_methtype: 0x0
-  __DATA_CONST.__const: 0x1d48
-  __DATA_CONST.__objc_classlist: 0x320
+  __DATA_CONST.__const: 0x1d78
+  __DATA_CONST.__objc_classlist: 0x328
   __DATA_CONST.__objc_catlist: 0x68
   __DATA_CONST.__objc_protolist: 0x2b8
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x4590
+  __DATA_CONST.__objc_selrefs: 0x45a0
   __DATA_CONST.__objc_protorefs: 0xd0
   __DATA_CONST.__objc_superrefs: 0x190
   __DATA_CONST.__objc_arraydata: 0x40
-  __DATA_CONST.__got: 0x18b0
-  __AUTH_CONST.__const: 0xab88
-  __AUTH_CONST.__cfstring: 0x3f20
-  __AUTH_CONST.__objc_const: 0xa058
+  __DATA_CONST.__got: 0x18d8
+  __AUTH_CONST.__const: 0xb238
+  __AUTH_CONST.__cfstring: 0x4040
+  __AUTH_CONST.__objc_const: 0xa210
   __AUTH_CONST.__objc_intobj: 0xc0
   __AUTH_CONST.__objc_dictobj: 0x28
-  __AUTH_CONST.__auth_got: 0x2118
+  __AUTH_CONST.__auth_got: 0x2160
   __AUTH.__objc_data: 0x830
-  __AUTH.__data: 0x11e0
-  __DATA.__objc_ivar: 0x3e0
-  __DATA.__data: 0x2670
+  __AUTH.__data: 0x12a8
+  __DATA.__objc_ivar: 0x3e8
+  __DATA.__data: 0x26d8
   __DATA.__common: 0x18
   __DATA_DIRTY.__objc_data: 0x1490
   __DATA_DIRTY.__data: 0x2a10
   __DATA_DIRTY.__crash_info: 0x148
-  __DATA_DIRTY.__bss: 0x3450
+  __DATA_DIRTY.__bss: 0x3440
   __DATA_DIRTY.__common: 0x20
   - /System/Library/Frameworks/AppIntents.framework/AppIntents
   - /System/Library/Frameworks/CloudKit.framework/CloudKit

   - /usr/lib/swift/libswiftOSLog.dylib
   - /usr/lib/swift/libswiftObjectiveC.dylib
   - /usr/lib/swift/libswiftQuartzCore.dylib
-  - /usr/lib/swift/libswiftRegexBuilder.dylib
   - /usr/lib/swift/libswiftSpatial.dylib
   - /usr/lib/swift/libswiftUniformTypeIdentifiers.dylib
   - /usr/lib/swift/libswiftXPC.dylib

   - /usr/lib/swift/libswift_DarwinFoundation3.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  Functions: 8094
-  Symbols:   5340
-  CStrings:  2221
+  Functions: 8307
+  Symbols:   5308
+  CStrings:  2260
 
Symbols:
+ +[VCDaemonDatabaseProvider loadActionKit]
+ -[VCCKShortcutSyncCoordinator walrusStatus]
+ -[VCCKShortcutSyncService encryptedSchemaVersion]
+ -[VCCKShortcutSyncService initWithContainer:database:daemonTaskScheduler:applicationObserver:debuggingOptions:logger:encryptedSchemaVersion:]
+ -[VCCKShortcutSyncService sendChangedWorkflowsForEventName:]
+ -[VCCKShortcutSyncService setEncryptedSchemaVersion:]
+ -[VCCKShortcutSyncService updateEncryptedSchemaVersion:]
+ -[WFConfiguredSystemActionMigrator updateActionsUsingTransform:]
+ GCC_except_table1003
+ GCC_except_table1053
+ GCC_except_table1059
+ GCC_except_table1084
+ GCC_except_table1105
+ GCC_except_table1190
+ GCC_except_table1196
+ GCC_except_table1201
+ GCC_except_table1202
+ GCC_except_table1207
+ GCC_except_table1258
+ GCC_except_table1308
+ GCC_except_table1314
+ GCC_except_table1326
+ GCC_except_table1332
+ GCC_except_table1342
+ GCC_except_table1347
+ GCC_except_table1384
+ GCC_except_table1406
+ GCC_except_table1420
+ GCC_except_table1426
+ GCC_except_table1444
+ GCC_except_table1447
+ GCC_except_table1461
+ GCC_except_table411
+ GCC_except_table437
+ GCC_except_table450
+ GCC_except_table524
+ GCC_except_table604
+ GCC_except_table605
+ GCC_except_table618
+ GCC_except_table629
+ GCC_except_table658
+ GCC_except_table817
+ GCC_except_table951
+ GCC_except_table977
+ GCC_except_table983
+ GCC_except_table985
+ _OBJC_CLASS_$_CHSWidget
+ _OBJC_CLASS_$_INAppDescriptor
+ _OBJC_CLASS_$_INAppResolver
+ _OBJC_IVAR_$_VCCKShortcutSyncCoordinator._walrusStatus
+ _OBJC_IVAR_$_VCCKShortcutSyncService._encryptedSchemaVersion
+ _WFDebugViewExpectedEncryptedSchemaVersion
+ _WFLogCategoryHomescreen
+ _WFSystemShortcutTypeIdentifier
+ __DATA__TtC14VoiceShortcuts27VCAppReplacementCoordinator
+ __IVARS__TtC14VoiceShortcuts27VCAppReplacementCoordinator
+ __METACLASS_DATA__TtC14VoiceShortcuts27VCAppReplacementCoordinator
+ __OBJC_$_CLASS_METHODS_VCDaemonDatabaseProvider
+ ___56-[VCCKShortcutSyncService updateEncryptedSchemaVersion:]_block_invoke
+ ___56-[VCCKShortcutSyncService updateEncryptedSchemaVersion:]_block_invoke_2
+ ___block_descriptor_157_e8_32s40s_e26_"NSMutableDictionary"8?0ls32l8s40l8
+ ___block_descriptor_48_e8_32s_e5_v8?0ls32l8
+ ___block_descriptor_64_e8_32s40s48r56r_e35_v24?0"CKAccountInfo"8"NSError"16ls32l8s40l8r48l8r56l8
+ ___swift_closure_destructor.109Tm
+ ___swift_closure_destructor.14Tm
+ ___swift_closure_destructor.17Tm
+ ___swift_closure_destructor.31Tm
+ ___swift_closure_destructor.5Tm
+ ___swift_memcpy25_8
+ _getWFSystemShortcutLogObject
+ _symbolic Ig_
+ _symbolic SDySo19WFUnifiedTriggerKeyCSSG
+ _symbolic SS3key_yp5valuet
+ _symbolic SS______pIegHgzo_ s5ErrorP
+ _symbolic SS_ypt
+ _symbolic SSyt______pIegHnrzo_ s5ErrorP
+ _symbolic SaySo9CHSWidgetCG
+ _symbolic Say______pG So26CHSWidgetConfigurationHostP
+ _symbolic ScCy___________pG 14VoiceShortcuts31SystemShortcutOrphanCleanupTaskC22ConfiguredWidgetTokens33_C75A3AE832D6F3623086BA112804A96ELLV s5ErrorP
+ _symbolic ShySSGSo10WFDatabaseCIeggg_
+ _symbolic ShySSGSo10WFDatabaseCytIegnnr_
+ _symbolic ShySo19WFUnifiedTriggerKeyCG
+ _symbolic So11LNValueTypeCm
+ _symbolic So20WFWorkflowCollectionC
+ _symbolic _____ 14VoiceShortcuts27VCAppReplacementCoordinatorC
+ _symbolic _____ 14VoiceShortcuts31SystemShortcutOrphanCleanupTaskC22ConfiguredWidgetTokens33_C75A3AE832D6F3623086BA112804A96ELLV
+ _symbolic _____ 19VoiceShortcutClient14AppReplacementC
+ _symbolic _____3key_yp5valuet So15WFNewTriggerKeya
+ _symbolic _____3key_yp5valuet So19WFWorkflowActionKeya
+ _symbolic _____Sg 14VoiceShortcuts27VCAppReplacementCoordinatorC
+ _symbolic ______p 11WorkflowKit28WFTriggerRegistrationStoringP
+ _symbolic ______ypt So15WFNewTriggerKeya
+ _symbolic ______ypt So19WFWorkflowActionKeya
+ _symbolic ______yptSg So15WFNewTriggerKeya
+ _symbolic ______yptSg So19WFWorkflowActionKeya
+ _symbolic _____ySS_yptG s23_ContiguousArrayStorageC
+ _symbolic _____ySo19WFUnifiedTriggerKeyCG s11_SetStorageC
+ _symbolic _____ySo19WFUnifiedTriggerKeyCSSG s17_NativeDictionaryV
+ _symbolic _____ySsG s23_ContiguousArrayStorageC
+ _symbolic _____y______yptG s23_ContiguousArrayStorageC So15WFNewTriggerKeya
+ _symbolic _____y______yptG s23_ContiguousArrayStorageC So19WFWorkflowActionKeya
+ _symbolic _____y_____ypG s18_DictionaryStorageC So19WFWorkflowActionKeya
+ _symbolic ySSYaKc
+ _symbolic yShySSG_So10WFDatabaseCtc
+ _type_layout_string 14VoiceShortcuts31SystemShortcutOrphanCleanupTaskC22ConfiguredWidgetTokens33_C75A3AE832D6F3623086BA112804A96ELLV
+ _type_layout_string SC11VCErrorCodeLeV
+ _type_layout_string So14WFEventInfoKeya
- -[VCCKShortcutSyncCoordinator handleWalrusStatusDidChange]
- -[VCCKShortcutSyncService initWithContainer:database:daemonTaskScheduler:applicationObserver:debuggingOptions:logger:]
- -[VCCKShortcutSyncService sendChangedWorkflows]
- -[VCMetricSubmitter hasSeenAutoShortcutsSections]
- GCC_except_table1049
- GCC_except_table1051
- GCC_except_table1080
- GCC_except_table1097
- GCC_except_table1127
- GCC_except_table1186
- GCC_except_table1192
- GCC_except_table1194
- GCC_except_table1197
- GCC_except_table1203
- GCC_except_table1254
- GCC_except_table1303
- GCC_except_table1309
- GCC_except_table1321
- GCC_except_table1327
- GCC_except_table1337
- GCC_except_table1343
- GCC_except_table1376
- GCC_except_table1398
- GCC_except_table1416
- GCC_except_table1418
- GCC_except_table1440
- GCC_except_table1443
- GCC_except_table1457
- GCC_except_table409
- GCC_except_table432
- GCC_except_table445
- GCC_except_table519
- GCC_except_table600
- GCC_except_table601
- GCC_except_table614
- GCC_except_table625
- GCC_except_table654
- GCC_except_table813
- GCC_except_table947
- GCC_except_table973
- GCC_except_table979
- GCC_except_table981
- GCC_except_table999
- _AssistantServicesLibraryCore.frameworkLibrary
- _OUTLINED_FUNCTION_290
- _OUTLINED_FUNCTION_291
- _OUTLINED_FUNCTION_292
- _OUTLINED_FUNCTION_293
- _OUTLINED_FUNCTION_294
- _OUTLINED_FUNCTION_295
- _OUTLINED_FUNCTION_296
- _OUTLINED_FUNCTION_297
- _OUTLINED_FUNCTION_298
- _OUTLINED_FUNCTION_299
- _OUTLINED_FUNCTION_300
- _OUTLINED_FUNCTION_301
- _OUTLINED_FUNCTION_302
- _OUTLINED_FUNCTION_303
- _OUTLINED_FUNCTION_304
- _OUTLINED_FUNCTION_305
- _OUTLINED_FUNCTION_306
- _OUTLINED_FUNCTION_307
- _OUTLINED_FUNCTION_308
- _OUTLINED_FUNCTION_309
- _OUTLINED_FUNCTION_310
- _OUTLINED_FUNCTION_311
- _OUTLINED_FUNCTION_312
- _OUTLINED_FUNCTION_313
- _OUTLINED_FUNCTION_314
- _OUTLINED_FUNCTION_315
- _OUTLINED_FUNCTION_316
- _OUTLINED_FUNCTION_317
- _OUTLINED_FUNCTION_318
- _OUTLINED_FUNCTION_319
- _OUTLINED_FUNCTION_320
- _OUTLINED_FUNCTION_321
- _OUTLINED_FUNCTION_322
- _OUTLINED_FUNCTION_323
- _OUTLINED_FUNCTION_324
- _OUTLINED_FUNCTION_325
- _OUTLINED_FUNCTION_326
- _OUTLINED_FUNCTION_327
- _OUTLINED_FUNCTION_328
- _OUTLINED_FUNCTION_329
- _OUTLINED_FUNCTION_330
- _OUTLINED_FUNCTION_331
- _OUTLINED_FUNCTION_332
- _OUTLINED_FUNCTION_333
- _OUTLINED_FUNCTION_334
- _OUTLINED_FUNCTION_335
- _OUTLINED_FUNCTION_336
- _OUTLINED_FUNCTION_337
- _OUTLINED_FUNCTION_338
- _OUTLINED_FUNCTION_339
- _OUTLINED_FUNCTION_340
- _OUTLINED_FUNCTION_341
- _OUTLINED_FUNCTION_342
- _OUTLINED_FUNCTION_343
- _OUTLINED_FUNCTION_344
- _OUTLINED_FUNCTION_345
- _OUTLINED_FUNCTION_346
- _OUTLINED_FUNCTION_347
- _OUTLINED_FUNCTION_348
- _OUTLINED_FUNCTION_349
- _OUTLINED_FUNCTION_350
- _OUTLINED_FUNCTION_351
- _OUTLINED_FUNCTION_352
- _OUTLINED_FUNCTION_353
- _OUTLINED_FUNCTION_354
- _OUTLINED_FUNCTION_355
- _OUTLINED_FUNCTION_356
- _OUTLINED_FUNCTION_357
- _OUTLINED_FUNCTION_358
- _WFLastViewedAutoShortcutsAtTimeKey
- _WFWalrusEnabledKey
- ___AssistantServicesLibraryCore_block_invoke
- ___block_descriptor_158_e8_32s40s_e26_"NSMutableDictionary"8?0ls32l8s40l8
- ___block_descriptor_64_e8_32s40s48r56r_e35_v24?0"CKAccountInfo"8"NSError"16ls32l8r48l8s40l8r56l8
- ___getAFVisualIntelligenceCameraRestrictedSymbolLoc_block_invoke
- ___swift_closure_destructor.12Tm
- ___swift_closure_destructor.198Tm
- ___swift_closure_destructor.38Tm
- ___swift_closure_destructor.63Tm
- ___swift_closure_destructor.99Tm
- _audit_stringAssistantServices
- _getAFVisualIntelligenceCameraRestrictedSymbolLoc.ptr
- _swift_task_immediate
- _swift_task_isCurrentExecutorWithFlags
- _symbolic SbIegd_
- _symbolic ScCyShy_____G______pG 10Foundation4UUIDV s5ErrorP
- _symbolic _____ 11WorkflowKit26WFTriggerRegistrationStoreC
- _symbolic _____Iegd_ s5Int32V
- _symbolic _____Iegr_ s5Int32V
- _symbolic _____ySSG s20CollectionDifferenceV
- _symbolic _____ySS_G s20CollectionDifferenceV6ChangeO
- _symbolic _____y_____G s23_ContiguousArrayStorageC 10Foundation4UUIDV
- _symbolic _____y_____ySS_GG s23_ContiguousArrayStorageC s20CollectionDifferenceV6ChangeO
- _type_layout_string SC19WFDatabaseErrorCodeLeV
- _type_layout_string So16VCXPCEventStreama
CStrings:
+ " in root instead"
+ " in the system actions"
+ " isn't installed"
+ "%s Encrypted schema version changed from %ld to %ld"
+ "%s Failed to resolve system shortcut %{public}@: %{public}@"
+ "%s Should show Visual Intelligence: VI enabled: %@"
+ "%s Updated system action type: %@ with the transform, success: %i"
+ "%s Walrus status is unknown (%{public}@), not creating new sync service"
+ ", unavailable resources: ["
+ "-[VCCKShortcutSyncService sendChangedWorkflowsForEventName:]"
+ "-[VCCKShortcutSyncService updateEncryptedSchemaVersion:]"
+ "-[WFConfiguredSystemActionMigrator updateActionsUsingTransform:]"
+ "-[WFSystemShortcutService runSystemShortcutWithToken:bundleIdentifier:reply:]"
+ "Could not extract a system shortcut token from a matching value"
+ "Couldn't replace "
+ "Deleted the app shortcut domain of replaced app %{public}s"
+ "Deleting %{public}ld stale system shortcut tokens (stored: %{public}ld, active: %{public}ld)"
+ "Failed to initialize VCAppReplacementCoordinator: missing the Spotlight sync service or the system action migrator. App Replacement requests will not be handled."
+ "Failed to read configured widgets: %@"
+ "Failed to replace app %{public}s in shortcut - %{public}s: %{public}s"
+ "Fetched %{public}ld active system shortcut tokens from configured widgets: %{public}s"
+ "Fetched %{public}ld stored system shortcut tokens: %{public}s"
+ "Finished updating trigger registration with no changes. Skipped: %{public}ld. Total active: %{public}ld."
+ "Finished updating trigger registration. Registered: %{public}ld, re-registered: %{public}ld, unregistered: %{public}ld, skipped: %{public}ld, failed: %{public}ld. Total active: %{public}ld."
+ "Found a system shortcut token under value type %{public}s"
+ "Local categories (%{public}s) do not match remote categories (%{public}s)"
+ "Read %{public}ld widget hosts, %{public}ld configured widgets, %{public}ld uninspectable"
+ "Reading configured widgets returned neither hosts nor an error"
+ "Received unregistered events for %{public}ld apps, confirmed inactive, entries kept: %s, ignored as still active: %s"
+ "Reconciliation added folder %{public}s"
+ "Reconciliation failed to add shortcut "
+ "Reconciliation failed to add shortcut %{public}s to category %{public}s, should be unreachable."
+ "Reconciliation: can't find folder "
+ "Reconciliation: can't find folder %{public}s, putting %{public}s in root instead."
+ "Reconciliation: couldn't get shortcuts for folder "
+ "Reconciliation: throwing on getting shortcuts from a folder ID (%{public}s) we got from the same library should be unreachable. \n%s"
+ "Reconciling shortcuts in %{public}s."
+ "Reconciling shortcuts in folder %{public}s."
+ "Replaced app %{public}s with %{public}s in %ld shortcuts, %ld failed"
+ "Replacement app %{public}s isn't installed; leaving shortcuts as they are"
+ "Shortcuts in %{public}s don't need to be reconciled."
+ "Shortcuts in folder %{public}s don't need to be reconciled."
+ "Skipping orphan cleanup: %{public}ld system shortcut values and %{public}ld widgets could not be inspected"
+ "Skipping orphan cleanup: no active tokens found for %{public}ld stored tokens"
+ "Skipping trigger with identifier: %{public}s, key: %{public}@ | %{public}s."
+ "Unrecognized system shortcut value type identifier %{public}s"
+ "Updating web clips for %ld shortcuts that moved to %{public}s"
+ "VCCKShortcutSyncService.encryptedSchemaVersionChanged"
+ "Widget intent %s from %s has no link action to inspect"
+ "], unconfigured parameters: ["
+ "account info fetch failed: %@:%ld"
+ "account info fetch returned an error: %@:%ld"
+ "account status changed: %@ -> %@"
+ "com.apple.shortcuts.WFTriggerRegistrar.registration"
+ "com.apple.shortcuts.app-replacement"
+ "could not build WFNewTrigger"
+ "encrypted schema version changed: %ld -> %ld"
+ "fetched folder %@ with newer encrypted schema version %lld, leaving it alone"
+ "fetched workflow %@ with newer encrypted schema version %lld, leaving it alone"
+ "logUninstalledAppsForSystemShortcutEntries"
+ "not starting sync service: walrus status unknown"
+ "searchAttributionAppBundleIdentifier"
+ "up to date"
+ "update encrypted schema version to %ld"
+ "walrus status changed: %@ -> %@"
- "%s Handling CloudKit Walrus status change, walrusEnabled = %d"
- "%s Should show Visual Intelligence: AI enabled: %@ VI enabled: %@"
- "%s Walrus status did change, but we couldn't find a database to update: %@"
- "-[VCCKShortcutSyncCoordinator handleWalrusStatusDidChange]"
- "-[VCCKShortcutSyncService sendChangedWorkflows]"
- "AFVisualIntelligenceCameraRestricted"
- "BOOL soft_AFVisualIntelligenceCameraRestricted(void)"
- "Cleaned up system shortcut entries for %ld uninstalled apps"
- "Deleting %ld stale system shortcut tokens"
- "Device records response was unexpectedly empty."
- "Failed to cleanup entries for uninstalled apps: %@"
- "Fetched %ld active system shortcut tokens from configured widgets"
- "Fetched %ld stored system shortcut tokens"
- "Finished updating trigger registration. Registered: %{public}ld, re-registered: %{public}ld, unregistered: %{public}ld, skipped: %{public}ld. Total active: %{public}ld."
- "Inserted folder %s not found in local library."
- "Local categories (%s) do not match remote categories (%s)"
- "Reconciling shortcuts in %s."
- "Reconciling shortcuts in folder %s."
- "Shortcuts in %s don't need to be reconciled."
- "Shortcuts in folder %s don't need to be reconciled."
- "Skipping trigger with identifier: %{public}s, key: %{public}@ | isAvailable: %{bool,public}d, isValid: %{bool,public}d."
- "autoShortcutsSectionsViewed"
- "cleanupUninstalledAppSystemShortcutEntries"
- "com.apple.shortcuts.walrus"
- "softlink:o:path:/System/Library/PrivateFrameworks/AssistantServices.framework/AssistantServices"
- "void *AssistantServicesLibrary(void)"
```
