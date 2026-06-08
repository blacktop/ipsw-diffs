## OSAServicesClient

> `/System/Library/PrivateFrameworks/OSAServicesClient.framework/OSAServicesClient`

```diff

-934.120.2.0.0
-  __TEXT.__text: 0x4278
-  __TEXT.__auth_stubs: 0x380
+1049.0.0.502.1
+  __TEXT.__text: 0x3f80
   __TEXT.__objc_methlist: 0x680
   __TEXT.__const: 0x78
   __TEXT.__gcc_except_tab: 0x54
-  __TEXT.__cstring: 0x457
+  __TEXT.__cstring: 0x461
   __TEXT.__oslogstring: 0x495
-  __TEXT.__unwind_info: 0x210
-  __TEXT.__objc_classname: 0x150
-  __TEXT.__objc_methname: 0xc9e
-  __TEXT.__objc_methtype: 0x47c
-  __TEXT.__objc_stubs: 0xa40
-  __DATA_CONST.__got: 0xb0
+  __TEXT.__unwind_info: 0x208
+  __TEXT.__objc_stubs: 0x0
+  __TEXT.__auth_stubs: 0x0
+  __TEXT.__objc_classname: 0x0
+  __TEXT.__objc_methname: 0x0
+  __TEXT.__objc_methtype: 0x0
   __DATA_CONST.__const: 0x1f8
   __DATA_CONST.__objc_classlist: 0x48
   __DATA_CONST.__objc_protolist: 0x40

   __DATA_CONST.__objc_selrefs: 0x3b0
   __DATA_CONST.__objc_protorefs: 0x18
   __DATA_CONST.__objc_superrefs: 0x48
-  __AUTH_CONST.__auth_got: 0x1d0
+  __DATA_CONST.__got: 0xb0
   __AUTH_CONST.__const: 0x160
   __AUTH_CONST.__cfstring: 0x320
   __AUTH_CONST.__objc_const: 0x1208
+  __AUTH_CONST.__auth_got: 0x208
   __DATA.__objc_ivar: 0x5c
   __DATA.__data: 0x300
   __DATA.__bss: 0x20

   - /System/Library/PrivateFrameworks/DeviceRecovery.framework/DeviceRecovery
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 04A5A5D8-633B-3B7C-B0CF-3D5A1F01D5CB
-  Functions: 139
-  Symbols:   633
-  CStrings:  309
+  UUID: EC11BAE7-DF0E-3C45-9970-63BD534A6E54
+  Functions: 137
+  Symbols:   636
+  CStrings:  83
 
Symbols:
+ ___block_literal_global.43
+ ___block_literal_global.45
+ _objc_claimAutoreleasedReturnValue
+ _objc_retainAutoreleaseReturnValue
+ _objc_retain_x1
+ _objc_retain_x2
+ _objc_retain_x3
+ _objc_retain_x4
+ _objc_retain_x8
- _OUTLINED_FUNCTION_4
- _OUTLINED_FUNCTION_5
- ___block_literal_global.44
- ___block_literal_global.46
CStrings:
- "#16@0:8"
- ".cxx_destruct"
- "@\"<OSADiagnosticEventObserver>\""
- "@\"<OSADiagnosticObserver>\""
- "@\"<OSADiagnosticWriteObserver>\""
- "@\"<OTAAgentServices>\""
- "@\"NSDictionary\""
- "@\"NSError\""
- "@\"NSMutableArray\""
- "@\"NSMutableSet\""
- "@\"NSObject<OS_dispatch_queue>\""
- "@\"NSSet\""
- "@\"NSString\""
- "@\"NSString\"16@0:8"
- "@\"NSXPCConnection\""
- "@\"OSALogIdentity\""
- "@16@0:8"
- "@24@0:8:16"
- "@24@0:8@\"NSCoder\"16"
- "@24@0:8@16"
- "@24@0:8^{__CFString=}16"
- "@32@0:8:16@24"
- "@32@0:8@16@24"
- "@32@0:8@16B24B28"
- "@40@0:8:16@24@32"
- "B16@0:8"
- "B24@0:8#16"
- "B24@0:8:16"
- "B24@0:8@\"Protocol\"16"
- "B24@0:8@16"
- "B40@0:8@16@24@32"
- "B48@0:8@16@24@32^v40"
- "EventObserver"
- "I24@0:8@16"
- "NSCoding"
- "NSObject"
- "NSSecureCoding"
- "OSADiagnosticEventObserver"
- "OSADiagnosticMonitor"
- "OSADiagnosticMonitorClient"
- "OSADiagnosticMonitorClientProtocol"
- "OSADiagnosticMonitorServerProtocol"
- "OSADiagnosticWriteObserver"
- "OSALogEvent"
- "OSALogIdentity"
- "OSALogWriteResult"
- "OSAServicesClient"
- "OTAAgentServices"
- "ObserverShim"
- "Q16@0:8"
- "T#,R"
- "T@\"<OSADiagnosticEventObserver>\",R,W,N,V_observer"
- "T@\"<OSADiagnosticObserver>\",R,W,N,V_observer"
- "T@\"<OSADiagnosticWriteObserver>\",R,W,N,V_observer"
- "T@\"NSDictionary\",R,N,V_details"
- "T@\"NSError\",R,N,V_error"
- "T@\"NSSet\",R,N,V_bugTypes"
- "T@\"NSString\",?,R,C"
- "T@\"NSString\",R,C"
- "T@\"NSString\",R,N,V_bugType"
- "T@\"NSString\",R,N,V_filePath"
- "T@\"NSString\",R,N,V_incidentID"
- "T@\"OSADiagnosticMonitor\",R,N"
- "T@\"OSADiagnosticMonitorClient\",R,N"
- "T@\"OSALogIdentity\",R,N,V_identity"
- "TB,R"
- "TQ,R"
- "UTF8String"
- "Vv16@0:8"
- "WriteObserver"
- "^{_NSZone=}16@0:8"
- "_bugType"
- "_bugTypes"
- "_calloutQueue"
- "_connection"
- "_details"
- "_error"
- "_eventObservers"
- "_filePath"
- "_identity"
- "_incidentID"
- "_observedEventTypes"
- "_observedWriteTypes"
- "_observer"
- "_observers"
- "_queue"
- "_serverConnection"
- "_setQueue:"
- "_synchRemoteObjectProxy"
- "_writeObservers"
- "addEventObserver:forTypes:"
- "addObject:"
- "addObserver:forTypes:"
- "addWriteObserver:forTypes:"
- "array"
- "autorelease"
- "awdKey"
- "awdKeyWithReply:"
- "bugTypes"
- "class"
- "conformsToProtocol:"
- "containsObject:"
- "count"
- "countByEnumeratingWithState:objects:count:"
- "crashreporterKey"
- "crashreporterKeyWithReply:"
- "dataWithPropertyList:format:options:error:"
- "dealloc"
- "debugDescription"
- "decodeObjectOfClass:forKey:"
- "deletePreference:forUser:inDomain:"
- "deletePreferenceForDomain:preference:UID:withReply:"
- "deliverDidWrite:on:"
- "deliverEvent:on:"
- "deliverWillWrite:on:"
- "description"
- "didReceiveDiagnosticLog:ofType:details:"
- "didWriteDiagnosticLog:logId:logFilePath:logInfo:error:"
- "didWriteDiagnosticLog:ofType:toPath:"
- "didWriteLog:"
- "encodeObject:forKey:"
- "encodeWithCoder:"
- "failedToWriteDiagnosticLog:ofType:error:"
- "filePath"
- "hash"
- "indexOfObjectPassingTest:"
- "init"
- "initWithCoder:"
- "initWithIdentity:details:"
- "initWithIdentity:error:"
- "initWithIdentity:filePath:"
- "initWithIncidentID:bugType:"
- "initWithMachServiceName:options:"
- "initWithObserver:"
- "initWithObserver:bugTypes:"
- "interfaceWithProtocol:"
- "invalidate"
- "isEqual:"
- "isEqualToString:"
- "isKindOfClass:"
- "isMemberOfClass:"
- "isProxy"
- "localizedDescription"
- "matches:"
- "objectAtIndexedSubscript:"
- "observer"
- "performSelector:"
- "performSelector:withObject:"
- "performSelector:withObject:withObject:"
- "propertyListWithData:options:format:error:"
- "q_addEventObserver:forTypes:"
- "q_addWriteObserver:forTypes:"
- "q_computeEventObserverTypes"
- "q_computeWriteObserverTypes"
- "q_registerForEventTypes"
- "q_registerForWriteTypes"
- "q_removeEventObserver:andComputeObservedTypes:"
- "q_removeWriteObserver:andComputeObservedTypes:"
- "q_serverConnection"
- "q_shimWrappingObserver:creatingIfAbsent:removingIfPresent:"
- "q_teardownServerConnectionIfNoMoreObservers"
- "queryKey:"
- "raise:format:"
- "receivedLogEvent:"
- "registerForEvents:replyHandler:"
- "registerForWrites:replyHandler:"
- "release"
- "remoteObjectProxyWithErrorHandler:"
- "removeAllObjects"
- "removeEventObserver:"
- "removeObjectAtIndex:"
- "removeObserver:"
- "removeWriteObserver:"
- "respondsToSelector:"
- "resume"
- "retain"
- "retainCount"
- "self"
- "set"
- "setClasses:forSelector:argumentIndex:ofReply:"
- "setExportedInterface:"
- "setExportedObject:"
- "setInterruptionHandler:"
- "setPreference:forUser:inDomain:toValue:"
- "setPreferenceForDomain:preference:value:UID:withReply:"
- "setRemoteObjectInterface:"
- "setWithArray:"
- "setWithObjects:"
- "sharedClient"
- "sharedMonitor"
- "stringWithFormat:"
- "superclass"
- "supportsSecureCoding"
- "synchronousRemoteObjectProxyWithErrorHandler:"
- "uidForUser:"
- "unionSet:"
- "v16@0:8"
- "v24@0:8@\"NSCoder\"16"
- "v24@0:8@\"OSALogEvent\"16"
- "v24@0:8@\"OSALogIdentity\"16"
- "v24@0:8@\"OSALogWriteResult\"16"
- "v24@0:8@16"
- "v24@0:8@?16"
- "v24@0:8@?<v@?@\"NSString\">16"
- "v28@0:8@16B24"
- "v32@0:8@\"NSSet\"16@?<v@?@\"NSError\">24"
- "v32@0:8@\"NSString\"16@\"NSString\"24"
- "v32@0:8@16@24"
- "v32@0:8@16@?24"
- "v40@0:8@\"NSString\"16@\"NSString\"24@\"NSDictionary\"32"
- "v40@0:8@\"NSString\"16@\"NSString\"24@\"NSError\"32"
- "v40@0:8@\"NSString\"16@\"NSString\"24@\"NSString\"32"
- "v40@0:8@16@24@32"
- "v44@0:8@\"NSString\"16@\"NSString\"24I32@?<v@?B>36"
- "v44@0:8@16@24I32@?36"
- "v52@0:8@\"NSString\"16@\"NSString\"24@32I40@?<v@?B>44"
- "v52@0:8@16@24@32I40@?44"
- "willWriteDiagnosticLog:logId:logInfo:"
- "willWriteDiagnosticLog:ofType:"
- "willWriteLog:"
- "zone"

```
