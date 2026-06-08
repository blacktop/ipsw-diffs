## AdPlatformsInternal

> `/System/Library/PrivateFrameworks/AdPlatformsInternal.framework/AdPlatformsInternal`

```diff

-637.5.1.0.0
-  __TEXT.__text: 0x19a4
-  __TEXT.__auth_stubs: 0x2d0
+638.0.7.0.0
+  __TEXT.__text: 0x17a0
   __TEXT.__objc_methlist: 0x294
   __TEXT.__const: 0x48
   __TEXT.__gcc_except_tab: 0x60
-  __TEXT.__cstring: 0x953
-  __TEXT.__unwind_info: 0xf0
-  __TEXT.__objc_classname: 0x60
-  __TEXT.__objc_methname: 0x7dc
-  __TEXT.__objc_methtype: 0x1be
-  __TEXT.__objc_stubs: 0x6c0
-  __DATA_CONST.__got: 0xc0
+  __TEXT.__cstring: 0x955
+  __TEXT.__unwind_info: 0xd0
+  __TEXT.__objc_stubs: 0x0
+  __TEXT.__auth_stubs: 0x0
+  __TEXT.__objc_classname: 0x0
+  __TEXT.__objc_methname: 0x0
+  __TEXT.__objc_methtype: 0x0
   __DATA_CONST.__const: 0x108
   __DATA_CONST.__objc_classlist: 0x10
   __DATA_CONST.__objc_protolist: 0x18

   __DATA_CONST.__objc_protorefs: 0x8
   __DATA_CONST.__objc_superrefs: 0x10
   __DATA_CONST.__objc_arraydata: 0x20
-  __AUTH_CONST.__auth_got: 0x178
+  __DATA_CONST.__got: 0xc0
   __AUTH_CONST.__const: 0x20
   __AUTH_CONST.__cfstring: 0x6e0
   __AUTH_CONST.__objc_const: 0x3f0
   __AUTH_CONST.__objc_dictobj: 0x50
+  __AUTH_CONST.__auth_got: 0x0
   __DATA.__objc_ivar: 0x18
   __DATA.__data: 0x120
   __DATA_DIRTY.__objc_data: 0xa0

   - /usr/lib/libMobileGestalt.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 20C55BB1-FBB7-3E97-95C0-94F9BF63DEA6
+  UUID: 30014693-D440-3AA1-970F-175C747985B6
   Functions: 33
-  Symbols:   250
-  CStrings:  250
+  Symbols:   251
+  CStrings:  111
 
Symbols:
+ _objc_claimAutoreleasedReturnValue
+ _objc_retainAutoreleaseReturnValue
+ _objc_retain_x2
+ _objc_retain_x24
+ _objc_retain_x25
- _objc_autoreleaseReturnValue
- _objc_retain
- _objc_retainAutoreleasedReturnValue
- _objc_retain_x21
CStrings:
- "#16@0:8"
- ".cxx_destruct"
- "@\"NSMutableDictionary\""
- "@\"NSNumber\""
- "@\"NSString\""
- "@\"NSString\"16@0:8"
- "@\"NSXPCConnection\""
- "@\"NSXPCListener\""
- "@16@0:8"
- "@24@0:8:16"
- "@32@0:8:16@24"
- "@40@0:8:16@24@32"
- "@40@0:8@16@24@32"
- "ADAttributionRequester"
- "ADAttributionService"
- "ADAttribution_XPC"
- "AD_jsonString"
- "B16@0:8"
- "B24@0:8#16"
- "B24@0:8:16"
- "B24@0:8@\"Protocol\"16"
- "B24@0:8@16"
- "B32@0:8@\"NSXPCListener\"16@\"NSXPCConnection\"24"
- "B32@0:8@16@24"
- "NSObject"
- "NSXPCListenerDelegate"
- "Q16@0:8"
- "T#,R"
- "T@\"NSMutableDictionary\",&,N,V_clients"
- "T@\"NSNumber\",&,N,V_transactionID"
- "T@\"NSNumber\",&,N,V_transactionToken"
- "T@\"NSString\",&,N,V_bundleID"
- "T@\"NSString\",?,R,C"
- "T@\"NSString\",R,C"
- "T@\"NSXPCConnection\",&,N,V_connection"
- "T@\"NSXPCListener\",&,V_listener"
- "TQ,R"
- "Vv16@0:8"
- "^{_NSZone=}16@0:8"
- "_bundleID"
- "_clients"
- "_connection"
- "_isAppTrackingAuthorized"
- "_listener"
- "_transactionID"
- "_transactionToken"
- "activeDSIDRecord"
- "addOperationWithBlock:"
- "auditToken"
- "autorelease"
- "beginAttributionRequest:reason:completionHandler:"
- "boolValue"
- "bundle"
- "bundleID"
- "bundleInfoValueForKey:"
- "class"
- "clients"
- "conformsToProtocol:"
- "connection"
- "createNewWatchdog:withTimer:"
- "debugDescription"
- "defaultCenter"
- "description"
- "dictionary"
- "dictionaryWithObjects:forKeys:count:"
- "errorWithDomain:code:userInfo:"
- "handleForIdentifier:error:"
- "hash"
- "iTunesAccountDSID"
- "init"
- "initWithConnection:bundleID:transactionID:"
- "initWithMachServiceName:"
- "interfaceWithProtocol:"
- "isAccountRestricted"
- "isBoolSettingLockedDownByRestrictions:"
- "isEqual:"
- "isKindOfClass:"
- "isMemberOfClass:"
- "isProxy"
- "length"
- "listener"
- "listener:shouldAcceptNewConnection:"
- "localizedStringForKey:value:table:"
- "mainBundle"
- "numberWithInt:"
- "numberWithUnsignedInt:"
- "performOperationAfterReconcile:"
- "performSelector:"
- "performSelector:withObject:"
- "performSelector:withObject:withObject:"
- "postNotificationName:object:userInfo:"
- "processIdentifier"
- "reconcileInProgress"
- "release"
- "removeClientForToken:"
- "removeObjectForKey:"
- "removeWatchdogWithToken:"
- "requestAttributionDetails:"
- "requestAttributionDetailsWithBlock:"
- "respondsToSelector:"
- "resume"
- "retain"
- "retainCount"
- "self"
- "setBool:forKey:"
- "setBundleID:"
- "setClients:"
- "setConfigurationExpirationTime:"
- "setConnection:"
- "setDSID:completionHandler:"
- "setDelegate:"
- "setExportedInterface:"
- "setExportedObject:"
- "setInterruptionHandler:"
- "setInvalidationHandler:"
- "setListener:"
- "setObject:forKeyedSubscript:"
- "setRemoteObjectInterface:"
- "setServerToTest:"
- "setStocksAdEnabled:"
- "setString:forKey:"
- "setTransactionID:"
- "setTransactionToken:"
- "sharedConnection"
- "sharedInstance"
- "stringWithFormat:"
- "superclass"
- "transactionID"
- "transactionToken"
- "v16@0:8"
- "v20@0:8B16"
- "v24@0:8@16"
- "v24@0:8@?16"
- "v24@0:8@?<v@?@\"NSDictionary\"@\"NSError\">16"
- "v24@0:8q16"
- "v40@0:8@16@24@?32"
- "valueForEntitlement:"
- "workQueue"
- "zone"

```
