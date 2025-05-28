## Passbook

> `/private/var/staged_system_apps/Passbook.app/Passbook`

```diff

 0.0.0.0.0
-  __TEXT.__text: 0xbc30
-  __TEXT.__auth_stubs: 0x5b0
-  __TEXT.__objc_stubs: 0x2300
+  __TEXT.__text: 0xbf60
+  __TEXT.__auth_stubs: 0x560
+  __TEXT.__objc_stubs: 0x2400
   __TEXT.__objc_methlist: 0x278
   __TEXT.__const: 0x50
-  __TEXT.__gcc_except_tab: 0xa4
-  __TEXT.__objc_methname: 0x3730
-  __TEXT.__cstring: 0x50d
-  __TEXT.__oslogstring: 0x33a
-  __TEXT.__objc_classname: 0xe9
-  __TEXT.__objc_methtype: 0xe13
-  __TEXT.__unwind_info: 0x20c
-  __DATA_CONST.__auth_got: 0x2e0
-  __DATA_CONST.__got: 0x5b8
-  __DATA_CONST.__const: 0x610
-  __DATA_CONST.__cfstring: 0x2e0
+  __TEXT.__gcc_except_tab: 0x34
+  __TEXT.__objc_methname: 0x352a
+  __TEXT.__cstring: 0x59a
+  __TEXT.__oslogstring: 0x46c
+  __TEXT.__objc_classname: 0xf3
+  __TEXT.__objc_methtype: 0xb08
+  __TEXT.__unwind_info: 0x1f4
+  __DATA_CONST.__auth_got: 0x2b8
+  __DATA_CONST.__got: 0x5e8
+  __DATA_CONST.__const: 0x570
+  __DATA_CONST.__cfstring: 0x360
   __DATA_CONST.__objc_classlist: 0x10
   __DATA_CONST.__objc_protolist: 0x30
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA.__objc_const: 0x12d8
-  __DATA.__objc_selrefs: 0x9b8
-  __DATA.__objc_classrefs: 0x1d0
+  __DATA.__objc_const: 0x1058
+  __DATA.__objc_selrefs: 0xa00
+  __DATA.__objc_classrefs: 0x1e0
   __DATA.__objc_superrefs: 0x10
-  __DATA.__objc_ivar: 0x58
+  __DATA.__objc_ivar: 0x50
   __DATA.__objc_data: 0xa0
   __DATA.__data: 0x240
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation

   - /System/Library/PrivateFrameworks/SpringBoardServices.framework/SpringBoardServices
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 122
-  Symbols:   340
-  CStrings:  610
+  Functions: 120
+  Symbols:   343
+  CStrings:  589
 
Symbols:
+ _OBJC_CLASS_$_NSInvocation
+ _OBJC_CLASS_$_NSJSONSerialization
+ _OBJC_CLASS_$_PKAddShareablePassConfiguration
+ _OBJC_CLASS_$_PKBankConnectTransactionsProvider
+ _OBJC_CLASS_$_PKLaunchAuthorizationPromptController
+ _OBJC_CLASS_$_PKPushProvisioningTarget
+ _OBJC_CLASS_$_PKShareablePassMetadata
+ _PKAddShareableConfigurationActionConfigurationParameter
+ _PKAddShareableConfigurationActionRoute
+ _PKAddShareableConfigurationActionTitleParameter
+ _PKStockholmEnvironmentIsLikelyProduction
+ _PKURLActionRouteIssuer
+ _PKURLRedirectURLQueryItemKey
+ _PKURLSubactionRouteAuthorization
- _OBJC_CLASS_$_CLLocationManager
- _OBJC_CLASS_$_NSNull
- _OBJC_CLASS_$_PKAsyncUnaryOperationComposer
- _OBJC_CLASS_$_PKNavigationController
- _OBJC_CLASS_$_PKUserNotificationAuthorizationExplanationViewController
- _dispatch_assert_queue$V2
- _objc_copyWeak
- _objc_destroyWeak
- _objc_initWeak
- _objc_loadWeakRetained
- _objc_release_x1
CStrings:
+ "\x02\x15\x11\x13"
+ "@\"PKLaunchAuthorizationPromptController\""
+ "Failed to addShareable route due to missing configuration"
+ "Failed to addShareable route due to no metadatas"
+ "Failed to handle BankConnect auth redirect. The redirectURL is nil!"
+ "Failed to parse raw provisioning target due to it not being a dictionary. \n %{public}@"
+ "Failed to retrieve pass for transaction with url %@"
+ "Failed to retrieve transaction with url %@"
+ "Handling addShareable route for url: %{public}@"
+ "Handling failed to deserialization addShareable json with error: %{public}@"
+ "JSONObjectWithData:options:error:"
+ "PKLaunchAuthorizationPromptDelegate"
+ "PKUserNotificationAuthorizationControllerDelegate"
+ "Transaction"
+ "_bankConnectAuthorizationRedirectURLFromPathComponents:queryItems:"
+ "_launchAuthorizationPromptController"
+ "_presentBankConnectAuthorizationViewControllerWithRedirectURL:"
+ "canPresentLaunchPrompts"
+ "containsString:"
+ "didReceiveAppAuthorizationRedirectToURL:"
+ "disableLaunchPromptsForSession"
+ "enableLaunchPromptsForSession"
+ "fulfillments"
+ "initWithContext:dataProvider:delegate:"
+ "initWithPrimaryAction:credentialsMetadata:"
+ "initWithProvisioningDict:"
+ "initWithPushProvisioningTarget:"
+ "instanceMethodSignatureForSelector:"
+ "invocationWithMethodSignature:"
+ "invokeWithTarget:"
+ "pk_decodeURLBase64"
+ "presentAddShareablePassConfiguration:animated:"
+ "presentAuthorizationFlowAnimated:completion:"
+ "presentLaunchPromptViewController:"
+ "presentLaunchPromptsForPassesIfNeeded:"
+ "presentTransactionDetailsForBankConnectTransaction:applePayPrimaryAccountIdentifier:"
+ "preview"
+ "returns"
+ "setArgument:atIndex:"
+ "setLocalizedDescription:"
+ "setSelector:"
+ "showReturnDetailsForOrderTypeIdentifier:orderIdentifier:returnIdentifier:sourceApplication:"
+ "transactionWithURL:completion:"
+ "v16@?0@\"UIViewController<FKBankConnectAuthorizationViewControllerProtocol>\"8"
+ "v24@0:8@\"UIViewController\"16"
+ "v24@?0@\"PKPaymentTransaction\"8@\"NSString\"16"
- "\x02\x16\x11\x11\x12"
- "@\"CLLocationManager\""
- "@\"PKUserNotificationAuthorizationExplanationViewController\""
- "B24@0:8@\"CLLocationManager\"16"
- "CLLocationManagerDelegate"
- "PKUserNotificationAuthorizationController: Skipping presentation due to other launch activity"
- "PKUserNotificationAuthorizationControllerDelgate"
- "Q"
- "Skipping notification TCC warming screen as other content is currently presented"
- "_disableLaunchPromptsForSession"
- "_enableLaunchPromptsForSession"
- "_requestManager"
- "_resetLaunchPromptsForNextSession"
- "_shouldShowLaunchPrompts"
- "_userNotificationAuthorizationViewController"
- "addOperation:"
- "authorizationStatus"
- "bundlePath"
- "evaluateWithInput:completion:"
- "initWithController:contentType:context:dataProvider:"
- "initWithEffectiveBundlePath:delegate:onQueue:"
- "initWithRootViewController:"
- "locationManager:didChangeAuthorizationStatus:"
- "locationManager:didDetermineState:forRegion:"
- "locationManager:didEnterRegion:"
- "locationManager:didExitRegion:"
- "locationManager:didFailRangingBeaconsForConstraint:error:"
- "locationManager:didFailWithError:"
- "locationManager:didFinishDeferredUpdatesWithError:"
- "locationManager:didRangeBeacons:inRegion:"
- "locationManager:didRangeBeacons:satisfyingConstraint:"
- "locationManager:didStartMonitoringForRegion:"
- "locationManager:didUpdateHeading:"
- "locationManager:didUpdateLocations:"
- "locationManager:didUpdateToLocation:fromLocation:"
- "locationManager:didVisit:"
- "locationManager:monitoringDidFailForRegion:withError:"
- "locationManager:rangingBeaconsDidFailForRegion:withError:"
- "locationManagerDidChangeAuthorization:"
- "locationManagerDidPauseLocationUpdates:"
- "locationManagerDidResumeLocationUpdates:"
- "locationManagerShouldDisplayHeadingCalibration:"
- "null"
- "requestWhenInUseAuthorization"
- "setNavigationBarHidden:"
- "setNextStepHandler:"
- "shouldOfferAuthorizationPromptWithPasses:completion:"
- "showDetailsForOrderTypeIdentifier:orderIdentifier:fulfillmentIdentifier:"
- "v20@?0B8Q12"
- "v24@0:8@\"CLLocationManager\"16"
- "v28@0:8@\"CLLocationManager\"16i24"
- "v28@0:8@16i24"
- "v28@?0B8@12@\"<PKCancelable>\"20"
- "v32@0:8@\"CLLocationManager\"16@\"CLHeading\"24"
- "v32@0:8@\"CLLocationManager\"16@\"CLRegion\"24"
- "v32@0:8@\"CLLocationManager\"16@\"CLVisit\"24"
- "v32@0:8@\"CLLocationManager\"16@\"NSArray\"24"
- "v32@0:8@\"CLLocationManager\"16@\"NSError\"24"
- "v32@?0@\"PKAsyncOperationState\"8@\"NSNull\"16@?<v@?@\"NSNull\"B>24"
- "v40@0:8@\"CLLocationManager\"16@\"CLBeaconIdentityConstraint\"24@\"NSError\"32"
- "v40@0:8@\"CLLocationManager\"16@\"CLBeaconRegion\"24@\"NSError\"32"
- "v40@0:8@\"CLLocationManager\"16@\"CLLocation\"24@\"CLLocation\"32"
- "v40@0:8@\"CLLocationManager\"16@\"CLRegion\"24@\"NSError\"32"
- "v40@0:8@\"CLLocationManager\"16@\"NSArray\"24@\"CLBeaconIdentityConstraint\"32"
- "v40@0:8@\"CLLocationManager\"16@\"NSArray\"24@\"CLBeaconRegion\"32"
- "v40@0:8@\"CLLocationManager\"16q24@\"CLRegion\"32"
- "v40@0:8@16q24@32"

```
