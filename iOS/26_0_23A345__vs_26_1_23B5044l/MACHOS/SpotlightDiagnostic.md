## SpotlightDiagnostic

> `/System/Library/PrivateFrameworks/Search.framework/PlugIns/SpotlightDiagnostic.appex/SpotlightDiagnostic`

```diff

-2393.100.0.0.0
-  __TEXT.__text: 0xe30
-  __TEXT.__auth_stubs: 0x230
-  __TEXT.__objc_stubs: 0x320
-  __TEXT.__objc_methlist: 0x20
-  __TEXT.__const: 0x70
-  __TEXT.__gcc_except_tab: 0x16c
-  __TEXT.__cstring: 0x327
-  __TEXT.__objc_classname: 0x1d
-  __TEXT.__objc_methname: 0x279
-  __TEXT.__objc_methtype: 0x13
-  __TEXT.__dlopen_cstrs: 0x3a
-  __TEXT.__unwind_info: 0xa0
-  __DATA_CONST.__auth_got: 0x128
-  __DATA_CONST.__got: 0x70
-  __DATA_CONST.__const: 0xc8
-  __DATA_CONST.__cfstring: 0x280
+2400.8.1.0.0
+  __TEXT.__text: 0x1c78
+  __TEXT.__auth_stubs: 0x380
+  __TEXT.__objc_stubs: 0x8c0
+  __TEXT.__objc_methlist: 0x5c
+  __TEXT.__const: 0x78
+  __TEXT.__gcc_except_tab: 0x2a8
+  __TEXT.__cstring: 0x464
+  __TEXT.__oslogstring: 0x435
+  __TEXT.__objc_classname: 0x56
+  __TEXT.__objc_methname: 0x652
+  __TEXT.__objc_methtype: 0x73
+  __TEXT.__unwind_info: 0xc8
+  __DATA_CONST.__auth_got: 0x1d0
+  __DATA_CONST.__got: 0xb8
+  __DATA_CONST.__const: 0x130
+  __DATA_CONST.__cfstring: 0x3e0
   __DATA_CONST.__objc_classlist: 0x8
+  __DATA_CONST.__objc_protolist: 0x10
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_classrefs: 0x28
-  __DATA.__objc_const: 0x90
-  __DATA.__objc_selrefs: 0xd8
+  __DATA_CONST.__objc_protorefs: 0x8
+  __DATA_CONST.__objc_arraydata: 0x68
+  __DATA_CONST.__objc_arrayobj: 0x30
+  __DATA.__objc_const: 0xb8
+  __DATA.__objc_selrefs: 0x248
   __DATA.__objc_data: 0x50
-  __DATA.__bss: 0x10
+  __DATA.__data: 0xc0
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/CoreSpotlight.framework/CoreSpotlight
   - /System/Library/Frameworks/Foundation.framework/Foundation
   - /System/Library/PrivateFrameworks/DiagnosticExtensions.framework/DiagnosticExtensions
   - /System/Library/PrivateFrameworks/LoggingSupport.framework/LoggingSupport
   - /System/Library/PrivateFrameworks/SoftLinking.framework/SoftLinking
+  - /System/Library/PrivateFrameworks/SpotlightDiagnostics.framework/SpotlightDiagnostics
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 20280C3A-869D-3E0F-A6C2-C84FF9C7A0D2
-  Functions: 9
-  Symbols:   68
-  CStrings:  76
+  UUID: 9C47389A-0BD2-31F7-9E01-FD13C79731CE
+  Functions: 32
+  Symbols:   94
+  CStrings:  169
 
Symbols:
+ _CFAbsoluteTimeGetCurrent
+ _NSTemporaryDirectory
+ _OBJC_CLASS_$_DEDaemonHelper
+ _OBJC_CLASS_$_DEUtils
+ _OBJC_CLASS_$_NSConstantArray
+ _OBJC_CLASS_$_NSXPCConnection
+ _OBJC_CLASS_$_NSXPCInterface
+ _OBJC_CLASS_$_SDCoreSpotlightDiagnosticClient
+ _SDIsAppleInternalInstall
+ _SDLogCategoryExtension
+ ___kCFBooleanTrue
+ __os_log_debug_impl
+ __os_log_error_impl
+ __os_log_impl
+ _dispatch_semaphore_create
+ _dispatch_semaphore_signal
+ _dispatch_semaphore_wait
+ _objc_alloc
+ _objc_autoreleasePoolPop
+ _objc_autoreleasePoolPush
+ _objc_release_x25
+ _objc_release_x26
+ _objc_release_x27
+ _objc_release_x9
+ _objc_retain_x19
+ _objc_retain_x22
+ _objc_retain_x24
+ _objc_retain_x27
+ _objc_storeStrong
+ _os_log_type_enabled
+ _os_variant_allows_internal_security_policies
+ _os_variant_has_internal_diagnostics
+ _unlink
- _NSLog
- _NSURLCreationDateKey
- _NSURLFileSizeKey
- __sl_dlopen
- _abort_report_np
- _free
- _objc_getClass
CStrings:
+ "%@ 0x%05llx %s %d %@(%@):%@ [%@] %@\n"
+ "(searchd|Spotlight|CoreSpotlightService|com.apple.spotlight.IndexAgent|spotlightknowledged|CoreSpotlightImportExtension*_iOS).*(ips|ips.synced)$"
+ "-[SpotlightDiagnosticExtension attachmentsForParameters:] - helperResultURL %@"
+ "CoreSpotlight"
+ "CoreSpotlight-status.log"
+ "CoreSpotlightService"
+ "DEPingDaemonProtocol"
+ "DESpotlightDiagnosticHelperProtocol"
+ "ERROR"
+ "Error writing status to file: %@"
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
+ "Status query timed out"
+ "UTF8String"
+ "Using temp directory %@"
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
+ "attachmentWithPathURL:"
+ "category"
+ "closeFile"
+ "com.apple.spotlight.diagnostic.helper"
+ "composedMessage"
+ "containsObject:"
+ "createFileAtPath:contents:attributes:"
+ "dataUsingEncoding:"
+ "date"
+ "dateByAddingTimeInterval:"
+ "dateWithTimeIntervalSinceReferenceDate:"
+ "defaultClientWithBundleID:protectionClass:"
+ "dispatch_semaphore for Spotlight diagnostics timed out."
+ "fileHandleForWritingAtPath:"
+ "fileURLWithPath:relativeToURL:"
+ "generateSandboxExtensionWithDestinationDir:pingTarget:"
+ "getStatus:protectionClasses:queue:completionHandler:"
+ "initWithMachServiceName:options:"
+ "initWithSource:"
+ "interfaceWithProtocol:"
+ "invalidate"
+ "issueDiagnose:privacyLevel:completionHandler:"
+ "localStore"
+ "localizedDescription"
+ "logType"
+ "orPredicateWithSubpredicates:"
+ "path"
+ "ping:"
+ "predicateWithFormat:"
+ "prepareWithCompletionHandler:"
+ "process"
+ "process == %@"
+ "processIdentifier"
+ "remoteObjectProxy"
+ "resume"
+ "runDiagnosticWithDestinationDir:sandboxExtension:replyURL:"
+ "runHelperWithDestination:"
+ "searchd"
+ "searchd diagnose error %@"
+ "searchd diagnose timed out"
+ "sender"
+ "setDeleteOnAttach:"
+ "setEventHandler:"
+ "setFilterPredicate:"
+ "setFlags:"
+ "setInvalidationHandler:"
+ "setRemoteObjectInterface:"
+ "stringByAppendingPathComponent:"
+ "stringWithFormat:"
+ "subsystem"
+ "threadIdentifier"
+ "truncateAtOffset:error:"
+ "type"
+ "uniqueTemporaryDirectory"
+ "v16@?0@\"NSURL\"8"
+ "v16@?0@\"OSLogEventProxy\"8"
+ "v24@0:8@?16"
+ "v24@0:8@?<v@?i>16"
+ "v24@?0@\"NSString\"8@\"NSError\"16"
+ "v24@?0@\"OSLogEventSource\"8@\"NSError\"16"
+ "v24@?0Q8@\"OSLogEventStreamPosition\"16"
+ "v40@0:8@\"NSURL\"16@\"NSString\"24@?<v@?@\"NSURL\">32"
+ "v40@0:8@16@24@?32"
+ "writeData:"
+ "writeToURL:atomically:encoding:error:"
- "%s"
- "(searchd|Spotlight|CoreSpotlightService|com.apple.spotlight.IndexAgent|spotlightknowledged|CoreSpotlight*Importer*|Search).*(ips|ips.synced)$"
- ":%@"
- "RMECacheEnumerator"
- "Unable to find class %s"
- "_searchd_.*(memgraph|lite_diag)$"
- "compare:"
- "dateWithTimeIntervalSinceNow:"
- "diagnose"
- "diagnose error %@"
- "diagnose_logq"
- "firstMatchInString:options:range:"
- "getLogPathsSortedByTime"
- "getResourceValue:forKey:error:"
- "softlink:r:path:/usr/lib/libMemoryResourceException.dylib"
- "stringByAppendingFormat:"
- "unsignedLongLongValue"
- "v8@?0"

```
