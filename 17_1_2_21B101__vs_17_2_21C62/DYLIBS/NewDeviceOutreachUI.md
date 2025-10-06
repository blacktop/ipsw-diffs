## NewDeviceOutreachUI

> `/System/Library/PrivateFrameworks/NewDeviceOutreachUI.framework/NewDeviceOutreachUI`

```diff

-405.0.0.0.0
-  __TEXT.__text: 0x171ac
-  __TEXT.__auth_stubs: 0x550
-  __TEXT.__objc_methlist: 0x120c
+407.8.0.0.0
+  __TEXT.__text: 0x19164
+  __TEXT.__auth_stubs: 0x560
+  __TEXT.__objc_methlist: 0x1284
   __TEXT.__const: 0xa0
-  __TEXT.__cstring: 0x1882
-  __TEXT.__oslogstring: 0xf1e
+  __TEXT.__cstring: 0x1ef9
+  __TEXT.__oslogstring: 0x12ee
   __TEXT.__gcc_except_tab: 0x2ac
-  __TEXT.__unwind_info: 0x554
+  __TEXT.__unwind_info: 0x574
   __TEXT.__objc_classname: 0x2d1
-  __TEXT.__objc_methname: 0x4b72
+  __TEXT.__objc_methname: 0x4cb6
   __TEXT.__objc_methtype: 0xdf9
-  __TEXT.__objc_stubs: 0x42c0
-  __DATA_CONST.__got: 0xf8
-  __DATA_CONST.__const: 0x770
+  __TEXT.__objc_stubs: 0x44a0
+  __DATA_CONST.__got: 0x100
+  __DATA_CONST.__const: 0x810
   __DATA_CONST.__objc_classlist: 0x88
   __DATA_CONST.__objc_protolist: 0x50
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_const: 0x3280
-  __DATA_CONST.__objc_selrefs: 0x1340
+  __DATA_CONST.__objc_const: 0x32e0
+  __DATA_CONST.__objc_selrefs: 0x13a0
   __AUTH_CONST.__objc_const: 0x678
-  __AUTH_CONST.__cfstring: 0x1220
+  __AUTH_CONST.__cfstring: 0x11c0
   __AUTH_CONST.__const: 0xe0
   __AUTH_CONST.__objc_intobj: 0x30
-  __AUTH_CONST.__auth_got: 0x2b8
+  __AUTH_CONST.__auth_got: 0x2c0
   __AUTH.__objc_data: 0x550
-  __DATA.__objc_classrefs: 0x2a0
+  __DATA.__objc_classrefs: 0x2a8
   __DATA.__objc_superrefs: 0x80
-  __DATA.__objc_ivar: 0x194
+  __DATA.__objc_ivar: 0x19c
   __DATA.__data: 0x3c0
   __DATA.__bss: 0x18
   - /System/Library/Frameworks/Accounts.framework/Accounts

   - /System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 7F7D5DCE-4189-3D26-AC37-05032EDE76BE
-  Functions: 535
-  Symbols:   2204
-  CStrings:  1459
+  UUID: 2D315C5D-B8DF-39D0-9B44-49E7053FACFB
+  Functions: 565
+  Symbols:   2293
+  CStrings:  1510
 
Symbols:
+ -[NDOAppleCareViewController viewDidAppear:]
+ -[NDOCoverageCentralViewController _refresh:].cold.1
+ -[NDOCoverageCentralViewController allLocalDevices]
+ -[NDOCoverageCentralViewController deviceListAPISections]
+ -[NDOCoverageCentralViewController deviceLoadCompleted]
+ -[NDOCoverageCentralViewController fetchAllDeviceInfoUsingPolicy:sessionID:params:isSales:andForcePostFollowup:withReply:].cold.2
+ -[NDOCoverageCentralViewController fetchAllDeviceInfoUsingPolicy:sessionID:params:isSales:andForcePostFollowup:withReply:].cold.3
+ -[NDOCoverageCentralViewController fetchAllLocalDevices]
+ -[NDOCoverageCentralViewController fetchAllLocalDevices].cold.1
+ -[NDOCoverageCentralViewController fetchAllLocalDevices].cold.2
+ -[NDOCoverageCentralViewController getDeviceInfoForSerialNumber:usingPolicy:sessionID:params:andForcePostFollowup:withReply:].cold.1
+ -[NDOCoverageCentralViewController offerTextForDeviceInfo:]
+ -[NDOCoverageCentralViewController setAllLocalDevices:]
+ -[NDOCoverageCentralViewController setDeviceListAPISections:]
+ -[NDOCoverageCentralViewController setDeviceLoadCompleted:]
+ -[NDOCoverageCentralViewController shouldShowDeviceListUI]
+ -[NDOCoverageCentralViewController updateCells].cold.4
+ -[NDOCoverageCentralViewController updateCells].cold.5
+ -[NDOCoverageCentralViewController updateDeviceInfoForDevice:usingPolicy:params:forceUpdateFollowup:withReply:].cold.4
+ -[NDOCoverageCentralViewController updateDeviceInfoForDevice:usingPolicy:params:forceUpdateFollowup:withReply:].cold.5
+ -[NDOCoverageItemCell updateDeviceImage]
+ -[NDOWarrantyInfoController _errorStateConfig]
+ -[NDOWarrantyInfoController _noAccountConfig]
+ -[NDOWarrantyInfoController _refreshWithForcedNetworkPolicy:forceUpdateFollowup:withCompletion:].cold.1
+ -[NDOWarrantyInfoController _refreshWithForcedNetworkPolicy:forceUpdateFollowup:withCompletion:].cold.2
+ -[NDOWarrantyInfoController errorUI]
+ -[NDOWarrantyInfoController hideUI]
+ -[NDOWarrantyInfoController isSignedIn]
+ -[NDOWarrantyInfoController loadView].cold.1
+ -[NDOWarrantyInfoController previousAppSupportAvailabilityType]
+ -[NDOWarrantyInfoController setIsSignedIn:]
+ -[NDOWarrantyInfoController setPreviousAppSupportAvailabilityType:]
+ -[NDOWarrantyInfoController showUI]
+ GCC_except_table14
+ GCC_except_table18
+ GCC_except_table31
+ GCC_except_table41
+ _NDOCoverageItemCellCoverageLabelKey
+ _NDOCoverageItemCellFallbackImageKey
+ _NDOCoverageItemCellImageURLKey
+ _NDOCoverageItemCellOfferLabelKey
+ _NDODeviceKey
+ _OBJC_CLASS_$_NDOUtilities
+ _OBJC_CLASS_$_NSUserDefaults
+ _OBJC_IVAR_$_NDOCoverageCentralViewController._allLocalDevices
+ _OBJC_IVAR_$_NDOCoverageCentralViewController._deviceListAPISections
+ _OBJC_IVAR_$_NDOCoverageCentralViewController._deviceLoadCompleted
+ _OBJC_IVAR_$_NDOWarrantyInfoController._isSignedIn
+ _OBJC_IVAR_$_NDOWarrantyInfoController._previousAppSupportAvailabilityType
+ _OUTLINED_FUNCTION_10
+ _OUTLINED_FUNCTION_9
+ ___111-[NDOCoverageCentralViewController updateDeviceInfoForDevice:usingPolicy:params:forceUpdateFollowup:withReply:]_block_invoke.59
+ ___111-[NDOCoverageCentralViewController updateDeviceInfoForDevice:usingPolicy:params:forceUpdateFollowup:withReply:]_block_invoke.59.cold.1
+ ___111-[NDOCoverageCentralViewController updateDeviceInfoForDevice:usingPolicy:params:forceUpdateFollowup:withReply:]_block_invoke.59.cold.2
+ ___111-[NDOCoverageCentralViewController updateDeviceInfoForDevice:usingPolicy:params:forceUpdateFollowup:withReply:]_block_invoke.59.cold.3
+ ___111-[NDOCoverageCentralViewController updateDeviceInfoForDevice:usingPolicy:params:forceUpdateFollowup:withReply:]_block_invoke.63
+ ___111-[NDOCoverageCentralViewController updateDeviceInfoForDevice:usingPolicy:params:forceUpdateFollowup:withReply:]_block_invoke.63.cold.1
+ ___111-[NDOCoverageCentralViewController updateDeviceInfoForDevice:usingPolicy:params:forceUpdateFollowup:withReply:]_block_invoke.63.cold.2
+ ___111-[NDOCoverageCentralViewController updateDeviceInfoForDevice:usingPolicy:params:forceUpdateFollowup:withReply:]_block_invoke.63.cold.3
+ ___111-[NDOCoverageCentralViewController updateDeviceInfoForDevice:usingPolicy:params:forceUpdateFollowup:withReply:]_block_invoke.64
+ ___111-[NDOCoverageCentralViewController updateDeviceInfoForDevice:usingPolicy:params:forceUpdateFollowup:withReply:]_block_invoke_2.65
+ ___111-[NDOCoverageCentralViewController updateDeviceInfoForDevice:usingPolicy:params:forceUpdateFollowup:withReply:]_block_invoke_2.65.cold.1
+ ___120-[NDOCoverageCentralViewController getAllDeviceInfoUsingPolicy:sessionID:params:isSales:andForcePostFollowup:withReply:]_block_invoke.56
+ ___120-[NDOCoverageCentralViewController getAllDeviceInfoUsingPolicy:sessionID:params:isSales:andForcePostFollowup:withReply:]_block_invoke.57
+ ___120-[NDOCoverageCentralViewController getAllDeviceInfoUsingPolicy:sessionID:params:isSales:andForcePostFollowup:withReply:]_block_invoke.57.cold.1
+ ___120-[NDOCoverageCentralViewController getAllDeviceInfoUsingPolicy:sessionID:params:isSales:andForcePostFollowup:withReply:]_block_invoke.58
+ ___122-[NDOCoverageCentralViewController fetchAllDeviceInfoUsingPolicy:sessionID:params:isSales:andForcePostFollowup:withReply:]_block_invoke
+ ___122-[NDOCoverageCentralViewController fetchAllDeviceInfoUsingPolicy:sessionID:params:isSales:andForcePostFollowup:withReply:]_block_invoke_2
+ ___122-[NDOCoverageCentralViewController fetchAllDeviceInfoUsingPolicy:sessionID:params:isSales:andForcePostFollowup:withReply:]_block_invoke_2.cold.1
+ ___37-[NDOWarrantyInfoController loadView]_block_invoke_2
+ ___40-[NDOCoverageItemCell updateDeviceImage]_block_invoke
+ ___40-[NDOCoverageItemCell updateDeviceImage]_block_invoke.cold.1
+ ___44-[NDOAppleCareViewController viewDidAppear:]_block_invoke
+ ___46-[NDOWarrantyInfoController _errorStateConfig]_block_invoke
+ ___47-[NDOCoverageCentralViewController updateCells]_block_invoke
+ ___47-[NDOWarrantyInfoController managePlanPressed:]_block_invoke.165
+ ___47-[NDOWarrantyInfoController managePlanPressed:]_block_invoke.167
+ ___56-[NDOCoverageCentralViewController fetchAllLocalDevices]_block_invoke
+ ___61-[NDOCoverageCentralViewController handleURL:withCompletion:]_block_invoke.74
+ ___61-[NDOCoverageCentralViewController handleURL:withCompletion:]_block_invoke.74.cold.1
+ ___61-[NDOCoverageCentralViewController handleURL:withCompletion:]_block_invoke.74.cold.2
+ ___62-[NDOCoverageCentralViewController completeWithStatus:params:]_block_invoke.173
+ ___62-[NDOCoverageCentralViewController completeWithStatus:params:]_block_invoke.181
+ ___83-[NDOSpecifierDataSource outreachFinishedForDeviceWithSerialNumber:withCompletion:]_block_invoke.88
+ ___83-[NDOSpecifierDataSource outreachFinishedForDeviceWithSerialNumber:withCompletion:]_block_invoke.96
+ ___86-[NDOWarrantyInfoController outreachFinishedForDeviceWithSerialNumber:withCompletion:]_block_invoke.192
+ ___86-[NDOWarrantyInfoController outreachFinishedForDeviceWithSerialNumber:withCompletion:]_block_invoke.200
+ ___86-[NDOWarrantyInfoController outreachFinishedForDeviceWithSerialNumber:withCompletion:]_block_invoke_2.201
+ ___96-[NDOWarrantyInfoController _refreshWithForcedNetworkPolicy:forceUpdateFollowup:withCompletion:]_block_invoke.75
+ ___96-[NDOWarrantyInfoController _refreshWithForcedNetworkPolicy:forceUpdateFollowup:withCompletion:]_block_invoke.76
+ ___96-[NDOWarrantyInfoController _refreshWithForcedNetworkPolicy:forceUpdateFollowup:withCompletion:]_block_invoke.77
+ ___NSArray0__struct
+ ___block_descriptor_48_e8_32s40w_e29_v24?0"UIImage"8"NSError"16lw40l8s32l8
+ ___block_descriptor_56_e8_32s40s48s_e26_v32?0"NDODevice"8Q16^B24ls32l8s40l8s48l8
+ ___block_descriptor_74_e8_32s40s48s56bs_e17_v16?0"NSArray"8ls32l8s56l8s40l8s48l8
+ ___block_descriptor_82_e8_32s40s48s56s64bs_e5_v8?0ls32l8s40l8s64l8s48l8s56l8
+ ___block_literal_global.170
+ ___block_literal_global.203
+ _dispatch_after
+ _dispatch_time
+ _objc_msgSend$allLocalDevices
+ _objc_msgSend$boolForKey:
+ _objc_msgSend$deviceList
+ _objc_msgSend$deviceListAPISections
+ _objc_msgSend$deviceLoadCompleted
+ _objc_msgSend$errorUI
+ _objc_msgSend$fetchAllLocalDevices
+ _objc_msgSend$getDeviceListForLocalDevices:sessionID:completionBlock:
+ _objc_msgSend$groupSpecifierWithID:
+ _objc_msgSend$groupSpecifierWithID:name:
+ _objc_msgSend$hideUI
+ _objc_msgSend$isInternal
+ _objc_msgSend$label
+ _objc_msgSend$mutableCopy
+ _objc_msgSend$offerTextForDeviceInfo:
+ _objc_msgSend$previousAppSupportAvailabilityType
+ _objc_msgSend$setAllLocalDevices:
+ _objc_msgSend$setDeviceListAPISections:
+ _objc_msgSend$setDeviceLoadCompleted:
+ _objc_msgSend$setPreviousAppSupportAvailabilityType:
+ _objc_msgSend$sharedController
+ _objc_msgSend$shouldShowDeviceListUI
+ _objc_msgSend$sourceFromDeviceType
+ _objc_msgSend$standardUserDefaults
+ _objc_msgSend$updateDeviceImage
- -[NDOCoverageCentralViewController allDevices]
- -[NDOCoverageCentralViewController fetchAllDevices]
- -[NDOCoverageCentralViewController fetchAllDevices].cold.1
- -[NDOCoverageCentralViewController fetchAllDevices].cold.2
- -[NDOCoverageCentralViewController footerTapped:]
- -[NDOCoverageCentralViewController setAllDevices:]
- -[NDOCoverageItemCell refreshCellContentsWithSpecifier:].cold.1
- -[NDOCoverageItemCell updateDeviceImageWithDeviceInfo:]
- -[NDOCoverageItemCell updateOfferLabelForDeviceInfo:]
- -[NDOSpecifierDataSource coverageSpecifier]
- -[NDOSpecifierDataSource setCoverageSpecifier:]
- -[NDOWarrantyInfoController previousAppSupportAvailablabilityType]
- -[NDOWarrantyInfoController setPreviousAppSupportAvailablabilityType:]
- GCC_except_table11
- GCC_except_table40
- GCC_except_table8
- _OBJC_IVAR_$_NDOCoverageCentralViewController._allDevices
- _OBJC_IVAR_$_NDOSpecifierDataSource._coverageSpecifier
- _OBJC_IVAR_$_NDOWarrantyInfoController._previousAppSupportAvailablabilityType
- ___111-[NDOCoverageCentralViewController updateDeviceInfoForDevice:usingPolicy:params:forceUpdateFollowup:withReply:]_block_invoke.77
- ___111-[NDOCoverageCentralViewController updateDeviceInfoForDevice:usingPolicy:params:forceUpdateFollowup:withReply:]_block_invoke.77.cold.1
- ___111-[NDOCoverageCentralViewController updateDeviceInfoForDevice:usingPolicy:params:forceUpdateFollowup:withReply:]_block_invoke.77.cold.2
- ___111-[NDOCoverageCentralViewController updateDeviceInfoForDevice:usingPolicy:params:forceUpdateFollowup:withReply:]_block_invoke.77.cold.3
- ___111-[NDOCoverageCentralViewController updateDeviceInfoForDevice:usingPolicy:params:forceUpdateFollowup:withReply:]_block_invoke.81
- ___111-[NDOCoverageCentralViewController updateDeviceInfoForDevice:usingPolicy:params:forceUpdateFollowup:withReply:]_block_invoke.81.cold.1
- ___111-[NDOCoverageCentralViewController updateDeviceInfoForDevice:usingPolicy:params:forceUpdateFollowup:withReply:]_block_invoke.81.cold.2
- ___111-[NDOCoverageCentralViewController updateDeviceInfoForDevice:usingPolicy:params:forceUpdateFollowup:withReply:]_block_invoke.81.cold.3
- ___111-[NDOCoverageCentralViewController updateDeviceInfoForDevice:usingPolicy:params:forceUpdateFollowup:withReply:]_block_invoke.82
- ___111-[NDOCoverageCentralViewController updateDeviceInfoForDevice:usingPolicy:params:forceUpdateFollowup:withReply:]_block_invoke_2.83
- ___111-[NDOCoverageCentralViewController updateDeviceInfoForDevice:usingPolicy:params:forceUpdateFollowup:withReply:]_block_invoke_2.83.cold.1
- ___120-[NDOCoverageCentralViewController getAllDeviceInfoUsingPolicy:sessionID:params:isSales:andForcePostFollowup:withReply:]_block_invoke.73
- ___120-[NDOCoverageCentralViewController getAllDeviceInfoUsingPolicy:sessionID:params:isSales:andForcePostFollowup:withReply:]_block_invoke.74
- ___120-[NDOCoverageCentralViewController getAllDeviceInfoUsingPolicy:sessionID:params:isSales:andForcePostFollowup:withReply:]_block_invoke.74.cold.1
- ___120-[NDOCoverageCentralViewController getAllDeviceInfoUsingPolicy:sessionID:params:isSales:andForcePostFollowup:withReply:]_block_invoke.75
- ___47-[NDOWarrantyInfoController managePlanPressed:]_block_invoke.159
- ___47-[NDOWarrantyInfoController managePlanPressed:]_block_invoke.161
- ___51-[NDOCoverageCentralViewController fetchAllDevices]_block_invoke
- ___55-[NDOCoverageItemCell updateDeviceImageWithDeviceInfo:]_block_invoke
- ___55-[NDOCoverageItemCell updateDeviceImageWithDeviceInfo:]_block_invoke.cold.1
- ___61-[NDOCoverageCentralViewController handleURL:withCompletion:]_block_invoke.92
- ___61-[NDOCoverageCentralViewController handleURL:withCompletion:]_block_invoke.92.cold.1
- ___61-[NDOCoverageCentralViewController handleURL:withCompletion:]_block_invoke.92.cold.2
- ___62-[NDOCoverageCentralViewController completeWithStatus:params:]_block_invoke.190
- ___62-[NDOCoverageCentralViewController completeWithStatus:params:]_block_invoke.198
- ___83-[NDOSpecifierDataSource outreachFinishedForDeviceWithSerialNumber:withCompletion:]_block_invoke.112
- ___83-[NDOSpecifierDataSource outreachFinishedForDeviceWithSerialNumber:withCompletion:]_block_invoke.120
- ___86-[NDOWarrantyInfoController outreachFinishedForDeviceWithSerialNumber:withCompletion:]_block_invoke.199
- ___86-[NDOWarrantyInfoController outreachFinishedForDeviceWithSerialNumber:withCompletion:]_block_invoke_2.200
- ___86-[NDOWarrantyInfoController outreachFinishedForDeviceWithSerialNumber:withCompletion:]_block_invoke_3
- ___96-[NDOWarrantyInfoController _refreshWithForcedNetworkPolicy:forceUpdateFollowup:withCompletion:]_block_invoke_3
- ___96-[NDOWarrantyInfoController _refreshWithForcedNetworkPolicy:forceUpdateFollowup:withCompletion:]_block_invoke_4
- ___96-[NDOWarrantyInfoController _refreshWithForcedNetworkPolicy:forceUpdateFollowup:withCompletion:]_block_invoke_5
- ___block_descriptor_56_e8_32s40s48w_e29_v24?0"UIImage"8"NSError"16lw48l8s32l8s40l8
- ___block_literal_global.164
- ___block_literal_global.202
- _objc_msgSend$allDevices
- _objc_msgSend$coverageSpecifier
- _objc_msgSend$fetchAllDevices
- _objc_msgSend$previousAppSupportAvailablabilityType
- _objc_msgSend$reloadSpecifier:
- _objc_msgSend$setAllDevices:
- _objc_msgSend$setCoverageSpecifier:
- _objc_msgSend$setPreviousAppSupportAvailablabilityType:
- _objc_msgSend$updateDeviceImageWithDeviceInfo:
- _objc_msgSend$updateOfferLabelForDeviceInfo:
- _objc_retain_x7
CStrings:
+ "\x02\x11\x13"
+ "\x03+"
+ "%s: %@"
+ "%s: %@ action: %@"
+ "%s: AMS Body: %@"
+ "%s: AMS Headers: %@"
+ "%s: Beginning amsUI flow with URL: %@"
+ "%s: DONE updateNDOSpecifiersWithPolicy: %@"
+ "%s: DONE updateNDOSpecifiersWithPolicy: %@ with no datasource"
+ "%s: Failed to instatiate amsUI flow from: %@"
+ "%s: Skipping info fetch: not logged in."
+ "%s: Testing kNDOAppleCareViewControllerTestPurchase"
+ "%s: Using override AMSUI flow URL: %@"
+ "%s: initWithDefaultDevice: %d"
+ "%s: initWithSerialNumber: %@ %d"
+ "%s: no achostingController, cannot call forceUpdateSpecifiersAndForceUpdateFollowup:withCompletionHandler:"
+ "%s: no achostingController, cannot call updateSpecifiersWithCompletionHandler:"
+ "%s: no settingshostingController, cannot call updateDeviceInfoForDevice:usingPolicy:params:forceUpdateFollowup:withReply:"
+ "%s: refreshing device list api"
+ "%s: refreshing summary api"
+ "%s: specifiers: %@"
+ "%s: status: %ld"
+ "%s: status: %ld, params: %@"
+ "%s: status: %ld, params: %@, presentor: %@"
+ "%s: updateNDOSpecifiersWithPolicy: %@"
+ "%{public}s: Refreshing device info after purchase done"
+ "%{public}s: all local devices %@"
+ "%{public}s: cannot load warranty: no deviceInfo or device to make query"
+ "%{public}s: finished updating warranty"
+ "%{public}s: generating specifiers from device list api response"
+ "%{public}s: generating specifiers from local cache"
+ "%{public}s: getDeviceListForLocalDevices reply: %@"
+ "%{public}s: skipping fetch: not logged in"
+ "%{public}s: starting fetch"
+ "%{public}s: status: %lu, params: %@"
+ "-[NDOACController initWithSerialNumber:]"
+ "-[NDOAppleCareAMSUIViewController loadAMSUIView]"
+ "-[NDOAppleCareAMSUIViewController webViewController:handleDelegateAction:completion:]"
+ "-[NDOAppleCareViewController amsUIViewFinishedWithCompletion:]"
+ "-[NDOAppleCareViewController amsUIViewFinishedWithCompletion:params:]"
+ "-[NDOAppleCareViewController cancelPressed:]"
+ "-[NDOAppleCareViewController completeWithStatus:params:]"
+ "-[NDOAppleCareViewController getAppleCarePressed:]"
+ "-[NDOAppleCareViewController notNowPressed:]"
+ "-[NDOAppleCareViewController okButtonPressed]"
+ "-[NDOAppleCareViewController viewDidAppear:]"
+ "-[NDOAppleCareViewController webviewFinishedWithCompletion:]"
+ "-[NDOCoverageCentralViewController _refresh:]"
+ "-[NDOCoverageCentralViewController completeWithStatus:params:]"
+ "-[NDOCoverageCentralViewController fetchAllDeviceInfoUsingPolicy:sessionID:params:isSales:andForcePostFollowup:withReply:]_block_invoke_2"
+ "-[NDOCoverageCentralViewController fetchAllLocalDevices]"
+ "-[NDOCoverageCentralViewController getDeviceInfoForSerialNumber:usingPolicy:sessionID:params:andForcePostFollowup:withReply:]"
+ "-[NDOSpecifierDataSource initWithDefaultDevice:]"
+ "-[NDOSpecifierDataSource specifiersWithPolicy:completionHandler:]"
+ "-[NDOSpecifierDataSource specifiersWithPolicy:completionHandler:]_block_invoke"
+ "-[NDOSpecifierDataSource specifiersWithPolicy:completionHandler:]_block_invoke_3"
+ "-[NDOSpecifierDataSource updateNDOSpecifiersWithPolicy:completion:]"
+ "-[NDOSpecifierDataSource updateNDOSpecifiersWithPolicy:completion:]_block_invoke"
+ "-[NDOSpecifierDataSource updateNDOSpecifiersWithPolicy:completion:]_block_invoke_3"
+ "-[NDOWarrantyInfoController loadView]_block_invoke_2"
+ "-[NDOWarrantyInfoController ndoAppleCareCoveragePressed:]"
+ "-[NDOWarrantyInfoController outreachFinishedForDeviceWithSerialNumber:withCompletion:]"
+ "CC_FOOTER_APPLEID"
+ "NDOAppleCareViewControllerTestPurchase"
+ "NDOCoverageItemCellCoverageLabelKey"
+ "NDOCoverageItemCellFallbackImageKey"
+ "NDOCoverageItemCellImageURLKey"
+ "NDOCoverageItemCellOfferLabelKey"
+ "NDODevice"
+ "T@\"NSArray\",&,N,V_deviceListAPISections"
+ "T@\"NSMutableArray\",&,N,V_allLocalDevices"
+ "TB,N,V_deviceLoadCompleted"
+ "TB,N,V_isSignedIn"
+ "TQ,V_previousAppSupportAvailabilityType"
+ "_allLocalDevices"
+ "_deviceListAPISections"
+ "_deviceLoadCompleted"
+ "_previousAppSupportAvailabilityType"
+ "allLocalDevices"
+ "boolForKey:"
+ "deviceList"
+ "deviceListAPISections"
+ "deviceLoadCompleted"
+ "errorUI"
+ "fetchAllLocalDevices"
+ "getDeviceListForLocalDevices:sessionID:completionBlock:"
+ "groupSpecifierWithID:"
+ "groupSpecifierWithID:name:"
+ "hideUI"
+ "isInternal"
+ "mutableCopy"
+ "offerTextForDeviceInfo:"
+ "previousAppSupportAvailabilityType"
+ "setAllLocalDevices:"
+ "setDeviceListAPISections:"
+ "setDeviceLoadCompleted:"
+ "setPreviousAppSupportAvailabilityType:"
+ "shouldShowDeviceListUI"
+ "sourceFromDeviceType"
+ "standardUserDefaults"
+ "updateDeviceImage"
- "\x02\x11\x14"
- "\x03*"
- "\n"
- "%@ action: %@"
- "%s - %@"
- "%{public}s: all devices %@"
- "%{public}s: start fetching info"
- "-[NDOCoverageCentralViewController fetchAllDevices]"
- "-[NDOCoverageItemCell refreshCellContentsWithSpecifier:]"
- "-[NDOWarrantyInfoController outreachFinishedForDeviceWithSerialNumber:withCompletion:]_block_invoke_3"
- "AMS Body: %@"
- "AMS Headers: %@"
- "Begining amsUI flow with URL: %@"
- "CC_FOOTER_IPAD"
- "CC_FOOTER_IPHONE"
- "CC_FOOTER_LINK"
- "CC_FOOTER_VISIONPRO"
- "DEFAULT"
- "DONE updateNDOSpecifiersWithPolicy: %@"
- "DONE updateNDOSpecifiersWithPolicy: %@ with no datasource"
- "Failed to instatiate amsUI flow from: %@"
- "OTHER"
- "T@\"NSMutableArray\",&,N,V_allDevices"
- "T@\"PSSpecifier\",&,N,V_coverageSpecifier"
- "TQ,V_previousAppSupportAvailablabilityType"
- "Using override AMSUI flow URL: %@"
- "WATCH"
- "_allDevices"
- "_coverageSpecifier"
- "_previousAppSupportAvailablabilityType"
- "allDevices"
- "coverageSpecifier"
- "fetchAllDevices"
- "footerTapped:"
- "https://mysupport.apple.com"
- "initWithDefaultDevice: %d"
- "initWithSerialNumber: %@ %d"
- "previousAppSupportAvailablabilityType"
- "reloadSpecifier:"
- "setAllDevices:"
- "setCoverageSpecifier:"
- "setPreviousAppSupportAvailablabilityType:"
- "specifiersWithPolicy:completionHandler: %@"
- "updateDeviceImageWithDeviceInfo:"
- "updateNDOSpecifiersWithPolicy: %@"
- "updateOfferLabelForDeviceInfo:"

```
