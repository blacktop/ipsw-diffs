## SpotlightDiagnostic

> `/System/Library/PrivateFrameworks/Search.framework/PlugIns/SpotlightDiagnostic.appex/SpotlightDiagnostic`

```diff

 2400.18.100.0.0
-  __TEXT.__text: 0x1f30
-  __TEXT.__auth_stubs: 0x400
-  __TEXT.__objc_stubs: 0x8a0
+  __TEXT.__text: 0x1158
+  __TEXT.__auth_stubs: 0x2e0
+  __TEXT.__objc_stubs: 0x3e0
   __TEXT.__objc_methlist: 0x5c
-  __TEXT.__const: 0x88
-  __TEXT.__gcc_except_tab: 0x25c
-  __TEXT.__cstring: 0x4a2
-  __TEXT.__oslogstring: 0x545
+  __TEXT.__const: 0x78
+  __TEXT.__gcc_except_tab: 0x7c
+  __TEXT.__cstring: 0x2be
+  __TEXT.__oslogstring: 0x216
   __TEXT.__objc_classname: 0x56
-  __TEXT.__objc_methname: 0x635
+  __TEXT.__objc_methname: 0x378
   __TEXT.__objc_methtype: 0x73
-  __TEXT.__unwind_info: 0xd0
-  __DATA_CONST.__auth_got: 0x210
-  __DATA_CONST.__got: 0xb0
-  __DATA_CONST.__const: 0xf0
-  __DATA_CONST.__cfstring: 0x420
+  __TEXT.__unwind_info: 0xb8
+  __DATA_CONST.__auth_got: 0x180
+  __DATA_CONST.__got: 0x70
+  __DATA_CONST.__const: 0x78
+  __DATA_CONST.__cfstring: 0x1c0
   __DATA_CONST.__objc_classlist: 0x8
   __DATA_CONST.__objc_protolist: 0x10
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_protorefs: 0x8
-  __DATA_CONST.__objc_arraydata: 0x68
-  __DATA_CONST.__objc_arrayobj: 0x30
+  __DATA_CONST.__objc_classrefs: 0x30
   __DATA.__objc_const: 0xb8
-  __DATA.__objc_selrefs: 0x240
+  __DATA.__objc_selrefs: 0x110
   __DATA.__objc_data: 0x50
   __DATA.__data: 0xc0
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation

   - /System/Library/PrivateFrameworks/SpotlightDiagnostics.framework/SpotlightDiagnostics
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 4B49C8C8-B1A9-3A8D-9883-3973A33559A5
-  Functions: 32
-  Symbols:   100
-  CStrings:  178
+  UUID: D718E63F-34EE-3921-BEE0-57F26A667291
+  Functions: 17
+  Symbols:   79
+  CStrings:  88
 
Symbols:
- _CFAbsoluteTimeGetCurrent
- _NSTemporaryDirectory
- _OBJC_CLASS_$_NSConstantArray
- _OBJC_EHTYPE_$_NSException
- ___kCFBooleanTrue
- _objc_autoreleasePoolPop
- _objc_autoreleasePoolPush
- _objc_begin_catch
- _objc_copyWeak
- _objc_destroyWeak
- _objc_end_catch
- _objc_enumerationMutation
- _objc_initWeak
- _objc_loadWeakRetained
- _objc_release_x9
- _objc_retainAutorelease
- _objc_retainAutoreleasedReturnValue
- _objc_retain_x1
- _objc_retain_x20
- _objc_retain_x27
- _unlink
CStrings:
- "%@ 0x%05llx %s %d %@(%@):%@ [%@] %@\n"
- "CoreSpotlight"
- "CoreSpotlightService"
- "DEExtensionHostAppKey"
- "ERROR"
- "FAULT"
- "Metadata"
- "MetadataUtilities"
- "MobileSpotlightIndex"
- "SearchFramework"
- "SpotlightDaemon"
- "SpotlightDiagnosticLogs-%llu.log"
- "SpotlightFramework"
- "SpotlightIndex"
- "SpotlightIndexUtilities"
- "SpotlightResources"
- "SpotlightServices"
- "UTF8String"
- "[SpotlightDiagnosticExtension attachmentsForParameters:ABC] Could not open: %s"
- "[SpotlightDiagnosticExtension attachmentsForParameters:ABC] Failed to create file: %s"
- "[SpotlightDiagnosticExtension attachmentsForParameters:ABC] Failed to prepare oslog stream"
- "[SpotlightDiagnosticExtension attachmentsForParameters:ABC] Failed to truncate file: %s"
- "[SpotlightDiagnosticExtension attachmentsForParameters:ABC] Failed to write log data: %@"
- "[SpotlightDiagnosticExtension attachmentsForParameters:ABC] Getting spotlight oslog past 15 mins error/fault level"
- "[SpotlightDiagnosticExtension attachmentsForParameters:ABC] Invalid oslog stream: reason = %lu"
- "[SpotlightDiagnosticExtension attachmentsForParameters:ABC] Timeout on getting oslog stream"
- "[SpotlightDiagnosticExtension attachmentsForParameters:ABC] Writing to file: %s"
- "activateStreamFromDate:toDate:"
- "array"
- "attachmentWithPath:"
- "category"
- "closeFile"
- "com.apple.symptomsd"
- "com.apple.symptomsd-diag"
- "composedMessage"
- "containsObject:"
- "countByEnumeratingWithState:objects:count:"
- "createFileAtPath:contents:attributes:"
- "dataUsingEncoding:"
- "date"
- "dateByAddingTimeInterval:"
- "dateWithTimeIntervalSinceReferenceDate:"
- "fileHandleForWritingAtPath:"
- "initWithSource:"
- "isEqualToString:"
- "localStore"
- "localizedDescription"
- "logType"
- "orPredicateWithSubpredicates:"
- "predicateWithFormat:"
- "prepareWithCompletionHandler:"
- "process"
- "process == %@"
- "processIdentifier"
- "reason"
- "searchd"
- "sender"
- "setDeleteOnAttach:"
- "setEventHandler:"
- "setFilterPredicate:"
- "setFlags:"
- "setInvalidationHandler:"
- "stringByAppendingPathComponent:"
- "subsystem"
- "threadIdentifier"
- "truncateAtOffset:error:"
- "type"
- "v16@?0@\"OSLogEventProxy\"8"
- "v24@?0@\"OSLogEventSource\"8@\"NSError\"16"
- "v24@?0Q8@\"OSLogEventStreamPosition\"16"
- "writeData:"

```
