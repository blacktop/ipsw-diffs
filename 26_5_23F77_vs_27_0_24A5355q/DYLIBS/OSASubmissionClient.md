## OSASubmissionClient

> `/System/Library/PrivateFrameworks/OSASubmissionClient.framework/OSASubmissionClient`

```diff

-934.120.2.0.0
-  __TEXT.__text: 0x25fc
-  __TEXT.__auth_stubs: 0x3b0
+1049.0.0.502.1
+  __TEXT.__text: 0x240c
   __TEXT.__objc_methlist: 0x2b8
   __TEXT.__const: 0x90
-  __TEXT.__gcc_except_tab: 0xb4
-  __TEXT.__cstring: 0x2d5
+  __TEXT.__gcc_except_tab: 0xa0
+  __TEXT.__cstring: 0x2d8
   __TEXT.__oslogstring: 0x4a7
-  __TEXT.__unwind_info: 0x118
-  __TEXT.__objc_classname: 0x7f
-  __TEXT.__objc_methname: 0x7f0
-  __TEXT.__objc_methtype: 0x262
-  __TEXT.__objc_stubs: 0x760
-  __DATA_CONST.__got: 0x110
+  __TEXT.__unwind_info: 0x110
+  __TEXT.__objc_stubs: 0x0
+  __TEXT.__auth_stubs: 0x0
+  __TEXT.__objc_classname: 0x0
+  __TEXT.__objc_methname: 0x0
+  __TEXT.__objc_methtype: 0x0
   __DATA_CONST.__const: 0x170
   __DATA_CONST.__objc_classlist: 0x18
   __DATA_CONST.__objc_protolist: 0x10

   __DATA_CONST.__objc_protorefs: 0x8
   __DATA_CONST.__objc_superrefs: 0x8
   __DATA_CONST.__objc_arraydata: 0x60
-  __AUTH_CONST.__auth_got: 0x1e8
+  __DATA_CONST.__got: 0x110
   __AUTH_CONST.__const: 0x40
   __AUTH_CONST.__cfstring: 0x2a0
   __AUTH_CONST.__objc_const: 0x3d8
   __AUTH_CONST.__objc_dictobj: 0x78
+  __AUTH_CONST.__auth_got: 0x0
   __DATA.__objc_ivar: 0xc
   __DATA.__data: 0xc0
   __DATA_DIRTY.__objc_data: 0xf0

   - /System/Library/PrivateFrameworks/OSAnalyticsPrivate.framework/OSAnalyticsPrivate
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: FC660FA6-6D10-3DDB-BA44-A14786B6A613
-  Functions: 53
+  UUID: E5EE5B12-E86F-3D03-A68E-262086B4243D
+  Functions: 51
   Symbols:   321
-  CStrings:  225
+  CStrings:  84
 
Symbols:
+ _objc_claimAutoreleasedReturnValue
+ _objc_retain
+ _objc_retain_x1
+ _objc_retain_x2
+ _objc_retain_x3
+ _objc_retain_x8
- GCC_except_table29
- _OUTLINED_FUNCTION_3
- _OUTLINED_FUNCTION_4
- _objc_retainAutoreleasedReturnValue
CStrings:
- "#16@0:8"
- ".cxx_destruct"
- "@\"<OSASubmissionServices>\""
- "@\"NSString\"16@0:8"
- "@\"NSXPCConnection\""
- "@16@0:8"
- "@24@0:8:16"
- "@24@0:8@16"
- "@24@0:8@?16"
- "@24@0:8B16B20"
- "@32@0:8:16@24"
- "@40@0:8:16@24@32"
- "B"
- "B16@0:8"
- "B20@0:8B16"
- "B24@0:8#16"
- "B24@0:8:16"
- "B24@0:8@\"Protocol\"16"
- "B24@0:8@16"
- "NSObject"
- "OSADRESubmissionClient"
- "OSASubmissionClient"
- "OSASubmissionClientOptions"
- "OSASubmissionScheduler"
- "OSASubmissionServices"
- "Q16@0:8"
- "T#,R"
- "T@\"NSString\",?,R,C"
- "T@\"NSString\",R,C"
- "TB,V_urgentSubmission"
- "TQ,R"
- "Vv16@0:8"
- "^{_NSZone=}16@0:8"
- "_calculateNewCadenceParametersWithPermissive:fastLane:"
- "_connection"
- "_getCurrentCadenceParametersFromActivity:"
- "_incrementRetryCount"
- "_lastSuccessTime"
- "_resetRetryCount"
- "_retryCount"
- "_saveLastSuccessTime"
- "_scheduleSubmissionWithPermissive:"
- "_synchRemoteObjectProxy"
- "_updateCadenceForActivity:newCadenceParameters:"
- "_urgentSubmission"
- "addEntriesFromDictionary:"
- "addObject:"
- "arrayWithObjects:count:"
- "autorelease"
- "beginEncoding"
- "boolValue"
- "canSubmitLogOfType:withReply:"
- "class"
- "cleanupForUser:"
- "cleanupWithHomeDirectoryLocation:"
- "cleanupWithHomeDirectoryLocation:options:"
- "conformsToProtocol:"
- "count"
- "countByEnumeratingWithState:objects:count:"
- "crashReporterKey"
- "d16@0:8"
- "dateWithTimeIntervalSinceReferenceDate:"
- "dealloc"
- "debugDescription"
- "description"
- "dictionaryWithObjects:forKeys:count:"
- "doubleForKey:"
- "encodeObject:forKey:"
- "fastLane"
- "fetchMainConfigFileWithOverrrides:withReply:"
- "fetchTypeBlackListWithReply:"
- "finishEncoding"
- "hash"
- "init"
- "initWithErrorHandler:"
- "initWithMachServiceName:options:"
- "initWithSandboxExtensions:"
- "integerForKey:"
- "interfaceWithProtocol:"
- "invalidate"
- "isEqual:"
- "isEqualToDictionary:"
- "isKindOfClass:"
- "isMemberOfClass:"
- "isProxy"
- "localizedDescription"
- "longLongValue"
- "mutableCopy"
- "numberWithBool:"
- "numberWithLongLong:"
- "objectForKeyedSubscript:"
- "overrideMountPath"
- "overrideSubmissionServiceMountPath:withReply:"
- "pathContainerRoot"
- "pathRoot"
- "performSelector:"
- "performSelector:withObject:"
- "performSelector:withObject:withObject:"
- "q16@0:8"
- "recordEvent:"
- "release"
- "respondsToSelector:"
- "resume"
- "retain"
- "retainCount"
- "scheduleCleanupForUser:"
- "scheduleSubmission"
- "self"
- "setDouble:forKey:"
- "setInteger:forKey:"
- "setObject:forKeyedSubscript:"
- "setRemoteObjectInterface:"
- "setUrgentSubmission:"
- "sharedInstance"
- "standardUserDefaults"
- "stringByAppendingPathComponent:"
- "stringWithUTF8String:"
- "submissionOptionsFromClientOptions:"
- "submitDRETelemetryAndDiagnostics:"
- "submitWithOptions:"
- "submitWithOptions:resultsCallback:"
- "superclass"
- "synchronousRemoteObjectProxyWithErrorHandler:"
- "timeIntervalSinceReferenceDate"
- "updateConfigFile"
- "urgentSubmission"
- "v16@0:8"
- "v20@0:8B16"
- "v24@0:8@\"NSString\"16"
- "v24@0:8@16"
- "v24@0:8@?16"
- "v24@0:8@?<v@?@\"NSSet\">16"
- "v32@0:8@\"NSDictionary\"16@?<v@?@\"NSData\">24"
- "v32@0:8@\"NSDictionary\"16@?<v@?@\"NSDictionary\">24"
- "v32@0:8@\"NSString\"16@\"NSDictionary\"24"
- "v32@0:8@\"NSString\"16@?<v@?B>24"
- "v32@0:8@\"OverrideMountPathRequest\"16@?<v@?B>24"
- "v32@0:8@16@24"
- "v32@0:8@16@?24"
- "zone"

```
