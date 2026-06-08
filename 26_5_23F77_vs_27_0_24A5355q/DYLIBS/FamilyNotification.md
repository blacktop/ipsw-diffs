## FamilyNotification

> `/System/Library/PrivateFrameworks/FamilyNotification.framework/FamilyNotification`

```diff

-254.575.9.0.0
-  __TEXT.__text: 0x252c
-  __TEXT.__auth_stubs: 0x270
+279.3.1.2.0
+  __TEXT.__text: 0x2254
   __TEXT.__objc_methlist: 0x55c
-  __TEXT.__cstring: 0x401
+  __TEXT.__cstring: 0x408
   __TEXT.__const: 0x28
   __TEXT.__gcc_except_tab: 0x48
   __TEXT.__oslogstring: 0x18a
   __TEXT.__unwind_info: 0xf8
-  __TEXT.__objc_classname: 0xa7
-  __TEXT.__objc_methname: 0xeea
-  __TEXT.__objc_methtype: 0x263
-  __TEXT.__objc_stubs: 0x740
-  __DATA_CONST.__got: 0x80
+  __TEXT.__objc_stubs: 0x0
+  __TEXT.__auth_stubs: 0x0
+  __TEXT.__objc_classname: 0x0
+  __TEXT.__objc_methname: 0x0
+  __TEXT.__objc_methtype: 0x0
   __DATA_CONST.__const: 0xe0
   __DATA_CONST.__objc_classlist: 0x10
   __DATA_CONST.__objc_protolist: 0x30

   __DATA_CONST.__objc_selrefs: 0x418
   __DATA_CONST.__objc_protorefs: 0x10
   __DATA_CONST.__objc_superrefs: 0x8
-  __AUTH_CONST.__auth_got: 0x148
+  __DATA_CONST.__got: 0x78
   __AUTH_CONST.__const: 0x40
   __AUTH_CONST.__cfstring: 0x320
   __AUTH_CONST.__objc_const: 0x8b8
+  __AUTH_CONST.__auth_got: 0x0
   __AUTH.__objc_data: 0x50
   __DATA.__objc_ivar: 0x74
   __DATA.__data: 0x240

   - /System/Library/PrivateFrameworks/FamilyCircle.framework/FamilyCircle
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 76BDCC19-C59B-3102-836B-82B012371087
+  UUID: E8DFC652-8BF8-3B2D-8CB8-0B3D127CE1C7
   Functions: 87
-  Symbols:   383
-  CStrings:  309
+  Symbols:   386
+  CStrings:  71
 
Symbols:
+ _objc_claimAutoreleasedReturnValue
+ _objc_release_x23
+ _objc_retainAutoreleaseReturnValue
+ _objc_retain_x1
+ _objc_retain_x23
+ _objc_retain_x3
+ _objc_retain_x8
- ___stack_chk_fail
- ___stack_chk_guard
- _objc_retain
- _objc_retainAutoreleasedReturnValue
Functions:
~ __FALogSystem : 84 -> 68
~ -[FAFamilyNotifier initWithIdentifier:machServiceName:] : 208 -> 216
~ -[FAFamilyNotifier deliverNotification:] : 208 -> 204
~ ___40-[FAFamilyNotifier deliverNotification:]_block_invoke : 220 -> 172
~ -[FAFamilyNotifier removeNotificationWithIdentifier:] : 208 -> 204
~ ___53-[FAFamilyNotifier removeNotificationWithIdentifier:]_block_invoke : 220 -> 172
~ -[FAFamilyNotifier removeAllNotifications] : 108 -> 100
~ ___42-[FAFamilyNotifier removeAllNotifications]_block_invoke : 196 -> 148
~ -[FAFamilyNotifier _pendingNotificationsWithClientIdentifier:] : 464 -> 468
~ ___62-[FAFamilyNotifier _pendingNotificationsWithClientIdentifier:]_block_invoke : 216 -> 168
~ ___62-[FAFamilyNotifier _pendingNotificationsWithClientIdentifier:]_block_invoke.2 : 112 -> 96
~ -[FAFamilyNotifier pendingNotifications] : 96 -> 88
~ -[FAFamilyNotifier agentConnection] : 744 -> 720
~ ___35-[FAFamilyNotifier agentConnection]_block_invoke_3 : 224 -> 176
~ -[FAFamilyNotifier _agentConnectionWasInterrupted] : 204 -> 156
~ -[FAFamilyNotifier _agentConnectionWasInvalidated] : 204 -> 156
~ -[FAFamilyNotifier _agentConnectionFailedToBootstrap] : 204 -> 156
~ -[FAFamilyNotifier listener:shouldAcceptNewConnection:] : 132 -> 128
~ -[FAFamilyNotifier didActivateNotification:] : 152 -> 144
~ -[FAFamilyNotifier didDismissNotification:] : 152 -> 144
~ -[FAFamilyNotifier didClearNotification:] : 152 -> 144
~ -[FAFamilyNotification init] : 128 -> 124
~ -[FAFamilyNotification initWithCoder:] : 1088 -> 1024
~ -[FAFamilyNotification encodeWithCoder:] : 476 -> 468
~ -[FAFamilyNotification cacheDictionaryRepresentation] : 848 -> 812
~ -[FAFamilyNotification initWithCacheDictionaryRepresentation:] : 1076 -> 968
~ -[FAFamilyNotification description] : 324 -> 296
CStrings:
- "#16@0:8"
- ".cxx_destruct"
- "@\"<FAFamilyNotificationDelegate>\""
- "@\"NSData\""
- "@\"NSDate\""
- "@\"NSDictionary\""
- "@\"NSLock\""
- "@\"NSNumber\""
- "@\"NSString\""
- "@\"NSString\"16@0:8"
- "@\"NSURL\""
- "@\"NSXPCConnection\""
- "@\"NSXPCListener\""
- "@16@0:8"
- "@24@0:8:16"
- "@24@0:8@\"NSCoder\"16"
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
- "FAFamilyNotification"
- "FAFamilyNotifier"
- "FAFamilyNotifierAgentProtocol"
- "FAFamilyNotifierRemoteObjectProtocol"
- "NSCoding"
- "NSObject"
- "NSSecureCoding"
- "NSXPCListenerDelegate"
- "Q16@0:8"
- "T#,R"
- "T@\"<FAFamilyNotificationDelegate>\",W,V_delegate"
- "T@\"NSData\",C,V_launchActionArguments"
- "T@\"NSDate\",C,V_expiryDate"
- "T@\"NSDate\",C,V_relevanceDate"
- "T@\"NSDictionary\",C,V_userInfo"
- "T@\"NSNumber\",C,V_familyMemberDSID"
- "T@\"NSString\",&,V_iconName"
- "T@\"NSString\",?,R,C"
- "T@\"NSString\",C,V_actionButtonLabel"
- "T@\"NSString\",C,V_clientIdentifier"
- "T@\"NSString\",C,V_delegateMachServiceName"
- "T@\"NSString\",C,V_identifier"
- "T@\"NSString\",C,V_informativeText"
- "T@\"NSString\",C,V_otherButtonLabel"
- "T@\"NSString\",C,V_title"
- "T@\"NSString\",C,V_unlockActionLabel"
- "T@\"NSString\",C,V_uuid"
- "T@\"NSString\",R,C"
- "T@\"NSString\",R,V_identifier"
- "T@\"NSString\",R,V_serviceName"
- "T@\"NSURL\",C,V_activateActionURL"
- "T@\"NSURL\",C,V_dismissActionlURL"
- "T@\"NSURL\",C,V_launchActionURL"
- "TB,R"
- "TB,V_hasActionButton"
- "TB,V_hasHeader"
- "TB,V_shouldPersistWhenActivated"
- "TB,V_shouldPersistWhenDismissed"
- "TQ,R"
- "TQ,V_displayStyle"
- "URLWithString:"
- "Vv16@0:8"
- "^{_NSZone=}16@0:8"
- "_agentConnectionFailedToBootstrap"
- "_agentConnectionWasInterrupted"
- "_agentConnectionWasInvalidated"
- "_conn"
- "_connLock"
- "_delegate"
- "_listener"
- "_pendingNotificationsForAllClients"
- "_pendingNotificationsWithClientIdentifier:"
- "_serviceName"
- "absoluteString"
- "actionButtonLabel"
- "activateActionURL"
- "agentConnection"
- "autorelease"
- "boolValue"
- "cacheDictionaryRepresentation"
- "class"
- "clientIdentifier"
- "conformsToProtocol:"
- "copy"
- "date"
- "debugDescription"
- "decodeBoolForKey:"
- "decodeIntegerForKey:"
- "decodeObjectOfClass:forKey:"
- "decodeObjectOfClasses:forKey:"
- "delegate"
- "delegateMachServiceName"
- "deliverNotification:"
- "deliverNotificaton:"
- "description"
- "dictionary"
- "didActivateFamilyNotification:"
- "didActivateNotification:"
- "didClearFamilyNotification:"
- "didClearNotification:"
- "didDismissFamilyNotification:"
- "didDismissNotification:"
- "dismissActionlURL"
- "displayStyle"
- "encodeBool:forKey:"
- "encodeInteger:forKey:"
- "encodeObject:forKey:"
- "encodeWithCoder:"
- "expiryDate"
- "familyMemberDSID"
- "hasActionButton"
- "hasHeader"
- "hash"
- "iconName"
- "identifier"
- "informativeText"
- "init"
- "initWithCacheDictionaryRepresentation:"
- "initWithCoder:"
- "initWithIdentifier:machServiceName:"
- "initWithMachServiceName:"
- "initWithMachServiceName:options:"
- "integerValue"
- "interfaceWithProtocol:"
- "isEqual:"
- "isKindOfClass:"
- "isMemberOfClass:"
- "isProxy"
- "launchActionArguments"
- "launchActionURL"
- "length"
- "listener:shouldAcceptNewConnection:"
- "lock"
- "numberWithBool:"
- "numberWithInteger:"
- "objectForKeyedSubscript:"
- "otherButtonLabel"
- "pendingNotifications"
- "pendingNotificationsWithIdentifier:replyBlock:"
- "performSelector:"
- "performSelector:withObject:"
- "performSelector:withObject:withObject:"
- "release"
- "relevanceDate"
- "remoteObjectProxyWithErrorHandler:"
- "removeAllNotifications"
- "removeNotificationWithIdentifier:"
- "respondsToSelector:"
- "resume"
- "retain"
- "retainCount"
- "self"
- "serviceName"
- "setActionButtonLabel:"
- "setActivateActionURL:"
- "setClasses:forSelector:argumentIndex:ofReply:"
- "setClientIdentifier:"
- "setDelegate:"
- "setDelegateMachServiceName:"
- "setDismissActionlURL:"
- "setDisplayStyle:"
- "setExpiryDate:"
- "setExportedInterface:"
- "setExportedObject:"
- "setFamilyMemberDSID:"
- "setHasActionButton:"
- "setHasHeader:"
- "setIconName:"
- "setIdentifier:"
- "setInformativeText:"
- "setInterruptionHandler:"
- "setInvalidationHandler:"
- "setLaunchActionArguments:"
- "setLaunchActionURL:"
- "setObject:forKeyedSubscript:"
- "setOtherButtonLabel:"
- "setRelevanceDate:"
- "setRemoteObjectInterface:"
- "setShouldPersistWhenActivated:"
- "setShouldPersistWhenDismissed:"
- "setTitle:"
- "setUnlockActionLabel:"
- "setUserInfo:"
- "setUuid:"
- "setWithObjects:"
- "shouldPersistWhenActivated"
- "shouldPersistWhenDismissed"
- "stringByReplacingCharactersInRange:withString:"
- "stringWithFormat:"
- "superclass"
- "supportsSecureCoding"
- "title"
- "unlock"
- "unlockActionLabel"
- "userInfo"
- "uuid"
- "v16@0:8"
- "v20@0:8B16"
- "v24@0:8@\"FAFamilyNotification\"16"
- "v24@0:8@\"NSCoder\"16"
- "v24@0:8@\"NSString\"16"
- "v24@0:8@16"
- "v24@0:8Q16"
- "v32@0:8@\"NSString\"16@?<v@?@\"NSArray\"@\"NSError\">24"
- "v32@0:8@16@?24"
- "zone"

```
