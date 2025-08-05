## DigitalSeparationUI

> `/System/Library/PrivateFrameworks/DigitalSeparationUI.framework/DigitalSeparationUI`

```diff

-574.0.0.0.0
-  __TEXT.__text: 0x54274
+579.0.0.0.0
+  __TEXT.__text: 0x5395c
   __TEXT.__auth_stubs: 0xfe0
-  __TEXT.__objc_methlist: 0x50c8
-  __TEXT.__cstring: 0x4401
+  __TEXT.__objc_methlist: 0x5088
+  __TEXT.__cstring: 0x43f1
   __TEXT.__const: 0x704
   __TEXT.__gcc_except_tab: 0x710
   __TEXT.__oslogstring: 0x273e

   __TEXT.__swift_as_entry: 0x6c
   __TEXT.__swift_as_ret: 0x8c
   __TEXT.__swift5_assocty: 0x50
-  __TEXT.__unwind_info: 0x1630
+  __TEXT.__unwind_info: 0x15f8
   __TEXT.__eh_frame: 0xbf8
   __TEXT.__objc_classname: 0x968
-  __TEXT.__objc_methname: 0xd974
-  __TEXT.__objc_methtype: 0x28f0
-  __TEXT.__objc_stubs: 0x9d00
+  __TEXT.__objc_methname: 0xd89d
+  __TEXT.__objc_methtype: 0x28ec
+  __TEXT.__objc_stubs: 0x9be0
   __DATA_CONST.__got: 0x8a0
-  __DATA_CONST.__const: 0x10f0
+  __DATA_CONST.__const: 0x1078
   __DATA_CONST.__objc_classlist: 0x1d8
   __DATA_CONST.__objc_catlist: 0x38
   __DATA_CONST.__objc_protolist: 0xf0
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x33f0
+  __DATA_CONST.__objc_selrefs: 0x33b0
   __DATA_CONST.__objc_protorefs: 0x8
   __DATA_CONST.__objc_superrefs: 0x190
   __DATA_CONST.__objc_arraydata: 0xa0
   __AUTH_CONST.__auth_got: 0x800
   __AUTH_CONST.__const: 0x1008
   __AUTH_CONST.__cfstring: 0x4600
-  __AUTH_CONST.__objc_const: 0x10440
+  __AUTH_CONST.__objc_const: 0x10490
   __AUTH_CONST.__objc_dictobj: 0xf0
   __AUTH_CONST.__objc_intobj: 0x1f8
   __AUTH.__objc_data: 0x11e8

   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  UUID: 59203107-692F-3AF1-8A7A-0682C6D9A13A
-  Functions: 2198
-  Symbols:   6834
-  CStrings:  3898
+  UUID: 051719FB-73B8-3DB7-8BAE-D38A32FB2859
+  Functions: 2180
+  Symbols:   6788
+  CStrings:  3889
 
Symbols:
+ +[DSIconFactory detailIconForContact:]
+ +[DSIconFactory iconWithSize:contact:]
+ +[DSIconFactory tableIconForContact:]
+ -[DSBlockingPermissionsController tableIconForPerson:]
+ -[DSSharingPermissionsController tableIconForPerson:]
+ -[DSSharingPerson(DigitalSeparationUI) iconForDetail]
+ -[DSSharingPerson(DigitalSeparationUI) iconForTable]
+ -[DSXPCSharingPerson(DigitalSeparationUI) iconForDetail]
+ -[DSXPCSharingPerson(DigitalSeparationUI) iconForTable]
+ GCC_except_table16
+ __OBJC_$_PROP_LIST_DSSharingPerson_$_DigitalSeparationUI
+ __OBJC_$_PROP_LIST_DSXPCSharingPerson_$_DigitalSeparationUI
+ ___38-[DSTouchIDController beginEnrollment]_block_invoke.346
+ ___43-[DSFaceIDController beginFaceIDEnrollment]_block_invoke.397
+ ___43-[DSFaceIDController beginFaceIDEnrollment]_block_invoke_2.402
+ ___44-[DSEmergencyResetController safetyResetAll]_block_invoke.405
+ ___44-[DSEmergencyResetController safetyResetAll]_block_invoke.409
+ ___46-[DSPrivateRelayController turnOnPrivateRelay]_block_invoke.340
+ ___47-[DSPasscodePopupViewController _applyPasscode]_block_invoke.391
+ ___47-[DSPasscodePopupViewController _applyPasscode]_block_invoke.391.cold.1
+ ___47-[DSPasscodePopupViewController _applyPasscode]_block_invoke.392
+ ___47-[DSPasscodePopupViewController _applyPasscode]_block_invoke.392.cold.1
+ ___47-[DSPasscodePopupViewController _applyPasscode]_block_invoke.393
+ ___51-[DSContinuityController getDevicesWithCompletion:]_block_invoke.368
+ ___51-[DSEmergencySOSController gatherEmergencyContacts]_block_invoke.389
+ ___51-[DSEmergencySOSController gatherEmergencyContacts]_block_invoke.389.cold.1
+ ___51-[DSEmergencySOSController gatherEmergencyContacts]_block_invoke.393
+ ___51-[DSNavigationController authToReturnToSafetyCheck]_block_invoke.490
+ ___51-[DSNavigationController authToReturnToSafetyCheck]_block_invoke.490.cold.1
+ ___51-[DSNavigationController authToReturnToSafetyCheck]_block_invoke.491
+ ___53-[DSPrivateRelayController shouldShowWithCompletion:]_block_invoke.316
+ ___53-[DSPrivateRelayController shouldShowWithCompletion:]_block_invoke.316.cold.1
+ ___53-[DSPrivateRelayController shouldShowWithCompletion:]_block_invoke.317
+ ___53-[DSPrivateRelayController shouldShowWithCompletion:]_block_invoke.317.cold.1
+ ___53-[DSPrivateRelayController shouldShowWithCompletion:]_block_invoke.318
+ ___53-[DSPrivateRelayController shouldShowWithCompletion:]_block_invoke.318.cold.1
+ ___58-[DSBlockingPermissionsController selectAndStopAllSharing]_block_invoke.348
+ ___58-[DSWifiSyncController returnFromDetailAndRemoveComputer:]_block_invoke.411
+ ___61-[DSAlternateDeviceAccessManager performFetchWithCompletion:]_block_invoke.308
+ ___61-[DSAlternateDeviceAccessManager performFetchWithCompletion:]_block_invoke.308.cold.1
+ ___61-[DSEmergencyResetController initializeEmergencyResetActions]_block_invoke.352
+ ___61-[DSEmergencyResetController initializeEmergencyResetActions]_block_invoke.357
+ ___61-[DSEmergencyResetController initializeEmergencyResetActions]_block_invoke.362
+ ___61-[DSEmergencyResetController initializeEmergencyResetActions]_block_invoke.367
+ ___61-[DSEmergencyResetController initializeEmergencyResetActions]_block_invoke.373
+ ___61-[DSEmergencyResetController initializeEmergencyResetActions]_block_invoke.378
+ ___61-[DSEmergencyResetController initializeEmergencyResetActions]_block_invoke.383
+ ___61-[DSEmergencyResetController initializeEmergencyResetActions]_block_invoke.388
+ ___61-[DSEmergencyResetController initializeEmergencyResetActions]_block_invoke.393
+ ___61-[DSEmergencyResetController initializeEmergencyResetActions]_block_invoke.399
+ ___61-[DSEmergencyResetController initializeEmergencyResetActions]_block_invoke_2.361
+ ___61-[DSEmergencyResetController initializeEmergencyResetActions]_block_invoke_2.366
+ ___61-[DSEmergencyResetController initializeEmergencyResetActions]_block_invoke_2.371
+ ___61-[DSEmergencyResetController initializeEmergencyResetActions]_block_invoke_2.377
+ ___61-[DSEmergencyResetController initializeEmergencyResetActions]_block_invoke_2.382
+ ___61-[DSEmergencyResetController initializeEmergencyResetActions]_block_invoke_2.384
+ ___61-[DSEmergencyResetController initializeEmergencyResetActions]_block_invoke_2.392
+ ___61-[DSEmergencyResetController initializeEmergencyResetActions]_block_invoke_2.394
+ ___61-[DSEmergencyResetController initializeEmergencyResetActions]_block_invoke_2.400
+ ___61-[DSEmergencyResetController initializeEmergencyResetActions]_block_invoke_3.398
+ ___61-[DSWifiSyncController removeAllPairedDevicesAndPushNextPane]_block_invoke.341
+ ___62-[DSCompletedController fetchAdditionalSharingWithCompletion:]_block_invoke.424
+ ___62-[DSCompletedController fetchAdditionalSharingWithCompletion:]_block_invoke.424.cold.1
+ ___62-[DSCompletedController fetchAdditionalSharingWithCompletion:]_block_invoke.426
+ ___64-[DSBlockingPermissionsDetailController _stopFindMyPushNextPane]_block_invoke.393
+ ___66-[DSEmergencySOSController emergencyContactFlow:didSelectContact:]_block_invoke.424
+ ___66-[DSWifiSyncController removeSelectedPairedDevicesAndPushNextPane]_block_invoke.388
+ ___70-[DSAlternateDeviceAccessManager resetAllAccessMethodsWithCompletion:]_block_invoke.315
+ ___70-[DSAlternateDeviceAccessManager resetAllAccessMethodsWithCompletion:]_block_invoke.315.cold.1
+ ___70-[DSAlternateDeviceAccessManager resetAllAccessMethodsWithCompletion:]_block_invoke.316
+ ___77-[DSPublicResourceSharingController stopSharingTypes:alertLabel:alertDetail:]_block_invoke.340
+ ___77-[DSPublicResourceSharingController stopSharingTypes:alertLabel:alertDetail:]_block_invoke.340.cold.1
+ ___77-[DSPublicResourceSharingController stopSharingTypes:alertLabel:alertDetail:]_block_invoke.342
+ ___83+[DSSafetyCheck showHSA2UpgradeWithPresentingViewController:safetyCheckController:]_block_invoke.431
+ ___83+[DSSafetyCheck showHSA2UpgradeWithPresentingViewController:safetyCheckController:]_block_invoke_2.434
+ ___86+[DSSafetyCheck authForSafetyCheckWithPresentingViewController:safetyCheckController:]_block_invoke.358
+ ___block_literal_global.313
+ ___block_literal_global.329
+ ___block_literal_global.333
+ ___block_literal_global.345
+ ___block_literal_global.349
+ ___block_literal_global.353
+ ___block_literal_global.360
+ ___block_literal_global.365
+ ___block_literal_global.373
+ ___block_literal_global.384
+ ___block_literal_global.389
+ ___block_literal_global.393
+ ___block_literal_global.400
+ ___block_literal_global.410
+ ___block_literal_global.412
+ ___block_literal_global.421
+ ___block_literal_global.426
+ ___block_literal_global.436
+ ___block_literal_global.483
+ ___block_literal_global.493
+ _objc_msgSend$avatarImageForContacts:scope:
+ _objc_msgSend$detailIconForContact:
+ _objc_msgSend$iconWithSize:contact:
+ _objc_msgSend$tableIconForContact:
+ _objc_msgSend$tableIconForPerson:
- +[DSIconFactory detailIconForContact:completion:]
- +[DSIconFactory iconWithSize:contact:completion:]
- +[DSIconFactory tableIconForContact:completion:]
- -[DSBlockingPermissionsController setTableIconForPerson:forCell:]
- -[DSBlockingPermissionsDetailController _setUpHeaderViewIcon]
- -[DSDeviceManager iconForDevice:]
- -[DSReadOnlyResourceSharingDetailController _setUpHeaderViewIcon]
- -[DSSharingPermissionsController cellForPerson:]
- -[DSSharingPermissionsController setTableIconForPerson:forCell:]
- -[DSSharingPermissionsDetailController _setUpHeaderViewIcon]
- -[DSSharingPermissionsDetailController cellForPerson:detailText:]
- -[DSSharingPerson(DigitalSeparationUI) detailIconWithCompletion:]
- -[DSSharingPerson(DigitalSeparationUI) tableIconWithCompletion:]
- -[DSXPCSharingPerson(DigitalSeparationUI) detailIconWithCompletion:]
- -[DSXPCSharingPerson(DigitalSeparationUI) tableIconWithCompletion:]
- GCC_except_table17
- GCC_except_table20
- GCC_except_table26
- ___38-[DSTouchIDController beginEnrollment]_block_invoke.343
- ___43-[DSFaceIDController beginFaceIDEnrollment]_block_invoke.394
- ___43-[DSFaceIDController beginFaceIDEnrollment]_block_invoke_2.399
- ___44-[DSEmergencyResetController safetyResetAll]_block_invoke.402
- ___44-[DSEmergencyResetController safetyResetAll]_block_invoke.406
- ___46-[DSPrivateRelayController turnOnPrivateRelay]_block_invoke.337
- ___47-[DSPasscodePopupViewController _applyPasscode]_block_invoke.388
- ___47-[DSPasscodePopupViewController _applyPasscode]_block_invoke.388.cold.1
- ___47-[DSPasscodePopupViewController _applyPasscode]_block_invoke.389
- ___47-[DSPasscodePopupViewController _applyPasscode]_block_invoke.389.cold.1
- ___47-[DSPasscodePopupViewController _applyPasscode]_block_invoke.390
- ___49+[DSIconFactory iconWithSize:contact:completion:]_block_invoke
- ___49+[DSIconFactory iconWithSize:contact:completion:]_block_invoke_2
- ___51-[DSContinuityController getDevicesWithCompletion:]_block_invoke.365
- ___51-[DSEmergencySOSController gatherEmergencyContacts]_block_invoke.386
- ___51-[DSEmergencySOSController gatherEmergencyContacts]_block_invoke.386.cold.1
- ___51-[DSEmergencySOSController gatherEmergencyContacts]_block_invoke.390
- ___51-[DSNavigationController authToReturnToSafetyCheck]_block_invoke.487
- ___51-[DSNavigationController authToReturnToSafetyCheck]_block_invoke.487.cold.1
- ___51-[DSNavigationController authToReturnToSafetyCheck]_block_invoke.488
- ___53-[DSPrivateRelayController shouldShowWithCompletion:]_block_invoke.313
- ___53-[DSPrivateRelayController shouldShowWithCompletion:]_block_invoke.313.cold.1
- ___53-[DSPrivateRelayController shouldShowWithCompletion:]_block_invoke.314
- ___53-[DSPrivateRelayController shouldShowWithCompletion:]_block_invoke.314.cold.1
- ___53-[DSPrivateRelayController shouldShowWithCompletion:]_block_invoke.315
- ___53-[DSPrivateRelayController shouldShowWithCompletion:]_block_invoke.315.cold.1
- ___58-[DSBlockingPermissionsController selectAndStopAllSharing]_block_invoke.345
- ___58-[DSWifiSyncController returnFromDetailAndRemoveComputer:]_block_invoke.408
- ___60-[DSSharingPermissionsDetailController _setUpHeaderViewIcon]_block_invoke
- ___61-[DSAlternateDeviceAccessManager performFetchWithCompletion:]_block_invoke.305
- ___61-[DSAlternateDeviceAccessManager performFetchWithCompletion:]_block_invoke.305.cold.1
- ___61-[DSBlockingPermissionsDetailController _setUpHeaderViewIcon]_block_invoke
- ___61-[DSEmergencyResetController initializeEmergencyResetActions]_block_invoke.349
- ___61-[DSEmergencyResetController initializeEmergencyResetActions]_block_invoke.354
- ___61-[DSEmergencyResetController initializeEmergencyResetActions]_block_invoke.359
- ___61-[DSEmergencyResetController initializeEmergencyResetActions]_block_invoke.364
- ___61-[DSEmergencyResetController initializeEmergencyResetActions]_block_invoke.370
- ___61-[DSEmergencyResetController initializeEmergencyResetActions]_block_invoke.375
- ___61-[DSEmergencyResetController initializeEmergencyResetActions]_block_invoke.380
- ___61-[DSEmergencyResetController initializeEmergencyResetActions]_block_invoke.385
- ___61-[DSEmergencyResetController initializeEmergencyResetActions]_block_invoke.390
- ___61-[DSEmergencyResetController initializeEmergencyResetActions]_block_invoke.396
- ___61-[DSEmergencyResetController initializeEmergencyResetActions]_block_invoke_2.358
- ___61-[DSEmergencyResetController initializeEmergencyResetActions]_block_invoke_2.363
- ___61-[DSEmergencyResetController initializeEmergencyResetActions]_block_invoke_2.368
- ___61-[DSEmergencyResetController initializeEmergencyResetActions]_block_invoke_2.374
- ___61-[DSEmergencyResetController initializeEmergencyResetActions]_block_invoke_2.379
- ___61-[DSEmergencyResetController initializeEmergencyResetActions]_block_invoke_2.381
- ___61-[DSEmergencyResetController initializeEmergencyResetActions]_block_invoke_2.389
- ___61-[DSEmergencyResetController initializeEmergencyResetActions]_block_invoke_2.391
- ___61-[DSEmergencyResetController initializeEmergencyResetActions]_block_invoke_2.397
- ___61-[DSEmergencyResetController initializeEmergencyResetActions]_block_invoke_3.395
- ___61-[DSWifiSyncController removeAllPairedDevicesAndPushNextPane]_block_invoke.338
- ___62-[DSCompletedController fetchAdditionalSharingWithCompletion:]_block_invoke.421
- ___62-[DSCompletedController fetchAdditionalSharingWithCompletion:]_block_invoke.421.cold.1
- ___62-[DSCompletedController fetchAdditionalSharingWithCompletion:]_block_invoke.423
- ___64-[DSBlockingPermissionsDetailController _stopFindMyPushNextPane]_block_invoke.391
- ___64-[DSSharingPermissionsController setTableIconForPerson:forCell:]_block_invoke
- ___64-[DSSharingPermissionsController setTableIconForPerson:forCell:]_block_invoke_2
- ___65-[DSBlockingPermissionsController setTableIconForPerson:forCell:]_block_invoke
- ___65-[DSBlockingPermissionsController setTableIconForPerson:forCell:]_block_invoke_2
- ___65-[DSReadOnlyResourceSharingDetailController _setUpHeaderViewIcon]_block_invoke
- ___65-[DSSharingPermissionsDetailController cellForPerson:detailText:]_block_invoke
- ___66-[DSEmergencySOSController emergencyContactFlow:didSelectContact:]_block_invoke.421
- ___66-[DSWifiSyncController removeSelectedPairedDevicesAndPushNextPane]_block_invoke.385
- ___70-[DSAlternateDeviceAccessManager resetAllAccessMethodsWithCompletion:]_block_invoke.312
- ___70-[DSAlternateDeviceAccessManager resetAllAccessMethodsWithCompletion:]_block_invoke.312.cold.1
- ___70-[DSAlternateDeviceAccessManager resetAllAccessMethodsWithCompletion:]_block_invoke.313
- ___71-[DSReadOnlyResourceSharingController tableView:cellForRowAtIndexPath:]_block_invoke
- ___77-[DSPublicResourceSharingController stopSharingTypes:alertLabel:alertDetail:]_block_invoke.337
- ___77-[DSPublicResourceSharingController stopSharingTypes:alertLabel:alertDetail:]_block_invoke.337.cold.1
- ___77-[DSPublicResourceSharingController stopSharingTypes:alertLabel:alertDetail:]_block_invoke.339
- ___77-[DSReadOnlyResourceSharingDetailController tableView:cellForRowAtIndexPath:]_block_invoke
- ___83+[DSSafetyCheck showHSA2UpgradeWithPresentingViewController:safetyCheckController:]_block_invoke.428
- ___83+[DSSafetyCheck showHSA2UpgradeWithPresentingViewController:safetyCheckController:]_block_invoke_2.431
- ___86+[DSSafetyCheck authForSafetyCheckWithPresentingViewController:safetyCheckController:]_block_invoke.352
- ___block_descriptor_40_e8_32bs_e17_v16?0"UIImage"8ls32l8
- ___block_descriptor_40_e8_32s_e17_v16?0"UIImage"8ls32l8
- ___block_descriptor_56_e8_32s40s48s_e17_v16?0"UIImage"8ls32l8s40l8s48l8
- ___block_literal_global.310
- ___block_literal_global.326
- ___block_literal_global.330
- ___block_literal_global.342
- ___block_literal_global.346
- ___block_literal_global.347
- ___block_literal_global.357
- ___block_literal_global.362
- ___block_literal_global.370
- ___block_literal_global.381
- ___block_literal_global.383
- ___block_literal_global.390
- ___block_literal_global.397
- ___block_literal_global.407
- ___block_literal_global.409
- ___block_literal_global.418
- ___block_literal_global.423
- ___block_literal_global.430
- ___block_literal_global.480
- ___block_literal_global.490
- _objc_msgSend$_setUpHeaderViewIcon
- _objc_msgSend$cellForPerson:
- _objc_msgSend$cellForPerson:detailText:
- _objc_msgSend$detailIconForContact:completion:
- _objc_msgSend$detailIconWithCompletion:
- _objc_msgSend$deviceImage
- _objc_msgSend$iconForDevice:
- _objc_msgSend$iconWithSize:contact:completion:
- _objc_msgSend$renderAvatarsForContacts:scope:imageHandler:
- _objc_msgSend$setDeviceImage:
- _objc_msgSend$setIcon:
- _objc_msgSend$setTableIconForPerson:forCell:
- _objc_msgSend$tableIconForContact:completion:
- _objc_msgSend$tableIconWithCompletion:
CStrings:
+ "@28@0:8f16@20"
+ "avatarImageForContacts:scope:"
+ "detailIconForContact:"
+ "iconWithSize:contact:"
+ "tableIconForContact:"
+ "tableIconForPerson:"
- "_setUpHeaderViewIcon"
- "cellForPerson:"
- "cellForPerson:detailText:"
- "detailIconForContact:completion:"
- "detailIconWithCompletion:"
- "deviceImage"
- "iconForDevice:"
- "iconWithSize:contact:completion:"
- "renderAvatarsForContacts:scope:imageHandler:"
- "setDeviceImage:"
- "setTableIconForPerson:forCell:"
- "tableIconForContact:completion:"
- "tableIconWithCompletion:"
- "v16@?0@\"UIImage\"8"
- "v36@0:8f16@20@?28"

```
