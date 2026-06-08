## AccessibilitySettingsLoader

> `/System/Library/AccessibilityBundles/AccessibilitySettingsLoader.bundle/AccessibilitySettingsLoader`

```diff

-3191.35.0.0.0
-  __TEXT.__text: 0x11430
-  __TEXT.__auth_stubs: 0x750
-  __TEXT.__objc_methlist: 0x1144
-  __TEXT.__const: 0x88
-  __TEXT.__gcc_except_tab: 0x518
-  __TEXT.__cstring: 0x20d7
+3229.1.6.0.0
+  __TEXT.__text: 0x125a8
+  __TEXT.__objc_methlist: 0x11bc
+  __TEXT.__dlopen_cstrs: 0x7e4
+  __TEXT.__const: 0x78
+  __TEXT.__gcc_except_tab: 0x574
+  __TEXT.__cstring: 0x20cb
   __TEXT.__oslogstring: 0x6a4
-  __TEXT.__dlopen_cstrs: 0x6b0
-  __TEXT.__unwind_info: 0x768
-  __TEXT.__objc_classname: 0x71c
-  __TEXT.__objc_methname: 0x2f9b
-  __TEXT.__objc_methtype: 0xbbf
-  __TEXT.__objc_stubs: 0x1e20
-  __DATA_CONST.__got: 0x268
-  __DATA_CONST.__const: 0x590
-  __DATA_CONST.__objc_classlist: 0x180
+  __TEXT.__unwind_info: 0x750
+  __TEXT.__objc_stubs: 0x0
+  __TEXT.__auth_stubs: 0x0
+  __TEXT.__objc_classname: 0x0
+  __TEXT.__objc_methname: 0x0
+  __TEXT.__objc_methtype: 0x0
+  __DATA_CONST.__const: 0x5d8
+  __DATA_CONST.__objc_classlist: 0x178
   __DATA_CONST.__objc_protolist: 0x28
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0xd40
+  __DATA_CONST.__objc_selrefs: 0xd90
   __DATA_CONST.__objc_protorefs: 0x8
   __DATA_CONST.__objc_superrefs: 0xc0
   __DATA_CONST.__objc_arraydata: 0x38
-  __AUTH_CONST.__auth_got: 0x3b8
-  __AUTH_CONST.__const: 0x600
+  __DATA_CONST.__got: 0x290
+  __AUTH_CONST.__const: 0x620
   __AUTH_CONST.__cfstring: 0x14e0
-  __AUTH_CONST.__objc_const: 0x23e0
+  __AUTH_CONST.__objc_const: 0x23c0
   __AUTH_CONST.__objc_arrayobj: 0x18
-  __AUTH.__objc_data: 0xb90
-  __DATA.__objc_ivar: 0x24
+  __AUTH_CONST.__auth_got: 0x0
+  __AUTH.__objc_data: 0xb40
+  __DATA.__objc_ivar: 0x2c
   __DATA.__data: 0x1e0
-  __DATA.__bss: 0x220
+  __DATA.__bss: 0x300
   __DATA_DIRTY.__objc_data: 0x370
-  __DATA_DIRTY.__bss: 0x188
+  __DATA_DIRTY.__bss: 0x100
   - /System/Library/Frameworks/Accessibility.framework/Accessibility
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/CoreGraphics.framework/CoreGraphics

   - /System/Library/Frameworks/Security.framework/Security
   - /System/Library/Frameworks/UIKit.framework/UIKit
   - /System/Library/PrivateFrameworks/AXGuestPassServices.framework/AXGuestPassServices
+  - /System/Library/PrivateFrameworks/AccessibilitySharedSupport.framework/AccessibilitySharedSupport
   - /System/Library/PrivateFrameworks/AccessibilityUtilities.framework/AccessibilityUtilities
   - /System/Library/PrivateFrameworks/AppSupport.framework/AppSupport
   - /System/Library/PrivateFrameworks/SoftLinking.framework/SoftLinking

   - /usr/lib/libAccessibility.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 394C9C59-3DE1-35B3-AD31-C022472FA5DF
-  Functions: 483
-  Symbols:   1995
-  CStrings:  1117
+  UUID: 8DEC560D-F829-3220-9DE4-E855351A7D5D
+  Functions: 413
+  Symbols:   1863
+  CStrings:  496
 
Symbols:
+ +[AccessibilityFloatingUIKeyboardHelper initializeMonitoring]
+ -[AccessibilityFloatingUIKeyboardHelper .cxx_destruct]
+ -[AccessibilityFloatingUIKeyboardHelper _handleKeyboardWillHideNotification:]
+ -[AccessibilityFloatingUIKeyboardHelper _handleKeyboardWillShowNotification:]
+ -[AccessibilityFloatingUIKeyboardHelper _startListening]
+ -[AccessibilityFloatingUIKeyboardHelper _stopListening]
+ -[AccessibilityFloatingUIKeyboardHelper _updateListenerState]
+ -[AccessibilityFloatingUIKeyboardHelper client]
+ -[AccessibilityFloatingUIKeyboardHelper dealloc]
+ -[AccessibilityFloatingUIKeyboardHelper init]
+ -[AccessibilityFloatingUIKeyboardHelper listening]
+ -[AccessibilityFloatingUIKeyboardHelper setClient:]
+ -[AccessibilityFloatingUIKeyboardHelper setListening:]
+ GCC_except_table104
+ GCC_except_table107
+ GCC_except_table139
+ GCC_except_table142
+ GCC_except_table143
+ GCC_except_table151
+ GCC_except_table158
+ GCC_except_table163
+ GCC_except_table165
+ GCC_except_table168
+ GCC_except_table173
+ GCC_except_table174
+ GCC_except_table175
+ GCC_except_table176
+ GCC_except_table180
+ GCC_except_table182
+ GCC_except_table192
+ GCC_except_table201
+ GCC_except_table231
+ GCC_except_table237
+ GCC_except_table240
+ GCC_except_table251
+ GCC_except_table259
+ GCC_except_table28
+ GCC_except_table281
+ GCC_except_table282
+ GCC_except_table293
+ GCC_except_table294
+ GCC_except_table307
+ GCC_except_table322
+ GCC_except_table328
+ GCC_except_table33
+ GCC_except_table338
+ GCC_except_table346
+ GCC_except_table350
+ GCC_except_table351
+ GCC_except_table356
+ GCC_except_table367
+ GCC_except_table369
+ GCC_except_table377
+ GCC_except_table38
+ GCC_except_table407
+ GCC_except_table42
+ GCC_except_table46
+ GCC_except_table59
+ GCC_except_table60
+ GCC_except_table66
+ GCC_except_table68
+ GCC_except_table70
+ GCC_except_table84
+ GCC_except_table98
+ _AccessibilityUILibraryCore.frameworkLibrary
+ _AccessibilityUIUtilitiesLibrary.358
+ _AccessibilityUIUtilitiesLibrary.411
+ _AccessibilityUIUtilitiesLibrary.548
+ _AccessibilityUIUtilitiesLibraryCore.frameworkLibrary.362
+ _AccessibilityUIUtilitiesLibraryCore.frameworkLibrary.429
+ _AccessibilityUIUtilitiesLibraryCore.frameworkLibrary.555
+ _AccessibilityUtilitiesLibrary.154
+ _AccessibilityUtilitiesLibrary.305
+ _AccessibilityUtilitiesLibrary.452
+ _AccessibilityUtilitiesLibrary.47
+ _AccessibilityUtilitiesLibrary.480
+ _AccessibilityUtilitiesLibrary.9
+ _AccessibilityUtilitiesLibraryCore.frameworkLibrary.15
+ _AccessibilityUtilitiesLibraryCore.frameworkLibrary.157
+ _AccessibilityUtilitiesLibraryCore.frameworkLibrary.313
+ _AccessibilityUtilitiesLibraryCore.frameworkLibrary.463
+ _AccessibilityUtilitiesLibraryCore.frameworkLibrary.51
+ _AccessibilityUtilitiesLibraryCore.frameworkLibrary.539
+ _AccessibilityUtilitiesLibraryCore.frameworkLibrary.601
+ _OBJC_CLASS_$_AccessibilityFloatingUIKeyboardHelper
+ _OBJC_CLASS_$_UIApplication
+ _OBJC_CLASS_$_UIWindowScene
+ _OBJC_IVAR_$_AccessibilityFloatingUIKeyboardHelper._client
+ _OBJC_IVAR_$_AccessibilityFloatingUIKeyboardHelper._listening
+ _OBJC_METACLASS_$_AccessibilityFloatingUIKeyboardHelper
+ _SpeakTypingServicesLibraryCore.frameworkLibrary.563
+ __AXSHoverTextEnabled
+ __AXSLiveSpeechEnabled
+ __AXSLiveTranscriptionEnabled
+ __OBJC_$_CLASS_METHODS_AccessibilityFloatingUIKeyboardHelper
+ __OBJC_$_INSTANCE_METHODS_AccessibilityFloatingUIKeyboardHelper
+ __OBJC_$_INSTANCE_VARIABLES_AccessibilityFloatingUIKeyboardHelper
+ __OBJC_$_PROP_LIST_AccessibilityFloatingUIKeyboardHelper
+ __OBJC_CLASS_RO_$_AccessibilityFloatingUIKeyboardHelper
+ __OBJC_METACLASS_RO_$_AccessibilityFloatingUIKeyboardHelper
+ ___47-[AssistiveTouchHelper installKeyboardListener]_block_invoke.373
+ ___47-[AssistiveTouchHelper installKeyboardListener]_block_invoke.374
+ ___47-[AssistiveTouchHelper installKeyboardListener]_block_invoke.375
+ ___61+[AccessibilityFloatingUIKeyboardHelper initializeMonitoring]_block_invoke
+ ___70-[AccessibilitySettingsLoader _initializeDelayedAccessibilitySettings]_block_invoke.369
+ ___AccessibilityUILibraryCore_block_invoke
+ ___AccessibilityUIUtilitiesLibraryCore_block_invoke.363
+ ___AccessibilityUIUtilitiesLibraryCore_block_invoke.430
+ ___AccessibilityUIUtilitiesLibraryCore_block_invoke.556
+ ___AccessibilityUtilitiesLibraryCore_block_invoke.158
+ ___AccessibilityUtilitiesLibraryCore_block_invoke.16
+ ___AccessibilityUtilitiesLibraryCore_block_invoke.314
+ ___AccessibilityUtilitiesLibraryCore_block_invoke.464
+ ___AccessibilityUtilitiesLibraryCore_block_invoke.52
+ ___AccessibilityUtilitiesLibraryCore_block_invoke.540
+ ___AccessibilityUtilitiesLibraryCore_block_invoke.602
+ ___SpeakTypingServicesLibraryCore_block_invoke.564
+ ___UIAccessibilityCastAsClass
+ ____accessibilityFloatingUIFeatureToggled_block_invoke
+ ___block_literal_global.112
+ ___block_literal_global.184
+ ___block_literal_global.207
+ ___block_literal_global.220
+ ___block_literal_global.246
+ ___block_literal_global.277
+ ___block_literal_global.351
+ ___block_literal_global.354
+ ___block_literal_global.357
+ ___block_literal_global.362
+ ___block_literal_global.363
+ ___block_literal_global.363.168
+ ___block_literal_global.366
+ ___block_literal_global.367
+ ___block_literal_global.368
+ ___block_literal_global.368.162
+ ___block_literal_global.371
+ ___block_literal_global.373
+ ___block_literal_global.377.323
+ ___block_literal_global.385
+ ___block_literal_global.393
+ ___block_literal_global.395
+ ___block_literal_global.397
+ ___block_literal_global.400
+ ___block_literal_global.401
+ ___block_literal_global.404
+ ___block_literal_global.405
+ ___block_literal_global.406
+ ___block_literal_global.409
+ ___block_literal_global.411
+ ___block_literal_global.414
+ ___block_literal_global.416
+ ___block_literal_global.421
+ ___block_literal_global.451
+ ___block_literal_global.456
+ ___block_literal_global.459
+ ___block_literal_global.573
+ ___block_literal_global.580
+ ___block_literal_global.586
+ ___block_literal_global.589
+ ___block_literal_global.911
+ ___block_literal_global.920
+ ___getAXBackBoardServerClass_block_invoke.172
+ ___getAXBackBoardServerClass_block_invoke.98
+ ___getAXBinaryMonitorClass_block_invoke.485
+ ___getAXDeviceHasHomeButtonSymbolLoc_block_invoke.91
+ ___getAXPerformSafeBlockSymbolLoc_block_invoke.545
+ ___getAXPerformValidationChecksSymbolLoc_block_invoke.491
+ ___getAXPerformValidationChecksSymbolLoc_block_invoke.62
+ ___getAXProcessIsAXUIServerSymbolLoc_block_invoke.451
+ ___getAXProcessIsAssistiveTouchSymbolLoc_block_invoke.455
+ ___getAXProcessIsSetupSymbolLoc_block_invoke.304
+ ___getAXProcessIsSpringBoardSymbolLoc_block_invoke.153
+ ___getAXProcessIsSpringBoardSymbolLoc_block_invoke.341
+ ___getAXProcessIsSpringBoardSymbolLoc_block_invoke.95
+ ___getAXResourceLoaderClass_block_invoke.482
+ ___getAXSafeClassFromStringSymbolLoc_block_invoke.8
+ ___getAXSettingsClass_block_invoke.84
+ ___getAXSpringBoardUserChangedAudioRouteNotificationSymbolLoc_block_invoke.589
+ ___getAXUIClientClass_block_invoke
+ ___getAXUIKeyboardIsOnScreenSymbolLoc_block_invoke.357
+ ___getAXUIKeyboardIsOnScreenSymbolLoc_block_invoke.410
+ ___getAXUIKeyboardScreenFrameExcludingInputAccessoryIfFirstResponderInsideSymbolLoc_block_invoke.421
+ ___getAXUIKeyboardWindowSymbolLoc_block_invoke.417
+ ___getAXUIKeyboardWindowSymbolLoc_block_invoke.550
+ ___getAXValidationManagerClass_block_invoke.534
+ ___getAXValidationManagerClass_block_invoke.67
+ ___getSpeakTypingServicesClass_block_invoke.562
+ __accessibilityFloatingUIFeatureToggled
+ __zoomServicesUIGetScreen
+ __zoomServicesUIGetScreenForView
+ _audit_stringAccessibilityUI
+ _audit_stringAccessibilityUIUtilities.366
+ _audit_stringAccessibilityUIUtilities.432
+ _audit_stringAccessibilityUIUtilities.558
+ _audit_stringAccessibilityUtilities.161
+ _audit_stringAccessibilityUtilities.18
+ _audit_stringAccessibilityUtilities.316
+ _audit_stringAccessibilityUtilities.467
+ _audit_stringAccessibilityUtilities.542
+ _audit_stringAccessibilityUtilities.55
+ _audit_stringAccessibilityUtilities.605
+ _audit_stringSpeakTypingServices.568
+ _getAXBackBoardServerClass.71
+ _getAXBackBoardServerClass.softClass.171
+ _getAXBackBoardServerClass.softClass.97
+ _getAXBinaryMonitorClass.softClass.484
+ _getAXDeviceHasHomeButtonSymbolLoc.ptr.90
+ _getAXPerformSafeBlockSymbolLoc.ptr.544
+ _getAXPerformValidationChecksSymbolLoc.ptr.490
+ _getAXPerformValidationChecksSymbolLoc.ptr.61
+ _getAXProcessIsAXUIServerSymbolLoc.ptr.450
+ _getAXProcessIsAssistiveTouchSymbolLoc.ptr.454
+ _getAXProcessIsSetupSymbolLoc.ptr.303
+ _getAXProcessIsSpringBoardSymbolLoc.ptr.152
+ _getAXProcessIsSpringBoardSymbolLoc.ptr.340
+ _getAXProcessIsSpringBoardSymbolLoc.ptr.94
+ _getAXResourceLoaderClass.softClass.481
+ _getAXSafeClassFromStringSymbolLoc.ptr.7
+ _getAXSettingsClass.74
+ _getAXSettingsClass.softClass.83
+ _getAXSpringBoardUserChangedAudioRouteNotificationSymbolLoc.ptr.588
+ _getAXUIClientClass.softClass
+ _getAXUIKeyboardIsOnScreenSymbolLoc.ptr.356
+ _getAXUIKeyboardIsOnScreenSymbolLoc.ptr.409
+ _getAXUIKeyboardScreenFrameExcludingInputAccessoryIfFirstResponderInsideSymbolLoc.ptr.420
+ _getAXUIKeyboardWindowSymbolLoc.ptr.416
+ _getAXUIKeyboardWindowSymbolLoc.ptr.549
+ _getAXValidationManagerClass.483
+ _getAXValidationManagerClass.softClass.533
+ _getAXValidationManagerClass.softClass.66
+ _getSpeakTypingServicesClass.560
+ _getSpeakTypingServicesClass.softClass.561
+ _initializeMonitoring.Helper.462
+ _initializeMonitoring.onceToken.378
+ _initializeMonitoring.onceToken.458
+ _initializeMonitoring.onceToken.571
+ _kAXSHoverTextEnabledNotification
+ _kAXSLiveSpeechEnabledNotification
+ _kAXSLiveTranscriptionEnabledDidChangeNotification
+ _objc_claimAutoreleasedReturnValue
+ _objc_msgSend$_startListening
+ _objc_msgSend$_stopListening
+ _objc_msgSend$_updateListenerState
+ _objc_msgSend$client
+ _objc_msgSend$connectedScenes
+ _objc_msgSend$dictionaryWithDictionary:
+ _objc_msgSend$initWithIdentifier:serviceBundleName:
+ _objc_msgSend$listening
+ _objc_msgSend$sendAsynchronousMessage:withIdentifier:targetAccessQueue:completion:
+ _objc_msgSend$setListening:
+ _objc_msgSend$sharedApplication
+ _objc_msgSend$stringWithFormat:
+ _objc_msgSend$windowScene
+ _objc_retainAutoreleaseReturnValue
+ _objc_retain_x1
+ _objc_retain_x3
+ _objc_retain_x8
+ _objc_retain_x9
+ _sharedInstance.SharedInstance.574
+ _sharedInstance.onceToken.572
+ _soft_AXPerformSafeBlock.543
+ _soft_AXPerformValidationChecks.489
+ _soft_AXProcessIsSpringBoard.331
+ _soft_AXProcessIsSpringBoard.88
- +[AXInvertColorsController loadInvertColorsBundle].cold.1
- +[AccessibilitySettingsLoader _handleKeyboardWillChangeFrameNotification:].cold.1
- +[AccessibilitySettingsLoader _handleKeyboardWillHideNotification:].cold.1
- +[AccessibilitySettingsLoader _isAXUIServer].cold.1
- +[AccessibilitySettingsLoader initialize].cold.1
- +[AssistiveTouchHelper initializeMonitoring].cold.1
- +[GuidedAccessManager initializeMonitoring].cold.1
- +[HearingManager sharedInstance].cold.1
- +[SpeakTypingManager initializeMonitoring].cold.1
- +[SpeakTypingManager sharedInstance].cold.1
- +[ZoomServicesUI enableZoomServices].cold.1
- +[ZoomUI_UIKeyShortcutHUDServiceOverride(SafeCategory) safeCategoryBaseClass]
- +[ZoomUI_UIKeyShortcutHUDServiceOverride(SafeCategory) safeCategoryTargetClassName]
- -[AccessibilitySettingsLoader _accessibilityUserChangedRouteNotification:].cold.1
- -[AccessibilitySettingsLoader _initializeDelayedAccessibilitySettings].cold.1
- -[AccessibilitySettingsLoader _initializeDelayedAccessibilitySettings].cold.2
- -[AccessibilitySettingsLoader _initializeDelayedAccessibilitySettings].cold.3
- -[AccessibilitySettingsLoader _initializeDelayedAccessibilitySettings].cold.4
- -[AccessibilitySettingsLoader _initializeImmediateAccessibilitySettings].cold.1
- -[AssistiveTouchHelper _astDispatchQueue].cold.1
- -[AssistiveTouchHelper _sendKeyboardStatusUpdate].cold.1
- -[AssistiveTouchHelper _sendKeyboardStatusUpdate].cold.2
- -[AssistiveTouchHelper enable].cold.1
- -[AssistiveTouchHelper installKeyboardListener].cold.1
- -[AssistiveTouchHelper loadBuddyBundles].cold.1
- -[FBSceneWorkspaceAccessibility_SettingsLoader initWithIdentifier:].cold.1
- -[FBSceneWorkspaceAccessibility_SettingsLoader initWithIdentifier:].cold.2
- -[GuidedAccessManager _isValidClientApp].cold.1
- -[GuidedAccessManager _loadClientBundle].cold.1
- -[GuidedAccessManager _loadRequiredBundles].cold.1
- -[GuidedAccessManager _loadSpringboardServerBundle].cold.1
- -[MPAVOutputDeviceRoutingDataSourceAccessibility setPickedRoute:withPassword:completion:].cold.1
- -[SpeakCorrections _speakCorrection:].cold.1
- -[SpeakTypingManager _installSpeakTypingSafeCategoriesIfNeeded].cold.1
- -[SpeakTypingManager _installSpeakTypingSafeCategoriesIfNeeded].cold.2
- -[ZoomServicesUI _handleKeyboardDidHideNotification:].cold.1
- -[ZoomServicesUI _handleKeyboardWillHideNotification:].cold.1
- -[ZoomServicesUI _handleZoomFocusDidChangeNotification:].cold.1
- -[ZoomServicesUI _installZoomUISafeCategoriesIfNeeded].cold.1
- -[ZoomUI_UIKeyShortcutHUDServiceOverride _requestHUDPresentationIfAllowedWithUnpreparedConfiguration:]
- GCC_except_table0
- GCC_except_table11
- GCC_except_table110
- GCC_except_table113
- GCC_except_table12
- GCC_except_table13
- GCC_except_table14
- GCC_except_table16
- GCC_except_table17
- GCC_except_table18
- GCC_except_table19
- GCC_except_table20
- GCC_except_table21
- GCC_except_table22
- GCC_except_table23
- GCC_except_table25
- GCC_except_table26
- GCC_except_table27
- GCC_except_table29
- GCC_except_table30
- GCC_except_table32
- GCC_except_table34
- GCC_except_table4
- GCC_except_table50
- GCC_except_table6
- GCC_except_table7
- GCC_except_table79
- GCC_except_table96
- _AccessibilityLibrary.cold.1
- _AccessibilityUIUtilitiesLibrary.cold.1
- _AccessibilityUtilitiesLibrary.cold.1
- _NSRectFromString
- _OBJC_CLASS_$_UIScreen
- _OBJC_CLASS_$_ZoomUI_UIKeyShortcutHUDServiceOverride
- _OBJC_CLASS_$___ZoomUI_UIKeyShortcutHUDServiceOverride_super
- _OBJC_METACLASS_$_ZoomUI_UIKeyShortcutHUDServiceOverride
- _OBJC_METACLASS_$___ZoomUI_UIKeyShortcutHUDServiceOverride_super
- _OUTLINED_FUNCTION_0
- _OUTLINED_FUNCTION_1
- _OUTLINED_FUNCTION_2
- _OUTLINED_FUNCTION_3
- _OUTLINED_FUNCTION_4
- __OBJC_$_CLASS_METHODS_ZoomUI_UIKeyShortcutHUDServiceOverride(SafeCategory)
- __OBJC_$_INSTANCE_METHODS_ZoomUI_UIKeyShortcutHUDServiceOverride
- __OBJC_CLASS_RO_$_ZoomUI_UIKeyShortcutHUDServiceOverride
- __OBJC_CLASS_RO_$___ZoomUI_UIKeyShortcutHUDServiceOverride_super
- __OBJC_METACLASS_RO_$_ZoomUI_UIKeyShortcutHUDServiceOverride
- __OBJC_METACLASS_RO_$___ZoomUI_UIKeyShortcutHUDServiceOverride_super
- ___37-[SpeakCorrections _speakCorrection:]_block_invoke.cold.1
- ___40-[AssistiveTouchHelper loadBuddyBundles]_block_invoke.cold.1
- ___40-[GuidedAccessManager _loadClientBundle]_block_invoke.cold.1
- ___40-[GuidedAccessManager _loadClientBundle]_block_invoke.cold.2
- ___40-[GuidedAccessManager _loadClientBundle]_block_invoke.cold.3
- ___42-[SpeakThisServicesUI _kbFrameWillChange:]_block_invoke.cold.1
- ___47-[AssistiveTouchHelper installKeyboardListener]_block_invoke.352
- ___47-[AssistiveTouchHelper installKeyboardListener]_block_invoke.353
- ___47-[AssistiveTouchHelper installKeyboardListener]_block_invoke.354
- ___50+[AXInvertColorsController loadInvertColorsBundle]_block_invoke.cold.1
- ___51-[GuidedAccessManager _loadSpringboardServerBundle]_block_invoke.cold.1
- ___51-[GuidedAccessManager _loadSpringboardServerBundle]_block_invoke.cold.2
- ___51-[GuidedAccessManager _loadSpringboardServerBundle]_block_invoke.cold.3
- ___54-[ZoomServicesUI _handleKeyboardWillShowNotification:]_block_invoke.cold.1
- ___54-[ZoomServicesUI _installZoomUISafeCategoriesIfNeeded]_block_invoke_3.cold.1
- ___58-[GuidedAccessManager loadRequiredBundlesForUnmanagedASAM]_block_invoke_2.cold.1
- ___69-[AccessibilitySettingsLoader _loadSystemAppResourceAndContinueWith:]_block_invoke.cold.1
- ___70-[AccessibilitySettingsLoader _initializeDelayedAccessibilitySettings]_block_invoke.348
- ___70-[AccessibilitySettingsLoader _initializeDelayedAccessibilitySettings]_block_invoke.348.cold.1
- ___70-[AccessibilitySettingsLoader _initializeDelayedAccessibilitySettings]_block_invoke.348.cold.2
- ___70-[AccessibilitySettingsLoader _initializeDelayedAccessibilitySettings]_block_invoke.348.cold.3
- ___72-[SpeakTypingManager speakTypingLoadAccessibilityForExistingPredictions]_block_invoke.cold.1
- ___72-[SpeakTypingManager speakTypingLoadAccessibilityForExistingPredictions]_block_invoke.cold.2
- ___block_literal_global.330
- ___block_literal_global.333
- ___block_literal_global.336
- ___block_literal_global.341
- ___block_literal_global.342
- ___block_literal_global.345
- ___block_literal_global.346
- ___block_literal_global.347
- ___block_literal_global.349
- ___block_literal_global.350
- ___block_literal_global.352
- ___block_literal_global.356
- ___block_literal_global.364
- ___block_literal_global.374
- ___block_literal_global.375
- ___block_literal_global.379
- ___block_literal_global.380
- ___block_literal_global.383
- ___block_literal_global.386
- ___block_literal_global.388
- ___block_literal_global.390
- ___block_literal_global.430
- ___block_literal_global.435
- ___block_literal_global.572
- ___block_literal_global.578
- ___block_literal_global.581
- ___block_literal_global.909
- ___block_literal_global.915
- ___getAXBackBoardServerClass_block_invoke.cold.1
- ___getAXBinaryMonitorClass_block_invoke.cold.1
- ___getAXReplayerClass_block_invoke.cold.1
- ___getAXResourceLoaderClass_block_invoke.cold.1
- ___getAXSettingsClass_block_invoke.cold.1
- ___getAXSpringBoardUserChangedAudioRouteNotificationSymbolLoc_block_invoke.cold.1
- ___getAXValidationManagerClass_block_invoke.cold.1
- ___getSpeakThisServicesClass_block_invoke.cold.1
- ___getSpeakThisServicesClass_block_invoke.cold.2
- ___getSpeakTypingServicesClass_block_invoke.cold.1
- ___getSpeakTypingServicesClass_block_invoke.cold.2
- ___getTTSSpeechSynthesizerClass_block_invoke.cold.1
- ___getTTSSpeechSynthesizerClass_block_invoke.cold.2
- ___getZoomServicesClass_block_invoke.cold.1
- ___getZoomServicesClass_block_invoke.cold.2
- ___getkMADisplayFilterSettingsChangedNotificationSymbolLoc_block_invoke.cold.1
- __axSettingsHandlePreferenceChanged.cold.1
- __axSettingsHandlePreferenceChanged.cold.2
- _objc_autorelease
- _objc_msgSend$mainScreen
- _objc_msgSend$shouldSuppressKeyCommandHUD
- _objc_msgSend$validateClass:hasClassMethod:withFullSignature:
- _soft_AXDeviceHasHomeButton.cold.1
- _soft_AXDeviceIsPad.cold.1
- _soft_AXPerformSafeBlock.cold.1
- _soft_AXPerformValidationChecks.cold.1
- _soft_AXProcessIsAssistiveTouch.cold.1
- _soft_AXProcessIsInCallService.cold.1
- _soft_AXProcessIsSpringBoard.cold.1
- _soft_AXProcessIsSystemApplication.cold.1
- _soft_AXSafeClassFromString.cold.1
- _soft_AXUIConvertRectFromScreenToContextSpace.cold.1
- _soft_AXUIKeyboardIsOnScreen.cold.1
- _soft_AXUIKeyboardScreenFrameExcludingInputAccessoryIfFirstResponderInside.cold.1
- _soft_AXUIKeyboardWindow.cold.1
- _soft___UIAccessibilityCastAsClass.cold.1
- _soft___ax_verbose_encode_with_type_encoding_group_class.cold.1
CStrings:
+ ""
+ "AXFloatingUIKeyboardUIServer"
+ "AXUIClient"
+ "Class getAXUIClientClass(void)_block_invoke"
+ "FloatingUIKBClient-%d"
+ "bundleID"
+ "softlink:r:path:/System/Library/PrivateFrameworks/AccessibilityUI.framework/AccessibilityUI"
+ "void *AccessibilityUILibrary(void)"
- "#16@0:8"
- ".cxx_destruct"
- "@\"<UITextInputDelegate>\"16@0:8"
- "@\"<UITextInputTokenizer>\"16@0:8"
- "@\"AVSpeechSynthesizer\""
- "@\"NSArray\""
- "@\"NSArray\"24@0:8@\"UITextRange\"16"
- "@\"NSAttributedString\"24@0:8@\"UITextRange\"16"
- "@\"NSDictionary\""
- "@\"NSDictionary\"16@0:8"
- "@\"NSDictionary\"32@0:8@\"UITextPosition\"16q24"
- "@\"NSObject<OS_dispatch_queue>\""
- "@\"NSString\"16@0:8"
- "@\"NSString\"24@0:8@\"UITextRange\"16"
- "@\"UIConversationContext\"16@0:8"
- "@\"UIMenu\"32@0:8@\"UITextRange\"16@\"NSArray\"24"
- "@\"UITextInputPasswordRules\"16@0:8"
- "@\"UITextPlaceholder\"32@0:8{CGSize=dd}16"
- "@\"UITextPosition\"16@0:8"
- "@\"UITextPosition\"32@0:8@\"UITextPosition\"16q24"
- "@\"UITextPosition\"32@0:8@\"UITextRange\"16q24"
- "@\"UITextPosition\"32@0:8{CGPoint=dd}16"
- "@\"UITextPosition\"40@0:8@\"UITextPosition\"16q24q32"
- "@\"UITextPosition\"40@0:8{CGPoint=dd}16@\"UITextRange\"32"
- "@\"UITextRange\"16@0:8"
- "@\"UITextRange\"32@0:8@\"UITextPosition\"16@\"UITextPosition\"24"
- "@\"UITextRange\"32@0:8@\"UITextPosition\"16q24"
- "@\"UITextRange\"32@0:8{CGPoint=dd}16"
- "@\"UIView\"16@0:8"
- "@16@0:8"
- "@24@0:8:16"
- "@24@0:8@16"
- "@32@0:8:16@24"
- "@32@0:8@16@24"
- "@32@0:8@16q24"
- "@32@0:8{CGPoint=dd}16"
- "@32@0:8{CGSize=dd}16"
- "@40@0:8:16@24@32"
- "@40@0:8@16q24q32"
- "@40@0:8{CGPoint=dd}16@32"
- "@48@0:8{CGRect={CGPoint=dd}{CGSize=dd}}16"
- "AVSpeechSynthesizerDelegate"
- "AXInvertColorsController"
- "AccessibilitySettingsLoader"
- "AssistiveTouchHelper"
- "B16@0:8"
- "B24@0:8#16"
- "B24@0:8:16"
- "B24@0:8@\"Protocol\"16"
- "B24@0:8@16"
- "B32@0:8@\"UITextRange\"16@\"NSString\"24"
- "B32@0:8@16@24"
- "CGRectValue"
- "GuidedAccessManager"
- "HearingManager"
- "NSObject"
- "Q16@0:8"
- "SafeCategory"
- "SpeakCorrections"
- "SpeakThisServicesUI"
- "SpeakTypingManager"
- "T#,R"
- "T@\"<UITextInputDelegate>\",W,N"
- "T@\"<UITextInputTokenizer>\",R,N"
- "T@\"NSDictionary\",C,N"
- "T@\"NSString\",?,C,N"
- "T@\"NSString\",?,R,C"
- "T@\"NSString\",R,C"
- "T@\"UIConversationContext\",?,&,N"
- "T@\"UITextInputPasswordRules\",?,C,N"
- "T@\"UITextPosition\",R,N"
- "T@\"UITextRange\",C"
- "T@\"UITextRange\",R,N"
- "T@\"UIView\",?,R,N"
- "T@,&,N,V_notificationToken"
- "T@,?,R,N"
- "TB,?,N"
- "TB,?,N,GisSecureTextEntry"
- "TB,?,R,N,GisEditable"
- "TB,N,GisRegisteredForAppNotifications,V_registeredForAppNotifications"
- "TB,R,N"
- "TQ,?"
- "TQ,R"
- "Tq,?"
- "Tq,?,N"
- "T{CGRect={CGPoint=dd}{CGSize=dd}},?,R,N"
- "UIKeyInput"
- "UIKeyShortcutHUDService"
- "UITextInput"
- "Vv16@0:8"
- "ZoomServicesUI"
- "ZoomUI_UIFocusScrollAnimatorOverride"
- "ZoomUI_UIKeyShortcutHUDServiceOverride"
- "^{_NSZone=}16@0:8"
- "__FBSceneWorkspaceAccessibility_SettingsLoader_super"
- "__MPAVOutputDeviceRoutingDataSourceAccessibility_super"
- "__TUIPredictionView_TFExtras_super"
- "__UIKeyboardImpl_TFExtras_super"
- "__ZoomServices"
- "__ZoomUI_PHSOSViewController_super"
- "__ZoomUI_SBBacklightController_super"
- "__ZoomUI_SBDashBoardLockScreenEnvironmentOverride_super"
- "__ZoomUI_SBFluidSwitcherGestureManager_super"
- "__ZoomUI_SBFluidSwitcherScreenEdgePanGestureRecognizer_super"
- "__ZoomUI_SBFluidSwitcherViewController_super"
- "__ZoomUI_SBHomeGesturePanGestureRecognizer_super"
- "__ZoomUI_SBReachabilityGestureRecognizer_super"
- "__ZoomUI_SBReachabilitySettingsOverride_super"
- "__ZoomUI_SpringBoardOverride_super"
- "__ZoomUI_UIAlertControllerOverride_super"
- "__ZoomUI_UIDragInteraction_super"
- "__ZoomUI_UIFocusScrollAnimatorOverride_super"
- "__ZoomUI_UIKeyShortcutHUDServiceOverride_super"
- "__ZoomUI_UITouchReachabilityOverride_super"
- "_accessibilityBoolValueForKey:"
- "_accessibilityBundlePrincipalClass"
- "_accessibilityCachedWorkspaces"
- "_accessibilityIntegerValueForKey:"
- "_accessibilityPerformValidations:"
- "_accessibilitySetBoolValue:forKey:"
- "_accessibilitySetIntegerValue:forKey:"
- "_accessibilityStartServer"
- "_accessibilityUIFindSubviewDescendant:"
- "_accessibilityUserChangedRouteNotification:"
- "_astDispatchQueue"
- "_availableLanguageCodes"
- "_contextId"
- "_convertPortaitPointToSBOrientation:"
- "_convertRectToSceneReferenceSpace:"
- "_convertSBPointToPortaitOrientation:"
- "_correctionCanceled"
- "_correctionDisplayed:"
- "_deviceIsPortrait"
- "_handleAXLongPress:"
- "_handleAlertWillAppearNotification:"
- "_handleAppDidBecomeActiveNotification:"
- "_handleAppDidEnterBackgroundNotification:"
- "_handleAppSwitcherWillBeginRevealNotification:"
- "_handleFirstResponderDidChangeNotification:"
- "_handleKeyboardDidHideNotification:"
- "_handleKeyboardWillChangeFrameNotification:"
- "_handleKeyboardWillHideNotification:"
- "_handleKeyboardWillShowNotification:"
- "_handleLockButtonWasPressedNotification:"
- "_handleRegisterZoomConflictNotification:"
- "_handleSpeakThisEnabledStatusDidChangeNotification:"
- "_handleSpecificHardwareKeyboard:"
- "_handleZoomEnabledStatusDidChangeNotification:"
- "_handleZoomFocusDidChangeNotification:"
- "_initializeDelayedAccessibilitySettings"
- "_initializeImmediateAccessibilitySettings"
- "_installSpeakTypingSafeCategoriesIfNeeded"
- "_installZoomUISafeCategoriesIfNeeded"
- "_isAXUIServer"
- "_isValidClientApp"
- "_kbFrameWillChange:"
- "_keyboardFrameInScreenCoordinates"
- "_keyboardToLanguage"
- "_loadClientBundle"
- "_loadRequiredBundles"
- "_loadSpringboardServerBundle"
- "_loadSystemAppResourceAndContinueWith:"
- "_notificationToken"
- "_notifyToInitializeServerConnection"
- "_registerForAppNotifications"
- "_registerForKBFrameNotifications"
- "_registerForKeyboardNotifications"
- "_registerForLetterFeedbackAXSettingsUpdate"
- "_registerForPhoneticFeedbackAXSettingsUpdate"
- "_registerForQuickTypePredictionFeedbackAXSettingsUpdate"
- "_registerForWordFeedbackAXSettingsUpdate"
- "_registerSpeakThisNotificationListeners"
- "_registerZoomNotificationListeners"
- "_registeredForAppNotifications"
- "_requestHUDPresentationIfAllowedWithUnpreparedConfiguration:"
- "_resetD22ReduceMotion"
- "_selectedTextRangeForInputDelegate:"
- "_sendKeyboardStatusUpdate"
- "_sendKeyboardStatusUpdate:"
- "_sendKeyboardStatusUpdateHidden"
- "_shouldUnmapPointsForFluidGestures"
- "_speakCorrection:"
- "_speakLabelAtCell:forCurrentInputMode:"
- "_speakingQueue"
- "_synthesizer"
- "_textInInputDelegate:"
- "_unMappedZoomPoint:"
- "_unregisterForAppNotifications"
- "_unregisterForKBFrameNotifications"
- "_update"
- "_updateAccessibilitySpeakCorrections"
- "_updateAssistiveTouchInformation"
- "_updateForCurrentZoomStatus"
- "_updateITunesSettings"
- "_updateStatus"
- "_viewOrientationDoesNotMatchSBOrientation:"
- "_webKitInitialized"
- "accessibilityIdentifier"
- "activeInstance"
- "activeInterfaceOrientation"
- "activeKeyboard"
- "activeZoomModeOnDisplay:"
- "addGestureRecognizer:"
- "addHandler:forFramework:"
- "addObserver:selector:name:object:"
- "addObserverForName:object:queue:usingBlock:"
- "allowedWritingToolsResultOptions"
- "allowsNumberPadPopover"
- "anyObject"
- "appActivationAnimationStartDelay"
- "appDeactivationAnimationStartDelay"
- "applicationIsEntitledForUnmanagedASAM"
- "attributedTextInRange:"
- "autocapitalizationType"
- "autocorrectionType"
- "autorelease"
- "availableLanguageCodes"
- "axAttributedStringWithString:"
- "baseWritingDirectionForPosition:inDirection:"
- "beginFloatingCursorAtPoint:"
- "beginningOfDocument"
- "bundleIdentifier"
- "bundleWithIdentifier:"
- "bundleWithPath:"
- "cancelPreviousPerformRequestsWithTarget:"
- "caretRectForPosition:"
- "caretTransformForPosition:"
- "centerNamed:"
- "characterOffsetOfPosition:withinRange:"
- "characterRangeAtPoint:"
- "characterRangeByExtendingPosition:inDirection:"
- "class"
- "closestPositionToPoint:"
- "closestPositionToPoint:withinRange:"
- "comparePosition:toPosition:"
- "conformsToProtocol:"
- "containsObject:"
- "conversationContext"
- "convertRect:fromView:"
- "convertRect:toWindow:"
- "count"
- "countByEnumeratingWithState:objects:count:"
- "currentHandler"
- "currentInputMode"
- "d16@0:8"
- "dealloc"
- "debugDescription"
- "defaultCenter"
- "deleteBackward"
- "description"
- "detachNewThreadSelector:toTarget:withObject:"
- "dictationRecognitionFailed"
- "dictationRecordingDidEnd"
- "dictionaryWithObjects:forKeys:count:"
- "didDismissWritingTools"
- "didResetD22Preferences"
- "disable"
- "disableSpeakThisServices"
- "disableZoomServices"
- "dismissOrCancelHUDPresentationIfNeeded"
- "displayIdentity"
- "editMenuForTextRange:suggestedActions:"
- "editable"
- "enable"
- "enableSpeakThisServices"
- "enableZoomServices"
- "enablesReturnKeyAutomatically"
- "end"
- "endFloatingCursor"
- "endGuestPassSessionWithCompletionBlock:"
- "endOfDocument"
- "fileSystemRepresentation"
- "firstRectForRange:"
- "floatValue"
- "frameForDictationResultPlaceholder:"
- "gestureRecognizers"
- "handleFailureInFunction:file:lineNumber:description:"
- "hasText"
- "hash"
- "init"
- "initWithContentsOfFile:"
- "initWithName:object:userInfo:"
- "initWithTarget:action:"
- "initialize"
- "initializeMonitoring"
- "inlinePredictionType"
- "insertAdaptiveImageGlyph:replacementRange:"
- "insertAttributedText:"
- "insertDictationResult:"
- "insertDictationResultPlaceholder"
- "insertInputSuggestion:"
- "insertText:"
- "insertText:alternatives:style:"
- "insertTextPlaceholderWithSize:"
- "installKeyboardListener"
- "installSafeCategory:canInteractWithTargetClass:"
- "integerValue"
- "isEditable"
- "isEqual:"
- "isEqualToString:"
- "isKindOfClass:"
- "isLoaded"
- "isMemberOfClass:"
- "isProxy"
- "isRegisteredForAppNotifications"
- "isSecureTextEntry"
- "keyboardAppearance"
- "keyboardFrameWillUpdate:errorHandler:"
- "keyboardType"
- "lastObject"
- "loadAndReturnError:"
- "loadBuddyBundles"
- "loadGAXBundleForUnmanagedASAM"
- "loadInvertColorsBundle"
- "loadRequiredBundlesForUnmanagedASAM"
- "loadResource:principalClass:error:"
- "loadUIAccessibilityIfNecessary"
- "localizedDescription"
- "lock"
- "mainBundle"
- "mainQueue"
- "mainScreen"
- "markedTextRange"
- "markedTextStyle"
- "mathExpressionCompletionType"
- "notificationToken"
- "notifySpeakServicesForSpeakAutoCorrections:forCurrentInputMode:"
- "notifySpeakServicesToFeedbackQuickTypePrediction:forCurrentInputMode:"
- "notifySpeakServicesToInitializeServerConnection"
- "notifySpeakServicesToStopSpeakingAutocorrections"
- "notifyZoomAppActivationAnimationWillBegin"
- "notifyZoomAppDeactivationAnimationWillBegin"
- "notifyZoomAppDidBecomeActive:keyboardFrameIfVisible:"
- "notifyZoomAppDidEnterBackground:"
- "notifyZoomAppSwitcherRevealAnimationWillBegin"
- "notifyZoomDeviceWasUnlocked"
- "notifyZoomDeviceWillWake"
- "notifyZoomDragWillEnd"
- "notifyZoomDragWillStart"
- "notifyZoomFluidSwitcherGestureDidFinish"
- "notifyZoomFluidSwitcherGestureDidFinishWithDock"
- "notifyZoomFluidSwitcherGestureWillBegin"
- "notifyZoomFocusDidChangeWithType:rect:contextId:displayId:"
- "notifyZoomFocusDidChangeWithType:rect:contextId:keyboardFrame:displayId:"
- "notifyZoomKeyboardDidHideInAppWithBundleID:displayID:"
- "notifyZoomKeyboardWillBecomeVisibleWithFrame:inAppWithBundleID:displayID:"
- "notifyZoomKeyboardWillHideInAppWithBundleID:displayID:"
- "notifyZoomLockButtonWasPressed"
- "notifyZoomSOSMedicalIDShown"
- "numberWithInt:"
- "numberWithUnsignedInt:"
- "objectAtIndex:"
- "objectAtIndexedSubscript:"
- "objectForKey:"
- "objectForKeyedSubscript:"
- "offsetFromPosition:toPosition:"
- "passwordRules"
- "pathForResource:ofType:"
- "performSelector:"
- "performSelector:withObject:"
- "performSelector:withObject:afterDelay:"
- "performSelector:withObject:withObject:"
- "performValidations:withPreValidationHandler:postValidationHandler:safeCategoryInstallationHandler:"
- "positionFromPosition:inDirection:offset:"
- "positionFromPosition:offset:"
- "positionWithinRange:atCharacterOffset:"
- "positionWithinRange:farthestInDirection:"
- "postNotification:"
- "postNotificationName:object:"
- "primaryLanguage"
- "principalClass"
- "q16@0:8"
- "q32@0:8@\"UITextPosition\"16@\"UITextPosition\"24"
- "q32@0:8@\"UITextPosition\"16@\"UITextRange\"24"
- "q32@0:8@\"UITextPosition\"16q24"
- "q32@0:8@16@24"
- "q32@0:8@16q24"
- "reachabilityScaleFactor"
- "rectValue"
- "registerGestureConflictWithZoom:"
- "registerInterestInZoomAttributes"
- "registerUpdateBlock:forRetrieveSelector:withListener:"
- "registeredForAppNotifications"
- "release"
- "removeDictationResultPlaceholder:willInsertResult:"
- "removeObserver:"
- "removeObserver:name:object:"
- "removeTextPlaceholder:"
- "replaceRange:withAttributedText:"
- "replaceRange:withText:"
- "replayWithName:attempts:interval:async:queue:replayBlock:completion:"
- "replayer"
- "respondsToSelector:"
- "retain"
- "retainCount"
- "returnKeyType"
- "safeArrayForKey:"
- "safeCGFloatForKey:"
- "safeCGPointForKey:"
- "safeCategoryBaseClass"
- "safeCategoryTargetClassName"
- "safeIntegerForKey:"
- "safeStringForKey:"
- "safeUIViewForKey:"
- "safeValueForKey:"
- "screen"
- "selectedTextRange"
- "selectionAffinity"
- "selectionRectsForRange:"
- "self"
- "sendMessageName:userInfo:"
- "server"
- "setAccessibilityIdentifier:"
- "setAllowableMovement:"
- "setAllowedWritingToolsResultOptions:"
- "setAllowsNumberPadPopover:"
- "setAttribute:forKey:"
- "setAttributedMarkedText:selectedRange:"
- "setAutocapitalizationType:"
- "setAutocorrectionType:"
- "setBaseWritingDirection:forRange:"
- "setConversationContext:"
- "setDebugBuild:"
- "setDidResetD22Preferences:"
- "setEnablesReturnKeyAutomatically:"
- "setInCheckerBoardMode:"
- "setInPreboardMode:"
- "setInlinePredictionType:"
- "setInputDelegate:"
- "setKeyboardAppearance:"
- "setKeyboardType:"
- "setMarkedText:selectedRange:"
- "setMarkedTextStyle:"
- "setMathExpressionCompletionType:"
- "setNotificationToken:"
- "setObject:forKey:"
- "setObject:forKeyedSubscript:"
- "setOverrideProcessName:"
- "setPasswordRules:"
- "setReduceMotionEnabled:"
- "setRegisteredForAppNotifications:"
- "setReturnKeyType:"
- "setSecureTextEntry:"
- "setSelectedTextRange:"
- "setSelectionAffinity:"
- "setSessionIsLoginSession:"
- "setSmartDashesType:"
- "setSmartInsertDeleteType:"
- "setSmartQuotesType:"
- "setSpellCheckingType:"
- "setSupportsAdaptiveImageGlyph:"
- "setTargetContentOffset:forEnvironmentScrollableContainer:convergenceRate:completion:"
- "setTextContentType:"
- "setValidationTargetName:"
- "setWithArray:"
- "setWritingToolsBehavior:"
- "sharedHUDService"
- "sharedInputModeController"
- "sharedInstance"
- "shouldChangeTextInRange:replacementText:"
- "shouldSuppressKeyCommandHUD"
- "smartDashesType"
- "smartInsertDeleteType"
- "smartQuotesType"
- "speakCorrectionsEnabled"
- "speakThisMessageKeyKBFrame"
- "speakTypingLoadAccessibilityForExistingPredictions"
- "speakTypingLoadAccessibilityInformation"
- "speechSynthesizer:didCancelSpeechUtterance:"
- "speechSynthesizer:didContinueSpeechUtterance:"
- "speechSynthesizer:didFinishSpeechUtterance:"
- "speechSynthesizer:didPauseSpeechUtterance:"
- "speechSynthesizer:didStartSpeechUtterance:"
- "speechSynthesizer:willSpeakMarker:utterance:"
- "speechSynthesizer:willSpeakRangeOfSpeechString:utterance:"
- "spellCheckingType"
- "start"
- "startMonitoring"
- "state"
- "stringByAppendingPathComponent:"
- "stringByAppendingPathExtension:"
- "stringByReplacingOccurrencesOfString:withString:"
- "stringWithUTF8String:"
- "superclass"
- "supportsAdaptiveImageGlyph"
- "textContentType"
- "textInRange:"
- "textInputView"
- "textRangeFromPosition:toPosition:"
- "textStylingAtPosition:inDirection:"
- "tokenizer"
- "unlock"
- "unmarkText"
- "unobscuredContentRect"
- "unsignedIntValue"
- "update"
- "updateFloatingCursorAtPoint:"
- "updateForCurrentQuickTypeFeedbackStatus"
- "updateForCurrentTypingFeedbackStatus"
- "updateForCurrentWordFeedbackStatus"
- "updateITunesSettings"
- "updateStatus"
- "userInfo"
- "v16@0:8"
- "v20@0:8B16"
- "v20@0:8i16"
- "v24@0:8@\"<UIEditMenuInteractionAnimating>\"16"
- "v24@0:8@\"<UITextInputDelegate>\"16"
- "v24@0:8@\"NSArray\"16"
- "v24@0:8@\"NSAttributedString\"16"
- "v24@0:8@\"NSDictionary\"16"
- "v24@0:8@\"NSString\"16"
- "v24@0:8@\"UIConversationContext\"16"
- "v24@0:8@\"UIInputSuggestion\"16"
- "v24@0:8@\"UITextInputPasswordRules\"16"
- "v24@0:8@\"UITextPlaceholder\"16"
- "v24@0:8@\"UITextRange\"16"
- "v24@0:8@16"
- "v24@0:8@?16"
- "v24@0:8Q16"
- "v24@0:8q16"
- "v28@0:8@16B24"
- "v32@0:8@\"AVSpeechSynthesizer\"16@\"AVSpeechUtterance\"24"
- "v32@0:8@\"NSAdaptiveImageGlyph\"16@\"UITextRange\"24"
- "v32@0:8@\"UITextRange\"16@\"NSAttributedString\"24"
- "v32@0:8@\"UITextRange\"16@\"NSString\"24"
- "v32@0:8@16@24"
- "v32@0:8@16Q24"
- "v32@0:8q16@\"UITextRange\"24"
- "v32@0:8q16@24"
- "v32@0:8{CGPoint=dd}16"
- "v40@0:8@\"AVSpeechSynthesizer\"16@\"AVSpeechSynthesisMarker\"24@\"AVSpeechUtterance\"32"
- "v40@0:8@\"NSAttributedString\"16{_NSRange=QQ}24"
- "v40@0:8@\"NSString\"16@\"NSArray\"24q32"
- "v40@0:8@\"NSString\"16{_NSRange=QQ}24"
- "v40@0:8@16@24@32"
- "v40@0:8@16@24@?32"
- "v40@0:8@16@24q32"
- "v40@0:8@16{_NSRange=QQ}24"
- "v40@0:8{CGPoint=dd}16@32"
- "v48@0:8@\"AVSpeechSynthesizer\"16{_NSRange=QQ}24@\"AVSpeechUtterance\"40"
- "v48@0:8@16{_NSRange=QQ}24@40"
- "v48@0:8{CGRect={CGPoint=dd}{CGSize=dd}}16"
- "v56@0:8{CGPoint=dd}16@32d40@?48"
- "validateClass:"
- "validateClass:hasClassMethod:withFullSignature:"
- "validateClass:hasInstanceMethod:withFullSignature:"
- "validateClass:hasInstanceVariable:withType:"
- "validateClass:isKindOfClass:"
- "validateProtocol:hasRequiredInstanceMethod:"
- "valueForKey:"
- "valueWithCGRect:"
- "viewDidAppear:"
- "willDismissEditMenuWithAnimator:"
- "willPresentEditMenuWithAnimator:"
- "willPresentWritingTools"
- "writingToolsBehavior"
- "zone"
- "zoomFrameOnDisplay:"
- "zoomInStandby"
- "zoomScale"
- "{CGAffineTransform=dddddd}24@0:8@\"UITextPosition\"16"
- "{CGAffineTransform=dddddd}24@0:8@16"
- "{CGPoint=\"x\"d\"y\"d}"
- "{CGPoint=dd}24@0:8@16"
- "{CGPoint=dd}32@0:8{CGPoint=dd}16"
- "{CGRect={CGPoint=dd}{CGSize=dd}}16@0:8"
- "{CGRect={CGPoint=dd}{CGSize=dd}}24@0:8@\"UITextPosition\"16"
- "{CGRect={CGPoint=dd}{CGSize=dd}}24@0:8@\"UITextRange\"16"
- "{CGRect={CGPoint=dd}{CGSize=dd}}24@0:8@16"
- "{_NSRange=QQ}24@0:8@16"

```
