## continuitycaptured

> `/usr/libexec/continuitycaptured`

```diff

-587.122.6.0.2
-  __TEXT.__text: 0xdc7c
-  __TEXT.__auth_stubs: 0x660
-  __TEXT.__objc_stubs: 0x1680
-  __TEXT.__objc_methlist: 0x634
+650.0.0.122.4
+  __TEXT.__text: 0x100c8
+  __TEXT.__auth_stubs: 0x6a0
+  __TEXT.__objc_stubs: 0x1bc0
+  __TEXT.__objc_methlist: 0x81c
   __TEXT.__const: 0xc0
-  __TEXT.__gcc_except_tab: 0x880
-  __TEXT.__objc_methname: 0x17ea
-  __TEXT.__oslogstring: 0x1a93
-  __TEXT.__cstring: 0x1069
-  __TEXT.__objc_classname: 0x148
-  __TEXT.__objc_methtype: 0x4f2
-  __TEXT.__unwind_info: 0x3a8
-  __DATA_CONST.__auth_got: 0x340
-  __DATA_CONST.__got: 0x318
-  __DATA_CONST.__const: 0x658
-  __DATA_CONST.__cfstring: 0x280
+  __TEXT.__gcc_except_tab: 0x5d8
+  __TEXT.__objc_methname: 0x2011
+  __TEXT.__oslogstring: 0x2213
+  __TEXT.__cstring: 0x13d6
+  __TEXT.__objc_classname: 0x19f
+  __TEXT.__objc_methtype: 0x85a
+  __TEXT.__unwind_info: 0x418
+  __DATA_CONST.__auth_got: 0x360
+  __DATA_CONST.__got: 0x350
+  __DATA_CONST.__const: 0x838
+  __DATA_CONST.__cfstring: 0x340
   __DATA_CONST.__objc_classlist: 0x20
-  __DATA_CONST.__objc_protolist: 0x38
+  __DATA_CONST.__objc_protolist: 0x50
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_superrefs: 0x20
   __DATA_CONST.__objc_intobj: 0x90
-  __DATA.__objc_const: 0xa60
-  __DATA.__objc_selrefs: 0x6a0
-  __DATA.__objc_ivar: 0x9c
+  __DATA.__objc_const: 0xc48
+  __DATA.__objc_selrefs: 0x880
+  __DATA.__objc_ivar: 0xb8
   __DATA.__objc_data: 0x140
-  __DATA.__data: 0x2a0
+  __DATA.__data: 0x3c0
   __DATA.__bss: 0x20
   - /System/Library/Frameworks/AVFoundation.framework/AVFoundation
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/CoreMedia.framework/CoreMedia
+  - /System/Library/Frameworks/CoreServices.framework/CoreServices
   - /System/Library/Frameworks/Foundation.framework/Foundation
+  - /System/Library/Frameworks/MediaPlayer.framework/MediaPlayer
   - /System/Library/PrivateFrameworks/CMCapture.framework/CMCapture
   - /System/Library/PrivateFrameworks/CMContinuityCaptureCore.framework/CMContinuityCaptureCore
   - /System/Library/PrivateFrameworks/CoreUtils.framework/CoreUtils
   - /System/Library/PrivateFrameworks/FrontBoardServices.framework/FrontBoardServices
+  - /System/Library/PrivateFrameworks/MediaRemote.framework/MediaRemote
   - /System/Library/PrivateFrameworks/Rapport.framework/Rapport
   - /System/Library/PrivateFrameworks/RunningBoardServices.framework/RunningBoardServices
   - /System/Library/PrivateFrameworks/SpringBoardServices.framework/SpringBoardServices
   - /System/Library/PrivateFrameworks/SystemStatus.framework/SystemStatus
+  - /System/Library/PrivateFrameworks/iTunesCloud.framework/iTunesCloud
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 327EE44D-EA4A-3219-8FED-42282455E17B
-  Functions: 172
-  Symbols:   211
-  CStrings:  561
+  UUID: AF256AA9-6380-36BE-B611-D70C1246F048
+  Functions: 221
+  Symbols:   222
+  CStrings:  714
 
Symbols:
+ _MRGroupSessionJoinSessionWithToken
+ _MRGroupSessionLeaveSessionWithIdentifier
+ _OBJC_CLASS_$_CMContinuityCaptureParticipantInfo
+ _OBJC_CLASS_$_ICMediaUserStateCenter
+ _OBJC_CLASS_$_MPAVRoutingController
+ _OBJC_CLASS_$_MRGroupSessionDiscovery
+ _OBJC_CLASS_$_MRGroupSessionProvider
+ _OBJC_CLASS_$_MRGroupSessionToken
+ _OBJC_CLASS_$_MRUpdateActiveSystemEndpointRequest
+ _RPOptionSenderSessionPairingID
+ __os_feature_enabled_impl
+ _objc_enumerationMutation
+ _objc_opt_respondsToSelector
- ___stack_chk_fail
- ___stack_chk_guard
CStrings:
+ "%@ %s %@"
+ "%@ Could not find social profile for musicProfile: %@"
+ "%@ Leaving wrangler session with identifier %@"
+ "%@ active route did change: %@"
+ "%@ discovery active session did change: %@"
+ "%@ discovery session did change with discovered sessions: %@"
+ "%@ error leaving group session: %@"
+ "%@ group session %@ did invalidate with error: %@"
+ "%@ group session did connect: session %@"
+ "%@ group session: session %@ did update members %@"
+ "%@ group session: session %@ did update participants %@"
+ "%@ senderIdentifiers %{public}@ name %{public}@ model %d"
+ "%@ unable to get ICMediaUser activeUserState, reloading"
+ "%@://"
+ "%s paused: %d connectedRPDisplaySession %@ compositeDevice %@"
+ "%{public}@ %s %@ %@"
+ "%{public}@ %s skipPlacementStep:%d isDedicated:%d micOnly:%d identifier:%{public}@ name:%{public}@ model:%d activeSession:%{public}@"
+ "%{public}@ Activate pending connection %{public}@"
+ "%{public}@ Firing session clear out block"
+ "%{public}@ Launch shield ui event for %{public}@ skipPlacementStep %d isDedicated %d micOnly %d"
+ "%{public}@ Scheduling session to be cleared in %dsec. %{public}@"
+ "%{public}@ attempting to join group session with token: %@ requestID: %@"
+ "%{public}@ bootstrapping sing session from prox path; getting mediaRouteIdentifier from rapport device"
+ "%{public}@ failed to endpoint to: %@; error: %{public}@"
+ "%{public}@ failed to find rapport device for sing session endpoint"
+ "%{public}@ failed to get token for group session with url: %@"
+ "%{public}@ failed to join MRGroupSession with error: %{public}@ requestID: %@"
+ "%{public}@ found rapport device for sing media route endpoint: %@"
+ "%{public}@ got ICMediaUser activeUserState, retrying join"
+ "%{public}@ join group session request finished for a different request ID (requestID: %@, currentRequestID: %@) result identifier: %@ error: %@"
+ "%{public}@ successfully endpointed to mediaRouteIdentifier: %{public}@"
+ "%{public}@ successfully joined MRGroupSession: %{public}@ requestID: %@"
+ "%{public}@ terms not accepted for ICMediaUser activeUserState, bailing to Music"
+ "%{public}@ unable to get ICMediaUser activeUserState, reloading"
+ "%{public}@ unable to refresh ICMediaUser activeUserState, bailing to Music"
+ "%{public}@ unable to retrieve local participant info, present music error"
+ "%{public}@ updating local participant info to %@ with active session %@"
+ "-[CCDShieldUILifeCycleManager _forceTerminateShieldIfApplicableWithBundleID:completion:completionTimeoutInSec:]"
+ "-[CCDShieldUILifeCycleManager _forceTerminateShieldIfApplicableWithBundleID:completion:completionTimeoutInSec:]_block_invoke"
+ "-[CCDShieldUILifeCycleManager _launchShieldForDeviceIdentifier:name:model:skipPlacementStep:isDedicated:micOnly:statusHandler:]"
+ "-[CCDShieldUILifeCycleManager _launchShieldForDeviceIdentifier:name:model:skipPlacementStep:isDedicated:micOnly:statusHandler:]_block_invoke"
+ "-[CCDShieldUILifeCycleManager _setSystemStatusAttributionStatus:]"
+ "-[CCDShieldUILifeCycleManager launchShieldForDeviceIdentifier:name:model:skipPlacementStep:isDedicated:micOnly:statusHandler:]"
+ "-[CCDShieldUILifeCycleManager shieldDidConnect:]"
+ "-[CMContinuityCaptureDServer _fetchLocalParticipantInfo:]"
+ "-[CMContinuityCaptureDServer _joinGroupSessionWithURLString:]"
+ "-[CMContinuityCaptureDServer _launchShieldUIForDeviceIdentifier:name:model:skipPlacementStep:isDedicated:micOnly:]"
+ "-[CMContinuityCaptureDServer _launchShieldUIForDeviceIdentifier:name:model:skipPlacementStep:isDedicated:micOnly:]_block_invoke_2"
+ "-[CMContinuityCaptureDServer _teardownSingShieldUIIfNeeded]"
+ "-[CMContinuityCaptureDServer _updateLocalParticipantInfo]"
+ "-[CMContinuityCaptureDServer setupSingSessionFromURL:remoteDisplayIdentifier:]"
+ "-[CMContinuityCaptureDServer setupSingSessionWithMediaRouteIdentifier:remoteDisplayIdentifier:]"
+ "@\"<MRGroupSession>\""
+ "@\"CMContinuityCaptureParticipantInfo\""
+ "@\"MPAVRoutingController\""
+ "@\"MRGroupSessionDiscovery\""
+ "@\"NSUUID\""
+ "@64@0:8@16@24q32@40B48B52@?56"
+ "Active user state still nil after refresh"
+ "ContinuityCaptureShieldUILaunch"
+ "ContinuitySing"
+ "Error fetching user state: %@"
+ "Failed to launch %@ with error: %{public}@"
+ "MPAVRoutingControllerDelegate"
+ "MRGroupSessionDelegate"
+ "MRGroupSessionDiscoveryDelegate"
+ "Music"
+ "Successfully launched %@"
+ "UUID"
+ "_activeGroupSession"
+ "_avRoutingController"
+ "_endpointToMediaRemoteIdentifier:completion:"
+ "_fetchLocalParticipantInfo:"
+ "_forceTerminateShieldIfApplicableWithBundleID:completion:completionTimeoutInSec:"
+ "_groupSessionDiscovery"
+ "_groupSessionRequestUUID"
+ "_inLagunaSession"
+ "_joinGroupSessionRequestFinishedWithSessionIdentifier:requestID:error:"
+ "_joinGroupSessionWithURLString:"
+ "_launchShieldForDeviceIdentifier:name:model:skipPlacementStep:isDedicated:micOnly:statusHandler:"
+ "_launchShieldUIForDeviceIdentifier:name:model:skipPlacementStep:isDedicated:micOnly:"
+ "_localParticipantInfo"
+ "_setSystemStatusAttributionStatus:"
+ "_singSessionMediaRemoteIdentifier"
+ "_teardownSingShieldUIIfNeeded"
+ "_updateLocalParticipantInfo"
+ "absoluteString"
+ "activeDevices"
+ "activeUserState"
+ "allValues"
+ "attempting to endpoint to %@"
+ "atv_sing"
+ "atv_sing_quick_setup"
+ "com.apple.ContinuitySingShieldUI"
+ "compareWithDeviceIdentifier:"
+ "completed endpoint to %@ action with error %@"
+ "connect continuity sing"
+ "countByEnumeratingWithState:objects:count:"
+ "disconnect continuity sing"
+ "discoverySessionStartReason"
+ "displayNameAccepted"
+ "error"
+ "getActiveRouteWithCompletion:"
+ "groupSession:didChangeState:"
+ "groupSession:didInvalidateWithError:"
+ "groupSession:didUpdateMembers:"
+ "groupSession:didUpdateParticipants:"
+ "groupSession:didUpdatePendingParticipants:"
+ "groupSession:didUpdateSynchronizedMetadata:"
+ "groupSessionDidConnect:"
+ "groupSessionDiscovery:activeSessionDidChange:"
+ "groupSessionDiscovery:discoveredSessionsDidChange:"
+ "initWithDelegate:"
+ "initWithDeviceIdentifier:name:model:placementStepSkipped:isDedicated:micOnly:sessionInterruptionBlock:"
+ "initWithGroupSessionIdentifier:socialProfileIdentifier:displayName:"
+ "initWithMRParticipant:"
+ "initWithOutputDeviceUID:reason:"
+ "launchShieldForDeviceIdentifier:name:model:skipPlacementStep:isDedicated:micOnly:statusHandler:"
+ "launchShieldUIForDeviceIdentifier:name:model:skipPlacementStep:isDedicated:micOnly:"
+ "leaveWranglerIfActive"
+ "localParticipant"
+ "mediaRemoteIdentifier"
+ "mediaRouteIdentifier"
+ "micOnly"
+ "music"
+ "perform:completion:"
+ "presentShieldError:userInfo:"
+ "refreshUserStatesWithCompletion:"
+ "remoteControlGroupSessionWithIdentifier:delegate:"
+ "routeUID"
+ "routingController:didFailToPickRouteWithError:"
+ "routingController:pickedRouteDidChange:"
+ "routingController:pickedRoutesDidChange:"
+ "routingController:shouldHijackRoute:alertStyle:busyRouteName:presentingAppName:completion:"
+ "routingController:volumeControlAvailabilityDidChange:"
+ "routingControllerAvailableRoutesDidChange:"
+ "routingControllerDidPauseFromActiveRouteChange:"
+ "routingControllerExternalScreenTypeDidChange:"
+ "setMicOnly:"
+ "setParticipantInfo:"
+ "setRemoteDisplayIdentifier:"
+ "setupSingSessionFromURL:remoteDisplayIdentifier:"
+ "setupSingSessionWithMediaRouteIdentifier:remoteDisplayIdentifier:"
+ "shared"
+ "shieldDidConnect:"
+ "socialProfile"
+ "socialProfileID"
+ "tokenForJoinURLString:"
+ "userProfile"
+ "v16@?0@\"CMContinuityCaptureParticipantInfo\"8"
+ "v16@?0@\"MPAVRoute\"8"
+ "v16@?0@\"MRUpdateActiveSystemEndpointResponse\"8"
+ "v24@0:8@\"<MRGroupSession>\"16"
+ "v24@0:8@\"MPAVRoutingController\"16"
+ "v24@?0@\"NSArray\"8@\"NSError\"16"
+ "v24@?0@\"NSString\"8@\"NSError\"16"
+ "v28@0:8@\"MPAVRoutingController\"16B24"
+ "v28@0:8@16B24"
+ "v32@0:8@\"<MRGroupSession>\"16@\"NSData\"24"
+ "v32@0:8@\"<MRGroupSession>\"16@\"NSError\"24"
+ "v32@0:8@\"<MRGroupSession>\"16@\"NSSet\"24"
+ "v32@0:8@\"<MRGroupSession>\"16q24"
+ "v32@0:8@\"MPAVRoutingController\"16@\"MPAVRoute\"24"
+ "v32@0:8@\"MPAVRoutingController\"16@\"NSArray\"24"
+ "v32@0:8@\"MPAVRoutingController\"16@\"NSError\"24"
+ "v32@0:8@\"MRGroupSessionDiscovery\"16@\"MRGroupSessionInfo\"24"
+ "v32@0:8@\"MRGroupSessionDiscovery\"16@\"NSSet\"24"
+ "v32@0:8@\"NSString\"16@\"NSString\"24"
+ "v32@0:8@\"NSURL\"16@\"NSString\"24"
+ "v32@0:8@16@?24"
+ "v40@0:8@16@24@32"
+ "v40@0:8@16@?24Q32"
+ "v48@0:8{?=[8I]}16"
+ "v52@0:8@16@24q32B40B44B48"
+ "v60@0:8@16@24q32B40B44B48@?52"
+ "v64@0:8@\"MPAVRoutingController\"16@\"MPAVRoute\"24q32@\"NSString\"40@\"NSString\"48@?<v@?B>56"
+ "v64@0:8@16@24q32@40@48@?56"
- "%@ deviceIdentifier %{public}@ name %{public}@ model %d"
- "%s paused: %d"
- "%{public}@  Activate pending connection %{public}@"
- "%{public}@  Teardown timeout"
- "%{public}@ %s skipPlacementStep:%d isDedicated:%d identifier:%{public}@ name:%{public}@ model:%d activeSession:%{public}@"
- "%{public}@ Launch shield ui event for %{public}@ skipPlacementStep %d"
- "%{public}@ setup timeout for %{public}@"
- "-[CCDShieldUILifeCycleManager _forceTerminateShieldIfApplicable:completionTimeoutInSec:]"
- "-[CCDShieldUILifeCycleManager _forceTerminateShieldIfApplicable:completionTimeoutInSec:]_block_invoke"
- "-[CCDShieldUILifeCycleManager _launchShieldForDeviceIdentifier:name:model:skipPlacementStep:isDedicated:statusHandler:]"
- "-[CCDShieldUILifeCycleManager _launchShieldForDeviceIdentifier:name:model:skipPlacementStep:isDedicated:statusHandler:]_block_invoke"
- "-[CCDShieldUILifeCycleManager launchShieldForDeviceIdentifier:name:model:skipPlacementStep:isDedicated:statusHandler:]"
- "-[CCDShieldUILifeCycleManager shieldDidConnect]"
- "-[CMContinuityCaptureDServer _launchShieldUIForDeviceIdentifier:name:model:skipPlacementStep:isDedicated:]"
- "-[CMContinuityCaptureDServer _launchShieldUIForDeviceIdentifier:name:model:skipPlacementStep:isDedicated:]_block_invoke_2"
- "@60@0:8@16@24q32@40B48@?52"
- "ContinuityCaptureShieldUILaunch://"
- "Failed to launch ContinuityCaptureShieldUI with error: %{public}@"
- "Setting System Status attribution to com.apple.ContinuityCaptureShieldUI"
- "Successfully launched ContinuityCaptureShieldUI"
- "_forceTerminateShieldIfApplicable:completionTimeoutInSec:"
- "_launchShieldForDeviceIdentifier:name:model:skipPlacementStep:isDedicated:statusHandler:"
- "_launchShieldUIForDeviceIdentifier:name:model:skipPlacementStep:isDedicated:"
- "initWithDeviceIdentifier:name:model:placementStepSkipped:isDedicated:sessionInterruptionBlock:"
- "launchShieldForDeviceIdentifier:name:model:skipPlacementStep:isDedicated:statusHandler:"
- "launchShieldUIForDeviceIdentifier:name:model:skipPlacementStep:isDedicated:"
- "shieldDidConnect"
- "v32@0:8@?16Q24"
- "v48@0:8@16@24q32B40B44"
- "v56@0:8@16@24q32B40B44@?48"

```
