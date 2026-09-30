## MediaRemote

> `/System/Library/PrivateFrameworks/MediaRemote.framework/MediaRemote`

```diff

-4024.310.19.2.0
-  __TEXT.__text: 0x2c20a8
+4024.310.30.1.0
+  __TEXT.__text: 0x2bc538
   __TEXT.__auth_stubs: 0x1650
-  __TEXT.__objc_methlist: 0x27ca4
-  __TEXT.__const: 0x558
-  __TEXT.__cstring: 0x2af7a
-  __TEXT.__oslogstring: 0xd003
-  __TEXT.__gcc_except_tab: 0x629c
+  __TEXT.__objc_methlist: 0x27e24
+  __TEXT.__const: 0x568
+  __TEXT.__cstring: 0x2a62d
+  __TEXT.__oslogstring: 0xce41
+  __TEXT.__gcc_except_tab: 0x6308
   __TEXT.__ustring: 0x12
-  __TEXT.__unwind_info: 0xa940
-  __TEXT.__objc_classname: 0x4a0a
-  __TEXT.__objc_methname: 0x4827b
-  __TEXT.__objc_methtype: 0x8a03
-  __TEXT.__objc_stubs: 0x25b40
-  __DATA_CONST.__got: 0x1268
-  __DATA_CONST.__const: 0xa4e0
+  __TEXT.__unwind_info: 0xa7a0
+  __TEXT.__objc_classname: 0x4a09
+  __TEXT.__objc_methname: 0x4861c
+  __TEXT.__objc_methtype: 0x8a73
+  __TEXT.__objc_stubs: 0x25e60
+  __DATA_CONST.__got: 0x1270
+  __DATA_CONST.__const: 0xa2e8
   __DATA_CONST.__objc_classlist: 0x1110
   __DATA_CONST.__objc_catlist: 0x60
   __DATA_CONST.__objc_protolist: 0x230
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0xddb0
+  __DATA_CONST.__objc_selrefs: 0xde40
   __DATA_CONST.__objc_protorefs: 0x88
   __DATA_CONST.__objc_superrefs: 0xf58
   __DATA_CONST.__objc_arraydata: 0x228
   __AUTH_CONST.__auth_got: 0xb38
   __AUTH_CONST.__auth_ptr: 0x8
-  __AUTH_CONST.__const: 0x32a0
-  __AUTH_CONST.__cfstring: 0x20400
-  __AUTH_CONST.__objc_const: 0x44ee0
+  __AUTH_CONST.__const: 0x3080
+  __AUTH_CONST.__cfstring: 0x202e0
+  __AUTH_CONST.__objc_const: 0x45158
   __AUTH_CONST.__objc_intobj: 0x4c8
   __AUTH_CONST.__objc_arrayobj: 0x150
   __AUTH_CONST.__objc_dictobj: 0x50
   __AUTH_CONST.__objc_doubleobj: 0x10
   __AUTH.__objc_data: 0x7850
-  __AUTH.__data: 0x1a0
-  __DATA.__objc_ivar: 0x2fd8
+  __AUTH.__data: 0x108
+  __DATA.__objc_ivar: 0x3000
   __DATA.__data: 0x1a88
-  __DATA.__bss: 0x8f8
+  __DATA.__bss: 0x878
   __DATA.__common: 0x8
   __DATA_DIRTY.__objc_data: 0x3250
-  __DATA_DIRTY.__data: 0x220
-  __DATA_DIRTY.__bss: 0x6d8
+  __DATA_DIRTY.__data: 0x228
+  __DATA_DIRTY.__bss: 0x6d0
   - /System/Library/Frameworks/AudioToolbox.framework/AudioToolbox
   - /System/Library/Frameworks/CFNetwork.framework/CFNetwork
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation

   - /usr/lib/libMobileGestalt.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 18893
-  Symbols:   22469
-  CStrings:  18946
+  Functions: 18826
+  Symbols:   22409
+  CStrings:  18949
 
Symbols:
+ OBJC_IVAR_$__MRGroupTopologyModificationRequestProtobuf._shouldClearPredictedRoutes
+ OBJC_IVAR_$__MRRequestDetailsProtobuf._initiator
+ OBJC_IVAR_$__MRRequestDetailsProtobuf._initiatorWasInferred
+ OBJC_IVAR_$__MRRequestDetailsProtobuf._originatingBundleID
+ _MRAVOutputContextModificationRequestToClearPredictedRoutesNotifications
+ _MRCreateRequestDetailsFromXPCMessage
+ _MRRequestDetailsInitiatorAccessory
+ _MRRequestDetailsInitiatorAirPlay
+ _MRRequestDetailsInitiatorAlarm
+ _MRRequestDetailsInitiatorAutomation
+ _MRRequestDetailsInitiatorBanner
+ _MRRequestDetailsInitiatorInfer
+ _MRRequestDetailsInitiatorShortcut
- OBJC_IVAR_$__MRRequestDetailsProtobuf._name
CStrings:
+ "\x01\x14\x13"
+ "\x03$"
+ "\x12\x12"
+ "<%!@(MISSING):%!p(MISSING)/initiator=%!@(MISSING)/bundleID=%!@(MISSING)/reason=%!@(MISSING)/ui=%!u(MISSING)/qos=%!u(MISSING)/i=%!u(MISSING)>"
+ "@52@0:8@16@24@32B40@44"
+ "ActiveUserTimeoutInterval"
+ "AirPlayClientNotAvailable"
+ "Alarm"
+ "Automation"
+ "Banner"
+ "ElectedPlayerInterval"
+ "Infer"
+ "MRAVOutputContextModificationRequestToClearPredictedRoutesNotifications"
+ "Shortcut"
+ "T@\"NSString\",&,N,V_originatingBundleID"
+ "T@\"NSString\",R,N,V_originatingBundleID"
+ "TB,N,V_hasClusterType"
+ "TB,N,V_hasConfiguredClusterSize"
+ "TB,N,V_hasIsClusterAware"
+ "TB,N,V_hasIsClusterLeader"
+ "TB,N,V_hasLastSupportedClusterType"
+ "TB,N,V_hasLastSupportedProtocolMessageType"
+ "TB,N,V_hasSupportsOutputContextSync"
+ "TB,N,V_initiatorWasInferred"
+ "TB,N,V_shouldClearPredictedRoutes"
+ "TB,R,N,V_initiatorWasInferred"
+ "TI,N,V_lastSupportedClusterType"
+ "[AVDiscoverySession] Dispatching to reloadQueue took %!l(MISSING)f seconds"
+ "[AVDiscoverySession] Querying AVDiscoverySession time took %!l(MISSING)f seconds"
+ "[AVDiscoverySession] ReloadQueue priority degrated from %!u(MISSING) -> %!u(MISSING)"
+ "[MRNowPlayingPlayerClientRequests] %!{(MISSING)public}@ UpdatingCache: clearing contentItemArtwork for %!@(MISSING)"
+ "[MRNowPlayingPlayerClientRequests] %!{(MISSING)public}@ UpdatingCache: clearing formatted data artworks for %!@(MISSING)"
+ "[MRNowPlayingPlayerClientRequests] %!{(MISSING)public}@ UpdatingCache: clearing formatted remote artworks for %!@(MISSING)"
+ "[MRNowPlayingPlayerClientRequests] %!{(MISSING)public}@ UpdatingCache: contentItem %!@(MISSING)"
+ "[MRNowPlayingPlayerClientRequests] %!{(MISSING)public}@ UpdatingCache: playbackQueue %!@(MISSING)"
+ "_hasClusterType"
+ "_hasConfiguredClusterSize"
+ "_hasIsClusterAware"
+ "_hasIsClusterLeader"
+ "_hasLastSupportedClusterType"
+ "_hasLastSupportedProtocolMessageType"
+ "_hasSupportsOutputContextSync"
+ "_inferInitatorForBundleID:"
+ "_initiatorShouldClearPredictedRoutesByDefault:forModificationType:"
+ "_initiatorWasInferred"
+ "_isCLIBundleID:"
+ "_isSiriBundleID:"
+ "_lastSupportedClusterType"
+ "_originatingBundleID"
+ "_shouldClearPredictedRoutes"
+ "activeUserTimeoutInterval"
+ "assistantd"
+ "com.apple.BackgroundShortcutRunner"
+ "com.apple.MusicUIService"
+ "com.apple.NanoNowPlaying"
+ "com.apple.Siri"
+ "com.apple.SoundBoard"
+ "com.apple.SpringBoard"
+ "com.apple.TVSystemUIService"
+ "com.apple.assistant_service"
+ "com.apple.homed"
+ "com.apple.mediactl"
+ "com.apple.mediaplayertool"
+ "com.apple.mediaremotetool"
+ "contextID=%!@(MISSING)"
+ "electedPlayerInterval"
+ "hasInitiatorWasInferred"
+ "hasLastSupportedClusterType"
+ "hasLastSupportedProtocolMessageType"
+ "hasOriginatingBundleID"
+ "hasShouldClearPredictedRoutes"
+ "initWithInitiator:requestID:reason:userInitiated:originatingBundleID:"
+ "initiatorWasInferred"
+ "lastSupportedClusterType"
+ "modifyOutputContextImplementation"
+ "originatingBundleID"
+ "requestType=%!@(MISSING)/%!@(MISSING)/"
+ "setHasInitiatorWasInferred:"
+ "setHasLastSupportedClusterType:"
+ "setHasLastSupportedProtocolMessageType:"
+ "setHasShouldClearPredictedRoutes:"
+ "setInitiatorWasInferred:"
+ "setLastSupportedClusterType:"
+ "setModifyOutputContextImplementation:"
+ "setOriginatingBundleID:"
+ "setPreferredState:"
+ "setPreferredState:reply:"
+ "setShouldClearPredictedRoutes:"
+ "shouldClearPredictedRoutes"
+ "shouldClearPredictedRoutes/"
+ "v32@0:8q16@?24"
+ "v32@0:8q16@?<v@?>24"
+ "{?=\"startDate\"b1\"qos\"b1\"initiatorWasInferred\"b1\"userInitiated\"b1}"
+ "{?=\"type\"b1\"fadeAudio\"b1\"muteUntilFinished\"b1\"shouldClearPredictedRoutes\"b1\"shouldModifyPredictedRoutes\"b1\"shouldNotPauseIfLastDeviceRemoved\"b1\"suppressErrorDialog\"b1}"
+ "\xef\x0f\x01"
- "\x01\x14\x12"
- "\x03\"\x12"
- "\x11\x12"
- "%!@(MISSING) %!@(MISSING) "
- "%!@(MISSING)(%!@(MISSING))<%!@(MISSING)>/%!u(MISSING)/%!u(MISSING)"
- "%!@(MISSING)OutputContextModification timedout after %!l(MISSING)f seconds"
- "%!@(MISSING)OutputDevices"
- "%!@(MISSING)PredictedOutputDevices"
- "-[MRAVOutputContext uniqueIdentifier]"
- "<MRAVOutputContextModification (%!@(MISSING)) discovered=%!@(MISSING)"
- "@16@?0@\"MRAVConcreteOutputDevice\"8"
- "AVAudioSessionCategoryPlayAndRecord"
- "AVOutputContextAddOutputDeviceOptionDidFailToConnectToOutputDeviceUserInfo"
- "AVOutputContextAddOutputDeviceOptionFadePlayback"
- "AVOutputContextAddOutputDeviceOptionInitiator"
- "AVOutputContextAddOutputDeviceOptionMuteUntilContextModificationIsFinished"
- "AVOutputContextRemoveOutputDeviceOptionContinuePlayingAfterLastDeviceRemoved"
- "AVOutputContextRemoveOutputDeviceOptionDidFailToConnectToOutputDeviceUserInfo"
- "AVOutputContextRemoveOutputDeviceOptionFadePlayback"
- "AVOutputContextRemoveOutputDeviceOptionInitiator"
- "AVOutputContextSetOutputDeviceCancelIfAuthRequiredKey"
- "AVOutputContextSetOutputDeviceDidFailToConnectToOutputDeviceUserInfoKey"
- "AVOutputContextSetOutputDeviceFadePlaybackKey"
- "AVOutputContextSetOutputDeviceMuteUntilContextModificationIsFinishedKey"
- "AVOutputContextSetOutputDevicePasswordKey"
- "AVOutputContextSetOutputDevicesOptionDidFailToConnectToOutputDeviceUserInfo"
- "AVOutputContextSetOutputDevicesOptionFadePlayback"
- "AVOutputContextSetOutputDevicesOptionMuteUntilContextModificationIsFinished"
- "Attempting to make topology modification from client process"
- "B16@?0@\"MRAVConcreteOutputDevice\"8"
- "Endpoint.addOutputDevices"
- "Endpoint.removeOutputDevices"
- "Endpoint.setOutputDevices"
- "Existing devices in context %!@(MISSING)"
- "Existing predictedOutputDevices: <%!@(MISSING)>"
- "Failed to discover all output devices involved in modification: discovered=%!@(MISSING) vs requested=%!@(MISSING)"
- "Final devices in context %!@(MISSING)"
- "Final predictedOutputDevices: <%!@(MISSING)>"
- "MRAVOutputContextModification.m"
- "Missing entitlement needed to modify output context. Operation will likley not work"
- "No devices on output context"
- "Output context modification failed. Attempted to group multiple devices where at least one is not groupable"
- "Output context modification failed. Output context doesn't support multiple devices"
- "OutputContext.addOutputDevices"
- "OutputContext.removeAllOutputDevices"
- "OutputContext.removeOutputDevices"
- "OutputContext.setOutputDevices"
- "Setting predictedOutputDevices: <%!@(MISSING)>"
- "T@\"NSArray\",R,N,V_avOutputDevices"
- "T@\"NSArray\",R,N,V_discoveredConcreteOutputDevices"
- "Timed out waiting for verification %!@(MISSING) vs %!@(MISSING)"
- "[MRNowPlayingPlayerClientRequests] %!{(MISSING)public}@ UpdatingCache: clearing contentItemArtwork for %!{(MISSING)public}@"
- "[MRNowPlayingPlayerClientRequests] %!{(MISSING)public}@ UpdatingCache: clearing formatted data artworks for %!{(MISSING)public}@"
- "[MRNowPlayingPlayerClientRequests] %!{(MISSING)public}@ UpdatingCache: clearing formatted remote artworks for %!{(MISSING)public}@"
- "[MRNowPlayingPlayerClientRequests] %!{(MISSING)public}@ UpdatingCache: contentItem %!{(MISSING)public}@"
- "[MRNowPlayingPlayerClientRequests] %!{(MISSING)public}@ UpdatingCache: playbackQueue %!{(MISSING)public}@"
- "[OutputContextModification] Failed to discover all output devices involved in modification: %!{(MISSING)public}@"
- "[OutputContextModification] Request to add outputDevices %!@(MISSING) to context %!@(MISSING)"
- "[OutputContextModification] Request to remove localDevice %!@(MISSING) from context %!@(MISSING)"
- "[OutputContextModification] Request to remove outputDevices %!@(MISSING) from context %!@(MISSING)"
- "[OutputContextModification] Will add localDevice %!@(MISSING) to context %!@(MISSING)"
- "[OutputContextModification] Will add outputDevices %!@(MISSING) to context %!@(MISSING)"
- "[OutputContextModification] Will remove localDevice %!@(MISSING) from context %!@(MISSING)"
- "[OutputContextModification] Will remove outputDevices %!@(MISSING) from context %!@(MISSING)"
- "_avOutputDevices"
- "_discoveredConcreteOutputDevices"
- "_modifyOutputDevicesOutputContext:queue:completion:"
- "_modifyPredictedOutputDevicesWithOutputContext:"
- "_postChangedScheduled"
- "_scheduledAvailableOutputDevicesReload"
- "addOutputDevice:options:completionHandler:"
- "avOutputDevices"
- "available devices=%!@(MISSING)\n"
- "com.apple.avfoundation.allows-set-output-device"
- "device %!@(MISSING) does not support bluetooth sharing"
- "device %!@(MISSING) is not groupable"
- "devices=%!@(MISSING) , outputContext=%!@(MISSING)"
- "discoveredConcreteOutputDevices"
- "instead of setting nil devices removing all non local devices, but only local devices remain so nothing to do..."
- "instead of setting nil devices removing all non local devices..."
- "output contexts that support multiple devices do not yet support passwords"
- "outputContext does not support mutiple devices"
- "pausing now playing app before removing last output device..."
- "performModificationWithOutputContext:queue:completion:"
- "removeOutputDevice:options:completionHandler:"
- "removing last output device..."
- "setOutputDevice:options:completionHandler:"
- "setOutputDevices:options:completionHandler:"
- "supportsMultipleOutputDevices"
- "v16@?0@\"AVOutputContextDestinationChange\"8"
- "void MRMediaRemoteServiceResetOutputContext(MRMediaRemoteServiceRef, NSString *__strong, __strong dispatch_queue_t, void (^__strong)(NSError *__strong))"
- "waitForOutputContextModificationVerification"
- "waitForOutputContextModificationVerification<%!@(MISSING)>"
- "{?=\"startDate\"b1\"qos\"b1\"userInitiated\"b1}"
- "{?=\"type\"b1\"fadeAudio\"b1\"muteUntilFinished\"b1\"shouldModifyPredictedRoutes\"b1\"shouldNotPauseIfLastDeviceRemoved\"b1\"suppressErrorDialog\"b1}"
- "\xcf\n\x16"

```
