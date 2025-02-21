## Logging

> `/System/Library/Trace/Providers/Logging.bundle/Logging`

```diff

-65.2.0.0.0
-  __TEXT.__text: 0xc8c
-  __TEXT.__auth_stubs: 0x240
-  __TEXT.__objc_stubs: 0x420
-  __TEXT.__objc_methlist: 0x80
-  __TEXT.__const: 0x58
-  __TEXT.__gcc_except_tab: 0x38
-  __TEXT.__cstring: 0x4a5
-  __TEXT.__objc_classname: 0x26
-  __TEXT.__objc_methname: 0x48e
-  __TEXT.__objc_methtype: 0x1a2
-  __TEXT.__unwind_info: 0xa8
-  __DATA_CONST.__auth_got: 0x130
-  __DATA_CONST.__got: 0x78
-  __DATA_CONST.__const: 0x120
-  __DATA_CONST.__cfstring: 0x380
+84.100.16.0.0
+  __TEXT.__text: 0x522c
+  __TEXT.__auth_stubs: 0x790
+  __TEXT.__objc_methlist: 0x170
+  __TEXT.__const: 0x596
+  __TEXT.__cstring: 0x70c
+  __TEXT.__swift5_typeref: 0x1e7
+  __TEXT.__swift5_capture: 0x88
+  __TEXT.__objc_methname: 0x331
+  __TEXT.__constg_swiftt: 0xe0
+  __TEXT.__swift5_builtin: 0x28
+  __TEXT.__swift5_mpenum: 0x8
+  __TEXT.__swift5_reflstr: 0x1f5
+  __TEXT.__swift5_fieldmd: 0x14c
+  __TEXT.__swift5_assocty: 0xc0
+  __TEXT.__swift5_proto: 0x30
+  __TEXT.__swift5_types: 0x14
+  __TEXT.__objc_classname: 0x20
+  __TEXT.__objc_methtype: 0x17a
+  __TEXT.__unwind_info: 0x1e0
+  __TEXT.__eh_frame: 0xe8
+  __DATA_CONST.__auth_got: 0x3c8
+  __DATA_CONST.__got: 0x90
+  __DATA_CONST.__auth_ptr: 0x1b8
+  __DATA_CONST.__const: 0x488
   __DATA_CONST.__objc_classlist: 0x8
-  __DATA_CONST.__objc_protolist: 0x8
+  __DATA_CONST.__objc_protolist: 0x20
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA.__objc_const: 0x380
-  __DATA.__objc_selrefs: 0x148
-  __DATA.__objc_ivar: 0x20
-  __DATA.__objc_data: 0x50
-  __DATA.__data: 0x60
-  - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
+  __DATA_CONST.__objc_protorefs: 0x10
+  __DATA.__objc_const: 0x1f0
+  __DATA.__objc_selrefs: 0x130
+  __DATA.__objc_data: 0xf8
+  __DATA.__data: 0x218
+  __DATA.__bss: 0x650
   - /System/Library/Frameworks/Foundation.framework/Foundation
   - /System/Library/PrivateFrameworks/LoggingSupport.framework/LoggingSupport
   - /System/Library/PrivateFrameworks/SignpostSupport.framework/SignpostSupport
   - /System/Library/PrivateFrameworks/ktrace.framework/ktrace
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 17
-  Symbols:   68
-  CStrings:  109
+  - /usr/lib/swift/libswiftCore.dylib
+  - /usr/lib/swift/libswiftCoreFoundation.dylib
+  - /usr/lib/swift/libswiftDarwin.dylib
+  - /usr/lib/swift/libswiftDispatch.dylib
+  - /usr/lib/swift/libswiftOSLog.dylib
+  - /usr/lib/swift/libswiftObjectiveC.dylib
+  - /usr/lib/swift/libswiftSystem.dylib
+  - /usr/lib/swift/libswiftXPC.dylib
+  - /usr/lib/swift/libswift_Builtin_float.dylib
+  - /usr/lib/swift/libswift_errno.dylib
+  - /usr/lib/swift/libswift_math.dylib
+  - /usr/lib/swift/libswift_signal.dylib
+  - /usr/lib/swift/libswift_stdio.dylib
+  - /usr/lib/swift/libswift_time.dylib
+  - /usr/lib/swift/libswiftos.dylib
+  - /usr/lib/swift/libswiftsys_time.dylib
+  - /usr/lib/swift/libswiftunistd.dylib
+  Functions: 161
+  Symbols:   110
+  CStrings:  106
 
Symbols:
+ _OBJC_CLASS_$_OSLogPreferencesCategory
+ _OBJC_CLASS_$_OSLogPreferencesSubsystem
+ __Block_copy
+ __Block_release
+ ___chkstk_darwin
+ __swiftEmptyArrayStorage
+ __swiftEmptyDictionarySingleton
+ __swiftImmortalRefCount
+ __swift_FORCE_LOAD_$_swiftCoreFoundation
+ __swift_FORCE_LOAD_$_swiftDarwin
+ __swift_FORCE_LOAD_$_swiftDispatch
+ __swift_FORCE_LOAD_$_swiftFoundation
+ __swift_FORCE_LOAD_$_swiftOSLog
+ __swift_FORCE_LOAD_$_swiftObjectiveC
+ __swift_FORCE_LOAD_$_swiftXPC
+ __swift_FORCE_LOAD_$_swift_Builtin_float
+ __swift_FORCE_LOAD_$_swift_errno
+ __swift_FORCE_LOAD_$_swift_math
+ __swift_FORCE_LOAD_$_swift_signal
+ __swift_FORCE_LOAD_$_swift_stdio
+ __swift_FORCE_LOAD_$_swift_time
+ __swift_FORCE_LOAD_$_swiftos
+ __swift_FORCE_LOAD_$_swiftsys_time
+ __swift_FORCE_LOAD_$_swiftunistd
+ _ktrace_events_range
+ _ktrace_file_iterate
+ _objc_allocWithZone
+ _objc_msgSendSuper2
+ _objc_opt_self
+ _objc_release_x26
+ _objc_release_x28
+ _objc_retain_x22
+ _objc_retain_x25
+ _objc_retain_x27
+ _objc_retain_x28
+ _objc_retain_x8
+ _swift_allocError
+ _swift_allocObject
+ _swift_beginAccess
+ _swift_bridgeObjectRelease
+ _swift_bridgeObjectRetain
+ _swift_bridgeObjectRetain_n
+ _swift_deallocObject
+ _swift_dynamicCastObjCClass
+ _swift_endAccess
+ _swift_enumFn_getEnumTag
+ _swift_errorRelease
+ _swift_errorRetain
+ _swift_generic_assignWithCopy
+ _swift_generic_assignWithTake
+ _swift_generic_destroy
+ _swift_generic_initWithCopy
+ _swift_generic_initWithTake
+ _swift_generic_initializeBufferWithCopyOfBuffer
+ _swift_getEnumTagSinglePayloadGeneric
+ _swift_getErrorValue
+ _swift_getForeignTypeMetadata
+ _swift_getObjCClassFromMetadata
+ _swift_getObjCClassMetadata
+ _swift_getObjectType
+ _swift_getSingletonMetadata
+ _swift_getTypeByMangledNameInContext2
+ _swift_getTypeByMangledNameInContextInMetadataState2
+ _swift_getWitnessTable
+ _swift_initStructMetadataWithLayoutString
+ _swift_isUniquelyReferenced_nonNull_bridgeObject
+ _swift_release
+ _swift_retain
+ _swift_storeEnumTagSinglePayloadGeneric
+ _swift_unknownObjectRelease
+ _swift_unknownObjectRetain
+ _swift_updateClassMetadata2
+ _swift_willThrow
- _ATSLoggingProviderArchive
- _ATSLoggingProviderDisableOSLogCapture
- _ATSLoggingProviderDisableOSSignpostCapture
- _ATSLoggingProviderEnableOSLogCapture
- _ATSLoggingProviderEnableOSSignpostCapture
- _ATSLoggingProviderPredicate
- _ATSLoggingProviderRedactContent
- _NSLocalizedDescriptionKey
- _OBJC_CLASS_$_ATSLoggingProvider
- _OBJC_CLASS_$_NSDate
- _OBJC_CLASS_$_NSDictionary
- _OBJC_CLASS_$_NSError
- _OBJC_CLASS_$_NSMutableIndexSet
- _OBJC_CLASS_$_NSURL
- _OBJC_METACLASS_$_ATSLoggingProvider
- __Block_object_dispose
- __Unwind_Resume
- ___CFConstantStringClassReference
- ___error
- ___objc_personality_v0
- ___stack_chk_fail
- ___stack_chk_guard
- _dispatch_semaphore_signal
- _dispatch_semaphore_wait
- _objc_alloc
- _objc_claimAutoreleasedReturnValue
- _objc_retainAutorelease
- _objc_retainBlock
- _objc_retain_x1
- _objc_storeStrong
- _strerror
CStrings:
+ "@24@0:8^v16"
+ "B16@?0^v8"
+ "B32@0:8^v16^@24"
+ "B48@0:8@16^v24@32^@40"
+ "Earliest timestamp of the file has not been found."
+ "KTProviderLogger"
+ "Latest timestamp of the file has not been found."
+ "Log archive doesn't exist as a specified path."
+ "Log archive for amending not provided. Specify --archive [path] argument."
+ "Log source preparation failed: "
+ "Redacting is not available on this platform."
+ "Unsupported option: '"
+ "archivePath"
+ "com.apple.SwiftUI"
+ "com.apple.swift.concurrency"
+ "dealloc"
+ "initWithName:"
+ "initWithName:subsystem:"
+ "initializationError"
+ "log stream failed due to an unknown error"
+ "logger"
+ "logging data is already present in the file"
+ "modifiedCategories"
+ "os_log and os_signpost capture is both disabled."
+ "os_signpost and os_log data will be missing from trace: "
+ "recordingLayerOptions"
+ "reset"
+ "setSignpostEnabled:"
+ "setSignpostPersisted:"
+ "shouldRedactContent"
+ "streamFlags"
+ "swift-concurrency"
+ "swift-ui"
+ "v16@?0^{trace_point=QQQQQQII{timeval=qi}**i}8"
+ "v24@0:8@\"NSString\"16"
+ "v24@0:8@16"
+ "v24@0:8^v16"
+ "v32@0:8^v16^v24"
- "\x01\x12\x13"
- "@\"<KTProviderLogger>\""
- "@\"NSDate\""
- "@\"NSPredicate\""
- "@\"NSString\""
- "@\"NSURL\""
- "B"
- "Cannot redact the content, allow-list is not available; logging will be disabled"
- "Failed to capture earliest trace timestamp with error: %s"
- "Failed to prepare log source for unknown reason"
- "Failed to prepare log source: %@"
- "LoggingProvider"
- "Missing logarchive path. Use --Logging:archive=[path] to pass it"
- "Passed logarchive path doesn't exist"
- "Passed predicate is invalid ('%@'); logging will be disabled"
- "Q"
- "_appendLogsToFile:"
- "_archivePath"
- "_archiveURL"
- "_endDate"
- "_filterPredicate"
- "_findStartAndEndTimeForFile:"
- "_logger"
- "_shouldRedactLogContent"
- "_startDate"
- "_streamingFlags"
- "addIndex:"
- "bytes"
- "containsObject:"
- "dateWithTimeIntervalSince1970:"
- "dictionaryWithObjects:forKeys:count:"
- "errorWithDomain:code:userInfo:"
- "fileURLWithPath:"
- "indexSetWithIndex:"
- "initWithFormat:arguments:"
- "length"
- "localizedDescription"
- "log content"
- "log metadata"
- "objectForKeyedSubscript:"
- "os_signpost and os_log data will be missing from trace, due to error in extracting trace file start and end times."
- "predicateWithFormat:"
- "stringWithFormat:"

```
