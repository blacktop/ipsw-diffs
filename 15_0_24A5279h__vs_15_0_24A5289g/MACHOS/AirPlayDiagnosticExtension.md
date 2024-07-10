## AirPlayDiagnosticExtension

> `/System/Library/PrivateFrameworks/DiagnosticExtensions.framework/PlugIns/AirPlayDiagnosticExtension.appex/Contents/MacOS/AirPlayDiagnosticExtension`

```diff

-800.61.1.0.0
-  __TEXT.__text: 0x27c0
-  __TEXT.__auth_stubs: 0x350
-  __TEXT.__objc_stubs: 0x520
-  __TEXT.__objc_methlist: 0x14
-  __TEXT.__cstring: 0x9f1
-  __TEXT.__objc_classname: 0x1b
-  __TEXT.__objc_methname: 0x39c
-  __TEXT.__objc_methtype: 0xb
-  __TEXT.__const: 0x10
-  __TEXT.__gcc_except_tab: 0x184
-  __TEXT.__unwind_info: 0xa0
-  __DATA_CONST.__auth_got: 0x1b8
-  __DATA_CONST.__got: 0x128
+800.65.1.0.0
+  __TEXT.__text: 0x33f8
+  __TEXT.__auth_stubs: 0x270
+  __TEXT.__objc_stubs: 0xae0
+  __TEXT.__objc_methlist: 0x36c
+  __TEXT.__cstring: 0xa9b
+  __TEXT.__objc_classname: 0x6b
+  __TEXT.__objc_methname: 0x886
+  __TEXT.__objc_methtype: 0x1b4
+  __TEXT.__const: 0x8
+  __TEXT.__gcc_except_tab: 0xcc
+  __TEXT.__unwind_info: 0x130
+  __DATA_CONST.__auth_got: 0x148
+  __DATA_CONST.__got: 0x118
   __DATA_CONST.__const: 0xa0
-  __DATA_CONST.__cfstring: 0x160
-  __DATA_CONST.__objc_classlist: 0x8
+  __DATA_CONST.__cfstring: 0x2a0
+  __DATA_CONST.__objc_classlist: 0x20
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_intobj: 0x18
-  __DATA.__objc_const: 0x90
-  __DATA.__objc_selrefs: 0x150
-  __DATA.__objc_data: 0x50
-  __DATA.__data: 0xe0
-  __DATA.__bss: 0x24
+  __DATA_CONST.__objc_superrefs: 0x10
+  __DATA_CONST.__objc_intobj: 0x30
+  __DATA.__objc_const: 0x5f0
+  __DATA.__objc_selrefs: 0x2e8
+  __DATA.__objc_ivar: 0x44
+  __DATA.__objc_data: 0x140
+  __DATA.__data: 0x150
+  __DATA.__crash_info: 0x40
   - /System/Library/Frameworks/CoreFoundation.framework/Versions/A/CoreFoundation
   - /System/Library/Frameworks/CoreMedia.framework/Versions/A/CoreMedia
   - /System/Library/Frameworks/Foundation.framework/Versions/C/Foundation

   - /System/Library/PrivateFrameworks/DiagnosticExtensions.framework/Versions/A/DiagnosticExtensions
   - /System/Library/PrivateFrameworks/MediaExperience.framework/Versions/A/MediaExperience
   - /usr/lib/libSystem.B.dylib
-  - /usr/lib/libarchive.2.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 16
-  Symbols:   104
-  CStrings:  62
+  Functions: 73
+  Symbols:   93
+  CStrings:  77
 
Symbols:
+ _CFDictionaryGetDouble
+ _CFRetain
+ _CUObfuscatedPtr
+ _OBJC_CLASS_$_APDiagnosticsEndpoint
+ _OBJC_CLASS_$_APDiagnosticsEndpointActivity
+ _OBJC_CLASS_$_APDiagnosticsEngine
+ _OBJC_CLASS_$_DEUtils
+ _OBJC_CLASS_$_NSDate
+ _OBJC_CLASS_$_NSMutableArray
+ _OBJC_CLASS_$_NSObject
+ _OBJC_CLASS_$_NSPropertyListSerialization
+ _OBJC_CLASS_$_NSThread
+ _OBJC_METACLASS_$_APDiagnosticsEndpoint
+ _OBJC_METACLASS_$_APDiagnosticsEndpointActivity
+ _OBJC_METACLASS_$_APDiagnosticsEngine
+ _kFigEndpointProperty_ActivatedFeatures
+ _kFigEndpointProperty_ActivationSeed
+ _kFigEndpointProperty_ID
+ _objc_alloc
+ _objc_alloc_init
+ _objc_getProperty
+ _objc_msgSendSuper2
+ _objc_retainBlock
+ _objc_setProperty_atomic
+ _objc_storeStrong
+ _objc_sync_enter
+ _objc_sync_exit
- _AirPlayDiagnosticsGatherRemoteLogsArchiveFromAirPlaySDKReceivers
- _CFGetTypeID
- _CFPropertyListCreateData
- _FigEndpointExtendedGetFigEndpoint
- _FigEndpointGetTypeID
- _NSFilePathErrorKey
- _NSFilePosixPermissions
- _NSFileSize
- _NSOSStatusErrorDomain
- _OBJC_CLASS_$_NSArray
- _OBJC_CLASS_$_NSData
- _OBJC_CLASS_$_NSError
- _OBJC_CLASS_$_NSMutableSet
- _OBJC_CLASS_$_NSNumber
- _OBJC_CLASS_$_NSPredicate
- __Block_object_assign
- __Block_object_dispose
- __NSConcreteGlobalBlock
- _archive_entry_free
- _archive_entry_new
- _archive_entry_set_filetype
- _archive_entry_set_pathname
- _archive_entry_set_perm
- _archive_entry_set_size
- _archive_write_add_filter_gzip
- _archive_write_close
- _archive_write_data
- _archive_write_free
- _archive_write_header
- _archive_write_new
- _archive_write_open_filename
- _archive_write_set_format_pax_restricted
- _dispatch_semaphore_create
- _dispatch_semaphore_signal
- _dispatch_semaphore_wait
- _dispatch_time
- _mkpath
- _objc_retainAutorelease
CStrings:
+ "### [%!@(MISSING)] Property %!@(MISSING) err %!m(MISSING)"
+ "%!@(MISSING) - %!@(MISSING) - %!@(MISSING)"
+ "%!@(MISSING)-%!s(MISSING)"
+ "+[APDiagnosticsEndpoint discoveredEndpoint:]"
+ "-[APDiagnosticsEndpoint activateWithOptions:completion:]"
+ "-[APDiagnosticsEndpoint deactivate]"
+ "-[APDiagnosticsEndpoint propertyForKey:]"
+ "-[APDiagnosticsEndpoint retrieveLogsWithParameters:completion:]"
+ "-[APDiagnosticsEngine _activateAndRetrieveLogs:]"
+ "-[APDiagnosticsEngine _activateAndRetrieveLogs:]_block_invoke"
+ "-[APDiagnosticsEngine _handleAvailableRoutesChanged:]"
+ "-[APDiagnosticsEngine _handleEndpointDiscovered:]"
+ "-[APDiagnosticsEngine _joinWithTimeout]"
+ "-[APDiagnosticsEngine _prepare]"
+ "-[APDiagnosticsEngine _retrieveLogs:]_block_invoke"
+ "-[APDiagnosticsEngine _runDiscovery]"
+ "-[APDiagnosticsEngine _startDiscovery]"
+ "-[APDiagnosticsEngine _updateEndpoints]"
+ "-[APDiagnosticsEngine _writeInfoPlist:]"
+ "-[APDiagnosticsEngine _writeLogs:response:]"
+ "-[APDiagnosticsEngine run]"
+ "0x%!X(MISSING)"
+ "APDiagnosticsEndpoint"
+ "APDiagnosticsEngine"
+ "Activated"
+ "Activating"
+ "ActivatingFailed"
+ "AirPlayDiagnostics"
+ "Deactivated"
+ "Discovered"
+ "Error in client of APDiagnosticsEndpoint: -init unsupported, use -initWithEndpoint:state:"
+ "ReceivingLogsFailed"
+ "RetrievedLogs"
+ "RetrievingLogs"
+ "UnknownManufacturer"
+ "UnknownModel"
+ "UnknownName"
+ "[%!@(MISSING)] ### Endpoint [%!@(MISSING)] timed out"
+ "[%!@(MISSING)] ### Failed to copy available routes: err %!m(MISSING)"
+ "[%!@(MISSING)] ### Failed to create directory for endpoint [%!@(MISSING)]%!?(MISSING){end}: %!@(MISSING)"
+ "[%!@(MISSING)] ### Failed to create run instance directory%!?(MISSING){end}: %!@(MISSING)"
+ "[%!@(MISSING)] ### Failed to create working directory"
+ "[%!@(MISSING)] ### Failed to obtain logs for endpoint [%!@(MISSING)]: err %!m(MISSING)"
+ "[%!@(MISSING)] ### Failed to serialize info plist for endpoint [%!@(MISSING)]%!?(MISSING){end}: %!@(MISSING)"
+ "[%!@(MISSING)] ### Failed to start discovery: err %!m(MISSING)"
+ "[%!@(MISSING)] ### Failed to write info plist for endpoint [%!@(MISSING)]%!?(MISSING){end}: %!@(MISSING)"
+ "[%!@(MISSING)] ### Failed to write logs for endpoint [%!@(MISSING)]: response is empty"
+ "[%!@(MISSING)] ### Failed to write logs to file for endpoint [%!@(MISSING)]%!?(MISSING){end}: %!@(MISSING)"
+ "[%!@(MISSING)] Activate"
+ "[%!@(MISSING)] Activation completed for endpoint [%!@(MISSING)] %!'(MISSING)@ with error %!m(MISSING)"
+ "[%!@(MISSING)] Deactivating endpoint %!'(MISSING)@"
+ "[%!@(MISSING)] Discovered"
+ "[%!@(MISSING)] Endpoint [%!@(MISSING)] already activated for RC"
+ "[%!@(MISSING)] Endpoint [%!@(MISSING)] state %!@(MISSING)"
+ "[%!@(MISSING)] Found AirPlaySDK-based endpoint: [%!@(MISSING)] %!'(MISSING)@\n"
+ "[%!@(MISSING)] Gather remote logs%!?(MISSING){end} to %!@(MISSING)"
+ "[%!@(MISSING)] Gathered remote logs%!?(MISSING){end} archive %!@(MISSING)"
+ "[%!@(MISSING)] Retrieve Logs"
+ "[%!@(MISSING)] Retrieving AirPlay logs from endpoint [%!@(MISSING)] %!'(MISSING)@%!?(MISSING){end} into %!@(MISSING)\n"
+ "[%!@(MISSING)] Saving endpoint info from endpoint [%!@(MISSING)] %!'(MISSING)@%!?(MISSING){end} into %!@(MISSING)"
+ "[%!@(MISSING)] Send command completed for endpoint [%!@(MISSING)] %!'(MISSING)@ with status %!m(MISSING)"
+ "[%!@(MISSING)] Waiting for %!d(MISSING) endpoint(s)"
+ "[%!@(MISSING)] infoDict for endpoint [%!@(MISSING)] %!'(MISSING)@: %!@(MISSING)\n"
+ "discoveryDuration"
+ "gracePeriod"
+ "inParameters: %!@(MISSING)"
+ "v28@?0@\"APDiagnosticsEndpoint\"8i16^{__CFDictionary=}20"
+ "v36@?0@\"APDiagnosticsEndpoint\"8Q16Q24i32"
- " log: "
- "### Failed to write AirPlay logs%!?(MISSING){end} into file %!@(MISSING)\n"
- "### Failed to write info.plist%!?(MISSING){end} into file %!@(MISSING)\n"
- "### Route Changed -- logging into %!@(MISSING)\n"
- "%!@(MISSING)"
- "%!@(MISSING).tgz"
- "%!@(MISSING)_%!@(MISSING)"
- "%!@(MISSING)_%!@(MISSING)_"
- "/tmp"
- "/var/tmp/AirPlayDiagnostics"
- ": "
- "Activation completed for endpoint %!'(MISSING)@ with error %!m(MISSING)\n"
- "Adding file (%!l(MISSING)ld bytes)%!?(MISSING){end} into archive: %!@(MISSING)"
- "AirPlayDiagnosticEngine"
- "AirPlayDiagnostics-%!@(MISSING)"
- "AirPlayDiagnosticsGatherRemoteLogsArchiveFromAirPlaySDKReceivers"
- "B24@?0@8@\"NSDictionary\"16"
- "Called _AirPlayDiagnosticsCopyAirPlaySDKEndpoints on discoverer %!@(MISSING). %!d(MISSING) SDK-based endpoints=%!@(MISSING)\n"
- "Completed%!?(MISSING)s%!?(MISSING)@ error: %!d(MISSING)\n"
- "Creating baseDirectory [%!s(MISSING)] %!@(MISSING)\n"
- "Creating baseRemoteDirectory [%!s(MISSING)] %!@(MISSING)\n"
- "Deactivating endpoint %!'(MISSING)@"
- "FAILED"
- "Failed to collect log%!?(MISSING)s%!?(MISSING)'@ due to %!'(MISSING)@\n"
- "File content of: %!@(MISSING) ===> %!@(MISSING)\n"
- "Finish waiting for all logs\n"
- "Found AirPlaySDK-based endpoint: [%!{(MISSING)ptr}] %!@(MISSING)\n"
- "Gather remote logs%!?(MISSING){end} to %!@(MISSING)\n"
- "Gathered remote logs%!?(MISSING){end} archive %!@(MISSING)\n"
- "NSString * _Nullable AirPlayDiagnosticsGatherRemoteLogsArchiveFromAirPlaySDKReceivers(NSString * _Nullable __strong)"
- "Prepare to archive content%!?(MISSING){end} in\n\t%!@(MISSING)\n\tinto ===>\n\t%!@(MISSING)\n"
- "Retrieving AirPlay logs from endpoint %!'(MISSING)@%!?(MISSING){end} into %!@(MISSING)\n"
- "SUCCEEDED"
- "Saving endpoint info from endpoint %!'(MISSING)@%!?(MISSING){end} into %!@(MISSING)\n"
- "Send command completed for endpoint %!'(MISSING)@ with status %!m(MISSING)\n"
- "Start waiting for all logs\n"
- "Timed out waiting for logging completion. Pending log count: %!d(MISSING).\n"
- "_AirPlayDiagnosticsEndpointSendCommandCompletionCallback"
- "_AirPlayDiagnosticsGetAirPlaySDKEndpoints"
- "_AirPlayDiagnosticsGetEndpointManufacturerModelName"
- "_AirPlayDiagnosticsGetEndpointName"
- "_AirPlayDiagnosticsSaveEndpointInfoIntoPlist"
- "infoDict for endpoint %!'(MISSING)@: %!@(MISSING)\n"
- "v16@?0@\"NSNotification\"8"
- "v32@?0@8Q16^B24"
- "void _AirPlayDiagnosticsArchiveLogs(NSString *__strong, NSString *__strong, NSString *__strong)"
- "void _AirPlayDiagnosticsEndpointActivationCompletionCallback(FigEndpointRef, FigEndpointFeatures, uint64_t, OSStatus, void *)"
- "void _AirPlayDiagnosticsEndpointSendCommandCompletionCallback(FigEndpointExtendedRef, OSStatus, CFDictionaryRef, void *)"
- "void _AirPlayDiagnosticsHandleRoutesChanged(NSNotification *__strong, NSString *__strong)"
- "void _AirPlayDiagnosticsHandleRoutesChanged(NSNotification *__strong, NSString *__strong)_block_invoke"
- "void _AirPlayDiagnosticsSaveEndpointInfoIntoPlist(FigEndpointRef, NSString *__strong)"
- "void _AirPlayDiagnosticsSignalLogDone(NSString *__strong, OSStatus)"
- "void _AirPlayDiagnosticsWaitForAllLogs(void)"

```
