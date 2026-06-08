## datamigratorhelper

> `/System/Library/PrivateFrameworks/DataMigration.framework/XPCServices/datamigratorhelper.xpc/datamigratorhelper`

```diff

-2842.4.0.0.0
-  __TEXT.__text: 0x1384
-  __TEXT.__auth_stubs: 0x3a0
-  __TEXT.__objc_stubs: 0x260
-  __TEXT.__const: 0x30
-  __TEXT.__oslogstring: 0x25e
-  __TEXT.__cstring: 0x37e
-  __TEXT.__objc_methname: 0x1b1
-  __TEXT.__unwind_info: 0xa0
-  __DATA_CONST.__auth_got: 0x1d8
-  __DATA_CONST.__got: 0x68
-  __DATA_CONST.__const: 0x128
-  __DATA_CONST.__cfstring: 0x120
+2851.0.0.0.0
+  __TEXT.__text: 0x2368
+  __TEXT.__auth_stubs: 0x540
+  __TEXT.__objc_stubs: 0x6c0
+  __TEXT.__objc_methlist: 0x22c
+  __TEXT.__const: 0x48
+  __TEXT.__oslogstring: 0x397
+  __TEXT.__cstring: 0x458
+  __TEXT.__gcc_except_tab: 0xa0
+  __TEXT.__objc_methname: 0x739
+  __TEXT.__objc_classname: 0x2f
+  __TEXT.__objc_methtype: 0x1a3
+  __TEXT.__unwind_info: 0xf8
+  __DATA_CONST.__const: 0x1f0
+  __DATA_CONST.__cfstring: 0x200
+  __DATA_CONST.__objc_classlist: 0x8
+  __DATA_CONST.__objc_protolist: 0x10
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA.__objc_selrefs: 0x98
-  __DATA.__data: 0x4
-  __DATA.__bss: 0x20
+  __DATA_CONST.__objc_superrefs: 0x8
+  __DATA_CONST.__auth_got: 0x2b0
+  __DATA_CONST.__got: 0x90
+  __DATA.__objc_const: 0x360
+  __DATA.__objc_selrefs: 0x280
+  __DATA.__objc_ivar: 0x1c
+  __DATA.__objc_data: 0x50
+  __DATA.__data: 0xc8
+  __DATA.__bss: 0x30
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/Foundation.framework/Foundation
+  - /System/Library/PrivateFrameworks/PerformanceTrace.framework/PerformanceTrace
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 3FBAEA6E-FCA6-3A76-B32D-F2EDF7924D5B
-  Functions: 31
-  Symbols:   77
-  CStrings:  80
+  UUID: B7D4030D-70CC-31ED-A655-0AD2EA4D7E6C
+  Functions: 59
+  Symbols:   115
+  CStrings:  220
 
Symbols:
+ _NSLocalizedDescriptionKey
+ _OBJC_CLASS_$_DMTraceSession
+ _OBJC_CLASS_$_NSDictionary
+ _OBJC_CLASS_$_NSError
+ _OBJC_CLASS_$_NSObject
+ _OBJC_CLASS_$_PTTraceConfig
+ _OBJC_CLASS_$_PTTraceSession
+ _OBJC_METACLASS_$_DMTraceSession
+ _OBJC_METACLASS_$_NSObject
+ __Unwind_Resume
+ ___error
+ ___objc_personality_v0
+ __objc_empty_cache
+ _dispatch_async
+ _dispatch_queue_attr_make_with_qos_class
+ _helperLog
+ _objc_autorelease
+ _objc_claimAutoreleasedReturnValue
+ _objc_getProperty
+ _objc_msgSendSuper2
+ _objc_release
+ _objc_release_x26
+ _objc_release_x9
+ _objc_retain
+ _objc_retainAutoreleaseReturnValue
+ _objc_retain_x1
+ _objc_retain_x2
+ _objc_retain_x23
+ _objc_retain_x8
+ _objc_setProperty_atomic
+ _objc_setProperty_atomic_copy
+ _objc_storeStrong
+ _objc_sync_enter
+ _objc_sync_exit
+ _os_transaction_create
+ _sandbox_extension_consume
+ _sandbox_extension_release
+ _xpc_dictionary_get_bool
+ _xpc_dictionary_get_double
- _objc_retainAutoreleasedReturnValue
CStrings:
+ "#16@0:8"
+ ".cxx_destruct"
+ "@\"NSError\""
+ "@\"NSObject<OS_os_transaction>\""
+ "@\"NSString\""
+ "@\"NSString\"16@0:8"
+ "@\"NSURL\""
+ "@\"PTTraceSession\""
+ "@16@0:8"
+ "@24@0:8:16"
+ "@24@0:8@16"
+ "@32@0:8:16@24"
+ "@36@0:8d16B24^@28"
+ "@40@0:8:16@24@32"
+ "@?"
+ "@?16@0:8"
+ "Already stopping"
+ "B"
+ "B16@0:8"
+ "B24@0:8#16"
+ "B24@0:8:16"
+ "B24@0:8@\"Protocol\"16"
+ "B24@0:8@16"
+ "Cannot stop trace: no active session"
+ "DMTraceSession"
+ "Failed to consume sandbox token: %d (%s)"
+ "Failed to move trace file from %@ to %@: %@"
+ "Failed to start trace: %@"
+ "Moved trace file to %@"
+ "NSObject"
+ "PTTraceSessionDelegate"
+ "Q16@0:8"
+ "Started trace with duration %f, full: %d"
+ "T#,R"
+ "T@\"NSError\",&,V_traceError"
+ "T@\"NSObject<OS_os_transaction>\",&,V_transaction"
+ "T@\"NSString\",&,V_sandboxToken"
+ "T@\"NSString\",?,R,C"
+ "T@\"NSString\",R,C"
+ "T@\"NSURL\",&,V_traceFileURL"
+ "T@\"PTTraceSession\",&,V_session"
+ "T@?,C,V_completion"
+ "TB,V_traceCompleted"
+ "TQ,R"
+ "Trace already completed"
+ "Trace stopped with url: %@, sandboxToken: %@, error: %@"
+ "TraceSessionManagerErrorDomain"
+ "Tracing ended before a stop call was issued."
+ "URLByAppendingPathComponent:"
+ "URLByAppendingPathExtension:"
+ "URLByDeletingLastPathComponent"
+ "Vv16@0:8"
+ "^{_NSZone=}16@0:8"
+ "_completion"
+ "_sandboxToken"
+ "_session"
+ "_traceCompleted"
+ "_traceError"
+ "_traceFileURL"
+ "_transaction"
+ "autorelease"
+ "class"
+ "com.apple.datamigratorhelper.tracing"
+ "completion"
+ "configWithTemplate:"
+ "conformsToProtocol:"
+ "debugDescription"
+ "description"
+ "dictionaryWithObjects:forKeys:count:"
+ "duration"
+ "errorWithDomain:code:userInfo:"
+ "filename"
+ "full"
+ "hash"
+ "init"
+ "initAndStartWithSession:"
+ "initWithConfig:"
+ "invalid config"
+ "invalid session"
+ "isEqual:"
+ "isEqualToString:"
+ "isKindOfClass:"
+ "isMemberOfClass:"
+ "isProxy"
+ "isValid"
+ "moveItemAtURL:toURL:error:"
+ "nil"
+ "pathExtension"
+ "performSelector:"
+ "performSelector:withObject:"
+ "performSelector:withObject:withObject:"
+ "performanceTraceDidComplete:withToken:withError:"
+ "performanceTraceDidStart:"
+ "performanceTraceDidStop:"
+ "present"
+ "release"
+ "respondsToSelector:"
+ "retain"
+ "retainCount"
+ "sandboxToken"
+ "self"
+ "session"
+ "setCompletion:"
+ "setDelegate:"
+ "setIncludeOSLogs:"
+ "setSandboxToken:"
+ "setSession:"
+ "setSymbolicate:"
+ "setTraceCompleted:"
+ "setTraceDurationSecs:"
+ "setTraceError:"
+ "setTraceFileURL:"
+ "setTraceType:"
+ "setTransaction:"
+ "startPerformanceTrace"
+ "startTraceWithDuration:fullTrace:error:"
+ "stopPerformanceTrace"
+ "stopTracingWithCompletion:"
+ "superclass"
+ "traceCompleted"
+ "traceError"
+ "traceFileURL"
+ "transaction"
+ "v16@0:8"
+ "v20@0:8B16"
+ "v24@0:8@\"NSError\"16"
+ "v24@0:8@16"
+ "v24@0:8@?16"
+ "v32@?0@\"NSURL\"8@\"NSString\"16@\"NSError\"24"
+ "v40@0:8@\"NSURL\"16@\"NSString\"24@\"NSError\"32"
+ "v40@0:8@16@24@32"
+ "validateConfig"
+ "zone"

```
