## SpotlightDiagnostic

> `/System/Library/PrivateFrameworks/Search.framework/PlugIns/SpotlightDiagnostic.appex/SpotlightDiagnostic`

```diff

-2314.10.1.0.18
-  __TEXT.__text: 0x7e8
-  __TEXT.__auth_stubs: 0x1e0
-  __TEXT.__objc_stubs: 0x240
+2326.1.0.11.0
+  __TEXT.__text: 0x1134
+  __TEXT.__auth_stubs: 0x290
+  __TEXT.__objc_stubs: 0x6e0
   __TEXT.__objc_methlist: 0x20
   __TEXT.__const: 0x68
-  __TEXT.__gcc_except_tab: 0x80
-  __TEXT.__cstring: 0x281
+  __TEXT.__gcc_except_tab: 0x1d0
+  __TEXT.__cstring: 0x73b
   __TEXT.__objc_classname: 0x1d
-  __TEXT.__objc_methname: 0x1d2
+  __TEXT.__objc_methname: 0x466
   __TEXT.__objc_methtype: 0x13
-  __TEXT.__unwind_info: 0x80
-  __DATA_CONST.__auth_got: 0x100
-  __DATA_CONST.__got: 0x58
-  __DATA_CONST.__const: 0x68
-  __DATA_CONST.__cfstring: 0x1e0
+  __TEXT.__unwind_info: 0x90
+  __DATA_CONST.__auth_got: 0x158
+  __DATA_CONST.__got: 0x90
+  __DATA_CONST.__const: 0xe0
+  __DATA_CONST.__cfstring: 0x540
   __DATA_CONST.__objc_classlist: 0x8
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_classrefs: 0x30
+  __DATA_CONST.__objc_arraydata: 0x68
+  __DATA_CONST.__objc_arrayobj: 0x30
   __DATA.__objc_const: 0x90
-  __DATA.__objc_selrefs: 0xa0
+  __DATA.__objc_selrefs: 0x1c8
   __DATA.__objc_data: 0x50
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/CoreSpotlight.framework/CoreSpotlight

   - /System/Library/PrivateFrameworks/LoggingSupport.framework/LoggingSupport
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 6
-  Symbols:   61
-  CStrings:  39
+  Functions: 9
+  Symbols:   74
+  CStrings:  108
 
Symbols:
+ _CFAbsoluteTimeGetCurrent
+ _NSTemporaryDirectory
+ _OBJC_CLASS_$_NSConstantArray
+ ___kCFBooleanTrue
+ _objc_alloc
+ _objc_autoreleasePoolPop
+ _objc_autoreleasePoolPush
+ _objc_release_x26
+ _objc_release_x27
+ _objc_release_x28
+ _objc_retainAutorelease
+ _objc_retain_x27
+ _unlink
CStrings:
+ "%!@(MISSING) 0x%!l(MISSING)lx %!s(MISSING) %!d(MISSING) %!@(MISSING)(%!@(MISSING)):%!@(MISSING) [%!@(MISSING)] %!@(MISSING)\n"
+ "CoreSpotlight"
+ "CoreSpotlightService"
+ "DEExtensionHostAppKey"
+ "ERROR"
+ "FAULT"
+ "Metadata"
+ "MetadataUtilities"
+ "MobileSpotlightIndex"
+ "SearchFramework"
+ "SpotlightDaemon"
+ "SpotlightDiagnosticLogs-%!l(MISSING)lu.log"
+ "SpotlightFramework"
+ "SpotlightIndex"
+ "SpotlightIndexUtilities"
+ "SpotlightResources"
+ "SpotlightServices"
+ "UTF8String"
+ "[SpotlightDiagnosticExtension attachmentsForParameters:ABC] Could not open: %!s(MISSING)"
+ "[SpotlightDiagnosticExtension attachmentsForParameters:ABC] Failed to create file: %!s(MISSING)"
+ "[SpotlightDiagnosticExtension attachmentsForParameters:ABC] Failed to prepare oslog stream"
+ "[SpotlightDiagnosticExtension attachmentsForParameters:ABC] Failed to truncate file: %!s(MISSING)"
+ "[SpotlightDiagnosticExtension attachmentsForParameters:ABC] Getting spotlight oslog past 15 mins error/fault level"
+ "[SpotlightDiagnosticExtension attachmentsForParameters:ABC] Invalid oslog stream: reason = %!l(MISSING)u"
+ "[SpotlightDiagnosticExtension attachmentsForParameters:ABC] Timeout on getting oslog stream"
+ "[SpotlightDiagnosticExtension attachmentsForParameters:ABC] Writing to file: %!s(MISSING)"
+ "activateStreamFromDate:toDate:"
+ "array"
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
+ "process == %!@(MISSING)"
+ "processIdentifier"
+ "searchd"
+ "sender"
+ "setDeleteOnAttach:"
+ "setEventHandler:"
+ "setFilterPredicate:"
+ "setFlags:"
+ "setInvalidationHandler:"
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

```
