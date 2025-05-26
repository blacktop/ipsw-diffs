## NewDeviceOutreachUI

> `/System/Library/PrivateFrameworks/NewDeviceOutreachUI.framework/NewDeviceOutreachUI`

```diff

-407.8.0.0.0
-  __TEXT.__text: 0x19164
+407.15.0.0.0
+  __TEXT.__text: 0x18d60
   __TEXT.__auth_stubs: 0x560
-  __TEXT.__objc_methlist: 0x1284
+  __TEXT.__objc_methlist: 0x12ac
   __TEXT.__const: 0xa0
-  __TEXT.__cstring: 0x1ef9
-  __TEXT.__oslogstring: 0x12ee
-  __TEXT.__gcc_except_tab: 0x2ac
-  __TEXT.__unwind_info: 0x574
+  __TEXT.__cstring: 0x1f65
+  __TEXT.__oslogstring: 0x12fc
+  __TEXT.__gcc_except_tab: 0x2c4
+  __TEXT.__unwind_info: 0x578
   __TEXT.__objc_classname: 0x2d1
-  __TEXT.__objc_methname: 0x4cb6
-  __TEXT.__objc_methtype: 0xdf9
-  __TEXT.__objc_stubs: 0x44a0
+  __TEXT.__objc_methname: 0x4d84
+  __TEXT.__objc_methtype: 0xdfc
+  __TEXT.__objc_stubs: 0x44e0
   __DATA_CONST.__got: 0x100
-  __DATA_CONST.__const: 0x810
+  __DATA_CONST.__const: 0x860
   __DATA_CONST.__objc_classlist: 0x88
   __DATA_CONST.__objc_protolist: 0x50
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_const: 0x32e0
-  __DATA_CONST.__objc_selrefs: 0x13a0
+  __DATA_CONST.__objc_selrefs: 0x13b8
   __AUTH_CONST.__objc_const: 0x678
-  __AUTH_CONST.__cfstring: 0x11c0
+  __AUTH_CONST.__cfstring: 0x11a0
   __AUTH_CONST.__const: 0xe0
   __AUTH_CONST.__objc_intobj: 0x30
   __AUTH_CONST.__auth_got: 0x2c0

   - /System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 565
-  Symbols:   2293
-  CStrings:  1368
+  Functions: 557
+  Symbols:   2282
+  CStrings:  1370
 
Symbols:
+ -[NDOAppleCareAMSUIViewController initWithWarranty:serialNumber:source:url:purchaseBody:deeplinkParams:]
+ -[NDOCoverageCentralViewController handleDeviceListURL:withCompletion:]
+ -[NDOCoverageCentralViewController handleSummaryURL:withCompletion:]
+ -[NDOWarrantyInfoController shouldReloadSpecifiersOnResume]
+ GCC_except_table30
+ GCC_except_table34
+ GCC_except_table42
+ ___111-[NDOCoverageCentralViewController updateDeviceInfoForDevice:usingPolicy:params:forceUpdateFollowup:withReply:]_block_invoke_2.60
+ ___111-[NDOCoverageCentralViewController updateDeviceInfoForDevice:usingPolicy:params:forceUpdateFollowup:withReply:]_block_invoke_2.60.cold.1
+ ___47-[NDOWarrantyInfoController managePlanPressed:]_block_invoke.166
+ ___47-[NDOWarrantyInfoController managePlanPressed:]_block_invoke.168
+ ___62-[NDOCoverageCentralViewController completeWithStatus:params:]_block_invoke.170
+ ___62-[NDOCoverageCentralViewController completeWithStatus:params:]_block_invoke.178
+ ___68-[NDOCoverageCentralViewController handleSummaryURL:withCompletion:]_block_invoke
+ ___68-[NDOCoverageCentralViewController handleSummaryURL:withCompletion:]_block_invoke.78
+ ___68-[NDOCoverageCentralViewController handleSummaryURL:withCompletion:]_block_invoke.78.cold.1
+ ___68-[NDOCoverageCentralViewController handleSummaryURL:withCompletion:]_block_invoke.78.cold.2
+ ___71-[NDOCoverageCentralViewController handleDeviceListURL:withCompletion:]_block_invoke
+ ___71-[NDOCoverageCentralViewController handleDeviceListURL:withCompletion:]_block_invoke.63
+ ___71-[NDOCoverageCentralViewController handleDeviceListURL:withCompletion:]_block_invoke_2
+ ___86-[NDOWarrantyInfoController outreachFinishedForDeviceWithSerialNumber:withCompletion:]_block_invoke.193
+ ___86-[NDOWarrantyInfoController outreachFinishedForDeviceWithSerialNumber:withCompletion:]_block_invoke.201
+ ___86-[NDOWarrantyInfoController outreachFinishedForDeviceWithSerialNumber:withCompletion:]_block_invoke_2.202
+ ___96-[NDOWarrantyInfoController _refreshWithForcedNetworkPolicy:forceUpdateFollowup:withCompletion:]_block_invoke.74
+ ___96-[NDOWarrantyInfoController _refreshWithForcedNetworkPolicy:forceUpdateFollowup:withCompletion:]_block_invoke.78
+ ___block_descriptor_48_e8_32s40s_e43_v32?0"NSString"8"NSArray"16"NSString"24ls32l8s40l8
+ ___block_descriptor_48_e8_32s40w_e18_v16?0"NSString"8lw40l8s32l8
+ ___block_descriptor_56_e8_32s40s48bs_e23_v16?0"NDODeviceInfo"8ls32l8s40l8s48l8
+ ___block_descriptor_56_e8_32s40s48s_e5_v8?0ls32l8s40l8s48l8
+ ___block_descriptor_74_e8_32s40s48s56bs_e17_v16?0"NSArray"8ls32l8s40l8s48l8s56l8
+ ___block_descriptor_82_e8_32s40s48s56s64bs_e5_v8?0ls32l8s40l8s48l8s56l8s64l8
+ ___block_literal_global.171
+ ___block_literal_global.204
+ _objc_msgSend$getDeviceListForLocalDevices:sessionID:policy:params:salesReplyOnly:salesInfoReply:deviceInfoReply:completionBlock:
+ _objc_msgSend$handleDeviceListURL:withCompletion:
+ _objc_msgSend$handleSummaryURL:withCompletion:
+ _objc_msgSend$initWithWarranty:serialNumber:source:url:purchaseBody:deeplinkParams:
- -[NDOAppleCareAMSUIViewController initWithWarranty:serialNumber:source:url:purchaseBody:]
- -[NDOCoverageCentralViewController openAMSUIWithURL:httpBody:].cold.1
- -[NDOCoverageCentralViewController updateDeviceInfoForDevice:usingPolicy:params:forceUpdateFollowup:withReply:].cold.2
- -[NDOCoverageCentralViewController updateDeviceInfoForDevice:usingPolicy:params:forceUpdateFollowup:withReply:].cold.3
- -[NDOCoverageCentralViewController updateDeviceInfoForDevice:usingPolicy:params:forceUpdateFollowup:withReply:].cold.4
- -[NDOCoverageCentralViewController updateDeviceInfoForDevice:usingPolicy:params:forceUpdateFollowup:withReply:].cold.5
- GCC_except_table31
- GCC_except_table41
- _OUTLINED_FUNCTION_10
- ___111-[NDOCoverageCentralViewController updateDeviceInfoForDevice:usingPolicy:params:forceUpdateFollowup:withReply:]_block_invoke.59.cold.1
- ___111-[NDOCoverageCentralViewController updateDeviceInfoForDevice:usingPolicy:params:forceUpdateFollowup:withReply:]_block_invoke.59.cold.2
- ___111-[NDOCoverageCentralViewController updateDeviceInfoForDevice:usingPolicy:params:forceUpdateFollowup:withReply:]_block_invoke.59.cold.3
- ___111-[NDOCoverageCentralViewController updateDeviceInfoForDevice:usingPolicy:params:forceUpdateFollowup:withReply:]_block_invoke.63
- ___111-[NDOCoverageCentralViewController updateDeviceInfoForDevice:usingPolicy:params:forceUpdateFollowup:withReply:]_block_invoke.63.cold.1
- ___111-[NDOCoverageCentralViewController updateDeviceInfoForDevice:usingPolicy:params:forceUpdateFollowup:withReply:]_block_invoke.63.cold.2
- ___111-[NDOCoverageCentralViewController updateDeviceInfoForDevice:usingPolicy:params:forceUpdateFollowup:withReply:]_block_invoke.63.cold.3
- ___111-[NDOCoverageCentralViewController updateDeviceInfoForDevice:usingPolicy:params:forceUpdateFollowup:withReply:]_block_invoke.64
- ___111-[NDOCoverageCentralViewController updateDeviceInfoForDevice:usingPolicy:params:forceUpdateFollowup:withReply:]_block_invoke_2.65
- ___111-[NDOCoverageCentralViewController updateDeviceInfoForDevice:usingPolicy:params:forceUpdateFollowup:withReply:]_block_invoke_2.65.cold.1
- ___47-[NDOWarrantyInfoController managePlanPressed:]_block_invoke.165
- ___47-[NDOWarrantyInfoController managePlanPressed:]_block_invoke.167
- ___61-[NDOCoverageCentralViewController handleURL:withCompletion:]_block_invoke
- ___61-[NDOCoverageCentralViewController handleURL:withCompletion:]_block_invoke.74
- ___61-[NDOCoverageCentralViewController handleURL:withCompletion:]_block_invoke.74.cold.1
- ___61-[NDOCoverageCentralViewController handleURL:withCompletion:]_block_invoke.74.cold.2
- ___62-[NDOCoverageCentralViewController completeWithStatus:params:]_block_invoke.173
- ___62-[NDOCoverageCentralViewController completeWithStatus:params:]_block_invoke.181
- ___86-[NDOWarrantyInfoController outreachFinishedForDeviceWithSerialNumber:withCompletion:]_block_invoke.191
- ___86-[NDOWarrantyInfoController outreachFinishedForDeviceWithSerialNumber:withCompletion:]_block_invoke.200
- ___86-[NDOWarrantyInfoController outreachFinishedForDeviceWithSerialNumber:withCompletion:]_block_invoke_2.201
- ___96-[NDOWarrantyInfoController _refreshWithForcedNetworkPolicy:forceUpdateFollowup:withCompletion:]_block_invoke.75
- ___96-[NDOWarrantyInfoController _refreshWithForcedNetworkPolicy:forceUpdateFollowup:withCompletion:]_block_invoke_2
- ___block_descriptor_48_e8_32s40bs_e23_v16?0"NDODeviceInfo"8ls32l8s40l8
- ___block_descriptor_56_e8_32s40s48bs_e5_v8?0ls32l8s40l8s48l8
- ___block_descriptor_74_e8_32s40s48s56bs_e17_v16?0"NSArray"8ls32l8s56l8s40l8s48l8
- ___block_descriptor_82_e8_32s40s48s56s64bs_e5_v8?0ls32l8s40l8s64l8s48l8s56l8
- ___block_literal_global.170
- ___block_literal_global.203
- _objc_msgSend$initWithWarranty:serialNumber:source:url:purchaseBody:
- _objc_msgSend$specifierIDPendingPush
CStrings:
+ "%{public}s"
+ "%{public}s: isHostSettings == NO, setting specifier deviceInfo: %@"
+ "%{public}s: isHostSettings == YES, setting specifier deviceInfo: %@"
+ "%{public}s: localDevices: %@, params: %@"
+ "%{public}s: refresh completion: specifier: %@, deviceInfo: %@"
+ "%{public}s: url: %@, httpBody: %@, deeplinkParams: %@"
+ "-[NDOCoverageCentralViewController handleDeviceListURL:withCompletion:]"
+ "-[NDOCoverageCentralViewController handleDeviceListURL:withCompletion:]_block_invoke"
+ "-[NDOCoverageCentralViewController handleSummaryURL:withCompletion:]_block_invoke"
+ "-[NDOWarrantyInfoController _refreshWithForcedNetworkPolicy:forceUpdateFollowup:withCompletion:]_block_invoke"
+ "@64@0:8@16@24@32@40@48@56"
+ "getDeviceListForLocalDevices:sessionID:policy:params:salesReplyOnly:salesInfoReply:deviceInfoReply:completionBlock:"
+ "handleDeviceListURL:withCompletion:"
+ "handleSummaryURL:withCompletion:"
+ "initWithWarranty:serialNumber:source:url:purchaseBody:deeplinkParams:"
+ "shouldReloadSpecifiersOnResume"
+ "v32@?0@\"NSString\"8@\"NSArray\"16@\"NSString\"24"
- "%s: refreshing device list api"
- "%{public}s: Deferring"
- "%{public}s: called for sn: %@"
- "%{public}s: entering for sn: %@"
- "%{public}s: handling deferred url after ndo specifiers did load"
- "%{public}s: nil for secifier"
- "%{public}s: no device info"
- "%{public}s: updating deviceInfo: %@ for device sn: %@"
- "-[NDOCoverageCentralViewController handleURL:withCompletion:]_block_invoke"
- "-[NDOCoverageCentralViewController shouldDeferPushForSpecifierID:]"
- "-[NDOCoverageCentralViewController updateDeviceInfoForDevice:usingPolicy:params:forceUpdateFollowup:withReply:]_block_invoke"
- "@56@0:8@16@24@32@40@48"
- "WARRANTY_COVERAGE"
- "initWithWarranty:serialNumber:source:url:purchaseBody:"
- "specifierIDPendingPush"

```
