## BlockMonitoring

> `/System/Library/PrivateFrameworks/BlockMonitoring.framework/BlockMonitoring`

```diff

-427.0.0.0.0
-  __TEXT.__text: 0x4a54
-  __TEXT.__auth_stubs: 0x840
+434.0.0.0.0
+  __TEXT.__text: 0x4814
   __TEXT.__objc_methlist: 0x1e8
   __TEXT.__const: 0xc8
-  __TEXT.__gcc_except_tab: 0x198
-  __TEXT.__cstring: 0x566
+  __TEXT.__gcc_except_tab: 0x180
+  __TEXT.__cstring: 0x56d
   __TEXT.__oslogstring: 0xf37
   __TEXT.__dlopen_cstrs: 0x5a
   __TEXT.__unwind_info: 0x158
-  __TEXT.__objc_classname: 0x22
-  __TEXT.__objc_methname: 0x87f
-  __TEXT.__objc_methtype: 0x158
-  __TEXT.__objc_stubs: 0x5a0
-  __DATA_CONST.__got: 0xb0
+  __TEXT.__objc_stubs: 0x0
+  __TEXT.__auth_stubs: 0x0
+  __TEXT.__objc_classname: 0x0
+  __TEXT.__objc_methname: 0x0
+  __TEXT.__objc_methtype: 0x0
   __DATA_CONST.__const: 0x190
   __DATA_CONST.__objc_classlist: 0x8
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_selrefs: 0x258
   __DATA_CONST.__objc_superrefs: 0x8
-  __AUTH_CONST.__auth_got: 0x430
+  __DATA_CONST.__got: 0xb0
   __AUTH_CONST.__const: 0x40
   __AUTH_CONST.__cfstring: 0x380
   __AUTH_CONST.__objc_const: 0x438
+  __AUTH_CONST.__auth_got: 0x0
   __DATA.__objc_ivar: 0x74
   __DATA.__bss: 0x10
   __DATA_DIRTY.__objc_data: 0x50

   - /usr/lib/libMobileGestalt.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 7D30355D-1B2F-3AEE-B95E-3FA4A2430B34
-  Functions: 117
-  Symbols:   507
-  CStrings:  286
+  UUID: B4497A63-57AD-3D89-A5C4-A1E5BBEC8C1D
+  Functions: 114
+  Symbols:   502
+  CStrings:  150
 
Symbols:
+ ___block_literal_global.167
+ _objc_claimAutoreleasedReturnValue
+ _objc_retainAutoreleaseReturnValue
+ _objc_retain_x1
+ _objc_retain_x3
+ _objc_retain_x4
+ _objc_retain_x5
- _OUTLINED_FUNCTION_27
- _OUTLINED_FUNCTION_28
- _OUTLINED_FUNCTION_29
- ___block_literal_global.168
- _objc_retainAutoreleasedReturnValue
- _objc_retain_x23
- _objc_retain_x24
- _objc_retain_x26
- _objc_retain_x28
CStrings:
- ".cxx_destruct"
- "@\"NSDictionary\""
- "@\"NSObject<OS_dispatch_queue>\""
- "@\"NSObject<OS_os_log>\""
- "@\"NSString\""
- "@16@0:8"
- "@24@0:8@16"
- "@32@0:8@16q24"
- "@32@0:8^q16^@24"
- "@?"
- "AB"
- "AI"
- "B"
- "B16@0:8"
- "C"
- "C16@0:8"
- "I"
- "Q"
- "Testing"
- "URLWithString:"
- "UTF8String"
- "_alreadyFaulted"
- "_bootArgsBMFlags"
- "_bootArgsDebugFlags"
- "_coreDumpsDisabled"
- "_deviceState"
- "_enabled"
- "_entitledToFlushOSLogs"
- "_executionDuration"
- "_logger"
- "_osVersion"
- "_panicPacing"
- "_panicWithData"
- "_persistencePath"
- "_presentAlert"
- "_queue"
- "_sandboxHandle"
- "_test_actionDoneCallback"
- "_test_alertShown"
- "_test_allowPanic"
- "_test_allowPanic:"
- "_test_bootArgs"
- "_test_debuggerState"
- "_test_getAlertPath"
- "_test_getAlertShown"
- "_test_getAlreadyFaulted"
- "_test_getCoreDumpsDisabled"
- "_test_getDebuggerState"
- "_test_getEnabled"
- "_test_getOSVersion"
- "_test_getPanicDeny"
- "_test_getPanicReason"
- "_test_getPanicWithData"
- "_test_getPresentAlert"
- "_test_getResultType"
- "_test_getSignaturePath"
- "_test_getWasFirstFault"
- "_test_logFlushSleep"
- "_test_panicDeny"
- "_test_panicReason"
- "_test_panicSleep"
- "_test_postPersistenceSleep"
- "_test_resetVariables"
- "_test_resultType"
- "_test_setActionDoneCallback:"
- "_test_setDebuggerState:"
- "_test_setEnabled:"
- "_test_setExecutionDuration:"
- "_test_setLogFlushSleep:"
- "_test_setOSVersion:"
- "_test_setPanicPacing:"
- "_test_setPanicSleep:"
- "_test_setPostPersistenceSleep:"
- "_test_setPresentAlert:"
- "_test_wasFirstFault"
- "_testing"
- "addCharactersInString:"
- "alertFileName"
- "alphanumericCharacterSet"
- "arrayByAddingObject:"
- "arrayWithObjects:count:"
- "bundleIdentifier"
- "bytes"
- "componentsJoinedByString:"
- "componentsSeparatedByCharactersInSet:"
- "computePersistencePath:error:"
- "containsObject:"
- "copy"
- "dataWithPropertyList:format:options:error:"
- "dealloc"
- "defaultWorkspace"
- "dictionaryWithObjects:forKeys:count:"
- "executeBlockWithSignature:block:"
- "executeBlockWithSignature:timeout:options:block:"
- "executeBlockWithSignature:timeout:options:diagnosticCollectionBlock:block:"
- "fileSystemRepresentation"
- "init"
- "initWithBytes:length:"
- "initWithCString:encoding:"
- "initWithUTF8String:"
- "invertedSet"
- "isEqualToString:"
- "isProcessBeingDebugged"
- "length"
- "longLongValue"
- "mainBundle"
- "monitorForTestingWithBootArgs:"
- "now"
- "objectForKey:"
- "objectForKeyedSubscript:"
- "openURL:withOptions:"
- "propertyListWithData:options:format:error:"
- "q"
- "readEntitlement:withBlock:"
- "sanitizedSignature:maxLength:"
- "sharedManager"
- "signatureFileName"
- "stringByAppendingPathComponent:"
- "stringByReplacingOccurrencesOfString:withString:"
- "stringWithCString:encoding:"
- "stringWithFormat:"
- "substringToIndex:"
- "timeIntervalSinceNow"
- "v16@0:8"
- "v20@0:8B16"
- "v20@0:8C16"
- "v20@0:8I16"
- "v24@0:8@16"
- "v24@0:8@?16"
- "v24@0:8Q16"
- "v24@0:8q16"
- "v32@0:8^{__CFString=}16@?24"
- "v32@0:8r*16@?24"
- "v44@0:8r*16Q24i32@?36"
- "v52@0:8r*16Q24i32@?36@?44"

```
