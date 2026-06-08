## DACoreDAVGlue

> `/System/Library/PrivateFrameworks/DataAccess.framework/Frameworks/DACoreDAVGlue.framework/DACoreDAVGlue`

```diff

-2691.4.6.0.0
-  __TEXT.__text: 0xc6c
-  __TEXT.__auth_stubs: 0x1f0
+2703.0.0.0.0
+  __TEXT.__text: 0xc34
   __TEXT.__objc_methlist: 0x38c
   __TEXT.__const: 0x20
   __TEXT.__oslogstring: 0x17b
   __TEXT.__gcc_except_tab: 0x20
-  __TEXT.__cstring: 0xd
-  __TEXT.__unwind_info: 0xa0
-  __TEXT.__objc_classname: 0x75
-  __TEXT.__objc_methname: 0x5de
-  __TEXT.__objc_methtype: 0x1e3
-  __TEXT.__objc_stubs: 0x300
-  __DATA_CONST.__got: 0x78
+  __TEXT.__cstring: 0xf
+  __TEXT.__unwind_info: 0xa8
+  __TEXT.__objc_stubs: 0x0
+  __TEXT.__auth_stubs: 0x0
+  __TEXT.__objc_classname: 0x0
+  __TEXT.__objc_methname: 0x0
+  __TEXT.__objc_methtype: 0x0
   __DATA_CONST.__const: 0x20
   __DATA_CONST.__objc_classlist: 0x10
   __DATA_CONST.__objc_catlist: 0x8

   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_selrefs: 0x258
   __DATA_CONST.__objc_superrefs: 0x8
-  __AUTH_CONST.__auth_got: 0x108
+  __DATA_CONST.__got: 0x78
   __AUTH_CONST.__const: 0x20
   __AUTH_CONST.__cfstring: 0x40
   __AUTH_CONST.__objc_const: 0xa78
+  __AUTH_CONST.__auth_got: 0x0
   __DATA.__objc_ivar: 0x4
   __DATA.__data: 0x180
   __DATA_DIRTY.__objc_data: 0xa0

   - /System/Library/PrivateFrameworks/SpringBoardServices.framework/SpringBoardServices
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 06C4BEA3-02D5-38DB-9152-0CCB6456A805
+  UUID: FDEE1BC3-E2D0-3A09-A21A-AB1C936CF526
   Functions: 24
-  Symbols:   186
-  CStrings:  132
+  Symbols:   189
+  CStrings:  12
 
Symbols:
+ _objc_claimAutoreleasedReturnValue
+ _objc_retain
+ _objc_retainAutoreleaseReturnValue
+ _objc_retain_x2
+ _objc_retain_x28
+ _objc_retain_x3
+ _objc_retain_x8
- _objc_release_x26
- _objc_retainAutoreleasedReturnValue
- _objc_retain_x19
- _objc_retain_x26
Functions:
~ _coreDAVValidationErrorFromRawError : 628 -> 604
~ -[CoreDAVTask(DACoreDAVGlueExtensions) cancelTaskWithReason:underlyingError:] : 356 -> 344
~ -[DACoreDAVTaskManager initWithAccount:] : 108 -> 112
~ -[DACoreDAVTaskManager _updateSpinner:] : 980 -> 976
~ +[DACoreDAVLogger registerDefaultLoggerWithCoreDAV] : 84 -> 68
~ ___51+[DACoreDAVLogger registerDefaultLoggerWithCoreDAV]_block_invoke : 128 -> 124
CStrings:
- "#16@0:8"
- ".cxx_destruct"
- "@\"NSMutableSet\""
- "@\"NSObject<OS_os_log>\"16@0:8"
- "@\"NSRunLoop\"16@0:8"
- "@\"NSString\"16@0:8"
- "@16@0:8"
- "@24@0:8:16"
- "@24@0:8@16"
- "@32@0:8:16@24"
- "@40@0:8:16@24@32"
- "B16@0:8"
- "B24@0:8#16"
- "B24@0:8:16"
- "B24@0:8@\"Protocol\"16"
- "B24@0:8@16"
- "CoreDAVLogDelegate"
- "CoreDAVTaskManager"
- "DACoreDAVGlueExtensions"
- "DACoreDAVLogger"
- "DACoreDAVTaskManager"
- "DATask"
- "NSObject"
- "Q16@0:8"
- "T#,R"
- "T@\"NSRunLoop\",&,N"
- "T@\"NSString\",?,R,C"
- "T@\"NSString\",R,C"
- "TQ,R"
- "Vv16@0:8"
- "^{_NSZone=}16@0:8"
- "_applicationsShowingActivity"
- "_updateSpinner:"
- "addLogDelegate:forAccountInfoProvider:"
- "addObject:"
- "autorelease"
- "cal_isCertificateError"
- "cancelTaskWithReason:underlyingError:"
- "class"
- "code"
- "conformsToProtocol:"
- "containsObject:"
- "coreDAVLogDiagnosticMessage:atLevel:"
- "coreDAVLogLevel"
- "coreDAVLogRequestBody:"
- "coreDAVLogResponseBody:"
- "coreDAVLogTransmittedDataPartial:"
- "coreDAVOutputLevel"
- "coreDAVTaskDidFinish:"
- "coreDAVTaskEndModal:"
- "coreDAVTaskRequestModal:"
- "coreDAVTransmittedDataFinished"
- "count"
- "countByEnumeratingWithState:objects:count:"
- "dealloc"
- "debugDescription"
- "description"
- "dictionaryWithObjects:forKeys:count:"
- "domain"
- "errorWithDomain:code:userInfo:"
- "finishCoreDAVTaskWithError:"
- "finishWithError:"
- "hash"
- "initWithAccount:"
- "initWithFilename:"
- "isEqual:"
- "isEqualToString:"
- "isKindOfClass:"
- "isMemberOfClass:"
- "isProxy"
- "logHandle"
- "performCoreDAVTask"
- "performSelector:"
- "performSelector:withObject:"
- "performSelector:withObject:withObject:"
- "performTask"
- "q16@0:8"
- "registerDefaultLoggerWithCoreDAV"
- "release"
- "removeObject:"
- "requestCancelTaskWithReason:"
- "respondsToSelector:"
- "retain"
- "retainCount"
- "self"
- "setTaskManager:"
- "setWorkRunLoop:"
- "sharedLogging"
- "sharedRunLoop"
- "shouldForceNetworking"
- "shouldHoldPowerAssertion"
- "shouldLogTransmittedData"
- "shutdown"
- "spinnerIdentifiers"
- "startModal"
- "submitIndependentCoreDAVTask:"
- "submitIndependentTask:"
- "submitQueuedCoreDAVTask:"
- "submitQueuedTask:"
- "superclass"
- "taskDidFinish:"
- "taskEndModal:"
- "taskManagerDidAddTask:"
- "taskManagerWillRemoveTask:"
- "taskRequestModal:"
- "v16@0:8"
- "v20@0:8B16"
- "v20@0:8i16"
- "v24@0:8@\"CoreDAVTask\"16"
- "v24@0:8@\"DATaskManager\"16"
- "v24@0:8@\"NSData\"16"
- "v24@0:8@\"NSError\"16"
- "v24@0:8@\"NSRunLoop\"16"
- "v24@0:8@16"
- "v28@0:8i16@\"NSError\"20"
- "v28@0:8i16@20"
- "v32@0:8@\"NSString\"16q24"
- "v32@0:8@16q24"
- "workRunLoop"
- "zone"

```
