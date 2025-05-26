## BluetoothUIService

> `/System/Library/CoreServices/BluetoothUIService.app/BluetoothUIService`

```diff

-471.0.0.0.0
-  __TEXT.__text: 0xa420
-  __TEXT.__auth_stubs: 0x5b0
-  __TEXT.__objc_stubs: 0x2100
-  __TEXT.__objc_methlist: 0x720
-  __TEXT.__const: 0x70
-  __TEXT.__gcc_except_tab: 0x54
-  __TEXT.__cstring: 0x12c7
-  __TEXT.__objc_methname: 0x2bdc
+14.16.2.0.0
+  __TEXT.__text: 0xbaf4
+  __TEXT.__auth_stubs: 0x5c0
+  __TEXT.__objc_stubs: 0x2320
+  __TEXT.__objc_methlist: 0x750
+  __TEXT.__const: 0x78
+  __TEXT.__gcc_except_tab: 0xc0
+  __TEXT.__cstring: 0x13e7
+  __TEXT.__objc_methname: 0x2dbc
   __TEXT.__objc_classname: 0x14f
-  __TEXT.__objc_methtype: 0x6b9
-  __TEXT.__unwind_info: 0x1e8
-  __DATA_CONST.__auth_got: 0x2e8
-  __DATA_CONST.__got: 0x80
-  __DATA_CONST.__const: 0x168
-  __DATA_CONST.__cfstring: 0x900
+  __TEXT.__objc_methtype: 0x6a7
+  __TEXT.__unwind_info: 0x218
+  __DATA_CONST.__auth_got: 0x2f0
+  __DATA_CONST.__got: 0x90
+  __DATA_CONST.__const: 0x190
+  __DATA_CONST.__cfstring: 0x9a0
   __DATA_CONST.__objc_classlist: 0x30
   __DATA_CONST.__objc_protolist: 0x38
   __DATA_CONST.__objc_imageinfo: 0x8
+  __DATA_CONST.__objc_classrefs: 0x148
+  __DATA_CONST.__objc_superrefs: 0x18
+  __DATA_CONST.__objc_arraydata: 0x8
+  __DATA_CONST.__objc_arrayobj: 0x18
   __DATA_CONST.__objc_intobj: 0x48
   __DATA.__objc_const: 0x1ed8
-  __DATA.__objc_selrefs: 0xa00
-  __DATA.__objc_classrefs: 0x148
-  __DATA.__objc_superrefs: 0x18
+  __DATA.__objc_selrefs: 0xa88
   __DATA.__objc_ivar: 0x148
   __DATA.__objc_data: 0x1e0
   __DATA.__data: 0x380

   - /System/Library/PrivateFrameworks/SpringBoardUIServices.framework/SpringBoardUIServices
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 159
-  Symbols:   158
-  CStrings:  802
+  Functions: 167
+  Symbols:   162
+  CStrings:  831
 
Symbols:
+ _CMTimeRangeMake
+ _OBJC_CLASS_$_AVPlayer
+ _OBJC_CLASS_$_NSConstantArray
+ _OBJC_CLASS_$_UIButton
+ _UIFontTextStyleSubheadline
+ _kCMTimeZero
- _OBJC_CLASS_$_AVPlayerLooper
- _OBJC_CLASS_$_AVQueuePlayer
CStrings:
+ "\x01"
+ "-[BluetoothUIServiceBanner _showInUseBanner]"
+ "-[BluetoothUIServiceBanner createInUseConnectButton]"
+ "8229"
+ "CONNECT"
+ "IN_USE_BY_OTHER_DEVICE"
+ "InUse"
+ "InUseBanner: Creating connect button"
+ "InUseBanner: Legacy banner"
+ "InUseBanner: process banner request"
+ "Post Banner ccText %@, ccItemsIcon %@ ccItemsText %@ leadingAccessoryIconName %@ trailingAccessoryText %@ trailingAccessoryIconName %@ bannerType: %s"
+ "T@\"<BNPresentableContext>\",?,W,N"
+ "T@\"<SBUISystemApertureElement>\",?,R,W,N"
+ "T@\"AVPlayer\",&,N"
+ "T@\"BSAction\",?,R,N"
+ "T@\"NSSet\",?,R,C,N"
+ "T@\"NSString\",?,R,C"
+ "T@\"NSString\",?,R,C,N"
+ "T@\"NSURL\",?,R,C,N"
+ "T@\"UIColor\",?,R,C,N"
+ "T@\"UIView<SBUISystemApertureAccessoryView>\",?,R,N"
+ "T@\"UIView<SBUISystemApertureAccessoryView>\",?,R,N,V_leadingView"
+ "T@\"UIView<SBUISystemApertureAccessoryView>\",?,R,N,V_trailingView"
+ "T@\"UIViewController\",?,R,N"
+ "TB,?,N"
+ "TB,?,N,V_canRequestAlertingAssertion"
+ "TB,?,R,N"
+ "TB,?,R,N,GisDraggingDismissalEnabled"
+ "TB,?,R,N,GisDraggingInteractionEnabled"
+ "TB,?,R,N,GisTouchOutsideDismissalEnabled"
+ "TQ,?,N"
+ "TQ,?,R,N"
+ "Td,?,R,N"
+ "Tq,?,R,N"
+ "Tq,?,R,N,V_presentableType"
+ "T{CGSize=dd},?,R,N"
+ "_createConstraintsForInUseBannerIfNeeded"
+ "_createInUseBannerTextLabel:bottomLabel:"
+ "_isInUseBanner"
+ "_preferredFontForTextStyle:variant:"
+ "_setCornerRadius:"
+ "_showInUseBanner"
+ "asset"
+ "buttonWithType:"
+ "createInUseConnectButton"
+ "duration"
+ "isBeingRemoved"
+ "labelColor"
+ "loadValuesAsynchronouslyForKeys:completionHandler:"
+ "replaceCurrentItemWithPlayerItem:"
+ "secondarySystemFillColor"
+ "setContentEdgeInsets:"
+ "setLoopTimeRange:"
+ "setTitle:forState:"
+ "statusOfValueForKey:error:"
+ "titleLabel"
- "\x02"
- "@\"AVPlayerLooper\""
- "Post Banner ccText: %@, ccItemsText: %@ _leadingAccessoryIconName %@ _trailingAccessoryText %@ _bannerType: %s"
- "T@\"<BNPresentableContext>\",W,N"
- "T@\"<SBUISystemApertureElement>\",R,W,N"
- "T@\"AVQueuePlayer\",&,N"
- "T@\"BSAction\",R,N"
- "T@\"NSSet\",R,C,N"
- "T@\"NSURL\",R,C,N"
- "T@\"UIColor\",R,C,N"
- "T@\"UIView<SBUISystemApertureAccessoryView>\",R,N"
- "T@\"UIView<SBUISystemApertureAccessoryView>\",R,N,V_leadingView"
- "T@\"UIView<SBUISystemApertureAccessoryView>\",R,N,V_trailingView"
- "T@\"UIViewController\",R,N"
- "TB,N"
- "TB,N,V_canRequestAlertingAssertion"
- "TB,R,N"
- "TB,R,N,GisDraggingDismissalEnabled"
- "TB,R,N,GisDraggingInteractionEnabled"
- "TB,R,N,GisTouchOutsideDismissalEnabled"
- "TQ,N"
- "TQ,R,N"
- "Td,R,N"
- "Tq,R,N,V_presentableType"
- "T{CGSize=dd},R,N"
- "_avLooper"
- "playerLooperWithPlayer:templateItem:"
- "removeAllItems"

```
