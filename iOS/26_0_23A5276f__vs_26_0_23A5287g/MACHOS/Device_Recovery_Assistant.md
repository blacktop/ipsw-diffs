## Device Recovery Assistant

> `/Applications/Device Recovery Assistant.app/Device Recovery Assistant`

```diff

-82.0.0.502.1
-  __TEXT.__text: 0xce64
-  __TEXT.__auth_stubs: 0x5f0
-  __TEXT.__objc_stubs: 0x2f60
-  __TEXT.__objc_methlist: 0x1ab8
-  __TEXT.__cstring: 0x1925
-  __TEXT.__const: 0x30
-  __TEXT.__objc_methname: 0x5209
-  __TEXT.__oslogstring: 0x16ce
-  __TEXT.__objc_classname: 0x3eb
-  __TEXT.__objc_methtype: 0x1fd0
+85.0.0.0.9
+  __TEXT.__text: 0x10674
+  __TEXT.__auth_stubs: 0x630
+  __TEXT.__objc_stubs: 0x3820
+  __TEXT.__objc_methlist: 0x1d48
+  __TEXT.__cstring: 0x1d99
+  __TEXT.__const: 0x38
+  __TEXT.__objc_methname: 0x5b65
+  __TEXT.__oslogstring: 0x2233
+  __TEXT.__objc_classname: 0x437
+  __TEXT.__objc_methtype: 0x207f
   __TEXT.__gcc_except_tab: 0x64
-  __TEXT.__unwind_info: 0x3b0
-  __DATA_CONST.__auth_got: 0x308
-  __DATA_CONST.__got: 0x2f8
-  __DATA_CONST.__const: 0x5f0
-  __DATA_CONST.__cfstring: 0xb40
-  __DATA_CONST.__objc_classlist: 0xa0
-  __DATA_CONST.__objc_protolist: 0xc0
+  __TEXT.__unwind_info: 0x428
+  __DATA_CONST.__auth_got: 0x328
+  __DATA_CONST.__got: 0x340
+  __DATA_CONST.__const: 0x6e8
+  __DATA_CONST.__cfstring: 0xbc0
+  __DATA_CONST.__objc_classlist: 0xb0
+  __DATA_CONST.__objc_protolist: 0xc8
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_superrefs: 0x88
-  __DATA.__objc_const: 0x3098
-  __DATA.__objc_selrefs: 0x1428
-  __DATA.__objc_ivar: 0xd8
-  __DATA.__objc_data: 0x640
-  __DATA.__data: 0x918
-  __DATA.__bss: 0x68
+  __DATA_CONST.__objc_superrefs: 0xa0
+  __DATA.__objc_const: 0x3748
+  __DATA.__objc_selrefs: 0x1680
+  __DATA.__objc_ivar: 0x104
+  __DATA.__objc_data: 0x6e0
+  __DATA.__data: 0x978
+  __DATA.__bss: 0x78
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/CoreGraphics.framework/CoreGraphics
   - /System/Library/Frameworks/CoreImage.framework/CoreImage
+  - /System/Library/Frameworks/CoreServices.framework/CoreServices
   - /System/Library/Frameworks/CoreTelephony.framework/CoreTelephony
   - /System/Library/Frameworks/CoreText.framework/CoreText
   - /System/Library/Frameworks/Foundation.framework/Foundation

   - /System/Library/PrivateFrameworks/InternationalSupport.framework/InternationalSupport
   - /System/Library/PrivateFrameworks/KeyboardArbiter.framework/KeyboardArbiter
   - /System/Library/PrivateFrameworks/ManagedConfiguration.framework/ManagedConfiguration
+  - /System/Library/PrivateFrameworks/MobileSoftwareUpdate.framework/MobileSoftwareUpdate
   - /System/Library/PrivateFrameworks/OnBoardingKit.framework/OnBoardingKit
   - /System/Library/PrivateFrameworks/RunningBoardServices.framework/RunningBoardServices
   - /System/Library/PrivateFrameworks/SetupAssistantUI.framework/SetupAssistantUI
   - /System/Library/PrivateFrameworks/SpringBoardFoundation.framework/SpringBoardFoundation
+  - /System/Library/PrivateFrameworks/SpringBoardUIServices.framework/SpringBoardUIServices
   - /System/Library/PrivateFrameworks/UIKitServices.framework/UIKitServices
   - /System/Library/PrivateFrameworks/WiFiKit.framework/WiFiKit
   - /System/Library/PrivateFrameworks/WiFiKitUI.framework/WiFiKitUI
   - /usr/lib/libMobileGestalt.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: C890596F-B517-3686-A7D6-AA2BE12F0316
-  Functions: 375
-  Symbols:   213
-  CStrings:  1400
+  UUID: 56A4F969-8426-3286-9CA5-757EFD125CC5
+  Functions: 443
+  Symbols:   226
+  CStrings:  1589
 
Symbols:
+ _DeviceRecoveryErrorAttributePasscodeBackOffEndDate
+ _MSUCopyInstalledRecoveryOSVersion
+ _OBJC_CLASS_$_LSApplicationRecord
+ _OBJC_CLASS_$_NSDate
+ _OBJC_CLASS_$_NSDateComponentsFormatter
+ _OBJC_CLASS_$_SBUIPowerDownViewControllerFactory
+ _OBJC_CLASS_$_UIApplication
+ _OBJC_CLASS_$_UIDevice
+ _OBJC_CLASS_$_UINavigationController
+ _OBJC_CLASS_$_UITabBarController
+ _objc_retain_x23
+ _objc_setProperty_atomic_copy
+ _objc_setProperty_nonatomic_copy
CStrings:
+ "%{public}s: An alert or modal managed by DREAlertManager is already visible."
+ "%{public}s: Attempting to undim display due to power long press timer."
+ "%{public}s: Attempting to undim display due to power+volUp long press timer."
+ "%{public}s: Could not find root view controller to present from."
+ "%{public}s: Failed to create power down view controller. Check entitlements and framework linking."
+ "%{public}s: Failed to find presenting view controller for menu sheet."
+ "%{public}s: Failed to find presenting view controller for power down UI."
+ "%{public}s: HID Event phase %ld isn't caught/handled by us"
+ "%{public}s: HID Routing rules initialized."
+ "%{public}s: Invalidated power long press timer."
+ "%{public}s: Invalidated power+volume up long press timer."
+ "%{public}s: Menu sheet cancelled or debug option selected."
+ "%{public}s: Menu sheet presented."
+ "%{public}s: Menu sheet response was %lu"
+ "%{public}s: Menu view requested, but an alert is already presented."
+ "%{public}s: Power + Volume Up long press conditions met. Showing power down view."
+ "%{public}s: Power Down UI presented."
+ "%{public}s: Power button down. Started power long press timer."
+ "%{public}s: Power button long press conditions met. Showing menu view."
+ "%{public}s: Power button short press detected. Toggling display power."
+ "%{public}s: Power button up."
+ "%{public}s: Power down UI dismissed."
+ "%{public}s: Power down cancelled."
+ "%{public}s: Power down request canceled - dismissing power down UI."
+ "%{public}s: Power down requested."
+ "%{public}s: Power down view requested, but an alert is already presented."
+ "%{public}s: Power long press conditions not met (Power:%d, VolUp:%d, ActionTriggered:%d). Menu not shown."
+ "%{public}s: Power long press timer fired."
+ "%{public}s: Power menu response was %lu"
+ "%{public}s: Power+VolUp long press conditions not met (Power:%d, VolUp:%d, ActionTriggered:%d). Power down view not shown."
+ "%{public}s: Power+Volume up long press timer fired."
+ "%{public}s: Presenting menu sheet…"
+ "%{public}s: Presenting power down UI…"
+ "%{public}s: Pushing lockout screen onto stack."
+ "%{public}s: Received powerDownViewRequestCancel from unexpected controller: %@"
+ "%{public}s: Received powerDownViewRequestPowerDown from unexpected controller: %@"
+ "%{public}s: Reset buttons' internal states after UIKit responder chain changes as a workaround for %@"
+ "%{public}s: Showing menu view."
+ "%{public}s: Showing power down view."
+ "%{public}s: Shutdown result was: %{public}@. Error: %{public}@"
+ "%{public}s: Shutting down device…"
+ "%{public}s: Started power+volume up long press timer."
+ "%{public}s: Triggered [Cancel]."
+ "%{public}s: Triggered [Exit Device Recovery]."
+ "%{public}s: Triggered [Reboot NeRD]."
+ "%{public}s: Triggered [Shut Down]."
+ "%{public}s: Volume Down/Home button down."
+ "%{public}s: Volume Down/Home button up. Skipping undim as another action was triggered."
+ "%{public}s: Volume Down/Home button up. Undimming display if needed."
+ "%{public}s: Volume Up button down."
+ "%{public}s: Volume Up button short press detected. Undimming display if needed."
+ "%{public}s: Volume Up button up."
+ "%{public}s: Volume Up button up. Skipping undim as another action was triggered."
+ "%{public}s: [Keyboard HID Event Info] usagePage: 0x%x, usage: 0x%x, phase: %ld, hash: 0x%x. Currently, isPowerButtonDown:%d, isVolumeUpButtonDown:%d"
+ "-[Application _initRoutingRules]"
+ "-[Application _invalidatePowerAndVolumeUpLongPressTimer]"
+ "-[Application _invalidatePowerButtonLongPressTimer]"
+ "-[Application _powerAndVolumeUpLongPressFired:]"
+ "-[Application _powerButtonLongPressFired:]"
+ "-[Application _resetButtonsStatesUIKitWorkaround]"
+ "-[Application _showMenuView]"
+ "-[Application _showMenuView]_block_invoke"
+ "-[Application _showPowerDownView]"
+ "-[Application _showPowerDownView]_block_invoke"
+ "-[Application _startPowerAndVolumeUpLongPressTimerIfNeeded]"
+ "-[Application handlePressEvent:phase:]"
+ "-[DREAlertManager _getTopViewController]"
+ "-[DREAlertManager _isAnyAlertOrModalVisible]"
+ "-[DREAlertManager powerDownViewRequestCancel:]"
+ "-[DREAlertManager powerDownViewRequestCancel:]_block_invoke"
+ "-[DREAlertManager powerDownViewRequestPowerDown:]"
+ "-[DREAlertManager showMenuSheetWithOptions:completion:response:]"
+ "-[DREAlertManager showMenuSheetWithOptions:completion:response:]_block_invoke"
+ "-[DREAlertManager showPowerDownWithCompletion:response:]"
+ "-[DREAlertManager showPowerDownWithCompletion:response:]_block_invoke"
+ "-[SceneDelegate showLockoutViewUntilDate:]"
+ "-[WelcomeViewController menuItems]_block_invoke_2"
+ "@\"NSDate\""
+ "@\"UIViewController\""
+ "@?"
+ "@?16@0:8"
+ "DREAlertManager"
+ "LOCKOUT_DETAIL_FORMAT"
+ "LOCKOUT_TITLE"
+ "LockoutViewController"
+ "SBUIPowerDownViewControllerDelegate"
+ "SHUT_DOWN"
+ "T@\"NSDate\",C,V_endDate"
+ "T@\"NSTimer\",&,N,V_powerAndVolumeUpLongPressTimer"
+ "T@\"NSTimer\",&,N,V_powerButtonLongPressTimer"
+ "T@\"NSTimer\",&,V_lockoutTimer"
+ "T@\"UIViewController\",W,N,V_presentedPowerDownVC"
+ "T@?,C,N,V_powerDownResponse"
+ "TB,N,V_alertVisible"
+ "TB,N,V_isActionTriggeredForCurrentPressSequence"
+ "TB,N,V_isPowerButtonDown"
+ "TB,N,V_isVolumeUpButtonDown"
+ "TB,N,V_powerDownVisible"
+ "_alertVisible"
+ "_descriptionStringForEndDate:"
+ "_endDate"
+ "_findTopViewController:"
+ "_getTopViewController"
+ "_invalidatePowerAndVolumeUpLongPressTimer"
+ "_invalidatePowerButtonLongPressTimer"
+ "_isActionTriggeredForCurrentPressSequence"
+ "_isAnyAlertOrModalVisible"
+ "_isPowerButtonDown"
+ "_isVolumeUpButtonDown"
+ "_lockoutTimer"
+ "_powerAndVolumeUpLongPressFired:"
+ "_powerAndVolumeUpLongPressTimer"
+ "_powerButtonLongPressFired:"
+ "_powerButtonLongPressTimer"
+ "_powerDownResponse"
+ "_powerDownVisible"
+ "_presentedPowerDownVC"
+ "_resetButtonsStatesUIKitWorkaround"
+ "_showExitConfirmation"
+ "_showMenuView"
+ "_showNeRDBootConfirmation"
+ "_showPowerDownView"
+ "_startPowerAndVolumeUpLongPressTimerIfNeeded"
+ "activationState"
+ "alertVisible"
+ "alloc"
+ "bundleIdentifier"
+ "bundleRecordWithApplicationIdentifier:error:"
+ "connectedScenes"
+ "currentDevice"
+ "dismissViewControllerAnimated:completion:"
+ "endDate"
+ "handlePressEvent:phase:"
+ "initWithEndDate:"
+ "isActionTriggeredForCurrentPressSequence"
+ "isHidden"
+ "isPowerButtonDown"
+ "isVolumeUpButtonDown"
+ "keyWindow"
+ "lightGrayColor"
+ "lockoutTimer"
+ "newPowerDownViewController"
+ "now"
+ "popViewControllerAnimated:"
+ "powerAndVolumeUpLongPressTimer"
+ "powerButtonLongPressTimer"
+ "powerDownResponse"
+ "powerDownViewRequestCancel:"
+ "powerDownViewRequestPowerDown:"
+ "powerDownVisible"
+ "presentedPowerDownVC"
+ "presentedViewController"
+ "pressesCancelled:withEvent:"
+ "rdar://151218296"
+ "rootViewController"
+ "scheduledTimerWithTimeInterval:target:selector:userInfo:repeats:"
+ "selectedViewController"
+ "setAlertVisible:"
+ "setAllowedUnits:"
+ "setEndDate:"
+ "setIsActionTriggeredForCurrentPressSequence:"
+ "setIsPowerButtonDown:"
+ "setIsVolumeUpButtonDown:"
+ "setLockoutTimer:"
+ "setModalPresentationStyle:"
+ "setModalTransitionStyle:"
+ "setPowerAndVolumeUpLongPressTimer:"
+ "setPowerButtonLongPressTimer:"
+ "setPowerDownDelegate:"
+ "setPowerDownResponse:"
+ "setPowerDownVisible:"
+ "setPresentedPowerDownVC:"
+ "setUnitsStyle:"
+ "setZeroFormattingBehavior:"
+ "sharedApplication"
+ "showLockoutViewUntilDate:"
+ "showMenuSheetWithOptions:completion:response:"
+ "showPowerDownWithCompletion:response:"
+ "shutdownWithCompletion:"
+ "stringFromTimeInterval:"
+ "timeIntervalSinceDate:"
+ "userInfo"
+ "userInterfaceIdiom"
+ "v12@?0B8"
+ "v16@?0Q8"
+ "v24@0:8@\"NSDate\"16"
+ "v24@0:8@\"UIViewController<SBUIPowerDownViewControllerInterface>\"16"
+ "v24@0:8@?16"
+ "v32@0:8@?16@?24"
+ "v40@0:8Q16@?24@?32"
+ "visibleViewController"
+ "windowScene"
+ "windows"
- "%{public}s: A volume button/Home button pressed. Undimming display if needed"
- "%{public}s: HID Event isn't caught/handled by us"
- "%{public}s: Handle Physical Button Event: %@"
- "%{public}s: Power button pressed. Toggling display power"
- "%{public}s: [Keyboard HID Event Info] usagePage: 0x%x, usage: 0x%x, downEvent: %d, hash: 0x%x"
- "-[Application handlePressEvent:]"
- "-[WelcomeViewController menuItems]_block_invoke"
- "handlePressEvent:"

```
