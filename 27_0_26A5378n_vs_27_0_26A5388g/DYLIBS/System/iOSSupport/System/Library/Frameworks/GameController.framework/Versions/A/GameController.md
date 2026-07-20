## GameController

> `/System/iOSSupport/System/Library/Frameworks/GameController.framework/Versions/A/GameController`

### Sections with Same Size but Changed Content

- `__TEXT.__init_offsets`
- `__TEXT.__swift5_typeref`
- `__TEXT.__constg_swiftt`
- `__TEXT.__swift5_proto`
- `__TEXT.__eh_frame`
- `__DATA_CONST.__objc_catlist`
- `__DATA_CONST.__objc_arraydata`
- `__AUTH_CONST.__objc_dictobj`
- `__AUTH_CONST.__objc_arrayobj`
- `__AUTH.__data`

```diff

-14.0.19.0.0
-  __TEXT.__text: 0xfa0e0
+14.0.21.0.0
+  __TEXT.__text: 0xff618
   __TEXT.__init_offsets: 0x4
-  __TEXT.__objc_methlist: 0xf254
-  __TEXT.__const: 0x23ec
-  __TEXT.__gcc_except_tab: 0x3548
-  __TEXT.__cstring: 0x9b11
-  __TEXT.__oslogstring: 0x8178
+  __TEXT.__objc_methlist: 0xff1c
+  __TEXT.__const: 0x23fc
+  __TEXT.__gcc_except_tab: 0x3658
+  __TEXT.__cstring: 0xa081
+  __TEXT.__oslogstring: 0x85d8
   __TEXT.__swift5_typeref: 0x878
   __TEXT.__swift5_reflstr: 0x34f
   __TEXT.__swift5_assocty: 0x3e8

   __TEXT.__swift5_types: 0xb0
   __TEXT.__swift5_capture: 0x10c
   __TEXT.__swift5_builtin: 0x28
-  __TEXT.__unwind_info: 0x4b38
+  __TEXT.__unwind_info: 0x4d40
   __TEXT.__eh_frame: 0x170
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0
   __TEXT.__objc_classname: 0x0
   __TEXT.__objc_methname: 0x0
   __TEXT.__objc_methtype: 0x0
-  __DATA_CONST.__const: 0x2b70
-  __DATA_CONST.__objc_classlist: 0x9b8
+  __DATA_CONST.__const: 0x2c48
+  __DATA_CONST.__objc_classlist: 0xa28
   __DATA_CONST.__objc_catlist: 0xb8
-  __DATA_CONST.__objc_protolist: 0x7d0
+  __DATA_CONST.__objc_protolist: 0x818
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x4b00
-  __DATA_CONST.__objc_protorefs: 0x4a0
-  __DATA_CONST.__objc_superrefs: 0x890
+  __DATA_CONST.__objc_selrefs: 0x4f30
+  __DATA_CONST.__objc_protorefs: 0x4d0
+  __DATA_CONST.__objc_superrefs: 0x900
   __DATA_CONST.__objc_arraydata: 0x470
-  __DATA_CONST.__got: 0xcb8
-  __AUTH_CONST.__const: 0x22d0
-  __AUTH_CONST.__cfstring: 0xaf00
-  __AUTH_CONST.__objc_const: 0x48498
-  __AUTH_CONST.__objc_intobj: 0x1080
+  __DATA_CONST.__got: 0xdc0
+  __AUTH_CONST.__const: 0x23c0
+  __AUTH_CONST.__cfstring: 0xb3a0
+  __AUTH_CONST.__objc_const: 0x4cac0
+  __AUTH_CONST.__objc_intobj: 0x1098
   __AUTH_CONST.__objc_dictobj: 0xa0
   __AUTH_CONST.__objc_arrayobj: 0x18
-  __AUTH_CONST.__auth_got: 0xf60
-  __AUTH.__objc_data: 0x4e78
+  __AUTH_CONST.__auth_got: 0xfe0
+  __AUTH.__objc_data: 0x4b58
   __AUTH.__data: 0x5a0
-  __DATA.__objc_ivar: 0x15b4
-  __DATA.__data: 0x5bb0
+  __DATA.__objc_ivar: 0x16a0
+  __DATA.__data: 0x5f10
   __DATA.__crash_info: 0x148
-  __DATA.__bss: 0x27c0
+  __DATA.__bss: 0x2800
   __DATA.__common: 0x90
-  __DATA_DIRTY.__objc_data: 0x16d0
+  __DATA_DIRTY.__objc_data: 0x1e50
   __DATA_DIRTY.__data: 0x18
   __DATA_DIRTY.__bss: 0x220
   - /System/Library/Frameworks/CoreBluetooth.framework/Versions/A/CoreBluetooth

   - /System/Library/Frameworks/ExternalAccessory.framework/ExternalAccessory
   - /System/Library/Frameworks/Foundation.framework/Versions/C/Foundation
   - /System/Library/Frameworks/IOKit.framework/Versions/A/IOKit
+  - /System/Library/Frameworks/ImageIO.framework/Versions/A/ImageIO
   - /System/Library/Frameworks/QuartzCore.framework/Versions/A/QuartzCore
   - /System/Library/Frameworks/UniformTypeIdentifiers.framework/Versions/A/UniformTypeIdentifiers
   - /System/Library/Frameworks/UserNotifications.framework/Versions/A/UserNotifications

   - /System/Library/PrivateFrameworks/GameControllerFoundation.framework/Versions/A/GameControllerFoundation
   - /System/Library/PrivateFrameworks/GameControllerIO.framework/Versions/A/GameControllerIO
   - /System/Library/PrivateFrameworks/GameControllerSettings.framework/Versions/A/GameControllerSettings
+  - /System/Library/PrivateFrameworks/IconServices.framework/Versions/A/IconServices
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
   - /usr/lib/swift/libswiftCore.dylib

   - /usr/lib/swift/libswiftObjectiveC.dylib
   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
-  Functions: 7439
-  Symbols:   16376
-  CStrings:  2356
+  Functions: 7682
+  Symbols:   16957
+  CStrings:  2420
 
Symbols:
+ +[GCControllerLowBatteryNotification supportsSecureCoding]
+ +[GCGameIntentLaunchAppleGamesAction supportsSecureCoding]
+ +[GCGameIntentLaunchApplicationAction supportsSecureCoding]
+ +[GCGameIntentOpenPlatformGameLibraryAction supportsSecureCoding]
+ +[GCGameIntentShowAppleGameOverlayAction supportsSecureCoding]
+ +[GCHomeButtonPermissionUserNotification supportsSecureCoding]
+ +[GCSpatialControllerHSUserNotification supportsSecureCoding]
+ +[GCUserNotificationResponse supportsSecureCoding]
+ +[NSError(GCUserNotificationErrorDomain) gc_userNotificationError:userInfo:]
+ +[_GCAgentClientProxy clientProxyWithConnection:server:userDefaultsProxy:gameIntentProxy:userNotificationProxy:]
+ +[_GCSonyPSVR2SenseControllerProfile physicalDeviceChirality:]
+ +[_GCUserNotificationConfiguration initialize]
+ -[GCControllerLowBatteryNotification batteryLevel]
+ -[GCControllerLowBatteryNotification chirality]
+ -[GCControllerLowBatteryNotification copyWithZone:]
+ -[GCControllerLowBatteryNotification encodeWithCoder:]
+ -[GCControllerLowBatteryNotification initWithChirality:batteryLevel:]
+ -[GCControllerLowBatteryNotification initWithCoder:]
+ -[GCControllerLowBatteryNotification init]
+ -[GCControllerLowBatteryNotification prepareNotification:error:]
+ -[GCGameIntentLaunchAppleGamesAction copyWithZone:]
+ -[GCGameIntentLaunchAppleGamesAction description]
+ -[GCGameIntentLaunchAppleGamesAction encodeWithCoder:]
+ -[GCGameIntentLaunchAppleGamesAction initWithCoder:]
+ -[GCGameIntentLaunchAppleGamesAction init]
+ -[GCGameIntentLaunchAppleGamesAction performAction]
+ -[GCGameIntentLaunchApplicationAction .cxx_destruct]
+ -[GCGameIntentLaunchApplicationAction bundleIdentifier]
+ -[GCGameIntentLaunchApplicationAction copyWithZone:]
+ -[GCGameIntentLaunchApplicationAction description]
+ -[GCGameIntentLaunchApplicationAction encodeWithCoder:]
+ -[GCGameIntentLaunchApplicationAction initWithBundleIdentifier:]
+ -[GCGameIntentLaunchApplicationAction initWithCoder:]
+ -[GCGameIntentLaunchApplicationAction init]
+ -[GCGameIntentLaunchApplicationAction performAction]
+ -[GCGameIntentLauncherXPCProxyClient performActions:]
+ -[GCGameIntentManager _runNextAction:]
+ -[GCGameIntentManager performActions:]
+ -[GCGameIntentOpenPlatformGameLibraryAction copyWithZone:]
+ -[GCGameIntentOpenPlatformGameLibraryAction description]
+ -[GCGameIntentOpenPlatformGameLibraryAction encodeWithCoder:]
+ -[GCGameIntentOpenPlatformGameLibraryAction initWithCoder:]
+ -[GCGameIntentOpenPlatformGameLibraryAction init]
+ -[GCGameIntentOpenPlatformGameLibraryAction performAction]
+ -[GCGameIntentShowAppleGameOverlayAction copyWithZone:]
+ -[GCGameIntentShowAppleGameOverlayAction description]
+ -[GCGameIntentShowAppleGameOverlayAction encodeWithCoder:]
+ -[GCGameIntentShowAppleGameOverlayAction initWithCoder:]
+ -[GCGameIntentShowAppleGameOverlayAction initWithConditional:]
+ -[GCGameIntentShowAppleGameOverlayAction init]
+ -[GCGameIntentShowAppleGameOverlayAction isConditional]
+ -[GCGameIntentShowAppleGameOverlayAction performAction]
+ -[GCHomeButtonPermissionUserNotification .cxx_destruct]
+ -[GCHomeButtonPermissionUserNotification bundleIdentifier]
+ -[GCHomeButtonPermissionUserNotification checkUserResponse:]
+ -[GCHomeButtonPermissionUserNotification copyWithZone:]
+ -[GCHomeButtonPermissionUserNotification encodeWithCoder:]
+ -[GCHomeButtonPermissionUserNotification initWithBundleIdentifier:]
+ -[GCHomeButtonPermissionUserNotification initWithCoder:]
+ -[GCHomeButtonPermissionUserNotification prepareNotification:error:]
+ -[GCSpatialControllerHSUserNotification copyWithZone:]
+ -[GCSpatialControllerHSUserNotification encodeWithCoder:]
+ -[GCSpatialControllerHSUserNotification initWithCoder:]
+ -[GCSpatialControllerHSUserNotification init]
+ -[GCSpatialControllerHSUserNotification prepareNotification:error:]
+ -[GCSpatialControllerHSUserNotification userTappedLearnMoreInResponse:]
+ -[GCUserNotificationManager .cxx_destruct]
+ -[GCUserNotificationManager _cancelEntry:]
+ -[GCUserNotificationManager _enqueueEntry:]
+ -[GCUserNotificationManager _onrunloop_cancelEntry:]
+ -[GCUserNotificationManager _onrunloop_finalizeEntry:]
+ -[GCUserNotificationManager _onrunloop_handleResponseForNotification:responseFlags:]
+ -[GCUserNotificationManager _onrunloop_pump]
+ -[GCUserNotificationManager _runLoopThreadMain]
+ -[GCUserNotificationManager dealloc]
+ -[GCUserNotificationManager init]
+ -[GCUserNotificationManager presentUserNotificationForRequest:]
+ -[GCUserNotificationManager(XPCProxy) presentUserNotificationForRequest:client:reply:]
+ -[GCUserNotificationResponse .cxx_destruct]
+ -[GCUserNotificationResponse checkedCheckBoxes]
+ -[GCUserNotificationResponse copyWithZone:]
+ -[GCUserNotificationResponse description]
+ -[GCUserNotificationResponse dismissAction]
+ -[GCUserNotificationResponse encodeWithCoder:]
+ -[GCUserNotificationResponse hash]
+ -[GCUserNotificationResponse initWithCoder:]
+ -[GCUserNotificationResponse initWithDismissAction:textFieldValues:checkedCheckBoxes:popUpSelection:]
+ -[GCUserNotificationResponse init]
+ -[GCUserNotificationResponse isEqual:]
+ -[GCUserNotificationResponse popUpSelection]
+ -[GCUserNotificationResponse textFieldValues]
+ -[GCUserNotificationXPCProxyClient .cxx_destruct]
+ -[GCUserNotificationXPCProxyClient agentCheckIn:effectiveUserIdentifier:]
+ -[GCUserNotificationXPCProxyClient consoleUserDidChange:]
+ -[GCUserNotificationXPCProxyClient dealloc]
+ -[GCUserNotificationXPCProxyClient init]
+ -[GCUserNotificationXPCProxyClient presentUserNotificationForRequest:]
+ -[GCUserNotificationXPCProxyClient refreshActiveServer]
+ -[GCUserNotificationXPCProxyClient server]
+ -[GCUserNotificationXPCProxyClient setServer:]
+ -[_GCAgentClientProxy _initWithConnection:server:userDefaultsProxy:gameIntentProxy:userNotificationProxy:]
+ -[_GCAgentClientProxy connectToUserNotificationXPCProxyServiceWithClient:reply:]
+ -[_GCUserNotificationConfiguration .cxx_destruct]
+ -[_GCUserNotificationConfiguration _configureNotificationDictionary:]
+ -[_GCUserNotificationConfiguration _ui_configureNotificationDictionary:]
+ -[_GCUserNotificationConfiguration alertAccessibilityIdentifier]
+ -[_GCUserNotificationConfiguration alertHeader]
+ -[_GCUserNotificationConfiguration alertLevel]
+ -[_GCUserNotificationConfiguration alertMessage]
+ -[_GCUserNotificationConfiguration alertTopMost]
+ -[_GCUserNotificationConfiguration alternateButtonAccessibilityIdentifier]
+ -[_GCUserNotificationConfiguration alternateButtonTitle]
+ -[_GCUserNotificationConfiguration checkBoxCount]
+ -[_GCUserNotificationConfiguration checkBoxTitles]
+ -[_GCUserNotificationConfiguration copyNotificationDictionary]
+ -[_GCUserNotificationConfiguration dealloc]
+ -[_GCUserNotificationConfiguration defaultButtonAccessibilityIdentifier]
+ -[_GCUserNotificationConfiguration defaultButtonTitle]
+ -[_GCUserNotificationConfiguration hasPopUp]
+ -[_GCUserNotificationConfiguration iconURL]
+ -[_GCUserNotificationConfiguration init]
+ -[_GCUserNotificationConfiguration initiallyCheckedCheckBoxes]
+ -[_GCUserNotificationConfiguration initiallySelectedPopUpItem]
+ -[_GCUserNotificationConfiguration localizationURL]
+ -[_GCUserNotificationConfiguration noDefaultButton]
+ -[_GCUserNotificationConfiguration otherButtonAccessibilityIdentifier]
+ -[_GCUserNotificationConfiguration otherButtonTitle]
+ -[_GCUserNotificationConfiguration popUpTitles]
+ -[_GCUserNotificationConfiguration progressIndicatorValue]
+ -[_GCUserNotificationConfiguration requestFlags]
+ -[_GCUserNotificationConfiguration runCleanupHandlers]
+ -[_GCUserNotificationConfiguration secureTextFieldIndexes]
+ -[_GCUserNotificationConfiguration setAlertAccessibilityIdentifier:]
+ -[_GCUserNotificationConfiguration setAlertHeader:]
+ -[_GCUserNotificationConfiguration setAlertLevel:]
+ -[_GCUserNotificationConfiguration setAlertMessage:]
+ -[_GCUserNotificationConfiguration setAlertTopMost:]
+ -[_GCUserNotificationConfiguration setAlternateButtonAccessibilityIdentifier:]
+ -[_GCUserNotificationConfiguration setAlternateButtonTitle:]
+ -[_GCUserNotificationConfiguration setCheckBoxTitles:]
+ -[_GCUserNotificationConfiguration setDefaultButtonAccessibilityIdentifier:]
+ -[_GCUserNotificationConfiguration setDefaultButtonTitle:]
+ -[_GCUserNotificationConfiguration setIconURL:]
+ -[_GCUserNotificationConfiguration setIconURL:withCleanupHandler:]
+ -[_GCUserNotificationConfiguration setInitiallyCheckedCheckBoxes:]
+ -[_GCUserNotificationConfiguration setInitiallySelectedPopUpItem:]
+ -[_GCUserNotificationConfiguration setLocalizationURL:]
+ -[_GCUserNotificationConfiguration setNoDefaultButton:]
+ -[_GCUserNotificationConfiguration setOtherButtonAccessibilityIdentifier:]
+ -[_GCUserNotificationConfiguration setOtherButtonTitle:]
+ -[_GCUserNotificationConfiguration setPopUpTitles:]
+ -[_GCUserNotificationConfiguration setProgressIndicatorValue:]
+ -[_GCUserNotificationConfiguration setSecureTextFieldIndexes:]
+ -[_GCUserNotificationConfiguration setSoundURL:]
+ -[_GCUserNotificationConfiguration setSoundURL:withCleanupHandler:]
+ -[_GCUserNotificationConfiguration setTextFieldDefaultValues:]
+ -[_GCUserNotificationConfiguration setTextFieldTitles:]
+ -[_GCUserNotificationConfiguration setTimeout:]
+ -[_GCUserNotificationConfiguration setUseRadioButtons:]
+ -[_GCUserNotificationConfiguration soundURL]
+ -[_GCUserNotificationConfiguration textFieldCount]
+ -[_GCUserNotificationConfiguration textFieldDefaultValues]
+ -[_GCUserNotificationConfiguration textFieldTitles]
+ -[_GCUserNotificationConfiguration timeout]
+ -[_GCUserNotificationConfiguration useRadioButtons]
+ -[_GCUserNotificationManagerEntry .cxx_destruct]
+ -[_GCUserNotificationManagerEntry configuration]
+ -[_GCUserNotificationManagerEntry dealloc]
+ -[_GCUserNotificationManagerEntry initWithRequest:promise:]
+ -[_GCUserNotificationManagerEntry notification]
+ -[_GCUserNotificationManagerEntry promise]
+ -[_GCUserNotificationManagerEntry request]
+ -[_GCUserNotificationManagerEntry setNotification:]
+ -[_GCUserNotificationManagerEntry setSource:]
+ -[_GCUserNotificationManagerEntry setTerminated:]
+ -[_GCUserNotificationManagerEntry source]
+ -[_GCUserNotificationManagerEntry terminated]
+ -[_GCUserNotificationXPCProxyClientPresentationClient .cxx_destruct]
+ -[_GCUserNotificationXPCProxyClientPresentationClient _terminate]
+ -[_GCUserNotificationXPCProxyClientPresentationClient cancel]
+ -[_GCUserNotificationXPCProxyClientPresentationClient initWithPromise:]
+ -[_GCUserNotificationXPCProxyClientPresentationClient presentationDidCancel]
+ -[_GCUserNotificationXPCProxyClientPresentationClient presentationDidFailWithError:]
+ -[_GCUserNotificationXPCProxyClientPresentationClient presentationDidSucceedWithResponse:]
+ -[_GCUserNotificationXPCProxyClientPresentationClient setServerHandle:]
+ -[_GCUserNotificationXPCProxyServerPresentationServer .cxx_destruct]
+ -[_GCUserNotificationXPCProxyServerPresentationServer cancelPresentation]
+ -[_GCUserNotificationXPCProxyServerPresentationServer initWithFuture:]
+ -[_GCUserNotificationXPCProxyServerPresentationServer init]
+ GCGameIntentAction_Classes
+ GCGameIntentAction_Classes.Classes
+ GCGameIntentAction_Classes.onceToken
+ GCUserNotificationRequest_Classes
+ GCUserNotificationRequest_Classes.Classes
+ GCUserNotificationRequest_Classes.onceToken
+ OBJC_IVAR_$_GCControllerLowBatteryNotification._batteryLevel
+ OBJC_IVAR_$_GCControllerLowBatteryNotification._chirality
+ OBJC_IVAR_$_GCGameIntentLaunchApplicationAction._bundleIdentifier
+ OBJC_IVAR_$_GCGameIntentShowAppleGameOverlayAction._conditional
+ OBJC_IVAR_$_GCHomeButtonPermissionUserNotification._bundleIdentifier
+ OBJC_IVAR_$_GCSyntheticDeviceManager._upcallQueue
+ OBJC_IVAR_$_GCUserNotificationManager._current
+ OBJC_IVAR_$_GCUserNotificationManager._keepAliveSource
+ OBJC_IVAR_$_GCUserNotificationManager._lock
+ OBJC_IVAR_$_GCUserNotificationManager._pending
+ OBJC_IVAR_$_GCUserNotificationManager._runLoop
+ OBJC_IVAR_$_GCUserNotificationManager._runLoopThread
+ OBJC_IVAR_$_GCUserNotificationResponse._checkedCheckBoxes
+ OBJC_IVAR_$_GCUserNotificationResponse._dismissAction
+ OBJC_IVAR_$_GCUserNotificationResponse._popUpSelection
+ OBJC_IVAR_$_GCUserNotificationResponse._textFieldValues
+ OBJC_IVAR_$_GCUserNotificationXPCProxyClient._server
+ OBJC_IVAR_$_GCUserNotificationXPCProxyClient._servers
+ OBJC_IVAR_$__GCAgentClientProxy._userNotificationProxy
+ OBJC_IVAR_$__GCDefaultLogicalDevice._systemButtonArbitration
+ OBJC_IVAR_$__GCUserNotificationConfiguration._alertAccessibilityIdentifier
+ OBJC_IVAR_$__GCUserNotificationConfiguration._alertHeader
+ OBJC_IVAR_$__GCUserNotificationConfiguration._alertLevel
+ OBJC_IVAR_$__GCUserNotificationConfiguration._alertMessage
+ OBJC_IVAR_$__GCUserNotificationConfiguration._alertTopMost
+ OBJC_IVAR_$__GCUserNotificationConfiguration._alternateButtonAccessibilityIdentifier
+ OBJC_IVAR_$__GCUserNotificationConfiguration._alternateButtonTitle
+ OBJC_IVAR_$__GCUserNotificationConfiguration._checkBoxTitles
+ OBJC_IVAR_$__GCUserNotificationConfiguration._defaultButtonAccessibilityIdentifier
+ OBJC_IVAR_$__GCUserNotificationConfiguration._defaultButtonTitle
+ OBJC_IVAR_$__GCUserNotificationConfiguration._iconCleanupHandler
+ OBJC_IVAR_$__GCUserNotificationConfiguration._iconCleanupURL
+ OBJC_IVAR_$__GCUserNotificationConfiguration._iconURL
+ OBJC_IVAR_$__GCUserNotificationConfiguration._initiallyCheckedCheckBoxes
+ OBJC_IVAR_$__GCUserNotificationConfiguration._initiallySelectedPopUpItem
+ OBJC_IVAR_$__GCUserNotificationConfiguration._localizationURL
+ OBJC_IVAR_$__GCUserNotificationConfiguration._noDefaultButton
+ OBJC_IVAR_$__GCUserNotificationConfiguration._otherButtonAccessibilityIdentifier
+ OBJC_IVAR_$__GCUserNotificationConfiguration._otherButtonTitle
+ OBJC_IVAR_$__GCUserNotificationConfiguration._popUpTitles
+ OBJC_IVAR_$__GCUserNotificationConfiguration._progressIndicatorValue
+ OBJC_IVAR_$__GCUserNotificationConfiguration._secureTextFieldIndexes
+ OBJC_IVAR_$__GCUserNotificationConfiguration._soundCleanupHandler
+ OBJC_IVAR_$__GCUserNotificationConfiguration._soundCleanupURL
+ OBJC_IVAR_$__GCUserNotificationConfiguration._soundURL
+ OBJC_IVAR_$__GCUserNotificationConfiguration._textFieldDefaultValues
+ OBJC_IVAR_$__GCUserNotificationConfiguration._textFieldTitles
+ OBJC_IVAR_$__GCUserNotificationConfiguration._timeout
+ OBJC_IVAR_$__GCUserNotificationConfiguration._useRadioButtons
+ OBJC_IVAR_$__GCUserNotificationManagerEntry._configuration
+ OBJC_IVAR_$__GCUserNotificationManagerEntry._notification
+ OBJC_IVAR_$__GCUserNotificationManagerEntry._promise
+ OBJC_IVAR_$__GCUserNotificationManagerEntry._request
+ OBJC_IVAR_$__GCUserNotificationManagerEntry._source
+ OBJC_IVAR_$__GCUserNotificationManagerEntry._terminated
+ OBJC_IVAR_$__GCUserNotificationXPCProxyClientPresentationClient._cancelled
+ OBJC_IVAR_$__GCUserNotificationXPCProxyClientPresentationClient._lock
+ OBJC_IVAR_$__GCUserNotificationXPCProxyClientPresentationClient._promise
+ OBJC_IVAR_$__GCUserNotificationXPCProxyClientPresentationClient._serverHandle
+ OBJC_IVAR_$__GCUserNotificationXPCProxyClientPresentationClient._terminated
+ OBJC_IVAR_$__GCUserNotificationXPCProxyServerPresentationServer._future
+ _CFRunLoopAddSource
+ _CFRunLoopGetCurrent
+ _CFRunLoopRemoveSource
+ _CFRunLoopRunInMode
+ _CFRunLoopSourceCreate
+ _CFRunLoopSourceInvalidate
+ _CFRunLoopStop
+ _CFUserNotificationCancel
+ _CFUserNotificationCreate
+ _CFUserNotificationCreateRunLoopSource
+ _CFUserNotificationGetResponseDictionary
+ _CGImageDestinationAddImage
+ _CGImageDestinationCreateWithURL
+ _CGImageDestinationFinalize
+ _GCGameIntentAction_Classes
+ _GCGameIntentErrorDomain
+ _GCUserNotificationCFErrorKey
+ _GCUserNotificationErrorDomain
+ _GCUserNotificationRequest_Classes
+ _GCUserNotificationXPCClientInterface
+ _GCUserNotificationXPCPresentationClientInterface
+ _GCUserNotificationXPCPresentationServerInterface
+ _GCUserNotificationXPCServerInterface
+ _NSTemporaryDirectory
+ _NSUnderlyingErrorKey
+ _OBJC_CLASS_$_GCControllerLowBatteryNotification
+ _OBJC_CLASS_$_GCGameIntentLaunchAppleGamesAction
+ _OBJC_CLASS_$_GCGameIntentLaunchApplicationAction
+ _OBJC_CLASS_$_GCGameIntentOpenPlatformGameLibraryAction
+ _OBJC_CLASS_$_GCGameIntentShowAppleGameOverlayAction
+ _OBJC_CLASS_$_GCHomeButtonPermissionUserNotification
+ _OBJC_CLASS_$_GCSpatialControllerHSUserNotification
+ _OBJC_CLASS_$_GCUserNotificationManager
+ _OBJC_CLASS_$_GCUserNotificationResponse
+ _OBJC_CLASS_$_GCUserNotificationXPCProxyClient
+ _OBJC_CLASS_$_IFColor
+ _OBJC_CLASS_$_ISGraphicIconConfiguration
+ _OBJC_CLASS_$_ISIcon
+ _OBJC_CLASS_$_ISIconDecoration
+ _OBJC_CLASS_$_ISImageDescriptor
+ _OBJC_CLASS_$_NSFileManager
+ _OBJC_CLASS_$_NSIndexSet
+ _OBJC_CLASS_$_NSMutableIndexSet
+ _OBJC_CLASS_$__GCUserNotificationConfiguration
+ _OBJC_CLASS_$__GCUserNotificationManagerEntry
+ _OBJC_CLASS_$__GCUserNotificationXPCProxyClientPresentationClient
+ _OBJC_CLASS_$__GCUserNotificationXPCProxyServerPresentationServer
+ _OBJC_METACLASS_$_GCControllerLowBatteryNotification
+ _OBJC_METACLASS_$_GCGameIntentLaunchAppleGamesAction
+ _OBJC_METACLASS_$_GCGameIntentLaunchApplicationAction
+ _OBJC_METACLASS_$_GCGameIntentOpenPlatformGameLibraryAction
+ _OBJC_METACLASS_$_GCGameIntentShowAppleGameOverlayAction
+ _OBJC_METACLASS_$_GCHomeButtonPermissionUserNotification
+ _OBJC_METACLASS_$_GCSpatialControllerHSUserNotification
+ _OBJC_METACLASS_$_GCUserNotificationManager
+ _OBJC_METACLASS_$_GCUserNotificationResponse
+ _OBJC_METACLASS_$_GCUserNotificationXPCProxyClient
+ _OBJC_METACLASS_$__GCUserNotificationConfiguration
+ _OBJC_METACLASS_$__GCUserNotificationManagerEntry
+ _OBJC_METACLASS_$__GCUserNotificationXPCProxyClientPresentationClient
+ _OBJC_METACLASS_$__GCUserNotificationXPCProxyServerPresentationServer
+ _UTTypePNG
+ __38-[GCGameIntentManager _runNextAction:]_block_invoke
+ __70-[GCUserNotificationXPCProxyClient presentUserNotificationForRequest:]_block_invoke
+ __GCNoopRunLoopSourcePerform
+ __GCUserNotificationCallout
+ __OBJC_$_CATEGORY_NSError_$_GCUserNotificationErrorDomain
+ __OBJC_$_CLASS_METHODS_GCControllerLowBatteryNotification
+ __OBJC_$_CLASS_METHODS_GCGameIntentLaunchAppleGamesAction
+ __OBJC_$_CLASS_METHODS_GCGameIntentLaunchApplicationAction
+ __OBJC_$_CLASS_METHODS_GCGameIntentOpenPlatformGameLibraryAction
+ __OBJC_$_CLASS_METHODS_GCGameIntentShowAppleGameOverlayAction
+ __OBJC_$_CLASS_METHODS_GCHomeButtonPermissionUserNotification
+ __OBJC_$_CLASS_METHODS_GCSpatialControllerHSUserNotification
+ __OBJC_$_CLASS_METHODS_GCUserNotificationResponse
+ __OBJC_$_CLASS_METHODS_NSError(GCUserNotificationErrorDomain|GCSessionErrorDomain)
+ __OBJC_$_CLASS_METHODS__GCUserNotificationConfiguration
+ __OBJC_$_CLASS_PROP_LIST_GCControllerLowBatteryNotification
+ __OBJC_$_CLASS_PROP_LIST_GCGameIntentLaunchAppleGamesAction
+ __OBJC_$_CLASS_PROP_LIST_GCGameIntentLaunchApplicationAction
+ __OBJC_$_CLASS_PROP_LIST_GCGameIntentOpenPlatformGameLibraryAction
+ __OBJC_$_CLASS_PROP_LIST_GCGameIntentShowAppleGameOverlayAction
+ __OBJC_$_CLASS_PROP_LIST_GCHomeButtonPermissionUserNotification
+ __OBJC_$_CLASS_PROP_LIST_GCSpatialControllerHSUserNotification
+ __OBJC_$_CLASS_PROP_LIST_GCUserNotificationResponse
+ __OBJC_$_INSTANCE_METHODS_GCControllerLowBatteryNotification
+ __OBJC_$_INSTANCE_METHODS_GCGameIntentLaunchAppleGamesAction
+ __OBJC_$_INSTANCE_METHODS_GCGameIntentLaunchApplicationAction
+ __OBJC_$_INSTANCE_METHODS_GCGameIntentOpenPlatformGameLibraryAction
+ __OBJC_$_INSTANCE_METHODS_GCGameIntentShowAppleGameOverlayAction
+ __OBJC_$_INSTANCE_METHODS_GCHomeButtonPermissionUserNotification
+ __OBJC_$_INSTANCE_METHODS_GCSpatialControllerHSUserNotification
+ __OBJC_$_INSTANCE_METHODS_GCUserNotificationManager(XPCProxy)
+ __OBJC_$_INSTANCE_METHODS_GCUserNotificationResponse
+ __OBJC_$_INSTANCE_METHODS_GCUserNotificationXPCProxyClient
+ __OBJC_$_INSTANCE_METHODS__GCUserNotificationConfiguration
+ __OBJC_$_INSTANCE_METHODS__GCUserNotificationManagerEntry
+ __OBJC_$_INSTANCE_METHODS__GCUserNotificationXPCProxyClientPresentationClient
+ __OBJC_$_INSTANCE_METHODS__GCUserNotificationXPCProxyServerPresentationServer
+ __OBJC_$_INSTANCE_VARIABLES_GCControllerLowBatteryNotification
+ __OBJC_$_INSTANCE_VARIABLES_GCGameIntentLaunchApplicationAction
+ __OBJC_$_INSTANCE_VARIABLES_GCGameIntentShowAppleGameOverlayAction
+ __OBJC_$_INSTANCE_VARIABLES_GCHomeButtonPermissionUserNotification
+ __OBJC_$_INSTANCE_VARIABLES_GCUserNotificationManager
+ __OBJC_$_INSTANCE_VARIABLES_GCUserNotificationResponse
+ __OBJC_$_INSTANCE_VARIABLES_GCUserNotificationXPCProxyClient
+ __OBJC_$_INSTANCE_VARIABLES__GCUserNotificationConfiguration
+ __OBJC_$_INSTANCE_VARIABLES__GCUserNotificationManagerEntry
+ __OBJC_$_INSTANCE_VARIABLES__GCUserNotificationXPCProxyClientPresentationClient
+ __OBJC_$_INSTANCE_VARIABLES__GCUserNotificationXPCProxyServerPresentationServer
+ __OBJC_$_PROP_LIST_GCControllerLowBatteryNotification
+ __OBJC_$_PROP_LIST_GCGameIntentLaunchAppleGamesAction
+ __OBJC_$_PROP_LIST_GCGameIntentLaunchApplicationAction
+ __OBJC_$_PROP_LIST_GCGameIntentOpenPlatformGameLibraryAction
+ __OBJC_$_PROP_LIST_GCGameIntentShowAppleGameOverlayAction
+ __OBJC_$_PROP_LIST_GCHomeButtonPermissionUserNotification
+ __OBJC_$_PROP_LIST_GCSpatialControllerHSUserNotification
+ __OBJC_$_PROP_LIST_GCSystemButtonArbitrationService
+ __OBJC_$_PROP_LIST_GCUserNotificationConfiguration
+ __OBJC_$_PROP_LIST_GCUserNotificationResponse
+ __OBJC_$_PROP_LIST_GCUserNotificationXPCProxyClient
+ __OBJC_$_PROP_LIST__GCUserNotificationConfiguration
+ __OBJC_$_PROP_LIST__GCUserNotificationManagerEntry
+ __OBJC_$_PROP_LIST__GCUserNotificationXPCProxyClientPresentationClient
+ __OBJC_$_PROP_LIST__GCUserNotificationXPCProxyServerPresentationServer
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_GCGameIntentAction
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_GCSystemButtonArbitrationService
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_GCUserNotificationConfiguration
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_GCUserNotificationRequest
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_GCUserNotificationService
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_GCUserNotificationXPCPresentationClientInterface
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_GCUserNotificationXPCPresentationServerInterface
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_GCUserNotificationXPCServerInterface
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_OPT_GCGameIntentAction
+ __OBJC_$_PROTOCOL_METHOD_TYPES_GCGameIntentAction
+ __OBJC_$_PROTOCOL_METHOD_TYPES_GCSystemButtonArbitrationService
+ __OBJC_$_PROTOCOL_METHOD_TYPES_GCUserNotificationConfiguration
+ __OBJC_$_PROTOCOL_METHOD_TYPES_GCUserNotificationRequest
+ __OBJC_$_PROTOCOL_METHOD_TYPES_GCUserNotificationService
+ __OBJC_$_PROTOCOL_METHOD_TYPES_GCUserNotificationXPCPresentationClientInterface
+ __OBJC_$_PROTOCOL_METHOD_TYPES_GCUserNotificationXPCPresentationServerInterface
+ __OBJC_$_PROTOCOL_METHOD_TYPES_GCUserNotificationXPCServerInterface
+ __OBJC_$_PROTOCOL_REFS_GCGameIntentAction
+ __OBJC_$_PROTOCOL_REFS_GCSystemButtonArbitrationService
+ __OBJC_$_PROTOCOL_REFS_GCUserNotificationConfiguration
+ __OBJC_$_PROTOCOL_REFS_GCUserNotificationRequest
+ __OBJC_$_PROTOCOL_REFS_GCUserNotificationService
+ __OBJC_$_PROTOCOL_REFS_GCUserNotificationXPCClientInterface
+ __OBJC_$_PROTOCOL_REFS_GCUserNotificationXPCPresentationClientInterface
+ __OBJC_$_PROTOCOL_REFS_GCUserNotificationXPCPresentationServerInterface
+ __OBJC_$_PROTOCOL_REFS_GCUserNotificationXPCServerInterface
+ __OBJC_CLASS_PROTOCOLS_$_GCControllerLowBatteryNotification
+ __OBJC_CLASS_PROTOCOLS_$_GCGameIntentLaunchAppleGamesAction
+ __OBJC_CLASS_PROTOCOLS_$_GCGameIntentLaunchApplicationAction
+ __OBJC_CLASS_PROTOCOLS_$_GCGameIntentOpenPlatformGameLibraryAction
+ __OBJC_CLASS_PROTOCOLS_$_GCGameIntentShowAppleGameOverlayAction
+ __OBJC_CLASS_PROTOCOLS_$_GCHomeButtonPermissionUserNotification
+ __OBJC_CLASS_PROTOCOLS_$_GCSpatialControllerHSUserNotification
+ __OBJC_CLASS_PROTOCOLS_$_GCUserNotificationManager(XPCProxy)
+ __OBJC_CLASS_PROTOCOLS_$_GCUserNotificationResponse
+ __OBJC_CLASS_PROTOCOLS_$_GCUserNotificationXPCProxyClient
+ __OBJC_CLASS_PROTOCOLS_$__GCUserNotificationConfiguration
+ __OBJC_CLASS_PROTOCOLS_$__GCUserNotificationXPCProxyClientPresentationClient
+ __OBJC_CLASS_PROTOCOLS_$__GCUserNotificationXPCProxyServerPresentationServer
+ __OBJC_CLASS_RO_$_GCControllerLowBatteryNotification
+ __OBJC_CLASS_RO_$_GCGameIntentLaunchAppleGamesAction
+ __OBJC_CLASS_RO_$_GCGameIntentLaunchApplicationAction
+ __OBJC_CLASS_RO_$_GCGameIntentOpenPlatformGameLibraryAction
+ __OBJC_CLASS_RO_$_GCGameIntentShowAppleGameOverlayAction
+ __OBJC_CLASS_RO_$_GCHomeButtonPermissionUserNotification
+ __OBJC_CLASS_RO_$_GCSpatialControllerHSUserNotification
+ __OBJC_CLASS_RO_$_GCUserNotificationManager
+ __OBJC_CLASS_RO_$_GCUserNotificationResponse
+ __OBJC_CLASS_RO_$_GCUserNotificationXPCProxyClient
+ __OBJC_CLASS_RO_$__GCUserNotificationConfiguration
+ __OBJC_CLASS_RO_$__GCUserNotificationManagerEntry
+ __OBJC_CLASS_RO_$__GCUserNotificationXPCProxyClientPresentationClient
+ __OBJC_CLASS_RO_$__GCUserNotificationXPCProxyServerPresentationServer
+ __OBJC_LABEL_PROTOCOL_$_GCGameIntentAction
+ __OBJC_LABEL_PROTOCOL_$_GCSystemButtonArbitrationService
+ __OBJC_LABEL_PROTOCOL_$_GCUserNotificationConfiguration
+ __OBJC_LABEL_PROTOCOL_$_GCUserNotificationRequest
+ __OBJC_LABEL_PROTOCOL_$_GCUserNotificationService
+ __OBJC_LABEL_PROTOCOL_$_GCUserNotificationXPCClientInterface
+ __OBJC_LABEL_PROTOCOL_$_GCUserNotificationXPCPresentationClientInterface
+ __OBJC_LABEL_PROTOCOL_$_GCUserNotificationXPCPresentationServerInterface
+ __OBJC_LABEL_PROTOCOL_$_GCUserNotificationXPCServerInterface
+ __OBJC_METACLASS_RO_$_GCControllerLowBatteryNotification
+ __OBJC_METACLASS_RO_$_GCGameIntentLaunchAppleGamesAction
+ __OBJC_METACLASS_RO_$_GCGameIntentLaunchApplicationAction
+ __OBJC_METACLASS_RO_$_GCGameIntentOpenPlatformGameLibraryAction
+ __OBJC_METACLASS_RO_$_GCGameIntentShowAppleGameOverlayAction
+ __OBJC_METACLASS_RO_$_GCHomeButtonPermissionUserNotification
+ __OBJC_METACLASS_RO_$_GCSpatialControllerHSUserNotification
+ __OBJC_METACLASS_RO_$_GCUserNotificationManager
+ __OBJC_METACLASS_RO_$_GCUserNotificationResponse
+ __OBJC_METACLASS_RO_$_GCUserNotificationXPCProxyClient
+ __OBJC_METACLASS_RO_$__GCUserNotificationConfiguration
+ __OBJC_METACLASS_RO_$__GCUserNotificationManagerEntry
+ __OBJC_METACLASS_RO_$__GCUserNotificationXPCProxyClientPresentationClient
+ __OBJC_METACLASS_RO_$__GCUserNotificationXPCProxyServerPresentationServer
+ __OBJC_PROTOCOL_$_GCGameIntentAction
+ __OBJC_PROTOCOL_$_GCSystemButtonArbitrationService
+ __OBJC_PROTOCOL_$_GCUserNotificationConfiguration
+ __OBJC_PROTOCOL_$_GCUserNotificationRequest
+ __OBJC_PROTOCOL_$_GCUserNotificationService
+ __OBJC_PROTOCOL_$_GCUserNotificationXPCClientInterface
+ __OBJC_PROTOCOL_$_GCUserNotificationXPCPresentationClientInterface
+ __OBJC_PROTOCOL_$_GCUserNotificationXPCPresentationServerInterface
+ __OBJC_PROTOCOL_$_GCUserNotificationXPCServerInterface
+ __OBJC_PROTOCOL_REFERENCE_$_GCGameIntentLauncherService
+ __OBJC_PROTOCOL_REFERENCE_$_GCSystemButtonArbitrationService
+ __OBJC_PROTOCOL_REFERENCE_$_GCUserNotificationXPCClientInterface
+ __OBJC_PROTOCOL_REFERENCE_$_GCUserNotificationXPCPresentationClientInterface
+ __OBJC_PROTOCOL_REFERENCE_$_GCUserNotificationXPCPresentationServerInterface
+ __OBJC_PROTOCOL_REFERENCE_$_GCUserNotificationXPCServerInterface
+ ___106-[_GCAgentClientProxy _initWithConnection:server:userDefaultsProxy:gameIntentProxy:userNotificationProxy:]_block_invoke
+ ___38-[GCGameIntentManager _runNextAction:]_block_invoke
+ ___63-[GCUserNotificationManager presentUserNotificationForRequest:]_block_invoke
+ ___63-[GCUserNotificationManager presentUserNotificationForRequest:]_block_invoke_2
+ ___68-[GCHomeButtonPermissionUserNotification prepareNotification:error:]_block_invoke
+ ___70-[GCUserNotificationXPCProxyClient presentUserNotificationForRequest:]_block_invoke
+ ___70-[GCUserNotificationXPCProxyClient presentUserNotificationForRequest:]_block_invoke_2
+ ___80-[_GCAgentClientProxy connectToUserNotificationXPCProxyServiceWithClient:reply:]_block_invoke
+ ___86-[GCUserNotificationManager(XPCProxy) presentUserNotificationForRequest:client:reply:]_block_invoke
+ ___GCGameIntentAction_Classes_block_invoke
+ ___GCUserNotificationRequest_Classes_block_invoke
+ ____gc_log_game_intent_block_invoke
+ ____gc_log_user_notification_block_invoke
+ ___block_descriptor_32_e15_v16?0"NSURL"8l
+ ___block_descriptor_40_e8_32s_e51_v32?0q8"GCUserNotificationResponse"16"NSError"24ls32l8
+ ___block_descriptor_48_e8_32s40s_e19_v16?0"GCPromise"8ls32l8s40l8
+ ___block_descriptor_48_e8_32s40s_e33_v32?0q8"NSNumber"16"NSError"24ls32l8s40l8
+ ___block_descriptor_48_e8_32s40s_e72_v24?0"<GCUserNotificationXPCPresentationServerInterface>"8"NSError"16ls32l8s40l8
+ ___block_descriptor_60_e8_32s40w_e46_v28?0Q8"NSObject<OS_dispatch_mach_msg>"16i24lw40l8s32l8
+ __gc_log_game_intent
+ __gc_log_user_notification
+ _dispatch_queue_attr_make_with_overcommit
+ _gc_log_game_intent
+ _gc_log_game_intent.Log
+ _gc_log_game_intent.onceToken
+ _gc_log_user_notification
+ _gc_log_user_notification.Log
+ _gc_log_user_notification.onceToken
+ _kCFRunLoopDefaultMode
+ _kCFUserNotificationAlertHeaderKey
+ _kCFUserNotificationAlertMessageKey
+ _kCFUserNotificationAlertTopMostKey
+ _kCFUserNotificationAlternateButtonTitleKey
+ _kCFUserNotificationCheckBoxTitlesKey
+ _kCFUserNotificationDefaultButtonTitleKey
+ _kCFUserNotificationIconURLKey
+ _kCFUserNotificationLocalizationURLKey
+ _kCFUserNotificationOtherButtonTitleKey
+ _kCFUserNotificationPopUpTitlesKey
+ _kCFUserNotificationProgressIndicatorValueKey
+ _kCFUserNotificationSoundURLKey
+ _kCFUserNotificationTextFieldTitlesKey
+ _kCFUserNotificationTextFieldValuesKey
+ _kEntryAssociatedKey
+ _objc_msgSend$CGImage
+ _objc_msgSend$GameControllerFoundationBundle
+ _objc_msgSend$_cancelEntry:
+ _objc_msgSend$_enqueueEntry:
+ _objc_msgSend$_initWithConnection:server:userDefaultsProxy:gameIntentProxy:userNotificationProxy:
+ _objc_msgSend$_onrunloop_finalizeEntry:
+ _objc_msgSend$_onrunloop_handleResponseForNotification:responseFlags:
+ _objc_msgSend$_onrunloop_pump
+ _objc_msgSend$_terminate
+ _objc_msgSend$_ui_configureNotificationDictionary:
+ _objc_msgSend$addIndex:
+ _objc_msgSend$cancelPresentation
+ _objc_msgSend$checkBoxCount
+ _objc_msgSend$checkExceptionForApp:parent:
+ _objc_msgSend$checkSystemGestureEnabled
+ _objc_msgSend$code
+ _objc_msgSend$copyNotificationDictionary
+ _objc_msgSend$currentThread
+ _objc_msgSend$defaultManager
+ _objc_msgSend$dismissAction
+ _objc_msgSend$domain
+ _objc_msgSend$firstIndex
+ _objc_msgSend$future
+ _objc_msgSend$futureWithError:
+ _objc_msgSend$gc_userNotificationError:userInfo:
+ _objc_msgSend$hasPopUp
+ _objc_msgSend$iconWithDecorations:
+ _objc_msgSend$imageForDescriptor:
+ _objc_msgSend$indexGreaterThanIndex:
+ _objc_msgSend$indexOfObjectIdenticalTo:
+ _objc_msgSend$initWithChirality:batteryLevel:
+ _objc_msgSend$initWithConditional:
+ _objc_msgSend$initWithDismissAction:textFieldValues:checkedCheckBoxes:popUpSelection:
+ _objc_msgSend$initWithFuture:
+ _objc_msgSend$initWithPromise:
+ _objc_msgSend$initWithRequest:promise:
+ _objc_msgSend$initWithSize:scale:
+ _objc_msgSend$initWithSystemColor:
+ _objc_msgSend$initWithTarget:selector:object:
+ _objc_msgSend$initWithType:
+ _objc_msgSend$isEqualToIndexSet:
+ _objc_msgSend$localizedStringForKey:value:table:
+ _objc_msgSend$notification
+ _objc_msgSend$observeCancellation:
+ _objc_msgSend$observeFinish:
+ _objc_msgSend$performAction
+ _objc_msgSend$performActions:
+ _objc_msgSend$performSelector:onThread:withObject:waitUntilDone:
+ _objc_msgSend$placeholder
+ _objc_msgSend$prepareImageForDescriptor:
+ _objc_msgSend$prepareNotification:error:
+ _objc_msgSend$presentUserNotificationForRequest:
+ _objc_msgSend$presentUserNotificationForRequest:client:reply:
+ _objc_msgSend$presentationDidCancel
+ _objc_msgSend$presentationDidFailWithError:
+ _objc_msgSend$presentationDidSucceedWithResponse:
+ _objc_msgSend$promise
+ _objc_msgSend$refreshActiveServer
+ _objc_msgSend$removeItemAtURL:error:
+ _objc_msgSend$request
+ _objc_msgSend$requestFlags
+ _objc_msgSend$runCleanupHandlers
+ _objc_msgSend$setAlertHeader:
+ _objc_msgSend$setAlertLevel:
+ _objc_msgSend$setAlertMessage:
+ _objc_msgSend$setAlternateButtonTitle:
+ _objc_msgSend$setDefaultButtonTitle:
+ _objc_msgSend$setEnclosureColors:
+ _objc_msgSend$setIconURL:
+ _objc_msgSend$setIconURL:withCleanupHandler:
+ _objc_msgSend$setName:
+ _objc_msgSend$setNoDefaultButton:
+ _objc_msgSend$setNotification:
+ _objc_msgSend$setPosition:
+ _objc_msgSend$setQualityOfService:
+ _objc_msgSend$setRenderingMode:
+ _objc_msgSend$setServerHandle:
+ _objc_msgSend$setSoundURL:
+ _objc_msgSend$setSource:
+ _objc_msgSend$setSymbolColors:
+ _objc_msgSend$setTerminated:
+ _objc_msgSend$setTimeout:
+ _objc_msgSend$start
+ _objc_msgSend$terminated
+ _objc_msgSend$textFieldCount
+ _objc_msgSend$timeout
+ _objc_msgSend$tryMergeWithOther:
+ _objc_retain_x6
- +[_GCAgentClientProxy clientProxyWithConnection:server:userDefaultsProxy:gameIntentProxy:]
- -[GCGameIntentLauncherXPCProxyClient launchApplicationWithBundleIdentifier:]
- -[GCGameIntentLauncherXPCProxyClient togglePlatformGamesLibrary]
- -[GCGameIntentManager _ui_launchApplicationWithBundleIdentifier:]
- -[GCGameIntentManager dealloc]
- -[GCGameIntentManager launchApplicationWithBundleIdentifier:]
- -[GCGameIntentManager togglePlatformGamesLibrary]
- -[GCGameIntentManager ui_togglePlatformGamesLibrary]
- -[_GCAgentClientProxy _initWithConnection:server:userDefaultsProxy:gameIntentProxy:]
- OBJC_IVAR_$__GCDefaultLogicalDevice._systemShellLauncherService
- OBJC_IVAR_$__GCDefaultLogicalDevice._userDefaults
- _OBJC_CLASS_$_LSApplicationWorkspace
- __OBJC_$_CATEGORY_CLASS_METHODS_NSError_$_GCSessionErrorDomain
- __OBJC_$_CATEGORY_NSError_$_GCSessionErrorDomain
- ___84-[_GCAgentClientProxy _initWithConnection:server:userDefaultsProxy:gameIntentProxy:]_block_invoke
- ___block_descriptor_60_e8_32s_e46_v28?0Q8"NSObject<OS_dispatch_mach_msg>"16i24lu40l8s32l8
- _objc_msgSend$_initWithConnection:server:userDefaultsProxy:gameIntentProxy:
- _objc_msgSend$defaultWorkspace
- _objc_msgSend$launchApplicationWithBundleIdentifier:
- _objc_msgSend$openApplicationWithBundleID:
- _objc_msgSend$togglePlatformGamesLibrary
- _objc_msgSend$tryHandleButtonPress
- _objc_retain_x5
CStrings:
+ "#Mach message received during teardown"
+ "%d%%"
+ "(Agent Client) Connect 'User Notification XPC Proxy Service'"
+ "(LaunchApplication '$Games')"
+ "(LaunchApplication '%@')"
+ "(OpenPlatformGameLibrary)"
+ "(ShowOverlay)"
+ "<%@ %p; dismissAction=%ld textFields=%@ checked=%@ popUp=%ld>"
+ "BUG IN _GCDevicePhysicalInput: Recursive or concurrent mutation detected."
+ "Entry pulled from _pending should not be terminated"
+ "GCGameIntentError"
+ "GCHomeButtonPermission-%@.png"
+ "GCHomeButtonPermissionUserNotification: Failed to create CGImageDestination for %@."
+ "GCHomeButtonPermissionUserNotification: Failed to look up application record for %@: %@"
+ "GCHomeButtonPermissionUserNotification: Failed to render composite icon for %@."
+ "GCHomeButtonPermissionUserNotification: Failed to write composite icon to %@."
+ "GCHomeButtonPermissionUserNotification: Wrote icon to '%@'."
+ "GCUserNotificationCFError"
+ "GCUserNotificationError"
+ "GCUserNotificationManager.RunLoop"
+ "GCUserNotificationManager.m"
+ "GCUserNotificationXPCProxy - agent connection fully established for user %d /w %@"
+ "GCUserNotificationXPCProxy - new server"
+ "GCUserNotificationXPCProxy - new server is %@"
+ "GCUserNotificationXPCProxy - no server available, failing presentation"
+ "GCUserNotificationXPCProxy - refreshActiveServer for user %@"
+ "GCUserNotificationXPCProxy - server hasn't changed, early exit"
+ "GCUserNotificationXPCProxy - serverForCurrentUser %@ is nil, early exit"
+ "GameIntent"
+ "Must run on the runloop thread"
+ "NOTIFY_CONTROLLER_LOW_BATTERY_HEADER"
+ "NOTIFY_CONTROLLER_LOW_BATTERY_HEADER_LEFT"
+ "NOTIFY_CONTROLLER_LOW_BATTERY_HEADER_RIGHT"
+ "NOTIFY_CONTROLLER_LOW_BATTERY_MESSAGE"
+ "NOTIFY_HOME_BUTTON_PERMISSION_ACTION_ALLOW"
+ "NOTIFY_HOME_BUTTON_PERMISSION_ACTION_DENY"
+ "NOTIFY_HOME_BUTTON_PERMISSION_HEADER"
+ "NOTIFY_HOME_BUTTON_PERMISSION_MESSAGE_WITH_CHILDREN"
+ "NOTIFY_SPATIAL_CONTROLLER_HS_ACTION_CONTINUE"
+ "NOTIFY_SPATIAL_CONTROLLER_HS_ACTION_LEARN_MORE"
+ "NOTIFY_SPATIAL_CONTROLLER_HS_HEADER"
+ "NOTIFY_SPATIAL_CONTROLLER_HS_MESSAGE"
+ "Perform System Gesture Actions"
+ "Perform game intent action: %@"
+ "Perform system gesture actions: %@"
+ "Prepare %@"
+ "Prepare user notification '%@' failed with error: %@"
+ "Present %@"
+ "Received nil server in agentCheckIn!"
+ "Run loop thread should have exited before manager deallocation"
+ "Servers is now: %@"
+ "SpatialController"
+ "SyntheticDeviceManager.Upcall"
+ "UserNotification"
+ "[%@] #WARNING: Missing game intent."
+ "[%@] #WARNING: Missing system button arbitration."
+ "[%@] Computed new system gesture state {\n\t activeApplication = pid:%i (%@) (wants HOME: %{BOOL}d)\n\t parentApplication = pid:%i (%@) (wants HOME: %{BOOL}d)\n}"
+ "[%@] Shortcuts settings changed."
+ "bundleIdentifier"
+ "checkedCheckBoxes"
+ "chirality"
+ "com.apple.gamecontrollersettings.gamecontroller"
+ "conditional"
+ "dismissAction"
+ "popUpSelection"
+ "settingsGeneration"
+ "textFieldValues"
+ "v16@?0@\"NSURL\"8"
+ "v24@?0@\"<GCUserNotificationXPCPresentationServerInterface>\"8@\"NSError\"16"
+ "v32@?0q8@\"GCUserNotificationResponse\"16@\"NSError\"24"
+ "v32@?0q8@\"NSNumber\"16@\"NSError\"24"
- "0`"
- "BUG IN _GCDevicePhysicalInput: -handleEvent called recursively."
- "UI not loaded"
- "[%@] #WARNING: Missing user defaults."
- "[%@] Computed new system gesture state: {\n\t activeApplication = pid:%i (%@) (grants: %zx, wants HOME: %{BOOL}d)\n\t parentApplication = pid:%i (%@) (grants: %zx, wants HOME: %{BOOL}d)\n}"
- "[%@] Handled by consumer."
- "[%@] Shortcuts Enabled changed: %{public}@"
```
