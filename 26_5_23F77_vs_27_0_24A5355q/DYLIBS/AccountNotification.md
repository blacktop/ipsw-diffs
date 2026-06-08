## AccountNotification

> `/System/Library/PrivateFrameworks/AccountNotification.framework/AccountNotification`

```diff

 14.0.0.0.0
-  __TEXT.__text: 0x3a40
-  __TEXT.__auth_stubs: 0x260
+  __TEXT.__text: 0x3488
   __TEXT.__objc_methlist: 0x66c
   __TEXT.__const: 0x68
-  __TEXT.__cstring: 0x58b
-  __TEXT.__gcc_except_tab: 0x144
+  __TEXT.__cstring: 0x598
+  __TEXT.__gcc_except_tab: 0x12c
   __TEXT.__oslogstring: 0x446
-  __TEXT.__unwind_info: 0x180
-  __TEXT.__objc_classname: 0x154
-  __TEXT.__objc_methname: 0xf9b
-  __TEXT.__objc_methtype: 0x2a8
-  __TEXT.__objc_stubs: 0xb20
-  __DATA_CONST.__got: 0xa0
+  __TEXT.__unwind_info: 0x178
+  __TEXT.__objc_stubs: 0x0
+  __TEXT.__auth_stubs: 0x0
+  __TEXT.__objc_classname: 0x0
+  __TEXT.__objc_methname: 0x0
+  __TEXT.__objc_methtype: 0x0
   __DATA_CONST.__const: 0xc8
   __DATA_CONST.__objc_classlist: 0x40
   __DATA_CONST.__objc_protolist: 0x38

   __DATA_CONST.__objc_selrefs: 0x470
   __DATA_CONST.__objc_protorefs: 0x10
   __DATA_CONST.__objc_superrefs: 0x20
-  __AUTH_CONST.__auth_got: 0x140
+  __DATA_CONST.__got: 0x98
   __AUTH_CONST.__const: 0x80
   __AUTH_CONST.__cfstring: 0x2c0
   __AUTH_CONST.__objc_const: 0x1750
+  __AUTH_CONST.__auth_got: 0x0
   __AUTH.__objc_data: 0x230
   __DATA.__objc_ivar: 0x60
   __DATA.__data: 0x2a0

   - /System/Library/PrivateFrameworks/AppSupport.framework/AppSupport
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 8A09E9AA-E2D3-3985-AABE-4E75ABBD9F19
-  Functions: 132
-  Symbols:   584
-  CStrings:  346
+  UUID: A510DA9E-342B-3312-B69D-64FC2BEDC69D
+  Functions: 129
+  Symbols:   577
+  CStrings:  91
 
Symbols:
+ _objc_claimAutoreleasedReturnValue
+ _objc_retainAutoreleaseReturnValue
+ _objc_retain_x1
+ _objc_retain_x2
+ _objc_retain_x21
+ _objc_retain_x3
- _OUTLINED_FUNCTION_8
- _OUTLINED_FUNCTION_9
- ___stack_chk_fail
- ___stack_chk_guard
- _objc_release_x23
- _objc_retain
- _objc_retain_x20
CStrings:
- "#16@0:8"
- ".cxx_destruct"
- "@\"<ANAccountNotifierDelegate>\""
- "@\"ANNotificationAction\""
- "@\"NSDate\""
- "@\"NSDictionary\""
- "@\"NSDictionary\"16@0:8"
- "@\"NSString\""
- "@\"NSString\"16@0:8"
- "@\"NSURL\""
- "@\"NSXPCConnection\""
- "@\"NSXPCListener\""
- "@16@0:8"
- "@24@0:8:16"
- "@24@0:8@\"NSCoder\"16"
- "@24@0:8@\"NSDictionary\"16"
- "@24@0:8@16"
- "@32@0:8:16@24"
- "@32@0:8@16@24"
- "@40@0:8:16@24@32"
- "ANAccountNotification"
- "ANAccountNotifier"
- "ANCachedDictionaryRepresentationProtocol"
- "ANClientCallbackInterface"
- "ANClientCallbackProtocol"
- "ANDaemonInterface"
- "ANDaemonProtocol"
- "ANManagedAccountNotification"
- "ANManagedNotificationAction"
- "ANNotificationAction"
- "ANSectionSubtypeDescriptor"
- "B"
- "B16@0:8"
- "B24@0:8#16"
- "B24@0:8:16"
- "B24@0:8@\"Protocol\"16"
- "B24@0:8@16"
- "B32@0:8@\"NSXPCListener\"16@\"NSXPCConnection\"24"
- "B32@0:8@16@24"
- "NSCoding"
- "NSObject"
- "NSSecureCoding"
- "NSXPCListenerDelegate"
- "Q16@0:8"
- "T#,R"
- "T@\"<ANAccountNotifierDelegate>\",W,N,V_delegate"
- "T@\"ANManagedAccountNotification\",&,D,N"
- "T@\"ANManagedNotificationAction\",&,D,N"
- "T@\"ANNotificationAction\",&,N,V_activateAction"
- "T@\"ANNotificationAction\",&,N,V_dismissAction"
- "T@\"NSDate\",&,D,N"
- "T@\"NSDate\",C,N,V_date"
- "T@\"NSDictionary\",C,N,V_options"
- "T@\"NSDictionary\",C,N,V_userInfo"
- "T@\"NSNumber\",&,D,N"
- "T@\"NSString\",&,D,N"
- "T@\"NSString\",?,R,C"
- "T@\"NSString\",C,N,V_activateButtonTitle"
- "T@\"NSString\",C,N,V_callbackMachService"
- "T@\"NSString\",C,N,V_eventIdentifier"
- "T@\"NSString\",C,N,V_fullUnlockActionLabel"
- "T@\"NSString\",C,N,V_message"
- "T@\"NSString\",C,N,V_title"
- "T@\"NSString\",R,C"
- "T@\"NSString\",R,N,V_accountTypeID"
- "T@\"NSString\",R,N,V_identifier"
- "T@\"NSURL\",C,N,V_url"
- "T@,&,D,N"
- "TB,N,V_allowsAddingToLockScreenWhenUnlocked"
- "TB,N,V_isInternalURL"
- "TB,R"
- "TQ,R"
- "Tq,N,V_destinations"
- "Tq,N,V_sectionSubtype"
- "Tq,N,V_subtype"
- "URLWithString:"
- "UUID"
- "UUIDString"
- "Vv16@0:8"
- "XPCInterface"
- "^{_NSZone=}16@0:8"
- "_activateButtonTitle"
- "_buildXPCInterface"
- "_bulletinResponseListener"
- "_createDaemonConnection"
- "_daemonConnection"
- "_daemonConnectionWasInterrupted"
- "_daemonConnectionWasInvalidated"
- "_delegate"
- "_disconnectFromDaemon"
- "_startNotificationCallbackListenerWithMachServiceName:"
- "_stopNotificationCallbackListener"
- "absoluteString"
- "accountNotifier:didActivateNotification:"
- "accountNotifier:didClearNotification:"
- "accountNotifier:didDismissNotification:"
- "accountTypeID"
- "actionForLaunchingApp:"
- "actionForLaunchingApp:withOptions:"
- "actionForOpeningWebURL:"
- "activateAction"
- "activateButtonTitle"
- "addNotification:"
- "addNotification:withCompletion:"
- "allowsAddingToLockScreenWhenUnlocked"
- "autorelease"
- "boolValue"
- "callbackMachService"
- "callbackMachServiceName"
- "class"
- "clearAction"
- "conformsToProtocol:"
- "copy"
- "date"
- "dealloc"
- "debugDescription"
- "decodeBoolForKey:"
- "decodeIntegerForKey:"
- "decodeObjectOfClass:forKey:"
- "decodeObjectOfClasses:forKey:"
- "defaultWorkspace"
- "delegate"
- "description"
- "destinations"
- "dictionaryRepresentation"
- "dismissAction"
- "dismissButtonTitle"
- "encodeBool:forKey:"
- "encodeInteger:forKey:"
- "encodeObject:forKey:"
- "encodeWithCoder:"
- "eventID"
- "eventIdentifier"
- "fullUnlockActionLabel"
- "hash"
- "identifier"
- "init"
- "initForAccountWithType:"
- "initWithCallbackMachService:"
- "initWithCoder:"
- "initWithDictionaryRepresentation:"
- "initWithMachServiceName:"
- "initWithMachServiceName:options:"
- "initWithManagedObject:"
- "integerValue"
- "interfaceWithProtocol:"
- "invalidate"
- "isEqual:"
- "isEqualToString:"
- "isInternal"
- "isInternalURL"
- "isKindOfClass:"
- "isMemberOfClass:"
- "isProxy"
- "listener:shouldAcceptNewConnection:"
- "message"
- "name"
- "notificationToActivate"
- "notificationToClear"
- "notificationToDismiss"
- "notificationWasActivated:"
- "notificationWasCleared:"
- "notificationWasDismissed:"
- "numberWithBool:"
- "numberWithInteger:"
- "objectForKeyedSubscript:"
- "openSensitiveURL:withOptions:"
- "openURL:"
- "options"
- "perform"
- "performSelector:"
- "performSelector:withObject:"
- "performSelector:withObject:withObject:"
- "q"
- "q16@0:8"
- "release"
- "removeNotificationWithID:completion:"
- "removeNotificationWithIdentifier:"
- "removeNotificationsWithEventID:completion:"
- "removeNotificationsWithEventIdentifier:"
- "respondsToSelector:"
- "resume"
- "retain"
- "retainCount"
- "sectionSubtype"
- "self"
- "setAccountTypeID:"
- "setActivateAction:"
- "setActivateButtonTitle:"
- "setAllowsAddingToLockScreenWhenUnlocked:"
- "setCallbackMachService:"
- "setCallbackMachServiceName:"
- "setDate:"
- "setDelegate:"
- "setDestinations:"
- "setDismissAction:"
- "setEventID:"
- "setEventIdentifier:"
- "setExportedInterface:"
- "setExportedObject:"
- "setFullUnlockActionLabel:"
- "setIdentifier:"
- "setInterruptionHandler:"
- "setInvalidationHandler:"
- "setIsInternal:"
- "setIsInternalURL:"
- "setMessage:"
- "setObject:forKeyedSubscript:"
- "setOptions:"
- "setRemoteObjectInterface:"
- "setSectionSubtype:"
- "setSubtype:"
- "setTitle:"
- "setUrl:"
- "setUserInfo:"
- "setWithObjects:"
- "stringWithFormat:"
- "subtype"
- "superclass"
- "supportsSecureCoding"
- "synchronousRemoteObjectProxyWithErrorHandler:"
- "takeValuesFromAccountNotification:"
- "takeValuesFromNotificationAction:"
- "title"
- "url"
- "userInfo"
- "v16@0:8"
- "v20@0:8B16"
- "v24@0:8@\"ANAccountNotification\"16"
- "v24@0:8@\"NSCoder\"16"
- "v24@0:8@16"
- "v24@0:8q16"
- "v32@0:8@\"ANAccountNotification\"16@?<v@?B@\"NSError\">24"
- "v32@0:8@\"NSString\"16@?<v@?B@\"NSError\">24"
- "v32@0:8@16@?24"
- "valueForEntitlement:"
- "zone"

```
