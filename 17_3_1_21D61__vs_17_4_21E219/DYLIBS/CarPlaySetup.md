## CarPlaySetup

> `/System/Library/PrivateFrameworks/CarPlaySetup.framework/CarPlaySetup`

```diff

-533.8.0.0.0
-  __TEXT.__text: 0x46fc
-  __TEXT.__auth_stubs: 0x340
-  __TEXT.__objc_methlist: 0x314
-  __TEXT.__const: 0x58
-  __TEXT.__cstring: 0x3f6
-  __TEXT.__gcc_except_tab: 0x74
-  __TEXT.__oslogstring: 0x5b5
-  __TEXT.__unwind_info: 0x178
-  __TEXT.__objc_classname: 0x148
-  __TEXT.__objc_methname: 0xf3f
-  __TEXT.__objc_methtype: 0x338
-  __TEXT.__objc_stubs: 0xba0
-  __DATA_CONST.__got: 0x18
-  __DATA_CONST.__const: 0x210
-  __DATA_CONST.__objc_classlist: 0x30
+553.12.2.0.0
+  __TEXT.__text: 0x4438
+  __TEXT.__auth_stubs: 0x360
+  __TEXT.__objc_methlist: 0x1e4
+  __TEXT.__const: 0x60
+  __TEXT.__oslogstring: 0x21c
+  __TEXT.__cstring: 0x6b0
+  __TEXT.__gcc_except_tab: 0x4c
+  __TEXT.__unwind_info: 0x138
+  __TEXT.__objc_classname: 0x72
+  __TEXT.__objc_methname: 0xde1
+  __TEXT.__objc_methtype: 0x255
+  __TEXT.__objc_stubs: 0xaa0
+  __DATA_CONST.__got: 0x40
+  __DATA_CONST.__const: 0x178
+  __DATA_CONST.__objc_classlist: 0x18
   __DATA_CONST.__objc_catlist: 0x8
-  __DATA_CONST.__objc_protolist: 0x40
+  __DATA_CONST.__objc_protolist: 0x10
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_const: 0x1088
-  __DATA_CONST.__objc_selrefs: 0x370
-  __AUTH_CONST.__cfstring: 0x340
-  __AUTH_CONST.__objc_const: 0x1f0
-  __AUTH_CONST.__const: 0x120
-  __AUTH_CONST.__auth_got: 0x1b0
-  __AUTH.__objc_data: 0x1e0
-  __DATA.__objc_protorefs: 0x18
-  __DATA.__objc_classrefs: 0x88
-  __DATA.__objc_superrefs: 0x20
-  __DATA.__objc_ivar: 0x28
-  __DATA.__data: 0x300
+  __DATA_CONST.__objc_const: 0x4f0
+  __DATA_CONST.__objc_selrefs: 0x340
+  __DATA_CONST.__objc_protorefs: 0x8
+  __DATA_CONST.__objc_classrefs: 0xa8
+  __DATA_CONST.__objc_superrefs: 0x10
+  __AUTH_CONST.__objc_const: 0x118
+  __AUTH_CONST.__cfstring: 0x660
+  __AUTH_CONST.__objc_doubleobj: 0x10
+  __AUTH_CONST.__const: 0x60
+  __AUTH_CONST.__auth_got: 0x1c0
+  __AUTH.__objc_data: 0xf0
+  __DATA.__objc_ivar: 0x10
+  __DATA.__data: 0xc0
   __DATA.__bss: 0x10
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
+  - /System/Library/Frameworks/CoreGraphics.framework/CoreGraphics
   - /System/Library/Frameworks/Foundation.framework/Foundation
   - /System/Library/Frameworks/UIKit.framework/UIKit
   - /System/Library/PrivateFrameworks/CarKit.framework/CarKit
   - /System/Library/PrivateFrameworks/ProxCardKit.framework/ProxCardKit
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 2EAC894A-B446-3699-8B90-F5F205D9DBF0
-  Functions: 122
-  Symbols:   552
-  CStrings:  310
+  UUID: E87334D4-47E0-303C-8B77-2E4120E92546
+  Functions: 76
+  Symbols:   381
+  CStrings:  304
 
Symbols:
+ +[CARSetupPrompts addSkipForNowToAssetProgressPrompt:skipHandler:]
+ +[CARSetupPrompts assetProgressPromptForVehicleName:progressReporter:cancelHandler:]
+ +[CARSetupPrompts assetReadyPromptForVehicleName:confirmationHandler:]
+ +[CARSetupPrompts assetSupportingConnectPromptWithBluetoothOnlyOption:responseHandler:]
+ +[CARSetupPrompts assetSupportingUseWirelessPromptWithWirelessEnablement:declineVariant:responseHandler:]
+ +[CARSetupPrompts bluetoothConfirmationPromptForVehicleName:numericCode:responseHandler:]
+ +[CARSetupPrompts bluetoothContactsSyncPromptWithResponseHandler:]
+ +[CARSetupPrompts bluetoothFailedPromptForVehicleName:isTimeout:responseHandler:]
+ +[CARSetupPrompts connectPromptWithBluetoothOnlyOption:responseHandler:]
+ +[CARSetupPrompts useWirelessPromptWithWirelessEnablement:declineVariant:responseHandler:]
+ +[CARSetupPrompts waitingPrompt]
+ -[PRXCardContentViewController(CARSetupPrompts) carSetup_addMainContentCenteredView:size:]
+ _CGSizeZero
+ _CRLocalizedWiFiVariantKeyForKey
+ _CarPairingLogging
+ _NSFontAttributeName
+ _NSKernAttributeName
+ _NSParagraphStyleAttributeName
+ _OBJC_CLASS_$_NSConstantDoubleNumber
+ _OBJC_CLASS_$_NSMutableAttributedString
+ _OBJC_CLASS_$_NSMutableParagraphStyle
+ _OBJC_CLASS_$_UIActivityIndicatorView
+ _OBJC_CLASS_$_UIFont
+ _OBJC_CLASS_$_UILabel
+ _UIFontWeightRegular
+ ___49-[CARSetupHeadUnitPairingPrompt _setupConnection]_block_invoke.62
+ ___49-[CARSetupHeadUnitPairingPrompt _setupConnection]_block_invoke.62.cold.1
+ ___66+[CARSetupPrompts addSkipForNowToAssetProgressPrompt:skipHandler:]_block_invoke
+ ___66+[CARSetupPrompts bluetoothContactsSyncPromptWithResponseHandler:]_block_invoke
+ ___66+[CARSetupPrompts bluetoothContactsSyncPromptWithResponseHandler:]_block_invoke_2
+ ___70+[CARSetupPrompts assetReadyPromptForVehicleName:confirmationHandler:]_block_invoke
+ ___72+[CARSetupPrompts connectPromptWithBluetoothOnlyOption:responseHandler:]_block_invoke
+ ___72+[CARSetupPrompts connectPromptWithBluetoothOnlyOption:responseHandler:]_block_invoke.139
+ ___72+[CARSetupPrompts connectPromptWithBluetoothOnlyOption:responseHandler:]_block_invoke.140
+ ___81+[CARSetupPrompts bluetoothFailedPromptForVehicleName:isTimeout:responseHandler:]_block_invoke
+ ___84+[CARSetupPrompts assetProgressPromptForVehicleName:progressReporter:cancelHandler:]_block_invoke
+ ___89+[CARSetupPrompts bluetoothConfirmationPromptForVehicleName:numericCode:responseHandler:]_block_invoke
+ ___89+[CARSetupPrompts bluetoothConfirmationPromptForVehicleName:numericCode:responseHandler:]_block_invoke_2
+ ___90+[CARSetupPrompts useWirelessPromptWithWirelessEnablement:declineVariant:responseHandler:]_block_invoke
+ ___90+[CARSetupPrompts useWirelessPromptWithWirelessEnablement:declineVariant:responseHandler:]_block_invoke_2
+ ___block_literal_global.72
+ _objc_msgSend$addAttribute:value:range:
+ _objc_msgSend$carSetup_addMainContentCenteredView:size:
+ _objc_msgSend$connectPromptWithBluetoothOnlyOption:responseHandler:
+ _objc_msgSend$constraintEqualToAnchor:constant:
+ _objc_msgSend$constraintEqualToAnchor:multiplier:
+ _objc_msgSend$constraintEqualToSystemSpacingBelowAnchor:multiplier:
+ _objc_msgSend$constraintGreaterThanOrEqualToSystemSpacingBelowAnchor:multiplier:
+ _objc_msgSend$imageNamed:inBundle:withConfiguration:
+ _objc_msgSend$initWithActivityIndicatorStyle:
+ _objc_msgSend$initWithString:
+ _objc_msgSend$labelColor
+ _objc_msgSend$length
+ _objc_msgSend$monospacedDigitSystemFontOfSize:weight:
+ _objc_msgSend$progress
+ _objc_msgSend$setAlignment:
+ _objc_msgSend$setAttributedText:
+ _objc_msgSend$setObservedProgress:animated:
+ _objc_msgSend$startAnimating
+ _objc_msgSend$useWirelessPromptWithWirelessEnablement:declineVariant:responseHandler:
+ _objc_opt_isKindOfClass
- +[CARSetupPrompts connectPromptWithResponseHandler:]
- +[CARSetupPrompts useWirelessPromptWithResponseHandler:]
- -[CARSetupPromptDirector .cxx_destruct]
- -[CARSetupPromptDirector _handleConnectionReset]
- -[CARSetupPromptDirector _presenterIsReady]
- -[CARSetupPromptDirector _servicePerform:]
- -[CARSetupPromptDirector _setupConnection]
- -[CARSetupPromptDirector _synchronous_servicePerform:]
- -[CARSetupPromptDirector connection]
- -[CARSetupPromptDirector dealloc]
- -[CARSetupPromptDirector initWithPresenter:]
- -[CARSetupPromptDirector invalidate]
- -[CARSetupPromptDirector presenterDidDismiss]
- -[CARSetupPromptDirector presenter]
- -[CARSetupPromptDirector setConnection:]
- -[CARSetupPromptPresenter .cxx_destruct]
- -[CARSetupPromptPresenter _presentPromptViewController:]
- -[CARSetupPromptPresenter initWithPresentingViewController:]
- -[CARSetupPromptPresenter navigationController]
- -[CARSetupPromptPresenter presentingViewController]
- -[CARSetupPromptPresenter promptDirector:wantsToPresentAllowWhileLockedPromptForVehicleName:responseHandler:]
- -[CARSetupPromptPresenter promptDirector:wantsToPresentConnectPromptWithResponseHandler:]
- -[CARSetupPromptPresenter promptDirector:wantsToPresentEnhancedIntegrationPromptForVehicleName:responseHandler:]
- -[CARSetupPromptPresenter promptDirector:wantsToPresentUseWirelessPromptWithResponseHandler:]
- -[CARSetupPromptPresenter promptDirector]
- -[CARSetupPromptPresenter proxCardFlowDidDismiss]
- -[CARSetupPromptPresenter proxCardFlowWillPresent]
- -[CARSetupPromptPresenter setNavigationController:]
- -[CARSetupPromptPresenterProxy .cxx_destruct]
- -[CARSetupPromptPresenterProxy director]
- -[CARSetupPromptPresenterProxy presentAllowWhileLockedPromptForVehicleName:responseHandler:]
- -[CARSetupPromptPresenterProxy presentConnectPromptWithResponseHandler:]
- -[CARSetupPromptPresenterProxy presentEnhancedIntegrationPromptForVehicleName:responseHandler:]
- -[CARSetupPromptPresenterProxy presentUseWirelessPromptWithResponseHandler:]
- -[CARSetupPromptPresenterProxy setDirector:]
- GCC_except_table24
- _OBJC_CLASS_$_CARSetupPromptDirector
- _OBJC_CLASS_$_CARSetupPromptPresenter
- _OBJC_CLASS_$_CARSetupPromptPresenterProxy
- _OBJC_IVAR_$_CARSetupPromptDirector._connection
- _OBJC_IVAR_$_CARSetupPromptDirector._presenter
- _OBJC_IVAR_$_CARSetupPromptPresenter._navigationController
- _OBJC_IVAR_$_CARSetupPromptPresenter._presentingViewController
- _OBJC_IVAR_$_CARSetupPromptPresenter._promptDirector
- _OBJC_IVAR_$_CARSetupPromptPresenterProxy._director
- _OBJC_METACLASS_$_CARSetupPromptDirector
- _OBJC_METACLASS_$_CARSetupPromptPresenter
- _OBJC_METACLASS_$_CARSetupPromptPresenterProxy
- _OUTLINED_FUNCTION_2
- __OBJC_$_INSTANCE_METHODS_CARSetupPromptDirector
- __OBJC_$_INSTANCE_METHODS_CARSetupPromptPresenter
- __OBJC_$_INSTANCE_METHODS_CARSetupPromptPresenterProxy
- __OBJC_$_INSTANCE_VARIABLES_CARSetupPromptDirector
- __OBJC_$_INSTANCE_VARIABLES_CARSetupPromptPresenter
- __OBJC_$_INSTANCE_VARIABLES_CARSetupPromptPresenterProxy
- __OBJC_$_PROP_LIST_CARSetupPromptDirector
- __OBJC_$_PROP_LIST_CARSetupPromptPresenter
- __OBJC_$_PROP_LIST_CARSetupPromptPresenterProxy
- __OBJC_$_PROP_LIST_NSProgressReporting
- __OBJC_$_PROTOCOL_INSTANCE_METHODS_BSInvalidatable
- __OBJC_$_PROTOCOL_INSTANCE_METHODS_CARSetupPromptPresenting
- __OBJC_$_PROTOCOL_INSTANCE_METHODS_CRSetupPromptDirectorService
- __OBJC_$_PROTOCOL_INSTANCE_METHODS_CRSetupPromptPresenterService
- __OBJC_$_PROTOCOL_INSTANCE_METHODS_NSProgressReporting
- __OBJC_$_PROTOCOL_INSTANCE_METHODS_OPT_PRXFlowDelegate
- __OBJC_$_PROTOCOL_METHOD_TYPES_BSInvalidatable
- __OBJC_$_PROTOCOL_METHOD_TYPES_CARSetupPromptPresenting
- __OBJC_$_PROTOCOL_METHOD_TYPES_CRSetupPromptDirectorService
- __OBJC_$_PROTOCOL_METHOD_TYPES_CRSetupPromptPresenterService
- __OBJC_$_PROTOCOL_METHOD_TYPES_NSProgressReporting
- __OBJC_$_PROTOCOL_METHOD_TYPES_PRXFlowDelegate
- __OBJC_$_PROTOCOL_REFS_BSInvalidatable
- __OBJC_$_PROTOCOL_REFS_CARSetupPromptPresenting
- __OBJC_$_PROTOCOL_REFS_CRSetupPromptDirectorService
- __OBJC_$_PROTOCOL_REFS_CRSetupPromptPresenterService
- __OBJC_$_PROTOCOL_REFS_NSProgressReporting
- __OBJC_$_PROTOCOL_REFS_PRXFlowDelegate
- __OBJC_CLASS_PROTOCOLS_$_CARSetupPromptDirector
- __OBJC_CLASS_PROTOCOLS_$_CARSetupPromptPresenter
- __OBJC_CLASS_PROTOCOLS_$_CARSetupPromptPresenterProxy
- __OBJC_CLASS_RO_$_CARSetupPromptDirector
- __OBJC_CLASS_RO_$_CARSetupPromptPresenter
- __OBJC_CLASS_RO_$_CARSetupPromptPresenterProxy
- __OBJC_LABEL_PROTOCOL_$_BSInvalidatable
- __OBJC_LABEL_PROTOCOL_$_CARSetupPromptPresenting
- __OBJC_LABEL_PROTOCOL_$_CRSetupPromptDirectorService
- __OBJC_LABEL_PROTOCOL_$_CRSetupPromptPresenterService
- __OBJC_LABEL_PROTOCOL_$_NSProgressReporting
- __OBJC_LABEL_PROTOCOL_$_PRXFlowDelegate
- __OBJC_METACLASS_RO_$_CARSetupPromptDirector
- __OBJC_METACLASS_RO_$_CARSetupPromptPresenter
- __OBJC_METACLASS_RO_$_CARSetupPromptPresenterProxy
- __OBJC_PROTOCOL_$_BSInvalidatable
- __OBJC_PROTOCOL_$_CARSetupPromptPresenting
- __OBJC_PROTOCOL_$_CRSetupPromptDirectorService
- __OBJC_PROTOCOL_$_CRSetupPromptPresenterService
- __OBJC_PROTOCOL_$_NSProgressReporting
- __OBJC_PROTOCOL_$_PRXFlowDelegate
- __OBJC_PROTOCOL_REFERENCE_$_CRSetupPromptDirectorService
- __OBJC_PROTOCOL_REFERENCE_$_CRSetupPromptPresenterService
- ___109-[CARSetupPromptPresenter promptDirector:wantsToPresentAllowWhileLockedPromptForVehicleName:responseHandler:]_block_invoke
- ___112-[CARSetupPromptPresenter promptDirector:wantsToPresentEnhancedIntegrationPromptForVehicleName:responseHandler:]_block_invoke
- ___42-[CARSetupPromptDirector _servicePerform:]_block_invoke
- ___42-[CARSetupPromptDirector _servicePerform:]_block_invoke.cold.1
- ___42-[CARSetupPromptDirector _setupConnection]_block_invoke
- ___42-[CARSetupPromptDirector _setupConnection]_block_invoke.102
- ___42-[CARSetupPromptDirector _setupConnection]_block_invoke.103
- ___42-[CARSetupPromptDirector _setupConnection]_block_invoke.cold.1
- ___42-[CARSetupPromptDirector _setupConnection]_block_invoke_2
- ___42-[CARSetupPromptDirector _setupConnection]_block_invoke_2.cold.1
- ___43-[CARSetupPromptDirector _presenterIsReady]_block_invoke
- ___43-[CARSetupPromptDirector _presenterIsReady]_block_invoke_2
- ___43-[CARSetupPromptDirector _presenterIsReady]_block_invoke_2.cold.1
- ___43-[CARSetupPromptDirector _presenterIsReady]_block_invoke_2.cold.2
- ___45-[CARSetupPromptDirector presenterDidDismiss]_block_invoke
- ___45-[CARSetupPromptDirector presenterDidDismiss]_block_invoke_2
- ___45-[CARSetupPromptDirector presenterDidDismiss]_block_invoke_2.cold.1
- ___45-[CARSetupPromptDirector presenterDidDismiss]_block_invoke_2.cold.2
- ___49-[CARSetupHeadUnitPairingPrompt _setupConnection]_block_invoke.61
- ___49-[CARSetupHeadUnitPairingPrompt _setupConnection]_block_invoke.61.cold.1
- ___52+[CARSetupPrompts connectPromptWithResponseHandler:]_block_invoke
- ___52+[CARSetupPrompts connectPromptWithResponseHandler:]_block_invoke_2
- ___54-[CARSetupPromptDirector _synchronous_servicePerform:]_block_invoke
- ___54-[CARSetupPromptDirector _synchronous_servicePerform:]_block_invoke.cold.1
- ___56+[CARSetupPrompts useWirelessPromptWithResponseHandler:]_block_invoke
- ___56+[CARSetupPrompts useWirelessPromptWithResponseHandler:]_block_invoke_2
- ___72-[CARSetupPromptPresenterProxy presentConnectPromptWithResponseHandler:]_block_invoke
- ___72-[CARSetupPromptPresenterProxy presentConnectPromptWithResponseHandler:]_block_invoke.9
- ___76-[CARSetupPromptPresenterProxy presentUseWirelessPromptWithResponseHandler:]_block_invoke
- ___76-[CARSetupPromptPresenterProxy presentUseWirelessPromptWithResponseHandler:]_block_invoke.12
- ___89-[CARSetupPromptPresenter promptDirector:wantsToPresentConnectPromptWithResponseHandler:]_block_invoke
- ___92-[CARSetupPromptPresenterProxy presentAllowWhileLockedPromptForVehicleName:responseHandler:]_block_invoke
- ___92-[CARSetupPromptPresenterProxy presentAllowWhileLockedPromptForVehicleName:responseHandler:]_block_invoke.1
- ___93-[CARSetupPromptPresenter promptDirector:wantsToPresentUseWirelessPromptWithResponseHandler:]_block_invoke
- ___95-[CARSetupPromptPresenterProxy presentEnhancedIntegrationPromptForVehicleName:responseHandler:]_block_invoke
- ___95-[CARSetupPromptPresenterProxy presentEnhancedIntegrationPromptForVehicleName:responseHandler:]_block_invoke.15
- ___block_descriptor_32_e40_v16?0"<CRSetupPromptDirectorService>"8l
- ___block_descriptor_40_e8_32bs_e8_v12?0B8ls32l8
- ___block_descriptor_48_e8_32s40bs_e5_v8?0ls32l8s40l8
- ___block_descriptor_56_e8_32s40s48bs_e5_v8?0ls32l8s40l8s48l8
- ___block_literal_global.106
- ___block_literal_global.108
- ___block_literal_global.71
- ___block_literal_global.88
- ___block_literal_global.90
- ___block_literal_global.92
- _dispatch_sync
- _objc_msgSend$_presentPromptViewController:
- _objc_msgSend$_presenterIsReady
- _objc_msgSend$allowWhileLockedPromptForVehicleName:responseHandler:
- _objc_msgSend$blackColor
- _objc_msgSend$connectPromptWithResponseHandler:
- _objc_msgSend$director
- _objc_msgSend$enhancedIntegrationPromptForVehicleName:responseHandler:
- _objc_msgSend$initWithPresenter:
- _objc_msgSend$navigationController
- _objc_msgSend$presentProxCardFlowWithDelegate:initialViewController:
- _objc_msgSend$presenter
- _objc_msgSend$presenterDidDismiss
- _objc_msgSend$presenterDidDismissWithCompletion:
- _objc_msgSend$presenterIsReadyWithCompletion:
- _objc_msgSend$presentingViewController
- _objc_msgSend$promptDirector
- _objc_msgSend$promptDirector:wantsToPresentAllowWhileLockedPromptForVehicleName:responseHandler:
- _objc_msgSend$promptDirector:wantsToPresentConnectPromptWithResponseHandler:
- _objc_msgSend$promptDirector:wantsToPresentEnhancedIntegrationPromptForVehicleName:responseHandler:
- _objc_msgSend$promptDirector:wantsToPresentUseWirelessPromptWithResponseHandler:
- _objc_msgSend$pushViewController:animated:
- _objc_msgSend$remoteObjectProxyWithErrorHandler:
- _objc_msgSend$setDirector:
- _objc_msgSend$setExportedInterface:
- _objc_msgSend$setExportedObject:
- _objc_msgSend$setNavigationController:
- _objc_msgSend$useWirelessPromptWithResponseHandler:
CStrings:
+ "@28@0:8B16@?20"
+ "@36@0:8@16B24@?28"
+ "@40@0:8@16@24@?32"
+ "@40@0:8Q16Q24@?32"
+ "BLUETOOTH_CONTACTS_SYNC_ALLOW"
+ "BLUETOOTH_CONTACTS_SYNC_DONT_ALLOW"
+ "BLUETOOTH_CONTACTS_SYNC_MESSAGE"
+ "BLUETOOTH_CONTACTS_SYNC_TITLE"
+ "BLUETOOTH_FAILED_CARD_TITLE"
+ "BLUETOOTH_FAILED_MESSAGE_GENERIC_%@"
+ "BLUETOOTH_FAILED_MESSAGE_TIMEOUT"
+ "BLUETOOTH_FAILED_OK"
+ "BLUETOOTH_PAIRING_CARD_CANCEL"
+ "BLUETOOTH_PAIRING_CARD_MESSAGE_IPHONE_%@"
+ "BLUETOOTH_PAIRING_CARD_PAIR"
+ "BLUETOOTH_PAIRING_CARD_TITLE"
+ "CONNECT_USE_BLUETOOTH_ONLY"
+ "Connection_Failure"
+ "Localizable-Themed"
+ "T@\"NSString\",?,R,C"
+ "TAILORING_PROGRESS_CARD_MESSAGE_%@"
+ "TAILORING_PROGRESS_CARD_TITLE"
+ "TAILORING_READY_CARD_FINISH"
+ "TAILORING_READY_CARD_MESSAGE_%@"
+ "TAILORING_READY_CARD_TITLE"
+ "USE_LATER"
+ "USE_WIRELESS_CARPLAY_CARD_DONTUSE"
+ "USE_WIRELESS_CARPLAY_CARD_MESSAGE_BT"
+ "USE_WIRELESS_CARPLAY_CARD_MESSAGE_BT_WIFI"
+ "USE_WIRELESS_CARPLAY_CARD_MESSAGE_WIFI"
+ "USE_WIRELESS_CARPLAY_CARD_NOTNOW"
+ "addAttribute:value:range:"
+ "addSkipForNowToAssetProgressPrompt:skipHandler:"
+ "assetProgressPromptForVehicleName:progressReporter:cancelHandler:"
+ "assetReadyPromptForVehicleName:confirmationHandler:"
+ "assetSupportingConnectPromptWithBluetoothOnlyOption:responseHandler:"
+ "assetSupportingUseWirelessPromptWithWirelessEnablement:declineVariant:responseHandler:"
+ "bluetoothConfirmationPromptForVehicleName:numericCode:responseHandler:"
+ "bluetoothContactsSyncPromptWithResponseHandler:"
+ "bluetoothFailedPromptForVehicleName:isTimeout:responseHandler:"
+ "carSetup_addMainContentCenteredView:size:"
+ "connectPromptWithBluetoothOnlyOption:responseHandler:"
+ "constraintEqualToAnchor:constant:"
+ "constraintEqualToAnchor:multiplier:"
+ "constraintEqualToSystemSpacingBelowAnchor:multiplier:"
+ "constraintGreaterThanOrEqualToSystemSpacingBelowAnchor:multiplier:"
+ "imageNamed:inBundle:withConfiguration:"
+ "initWithActivityIndicatorStyle:"
+ "initWithString:"
+ "labelColor"
+ "length"
+ "monospacedDigitSystemFontOfSize:weight:"
+ "received accept for connect prompt"
+ "received decline for connect prompt"
+ "received dismiss / decline for connect prompt"
+ "setAlignment:"
+ "setAttributedText:"
+ "startAnimating"
+ "useWirelessPromptWithWirelessEnablement:declineVariant:responseHandler:"
+ "v40@0:8@16{CGSize=dd}24"
+ "waitingPrompt"
- "\x12"
- "@\"<CARSetupPromptPresenting>\""
- "@\"CARSetupPromptDirector\""
- "@\"NSProgress\"16@0:8"
- "@\"UINavigationController\""
- "@\"UIViewController\""
- "BSInvalidatable"
- "CARSetupPromptDirector"
- "CARSetupPromptPresenter"
- "CARSetupPromptPresenterProxy"
- "CARSetupPromptPresenting"
- "CRSetupPromptDirectorService"
- "CRSetupPromptPresenterService"
- "CarKit setup prompt director service was interrupted"
- "CarKit setup prompt director service was invalidated"
- "NSProgressReporting"
- "PRXFlowDelegate"
- "T@\"<CARSetupPromptPresenting>\",R,W,N,V_presenter"
- "T@\"CARSetupPromptDirector\",R,N,V_promptDirector"
- "T@\"CARSetupPromptDirector\",W,N,V_director"
- "T@\"NSProgress\",R"
- "T@\"UINavigationController\",&,N,V_navigationController"
- "T@\"UIViewController\",R,W,N,V_presentingViewController"
- "_director"
- "_navigationController"
- "_presentPromptViewController:"
- "_presenter"
- "_presenterIsReady"
- "_presentingViewController"
- "_promptDirector"
- "_servicePerform:"
- "allow while locked prompt answered: %{public}@"
- "allow while locked prompt received response: %{public}@"
- "blackColor"
- "com.apple.carkit.setupPromptDirector.service"
- "connect prompt answered: %{public}@"
- "connect prompt received response: %{public}@"
- "connectPromptWithResponseHandler:"
- "director"
- "enhanced integration prompt answered: %{public}@"
- "enhanced integration prompt received response: %{public}@"
- "error calling CarKit setup prompt service: %@"
- "initWithPresenter:"
- "initWithPresentingViewController:"
- "navigationController"
- "present allow while locked prompt"
- "present connect prompt"
- "present enhanced integration prompt for vehicle name: %@"
- "present use wireless prompt"
- "presentAllowWhileLockedPromptForVehicleName:responseHandler:"
- "presentConnectPromptWithResponseHandler:"
- "presentEnhancedIntegrationPromptForVehicleName:responseHandler:"
- "presentProxCardFlowWithDelegate:initialViewController:"
- "presentUseWirelessPromptWithResponseHandler:"
- "presenter"
- "presenterDidDismiss"
- "presenterDidDismiss, director replied"
- "presenterDidDismiss, director replied with error: %@"
- "presenterDidDismissWithCompletion:"
- "presenterIsReady"
- "presenterIsReady, director replied"
- "presenterIsReady, director replied with error: %@"
- "presenterIsReadyWithCompletion:"
- "presentingViewController"
- "promptDirector"
- "promptDirector:wantsToPresentAllowWhileLockedPromptForVehicleName:responseHandler:"
- "promptDirector:wantsToPresentConnectPromptWithResponseHandler:"
- "promptDirector:wantsToPresentEnhancedIntegrationPromptForVehicleName:responseHandler:"
- "promptDirector:wantsToPresentUseWirelessPromptWithResponseHandler:"
- "prox card flow did dismiss"
- "prox card flow will present"
- "proxCardFlowDidDismiss"
- "proxCardFlowWillPresent"
- "pushViewController:animated:"
- "pushing prox card view controller: %@"
- "remoteObjectProxyWithErrorHandler:"
- "setDirector:"
- "setExportedInterface:"
- "setExportedObject:"
- "setNavigationController:"
- "starting prox card presentation for view controller: %@"
- "use wireless prompt answered: %{public}@"
- "use wireless prompt received response: %{public}@"
- "useWirelessPromptWithResponseHandler:"
- "v16@?0@\"<CRSetupPromptDirectorService>\"8"
- "v24@0:8@?<v@?B>16"
- "v24@0:8@?<v@?B@\"NSError\">16"
- "v32@0:8@\"CARSetupPromptDirector\"16@?<v@?B>24"
- "v32@0:8@\"NSString\"16@?<v@?B>24"
- "v40@0:8@\"CARSetupPromptDirector\"16@\"NSString\"24@?<v@?B>32"
- "v40@0:8@16@24@?32"

```
