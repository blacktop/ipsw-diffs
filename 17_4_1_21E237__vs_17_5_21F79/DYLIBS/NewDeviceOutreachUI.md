## NewDeviceOutreachUI

> `/System/Library/PrivateFrameworks/NewDeviceOutreachUI.framework/NewDeviceOutreachUI`

```diff

-407.17.0.0.0
-  __TEXT.__text: 0x184f0
-  __TEXT.__auth_stubs: 0x570
-  __TEXT.__objc_methlist: 0x12ac
-  __TEXT.__const: 0xa0
-  __TEXT.__cstring: 0x1eb0
-  __TEXT.__oslogstring: 0x12c7
-  __TEXT.__gcc_except_tab: 0x2b0
+407.25.0.0.0
+  __TEXT.__text: 0x183b0
+  __TEXT.__auth_stubs: 0x540
+  __TEXT.__objc_methlist: 0x1268
+  __TEXT.__const: 0x88
+  __TEXT.__cstring: 0x1f0f
+  __TEXT.__oslogstring: 0x12fb
+  __TEXT.__gcc_except_tab: 0x2d0
   __TEXT.__unwind_info: 0x560
-  __TEXT.__objc_classname: 0x2d1
-  __TEXT.__objc_methname: 0x4da0
-  __TEXT.__objc_methtype: 0xdfc
-  __TEXT.__objc_stubs: 0x44a0
+  __TEXT.__objc_classname: 0x2ab
+  __TEXT.__objc_methname: 0x4d80
+  __TEXT.__objc_methtype: 0xe17
+  __TEXT.__objc_stubs: 0x4420
   __DATA_CONST.__got: 0x100
-  __DATA_CONST.__const: 0x818
-  __DATA_CONST.__objc_classlist: 0x88
+  __DATA_CONST.__const: 0x7f0
+  __DATA_CONST.__objc_classlist: 0x78
   __DATA_CONST.__objc_protolist: 0x50
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_const: 0x3310
-  __DATA_CONST.__objc_selrefs: 0x13b0
-  __DATA_CONST.__objc_classrefs: 0x2b0
-  __DATA_CONST.__objc_superrefs: 0x80
-  __AUTH_CONST.__objc_const: 0x678
+  __DATA_CONST.__objc_const: 0x3210
+  __DATA_CONST.__objc_selrefs: 0x1378
+  __DATA_CONST.__objc_classrefs: 0x2a8
+  __DATA_CONST.__objc_superrefs: 0x78
   __AUTH_CONST.__cfstring: 0x10c0
-  __AUTH_CONST.__const: 0xe0
+  __AUTH_CONST.__objc_const: 0x5e8
+  __AUTH_CONST.__const: 0x100
   __AUTH_CONST.__objc_intobj: 0x30
-  __AUTH_CONST.__auth_got: 0x2c8
-  __AUTH.__objc_data: 0x550
-  __DATA.__objc_ivar: 0x1a0
+  __AUTH_CONST.__auth_got: 0x2b0
+  __AUTH.__objc_data: 0x460
+  __DATA.__objc_ivar: 0x198
   __DATA.__data: 0x3c0
-  __DATA.__bss: 0x18
+  __DATA.__bss: 0x20
+  __DATA_DIRTY.__objc_data: 0x50
   - /System/Library/Frameworks/Accounts.framework/Accounts
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/CoreGraphics.framework/CoreGraphics

   - /System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 556
-  Symbols:   2279
-  CStrings:  1362
+  Functions: 552
+  Symbols:   2250
+  CStrings:  1354
 
Symbols:
+ -[NDOCoverageCentralViewController _refreshAndForcePostFollowUp:refreshControlToStop:]
+ -[NDOCoverageCentralViewController _refreshAndForcePostFollowUp:refreshControlToStop:].cold.1
+ -[NDOCoverageCentralViewController dismissAMSUI]
+ -[NDOCoverageCentralViewController initWithIsSignedIn:deviceManager:]
+ -[NDOCoverageCentralViewController initWithIsSignedIn:deviceManager:].cold.1
+ -[NDOCoverageCentralViewController offerTextForDevice:]
+ GCC_except_table29
+ GCC_except_table33
+ GCC_except_table56
+ ___35+[NDOACController sharedController]_block_invoke
+ ___47-[NDOWarrantyInfoController managePlanPressed:]_block_invoke.170
+ ___47-[NDOWarrantyInfoController managePlanPressed:]_block_invoke.172
+ ___48-[NDOCoverageCentralViewController dismissAMSUI]_block_invoke
+ ___62-[NDOCoverageCentralViewController completeWithStatus:params:]_block_invoke.151
+ ___86-[NDOCoverageCentralViewController _refreshAndForcePostFollowUp:refreshControlToStop:]_block_invoke
+ ___86-[NDOWarrantyInfoController outreachFinishedForDeviceWithSerialNumber:withCompletion:]_block_invoke.196
+ ___86-[NDOWarrantyInfoController outreachFinishedForDeviceWithSerialNumber:withCompletion:]_block_invoke.198
+ ___86-[NDOWarrantyInfoController outreachFinishedForDeviceWithSerialNumber:withCompletion:]_block_invoke.206
+ ___86-[NDOWarrantyInfoController outreachFinishedForDeviceWithSerialNumber:withCompletion:]_block_invoke_2.207
+ ___96-[NDOWarrantyInfoController _refreshWithForcedNetworkPolicy:forceUpdateFollowup:withCompletion:]_block_invoke.78
+ ___96-[NDOWarrantyInfoController _refreshWithForcedNetworkPolicy:forceUpdateFollowup:withCompletion:]_block_invoke.82
+ ___block_descriptor_40_e8_32w_e23_v16?0"NDODeviceInfo"8lw32l8
+ ___block_descriptor_40_e8_32w_e5_v8?0lw32l8
+ ___block_descriptor_48_e8_32s40bs_e17_v16?0"NSArray"8ls32l8s40l8
+ ___block_descriptor_56_e8_32s40s48bs_e5_v8?0ls32l8s40l8s48l8
+ ___block_literal_global.175
+ ___block_literal_global.209
+ ___block_literal_global.98
+ _objc_msgSend$_refreshAndForcePostFollowUp:refreshControlToStop:
+ _objc_msgSend$clientConfiguration
+ _objc_msgSend$dismissAMSUI
+ _objc_msgSend$generalAboutPolicy
+ _objc_msgSend$initWithIsSignedIn:deviceManager:
+ _objc_msgSend$offerTextForDevice:
+ _sharedController.onceToken
+ _sharedController.sharedController
- -[NDOCoverageCentralViewController _refresh:].cold.1
- -[NDOCoverageCentralViewController init].cold.2
- -[NDOCustomCellBackground drawRect:]
- -[NDODeviceCell .cxx_destruct]
- -[NDODeviceCell drawRect:]
- -[NDODeviceCell image]
- -[NDODeviceCell initWithCoder:]
- -[NDODeviceCell label]
- -[NDODeviceCell setImage:]
- -[NDODeviceCell setLabel:]
- GCC_except_table16
- GCC_except_table17
- GCC_except_table28
- GCC_except_table31
- _CGContextRestoreGState
- _CGContextSaveGState
- _OBJC_CLASS_$_NDOCustomCellBackground
- _OBJC_CLASS_$_NDODeviceCell
- _OBJC_CLASS_$_UIBezierPath
- _OBJC_IVAR_$_NDODeviceCell._image
- _OBJC_IVAR_$_NDODeviceCell._label
- _OBJC_METACLASS_$_NDOCustomCellBackground
- _OBJC_METACLASS_$_NDODeviceCell
- _OBJC_METACLASS_$_UIView
- _UIGraphicsGetCurrentContext
- __OBJC_$_INSTANCE_METHODS_NDOCustomCellBackground
- __OBJC_$_INSTANCE_METHODS_NDODeviceCell
- __OBJC_$_INSTANCE_VARIABLES_NDODeviceCell
- __OBJC_$_PROP_LIST_NDODeviceCell
- __OBJC_CLASS_RO_$_NDOCustomCellBackground
- __OBJC_CLASS_RO_$_NDODeviceCell
- __OBJC_METACLASS_RO_$_NDOCustomCellBackground
- __OBJC_METACLASS_RO_$_NDODeviceCell
- ___45-[NDOCoverageCentralViewController _refresh:]_block_invoke
- ___47-[NDOWarrantyInfoController managePlanPressed:]_block_invoke.169
- ___47-[NDOWarrantyInfoController managePlanPressed:]_block_invoke.171
- ___62-[NDOCoverageCentralViewController completeWithStatus:params:]_block_invoke.144
- ___62-[NDOCoverageCentralViewController completeWithStatus:params:]_block_invoke.152
- ___62-[NDOCoverageCentralViewController completeWithStatus:params:]_block_invoke_2
- ___86-[NDOWarrantyInfoController outreachFinishedForDeviceWithSerialNumber:withCompletion:]_block_invoke.195
- ___86-[NDOWarrantyInfoController outreachFinishedForDeviceWithSerialNumber:withCompletion:]_block_invoke.197
- ___86-[NDOWarrantyInfoController outreachFinishedForDeviceWithSerialNumber:withCompletion:]_block_invoke.205
- ___86-[NDOWarrantyInfoController outreachFinishedForDeviceWithSerialNumber:withCompletion:]_block_invoke_2.206
- ___96-[NDOWarrantyInfoController _refreshWithForcedNetworkPolicy:forceUpdateFollowup:withCompletion:]_block_invoke.77
- ___96-[NDOWarrantyInfoController _refreshWithForcedNetworkPolicy:forceUpdateFollowup:withCompletion:]_block_invoke.79
- ___block_descriptor_48_e8_32bs_e23_v16?0"NDODeviceInfo"8ls32l8
- ___block_descriptor_56_e8_32s40s_e5_v8?0ls32l8s40l8
- ___block_descriptor_56_e8_32s40w_e5_v8?0lw40l8s32l8
- ___block_descriptor_74_e8_32s40s48s56bs_e17_v16?0"NSArray"8ls32l8s40l8s48l8s56l8
- ___block_descriptor_82_e8_32s40s48s56s64bs_e5_v8?0ls32l8s40l8s48l8s56l8s64l8
- ___block_literal_global.174
- ___block_literal_global.208
- _objc_msgSend$bezierPathWithRoundedRect:cornerRadius:
- _objc_msgSend$blackColor
- _objc_msgSend$colorWithRed:green:blue:alpha:
- _objc_msgSend$fill
- _objc_msgSend$getAllDeviceInfoUsingPolicy:sessionID:params:isSales:andForcePostFollowup:withReply:
- _objc_msgSend$redColor
- _objc_msgSend$setFill
- _objc_msgSend$setLineWidth:
- _objc_msgSend$setStroke
- _objc_msgSend$stroke
- _sharedController
CStrings:
+ "%s: dismissing amsui"
+ "%s: refreshing device list"
+ "%{public}s: serialNumber: %@, source: %@, url: %@, deeplinkParams: %@, body: %@, isMultiCall: %d, clientInfo: %@"
+ "-[NDOCoverageCentralViewController _refreshAndForcePostFollowUp:refreshControlToStop:]"
+ "-[NDOCoverageCentralViewController dismissAMSUI]_block_invoke"
+ "-[NDOCoverageCentralViewController initWithIsSignedIn:deviceManager:]"
+ "@\"NSObject<NDOCoverageCentralVCManager>\""
+ "@28@0:8B16@20"
+ "T@\"NSObject<NDOCoverageCentralVCManager>\",&,N,V_ndoManager"
+ "_refreshAndForcePostFollowUp:refreshControlToStop:"
+ "clientConfiguration"
+ "dismissAMSUI"
+ "generalAboutPolicy"
+ "initWithIsSignedIn:deviceManager:"
+ "offerTextForDevice:"
+ "v28@0:8B16@20"
- "%{public}s: %@ :: %@ :: %@ :: %@ :: %@ :: %d"
- "%{public}s: Dismissing amsui vc for status: %lu with params: %@"
- "-[NDOCoverageCentralViewController _refresh:]"
- "-[NDOCoverageCentralViewController completeWithStatus:params:]_block_invoke_2"
- "NDOCustomCellBackground"
- "NDODeviceCell"
- "T@\"UIImageView\",&,N,V_image"
- "T@\"UILabel\",&,N,V_label"
- "_image"
- "_label"
- "bezierPathWithRoundedRect:cornerRadius:"
- "blackColor"
- "colorWithRed:green:blue:alpha:"
- "drawRect:"
- "fill"
- "image"
- "initWithCoder:"
- "redColor"
- "setFill"
- "setLabel:"
- "setLineWidth:"
- "setStroke"
- "stroke"
- "v48@0:8{CGRect={CGPoint=dd}{CGSize=dd}}16"

```
