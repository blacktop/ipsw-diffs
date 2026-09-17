## Erase Assistant

> `/System/Library/CoreServices/Erase Assistant.app/Contents/MacOS/Erase Assistant`

### Sections with Same Size but Changed Content

- `__DATA_CONST.__cfstring`
- `__DATA_CONST.__objc_arraydata`
- `__DATA_CONST.__objc_arrayobj`

```diff

-285.0.0.0.0
-  __TEXT.__text: 0xcfb0
-  __TEXT.__auth_stubs: 0x3b0
-  __TEXT.__objc_stubs: 0x2bc0
-  __TEXT.__objc_methlist: 0x1060
-  __TEXT.__const: 0x90
-  __TEXT.__cstring: 0xde1
-  __TEXT.__oslogstring: 0x800
-  __TEXT.__objc_classname: 0x290
-  __TEXT.__objc_methname: 0x3265
-  __TEXT.__objc_methtype: 0xac2
-  __TEXT.__gcc_except_tab: 0x58
+285.1.3.0.0
+  __TEXT.__text: 0xe3ec
+  __TEXT.__auth_stubs: 0x3d0
+  __TEXT.__objc_stubs: 0x3000
+  __TEXT.__objc_methlist: 0x1238
+  __TEXT.__const: 0xa8
+  __TEXT.__cstring: 0xe67
+  __TEXT.__oslogstring: 0x937
+  __TEXT.__objc_classname: 0x2de
+  __TEXT.__objc_methname: 0x386c
+  __TEXT.__objc_methtype: 0xb3c
+  __TEXT.__gcc_except_tab: 0x78
   __TEXT.__dlopen_cstrs: 0x64
-  __TEXT.__unwind_info: 0x3e8
-  __DATA_CONST.__const: 0x550
+  __TEXT.__unwind_info: 0x448
+  __DATA_CONST.__const: 0x568
   __DATA_CONST.__cfstring: 0x12a0
-  __DATA_CONST.__objc_classlist: 0x88
-  __DATA_CONST.__objc_protolist: 0x50
+  __DATA_CONST.__objc_classlist: 0x98
+  __DATA_CONST.__objc_protolist: 0x60
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_superrefs: 0x38
+  __DATA_CONST.__objc_superrefs: 0x40
   __DATA_CONST.__objc_arraydata: 0x20
   __DATA_CONST.__objc_arrayobj: 0x30
-  __DATA_CONST.__auth_got: 0x1e8
-  __DATA_CONST.__got: 0x2c0
-  __DATA.__objc_const: 0x1b70
-  __DATA.__objc_selrefs: 0xea8
-  __DATA.__objc_ivar: 0xd8
-  __DATA.__objc_data: 0x550
-  __DATA.__data: 0x3c0
+  __DATA_CONST.__auth_got: 0x1f8
+  __DATA_CONST.__got: 0x2e8
+  __DATA.__objc_const: 0x1f98
+  __DATA.__objc_selrefs: 0xfd0
+  __DATA.__objc_ivar: 0x100
+  __DATA.__objc_data: 0x5f0
+  __DATA.__data: 0x480
   - /System/Library/Frameworks/Accounts.framework/Versions/A/Accounts
   - /System/Library/Frameworks/AppKit.framework/Versions/C/AppKit
   - /System/Library/Frameworks/CoreBluetooth.framework/Versions/A/CoreBluetooth

   - /System/Library/Frameworks/LocalAuthentication.framework/Versions/A/LocalAuthentication
   - /System/Library/Frameworks/LocalAuthenticationEmbeddedUI.framework/Versions/A/LocalAuthenticationEmbeddedUI
   - /System/Library/Frameworks/QuartzCore.framework/Versions/A/QuartzCore
+  - /System/Library/PrivateFrameworks/AuthKit.framework/Versions/A/AuthKit
   - /System/Library/PrivateFrameworks/BiometricKit.framework/Versions/A/BiometricKit
   - /System/Library/PrivateFrameworks/ConfigurationProfiles.framework/Versions/A/ConfigurationProfiles
   - /System/Library/PrivateFrameworks/CoreAnalytics.framework/Versions/A/CoreAnalytics

   - /System/Library/PrivateFrameworks/LocalAuthenticationRecoveryUI.framework/Versions/A/LocalAuthenticationRecoveryUI
   - /System/Library/PrivateFrameworks/LocalAuthenticationUI.framework/Versions/A/LocalAuthenticationUI
   - /System/Library/PrivateFrameworks/LoginUIKit.framework/Versions/A/LoginUIKit
+  - /System/Library/PrivateFrameworks/OSEligibility.framework/Versions/A/OSEligibility
   - /System/Library/PrivateFrameworks/OnBoardingKit.framework/Versions/A/OnBoardingKit
   - /System/Library/PrivateFrameworks/PassKitCore.framework/Versions/A/PassKitCore
   - /System/Library/PrivateFrameworks/PassKitUI.framework/Versions/A/PassKitUI

   - /System/Library/PrivateFrameworks/TimeMachine.framework/Versions/A/TimeMachine
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 299
-  Symbols:   164
-  CStrings:  906
+  Functions: 337
+  Symbols:   171
+  CStrings:  980
 
Symbols:
+ _DKEACSSanitizeStorage
+ _OBJC_CLASS_$_AKAppleIDAuthenticationContext
+ _OBJC_CLASS_$_AKAppleIDAuthenticationController
+ _OBJC_CLASS_$_NSButton
+ _OBJC_CLASS_$_OSEligibilityQuery
+ _objc_copyWeak
+ _objc_initWeak
CStrings:
+ "@\"DKSanitizeStorageManager\""
+ "@\"NSNumber\""
+ "@\"NSStackView\""
+ "@\"NSView\""
+ "@20@0:8B16"
+ "Account is federated"
+ "Account is not federated"
+ "CANCEL"
+ "DKSanitizeStorageManager"
+ "DKSanitizeStorageProvider"
+ "DUIFederationCheckProvider"
+ "Determining if username is federated auth..."
+ "Device eligibility for sanitization: %lu"
+ "Failed to determine Sanitize Storage eligibility: %@"
+ "Federation auth-mode fetch failed: %{public}@"
+ "ForceAllowSanitization"
+ "Forcing sanitization eligibility to ON"
+ "OVERWRITE_STORAGE_CHECKBOX_TITLE"
+ "SANITIZE_STORAGE_CONFIRMATION_ALERT_BUTTON"
+ "SANITIZE_STORAGE_CONFIRMATION_ALERT_MESSAGE"
+ "SANITIZE_STORAGE_CONFIRMATION_ALERT_TITLE"
+ "Sanitize storage selected: %i"
+ "T@\"DKSanitizeStorageManager\",R,N,V_sanitizeStorageManager"
+ "T@\"NSButton\",&,V_overwriteStorageCheckbox"
+ "T@\"NSNumber\",V_hasFederatedAuthAccount"
+ "T@\"NSStackView\",&,V_passwordStackView"
+ "T@\"NSView\",&,V_bottomLeadingAccessoryView"
+ "TB,N,V_pendingSanitizeStorageEligible"
+ "TB,N,V_pendingSanitizeStorageSelected"
+ "TB,R,N"
+ "TB,V_isFederatedAuthAccount"
+ "TB,V_sanitizeStorageEligible"
+ "TimeMachineDisabled"
+ "TimeMachinePrompted"
+ "_bottomLeadingAccessoryView"
+ "_determineSanitizeStorageEligibility"
+ "_hasFederatedAuthAccount"
+ "_isFederatedAuthAccount"
+ "_overwriteStorageCheckbox"
+ "_passwordStackView"
+ "_pendingSanitizeStorageEligible"
+ "_pendingSanitizeStorageSelected"
+ "_sanitizeStorageEligible"
+ "_sanitizeStorageManager"
+ "answer"
+ "applyFederationStatus:"
+ "bottomLeadingAccessoryView"
+ "centerYAnchor"
+ "checkboxWithTitle:target:action:"
+ "failed to complete iMessage sign out, error: %@"
+ "fetchAuthModeWithContext:completion:"
+ "fetchIsFederatedAccountForUsername:completion:"
+ "hasFederatedAuthAccount"
+ "initWithDomain:error:"
+ "initWithEligibility:"
+ "initWithUserID:password:mdmInitiated:options:"
+ "isEligible"
+ "isFederatedAuthAccount"
+ "overwriteStorageCheckbox"
+ "overwriteStorageCheckboxToggled:"
+ "overwriteStorageSelected"
+ "passwordStackView"
+ "pendingSanitizeStorageEligible"
+ "pendingSanitizeStorageSelected"
+ "presentOverwriteStorageConfirmation"
+ "removeFromSuperview"
+ "requiresFederatedAuthAccountUI"
+ "sanitizeStorageEligible"
+ "sanitizeStorageManager"
+ "sanitizeStorageSelected"
+ "setBottomLeadingAccessoryView:"
+ "setDisplayInfoIcon:"
+ "setHasFederatedAuthAccount:"
+ "setIsFederatedAuthAccount:"
+ "setOverwriteStorageCheckbox:"
+ "setPasswordStackView:"
+ "setPendingSanitizeStorageEligible:"
+ "setPendingSanitizeStorageSelected:"
+ "setSanitizeStorageEligible:"
+ "setState:"
+ "setUsername:"
+ "state"
+ "timeIntervalSinceNow"
+ "v24@?0Q8@\"NSError\"16"
+ "v32@0:8@\"NSString\"16@?<v@?B>24"
+ "v32@0:8@16@?24"
- "alreadyCompleted"
- "cancelledDuringUpload"
- "configurationSkipped"
- "failed to complete iMessage sign out"
- "failedUserCancelled"
- "failedUserSkipped"
- "initWithUserID:password:"
- "notNeeded"
- "notReached"
- "skippedAtPrompt"
- "skippedDuringUpload"
- "uploadCompleted"
```
