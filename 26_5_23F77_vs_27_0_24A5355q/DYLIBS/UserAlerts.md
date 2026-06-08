## UserAlerts

> `/System/Library/PrivateFrameworks/UserAlerts.framework/UserAlerts`

```diff

 14.7.0.0.0
-  __TEXT.__text: 0x67e8
-  __TEXT.__auth_stubs: 0x410
+  __TEXT.__text: 0x5ef8
   __TEXT.__objc_methlist: 0x958
   __TEXT.__const: 0x68
-  __TEXT.__cstring: 0x453
-  __TEXT.__gcc_except_tab: 0x258
+  __TEXT.__cstring: 0x469
+  __TEXT.__gcc_except_tab: 0x22c
   __TEXT.__oslogstring: 0x3f0
-  __TEXT.__unwind_info: 0x2d0
-  __TEXT.__objc_classname: 0x217
-  __TEXT.__objc_methname: 0x165f
-  __TEXT.__objc_methtype: 0x59f
-  __TEXT.__objc_stubs: 0x1200
-  __DATA_CONST.__got: 0x100
+  __TEXT.__unwind_info: 0x2b0
+  __TEXT.__objc_stubs: 0x0
+  __TEXT.__auth_stubs: 0x0
+  __TEXT.__objc_classname: 0x0
+  __TEXT.__objc_methname: 0x0
+  __TEXT.__objc_methtype: 0x0
   __DATA_CONST.__const: 0x338
   __DATA_CONST.__objc_classlist: 0x58
   __DATA_CONST.__objc_protolist: 0x58

   __DATA_CONST.__objc_selrefs: 0x568
   __DATA_CONST.__objc_protorefs: 0x10
   __DATA_CONST.__objc_superrefs: 0x50
-  __AUTH_CONST.__auth_got: 0x218
+  __DATA_CONST.__got: 0x100
   __AUTH_CONST.__const: 0xa0
   __AUTH_CONST.__cfstring: 0x3a0
   __AUTH_CONST.__objc_const: 0x14d8
   __AUTH_CONST.__objc_intobj: 0x18
+  __AUTH_CONST.__auth_got: 0x0
   __AUTH.__objc_data: 0x2d0
   __DATA.__objc_ivar: 0xac
   __DATA.__data: 0x420

   - /System/Library/PrivateFrameworks/BoardServices.framework/BoardServices
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: D62D8415-2152-30F5-BFF6-7CDE5241761A
-  Functions: 205
-  Symbols:   888
-  CStrings:  449
+  UUID: F58EB191-D546-3FE6-9132-42BC76288686
+  Functions: 200
+  Symbols:   882
+  CStrings:  100
 
Symbols:
+ ___61-[URTAlertService listener:didReceiveConnection:withContext:]_block_invoke.89
+ ___91-[URTAlertService _connectionQueue_presentAlert:preferringPresentationStyle:forConnection:]_block_invoke.101
+ ___91-[URTAlertService _connectionQueue_presentAlert:preferringPresentationStyle:forConnection:]_block_invoke.94
+ ___91-[URTAlertService _connectionQueue_presentAlert:preferringPresentationStyle:forConnection:]_block_invoke.97
+ ___91-[URTAlertService _connectionQueue_presentAlert:preferringPresentationStyle:forConnection:]_block_invoke_2.100
+ ___block_literal_global.103
+ ___block_literal_global.99
+ _objc_claimAutoreleasedReturnValue
+ _objc_retainAutoreleaseReturnValue
+ _objc_retain_x1
+ _objc_retain_x22
+ _objc_retain_x23
+ _objc_retain_x8
- _OUTLINED_FUNCTION_2
- _OUTLINED_FUNCTION_3
- ___61-[URTAlertService listener:didReceiveConnection:withContext:]_block_invoke.90
- ___91-[URTAlertService _connectionQueue_presentAlert:preferringPresentationStyle:forConnection:]_block_invoke.102
- ___91-[URTAlertService _connectionQueue_presentAlert:preferringPresentationStyle:forConnection:]_block_invoke.95
- ___91-[URTAlertService _connectionQueue_presentAlert:preferringPresentationStyle:forConnection:]_block_invoke.98
- ___91-[URTAlertService _connectionQueue_presentAlert:preferringPresentationStyle:forConnection:]_block_invoke_2.101
- ___block_literal_global.100
- ___block_literal_global.104
- _objc_retainAutoreleasedReturnValue
- _objc_retain_x24
CStrings:
- "#16@0:8"
- ".cxx_destruct"
- "@\"<BSInvalidatable>\""
- "@\"<URTAlertPresentable>\""
- "@\"<URTAlertServiceDelegate>\""
- "@\"<URTDestinationPresentationDelegate>\""
- "@\"<URTDestinationPresentationDelegate>\"16@0:8"
- "@\"BSServiceConnection\""
- "@\"BSServiceConnectionListener\""
- "@\"NSArray\""
- "@\"NSDictionary\""
- "@\"NSMutableArray\""
- "@\"NSMutableDictionary\""
- "@\"NSObject<OS_dispatch_queue>\""
- "@\"NSString\""
- "@\"NSString\"16@0:8"
- "@\"URTAlert\""
- "@\"URTAlert\"16@0:8"
- "@\"URTAlertAction\""
- "@\"URTAlertService\""
- "@\"URTAlertServiceDelegateProxy\""
- "@\"URTUserNotificationPresentation\""
- "@16@0:8"
- "@24@0:8:16"
- "@24@0:8@\"NSCoder\"16"
- "@24@0:8@16"
- "@32@0:8:16@24"
- "@32@0:8@16@24"
- "@32@0:8@16@?24"
- "@32@0:8@16Q24"
- "@40@0:8:16@24@32"
- "@40@0:8@\"URTAlert\"16q24q32"
- "@40@0:8@16q24q32"
- "@?"
- "@?16@0:8"
- "B16@0:8"
- "B24@0:8#16"
- "B24@0:8:16"
- "B24@0:8@\"Protocol\"16"
- "B24@0:8@16"
- "BSInvalidatable"
- "BSServiceConnectionListenerDelegate"
- "CFUserNotifications"
- "NSCoding"
- "NSObject"
- "NSSecureCoding"
- "Q"
- "Q16@0:8"
- "T#,R"
- "T@\"<BSInvalidatable>\",&,N,V_domainActivationToken"
- "T@\"<URTAlertPresentable>\",&,N,V_header"
- "T@\"<URTAlertServiceDelegate>\",W,N,V_delegate"
- "T@\"<URTDestinationPresentationDelegate>\",W,N"
- "T@\"<URTDestinationPresentationDelegate>\",W,N,V_delegate"
- "T@\"BSServiceConnection\",R,N,V_connection"
- "T@\"BSServiceConnectionListener\",R,N,V_listener"
- "T@\"BSServiceInterface\",R,C,N"
- "T@\"BSServiceQuality\",R,C,N"
- "T@\"NSArray\",C,N,V_allowedApplicationBundleIDs"
- "T@\"NSDictionary\",R,C,N,V_contents"
- "T@\"NSMutableArray\",R,N,V_connections"
- "T@\"NSMutableDictionary\",R,N,V_presentationsForDestinations"
- "T@\"NSObject<OS_dispatch_queue>\",R,N,V_connectionQueue"
- "T@\"NSObject<OS_dispatch_queue>\",R,N,V_presentationsQueue"
- "T@\"NSObject<OS_dispatch_queue>\",R,N,V_remoteTargetQueue"
- "T@\"NSString\",?,R,C"
- "T@\"NSString\",R,C"
- "T@\"NSString\",R,C,N"
- "T@\"NSString\",R,C,N,V_domain"
- "T@\"NSString\",R,C,N,V_identifier"
- "T@\"NSString\",R,C,N,V_message"
- "T@\"NSString\",R,C,N,V_title"
- "T@\"NSString\",R,N,V_symbolName"
- "T@\"URTAlert\",&,N,V_alert"
- "T@\"URTAlert\",R,N"
- "T@\"URTAlert\",R,N,V_alert"
- "T@\"URTAlertAction\",&,N,V_cancelAction"
- "T@\"URTAlertAction\",&,N,V_defaultAction"
- "T@\"URTAlertAction\",&,N,V_otherAction"
- "T@\"URTAlertService\",R,W,N,V_service"
- "T@\"URTAlertServiceDelegateProxy\",R,N,V_delegateProxy"
- "T@\"URTUserNotificationPresentation\",R,W,N,V_userNotificationPresentation"
- "T@?,R,C,N,V_handler"
- "TB,R"
- "TQ,R"
- "TQ,R,N,V_creationFlags"
- "T^?,N,V_compatibilityCallback"
- "Ti,R,N,V_compatibilityResponse"
- "Ti,R,N,V_compatibilityResponseButtonFlag"
- "Ti,R,N,V_error"
- "Tq,R,N"
- "Tq,R,N,V_destination"
- "Tq,R,N,V_preferredPresentationStyle"
- "URTAlert"
- "URTAlertAction"
- "URTAlertClientToServerInterface"
- "URTAlertConnection"
- "URTAlertPresentable"
- "URTAlertPresenter"
- "URTAlertServerToClientInterface"
- "URTAlertService"
- "URTAlertServiceDelegateProxy"
- "URTAlertServiceSpecification"
- "URTAlertSymbol"
- "URTDefaultDestinationPresentation"
- "URTDestinationPresentationDelegate"
- "URTDestinationPresenting"
- "URTPresenting"
- "URTServiceDestinationPresentation"
- "URTUserNotificationPresentation"
- "UUID"
- "UUIDString"
- "Vv16@0:8"
- "Vv24@0:8@\"URTAlert\"16"
- "Vv24@0:8@16"
- "Vv32@0:8@\"URTAlert\"16@\"NSNumber\"24"
- "Vv32@0:8@16@24"
- "^?"
- "^?16@0:8"
- "^{_NSZone=}16@0:8"
- "^{__CFRunLoopSource=}"
- "^{__CFRunLoopSource=}32@0:8q16@?24"
- "^{__CFUserNotification=}"
- "_addDefaultDestinationAlertFromUserNotificationContents:flags:"
- "_addFromUserNotificationContents:toServiceDestination:"
- "_alert"
- "_allowedApplicationBundleIDs"
- "_cancelAction"
- "_compatibilityCallback"
- "_compatibilityResponse"
- "_compatibilityResponseButtonFlag"
- "_connection"
- "_connectionQueue"
- "_connectionQueue_addConnection:"
- "_connectionQueue_alertConnectionForConnection:"
- "_connectionQueue_dismissAlert:forConnection:"
- "_connectionQueue_presentAlert:preferringPresentationStyle:forConnection:"
- "_connectionQueue_removeConnection:"
- "_connections"
- "_contents"
- "_creationFlags"
- "_defaultAction"
- "_delegate"
- "_delegateProxy"
- "_destination"
- "_domain"
- "_domainActivationToken"
- "_error"
- "_handleConnectionActivated"
- "_handleConnectionInterrupted"
- "_handleUserNotificationResponse:"
- "_handler"
- "_header"
- "_identifier"
- "_invokeCallbackForResponseFlags:"
- "_invokeDelegateForResponseFlags:"
- "_listener"
- "_message"
- "_otherAction"
- "_performClientActionForAlert:clientAction:"
- "_preferredPresentationStyle"
- "_presentationQueue_dismiss"
- "_presentationQueue_invalidate"
- "_presentationQueue_invokeAction:forPresentation:"
- "_presentationQueue_removePresentation:forDestination:"
- "_presentationsForDestinations"
- "_presentationsQueue"
- "_remoteTargetQueue"
- "_runLoopSource"
- "_service"
- "_symbolName"
- "_title"
- "_userNotification"
- "_userNotificationPresentation"
- "actionWithTitle:handler:"
- "activate"
- "activateManualDomain:"
- "addAlert:forDestination:"
- "addAlert:forDestination:preferringStyle:"
- "addObject:"
- "alert"
- "alertService:wantsDismissalForAlert:"
- "alertService:wantsPresentationForAlert:preferredPresentationStyle:"
- "alertSymbolWithSymbolName:"
- "alertWithTitle:message:"
- "allValues"
- "allowedApplicationBundleIDs"
- "autorelease"
- "boolValue"
- "bs_firstObjectPassingTest:"
- "cancelAction"
- "class"
- "compatibilityCallback"
- "compatibilityResponse"
- "compatibilityResponseButtonFlag"
- "configureConnection:"
- "conformsToProtocol:"
- "connection"
- "connectionQueue"
- "connectionWithEndpoint:"
- "connections"
- "containsObject:"
- "contents"
- "copy"
- "count"
- "countByEnumeratingWithState:objects:count:"
- "createRunLoopSourceOrdered:handler:"
- "creationFlags"
- "currentContext"
- "debugDescription"
- "decodeObjectOfClass:forKey:"
- "decodeObjectOfClasses:forKey:"
- "defaultAction"
- "delegate"
- "delegateProxy"
- "description"
- "destination"
- "dictionary"
- "dismiss"
- "dismissAlert:"
- "domain"
- "domainActivationToken"
- "encodeObject:forKey:"
- "encodeWithCoder:"
- "endpointForMachName:service:instance:"
- "entitlementName"
- "error"
- "handleCancelAction"
- "handleCancelActionForAlertPresentation:"
- "handleDefaultAction"
- "handleDefaultActionForAlertPresentation:"
- "handleOtherAction"
- "handleOtherActionForAlertPresentation:"
- "handler"
- "hash"
- "header"
- "i"
- "i16@0:8"
- "identifier"
- "init"
- "initWithAlert:forDestination:preferredPresentationStyle:"
- "initWithCapacity:"
- "initWithCoder:"
- "initWithConnection:"
- "initWithContents:flags:"
- "initWithDomain:"
- "initWithKeyOptions:valueOptions:capacity:"
- "initWithService:"
- "initWithSymbolName:"
- "initWithTitle:handler:"
- "initWithTitle:message:"
- "instance"
- "interface"
- "interfaceWithIdentifier:"
- "invalidate"
- "invokeHandlerForUserNotification:responseFlags:"
- "isEqual:"
- "isKindOfClass:"
- "isMemberOfClass:"
- "isProxy"
- "listener"
- "listener:didReceiveConnection:withContext:"
- "listenerWithConfigurator:"
- "message"
- "numberWithInteger:"
- "objectForKey:"
- "objectForKeyedSubscript:"
- "otherAction"
- "performSelector:"
- "performSelector:withObject:"
- "performSelector:withObject:withObject:"
- "preferredPresentationStyle"
- "present"
- "presentAlert:preferringPresentationStyle:"
- "presentationsForDestinations"
- "presentationsQueue"
- "protocolForProtocol:"
- "q16@0:8"
- "registerUserNotification:handler:"
- "release"
- "remoteProcess"
- "remoteTarget"
- "remoteTargetQueue"
- "removeAllObjects"
- "removeObject:"
- "removeObjectForKey:"
- "respondsToSelector:"
- "retain"
- "retainCount"
- "self"
- "serial"
- "service"
- "serviceQuality"
- "setActivationHandler:"
- "setAlert:"
- "setAllowedApplicationBundleIDs:"
- "setCancelAction:"
- "setClient:"
- "setClientMessagingExpectation:"
- "setCompatibilityCallback:"
- "setDefaultAction:"
- "setDelegate:"
- "setDomain:"
- "setDomainActivationToken:"
- "setHeader:"
- "setInterface:"
- "setInterfaceTarget:"
- "setInterruptionHandler:"
- "setInvalidationHandler:"
- "setObject:forKey:"
- "setObject:forKeyedSubscript:"
- "setOtherAction:"
- "setServer:"
- "setService:"
- "setServiceQuality:"
- "setTargetQueue:"
- "setWithObject:"
- "setWithObjects:"
- "stringWithFormat:"
- "superclass"
- "supportsSecureCoding"
- "symbolName"
- "title"
- "unregisterHandlerForUserNotification:"
- "unsignedIntegerValue"
- "userInteractive"
- "userNotificationPresentation"
- "userNotificationRepresentation"
- "v16@0:8"
- "v24@0:8@\"<URTDestinationPresentationDelegate>\"16"
- "v24@0:8@\"<URTDestinationPresenting>\"16"
- "v24@0:8@\"NSCoder\"16"
- "v24@0:8@16"
- "v24@0:8Q16"
- "v24@0:8^?16"
- "v24@0:8^{__CFUserNotification=}16"
- "v32@0:8@16@24"
- "v32@0:8@16@?24"
- "v32@0:8@16Q24"
- "v32@0:8@16q24"
- "v32@0:8^{__CFUserNotification=}16@?24"
- "v32@0:8^{__CFUserNotification=}16Q24"
- "v40@0:8@\"BSServiceConnectionListener\"16@\"BSServiceConnection<BSServiceConnectionHost>\"24@\"<BSXPCDecoding>\"32"
- "v40@0:8@16@24@32"
- "v40@0:8@16q24@32"
- "v40@0:8@16q24q32"
- "valueForEntitlement:"
- "zone"

```
