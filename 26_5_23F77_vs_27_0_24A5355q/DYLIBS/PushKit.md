## PushKit

> `/System/Library/Frameworks/PushKit.framework/PushKit`

```diff

-109.500.11.0.0
-  __TEXT.__text: 0x4ce4
-  __TEXT.__auth_stubs: 0x400
+111.100.1.0.0
+  __TEXT.__text: 0x4998
   __TEXT.__objc_methlist: 0x798
   __TEXT.__const: 0x48
   __TEXT.__gcc_except_tab: 0x84
-  __TEXT.__cstring: 0x646
-  __TEXT.__unwind_info: 0x238
-  __TEXT.__objc_classname: 0x1a9
-  __TEXT.__objc_methname: 0x13f5
-  __TEXT.__objc_methtype: 0x315
-  __TEXT.__objc_stubs: 0xac0
-  __DATA_CONST.__got: 0x98
+  __TEXT.__cstring: 0x651
+  __TEXT.__unwind_info: 0x208
+  __TEXT.__objc_stubs: 0x0
+  __TEXT.__auth_stubs: 0x0
+  __TEXT.__objc_classname: 0x0
+  __TEXT.__objc_methname: 0x0
+  __TEXT.__objc_methtype: 0x0
   __DATA_CONST.__const: 0x340
   __DATA_CONST.__objc_classlist: 0x30
   __DATA_CONST.__objc_protolist: 0x50

   __DATA_CONST.__objc_selrefs: 0x510
   __DATA_CONST.__objc_protorefs: 0x40
   __DATA_CONST.__objc_superrefs: 0x18
-  __AUTH_CONST.__auth_got: 0x210
+  __DATA_CONST.__got: 0x98
   __AUTH_CONST.__const: 0x80
   __AUTH_CONST.__cfstring: 0x3a0
   __AUTH_CONST.__objc_const: 0xe28
+  __AUTH_CONST.__auth_got: 0x0
   __AUTH.__objc_data: 0x50
   __DATA.__objc_ivar: 0x68
   __DATA.__data: 0x3c0

   - /System/Library/Frameworks/Security.framework/Security
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: F13C811C-DDA1-3F31-8BA0-7721C297CDA3
-  Functions: 161
-  Symbols:   661
-  CStrings:  353
+  UUID: 5045482C-BE49-35B0-8ED4-032CA5B34355
+  Functions: 162
+  Symbols:   673
+  CStrings:  70
 
Symbols:
+ ___73-[PKPushRegistry voipPayloadReceived:mustPostCall:withCompletionHandler:]_block_invoke_7
+ _dispatch_after
+ _dispatch_time
+ _objc_claimAutoreleasedReturnValue
+ _objc_retainAutoreleaseReturnValue
+ _objc_retain_x1
+ _objc_retain_x2
+ _objc_retain_x23
+ _objc_retain_x25
+ _objc_retain_x28
+ _objc_retain_x8
CStrings:
- "#16@0:8"
- ".cxx_destruct"
- "@\"<PKPushRegistryDelegate>\""
- "@\"NSData\""
- "@\"NSDictionary\""
- "@\"NSMutableDictionary\""
- "@\"NSMutableSet\""
- "@\"NSObject<OS_dispatch_queue>\""
- "@\"NSSet\""
- "@\"NSString\""
- "@\"NSString\"16@0:8"
- "@\"NSXPCConnection\""
- "@16@0:8"
- "@24@0:8:16"
- "@24@0:8@16"
- "@32@0:8:16@24"
- "@40@0:8:16@24@32"
- "@48@0:8@16@24@32Q40"
- "@56@0:8@16@24@32@40Q48"
- "B"
- "B16@0:8"
- "B24@0:8#16"
- "B24@0:8:16"
- "B24@0:8@\"Protocol\"16"
- "B24@0:8@16"
- "B24@0:8^{__CFString=}16"
- "NSObject"
- "PKComplicationXPCClient"
- "PKComplicationXPCServer"
- "PKFileProviderXPCClient"
- "PKFileProviderXPCServer"
- "PKPublicChannel"
- "PKPushCredentials"
- "PKPushPayload"
- "PKPushRegistry"
- "PKUserNotificationServerRemoteNotificationXPCClient"
- "PKUserNotificationServerRemoteNotificationXPCServer"
- "PKUserNotificationsConnectionClient"
- "PKUserNotificationsRemoteNotificationServiceConnection"
- "PKVoIPPushMetadata"
- "PKVoIPXPCClient"
- "PKVoIPXPCServer"
- "Q"
- "Q16@0:8"
- "T#,R"
- "T@\"<PKPushRegistryDelegate>\",W,V_delegate"
- "T@\"NSData\",C,V_token"
- "T@\"NSDictionary\",C,V_dictionaryPayload"
- "T@\"NSDictionary\",R,N"
- "T@\"NSMutableDictionary\",&,N,V_pushTypeToConnection"
- "T@\"NSMutableDictionary\",&,N,V_pushTypeToToken"
- "T@\"NSMutableSet\",&,N,V_registries"
- "T@\"NSObject<OS_dispatch_queue>\",&,N,V_callOutQueue"
- "T@\"NSObject<OS_dispatch_queue>\",&,N,V_delegateQueue"
- "T@\"NSObject<OS_dispatch_queue>\",&,N,V_ivarQueue"
- "T@\"NSObject<OS_dispatch_queue>\",&,N,V_queue"
- "T@\"NSSet\",C,V_desiredPushTypes"
- "T@\"NSString\",&,N,V_channelTopic"
- "T@\"NSString\",&,N,V_environment"
- "T@\"NSString\",&,N,V_tokenName"
- "T@\"NSString\",?,R,C"
- "T@\"NSString\",C,N,V_bundleIdentifier"
- "T@\"NSString\",C,N,V_channelID"
- "T@\"NSString\",C,V_type"
- "T@\"NSString\",R,C"
- "T@\"NSXPCConnection\",&,N,V_connection"
- "TB,V_mustReport"
- "TQ,N,V_checkpoint"
- "TQ,R"
- "Td,N,V_lastReportedCallTime"
- "Ti,N,V_complicationToken"
- "Ti,N,V_fileProviderToken"
- "Ti,N,V_outstandingVoIPPushes"
- "Ti,N,V_voipToken"
- "Vv16@0:8"
- "^{_NSZone=}16@0:8"
- "_assertIfCallKitNotLinked"
- "_bundleIdentifier"
- "_callOutQueue"
- "_channelID"
- "_channelTopic"
- "_checkpoint"
- "_complicationToken"
- "_connection"
- "_createConnectionForPushType:"
- "_delegate"
- "_delegateQueue"
- "_desiredPushTypes"
- "_dictionaryPayload"
- "_environment"
- "_fileProviderToken"
- "_invalidate"
- "_ivarQueue"
- "_lastReportedCallTime"
- "_mustReport"
- "_noteIncomingCallReported"
- "_outstandingVoIPPushes"
- "_pushTypeToConnection"
- "_pushTypeToMachServiceName"
- "_pushTypeToToken"
- "_queue"
- "_queue_ensureConnection"
- "_queue_interruptedConnection"
- "_queue_invalidatedConnection"
- "_queue_remoteUserNotificationPayloadReceived:completionHandler:"
- "_queue_remoteUserNotificationsRegistrationSucceededWithDeviceToken:"
- "_registerForPushType:"
- "_registries"
- "_renewConnectionForPushTypeIfRegistered:"
- "_selfTaskHasEntitlement:"
- "_terminateAppIfThereAreUnhandledVoIPPushes"
- "_token"
- "_tokenName"
- "_type"
- "_unregisterForPushType:"
- "_voipToken"
- "addObject:"
- "addObserver:selector:name:object:"
- "allowsRemoteNotifications"
- "autorelease"
- "bundleIdentifier"
- "callOutQueue"
- "channelID"
- "channelTopic"
- "class"
- "complicationPayloadReceived:"
- "complicationRegister"
- "complicationRegistrationFailed"
- "complicationRegistrationSucceededWithDeviceToken:"
- "complicationToken"
- "complicationUnregister"
- "conformsToProtocol:"
- "connection"
- "copy"
- "count"
- "countByEnumeratingWithState:objects:count:"
- "currentHandler"
- "d"
- "d16@0:8"
- "dealloc"
- "debugDescription"
- "defaultCenter"
- "delegate"
- "delegateQueue"
- "description"
- "desiredPushTypes"
- "dictionary"
- "dictionaryPayload"
- "dictionaryRepresentation"
- "dictionaryWithObjects:forKeys:count:"
- "didReceiveDeviceToken:forBundleIdentifier:"
- "fileProviderPayloadReceived:"
- "fileProviderRegister"
- "fileProviderRegistrationFailed"
- "fileProviderRegistrationSucceededWithDeviceToken:"
- "fileProviderToken"
- "fileProviderUnregister"
- "getAllowsRemoteNotificationsForBundleIdentifier:withCompletionHandler:"
- "handleFailureInMethod:object:file:lineNumber:description:"
- "hash"
- "i"
- "i16@0:8"
- "init"
- "initWithBundleIdentifier:"
- "initWithChannelID:"
- "initWithChannelID:channelTopic:environment:checkpoint:"
- "initWithChannelID:channelTopic:environment:tokenName:checkpoint:"
- "initWithDictionary:"
- "initWithMachServiceName:options:"
- "initWithQueue:"
- "interfaceWithProtocol:"
- "invalidate"
- "invalidateTokenForRemoteNotificationsForBundleIdentifier:"
- "isEqual:"
- "isEqualToString:"
- "isKindOfClass:"
- "isMemberOfClass:"
- "isProxy"
- "ivarQueue"
- "lastReportedCallTime"
- "mainBundle"
- "minusSet:"
- "mustReport"
- "mutableCopy"
- "numberWithUnsignedLongLong:"
- "objectForKeyedSubscript:"
- "outstandingVoIPPushes"
- "performSelector:"
- "performSelector:withObject:"
- "performSelector:withObject:withObject:"
- "pushRegistry:didInvalidatePushTokenForType:"
- "pushRegistry:didInvalidatePushTokenForType:error:"
- "pushRegistry:didReceiveIncomingPushWithPayload:forType:"
- "pushRegistry:didReceiveIncomingPushWithPayload:forType:withCompletionHandler:"
- "pushRegistry:didReceiveIncomingVoIPPushWithPayload:metadata:withCompletionHandler:"
- "pushRegistry:didUpdatePushCredentials:forType:"
- "pushTokenForType:"
- "pushTypeToConnection"
- "pushTypeToToken"
- "queue"
- "registerPushRegistry:completionHandler:"
- "registries"
- "release"
- "remoteObjectProxy"
- "remoteObjectProxyWithErrorHandler:"
- "remoteUserNotificationPayloadReceived:completionHandler:"
- "remoteUserNotificationRegistrationSucceededWithDeviceToken:"
- "removeObject:"
- "removeObjectForKey:"
- "requestTokenForRemoteNotificationsForBundleIdentifier:withCompletionHandler:"
- "resetCheckpoint"
- "respondsToSelector:"
- "resume"
- "retain"
- "retainCount"
- "self"
- "setBundleIdentifier:"
- "setCallOutQueue:"
- "setChannelID:"
- "setChannelTopic:"
- "setCheckpoint:"
- "setComplicationToken:"
- "setConnection:"
- "setDelegate:"
- "setDelegateQueue:"
- "setDesiredPushTypes:"
- "setDictionaryPayload:"
- "setEnvironment:"
- "setExportedInterface:"
- "setExportedObject:"
- "setFileProviderToken:"
- "setInterruptionHandler:"
- "setInvalidationHandler:"
- "setIvarQueue:"
- "setLastReportedCallTime:"
- "setMustReport:"
- "setObject:forKeyedSubscript:"
- "setOutstandingVoIPPushes:"
- "setPushTypeToConnection:"
- "setPushTypeToToken:"
- "setQueue:"
- "setRegistries:"
- "setRemoteObjectInterface:"
- "setToken:"
- "setTokenName:"
- "setType:"
- "setVoipToken:"
- "sharedInstance"
- "stringWithFormat:"
- "superclass"
- "synchronousRemoteObjectProxyWithErrorHandler:"
- "timeIntervalSinceReferenceDate"
- "token"
- "tokenName"
- "type"
- "unregisterPushRegistry:"
- "unsignedLongLongValue"
- "v16@0:8"
- "v20@0:8B16"
- "v20@0:8i16"
- "v24@0:8@\"NSData\"16"
- "v24@0:8@\"NSDictionary\"16"
- "v24@0:8@\"NSString\"16"
- "v24@0:8@16"
- "v24@0:8Q16"
- "v24@0:8d16"
- "v32@0:8@\"NSData\"16@\"NSString\"24"
- "v32@0:8@\"NSDictionary\"16@?<v@?>24"
- "v32@0:8@\"NSString\"16@?<v@?B>24"
- "v32@0:8@\"NSString\"16@?<v@?B@\"NSError\">24"
- "v32@0:8@16@24"
- "v32@0:8@16@?24"
- "v36@0:8@\"NSDictionary\"16B24@?<v@?>28"
- "v36@0:8@16B24@?28"
- "voipPayloadReceived:mustPostCall:withCompletionHandler:"
- "voipRegister"
- "voipRegistrationFailed"
- "voipRegistrationSucceededWithDeviceToken:"
- "voipToken"
- "voipUnregister"
- "zone"

```
