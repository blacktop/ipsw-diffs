## SpotlightDiagnostic

> `/System/Library/PrivateFrameworks/Search.framework/PlugIns/SpotlightDiagnostic.appex/SpotlightDiagnostic`

```diff

-2333.22.13.0.3
-  __TEXT.__text: 0x7e8
-  __TEXT.__auth_stubs: 0x1e0
-  __TEXT.__objc_stubs: 0x240
+2333.41.0.1.0
+  __TEXT.__text: 0x1730
+  __TEXT.__auth_stubs: 0x2d0
+  __TEXT.__objc_stubs: 0x7a0
   __TEXT.__objc_methlist: 0x20
-  __TEXT.__const: 0x68
-  __TEXT.__gcc_except_tab: 0x80
-  __TEXT.__cstring: 0x281
+  __TEXT.__const: 0x70
+  __TEXT.__gcc_except_tab: 0x278
+  __TEXT.__cstring: 0x79e
   __TEXT.__objc_classname: 0x1d
-  __TEXT.__objc_methname: 0x1d2
+  __TEXT.__objc_methname: 0x4fc
   __TEXT.__objc_methtype: 0x13
-  __TEXT.__unwind_info: 0x80
-  __DATA_CONST.__auth_got: 0x100
-  __DATA_CONST.__got: 0x58
-  __DATA_CONST.__const: 0x68
-  __DATA_CONST.__cfstring: 0x1e0
+  __TEXT.__dlopen_cstrs: 0x3a
+  __TEXT.__unwind_info: 0xa8
+  __DATA_CONST.__auth_got: 0x178
+  __DATA_CONST.__got: 0xa0
+  __DATA_CONST.__const: 0x140
+  __DATA_CONST.__cfstring: 0x580
   __DATA_CONST.__objc_classlist: 0x8
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_classrefs: 0x30
+  __DATA_CONST.__objc_arraydata: 0x68
+  __DATA_CONST.__objc_arrayobj: 0x30
   __DATA.__objc_const: 0x90
-  __DATA.__objc_selrefs: 0xa0
+  __DATA.__objc_selrefs: 0x1f8
   __DATA.__objc_data: 0x50
+  __DATA.__bss: 0x10
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/CoreSpotlight.framework/CoreSpotlight
   - /System/Library/Frameworks/Foundation.framework/Foundation
   - /System/Library/PrivateFrameworks/DiagnosticExtensions.framework/DiagnosticExtensions
   - /System/Library/PrivateFrameworks/LoggingSupport.framework/LoggingSupport
+  - /System/Library/PrivateFrameworks/SoftLinking.framework/SoftLinking
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 6
-  Symbols:   61
-  CStrings:  39
+  Functions: 12
+  Symbols:   80
+  CStrings:  121
 
Symbols:
+ _CFAbsoluteTimeGetCurrent
+ _NSTemporaryDirectory
+ _NSURLCreationDateKey
+ _NSURLFileSizeKey
+ _OBJC_CLASS_$_NSConstantArray
+ ___kCFBooleanTrue
+ __sl_dlopen
+ _abort_report_np
+ _free
+ _objc_alloc
+ _objc_autoreleasePoolPop
+ _objc_autoreleasePoolPush
+ _objc_getClass
+ _objc_release_x26
+ _objc_release_x27
+ _objc_release_x28
+ _objc_retainAutorelease
+ _objc_retain_x19
+ _objc_retain_x20
+ _objc_retain_x27
+ _unlink
- _objc_release_x25
- _objc_retain_x24
CStrings:
+ "%@ 0x%05llx %s %d %@(%@):%@ [%@] %@\n"
+ "%s"
+ "CoreSpotlight"
+ "CoreSpotlightService"
+ "DEExtensionHostAppKey"
+ "ERROR"
+ "FAULT"
+ "Metadata"
+ "MetadataUtilities"
+ "MobileSpotlightIndex"
+ "RMECacheEnumerator"
+ "SearchFramework"
+ "SpotlightDaemon"
+ "SpotlightDiagnosticLogs-%llu.log"
+ "SpotlightFramework"
+ "SpotlightIndex"
+ "SpotlightIndexUtilities"
+ "SpotlightResources"
+ "SpotlightServices"
+ "UTF8String"
+ "Unable to find class %s"
+ "[SpotlightDiagnosticExtension attachmentsForParameters:ABC] Could not open: %s"
+ "[SpotlightDiagnosticExtension attachmentsForParameters:ABC] Failed to create file: %s"
+ "[SpotlightDiagnosticExtension attachmentsForParameters:ABC] Failed to prepare oslog stream"
+ "[SpotlightDiagnosticExtension attachmentsForParameters:ABC] Failed to truncate file: %s"
+ "[SpotlightDiagnosticExtension attachmentsForParameters:ABC] Getting spotlight oslog past 15 mins error/fault level"
+ "[SpotlightDiagnosticExtension attachmentsForParameters:ABC] Invalid oslog stream: reason = %lu"
+ "[SpotlightDiagnosticExtension attachmentsForParameters:ABC] Timeout on getting oslog stream"
+ "[SpotlightDiagnosticExtension attachmentsForParameters:ABC] Writing to file: %s"
+ "_searchd_.*(memgraph|lite_diag)$"
+ "activateStreamFromDate:toDate:"
+ "array"
+ "category"
+ "closeFile"
+ "com.apple.symptomsd"
+ "com.apple.symptomsd-diag"
+ "compare:"
+ "composedMessage"
+ "containsObject:"
+ "createFileAtPath:contents:attributes:"
+ "dataUsingEncoding:"
+ "date"
+ "dateByAddingTimeInterval:"
+ "dateWithTimeIntervalSinceNow:"
+ "dateWithTimeIntervalSinceReferenceDate:"
+ "diagnose_logq"
+ "fileHandleForWritingAtPath:"
+ "firstMatchInString:options:range:"
+ "getLogPathsSortedByTime"
+ "getResourceValue:forKey:error:"
+ "initWithSource:"
+ "invalidate"
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
+ "searchd"
+ "sender"
+ "setDeleteOnAttach:"
+ "setEventHandler:"
+ "setFilterPredicate:"
+ "setFlags:"
+ "setInvalidationHandler:"
+ "softlink:r:path:/usr/lib/libMemoryResourceException.dylib"
+ "stringByAppendingPathComponent:"
+ "stringWithFormat:"
+ "subsystem"
+ "threadIdentifier"
+ "truncateAtOffset:error:"
+ "type"
+ "unsignedLongLongValue"
+ "v16@?0@\"OSLogEventProxy\"8"
+ "v24@?0@\"OSLogEventSource\"8@\"NSError\"16"
+ "v24@?0Q8@\"OSLogEventStreamPosition\"16"
+ "v8@?0"
+ "writeData:"

```
