## UARPUpdaterService

> `/System/Library/PrivateFrameworks/UARPUpdaterService.framework/UARPUpdaterService`

```diff

-1345.120.5.0.0
-  __TEXT.__text: 0x1b58
-  __TEXT.__auth_stubs: 0x150
+1576.0.0.0.0
+  __TEXT.__text: 0x1880
   __TEXT.__objc_methlist: 0x440
   __TEXT.__const: 0x68
-  __TEXT.__cstring: 0x453
+  __TEXT.__cstring: 0x455
   __TEXT.__oslogstring: 0x106
   __TEXT.__unwind_info: 0x108
-  __TEXT.__objc_classname: 0xef
-  __TEXT.__objc_methname: 0x67a
-  __TEXT.__objc_methtype: 0x28d
-  __TEXT.__objc_stubs: 0x2e0
-  __DATA_CONST.__got: 0x88
+  __TEXT.__objc_stubs: 0x0
+  __TEXT.__auth_stubs: 0x0
+  __TEXT.__objc_classname: 0x0
+  __TEXT.__objc_methname: 0x0
+  __TEXT.__objc_methtype: 0x0
   __DATA_CONST.__objc_classlist: 0x30
   __DATA_CONST.__objc_protolist: 0x18
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_selrefs: 0x1c0
   __DATA_CONST.__objc_superrefs: 0x30
-  __AUTH_CONST.__auth_got: 0xb0
+  __DATA_CONST.__got: 0x88
   __AUTH_CONST.__cfstring: 0x1a0
   __AUTH_CONST.__objc_const: 0x908
+  __AUTH_CONST.__auth_got: 0x0
   __AUTH.__objc_data: 0xa0
   __DATA.__objc_ivar: 0x28
   __DATA.__data: 0x120

   - /System/Library/Frameworks/Foundation.framework/Foundation
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 0497541B-DF0B-3FDB-A348-004D3FA989F2
+  UUID: 4394EEF3-153A-3520-B578-5DB9C5A5F641
   Functions: 61
-  Symbols:   282
-  CStrings:  156
+  Symbols:   283
+  CStrings:  46
 
Symbols:
+ _objc_claimAutoreleasedReturnValue
+ _objc_retain_x2
+ _objc_retain_x5
- _objc_retainAutoreleasedReturnValue
- _objc_retain_x19
Functions:
~ -[UARPUpdaterServicePreferences uuidForAccessory:serialNumber:error:] : 848 -> 780
~ -[UARPUpdaterServiceBase getMatchingServicesListWithReply:] : 200 -> 156
~ -[UARPUpdaterServiceBase ioKitRuleMatched:] : 156 -> 112
~ -[UARPUpdaterServiceBase getBSDNotificationsListWithReply:] : 200 -> 156
~ -[UARPUpdaterServiceBase bsdNotificationReceived:] : 156 -> 112
~ -[UARPUpdaterServiceBase getDASActivityListWithReply:] : 200 -> 156
~ -[UARPUpdaterServiceBase dasActivityReceived:] : 156 -> 112
~ -[UARPUpdaterServiceBase consentReceived:] : 156 -> 112
~ -[UARPUpdaterServiceBase consentReceivedPostLogoutMode:] : 156 -> 112
~ -[UARPUpdaterServiceBase disabledProductIdentifiers:] : 156 -> 112
~ -[UARPUpdaterServiceBase getIsBusyStatusWithReply:] : 196 -> 152
~ -[UARPUpdaterServiceBase eaRuleMatched:] : 156 -> 112
~ -[UARPUpdaterServiceBase standaloneDynamicAssetSolicitation:modelNumber:notifyService:reply:] : 196 -> 152
~ -[UARPUpdaterServiceBase standaloneDynamicAssetSolicitation:modelNumbers:notifyService:reply:] : 196 -> 152
~ -[UARPUpdaterServiceBase queryPendingTssRequests:] : 200 -> 156
~ -[UARPUpdaterServiceBase tssResponse:] : 156 -> 112
CStrings:
- ".cxx_destruct"
- "@\"NSDictionary\""
- "@\"NSString\""
- "@16@0:8"
- "@24@0:8@\"NSCoder\"16"
- "@24@0:8@16"
- "@32@0:8@16@24"
- "@32@0:8@16Q24"
- "@40@0:8@16@24@32"
- "@40@0:8@16@24^@32"
- "B16@0:8"
- "B24@0:8@16"
- "NSCoding"
- "NSSecureCoding"
- "Q"
- "Q16@0:8"
- "T@\"NSDictionary\",R,V_matchingDictionary"
- "T@\"NSString\",R,V_accessorySerialNumber"
- "T@\"NSString\",R,V_domain"
- "T@\"NSString\",R,V_eaIdentifier"
- "T@\"NSString\",R,V_identifier"
- "T@\"NSString\",R,V_xpcEventStream"
- "TB,R"
- "TQ,R,V_registryEntryID"
- "UARPServiceUpdaterAccessoryMatchingRule"
- "UARPServiceUpdaterDASMatchingRule"
- "UARPServiceUpdaterMatchedEARule"
- "UARPServiceUpdaterMatchedIOKitRule"
- "UARPUpdaterService"
- "UARPUpdaterServiceBase"
- "UARPUpdaterServicePreferences"
- "UUID"
- "_accessorySerialNumber"
- "_domain"
- "_eaIdentifier"
- "_identifier"
- "_matchingDictionary"
- "_registryEntryID"
- "_xpcEventStream"
- "accessorySerialNumber"
- "appendWithTabDepth:format:"
- "archivedDataWithRootObject:requiringSecureCoding:error:"
- "arrayWithObjects:count:"
- "bsdNotificationReceived:"
- "consentReceived:"
- "consentReceivedPostLogoutMode:"
- "copy"
- "dasActivityReceived:"
- "dealloc"
- "decodeObjectOfClass:forKey:"
- "decodeObjectOfClasses:forKey:"
- "description"
- "disabledProductIdentifiers:"
- "domain"
- "dumpWithTabDepth:dumpString:"
- "eaIdentifier"
- "eaRuleMatched:"
- "encodeObject:forKey:"
- "encodeWithCoder:"
- "getBSDNotificationsListWithReply:"
- "getDASActivityListWithReply:"
- "getIsBusyStatusWithReply:"
- "getMatchingServicesListWithReply:"
- "hash"
- "init"
- "initWithCoder:"
- "initWithDomain:"
- "initWithEAIdentifier:accessorySerialNumber:"
- "initWithIdentifier:matchingDictionary:"
- "initWithIdentifier:registryEntryID:"
- "initWithIdentifier:xpcEventStream:matchingDictionary:"
- "initWithSuiteName:"
- "ioKitRuleMatched:"
- "isEqual:"
- "numberWithUnsignedLongLong:"
- "objectForKey:"
- "queryPendingTssRequests:"
- "r*16@0:8"
- "removeObjectForKey:"
- "setObject:forKey:"
- "setWithArray:"
- "standaloneDynamicAssetSolicitation:modelNumber:notifyService:reply:"
- "standaloneDynamicAssetSolicitation:modelNumbers:notifyService:reply:"
- "stringWithFormat:"
- "supportsSecureCoding"
- "transportDescription"
- "tssResponse:"
- "unarchivedObjectOfClass:fromData:error:"
- "unsignedLongLongValue"
- "uuidForAccessory:serialNumber:error:"
- "v16@0:8"
- "v24@0:8@\"NSCoder\"16"
- "v24@0:8@\"NSDictionary\"16"
- "v24@0:8@\"NSString\"16"
- "v24@0:8@\"UARPConsent\"16"
- "v24@0:8@\"UARPServiceUpdaterDASMatchingRule\"16"
- "v24@0:8@\"UARPServiceUpdaterMatchedEARule\"16"
- "v24@0:8@\"UARPServiceUpdaterMatchedIOKitRule\"16"
- "v24@0:8@16"
- "v24@0:8@?16"
- "v24@0:8@?<v@?@\"NSArray\">16"
- "v24@0:8@?<v@?B>16"
- "v32@0:8Q16@24"
- "v48@0:8@\"UARPAssetTag\"16@\"NSArray\"24@\"NSXPCListenerEndpoint\"32@?<v@?B>40"
- "v48@0:8@\"UARPAssetTag\"16@\"NSString\"24@\"NSXPCListenerEndpoint\"32@?<v@?B>40"
- "v48@0:8@16@24@32@?40"

```
