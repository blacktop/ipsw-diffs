## com.apple.NeighborhoodActivityConduitService

> `/System/Library/PrivateFrameworks/NeighborhoodActivityConduit.framework/XPCServices/com.apple.NeighborhoodActivityConduitService.xpc/com.apple.NeighborhoodActivityConduitService`

```diff

-1525.200.101.2.3
-  __TEXT.__text: 0xd921c
-  __TEXT.__auth_stubs: 0x28f0
-  __TEXT.__objc_methlist: 0x370
-  __TEXT.__objc_methname: 0x3c3d
-  __TEXT.__cstring: 0x35bf
-  __TEXT.__swift5_typeref: 0x2685
+1525.300.124.2.1
+  __TEXT.__text: 0xebe5c
+  __TEXT.__auth_stubs: 0x2a70
+  __TEXT.__objc_methlist: 0x328
+  __TEXT.__objc_methname: 0x3cfc
+  __TEXT.__cstring: 0x382f
+  __TEXT.__swift5_typeref: 0x2703
   __TEXT.__swift5_entry: 0x8
-  __TEXT.__const: 0x1d6c
-  __TEXT.__constg_swiftt: 0x1860
-  __TEXT.__swift5_builtin: 0x118
-  __TEXT.__swift5_reflstr: 0x125b
-  __TEXT.__swift5_fieldmd: 0xe14
-  __TEXT.__swift5_assocty: 0x108
-  __TEXT.__swift5_proto: 0x138
-  __TEXT.__swift5_types: 0xe4
+  __TEXT.__const: 0x1fcc
+  __TEXT.__constg_swiftt: 0x19c0
+  __TEXT.__swift5_builtin: 0x140
+  __TEXT.__swift5_reflstr: 0x13fb
+  __TEXT.__swift5_fieldmd: 0xedc
+  __TEXT.__swift5_assocty: 0x120
+  __TEXT.__swift5_proto: 0x158
+  __TEXT.__swift5_types: 0xf4
   __TEXT.__objc_classname: 0x11f
   __TEXT.__objc_methtype: 0xae5
-  __TEXT.__oslogstring: 0x47e4
-  __TEXT.__swift5_capture: 0x1a00
+  __TEXT.__oslogstring: 0x5004
+  __TEXT.__swift5_capture: 0x1bd8
   __TEXT.__swift5_mpenum: 0x20
-  __TEXT.__swift5_protos: 0x30
-  __TEXT.__unwind_info: 0x3548
-  __TEXT.__eh_frame: 0x9f70
-  __DATA_CONST.__auth_got: 0x1478
-  __DATA_CONST.__got: 0xae8
-  __DATA_CONST.__auth_ptr: 0x640
-  __DATA_CONST.__const: 0x4320
+  __TEXT.__swift5_protos: 0x34
+  __TEXT.__unwind_info: 0x38f8
+  __TEXT.__eh_frame: 0xae3c
+  __DATA_CONST.__auth_got: 0x1538
+  __DATA_CONST.__got: 0xb78
+  __DATA_CONST.__auth_ptr: 0x6b8
+  __DATA_CONST.__const: 0x4560
   __DATA_CONST.__objc_classlist: 0xb8
-  __DATA_CONST.__objc_protolist: 0x100
+  __DATA_CONST.__objc_protolist: 0xf8
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_protorefs: 0x90
-  __DATA.__objc_const: 0x4748
-  __DATA.__objc_selrefs: 0xa08
-  __DATA.__objc_data: 0xdd8
-  __DATA.__data: 0x3890
-  __DATA.__bss: 0x20a0
+  __DATA_CONST.__objc_protorefs: 0x88
+  __DATA.__objc_const: 0x4730
+  __DATA.__objc_selrefs: 0xa68
+  __DATA.__objc_data: 0xda8
+  __DATA.__data: 0x3b80
+  __DATA.__bss: 0x2420
   __DATA.__common: 0x110
   - /System/Library/Frameworks/Accounts.framework/Accounts
   - /System/Library/Frameworks/Combine.framework/Combine

   - /System/Library/PrivateFrameworks/NeighborhoodActivityConduit.framework/NeighborhoodActivityConduit
   - /System/Library/PrivateFrameworks/Rapport.framework/Rapport
   - /System/Library/PrivateFrameworks/TelephonyUtilities.framework/TelephonyUtilities
+  - /System/Library/PrivateFrameworks/UserManagement.framework/UserManagement
   - /usr/appleinternal/lib/liblinkguard.dylib
   - /usr/lib/libMobileGestalt.dylib
   - /usr/lib/libSystem.B.dylib

   - /usr/lib/swift/libswiftsimd.dylib
   - /usr/lib/swift/libswiftsys_time.dylib
   - /usr/lib/swift/libswiftunistd.dylib
-  Functions: 3042
-  Symbols:   338
-  CStrings:  1279
+  Functions: 3195
+  Symbols:   339
+  CStrings:  1338
 
Symbols:
+ _OBJC_CLASS_$_TUConversationLink
+ _TUCallIsSendingVideoChangedNotification
+ _TUCallIsUplinkMutedChangedNotification
- _dispatch_semaphore_create
- _swift_unknownObjectRetain_n
CStrings:
+ " conversationUuidString="
+ "<NCProtoContinuityCall uuidString="
+ "<PreparingHandoffInfo idsDeviceIdentifier="
+ "Continuity session ended: %!s(MISSING)"
+ "Conversation state changed from %!s(MISSING) to %!s(MISSING) for %!s(MISSING)"
+ "Disconnecting camera session (%!s(MISSING) because rapport is now out of session."
+ "End preparingHandoff: %!s(MISSING)."
+ "Ending existing conversation as we join another: %!s(MISSING)"
+ "Ending preparing handoff because device is no longer reachable %!s(MISSING)."
+ "Ending preparing handoff: %!s(MISSING)"
+ "Got %!s(MISSING) from server bag with a value of: %!@(MISSING)"
+ "Joined %!s(MISSING). Ending preparingHandoff: %!s(MISSING)"
+ "Left %!s(MISSING). Ending preparingHandoff: %!s(MISSING)"
+ "Pushing %!l(MISSING)d new contacts."
+ "Rejecting request because we're already joining a conversation: %!s(MISSING)"
+ "Removed active conversation %!@(MISSING)."
+ "Reset handoff for %!s(MISSING) - handoffState: %!s(MISSING)"
+ "Reset session state for %!s(MISSING)"
+ "Reseting state for session with %!s(MISSING)."
+ "Skipping contact push, no matching conversation for handoff info: %!s(MISSING))"
+ "TUConversationLetMeInRequestStateApproved"
+ "TUConversationLetMeInRequestStateNone"
+ "TUConversationLetMeInRequestStateNotRequested"
+ "TUConversationLetMeInRequestStateRequested"
+ "TUConversationLetMeInRequestStateUnknown("
+ "[AddParticipants] Not pushing contacts for %!s(MISSING)."
+ "[CreateLinkConversation] Continuity session doesn't exist for %!s(MISSING)"
+ "[CreateLinkConversation] Created conversation with link: %!s(MISSING)"
+ "[CreateLinkConversation] Creating conversation with link: %!s(MISSING) from %!s(MISSING)"
+ "[CreateLinkConversation] Handoff state unexpectedly changed: %!s(MISSING)"
+ "[CreateLinkConversation] Invalid conversation link %!s(MISSING)"
+ "[CreateLinkConversation] Join conversation link failed due to %!@(MISSING)"
+ "[CreateLinkConversation] Leaving conversation after timeout: %!s(MISSING)."
+ "[CreateLinkConversation] Reached timeout for %!@(MISSING)"
+ "[CreateLinkConversation] Reached timeout for %!s(MISSING) but conversation not found. No cleanup needed."
+ "[CreateLinkConversation] Rejecting request because we're already in a session: %!s(MISSING))"
+ "[CreateLinkConversation] Unable to join conversation link with blocked handles"
+ "[CreateLinkConversation] Waiting for conversation with link."
+ "[CreateLinkConversation] requested to create conversation with link: %!s(MISSING) from %!s(MISSING)"
+ "[Handoff][PullExpanse] No clients registered to approve sessions."
+ "[Handoff][Push] Unable to push conversation from Green Tea device."
+ "[LinkConversationAction] Continuity session doesn't exist for %!s(MISSING)"
+ "[LinkConversationAction] conversation not found %!s(MISSING)"
+ "[LinkConversationAction] invalid conversationUUID from %!s(MISSING)"
+ "[LinkConversationAction] invalid request from %!s(MISSING) for preparingHandoffInfo %!s(MISSING)"
+ "[LinkConversationAction] link for conversation not found %!@(MISSING)"
+ "[LinkConversationAction] unexpected no preparing handoff info"
+ "[LinkConversationCancel] %!s(MISSING) from %!s(MISSING)"
+ "[LinkConversationCancel] End prepared handoff for %!@(MISSING)."
+ "[PullConversationHandoff] Re-enabling Wombat priority and upgrading to %!s(MISSING)."
+ "[SendLetMeInRequest] %!s(MISSING) from %!s(MISSING)"
+ "[SendLetMeInRequest] Conversation does not have link %!s(MISSING)"
+ "[SendLetMeInRequest] Sending let me in request for: %!s(MISSING)"
+ "[SendLetMeInRequest] Sent let me in request to %!s(MISSING)"
+ "accountAltDSID"
+ "callDirectoryName"
+ "callGroupUUID"
+ "callServicesClientCapabilities"
+ "com.apple.callservicesd.createConversationLink"
+ "com.apple.callservicesd.linkConversationCancelRequest"
+ "com.apple.callservicesd.linkConversationSendLetMeInRequest"
+ "com_apple_NeighborhoodActivityConduitService.NeighborhoodActivityConduitServer"
+ "conduit-links-enabled"
+ "conversationLinkForURL:"
+ "defaultAppsEnabled"
+ "iCloudAltDSID"
+ "imageURL"
+ "initWithConversationLink:otherInvitedHandles:sendLetMeInRequest:"
+ "invitedMemberHandles"
+ "isEquivalentToConversationLink:"
+ "isScreening"
+ "isSendingVideoChangedNotificationToken"
+ "isTelephonyProvider"
+ "isUplinkMutedChangedNotificationToken"
+ "letMeInRequestState"
+ "localizedLabel"
+ "neighborhood-activity-conduit-prepared-conversation-timeout"
+ "preparingHandoffInfo"
+ "provider"
+ "sessionEndedSubject"
+ "setJoiningConversationWithLink:"
+ "setWantsToScreenCalls:"
+ "shouldRingForIncomingCallEnabled"
+ "splitSessionUpdated:"
+ "unknownInitiatorReportEnabled"
- "<NCProtoContinuityCall conversationUuidString="
- "Active conversation %!s(MISSING) removed while in joined state. Leaving..."
- "Asked to create nearby device handle for unrecognized IDS device %!s(MISSING)"
- "CSDNeighborhoodActivityConduitDelegate"
- "Conversation state changed from %!s(MISSING) to %!s(MISSING)"
- "Disconnecting camera session because rapport is now out of session."
- "NAC received an invalid conversation state transition from .joined -> .waiting. OldConversation: %!@(MISSING). NewConversation: %!@(MISSING)"
- "New delegate %!s(MISSING)"
- "Pushing %!l(MISSING)d new contacts for %!s(MISSING)."
- "Reseting state for camera session with %!s(MISSING)."
- "[JoinActiveConversation] Ending existing conversation as we join another: %!s(MISSING)"
- "[JoinActiveConversation] Rejecting join active conversation request because we're already handing off."
- "[PullConversationHandoff] Re-enabling Wombat priority and upgrading to video."
- "approveSplitSessionFor:from:pullContext:completion:"
- "canApproveSessions"
- "delegatesToQueues"
- "groupFaceTimeBlockEnabled"
- "initWithType:identifier:name:"
- "keyEnumerator"
- "mapTableWithKeyOptions:valueOptions:"
- "reportInitiatorEnabled"
- "splitSessionEnded:"
- "splitSessionStarted:"
- "v24@0:8@\"TUNearbyDeviceHandle\"16"
- "v48@0:8@\"TUConversation\"16@\"TUNearbyDeviceHandle\"24q32@?<v@?B@\"NSError\">40"
- "voiceCallSpamReportToCarrierEnabled"

```
