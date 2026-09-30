## AuthKitUI

> `/System/Library/PrivateFrameworks/AuthKitUI.framework/AuthKitUI`

```diff

-493.230.1.0.0
-  __TEXT.__text: 0x643e8
-  __TEXT.__auth_stubs: 0xbf0
-  __TEXT.__objc_methlist: 0x64fc
-  __TEXT.__const: 0x310
-  __TEXT.__gcc_except_tab: 0x9a8
-  __TEXT.__cstring: 0x447a
-  __TEXT.__oslogstring: 0x3d51
+493.458.3.2.0
+  __TEXT.__text: 0x68958
+  __TEXT.__auth_stubs: 0xc40
+  __TEXT.__objc_methlist: 0x7c1c
+  __TEXT.__const: 0x370
+  __TEXT.__gcc_except_tab: 0x9ec
+  __TEXT.__cstring: 0x4c53
+  __TEXT.__oslogstring: 0x42f5
   __TEXT.__ustring: 0x2c
   __TEXT.__dlopen_cstrs: 0x71
-  __TEXT.__unwind_info: 0x1b00
-  __TEXT.__objc_classname: 0x133c
-  __TEXT.__objc_methname: 0x15440
-  __TEXT.__objc_methtype: 0x3fbc
-  __TEXT.__objc_stubs: 0x10c60
-  __DATA_CONST.__got: 0xbf8
-  __DATA_CONST.__const: 0x12b8
-  __DATA_CONST.__objc_classlist: 0x348
+  __TEXT.__unwind_info: 0x1c38
+  __TEXT.__objc_classname: 0x1452
+  __TEXT.__objc_methname: 0x1637e
+  __TEXT.__objc_methtype: 0x43a8
+  __TEXT.__objc_stubs: 0x11700
+  __DATA_CONST.__got: 0xc38
+  __DATA_CONST.__const: 0x14b0
+  __DATA_CONST.__objc_classlist: 0x368
   __DATA_CONST.__objc_catlist: 0x50
-  __DATA_CONST.__objc_protolist: 0x1b8
+  __DATA_CONST.__objc_protolist: 0x1e8
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x4fd8
+  __DATA_CONST.__objc_selrefs: 0x5830
   __DATA_CONST.__objc_protorefs: 0x18
-  __DATA_CONST.__objc_superrefs: 0x270
-  __DATA_CONST.__objc_arraydata: 0xe0
-  __AUTH_CONST.__auth_got: 0x608
-  __AUTH_CONST.__const: 0x1a0
-  __AUTH_CONST.__cfstring: 0x40e0
-  __AUTH_CONST.__objc_const: 0x17410
-  __AUTH_CONST.__objc_intobj: 0x288
+  __DATA_CONST.__objc_superrefs: 0x290
+  __DATA_CONST.__objc_arraydata: 0x2a8
+  __AUTH_CONST.__auth_got: 0x630
+  __AUTH_CONST.__auth_ptr: 0x8
+  __AUTH_CONST.__const: 0x1e0
+  __AUTH_CONST.__cfstring: 0x4960
+  __AUTH_CONST.__objc_const: 0x15d90
+  __AUTH_CONST.__objc_intobj: 0x2a0
   __AUTH_CONST.__objc_doubleobj: 0x30
-  __AUTH_CONST.__objc_dictobj: 0x50
-  __AUTH_CONST.__objc_arrayobj: 0x48
-  __AUTH.__objc_data: 0x1db0
-  __DATA.__objc_ivar: 0x678
-  __DATA.__data: 0x14c8
+  __AUTH_CONST.__objc_dictobj: 0x78
+  __AUTH_CONST.__objc_arrayobj: 0x90
+  __AUTH.__objc_data: 0x1ef0
+  __DATA.__objc_ivar: 0x6d0
+  __DATA.__data: 0x1708
   __DATA.__bss: 0x158
   __DATA_DIRTY.__objc_data: 0x320
   - /System/Library/Frameworks/AVFAudio.framework/AVFAudio

   - /usr/lib/libMobileGestalt.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 2614
-  Symbols:   3447
-  CStrings:  5041
+  Functions: 2738
+  Symbols:   3616
+  CStrings:  5313
 
Symbols:
+ _AKBiometricRatchetCalloutReasonKey
+ _AKBiometricRatchetDeeplinkKey
+ _AKBiometricRatchetDeeplinkTypeKey
+ _AKBiometricRatchetDeeplinkTypeURL
+ _AKBiometricRatchetDeeplinkTypeURLBagKey
+ _AKBiometricRatchetFallbackKey
+ _AKBiometricRatchetFallbackTextKey
+ _AKBiometricRatchetNotInteractiveKey
+ _AKBiometricRatchetReasonKey
+ _AKBiometryBeginRatchetBodyKey
+ _AKBiometryBeginRatchetTitleKey
+ _AKBiometryDisableFMErrorMessageKey
+ _AKBiometryDisableFMErrorTitleKey
+ _AKBiometryDisableFMKey
+ _AKBiometryDisableFMMessageKey
+ _AKBiometryEmbeddedUIPresentationModeKey
+ _AKBiometryEmbeddedUIRightNavButtonTitleKey
+ _AKBiometryMetaContext
+ _MGCopyAnswer
+ _OBJC_CLASS_$_AKChildSetupTwoDeviceProxView
+ _OBJC_CLASS_$_AKProtoAccountContext
+ _OBJC_CLASS_$_AKRemoteViewSessionController
+ _OBJC_CLASS_$_NSXPCConnection
+ _OBJC_CLASS_$_NSXPCInterface
+ _OBJC_CLASS_$_NSXPCListenerEndpoint
+ _OBJC_CLASS_$__AKRemoteViewService
+ _OBJC_CLASS_$__AKRemoteViewSession
+ _OBJC_METACLASS_$_AKChildSetupTwoDeviceProxView
+ _OBJC_METACLASS_$_AKRemoteViewSessionController
+ _OBJC_METACLASS_$__AKRemoteViewService
+ _OBJC_METACLASS_$__AKRemoteViewSession
+ __xpc_type_endpoint
+ _objc_autorelease
+ _os_unfair_lock_lock
+ _os_unfair_lock_unlock
+ _xpc_get_type
CStrings:
+ "\x15\x1a\x11"
+ "%@ Pair Hello"
+ "%@ Pair Home"
+ "%@: Not presenting shield UI, not needed"
+ "%@: Shielding sign in / create flows by presenting shield UI with view controller: %@"
+ "-[AKInlineSignInViewController _presentShieldUIIfNeededWithViewController:]"
+ "-[AKInlineSignInViewController _presentShieldUIWithViewController:]"
+ "-[_AKRemoteViewService _onmainqueue_presentAuthorizationWithContext:usingHost:completionHandler:]"
+ "-[_AKRemoteViewService _onmainqueue_presentPrivateEmailWithContext:usingHost:completionHandler:]"
+ "-[_AKRemoteViewService _onmainqueue_presentShieldWithContext:completionHandler:]"
+ "-[_AKRemoteViewService _onxpcqueue_continueAuthenticationWithSurrogateID:completionHandler:]"
+ "/System/AppleInternal/Library/Frameworks/AVKit.framework/AVKit"
+ "/System/AppleInternal/Library/Frameworks/AppleAccountUI.framework/AppleAccountUI"
+ "/System/AppleInternal/Library/Frameworks/AuthenticationServices.framework/AuthenticationServices"
+ "/System/AppleInternal/Library/Frameworks/BridgePreferences.framework/BridgePreferences"
+ "/System/AppleInternal/Library/Frameworks/CoreFollowUp.framework/CoreFollowUp"
+ "/System/AppleInternal/Library/Frameworks/ProximityAppleIDSetupUI.framework/ProximityAppleIDSetupUI"
+ "/System/AppleInternal/Library/Frameworks/SafariFoundation.framework/SafariFoundation"
+ "/System/AppleInternal/Library/Frameworks/VisualPairing.framework/VisualPairing"
+ "@\"<AKAppleIDProximityAuthenticationContextDelegate>\""
+ "@\"<BSInvalidatable>\""
+ "@\"NSMutableSet\""
+ "@\"NSSet\"48@0:8@\"NSSet\"16@\"FBSScene\"24@\"UIScene\"32@\"FBSSceneTransitionContext\"40"
+ "@\"NSXPCConnection\""
+ "@\"UIConversationContext\"16@0:8"
+ "@\"UISceneSession\""
+ "@\"UIWindow\""
+ "@\"_UISceneConnectionOptionsContext\"48@0:8@\"NSSet\"16@\"FBSScene\"24@\"UISceneSession\"32@\"FBSSceneTransitionContext\"40"
+ "@32@0:8Q16@24"
+ "@48@0:8@16@24d32d40"
+ "AKAdaptiveServiceInterface"
+ "AKChildSetupTwoDeviceProxView"
+ "AKRemoteViewServiceInterface"
+ "AKRemoteViewSessionController"
+ "AKRemoteViewSessionInterface"
+ "APPLE_ID_ALERT_PLACEHOLDER_REBRAND"
+ "APPLE_ID_PASSWORD_HEADER_REBRAND"
+ "APPLE_ID_REBRAND"
+ "APPLE_ID_SIGN_IN_HEADER_REBRAND"
+ "AUTHORIZATION_VIEWCONTROLLER_TITLE_REBRAND"
+ "AUTHORIZE_APPLE_ID_1ST_PARTY_LOGIN_KEY_ACCESS_REBRAND"
+ "AUTHORIZE_APPLE_ID_1ST_PARTY_LOGIN_REBRAND"
+ "AUTHORIZE_FIRST_TIME_MANAGED_ACCOUNT_MESSAGE_1_REBRAND"
+ "AUTHORIZE_FIRST_TIME_MESSAGE_1_REBRAND"
+ "AUTHORIZE_FOR_ACCOUNT_WITH_PASSWORD_REBRAND"
+ "AUTHORIZE_UPGRADE_MESSAGE_1_NOBIO_REBRAND"
+ "Activated remote view session (%@) and received config: %@"
+ "Applying empty proto account context to %@ in order to bypass shield UI"
+ "Attempting to create view session for action: %@"
+ "Auth context has a prox delegate to respond to: %@"
+ "Auth context is of proximity type: %@"
+ "B16@?0@\"BSAction\"8"
+ "B32@0:8@16^@24"
+ "CREATE_APPLE_ID_BUTTON_TITLE_REBRAND"
+ "CREATE_APPLE_ID_REBRAND"
+ "Calling prox delegate selected account with account type: %ld"
+ "Calling prox delegate to go ahead and setup passcode and biometrics"
+ "Calling prox delegate to perform AIDA sign in with auth results: %@"
+ "Calling prox delegate with auth results: %@ and error: %@"
+ "Cursive Hello %@"
+ "Cursive Hello en"
+ "FORGOT_APPLE_ID_REBRAND"
+ "FORGOT_DESCRIPTION_REBRAND"
+ "FORGOT_PASSWORD_ALERT_MESSAGE_REBRAND"
+ "Failed to activate remote view session (%@) with error: %@"
+ "Failed to create view session for action (%@) with error: %@"
+ "Failed to destroy scene session with error, executing cliff jump: %@"
+ "Finished activating UI with configuration: %@"
+ "KEEP_USING_ALERT_NO_BUTTON_REBRAND"
+ "KEEP_USING_ALERT_TITLE_REBRAND"
+ "No more sessions registered, calling to dismiss & destroy"
+ "PASSWORD_RESET_OPTIONS_SERVICE_TITLE_REBRAND"
+ "PROXIMITY_AUTH_CHILD_SETUP_DESCRIPTION"
+ "PROXIMITY_AUTH_CHILD_SETUP_SETUP_WITHOUT_ANOTHER_DEVICE_BUTTON"
+ "PROXIMITY_AUTH_CHILD_SETUP_TITLE"
+ "P`"
+ "ProductType"
+ "Registering remote view session: %@"
+ "Responding to BS actions (%@) for FBS scene (%@) in UI scene (%@) from context (%@)"
+ "T@\"<AKAppleIDProximityAuthenticationContextDelegate>\",W,N,V_proxDelegate"
+ "T@\"NSXPCConnection\",&,N,V_connection"
+ "T@\"NSXPCConnection\",R,N,V_connection"
+ "T@\"UIConversationContext\",?,&,N"
+ "T@\"UILabel\",&,N,V_secondaryContentLabel"
+ "T@\"UISceneSession\",R,N,V_sceneSession"
+ "T@\"UIViewController\",R,N,V_rootViewController"
+ "T@?,C,N,V_invalidationHandler"
+ "T@?,C,N,V_newAuthorizationViewController"
+ "T@?,C,N,V_newPrivateEmailViewController"
+ "T@?,C,N,V_newShieldViewController"
+ "T@?,C,N,V_windowBlock"
+ "T@?,N,V_proximityAIDAHandler"
+ "USE_APPLE_ID_REBRAND"
+ "USE_DIFFERENT_APPLE_ID_REBRAND"
+ "Unable to continue with endpoint (%@) from info (%@) for action: %@"
+ "Unregistering remote view session: %@"
+ "Updating placement with scene ID: %@"
+ "Updating scene placement with view service configuration: %@"
+ "VERIFICATION_HEADER_REBRAND"
+ "View service configuration (%@) does not contain host scene ID or bundle ID; updating effective placement to default"
+ "View session (%@) was created; proceeding to register and activate"
+ "Vv24@0:8@?16"
+ "Vv24@0:8@?<v@?@\"AKRemoteViewServiceConfiguration\"@\"NSError\">16"
+ "Vv32@0:8@\"AKProtoAccountShieldContext\"16@?<v@?@\"NSError\"@\"NSDictionary\">24"
+ "Vv32@0:8@\"NSUUID\"16@?<v@?@\"NSError\">24"
+ "Vv32@0:8@16@?24"
+ "Vv40@0:8@\"AKAuthorizationPresentationContext\"16@\"<AKAuthorizationPresenterHostProtocol>\"24@?<v@?@\"AKAuthorization\"@\"NSError\">32"
+ "Vv40@0:8@\"AKPrivateEmailContext\"16@\"<AKPrivateEmailPresenterHostProtocol>\"24@?<v@?@\"AKPrivateEmail\"@\"NSError\">32"
+ "Vv40@0:8@16@24@?32"
+ "XPC endpoint (%@) of unexpected type: %@"
+ "_AKRemoteViewService"
+ "_AKRemoteViewSession"
+ "_UISceneBSActionHandler"
+ "_UISceneBSActionResponding"
+ "_UISceneConnectionOptionProviding"
+ "_activate"
+ "_activateUIWithConfiguration:completion:"
+ "_addChildSetupImageView"
+ "_addPairForiPad"
+ "_addPairForiPhone"
+ "_addSecondaryView"
+ "_connection"
+ "_deviceTypeForProductType:"
+ "_dismissAndDestroy"
+ "_helloBackgroundForProductType:"
+ "_helloScreenViewForProductType:"
+ "_helloScreenViewWithBackgroundImage:cursiveImage:labelBottomOffset:labelHorizontalInset:"
+ "_homeScreenImageForProductType:"
+ "_homeScreenViewForProductType:"
+ "_homeScreenViewWithImage:"
+ "_invalidationHandler"
+ "_launchOptionsFromActions:forFBSScene:uiSceneSession:transitionContext:"
+ "_localizedHelloCursiveAssetForDeviceType"
+ "_lock"
+ "_newAuthorizationViewController"
+ "_newPrivateEmailViewController"
+ "_newShieldViewController"
+ "_onmainqueue_presentAuthorizationWithContext:usingHost:completionHandler:"
+ "_onmainqueue_presentPrivateEmailWithContext:usingHost:completionHandler:"
+ "_onmainqueue_presentShieldWithContext:completionHandler:"
+ "_onmainqueue_requestDimmingWithConfiguration:"
+ "_onmainqueue_updatePlacementWithConfiguration:completion:"
+ "_onmainqueue_updatePlacementWithSceneID:completion:"
+ "_onxpcqueue_continueAuthenticationWithSurrogateID:completionHandler:"
+ "_presentShieldUIIfNeededWithViewController:"
+ "_presentShieldUIWithViewController:"
+ "_proxDelegate"
+ "_proximityAIDAHandler"
+ "_registerSession:"
+ "_requestDimmingWithConfiguration:completion:"
+ "_respondToActions:forFBSScene:inUIScene:fromTransitionContext:"
+ "_sceneSession"
+ "_sceneSessionInvalidatable"
+ "_screenImagePrefixForProductType:"
+ "_secondaryContentLabel"
+ "_sessions"
+ "_setEndpoint:"
+ "_unregisterSession:"
+ "_updatePlacementWithConfiguration:completion:"
+ "_updatePlacementWithSceneID:completion:"
+ "_window"
+ "_windowBlock"
+ "`"
+ "aaf_filter:"
+ "activate"
+ "activateWithCompletionHandler:"
+ "ar"
+ "bg"
+ "ca"
+ "connection"
+ "constraintGreaterThanOrEqualToAnchor:"
+ "continueAuthenticationWithSurrogateID:completionHandler:"
+ "conversationContext"
+ "createViewSessionForAction:error:"
+ "cs"
+ "da"
+ "de"
+ "disableFMMessage"
+ "el"
+ "en"
+ "es"
+ "fi"
+ "fr"
+ "he"
+ "hi"
+ "hostBundleID"
+ "hostSceneID"
+ "hr"
+ "hu"
+ "iPad Pair Hello"
+ "iPad Phone Pair Home"
+ "iPhone"
+ "iPhone 11 Pro"
+ "iPhone 11 Pro Max"
+ "iPhone 7"
+ "iPhone 7 Plus"
+ "iPhone SE"
+ "iPhone10,1"
+ "iPhone10,2"
+ "iPhone10,3"
+ "iPhone10,4"
+ "iPhone10,5"
+ "iPhone10,6"
+ "iPhone11,2"
+ "iPhone11,4"
+ "iPhone11,6"
+ "iPhone11,8"
+ "iPhone12,3"
+ "iPhone12,5"
+ "iPhone12,8"
+ "iPhone6"
+ "iPhone7,1"
+ "iPhone7,2"
+ "iPhone8,1"
+ "iPhone8,2"
+ "iPhone8,4"
+ "iPhone9,1"
+ "iPhone9,2"
+ "iPhone9,3"
+ "iPhone9,4"
+ "imageNamed:"
+ "info"
+ "initWithConnection:"
+ "initWithConnection:rootViewController:"
+ "initWithGivenName:lastName:ageRange:"
+ "initWithListenerEndpoint:"
+ "initWithReason:calloutReason:deeplinkURL:fallbackToNoAuth:useShortExpiration:beginRatchetTitle:beginRatchetBody:showsLocationWarning:countdownText:findMyErrorTitle:findMyErrorMessage:metaContext:notInteractive:"
+ "initWithRootViewController:sceneSession:"
+ "initWithTitle:detailText:icon:contentLayout:"
+ "initWithType:secondaryButtonTitle:"
+ "invalidationHandler"
+ "isAgeAttestationPhase1Enabled"
+ "it"
+ "ja"
+ "kk"
+ "ko"
+ "leftAnchor"
+ "ms"
+ "newAuthorizationViewController"
+ "newPrivateEmailViewController"
+ "newShieldViewController"
+ "nl"
+ "no"
+ "notInteractive"
+ "objectForSetting:"
+ "pl"
+ "preferredFontDescriptorWithTextStyle:compatibleWithTraitCollection:"
+ "preferredLanguages"
+ "preferredLocalizationsFromArray:forPreferences:"
+ "presentAuthorizationWithContext:usingHost:completionHandler:"
+ "presentPrivateEmailWithContext:usingHost:completionHandler:"
+ "presentShieldWithContext:completionHandler:"
+ "protoAccountContext"
+ "proxDelegate"
+ "proximitySetupCompletedWithResult:error:"
+ "pt"
+ "remoteObjectProxyWithErrorHandler:"
+ "remoteViewServiceInterface"
+ "remoteViewSessionInterface"
+ "removeObject:"
+ "requestSceneSessionDestruction:options:errorHandler:"
+ "respondToAction:error:"
+ "rightAnchor"
+ "ro"
+ "ru"
+ "sceneSession"
+ "secondaryContentLabel"
+ "secondaryContentView"
+ "setAccessibilityIgnoresInvertColors:"
+ "setConnection:"
+ "setConversationContext:"
+ "setExportedInterface:"
+ "setExportedObject:"
+ "setInterruptionHandler:"
+ "setInvalidationHandler:"
+ "setNewAuthorizationViewController:"
+ "setNewPrivateEmailViewController:"
+ "setNewShieldViewController:"
+ "setProtoAccountContext:"
+ "setProxDelegate:"
+ "setProximityAIDAHandler:"
+ "setRemoteObjectInterface:"
+ "setSecondaryContentLabel:"
+ "setShadowOffset:"
+ "setShadowOpacity:"
+ "setShadowRadius:"
+ "setWindowBlock:"
+ "shieldSignInOrCreateFlows"
+ "sk"
+ "sv"
+ "systemGray6Color"
+ "textField:insertInputSuggestion:"
+ "th"
+ "tr"
+ "uk"
+ "v24@0:8@\"UIConversationContext\"16"
+ "v24@?0@\"<AKRemoteViewSessionInterface>\"8^B16"
+ "v24@?0@\"AKRemoteViewServiceConfiguration\"8@\"NSError\"16"
+ "v32@0:8@\"UITextField\"16@\"UIInputSuggestion\"24"
+ "vi"
+ "windowBlock"
+ "zh-Hans"
+ "zh-Hant"
+ "{os_unfair_lock_s=\"_os_unfair_lock_opaque\"I}"
- "\x15\x1a"
- "APPLE_ID"
- "APPLE_ID_ALERT_PLACEHOLDER"
- "APPLE_ID_PASSWORD_HEADER"
- "APPLE_ID_SIGN_IN_HEADER"
- "AUTHORIZATION_VIEWCONTROLLER_TITLE"
- "AUTHORIZE_APPLEID_CREATE"
- "AUTHORIZE_APPLE_ID_1ST_PARTY_LOGIN"
- "AUTHORIZE_APPLE_ID_1ST_PARTY_LOGIN_KEY_ACCESS"
- "AUTHORIZE_APPLE_ID_UPGRADE_LOGIN"
- "AUTHORIZE_APPLE_ID_WELCOME"
- "AUTHORIZE_FIRST_TIME_MANAGED_ACCOUNT_MESSAGE_1"
- "AUTHORIZE_FIRST_TIME_MESSAGE_1"
- "AUTHORIZE_FOR_ACCOUNT_WITH_PASSWORD"
- "AUTHORIZE_MANAGED_APPLEID_CREATE"
- "AUTHORIZE_MANAGED_APPLEID_WELCOME"
- "AUTHORIZE_UPGRADE_MESSAGE_1_NOBIO"
- "CREATE_APPLE_ID"
- "CREATE_APPLE_ID_BUTTON_TITLE"
- "FORGOT_APPLE_ID"
- "FORGOT_DESCRIPTION"
- "FORGOT_PASSWORD_ALERT_MESSAGE"
- "KEEP_USING_ALERT_NO_BUTTON"
- "KEEP_USING_ALERT_TITLE"
- "PASSWORD_RESET_OPTIONS_SERVICE_TITLE"
- "REBRAND"
- "USE_APPLE_ID"
- "USE_DIFFERENT_APPLE_ID"
- "User choose secondary fallback to proximity auth."
- "VERIFICATION_HEADER"
- "_REBRAND"
- "initWithReason:calloutReason:deeplinkURL:fallbackToNoAuth:useShortExpiration:beginRatchetTitle:beginRatchetBody:showsLocationWarning:countdownText:findMyErrorTitle:findMyErrorMessage:metaContext:"
- "isAABrandingEnabled"

```
