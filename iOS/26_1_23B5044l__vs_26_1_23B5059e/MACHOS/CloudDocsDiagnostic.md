## CloudDocsDiagnostic

> `/System/Library/PrivateFrameworks/iCloudDriveCore.framework/PlugIns/CloudDocsDiagnostic.appex/CloudDocsDiagnostic`

```diff

-4257.40.32.502.1
-  __TEXT.__text: 0x1444
-  __TEXT.__auth_stubs: 0x3b0
-  __TEXT.__objc_stubs: 0x420
-  __TEXT.__objc_methlist: 0x5c
-  __TEXT.__const: 0x90
-  __TEXT.__gcc_except_tab: 0x1d4
-  __TEXT.__cstring: 0x31f
-  __TEXT.__oslogstring: 0x203
+4257.40.57.0.1
+  __TEXT.__text: 0x2488
+  __TEXT.__auth_stubs: 0x3f0
+  __TEXT.__objc_stubs: 0x8c0
+  __TEXT.__objc_methlist: 0x74
+  __TEXT.__const: 0xb0
+  __TEXT.__gcc_except_tab: 0x368
+  __TEXT.__cstring: 0x49a
+  __TEXT.__oslogstring: 0x370
   __TEXT.__objc_classname: 0x1d
-  __TEXT.__objc_methname: 0x33e
-  __TEXT.__objc_methtype: 0x3e
-  __TEXT.__unwind_info: 0xa8
-  __DATA_CONST.__auth_got: 0x1e8
-  __DATA_CONST.__got: 0x88
-  __DATA_CONST.__const: 0x50
-  __DATA_CONST.__cfstring: 0x140
+  __TEXT.__objc_methname: 0x5c7
+  __TEXT.__objc_methtype: 0x51
+  __TEXT.__unwind_info: 0xe0
+  __DATA_CONST.__auth_got: 0x208
+  __DATA_CONST.__got: 0xc8
+  __DATA_CONST.__const: 0xc8
+  __DATA_CONST.__cfstring: 0x2e0
   __DATA_CONST.__objc_classlist: 0x8
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_intobj: 0x18
+  __DATA_CONST.__objc_arraydata: 0x10
+  __DATA_CONST.__objc_arrayobj: 0x18
   __DATA.__objc_const: 0x90
-  __DATA.__objc_selrefs: 0x110
+  __DATA.__objc_selrefs: 0x238
   __DATA.__objc_data: 0x50
   - /System/Library/Frameworks/Accounts.framework/Accounts
   - /System/Library/Frameworks/CFNetwork.framework/CFNetwork

   - /System/Library/PrivateFrameworks/CrashReporterSupport.framework/CrashReporterSupport
   - /System/Library/PrivateFrameworks/DiagnosticExtensions.framework/DiagnosticExtensions
   - /System/Library/PrivateFrameworks/GenerationalStorage.framework/GenerationalStorage
+  - /System/Library/PrivateFrameworks/LoggingSupport.framework/LoggingSupport
   - /System/Library/PrivateFrameworks/ManagedConfiguration.framework/ManagedConfiguration
   - /System/Library/PrivateFrameworks/MobileKeyBag.framework/MobileKeyBag
   - /System/Library/PrivateFrameworks/PowerLog.framework/PowerLog

   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libprequelite.dylib
   - /usr/lib/libsqlite3.dylib
-  UUID: A2A3EE60-B153-31A8-AF7D-6D02556FB0D6
-  Functions: 19
-  Symbols:   86
-  CStrings:  87
+  UUID: 45C5D21A-A9A7-370B-B8C7-E8E88E9150F7
+  Functions: 30
+  Symbols:   99
+  CStrings:  164
 
Symbols:
+ _CFAbsoluteTimeGetCurrent
+ _OBJC_CLASS_$_BRRuntimeBehavior
+ _OBJC_CLASS_$_NSCompoundPredicate
+ _OBJC_CLASS_$_NSConstantArray
+ _OBJC_CLASS_$_NSData
+ _OBJC_CLASS_$_NSDate
+ _OBJC_CLASS_$_NSDateFormatter
+ _OBJC_CLASS_$_NSPredicate
+ _OBJC_CLASS_$_OSLogEventStore
+ _OBJC_CLASS_$_OSLogEventStream
+ _objc_alloc_init
+ _objc_opt_new
+ _objc_release_x9
+ _objc_retain_x20
+ _objc_retain_x23
+ _unlink
- _BRActivityDump
- _fclose
- _fopen
CStrings:
+ "\nERROR: Log Collection could not complete, timed out."
+ "%@ 0x%05llx %@ %d %@(%@):%@ [%@] %@\n"
+ "-[CloudDocsDiagnosticExtension _dumpSystemLogsToOutputPath:]"
+ "-[CloudDocsDiagnosticExtension _dumpSystemLogsToOutputPath:]_block_invoke"
+ "@24@0:8Q16"
+ "CloudDocsDiagnosticLogs-%@-%llu.txt"
+ "Debug"
+ "Default"
+ "Error"
+ "Fault"
+ "Info"
+ "System Logs for File Sync"
+ "Unknown"
+ "[ERROR] Could not open: %@%@"
+ "[ERROR] Failed to create empty file: %@%@"
+ "[ERROR] Failed to create file: %@%@"
+ "[ERROR] Failed to prepare oslog stream%@"
+ "[ERROR] Failed to truncate file: %@ : %@%@"
+ "[ERROR] Failed writing log line '%@' to file %@: %@%@"
+ "[ERROR] Invalid oslog stream: reason = %lu%@"
+ "[ERROR] Timeout on getting oslog stream%@"
+ "[INFO] Dumping CloudDocs system logs%@"
+ "[INFO] Getting clouddocs oslog for past %f mins%@"
+ "[INFO] Writing to file: %@%@"
+ "_displayStringForLogType:"
+ "_dumpSystemLogsToOutputPath:"
+ "_logCollectionInterval"
+ "activateStreamFromDate:toDate:"
+ "category"
+ "closeFile"
+ "com.apple.clouddocs"
+ "com.apple.cloudkit"
+ "composedMessage"
+ "count"
+ "d16@0:8"
+ "dataUsingEncoding:"
+ "database backup for File Sync"
+ "database dump for File Sync"
+ "date"
+ "dateByAddingTimeInterval:"
+ "dateWithTimeIntervalSinceReferenceDate:"
+ "fileHandleForWritingAtPath:"
+ "fp_prettyDescription"
+ "fp_prettyPath"
+ "initWithSource:"
+ "invalidate"
+ "isInternalBuild"
+ "localStore"
+ "localizedDescription"
+ "logType"
+ "orPredicateWithSubpredicates:"
+ "predicateWithFormat:"
+ "prepareWithCompletionHandler:"
+ "process"
+ "processIdentifier"
+ "sender"
+ "setDateFormat:"
+ "setDisplayName:"
+ "setEventHandler:"
+ "setFilterPredicate:"
+ "setFlags:"
+ "setInvalidationHandler:"
+ "stringFromDate:"
+ "subsystem"
+ "subsystem == %@"
+ "threadIdentifier"
+ "truncateAtOffset:error:"
+ "v16@?0@\"OSLogEventProxy\"8"
+ "v24@?0@\"OSLogEventSource\"8@\"NSError\"16"
+ "v24@?0Q8@\"OSLogEventStreamPosition\"16"
+ "writeData:error:"
+ "writeToFile:options:error:"
+ "yyyy-MM-dd HH:mm:ss.SSS Z"
- "Spotlight/CoreSpotlight/NSFileProtectionCompleteUntilFirstUserAuthentication/index.spotlightV2/activityJournal.1"
- "[DEBUG] Don't dump the spotlight index from TimberLorry%@"
- "[INFO] Dumping spotlight%@"
- "_dumpSpotlightJournalToOutputPath:"
- "spotlight-dump-%@.txt"
- "stringByExpandingTildeInPath"
- "unable to dump spotlight journal at %s: %s"
- "w"
- "~/Library"

```
