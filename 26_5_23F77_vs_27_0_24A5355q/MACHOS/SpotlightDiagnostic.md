## SpotlightDiagnostic

> `/System/Library/PrivateFrameworks/Search.framework/PlugIns/SpotlightDiagnostic.appex/SpotlightDiagnostic`

```diff

-2418.5.9.101.0
-  __TEXT.__text: 0x1208
-  __TEXT.__auth_stubs: 0x300
-  __TEXT.__objc_stubs: 0x3e0
+2444.104.0.0.0
+  __TEXT.__text: 0x1ef0
+  __TEXT.__auth_stubs: 0x3f0
+  __TEXT.__objc_stubs: 0x8c0
   __TEXT.__objc_methlist: 0x5c
-  __TEXT.__const: 0x80
-  __TEXT.__gcc_except_tab: 0x80
-  __TEXT.__cstring: 0x2d2
-  __TEXT.__oslogstring: 0x216
+  __TEXT.__const: 0x88
+  __TEXT.__gcc_except_tab: 0x204
+  __TEXT.__cstring: 0x476
+  __TEXT.__oslogstring: 0x598
   __TEXT.__objc_classname: 0x56
-  __TEXT.__objc_methname: 0x378
+  __TEXT.__objc_methname: 0x649
   __TEXT.__objc_methtype: 0x73
-  __TEXT.__unwind_info: 0xb8
-  __DATA_CONST.__auth_got: 0x190
-  __DATA_CONST.__got: 0x70
-  __DATA_CONST.__const: 0x78
-  __DATA_CONST.__cfstring: 0x1e0
+  __TEXT.__unwind_info: 0xc8
+  __DATA_CONST.__const: 0xf0
+  __DATA_CONST.__cfstring: 0x420
   __DATA_CONST.__objc_classlist: 0x8
   __DATA_CONST.__objc_protolist: 0x10
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_protorefs: 0x8
-  __DATA_CONST.__objc_classrefs: 0x30
+  __DATA_CONST.__objc_arraydata: 0x60
+  __DATA_CONST.__objc_arrayobj: 0x30
+  __DATA_CONST.__auth_got: 0x208
+  __DATA_CONST.__got: 0xb0
   __DATA.__objc_const: 0xb8
-  __DATA.__objc_selrefs: 0x110
+  __DATA.__objc_selrefs: 0x248
   __DATA.__objc_data: 0x50
   __DATA.__data: 0xc0
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation

   - /System/Library/PrivateFrameworks/SpotlightDiagnostics.framework/SpotlightDiagnostics
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 1D36E085-08B7-3771-B0BF-C652E6BBA361
-  Functions: 20
-  Symbols:   81
-  CStrings:  90
+  UUID: E8DECC6B-5C56-3419-9B2E-75A68AF1459C
+  Functions: 33
+  Symbols:   99
+  CStrings:  181
 
Symbols:
+ _CFAbsoluteTimeGetCurrent
+ _NSTemporaryDirectory
+ _OBJC_CLASS_$_NSConstantArray
+ _OBJC_EHTYPE_$_NSException
+ _SDDiagnosticDefaultPrivacyLevel
+ _SDDiagnosticGateIsSeedBuild
+ ___kCFBooleanTrue
+ _objc_autoreleasePoolPop
+ _objc_autoreleasePoolPush
+ _objc_begin_catch
+ _objc_claimAutoreleasedReturnValue
+ _objc_copyWeak
+ _objc_destroyWeak
+ _objc_end_catch
+ _objc_enumerationMutation
+ _objc_initWeak
+ _objc_loadWeakRetained
+ _objc_release_x9
+ _objc_retainAutorelease
+ _objc_retain_x1
+ _objc_retain_x27
+ _objc_retain_x8
+ _objc_storeStrong
+ _unlink
- _SDIsAppleInternalInstall
- _objc_retain
- _objc_retain_x23
- _objc_retain_x24
- _os_variant_allows_internal_security_policies
- _os_variant_has_internal_diagnostics
CStrings:
+ "%@ 0x%05llx %s %d %@(%@):%@ [%@] %@\n"
+ "CoreSpotlight"
+ "CoreSpotlightService"
+ "DEExtensionHostAppKey"
+ "ERROR"
+ "Error writing build history data: %@"
+ "FAULT"
+ "Metadata"
+ "MetadataUtilities"
+ "SearchFramework"
+ "SpotlightDaemon"
+ "SpotlightDiagnosticLogs-%llu.log"
+ "SpotlightFramework"
+ "SpotlightIndex"
+ "SpotlightIndexUtilities"
+ "SpotlightResources"
+ "SpotlightServices"
+ "UTF8String"
+ "Wrote build history data to build-history.log"
+ "[SpotlightDiagnosticExtension attachmentsForParameters:ABC] Could not open: %s"
+ "[SpotlightDiagnosticExtension attachmentsForParameters:ABC] Failed to create file: %s"
+ "[SpotlightDiagnosticExtension attachmentsForParameters:ABC] Failed to prepare oslog stream"
+ "[SpotlightDiagnosticExtension attachmentsForParameters:ABC] Failed to truncate file: %s"
+ "[SpotlightDiagnosticExtension attachmentsForParameters:ABC] Failed to write log data: %@"
+ "[SpotlightDiagnosticExtension attachmentsForParameters:ABC] Getting spotlight oslog past 15 mins error/fault level"
+ "[SpotlightDiagnosticExtension attachmentsForParameters:ABC] Invalid oslog stream: reason = %lu"
+ "[SpotlightDiagnosticExtension attachmentsForParameters:ABC] Timeout on getting oslog stream"
+ "[SpotlightDiagnosticExtension attachmentsForParameters:ABC] Writing to file: %s"
+ "activateStreamFromDate:toDate:"
+ "array"
+ "attachmentWithPath:"
+ "build-history.log"
+ "category"
+ "closeFile"
+ "com.apple.symptomsd"
+ "com.apple.symptomsd-diag"
+ "composedMessage"
+ "containsObject:"
+ "countByEnumeratingWithState:objects:count:"
+ "createFileAtPath:contents:attributes:"
+ "dataUsingEncoding:"
+ "date"
+ "dateByAddingTimeInterval:"
+ "dateWithTimeIntervalSinceReferenceDate:"
+ "fileHandleForWritingAtPath:"
+ "getBuildHistoryData"
+ "initWithSource:"
+ "isEqualToString:"
+ "localStore"
+ "localizedDescription"
+ "logType"
+ "orPredicateWithSubpredicates:"
+ "predicateWithFormat:"
+ "prepareWithCompletionHandler:"
+ "process"
+ "process == %@"
+ "processIdentifier"
+ "reason"
+ "searchd"
+ "sender"
+ "setDeleteOnAttach:"
+ "setEventHandler:"
+ "setFilterPredicate:"
+ "setFlags:"
+ "setInvalidationHandler:"
+ "stringByAppendingPathComponent:"
+ "subsystem"
+ "threadIdentifier"
+ "truncateAtOffset:error:"
+ "type"
+ "v16@?0@\"OSLogEventProxy\"8"
+ "v24@?0@\"OSLogEventSource\"8@\"NSError\"16"
+ "v24@?0Q8@\"OSLogEventStreamPosition\"16"
+ "writeData:"
- "/var/mobile/Library/Logs/CrashReporter/DiagnosticLogs/Search"

```
