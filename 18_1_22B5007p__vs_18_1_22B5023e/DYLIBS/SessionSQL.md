## SessionSQL

> `/System/Library/PrivateFrameworks/SessionSQL.framework/SessionSQL`

```diff

-198.100.0.0.0
-  __TEXT.__text: 0xc0fc
+200.100.0.0.0
+  __TEXT.__text: 0xbff4
   __TEXT.__auth_stubs: 0x8b0
   __TEXT.__const: 0x6ca
   __TEXT.__cstring: 0x724

   __TEXT.__eh_frame: 0x4f0
   __TEXT.__objc_methname: 0x122
   __DATA_CONST.__got: 0x110
-  __DATA_CONST.__const: 0x58
+  __DATA_CONST.__const: 0x98
   __DATA_CONST.__objc_classlist: 0x10
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_selrefs: 0x78
   __AUTH_CONST.__auth_got: 0x458
-  __AUTH_CONST.__auth_ptr: 0x2e8
+  __AUTH_CONST.__auth_ptr: 0x2e0
   __AUTH_CONST.__const: 0x538
   __AUTH_CONST.__objc_const: 0x210
   __DATA.__data: 0x90

   - /usr/lib/swift/libswiftObjectiveC.dylib
   - /usr/lib/swift/libswiftQuartzCore.dylib
   - /usr/lib/swift/libswiftXPC.dylib
+  - /usr/lib/swift/libswift_Builtin_float.dylib
+  - /usr/lib/swift/libswift_errno.dylib
+  - /usr/lib/swift/libswift_math.dylib
+  - /usr/lib/swift/libswift_signal.dylib
+  - /usr/lib/swift/libswift_stdio.dylib
+  - /usr/lib/swift/libswift_time.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
+  - /usr/lib/swift/libswiftsys_time.dylib
+  - /usr/lib/swift/libswiftunistd.dylib
   Functions: 302
-  Symbols:   126
-  CStrings:  95
+  Symbols:   134
+  CStrings:  86
 
Symbols:
+ __swift_FORCE_LOAD_$_swift_Builtin_float
+ __swift_FORCE_LOAD_$_swift_errno
+ __swift_FORCE_LOAD_$_swift_math
+ __swift_FORCE_LOAD_$_swift_signal
+ __swift_FORCE_LOAD_$_swift_stdio
+ __swift_FORCE_LOAD_$_swift_time
+ __swift_FORCE_LOAD_$_swiftsys_time
+ __swift_FORCE_LOAD_$_swiftunistd
CStrings:
+ "algorithmWithIdentifier:"
+ "algorithmWithSigningAlgorithm:"
+ "allowedElementKeys"
+ "analyticsForPasswordChange:credentialNeeded:result:"
+ "analyticsForStatus"
+ "analyticsForTestMessages"
+ "audArray"
+ "authGracePeriodStart"
+ "base64URLtokenHashForUser:"
+ "baseSystem"
+ "canLogin"
+ "canTokenIdLogin:pubKeyHash:"
+ "checkIfBiometricConstraintsForSigningForKey:"
+ "clearSmartCardPIN"
+ "concatKDFWithKey:algorithm:partyUInfo:partyVInfo:"
+ "configurationWithOpenIdConfigurationURL:clientID:issuer:completion:"
+ "configurationWithOpenIdConfigurationURL:identityProviderURL:clientId:issuer:completion:"
+ "createEmbeddedAssertionWithContext:"
+ "createEmbeddedPasswordAssertionWithContext:"
+ "createEncryptionKeyForAlgorithm:"
+ "createKeyAndReturnError:"
+ "createKeyExchangeRequestJWTWithContext:otherPartyPublicKey:"
+ "createKeyExchangeRequestWithContext:jwt:"
+ "createKeyRequestWithContext:jwt:"
+ "createLoginJWTWithContext:embeddedAssertion:"
+ "createLoginRequestWithContext:jwt:"
+ "createNonceRequestWithContext:"
+ "createPartyVInfoWithNonce:apvKey:"
+ "createPartyVInfoWithNonce:prefixData:apvPublicKey:"
+ "createPlatformSSOSystemKey:"
+ "createPreAuthenticationRequestWithContext:"
+ "createRefreshJWTWithContext:"
+ "createSEPEncryptionKeyForAlgorithm:shared:preboot:"
+ "createSEPSigningKeyForAlgorithm:shared:preboot:"
+ "createTestMessagesForLoginConfiguration:certificate:"
+ "createUnlockKeyWithPublicKey:error:"
+ "createWSTrust13Request:"
+ "createWSTrust13RequestWithContext:"
+ "createWSTrust13Response:"
+ "createWSTrust2005Request:"
+ "createWSTrust2005RequestWithContext:"
+ "createWSTrust2005Response:"
+ "createWSTrustFault:"
+ "createWSTrustMexRequestWithContext:"
+ "customAssertionRequestBodyClaims"
+ "customAssertionRequestHeaderClaims"
+ "customDecryptionRequestValues"
+ "customFederationUserPreauthenticationRequestValues"
+ "customKeyExchangeRequestBodyClaims"
+ "customKeyExchangeRequestHeaderClaims"
+ "customKeyExchangeRequestValues"
+ "customKeyRequestBodyClaims"
+ "performKeyExchangeRequestWithContext:request:completion:"
+ "performKeyRequestWithContext:request:completion:"
+ "performLoginRequestWithContext:request:completion:"
+ "performLoginWithContext:loginJWT:completion:"
+ "performNonceRequestWithContext:request:completion:"
+ "performPreAuthenticationRequestWithContext:request:completion:"
+ "performWSTrustAuthenticationRequestWithContext:request:completion:"
+ "performWSTrustMexRequestWithContext:request:completion:"
+ "platformSSODevModeTriggerFile"
+ "platformSSOSystemKey"
+ "policyName"
+ "prebootEncryptionAlgorithm"
+ "prebootKey"
+ "preferred_username"
+ "prefixForNamespaceURI:"
+ "previousRefreshTokenClaimName"
+ "printKey:"
+ "psso_DisplayRequest"
+ "psso_base64URLEncodedString"
+ "setFaultactor:"
+ "setFaultcode:"
+ "setFederationMexURL:"
+ "setFederationMexURLKeypath:"
+ "setFederationPredicate:"
+ "setFederationRequestURN:"
+ "setFederationType:"
+ "setFederationUserPreauthenticationURL:"
+ "setGrant_type:"
+ "setGroupRequestClaimName:"
+ "setGroupResponseClaimName:"
+ "setHpkeAuthPublicKey:"
+ "singContext:otherPartyPublicKeyData:completion:"
+ "tionAlgorithm:"
+ "ue:"
- "UICABackdropLayer"
- "UICellAccessoryConfiguration"
- "UICellAccessoryManager"
- "UIContentSizeCategoryPreference"
- "UIDragPreviewParameters"
- "UIDragPreviewShadowProperties"
- "UIDraggingBeginningSessionConfiguration"
- "UIDraggingSessionConfiguration"
- "UIInterpolatedCornerRadii"
- "UIKeyboardUIHandle"
- "UIKeyboardUIService"
- "UISceneSizeRestrictions"
- "UITableCellAccessoryLayout"
- "UITableConstants_CarPlay"
- "UITableConstants_IOS"
- "UITableConstants_Pad"
- "UITableConstants_Phone"
- "UITableConstants_TV"
- "UITableConstants_Watch"
- "UITableViewCell"
- "UITableViewCellContentView"
- "UITableViewCellDetailDisclosureView"
- "UITableViewCellEditControl"
- "UITableViewCellEditingData"
- "UITableViewCellFocusableEditControl"
- "UITableViewCellFocusableReorderControl"
- "UITableViewCellLayoutManagerSubtitle"
- "UITableViewCellLayoutManagerValue1"
- "UITableViewCellLayoutManagerValue2"
- "UITableViewCellReorderControl"
- "UITableViewCellSelectedBackground"
- "UITextCursorAssertionController"
- "UITextDragAssistant"
- "UITextDragDropSupport"
- "UITextDragFinishState"
- "UITextDragPreviewRenderer"
- "UITextDragRequest"
- "UITextDraggableGeometrySameViewDropOperationResult"
- "UITextDraggableObject"
- "UITextFormattingCoordinator"
- "UITextFormattingViewControllerFormattingStyle"
- "UIUpdateActionPhase"
- "UIWKAutocorrectionContext"
- "UIWindowSceneTouchCancellationOnRotationAssertion"
- "UIZoomTransitionAlignmentRectContext"
- "UIZoomTransitionInteractionContext"
- "UIZoomTransitionOptions"
- "_UIBurnableBlock"
- "_UICellAccessory"
- "_UICellSpacingAccessory"
- "_UICellViewAccessory"
- "_UICollectionViewSubviewRouter"
- "_UICollectionViewSubviewRouterBookmark"
- "_UIColorSampler"
- "_UIContentSizeCategoryPreferenceSystem"
- "_UIDatePickerWheelsTimeLabel"
- "_UIDefaultSwipeViewManipulator"
- "_UIFluidSliderDiscreteButtonDriverSettings"
- "_UIFluidSliderDriverSettings"
- "_UIFluidSliderElasticPanDriverSettings"
- "_UIFluidSliderSettings"
- "_UIFluidSliderSettingsDomain"
- "_UIFocusEnvironmentPreferenceCache"
- "_UIFocusRegionEvaluator"
- "_UIGroupTableViewCellBackground_TV"
- "_UIInputViewAnimationAssertion"
- "_UILegacyPageControlVisualProvider"
- "_UIListSeparatorConfiguration"
- "_UIPhysicalButtonAction"
- "_UIPhysicalButtonActionContext"
- "_UIPhysicalButtonInteraction"
- "_UIReturnToDocumentAction"
- "_UISceneHostingContentSizePreferenceExtension"
- "_UISceneHostingEventDeferringHostComponent"
- "_UIShareableContentSceneComponent"
- "_UIStatusBarVisualProvider_PillRegionCoordinator"
- "_UITableViewCellActionButton"
- "_UITableViewCellBadge"
- "_UITableViewCellSeparatorView"
- "_UITableViewCellSwipeContainerView"
- "_UITableViewCellVerticalSeparator"
- "_UITextCursorAssertion"
- "_UITextCursorTrailingGlowView"
- "_UITextInputSessionDeletionAction"
- "_UITextInputSessionDictationBeganAction"
- "_UITextInputSessionDictationEndedAction"
- "_UITextInputSessionEndAction"
- "_UITextInputSessionInsertionAction"
- "_UITextInputSessionKeyboardDockItemButtonPressAction"
- "_UITextInputSessionSelectionAction"
- "_UITextStorageDraggableGeometry"
- "_UIVisualEffectBackdropView"
- "_UIWindowSceneFullscreenPlacement"
- "_UIWindowSceneOverlayPlacement"
- "essionBeganAction"

```
