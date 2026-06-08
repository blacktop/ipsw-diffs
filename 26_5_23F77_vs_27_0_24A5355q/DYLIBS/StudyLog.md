## StudyLog

> `/System/Library/PrivateFrameworks/StudyLog.framework/StudyLog`

```diff

 35.0.0.0.0
-  __TEXT.__text: 0x5118
-  __TEXT.__auth_stubs: 0x4b0
+  __TEXT.__text: 0x5048
   __TEXT.__objc_methlist: 0x8ac
   __TEXT.__const: 0x60
-  __TEXT.__cstring: 0x217
+  __TEXT.__cstring: 0x225
   __TEXT.__gcc_except_tab: 0x5c
   __TEXT.__oslogstring: 0x6f
-  __TEXT.__unwind_info: 0x278
-  __TEXT.__objc_classname: 0x133
-  __TEXT.__objc_methname: 0xd70
-  __TEXT.__objc_methtype: 0x661
-  __TEXT.__objc_stubs: 0xc00
-  __DATA_CONST.__got: 0xb8
+  __TEXT.__unwind_info: 0x288
+  __TEXT.__objc_stubs: 0x0
+  __TEXT.__auth_stubs: 0x0
+  __TEXT.__objc_classname: 0x0
+  __TEXT.__objc_methname: 0x0
+  __TEXT.__objc_methtype: 0x0
   __DATA_CONST.__const: 0x388
   __DATA_CONST.__objc_classlist: 0x38
   __DATA_CONST.__objc_protolist: 0x40

   __DATA_CONST.__objc_selrefs: 0x498
   __DATA_CONST.__objc_protorefs: 0x10
   __DATA_CONST.__objc_superrefs: 0x18
-  __AUTH_CONST.__auth_got: 0x268
+  __DATA_CONST.__got: 0xb8
   __AUTH_CONST.__const: 0x60
   __AUTH_CONST.__cfstring: 0x240
   __AUTH_CONST.__objc_const: 0x2140
+  __AUTH_CONST.__auth_got: 0x0
   __DATA.__objc_ivar: 0x7c
   __DATA.__data: 0x300
   __DATA.__bss: 0x18

   - /System/Library/Frameworks/Foundation.framework/Foundation
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: DF76D3CC-D602-35E2-B4AE-E6B9451022DA
-  Functions: 198
-  Symbols:   799
-  CStrings:  330
+  UUID: B5459CA3-D794-3517-BDE3-F9384B3A4F96
+  Functions: 196
+  Symbols:   797
+  CStrings:  53
 
Symbols:
+ _objc_claimAutoreleasedReturnValue
+ _objc_retainAutoreleaseReturnValue
+ _objc_retain_x1
+ _objc_retain_x3
- _OUTLINED_FUNCTION_1
- _OUTLINED_FUNCTION_2
- _objc_retain_x25
- _objc_retain_x26
CStrings:
- "#16@0:8"
- ".cxx_destruct"
- "@\"<SLGActivatableLogging>\""
- "@\"<SLGDomainWhitelisting>\""
- "@\"<SLGLogClientProtocol>\""
- "@\"<SLGLogClientProtocolDelegate>\""
- "@\"<SLGLogClientProtocolDelegate>\"16@0:8"
- "@\"<SLGLogging>\""
- "@\"NSDateFormatter\""
- "@\"NSHashTable\""
- "@\"NSMutableDictionary\""
- "@\"NSMutableSet\""
- "@\"NSNumber\""
- "@\"NSObject<OS_dispatch_queue>\""
- "@\"NSObject<OS_dispatch_source>\""
- "@\"NSSet\""
- "@\"NSSet\"16@0:8"
- "@\"NSString\""
- "@\"NSString\"16@0:8"
- "@\"NSXPCConnection\""
- "@16@0:8"
- "@24@0:8:16"
- "@24@0:8@16"
- "@24@0:8i16i20"
- "@32@0:8:16@24"
- "@32@0:8@16d24"
- "@36@0:8@16@24B32"
- "@40@0:8:16@24@32"
- "@40@0:8@16@24@32"
- "@48@0:8@16@24@32^@40"
- "@?"
- "@?16@0:8"
- "@?<v@?@\"<SLGActivatableLogging>\">16@0:8"
- "B"
- "B16@0:8"
- "B24@0:8#16"
- "B24@0:8:16"
- "B24@0:8@\"NSString\"16"
- "B24@0:8@\"Protocol\"16"
- "B24@0:8@16"
- "NSObject"
- "Q16@0:8"
- "SLGActivatableLogger"
- "SLGActivatableLogging"
- "SLGDomainWhitelisting"
- "SLGLog"
- "SLGLogClient"
- "SLGLogClientProtocol"
- "SLGLogClientProtocolDelegate"
- "SLGLogService"
- "SLGLogXPCClient"
- "SLGLogging"
- "SLGNotificationActivatedLogger"
- "SLGNotificationActivatedLoggerRegistration"
- "SLGTimedLogger"
- "T#,R"
- "T@\"<SLGLogClientProtocolDelegate>\",W,N"
- "T@\"<SLGLogClientProtocolDelegate>\",W,N,V_delegate"
- "T@\"NSSet\",R,C,N"
- "T@\"NSSet\",R,N"
- "T@\"NSString\",?,R,C"
- "T@\"NSString\",R,C"
- "T@?,C,N"
- "TB,N"
- "TB,N,GisActive"
- "TQ,R"
- "Ti,N,V_beginToken"
- "Ti,N,V_endToken"
- "UTF8String"
- "UUID"
- "UUIDString"
- "Vv16@0:8"
- "^{_NSZone=}16@0:8"
- "_activationHandler"
- "_active"
- "_activeReasons"
- "_allowUnspecifiedDomains"
- "_beginLoggingForReason:"
- "_beginObservingSettings"
- "_beginToken"
- "_calloutQueue"
- "_cancelRegistrations"
- "_client"
- "_connectWithCompletion:"
- "_connection"
- "_dateFormatter"
- "_deactivationHandler"
- "_delegate"
- "_duration"
- "_endLoggingForReason:"
- "_endToken"
- "_fetchProcessInfo"
- "_handshake"
- "_isEnabled"
- "_lock"
- "_lockQueue"
- "_lockQueue_loadSettings"
- "_lockQueue_loadUnspecifiedDomains"
- "_lockQueue_loadWhitelist"
- "_logger"
- "_observerCalloutQueue"
- "_observerLockQueue"
- "_observers"
- "_pid"
- "_processName"
- "_registrationsByReason"
- "_reloadSettings"
- "_serializeObjectAsLogEntry:domain:tags:error:"
- "_setClient:"
- "_startTimer"
- "_stopObservingSettings"
- "_stopTimer"
- "_timer"
- "_whitelist"
- "_wrapObjectWithEntryMetadata:domain:tags:"
- "activationHandler"
- "active"
- "addBeginNotification:endNotification:"
- "addDomain:"
- "addDomainToWhitelist:"
- "addObject:"
- "addObserver:"
- "allObjects"
- "allowUnspecifiedDomains"
- "autorelease"
- "beginSession"
- "beginSessionWithCompletion:"
- "beginSessionWithJSONMetadata:completion:"
- "beginToken"
- "boolValue"
- "class"
- "client:didReceiveInitialLogMessageFromDomain:"
- "clientDidReceiveServerReset:"
- "conformsToProtocol:"
- "containsObject:"
- "copy"
- "count"
- "countByEnumeratingWithState:objects:count:"
- "d"
- "dataWithJSONObject:options:error:"
- "deactivationHandler"
- "dealloc"
- "debugDescription"
- "delegate"
- "description"
- "dictionary"
- "dictionaryWithObjects:forKeys:count:"
- "didReceiveInitialLogMessageFromDomain:"
- "endSession"
- "endSessionAndRenameFileTo:withCompletion:"
- "endSessionAndRenameFileTo:withJSONMetadata:completion:"
- "endSessionWithCompletion:"
- "endToken"
- "enumerateObjectsUsingBlock:"
- "errorWithDomain:code:userInfo:"
- "handshake"
- "hash"
- "i"
- "i16@0:8"
- "init"
- "initWithClient:whitelist:enabled:"
- "initWithLogger:"
- "initWithLogger:duration:"
- "initWithMachServiceName:options:"
- "interfaceWithProtocol:"
- "invalidate"
- "isActive"
- "isDomainWhitelisted:"
- "isEnabled"
- "isEqual:"
- "isKindOfClass:"
- "isMemberOfClass:"
- "isProxy"
- "log:"
- "log:completion:"
- "log:didReceiveInitialLogMessageFromDomain:"
- "log:domain:"
- "log:domain:completion:"
- "log:domain:tags:"
- "log:domain:tags:completion:"
- "log:tags:"
- "log:tags:completion:"
- "logBlock:"
- "logBlock:completion:"
- "logBlock:domain:"
- "logBlock:domain:completion:"
- "logBlock:domain:tags:"
- "logBlock:domain:tags:completion:"
- "logBlock:tags:"
- "logBlock:tags:completion:"
- "logDidReceiveResetFromServer:"
- "logJSONData:domain:completion:"
- "mutableCopy"
- "numberWithBool:"
- "numberWithDouble:"
- "numberWithInt:"
- "numberWithUnsignedLongLong:"
- "objectForKeyedSubscript:"
- "performSelector:"
- "performSelector:withObject:"
- "performSelector:withObject:withObject:"
- "queryServer:errorHandler:"
- "registrationWithBeginToken:endToken:"
- "release"
- "remoteObjectProxy"
- "remoteObjectProxyWithErrorHandler:"
- "removeAllObjects"
- "removeDomain:"
- "removeDomainFromWhitelist:"
- "removeObject:"
- "removeObserver:"
- "reset"
- "reset:completion:"
- "resetWithCompletion:"
- "respondsToSelector:"
- "resume"
- "retain"
- "retainCount"
- "self"
- "serverDidReset"
- "set"
- "setActivationHandler:"
- "setActive:"
- "setAllowUnspecifiedDomains:"
- "setBeginToken:"
- "setByAddingObject:"
- "setDeactivationHandler:"
- "setDelegate:"
- "setEndToken:"
- "setExportedInterface:"
- "setExportedObject:"
- "setInterruptionHandler:"
- "setInvalidationHandler:"
- "setObject:forKeyedSubscript:"
- "setRemoteObjectInterface:"
- "sharedInstance"
- "stringWithCString:encoding:"
- "stringWithFormat:"
- "superclass"
- "timeIntervalSince1970"
- "v16@0:8"
- "v20@0:8B16"
- "v20@0:8i16"
- "v24@0:8@\"<SLGLogClientProtocol>\"16"
- "v24@0:8@\"<SLGLogClientProtocolDelegate>\"16"
- "v24@0:8@\"NSString\"16"
- "v24@0:8@16"
- "v24@0:8@?16"
- "v24@0:8@?<v@?@\"<SLGActivatableLogging>\">16"
- "v32@0:8@\"<SLGLogClientProtocol>\"16@\"NSString\"24"
- "v32@0:8@\"NSData\"16@?<v@?B@\"NSError\">24"
- "v32@0:8@16@24"
- "v32@0:8@16@?24"
- "v32@0:8@?16@24"
- "v32@0:8@?16@?24"
- "v32@0:8@?<@@?>16@\"NSString\"24"
- "v32@0:8@?<v@?@\"<SLGLogService>\">16@?<v@?B@\"NSError\">24"
- "v32@0:8Q16@?24"
- "v32@0:8Q16@?<v@?B@\"NSError\">24"
- "v40@0:8@\"NSData\"16@\"NSString\"24@?<v@?B@\"NSError\">32"
- "v40@0:8@\"NSString\"16@\"NSData\"24@?<v@?B@\"NSError\">32"
- "v40@0:8@16@24@32"
- "v40@0:8@16@24@?32"
- "v40@0:8@?16@24@?32"
- "v40@0:8@?16@?24@?32"
- "v40@0:8@?<@@?>16@\"NSString\"24@?<@\"NSArray\"@?>32"
- "v40@0:8@?<@@?>16@\"NSString\"24@?<v@?B@\"NSError\">32"
- "v48@0:8@16@24@32@?40"
- "v48@0:8@?16@24@?32@?40"
- "v48@0:8@?<@@?>16@\"NSString\"24@?<@\"NSArray\"@?>32@?<v@?B@\"NSError\">40"
- "weakObjectsHashTable"
- "whitelist"
- "whitelistedDomains"
- "zone"
- "{os_unfair_lock_s=\"_os_unfair_lock_opaque\"I}"

```
