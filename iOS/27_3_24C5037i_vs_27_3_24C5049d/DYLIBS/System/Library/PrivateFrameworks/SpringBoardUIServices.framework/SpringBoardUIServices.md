## SpringBoardUIServices

> `/System/Library/PrivateFrameworks/SpringBoardUIServices.framework/SpringBoardUIServices`

```diff

-4637.2.11.104.0
-  __TEXT.__text: 0xa7454
-  __TEXT.__objc_methlist: 0xf72c
-  __TEXT.__const: 0xbb0
-  __TEXT.__gcc_except_tab: 0xa1c
-  __TEXT.__cstring: 0xaec3
+4637.2.17.3.0
+  __TEXT.__text: 0xa9ec8
+  __TEXT.__objc_methlist: 0xfa7c
+  __TEXT.__const: 0xbd0
+  __TEXT.__gcc_except_tab: 0xab0
+  __TEXT.__cstring: 0xb024
   __TEXT.__dlopen_cstrs: 0x42e
   __TEXT.__ustring: 0x4
-  __TEXT.__oslogstring: 0x4e6f
-  __TEXT.__unwind_info: 0x4338
+  __TEXT.__oslogstring: 0x5628
+  __TEXT.__unwind_info: 0x4440
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0
   __TEXT.__objc_classname: 0x0
   __TEXT.__objc_methname: 0x0
   __TEXT.__objc_methtype: 0x0
-  __DATA_CONST.__const: 0x2d38
-  __DATA_CONST.__objc_classlist: 0x9f0
+  __DATA_CONST.__const: 0x2db8
+  __DATA_CONST.__objc_classlist: 0xa00
   __DATA_CONST.__objc_catlist: 0xd8
-  __DATA_CONST.__objc_protolist: 0x4d0
+  __DATA_CONST.__objc_protolist: 0x4e0
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x8478
-  __DATA_CONST.__objc_protorefs: 0x150
+  __DATA_CONST.__objc_selrefs: 0x8648
+  __DATA_CONST.__objc_protorefs: 0x158
   __DATA_CONST.__objc_superrefs: 0x610
   __DATA_CONST.__objc_arraydata: 0x110
-  __DATA_CONST.__got: 0x1140
+  __DATA_CONST.__got: 0x1160
   __AUTH_CONST.__const: 0xa40
-  __AUTH_CONST.__cfstring: 0xa600
-  __AUTH_CONST.__objc_const: 0x2f9c8
+  __AUTH_CONST.__cfstring: 0xa740
+  __AUTH_CONST.__objc_const: 0x30528
   __AUTH_CONST.__objc_doubleobj: 0x160
   __AUTH_CONST.__objc_floatobj: 0x10
   __AUTH_CONST.__objc_intobj: 0x168
   __AUTH_CONST.__objc_dictobj: 0x28
   __AUTH_CONST.__objc_arrayobj: 0x138
   __AUTH_CONST.__auth_got: 0x0
-  __AUTH.__objc_data: 0x5488
-  __DATA.__objc_ivar: 0xe2c
-  __DATA.__data: 0x39f0
+  __AUTH.__objc_data: 0x5528
+  __DATA.__objc_ivar: 0xe58
+  __DATA.__data: 0x3ab0
   __DATA_DIRTY.__objc_data: 0xed8
   __DATA_DIRTY.__data: 0x8
   __DATA_DIRTY.__bss: 0x8

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libicucore.A.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 5091
-  Symbols:   9886
-  CStrings:  1881
+  Functions: 5162
+  Symbols:   9995
+  CStrings:  1918
 
Symbols:
+ +[SBSUICloseToLockSceneExtension clientComponents]
+ +[SBSUICloseToLockSceneExtension clientSettingsExtensions]
+ +[SBSUICloseToLockSceneExtension hostComponents]
+ +[SBUIPhoneUnlockWithWatchController errorCodeIndicatesWatchUnavailable:]
+ -[FBSScene(SBSUICloseToLockClient) sbsui_closeToLockClient]
+ -[SBSUICloseToLockClientComponent setCloseToLockDisabled:]
+ -[SBUIBiometricResource _bioConvenienceSuppressionDidChange]
+ -[SBUIBiometricResource _credentialSetForMatchMode:]
+ -[SBUIBiometricResource _isUnlockAllowedForDeviceKind:]
+ -[SBUIBiometricResource _noteUpdatedFingerPresence:]
+ -[SBUIBiometricResource _notifyObserversOfEvent:forDeviceKind:]
+ -[SBUIBiometricResource _prewarmBioConvenienceIfEligible]
+ -[SBUIBiometricResource _restartTouchIDOperationsForStrictTouchCoverageForAssertion:]
+ -[SBUIBiometricResource _shouldActivateMatchOperations]
+ -[SBUIBiometricResource _startMatchOperations:forAssertion:]
+ -[SBUIBiometricResource _transferBioConvenienceOperationsFromAssertion:toAssertion:]
+ -[SBUIBiometricResource _updateHandlersForEvent:forDeviceKind:]
+ -[SBUIBiometricResource _updateLastBioUnlockDeviceKind]
+ -[SBUIBiometricResource acquireBioConvenienceSuppressionAssertionForReason:]
+ -[SBUIBiometricResource acquireMatchingAssertionWithMode:reason:replacingAssertion:]
+ -[SBUIBiometricResource biometricKitInterface:handleEvent:forDeviceKind:]
+ -[SBUIBiometricResource hasBioConvenienceSupport]
+ -[SBUIBiometricResource hasVisualBiometricSupport]
+ -[SBUIBiometricResource isBioConvenienceSuppressed]
+ -[SBUIBiometricResource lastBioUnlockDeviceKind]
+ -[SBUIBiometricResource lastBioUnlockPlaysAccessibilityAuthenticationHaptic]
+ -[SBUIPasscodeBiometricResource acquireBioConvenienceSuppressionAssertionForReason:]
+ -[SBUIPasscodeBiometricResource hasBioConvenienceSupport]
+ -[SBUIPasscodeBiometricResource hasVisualBiometricSupport]
+ -[SBUIPasscodeBiometricResource isBioConvenienceSuppressed]
+ -[SBUIPasscodeBiometricResource lastBioUnlockDeviceKind]
+ -[SBUIPasscodeBiometricResource lastBioUnlockPlaysAccessibilityAuthenticationHaptic]
+ -[SBUIPasscodeLockViewBase _beginPasscodeEntryUnlockSuppressionIfTouchIDLockedOut]
+ -[SBUIPasscodeLockViewBase _biometricAuthenticationLockoutState]
+ -[SBUIPasscodeLockViewBase _biometricHardwareDeviceKind]
+ -[SBUIPasscodeLockViewBase _endPasscodeEntryUnlockSuppression]
+ -[SBUIPasscodeLockViewBase _lastBioUnlockWasTouchID]
+ -[SBUIPasscodeLockViewBase _noteEntryFieldTextDidChange]
+ -[SBUIPasscodeLockViewBase _showPendingWatchUnlockFailureStatus]
+ -[SBUIPasscodeLockViewBase biometricResource:observeEvent:forDeviceKind:]
+ -[SBUIPhoneUnlockWithRemoteDeviceCoordinator biometricResource:observeEvent:forDeviceKind:]
+ -[SBUIPhoneUnlockWithWatchController _cancelUnlockAttempt]
+ -[SBUIPhoneUnlockWithWatchController _lockoutStatePermitsPhoneUnlockWithWatch]
+ -[SBUIPhoneUnlockWithWatchController isTouchIDPhoneWithoutHomeButton]
+ -[SBUIPhoneUnlockWithWatchController isUnlockSuppressed]
+ -[UIWindowScene(SBSUICloseToLockClient) sbsui_closeToLockClient]
+ -[_SBUIBiometricKitInterface _createMatchOperationsForDevices:withMode:credentialSet:error:]
+ -[_SBUIBiometricKitInterface _deviceKindForOperation:]
+ -[_SBUIBiometricKitInterface _hardwareDeviceKind]
+ -[_SBUIBiometricKitInterface _sendDelegateEvent:forOperation:]
+ -[_SBUIBiometricKitInterface bioConvenienceMatchModeForMatchMode:]
+ -[_SBUIBiometricKitInterface createMatchOperationsWithMode:credentialSet:error:]
+ -[_SBUIBiometricKitInterface createMatchOperationsWithMode:credentialSet:excludingDeviceKind:error:]
+ -[_SBUIBiometricKitInterface createMatchOperationsWithMode:credentialSet:forDeviceKind:error:]
+ -[_SBUIBiometricKitInterface isBioConvenienceCapable]
+ -[_SBUIBiometricKitInterface isBioConvenienceMatchingSuppressed]
+ -[_SBUIBiometricKitInterface isBioConvenienceOperation:]
+ -[_SBUIBiometricKitInterface isTouchIDMatchingSuppressed]
+ -[_SBUIBiometricKitInterface isTouchIDOperation:]
+ -[_SBUIBiometricKitInterface lastTouchDidFailToMatch]
+ -[_SBUIBiometricKitInterface prewarmBioConvenience]
+ -[_SBUIBiometricKitInterface setBioConvenienceMatchingSuppressed:]
+ -[_SBUIBiometricKitInterface setLastTouchDidFailToMatch:]
+ -[_SBUIBiometricKitInterface setTouchIDMatchingSuppressed:]
+ -[_SBUIBiometricKitInterface updateFingerPresenceWithOperations:completion:]
+ GCC_except_table150
+ GCC_except_table30
+ GCC_except_table35
+ GCC_except_table37
+ GCC_except_table40
+ GCC_except_table42
+ GCC_except_table44
+ GCC_except_table75
+ GCC_except_table79
+ _MCFeatureFingerprintUnlockAllowed
+ _OBJC_CLASS_$_BSAuditToken
+ _OBJC_CLASS_$_SBSUICloseToLockClientComponent
+ _OBJC_CLASS_$_SBSUICloseToLockSceneExtension
+ _OBJC_IVAR_$_SBUIBiometricResource._bioConvenienceSuppressionAssertions
+ _OBJC_IVAR_$_SBUIBiometricResource._hasBioConvenienceCapability
+ _OBJC_IVAR_$_SBUIBiometricResource._hasFingerPresenceSinceScreenOff
+ _OBJC_IVAR_$_SBUIBiometricResource._lastBioUnlockDeviceKind
+ _OBJC_IVAR_$_SBUIPasscodeLockViewBase._bioConvenienceSuppressionAssertion
+ _OBJC_IVAR_$_SBUIPasscodeLockViewBase._watchUnlockSuppressionAssertion
+ _OBJC_IVAR_$__SBUIBiometricKitInterface._bioConvenienceDevice
+ _OBJC_IVAR_$__SBUIBiometricKitInterface._bioConvenienceMatchingSuppressed
+ _OBJC_IVAR_$__SBUIBiometricKitInterface._bioConveniencePrewarmQueue
+ _OBJC_IVAR_$__SBUIBiometricKitInterface._isBioConveniencePrewarming
+ _OBJC_IVAR_$__SBUIBiometricKitInterface._isDeferringBioConvenienceDeviceAccess
+ _OBJC_IVAR_$__SBUIBiometricKitInterface._lastTouchDidFailToMatch
+ _OBJC_IVAR_$__SBUIBiometricKitInterface._touchIDMatchingSuppressed
+ _OBJC_METACLASS_$_SBSUICloseToLockClientComponent
+ _OBJC_METACLASS_$_SBSUICloseToLockSceneExtension
+ _SBUIBiometricEventSuppressesFailureFeedback
+ __OBJC_$_CLASS_METHODS_SBSUICloseToLockSceneExtension
+ __OBJC_$_INSTANCE_METHODS_FBSScene(Resizability|SBSUISurfaceTypeClient|SBSUICameraOverlaySceneClientMonitor|SBSUICloseToLockClient|SBSUIRemoteAlertSceneClientComponent|SBUIContinuitySessionParticipantClientComponent|SBContinuitySessionSceneParticipant)
+ __OBJC_$_INSTANCE_METHODS_SBSUICloseToLockClientComponent
+ __OBJC_$_INSTANCE_METHODS_UIWindowScene(SBSUIScreenSharingOverlaySceneSpecification|RetailDemoSupport|Resizability|SBSUISurfaceTypeClient|SBSUIHearingTestModeAdditions|SBSUICloseToLockClient|SBUISystemAperture)
+ __OBJC_$_PROP_LIST_SBSUICloseToLockClientComponent
+ __OBJC_$_PROP_LIST_SBSUICloseToLockClientSettings
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_SBSUICloseToLockClient
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_SBSUICloseToLockClientSettings
+ __OBJC_$_PROTOCOL_METHOD_TYPES_SBSUICloseToLockClient
+ __OBJC_$_PROTOCOL_METHOD_TYPES_SBSUICloseToLockClientSettings
+ __OBJC_$_PROTOCOL_REFS_SBSUICloseToLockClient
+ __OBJC_$_PROTOCOL_REFS_SBSUICloseToLockClientSettings
+ __OBJC_CLASS_PROTOCOLS_$_SBSUICloseToLockClientComponent
+ __OBJC_CLASS_RO_$_SBSUICloseToLockClientComponent
+ __OBJC_CLASS_RO_$_SBSUICloseToLockSceneExtension
+ __OBJC_LABEL_PROTOCOL_$_SBSUICloseToLockClient
+ __OBJC_LABEL_PROTOCOL_$_SBSUICloseToLockClientSettings
+ __OBJC_METACLASS_RO_$_SBSUICloseToLockClientComponent
+ __OBJC_METACLASS_RO_$_SBSUICloseToLockSceneExtension
+ __OBJC_PROTOCOL_$_SBSUICloseToLockClient
+ __OBJC_PROTOCOL_$_SBSUICloseToLockClientSettings
+ __OBJC_PROTOCOL_REFERENCE_$_SBSUICloseToLockClientSettings
+ ___34-[_SBUIBiometricKitInterface init]_block_invoke_2
+ ___34-[_SBUIBiometricKitInterface init]_block_invoke_3
+ ___51-[_SBUIBiometricKitInterface prewarmBioConvenience]_block_invoke
+ ___58-[SBSUICloseToLockClientComponent setCloseToLockDisabled:]_block_invoke
+ ___60-[SBUIBiometricResource _startMatchOperations:forAssertion:]_block_invoke
+ ___60-[SBUIBiometricResource _startMatchOperations:forAssertion:]_block_invoke_2
+ ___63-[SBUIBiometricResource _updateHandlersForEvent:forDeviceKind:]_block_invoke
+ ___69-[SBUIBiometricResource _updateFingerPresenceIfNeededWithOperations:]_block_invoke
+ ___73-[SBUIPasscodeLockViewBase biometricResource:observeEvent:forDeviceKind:]_block_invoke
+ ___76-[SBUIBiometricResource acquireBioConvenienceSuppressionAssertionForReason:]_block_invoke
+ ___76-[_SBUIBiometricKitInterface updateFingerPresenceWithOperations:completion:]_block_invoke
+ ___76-[_SBUIBiometricKitInterface updateFingerPresenceWithOperations:completion:]_block_invoke_2
+ ___81-[SBUIPhoneUnlockWithWatchController acquireUnlockSuppressionAssertionForReason:]_block_invoke
+ ___84-[SBUIBiometricResource acquireMatchingAssertionWithMode:reason:replacingAssertion:]_block_invoke
+ ___91-[SBUIPhoneUnlockWithRemoteDeviceCoordinator biometricResource:observeEvent:forDeviceKind:]_block_invoke
+ ___block_descriptor_48_e8_32s40w_e5_v8?0ls32l8w40l8
+ ___block_descriptor_56_e8_32s40s48bs_e5_v8?0ls32l8s40l8s48l8
+ ___block_descriptor_64_e8_32s40s48s56bs_e5_v8?0ls32l8s40l8s48l8s56l8
- -[SBUIBiometricResource _notifyObserversOfEvent:]
- -[SBUIBiometricResource _updateHandlersForEvent:]
- -[SBUIBiometricResource biometricKitInterface:handleEvent:]
- -[SBUIPasscodeLockViewBase biometricResource:observeEvent:]
- -[SBUIPhoneUnlockWithRemoteDeviceCoordinator biometricResource:observeEvent:]
- -[_SBUIBiometricKitInterface createMatchOperationsWithMode:andCredentialSet:error:]
- -[_SBUIBiometricKitInterface updateFingerPresenceWithOperations:]
- GCC_except_table145
- GCC_except_table29
- GCC_except_table31
- GCC_except_table34
- GCC_except_table36
- GCC_except_table64
- _OBJC_IVAR_$_SBUIBiometricResource._bkMatchConvenienceOperationClass
- _OBJC_IVAR_$__SBUIBiometricKitInterface._currentTouchDidFailToMatch
- __OBJC_$_INSTANCE_METHODS_FBSScene(Resizability|SBSUISurfaceTypeClient|SBSUICameraOverlaySceneClientMonitor|SBSUIRemoteAlertSceneClientComponent|SBUIContinuitySessionParticipantClientComponent|SBContinuitySessionSceneParticipant)
- __OBJC_$_INSTANCE_METHODS_UIWindowScene(SBSUIScreenSharingOverlaySceneSpecification|RetailDemoSupport|Resizability|SBSUISurfaceTypeClient|SBSUIHearingTestModeAdditions|SBUISystemAperture)
- ___49-[SBUIBiometricResource _activateMatchAssertion:]_block_invoke
- ___49-[SBUIBiometricResource _activateMatchAssertion:]_block_invoke_2
- ___49-[SBUIBiometricResource _updateHandlersForEvent:]_block_invoke
- ___59-[SBUIPasscodeLockViewBase biometricResource:observeEvent:]_block_invoke
- ___65-[SBUIBiometricResource acquireMatchingAssertionWithMode:reason:]_block_invoke
- ___65-[_SBUIBiometricKitInterface updateFingerPresenceWithOperations:]_block_invoke
- ___65-[_SBUIBiometricKitInterface updateFingerPresenceWithOperations:]_block_invoke_2
- ___77-[SBUIPhoneUnlockWithRemoteDeviceCoordinator biometricResource:observeEvent:]_block_invoke
CStrings:
+ "BKDeviceConvenience"
+ "Bio unlock attributed to device: %{public}@, finger present since screen off: %d, finger on: %d"
+ "BioConvenience"
+ "BioConvenience prewarm complete"
+ "BioConvenience prewarm failed: %{public}@"
+ "BioConvenience suppressed: %d for assertions: %@"
+ "BioConvenienceSuppression"
+ "BioConvenienceSuppressionAssertions"
+ "Cancelling BioConvenience operation %{public}@ for match assertion %{public}@, BioConvenience suppressed"
+ "Cancelling phone unlock with watch attempt, unlock is suppressed"
+ "Failed to create operations for match assertion %{public}@, not handing off BioConvenience operations: %{public}@"
+ "Failed to replace Touch ID operations for match assertion %{public}@ with error %{public}@"
+ "Handing off UC match operations %{public}@ from assertion %{public}@ to %{public}@"
+ "Ignoring biometric event %{public}@ on passcode view, failure feedback is suppressed"
+ "Ignoring phone unlock with watch failure while unlock is suppressed: %{public}@"
+ "Match mode should have been resolved per-device by -_matchModeForDevice: %@"
+ "Not attempting phone unlock with watch because of biolockout: %{public}@"
+ "Not prewarming BioConvenience, capability isn't enabled"
+ "Not prewarming BioConvenience, deferring device access until first unlock"
+ "Not prewarming BioConvenience, device is locked out: %{public}@"
+ "Not prewarming BioConvenience, no device support"
+ "Not prewarming BioConvenience, prewarm already in flight"
+ "Not restarting match assertion %{public}@ for BioConvenience, finger is on"
+ "Passcode entry began with Touch ID lockout state %{public}@, suppressing UC/PAU unlocks"
+ "Passcode entry for Touch ID biolock"
+ "PreArmAndBioConvenienceUnlock"
+ "Received commit of scene size: %{public}@"
+ "Replacing Touch ID operations %{public}@ for match assertion %{public}@"
+ "Restarting match assertion %{public}@ for BioConvenience, BioConvenience is no longer suppressed"
+ "SBCloseToLockHostComponent"
+ "SBSUICloseToLockClientComponent: process lacks %{public}@, not setting disablesCloseToLock"
+ "Skipping PAU failure feedback, unlock error %ld indicates Watch unavailablity"
+ "Skipping creation of BioConvenience match operation, BioConvenience matching is suppressed"
+ "Skipping creation of BioConvenience match operation, lockout state %{public}@"
+ "Skipping creation of Touch ID match operation, Touch ID matching is suppressed"
+ "Starting BioConvenience prewarm"
+ "com.apple.springboard.bioconvenience.prewarm"
+ "com.apple.springboard.disableCloseToLock"
+ "\xf0\xb1"
- "Not attempting phone unlock with watch because of biolockout"
- "\xf0\x91"
```
