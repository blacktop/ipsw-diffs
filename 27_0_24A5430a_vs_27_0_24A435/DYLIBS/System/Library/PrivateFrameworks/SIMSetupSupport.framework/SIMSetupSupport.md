## SIMSetupSupport

> `/System/Library/PrivateFrameworks/SIMSetupSupport.framework/SIMSetupSupport`

```diff

 973.1.0.0.0
-  __TEXT.__text: 0xe337c
-  __TEXT.__objc_methlist: 0xc474
+  __TEXT.__text: 0xe6494
+  __TEXT.__objc_methlist: 0xc7ec
   __TEXT.__const: 0x1f0
-  __TEXT.__gcc_except_tab: 0x2120
-  __TEXT.__cstring: 0x175c9
-  __TEXT.__oslogstring: 0x8af5
+  __TEXT.__gcc_except_tab: 0x218c
+  __TEXT.__cstring: 0x17aa0
+  __TEXT.__oslogstring: 0x8c70
   __TEXT.__dlopen_cstrs: 0x2be
   __TEXT.__ustring: 0xa
-  __TEXT.__unwind_info: 0x2fa8
+  __TEXT.__unwind_info: 0x3080
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0
   __TEXT.__objc_classname: 0x0
   __TEXT.__objc_methname: 0x0
   __TEXT.__objc_methtype: 0x0
-  __DATA_CONST.__const: 0x2128
-  __DATA_CONST.__objc_classlist: 0x578
+  __DATA_CONST.__const: 0x2130
+  __DATA_CONST.__objc_classlist: 0x590
   __DATA_CONST.__objc_catlist: 0x70
-  __DATA_CONST.__objc_protolist: 0x108
+  __DATA_CONST.__objc_protolist: 0x118
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x5e38
+  __DATA_CONST.__objc_selrefs: 0x5f58
   __DATA_CONST.__objc_protorefs: 0x10
-  __DATA_CONST.__objc_superrefs: 0x518
+  __DATA_CONST.__objc_superrefs: 0x530
   __DATA_CONST.__objc_arraydata: 0x228
-  __DATA_CONST.__got: 0xbf0
-  __AUTH_CONST.__const: 0xba0
-  __AUTH_CONST.__cfstring: 0xab20
-  __AUTH_CONST.__objc_const: 0x4e0c8
-  __AUTH_CONST.__objc_intobj: 0x7e0
+  __DATA_CONST.__got: 0xc10
+  __AUTH_CONST.__const: 0xbc0
+  __AUTH_CONST.__cfstring: 0xae60
+  __AUTH_CONST.__objc_const: 0x4f8d8
+  __AUTH_CONST.__objc_intobj: 0x7f8
   __AUTH_CONST.__objc_dictobj: 0x28
   __AUTH_CONST.__objc_arrayobj: 0x108
   __AUTH_CONST.__auth_got: 0x0
-  __AUTH.__objc_data: 0x35c0
-  __DATA.__objc_ivar: 0x130c
-  __DATA.__data: 0xc70
+  __AUTH.__objc_data: 0x36b0
+  __DATA.__objc_ivar: 0x1358
+  __DATA.__data: 0xd30
   __DATA_DIRTY.__objc_data: 0xf0
   - /System/Library/Frameworks/AVFoundation.framework/AVFoundation
   - /System/Library/Frameworks/Accounts.framework/Accounts
   - /System/Library/Frameworks/AudioToolbox.framework/AudioToolbox
+  - /System/Library/Frameworks/CallKit.framework/CallKit
   - /System/Library/Frameworks/Contacts.framework/Contacts
   - /System/Library/Frameworks/ContactsUI.framework/ContactsUI
   - /System/Library/Frameworks/CoreBluetooth.framework/CoreBluetooth

   - /usr/lib/libMobileGestalt.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 4889
-  Symbols:   9981
-  CStrings:  3110
+  Functions: 4970
+  Symbols:   10145
+  CStrings:  3151
 
Symbols:
+ +[TSSIMSetupFlow _maybeCreateSIMConfigFlowAsPreFlow:options:]
+ +[TSSIMSetupFlow _simConfigSwitchPreFlowForDeviceIdentifierOptions:]
+ -[SSSIMConfigSwitchFailedViewController .cxx_destruct]
+ -[SSSIMConfigSwitchFailedViewController _okTapped]
+ -[SSSIMConfigSwitchFailedViewController backOption]
+ -[SSSIMConfigSwitchFailedViewController delegate]
+ -[SSSIMConfigSwitchFailedViewController initWithSwitchToEuicc:parentFlowType:]
+ -[SSSIMConfigSwitchFailedViewController setDelegate:]
+ -[SSSIMConfigSwitchFailedViewController setSwitchToEuicc:]
+ -[SSSIMConfigSwitchFailedViewController switchToEuicc]
+ -[SSSIMConfigSwitchFailedViewController viewDidLoad]
+ -[SSSIMConfigSwitchFailedViewController viewWillAppear:]
+ -[SSSIMConfigSwitchViewController .cxx_destruct]
+ -[SSSIMConfigSwitchViewController _buildBodyMessageForSwitchToEuicc:]
+ -[SSSIMConfigSwitchViewController _cancelTapped]
+ -[SSSIMConfigSwitchViewController _continueTapped]
+ -[SSSIMConfigSwitchViewController _titleForFlowType:]
+ -[SSSIMConfigSwitchViewController _updateContinueButton]
+ -[SSSIMConfigSwitchViewController animating]
+ -[SSSIMConfigSwitchViewController backOption]
+ -[SSSIMConfigSwitchViewController cachedButtons]
+ -[SSSIMConfigSwitchViewController callObserver:callChanged:]
+ -[SSSIMConfigSwitchViewController callObserver]
+ -[SSSIMConfigSwitchViewController customizeSpinner]
+ -[SSSIMConfigSwitchViewController delegate]
+ -[SSSIMConfigSwitchViewController forceShow]
+ -[SSSIMConfigSwitchViewController initWithSwitchToEuicc:forceShow:flowType:]
+ -[SSSIMConfigSwitchViewController prepare:]
+ -[SSSIMConfigSwitchViewController setAnimating:]
+ -[SSSIMConfigSwitchViewController setCachedButtons:]
+ -[SSSIMConfigSwitchViewController setCallObserver:]
+ -[SSSIMConfigSwitchViewController setDelegate:]
+ -[SSSIMConfigSwitchViewController setForceShow:]
+ -[SSSIMConfigSwitchViewController setSpinner:]
+ -[SSSIMConfigSwitchViewController setSpinnerContainer:]
+ -[SSSIMConfigSwitchViewController setSwitchSucceeded:]
+ -[SSSIMConfigSwitchViewController setSwitchToEuicc:]
+ -[SSSIMConfigSwitchViewController spinnerContainer]
+ -[SSSIMConfigSwitchViewController spinner]
+ -[SSSIMConfigSwitchViewController switchSucceeded]
+ -[SSSIMConfigSwitchViewController switchToEuicc]
+ -[SSSIMConfigSwitchViewController viewDidLoad]
+ -[SSSIMConfigSwitchViewController viewWillAppear:]
+ -[TSCoreTelephonyClientCache appForegrounded]
+ -[TSCoreTelephonyClientCache isEuiccActiveCache]
+ -[TSCoreTelephonyClientCache requestEUICCHardware:completion:]
+ -[TSCoreTelephonyClientCache setIsEuiccActiveCache:]
+ -[TSCoreTelephonyClientCache simHardwareConfigurationChanged:]
+ -[TSQRCodeScanFlow _resetDeferredState]
+ -[TSQRCodeScanFlow _shouldDeferSwitchForCardData:]
+ -[TSQRCodeScanFlow _simConfigSwitchSubFlowVC]
+ -[TSSIMConfigSwitchFlow .cxx_destruct]
+ -[TSSIMConfigSwitchFlow _iseSIMInstallFlow]
+ -[TSSIMConfigSwitchFlow _maybePresentFirstViewController:firstViewControllerCallback:]
+ -[TSSIMConfigSwitchFlow cancelButton]
+ -[TSSIMConfigSwitchFlow firstViewController:]
+ -[TSSIMConfigSwitchFlow firstViewController]
+ -[TSSIMConfigSwitchFlow initWithFlowOptions:]
+ -[TSSIMConfigSwitchFlow initWithSwitchToEuicc:]
+ -[TSSIMConfigSwitchFlow isBootstrapAssertionRequired]
+ -[TSSIMConfigSwitchFlow nextViewControllerFrom:]
+ -[TSSIMConfigSwitchFlow optionsForNextFlow]
+ -[TSSIMConfigSwitchFlow setCancelButton:]
+ -[TSSIMConfigSwitchFlow setCancelNavigationBarItems:]
+ -[TSSIMConfigSwitchFlow setOptionsForNextFlow:]
+ -[TSSIMConfigSwitchFlow setSwitchToEuicc:]
+ -[TSSIMConfigSwitchFlow switchToEuicc]
+ GCC_except_table38
+ GCC_except_table51
+ _OBJC_CLASS_$_CXCallObserver
+ _OBJC_CLASS_$_SSSIMConfigSwitchFailedViewController
+ _OBJC_CLASS_$_SSSIMConfigSwitchViewController
+ _OBJC_CLASS_$_TSSIMConfigSwitchFlow
+ _OBJC_IVAR_$_SSSIMConfigSwitchFailedViewController._delegate
+ _OBJC_IVAR_$_SSSIMConfigSwitchFailedViewController._okButton
+ _OBJC_IVAR_$_SSSIMConfigSwitchFailedViewController._okButtonTitle
+ _OBJC_IVAR_$_SSSIMConfigSwitchFailedViewController._switchToEuicc
+ _OBJC_IVAR_$_SSSIMConfigSwitchViewController._animating
+ _OBJC_IVAR_$_SSSIMConfigSwitchViewController._cachedButtons
+ _OBJC_IVAR_$_SSSIMConfigSwitchViewController._callObserver
+ _OBJC_IVAR_$_SSSIMConfigSwitchViewController._cancelButton
+ _OBJC_IVAR_$_SSSIMConfigSwitchViewController._continueButton
+ _OBJC_IVAR_$_SSSIMConfigSwitchViewController._delegate
+ _OBJC_IVAR_$_SSSIMConfigSwitchViewController._forceShow
+ _OBJC_IVAR_$_SSSIMConfigSwitchViewController._spinner
+ _OBJC_IVAR_$_SSSIMConfigSwitchViewController._spinnerContainer
+ _OBJC_IVAR_$_SSSIMConfigSwitchViewController._switchSucceeded
+ _OBJC_IVAR_$_SSSIMConfigSwitchViewController._switchToEuicc
+ _OBJC_IVAR_$_TSCoreTelephonyClientCache._isEuiccActiveCache
+ _OBJC_IVAR_$_TSSIMConfigSwitchFlow._cancelButton
+ _OBJC_IVAR_$_TSSIMConfigSwitchFlow._optionsForNextFlow
+ _OBJC_IVAR_$_TSSIMConfigSwitchFlow._switchToEuicc
+ _OBJC_METACLASS_$_SSSIMConfigSwitchFailedViewController
+ _OBJC_METACLASS_$_SSSIMConfigSwitchViewController
+ _OBJC_METACLASS_$_TSSIMConfigSwitchFlow
+ _TSUserInfoSIMConfigSwitchToEuiccKey
+ __OBJC_$_INSTANCE_METHODS_SSSIMConfigSwitchFailedViewController
+ __OBJC_$_INSTANCE_METHODS_SSSIMConfigSwitchViewController
+ __OBJC_$_INSTANCE_METHODS_TSSIMConfigSwitchFlow
+ __OBJC_$_INSTANCE_VARIABLES_SSSIMConfigSwitchFailedViewController
+ __OBJC_$_INSTANCE_VARIABLES_SSSIMConfigSwitchViewController
+ __OBJC_$_INSTANCE_VARIABLES_TSSIMConfigSwitchFlow
+ __OBJC_$_PROP_LIST_SSSIMConfigSwitchFailedViewController
+ __OBJC_$_PROP_LIST_SSSIMConfigSwitchViewController
+ __OBJC_$_PROP_LIST_TSSIMConfigSwitchFlow
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_CXCallObserverDelegate
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_OPT_CoreTelephonyClientSimHardwareConfigurationDelegate
+ __OBJC_$_PROTOCOL_METHOD_TYPES_CXCallObserverDelegate
+ __OBJC_$_PROTOCOL_METHOD_TYPES_CoreTelephonyClientSimHardwareConfigurationDelegate
+ __OBJC_$_PROTOCOL_REFS_CXCallObserverDelegate
+ __OBJC_$_PROTOCOL_REFS_CoreTelephonyClientSimHardwareConfigurationDelegate
+ __OBJC_CLASS_PROTOCOLS_$_SSSIMConfigSwitchFailedViewController
+ __OBJC_CLASS_PROTOCOLS_$_SSSIMConfigSwitchViewController
+ __OBJC_CLASS_PROTOCOLS_$_TSCoreTelephonyClientCache
+ __OBJC_CLASS_PROTOCOLS_$_TSSIMConfigSwitchFlow
+ __OBJC_CLASS_RO_$_SSSIMConfigSwitchFailedViewController
+ __OBJC_CLASS_RO_$_SSSIMConfigSwitchViewController
+ __OBJC_CLASS_RO_$_TSSIMConfigSwitchFlow
+ __OBJC_LABEL_PROTOCOL_$_CXCallObserverDelegate
+ __OBJC_LABEL_PROTOCOL_$_CoreTelephonyClientSimHardwareConfigurationDelegate
+ __OBJC_METACLASS_RO_$_SSSIMConfigSwitchFailedViewController
+ __OBJC_METACLASS_RO_$_SSSIMConfigSwitchViewController
+ __OBJC_METACLASS_RO_$_TSSIMConfigSwitchFlow
+ __OBJC_PROTOCOL_$_CXCallObserverDelegate
+ __OBJC_PROTOCOL_$_CoreTelephonyClientSimHardwareConfigurationDelegate
+ ___46-[TSQRCodeScanFlow viewControllerDidComplete:]_block_invoke
+ ___46-[TSQRCodeScanFlow viewControllerDidComplete:]_block_invoke_2
+ ___50-[SSSIMConfigSwitchViewController _continueTapped]_block_invoke
+ ___62-[TSCoreTelephonyClientCache requestEUICCHardware:completion:]_block_invoke
+ ___86-[TSSIMConfigSwitchFlow _maybePresentFirstViewController:firstViewControllerCallback:]_block_invoke
+ _objc_msgSend$_buildBodyMessageForSwitchToEuicc:
+ _objc_msgSend$_iseSIMInstallFlow
+ _objc_msgSend$_maybeCreateSIMConfigFlowAsPreFlow:options:
+ _objc_msgSend$_resetDeferredState
+ _objc_msgSend$_shouldDeferSwitchForCardData:
+ _objc_msgSend$_simConfigSwitchPreFlowForDeviceIdentifierOptions:
+ _objc_msgSend$_simConfigSwitchSubFlowVC
+ _objc_msgSend$_titleForFlowType:
+ _objc_msgSend$_updateContinueButton
+ _objc_msgSend$calls
+ _objc_msgSend$configType
+ _objc_msgSend$enteredConfirmationCode
+ _objc_msgSend$initWithFlowOptions:
+ _objc_msgSend$initWithSwitchToEuicc:
+ _objc_msgSend$initWithSwitchToEuicc:forceShow:flowType:
+ _objc_msgSend$initWithSwitchToEuicc:parentFlowType:
+ _objc_msgSend$isEuiccActiveCache
+ _objc_msgSend$isEuiccActiveWithError:
+ _objc_msgSend$optionsForNextFlow
+ _objc_msgSend$requestEUICCHardware:completion:
+ _objc_msgSend$setAccessibilityIdentifier:
+ _objc_msgSend$setDeferredAddress:
+ _objc_msgSend$setDeferredCardData:
+ _objc_msgSend$setDeferredConfirmationCode:
+ _objc_msgSend$setDeferredInstallTriggered:
+ _objc_msgSend$setDeferredMatchingId:
+ _objc_msgSend$setDelegate:queue:
+ _objc_msgSend$setIsEuiccActiveCache:
+ _objc_msgSend$setSwitchSucceeded:
+ _objc_msgSend$simLocation
+ _objc_msgSend$stringWithString:
+ _objc_msgSend$supportsDynamicSIMConfiguration
+ _objc_msgSend$switchSucceeded
+ _objc_msgSend$switchToEuicc
CStrings:
+ "-[TSCoreTelephonyClientCache isESIMUnavailable]"
+ "-[TSCoreTelephonyClientCache requestEUICCHardware:completion:]_block_invoke"
+ "-[TSCoreTelephonyClientCache simHardwareConfigurationChanged:]"
+ "-[TSQRCodeScanFlow viewControllerDidComplete:]"
+ "-[TSSIMConfigSwitchFlow _maybePresentFirstViewController:firstViewControllerCallback:]"
+ "-[TSSIMConfigSwitchFlow _maybePresentFirstViewController:firstViewControllerCallback:]_block_invoke"
+ "-[TSSIMConfigSwitchFlow firstViewController]"
+ "Localizable-V63"
+ "SIM config switch succeeded, triggering deferred install @%s"
+ "SIM hardware configuration changed: isEuiccActive=%@ @%s"
+ "SIMConfigCancelButton"
+ "SIMConfigContinueButton"
+ "SIMConfigOKButton"
+ "SIMConfigSwitch"
+ "SIMConfigSwitchToEuiccKey"
+ "SS_SIM_CONFIG_BACK_SIM_ROW_%@"
+ "SS_SIM_CONFIG_CANCEL"
+ "SS_SIM_CONFIG_CURRENT_PE"
+ "SS_SIM_CONFIG_CURRENT_PP"
+ "SS_SIM_CONFIG_DONE"
+ "SS_SIM_CONFIG_ESIM1_ROW_%@"
+ "SS_SIM_CONFIG_ESIM2_ROW_%@"
+ "SS_SIM_CONFIG_ESIM_ROW_%@"
+ "SS_SIM_CONFIG_FRONT_SIM_ROW_%@"
+ "SS_SIM_CONFIG_NO_ACTIVE_NUMBERS"
+ "SS_SIM_CONFIG_SUGGEST_PE"
+ "SS_SIM_CONFIG_SUGGEST_PP"
+ "SS_SIM_CONFIG_SWITCHING_FOR_BACK_SIM"
+ "SS_SIM_CONFIG_SWITCHING_FOR_ESIM"
+ "SS_SIM_CONFIG_SWITCH_FAILED_MESSAGE_CURRENT_CONFIG_PE"
+ "SS_SIM_CONFIG_SWITCH_FAILED_MESSAGE_CURRENT_CONFIG_PP"
+ "SS_SIM_CONFIG_SWITCH_FAILED_TITLE"
+ "SS_SIM_CONFIG_TITLE"
+ "SS_SIM_CONFIG_TITLE_SHARE_IDENTIFIERS"
+ "SS_SIM_CONFIG_USE_DUAL_PSIM_BUTTON"
+ "SS_SIM_CONFIG_USE_ESIM_BUTTON"
+ "[E]Device does not support dynamic SIM configuration @%s"
+ "[E]Failed to query isEuiccActive: %@ @%s"
+ "[E]SIM config switch did not occur (isEuiccActive=%@, error=%@), cancelling QR scan flow @%s"
+ "[E]no deferred data; cancelling flow @%s"
+ "[E]sim config failed. %@ @%s"
```
