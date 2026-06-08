## AXFrontBoardUtils

> `/System/Library/PrivateFrameworks/AXFrontBoardUtils.framework/AXFrontBoardUtils`

```diff

-3191.35.0.0.0
-  __TEXT.__text: 0x63c8
-  __TEXT.__auth_stubs: 0x4f0
-  __TEXT.__objc_methlist: 0x5bc
-  __TEXT.__const: 0x88
-  __TEXT.__gcc_except_tab: 0x35c
-  __TEXT.__cstring: 0xa28
-  __TEXT.__oslogstring: 0x217
-  __TEXT.__unwind_info: 0x208
-  __TEXT.__objc_classname: 0xb0
-  __TEXT.__objc_methname: 0x1559
-  __TEXT.__objc_methtype: 0x2cd
-  __TEXT.__objc_stubs: 0x1380
-  __DATA_CONST.__got: 0x178
-  __DATA_CONST.__const: 0x298
-  __DATA_CONST.__objc_classlist: 0x18
+3229.1.6.0.0
+  __TEXT.__text: 0x8de0
+  __TEXT.__objc_methlist: 0x704
+  __TEXT.__const: 0xa8
+  __TEXT.__gcc_except_tab: 0x43c
+  __TEXT.__cstring: 0xd09
+  __TEXT.__oslogstring: 0x540
+  __TEXT.__unwind_info: 0x260
+  __TEXT.__objc_stubs: 0x0
+  __TEXT.__auth_stubs: 0x0
+  __TEXT.__objc_classname: 0x0
+  __TEXT.__objc_methname: 0x0
+  __TEXT.__objc_methtype: 0x0
+  __DATA_CONST.__const: 0x3a0
+  __DATA_CONST.__objc_classlist: 0x28
   __DATA_CONST.__objc_catlist: 0x18
-  __DATA_CONST.__objc_protolist: 0x20
+  __DATA_CONST.__objc_protolist: 0x28
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x720
+  __DATA_CONST.__objc_selrefs: 0x940
   __DATA_CONST.__objc_protorefs: 0x8
-  __DATA_CONST.__objc_superrefs: 0x8
-  __AUTH_CONST.__auth_got: 0x288
-  __AUTH_CONST.__const: 0x40
-  __AUTH_CONST.__cfstring: 0xb00
-  __AUTH_CONST.__objc_const: 0x8e8
-  __DATA.__objc_ivar: 0x18
-  __DATA.__data: 0x188
-  __DATA.__bss: 0x18
+  __DATA_CONST.__objc_superrefs: 0x18
+  __DATA_CONST.__objc_arraydata: 0x10
+  __DATA_CONST.__got: 0x238
+  __AUTH_CONST.__const: 0x80
+  __AUTH_CONST.__cfstring: 0xe80
+  __AUTH_CONST.__objc_const: 0xbc0
+  __AUTH_CONST.__objc_intobj: 0x18
+  __AUTH_CONST.__objc_dictobj: 0x28
+  __AUTH_CONST.__auth_got: 0x0
+  __AUTH.__objc_data: 0xa0
+  __DATA.__objc_ivar: 0x34
+  __DATA.__data: 0x1e8
+  __DATA.__bss: 0x28
   __DATA_DIRTY.__objc_data: 0xf0
-  __DATA_DIRTY.__bss: 0x8
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/CoreGraphics.framework/CoreGraphics
+  - /System/Library/Frameworks/CoreHaptics.framework/CoreHaptics
   - /System/Library/Frameworks/CoreServices.framework/CoreServices
   - /System/Library/Frameworks/Foundation.framework/Foundation
   - /System/Library/Frameworks/UIKit.framework/UIKit
   - /System/Library/PrivateFrameworks/AXGuestPassServices.framework/AXGuestPassServices
+  - /System/Library/PrivateFrameworks/AXIDSServices.framework/AXIDSServices
   - /System/Library/PrivateFrameworks/AXRuntime.framework/AXRuntime
   - /System/Library/PrivateFrameworks/AccessibilityUtilities.framework/AccessibilityUtilities
+  - /System/Library/PrivateFrameworks/AudioSession.framework/AudioSession
   - /System/Library/PrivateFrameworks/BaseBoard.framework/BaseBoard
   - /System/Library/PrivateFrameworks/FrontBoard.framework/FrontBoard
+  - /System/Library/PrivateFrameworks/NanoPreferencesSync.framework/NanoPreferencesSync
+  - /System/Library/PrivateFrameworks/PairedDeviceRegistry.framework/PairedDeviceRegistry
   - /System/Library/PrivateFrameworks/SpringBoardServices.framework/SpringBoardServices
+  - /System/Library/PrivateFrameworks/TelephonyUtilities.framework/TelephonyUtilities
+  - /usr/lib/libAccessibility.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: F9DA88E9-3E12-360D-87F8-A2FBC182FEFF
-  Functions: 121
-  Symbols:   592
-  CStrings:  510
+  UUID: 52F20CA7-0D54-358C-B8D3-6973B77CC958
+  Functions: 148
+  Symbols:   797
+  CStrings:  280
 
Symbols:
+ -[AXIOSAutoAnswerHelper .cxx_destruct]
+ -[AXIOSAutoAnswerHelper _initializeAutoAnswerWatchObserver]
+ -[AXIOSAutoAnswerHelper _performBlockAsynchronously:afterDelay:]
+ -[AXIOSAutoAnswerHelper _playSafetySoundAndHapticWithRingerMuted:]
+ -[AXIOSAutoAnswerHelper _requestOnWristState]
+ -[AXIOSAutoAnswerHelper didReceiveIncomingData:]
+ -[AXIOSAutoAnswerHelper handleIncomingCallStateChangedWithRingerMuted:]
+ -[AXIOSAutoAnswerHelper init]
+ -[AXIOSAutoAnswerHelper setWatchActiveWristState:]
+ -[AXIOSAutoAnswerHelper shouldAllowActiveWatchToAutoAnswer]
+ -[AXIOSAutoAnswerHelper watchActiveWristState]
+ -[AXServerInstanceActionHandlerHelper .cxx_destruct]
+ -[AXServerInstanceActionHandlerHelper _addActionHandlerIfNeeded:forClientPort:]
+ -[AXServerInstanceActionHandlerHelper _removeActionHandler:]
+ -[AXServerInstanceActionHandlerHelper actionResultMessageKey]
+ -[AXServerInstanceActionHandlerHelper handleActionHandlerRegistrationMessage:]
+ -[AXServerInstanceActionHandlerHelper initWithRegistrationMessageKey:actionResultMessageKey:]
+ -[AXServerInstanceActionHandlerHelper notifyActionOccurredWithType:payload:]
+ -[AXServerInstanceActionHandlerHelper registrationMessageKey]
+ -[FBScene(AXExtras) accessibilityIsSceneOnAlwaysConnectedScreen]
+ -[FBScene(AXExtras) accessibilitySceneSettingsIndicateForeground]
+ GCC_except_table110
+ GCC_except_table25
+ GCC_except_table61
+ GCC_except_table71
+ GCC_except_table74
+ GCC_except_table89
+ GCC_except_table95
+ _AVAudioSessionCategoryVoiceOver
+ _AXColorizeFormatLog
+ _AXDeviceIsPhone
+ _AXIDSServiceDeviceNRIdentifierKey
+ _AXIDSServiceMessageKey
+ _AXLogIPC
+ _AXLoggerForFacility
+ _AXOSLogLevelFromAXLogLevel
+ _AXPerformBlockOnMainThread
+ _AXPerformBlockOnMainThreadAfterDelay
+ _AXPerformBlockSynchronouslyOnMainThread
+ _AX_CampoBundleName
+ _AX_PERFORM_WITH_LOCK
+ _OBJC_CLASS_$_AVAudioSession
+ _OBJC_CLASS_$_AXAttributedString
+ _OBJC_CLASS_$_AXIDSServices
+ _OBJC_CLASS_$_AXIOSAutoAnswerHelper
+ _OBJC_CLASS_$_AXIPCClient
+ _OBJC_CLASS_$_AXIPCMessage
+ _OBJC_CLASS_$_AXServerInstanceActionHandlerHelper
+ _OBJC_CLASS_$_AXSettings
+ _OBJC_CLASS_$_AXSubsystemAudioRouting
+ _OBJC_CLASS_$_CHHapticEngine
+ _OBJC_CLASS_$_FBDisplayManager
+ _OBJC_CLASS_$_NPSDomainAccessor
+ _OBJC_CLASS_$_NSConstantDictionary
+ _OBJC_CLASS_$_NSConstantIntegerNumber
+ _OBJC_CLASS_$_NSMutableDictionary
+ _OBJC_CLASS_$_PDRRegistry
+ _OBJC_CLASS_$_TUCallCenter
+ _OBJC_IVAR_$_AXIOSAutoAnswerHelper._hapticEngine
+ _OBJC_IVAR_$_AXIOSAutoAnswerHelper._watchActiveWristState
+ _OBJC_IVAR_$_AXIOSAutoAnswerHelper._watchActiveWristStateLock
+ _OBJC_IVAR_$_AXServerInstanceActionHandlerHelper._actionHandlers
+ _OBJC_IVAR_$_AXServerInstanceActionHandlerHelper._actionHandlersLock
+ _OBJC_IVAR_$_AXServerInstanceActionHandlerHelper._actionResultMessageKey
+ _OBJC_IVAR_$_AXServerInstanceActionHandlerHelper._registrationMessageKey
+ _OBJC_METACLASS_$_AXIOSAutoAnswerHelper
+ _OBJC_METACLASS_$_AXServerInstanceActionHandlerHelper
+ _PDRDevicePropertyKeyLocalPairingDataStorePath
+ _PDRDevicePropertyKeyPairingID
+ _UIAccessibilityAnnouncementNotification
+ _UIAccessibilityIsVoiceOverRunning
+ _UIAccessibilityTokenAnnouncementPriority
+ __AXFrontBoardFloatingDockIsPresenting
+ __AXFrontBoardSortedNonSystemAppProcessesAndScenes
+ __AXStringForArgs
+ __OBJC_$_INSTANCE_METHODS_AXIOSAutoAnswerHelper
+ __OBJC_$_INSTANCE_METHODS_AXServerInstanceActionHandlerHelper
+ __OBJC_$_INSTANCE_VARIABLES_AXIOSAutoAnswerHelper
+ __OBJC_$_INSTANCE_VARIABLES_AXServerInstanceActionHandlerHelper
+ __OBJC_$_PROP_LIST_AXIOSAutoAnswerHelper
+ __OBJC_$_PROP_LIST_AXServerInstanceActionHandlerHelper
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_AXIDSServicesClient
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_OPT_AXIDSServicesClient
+ __OBJC_$_PROTOCOL_METHOD_TYPES_AXIDSServicesClient
+ __OBJC_$_PROTOCOL_REFS_AXIDSServicesClient
+ __OBJC_CLASS_PROTOCOLS_$_AXIOSAutoAnswerHelper
+ __OBJC_CLASS_RO_$_AXIOSAutoAnswerHelper
+ __OBJC_CLASS_RO_$_AXServerInstanceActionHandlerHelper
+ __OBJC_LABEL_PROTOCOL_$_AXIDSServicesClient
+ __OBJC_METACLASS_RO_$_AXIOSAutoAnswerHelper
+ __OBJC_METACLASS_RO_$_AXServerInstanceActionHandlerHelper
+ __OBJC_PROTOCOL_$_AXIDSServicesClient
+ ___59-[AXIOSAutoAnswerHelper _initializeAutoAnswerWatchObserver]_block_invoke
+ ___59-[AXIOSAutoAnswerHelper shouldAllowActiveWatchToAutoAnswer]_block_invoke
+ ___60-[AXServerInstanceActionHandlerHelper _removeActionHandler:]_block_invoke
+ ___60-[AXServerInstanceActionHandlerHelper _removeActionHandler:]_block_invoke_2
+ ___66-[AXIOSAutoAnswerHelper _playSafetySoundAndHapticWithRingerMuted:]_block_invoke
+ ___71-[AXIOSAutoAnswerHelper handleIncomingCallStateChangedWithRingerMuted:]_block_invoke
+ ___71-[AXIOSAutoAnswerHelper handleIncomingCallStateChangedWithRingerMuted:]_block_invoke.357
+ ___71-[AXIOSAutoAnswerHelper handleIncomingCallStateChangedWithRingerMuted:]_block_invoke.362
+ ___71-[AXIOSAutoAnswerHelper handleIncomingCallStateChangedWithRingerMuted:]_block_invoke_2
+ ___76-[AXServerInstanceActionHandlerHelper notifyActionOccurredWithType:payload:]_block_invoke
+ ___76-[AXServerInstanceActionHandlerHelper notifyActionOccurredWithType:payload:]_block_invoke.361
+ ___76-[AXServerInstanceActionHandlerHelper notifyActionOccurredWithType:payload:]_block_invoke_2
+ ___78-[AXServerInstanceActionHandlerHelper handleActionHandlerRegistrationMessage:]_block_invoke
+ ___79-[AXServerInstanceActionHandlerHelper _addActionHandlerIfNeeded:forClientPort:]_block_invoke
+ ___79-[AXServerInstanceActionHandlerHelper _addActionHandlerIfNeeded:forClientPort:]_block_invoke_2
+ ___Block_byref_object_copy_.100
+ ___Block_byref_object_copy_.26
+ ___Block_byref_object_copy_.45
+ ___Block_byref_object_dispose_.101
+ ___Block_byref_object_dispose_.27
+ ___Block_byref_object_dispose_.46
+ ____AXFrontBoardGetFrontmostAppProcessesAndScenes_block_invoke.540
+ ____AXFrontBoardGetFrontmostAppProcessesAndScenes_block_invoke.542
+ ___block_descriptor_36_e15_B32?08Q16^B24l
+ ___block_descriptor_36_e28_B32?0"AXIPCClient"8Q16^B24l
+ ___block_descriptor_44_e8_32s_e5_v8?0ls32l8
+ ___block_descriptor_44_e8_32w_e5_v8?0lw32l8
+ ___block_descriptor_52_e8_32s40s_e5_v8?0ls32l8s40l8
+ ___block_descriptor_56_e8_32r40r48r_e5_v8?0lr32l8r40l8r48l8
+ ___block_descriptor_64_e8_32s40s48s_e5_v8?0ls32l8s40l8s48l8
+ ___block_literal_global.138
+ ___block_literal_global.44
+ ___block_literal_global.99
+ ___kCFBooleanTrue
+ _dispatch_after
+ _dispatch_get_global_queue
+ _dispatch_queue_attr_make_with_autorelease_frequency
+ _dispatch_queue_attr_make_with_qos_class
+ _dispatch_queue_create
+ _dispatch_time
+ _kAXSAccessibilityPreferenceDomain
+ _kAXSCallAudioRoutingAutoAnswerEnabledPreference
+ _notifyActionOccurredWithType:payload:.actionQueue
+ _notifyActionOccurredWithType:payload:.onceToken
+ _objc_claimAutoreleasedReturnValue
+ _objc_msgSend$URLForResource:withExtension:
+ _objc_msgSend$UUIDString
+ _objc_msgSend$_addActionHandlerIfNeeded:forClientPort:
+ _objc_msgSend$_initializeAutoAnswerWatchObserver
+ _objc_msgSend$_performBlockAsynchronously:afterDelay:
+ _objc_msgSend$_playSafetySoundAndHapticWithRingerMuted:
+ _objc_msgSend$_removeActionHandler:
+ _objc_msgSend$_requestOnWristState
+ _objc_msgSend$accessibilityIsSceneOnAlwaysConnectedScreen
+ _objc_msgSend$accessibilityIsSceneOnUnknownScreen
+ _objc_msgSend$accessibilitySceneSettingsIndicateForeground
+ _objc_msgSend$actionResultMessageKey
+ _objc_msgSend$alwaysConnectedIdentities
+ _objc_msgSend$answerCall:
+ _objc_msgSend$auxiliarySession
+ _objc_msgSend$axAttributedStringWithString:
+ _objc_msgSend$bluetoothIdentifier
+ _objc_msgSend$boolForKey:
+ _objc_msgSend$callAudioRoutingAutoAnswerDelay
+ _objc_msgSend$callAudioRoutingAutoAnswerEnabled
+ _objc_msgSend$clientPort
+ _objc_msgSend$connectWithError:
+ _objc_msgSend$connectedDevices
+ _objc_msgSend$copy
+ _objc_msgSend$currentAudioAndVideoCallCount
+ _objc_msgSend$currentVideoCall
+ _objc_msgSend$dictionary
+ _objc_msgSend$dictionaryWithObject:forKey:
+ _objc_msgSend$displayName
+ _objc_msgSend$getActivePairedDeviceExcludingAltAccount
+ _objc_msgSend$ignoreLogging
+ _objc_msgSend$incomingCall
+ _objc_msgSend$incomingVideoCall
+ _objc_msgSend$indexOfObjectPassingTest:
+ _objc_msgSend$indexesOfObjectsPassingTest:
+ _objc_msgSend$initWithAudioSession:error:
+ _objc_msgSend$initWithDomain:pairingID:pairingDataStore:
+ _objc_msgSend$initWithKey:payload:
+ _objc_msgSend$initWithPort:
+ _objc_msgSend$isLiveRecognitionOverlayVisible
+ _objc_msgSend$isVideo
+ _objc_msgSend$payload
+ _objc_msgSend$playPatternFromURL:error:
+ _objc_msgSend$publishMessage:priority:requestingResponse:
+ _objc_msgSend$registerForIncomingData:
+ _objc_msgSend$registrationMessageKey
+ _objc_msgSend$removeObjectsAtIndexes:
+ _objc_msgSend$sendSimpleMessage:withError:
+ _objc_msgSend$serviceMachPort
+ _objc_msgSend$setActive:error:
+ _objc_msgSend$setAttribute:forKey:
+ _objc_msgSend$setAutoShutdownEnabled:
+ _objc_msgSend$setCategory:withOptions:error:
+ _objc_msgSend$setObject:forKeyedSubscript:
+ _objc_msgSend$setPortDeathHandler:
+ _objc_msgSend$setTimeout:
+ _objc_msgSend$setWatchActiveWristState:
+ _objc_msgSend$sharedApplication
+ _objc_msgSend$shouldAllowActiveWatchToAutoAnswer
+ _objc_msgSend$status
+ _objc_msgSend$valueForProperty:
+ _objc_msgSend$watchActiveWristState
+ _objc_retainAutoreleaseReturnValue
+ _objc_retain_x1
+ _objc_retain_x27
+ _objc_retain_x3
+ _os_unfair_lock_lock
+ _os_unfair_lock_unlock
- -[AXFrontBoardProcessWatcher _validateFocusedApps:].cold.1
- -[AXFrontBoardProcessWatcher _validateFocusedApps:].cold.2
- -[AXFrontBoardProcessWatcher _validateFocusedApps:].cold.3
- -[AXFrontBoardProcessWatcher processManager:didAddProcess:].cold.1
- -[UIApplication(AXFrontBoardExtras) _accessibilityAddRecentlyActivatedBundleIdFromSwitcher:].cold.1
- GCC_except_table1
- GCC_except_table15
- GCC_except_table38
- _AXApplicationNameLabelForBundleIdentifier.cold.1
- _AXFrontBoardSystemApplicationControllerInstance.AX_SBApplicationController
- _OUTLINED_FUNCTION_0
- _OUTLINED_FUNCTION_1
- _OUTLINED_FUNCTION_2
- __AXFrontBoardFrontmostAppProcesses
- __AXFrontBoardGetFrontmostAppProcessesAndScenes.cold.1
- __AXFrontBoardGetTransientProcessAndSceneForBundleIdentifier.cold.1
- ____AXFrontBoardGetFrontmostAppProcessesAndScenes_block_invoke.513
- ____AXFrontBoardGetFrontmostAppProcessesAndScenes_block_invoke.515
- ____AXFrontBoardSortedNonSystemAppProcessesAndScenes_block_invoke_6
- _objc_retainAutoreleasedReturnValue
- _objc_retain_x26
CStrings:
+ "  Scene settings foreground: %@\n"
+ "%{public}@"
+ "AX IDS connected devices: %@"
+ "Allowing active watch to auto answer non-video call"
+ "Auto Answer pref val is %{public}@ - call count is %lu, incoming call: %{public}@ , incoming video call: %{public}@"
+ "Auto-answering incoming call: %{public}@ , with status: %d"
+ "B32@?0@\"AXIPCClient\"8Q16^B24"
+ "B32@?0@8Q16^B24"
+ "Could not connect client for registering serveri nstance action handler: %{public}@"
+ "Error sending server instance action: %@"
+ "Filtering scene %@ (bundle: %@) — process foreground: %d, scene settings foreground: %d"
+ "Including scene %@ (bundle: %@) — process foreground: YES, scene settings foreground: YES"
+ "NO"
+ "NOT (bundleIdentifier == %@) AND NOT (bundleIdentifier == %@)"
+ "Playing safety sound, call answer delay: %@"
+ "Unable to determine device on-wrist state"
+ "YES"
+ "active device doesn't have auto answer enabled"
+ "active device identifier: %@"
+ "active device is not connected"
+ "activeDisplayWindowScene"
+ "ahap"
+ "applicationController"
+ "auto answer - played pattern: %@"
+ "auto answer safety asset playing, isSilentMode=%@"
+ "auto answer: should answer: %@"
+ "ax_autoAnswer"
+ "axserverinstance-action-queue"
+ "com.apple.InputUI"
+ "com.apple.Siri"
+ "com.apple.UIKit.remote-keyboard"
+ "failed to make haptic engine: %@"
+ "failed to play haptic: %@"
+ "failed to set audio session active due to: %@"
+ "failed to set audio session category (%@) due to: %@"
+ "floatingDockController"
+ "isRemoteContentPresenting"
+ "no active, paired device"
+ "no connected devices!"
+ "onWristState"
+ "payload"
+ "q"
+ "received incoming IDS data: %@"
+ "register"
+ "remoteContentManager"
+ "requesting watch on wrist state"
+ "result"
+ "windowSceneManager"
- "#16@0:8"
- ".cxx_destruct"
- "@"
- "@\"<BSInterfaceOrientationMapResolving><BSXPCSecureCoding>\"16@0:8"
- "@\"AXDispatchTimer\""
- "@\"AXFBFakeProcessState\""
- "@\"BSCornerRadiusConfiguration\"16@0:8"
- "@\"NSNumber\"16@0:8"
- "@\"NSSet\""
- "@\"NSSet\"16@0:8"
- "@\"NSString\""
- "@\"NSString\"16@0:8"
- "@16@0:8"
- "@20@0:8i16"
- "@24@0:8:16"
- "@24@0:8@16"
- "@32@0:8:16@24"
- "@40@0:8:16@24@32"
- "AXExtras"
- "AXFBFakeProcess"
- "AXFBFakeProcessState"
- "AXFrontBoardExtras"
- "AXFrontBoardProcessWatcher"
- "B16@0:8"
- "B24@0:8#16"
- "B24@0:8:16"
- "B24@0:8@\"Protocol\"16"
- "B24@0:8@16"
- "B32@0:8@16@24"
- "CGPointValue"
- "CGRectValue"
- "FBProcessManagerObserver"
- "FBProcessObserver"
- "I16@0:8"
- "NOT (bundleIdentifier == %@)"
- "NSObject"
- "Q16@0:8"
- "SBApplicationController"
- "T#,R"
- "T@\"<BSInterfaceOrientationMapResolving><BSXPCSecureCoding>\",R,N"
- "T@\"AXFBFakeProcessState\",&,N,V_state"
- "T@\"BSCornerRadiusConfiguration\",R,N"
- "T@\"NSNumber\",R,N"
- "T@\"NSSet\",R,N"
- "T@\"NSString\",&,N,V_bundleIdentifier"
- "T@\"NSString\",?,R,C"
- "T@\"NSString\",R,C"
- "T@\"NSString\",R,N"
- "TB,R,N"
- "TI,R,N"
- "TQ,R"
- "TQ,R,N"
- "Td,R,N"
- "Ti,N,V_pid"
- "Tq,R,N"
- "T{CGRect={CGPoint=dd}{CGSize=dd}},R,N"
- "T{UIEdgeInsets=dddd},R,N"
- "UIApplicationSceneSettings"
- "URL"
- "Vv16@0:8"
- "^{_NSZone=}16@0:8"
- "_accessibilityAddRecentlyActivatedBundleIdFromSwitcher:"
- "_accessibilityAllWindowsOnlyVisibleWindows:"
- "_accessibilityRecentlyActivatedApplicationBundleIdentifiers"
- "_accessibilityRemoveRecentlyActivatedBundleIdFromSwitcher:"
- "_appTransitionTimer"
- "_bundleIdentifier"
- "_cachedFocusedAppPIDs"
- "_observerToken"
- "_pid"
- "_processDescriptionForPID:"
- "_processStateChangeIsTaskStateChangeFrom:to:"
- "_processStateChangeIsVisibilityStateChangeFrom:to:"
- "_state"
- "_validateFocusedApps:"
- "accessibilityContrast"
- "accessibilityIsSceneOccluded"
- "accessibilityIsSceneOnCarScreen"
- "accessibilityIsSceneOnContinuityDisplay"
- "accessibilityIsSceneOnExternalScreen"
- "accessibilityIsSceneOnMainScreen"
- "accessibilityIsSceneOnUnknownScreen"
- "accessibilitySceneBelongsToTheSystemApp"
- "accessibilitySceneDescription"
- "accessibilitySceneFrame"
- "accessibilitySceneIdentifier"
- "accessibilitySceneIsCallServiceBanner"
- "accessibilitySceneIsDeactivatedBySidebar"
- "accessibilitySceneIsDeactivatedBySwitcher"
- "accessibilitySceneIsDismissedInCallService"
- "accessibilitySceneIsDismissedSearchScreen"
- "accessibilitySceneIsForegroundVisible"
- "accessibilitySceneIsRunningInForeground"
- "accessibilitySceneIsShieldedByAppProtection"
- "accessibilitySceneIsSuspended"
- "accessibilitySceneLevel"
- "accessibilitySceneOwnerIsAUIApplication"
- "accessibilityScenePID"
- "accessibilitySceneProcess"
- "accessibilitySpokenNameForProcess:"
- "accessibilityUIServicePID"
- "activeInterfaceOrientation"
- "addObject:"
- "addObserver:"
- "addObserverForName:object:queue:usingBlock:"
- "afterDelay:processBlock:cancelBlock:"
- "allKeys"
- "allObjects"
- "allProcesses"
- "allScenes"
- "allWindowsIncludingInternalWindows:onlyVisibleWindows:"
- "alpha"
- "angleFromHostReferenceUprightDirection"
- "appWithPID:bundleID:"
- "appendFormat:"
- "array"
- "arrayWithObjects:count:"
- "artworkSubtype"
- "autorelease"
- "ax_arrayByRemovingDuplicates"
- "ax_containsObjectUsingBlock:"
- "ax_removeObjectsFromArrayUsingBlock:"
- "boolValue"
- "bundleForClass:"
- "bundleRecordWithApplicationIdentifier:error:"
- "canShowAlerts"
- "cancel"
- "class"
- "conformsToProtocol:"
- "containsObject:"
- "containsString:"
- "cornerRadiusConfiguration"
- "count"
- "countByEnumeratingWithState:objects:count:"
- "currentLayout"
- "d16@0:8"
- "d24@0:8q16"
- "deactivationReasons"
- "dealloc"
- "debugDescription"
- "defaultCenter"
- "defaultStatusBarHeightForOrientation:"
- "description"
- "deviceOrientation"
- "deviceOrientationEventsEnabled"
- "dictionaryWithObjects:forKeys:count:"
- "displayIdentity"
- "elements"
- "enhancedWindowingEnabled"
- "enumerateObjectsUsingBlock:"
- "enumerateScenesWithBlock:"
- "filterUsingPredicate:"
- "firstObject"
- "floatValue"
- "forcedStatusBarForegroundTransparent"
- "forcedStatusBarStyle"
- "handle"
- "hasPrefix:"
- "hash"
- "homeAffordanceOverlayAllowance"
- "hostContextIdentifierForSnapshotting"
- "hostReferenceAngleMode"
- "i"
- "i16@0:8"
- "idleModeEnabled"
- "inLiveResize"
- "infoDictionary"
- "init"
- "initWithReason:"
- "initWithTargetSerialQueue:"
- "initWithURL:"
- "integerValue"
- "interfaceOrientationMapResolver"
- "interfaceOrientationMode"
- "isAppSwitcherVisible"
- "isAppleWatchRemoteScreenActive"
- "isApplicationProcess"
- "isCapturingContentForAdditionalRenderingDestination"
- "isCarDisplay"
- "isControlCenterVisible"
- "isEqual:"
- "isEqualToSet:"
- "isEqualToString:"
- "isExternal"
- "isHidden"
- "isKindOfClass:"
- "isMainDisplay"
- "isMainThread"
- "isMemberOfClass:"
- "isMenuBarModal"
- "isNonExclusiveSystemUIFocusableIncludingPIPWindow:"
- "isNotificationCenterVisible"
- "isPasscodeLockVisible"
- "isProxy"
- "isRemoteAlertVisible"
- "isScreenLockedWithPasscode:"
- "isSiriVisible"
- "isSoftwareUpdateUIVisible"
- "isSpotlightVisible"
- "isTransferUIShowing"
- "legacyProcess"
- "length"
- "localizedInfoDictionary"
- "localizedName"
- "localizedStringForKey:value:table:"
- "mainQueue"
- "mutableCopy"
- "name"
- "null"
- "numberWithBool:"
- "numberWithDouble:"
- "numberWithInt:"
- "numberWithInteger:"
- "objectAtIndex:"
- "objectAtIndexedSubscript:"
- "objectForKey:"
- "objectForKeyedSubscript:"
- "objectForSetting:"
- "performSelector:"
- "performSelector:withObject:"
- "performSelector:withObject:withObject:"
- "peripheryInsets"
- "persistenceIdentifier"
- "pointerLockStatus"
- "postNotificationName:object:userInfo:"
- "predicateWithFormat:"
- "process:stateDidChangeFromState:toState:"
- "processDidExit:"
- "processForBundleIdentifier:"
- "processForPID:"
- "processManager:didAddProcess:"
- "processManager:didRemoveProcess:"
- "processWillExit:"
- "processesForBundleIdentifier:"
- "q16@0:8"
- "release"
- "removeObject:"
- "removeObjectAtIndex:"
- "removeObserver:"
- "respondsToSelector:"
- "retain"
- "retainCount"
- "safeAreaInsetsLandscapeLeft"
- "safeAreaInsetsLandscapeRight"
- "safeAreaInsetsPortrait"
- "safeAreaInsetsPortraitUpsideDown"
- "safeBoolForKey:"
- "safeDictionaryForKey:"
- "safeIntForKey:"
- "safeIntegerForKey:"
- "safeStringForKey:"
- "safeValueForKey:"
- "safeValueForKeyPath:"
- "scenePresenterRenderIdentifierForSnapshotting"
- "screenBoundsIgnoresSceneOrientation"
- "screenReferenceDisplayModeStatus"
- "self"
- "server"
- "set"
- "setAutomaticallyCancelPendingBlockUponSchedulingNewBlock:"
- "setBundleIdentifier:"
- "setPid:"
- "setRebootType:"
- "setSource:"
- "setState:"
- "setWithArray:"
- "setupProcessName"
- "shutdownUsingOptions:"
- "sortUsingComparator:"
- "statusBarAvoidanceFrame"
- "statusBarDisabled"
- "statusBarHeight"
- "statusBarParts"
- "statusBarStyleOverridesToSuppress"
- "stringWithFormat:"
- "superclass"
- "systemMinimumMargin"
- "targetOfEventDeferringEnvironments"
- "underLock"
- "userInfo"
- "userInterfaceLayoutDirection"
- "userInterfaceStyle"
- "v16@0:8"
- "v20@0:8i16"
- "v24@0:8@\"FBProcess\"16"
- "v24@0:8@16"
- "v24@0:8q16"
- "v32@0:8@\"FBProcessManager\"16@\"FBProcess\"24"
- "v32@0:8@16@24"
- "v40@0:8@\"FBProcess\"16@\"FBProcessState\"24@\"FBProcessState\"32"
- "v40@0:8@16@24@32"
- "validateFocusedAppsWithEvent:"
- "valueForKey:"
- "zone"
- "{CGRect={CGPoint=dd}{CGSize=dd}}16@0:8"
- "{UIEdgeInsets=dddd}16@0:8"

```
