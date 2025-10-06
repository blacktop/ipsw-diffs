## ControlCenterUI

> `/System/Library/PrivateFrameworks/ControlCenterUI.framework/ControlCenterUI`

```diff

-655.1.3.100.0
-  __TEXT.__text: 0xa37b8
-  __TEXT.__auth_stubs: 0x2500
-  __TEXT.__objc_methlist: 0xa080
-  __TEXT.__const: 0x232a
-  __TEXT.__cstring: 0x79d4
-  __TEXT.__gcc_except_tab: 0x854
-  __TEXT.__oslogstring: 0x372b
+655.1.9.0.0
+  __TEXT.__text: 0xa6cc4
+  __TEXT.__auth_stubs: 0x2590
+  __TEXT.__objc_methlist: 0xa4d8
+  __TEXT.__const: 0x233a
+  __TEXT.__cstring: 0x7b74
+  __TEXT.__gcc_except_tab: 0x8ac
+  __TEXT.__oslogstring: 0x3d3b
   __TEXT.__dlopen_cstrs: 0x14e
-  __TEXT.__constg_swiftt: 0x2554
-  __TEXT.__swift5_typeref: 0x25ec
+  __TEXT.__constg_swiftt: 0x255c
+  __TEXT.__swift5_typeref: 0x260a
   __TEXT.__swift5_builtin: 0x190
   __TEXT.__swift5_reflstr: 0x19f2
   __TEXT.__swift5_fieldmd: 0x1178
   __TEXT.__swift5_assocty: 0x198
   __TEXT.__swift5_proto: 0xd4
   __TEXT.__swift5_types: 0x118
-  __TEXT.__swift5_capture: 0xbe0
+  __TEXT.__swift5_capture: 0xc44
   __TEXT.__swift5_protos: 0x10
   __TEXT.__swift5_mpenum: 0x8
   __TEXT.__swift_as_entry: 0xc
   __TEXT.__swift_as_ret: 0x4
-  __TEXT.__unwind_info: 0x2820
+  __TEXT.__unwind_info: 0x28f8
   __TEXT.__eh_frame: 0x448
-  __TEXT.__objc_classname: 0x15c4
-  __TEXT.__objc_methname: 0x1ba04
-  __TEXT.__objc_methtype: 0x7b76
-  __TEXT.__objc_stubs: 0xbc80
-  __DATA_CONST.__got: 0xc40
-  __DATA_CONST.__const: 0x1130
-  __DATA_CONST.__objc_classlist: 0x380
+  __TEXT.__objc_classname: 0x1617
+  __TEXT.__objc_methname: 0x1c0b7
+  __TEXT.__objc_methtype: 0x7fd7
+  __TEXT.__objc_stubs: 0xc040
+  __DATA_CONST.__got: 0xc60
+  __DATA_CONST.__const: 0x1180
+  __DATA_CONST.__objc_classlist: 0x388
   __DATA_CONST.__objc_catlist: 0x38
-  __DATA_CONST.__objc_protolist: 0x550
+  __DATA_CONST.__objc_protolist: 0x558
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x5ed0
+  __DATA_CONST.__objc_selrefs: 0x6078
   __DATA_CONST.__objc_protorefs: 0x1f8
-  __DATA_CONST.__objc_superrefs: 0x1d0
+  __DATA_CONST.__objc_superrefs: 0x1d8
   __DATA_CONST.__objc_arraydata: 0x68
-  __AUTH_CONST.__auth_got: 0x1290
-  __AUTH_CONST.__const: 0x39d8
-  __AUTH_CONST.__cfstring: 0x2800
-  __AUTH_CONST.__objc_const: 0xf638
+  __AUTH_CONST.__auth_got: 0x12d8
+  __AUTH_CONST.__const: 0x3ac8
+  __AUTH_CONST.__cfstring: 0x29c0
+  __AUTH_CONST.__objc_const: 0xfa08
   __AUTH_CONST.__objc_arrayobj: 0xc0
-  __AUTH_CONST.__objc_intobj: 0x90
-  __AUTH.__objc_data: 0x17a0
-  __AUTH.__data: 0x748
-  __DATA.__objc_ivar: 0x688
-  __DATA.__data: 0x3628
+  __AUTH_CONST.__objc_intobj: 0xa8
+  __AUTH.__objc_data: 0x1728
+  __AUTH.__data: 0x6e8
+  __DATA.__objc_ivar: 0x6ac
+  __DATA.__data: 0x3658
   __DATA.__bss: 0x11d0
   __DATA.__common: 0x20
-  __DATA_DIRTY.__objc_data: 0x3140
-  __DATA_DIRTY.__data: 0xb08
+  __DATA_DIRTY.__objc_data: 0x3208
+  __DATA_DIRTY.__data: 0xbb8
   __DATA_DIRTY.__bss: 0x9f8
   __DATA_DIRTY.__common: 0x10
   - /System/Library/Frameworks/AVFoundation.framework/AVFoundation

   - /System/Library/PrivateFrameworks/ControlCenterServices.framework/ControlCenterServices
   - /System/Library/PrivateFrameworks/ControlCenterUIKit.framework/ControlCenterUIKit
   - /System/Library/PrivateFrameworks/ControlCenterUIServices.framework/ControlCenterUIServices
+  - /System/Library/PrivateFrameworks/CorePhoneNumbers.framework/CorePhoneNumbers
   - /System/Library/PrivateFrameworks/CoverSheetKit.framework/CoverSheetKit
   - /System/Library/PrivateFrameworks/FeatureFlags.framework/FeatureFlags
   - /System/Library/PrivateFrameworks/FrontBoardServices.framework/FrontBoardServices

   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  UUID: 22DF41AE-AB5B-35AD-B4ED-1205383381C7
-  Functions: 4428
-  Symbols:   9366
-  CStrings:  6322
+  UUID: FB586FBC-2D9C-377C-9806-7E22CBB98279
+  Functions: 4528
+  Symbols:   9610
+  CStrings:  6450
 
Symbols:
+ +[CCUICellularDataModuleViewController isSupported]
+ -[CCUIBluetoothModuleViewController _subtitleForDeviceWithIdentifier:connected:]
+ -[CCUICellularDataModuleViewController .cxx_destruct]
+ -[CCUICellularDataModuleViewController _actionFromSubscriptionContext:]
+ -[CCUICellularDataModuleViewController _buttonViewForCollapsedConnectivityModuleTapped]
+ -[CCUICellularDataModuleViewController _canShowWhileLocked]
+ -[CCUICellularDataModuleViewController _currentCellularPlanName]
+ -[CCUICellularDataModuleViewController _currentCellularPlanName].cold.1
+ -[CCUICellularDataModuleViewController _debugDescriptionForState:]
+ -[CCUICellularDataModuleViewController _formatPhoneNumber:]
+ -[CCUICellularDataModuleViewController _glyphImageForSignalStrength:]
+ -[CCUICellularDataModuleViewController _glyphViewForExpandedConnectivityModuleTapped]
+ -[CCUICellularDataModuleViewController _isCellularDataButtonDemoMode]
+ -[CCUICellularDataModuleViewController _isCellularDataRestricted]
+ -[CCUICellularDataModuleViewController _isEnabled]
+ -[CCUICellularDataModuleViewController _multipleSubscriptionsAvailable]
+ -[CCUICellularDataModuleViewController _multipleSubscriptionsAvailable].cold.1
+ -[CCUICellularDataModuleViewController _setEnabled:]
+ -[CCUICellularDataModuleViewController _subtitleTextWithState:]
+ -[CCUICellularDataModuleViewController _toggleState]
+ -[CCUICellularDataModuleViewController _updateContentMenuActions]
+ -[CCUICellularDataModuleViewController _updateContentMenuActions].cold.1
+ -[CCUICellularDataModuleViewController _updateGlyphImagesWithSignalStrength:]
+ -[CCUICellularDataModuleViewController _updateSignalStrength]
+ -[CCUICellularDataModuleViewController _updateState]
+ -[CCUICellularDataModuleViewController accessibilityIdentifier]
+ -[CCUICellularDataModuleViewController activeSubscriptionsDidChange]
+ -[CCUICellularDataModuleViewController buttonTapped:forEvent:]
+ -[CCUICellularDataModuleViewController buttonViewForCollapsedConnectivityModule]
+ -[CCUICellularDataModuleViewController connectivityManager]
+ -[CCUICellularDataModuleViewController contentMenuActions]
+ -[CCUICellularDataModuleViewController contentModuleContext]
+ -[CCUICellularDataModuleViewController contextMenuItems]
+ -[CCUICellularDataModuleViewController contextMenuPreviewForControlTemplateView:]
+ -[CCUICellularDataModuleViewController contextMenuShouldPresentForControlTemplateView:withCompletion:]
+ -[CCUICellularDataModuleViewController contextMenu]
+ -[CCUICellularDataModuleViewController coreTelephonyClient]
+ -[CCUICellularDataModuleViewController dealloc]
+ -[CCUICellularDataModuleViewController didBeginContextMenuPresentationForControlTemplateView:]
+ -[CCUICellularDataModuleViewController didEndContextMenuPresentationForControlTemplateView:]
+ -[CCUICellularDataModuleViewController glyphViewForExpandedConnectivityModule]
+ -[CCUICellularDataModuleViewController initWithContentModuleContext:]
+ -[CCUICellularDataModuleViewController isObservingStateChanges]
+ -[CCUICellularDataModuleViewController menuDisplayName]
+ -[CCUICellularDataModuleViewController operatorNameChanged:name:]
+ -[CCUICellularDataModuleViewController performPrimaryActionForControlTemplateView:]
+ -[CCUICellularDataModuleViewController profileConnectionDidReceiveEffectiveSettingsChangedNotification:userInfo:]
+ -[CCUICellularDataModuleViewController providesTemplateViewContextMenuDelegateForExpandedConnectivityModule]
+ -[CCUICellularDataModuleViewController providesTemplateViewDelegateForExpandedConnectivityModule]
+ -[CCUICellularDataModuleViewController setButtonViewForCollapsedConnectivityModule:]
+ -[CCUICellularDataModuleViewController setConnectivityManager:]
+ -[CCUICellularDataModuleViewController setContentMenuActions:]
+ -[CCUICellularDataModuleViewController setContentModuleContext:]
+ -[CCUICellularDataModuleViewController setCoreTelephonyClient:]
+ -[CCUICellularDataModuleViewController setGlyphViewForExpandedConnectivityModule:]
+ -[CCUICellularDataModuleViewController setObservingStateChanges:]
+ -[CCUICellularDataModuleViewController setTemplateViewForExpandedConnectivityModule:]
+ -[CCUICellularDataModuleViewController shouldBeginTransitionToExpandedContentModule]
+ -[CCUICellularDataModuleViewController signalStrengthChanged:info:]
+ -[CCUICellularDataModuleViewController startObservingStateChangesIfNecessary]
+ -[CCUICellularDataModuleViewController startObservingStateChanges]
+ -[CCUICellularDataModuleViewController stopObservingStateChangesIfNecessary]
+ -[CCUICellularDataModuleViewController stopObservingStateChanges]
+ -[CCUICellularDataModuleViewController templateViewForExpandedConnectivityModule]
+ -[CCUICellularDataModuleViewController updateState]
+ -[CCUICellularDataModuleViewController viewDidLoad]
+ -[CCUICellularDataModuleViewController viewIsAppearing:]
+ -[CCUICellularDataModuleViewController viewWillDisappear:]
+ -[CCUIConnectivityManager addCellularDataViewControllerObservingStateChanges:]
+ -[CCUIConnectivityManager cellularDataViewControllersObservingStateChanges]
+ -[CCUIConnectivityManager removeCellularDataViewControllerObservingStateChanges:]
+ -[CCUIConnectivityManager setCellularDataViewControllersObservingStateChanges:]
+ -[CCUIMainViewController(PPT) _controlCenterEnterEditModeEventStream]
+ GCC_except_table16
+ GCC_except_table47
+ GCC_except_table49
+ _CFPhoneNumberCreate
+ _CFPhoneNumberCreateString
+ _CFRelease
+ _MCFeatureAppCellularDataModificationAllowed
+ _OBJC_CLASS_$_CCUICellularDataModuleViewController
+ _OBJC_CLASS_$_NSUserDefaults
+ _OBJC_IVAR_$_CCUICellularDataModuleViewController._buttonViewForCollapsedConnectivityModule
+ _OBJC_IVAR_$_CCUICellularDataModuleViewController._connectivityManager
+ _OBJC_IVAR_$_CCUICellularDataModuleViewController._contentMenuActions
+ _OBJC_IVAR_$_CCUICellularDataModuleViewController._contentModuleContext
+ _OBJC_IVAR_$_CCUICellularDataModuleViewController._coreTelephonyClient
+ _OBJC_IVAR_$_CCUICellularDataModuleViewController._glyphViewForExpandedConnectivityModule
+ _OBJC_IVAR_$_CCUICellularDataModuleViewController._observingStateChanges
+ _OBJC_IVAR_$_CCUICellularDataModuleViewController._templateViewForExpandedConnectivityModule
+ _OBJC_IVAR_$_CCUIConnectivityManager._cellularDataViewControllersObservingStateChanges
+ _OBJC_METACLASS_$_CCUICellularDataModuleViewController
+ __CTServerConnectionCreateWithIdentifier
+ __CTServerConnectionGetCellularDataIsEnabled
+ __CTServerConnectionGetCellularDataSettings
+ __CTServerConnectionSetCellularDataIsEnabled
+ __OBJC_$_CLASS_METHODS_CCUICellularDataModuleViewController
+ __OBJC_$_INSTANCE_METHODS_CCUICellularDataModuleViewController
+ __OBJC_$_INSTANCE_VARIABLES_CCUICellularDataModuleViewController
+ __OBJC_$_PROP_LIST_CCUICellularDataModuleViewController
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_OPT_CoreTelephonyClientRegistrationDelegate
+ __OBJC_$_PROTOCOL_METHOD_TYPES_CoreTelephonyClientRegistrationDelegate
+ __OBJC_$_PROTOCOL_REFS_CoreTelephonyClientRegistrationDelegate
+ __OBJC_CLASS_PROTOCOLS_$_CCUICellularDataModuleViewController
+ __OBJC_CLASS_RO_$_CCUICellularDataModuleViewController
+ __OBJC_LABEL_PROTOCOL_$_CoreTelephonyClientRegistrationDelegate
+ __OBJC_METACLASS_RO_$_CCUICellularDataModuleViewController
+ __OBJC_PROTOCOL_$_CoreTelephonyClientRegistrationDelegate
+ ___102-[CCUICellularDataModuleViewController contextMenuShouldPresentForControlTemplateView:withCompletion:]_block_invoke
+ ___51-[CCUICellularDataModuleViewController contextMenu]_block_invoke
+ ___56-[CCUIMainViewController(PPT) runTest:options:delegate:]_block_invoke_11
+ ___65-[CCUICellularDataModuleViewController operatorNameChanged:name:]_block_invoke
+ ___67-[CCUICellularDataModuleViewController signalStrengthChanged:info:]_block_invoke
+ ___68-[CCUICellularDataModuleViewController activeSubscriptionsDidChange]_block_invoke
+ ___69-[CCUIMainViewController(PPT) _controlCenterEnterEditModeEventStream]_block_invoke
+ ___71-[CCUICellularDataModuleViewController _actionFromSubscriptionContext:]_block_invoke
+ ___71-[CCUICellularDataModuleViewController _actionFromSubscriptionContext:]_block_invoke_2
+ ___71-[CCUICellularDataModuleViewController _actionFromSubscriptionContext:]_block_invoke_2.cold.1
+ ___block_descriptor_40_e8_32s_e17_v16?0"NSError"8ls32l8
+ ___block_descriptor_40_e8_32s_e21_"RCPEventStream"8?0ls32l8
+ ___block_literal_global.114
+ _block_copy_helper.267
+ _block_copy_helper.270
+ _block_copy_helper.288
+ _block_copy_helper.298
+ _block_copy_helper.309
+ _block_copy_helper.335
+ _block_copy_helper.339
+ _block_copy_helper.369
+ _block_copy_helper.379
+ _block_copy_helper.389
+ _block_copy_helper.395
+ _block_copy_helper.414
+ _block_copy_helper.418
+ _block_copy_helper.65
+ _block_copy_helper.7
+ _block_copy_helper.72
+ _block_descriptor.269
+ _block_descriptor.272
+ _block_descriptor.290
+ _block_descriptor.300
+ _block_descriptor.311
+ _block_descriptor.337
+ _block_descriptor.341
+ _block_descriptor.371
+ _block_descriptor.381
+ _block_descriptor.391
+ _block_descriptor.397
+ _block_descriptor.416
+ _block_descriptor.420
+ _block_descriptor.67
+ _block_descriptor.74
+ _block_descriptor.9
+ _block_destroy_helper.268
+ _block_destroy_helper.271
+ _block_destroy_helper.289
+ _block_destroy_helper.299
+ _block_destroy_helper.310
+ _block_destroy_helper.336
+ _block_destroy_helper.340
+ _block_destroy_helper.370
+ _block_destroy_helper.380
+ _block_destroy_helper.390
+ _block_destroy_helper.396
+ _block_destroy_helper.415
+ _block_destroy_helper.419
+ _block_destroy_helper.66
+ _block_destroy_helper.73
+ _block_destroy_helper.8
+ _kCFAllocatorDefault
+ _objc_msgSend$_actionFromSubscriptionContext:
+ _objc_msgSend$_controlCenterEnterEditModeEventStream
+ _objc_msgSend$_currentCellularPlanName
+ _objc_msgSend$_formatPhoneNumber:
+ _objc_msgSend$_glyphImageForSignalStrength:
+ _objc_msgSend$_isCellularDataButtonDemoMode
+ _objc_msgSend$_isCellularDataRestricted
+ _objc_msgSend$_isEnabled
+ _objc_msgSend$_multipleSubscriptionsAvailable
+ _objc_msgSend$_setEnabled:
+ _objc_msgSend$_subtitleForDeviceWithIdentifier:connected:
+ _objc_msgSend$_updateContentMenuActions
+ _objc_msgSend$_updateGlyphImagesWithSignalStrength:
+ _objc_msgSend$_updateSignalStrength
+ _objc_msgSend$addCellularDataViewControllerObservingStateChanges:
+ _objc_msgSend$boolForKey:
+ _objc_msgSend$cellularDataViewControllersObservingStateChanges
+ _objc_msgSend$displayBars
+ _objc_msgSend$doubleValue
+ _objc_msgSend$effectiveBoolValueForSetting:
+ _objc_msgSend$getCurrentDataServiceDescriptorSync:
+ _objc_msgSend$getPublicSignalStrength:error:
+ _objc_msgSend$getSubscriptionInfoWithError:
+ _objc_msgSend$getSubscriptionUserFacingName:error:
+ _objc_msgSend$isSimHidden
+ _objc_msgSend$phoneNumber
+ _objc_msgSend$removeCellularDataViewControllerObservingStateChanges:
+ _objc_msgSend$setActiveUserDataSelection:completion:
+ _objc_msgSend$standardUserDefaults
+ _objc_msgSend$subscriptionsInUse
+ _objc_msgSend$userDataPreferred
+ _objectdestroy.349Tm
+ _symbolic Ieg_
+ _symbolic _____SgXw 15ControlCenterUI39SensorAttributionExpandedViewControllerC
+ _symbolic _____SgXwz_Xx 15ControlCenterUI39SensorAttributionExpandedViewControllerC
- -[CCUIBluetoothModuleViewController _connectingImage]
- GCC_except_table52
- ___block_literal_global.117
- _block_copy_helper.1
- _block_copy_helper.264
- _block_copy_helper.273
- _block_copy_helper.276
- _block_copy_helper.294
- _block_copy_helper.304
- _block_copy_helper.321
- _block_copy_helper.341
- _block_copy_helper.352
- _block_copy_helper.376
- _block_copy_helper.393
- _block_copy_helper.396
- _block_copy_helper.409
- _block_copy_helper.425
- _block_copy_helper.428
- _block_descriptor.266
- _block_descriptor.275
- _block_descriptor.278
- _block_descriptor.296
- _block_descriptor.3
- _block_descriptor.306
- _block_descriptor.323
- _block_descriptor.343
- _block_descriptor.354
- _block_descriptor.378
- _block_descriptor.395
- _block_descriptor.398
- _block_descriptor.411
- _block_descriptor.427
- _block_descriptor.430
- _block_destroy_helper.2
- _block_destroy_helper.265
- _block_destroy_helper.274
- _block_destroy_helper.277
- _block_destroy_helper.295
- _block_destroy_helper.305
- _block_destroy_helper.322
- _block_destroy_helper.342
- _block_destroy_helper.353
- _block_destroy_helper.377
- _block_destroy_helper.394
- _block_destroy_helper.397
- _block_destroy_helper.410
- _block_destroy_helper.426
- _block_destroy_helper.429
- _objc_msgSend$_connectingImage
- _objectdestroy.356Tm
CStrings:
+ "CCUICellularDataModuleViewController"
+ "CCUI_EDIT_MODE_ENTER_BEGIN"
+ "CCUI_EDIT_MODE_ENTER_END"
+ "CCUI_EDIT_MODE_EXIT_BEGIN"
+ "CCUI_EDIT_MODE_EXIT_END"
+ "CONTROL_CENTER_STATUS_BLUETOOTH_CONNECTING"
+ "CONTROL_CENTER_STATUS_BLUETOOTH_DISCONNECTING"
+ "CONTROL_CENTER_STATUS_CELLULAR_DATA_NAME"
+ "CONTROL_CENTER_STATUS_CELLULAR_DATA_OFF"
+ "CONTROL_CENTER_STATUS_CELLULAR_DATA_ON"
+ "CONTROL_CENTER_STATUS_CELLULAR_SETTINGS"
+ "ControlCenterBringupAndEnterEditMode"
+ "ControlCenterCellularDataButtonDemoMode"
+ "CoreTelephonyClientRegistrationDelegate"
+ "Error fetching module, unable to update configuration, resetting first unlock tasks..."
+ "No cached view controllers, unable to update configurations, resetting first unlock tasks..."
+ "T@\"CoreTelephonyClient\",&,N,V_coreTelephonyClient"
+ "T@\"NSHashTable\",&,N,V_cellularDataViewControllersObservingStateChanges"
+ "[Cellular Data Module] (%{public}p) Dealloc"
+ "[Cellular Data Module] (%{public}p) Initialization"
+ "[Cellular Data Module] (ConnectivityManager) Added cellularDataViewController:%{public}@ to cellularDataViewControllersObservingStateChanges: %{public}@"
+ "[Cellular Data Module] (ConnectivityManager) Removed cellularDataViewController:%{public}@ from cellularDataViewControllersObservingStateChanges: %{public}@"
+ "[Cellular Data Module] Active subscriptions changed"
+ "[Cellular Data Module] Cellular Data state updated to %{public}@ [ capable: %d enabled: %d airplaneMode: %d subtitle: %{private}@ ]"
+ "[Cellular Data Module] Could not get subscription info. Error: %@"
+ "[Cellular Data Module] Could not get subscriptions Info. Error: %@"
+ "[Cellular Data Module] Error getting plan name: %@"
+ "[Cellular Data Module] Error setting active data selection to %@. Error: %@"
+ "[Cellular Data Module] Operator name changed, updating state"
+ "[Cellular Data Module] Profile connection settings changed"
+ "[Cellular Data Module] Setting Active user data selection to %@"
+ "[Cellular Data Module] Signal strength changed to %{public}@ bars"
+ "[Cellular Data Module] Toggle Cellular Data state from %{public}@"
+ "[Satellite] Actually launching SOSBuddy app..."
+ "[Satellite] Dispatching to launch SOSBuddy app..."
+ "_actionFromSubscriptionContext:"
+ "_cellularDataViewControllersObservingStateChanges"
+ "_controlCenterEnterEditModeEventStream"
+ "_coreTelephonyClient"
+ "_currentCellularPlanName"
+ "_formatPhoneNumber:"
+ "_glyphImageForSignalStrength:"
+ "_isCellularDataButtonDemoMode"
+ "_isCellularDataRestricted"
+ "_isEnabled"
+ "_multipleSubscriptionsAvailable"
+ "_setEnabled:"
+ "_subtitleForDeviceWithIdentifier:connected:"
+ "_updateContentMenuActions"
+ "_updateGlyphImagesWithSignalStrength:"
+ "_updateSignalStrength"
+ "activeSubscriptionsDidChange"
+ "addCellularDataViewControllerObservingStateChanges:"
+ "boolForKey:"
+ "cellChanged:cell:"
+ "cellMonitorUpdate:info:"
+ "cellular-button"
+ "cellular-data"
+ "cellularDataViewControllersObservingStateChanges"
+ "cellularbars"
+ "com.apple.ControlCenter.CellularData"
+ "coreTelephonyClient"
+ "customerServiceProfileChanged:visible:"
+ "dataRatesChanged"
+ "displayBars"
+ "displayStatusChanged:status:"
+ "doubleValue"
+ "editModeEnter"
+ "editModeExit"
+ "effectiveBoolValueForSetting:"
+ "encryptionStatusChanged:info:"
+ "enhancedDataLinkQualityChanged:metric:"
+ "enhancedVoiceLinkQualityChanged:metric:"
+ "getCurrentDataServiceDescriptorSync:"
+ "getPublicSignalStrength:error:"
+ "getSubscriptionInfoWithError:"
+ "getSubscriptionUserFacingName:error:"
+ "imsRegistrationChanged:info:"
+ "isSimHidden"
+ "networkListAvailable:list:"
+ "networkReselectionNeeded:"
+ "networkSelected:success:mode:"
+ "nrDisableStatusChanged:status:"
+ "operatorNameChanged:name:"
+ "phoneNumber"
+ "plmnChanged:plmn:"
+ "prefs:root=MOBILE_DATA_SETTINGS_ID"
+ "ratSelectionChanged:selection:"
+ "rejectCauseCodeChanged:causeCode:"
+ "removeCellularDataViewControllerObservingStateChanges:"
+ "setActiveUserDataSelection:completion:"
+ "setCellularDataViewControllersObservingStateChanges:"
+ "setCoreTelephonyClient:"
+ "signalStrengthChanged:info:"
+ "standardUserDefaults"
+ "subscriptionsInUse"
+ "userDataPreferred"
+ "v24@0:8@\"CTXPCServiceSubscriptionContext\"16"
+ "v28@0:8@\"CTXPCServiceSubscriptionContext\"16B24"
+ "v32@0:8@\"CTServiceDescriptor\"16@\"CTEncryptionStatusInfo\"24"
+ "v32@0:8@\"CTServiceDescriptor\"16@\"CTNRStatus\"24"
+ "v32@0:8@\"CTServiceDescriptor\"16@\"CTPlmnInfo\"24"
+ "v32@0:8@\"CTServiceDescriptor\"16@\"CTRatSelection\"24"
+ "v32@0:8@\"CTXPCServiceSubscriptionContext\"16@\"CTCellInfo\"24"
+ "v32@0:8@\"CTXPCServiceSubscriptionContext\"16@\"CTEnhancedDataLinkQualityMetric\"24"
+ "v32@0:8@\"CTXPCServiceSubscriptionContext\"16@\"CTEnhancedLinkQualityMetric\"24"
+ "v32@0:8@\"CTXPCServiceSubscriptionContext\"16@\"CTIMSRegistrationTransportInfo\"24"
+ "v32@0:8@\"CTXPCServiceSubscriptionContext\"16@\"CTNetworkList\"24"
+ "v32@0:8@\"CTXPCServiceSubscriptionContext\"16@\"CTRegistrationDisplayStatus\"24"
+ "v32@0:8@\"CTXPCServiceSubscriptionContext\"16@\"CTSignalStrengthInfo\"24"
+ "v32@0:8@\"CTXPCServiceSubscriptionContext\"16@\"CTVoiceLinkQualityMetric\"24"
+ "v32@0:8@\"CTXPCServiceSubscriptionContext\"16@\"NSDictionary\"24"
+ "v32@0:8@\"CTXPCServiceSubscriptionContext\"16@\"NSNumber\"24"
+ "v32@0:8@\"CTXPCServiceSubscriptionContext\"16@\"NSString\"24"
+ "v36@0:8@\"CTXPCServiceSubscriptionContext\"16B24@\"NSString\"28"
+ "v36@0:8@16B24@28"
+ "voiceLinkQualityChanged:metric:"
- "_connectingImage"
- "ccui_interaction"
- "progress.indicator"

```
