## MediaSafetyNet

> `/System/Library/PrivateFrameworks/MediaSafetyNet.framework/MediaSafetyNet`

```diff

 74.0.0.0.0
-  __TEXT.__text: 0xadf4
-  __TEXT.__auth_stubs: 0x730
+  __TEXT.__text: 0xa2ac
   __TEXT.__objc_methlist: 0x504
   __TEXT.__const: 0xc0
   __TEXT.__oslogstring: 0xdc1
-  __TEXT.__cstring: 0xc52
-  __TEXT.__gcc_except_tab: 0x194
+  __TEXT.__cstring: 0xc60
+  __TEXT.__gcc_except_tab: 0x188
   __TEXT.__dlopen_cstrs: 0x115
   __TEXT.__ustring: 0x60
-  __TEXT.__unwind_info: 0x290
-  __TEXT.__objc_classname: 0x105
-  __TEXT.__objc_methname: 0xdf7
-  __TEXT.__objc_methtype: 0x2f3
-  __TEXT.__objc_stubs: 0xe60
-  __DATA_CONST.__got: 0x130
+  __TEXT.__unwind_info: 0x288
+  __TEXT.__objc_stubs: 0x0
+  __TEXT.__auth_stubs: 0x0
+  __TEXT.__objc_classname: 0x0
+  __TEXT.__objc_methname: 0x0
+  __TEXT.__objc_methtype: 0x0
   __DATA_CONST.__const: 0x3a8
   __DATA_CONST.__objc_classlist: 0x38
   __DATA_CONST.__objc_protolist: 0x28

   __DATA_CONST.__objc_protorefs: 0x18
   __DATA_CONST.__objc_superrefs: 0x30
   __DATA_CONST.__objc_arraydata: 0x80
-  __AUTH_CONST.__auth_got: 0x3a8
+  __DATA_CONST.__got: 0x0
   __AUTH_CONST.__const: 0x220
   __AUTH_CONST.__cfstring: 0x660
   __AUTH_CONST.__objc_const: 0xdd8
   __AUTH_CONST.__objc_intobj: 0x30
   __AUTH_CONST.__objc_arrayobj: 0x138
+  __AUTH_CONST.__auth_got: 0x0
   __DATA.__objc_ivar: 0x60
   __DATA.__data: 0x1e8
   __DATA.__crash_info: 0x148
-  __DATA.__bss: 0x78
+  __DATA.__bss: 0x48
   __DATA_DIRTY.__objc_data: 0x230
   __DATA_DIRTY.__common: 0x44
-  __DATA_DIRTY.__bss: 0xc8
+  __DATA_DIRTY.__bss: 0xf8
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/CoreMedia.framework/CoreMedia
   - /System/Library/Frameworks/Foundation.framework/Foundation

   - /usr/lib/libMobileGestalt.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 63025276-585C-3864-918D-920BFFB25C6C
-  Functions: 239
-  Symbols:   1088
-  CStrings:  525
+  UUID: 0AA5E78D-AD34-333A-96A0-4B0D13A65D34
+  Functions: 233
+  Symbols:   1066
+  CStrings:  284
 
Symbols:
+ ___53+[MSNScopedExceptionsServer proxyForMachServiceName:]_block_invoke.84
+ ___62-[MSNPillDataSourceServer listener:shouldAcceptNewConnection:]_block_invoke.38
+ ___64-[MSNScopedExceptionsServer listener:shouldAcceptNewConnection:]_block_invoke.79
+ ___74-[MSNPillDataSourceServer fetchPillRegistrationForProcess:withCompletion:]_block_invoke.26
+ _objc_claimAutoreleasedReturnValue
+ _objc_retainAutorelease
+ _objc_retainAutoreleaseReturnValue
+ _objc_retain_x1
+ _objc_retain_x24
+ _objc_retain_x3
+ _objc_retain_x8
- _OUTLINED_FUNCTION_23
- _OUTLINED_FUNCTION_24
- _OUTLINED_FUNCTION_25
- _OUTLINED_FUNCTION_26
- ___53+[MSNScopedExceptionsServer proxyForMachServiceName:]_block_invoke.85
- ___62-[MSNPillDataSourceServer listener:shouldAcceptNewConnection:]_block_invoke.39
- ___64-[MSNScopedExceptionsServer listener:shouldAcceptNewConnection:]_block_invoke.80
- ___74-[MSNPillDataSourceServer fetchPillRegistrationForProcess:withCompletion:]_block_invoke.27
- _objc_autorelease
- _objc_retainAutoreleasedReturnValue
- _objc_retain_x22
CStrings:
- "#16@0:8"
- ".cxx_destruct"
- "@\"<MSNPillDataSourceProtocol>\""
- "@\"MXSystemController\""
- "@\"NSMutableArray\""
- "@\"NSObject<OS_dispatch_queue>\""
- "@\"NSSet\""
- "@\"NSString\""
- "@\"NSString\"16@0:8"
- "@\"NSURL\""
- "@\"NSXPCConnection\""
- "@\"NSXPCListener\""
- "@\"STCallingStatusDomain\""
- "@\"STCallingStatusDomainData\""
- "@\"STDynamicActivityAttributionMonitor\""
- "@16@0:8"
- "@24@0:8:16"
- "@24@0:8@16"
- "@32@0:8:16@24"
- "@32@0:8@16@24"
- "@40@0:8:16@24@32"
- "B"
- "B16@0:8"
- "B24@0:8#16"
- "B24@0:8:16"
- "B24@0:8@\"Protocol\"16"
- "B24@0:8@16"
- "B32@0:8@\"NSXPCListener\"16@\"NSXPCConnection\"24"
- "B32@0:8@16@24"
- "MSNCarPlay"
- "MSNPillDataSource"
- "MSNPillDataSourceController"
- "MSNPillDataSourceProtocol"
- "MSNPillDataSourceServer"
- "MSNPillRegistrationProtocol"
- "MSNScopedException"
- "MSNScopedExceptionsProtocol"
- "MSNScopedExceptionsServer"
- "MSNTTR"
- "NSObject"
- "NSXPCListenerDelegate"
- "Q16@0:8"
- "T#,R"
- "T@\"<MSNPillDataSourceProtocol>\",W,N,V_dataSource"
- "T@\"NSMutableArray\",R,N,V_activeDataSources"
- "T@\"NSObject<OS_dispatch_queue>\",R,N,V_queue"
- "T@\"NSSet\",C,N,V_identifiers"
- "T@\"NSString\",?,R,C"
- "T@\"NSString\",C,V_exception"
- "T@\"NSString\",R,C"
- "T@\"NSURL\",&,V_url"
- "T@\"NSXPCConnection\",&,N,V_xpcConnection"
- "T@\"NSXPCConnection\",&,V_connection"
- "T@\"NSXPCConnection\",W,N,V_connection"
- "T@\"NSXPCListener\",R,N,V_listener"
- "T@\"STCallingStatusDomain\",&,N,V_callingDomain"
- "T@\"STCallingStatusDomainData\",&,N,V_callingData"
- "T@\"STDynamicActivityAttributionMonitor\",R,N,V_systemStatusDynamicAttributionMonitor"
- "TB,R"
- "TB,R,N"
- "TB,V_pendedTTR"
- "TQ,R"
- "TTRInProgress"
- "Ti,R,N,V_token"
- "URLQueryAllowedCharacterSet"
- "URLWithString:"
- "Vv16@0:8"
- "^{_NSZone=}16@0:8"
- "^{__CFRunLoopSource=}"
- "^{__CFUserNotification=}"
- "_activeDataSources"
- "_activeExceptions"
- "_callingData"
- "_callingDataUpdatedWithData:"
- "_callingDomain"
- "_carplayConnected"
- "_connection"
- "_dataSource"
- "_exception"
- "_identifiers"
- "_listener"
- "_pendedTTR"
- "_queue"
- "_runLoopSource"
- "_setQueue:"
- "_systemController"
- "_systemStatusDynamicAttributionMonitor"
- "_token"
- "_url"
- "_userNotification"
- "_xpcConnection"
- "activate"
- "activeDataSources"
- "addObject:"
- "array"
- "arrayWithObjects:count:"
- "autorelease"
- "beginException:"
- "beginTTRWithTitle:"
- "beginTTRWithTitle:date:"
- "boolValue"
- "bundleIdentifier"
- "callDescriptors"
- "callingData"
- "callingDomain"
- "carplayConnected"
- "class"
- "clientExecutablePath"
- "completeTTR:"
- "componentsSeparatedByString:"
- "configurationForDefaultMainDisplayMonitor"
- "conformsToProtocol:"
- "connection"
- "containsObject:"
- "continueTTR"
- "copy"
- "copyAttributeForKey:withValueOut:"
- "count"
- "countByEnumeratingWithState:objects:count:"
- "currentAttributions"
- "currentConnection"
- "currentStatusDescriptorForIdentifier:reply:"
- "data"
- "dataSource"
- "date"
- "dateWithTimeIntervalSinceNow:"
- "dealloc"
- "debugDescription"
- "defaultWorkspace"
- "description"
- "dictionaryWithObjects:forKeys:count:"
- "elements"
- "endException:"
- "exception"
- "fetchPillRegistrationForProcess:withCompletion:"
- "formUnionWithCharacterSet:"
- "handleCallback:"
- "hash"
- "i16@0:8"
- "identifier"
- "identifiers"
- "init"
- "initWithConnection:exception:"
- "initWithConnection:identifiers:"
- "initWithMachServiceName:"
- "initWithMachServiceName:options:"
- "initWithPID:"
- "initWithQueue:"
- "intValue"
- "integerValue"
- "interfaceWithProtocol:"
- "invalidate"
- "isConnectionAllowedToAssertException:"
- "isEqual:"
- "isEqualToString:"
- "isExceptionInEffect:"
- "isKindOfClass:"
- "isMemberOfClass:"
- "isProxy"
- "lastPathComponent"
- "level"
- "listener"
- "listener:shouldAcceptNewConnection:"
- "monitorWithConfiguration:"
- "now"
- "objectAtIndexedSubscript:"
- "objectForKeyedSubscript:"
- "observeDataWithBlock:"
- "openURL:configuration:completionHandler:"
- "pendedTTR"
- "performSelector:"
- "performSelector:withObject:"
- "performSelector:withObject:withObject:"
- "processIdentifier"
- "proxiesForException:"
- "proxyForMachServiceName:"
- "queue"
- "registerPillDataSource:forIdentifiers:"
- "registerPillDataSourceForIdentifiers:"
- "release"
- "remoteObjectProxy"
- "removeCharactersInString:"
- "removeObjectAtIndex:"
- "removeObjectsInArray:"
- "respondsToSelector:"
- "resume"
- "retain"
- "retainCount"
- "self"
- "setAttributeForKey:andValue:"
- "setCallingData:"
- "setCallingDomain:"
- "setConnection:"
- "setDataSource:"
- "setDateFormat:"
- "setDelegate:"
- "setException:"
- "setExportedInterface:"
- "setExportedObject:"
- "setIdentifiers:"
- "setInterruptionHandler:"
- "setInvalidationHandler:"
- "setNeedsUserInteractivePriority:"
- "setPendedTTR:"
- "setRemoteObjectInterface:"
- "setTimeZone:"
- "setTransitionHandler:"
- "setUrl:"
- "setWithArray:"
- "setXpcConnection:"
- "sharedCamProxy"
- "sharedInstance"
- "sharedMicProxy"
- "sharedProxy"
- "shouldQueryPillDataSource"
- "stringByAddingPercentEncodingWithAllowedCharacters:"
- "stringByAppendingString:"
- "stringFromDate:"
- "stringWithFormat:"
- "stringWithUTF8String:"
- "superclass"
- "systemStatusDynamicAttributionMonitor"
- "systemTimeZone"
- "timeIntervalSinceDate:"
- "token"
- "url"
- "v16@0:8"
- "v20@0:8B16"
- "v24@0:8@\"NSSet\"16"
- "v24@0:8@\"NSString\"16"
- "v24@0:8@16"
- "v24@0:8Q16"
- "v32@0:8@\"NSString\"16@?<v@?@\"STCallingStatusDomainCallDescriptor\">24"
- "v32@0:8@16@24"
- "v32@0:8@16@?24"
- "validEntitlements"
- "validExceptions"
- "valueForEntitlement:"
- "xpcConnection"
- "zone"

```
