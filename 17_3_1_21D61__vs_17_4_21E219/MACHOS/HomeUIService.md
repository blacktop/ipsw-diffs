## HomeUIService

> `/Applications/HomeUIService.app/HomeUIService`

```diff

-841.4.10.1.1
-  __TEXT.__text: 0x5cd50
+873.5.8.1.5
+  __TEXT.__text: 0x5d0f8
   __TEXT.__auth_stubs: 0x750
   __TEXT.__objc_stubs: 0xdb20
-  __TEXT.__objc_methlist: 0x54c0
+  __TEXT.__objc_methlist: 0x5470
   __TEXT.__objc_methname: 0x13d98
-  __TEXT.__cstring: 0x73dc
+  __TEXT.__cstring: 0x73c8
   __TEXT.__objc_classname: 0x12f7
-  __TEXT.__objc_methtype: 0x3960
+  __TEXT.__objc_methtype: 0x3932
   __TEXT.__const: 0xc0
-  __TEXT.__oslogstring: 0x5cf0
+  __TEXT.__oslogstring: 0x5d76
   __TEXT.__gcc_except_tab: 0x858
   __TEXT.__dlopen_cstrs: 0x52
-  __TEXT.__unwind_info: 0x16a0
+  __TEXT.__unwind_info: 0x1688
   __DATA_CONST.__auth_got: 0x3b8
   __DATA_CONST.__got: 0x3b8
-  __DATA_CONST.__const: 0x2a58
+  __DATA_CONST.__const: 0x29b8
   __DATA_CONST.__cfstring: 0x3840
   __DATA_CONST.__objc_classlist: 0x378
   __DATA_CONST.__objc_catlist: 0x20
   __DATA_CONST.__objc_protolist: 0x190
   __DATA_CONST.__objc_imageinfo: 0x8
+  __DATA_CONST.__objc_protorefs: 0x20
+  __DATA_CONST.__objc_classrefs: 0x898
+  __DATA_CONST.__objc_superrefs: 0x320
   __DATA_CONST.__objc_intobj: 0xc48
   __DATA_CONST.__objc_doubleobj: 0x10
   __DATA_CONST.__objc_arraydata: 0xa0
   __DATA_CONST.__objc_arrayobj: 0x60
-  __DATA.__objc_const: 0xef48
-  __DATA.__objc_selrefs: 0x3ea8
-  __DATA.__objc_protorefs: 0x20
-  __DATA.__objc_classrefs: 0x898
-  __DATA.__objc_superrefs: 0x320
-  __DATA.__objc_ivar: 0x5fc
+  __DATA.__objc_const: 0xeee8
+  __DATA.__objc_selrefs: 0x3ea0
+  __DATA.__objc_ivar: 0x5f4
   __DATA.__objc_data: 0x22b0
   __DATA.__data: 0x12c0
   __DATA.__bss: 0xa8

   - /usr/lib/libMobileGestalt.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 6BD7BD7A-76DB-30F8-98DB-6DD36037A67C
-  Functions: 2272
+  UUID: 2D8EC9CD-9CE5-3781-BB2A-EA5A42131F06
+  Functions: 2270
   Symbols:   464
-  CStrings:  5074
+  CStrings:  5076
 
CStrings:
+ "(%@ : %s) %@ skipping %@ because hasWalletKeyCompatibleDevice is %{BOOL}d."
+ "(%@ :%s) Populating mica asset %@. error %@"
+ "(%@:%s) Authentication succeeded to enable express mode Tap to Unlock for currently existing Wallet Key with localAuthenticationContext %@"
+ "(%@:%s) Showing educational prox card about Wallet Key because shouldShowSingleContinueButton is YES"
+ "(HSSetupstateMachine:%s) Skipping express mode prox card because while adding accessory %@, wallet key already exists for %@"
+ "HSProximityCardWalletKeyExpressModeTapToUnlockSubtitle"
+ "HSProximityCardWalletKeyExpressModeTapToUnlockTitle"
+ "HSProximityCardWalletKeyExpressModeTapToUnlock_EnableTapToUnlockButton"
+ "HSProximityCardWalletKeyExpressModeTapToUnlock_ExpressModeAuthString"
+ "Not updating date added for %@ because it is already set to %@"
+ "T@\"NSString\",?,C,N"
+ "T@\"NSString\",?,R,C"
+ "T@\"UITextInputPasswordRules\",?,C,N"
+ "T@\"UIViewController\",?,&,N"
+ "T@\"UIViewController\",?,&,N,V_contentVC"
+ "T@\"UIWindow\",?,&,N"
+ "TB,?,N"
+ "TB,?,N,GisSecureTextEntry"
+ "TB,?,R,N"
+ "Tq,?,N"
+ "Tq,?,R,N"
+ "Updated date added for %@"
+ "Updating date added failed with %@ for %@"
+ "Updating date added to %@ for %@"
+ "configureAccessoryDateAdded"
+ "hf_dateAdded"
+ "hf_updateDateAdded:"
+ "home:didUpdateSupportsResidentActionSetStateEvaluation:"
+ "initWithCoordinator:configurationDelegate:"
+ "lazyFutureWithBlock:"
+ "rawSetupPayloadString"
- "(%@:%s) Authentication succeeded to enable express mode for currently existing Wallet Key with localAuthenticationContext %@"
- "(%@:%s) Showing educational prox card about Wallet Key because hasOnboardedForWalletKey is YES"
- "(HSPCWalletKeyExpressModeViewController :%s) Populating mica asset %@. error %@"
- "(HSSetupStateMachine : %s) %@ skipping %@ because there is at least one wallet key compatible device."
- "(HSSetupstateMachine:%s) Skipping express mode prox card because while adding accessory %@, hasWalletKey is YES"
- "@\"HMNetworkRouterProfile\""
- "@\"NSArray\"16@?0@\"HMAccessory\"8"
- "B16@?0@\"HMNetworkRouterProfile\"8"
- "HSProximityCardWalletKeyExpressModeSubtitle"
- "HSProximityCardWalletKeyExpressModeTitle"
- "HSProximityCardWalletKeyExpressMode_EnableExpressModeButton"
- "HSProximityCardWalletKeyExpressMode_ExpressModeAuthString"
- "T@\"HMNetworkRouterProfile\",R,N,V_profile"
- "T@\"UITextInputPasswordRules\",C,N"
- "T@\"UIViewController\",&,N"
- "T@\"UIViewController\",&,N,V_contentVC"
- "T@\"UIWindow\",&,N"
- "TB,N"
- "TB,N,GisSecureTextEntry"
- "Tq,N"
- "_presentAlertControllerWithTitle:message:style:actions:"
- "_primaryNetworkRouterProfileForProfiles:"
- "_profile"
- "allNetworkRouterProfiles"
- "hf_networkRouterProfiles"
- "initWithCoordinator:profile:configurationDelegate:"
- "isSatellite"
- "profile"
- "v48@0:8@16@24q32@40"

```
