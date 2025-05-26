## com.apple.NeighborhoodActivityConduitService

> `/System/Library/PrivateFrameworks/NeighborhoodActivityConduit.framework/XPCServices/com.apple.NeighborhoodActivityConduitService.xpc/com.apple.NeighborhoodActivityConduitService`

```diff

-1431.400.41.2.1
-  __TEXT.__text: 0xe5dbc
-  __TEXT.__auth_stubs: 0x2700
-  __TEXT.__objc_methlist: 0x2f4
-  __TEXT.__objc_methname: 0x360c
-  __TEXT.__cstring: 0x749f
-  __TEXT.__swift5_typeref: 0x24ba
+1431.500.151.2.9
+  __TEXT.__text: 0xe212c
+  __TEXT.__auth_stubs: 0x2750
+  __TEXT.__objc_methlist: 0x324
+  __TEXT.__objc_methname: 0x3778
+  __TEXT.__cstring: 0x7ab4
+  __TEXT.__swift5_typeref: 0x260f
   __TEXT.__swift5_entry: 0x8
-  __TEXT.__const: 0x183e
-  __TEXT.__constg_swiftt: 0x1574
-  __TEXT.__swift5_builtin: 0x104
-  __TEXT.__swift5_reflstr: 0x1006
-  __TEXT.__swift5_fieldmd: 0xd18
+  __TEXT.__const: 0x1b9c
+  __TEXT.__constg_swiftt: 0x17c0
+  __TEXT.__swift5_builtin: 0x154
+  __TEXT.__swift5_reflstr: 0x119b
+  __TEXT.__swift5_fieldmd: 0xe40
   __TEXT.__swift5_assocty: 0x108
-  __TEXT.__swift5_proto: 0x114
-  __TEXT.__swift5_types: 0xc8
+  __TEXT.__swift5_proto: 0x130
+  __TEXT.__swift5_types: 0xe8
   __TEXT.__objc_classname: 0x134
   __TEXT.__objc_methtype: 0xc11
-  __TEXT.__swift5_capture: 0x1b70
-  __TEXT.__swift5_mpenum: 0x10
+  __TEXT.__swift5_capture: 0x1c80
+  __TEXT.__swift5_mpenum: 0x20
   __TEXT.__swift5_protos: 0x30
-  __TEXT.__unwind_info: 0x4354
-  __TEXT.__eh_frame: 0xae18
-  __DATA_CONST.__auth_got: 0x1380
-  __DATA_CONST.__got: 0x798
-  __DATA_CONST.__auth_ptr: 0x80
-  __DATA_CONST.__const: 0x5300
-  __DATA_CONST.__objc_classlist: 0xa8
+  __TEXT.__unwind_info: 0x42ac
+  __TEXT.__eh_frame: 0xabf0
+  __DATA_CONST.__auth_got: 0x13a8
+  __DATA_CONST.__got: 0x7e0
+  __DATA_CONST.__auth_ptr: 0x90
+  __DATA_CONST.__const: 0x5970
+  __DATA_CONST.__objc_classlist: 0xb0
   __DATA_CONST.__objc_catlist: 0x10
   __DATA_CONST.__objc_protolist: 0x110
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA.__objc_const: 0x3e28
-  __DATA.__objc_selrefs: 0x978
-  __DATA.__objc_protorefs: 0x98
-  __DATA.__objc_classrefs: 0x250
-  __DATA.__objc_data: 0xc00
+  __DATA_CONST.__objc_protorefs: 0x98
+  __DATA_CONST.__objc_classrefs: 0x258
+  __DATA.__objc_const: 0x41a8
+  __DATA.__objc_selrefs: 0x988
+  __DATA.__objc_data: 0xdc0
   __DATA.__data: 0x3968
-  __DATA.__bss: 0x1e10
-  __DATA.__common: 0x108
+  __DATA.__bss: 0x21a0
+  __DATA.__common: 0x110
   - /System/Library/Frameworks/Accounts.framework/Accounts
   - /System/Library/Frameworks/Combine.framework/Combine
   - /System/Library/Frameworks/Contacts.framework/Contacts

   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  Functions: 3454
-  Symbols:   312
-  CStrings:  1196
+  Functions: 3590
+  Symbols:   317
+  CStrings:  1232
 
Symbols:
+ _CFNotificationCenterAddObserver
+ _CFNotificationCenterGetDarwinNotifyCenter
+ _CFNotificationCenterRemoveObserver
+ _OBJC_CLASS_$_SwiftNativeNSObject
+ _OBJC_CLASS_$_TUICFInterface
+ _OBJC_METACLASS_$_SwiftNativeNSObject
+ _TUBundleIdentifierFaceTimeApplication
+ _objc_retain_x2
- _objc_retain_x1
- _swift_getErrorValue
- _swift_isUniquelyReferenced_nonNull_bridgeObject
CStrings:
+ " conversationUUID="
+ " idsDeviceIdentifier="
+ " shouldResetCallState="
+ " shouldResetHandoffState="
+ " shouldTeardownContinuitySession="
+ "<ContinuitySession idsDeviceIdentifier="
+ "<FailureStatus shouldPrepareConversationForInitialMode="
+ "<HandoffInfo type="
+ "Asked to create nearby device handle for unrecognized IDS device %s"
+ "Asked to reset state for %s: %s."
+ "Camera continuity session updated to %s"
+ "Can't construct Array with count < 0"
+ "Cannot initiate session with %s while camera session already exists: %s"
+ "Continuity camera connected. End any ongoing calls on iOS device."
+ "Disconnect call %@ with reason: %s"
+ "DisconnectReason("
+ "DisconnectReason.UNRECOGNIZED("
+ "DisconnectReason.blockedContact"
+ "DisconnectReason.endingHandoff"
+ "DisconnectReason.pullingBackToPhone"
+ "DisconnectReason.unknown"
+ "Disconnected from %s with reason %ld result %{bool}d"
+ "Disconnecting camera session because rapport and conduit session devices are mismatched: [%s and %s]"
+ "Disconnecting camera session because rapport is now out of session."
+ "Division by zero"
+ "Division results in an overflow"
+ "Exiting discovery session due to teardownSession request."
+ "Failed to activate remote display discovery due to %@"
+ "Failed to disconnect from %s with reason %s. Error %@"
+ "Fatal error"
+ "Handoff state updated to %s"
+ "Insufficient space allocated to copy string contents"
+ "Negative value is not representable"
+ "Not enough bits to represent the passed value"
+ "PrepareForHandoff] Failed to establish laguna connection due to %@."
+ "Received language change, restarting process"
+ "Rejecting start laguna session request because we already have an active session."
+ "Reset suggestion for reason: %s"
+ "Sending cancel result for %@ reason: %s"
+ "Sending disconnect request for %s with reason %ld"
+ "Skipping contact push because we're not handed off: %s)"
+ "Swift/Array.swift"
+ "Swift/ContiguousArrayBuffer.swift"
+ "Swift/IntegerTypes.swift"
+ "Swift/Integers.swift"
+ "Swift/StringTesting.swift"
+ "Swift/StringUTF8View.swift"
+ "Swift/UnsafeBufferPointer.swift"
+ "Swift/UnsafePointer.swift"
+ "Swift/UnsafeRawPointer.swift"
+ "T@\"NSString\",?,R,C"
+ "Unexpectedly found nil while unwrapping an Optional value"
+ "UnsafeMutableBufferPointer with negative count"
+ "UnsafeMutablePointer.initialize overlapping range"
+ "UnsafeMutablePointer.initialize with negative count"
+ "UnsafeMutablePointer.moveInitialize with negative count"
+ "UnsafeMutableRawPointer.initializeMemory overlapping range"
+ "[%s] Failed to send event %s due to %@."
+ "[AddParticipants] Attempted to add a blocked contact but secondary member did not handle leaving the conversation so primary is leaving"
+ "[Auth] Incorrect password provided - aborting."
+ "[Auth] Pairing request throttled - aborting."
+ "[DeclineCall] Received decline continuity call request for %s from %s."
+ "[DeclineCall] Rejecting request because no session exists for %s."
+ "[GetContacts] Rejecting request to brows contacts from a device with which we do not have a session: %s"
+ "[HandoffConversation] Failed to hand off due to %@. Rolling back with %s"
+ "[HandoffConversation] Rejecting request because we already have a session active with a different device %s"
+ "[Handoff][PullExpanse] Failed to pull %s due to %@."
+ "[Handoff][PullExpanse] Initiating task for pulling %s."
+ "[Handoff][PullExpanse] Successfully pulled %s."
+ "[Handoff][Push] Failed to push to %@ due to %@."
+ "[Handoff][Push] Starting push task with %@."
+ "[Handoff][Push] Successfully pushed %s."
+ "[JoinActiveConversation] Continuity session doesn't exist for %s"
+ "[JoinActiveConversation] Unable to join conversation with blocked handles %s"
+ "[JoinActiveConversation] requested to join conversation %s from %s"
+ "[PrepareForHandoff] Requesting laguna connection with %s."
+ "[PullConversationHandoff] End handoff"
+ "[StartConversation] Failed to start conversation on %@ due to %@."
+ "[StartConversation] Failed to start conversation with %s due to %@"
+ "[StartConversation] Initializing request to start conversation on %@."
+ "[StartConversation] Initiated task to start conversation with %s"
+ "[StartConversation] Rejecting request because no session exists for %s."
+ "[StartConversation] Rejecting start conversation request because trying to initiate a request with a blocked contact"
+ "[StartConversation] Successfully started conversation %s"
+ "[StartConversation] Successfully started conversation on %@."
+ "_TtC44com_apple_NeighborhoodActivityConduitService23ContinuitySessionServer"
+ "activeConversationWithUUID:"
+ "allowCallForDestinationID:providerIdentifier:"
+ "callEndedUIBlockAndReportEnabled"
+ "cameraSession"
+ "com.apple.language.changed"
+ "contactBlockAndReportEnabled"
+ "continuitySessionServer"
+ "faceTimeCallSpamReportAndBlockEnabled"
+ "ftAppDeletionEnabled"
+ "groupConversations"
+ "handoffState"
+ "invalid Collection: less than 'count' elements in collection"
+ "isFromBlockList"
+ "isRingingFaceTimeCallsOnConnectedTVDeviceSubject"
+ "lagunaLiveCaptionsEnabled"
+ "lvmExpansionLiveOnEnabled"
+ "noJoinedConversation"
+ "noSuggestionAvailable"
+ "silencedCallNotificationBlockAndReportEnabled"
+ "systemLanguageChanged"
+ "uninstalledAppStoreLockupEnabled"
- " deviceEffectiveIdentifier="
- "<HandoffInfo conversationUUID="
- "<LagunaInfo deviceEffectiveIdentifier="
- "Asked to create nearby device handle for unrecognized device %s"
- "Call with conversationID: %s active on phone while inSession but in allowedActiveConversationIDs:%s"
- "Cannot end laguna session while we don't have a session active."
- "Contact lookup by identifier failed with error %@"
- "Continuity camera connected. End any ongoing calls on iOS device"
- "Disconnect call %@"
- "Disconnected from %s with result %{bool}d"
- "Disconnecting continuity session because rapport and conduit session devices are mismatched: [%s and %s]"
- "ERROR: Unexpectedly have no session state while adding member."
- "Ending laguna session %s."
- "Ending laguna session because device is no longer reachable %s."
- "Failed to disconnect from %s with error %@"
- "Failed to fulfill get contact image request for %s due to %@."
- "Failed to fulfill get contacts request for %s due to %@."
- "Failed to started laguna session with %s due to %@."
- "Rejecting start laguna session reqeust because we already have an active session."
- "Reset suggestion"
- "Sending cancel result for %@"
- "Sending disconnect request for %s"
- "SessionState.expanse("
- "SessionState.laguna("
- "Skipping contact push because we're not handed off: %s"
- "[DeclineCall] Rejecting decline continuity call request because we're not in a continuity session with the device: %s"
- "[GetContacts] Received request for contacts info."
- "[GetContacts] Rejecting request to browse contacts from device with which we do not have a laguna session %s."
- "[GetContacts] Returning 0 contacts because we are not in a laguna session."
- "[HandoffConversation] Failed to establish laguna connection due to %@."
- "[HandoffConversation] Failed to hand off due to %@."
- "[HandoffConversation] No existing session; allowing handoff."
- "[HandoffConversation] Rejecting request because we already have a session active with a different device"
- "[HandoffConversation] Session already exists; rejecting handoff: %s"
- "[JoinActiveConversation] Rejecting join active conversation request because we're not in a continuity session with the device."
- "[PullConversationHandoff] End Laguna NAC Session"
- "[PullConversationHandoff] Request TV to disconnect when it sees phone upgrade"
- "[PullConversationHandoff] TV disconnected: %{bool}d"
- "[StartConversation] Rejecting request to start conversation from device with which we do not have a laguna session %s."
- "addParticipantRequest"
- "allowedActiveConversationIDs"
- "authenticate(_:)"
- "com.apple.ContinuityCaptureShieldUI"
- "com.apple.PineBoard"
- "com.apple.TVSettings"
- "com.apple.TVSystemMenuService"
- "com.apple.TVSystemUIService"
- "com.apple.mediaremoted"
- "com.apple.taptoradard"
- "deviceHandleRequest"
- "endingConversation"
- "endingLagunaSession"
- "isRingingFaceTimeCallsOnConnectedTVDevice changed to %{bool}d"
- "joinedActiveConversation"
- "joiningActiveConversation"
- "networkSupport"
- "receivedActiveConversationUpdate"
- "receivedContinuityCallsUpdate"
- "receivedEndLagunaSessionEvent"
- "receivedStartConversationEvent"
- "receivedStartLagunaSessionEvent"
- "removeObserver:"
- "resetConversationState %s on conversationUUID: %s"
- "sessionState"
- "sessionState changed \n from: %s \n to: %s \n with reason:%s"
- "startedConversation"
- "startedExpanseSession"
- "startedLagunaSession"
- "startingConversation"
- "startingExpanseSession"
- "startingLagunaSession"

```
