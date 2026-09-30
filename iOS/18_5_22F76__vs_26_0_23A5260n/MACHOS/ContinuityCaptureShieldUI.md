## ContinuityCaptureShieldUI

> `/Applications/ContinuityCaptureShieldUI.app/ContinuityCaptureShieldUI`

```diff

-587.122.6.0.2
-  __TEXT.__text: 0xb58c
-  __TEXT.__auth_stubs: 0x480
-  __TEXT.__objc_stubs: 0x2820
-  __TEXT.__objc_methlist: 0x121c
+650.0.0.122.4
+  __TEXT.__text: 0x9a84
+  __TEXT.__auth_stubs: 0x450
+  __TEXT.__objc_stubs: 0x24c0
+  __TEXT.__objc_methlist: 0xdac
   __TEXT.__const: 0x78
-  __TEXT.__gcc_except_tab: 0x3a8
-  __TEXT.__objc_methname: 0x481e
-  __TEXT.__cstring: 0x174f
-  __TEXT.__objc_classname: 0x376
-  __TEXT.__objc_methtype: 0x162f
-  __TEXT.__oslogstring: 0xa77
-  __TEXT.__unwind_info: 0x340
-  __DATA_CONST.__auth_got: 0x250
-  __DATA_CONST.__got: 0x260
-  __DATA_CONST.__const: 0x428
-  __DATA_CONST.__cfstring: 0xaa0
+  __TEXT.__gcc_except_tab: 0x264
+  __TEXT.__objc_methname: 0x3352
+  __TEXT.__cstring: 0x16c1
+  __TEXT.__objc_classname: 0x313
+  __TEXT.__objc_methtype: 0x1031
+  __TEXT.__oslogstring: 0x946
+  __TEXT.__unwind_info: 0x2e8
+  __DATA_CONST.__auth_got: 0x238
+  __DATA_CONST.__got: 0x248
+  __DATA_CONST.__const: 0x3a8
+  __DATA_CONST.__cfstring: 0xa00
   __DATA_CONST.__objc_classlist: 0x70
-  __DATA_CONST.__objc_protolist: 0x50
+  __DATA_CONST.__objc_protolist: 0x38
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_superrefs: 0x48
-  __DATA.__objc_const: 0x19c0
-  __DATA.__objc_selrefs: 0x1078
-  __DATA.__objc_ivar: 0xcc
+  __DATA.__objc_const: 0x15a8
+  __DATA.__objc_selrefs: 0xd78
+  __DATA.__objc_ivar: 0xb0
   __DATA.__objc_data: 0x460
-  __DATA.__data: 0x3c0
-  __DATA.__bss: 0x40
+  __DATA.__data: 0x2a0
+  __DATA.__bss: 0x30
   - /System/Library/Frameworks/AVFoundation.framework/AVFoundation
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/CoreMedia.framework/CoreMedia
   - /System/Library/Frameworks/CoreServices.framework/CoreServices
   - /System/Library/Frameworks/Foundation.framework/Foundation
+  - /System/Library/Frameworks/MediaPlayer.framework/MediaPlayer
   - /System/Library/Frameworks/QuartzCore.framework/QuartzCore
   - /System/Library/Frameworks/UIKit.framework/UIKit
   - /System/Library/PrivateFrameworks/BaseBoard.framework/BaseBoard
   - /System/Library/PrivateFrameworks/CMCapture.framework/CMCapture
   - /System/Library/PrivateFrameworks/CMContinuityCaptureCore.framework/CMContinuityCaptureCore
+  - /System/Library/PrivateFrameworks/ContinuitySing.framework/ContinuitySing
   - /System/Library/PrivateFrameworks/FrontBoardServices.framework/FrontBoardServices
   - /System/Library/PrivateFrameworks/RunningBoardServices.framework/RunningBoardServices
   - /System/Library/PrivateFrameworks/SpringBoardServices.framework/SpringBoardServices

   - /System/Library/PrivateFrameworks/TelephonyUtilities.framework/TelephonyUtilities
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 3306E2F7-3091-34E6-A2BD-8BC6AFDA05AB
-  Functions: 226
-  Symbols:   163
-  CStrings:  1084
+  UUID: E6F9A583-CB45-3E37-B980-AA175691C728
+  Functions: 204
+  Symbols:   157
+  CStrings:  933
 
Symbols:
+ _CMContinuityCaptureUIStateTrackerActiveConfigurationKVOKey
+ _CMContinuityCaptureUIStateTrackerActiveFaceTimeContinuitySessionKVOKey
+ _CMContinuityCaptureUIStateTrackerActiveKVOKey
+ _OBJC_CLASS_$_CMContinuityCaptureUIStateTracker
+ _objc_retain_x4
- _OBJC_CLASS_$_NSThread
- _OBJC_CLASS_$_RBSAssertion
- _OBJC_CLASS_$_RBSDomainAttribute
- _OBJC_CLASS_$_RBSProcessIdentifier
- _OBJC_CLASS_$_RBSTarget
- ___kCFBooleanFalse
- ___stack_chk_fail
- ___stack_chk_guard
- _objc_retain
- _objc_sync_enter
- _objc_sync_exit
CStrings:
+ "+[ContinuityCaptureShieldUIBaseViewController _refreshConnectionType]"
+ "+[ContinuityCaptureShieldUIBaseViewController _refreshUIState]"
+ "-[ContinuityCaptureShieldUIBaseSceneDelegate scene:willConnectToSession:options:]"
+ "-[ContinuityCaptureShieldUIBaseViewController dealloc]"
+ "-[ContinuityCaptureShieldUIBaseViewController disconnectSession]"
+ "-[ContinuityCaptureShieldUIBaseViewController disconnectSession]_block_invoke"
+ "-[ContinuityCaptureShieldUIBaseViewController initWithSceneSessionRole:]"
+ "-[ContinuityCaptureShieldUIBaseViewController observeValueForKeyPath:ofObject:change:context:]_block_invoke"
+ "-[ContinuityCaptureShieldUIBaseViewController tearDownShield]"
+ "-[ContinuityCaptureShieldUIBaseViewController tearDownShield]_block_invoke"
+ "-[ContinuityCaptureShieldUIBaseViewController viewDidAppear:]"
+ "-[ContinuityCaptureShieldUIBaseViewController viewDidDisappear:]"
+ "-[ContinuityCaptureShieldUIBaseViewController viewWillAppear:]"
+ "-[ContinuityCaptureShieldUIBaseViewController viewWillDisappear:]"
+ "-[ContinuityCaptureShieldUIViewController tearDownShield]"
+ "-[ContinuityCaptureShieldUIViewController updateUI]"
+ "@\"UISceneWindowingControlStyle\"24@0:8@\"UIWindowScene\"16"
+ "ContinuityCaptureShieldUIBaseViewController"
+ "TB,R,N,GisOnLockScreen"
+ "TB,R,N,GisTerminated,V_terminated"
+ "Tq,N,V_disconnectReason"
+ "com.apple.systemstatus.background-activity.continuitycapture.mic-only"
+ "createWindowForScene:"
+ "disconnectReason"
+ "isOnLockScreen"
+ "isTerminated"
+ "onLockScreen"
+ "preferredWindowingControlStyleForScene:"
+ "setDisconnectReason:"
+ "terminated"
+ "updateState:micOnly:"
+ "updateState:micOnly:withUserInteractionHandler:"
+ "updateUI"
+ "v28@0:8q16B24"
+ "v32@0:8@\"UIWindowScene\"16@\"UIWindowSceneGeometry\"24"
+ "v36@0:8q16B24@?28"
+ "windowScene:didUpdateEffectiveGeometry:"
- "%s: %@ Failed to acquire app suspend assertion with error %@"
- "%s: %@ Successfully acquired app suspend assertion"
- "%s: %@ activeConfiguration change (%{public}@ -> %{public}@)"
- "%s: %@ activeConfiguration should not be set to nil, returning"
- "%s: %@ activeConfiguration shouldn't be nil"
- "%s: %@ teardown shieldUI"
- "+[ContinuityCaptureShieldUIViewController _refreshConnectionType]"
- "+[ContinuityCaptureShieldUIViewController _refreshUIState]"
- "-[CMContinuityCaptureUIStateTracker _aquireAppSuspendAssertion]"
- "-[CMContinuityCaptureUIStateTracker _sessionDidUpdateWithConfiguration:]"
- "-[CMContinuityCaptureUIStateTracker activeConfiguration]"
- "-[CMContinuityCaptureUIStateTracker tearDownShield]"
- "-[ContinuityCaptureShieldUISecureSceneDelegate scene:willConnectToSession:options:]"
- "-[ContinuityCaptureShieldUIViewController _disconnectSession]"
- "-[ContinuityCaptureShieldUIViewController _disconnectSession]_block_invoke"
- "-[ContinuityCaptureShieldUIViewController _tearDownShield]"
- "-[ContinuityCaptureShieldUIViewController _tearDownShield]_block_invoke"
- "-[ContinuityCaptureShieldUIViewController _updateUI]"
- "-[ContinuityCaptureShieldUIViewController dealloc]"
- "-[ContinuityCaptureShieldUIViewController initWithSceneSessionRole:]"
- "-[ContinuityCaptureShieldUIViewController observeValueForKeyPath:ofObject:change:context:]_block_invoke"
- "-[ContinuityCaptureShieldUIViewController viewDidAppear:]"
- "-[ContinuityCaptureShieldUIViewController viewDidDisappear:]"
- "-[ContinuityCaptureShieldUIViewController viewWillAppear:]"
- "-[ContinuityCaptureShieldUIViewController viewWillDisappear:]"
- "@\"CMContinuityCaptureUIConfiguration\""
- "@\"NSObject<OS_dispatch_queue>\""
- "@\"RBSAssertion\""
- "CMContinuityCaptureUIStateTracker"
- "CMContinuityCaptureXPCServerActionCCD"
- "DoCapture"
- "Shield Terminate XPC"
- "T@\"CMContinuityCaptureUIConfiguration\",R,&"
- "TB,R"
- "TB,R,N,GisDedicatedSession"
- "TB,R,N,GisInFaceTime"
- "TUConversationManagerDelegate"
- "TUNeighborhoodActivityConduitDelegate"
- "Tq,N"
- "_active"
- "_activeConfiguration"
- "_appSuspendAssertion"
- "_aquireAppSuspendAssertion"
- "_connectionType"
- "_disconnectSession"
- "_inFaceTime"
- "_isOnLockScreen"
- "_queue"
- "_refreshInFaceTime"
- "_releaseAppSuspendAssertion"
- "_sessionDidUpdateWithConfiguration:"
- "_uiState"
- "_updateUI"
- "acquireWithError:"
- "active"
- "addDelegate:queue:"
- "applicationIdentifier"
- "attributeWithDomain:name:"
- "avMode"
- "canPullBackConversation:"
- "connectToContinuityCaptureServerWithDelegate:"
- "conversationManager:activeRemoteParticipantsChangedForConversation:"
- "conversationManager:activeRemoteParticipantsChangedForConversation:fromOldConversation:"
- "conversationManager:activitySessionsChangedForConversation:"
- "conversationManager:activitySessionsChangedForConversation:fromOldConversation:"
- "conversationManager:addedActiveConversation:"
- "conversationManager:avModeChangedForConversation:"
- "conversationManager:avModeChangedForConversation:fromOldConversation:"
- "conversationManager:cameraMixedWithScreenDidChangeForConversation:"
- "conversationManager:cameraMixedWithScreenDidChangeForConversation:fromOldConversation:"
- "conversationManager:changedActivityAuthorizationForBundleIdentifier:"
- "conversationManager:collaborationChanged:forConversation:collaborationState:"
- "conversationManager:conversation:addedMembersLocally:"
- "conversationManager:conversation:buzzedMember:"
- "conversationManager:conversation:didChangeSceneAssociationForActivitySession:"
- "conversationManager:conversation:didChangeStateForActivitySession:"
- "conversationManager:conversation:launchStateChanged:forActivitySession:"
- "conversationManager:conversation:participant:addedCollaborationNotice:"
- "conversationManager:conversation:participant:addedNotice:"
- "conversationManager:conversation:receivedActivitySessionEvent:"
- "conversationManager:conversation:requestedScreenShareForParticipant:"
- "conversationManager:conversation:screenSharingChangedForParticipant:"
- "conversationManager:conversation:updatedMessagesGroupPhoto:"
- "conversationManager:conversationUpdatedMessagesGroupName:"
- "conversationManager:conversationUpdatedMessagesGroupName:fromOldConversation:"
- "conversationManager:conversationUpdatedMessagesGroupUUID:"
- "conversationManager:didChangeActivatedLinks:"
- "conversationManager:handoffEligibilityChangedForConversation:"
- "conversationManager:handoffEligibilityChangedToConversation:fromPreviousConversation:"
- "conversationManager:ignoreLMIRequestsChangedForConversation:"
- "conversationManager:kickedMembersChangedForConversation:"
- "conversationManager:kickedMembersChangedForConversation:fromOldConversation:"
- "conversationManager:letMeInRequestStateChangedForConversation:"
- "conversationManager:letMeInRequestStateChangedForConversation:fromOldConversation:"
- "conversationManager:linkChangedForConversation:"
- "conversationManager:linkChangedForConversation:fromOldConversation:"
- "conversationManager:linkInvitedMemberHandlesChangedForConversation:"
- "conversationManager:linkInvitedMemberHandlesChangedForConversation:fromOldConversation:"
- "conversationManager:localVideoToggledForConversation:"
- "conversationManager:localVideoToggledForConversation:fromOldConversation:"
- "conversationManager:migratingFromConversation:toConversation:"
- "conversationManager:oneToOneModeChangedForConversation:"
- "conversationManager:oneToOneModeChangedForConversation:fromOldConversation:"
- "conversationManager:otherInvitedHandlesChangedForConversation:"
- "conversationManager:otherInvitedHandlesChangedForConversation:fromOldConversation:"
- "conversationManager:pendingMembersChangedForConversation:"
- "conversationManager:pendingMembersChangedForConversation:fromOldConversation:"
- "conversationManager:presentationContextChangedForConversation:"
- "conversationManager:presentationContextChangedForConversation:fromOldConversation:"
- "conversationManager:rejectedMembersChangedForConversation:"
- "conversationManager:rejectedMembersChangedForConversation:fromOldConversation:"
- "conversationManager:remoteMembersChangedForConversation:"
- "conversationManager:remoteMembersChangedForConversation:fromOldConversation:"
- "conversationManager:remoteScreenShareAttributesChanged:isLocallySharing:"
- "conversationManager:remoteScreenShareEndedWithReason:"
- "conversationManager:removedActiveConversation:"
- "conversationManager:resolvedAudioVideoModeChangedForConversation:"
- "conversationManager:resolvedAudioVideoModeChangedForConversation:fromOldConversation:"
- "conversationManager:screenSharingAvailableChanged:"
- "conversationManager:screenSharingRequestsChangedForConversation:fromOldConversation:"
- "conversationManager:screeningChangedForConversation:"
- "conversationManager:sharePlayAvailableChanged:"
- "conversationManager:stateChangedForConversation:"
- "conversationManager:stateChangedForConversation:fromOldConversation:"
- "conversationManager:systemActivitySessionsChangedForConversation:"
- "conversationManager:systemActivitySessionsChangedForConversation:fromOldConversation:"
- "conversationManager:trackedPendingMember:forConversationLink:"
- "conversationManager:updatedIncomingPendingConversations:"
- "conversationsChangedForConversationManager:"
- "dedicatedSession"
- "didChangeValueForKey:"
- "identifierForCurrentProcess"
- "inFaceTime"
- "initWithExplanation:target:attributes:"
- "isDedicated"
- "isMainThread"
- "neighborhoodActivityConduit:splitSessionEnded:"
- "neighborhoodActivityConduit:splitSessionStarted:"
- "neighborhoodActivityConduit:suggestionUpdated:"
- "neighborhoodActivityConduit:tvDeviceAppeared:"
- "neighborhoodActivityConduit:tvDeviceDisappeared:"
- "pid"
- "removeDelegate:"
- "serverDisconnectedForConversationManager:"
- "serverXPCConnectionInterrupted"
- "sessionDidUpdateWithConfiguration:"
- "setApplicationIdentifier:"
- "setClientDeviceModel:"
- "setClientName:"
- "setCompositeState:"
- "setIsDedicated:"
- "setPlacementStepSkipped:"
- "targetWithPid:"
- "v24@0:8@\"CMContinuityCaptureUIConfiguration\"16"
- "v24@0:8@\"TUConversationManager\"16"
- "v28@0:8@\"TUConversationManager\"16B24"
- "v28@0:8@16B24"
- "v32@0:8@\"TUConversationManager\"16@\"NSArray\"24"
- "v32@0:8@\"TUConversationManager\"16@\"NSError\"24"
- "v32@0:8@\"TUConversationManager\"16@\"NSString\"24"
- "v32@0:8@\"TUConversationManager\"16@\"TUConversation\"24"
- "v32@0:8@\"TUNeighborhoodActivityConduit\"16@\"TUNearbyDeviceHandle\"24"
- "v32@0:8@\"TUNeighborhoodActivityConduit\"16@\"TUNearbySuggestion\"24"
- "v36@0:8@\"TUConversationManager\"16@\"<TUScreenShareAttributes>\"24B32"
- "v40@0:8@\"TUConversationManager\"16@\"TUConversation\"24@\"NSData\"32"
- "v40@0:8@\"TUConversationManager\"16@\"TUConversation\"24@\"NSSet\"32"
- "v40@0:8@\"TUConversationManager\"16@\"TUConversation\"24@\"TUConversation\"32"
- "v40@0:8@\"TUConversationManager\"16@\"TUConversation\"24@\"TUConversationActivityEvent\"32"
- "v40@0:8@\"TUConversationManager\"16@\"TUConversation\"24@\"TUConversationActivitySession\"32"
- "v40@0:8@\"TUConversationManager\"16@\"TUConversation\"24@\"TUConversationMember\"32"
- "v40@0:8@\"TUConversationManager\"16@\"TUConversation\"24@\"TUConversationParticipant\"32"
- "v40@0:8@\"TUConversationManager\"16@\"TUConversationMember\"24@\"TUConversationLink\"32"
- "v48@0:8@\"TUConversationManager\"16@\"SWCollaborationHighlight\"24@\"TUConversation\"32q40"
- "v48@0:8@\"TUConversationManager\"16@\"TUConversation\"24@\"TUConversationParticipant\"32@\"TUCollaborationNotice\"40"
- "v48@0:8@\"TUConversationManager\"16@\"TUConversation\"24@\"TUConversationParticipant\"32@\"TUConversationNotice\"40"
- "v48@0:8@\"TUConversationManager\"16@\"TUConversation\"24Q32@\"TUConversationActivitySession\"40"
- "v48@0:8@16@24@32@40"
- "v48@0:8@16@24@32q40"
- "v48@0:8@16@24Q32@40"
- "willChangeValueForKey:"

```
