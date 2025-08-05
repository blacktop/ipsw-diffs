## SIMSetupSupport

> `/System/Library/PrivateFrameworks/SIMSetupSupport.framework/SIMSetupSupport`

```diff

-862.0.0.0.0
-  __TEXT.__text: 0xab9d4
-  __TEXT.__auth_stubs: 0x830
-  __TEXT.__objc_methlist: 0x9954
+867.0.0.0.0
+  __TEXT.__text: 0xacbd8
+  __TEXT.__auth_stubs: 0x840
+  __TEXT.__objc_methlist: 0x9a14
   __TEXT.__const: 0x1b0
-  __TEXT.__gcc_except_tab: 0x1bf8
-  __TEXT.__cstring: 0xf37a
-  __TEXT.__oslogstring: 0x620a
+  __TEXT.__gcc_except_tab: 0x1c4c
+  __TEXT.__cstring: 0xf5a8
+  __TEXT.__oslogstring: 0x6331
   __TEXT.__dlopen_cstrs: 0x2be
   __TEXT.__ustring: 0xa
-  __TEXT.__unwind_info: 0x2430
-  __TEXT.__objc_classname: 0x14fd
-  __TEXT.__objc_methname: 0x15504
-  __TEXT.__objc_methtype: 0x350d
-  __TEXT.__objc_stubs: 0xda40
+  __TEXT.__unwind_info: 0x2440
+  __TEXT.__objc_classname: 0x1502
+  __TEXT.__objc_methname: 0x156a3
+  __TEXT.__objc_methtype: 0x3510
+  __TEXT.__objc_stubs: 0xdb40
   __DATA_CONST.__got: 0xa40
-  __DATA_CONST.__const: 0x1d10
+  __DATA_CONST.__const: 0x1d18
   __DATA_CONST.__objc_classlist: 0x460
   __DATA_CONST.__objc_catlist: 0x50
   __DATA_CONST.__objc_protolist: 0xf8
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x4df0
+  __DATA_CONST.__objc_selrefs: 0x4e38
   __DATA_CONST.__objc_protorefs: 0x10
   __DATA_CONST.__objc_superrefs: 0x400
   __DATA_CONST.__objc_arraydata: 0x38
-  __AUTH_CONST.__auth_got: 0x428
-  __AUTH_CONST.__const: 0x880
-  __AUTH_CONST.__cfstring: 0x70c0
-  __AUTH_CONST.__objc_const: 0x3b388
+  __AUTH_CONST.__auth_got: 0x430
+  __AUTH_CONST.__const: 0x860
+  __AUTH_CONST.__cfstring: 0x7220
+  __AUTH_CONST.__objc_const: 0x3b678
   __AUTH_CONST.__objc_intobj: 0x4e0
   __AUTH_CONST.__objc_dictobj: 0x28
   __AUTH_CONST.__objc_arrayobj: 0x48
   __AUTH.__objc_data: 0x2b70
-  __DATA.__objc_ivar: 0xdf8
+  __DATA.__objc_ivar: 0xe1c
   __DATA.__data: 0xbb0
   __DATA.__bss: 0x170
   __DATA_DIRTY.__objc_data: 0x50

   - /usr/lib/libMobileGestalt.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: AFCF5CF9-FCA5-3B7D-A5DE-B57DF9B089C4
-  Functions: 3712
-  Symbols:   13519
-  CStrings:  7112
+  UUID: BF8CEC45-D4CA-354C-BC01-FF8D4950EFE6
+  Functions: 3728
+  Symbols:   13574
+  CStrings:  7160
 
Symbols:
+ -[SSScanViewController _getCurrentDeviceOrientation]
+ -[TSPRXIdentityShareViewController continueAction]
+ -[TSPRXIdentityShareViewController setContinueAction:]
+ -[TSTransferListViewController _isAnyTransferPlanWithDirectAuth]
+ -[TSTransferListViewController _launchDirectAuthFlow:]
+ -[TSTransferListViewController _launchDirectAuthFlow:].cold.1
+ -[TSTransferListViewController _launchDirectAuthFlow:].cold.2
+ -[TSTransferListViewController isCarrierDirectAuthItemSelected]
+ -[TSTransferListViewController setIsCarrierDirectAuthItemSelected:]
+ -[TSTravelModeIntroViewController _skipButtonTapped:]
+ -[TSTravelModeIntroViewController initWithOptions:extractionSource:reduceEducation:arrivalCountry:]
+ -[TSTravelSimTypeSelectionViewController animating]
+ -[TSTravelSimTypeSelectionViewController cachedButtons]
+ -[TSTravelSimTypeSelectionViewController customizeSpinner]
+ -[TSTravelSimTypeSelectionViewController setAnimating:]
+ -[TSTravelSimTypeSelectionViewController setCachedButtons:]
+ -[TSTravelSimTypeSelectionViewController setSpinner:]
+ -[TSTravelSimTypeSelectionViewController setSpinnerContainer:]
+ -[TSTravelSimTypeSelectionViewController spinnerContainer]
+ -[TSTravelSimTypeSelectionViewController spinner]
+ GCC_except_table42
+ GCC_except_table44
+ GCC_except_table48
+ _AVCaptureSessionSetAuthorizedToUseCameraInMultipleForegroundAppLayout
+ _OBJC_IVAR_$_TSPRXIdentityShareViewController._continueAction
+ _OBJC_IVAR_$_TSTransferListViewController._isCarrierDirectAuthItemSelected
+ _OBJC_IVAR_$_TSTravelBuddyViewController._backFromNextPane
+ _OBJC_IVAR_$_TSTravelBuddyViewController._prevTravelOnlySelection
+ _OBJC_IVAR_$_TSTravelModeIntroViewController._isSourceThirdParty
+ _OBJC_IVAR_$_TSTravelSimTypeSelectionViewController._animating
+ _OBJC_IVAR_$_TSTravelSimTypeSelectionViewController._cachedButtons
+ _OBJC_IVAR_$_TSTravelSimTypeSelectionViewController._spinner
+ _OBJC_IVAR_$_TSTravelSimTypeSelectionViewController._spinnerContainer
+ _TSTravelArrivalCountry
+ ___115-[TSCellularPlanActivatingFlow(CoreTelephonyClientCellularPlanManagementDelegate) handleWaitingOnWifiStatusUpdate:]_block_invoke.498
+ ___39-[SSScanViewController decodeMetadata:]_block_invoke.50
+ ___47-[TSPRXIdentityShareViewController viewDidLoad]_block_invoke_4
+ ___53-[TSTransferListViewController _startPendingInstall:]_block_invoke.215
+ ___53-[TSTransferListViewController _startPendingInstall:]_block_invoke.217
+ ___53-[TSTransferListViewController _startPendingInstall:]_block_invoke_2.216
+ ___54-[TSTransferListViewController _launchDirectAuthFlow:]_block_invoke
+ ___54-[TSTransferListViewController _launchDirectAuthFlow:]_block_invoke.cold.1
+ ___56-[TSTravelBuddyViewController subscriptionInfoDidChange]_block_invoke
+ ___56-[TSTravelBuddyViewController subscriptionInfoDidChange]_block_invoke.cold.1
+ ___74-[TSCellularPlanActivatingFlow(TSSIMSetupDelegate) simSetupFlowCompleted:]_block_invoke.544
+ ___block_descriptor_48_e8_32s40w_e50_v24?0"CTXPCServiceSubscriptionInfo"8"NSError"16lw40l8s32l8
+ ___block_literal_global.122
+ ___block_literal_global.125
+ ___block_literal_global.219
+ ___block_literal_global.408
+ ___block_literal_global.497
+ ___block_literal_global.500
+ ___block_literal_global.678
+ ___block_literal_global.708
+ ___block_literal_global.768
+ _objc_msgSend$_getCurrentDeviceOrientation
+ _objc_msgSend$_isAnyTransferPlanWithDirectAuth
+ _objc_msgSend$_launchDirectAuthFlow:
+ _objc_msgSend$connection
+ _objc_msgSend$initWithOptions:extractionSource:reduceEducation:arrivalCountry:
+ _objc_msgSend$isAnyPlanTransferableFromThisDeviceForFlow:OrError:
+ _objc_msgSend$isCarrierDirectAuthItemSelected
+ _objc_msgSend$isVideoOrientationSupported
+ _objc_msgSend$previewLayer
+ _objc_msgSend$setVideoOrientation:
+ _objc_msgSend$transferEndpoint
- -[TSTransferListViewController _startPlanTransfer:withDeviceID:].cold.2
- -[TSTravelModeIntroViewController _cancelButtonTapped]
- -[TSTravelModeIntroViewController initWithOptions:extractionSource:reduceEducation:]
- GCC_except_table23
- GCC_except_table47
- ___115-[TSCellularPlanActivatingFlow(CoreTelephonyClientCellularPlanManagementDelegate) handleWaitingOnWifiStatusUpdate:]_block_invoke.497
- ___39-[SSScanViewController decodeMetadata:]_block_invoke.49
- ___53-[TSTransferListViewController _startPendingInstall:]_block_invoke.218
- ___53-[TSTransferListViewController _startPendingInstall:]_block_invoke.220
- ___53-[TSTransferListViewController _startPendingInstall:]_block_invoke_2.219
- ___57-[TSPRXIdentityShareViewController _successIdentityShare]_block_invoke
- ___57-[TSPRXIdentityShareViewController _successIdentityShare]_block_invoke_2
- ___62-[TSCellularSetupCompleteViewController _continueButtonTapped]_block_invoke
- ___62-[TSCellularSetupCompleteViewController _continueButtonTapped]_block_invoke.cold.1
- ___64-[TSTransferListViewController _startPlanTransfer:withDeviceID:]_block_invoke.203
- ___64-[TSTransferListViewController _startPlanTransfer:withDeviceID:]_block_invoke.cold.1
- ___74-[TSCellularPlanActivatingFlow(TSSIMSetupDelegate) simSetupFlowCompleted:]_block_invoke.543
- ___block_descriptor_40_e8_32bs_e41_v24?0"CTPlanTravelDetails"8"NSError"16ls32l8
- ___block_literal_global.123
- ___block_literal_global.222
- ___block_literal_global.406
- ___block_literal_global.496
- ___block_literal_global.499
- ___block_literal_global.672
- ___block_literal_global.702
- ___block_literal_global.762
- ___block_literal_global.83
- _objc_msgSend$initWithOptions:extractionSource:reduceEducation:
- _objc_msgSend$isAnyPlanTransferableFromThisDeviceOrError:
- _objc_msgSend$saveCellularSettingsForReturnToHome:
CStrings:
+ "-[TSTransferListViewController _launchDirectAuthFlow:]"
+ "-[TSTransferListViewController _launchDirectAuthFlow:]_block_invoke"
+ "-[TSTravelBuddyViewController subscriptionInfoDidChange]_block_invoke"
+ "-[TSTravelSimTypeSelectionViewController prepare:]_block_invoke"
+ "26.0"
+ "6"
+ "@48@0:8Q16@24Q32@40"
+ "CARRIER_TRANSFER_ERROR_CODE_MISSING_INFO_%@_%@"
+ "CROSSTRANSFER_SESSION_ERROR_CARRIER_NOT_SUPPORT"
+ "CROSSTRANSFER_SESSION_ERROR_CARRIER_NOT_SUPPORT_MSG"
+ "Found subscription context for (%@) @%s"
+ "Reset waitForPhoneNumber @%s"
+ "Same selection after tapping back from low data mode pane. @%s"
+ "Set plan item to (%@) @%s"
+ "Set waitForPhoneNumber to NO @%s"
+ "Siri"
+ "Subscription context UUID is not ready, continue waiting... @%s"
+ "T@\"PRXAction\",&,V_continueAction"
+ "TB,V_isCarrierDirectAuthItemSelected"
+ "TRAVEL_MODE_PRE_DEPARTURE_BODY_%@_%@"
+ "TRAVEL_MODE_PRE_DEPARTURE_BODY_THIRD_PARTY"
+ "TRAVEL_MODE_PRE_DEPARTURE_BODY_THIRD_PARTY_%@"
+ "TRAVEL_MODE_REDUCED_EDU_PRE_DEPARTURE_BODY_%@_%@"
+ "TRAVEL_MODE_REDUCED_EDU_PRE_DEPARTURE_BODY_THIRD_PARTY"
+ "TRAVEL_MODE_REDUCED_EDU_PRE_DEPARTURE_BODY_THIRD_PARTY_%@"
+ "User is in dual SIM config (non travel SIM) @%s"
+ "[E]not carrier direct item : %s @%s"
+ "_backFromNextPane"
+ "_continueAction"
+ "_getCurrentDeviceOrientation"
+ "_isAnyTransferPlanWithDirectAuth"
+ "_isCarrierDirectAuthItemSelected"
+ "_isSourceThirdParty"
+ "_launchDirectAuthFlow:"
+ "_prevTravelOnlySelection"
+ "arrivalCountry"
+ "connection"
+ "continueAction"
+ "initWithOptions:extractionSource:reduceEducation:arrivalCountry:"
+ "isAnyPlanTransferableFromThisDeviceForFlow:OrError:"
+ "isCarrierDirectAuthItemSelected"
+ "isVideoOrientationSupported"
+ "setContinueAction:"
+ "setIsCarrierDirectAuthItemSelected:"
+ "setVideoOrientation:"
+ "subscriptionInfoDidChange @%s"
+ "\xa1"
- "-[TSCellularSetupCompleteViewController _continueButtonTapped]_block_invoke"
- "-[TSTransferListViewController _startPlanTransfer:withDeviceID:]_block_invoke"
- "19.0"
- "5"
- "@40@0:8Q16@24Q32"
- "User is in dual SIM config @%s"
- "[E]Faile to save cellular settings: %@ @%s"
- "initWithOptions:extractionSource:reduceEducation:"
- "isAnyPlanTransferableFromThisDeviceOrError:"
- "saveCellularSettingsForReturnToHome:"

```
