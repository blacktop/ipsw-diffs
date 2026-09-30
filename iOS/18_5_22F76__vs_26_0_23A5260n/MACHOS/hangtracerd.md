## hangtracerd

> `/usr/libexec/hangtracerd`

```diff

-354.4.0.0.0
-  __TEXT.__text: 0x30e3c
-  __TEXT.__auth_stubs: 0xec0
-  __TEXT.__objc_stubs: 0x5340
-  __TEXT.__objc_methlist: 0x2014
-  __TEXT.__const: 0x2b8
-  __TEXT.__cstring: 0x4c27
-  __TEXT.__objc_classname: 0x31f
-  __TEXT.__objc_methname: 0x85a2
-  __TEXT.__objc_methtype: 0x1005
+375.0.0.0.0
+  __TEXT.__text: 0x34b48
+  __TEXT.__auth_stubs: 0x1020
+  __TEXT.__objc_stubs: 0x5620
+  __TEXT.__objc_methlist: 0x20cc
+  __TEXT.__const: 0x2d0
+  __TEXT.__cstring: 0x519d
+  __TEXT.__oslogstring: 0x630f
+  __TEXT.__objc_classname: 0x341
+  __TEXT.__objc_methname: 0x8964
+  __TEXT.__objc_methtype: 0x103a
   __TEXT.__gcc_except_tab: 0x57c
-  __TEXT.__oslogstring: 0x59cc
-  __TEXT.__unwind_info: 0x9a0
-  __DATA_CONST.__auth_got: 0x770
-  __DATA_CONST.__got: 0x3e8
+  __TEXT.__unwind_info: 0xa30
+  __DATA_CONST.__auth_got: 0x820
+  __DATA_CONST.__got: 0x460
   __DATA_CONST.__auth_ptr: 0x18
-  __DATA_CONST.__const: 0x1f08
-  __DATA_CONST.__cfstring: 0x63c0
-  __DATA_CONST.__objc_classlist: 0xf0
+  __DATA_CONST.__const: 0x2010
+  __DATA_CONST.__cfstring: 0x6a20
+  __DATA_CONST.__objc_classlist: 0xf8
   __DATA_CONST.__objc_protolist: 0x58
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_protorefs: 0x8

   __DATA_CONST.__objc_arrayobj: 0x18
   __DATA_CONST.__objc_intobj: 0x78
   __DATA_CONST.__objc_dictobj: 0x78
-  __DATA.__objc_const: 0x4950
-  __DATA.__objc_selrefs: 0x1a70
-  __DATA.__objc_ivar: 0x41c
-  __DATA.__objc_data: 0x960
+  __DATA.__objc_const: 0x4aa0
+  __DATA.__objc_selrefs: 0x1b38
+  __DATA.__objc_ivar: 0x42c
+  __DATA.__objc_data: 0x9b0
   __DATA.__data: 0x548
-  __DATA.__bss: 0xa98
-  __DATA.__common: 0x60
+  __DATA.__bss: 0xac0
+  __DATA.__common: 0x68
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/CoreGraphics.framework/CoreGraphics
   - /System/Library/Frameworks/CoreServices.framework/CoreServices

   - /usr/lib/libMobileGestalt.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libarchive.2.dylib
-  - /usr/lib/libnetwork.dylib
   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libtailspin.dylib
-  UUID: 7C2EABC8-EBAB-3BD6-B2E7-532895305677
-  Functions: 1115
-  Symbols:   375
-  CStrings:  3646
+  UUID: D1694CDA-9E16-3B90-8DFC-F555D3D86266
+  Functions: 1164
+  Symbols:   412
+  CStrings:  3830
 
Symbols:
+ _NSFileCreationDate
+ _NSFileType
+ _NSFileTypeRegular
+ _NSPOSIXErrorDomain
+ __xpc_type_array
+ __xpc_type_data
+ __xpc_type_date
+ __xpc_type_double
+ __xpc_type_endpoint
+ __xpc_type_fd
+ __xpc_type_int64
+ __xpc_type_null
+ __xpc_type_string
+ __xpc_type_uint64
+ __xpc_type_uuid
+ _proc_listpids
+ _sandbox_extension_consume
+ _sandbox_extension_release
+ _strcmp
+ _xpc_array_get_count
+ _xpc_array_get_value
+ _xpc_connection_send_message
+ _xpc_data_get_length
+ _xpc_date_get_value
+ _xpc_dictionary_apply
+ _xpc_dictionary_create_empty
+ _xpc_dictionary_create_reply
+ _xpc_dictionary_get_date
+ _xpc_dictionary_set_bool
+ _xpc_dictionary_set_string
+ _xpc_dictionary_set_uint64
+ _xpc_double_get_value
+ _xpc_fd_dup
+ _xpc_int64_get_value
+ _xpc_string_get_string_ptr
+ _xpc_uint64_get_value
+ _xpc_uuid_get_bytes
CStrings:
+ "\n%@]"
+ "\n%@}"
+ "\"%@\""
+ "\"<invalid string ptr>\""
+ "%@\"%@\": %@"
+ "%@%@"
+ "%@: Moving tailspin %@ to spool: %s\n"
+ "%f"
+ "%lld"
+ "%s, [HTHangreporterKickstartTelemetry collectTailspinSpoolData:error] collected data but did not successfully populate dictionary."
+ "%s: Checking tailspin processing rates for hangtracerd and hangreporter"
+ "%s: Did not collect hangreporter tailspin processing data because hangreporter is alive."
+ "%s: Error flag set in pidForProcessName, unable to check pid for hangreporter with error:%@"
+ "%s: Failed to collect hangreporter tailspin processing data with error: %@"
+ "%s: Failed to emit tailspin processing telemetry with error: %@"
+ "%s: Failed to retrive contents of directory at path %s with error: %@"
+ "%s: Found tailspin file: %@ in spool directory: %s"
+ "%s: No error flag set in pidForProcessName with return value=%d. Hangreporter is not alive."
+ "%s: Skipping non-regular file at path:%@"
+ "%s: Successfully emitted tailspin processing telemetry!"
+ "%s: Unable to get file attributes of file at path:%@ with error: %@"
+ "%{public}@: Moving tailspin %{public}@ to spool: %{public}@\n"
+ "+[HTHangreporterKickstartTelemetry collectTailspinSpoolData:error:]"
+ "+[HTHangreporterKickstartTelemetry emitTailspinProcessingEvent:error:]"
+ "<Connection: %s>"
+ "<Connection: unknown>"
+ "<Data: %zu bytes>"
+ "<Date: %@ (%lld ns)>"
+ "<Endpoint: %s>"
+ "<Endpoint: unknown>"
+ "<Error: %s>"
+ "<Error: unknown>"
+ "<FD: %d>"
+ "<FD: invalid>"
+ "<UUID: %@>"
+ "<UUID: invalid bytes>"
+ "<Unknown XPC Type: %s>"
+ "<Unknown XPC Type>"
+ "<null internal xpc_object_t>"
+ "<null xpc_object_t>"
+ "B24@?0r*8@\"NSObject<OS_xpc_object>\"16"
+ "B32@0:8@16^@24"
+ "B32@0:8^@16^@24"
+ "Collected tailspin data %@. Attempting to emit hangreporter tailspin processing telemetry."
+ "Created XPC Dictionary for HTHangLogs Client response: %@"
+ "Don't know how to handle %{public}@"
+ "Error accessing tailspin saves: %@"
+ "Error accessing tailspins processed: %@"
+ "Failed to consume sandbox extension %{public}s with error '%s'"
+ "Failed to fetch creation date for file %@"
+ "Failed to get hangreporter tailspins processed with error:%@"
+ "Failed to get successful tailspin saves with error:%@"
+ "Failed to move tailspin at %@ to spool directory path: %@"
+ "Failed to release sandbox extension with error '%s'"
+ "Failed to send message '%@' to HTHangLogsClient over connection '%@'"
+ "Found file: %@"
+ "Found matching pid:%d for processName:%s"
+ "Found tailspin: %@ over the threshold limit of %f seconds. Incrementing number of tailspins in spool over the reporting limit to %d"
+ "Found the following files with a creation date between %@ and %@: %@"
+ "HTFGTrackingTelemetryMinEmissionThresholdSec"
+ "HTFGTrackingTelemetryPersistentEmissionRateSec"
+ "HTHangreporterKickstartTelemetry"
+ "HTPrefs shouldEmitTelemetry=%d, telemetry emission disabled"
+ "HangTracerShouldEmitTelemetry"
+ "Hangreporter has processed more tailspins than hangtracerd has requested. tailspinsProcessed:%u successfulTailspinSaves:%u. This should never happen."
+ "Hangreporter is alive, not attempting to emit telemetry."
+ "I24@0:8^@16"
+ "Invalid class type %@ for key (%@): value (%@) pair. Values in %@ domain were modified"
+ "Missing value for key (%@) from tailspinDataDict: %@"
+ "Skipping abandoned tailspin file %@ in directory %s"
+ "Skipping non-tailspin file %@ in directory %s"
+ "Start Date: %lld is later than End Date: %lld"
+ "Successfully moved tailspin from %@ to spool directory path: %@"
+ "TB,R,V_shouldEmitTelemetry"
+ "Td,R,V_minFGEmissionThresholdSec"
+ "Td,R,V_persistentFGEmissionThresholdSec"
+ "Td,R,V_tailspinReportingThresholdSec"
+ "Unable to allocate pids buffer of size %d with error: %s"
+ "Unable to list all pids with error: %s"
+ "Updating oldest tailspin to %@, creation time was %f seconds before now"
+ "Value of %@ for key %@ is unexpected class %@. Values in %@ domain were modified"
+ "[\n"
+ "\\\""
+ "^{?=II[8{hangEvent=QQdAiCCCC^{_opaque_pthread_t}Qi[64c][256c]B^?AQAQAQBB}][10{HTAssertionInfo=QQQQ[64c]B}]iQAQ}"
+ "_minFGEmissionThresholdSec"
+ "_persistentFGEmissionThresholdSec"
+ "_resetHangreporterTailspinsProcessed"
+ "_resetKeysForTailspinProcessingTelemetry"
+ "_resetSuccessfulTailspinSaves"
+ "_shouldEmitTelemetry"
+ "_tailspinReportingThresholdSec"
+ "attributesOfItemAtPath:error:"
+ "checkForTimeouts"
+ "collectTailspinSpoolData:error:"
+ "com.apple.hangtracer.client"
+ "com.apple.hangtracer.tailspin_processing"
+ "com.apple.hangtracer.telemetry.error"
+ "componentsJoinedByString:"
+ "conclave limit"
+ "contentsOfDirectoryAtPath:error:"
+ "dateWithTimeIntervalSince1970:"
+ "emitTailspinProcessingEvent:error:"
+ "errorCode"
+ "false"
+ "getHangreporterTailspinsProcessed:"
+ "getSuccessfulTailspinSaves:"
+ "incrementHangreporterTailspinsProcessed"
+ "incrementSuccessfulTailspinSaves"
+ "initWithSuiteName:"
+ "initWithUUIDBytes:"
+ "minFGEmissionThresholdSec"
+ "moveAndTrackTailspinToSpoolDirectory:error:"
+ "oldestTailspinCreationSeconds"
+ "pathExtension"
+ "persistentFGEmissionThresholdSec"
+ "pidForProcessName"
+ "ping"
+ "processing.tailspin"
+ "rangeOfString:"
+ "sandboxExtension"
+ "setInteger:forKey:"
+ "shouldEmitTelemetry"
+ "sortUsingSelector:"
+ "success"
+ "successfulTailspinSaves"
+ "tailspinReportingThresholdSec"
+ "tailspinsInSpool"
+ "tailspinsOverReportingThresholds"
+ "tailspinsProcessed"
+ "tailspinsUnprocessed"
+ "timeIntervalSinceDate:"
+ "true"
+ "unblock deadlock"
+ "unblock thread limit"
- "%@: Moving tailspin to spool: %@\n"
- "%{public}@: Moving tailspin to spool: %{public}@\n"
- "Don't know how to handle %p"
- "^{?=II[8{hangEvent=QQdAiCCCC^{_opaque_pthread_t}Qi[64c][256c]B^?}][10{HTAssertionInfo=QQQQ[64c]B}]iQ}"

```
