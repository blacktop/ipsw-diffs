## PreBoard

> `/System/Library/AccessibilityBundles/PreBoard.axbundle/PreBoard`

```diff

-3005.4.19.0.0
-  __TEXT.__text: 0x1fe4
-  __TEXT.__auth_stubs: 0x2c0
+3005.16.0.0.0
+  __TEXT.__text: 0x2138
+  __TEXT.__auth_stubs: 0x280
   __TEXT.__objc_methlist: 0x210
   __TEXT.__cstring: 0x6cc
   __TEXT.__const: 0x18
-  __TEXT.__gcc_except_tab: 0x64
+  __TEXT.__gcc_except_tab: 0x60
   __TEXT.__dlopen_cstrs: 0x50
   __TEXT.__unwind_info: 0x138
   __TEXT.__objc_classname: 0x236

   __DATA_CONST.__objc_selrefs: 0x158
   __DATA_CONST.__objc_superrefs: 0x28
   __DATA_CONST.__objc_arraydata: 0x30
-  __AUTH_CONST.__auth_got: 0x170
+  __AUTH_CONST.__auth_got: 0x150
   __AUTH_CONST.__const: 0x60
   __AUTH_CONST.__cfstring: 0x960
   __AUTH_CONST.__objc_const: 0x7e0

   - /usr/lib/libAXSafeCategoryBundle.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 6B06C0E3-A5E0-3E59-B2E2-38EB954108C9
+  UUID: A4E48648-B216-3BC8-A720-283CCF6FBC1A
   Functions: 67
-  Symbols:   305
+  Symbols:   301
   CStrings:  227
 
Symbols:
+ _objc_retainAutoreleasedReturnValue
+ _objc_retain_x22
- _objc_claimAutoreleasedReturnValue
- _objc_retainAutoreleaseReturnValue
- _objc_retain_x1
- _objc_retain_x2
- _objc_retain_x3
- _objc_retain_x8
Functions:
~ +[AXPreBoardGlue accessibilityInitializeBundle] : 148 -> 152
~ ___47+[AXPreBoardGlue accessibilityInitializeBundle]_block_invoke_2 : 84 -> 88
~ ___47+[AXPreBoardGlue accessibilityInitializeBundle]_block_invoke_3 : 172 -> 180
~ _AXSBFloatingDockControllerFromActiveDisplayWindowScene : 92 -> 100
~ _AXWindowScene : 240 -> 256
~ _AXSpringBoardGlueSBIconControllerClass : 72 -> 84
~ _AXSBOnenessOrXCUITestIsCurrentlyRequestingClientDuringContinuitySession : 112 -> 116
~ _AXSBHIconManagerFromSharedIconController : 144 -> 160
~ _AXSBIconControllerSharedInstance : 452 -> 476
~ _AXSBHomeScreenControllerForContinuityDisplay : 456 -> 472
~ _AXMainSBHomeScreenController : 428 -> 448
~ _AXSBHomeScreenOverlayController : 104 -> 116
~ _AXSBCurrentFolderController : 104 -> 116
~ _AXSBRootFolderController : 104 -> 116
~ _AXSBAssistantControllerSharedInstance : 116 -> 128
~ _AXSBMainSwitcherControllerCoordinatorSharedInstance : 116 -> 128
~ _AXSBApplicationControllerSharedInstance : 100 -> 112
~ _accessibilityLocalizedString : 248 -> 256
~ _AXSBScrollDescriptionForCurrentPage : 372 -> 400
~ _AXSBFolderControllerIsRootFolder : 68 -> 72
~ _AXSwitcherController : 352 -> 340
~ ___AXSwitcherController_block_invoke : 80 -> 84
~ _AXSwitcherViewController : 332 -> 328
~ ___AXSwitcherViewController_block_invoke : 84 -> 88
~ _AXLibraryViewController : 208 -> 228
~ _AXControlCenterPageStatus : 352 -> 372
~ +[PBAIdleSleepControllerAccessibility _accessibilityPerformValidations:] : 128 -> 140
~ +[PBADataRecoveryViewControllerAccessibility _accessibilityPerformValidations:] : 208 -> 216
~ -[PBADataRecoveryViewControllerAccessibility _pushPasscodeView] : 112 -> 116
~ -[PBADataRecoveryViewControllerAccessibility passcodeEntryViewControllerEntryCompleted:passcode:] : 192 -> 196
~ +[PBADeviceUnlockViewControllerAccessibility _accessibilityPerformValidations:] : 148 -> 156
~ -[PBADeviceUnlockViewControllerAccessibility deviceUnlocked:] : 112 -> 116
~ +[PBA_SBUICallToActionLabelAccessibility _accessibilityPerformValidations:] : 172 -> 180
~ -[PBA_SBUICallToActionLabelAccessibility accessibilityActivate] : 444 -> 448
~ ___63-[PBA_SBUICallToActionLabelAccessibility accessibilityActivate]_block_invoke : 176 -> 180
~ -[PBA_SBUICallToActionLabelAccessibility accessibilityLabel] : 84 -> 92

```
