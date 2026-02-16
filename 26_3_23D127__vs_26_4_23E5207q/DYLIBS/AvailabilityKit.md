## AvailabilityKit

> `/System/Library/PrivateFrameworks/AvailabilityKit.framework/AvailabilityKit`

```diff

-116.400.11.0.0
-  __TEXT.__text: 0xdbc
-  __TEXT.__auth_stubs: 0x200
+116.500.122.2.1
+  __TEXT.__text: 0xe28
+  __TEXT.__auth_stubs: 0x1d0
   __TEXT.__objc_methlist: 0x154
   __TEXT.__const: 0x58
   __TEXT.__cstring: 0x46

   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_selrefs: 0x150
   __DATA_CONST.__objc_superrefs: 0x10
-  __AUTH_CONST.__auth_got: 0x108
+  __AUTH_CONST.__auth_got: 0xf0
   __AUTH_CONST.__const: 0x20
   __AUTH_CONST.__cfstring: 0x80
   __AUTH_CONST.__objc_const: 0x290

   - /System/Library/PrivateFrameworks/StatusKit.framework/StatusKit
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: B10F8DC0-8A8C-340E-98EB-B8D853D05CC9
+  UUID: A3A0893B-0C82-3216-90E0-3A58A3B0A41D
   Functions: 27
-  Symbols:   165
+  Symbols:   162
   CStrings:  94
 
Symbols:
+ _objc_retain_x22
+ _objc_retain_x23
- _objc_claimAutoreleasedReturnValue
- _objc_retainAutoreleaseReturnValue
- _objc_retain_x2
- _objc_retain_x24
- _objc_retain_x3
Functions:
~ -[AKAvailability(Deprecated) initWithAvailable:activityIdentifier:] : 88 -> 92
~ -[AKAvailability(StatusKit) initWithPublishedStatus:] : 140 -> 148
~ -[AKAvailability(StatusKit) statusPublishRequest] : 124 -> 128
~ -[AKAvailability(StatusKit) _payloadDictionary] : 200 -> 208
~ -[AKAvailability(StatusKit) initWithStatusPayload:invitationPayload:] : 1136 -> 1180
~ +[AKAvailability(StatusKit) logger] : 68 -> 84
~ -[NSDictionary(AvailabilityKit) availabilityKit_boolForKey:defaultValue:] : 92 -> 96
~ -[NSDictionary(AvailabilityKit) availabilityKit_stringForKey:] : 108 -> 112
~ -[AKAvailabilityInvitation initWithAvailableDuringActivityIdentifiers:unavailableDuringActivityIdentifiers:] : 156 -> 152
~ -[AKAvailabilityInvitation(StatusKit) initWithStatusKitInvitationPayload:] : 176 -> 184
~ -[AKAvailabilityInvitation(StatusKit) statusKitInvitationPayloadWithDateCreated:] : 120 -> 124
~ -[AKAvailabilityInvitation(StatusKit) _payloadDictionary] : 204 -> 212

```
