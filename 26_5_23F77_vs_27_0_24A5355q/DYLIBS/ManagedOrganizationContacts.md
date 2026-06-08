## ManagedOrganizationContacts

> `/System/Library/PrivateFrameworks/ManagedOrganizationContacts.framework/ManagedOrganizationContacts`

```diff

-151.5.0.0.0
-  __TEXT.__text: 0x29c4
-  __TEXT.__auth_stubs: 0x2a0
+152.0.10.0.0
+  __TEXT.__text: 0x259c
   __TEXT.__objc_methlist: 0x5e4
   __TEXT.__const: 0x68
-  __TEXT.__gcc_except_tab: 0x34
-  __TEXT.__cstring: 0x1e9
-  __TEXT.__unwind_info: 0x1c0
-  __TEXT.__objc_classname: 0x193
-  __TEXT.__objc_methname: 0x946
-  __TEXT.__objc_methtype: 0x294
-  __TEXT.__objc_stubs: 0x840
-  __DATA_CONST.__got: 0x98
+  __TEXT.__gcc_except_tab: 0x38
+  __TEXT.__cstring: 0x1f4
+  __TEXT.__unwind_info: 0x150
+  __TEXT.__objc_stubs: 0x0
+  __TEXT.__auth_stubs: 0x0
+  __TEXT.__objc_classname: 0x0
+  __TEXT.__objc_methname: 0x0
+  __TEXT.__objc_methtype: 0x0
   __DATA_CONST.__const: 0xf0
   __DATA_CONST.__objc_classlist: 0x38
   __DATA_CONST.__objc_protolist: 0x30

   __DATA_CONST.__objc_selrefs: 0x308
   __DATA_CONST.__objc_protorefs: 0x10
   __DATA_CONST.__objc_superrefs: 0x38
-  __AUTH_CONST.__auth_got: 0x160
+  __DATA_CONST.__got: 0x98
   __AUTH_CONST.__const: 0xa0
   __AUTH_CONST.__cfstring: 0x320
   __AUTH_CONST.__objc_const: 0xa70
+  __AUTH_CONST.__auth_got: 0x0
   __DATA.__objc_ivar: 0x2c
   __DATA.__data: 0x240
   __DATA_DIRTY.__objc_ivar: 0x2c

   - /System/Library/Frameworks/Foundation.framework/Foundation
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 62516747-3290-3D09-8C61-DF2BA375FAB2
+  UUID: 86D40C88-C180-3902-804C-E0384DB68B63
   Functions: 98
-  Symbols:   79
-  CStrings:  228
+  Symbols:   82
+  CStrings:  55
 
Symbols:
+ _objc_claimAutoreleasedReturnValue
+ _objc_retainAutoreleaseReturnValue
+ _objc_retain_x1
+ _objc_retain_x2
+ _objc_retain_x23
+ _objc_retain_x3
- _objc_retainAutoreleasedReturnValue
- _objc_retain_x22
- _objc_retain_x25
CStrings:
- "#16@0:8"
- ".cxx_destruct"
- "@\"NSMutableArray\""
- "@\"NSString\""
- "@\"NSString\"16@0:8"
- "@\"NSXPCConnection\""
- "@\"NSXPCListenerEndpoint\""
- "@16@0:8"
- "@24@0:8:16"
- "@24@0:8@\"NSCoder\"16"
- "@24@0:8@16"
- "@24@0:8@?16"
- "@24@0:8^{_NSZone=}16"
- "@32@0:8:16@24"
- "@40@0:8:16@24@32"
- "B16@0:8"
- "B24@0:8#16"
- "B24@0:8:16"
- "B24@0:8@\"Protocol\"16"
- "B24@0:8@16"
- "ManagedOrganizationContactsAPI"
- "ManagedOrganizationContactsClassObject"
- "ManagedOrganizationContactsConnection"
- "ManagedOrganizationContactsGroupObject"
- "ManagedOrganizationContactsPersonObject"
- "ManagedOrganizationContactsQuery"
- "ManagedOrganizationContactsRequestInterface"
- "ManagedOrganizationContactsResponseInterface"
- "ManagedOrganizationContactsRosterObject"
- "NSCoding"
- "NSCopying"
- "NSObject"
- "NSSecureCoding"
- "Q"
- "Q16@0:8"
- "T#,R"
- "T@\"NSMutableArray\",&,N,V_results"
- "T@\"NSPersonNameComponents\",R,N"
- "T@\"NSString\",&,N,V_groupID"
- "T@\"NSString\",&,N,VappleID"
- "T@\"NSString\",&,N,VdisplayName"
- "T@\"NSString\",&,N,VemailAddress"
- "T@\"NSString\",&,N,VfamilyName"
- "T@\"NSString\",&,N,VgivenName"
- "T@\"NSString\",&,N,VmiddleName"
- "T@\"NSString\",&,N,VobjectID"
- "T@\"NSString\",&,N,VphoneticFamilyName"
- "T@\"NSString\",&,N,VphoneticGivenName"
- "T@\"NSString\",&,N,VphoneticMiddleName"
- "T@\"NSString\",?,R,C"
- "T@\"NSString\",C,N,V_keyword"
- "T@\"NSString\",R,C"
- "TB,R"
- "TQ,N,V_rosterSearchBehaviors"
- "TQ,N,V_rosterSearchOptions"
- "TQ,R"
- "Vv16@0:8"
- "Vv24@0:8@16"
- "Vv32@0:8Q16@\"NSError\"24"
- "Vv32@0:8Q16@24"
- "Vv40@0:8@\"NSObject<ManagedOrganizationContactsResponseInterface>\"16@\"ManagedOrganizationContactsQuery\"24@?<v@?>32"
- "Vv40@0:8@16@24@?32"
- "^{_NSZone=}16@0:8"
- "_connection"
- "_endpoint"
- "_groupID"
- "_keyword"
- "_lock"
- "_results"
- "_rosterSearchBehaviors"
- "_rosterSearchOptions"
- "addObject:"
- "addObjectsFromArray:"
- "allocWithZone:"
- "appendFormat:"
- "arrayWithObjects:count:"
- "autorelease"
- "class"
- "clientRemote_deliverObject:"
- "clientRemote_finishWithOffset:error:"
- "conformsToProtocol:"
- "containsObject:"
- "copy"
- "copyWithZone:"
- "count"
- "countByEnumeratingWithState:objects:count:"
- "debugDescription"
- "decodeIntegerForKey:"
- "decodeObjectOfClass:forKey:"
- "description"
- "encodeInteger:forKey:"
- "encodeObject:forKey:"
- "encodeWithCoder:"
- "hash"
- "init"
- "initWithCapacity:"
- "initWithCoder:"
- "initWithDomain:code:userInfo:"
- "initWithEndpoint:"
- "initWithListenerEndpoint:"
- "initWithMachServiceName:options:"
- "initWithString:"
- "isEqual:"
- "isKindOfClass:"
- "isMemberOfClass:"
- "isProxy"
- "lock"
- "membersOfGroupWithIdentifier:completion:"
- "mutableCopy"
- "nameComponents"
- "objectsMatching:completion:"
- "performSelector:"
- "performSelector:withObject:"
- "performSelector:withObject:withObject:"
- "phoneticFamilyName"
- "phoneticGivenName"
- "phoneticMiddleName"
- "phoneticRepresentation"
- "release"
- "remoteObjectProxyWithErrorHandler:"
- "remote_executeRosterQuery:executeQuery:completion:"
- "respondsToSelector:"
- "resume"
- "retain"
- "retainCount"
- "self"
- "server:"
- "setAppleID:"
- "setClasses:forSelector:argumentIndex:ofReply:"
- "setDisplayName:"
- "setEmailAddress:"
- "setExportedInterface:"
- "setFamilyName:"
- "setGivenName:"
- "setGroupID:"
- "setInterface:forSelector:argumentIndex:ofReply:"
- "setInterruptionHandler:"
- "setInvalidationHandler:"
- "setKeyword:"
- "setMiddleName:"
- "setObjectID:"
- "setPhoneticFamilyName:"
- "setPhoneticGivenName:"
- "setPhoneticMiddleName:"
- "setPhoneticRepresentation:"
- "setProtocol:"
- "setRemoteObjectInterface:"
- "setResults:"
- "setRosterSearchBehaviors:"
- "setRosterSearchOptions:"
- "setWithArray:"
- "superclass"
- "supportsSecureCoding"
- "unlock"
- "v16@0:8"
- "v24@0:8@\"NSCoder\"16"
- "v24@0:8@16"
- "v24@0:8Q16"
- "v32@0:8@16@?24"
- "zone"
- "{os_unfair_recursive_lock_s=\"ourl_lock\"{os_unfair_lock_s=\"_os_unfair_lock_opaque\"I}\"ourl_count\"I}"

```
