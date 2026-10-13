## DisembarkUI

> `/System/Library/PrivateFrameworks/DisembarkUI.framework/DisembarkUI`

```diff

-285.1.4.0.0
-  __TEXT.__text: 0x21f30
-  __TEXT.__objc_methlist: 0x2dd0
+285.1.6.0.0
+  __TEXT.__text: 0x23fa8
+  __TEXT.__objc_methlist: 0x3058
   __TEXT.__const: 0x1b4
-  __TEXT.__cstring: 0x20d8
-  __TEXT.__gcc_except_tab: 0x2b8
-  __TEXT.__oslogstring: 0x11cf
+  __TEXT.__cstring: 0x21e8
+  __TEXT.__gcc_except_tab: 0x330
+  __TEXT.__oslogstring: 0x1276
   __TEXT.__dlopen_cstrs: 0xc6
   __TEXT.__swift5_typeref: 0x202
   __TEXT.__swift5_capture: 0x12c

   __TEXT.__swift_as_entry: 0x8
   __TEXT.__swift_as_ret: 0xc
   __TEXT.__swift_as_cont: 0x10
-  __TEXT.__unwind_info: 0xbb8
+  __TEXT.__unwind_info: 0xc80
   __TEXT.__eh_frame: 0x188
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0
   __TEXT.__objc_classname: 0x0
   __TEXT.__objc_methname: 0x0
   __TEXT.__objc_methtype: 0x0
-  __DATA_CONST.__const: 0x10f8
-  __DATA_CONST.__objc_classlist: 0x198
+  __DATA_CONST.__const: 0x1300
+  __DATA_CONST.__objc_classlist: 0x1a0
   __DATA_CONST.__objc_catlist: 0x10
   __DATA_CONST.__objc_protolist: 0x108
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x1df8
+  __DATA_CONST.__objc_selrefs: 0x1fb8
   __DATA_CONST.__objc_protorefs: 0x18
-  __DATA_CONST.__objc_superrefs: 0xc8
-  __DATA_CONST.__got: 0x548
+  __DATA_CONST.__objc_superrefs: 0xd0
+  __DATA_CONST.__got: 0x578
   __AUTH_CONST.__const: 0x4d0
-  __AUTH_CONST.__cfstring: 0x1820
-  __AUTH_CONST.__objc_const: 0x55b8
+  __AUTH_CONST.__cfstring: 0x1860
+  __AUTH_CONST.__objc_const: 0x58d8
   __AUTH_CONST.__objc_intobj: 0x30
-  __AUTH_CONST.__auth_got: 0x5f0
-  __AUTH.__objc_data: 0x10c8
+  __AUTH_CONST.__auth_got: 0x5f8
+  __AUTH.__objc_data: 0x1118
   __AUTH.__data: 0x190
-  __DATA.__objc_ivar: 0x2f4
+  __DATA.__objc_ivar: 0x328
   __DATA.__data: 0xc40
   - /System/Library/Frameworks/Accounts.framework/Accounts
   - /System/Library/Frameworks/AppManagedFeatures.framework/AppManagedFeatures

   - /System/Library/PrivateFrameworks/OnBoardingKit.framework/OnBoardingKit
   - /System/Library/PrivateFrameworks/PassKitCore.framework/PassKitCore
   - /System/Library/PrivateFrameworks/SIMSetupSupport.framework/SIMSetupSupport
+  - /System/Library/PrivateFrameworks/ScreenTimeCore.framework/ScreenTimeCore
   - /System/Library/PrivateFrameworks/SettingsFoundation.framework/SettingsFoundation
   - /System/Library/PrivateFrameworks/SetupAssistant.framework/SetupAssistant
   - /System/Library/PrivateFrameworks/SoftLinking.framework/SoftLinking

   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  Functions: 1055
-  Symbols:   2025
-  CStrings:  406
+  Functions: 1123
+  Symbols:   2128
+  CStrings:  416
 
Symbols:
+ +[DKPasscodeLockoutTimer minutesRemainingForInterval:]
+ +[DKPasscodeLockoutTimer nextRefreshIntervalForInterval:]
+ -[DKPasscodeLockoutTimer .cxx_destruct]
+ -[DKPasscodeLockoutTimer _refresh]
+ -[DKPasscodeLockoutTimer dealloc]
+ -[DKPasscodeLockoutTimer endDate]
+ -[DKPasscodeLockoutTimer initWithEndDate:]
+ -[DKPasscodeLockoutTimer invalidate]
+ -[DKPasscodeLockoutTimer onExpire]
+ -[DKPasscodeLockoutTimer onTick]
+ -[DKPasscodeLockoutTimer setEndDate:]
+ -[DKPasscodeLockoutTimer setOnExpire:]
+ -[DKPasscodeLockoutTimer setOnTick:]
+ -[DKPasscodeLockoutTimer setTimer:]
+ -[DKPasscodeLockoutTimer start]
+ -[DKPasscodeLockoutTimer timer]
+ -[DKPasscodeProvider .cxx_destruct]
+ -[DKPasscodeProvider _completeVerification:success:timeoutDate:attemptCount:]
+ -[DKPasscodeProvider fetchScreenTimePasscodeLockoutStateWithCompletion:]
+ -[DKPasscodeProvider managementState]
+ -[DKPasscodeProvider setManagementState:]
+ -[DKPasscodeProvider verifyScreenTimePasscode:completion:]
+ -[DKScreenTimePasscodeViewController _applyInitialLockoutStateWithTimeoutDate:attemptCount:]
+ -[DKScreenTimePasscodeViewController _applyLockoutStateWithTimeoutDate:attemptCount:]
+ -[DKScreenTimePasscodeViewController _beginLockoutUntilDate:attemptCount:]
+ -[DKScreenTimePasscodeViewController _clearAttemptCount]
+ -[DKScreenTimePasscodeViewController _endLockoutWithAttemptCount:]
+ -[DKScreenTimePasscodeViewController _focusPasscodeEntry]
+ -[DKScreenTimePasscodeViewController _setErrorMessage:]
+ -[DKScreenTimePasscodeViewController _setPasscodeEntryEnabled:]
+ -[DKScreenTimePasscodeViewController _showAttemptCount:]
+ -[DKScreenTimePasscodeViewController _showTimeoutMessageForMinutes:]
+ -[DKScreenTimePasscodeViewController dealloc]
+ -[DKScreenTimePasscodeViewController fetchLockoutState]
+ -[DKScreenTimePasscodeViewController isLockedOut]
+ -[DKScreenTimePasscodeViewController isVerifying]
+ -[DKScreenTimePasscodeViewController lockoutAttemptCount]
+ -[DKScreenTimePasscodeViewController lockoutEndDate]
+ -[DKScreenTimePasscodeViewController lockoutTimer]
+ -[DKScreenTimePasscodeViewController messageContainer]
+ -[DKScreenTimePasscodeViewController messageLabel]
+ -[DKScreenTimePasscodeViewController setFetchLockoutState:]
+ -[DKScreenTimePasscodeViewController setIsLockedOut:]
+ -[DKScreenTimePasscodeViewController setIsVerifying:]
+ -[DKScreenTimePasscodeViewController setLockoutAttemptCount:]
+ -[DKScreenTimePasscodeViewController setLockoutEndDate:]
+ -[DKScreenTimePasscodeViewController setLockoutTimer:]
+ -[DKScreenTimePasscodeViewController setMessageContainer:]
+ -[DKScreenTimePasscodeViewController setMessageLabel:]
+ -[DKScreenTimePasscodeViewController viewDidAppear:]
+ -[DKScreenTimePasscodeViewController viewDidLayoutSubviews]
+ -[DKScreenTimePasscodeViewController viewWillAppear:]
+ GCC_except_table20
+ GCC_except_table94
+ _CGRectGetHeight
+ _OBJC_CLASS_$_DKPasscodeLockoutTimer
+ _OBJC_CLASS_$_NSTimer
+ _OBJC_CLASS_$_STManagementState
+ _OBJC_IVAR_$_DKPasscodeLockoutTimer._endDate
+ _OBJC_IVAR_$_DKPasscodeLockoutTimer._onExpire
+ _OBJC_IVAR_$_DKPasscodeLockoutTimer._onTick
+ _OBJC_IVAR_$_DKPasscodeLockoutTimer._timer
+ _OBJC_IVAR_$_DKPasscodeProvider._managementState
+ _OBJC_IVAR_$_DKScreenTimePasscodeViewController._fetchLockoutState
+ _OBJC_IVAR_$_DKScreenTimePasscodeViewController._isLockedOut
+ _OBJC_IVAR_$_DKScreenTimePasscodeViewController._isVerifying
+ _OBJC_IVAR_$_DKScreenTimePasscodeViewController._lockoutAttemptCount
+ _OBJC_IVAR_$_DKScreenTimePasscodeViewController._lockoutEndDate
+ _OBJC_IVAR_$_DKScreenTimePasscodeViewController._lockoutTimer
+ _OBJC_IVAR_$_DKScreenTimePasscodeViewController._messageContainer
+ _OBJC_IVAR_$_DKScreenTimePasscodeViewController._messageLabel
+ _OBJC_METACLASS_$_DKPasscodeLockoutTimer
+ _OUTLINED_FUNCTION_2
+ _STErrorDomain
+ _STErrorKeyNumberOfPINAuthenticationAttempts
+ _STErrorKeyPINTimeoutDate
+ __OBJC_$_CLASS_METHODS_DKPasscodeLockoutTimer
+ __OBJC_$_INSTANCE_METHODS_DKPasscodeLockoutTimer
+ __OBJC_$_INSTANCE_VARIABLES_DKPasscodeLockoutTimer
+ __OBJC_$_INSTANCE_VARIABLES_DKPasscodeProvider
+ __OBJC_$_PROP_LIST_DKPasscodeLockoutTimer
+ __OBJC_CLASS_RO_$_DKPasscodeLockoutTimer
+ __OBJC_METACLASS_RO_$_DKPasscodeLockoutTimer
+ ___34-[DKPasscodeLockoutTimer _refresh]_block_invoke
+ ___53-[DKScreenTimePasscodeViewController viewWillAppear:]_block_invoke
+ ___53-[DKScreenTimePasscodeViewController viewWillAppear:]_block_invoke_2
+ ___58-[DKPasscodeProvider verifyScreenTimePasscode:completion:]_block_invoke
+ ___72-[DKPasscodeProvider fetchScreenTimePasscodeLockoutStateWithCompletion:]_block_invoke
+ ___74-[DKScreenTimePasscodeViewController _beginLockoutUntilDate:attemptCount:]_block_invoke
+ ___74-[DKScreenTimePasscodeViewController _beginLockoutUntilDate:attemptCount:]_block_invoke_2
+ ___77-[DKPasscodeProvider _completeVerification:success:timeoutDate:attemptCount:]_block_invoke
+ ___78-[DKScreenTimePasscodeViewController passcodeViewController:didEnterPasscode:]_block_invoke
+ ___block_descriptor_40_e8_32bs_e41_v32?0"NSNumber"8"NSDate"16"NSError"24ls32l8
+ ___block_descriptor_40_e8_32s_e34_v16?0?<v?"NSDate""NSNumber">8ls32l8
+ ___block_descriptor_40_e8_32s_e48_v24?0"NSString"8?<v?B"NSDate""NSNumber">16ls32l8
+ ___block_descriptor_40_e8_32w_e17_v16?0"NSTimer"8lw32l8
+ ___block_descriptor_40_e8_32w_e29_v24?0"NSDate"8"NSNumber"16lw32l8
+ ___block_descriptor_40_e8_32w_e5_v8?0lw32l8
+ ___block_descriptor_40_e8_32w_e8_v16?0Q8lw32l8
+ ___block_descriptor_48_e8_32s40bs_e17_v16?0"NSError"8ls32l8s40l8
+ ___block_descriptor_48_e8_32s40bs_e29_v24?0"NSDate"8"NSNumber"16ls40l8s32l8
+ ___block_descriptor_48_e8_32s40w_e32_v28?0B8"NSDate"12"NSNumber"20lw40l8s32l8
+ ___block_descriptor_56_e8_32s40s48bs_e5_v8?0ls48l8s32l8s40l8
+ ___block_descriptor_56_e8_32s40s48w_e5_v8?0lw48l8s32l8s40l8
+ ___block_descriptor_57_e8_32s40s48bs_e5_v8?0ls48l8s32l8s40l8
- -[DKPasscodeProvider verifyScreenTimePasscode:]
- GCC_except_table93
CStrings:
+ "Failed to fetch Screen Time lockout state; treating as unlocked: %{public}@"
+ "SCREEN_TIME_PASSCODE_FAILED_ATTEMPTS"
+ "SCREEN_TIME_PASSCODE_TIMEOUT"
+ "Screen Time passcode verification failed non-recoverably; proceeding with EACS: %{public}@"
+ "v16@?0@\"NSTimer\"8"
+ "v16@?0@?<v@?@\"NSDate\"@\"NSNumber\">8"
+ "v24@?0@\"NSDate\"8@\"NSNumber\"16"
+ "v24@?0@\"NSString\"8@?<v@?B@\"NSDate\"@\"NSNumber\">16"
+ "v28@?0B8@\"NSDate\"12@\"NSNumber\"20"
+ "v32@?0@\"NSNumber\"8@\"NSDate\"16@\"NSError\"24"
```
