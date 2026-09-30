## FileProviderDiagnosticExtension

> `/System/Library/PrivateFrameworks/FileProviderDaemon.framework/PlugIns/FileProviderDiagnosticExtension.appex/FileProviderDiagnosticExtension`

```diff

-2732.60.87.502.1
-  __TEXT.__text: 0x4d8
-  __TEXT.__auth_stubs: 0x1d0
-  __TEXT.__objc_stubs: 0x1c0
-  __TEXT.__objc_methlist: 0x14
-  __TEXT.__const: 0x20
-  __TEXT.__gcc_except_tab: 0x80
-  __TEXT.__cstring: 0x1f
-  __TEXT.__oslogstring: 0x76
+2732.60.111.0.0
+  __TEXT.__text: 0x1450
+  __TEXT.__auth_stubs: 0x300
+  __TEXT.__objc_stubs: 0x700
+  __TEXT.__objc_methlist: 0x2c
+  __TEXT.__const: 0x48
+  __TEXT.__gcc_except_tab: 0x21c
+  __TEXT.__cstring: 0x16f
+  __TEXT.__oslogstring: 0x46f
   __TEXT.__objc_classname: 0x20
-  __TEXT.__objc_methname: 0x15e
-  __TEXT.__objc_methtype: 0xb
-  __TEXT.__unwind_info: 0x80
-  __DATA_CONST.__auth_got: 0xf8
-  __DATA_CONST.__got: 0x48
-  __DATA_CONST.__const: 0x28
-  __DATA_CONST.__cfstring: 0x40
+  __TEXT.__objc_methname: 0x481
+  __TEXT.__objc_methtype: 0x16
+  __TEXT.__unwind_info: 0xb8
+  __DATA_CONST.__auth_got: 0x190
+  __DATA_CONST.__got: 0x98
+  __DATA_CONST.__const: 0xa0
+  __DATA_CONST.__cfstring: 0x220
   __DATA_CONST.__objc_classlist: 0x8
   __DATA_CONST.__objc_imageinfo: 0x8
+  __DATA_CONST.__objc_arraydata: 0x8
+  __DATA_CONST.__objc_arrayobj: 0x18
   __DATA.__objc_const: 0x90
-  __DATA.__objc_selrefs: 0x78
+  __DATA.__objc_selrefs: 0x1c8
   __DATA.__objc_data: 0x50
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/FileProvider.framework/FileProvider

   - /System/Library/PrivateFrameworks/FPFS.framework/FPFS
   - /System/Library/PrivateFrameworks/FileProviderDaemon.framework/FileProviderDaemon
   - /System/Library/PrivateFrameworks/GenerationalStorage.framework/GenerationalStorage
+  - /System/Library/PrivateFrameworks/LoggingSupport.framework/LoggingSupport
   - /System/Library/PrivateFrameworks/SpaceAttribution.framework/SpaceAttribution
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libprequelite.dylib
-  Functions: 5
-  Symbols:   47
-  CStrings:  22
+  Functions: 23
+  Symbols:   77
+  CStrings:  93
 
Symbols:
+ _CFAbsoluteTimeGetCurrent
+ _OBJC_CLASS_$_FPCTLTermDumper
+ _OBJC_CLASS_$_NSCompoundPredicate
+ _OBJC_CLASS_$_NSConstantArray
+ _OBJC_CLASS_$_NSData
+ _OBJC_CLASS_$_NSDate
+ _OBJC_CLASS_$_NSFileManager
+ _OBJC_CLASS_$_NSPredicate
+ _OBJC_CLASS_$_NSString
+ _OBJC_CLASS_$_OSLogEventStore
+ _OBJC_CLASS_$_OSLogEventStream
+ __Block_object_dispose
+ ___kCFBooleanFalse
+ __os_log_impl
+ _dispatch_group_create
+ _dispatch_group_enter
+ _dispatch_group_leave
+ _dispatch_group_wait
+ _dispatch_time
+ _objc_alloc_init
+ _objc_enumerationMutation
+ _objc_release
+ _objc_release_x24
+ _objc_release_x26
+ _objc_release_x27
+ _objc_release_x28
+ _objc_release_x9
+ _objc_retain_x25
+ _objc_retain_x26
+ _objc_retain_x27
+ _objc_retain_x8
- _objc_retain_x22
CStrings:
+ "%!@(MISSING) 0x%!l(MISSING)lx %!@(MISSING) %!d(MISSING) %!@(MISSING)(%!@(MISSING)):%!@(MISSING) [%!@(MISSING)] %!@(MISSING)\n"
+ ":de_parameter"
+ "@24@0:8Q16"
+ "DEExtensionHostAppKey"
+ "Debug"
+ "Default"
+ "Error"
+ "Fault"
+ "Feedback Assistant"
+ "FileProviderDiagnosticLogs-%!l(MISSING)lu.log"
+ "Info"
+ "TEST-CANARY\n"
+ "URLByAppendingPathComponent:isDirectory:"
+ "UTF8String"
+ "Unknown"
+ "[DEBUG] ┏%!l(MISSING)lx dumping FP domains for %!@(MISSING)"
+ "[ERROR] [FileProviderDiagnosticExtension attachmentsForParameters:ABC] Could not open: %!s(MISSING)"
+ "[ERROR] [FileProviderDiagnosticExtension attachmentsForParameters:ABC] Error could not capture logs"
+ "[ERROR] [FileProviderDiagnosticExtension attachmentsForParameters:ABC] Failed to create empty file: %!@(MISSING)"
+ "[ERROR] [FileProviderDiagnosticExtension attachmentsForParameters:ABC] Failed to create file: %!s(MISSING)"
+ "[ERROR] [FileProviderDiagnosticExtension attachmentsForParameters:ABC] Failed to prepare oslog stream"
+ "[ERROR] [FileProviderDiagnosticExtension attachmentsForParameters:ABC] Failed to truncate file: %!s(MISSING) : %!@(MISSING)"
+ "[ERROR] [FileProviderDiagnosticExtension attachmentsForParameters:ABC] Invalid oslog stream: reason = %!l(MISSING)u"
+ "[ERROR] [FileProviderDiagnosticExtension attachmentsForParameters:ABC] Timeout on getting oslog stream"
+ "[ERROR] [FileProviderDiagnosticExtension attachmentsForParameters:ABC] Writing to file: %!s(MISSING)"
+ "[INFO] [FileProviderDiagnosticExtension attachmentsForParameters:ABC] Getting fileprovider oslog for past 15 mins"
+ "_displayStringForLogType:"
+ "_logAttachmentItemWithTempURL:"
+ "activateStreamFromDate:toDate:"
+ "category"
+ "closeFile"
+ "com.apple.FileProvider"
+ "composedMessage"
+ "count"
+ "countByEnumeratingWithState:objects:count:"
+ "dataUsingEncoding:"
+ "date"
+ "dateByAddingTimeInterval:"
+ "dateWithTimeIntervalSinceReferenceDate:"
+ "defaultManager"
+ "fileDescriptor"
+ "fileHandleForWritingAtPath:"
+ "initWithFd:forceColor:"
+ "initWithSource:"
+ "invalidate"
+ "isEqualToString:"
+ "localStore"
+ "localizedDescription"
+ "logType"
+ "objectForKeyedSubscript:"
+ "orPredicateWithSubpredicates:"
+ "predicateWithFormat:"
+ "prepareWithCompletionHandler:"
+ "process"
+ "processIdentifier"
+ "sender"
+ "setEventHandler:"
+ "setFilterPredicate:"
+ "setFlags:"
+ "setInvalidationHandler:"
+ "stringWithFormat:"
+ "subsystem"
+ "subsystem == %!@(MISSING)"
+ "test_provider"
+ "threadIdentifier"
+ "truncateAtOffset:error:"
+ "v16@?0@\"OSLogEventProxy\"8"
+ "v24@?0@\"OSLogEventSource\"8@\"NSError\"16"
+ "v24@?0Q8@\"OSLogEventStreamPosition\"16"
+ "write:"
+ "writeData:"
+ "writeToFile:options:error:"
- "[DEBUG] ┏%!l(MISSING)lx dumping FP domains"

```
