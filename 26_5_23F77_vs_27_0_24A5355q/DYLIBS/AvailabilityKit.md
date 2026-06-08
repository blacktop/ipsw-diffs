## AvailabilityKit

> `/System/Library/PrivateFrameworks/AvailabilityKit.framework/AvailabilityKit`

```diff

-116.600.22.0.0
-  __TEXT.__text: 0xe28
-  __TEXT.__auth_stubs: 0x1d0
+143.100.3.0.0
+  __TEXT.__text: 0xd94
   __TEXT.__objc_methlist: 0x154
   __TEXT.__const: 0x58
-  __TEXT.__cstring: 0x46
+  __TEXT.__cstring: 0x4a
   __TEXT.__oslogstring: 0x4f6
   __TEXT.__unwind_info: 0xa8
-  __TEXT.__objc_classname: 0x51
-  __TEXT.__objc_methname: 0x5f2
-  __TEXT.__objc_methtype: 0x85
-  __TEXT.__objc_stubs: 0x420
-  __DATA_CONST.__got: 0x68
+  __TEXT.__objc_stubs: 0x0
+  __TEXT.__auth_stubs: 0x0
+  __TEXT.__objc_classname: 0x0
+  __TEXT.__objc_methname: 0x0
+  __TEXT.__objc_methtype: 0x0
   __DATA_CONST.__const: 0x28
   __DATA_CONST.__objc_classlist: 0x10
   __DATA_CONST.__objc_catlist: 0x8
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_selrefs: 0x150
   __DATA_CONST.__objc_superrefs: 0x10
-  __AUTH_CONST.__auth_got: 0xf0
+  __DATA_CONST.__got: 0x68
   __AUTH_CONST.__const: 0x20
   __AUTH_CONST.__cfstring: 0x80
   __AUTH_CONST.__objc_const: 0x290
-  __AUTH.__objc_data: 0x50
+  __AUTH_CONST.__auth_got: 0x0
   __DATA.__objc_ivar: 0x14
-  __DATA_DIRTY.__objc_data: 0x50
+  __DATA_DIRTY.__objc_data: 0xa0
   __DATA_DIRTY.__bss: 0x10
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/Foundation.framework/Foundation
   - /System/Library/PrivateFrameworks/StatusKit.framework/StatusKit
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 5FA1A353-8B69-320C-A3D8-5DBA6D98B74D
+  UUID: 2CE599D4-B412-3DDD-8378-38D1360CD05E
   Functions: 27
-  Symbols:   162
-  CStrings:  94
+  Symbols:   165
+  CStrings:  21
 
Symbols:
+ _objc_claimAutoreleasedReturnValue
+ _objc_retainAutoreleaseReturnValue
+ _objc_retain_x2
+ _objc_retain_x24
+ _objc_retain_x3
- _objc_retain_x22
- _objc_retain_x23
Functions:
~ -[AKAvailability(Deprecated) initWithAvailable:activityIdentifier:] : 92 -> 88
~ -[AKAvailability(StatusKit) initWithPublishedStatus:] : 148 -> 140
~ -[AKAvailability(StatusKit) statusPublishRequest] : 128 -> 124
~ -[AKAvailability(StatusKit) _payloadDictionary] : 208 -> 200
~ -[AKAvailability(StatusKit) initWithStatusPayload:invitationPayload:] : 1180 -> 1092
~ +[AKAvailability(StatusKit) logger] : 84 -> 68
~ -[NSDictionary(AvailabilityKit) availabilityKit_boolForKey:defaultValue:] : 96 -> 92
~ -[NSDictionary(AvailabilityKit) availabilityKit_stringForKey:] : 112 -> 108
~ -[AKAvailabilityInvitation initWithAvailableDuringActivityIdentifiers:unavailableDuringActivityIdentifiers:] : 152 -> 156
~ -[AKAvailabilityInvitation(StatusKit) initWithStatusKitInvitationPayload:] : 184 -> 176
~ -[AKAvailabilityInvitation(StatusKit) statusKitInvitationPayloadWithDateCreated:] : 124 -> 120
~ -[AKAvailabilityInvitation(StatusKit) _payloadDictionary] : 212 -> 204
~ -[NSDictionary(AvailabilityKit) availabilityKit_stringArrayForKey:allowEmptyString:] : 416 -> 420
CStrings:
- ".cxx_destruct"
- "@\"NSArray\""
- "@\"NSString\""
- "@16@0:8"
- "@24@0:8@16"
- "@28@0:8@16B24"
- "@28@0:8B16@20"
- "@32@0:8@16@24"
- "@32@0:8B16@20B28"
- "AKAvailabilityInvitation"
- "AvailabilityKit"
- "B"
- "B16@0:8"
- "B28@0:8@16B24"
- "Deprecated"
- "StatusKit"
- "T@\"NSArray\",R,N,V_availableDuringActivityIdentifiers"
- "T@\"NSArray\",R,N,V_unavailableDuringActivityIdentifiers"
- "T@\"NSString\",R,N,V_activityIdentifierString"
- "T@\"NSUUID\",R,N"
- "TB,R,N,GisAvailable,V_available"
- "TB,R,N,GisAvailableToMe"
- "TB,R,N,V_personalizedAvailability"
- "UUIDString"
- "_activityIdentifierString"
- "_available"
- "_availableDuringActivityIdentifiers"
- "_initWithAvailable:activityIdentifierString:personalizedAvailability:"
- "_payloadDictionary"
- "_personalizedAvailability"
- "_unavailableDuringActivityIdentifiers"
- "activityIdentifier"
- "activityIdentifierString"
- "addObject:"
- "availabilityKit_boolForKey:defaultValue:"
- "availabilityKit_stringArrayForKey:allowEmptyString:"
- "availabilityKit_stringForKey:"
- "available"
- "availableDuringActivityIdentifiers"
- "availableToMe"
- "boolValue"
- "containsObject:"
- "copy"
- "count"
- "countByEnumeratingWithState:objects:count:"
- "init"
- "initWithAvailable:activityIdentifier:"
- "initWithAvailable:activityIdentifierString:"
- "initWithAvailableDuringActivityIdentifiers:"
- "initWithAvailableDuringActivityIdentifiers:unavailableDuringActivityIdentifiers:"
- "initWithDictionary:"
- "initWithDictionary:dateCreated:"
- "initWithPublishedStatus:"
- "initWithStatusKitInvitationPayload:"
- "initWithStatusPayload:"
- "initWithStatusPayload:invitationPayload:"
- "initWithUUIDString:"
- "invitationPayload"
- "isAvailable"
- "isAvailableToMe"
- "length"
- "logger"
- "numberWithBool:"
- "objectForKeyedSubscript:"
- "payloadDictionary"
- "personalizedAvailability"
- "setObject:forKeyedSubscript:"
- "statusKitInvitationPayloadWithDateCreated:"
- "statusPayload"
- "statusPublishRequest"
- "unavailableDuringActivityIdentifiers"
- "v16@0:8"

```
