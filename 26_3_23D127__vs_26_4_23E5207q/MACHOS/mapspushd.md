## mapspushd

> `/System/Library/PrivateFrameworks/MapsSupport.framework/mapspushd`

```diff

-2911.33.11.13.11
-  __TEXT.__text: 0x205e8
-  __TEXT.__auth_stubs: 0x8f0
-  __TEXT.__objc_stubs: 0x58c0
-  __TEXT.__objc_methlist: 0x233c
-  __TEXT.__const: 0x108
-  __TEXT.__gcc_except_tab: 0x458
-  __TEXT.__objc_methname: 0x716d
-  __TEXT.__cstring: 0x2630
-  __TEXT.__oslogstring: 0x198f
-  __TEXT.__objc_classname: 0x63e
-  __TEXT.__objc_methtype: 0x1d78
+2921.34.7.17.49
+  __TEXT.__text: 0x1ffe0
+  __TEXT.__auth_stubs: 0x890
+  __TEXT.__objc_stubs: 0x5400
+  __TEXT.__objc_methlist: 0x1f54
+  __TEXT.__const: 0x110
+  __TEXT.__gcc_except_tab: 0x428
+  __TEXT.__objc_methname: 0x6bb0
+  __TEXT.__cstring: 0x22d5
+  __TEXT.__oslogstring: 0x19ce
+  __TEXT.__objc_classname: 0x566
+  __TEXT.__objc_methtype: 0x1cfd
   __TEXT.__ustring: 0x262
-  __TEXT.__unwind_info: 0x7b8
-  __DATA_CONST.__auth_got: 0x488
-  __DATA_CONST.__got: 0x428
+  __TEXT.__unwind_info: 0x790
+  __DATA_CONST.__auth_got: 0x458
+  __DATA_CONST.__got: 0x410
   __DATA_CONST.__const: 0x10c8
-  __DATA_CONST.__cfstring: 0x2580
-  __DATA_CONST.__objc_classlist: 0x108
+  __DATA_CONST.__cfstring: 0x22c0
+  __DATA_CONST.__objc_classlist: 0xd8
   __DATA_CONST.__objc_catlist: 0x48
-  __DATA_CONST.__objc_protolist: 0xe8
+  __DATA_CONST.__objc_protolist: 0xc8
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_protorefs: 0x48
-  __DATA_CONST.__objc_superrefs: 0xe0
+  __DATA_CONST.__objc_superrefs: 0xb0
   __DATA_CONST.__objc_arraydata: 0xa8
   __DATA_CONST.__objc_arrayobj: 0xf0
   __DATA_CONST.__objc_intobj: 0x918
   __DATA_CONST.__objc_doubleobj: 0x370
   __DATA_CONST.__objc_floatobj: 0x20
-  __DATA.__objc_const: 0x37a0
-  __DATA.__objc_selrefs: 0x1c70
-  __DATA.__objc_ivar: 0x1e4
-  __DATA.__objc_data: 0xa50
-  __DATA.__data: 0xba8
+  __DATA.__objc_const: 0x2f58
+  __DATA.__objc_selrefs: 0x1b28
+  __DATA.__objc_ivar: 0x198
+  __DATA.__objc_data: 0x870
+  __DATA.__data: 0xa28
   __DATA.__bss: 0xd0
   - /System/Library/Frameworks/Contacts.framework/Contacts
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation

   - /System/Library/PrivateFrameworks/IDS.framework/IDS
   - /System/Library/PrivateFrameworks/MapsSupport.framework/MapsSupport
   - /System/Library/PrivateFrameworks/MapsSync.framework/MapsSync
+  - /System/Library/PrivateFrameworks/Navigation.framework/Navigation
   - /System/Library/PrivateFrameworks/ProtocolBuffer.framework/ProtocolBuffer
   - /System/Library/PrivateFrameworks/UserManagement.framework/UserManagement
   - /usr/lib/libMobileGestalt.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 10FB628A-0024-3FDF-BAF3-16FB16E27696
-  Functions: 693
-  Symbols:   291
-  CStrings:  2169
+  UUID: 5C97DC16-128E-3083-91E6-8BF3D003EE0B
+  Functions: 623
+  Symbols:   284
+  CStrings:  2036
 
Symbols:
+ _OBJC_CLASS_$_MNIPCMessage
+ _OBJC_METACLASS_$_MNIPCMessage
- _NSKeyedArchiveRootObjectKey
- _OBJC_CLASS_$_NSKeyedUnarchiver
- ___NSDictionary0__struct
- __geo_NSErrorDictionaryRepresentationCopy
- __geo_NSErrorFromDictionaryRepresentationCopy
- _objc_claimAutoreleasedReturnValue
- _objc_retainAutoreleaseReturnValue
- _objc_retain_x4
- _objc_retain_x5
CStrings:
+ "-[MapsConnectionBrokerServer allListenerEndpointsForReply:]"
+ "-[MapsConnectionBrokerServer listenerEndpointForIdentifer:reply:]"
+ "MNMapsXPCClientInterface"
+ "MapsConnectionBrokerServer %s"
+ "MapsConnectionBrokerServer %s %@"
+ "allListenerEndpointsForReply:"
+ "v24@0:8@?<v@?@\"NSDictionary\">16"
- "%@             shieldID : {%@}             shieldStringID : {%@}             shieldText : {%@}"
- "%@             type : {%@}             title : {%@}             subtitle : {%@}             identifier : {%@}             incident : {%@}"
- "@\"GEORouteIncident\""
- "@\"IPCLoadDirectionsMessage\""
- "@\"NSDictionary\"16@0:8"
- "@\"NSError\""
- "@\"NSURL\""
- "@24@0:8@\"NSCoder\"16"
- "@24@0:8@\"NSDictionary\"16"
- "IPCLoadDirectionsMessage"
- "IPCLoadDirectionsReply"
- "IPCMessage"
- "IPCMessageObject"
- "IPCShieldInfoMessage"
- "IPCStartNavigationMessage"
- "IPCTrafficIncidentAlertMessage"
- "MapsPushDaemonXPCClientInterface"
- "MapsXPCConnectionClient"
- "NSCoding"
- "NSSecureCoding"
- "T@\"GEORouteIncident\",&,N,V_incident"
- "T@\"IPCLoadDirectionsMessage\",&,N,V_loadDirectionsMessage"
- "T@\"NSData\",C,N,V_routeContextData"
- "T@\"NSData\",C,N,V_routeID"
- "T@\"NSData\",C,N,V_routePersistentData"
- "T@\"NSError\",C,N,V_error"
- "T@\"NSString\",C,N,V_identifier"
- "T@\"NSString\",C,N,V_shieldStringID"
- "T@\"NSString\",C,N,V_shieldText"
- "T@\"NSString\",C,N,V_subtitle"
- "T@\"NSString\",C,N,V_title"
- "T@\"NSURL\",C,N,V_url"
- "TB,N,V_originIsWatch"
- "TB,R"
- "TQ,N,V_navigationState"
- "TQ,N,V_routeIndex"
- "TQ,N,V_safetyWarningType"
- "TQ,N,V_type"
- "Ti,N,V_shieldID"
- "_dataValue"
- "_dictionaryValueFromData:"
- "_error"
- "_identifier"
- "_incident"
- "_loadDirectionsMessage"
- "_maps_mapsPushDaemonXPCClientInterface"
- "_navigationState"
- "_originIsWatch"
- "_routeContextData"
- "_routeID"
- "_routeIndex"
- "_routePersistentData"
- "_safetyWarningType"
- "_shieldID"
- "_shieldStringID"
- "_shieldText"
- "_subtitle"
- "_url"
- "dataValue"
- "decodeObjectOfClass:forKey:"
- "decodeTopLevelObjectOfClasses:forKey:error:"
- "encodeObject:forKey:"
- "encodeWithCoder:"
- "error"
- "incident"
- "initForReadingFromData:error:"
- "initWithCoder:"
- "isEqualToDictionary:"
- "kIPCLoadDirectionsMessageOriginIsWatch"
- "kIPCLoadDirectionsMessageRouteContextData"
- "kIPCLoadDirectionsMessageRoutePersistentData"
- "kIPCLoadDirectionsMessageURL"
- "kIPCLoadDirectionsReplyError"
- "kIPCLoadDirectionsReplySafetyWarningType"
- "kIPCLoadDirectionsReplyState"
- "kIPCShieldInfoMessageShieldIDKey"
- "kIPCShieldInfoMessageShieldStringIDKey"
- "kIPCShieldInfoMessageShieldTextKey"
- "kIPCStartNavigationMessageLoadDirectionsMessageKey"
- "kIPCStartNavigationMessageOriginIsWatchKey"
- "kIPCStartNavigationMessageRouteIDKey"
- "kIPCStartNavigationMessageRouteIndexKey"
- "kIPCTrafficIncidentAlertMessageIdentifierKey"
- "kIPCTrafficIncidentAlertMessageIncidentKey"
- "kIPCTrafficIncidentAlertMessageSubtitleKey"
- "kIPCTrafficIncidentAlertMessageTitleKey"
- "kIPCTrafficIncidentAlertMessageTypeKey"
- "loadDirectionsMessage"
- "matchesLoadDirectionsMessage:"
- "navigationState"
- "originIsWatch"
- "routeContextData"
- "routeID"
- "routeIndex"
- "routePersistentData"
- "safetyWarningType"
- "setError:"
- "setIdentifier:"
- "setIncident:"
- "setLoadDirectionsMessage:"
- "setNavigationState:"
- "setOriginIsWatch:"
- "setRouteContextData:"
- "setRouteID:"
- "setRouteIndex:"
- "setRoutePersistentData:"
- "setSafetyWarningType:"
- "setShieldID:"
- "setShieldStringID:"
- "setShieldText:"
- "setUrl:"
- "shieldID"
- "shieldStringID"
- "shieldText"
- "startNavigationMessageWithLoadDirectionsMessage:"
- "supportsSecureCoding"
- "url"
- "v24@0:8@\"NSCoder\"16"

```
