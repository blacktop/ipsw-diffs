## callservicesd

> `/System/Library/PrivateFrameworks/TelephonyUtilities.framework/callservicesd`

```diff

-1431.300.81.2.2
-  __TEXT.__text: 0x33a6f0
-  __TEXT.__auth_stubs: 0x3a90
-  __TEXT.__objc_stubs: 0x2e520
-  __TEXT.__objc_methlist: 0x1a4f4
+1431.400.41.2.1
+  __TEXT.__text: 0x33b630
+  __TEXT.__auth_stubs: 0x3aa0
+  __TEXT.__objc_stubs: 0x2e680
+  __TEXT.__objc_methlist: 0x1a56c
   __TEXT.__objc_classname: 0x28ea
-  __TEXT.__objc_methname: 0x51812
+  __TEXT.__objc_methname: 0x51b3c
   __TEXT.__objc_methtype: 0xe1c5
-  __TEXT.__cstring: 0x21efd
-  __TEXT.__oslogstring: 0x30f75
+  __TEXT.__cstring: 0x21fed
+  __TEXT.__oslogstring: 0x3165a
   __TEXT.__const: 0x6aa6
-  __TEXT.__gcc_except_tab: 0x1c34
+  __TEXT.__gcc_except_tab: 0x1c84
   __TEXT.__ustring: 0x10
-  __TEXT.__swift5_typeref: 0x5102
+  __TEXT.__swift5_typeref: 0x50fc
   __TEXT.__swift5_entry: 0x8
-  __TEXT.__constg_swiftt: 0x4968
+  __TEXT.__constg_swiftt: 0x4980
   __TEXT.__swift5_builtin: 0x4c4
   __TEXT.__swift5_reflstr: 0x4233
   __TEXT.__swift5_fieldmd: 0x38b4
   __TEXT.__swift5_assocty: 0x650
   __TEXT.__swift5_proto: 0x540
   __TEXT.__swift5_types: 0x3ac
-  __TEXT.__swift5_capture: 0x1fd8
+  __TEXT.__swift5_capture: 0x1fe4
   __TEXT.__swift5_protos: 0xd8
   __TEXT.__swift5_mpenum: 0x20
-  __TEXT.__unwind_info: 0xa9f8
-  __TEXT.__eh_frame: 0x38f8
-  __DATA_CONST.__auth_got: 0x1d58
-  __DATA_CONST.__got: 0xfe8
+  __TEXT.__unwind_info: 0xa9e8
+  __TEXT.__eh_frame: 0x38a0
+  __DATA_CONST.__auth_got: 0x1d60
+  __DATA_CONST.__got: 0xff0
   __DATA_CONST.__auth_ptr: 0x2a0
   __DATA_CONST.__const: 0x113c0
-  __DATA_CONST.__cfstring: 0x9680
+  __DATA_CONST.__cfstring: 0x96c0
   __DATA_CONST.__objc_classlist: 0x908
   __DATA_CONST.__objc_catlist: 0x1a0
   __DATA_CONST.__objc_protolist: 0x8b8
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_intobj: 0x1b0
+  __DATA_CONST.__objc_intobj: 0x1c8
   __DATA_CONST.__objc_arraydata: 0x18
   __DATA_CONST.__objc_arrayobj: 0x30
   __DATA_CONST.__linkguard: 0x16
-  __DATA.__objc_const: 0x399c8
-  __DATA.__objc_selrefs: 0xeea8
+  __DATA.__objc_const: 0x39b58
+  __DATA.__objc_selrefs: 0xeef0
   __DATA.__objc_protorefs: 0x2b8
   __DATA.__objc_classrefs: 0x1290
   __DATA.__objc_superrefs: 0x5b0
-  __DATA.__objc_ivar: 0x193c
-  __DATA.__objc_data: 0x90f0
-  __DATA.__data: 0xae10
+  __DATA.__objc_ivar: 0x1948
+  __DATA.__objc_data: 0x9108
+  __DATA.__data: 0xae40
   __DATA.__bss: 0x8018
   __DATA.__common: 0x3a8
   - /System/Library/Frameworks/AVFAudio.framework/AVFAudio

   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  UUID: 0B5934AA-0002-3F77-AB8B-860E29D13D5D
-  Functions: 18877
-  Symbols:   2012
-  CStrings:  20324
+  UUID: 42F364F5-0B15-3AC1-A8D8-2CCDC386D889
+  Functions: 18888
+  Symbols:   2014
+  CStrings:  20384
 
Symbols:
+ _IDSCopyTokenAndIDForTokenWithID
+ _IDSSendMessageOptionForceQuery
CStrings:
+ "Approve the request, remove pending member and add remote member: %@"
+ "B\x14/\x0f\x02\x14/\x06\x12\x18"
+ "Could not find activated link for join call action %@, link: %@"
+ "Current IDStatus results: %@ service: %@, fromIDURI: %@"
+ "Current remote device results: %@ for destinationIDs: %@, service: %@, fromIDURI: %@"
+ "Decline the request, remove pending member: %@"
+ "DefaultsRemovedURI"
+ "Finding activated link in join call action %@"
+ "Found activated link for join call action %@, link: %@"
+ "Get matching memeber: %@ current pendingRemoteMembers: %@"
+ "Getting activated link for callerID %@, activatedLink: %@"
+ "LMI: Couldn't find activated link for join call action %@"
+ "No conversation participant"
+ "No info matching local user action {uuid: %@, handle: %@}, remove pending member: %@"
+ "No need to add lightweight member to the session"
+ "No pendingRemoteMembers, cancel letMeInRequestUINotificationBlock"
+ "Not link creator for %@ - not renewing"
+ "Processing local user action for pending member {info: %@, action: %@, member: %@, conversation.groupUUID: %@, conversation: %@}"
+ "Required IDStatus results: %@ service: %@ fromID: %@"
+ "T@\"NSMutableSet\",C,N,V_pendingRemoteMembers"
+ "T@?,C,N,V_letMeInRequestUINotificationBlock"
+ "T@?,C,N,V_noConversationParticipantTimeoutBlock"
+ "TB,R,N,GisLetMeInRequestUIForUnknownParticipantEnabled"
+ "TB,R,N,GisNoConversationParticipantEndCallEnabled"
+ "Use existing pendingConversationUUID: %@"
+ "User defaults: added to remote member: %@, continue adding active participant"
+ "User defaults: do not add %@ to participant"
+ "Validated link for join call action %@ link: %@"
+ "_endCallIfNecessary"
+ "_endCallIfNecessary: Cancel noConversationParticipantTimeoutBlock"
+ "_endCallIfNecessary: Conversation has activeRemoteParticipants: %@, return"
+ "_endCallIfNecessary: The participant couldn't add any active participants in the session, end call,  activeParticipantDestinationsByIdentifier: %@"
+ "_endCallIfNecessary: noConversationParticipantTimeout is running, return"
+ "_endCallIfNecessary: started noConversationParticipantTimeout: %d"
+ "_letMeInRequestUINotificationBlock"
+ "_noConversationParticipantTimeoutBlock"
+ "_pendingRemoteMembers"
+ "_showLetMeInUIIfNecessary"
+ "activatedLinksWithCompleted: tuconversation: %@"
+ "add pending remote members: %@ to %@"
+ "addRemoteMembers, remove pending member: %@"
+ "addRemoteMembers, remove pending remote member: %@ from: %@"
+ "completed invalidate the link: %@"
+ "completed renewPseudonym %@"
+ "currentIDStatusForDestinations:service:preferredFromID:listenerID:queue:completionBlock:"
+ "currentRemoteDevicesForDestinations:service:preferredFromID:listenerID:queue:completionBlock:"
+ "disable noConversationParticipantEndCall due to server over-ride"
+ "disable showLetMeInUI due to server over-ride"
+ "find existing conversation: %@"
+ "get resolved link: %@ for link: %@"
+ "handleReceivedLinkInvalidatedMessage: remove link: %@"
+ "isLetMeInRequestUIForUnknownParticipantEnabled"
+ "isNoConversationParticipantEndCallEnabled"
+ "leaveUsingContext: self UUID: %@"
+ "letMeIn: %@, link: %@"
+ "letMeInRequestUIForUnknownParticipantEnabled"
+ "letMeInRequestUINotificationBlock"
+ "letMeInRequestUINotificationGracePeriod"
+ "link based call, member: %@ is already added to remoteMembers: %@"
+ "link based call, show up LMI request UI for %@, remoteHandles: %@"
+ "lmi-request-ui-unknown-participant-enabled"
+ "member: %@ is in remoteMemberForHandle"
+ "member: %@ is not in pendingMemberHandles: %@"
+ "member: %@ is not in pendingRemoteMembers: %@"
+ "no-conversation-participant-end-call-enabled"
+ "noConversationParticipantEndCallEnabled"
+ "noConversationParticipantTimeout"
+ "noConversationParticipantTimeoutBlock"
+ "notifyDelegatesOfChangedLinkDescriptors: %@"
+ "pendingRemoteMembers"
+ "qr-session-no-conversation-participant-timeout"
+ "removeLink completed for %@ "
+ "removePendingMembers: %@ triggeredLocally: %d"
+ "renewLinkWithPseudonym succeeded: %@"
+ "requiredIDStatusForDestinations:service:preferredFromID:listenerID:queue:completionBlock:"
+ "sendDataBlock options: %@"
+ "set fromIDURI: %@, fromID: %@"
+ "setConversationLink %@ completed"
+ "setLetMeInRequestUINotificationBlock:"
+ "setNoConversationParticipantTimeoutBlock:"
+ "setPendingRemoteMembers:"
+ "setting state to: %ld, from: %ld"
+ "shouldRespondToLetMeInRequestForMember:"
+ "show-let-me-in-request-ui-grace-period"
+ "store received link"
+ "updated pendingRemoteMembers: %@"
+ "waiting till existing letMeInRequestUINotification completes"
- "B\x14/\x0f\x02\x14/\x03\x12\x18"
- "Current IDStatus results: %@ service: %@"
- "Current remote device results: %@ for destinationIDs: %@, service: %@"
- "Error finding a matching deleted link in join call action failed %@"
- "Error undeleting link %@ %@"
- "Finding activated or deleted link in join call action %@"
- "Found activated link for join call action %@ %@"
- "Found deleted link for join call action %@ %@"
- "Getting activated link for callerID %@"
- "LMI: Couldn't find activated or deleted link for join call action %@"
- "Link isn't deleted %@"
- "Loaded %ld conversation links for predicate %@ when we only expected one"
- "Loading descriptors for link %@ with predicate %@"
- "No info matching local user action -- ignoring {uuid: %@, handle: %@}"
- "Processing local user action for pending member {info: %@, action: %@, member: %@, conversation.groupUUID: %@}"
- "Requested to undelete link %@"
- "Required IDStatus results: %@ service: %@"
- "Unable to create mutable copy of %s as TUMutableConversationLinkDescriptor"
- "Undeleting link %@"
- "Updating descriptor for link %@ %@"
- "Validated link for join call action %@ %@"
- "currentIDStatusForDestinations:service:listenerID:queue:completionBlock:"
- "currentRemoteDevicesForDestinations:service:listenerID:queue:completionBlock:"
- "deletionDate"
- "downloadVoicemailAssetsFromCarrier: removing %s from greetingsDict: %s, because voicemailManager doesn't report it as an account %s"
- "letMeIn: %@"
- "remove pendingMembers: %@ triggeredLocally: %d"
- "requiredIDStatusForDestinations:service:listenerID:queue:completionBlock:"
- "self UUID: %@"
- "set fromID: %@"
- "setFromID:"
- "undeleteConversationLink:withError:"
- "undeleteConversationLinkIfNecessary:withError:"

```
