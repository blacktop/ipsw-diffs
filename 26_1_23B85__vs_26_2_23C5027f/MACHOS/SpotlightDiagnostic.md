## SpotlightDiagnostic

> `/System/Library/PrivateFrameworks/Search.framework/PlugIns/SpotlightDiagnostic.appex/SpotlightDiagnostic`

```diff

-2400.14.100.0.0
-  __TEXT.__text: 0x1054
-  __TEXT.__auth_stubs: 0x2f0
-  __TEXT.__objc_stubs: 0x440
+2400.16.0.0.0
+  __TEXT.__text: 0x1ebc
+  __TEXT.__auth_stubs: 0x400
+  __TEXT.__objc_stubs: 0x880
   __TEXT.__objc_methlist: 0x5c
-  __TEXT.__const: 0x60
-  __TEXT.__gcc_except_tab: 0x144
-  __TEXT.__cstring: 0x280
-  __TEXT.__oslogstring: 0x15f
+  __TEXT.__const: 0x88
+  __TEXT.__gcc_except_tab: 0x25c
+  __TEXT.__cstring: 0x4a2
+  __TEXT.__oslogstring: 0x510
   __TEXT.__objc_classname: 0x56
-  __TEXT.__objc_methname: 0x3c9
+  __TEXT.__objc_methname: 0x609
   __TEXT.__objc_methtype: 0x73
-  __TEXT.__unwind_info: 0xb8
-  __DATA_CONST.__auth_got: 0x188
-  __DATA_CONST.__got: 0x80
-  __DATA_CONST.__const: 0xb8
-  __DATA_CONST.__cfstring: 0x180
+  __TEXT.__unwind_info: 0xd0
+  __DATA_CONST.__auth_got: 0x210
+  __DATA_CONST.__got: 0xb0
+  __DATA_CONST.__const: 0xf0
+  __DATA_CONST.__cfstring: 0x420
   __DATA_CONST.__objc_classlist: 0x8
   __DATA_CONST.__objc_protolist: 0x10
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_protorefs: 0x8
-  __DATA_CONST.__objc_classrefs: 0x30
+  __DATA_CONST.__objc_arraydata: 0x68
+  __DATA_CONST.__objc_arrayobj: 0x30
   __DATA.__objc_const: 0xb8
-  __DATA.__objc_selrefs: 0x128
+  __DATA.__objc_selrefs: 0x238
   __DATA.__objc_data: 0x50
   __DATA.__data: 0xc0
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation

   - /System/Library/PrivateFrameworks/SpotlightDiagnostics.framework/SpotlightDiagnostics
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: FA8A2094-A797-3C27-AB29-352F3778FA8D
-  Functions: 18
-  Symbols:   83
-  CStrings:  82
+  UUID: 8F110C2B-1FF1-3C8E-8064-6471195358AD
+  Functions: 32
+  Symbols:   100
+  CStrings:  176
 
Symbols:
+ _CFAbsoluteTimeGetCurrent
+ _NSTemporaryDirectory
+ _OBJC_CLASS_$_NSConstantArray
+ _OBJC_EHTYPE_$_NSException
+ _SDSearchDirectory
+ ___kCFBooleanTrue
+ _objc_autoreleasePoolPop
+ _objc_autoreleasePoolPush
+ _objc_begin_catch
+ _objc_copyWeak
+ _objc_destroyWeak
+ _objc_end_catch
+ _objc_initWeak
+ _objc_loadWeakRetained
+ _objc_release_x28
+ _objc_release_x9
+ _objc_retainAutorelease
+ _objc_retainAutoreleasedReturnValue
+ _objc_retain_x20
+ _objc_retain_x27
+ _unlink
- _OBJC_CLASS_$_CSSearchableIndex
- _OBJC_CLASS_$_NSPropertyListSerialization
- __NSConcreteGlobalBlock
- _objc_retain_x24
CStrings:
+ "%@ 0x%05llx %s %d %@(%@):%@ [%@] %@\n"
+ "%@/Ranking"
+ "%{public}s seedbuild: %d"
+ "-[SpotlightDiagnosticExtension attachmentsForParameters:]"
+ "CoreSpotlight"
+ "CoreSpotlight-heartbeat.log"
+ "CoreSpotlightService"
+ "DEExtensionHostAppKey"
+ "ERROR"
+ "Error writing heartbeat data: %@"
+ "FAULT"
+ "Metadata"
+ "MetadataUtilities"
+ "MobileSpotlightIndex"
+ "SearchFramework"
+ "SpotlightDaemon"
+ "SpotlightDiagnosticLogs-%llu.log"
+ "SpotlightFramework"
+ "SpotlightIndex"
+ "SpotlightIndexUtilities"
+ "SpotlightResources"
+ "SpotlightServices"
+ "UTF8String"
+ "Wrote heartbeat data to CoreSpotlight-heartbeat.log"
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
+ "attachmentList searching in %{private}@"
+ "category"
+ "closeFile"
+ "com.apple.symptomsd"
+ "com.apple.symptomsd-diag"
+ "composedMessage"
+ "containsObject:"
+ "createFileAtPath:contents:attributes:"
+ "dataUsingEncoding:"
+ "date"
+ "dateByAddingTimeInterval:"
+ "dateWithTimeIntervalSinceReferenceDate:"
+ "fileHandleForWritingAtPath:"
+ "getSpotlightHeartbeatData"
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
+ "spotlight_heartbeat.*"
+ "spotlight_index_drop.*"
+ "stringByAppendingPathComponent:"
+ "stringWithFormat:"
+ "subsystem"
+ "threadIdentifier"
+ "truncateAtOffset:error:"
+ "type"
+ "v16@?0@\"OSLogEventProxy\"8"
+ "v24@?0@\"OSLogEventSource\"8@\"NSError\"16"
+ "v24@?0Q8@\"OSLogEventStreamPosition\"16"
+ "writeData:"
- "/var/mobile/Library/Logs/CrashReporter/DiagnosticLogs/Search/Ranking"
- "_issueCommand:completionHandler:"
- "defaultSearchableIndex"
- "length"
- "propertyListWithData:options:format:error:"
- "taptoradar"
- "taptoradar error %@"

```
