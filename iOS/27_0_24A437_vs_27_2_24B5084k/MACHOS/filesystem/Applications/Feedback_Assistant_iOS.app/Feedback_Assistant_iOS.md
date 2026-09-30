## Feedback Assistant iOS

> `/Applications/Feedback Assistant iOS.app/Feedback Assistant iOS`

### Sections with Same Size but Changed Content

- `__TEXT.__swift5_typeref`
- `__TEXT.__swift5_fieldmd`
- `__TEXT.__swift5_assocty`
- `__TEXT.__swift5_capture`
- `__TEXT.__swift5_proto`
- `__TEXT.__swift5_types`
- `__TEXT.__swift5_protos`
- `__TEXT.__eh_frame`
- `__DATA_CONST.__objc_catlist`
- `__DATA_CONST.__objc_protolist`
- `__DATA_CONST.__objc_protorefs`
- `__DATA_CONST.__auth_ptr`
- `__DATA.__data`
- `__DATA.__objc_stublist`

```diff

-639.0.0.0.0
-  __TEXT.__text: 0x73eb0
-  __TEXT.__auth_stubs: 0x2250
-  __TEXT.__objc_stubs: 0xad40
-  __TEXT.__objc_methlist: 0x52ac
-  __TEXT.__const: 0x2174
-  __TEXT.__gcc_except_tab: 0x580
-  __TEXT.__objc_methname: 0xf71f
-  __TEXT.__cstring: 0x41b2
-  __TEXT.__oslogstring: 0x2734
-  __TEXT.__objc_classname: 0x1122
-  __TEXT.__objc_methtype: 0x3dc5
+641.0.0.0.0
+  __TEXT.__text: 0x71b10
+  __TEXT.__auth_stubs: 0x2230
+  __TEXT.__objc_stubs: 0xa940
+  __TEXT.__objc_methlist: 0x50d4
+  __TEXT.__const: 0x2164
+  __TEXT.__gcc_except_tab: 0x528
+  __TEXT.__objc_methname: 0xf27f
+  __TEXT.__cstring: 0x4032
+  __TEXT.__oslogstring: 0x22e4
+  __TEXT.__objc_classname: 0x1102
+  __TEXT.__objc_methtype: 0x3d75
   __TEXT.__ustring: 0xcc
-  __TEXT.__constg_swiftt: 0x1ac4
+  __TEXT.__constg_swiftt: 0x1acc
   __TEXT.__swift5_typeref: 0x239a
   __TEXT.__swift5_builtin: 0xc8
   __TEXT.__swift5_reflstr: 0x976

   __TEXT.__swift5_proto: 0xe4
   __TEXT.__swift5_types: 0xf0
   __TEXT.__swift5_protos: 0x8
-  __TEXT.__unwind_info: 0x23f0
+  __TEXT.__unwind_info: 0x2328
   __TEXT.__eh_frame: 0x3a8
-  __DATA_CONST.__const: 0x32b8
-  __DATA_CONST.__cfstring: 0x2420
-  __DATA_CONST.__objc_classlist: 0x280
+  __DATA_CONST.__const: 0x3228
+  __DATA_CONST.__cfstring: 0x21e0
+  __DATA_CONST.__objc_classlist: 0x278
   __DATA_CONST.__objc_catlist: 0x40
   __DATA_CONST.__objc_protolist: 0x1d8
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_protorefs: 0xc8
-  __DATA_CONST.__objc_superrefs: 0xf0
-  __DATA_CONST.__objc_intobj: 0x48
-  __DATA_CONST.__auth_got: 0x1138
-  __DATA_CONST.__got: 0xc28
+  __DATA_CONST.__objc_superrefs: 0xe8
+  __DATA_CONST.__objc_intobj: 0x30
+  __DATA_CONST.__auth_got: 0x1128
+  __DATA_CONST.__got: 0xc18
   __DATA_CONST.__auth_ptr: 0x530
-  __DATA.__objc_const: 0xc900
-  __DATA.__objc_selrefs: 0x3e00
-  __DATA.__objc_ivar: 0x26c
-  __DATA.__objc_data: 0x3978
+  __DATA.__objc_const: 0xc6c0
+  __DATA.__objc_selrefs: 0x3cc8
+  __DATA.__objc_ivar: 0x248
+  __DATA.__objc_data: 0x3930
   __DATA.__data: 0x23c8
   __DATA.__objc_stublist: 0x8
   __DATA.__common: 0x90

   - /System/Library/Frameworks/UniformTypeIdentifiers.framework/UniformTypeIdentifiers
   - /System/Library/Frameworks/UserNotifications.framework/UserNotifications
   - /System/Library/Frameworks/WebKit.framework/WebKit
+  - /System/Library/PrivateFrameworks/AppProtection.framework/AppProtection
   - /System/Library/PrivateFrameworks/AppleAccountUI.framework/AppleAccountUI
   - /System/Library/PrivateFrameworks/AuthKit.framework/AuthKit
   - /System/Library/PrivateFrameworks/AuthKitUI.framework/AuthKitUI

   - /usr/lib/swift/libswift_Builtin_float.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  Functions: 2753
-  Symbols:   1108
-  CStrings:  3630
+  Functions: 2694
+  Symbols:   1104
+  CStrings:  3517
 
Symbols:
+ _OBJC_CLASS_$_APApplication
+ _OBJC_CLASS_$_APGuard
+ _OBJC_CLASS_$_APSettingsManager
- _OBJC_CLASS_$_LAContext
- _OBJC_CLASS_$_NSDate
- _OBJC_CLASS_$_NSTimer
- _OBJC_CLASS_$_UIBlurEffect
- _OBJC_CLASS_$_UIVisualEffectView
- _objc_sync_enter
- _objc_sync_exit
CStrings:
+ "AppProtection authentication checkpoint failed: [%{public}@]"
+ "AppProtection authentication checkpoint passed"
+ "AppProtection lock status is not changeable; deferring legacy biometric lock migration"
+ "FBA already locked by AppProtection; clearing legacy biometric lock preference"
+ "Failed to enable AppProtection lock during migration: [%{public}@]"
+ "Migrated legacy biometric lock preference to AppProtection lock"
+ "TB,N,V_didAttemptBiometricLockMigration"
+ "_didAttemptBiometricLockMigration"
+ "applicationWithBundleIdentifier:"
+ "canChangeLockedStatusOfSubject:"
+ "didAttemptBiometricLockMigration"
+ "initiateAuthenticationWithShieldingForSubject:completion:"
+ "isLocked"
+ "migrateLegacyBiometricLockToAppProtection"
+ "setDidAttemptBiometricLockMigration:"
+ "setHoverStyle:"
+ "setSubject:isLocked:error:"
+ "sharedGuard"
+ "sharedManager"
- "@\"LAContext\""
- "@\"NSTimer\""
- "@\"UIVisualEffectView\""
- "After %lu minutes"
- "Already evaluating biometrics"
- "Application is active and logged in. Biometric state [%lu]"
- "Biometric callback"
- "Biometric evaluation began with context [%@]"
- "Biometric evaluation completed"
- "Biometric evaluation pending. Will perform evaluation"
- "Biometric unlock cancelled by system – likely that user went home."
- "Biometric unlock cancelled by user - likely that user pressed Cancel (suspending)."
- "Biometric unlock failed - not authenticated"
- "Biometric unlock failed - unknown error."
- "Biometric unlock succeeded"
- "Biometric unlock unavailable - biometry is in lockout."
- "Biometrics Evaluation stuck evaluating. Will lock out"
- "Biometrics Evaluation stuck in cancelled state. Will lock out"
- "Biometrics Evaluation stuck in state [%lu]"
- "Biometrics authentication enabled"
- "Biometrics authentication has not timed out"
- "Biometrics authentication is not enabled"
- "Biometrics disabled. Will not save bio timer"
- "Biometrics evaluation callback"
- "Biometrics evaluation completed in background"
- "Biometrics evaluation happened while app was in background - Retrying"
- "Biometrics evaluation timer fired. Current state [%lu], Active? [%i]"
- "Biometrics handler context does not match last used context. Ignoring result"
- "Biometrics stuck - locking out"
- "Did add blur view"
- "FACE_ID_NOT_ENROLLED"
- "FACE_ID_NOT_ENROLLED_MESSAGE"
- "FACE_ID_PREFERENCE"
- "FACE_ID_PROMPT"
- "FACE_ID_REQUIRE"
- "Not Authenticated. Will not save bio timer"
- "Plurals"
- "Saving biometrics date [%@]"
- "SupportsBiometricsLock"
- "T@\"LAContext\",&,N,V_lastUsedLAContext"
- "T@\"NSTimer\",&,V_biometricsWatchDog"
- "T@\"UILabel\",W,N,V_requireTouchIDCellLabel"
- "T@\"UILabel\",W,N,V_touchIDTimeoutLabel"
- "T@\"UILabel\",W,N,V_useTouchIDSwitchCellLabel"
- "T@\"UISwitch\",W,N,V_touchIDSwitch"
- "T@\"UITableViewCell\",W,N,V_touchIDCell"
- "T@\"UIVisualEffectView\",&,N,V_blurView"
- "TB,N,V_hideTouchID"
- "TOUCH_ID_NOT_ENROLLED"
- "TOUCH_ID_NOT_ENROLLED_MESSAGE"
- "TOUCH_ID_PREFERENCE"
- "TOUCH_ID_PROMPT"
- "TOUCH_ID_REQUIRE"
- "TQ,R,V_biometricsState"
- "TimeoutCell"
- "Timer Fired, Authenticated, blurView visible? [%i]"
- "TouchIDEnableRequestShown"
- "TouchIDLastRequested"
- "TouchIDPreferenceCell"
- "TouchIDTimeoutDuration"
- "Will add blur view"
- "Will remove blur view"
- "_biometricsState"
- "_biometricsWatchDog"
- "_blurView"
- "_evaluationPolicy"
- "_hideTouchID"
- "_invalidateWatchDogTimer"
- "_lastUsedLAContext"
- "_logOutForBiometricsAuthFailure"
- "_performBiometricsEvaluationWithContext:"
- "_requireTouchIDCellLabel"
- "_startBiometricsTimer"
- "_touchIDCell"
- "_touchIDDidTimeout"
- "_touchIDSwitch"
- "_touchIDTimeoutLabel"
- "_useTouchIDSwitchCellLabel"
- "addBlurView"
- "bio"
- "biometricsState"
- "biometricsWatchDog"
- "blurView"
- "canEvaluatePolicy:error:"
- "cellConfiguration"
- "context [%@] last context used [%@]"
- "date"
- "dateWithTimeIntervalSince1970:"
- "deviceSupportsFaceID"
- "dictionary"
- "did remove blur view"
- "didToggleTouchID:"
- "effectWithStyle:"
- "evaluatePolicy:localizedReason:reply:"
- "handleInteractiveLoginResultWithLoginManager:pendingUI:startupFailures:skipBiometrics:"
- "hideTouchID"
- "iFBAPreferencesTimeoutViewController"
- "initWithEffect:"
- "invalidate"
- "lastUsedLAContext"
- "newLAContext"
- "not logged in, removing blur view"
- "performBiometricAuthenticationIfNeeded"
- "q24@0:8q16"
- "removeBlurView"
- "requireTouchIDCellLabel"
- "rowForTimeout:"
- "saveBiometricsDate"
- "scheduledTimerWithTimeInterval:repeats:block:"
- "setBiometricsState:"
- "setBiometricsWatchDog:"
- "setBlurView:"
- "setHideTouchID:"
- "setLastUsedLAContext:"
- "setOn:"
- "setRequireTouchIDCellLabel:"
- "setTouchIDCell:"
- "setTouchIDSwitch:"
- "setTouchIDTimeoutLabel:"
- "setUseTouchIDSwitchCellLabel:"
- "supportsBiometricsLock"
- "suspendReturningToLastApp:"
- "timeIntervalSinceDate:"
- "timeoutForRow:"
- "touchIDCell"
- "touchIDSwitch"
- "touchIDTimeoutLabel"
- "useTouchIDSwitchCellLabel"
- "v16@?0@\"NSTimer\"8"
- "v44@0:8@16Q24Q32B40"
- "will perform biometric evaluation if needed"
- "\xd1"
```
