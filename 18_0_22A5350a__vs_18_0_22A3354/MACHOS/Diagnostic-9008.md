## Diagnostic-9008

> `/Applications/DiagnosticsService.app/PlugIns/Diagnostic-9008.appex/Diagnostic-9008`

```diff

 625.2.2.0.0
-  __TEXT.__text: 0x7a8
-  __TEXT.__auth_stubs: 0x170
-  __TEXT.__objc_stubs: 0x320
-  __TEXT.__objc_methlist: 0xc4
-  __TEXT.__objc_methname: 0x431
-  __TEXT.__objc_classname: 0xa2
-  __TEXT.__objc_methtype: 0x16e
-  __TEXT.__const: 0x12
-  __TEXT.__oslogstring: 0xe
-  __TEXT.__cstring: 0x9d
-  __TEXT.__unwind_info: 0x80
-  __DATA_CONST.__auth_got: 0xc0
-  __DATA_CONST.__got: 0x30
-  __DATA_CONST.__cfstring: 0x40
-  __DATA_CONST.__objc_classlist: 0x18
-  __DATA_CONST.__objc_protolist: 0x20
+  __TEXT.__text: 0xb12c
+  __TEXT.__auth_stubs: 0x740
+  __TEXT.__objc_stubs: 0x1ce0
+  __TEXT.__objc_methlist: 0x62c
+  __TEXT.__objc_methname: 0x2185
+  __TEXT.__objc_classname: 0x13d
+  __TEXT.__objc_methtype: 0x99c
+  __TEXT.__const: 0x30a
+  __TEXT.__gcc_except_tab: 0x17c
+  __TEXT.__oslogstring: 0x947
+  __TEXT.__cstring: 0x94d
+  __TEXT.__dlopen_cstrs: 0x62
+  __TEXT.__swift5_typeref: 0x1a9
+  __TEXT.__swift5_reflstr: 0x36
+  __TEXT.__swift5_assocty: 0x48
+  __TEXT.__constg_swiftt: 0xc0
+  __TEXT.__swift5_fieldmd: 0x78
+  __TEXT.__swift5_proto: 0x28
+  __TEXT.__swift5_types: 0xc
+  __TEXT.__unwind_info: 0x300
+  __TEXT.__eh_frame: 0x74
+  __DATA_CONST.__auth_got: 0x3b0
+  __DATA_CONST.__got: 0x190
+  __DATA_CONST.__auth_ptr: 0x1a8
+  __DATA_CONST.__const: 0x4c8
+  __DATA_CONST.__cfstring: 0x7e0
+  __DATA_CONST.__objc_classlist: 0x40
+  __DATA_CONST.__objc_catlist: 0x8
+  __DATA_CONST.__objc_protolist: 0x30
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_superrefs: 0x8
-  __DATA_CONST.__objc_intobj: 0x30
-  __DATA.__objc_const: 0x6e8
-  __DATA.__objc_selrefs: 0x110
-  __DATA.__objc_ivar: 0x8
-  __DATA.__objc_data: 0xf0
-  __DATA.__data: 0x180
+  __DATA_CONST.__objc_superrefs: 0x28
+  __DATA_CONST.__objc_intobj: 0xd8
+  __DATA_CONST.__objc_arraydata: 0x70
+  __DATA_CONST.__objc_arrayobj: 0x90
+  __DATA.__objc_const: 0x1320
+  __DATA.__objc_selrefs: 0x838
+  __DATA.__objc_ivar: 0x74
+  __DATA.__objc_data: 0x230
+  __DATA.__data: 0x398
+  __DATA.__bss: 0x528
+  __DATA.__common: 0x8
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/Foundation.framework/Foundation
+  - /System/Library/Frameworks/SwiftUI.framework/SwiftUI
   - /System/Library/Frameworks/UIKit.framework/UIKit
   - /System/Library/PrivateFrameworks/AuthKit.framework/AuthKit
   - /System/Library/PrivateFrameworks/CoreRepairCore.framework/CoreRepairCore
   - /System/Library/PrivateFrameworks/DiagnosticsKit.framework/DiagnosticsKit
   - /System/Library/PrivateFrameworks/OnBoardingKit.framework/OnBoardingKit
   - /System/Library/PrivateFrameworks/RemoteUI.framework/RemoteUI
+  - /System/Library/PrivateFrameworks/SoftLinking.framework/SoftLinking
+  - /System/Library/PrivateFrameworks/UIFoundation.framework/UIFoundation
+  - /System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore
   - /usr/lib/libMobileGestalt.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 14
-  Symbols:   47
-  CStrings:  108
+  - /usr/lib/swift/libswiftAccelerate.dylib
+  - /usr/lib/swift/libswiftCompression.dylib
+  - /usr/lib/swift/libswiftCore.dylib
+  - /usr/lib/swift/libswiftCoreAudio.dylib
+  - /usr/lib/swift/libswiftCoreFoundation.dylib
+  - /usr/lib/swift/libswiftCoreImage.dylib
+  - /usr/lib/swift/libswiftDarwin.dylib
+  - /usr/lib/swift/libswiftDataDetection.dylib
+  - /usr/lib/swift/libswiftDispatch.dylib
+  - /usr/lib/swift/libswiftFileProvider.dylib
+  - /usr/lib/swift/libswiftMetal.dylib
+  - /usr/lib/swift/libswiftOSLog.dylib
+  - /usr/lib/swift/libswiftObjectiveC.dylib
+  - /usr/lib/swift/libswiftQuartzCore.dylib
+  - /usr/lib/swift/libswiftSpatial.dylib
+  - /usr/lib/swift/libswiftUniformTypeIdentifiers.dylib
+  - /usr/lib/swift/libswiftWebKit.dylib
+  - /usr/lib/swift/libswiftXPC.dylib
+  - /usr/lib/swift/libswift_Builtin_float.dylib
+  - /usr/lib/swift/libswift_errno.dylib
+  - /usr/lib/swift/libswift_math.dylib
+  - /usr/lib/swift/libswift_signal.dylib
+  - /usr/lib/swift/libswift_stdio.dylib
+  - /usr/lib/swift/libswift_time.dylib
+  - /usr/lib/swift/libswiftos.dylib
+  - /usr/lib/swift/libswiftsimd.dylib
+  - /usr/lib/swift/libswiftsys_time.dylib
+  - /usr/lib/swift/libswiftunistd.dylib
+  Functions: 290
+  Symbols:   186
+  CStrings:  657
 
Symbols:
+ _malloc_size
+ _objc_destroyWeak
+ _OBJC_CLASS_$_AKAppleIDAuthenticationContext
+ __NSConcreteStackBlock
+ __swift_FORCE_LOAD_$_swift_errno
+ __swift_FORCE_LOAD_$_swiftos
+ _abort_report_np
+ _dispatch_async
+ __swift_FORCE_LOAD_$_swiftUIKit
+ _objc_loadWeakRetained
+ _OBJC_CLASS_$_NSMutableDictionary
+ _OBJC_CLASS_$_NSMutableURLRequest
+ __swift_FORCE_LOAD_$_swiftAccelerate
+ _OBJC_METACLASS_$_ChimeraLockViewController
+ __swiftEmptyArrayStorage
+ __swift_FORCE_LOAD_$_swiftCompression
+ _memmove
+ _OBJC_CLASS_$_ActivationLockViewController
+ _OBJC_CLASS_$_CRPreflightController
+ _OBJC_CLASS_$_NSNumber
+ _OBJC_CLASS_$_RUIPage
+ _objc_alloc_init
+ _objc_release_x9
+ _objc_retain_x23
+ __swiftImmortalRefCount
+ _free
+ _swift_deallocClassInstance
+ _objc_release
+ _OBJC_CLASS_$_ChimeraLockViewController
+ ___objc_personality_v0
+ _OBJC_CLASS_$_AKAppleIDSession
+ __swift_FORCE_LOAD_$_swiftFileProvider
+ _objc_retain_x19
+ _swift_arrayInitWithCopy
+ _swift_beginAccess
+ _OBJC_CLASS_$_RUITableViewRow
+ _OBJC_CLASS_$_RemoteUIController
+ __swift_FORCE_LOAD_$_swiftQuartzCore
+ _dispatch_semaphore_wait
+ _OBJC_METACLASS_$_ActivationLockViewController
+ _OBJC_METACLASS_$_IDMSAuthenticator
+ __swift_FORCE_LOAD_$_swiftDataDetection
+ __swift_FORCE_LOAD_$_swift_signal
+ _OBJC_CLASS_$_IDMSAuthenticator
+ _OBJC_CLASS_$_OBBoldTrayButton
+ _swift_bridgeObjectRelease_n
+ _objc_copyWeak
+ _objc_retain_x22
+ _objc_retain_x26
+ _objc_storeWeak
+ _OBJC_CLASS_$_NSString
+ __dispatch_main_q
+ __swift_FORCE_LOAD_$_swiftObjectiveC
+ _swift_release
+ _OBJC_CLASS_$_NSArray
+ _objc_retainAutorelease
+ _objc_retain_x28
+ _OBJC_CLASS_$_OBHeaderAccessoryButton
+ _OBJC_CLASS_$_UIAlertController
+ __swiftEmptyDictionarySingleton
+ _objc_release_x24
+ _dispatch_time
+ _MGGetBoolAnswer
+ _OBJC_CLASS_$_UIImage
+ _OBJC_METACLASS_$_TokenChallenger
+ __swift_FORCE_LOAD_$_swiftsimd
+ _objc_release_x26
+ _objc_retain_x20
+ _OBJC_CLASS_$_NSURLSession
+ __sl_dlopen
+ __swift_FORCE_LOAD_$_swiftUniformTypeIdentifiers
+ _objc_retain_x1
+ _OBJC_CLASS_$_CRPreflightUtils
+ __swift_FORCE_LOAD_$_swiftSpatial
+ __swift_FORCE_LOAD_$_swiftunistd
+ _OBJC_CLASS_$__TtCs12_SwiftObject
+ _objc_retain_x25
+ _swift_getTypeByMangledNameInContext2
+ _NSStringFromClass
+ _OBJC_CLASS_$_NSURLComponents
+ __NSConcreteGlobalBlock
+ __swift_FORCE_LOAD_$_swift_time
+ __swift_FORCE_LOAD_$_swift_math
+ __swift_FORCE_LOAD_$_swiftMetal
+ __swift_FORCE_LOAD_$_swift_Builtin_float
+ _AKAuthenticationAlternateDSIDKey
+ _OBJC_CLASS_$_NSPropertyListSerialization
+ _OBJC_CLASS_$_OBLinkTrayButton
+ _OBJC_CLASS_$_RUIStyle
+ __swift_FORCE_LOAD_$_swiftCoreImage
+ _dispatch_semaphore_signal
+ __swift_FORCE_LOAD_$_swiftDarwin
+ __swift_FORCE_LOAD_$_swiftDispatch
+ _swift_bridgeObjectRelease
+ __Block_object_dispose
+ __Unwind_Resume
+ ___chkstk_darwin
+ __os_log_error_impl
+ __swift_FORCE_LOAD_$_swiftCoreFoundation
+ __swift_FORCE_LOAD_$_swiftFoundation
+ __swift_FORCE_LOAD_$_swiftOSLog
+ _OBJC_CLASS_$_NSConstantArray
+ _OBJC_CLASS_$_UIImageSymbolConfiguration
+ _objc_alloc
+ _objc_initWeak
+ _swift_getKeyPath
+ _objc_getClass
+ _objc_opt_new
+ _objc_opt_self
+ _OBJC_CLASS_$_UINavigationController
+ _objc_retain_x8
+ _swift_getTypeByMangledNameInContextInMetadataState2
+ _dispatch_semaphore_create
+ _objc_release_x28
+ _swift_allocObject
+ _AKAuthenticationIDMSTokenKey
+ _OBJC_CLASS_$_AKAppleIDAuthenticationController
+ _OBJC_CLASS_$_NSBundle
+ _objc_release_x27
+ _objc_retain_x4
+ __swift_FORCE_LOAD_$_swiftWebKit
+ __swift_FORCE_LOAD_$_swift_stdio
+ _swift_getWitnessTable
+ _swift_bridgeObjectRetain
+ _swift_getOpaqueTypeConformance2
+ _OBJC_CLASS_$_TokenChallenger
+ _OBJC_CLASS_$_UIAlertAction
+ _swift_retain
+ _OBJC_CLASS_$_NSLocale
+ _swift_endAccess
+ _swift_once
+ _OBJC_CLASS_$_NSMutableArray
+ _OBJC_CLASS_$_NSURLSessionConfiguration
+ _OBJC_METACLASS_$__TtCs12_SwiftObject
+ __swift_FORCE_LOAD_$_swiftXPC
+ _OBJC_CLASS_$_NSURL
+ __swift_FORCE_LOAD_$_swiftCoreAudio
+ __swift_FORCE_LOAD_$_swiftsys_time
+ _objc_unsafeClaimAutoreleasedReturnValue
CStrings:
+ "RKSignature"
+ "maskedAccount"
+ "preflightResponsePhase1"
+ "setPreflightResults:"
+ "@\"OBTextWelcomeController\""
+ "authKitSession"
+ "v24@0:8q16"
+ "URL"
+ "_state"
+ "setPreflightResponsePhase1:"
+ "ABOUT_ACTIVATION_BUTTON_TITLE"
+ "boldButton"
+ "firstObject"
+ "q32@0:8@16^@24"
+ "sharedSession"
+ "stringWithFormat:"
+ "v32@?0@\"RUIObjectModel\"8@\"RUIElement\"16@\"NSDictionary\"24"
+ "ACTIVATION_LOCK_INFO_TEXT"
+ "en"
+ "iphone.slash"
+ "@\"NSData\""
+ "Preflight phase 2 time out"
+ "URLWithString:"
+ "baseURL:"
+ "Failed to construct request: %!l(MISSING)d"
+ "Push at illegal state %!l(MISSING)d"
+ "START_ACTIVATION_BUTTON_TITLE"
+ "bundleIdentifier"
+ "ActivationLockViewController"
+ "T@\"NSData\",&,N,V_preflightBaaCert"
+ "_preflightBaaCert"
+ "addTarget:action:forControlEvents:"
+ "v32@0:8@\"RemoteUIController\"16@\"UINavigationController\"24"
+ "@48@0:8@16q24@32@40"
+ "TB,N,V_isTokenUnlocked"
+ "_buttonEventMonitor"
+ "_preflightResponsePhase1"
+ "fetchPasswordScreen"
+ "fetchPasswordWithCompletion:"
+ "setComponents:"
+ "tableCell"
+ "authenticator"
+ "Authenticating user credentials..."
+ "containsObject:"
+ "localizedComponents"
+ "preferredLanguages"
+ "pushViewController:animated:"
+ "v36@0:8@\"RemoteUIController\"16@\"RUIObjectModel\"24B32"
+ "Token unlocked"
+ "allHTTPHeaderFields"
+ "login"
+ "softlink:o:path:/System/Library/PrivateFrameworks/DiagnosticsSupport.framework/DiagnosticsSupport"
+ "Request URL: %!{(MISSING)public}@"
+ "allHeaderFields"
+ "removeTarget:"
+ "view"
+ "Preflight phase 1 failed"
+ "RKCertification"
+ "T@\"NSMutableArray\",&,N,V_viewControllers"
+ "learnMoreController"
+ "setTitle:forState:"
+ "uiNeededKnownSemaphore"
+ "StartPreflightPlugin-Release"
+ "-[ActivationLockViewController viewDidLoad]"
+ "@\"NSMutableDictionary\""
+ "Got push action"
+ "_dismissLearnMoreTapped"
+ "remoteUIController:willLoadRequest:"
+ "setActivationLockChallengeNeeded:"
+ "status"
+ "v32@0:8@\"RemoteUIController\"16@\"NSHTTPURLResponse\"24"
+ "v32@?0@\"NSData\"8@\"NSURLResponse\"16@\"NSError\"24"
+ "-[ActivationLockViewController _startActivateTapped]"
+ "v40@0:8@\"RemoteUIController\"16@\"NSHTTPURLResponse\"24@\"NSURLRequest\"32"
+ "Empty response"
+ "T@\"NSData\",&,N,V_preflightRIK"
+ "T@\"NSURL\",&,N,V_endpoint"
+ "remoteUIController:didFinishLoadWithError:"
+ "T@\"NSArray\",&,N,V_chimeraLockComponents"
+ "T@\"NSURL\",&,N,V_endpointBaseURL"
+ "setRequestCachePolicy:"
+ "B16@?0@\"RUIElement\"8"
+ "addTarget:action:forButtonEvents:propagate:"
+ "UNKNOWN_ERROR_ALERT_ACTION"
+ "Unable to find class %!s(MISSING)"
+ "setDelegate:"
+ "B40@0:8@\"RemoteUIController\"16@\"NSMutableURLRequest\"24@\"NSURLResponse\"32"
+ "Preflight phase 2 success: %!d(MISSING)"
+ "_uiNeededKnownSemaphore"
+ "q24@0:8@16"
+ "v28@?0B8@\"NSDictionary\"12@\"NSError\"20"
+ "-[ActivationLockViewController remoteUIController:didFinishLoadWithError:forRequest:]"
+ "addEntriesFromDictionary:"
+ "showUserAuthErrorAlert"
+ "viewDidAppear:"
+ "Error fetching password screen"
+ "Failed to sign payload"
+ "T@\"NSArray\",&,N,V_tokenChallengers"
+ "_isTokenUnlocked"
+ "q24@0:8@\"UINavigationController\"16"
+ "skip tapped"
+ "Array length mismatch: %!l(MISSING)d %!l(MISSING)d"
+ "_authenticator"
+ "_navigationController"
+ "activationResults:"
+ "-[ActivationLockViewController _dismissLearnMoreTapped]"
+ "Got load error at illegal state %!l(MISSING)d"
+ "Payload"
+ "_remoteUIController"
+ "addButton:"
+ "count"
+ "resume"
+ "set_appleIDContext:"
+ "v24@0:8@?16"
+ "-[ChimeraLockViewController _continueTapped]"
+ "@\"<StartPreflightSigner>\""
+ "next"
+ "no challenger"
+ "v32@0:8@\"RemoteUIController\"16@\"NSError\"24"
+ "CONTINUE_BUTTON_TITLE"
+ "Failed to serialize payload: %!@(MISSING)"
+ "MULTI_OWNER_MULTI_ACTIVATION_LOCK_TEXT"
+ "isTokenUnlocked"
+ "\x16"
+ "No password field"
+ "Response Headers: %!{(MISSING)public}@"
+ "containsString:"
+ "initWithIdentifier:"
+ "Got dismiss action with status %!@(MISSING)"
+ "alertControllerWithTitle:message:preferredStyle:"
+ "setPreflightBaaCert:"
+ "@\"<UIViewControllerInteractiveTransitioning>\"32@0:8@\"UINavigationController\"16@\"<UIViewControllerAnimatedTransitioning>\"24"
+ "Waiting for IDMS"
+ "activeTokenChallenger"
+ "Failed to fetch token: %!l(MISSING)d"
+ "Got unknown action"
+ "_constructAlbertRequest:objectModel:username:altDSID:gsToken:"
+ "attributes"
+ "-[StartPreflightViewController shouldPresentInHostApp]"
+ "Accept-Language"
+ "Empty data"
+ "T@\"NSDictionary\",&,N,V_preflightResults"
+ "T@\"OBTextWelcomeController\",&,N,V_learnMoreController"
+ "no component"
+ "setChimeraLockComponents:"
+ "setStyle:"
+ "token"
+ "Invalid type of SPCs"
+ "Move to next view"
+ "setViewControllers:animated:"
+ "\x13\x12"
+ "3kmXfug8VcxLI5yEmsqQKw"
+ "_skipActivateTapped"
+ "parts"
+ "setQuery:"
+ "setServiceType:"
+ "state"
+ "mainBundle"
+ "spc"
+ "<%!@(MISSING): token = %!@(MISSING), components = %!@(MISSING)>"
+ "IDMS authentication failed: %!l(MISSING)d"
+ "T@\"NSObject<OS_dispatch_semaphore>\",&,N,V_uiNeededKnownSemaphore"
+ "_TtC15Diagnostic_900823ComponentsMapDataSource"
+ "identifier"
+ "setupActivationLockView"
+ "AUTH_ERROR_ALERT_TITLE"
+ "MULTI_OWNER_MULTI_ACTIVATION_LOCK_TITLE"
+ "No email field"
+ "navigationController:willShowViewController:animated:"
+ "spcResults:"
+ "startWithPriority:completion:"
+ "v24@?0@\"NSDictionary\"8@\"NSError\"16"
+ "@\"IDMSAuthenticator\""
+ "@40@0:8@16@24@32"
+ "activeTokenChallengerIndex"
+ "startRequest:session:completion:"
+ "T@\"NSArray\",&,N,V_components"
+ "TQ,N,V_activeTokenChallengerIndex"
+ "didMoveToParentViewController:"
+ "objectAtIndexedSubscript:"
+ "setValue:forHTTPHeaderField:"
+ "keyBlob"
+ "registerPartsInfoViewWithComponentsMap:"
+ "setPath:"
+ "tintColor"
+ "Authenticated user credentials successfully."
+ "CHIMERA_LOCK_DETAIL_TEXT"
+ "Moved to next locked token: %!@(MISSING)"
+ "initWithData:encoding:"
+ "setViewControllers:"
+ "@\"UINavigationController\""
+ "accessoryButton"
+ "array"
+ "remoteUIController:didPresentObjectModel:modally:"
+ "v40@0:8@\"RemoteUIController\"16@\"NSError\"24@\"NSURLRequest\"32"
+ "linkButton"
+ "localizedComponentsMap"
+ "responsePhase1"
+ "buttonEventMonitor"
+ "setFdrTypes:"
+ "setIsTokenUnlocked:"
+ "Invalid MIME type %!@(MISSING)"
+ "v40@0:8@16@24^Q32"
+ "B24@0:8^@16"
+ "LOST"
+ "Physical button event: %!l(MISSING)d"
+ "coordinator"
+ "remoteUIController:loadResourcesForObjectModel:completion:"
+ "_setHandlerForNextButton"
+ "code"
+ "localizedStringForKey:value:table:"
+ "preflightPartSPC"
+ "preflightPhase2:withReply:"
+ "setTokenChallengers:"
+ "Invalid type of types"
+ "Lengths of localized components mismatch: %!l(MISSING)d, %!l(MISSING)d"
+ "_requestBuddyML:session:completion:"
+ "_viewControllers"
+ "requestWithURL:"
+ "setShouldShowPressHomeLabel:"
+ "setShouldUpdatePersistentServiceTokens:"
+ "v36@0:8@16@24B32"
+ "-[StartPreflightViewController setupActivationLockView]"
+ "_activeTokenChallengerIndex"
+ "host"
+ "initWithComponent:status:"
+ "v40@0:8@16@24@?32"
+ "IDMS timeout"
+ "_learnMoreTapped"
+ "ak_addClientInfoHeader"
+ "application/x-plist"
+ "v32@0:8q16@24"
+ "v8@?0"
+ "actionWithTitle:style:handler:"
+ "preflightResults"
+ "remoteUIController:didReceiveChallenge:completionHandler:"
+ "setEndpointBaseURL:"
+ "setAuthenticator:"
+ "setServiceIdentifier:"
+ "T@\"<StartPreflightNavigationCoordinator>\",W,N,V_coordinator"
+ "T@\"<StartPreflightSigner>\",&,N,V_signer"
+ "_components"
+ "_coordinator"
+ "authenticateWithContext:completion:"
+ "IDMS authentication succeed"
+ "navigationControllerSupportedInterfaceOrientations:"
+ "v32@0:8@\"RemoteUIController\"16@\"NSArray\"24"
+ "\n"
+ "@\"RUIPage\"40@0:8@\"RemoteUIController\"16@\"NSString\"24@\"NSDictionary\"32"
+ "InternalBuild"
+ "T@\"UINavigationController\",&,N,V_navigationController"
+ "preflightPhase1:withReply:"
+ "setActiveTokenChallengerIndex:"
+ "transitionTable"
+ "Failed to fetch buddyML: %!@(MISSING)"
+ "SINGLE_OWNER_MULTI_ACTIVATION_LOCK_TITLE"
+ "loadData:baseURL:"
+ "pass"
+ "setURLCache:"
+ "shouldPresentInHostApp"
+ "Invalid token: %!@(MISSING)"
+ "ak_addAuthorizationHeaderWithServiceToken:forAltDSID:"
+ "setPreflightRIK:"
+ "setRemoteUIController:"
+ "TB,N,V_activationLockChallengeNeeded"
+ "setNavigationController:"
+ "-[ActivationLockViewController _skipActivateTapped]"
+ "No more token left"
+ "Rendering xmlui"
+ "SKIP_ACTIVATION_BUTTON_TITLE"
+ "T@\"NSArray\",&,N,V_activationLockComponents"
+ "_activationLockChallengeNeeded"
+ "preflightBaaCert"
+ "remoteUIController:didReceiveHTTPResponse:forRequest:"
+ "v32@0:8@\"RemoteUIController\"16@\"RUIObjectModel\"24"
+ "ChimeraLockViewController"
+ "T@\"NSMutableDictionary\",&,N,V_localizedComponentMap"
+ "componentsWithURL:resolvingAgainstBaseURL:"
+ "dictionary"
+ "q56@0:8^@16@24@32@40@48"
+ "remoteUIController:createPageWithName:attributes:"
+ "stopWithCompletion:"
+ "v24@0:8@\"RemoteUIController\"16"
+ "@\"RemoteUIController\""
+ "systemImageNamed:withConfiguration:"
+ "Q24@0:8@\"UINavigationController\"16"
+ "SINGLE_OWNER_SINGLE_ACTIVATION_LOCK_TEXT"
+ "removing second-to-last RUI Page"
+ "setupRemoteUIController"
+ "v40@0:8@\"RemoteUIController\"16@\"NSURLAuthenticationChallenge\"24@?<v@?q@\"NSURLCredential\">32"
+ "-[ActivationLockViewController _learnMoreTapped]"
+ "_continueTapped"
+ "allKeys"
+ "scheme"
+ "@\"NSObject<OS_dispatch_semaphore>\""
+ "B48@0:8@16@24@32@40"
+ "Missing partSPCs"
+ "Preflight phase 1 success: %!d(MISSING)"
+ "setUsername:"
+ "subElementWithID:"
+ "Preflight phase 2 results: %!@(MISSING)"
+ "UNKNOWN_ERROR_ALERT_TITLE"
+ "addAction:"
+ "ak_addDeviceUDIDHeader"
+ "v40@0:8@\"RemoteUIController\"16@\"RUIObjectModel\"24@?<v@?B@\"NSError\">32"
+ "T@\"DSHardwareButtonEventMonitor\",&,N,V_buttonEventMonitor"
+ "T@\"NSString\",&,N,V_token"
+ "0"
+ "B48@0:8@\"RemoteUIController\"16@\"RUIObjectModel\"24@\"RUIElement\"32@\"RUIPage\"40"
+ "DENIED"
+ "_appendAdditionalHeaders:altDSID:gsToken:"
+ "localizedComponentMap"
+ "remoteUIController:didDismissModalNavigationWithObjectModels:"
+ "setCoordinator:"
+ "showUnknownErrorAlertWithCode:"
+ "Preflight phase 1 time out"
+ "RECOVER"
+ "configurationWithHierarchicalColor:"
+ "objectForKeyedSubscript:"
+ "q32@0:8@16@24"
+ "setShouldPromptForPasswordOnly:"
+ "Empty username"
+ "setObject:forKeyedSubscript:"
+ "-[StartPreflightViewController viewDidAppear:]"
+ "@\"NSArray\""
+ "Failed to serialize post data: %!@(MISSING)"
+ "Request Headers: %!{(MISSING)public}@"
+ "_activationLockComponents"
+ "length"
+ "setFrame:"
+ "setHostViewController:"
+ "setIsUsernameEditable:"
+ "Failed to request unlock status"
+ "_token"
+ "setAuthenticationType:"
+ "_localizedComponentMap"
+ "showButtonsAvailable"
+ "MIMEType"
+ "Unknown error: %!l(MISSING)d"
+ "T@\"NSArray\",&,N,V_fdrTypes"
+ "_fetchGSTokenWithPassword:username:altDSID:gsToken:"
+ "serverInfo"
+ "setHTTPBody:"
+ "ACTIVATION_LOST_DETAIL_TEXT"
+ "Preflight phase 1 resultsPhase1: %!@(MISSING)"
+ "Missing preflight RIK"
+ "Reset state from %!l(MISSING)d to %!l(MISSING)d"
+ "SINGLE_OWNER_SINGLE_ACTIVATION_LOCK_TITLE"
+ "init"
+ "remoteUIController:didRefreshObjectModel:"
+ "signer"
+ "viewControllers"
+ "Q"
+ "activationLockComponents"
+ "No BAA certificate found"
+ "activateElement:completion:"
+ "preflightPhase2:"
+ "remoteUIController:shouldLoadRequest:redirectResponse:withCompletionHandler:"
+ "sourceURL"
+ "systemFontSize"
+ "mutableCopy"
+ "resetState"
+ "<xmlui"
+ "@\"<UIViewControllerAnimatedTransitioning>\"48@0:8@\"UINavigationController\"16q24@\"UIViewController\"32@\"UIViewController\"40"
+ "B40@0:8@16@24@32"
+ "HTTPBody"
+ "Register physical button events"
+ "remoteUIController"
+ "setState:"
+ "v40@0:8@\"RemoteUIController\"16@\"RUIObjectModel\"24^Q32"
+ "BuddyML failed to load"
+ "No object model"
+ "_setHandlerForSkipButton"
+ "remoteUIController:didRemoveObjectModel:"
+ "removeObjectAtIndex:"
+ "setToken:"
+ "sign:keyBlob:"
+ "startNavigationBarSpinnerWithTitle:"
+ "%!s(MISSING): error: %!@(MISSING). request: %!@(MISSING)"
+ "Chimera lock needed"
+ "_learnMoreController"
+ "defaultSessionConfiguration"
+ "fdrTypes"
+ "initWithTokenChallengers:authenticator:"
+ "numberWithInteger:"
+ "setActivationLockComponents:"
+ "setObject:forKey:"
+ "-[ActivationLockViewController remoteUIController:shouldLoadRequest:redirectResponse:]"
+ "@\"DSHardwareButtonEventMonitor\""
+ "@\"<StartPreflightNavigationCoordinator>\""
+ "CHIMERA_LOCK_TITLE"
+ "Failed to authenticate: %!@(MISSING)"
+ "Missing activation token"
+ "_setPassword:"
+ "AUTH_ERROR_ALERT_ACTION"
+ "ButtonEventMonitor not available"
+ "Failed to unlock token: %!@(MISSING)"
+ "Not xmlui data"
+ "UINavigationControllerDelegate"
+ "v24@?0@\"NSData\"8q16"
+ "v48@0:8@16@24@32@?40"
+ "@\"NSMutableArray\""
+ "_endpoint"
+ "addSubview:"
+ "navigationController:interactionControllerForAnimationController:"
+ "type"
+ "POST"
+ "Token"
+ "components"
+ "sealed"
+ "remoteUIController:didReceiveHTTPResponse:"
+ "remoteUIController:objectModel:shouldDisplayNamedElement:page:"
+ "skip"
+ "bounds"
+ "chimeraLockComponents"
+ "setIsEphemeral:"
+ "v48@0:8@\"RemoteUIController\"16@\"NSMutableURLRequest\"24@\"NSURLResponse\"32@?<v@?B@\"NSError\">40"
+ "Unable to find next relative path"
+ "buttonTray"
+ "navigationControllerPreferredInterfaceOrientationForPresentation:"
+ "setButtonEventMonitor:"
+ "setLearnMoreController:"
+ "Missing activation challenge endpoint"
+ "Response Body: %!{(MISSING)private}@"
+ "arrayWithArray:"
+ "T@\"IDMSAuthenticator\",&,N,V_authenticator"
+ "_showAlertWithTitle:message:actionTitle:"
+ "lock.circle"
+ "setEndpoint:"
+ "systemImageNamed:"
+ "_fdrTypes"
+ "allValues"
+ "q16@0:8"
+ "setLocalizedComponentMap:"
+ "\x1b"
+ "Dismiss at illegal state %!l(MISSING)d"
+ "Failed to serialize the request: %!@(MISSING)"
+ "_endpointBaseURL"
+ "setSigner:"
+ "viewDidLoad"
+ "@\"NSURL\""
+ "Illegal state transition from %!l(MISSING)d to %!l(MISSING)d"
+ "moveToNextLockedTokenChallenger"
+ "setFragment:"
+ "_preflightRIK"
+ "navigationController:animationControllerForOperation:fromViewController:toViewController:"
+ "setText:"
+ "showButtonsBusy"
+ "Activation lock needed"
+ "RemoteUIControllerDelegate"
+ "addChildViewController:"
+ "remoteUIController:shouldLoadRequest:redirectResponse:"
+ "@56@0:8@16@24@32@40@48"
+ "Token has already been unlocked"
+ "initWithToken:components:fdrTypes:endpoint:signer:"
+ "B"
+ "_preflightResults"
+ "base64EncodedStringWithOptions:"
+ "preflightRIK"
+ "_chimeraLockComponents"
+ "activationLockChallengeNeeded"
+ "transitionToState:"
+ "T@\"NSDictionary\",&,N,V_preflightResponsePhase1"
+ "activationLockComplete"
+ "addObject:"
+ "dismissViewControllerAnimated:completion:"
+ "v40@0:8@16@24@32"
+ "DiagnosticsSupport not available"
+ "No more views. Activation lock complete"
+ "IDMSAuthenticator"
+ "com.apple.gs.corerepair.auth"
+ "DSHardwareButtonEventMonitor"
+ "Invalid status"
+ "TokenChallenger"
+ "activationLockCheck"
+ "clientInfo"
+ "popToViewController:animated:"
+ "remoteUIController:willPresentModalNavigationController:"
+ "sessionWithConfiguration:"
+ "stopNavigationBarSpinner"
+ "Preflight phase 2 failed"
+ "Request Body: %!{(MISSING)private}@"
+ "_sanityCheckBuddyMLResponse:data:"
+ "_tokenChallengers"
+ "endpoint"
+ "Preflight phase 1 error: %!@(MISSING)"
+ "SINGLE_OWNER_MULTI_ACTIVATION_LOCK_TEXT"
+ "Tq,N,V_state"
+ "challenger out of bounds: %!l(MISSING)u"
+ "preflightPhase1:"
+ "remoteUIController:didFinishLoadWithError:forRequest:"
+ "Empty password"
+ "remoteUIControllerDidDismiss:"
+ "setHTTPMethod:"
+ "CHALLENGED"
+ "Content-Type"
+ "Loading unlock status"
+ "Preflight phase 1 missing expected results"
+ "Preflight phase 2 error: %!@(MISSING)"
+ "application/x-buddyml"
+ "constructChallengeRequestDataWithToken:data:"
+ "password"
+ "url"
+ "v36@0:8@\"UINavigationController\"16@\"UIViewController\"24B32"
+ "Q24@0:8@16"
+ "Transitioning state from %!l(MISSING)d to %!l(MISSING)d"
+ "_signer"
+ "endpointBaseURL"
+ "v24@0:8Q16"
+ "-[StartPreflightViewController moveToNextViewController]"
+ "@\"NSDictionary\""
+ "editableTextField"
+ "remoteUIController:didReceiveObjectModel:actionSignal:"
+ "setHandlerForElementsMatching:handler:"
+ "v32@0:8@\"RemoteUIController\"16@\"NSMutableURLRequest\"24"
+ "Failed to construct challenge request: %!l(MISSING)d"
+ "Response URL: %!{(MISSING)public}@"
+ "handleButtonEvent:"
+ "authenticateFromObjectModel:outRequest:"
+ "navigationController"
+ "presentViewController:animated:completion:"
+ "q48@0:8@16@24^@32^@40"
+ "-[StartPreflightViewController viewDidLoad]"
+ "T@\"RemoteUIController\",&,N,V_remoteUIController"
+ "endTestWithStatusCode:error:"
+ "-[ActivationLockViewController viewDidAppear:]"
+ "Fetching password UI with token: %!@(MISSING)"
+ "URLByAppendingPathComponent:"
+ "setupAssistantStyle"
+ "tokenChallengers"
+ "UNKNOWN_ERROR_ALERT_MESSAGE"
+ "Unable to find base path"
+ "componentsJoinedByString:"
+ "dataTaskWithRequest:completionHandler:"
+ "remoteUIController:willPresentObjectModel:modally:"
+ "setUiNeededKnownSemaphore:"
+ "Next tapped"
+ "_startActivateTapped"
+ "componentsMap"
+ "dataWithPropertyList:format:options:error:"
+ "navigationController:didShowViewController:animated:"

```
