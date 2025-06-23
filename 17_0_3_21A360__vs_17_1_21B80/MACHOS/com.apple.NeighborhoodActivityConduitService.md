## com.apple.NeighborhoodActivityConduitService

> `/System/Library/PrivateFrameworks/NeighborhoodActivityConduit.framework/XPCServices/com.apple.NeighborhoodActivityConduitService.xpc/com.apple.NeighborhoodActivityConduitService`

```diff

-1431.100.4.2.39
-  __TEXT.__text: 0xcb77c
-  __TEXT.__auth_stubs: 0x2330
-  __TEXT.__objc_methlist: 0x28c
-  __TEXT.__cstring: 0x674f
-  __TEXT.__objc_methname: 0x3397
-  __TEXT.__swift5_typeref: 0x22ce
+1431.200.71.2.11
+  __TEXT.__text: 0xd7de8
+  __TEXT.__auth_stubs: 0x24c0
+  __TEXT.__objc_methlist: 0x294
+  __TEXT.__objc_methname: 0x347b
+  __TEXT.__cstring: 0x6e6f
+  __TEXT.__swift5_typeref: 0x236e
   __TEXT.__swift5_entry: 0x8
-  __TEXT.__const: 0x178e
-  __TEXT.__constg_swiftt: 0x1534
+  __TEXT.__const: 0x17ce
+  __TEXT.__constg_swiftt: 0x1564
   __TEXT.__swift5_builtin: 0x104
-  __TEXT.__swift5_reflstr: 0xf26
-  __TEXT.__swift5_fieldmd: 0xcac
+  __TEXT.__swift5_reflstr: 0xf86
+  __TEXT.__swift5_fieldmd: 0xcdc
   __TEXT.__swift5_assocty: 0x108
-  __TEXT.__swift5_proto: 0x108
+  __TEXT.__swift5_proto: 0x10c
   __TEXT.__swift5_types: 0xc8
   __TEXT.__objc_classname: 0x134
   __TEXT.__objc_methtype: 0xba2
-  __TEXT.__swift5_capture: 0x18cc
+  __TEXT.__swift5_capture: 0x19dc
   __TEXT.__swift5_mpenum: 0x10
   __TEXT.__swift5_protos: 0x30
-  __TEXT.__unwind_info: 0x39f0
-  __TEXT.__eh_frame: 0x9950
-  __DATA_CONST.__auth_got: 0x1198
-  __DATA_CONST.__got: 0x690
-  __DATA_CONST.__auth_ptr: 0x70
-  __DATA_CONST.__const: 0x4d08
+  __TEXT.__unwind_info: 0x34e4
+  __TEXT.__eh_frame: 0xa258
+  __DATA_CONST.__auth_got: 0x1260
+  __DATA_CONST.__got: 0x6d8
+  __DATA_CONST.__auth_ptr: 0x78
+  __DATA_CONST.__const: 0x4f50
   __DATA_CONST.__objc_classlist: 0xa8
   __DATA_CONST.__objc_catlist: 0x10
   __DATA_CONST.__objc_protolist: 0x110
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA.__objc_const: 0x3bd8
-  __DATA.__objc_selrefs: 0x8c0
+  __DATA.__objc_const: 0x3cb8
+  __DATA.__objc_selrefs: 0x908
   __DATA.__objc_protorefs: 0x98
-  __DATA.__objc_classrefs: 0x240
+  __DATA.__objc_classrefs: 0x248
   __DATA.__objc_data: 0xbd8
-  __DATA.__data: 0x3678
-  __DATA.__common: 0x118
-  __DATA.__bss: 0x1c90
+  __DATA.__data: 0x37c0
+  __DATA.__bss: 0x1d10
+  __DATA.__common: 0x108
   - /System/Library/Frameworks/Accounts.framework/Accounts
   - /System/Library/Frameworks/Combine.framework/Combine
   - /System/Library/Frameworks/Contacts.framework/Contacts

   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  UUID: 7B083C0C-3CD7-3223-8B42-FBEB1495476E
-  Functions: 3151
-  Symbols:   308
-  CStrings:  1118
+  UUID: 13A4B0C5-BA8E-38A0-8A68-DB74A1B52516
+  Functions: 3291
+  Symbols:   309
+  CStrings:  1156
 
Symbols:
+ _OBJC_CLASS_$_TUNeighborhoodActivityConduit
CStrings:
+ "CallState retrieved for associated TV with %s with result %s"
+ "Cannot sendSuggestionAdvertisementDidChangeEvent to deviceHandle without idsDeviceIdentifier"
+ "Continuity camera connected. End any ongoing calls on iOS device"
+ "Created IR candidate:%@ for idsIdentifier:%s with idsDeviceIdentifier:%s"
+ "Disconnect call %@"
+ "Failed to retrieve CallState for associated TV for %s with error %@"
+ "Informing IR to update idsIdentifiers: %s"
+ "NCProtoCallState("
+ "Rejecting start laguna session request because we're not currently connected via remote display discovery."
+ "Sending callState request for %s"
+ "[%s] Creating connection assertion (forceAWDL=%{bool}d)."
+ "[JoinActiveConversation] Attempting to join conversation %s."
+ "[JoinActiveConversation] Conversation joined, attempting to handoff..."
+ "[JoinActiveConversation] Handoff succeeded, returning success"
+ "[JoinActiveConversation] Join active conversation failed due to %@"
+ "[JoinActiveConversation] Rejecting join active conversation request because we're already handed off."
+ "[JoinActiveConversation] Rejecting join active conversation request because we're not in a continuity session with the device."
+ "[JoinActiveConversation] Unable to find conversation for %s"
+ "[PullConversationHandoff] End Laguna NAC Session"
+ "[PullConversationHandoff] Exit Laguna Rapport Session"
+ "[PullConversationHandoff] Request TV to disconnect when it sees phone upgrade"
+ "[PullConversationHandoff] Setting callState to match TV callState: %s"
+ "[PullConversationHandoff] TV disconnected: %{bool}d"
+ "boolForKey:"
+ "com.apple.callservicesd.activeConversationsDidChange"
+ "com.apple.callservicesd.callState"
+ "com.apple.callservicesd.joinActiveConversation"
+ "controlFlags"
+ "disconnectCall:"
+ "displayName"
+ "endCurrentCall executed but no frontmostAudioOrVideoCall to end"
+ "faceTimeCallSpamReportEnabled"
+ "faceTimeGroupCallSpamReportEnabled"
+ "filtered candidate but suggesting for onboarding:%@ classified:%s"
+ "idsIdentifier"
+ "initWithAVLessCapable:lagunaCapable:"
+ "initWithConversation:"
+ "isAvailableOverBLE"
+ "isConduitAvailable"
+ "joinedActiveConversation"
+ "joiningActiveConversation"
+ "lagunaIncomingCallsEnabled"
+ "receivedActiveConversationUpdate"
+ "resetConversationState %s on conversationUUID: %s"
+ "statusFlags"
+ "videoMessagingSpamReportEnabled"
- "Cannot sendSuggestionAdvertisementDidChangeEvent to deviceHandle without effectiveIdentifier"
- "Created IR candidate:%@ for rapportID:%s with idsDeviceIdentifier:%s"
- "Informing IR to update rapportIDs: %s"
- "[%s] Creating connection assertion."
- "[PullConversationHandoff] End Handoff"
- "[PullConversationHandoff] Exit Laguna Session"
- "initWithSourceVersion:modelString:"
- "rapportIdentifier"

```
