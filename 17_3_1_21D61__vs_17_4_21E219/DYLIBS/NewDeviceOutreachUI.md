## NewDeviceOutreachUI

> `/System/Library/PrivateFrameworks/NewDeviceOutreachUI.framework/NewDeviceOutreachUI`

```diff

-407.15.0.0.0
-  __TEXT.__text: 0x18d60
-  __TEXT.__auth_stubs: 0x560
+407.17.0.0.0
+  __TEXT.__text: 0x184f0
+  __TEXT.__auth_stubs: 0x570
   __TEXT.__objc_methlist: 0x12ac
   __TEXT.__const: 0xa0
-  __TEXT.__cstring: 0x1f65
-  __TEXT.__oslogstring: 0x12fc
-  __TEXT.__gcc_except_tab: 0x2c4
-  __TEXT.__unwind_info: 0x578
+  __TEXT.__cstring: 0x1eb0
+  __TEXT.__oslogstring: 0x12c7
+  __TEXT.__gcc_except_tab: 0x2b0
+  __TEXT.__unwind_info: 0x560
   __TEXT.__objc_classname: 0x2d1
-  __TEXT.__objc_methname: 0x4d84
+  __TEXT.__objc_methname: 0x4da0
   __TEXT.__objc_methtype: 0xdfc
-  __TEXT.__objc_stubs: 0x44e0
+  __TEXT.__objc_stubs: 0x44a0
   __DATA_CONST.__got: 0x100
-  __DATA_CONST.__const: 0x860
+  __DATA_CONST.__const: 0x818
   __DATA_CONST.__objc_classlist: 0x88
   __DATA_CONST.__objc_protolist: 0x50
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_const: 0x32e0
-  __DATA_CONST.__objc_selrefs: 0x13b8
+  __DATA_CONST.__objc_const: 0x3310
+  __DATA_CONST.__objc_selrefs: 0x13b0
+  __DATA_CONST.__objc_classrefs: 0x2b0
+  __DATA_CONST.__objc_superrefs: 0x80
   __AUTH_CONST.__objc_const: 0x678
-  __AUTH_CONST.__cfstring: 0x11a0
+  __AUTH_CONST.__cfstring: 0x10c0
   __AUTH_CONST.__const: 0xe0
   __AUTH_CONST.__objc_intobj: 0x30
-  __AUTH_CONST.__auth_got: 0x2c0
+  __AUTH_CONST.__auth_got: 0x2c8
   __AUTH.__objc_data: 0x550
-  __DATA.__objc_classrefs: 0x2a8
-  __DATA.__objc_superrefs: 0x80
-  __DATA.__objc_ivar: 0x19c
+  __DATA.__objc_ivar: 0x1a0
   __DATA.__data: 0x3c0
   __DATA.__bss: 0x18
   - /System/Library/Frameworks/Accounts.framework/Accounts

   - /System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 557
-  Symbols:   2282
-  CStrings:  1370
+  Functions: 556
+  Symbols:   2279
+  CStrings:  1362
 
Symbols:
+ -[NDOCoverageCentralViewController expectingLink]
+ -[NDOCoverageCentralViewController handlePurchaseCompleted]
+ -[NDOCoverageCentralViewController handlePurchaseCompleted].cold.1
+ -[NDOCoverageCentralViewController setExpectingLink:]
+ -[NDOCoverageCentralViewController shouldDeferPushForSpecifierID:].cold.1
+ GCC_except_table16
+ GCC_except_table31
+ _NDOPurchaseCompletedNotification
+ _OBJC_CLASS_$_NSNotificationCenter
+ _OBJC_IVAR_$_NDOCoverageCentralViewController._expectingLink
+ _OUTLINED_FUNCTION_10
+ ___111-[NDOCoverageCentralViewController updateDeviceInfoForDevice:usingPolicy:params:forceUpdateFollowup:withReply:]_block_invoke.71
+ ___111-[NDOCoverageCentralViewController updateDeviceInfoForDevice:usingPolicy:params:forceUpdateFollowup:withReply:]_block_invoke_2.72
+ ___111-[NDOCoverageCentralViewController updateDeviceInfoForDevice:usingPolicy:params:forceUpdateFollowup:withReply:]_block_invoke_2.72.cold.1
+ ___120-[NDOCoverageCentralViewController getAllDeviceInfoUsingPolicy:sessionID:params:isSales:andForcePostFollowup:withReply:]_block_invoke.68
+ ___120-[NDOCoverageCentralViewController getAllDeviceInfoUsingPolicy:sessionID:params:isSales:andForcePostFollowup:withReply:]_block_invoke.69
+ ___120-[NDOCoverageCentralViewController getAllDeviceInfoUsingPolicy:sessionID:params:isSales:andForcePostFollowup:withReply:]_block_invoke.69.cold.1
+ ___120-[NDOCoverageCentralViewController getAllDeviceInfoUsingPolicy:sessionID:params:isSales:andForcePostFollowup:withReply:]_block_invoke.70
+ ___122-[NDOCoverageCentralViewController fetchAllDeviceInfoUsingPolicy:sessionID:params:isSales:andForcePostFollowup:withReply:]_block_invoke.62
+ ___122-[NDOCoverageCentralViewController fetchAllDeviceInfoUsingPolicy:sessionID:params:isSales:andForcePostFollowup:withReply:]_block_invoke_2.63
+ ___122-[NDOCoverageCentralViewController fetchAllDeviceInfoUsingPolicy:sessionID:params:isSales:andForcePostFollowup:withReply:]_block_invoke_2.63.cold.1
+ ___47-[NDOWarrantyInfoController managePlanPressed:]_block_invoke.169
+ ___47-[NDOWarrantyInfoController managePlanPressed:]_block_invoke.171
+ ___61-[NDOCoverageCentralViewController handleURL:withCompletion:]_block_invoke
+ ___61-[NDOCoverageCentralViewController handleURL:withCompletion:]_block_invoke.81
+ ___62-[NDOCoverageCentralViewController completeWithStatus:params:]_block_invoke.144
+ ___62-[NDOCoverageCentralViewController completeWithStatus:params:]_block_invoke.152
+ ___86-[NDOWarrantyInfoController outreachFinishedForDeviceWithSerialNumber:withCompletion:]_block_invoke.195
+ ___86-[NDOWarrantyInfoController outreachFinishedForDeviceWithSerialNumber:withCompletion:]_block_invoke.197
+ ___86-[NDOWarrantyInfoController outreachFinishedForDeviceWithSerialNumber:withCompletion:]_block_invoke.205
+ ___86-[NDOWarrantyInfoController outreachFinishedForDeviceWithSerialNumber:withCompletion:]_block_invoke_2.206
+ ___96-[NDOWarrantyInfoController _refreshWithForcedNetworkPolicy:forceUpdateFollowup:withCompletion:]_block_invoke.79
+ ___96-[NDOWarrantyInfoController _refreshWithForcedNetworkPolicy:forceUpdateFollowup:withCompletion:]_block_invoke.80
+ ___96-[NDOWarrantyInfoController _refreshWithForcedNetworkPolicy:forceUpdateFollowup:withCompletion:]_block_invoke.81
+ ___block_descriptor_56_e8_32s40s48bs_e17_v16?0"NSArray"8ls32l8s48l8s40l8
+ ___block_descriptor_64_e8_32s40s48s56s_e5_v8?0ls32l8s40l8s48l8s56l8
+ ___block_literal_global.174
+ ___block_literal_global.208
+ _objc_msgSend$UTF8String
+ _objc_msgSend$addObserver:selector:name:object:
+ _objc_msgSend$defaultCenter
+ _objc_msgSend$expectingLink
+ _objc_msgSend$postNotificationName:object:
+ _objc_msgSend$setAccessibilityLabel:
+ _objc_msgSend$setExpectingLink:
+ _objc_retainAutorelease
- -[NDOCoverageCentralViewController _getDevicePayloadWithParams:]
- -[NDOCoverageCentralViewController handleDeviceListURL:withCompletion:]
- -[NDOCoverageCentralViewController handleSummaryURL:withCompletion:]
- GCC_except_table14
- GCC_except_table30
- GCC_except_table34
- ___111-[NDOCoverageCentralViewController updateDeviceInfoForDevice:usingPolicy:params:forceUpdateFollowup:withReply:]_block_invoke.59
- ___111-[NDOCoverageCentralViewController updateDeviceInfoForDevice:usingPolicy:params:forceUpdateFollowup:withReply:]_block_invoke_2.60
- ___111-[NDOCoverageCentralViewController updateDeviceInfoForDevice:usingPolicy:params:forceUpdateFollowup:withReply:]_block_invoke_2.60.cold.1
- ___120-[NDOCoverageCentralViewController getAllDeviceInfoUsingPolicy:sessionID:params:isSales:andForcePostFollowup:withReply:]_block_invoke.56
- ___120-[NDOCoverageCentralViewController getAllDeviceInfoUsingPolicy:sessionID:params:isSales:andForcePostFollowup:withReply:]_block_invoke.57
- ___120-[NDOCoverageCentralViewController getAllDeviceInfoUsingPolicy:sessionID:params:isSales:andForcePostFollowup:withReply:]_block_invoke.57.cold.1
- ___120-[NDOCoverageCentralViewController getAllDeviceInfoUsingPolicy:sessionID:params:isSales:andForcePostFollowup:withReply:]_block_invoke.58
- ___122-[NDOCoverageCentralViewController fetchAllDeviceInfoUsingPolicy:sessionID:params:isSales:andForcePostFollowup:withReply:]_block_invoke_2.cold.1
- ___47-[NDOWarrantyInfoController managePlanPressed:]_block_invoke.166
- ___47-[NDOWarrantyInfoController managePlanPressed:]_block_invoke.168
- ___62-[NDOCoverageCentralViewController completeWithStatus:params:]_block_invoke.170
- ___62-[NDOCoverageCentralViewController completeWithStatus:params:]_block_invoke.178
- ___64-[NDOCoverageCentralViewController _getDevicePayloadWithParams:]_block_invoke
- ___68-[NDOCoverageCentralViewController handleSummaryURL:withCompletion:]_block_invoke
- ___68-[NDOCoverageCentralViewController handleSummaryURL:withCompletion:]_block_invoke.78
- ___68-[NDOCoverageCentralViewController handleSummaryURL:withCompletion:]_block_invoke.78.cold.1
- ___68-[NDOCoverageCentralViewController handleSummaryURL:withCompletion:]_block_invoke.78.cold.2
- ___71-[NDOCoverageCentralViewController handleDeviceListURL:withCompletion:]_block_invoke
- ___71-[NDOCoverageCentralViewController handleDeviceListURL:withCompletion:]_block_invoke.63
- ___71-[NDOCoverageCentralViewController handleDeviceListURL:withCompletion:]_block_invoke_2
- ___86-[NDOWarrantyInfoController outreachFinishedForDeviceWithSerialNumber:withCompletion:]_block_invoke.192
- ___86-[NDOWarrantyInfoController outreachFinishedForDeviceWithSerialNumber:withCompletion:]_block_invoke.193
- ___86-[NDOWarrantyInfoController outreachFinishedForDeviceWithSerialNumber:withCompletion:]_block_invoke.201
- ___86-[NDOWarrantyInfoController outreachFinishedForDeviceWithSerialNumber:withCompletion:]_block_invoke_2.202
- ___96-[NDOWarrantyInfoController _refreshWithForcedNetworkPolicy:forceUpdateFollowup:withCompletion:]_block_invoke.74
- ___96-[NDOWarrantyInfoController _refreshWithForcedNetworkPolicy:forceUpdateFollowup:withCompletion:]_block_invoke.76
- ___96-[NDOWarrantyInfoController _refreshWithForcedNetworkPolicy:forceUpdateFollowup:withCompletion:]_block_invoke.78
- ___block_descriptor_48_e8_32s40s_e26_v32?0"NDODevice"8Q16^B24ls32l8s40l8
- ___block_descriptor_48_e8_32s40w_e18_v16?0"NSString"8lw40l8s32l8
- ___block_descriptor_56_e8_32s40s48s_e5_v8?0ls32l8s40l8s48l8
- ___block_descriptor_73_e8_32s40s48s56s64bs_e17_v16?0"NSArray"8ls32l8s40l8s48l8s64l8s56l8
- ___block_literal_global.171
- ___block_literal_global.204
- _objc_msgSend$_getDevicePayloadWithParams:
- _objc_msgSend$deviceDesc
- _objc_msgSend$getDeviceListForLocalDevices:sessionID:completionBlock:
- _objc_msgSend$handleDeviceListURL:withCompletion:
- _objc_msgSend$handleSummaryURL:withCompletion:
- _objc_msgSend$parentId
- _objc_msgSend$pfcId
- _objc_msgSend$pgfId
- _objc_msgSend$sgId
CStrings:
+ "%@\n%@"
+ "%@\n%@\n%@"
+ "%{public}s: NDOACControllerKey: %@ expectingLink:%d"
+ "%{public}s: amsui payload: %@"
+ "%{public}s: params:%{public}s isSales:%{public}d"
+ "-[NDOCoverageCentralViewController handlePurchaseCompleted]"
+ "-[NDOCoverageCentralViewController handleURL:withCompletion:]_block_invoke"
+ "-[NDOCoverageCentralViewController shouldDeferPushForSpecifierID:]"
+ "NDOPurchaseCompletedNotification"
+ "T@\"NSString\",?,R,C"
+ "TB,V_expectingLink"
+ "UTF8String"
+ "_expectingLink"
+ "addObserver:selector:name:object:"
+ "defaultCenter"
+ "expectingLink"
+ "handlePurchaseCompleted"
+ "postNotificationName:object:"
+ "setAccessibilityLabel:"
+ "setExpectingLink:"
- "%{public}s: Missing UL sales url."
- "%{public}s: No warranties found. Not showing purchase ui."
- "%{public}s: localDevices: %@, params: %@"
- "%{public}s: payload: %@"
- "%{public}s: sn: %@ sn2: %@"
- "-[NDOCoverageCentralViewController _getDevicePayloadWithParams:]_block_invoke"
- "-[NDOCoverageCentralViewController handleDeviceListURL:withCompletion:]"
- "-[NDOCoverageCentralViewController handleDeviceListURL:withCompletion:]_block_invoke"
- "-[NDOCoverageCentralViewController handleSummaryURL:withCompletion:]_block_invoke"
- "_getDevicePayloadWithParams:"
- "deviceDesc"
- "deviceName"
- "eligibilityRemainingInDays"
- "getDeviceListForLocalDevices:sessionID:completionBlock:"
- "handleDeviceListURL:withCompletion:"
- "handleSummaryURL:withCompletion:"
- "parentId"
- "pfcId"
- "pgfId"
- "serialNum"
- "sgId"

```
