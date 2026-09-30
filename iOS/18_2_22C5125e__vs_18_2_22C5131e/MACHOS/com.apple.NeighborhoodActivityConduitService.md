## com.apple.NeighborhoodActivityConduitService

> `/System/Library/PrivateFrameworks/NeighborhoodActivityConduit.framework/XPCServices/com.apple.NeighborhoodActivityConduitService.xpc/com.apple.NeighborhoodActivityConduitService`

```diff

-1525.300.154.0.0
-  __TEXT.__text: 0xec864
-  __TEXT.__auth_stubs: 0x2ab0
-  __TEXT.__objc_methlist: 0x328
-  __TEXT.__objc_methname: 0x3d71
-  __TEXT.__cstring: 0x382f
-  __TEXT.__swift5_typeref: 0x2703
+1525.300.161.0.0
+  __TEXT.__text: 0xdc4d0
+  __TEXT.__auth_stubs: 0x29a0
+  __TEXT.__objc_methlist: 0x358
+  __TEXT.__objc_methname: 0x3cbe
+  __TEXT.__cstring: 0x37af
+  __TEXT.__swift5_typeref: 0x26c7
   __TEXT.__swift5_entry: 0x8
-  __TEXT.__const: 0x1fcc
-  __TEXT.__constg_swiftt: 0x19c0
+  __TEXT.__const: 0x203c
+  __TEXT.__constg_swiftt: 0x19d0
   __TEXT.__swift5_builtin: 0x140
-  __TEXT.__swift5_reflstr: 0x13fb
-  __TEXT.__swift5_fieldmd: 0xedc
+  __TEXT.__swift5_reflstr: 0x13bb
+  __TEXT.__swift5_fieldmd: 0xed4
   __TEXT.__swift5_assocty: 0x120
   __TEXT.__swift5_proto: 0x158
   __TEXT.__swift5_types: 0xf4
   __TEXT.__objc_classname: 0x11f
   __TEXT.__objc_methtype: 0xae5
-  __TEXT.__oslogstring: 0x5004
-  __TEXT.__swift5_capture: 0x1bf0
+  __TEXT.__oslogstring: 0x4824
+  __TEXT.__swift5_capture: 0x1a3c
   __TEXT.__swift5_mpenum: 0x20
-  __TEXT.__swift5_protos: 0x34
-  __TEXT.__unwind_info: 0x3940
-  __TEXT.__eh_frame: 0xaf84
-  __DATA_CONST.__auth_got: 0x1558
-  __DATA_CONST.__got: 0xb80
-  __DATA_CONST.__auth_ptr: 0x698
-  __DATA_CONST.__const: 0x4588
-  __DATA_CONST.__objc_classlist: 0xb8
+  __TEXT.__swift5_protos: 0x38
+  __TEXT.__unwind_info: 0x3650
+  __TEXT.__eh_frame: 0xa2c4
+  __DATA_CONST.__auth_got: 0x14d0
+  __DATA_CONST.__got: 0xb18
+  __DATA_CONST.__auth_ptr: 0x690
+  __DATA_CONST.__const: 0x42d8
+  __DATA_CONST.__objc_classlist: 0xc0
   __DATA_CONST.__objc_protolist: 0xf8
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_protorefs: 0x88
-  __DATA.__objc_const: 0x4760
-  __DATA.__objc_selrefs: 0xa90
-  __DATA.__objc_data: 0xda8
-  __DATA.__data: 0x3b98
-  __DATA.__bss: 0x2420
-  __DATA.__common: 0x110
+  __DATA.__objc_const: 0x4840
+  __DATA.__objc_selrefs: 0xa60
+  __DATA.__objc_data: 0xe78
+  __DATA.__data: 0x3a68
+  __DATA.__bss: 0x23a0
+  __DATA.__common: 0x118
   - /System/Library/Frameworks/Accounts.framework/Accounts
   - /System/Library/Frameworks/Combine.framework/Combine
   - /System/Library/Frameworks/Contacts.framework/Contacts

   - /usr/lib/swift/libswiftsimd.dylib
   - /usr/lib/swift/libswiftsys_time.dylib
   - /usr/lib/swift/libswiftunistd.dylib
-  Functions: 3209
-  Symbols:   339
-  CStrings:  1344
+  Functions: 3089
+  Symbols:   338
+  CStrings:  1305
 
Symbols:
- _OBJC_CLASS_$_TUConversationLink
CStrings:
+ "_TtC44com_apple_NeighborhoodActivityConduitService22ConversationPublishers"
+ "conversationJoinedSubject"
+ "conversationLeftSubject"
+ "conversationPublishers"
+ "handoffStateSubject"
- "<PreparingHandoffInfo idsDeviceIdentifier="
- "End preparingHandoff: %!s(MISSING)."
- "Ending preparing handoff because device is no longer reachable %!s(MISSING)."
- "Ending preparing handoff: %!s(MISSING)"
- "Got %!s(MISSING) from server bag with a value of: %!@(MISSING)"
- "Joined %!s(MISSING). Ending preparingHandoff: %!s(MISSING)"
- "Left %!s(MISSING). Ending preparingHandoff: %!s(MISSING)"
- "[CreateLinkConversation] Continuity session doesn't exist for %!s(MISSING)"
- "[CreateLinkConversation] Created conversation with link: %!s(MISSING)"
- "[CreateLinkConversation] Creating conversation with link: %!s(MISSING) from %!s(MISSING)"
- "[CreateLinkConversation] Handoff state unexpectedly changed: %!s(MISSING)"
- "[CreateLinkConversation] Invalid conversation link %!s(MISSING)"
- "[CreateLinkConversation] Join conversation link failed due to %!@(MISSING)"
- "[CreateLinkConversation] Leaving conversation after timeout: %!s(MISSING)."
- "[CreateLinkConversation] Reached timeout for %!@(MISSING)"
- "[CreateLinkConversation] Reached timeout for %!s(MISSING) but conversation not found. No cleanup needed."
- "[CreateLinkConversation] Rejecting request because we're already in a session: %!s(MISSING))"
- "[CreateLinkConversation] Unable to join conversation link with blocked handles"
- "[CreateLinkConversation] Waiting for conversation with link."
- "[CreateLinkConversation] requested to create conversation with link: %!s(MISSING) from %!s(MISSING)"
- "[LinkConversationAction] Continuity session doesn't exist for %!s(MISSING)"
- "[LinkConversationAction] conversation not found %!s(MISSING)"
- "[LinkConversationAction] invalid conversationUUID from %!s(MISSING)"
- "[LinkConversationAction] invalid request from %!s(MISSING) for preparingHandoffInfo %!s(MISSING)"
- "[LinkConversationAction] link for conversation not found %!@(MISSING)"
- "[LinkConversationAction] unexpected no preparing handoff info"
- "[LinkConversationCancel] %!s(MISSING) from %!s(MISSING)"
- "[LinkConversationCancel] End prepared handoff for %!@(MISSING)."
- "[SendLetMeInRequest] %!s(MISSING) from %!s(MISSING)"
- "[SendLetMeInRequest] Conversation does not have link %!s(MISSING)"
- "[SendLetMeInRequest] Sending let me in request for: %!s(MISSING)"
- "[SendLetMeInRequest] Sent let me in request to %!s(MISSING)"
- "com.apple.callservicesd.createConversationLink"
- "com.apple.callservicesd.linkConversationCancelRequest"
- "com.apple.callservicesd.linkConversationSendLetMeInRequest"
- "conduit-links-enabled"
- "conversationLinkForURL:"
- "initWithConversationLink:otherInvitedHandles:sendLetMeInRequest:"
- "invitedMemberHandles"
- "isEquivalentToConversationLink:"
- "neighborhood-activity-conduit-prepared-conversation-timeout"
- "preparingHandoffInfo"
- "setJoiningConversationWithLink:"

```
