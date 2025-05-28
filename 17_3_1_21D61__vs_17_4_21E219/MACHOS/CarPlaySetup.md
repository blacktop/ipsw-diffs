## CarPlaySetup

> `/Applications/CarPlaySetup.app/CarPlaySetup`

```diff

-533.8.0.0.0
-  __TEXT.__text: 0x5c4
-  __TEXT.__auth_stubs: 0x190
-  __TEXT.__objc_stubs: 0x220
-  __TEXT.__objc_methlist: 0x128
-  __TEXT.__const: 0x38
-  __TEXT.__objc_classname: 0x91
-  __TEXT.__objc_methname: 0xfd1
-  __TEXT.__objc_methtype: 0xb4f
-  __TEXT.__cstring: 0x3c
-  __TEXT.__oslogstring: 0x81
-  __TEXT.__unwind_info: 0x88
-  __DATA_CONST.__auth_got: 0xd0
-  __DATA_CONST.__got: 0x8
-  __DATA_CONST.__const: 0x40
-  __DATA_CONST.__cfstring: 0x20
-  __DATA_CONST.__objc_classlist: 0x18
-  __DATA_CONST.__objc_protolist: 0x20
+553.12.2.0.0
+  __TEXT.__text: 0x5924
+  __TEXT.__auth_stubs: 0x360
+  __TEXT.__objc_stubs: 0xc60
+  __TEXT.__objc_methlist: 0x3f8
+  __TEXT.__const: 0x48
+  __TEXT.__objc_classname: 0x169
+  __TEXT.__objc_methname: 0x223d
+  __TEXT.__objc_methtype: 0xfec
+  __TEXT.__gcc_except_tab: 0x58
+  __TEXT.__oslogstring: 0x82d
+  __TEXT.__cstring: 0x125
+  __TEXT.__unwind_info: 0x1c8
+  __DATA_CONST.__auth_got: 0x1c0
+  __DATA_CONST.__got: 0x70
+  __DATA_CONST.__const: 0x3b0
+  __DATA_CONST.__cfstring: 0xc0
+  __DATA_CONST.__objc_classlist: 0x30
+  __DATA_CONST.__objc_protolist: 0x50
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA.__objc_const: 0x1258
-  __DATA.__objc_selrefs: 0x118
-  __DATA.__objc_classrefs: 0x28
-  __DATA.__objc_superrefs: 0x8
-  __DATA.__objc_ivar: 0x8
-  __DATA.__objc_data: 0xf0
-  __DATA.__data: 0x180
+  __DATA_CONST.__objc_protorefs: 0x10
+  __DATA_CONST.__objc_classrefs: 0x88
+  __DATA_CONST.__objc_superrefs: 0x18
+  __DATA.__objc_const: 0x2178
+  __DATA.__objc_selrefs: 0x430
+  __DATA.__objc_ivar: 0x28
+  __DATA.__objc_data: 0x1e0
+  __DATA.__data: 0x3c0
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/Foundation.framework/Foundation
   - /System/Library/Frameworks/UIKit.framework/UIKit
+  - /System/Library/PrivateFrameworks/BaseBoard.framework/BaseBoard
   - /System/Library/PrivateFrameworks/CarPlaySetup.framework/CarPlaySetup
+  - /System/Library/PrivateFrameworks/CoreAccessories.framework/CoreAccessories
+  - /System/Library/PrivateFrameworks/PassKitCore.framework/PassKitCore
+  - /System/Library/PrivateFrameworks/PassKitUI.framework/PassKitUI
   - /System/Library/PrivateFrameworks/SpringBoardUIServices.framework/SpringBoardUIServices
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 26
-  Symbols:   41
-  CStrings:  220
+  Functions: 149
+  Symbols:   94
+  CStrings:  443
 
Symbols:
+ _OBJC_CLASS_$_CARSetupPrompts
+ _OBJC_CLASS_$_NSNumber
+ _OBJC_CLASS_$_NSObject
+ _OBJC_CLASS_$_NSSet
+ _OBJC_CLASS_$_NSString
+ _OBJC_CLASS_$_NSTimer
+ _OBJC_CLASS_$_NSXPCConnection
+ _OBJC_CLASS_$_NSXPCInterface
+ _OBJC_CLASS_$_PKAddCarKeyPassConfiguration
+ _OBJC_CLASS_$_PKPaymentService
+ _OBJC_CLASS_$_PKVehicleInitiatedPairingViewController
+ __Block_object_dispose
+ __NSConcreteStackBlock
+ __Unwind_Resume
+ ___objc_personality_v0
+ __dispatch_main_q
+ __os_log_error_impl
+ _dispatch_async
+ _dispatch_sync
+ _kACCProperties_Endpoint_DigitalCarKey_CCCBrand
+ _kACCProperties_Endpoint_DigitalCarKey_CCCManufacturer
+ _kACCProperties_Endpoint_DigitalCarKey_OnlineServicesActivated
+ _kACCProperties_Endpoint_DigitalCarKey_OwnerKeyPairingAvailable
+ _kACCProperties_Endpoint_DigitalCarKey_ProductPlanUID
+ _kACCProperties_Endpoint_DigitalCarKey_ProofOfOwnershipPresent
+ _kACCProperties_Endpoint_DigitalCarKey_ProvisioningTemplate
+ _kACCProperties_Endpoint_DigitalCarKey_RadioTechnology_Bluetooth
+ _kACCProperties_Endpoint_DigitalCarKey_RadioTechnology_NearFieldCommunication
+ _kACCProperties_Endpoint_DigitalCarKey_SupportedRadioTechnologies
+ _kCFACCProperties_Endpoint_DigitalCarKey_VehicleIdentifier
+ _objc_alloc_init
+ _objc_copyWeak
+ _objc_destroyWeak
+ _objc_enumerationMutation
+ _objc_initWeak
+ _objc_loadWeakRetained
+ _objc_opt_isKindOfClass
+ _objc_opt_respondsToSelector
+ _objc_release_x1
+ _objc_release_x24
+ _objc_release_x26
+ _objc_release_x27
+ _objc_release_x28
+ _objc_retain
+ _objc_retain_x1
+ _objc_retain_x19
+ _objc_retain_x21
+ _objc_retain_x22
+ _objc_retain_x23
+ _objc_retain_x24
+ _objc_retain_x4
+ _objc_retain_x5
+ _objc_retain_x8
+ _objc_storeWeak
- _OBJC_CLASS_$_CARSetupPromptPresenter
CStrings:
+ "\x11"
+ "\x13"
+ "@\"<CARSetupPromptPresenting>\""
+ "@\"CARSetupPromptDirector\""
+ "@\"NSProgress\""
+ "@\"NSProgress\"16@0:8"
+ "@\"NSProgress\"24@0:8@?<v@?B@\"NSError\">16"
+ "@\"NSTimer\""
+ "@\"NSXPCConnection\""
+ "@\"UINavigationController\""
+ "@\"UIViewController\""
+ "@24@0:8@?16"
+ "BSInvalidatable"
+ "Bluetooth confirmation prompt answered: %{public}@"
+ "Bluetooth confirmation prompt received response: %{public}@"
+ "Bluetooth contacts sync prompt answered: %{public}@"
+ "Bluetooth contacts sync prompt received response: %{public}@"
+ "Bluetooth failed prompt answered"
+ "Bluetooth failed prompt received response"
+ "CARSetupPromptDirector"
+ "CARSetupPromptPresenter"
+ "CARSetupPromptPresenterProxy"
+ "CARSetupPromptPresenting"
+ "CRSetupPromptDirectorService"
+ "CRSetupPromptPresenterService"
+ "CarKit setup prompt director service was interrupted"
+ "CarKit setup prompt director service was invalidated"
+ "NO"
+ "NSProgressReporting"
+ "PRXFlowDelegate"
+ "PassKit didn't want to present car key setup"
+ "T@\"<CARSetupPromptPresenting>\",R,W,N,V_presenter"
+ "T@\"CARSetupPromptDirector\",R,N,V_promptDirector"
+ "T@\"CARSetupPromptDirector\",W,N,V_director"
+ "T@\"NSProgress\",&,N,V_progress"
+ "T@\"NSProgress\",R"
+ "T@\"NSString\",?,R,C"
+ "T@\"NSTimer\",&,N,V_skipTimer"
+ "T@\"NSXPCConnection\",&,N,V_connection"
+ "T@\"UINavigationController\",&,N,V_navigationController"
+ "T@\"UIViewController\",R,W,N,V_presentingViewController"
+ "T@\"UIWindow\",?,&,N"
+ "YES"
+ "_connection"
+ "_director"
+ "_handleConnectionReset"
+ "_invalidateSkipTimer"
+ "_navigationController"
+ "_passConfigurationFromDigitalCarKeyInfo:vehicleName:"
+ "_presentPromptViewController:"
+ "_presenter"
+ "_presenterIsReady"
+ "_presentingViewController"
+ "_progress"
+ "_promptDirector"
+ "_remoteAssetProgress"
+ "_servicePerform:"
+ "_setupConnection"
+ "_skipTimer"
+ "_synchronous_servicePerform:"
+ "accepted"
+ "addSkipForNowToAssetProgressPrompt:skipHandler:"
+ "allow while locked prompt answered: %{public}@"
+ "allow while locked prompt received response: %{public}@"
+ "allowWhileLockedPromptForVehicleName:responseHandler:"
+ "asset progress completed: success: %@ error: %@"
+ "asset progress prompt canceled"
+ "asset progress prompt skipped"
+ "asset progress prompt was canceled"
+ "asset ready prompt confirmed"
+ "asset ready prompt was confirmed"
+ "assetProgressPromptForVehicleName:progressReporter:cancelHandler:"
+ "assetReadyPromptForVehicleName:confirmationHandler:"
+ "assetSupportingConnectPromptWithBluetoothOnlyOption:responseHandler:"
+ "assetSupportingUseWirelessPromptWithWirelessEnablement:declineVariant:responseHandler:"
+ "bluetoothConfirmationPromptForVehicleName:numericCode:responseHandler:"
+ "bluetoothContactsSyncPromptWithResponseHandler:"
+ "bluetoothFailedPromptForVehicleName:isTimeout:responseHandler:"
+ "boolValue"
+ "com.apple.carkit.setupPromptDirector.service"
+ "connect prompt answered: %{public}@"
+ "connect prompt received response: %{public}@"
+ "connectPromptWithBluetoothOnlyOption:responseHandler:"
+ "connection"
+ "countByEnumeratingWithState:objects:count:"
+ "dealloc"
+ "declined"
+ "director"
+ "enhanced integration prompt answered: %{public}@"
+ "enhanced integration prompt received response: %{public}@"
+ "enhancedIntegrationPromptForVehicleName:responseHandler:"
+ "error calling CarKit setup prompt service: %@"
+ "init"
+ "initWithMachServiceName:options:"
+ "initWithPresenter:"
+ "integerValue"
+ "interfaceWithProtocol:"
+ "invalidate"
+ "navigationController"
+ "objectForKey:"
+ "present Bluetooth confirmation prompt"
+ "present Bluetooth contacts sync prompt"
+ "present Bluetooth failed prompt"
+ "present allow while locked prompt"
+ "present asset progress prompt for vehicle name: %@"
+ "present asset ready prompt for vehicle name: %@"
+ "present connect prompt"
+ "present enhanced integration prompt for vehicle name: %@"
+ "present setup car keys prompt for vehicle name: %@"
+ "present use wireless prompt"
+ "present waiting prompt"
+ "presentAllowWhileLockedPromptForVehicleName:responseHandler:"
+ "presentAssetProgressPromptForVehicleName:cancelHandler:"
+ "presentAssetReadyPromptForVehicleName:confirmationHandler:"
+ "presentAssetSupportingConnectPromptWithBluetoothOnlyOption:responseHandler:"
+ "presentAssetSupportingUseWirelessPromptWithWirelessEnablement:declineVariant:responseHandler:"
+ "presentBluetoothConfirmationPromptForVehicleName:numericCode:responseHandler:"
+ "presentBluetoothContactsSyncPromptWithResponseHandler:"
+ "presentBluetoothFailedPromptForVehicleName:isTimeout:responseHandler:"
+ "presentConnectPromptWithBluetoothOnlyOption:responseHandler:"
+ "presentEnhancedIntegrationPromptForVehicleName:responseHandler:"
+ "presentProxCardFlowWithDelegate:initialViewController:"
+ "presentSetupCarKeysPromptForVehicleName:carKeyInfo:cancelHandler:"
+ "presentUseWirelessPromptWithWirelessEnablement:declineVariant:responseHandler:"
+ "presentWaitingPrompt"
+ "presenter"
+ "presenterDidDismiss"
+ "presenterDidDismiss, director replied"
+ "presenterDidDismiss, director replied with error: %@"
+ "presenterDidDismissWithCompletion:"
+ "presenterIsReady"
+ "presenterIsReady, director replied"
+ "presenterIsReady, director replied with error: %@"
+ "presenterIsReadyWithCompletion:"
+ "presenterRequestsAssetProgressWithCompletion:"
+ "presentingViewController"
+ "progress"
+ "promptDirector"
+ "promptDirector:wantsToPresentAllowWhileLockedPromptForVehicleName:responseHandler:"
+ "promptDirector:wantsToPresentAssetProgressPromptForVehicleName:progressReporter:cancelHandler:"
+ "promptDirector:wantsToPresentAssetReadyPromptForVehicleName:confirmationHandler:"
+ "promptDirector:wantsToPresentAssetSupportingConnectPromptWithBluetoothOnlyOption:responseHandler:"
+ "promptDirector:wantsToPresentAssetSupportingUseWirelessPromptWithWirelessEnablement:declineVariant:responseHandler:"
+ "promptDirector:wantsToPresentBluetoothConfirmationPromptForVehicleName:numericCode:responseHandler:"
+ "promptDirector:wantsToPresentBluetoothContactsSyncPromptWithResponseHandler:"
+ "promptDirector:wantsToPresentBluetoothFailedPromptForVehicleName:isTimeout:responseHandler:"
+ "promptDirector:wantsToPresentConnectPromptWithBluetoothOnlyOption:responseHandler:"
+ "promptDirector:wantsToPresentEnhancedIntegrationPromptForVehicleName:responseHandler:"
+ "promptDirector:wantsToPresentSetupCarKeysPromptForVehicleName:carKeyInfo:cancelHandler:"
+ "promptDirector:wantsToPresentUseWirelessPromptWithWirelessEnablement:declineVariant:responseHandler:"
+ "promptDirectorWantsToPresentWaiting:"
+ "prox card flow did dismiss"
+ "prox card flow will present"
+ "proxCardFlowDidDismiss"
+ "proxCardFlowWillPresent"
+ "pushViewController:animated:"
+ "pushing prox card view controller: %@"
+ "remote asset progress: %@"
+ "remoteObjectProxyWithErrorHandler:"
+ "requesting remote asset progress"
+ "resume"
+ "scheduledTimerWithTimeInterval:repeats:block:"
+ "setConnection:"
+ "setDirector:"
+ "setExportedInterface:"
+ "setExportedObject:"
+ "setInterruptionHandler:"
+ "setInvalidationHandler:"
+ "setIssuerIdentifier:"
+ "setManufacturerIdentifier:"
+ "setNavigationController:"
+ "setOnlineServicesActivated:"
+ "setOwnerKeyPairingAvailable:"
+ "setPairedEntityIdentifier:"
+ "setProductPlanIdentifier:"
+ "setProgress:"
+ "setProofOfOwnershipPresent:"
+ "setProvisioningTemplateIdentifier:"
+ "setReferralSource:"
+ "setRemoteObjectInterface:"
+ "setSkipTimer:"
+ "setSupportedRadioTechnologies:"
+ "setVehicleName:"
+ "setup car keys prompt was canceled"
+ "skipTimer"
+ "starting prox card presentation for view controller: %@"
+ "synchronousRemoteObjectProxyWithErrorHandler:"
+ "use wireless prompt answered: %{public}@"
+ "use wireless prompt received response: %{public}@"
+ "useWirelessPromptWithWirelessEnablement:declineVariant:responseHandler:"
+ "v12@?0B8"
+ "v16@?0@\"<CRSetupPromptDirectorService>\"8"
+ "v16@?0@\"NSError\"8"
+ "v16@?0@\"NSTimer\"8"
+ "v16@?0@\"PKVehicleInitiatedPairingViewController\"8"
+ "v20@?0B8@\"NSError\"12"
+ "v24@0:8@\"CARSetupPromptDirector\"16"
+ "v24@0:8@?16"
+ "v24@0:8@?<v@?B>16"
+ "v24@0:8@?<v@?B@\"NSError\">16"
+ "v28@0:8B16@?20"
+ "v28@0:8B16@?<v@?B>20"
+ "v32@0:8@\"CARSetupPromptDirector\"16@?<v@?B>24"
+ "v32@0:8@\"NSString\"16@?<v@?>24"
+ "v32@0:8@\"NSString\"16@?<v@?B>24"
+ "v36@0:8@\"CARSetupPromptDirector\"16B24@?<v@?B>28"
+ "v36@0:8@\"NSString\"16B24@?<v@?>28"
+ "v36@0:8@16B24@?28"
+ "v40@0:8@\"CARSetupPromptDirector\"16@\"NSString\"24@?<v@?>32"
+ "v40@0:8@\"CARSetupPromptDirector\"16@\"NSString\"24@?<v@?B>32"
+ "v40@0:8@\"NSString\"16@\"NSDictionary\"24@?<v@?>32"
+ "v40@0:8@\"NSString\"16@\"NSString\"24@?<v@?B>32"
+ "v40@0:8Q16Q24@?32"
+ "v40@0:8Q16Q24@?<v@?B>32"
+ "v44@0:8@\"CARSetupPromptDirector\"16@\"NSString\"24B32@?<v@?>36"
+ "v44@0:8@16@24B32@?36"
+ "v48@0:8@\"CARSetupPromptDirector\"16@\"NSString\"24@\"<NSProgressReporting>\"32@?<v@?>40"
+ "v48@0:8@\"CARSetupPromptDirector\"16@\"NSString\"24@\"NSDictionary\"32@?<v@?>40"
+ "v48@0:8@\"CARSetupPromptDirector\"16@\"NSString\"24@\"NSString\"32@?<v@?B>40"
+ "v48@0:8@\"CARSetupPromptDirector\"16Q24Q32@?<v@?B>40"
+ "v48@0:8@16Q24Q32@?40"
+ "v8@?0"
+ "vehicleInitiatedPairingViewControllerForConfiguration:paymentService:completion:"
+ "waitingPrompt"
- "T@\"UIWindow\",&,N"
- "viewDidDisappear:"

```
