## SpotlightDiagnostic

> `/System/Library/PrivateFrameworks/Search.framework/PlugIns/SpotlightDiagnostic.appex/SpotlightDiagnostic`

```diff

-2333.50.1.0.0
-  __TEXT.__text: 0xe30
-  __TEXT.__auth_stubs: 0x230
-  __TEXT.__objc_stubs: 0x320
+2333.55.0.0.0
+  __TEXT.__text: 0x1730
+  __TEXT.__auth_stubs: 0x2d0
+  __TEXT.__objc_stubs: 0x7a0
   __TEXT.__objc_methlist: 0x20
   __TEXT.__const: 0x70
-  __TEXT.__gcc_except_tab: 0x16c
-  __TEXT.__cstring: 0x327
+  __TEXT.__gcc_except_tab: 0x278
+  __TEXT.__cstring: 0x79e
   __TEXT.__objc_classname: 0x1d
-  __TEXT.__objc_methname: 0x279
+  __TEXT.__objc_methname: 0x4fc
   __TEXT.__objc_methtype: 0x13
   __TEXT.__dlopen_cstrs: 0x3a
-  __TEXT.__unwind_info: 0xa0
-  __DATA_CONST.__auth_got: 0x128
-  __DATA_CONST.__got: 0x70
-  __DATA_CONST.__const: 0xc8
-  __DATA_CONST.__cfstring: 0x280
+  __TEXT.__unwind_info: 0xa8
+  __DATA_CONST.__auth_got: 0x178
+  __DATA_CONST.__got: 0xa0
+  __DATA_CONST.__const: 0x140
+  __DATA_CONST.__cfstring: 0x580
   __DATA_CONST.__objc_classlist: 0x8
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_classrefs: 0x28
+  __DATA_CONST.__objc_arraydata: 0x68
+  __DATA_CONST.__objc_arrayobj: 0x30
   __DATA.__objc_const: 0x90
-  __DATA.__objc_selrefs: 0xd8
+  __DATA.__objc_selrefs: 0x1f8
   __DATA.__objc_data: 0x50
   __DATA.__bss: 0x10
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation

   - /System/Library/PrivateFrameworks/SoftLinking.framework/SoftLinking
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: D4B15C58-E4BD-355E-AEB9-7C7C8A78C758
-  Functions: 9
-  Symbols:   68
-  CStrings:  76
+  UUID: 7A4FB820-5EB1-32DA-9EEB-203F0BCBC68F
+  Functions: 12
+  Symbols:   80
+  CStrings:  165
 
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
+ _objc_retain_x19
+ _objc_retain_x27
+ _unlink
CStrings:
+ "%@ 0x%05llx %s %d %@(%@):%@ [%@] %@\n"
+ "CoreSpotlight"
+ "CoreSpotlightService"
+ "ERROR"
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
+ "[SpotlightDiagnosticExtension attachmentsForParameters:ABC] Could not open: %s"
+ "[SpotlightDiagnosticExtension attachmentsForParameters:ABC] Failed to create file: %s"
+ "[SpotlightDiagnosticExtension attachmentsForParameters:ABC] Failed to prepare oslog stream"
+ "[SpotlightDiagnosticExtension attachmentsForParameters:ABC] Failed to truncate file: %s"
+ "[SpotlightDiagnosticExtension attachmentsForParameters:ABC] Getting spotlight oslog past 15 mins error/fault level"
+ "[SpotlightDiagnosticExtension attachmentsForParameters:ABC] Invalid oslog stream: reason = %lu"
+ "[SpotlightDiagnosticExtension attachmentsForParameters:ABC] Timeout on getting oslog stream"
+ "[SpotlightDiagnosticExtension attachmentsForParameters:ABC] Writing to file: %s"
+ "activateStreamFromDate:toDate:"
+ "array"
+ "category"
+ "closeFile"
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
