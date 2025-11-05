## AvailabilityKit

> `/System/Library/PrivateFrameworks/AvailabilityKit.framework/Versions/A/AvailabilityKit`

```diff

-80.400.131.0.0
-  __TEXT.__text: 0xf00
+80.500.181.0.0
+  __TEXT.__text: 0xef0
   __TEXT.__auth_stubs: 0x110
   __TEXT.__objc_methlist: 0x154
   __TEXT.__const: 0x50
   __TEXT.__cstring: 0x46
   __TEXT.__oslogstring: 0x4f6
-  __TEXT.__unwind_info: 0xa0
+  __TEXT.__unwind_info: 0xa8
   __TEXT.__objc_classname: 0x51
   __TEXT.__objc_methname: 0x5f2
   __TEXT.__objc_methtype: 0x85

   - /System/Library/PrivateFrameworks/StatusKit.framework/Versions/A/StatusKit
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: CBC36C9B-FF43-3D8E-ACAB-165FF14773F4
-  Functions: 26
-  Symbols:   126
+  UUID: 1C0555A8-CEAC-362B-B1E8-00310B953EF4
+  Functions: 27
+  Symbols:   127
   CStrings:  94
 
Symbols:
+ +[AKAvailability(StatusKit) logger].cold.1
Functions:
~ -[AKAvailability(StatusKit) initWithPublishedStatus:] : 164 -> 168
~ -[AKAvailability(StatusKit) initWithStatusPayload:invitationPayload:] : 1260 -> 1220
~ +[AKAvailability(StatusKit) logger] : 84 -> 68
~ -[AKAvailability(Deprecated) activityIdentifier] : 84 -> 96
~ -[AKAvailabilityInvitation(StatusKit) initWithStatusKitInvitationPayload:] : 200 -> 204

```
