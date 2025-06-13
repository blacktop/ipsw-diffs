## com.apple.NeighborhoodActivityConduitService

> `/System/Library/PrivateFrameworks/NeighborhoodActivityConduit.framework/XPCServices/com.apple.NeighborhoodActivityConduitService.xpc/com.apple.NeighborhoodActivityConduitService`

```diff

-1431.200.71.2.11
-  __TEXT.__text: 0xd7de8
-  __TEXT.__auth_stubs: 0x24c0
-  __TEXT.__objc_methlist: 0x294
-  __TEXT.__objc_methname: 0x347b
-  __TEXT.__cstring: 0x6e6f
-  __TEXT.__swift5_typeref: 0x236e
+1431.300.81.2.2
+  __TEXT.__text: 0xe5dbc
+  __TEXT.__auth_stubs: 0x2700
+  __TEXT.__objc_methlist: 0x2f4
+  __TEXT.__objc_methname: 0x360c
+  __TEXT.__cstring: 0x749f
+  __TEXT.__swift5_typeref: 0x24ba
   __TEXT.__swift5_entry: 0x8
-  __TEXT.__const: 0x17ce
-  __TEXT.__constg_swiftt: 0x1564
+  __TEXT.__const: 0x183e
+  __TEXT.__constg_swiftt: 0x1574
   __TEXT.__swift5_builtin: 0x104
-  __TEXT.__swift5_reflstr: 0xf86
-  __TEXT.__swift5_fieldmd: 0xcdc
+  __TEXT.__swift5_reflstr: 0x1006
+  __TEXT.__swift5_fieldmd: 0xd18
   __TEXT.__swift5_assocty: 0x108
-  __TEXT.__swift5_proto: 0x10c
+  __TEXT.__swift5_proto: 0x114
   __TEXT.__swift5_types: 0xc8
   __TEXT.__objc_classname: 0x134
-  __TEXT.__objc_methtype: 0xba2
-  __TEXT.__swift5_capture: 0x19dc
+  __TEXT.__objc_methtype: 0xc11
+  __TEXT.__swift5_capture: 0x1b70
   __TEXT.__swift5_mpenum: 0x10
   __TEXT.__swift5_protos: 0x30
-  __TEXT.__unwind_info: 0x34e4
-  __TEXT.__eh_frame: 0xa258
-  __DATA_CONST.__auth_got: 0x1260
-  __DATA_CONST.__got: 0x6d8
-  __DATA_CONST.__auth_ptr: 0x78
-  __DATA_CONST.__const: 0x4f50
+  __TEXT.__unwind_info: 0x4354
+  __TEXT.__eh_frame: 0xae18
+  __DATA_CONST.__auth_got: 0x1380
+  __DATA_CONST.__got: 0x798
+  __DATA_CONST.__auth_ptr: 0x80
+  __DATA_CONST.__const: 0x5300
   __DATA_CONST.__objc_classlist: 0xa8
   __DATA_CONST.__objc_catlist: 0x10
   __DATA_CONST.__objc_protolist: 0x110
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA.__objc_const: 0x3cb8
-  __DATA.__objc_selrefs: 0x908
+  __DATA.__objc_const: 0x3e28
+  __DATA.__objc_selrefs: 0x978
   __DATA.__objc_protorefs: 0x98
-  __DATA.__objc_classrefs: 0x248
-  __DATA.__objc_data: 0xbd8
-  __DATA.__data: 0x37c0
-  __DATA.__bss: 0x1d10
+  __DATA.__objc_classrefs: 0x250
+  __DATA.__objc_data: 0xc00
+  __DATA.__data: 0x3968
+  __DATA.__bss: 0x1e10
   __DATA.__common: 0x108
   - /System/Library/Frameworks/Accounts.framework/Accounts
   - /System/Library/Frameworks/Combine.framework/Combine

   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  UUID: 13A4B0C5-BA8E-38A0-8A68-DB74A1B52516
-  Functions: 3291
-  Symbols:   309
-  CStrings:  1156
+  UUID: D95B33C2-7098-3511-B8D9-66B04219897B
+  Functions: 3454
+  Symbols:   312
+  CStrings:  1196
 
Symbols:
+ _CNContactImageDataAvailableKey
+ _OBJC_CLASS_$_FTDeviceSupport
+ _notify_post
CStrings:
+ "<NCProtoContinuityCall conversationUuidString="
+ "Conversation state changed to %s for %s."
+ "NeighborhoodActivityConduitClientsShouldConnectNotification"
+ "Reporting call ended for %s because it was started on TV (avMode=%s)."
+ "TUConversationAVModeAudio"
+ "TUConversationAVModeNone"
+ "TUConversationAVModeUnknown("
+ "TUConversationAVModeVideo"
+ "Vv20@0:8B16"
+ "[ContinuityCalls] Sending updated calls of count %ld"
+ "[DeclineCall] Rejecting decline continuity call request because we can't find the requested call: %s."
+ "[DeclineCall] Rejecting decline continuity call request because we're not in a continuity session with the device: %s"
+ "[DeclineCall] Successfully declined call (%s)."
+ "[HandoffConversation] Rejecting request because cannot find conversation with uuid: %s"
+ "[JoinActiveConversation] Ending existing conversation as we join another: %s"
+ "[JoinActiveConversation] Rejecting join active conversation request because we're already handing off."
+ "[PullConversationHandoff] Set SharePlay not handedOff"
+ "[StartConversation] Leaving conversation: %s"
+ "[StartConversation] Leaving conversationManager avLess continuity conversation: %s"
+ "[StartConversation] Received request to start conversation with mode %s."
+ "[StartConversation] Rejecting start conversation request because we cannot find a device for %@."
+ "[StartConversation] [InternalStatusError] Unable to find conversation after it was started."
+ "avLessConversation"
+ "availableConversationUpdateCancellable"
+ "callHistoryControllerWithCoalescingStrategy:options:shouldUpdateMetadataCache:"
+ "callStateForConversation(_:targetDeviceCapabilities:)"
+ "callUUID"
+ "callWithCallUUID:"
+ "civicBlurAvatarsEnabled"
+ "civicBlurPosterEnabled"
+ "com.apple.callservicesd.continuityCallsDidChange"
+ "com.apple.callservicesd.declineContinuityCall"
+ "com_apple_NeighborhoodActivityConduitService.NearbySuggestionController"
+ "currentAudioAndVideoCalls"
+ "deviceSupport"
+ "disconnectCall:withReason:"
+ "filtered candidate not capable of receiving audio calls:%@ classified:%s"
+ "imageDataAvailable"
+ "initWithAVLessCapable:lagunaCapable:audioCallCapable:"
+ "isAudioCallCapable"
+ "isContinuitySession"
+ "isGreenTea"
+ "isRingingFaceTimeCallsOnConnectedTVDevice changed to %{bool}d"
+ "isRingingFaceTimeCallsOnConnectedTVDeviceChanged:"
+ "isRingingFaceTimeCallsOnConnectedTVDeviceWithCompletion:"
+ "lagunaAudioCallsEnabled"
+ "maybeSendCallsChangedEvent()"
+ "mergedRemoteMembers"
+ "onRequestDeclineContinuityCall(_:sender:)"
+ "receivedContinuityCallsUpdate"
+ "reportRecentCallForConversation:withStartDate:avMode:"
+ "resolvedAudioVideoMode"
+ "setCallState(_:forGroupUUID:)"
+ "startConversationWith:on:completion:"
+ "v24@0:8@?<v@?B@\"NSError\">16"
+ "v40@0:8@\"NSSet\"16@\"TUNearbyDeviceHandle\"24@?<v@?@\"NSUUID\"@\"NSError\">32"
- "Reporting call ended for %s because it was started on TV."
- "Unable to find requested converastion %s"
- "[JoinActiveConversation] Rejecting join active conversation request because we're already handed off."
- "[StartConversation] Received request to start conversation."
- "activeConversationUpdateCancellablesByDeviceID"
- "callHistoryControllerWithCoalescingStrategy:options:"
- "callStateForConversationUUID(_:)"
- "handoffConversation(_:to:)"
- "initWithAVLessCapable:lagunaCapable:"
- "isOneToOneModeEnabled"
- "reportRecentCallForConversation:withStartDate:"
- "requestCurrentContext"
- "requestCurrentRecommendations"
- "requestCurrentRecommendations -- overriding for forced TV suggestion:%s"
- "setVideoEnabled:"
- "stringForKey:"

```
