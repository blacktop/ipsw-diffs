## FamilyControlsObjC

> `/System/Library/PrivateFrameworks/FamilyControlsObjC.framework/FamilyControlsObjC`

```diff

-1223.120.2.0.0
-  __TEXT.__text: 0x2c30
-  __TEXT.__auth_stubs: 0x2a0
+1242.0.0.0.0
+  __TEXT.__text: 0x2af0
   __TEXT.__objc_methlist: 0x300
-  __TEXT.__const: 0x70
-  __TEXT.__gcc_except_tab: 0x48
-  __TEXT.__cstring: 0x12e
+  __TEXT.__const: 0x68
+  __TEXT.__gcc_except_tab: 0x44
+  __TEXT.__cstring: 0x132
   __TEXT.__oslogstring: 0x31f
-  __TEXT.__unwind_info: 0x140
-  __TEXT.__objc_classname: 0xa1
-  __TEXT.__objc_methname: 0xaa9
-  __TEXT.__objc_methtype: 0x18a
-  __TEXT.__objc_stubs: 0x700
-  __DATA_CONST.__got: 0x90
+  __TEXT.__unwind_info: 0x130
+  __TEXT.__objc_stubs: 0x0
+  __TEXT.__auth_stubs: 0x0
+  __TEXT.__objc_classname: 0x0
+  __TEXT.__objc_methname: 0x0
+  __TEXT.__objc_methtype: 0x0
   __DATA_CONST.__const: 0x148
   __DATA_CONST.__objc_classlist: 0x28
   __DATA_CONST.__objc_protolist: 0x18

   __DATA_CONST.__objc_selrefs: 0x280
   __DATA_CONST.__objc_protorefs: 0x8
   __DATA_CONST.__objc_superrefs: 0x10
-  __AUTH_CONST.__auth_got: 0x160
+  __DATA_CONST.__got: 0x90
   __AUTH_CONST.__const: 0x20
   __AUTH_CONST.__cfstring: 0x160
   __AUTH_CONST.__objc_const: 0x560
+  __AUTH_CONST.__auth_got: 0x0
   __AUTH.__objc_data: 0x50
   __DATA.__objc_ivar: 0x1c
   __DATA.__data: 0x120

   - /System/Library/Frameworks/Foundation.framework/Foundation
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: EDD1729C-3B23-33D8-B868-405ECEEC46A9
-  Functions: 83
-  Symbols:   377
-  CStrings:  167
+  UUID: D4B202B9-A87B-3A65-8ADA-615B198714EF
+  Functions: 79
+  Symbols:   375
+  CStrings:  36
 
Symbols:
+ _objc_claimAutoreleasedReturnValue
+ _objc_retainAutoreleaseReturnValue
+ _objc_retain_x1
+ _objc_retain_x2
+ _objc_retain_x3
+ _objc_retain_x4
+ _objc_retain_x8
- _OUTLINED_FUNCTION_4
- _OUTLINED_FUNCTION_5
- _objc_retainAutoreleasedReturnValue
CStrings:
- ".cxx_destruct"
- "@\"NSObject\""
- "@\"NSString\""
- "@\"NSUUID\""
- "@\"NSXPCConnection\""
- "@16@0:8"
- "@24@0:8@\"NSCoder\"16"
- "@24@0:8@16"
- "@56@0:8@16@24@32q40q48"
- "B16@0:8"
- "B24@0:8@16"
- "FOAgentConnectionPrivate"
- "FOAuthorizationCenter"
- "FOAuthorizationRecord"
- "FOFamilyControlsAgentPrivate"
- "FOLocations"
- "FOXPCRemoteObjectProxy"
- "NSCoding"
- "NSSecureCoding"
- "Q16@0:8"
- "T@\"FOAuthorizationCenter\",R"
- "T@\"NSArray\",R"
- "T@\"NSObject\",R,N,V_connectionLock"
- "T@\"NSString\",R,C,V_bundleIdentifier"
- "T@\"NSString\",R,C,V_teamIdentifier"
- "T@\"NSURL\",R"
- "T@\"NSUUID\",R,C,V_recordIdentifier"
- "T@\"NSXPCConnection\",&,N,V_currentConnection"
- "TB,R"
- "Tq,R,V_status"
- "Tq,R,V_type"
- "URLByAppendingPathComponent:isDirectory:"
- "_bundleIdentifier"
- "_connectionLock"
- "_currentConnection"
- "_recordIdentifier"
- "_status"
- "_teamIdentifier"
- "_type"
- "activate"
- "addObject:"
- "authorizationRecords"
- "authorizationRecordsWithReplyHandler:"
- "authorizationsPlist"
- "clearCurrentConnectionAndInvalidate:"
- "code"
- "connectionLock"
- "containsValueForKey:"
- "copy"
- "countByEnumeratingWithState:objects:count:"
- "currentConnection"
- "dealloc"
- "decodeIntegerForKey:"
- "decodeObjectOfClass:forKey:"
- "domain"
- "encodeInteger:forKey:"
- "encodeObject:forKey:"
- "encodeWithCoder:"
- "familyControlsAuthorization"
- "familyControlsDirectory"
- "fetchAllSharedActivity"
- "fileURLWithPath:"
- "fileURLWithPath:isDirectory:"
- "hash"
- "init"
- "initWithBundleIdentifier:teamIdentifier:recordIdentifier:status:type:"
- "initWithCoder:"
- "initWithContentsOfURL:error:"
- "initWithMachServiceName:options:"
- "initWithUUIDString:"
- "integerValue"
- "interfaceWithProtocol:"
- "invalidate"
- "isEqual:"
- "isEqualToString:"
- "newConnection"
- "newInterface"
- "path"
- "proxyFromConnection:withRetryCount:proxyHandler:"
- "q"
- "q16@0:8"
- "remoteObjectProxyWithErrorHandler:"
- "removeAllActivityWithReplyHandler:"
- "requestAuthorizationForRecordIdentifier:completionHandler:"
- "requestAuthorizationWithRecordIdentifier:replyHandler:"
- "requestDataAccessAuthorizationForRecordIdentifier:completionHandler:"
- "requestDataAccessAuthorizationWithRecordIdentifier:replyHandler:"
- "requestInternalAuthorizationForMember:completionHandler:"
- "requestInternalAuthorizationForMember:replyHandler:"
- "resetAuthorizationForRecordIdentifier:completionHandler:"
- "resetAuthorizationWithRecordIdentifier:replyHandler:"
- "resetDataAccessAuthorizationsWithCompletionHandler:"
- "resetDataAccessAuthorizationsWithReplyHandler:"
- "revokeAuthorizationForDeletionForRecordIdentifier:completionHandler:"
- "revokeAuthorizationForDeletionWithRecordIdentifier:replyHandler:"
- "revokeAuthorizationForRecordIdentifier:completionHandler:"
- "revokeAuthorizationWithRecordIdentifier:replyHandler:"
- "revokeInternalAuthorizationWithCompletionHandler:"
- "revokeInternalAuthorizationWithReplyHandler:"
- "serviceName"
- "setCurrentConnection:"
- "setInterruptionHandler:"
- "setInvalidationHandler:"
- "setRemoteObjectInterface:"
- "sharedCenter"
- "sharedDirectory"
- "silentlyResetAuthorizationForRecordIdentifier:completionHandler:"
- "silentlyResetAuthorizationWithRecordIdentifier:replyHandler:"
- "supportsSecureCoding"
- "synchronousProxyFromConnection:withRetryCount:proxyHandler:"
- "synchronousRemoteObjectProxyWithErrorHandler:"
- "updateActivityWithReplyHandler:"
- "v16@0:8"
- "v20@0:8B16"
- "v24@0:8@\"NSCoder\"16"
- "v24@0:8@16"
- "v24@0:8@?16"
- "v24@0:8@?<v@?@\"NSArray\"@\"NSError\">16"
- "v24@0:8@?<v@?@\"NSError\">16"
- "v32@0:8@\"NSUUID\"16@?<v@?@\"NSError\">24"
- "v32@0:8@16@?24"
- "v32@0:8q16@?24"
- "v32@0:8q16@?<v@?@\"NSError\">24"
- "v40@0:8@16Q24@?32"
- "valueForKey:"
- "xpcConnection"

```
