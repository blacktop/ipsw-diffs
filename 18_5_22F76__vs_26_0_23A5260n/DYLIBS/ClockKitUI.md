## ClockKitUI

> `/System/Library/PrivateFrameworks/ClockKitUI.framework/ClockKitUI`

```diff

-2483.147.79.1.2
-  __TEXT.__text: 0x336ec
-  __TEXT.__auth_stubs: 0x1220
-  __TEXT.__objc_methlist: 0x3fa4
-  __TEXT.__const: 0x7a86
+2483.284.3.0.0
+  __TEXT.__text: 0x341a4
+  __TEXT.__auth_stubs: 0x1240
+  __TEXT.__objc_methlist: 0x420c
+  __TEXT.__const: 0x7a76
   __TEXT.__gcc_except_tab: 0x588
-  __TEXT.__cstring: 0x14aa
+  __TEXT.__cstring: 0x14ba
   __TEXT.__oslogstring: 0xeec
   __TEXT.__ustring: 0x8
   __TEXT.__swift5_typeref: 0x18c

   __TEXT.__swift5_builtin: 0x64
   __TEXT.__swift5_mpenum: 0x8
   __TEXT.__swift5_types: 0x24
-  __TEXT.__unwind_info: 0x1038
-  __TEXT.__eh_frame: 0x158
-  __TEXT.__objc_classname: 0x695
-  __TEXT.__objc_methname: 0x9ab8
-  __TEXT.__objc_methtype: 0x199d
-  __TEXT.__objc_stubs: 0x7720
-  __DATA_CONST.__got: 0x4e8
-  __DATA_CONST.__const: 0xba8
-  __DATA_CONST.__objc_classlist: 0x1d8
+  __TEXT.__unwind_info: 0x1070
+  __TEXT.__eh_frame: 0xb8
+  __TEXT.__objc_classname: 0x6c2
+  __TEXT.__objc_methname: 0xa43f
+  __TEXT.__objc_methtype: 0x1a35
+  __TEXT.__objc_stubs: 0x7940
+  __DATA_CONST.__got: 0x4f8
+  __DATA_CONST.__const: 0xb80
+  __DATA_CONST.__objc_classlist: 0x1e0
   __DATA_CONST.__objc_catlist: 0x8
   __DATA_CONST.__objc_protolist: 0x78
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x26b0
-  __DATA_CONST.__objc_superrefs: 0x168
+  __DATA_CONST.__objc_selrefs: 0x2848
+  __DATA_CONST.__objc_superrefs: 0x170
   __DATA_CONST.__objc_arraydata: 0x340
-  __AUTH_CONST.__auth_got: 0x928
+  __AUTH_CONST.__auth_got: 0x938
   __AUTH_CONST.__const: 0x688
-  __AUTH_CONST.__cfstring: 0x1140
-  __AUTH_CONST.__objc_const: 0x9978
+  __AUTH_CONST.__cfstring: 0x1160
+  __AUTH_CONST.__objc_const: 0x7d70
   __AUTH_CONST.__objc_intobj: 0x378
   __AUTH_CONST.__objc_doubleobj: 0x1e0
   __AUTH_CONST.__objc_arrayobj: 0x120
-  __AUTH.__objc_data: 0xd70
+  __AUTH.__objc_data: 0xdc0
   __AUTH.__data: 0xe8
-  __DATA.__objc_ivar: 0x678
+  __DATA.__objc_ivar: 0x6c8
   __DATA.__data: 0x648
-  __DATA.__bss: 0x4b8
+  __DATA.__bss: 0x4e8
   __DATA_DIRTY.__objc_data: 0x5a0
   __DATA_DIRTY.__bss: 0x88
   - /System/Library/Frameworks/Accelerate.framework/Accelerate

   - /System/Library/Frameworks/Metal.framework/Metal
   - /System/Library/Frameworks/QuartzCore.framework/QuartzCore
   - /System/Library/Frameworks/UIKit.framework/UIKit
+  - /System/Library/Frameworks/_LocationEssentials.framework/_LocationEssentials
   - /System/Library/PrivateFrameworks/AppSupport.framework/AppSupport
   - /System/Library/PrivateFrameworks/BaseBoard.framework/BaseBoard
   - /System/Library/PrivateFrameworks/BaseBoardUI.framework/BaseBoardUI
   - /System/Library/PrivateFrameworks/GeoServices.framework/GeoServices
   - /System/Library/PrivateFrameworks/NanoRegistry.framework/NanoRegistry
-  - /System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore
+  - /System/Library/PrivateFrameworks/UIFoundation.framework/UIFoundation
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libc++.1.dylib
   - /usr/lib/libcompression.dylib

   - /usr/lib/swift/libswiftCoreFoundation.dylib
   - /usr/lib/swift/libswiftCoreImage.dylib
   - /usr/lib/swift/libswiftDarwin.dylib
-  - /usr/lib/swift/libswiftDataDetection.dylib
   - /usr/lib/swift/libswiftDispatch.dylib
   - /usr/lib/swift/libswiftMetal.dylib
   - /usr/lib/swift/libswiftOSLog.dylib

   - /usr/lib/swift/libswiftUniformTypeIdentifiers.dylib
   - /usr/lib/swift/libswiftXPC.dylib
   - /usr/lib/swift/libswift_Builtin_float.dylib
-  - /usr/lib/swift/libswift_errno.dylib
-  - /usr/lib/swift/libswift_math.dylib
-  - /usr/lib/swift/libswift_signal.dylib
-  - /usr/lib/swift/libswift_stdio.dylib
-  - /usr/lib/swift/libswift_time.dylib
+  - /usr/lib/swift/libswift_DarwinFoundation1.dylib
+  - /usr/lib/swift/libswift_DarwinFoundation2.dylib
+  - /usr/lib/swift/libswift_DarwinFoundation3.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  - /usr/lib/swift/libswiftsys_time.dylib
-  - /usr/lib/swift/libswiftunistd.dylib
-  UUID: 96ACBA67-DFB1-32FE-9D02-46827CFCF148
-  Functions: 1628
-  Symbols:   5654
-  CStrings:  2599
+  UUID: 05E67946-65C6-34FC-9743-D3E4BA2EA42E
+  Functions: 1682
+  Symbols:   5751
+  CStrings:  2694
 
Symbols:
+ +[CLKUIAnalogHandFactory _createHandOutlineImageWithSize:paths:colors:configuration:]
+ +[CLKUIAnalogHandFactory _createHandOutlineImageWithSize:paths:colors:configuration:].cold.1
+ +[CLKUIAnalogTimeView _handsViewClass]
+ +[CLKUIMetalAtlas createMTLTextureWithBacking:numMipmapLevelsToDrop:device:encoder:]
+ -[CLKUIAnalogHandConfiguration outlineOnly]
+ -[CLKUIAnalogHandConfiguration setOutlineOnly:]
+ -[CLKUIAnalogHandsView hourInlayColor]
+ -[CLKUIAnalogHandsView minuteInlayColor]
+ -[CLKUIAnalogHandsView setHourInlayColor:]
+ -[CLKUIAnalogHandsView setMinuteInlayColor:]
+ -[CLKUIAnalogTimeView handsView]
+ -[CLKUIAnalogTimeViewConfiguration backgroundViewClipsToBounds]
+ -[CLKUIAnalogTimeViewConfiguration hourHandInlayColor]
+ -[CLKUIAnalogTimeViewConfiguration hourHandOutlineColor]
+ -[CLKUIAnalogTimeViewConfiguration inactiveBackgroundViewClipsToBounds]
+ -[CLKUIAnalogTimeViewConfiguration inactiveHourHandInlayColor]
+ -[CLKUIAnalogTimeViewConfiguration inactiveHourHandOutlineColor]
+ -[CLKUIAnalogTimeViewConfiguration inactiveMinuteHandInlayColor]
+ -[CLKUIAnalogTimeViewConfiguration inactiveMinuteHandOutlineColor]
+ -[CLKUIAnalogTimeViewConfiguration inlayAlpha]
+ -[CLKUIAnalogTimeViewConfiguration minuteHandInlayColor]
+ -[CLKUIAnalogTimeViewConfiguration minuteHandOutlineColor]
+ -[CLKUIAnalogTimeViewConfiguration outlineOnly]
+ -[CLKUIAnalogTimeViewConfiguration setBackgroundViewClipsToBounds:]
+ -[CLKUIAnalogTimeViewConfiguration setHourHandInlayColor:]
+ -[CLKUIAnalogTimeViewConfiguration setHourHandOutlineColor:]
+ -[CLKUIAnalogTimeViewConfiguration setInactiveBackgroundViewClipsToBounds:]
+ -[CLKUIAnalogTimeViewConfiguration setInactiveHourHandInlayColor:]
+ -[CLKUIAnalogTimeViewConfiguration setInactiveHourHandOutlineColor:]
+ -[CLKUIAnalogTimeViewConfiguration setInactiveMinuteHandInlayColor:]
+ -[CLKUIAnalogTimeViewConfiguration setInactiveMinuteHandOutlineColor:]
+ -[CLKUIAnalogTimeViewConfiguration setInlayAlpha:]
+ -[CLKUIAnalogTimeViewConfiguration setMinuteHandInlayColor:]
+ -[CLKUIAnalogTimeViewConfiguration setMinuteHandOutlineColor:]
+ -[CLKUIAnalogTimeViewConfiguration setOutlineOnly:]
+ -[CLKUIColoringLabel _capOffsetFromBoundsTop]
+ -[CLKUICurvedLabel _capOffsetFromBoundsTop]
+ -[CLKUICylindricalPickerCollectionViewLayout .cxx_destruct]
+ -[CLKUICylindricalPickerCollectionViewLayout attributesByIndexPath]
+ -[CLKUICylindricalPickerCollectionViewLayout attributes]
+ -[CLKUICylindricalPickerCollectionViewLayout collectionViewContentSize]
+ -[CLKUICylindricalPickerCollectionViewLayout distaceFromCenterForLayoutAttributes:]
+ -[CLKUICylindricalPickerCollectionViewLayout farthestCellScaleFactor]
+ -[CLKUICylindricalPickerCollectionViewLayout layoutAttributesForElementsInRect:]
+ -[CLKUICylindricalPickerCollectionViewLayout layoutAttributesForItemAtIndexPath:]
+ -[CLKUICylindricalPickerCollectionViewLayout prepareLayout]
+ -[CLKUICylindricalPickerCollectionViewLayout setAttributes:]
+ -[CLKUICylindricalPickerCollectionViewLayout setAttributesByIndexPath:]
+ -[CLKUICylindricalPickerCollectionViewLayout setFarthestCellScaleFactor:]
+ -[CLKUICylindricalPickerCollectionViewLayout shouldInvalidateLayoutForBoundsChange:]
+ -[CLKUICylindricalPickerCollectionViewLayout targetContentOffsetForProposedContentOffset:]
+ -[CLKUICylindricalPickerCollectionViewLayout targetContentOffsetForProposedContentOffset:withScrollingVelocity:]
+ _CGRectIntersectsRect
+ _OBJC_CLASS_$_CLKUICylindricalPickerCollectionViewLayout
+ _OBJC_CLASS_$_UICollectionViewFlowLayout
+ _OBJC_IVAR_$_CLKUIAnalogHandConfiguration._outlineOnly
+ _OBJC_IVAR_$_CLKUIAnalogHandsView._hourInlayColor
+ _OBJC_IVAR_$_CLKUIAnalogHandsView._minuteInlayColor
+ _OBJC_IVAR_$_CLKUIAnalogTimeViewConfiguration._backgroundViewClipsToBounds
+ _OBJC_IVAR_$_CLKUIAnalogTimeViewConfiguration._hourHandInlayColor
+ _OBJC_IVAR_$_CLKUIAnalogTimeViewConfiguration._hourHandOutlineColor
+ _OBJC_IVAR_$_CLKUIAnalogTimeViewConfiguration._inactiveBackgroundViewClipsToBounds
+ _OBJC_IVAR_$_CLKUIAnalogTimeViewConfiguration._inactiveHourHandInlayColor
+ _OBJC_IVAR_$_CLKUIAnalogTimeViewConfiguration._inactiveHourHandOutlineColor
+ _OBJC_IVAR_$_CLKUIAnalogTimeViewConfiguration._inactiveMinuteHandInlayColor
+ _OBJC_IVAR_$_CLKUIAnalogTimeViewConfiguration._inactiveMinuteHandOutlineColor
+ _OBJC_IVAR_$_CLKUIAnalogTimeViewConfiguration._inlayAlpha
+ _OBJC_IVAR_$_CLKUIAnalogTimeViewConfiguration._minuteHandInlayColor
+ _OBJC_IVAR_$_CLKUIAnalogTimeViewConfiguration._minuteHandOutlineColor
+ _OBJC_IVAR_$_CLKUIAnalogTimeViewConfiguration._outlineOnly
+ _OBJC_IVAR_$_CLKUIColoringLabel.__capOffsetFromBoundsTop
+ _OBJC_IVAR_$_CLKUICurvedLabel.__capOffsetFromBoundsTop
+ _OBJC_IVAR_$_CLKUICylindricalPickerCollectionViewLayout._attributes
+ _OBJC_IVAR_$_CLKUICylindricalPickerCollectionViewLayout._attributesByIndexPath
+ _OBJC_IVAR_$_CLKUICylindricalPickerCollectionViewLayout._farthestCellScaleFactor
+ _OBJC_METACLASS_$_CLKUICylindricalPickerCollectionViewLayout
+ _OBJC_METACLASS_$_UICollectionViewFlowLayout
+ __OBJC_$_INSTANCE_METHODS_CLKUICylindricalPickerCollectionViewLayout
+ __OBJC_$_INSTANCE_VARIABLES_CLKUICylindricalPickerCollectionViewLayout
+ __OBJC_$_PROP_LIST_CLKUIAnalogTimeView
+ __OBJC_$_PROP_LIST_CLKUIColoringView.443
+ __OBJC_$_PROP_LIST_CLKUICylindricalPickerCollectionViewLayout
+ __OBJC_CLASS_RO_$_CLKUICylindricalPickerCollectionViewLayout
+ __OBJC_METACLASS_RO_$_CLKUICylindricalPickerCollectionViewLayout
+ __TimeAnimationKey_block_invoke.__cachedDevice
+ __TimeAnimationKey_block_invoke.__previousCLKDeviceVersion
+ __TimeAnimationKey_block_invoke.lock
+ __TimeAnimationKey_block_invoke.value
+ ___45+[CLKUIAnalogHandFactoryCache sharedInstance]_block_invoke.63
+ ___CLKUICurvedColoringLabelCenterSize_block_invoke_2
+ ___CLKUICurvedColoringLabelCornerSize_block_invoke_2
+ ___CLKUIImageNamedFromAssetBundleForDevice_block_invoke_3
+ ___CLKUIOrderedSuffixesForDevice_block_invoke_3
+ ____LayoutConstants_block_invoke_2
+ ___block_literal_global.194
+ ___block_literal_global.86
+ __block_invoke.__cachedDevice
+ __block_invoke.__previousCLKDeviceVersion
+ __block_invoke.lock
+ __block_invoke.value
+ __block_invoke.value.0
+ __block_invoke.value.1
+ __block_invoke.value.2
+ __block_invoke.value.3
+ __block_invoke_2.__cachedDevice
+ __block_invoke_2.__previousCLKDeviceVersion
+ __block_invoke_2.lock
+ __block_invoke_2.value
+ __block_invoke_2.value.0
+ __block_invoke_2.value.1
+ __swift_FORCE_LOAD_$_swift_DarwinFoundation1
+ __swift_FORCE_LOAD_$_swift_DarwinFoundation1_$_ClockKitUI
+ __swift_FORCE_LOAD_$_swift_DarwinFoundation2
+ __swift_FORCE_LOAD_$_swift_DarwinFoundation2_$_ClockKitUI
+ __swift_FORCE_LOAD_$_swift_DarwinFoundation3
+ __swift_FORCE_LOAD_$_swift_DarwinFoundation3_$_ClockKitUI
+ _kCAFillRuleEvenOdd
+ _objc_msgSend$_createHandOutlineImageWithSize:paths:colors:configuration:
+ _objc_msgSend$_handsViewClass
+ _objc_msgSend$appendPath:
+ _objc_msgSend$attributes
+ _objc_msgSend$attributesByIndexPath
+ _objc_msgSend$backgroundViewClipsToBounds
+ _objc_msgSend$bezierPathWithCGPath:
+ _objc_msgSend$collectionView
+ _objc_msgSend$contentInset
+ _objc_msgSend$contentOffset
+ _objc_msgSend$createMTLTextureWithBacking:numMipmapLevelsToDrop:device:encoder:
+ _objc_msgSend$inactiveBackgroundViewClipsToBounds
+ _objc_msgSend$indexPathsForVisibleItems
+ _objc_msgSend$layoutAttributesForItemAtIndexPath:
+ _objc_msgSend$outlineOnly
+ _objc_msgSend$path
+ _objc_msgSend$setOutlineOnly:
+ _objc_msgSend$targetContentOffsetForProposedContentOffset:withScrollingVelocity:
+ _swift_coroFrameAlloc
+ _swift_errorRelease
- +[CLKUIMetalAtlas _createMTLTextureWithBacking:numMipmapLevelsToDrop:device:encoder:]
- _CLKUICurvedColoringLabelCenterSize.__cachedDevice
- _CLKUICurvedColoringLabelCenterSize.__lock
- _CLKUICurvedColoringLabelCenterSize.__previousCLKDeviceVersion
- _CLKUICurvedColoringLabelCenterSize._size.0
- _CLKUICurvedColoringLabelCenterSize._size.1
- _CLKUICurvedColoringLabelCornerSize.__cachedDevice
- _CLKUICurvedColoringLabelCornerSize.__lock
- _CLKUICurvedColoringLabelCornerSize.__previousCLKDeviceVersion
- _CLKUICurvedColoringLabelCornerSize._size.0
- _CLKUICurvedColoringLabelCornerSize._size.1
- _CLKUIImageNamedFromAssetBundleForDevice.__cachedDevice
- _CLKUIImageNamedFromAssetBundleForDevice.__lock
- _CLKUIImageNamedFromAssetBundleForDevice.__previousCLKDeviceVersion
- _CLKUIOrderedSuffixesForDevice.__cachedDevice
- _CLKUIOrderedSuffixesForDevice.__lock
- _CLKUIOrderedSuffixesForDevice.__previousCLKDeviceVersion
- __LayoutConstants
- __LayoutConstants.__cachedDevice
- __LayoutConstants.__constants
- __LayoutConstants.__constants.0
- __LayoutConstants.__constants.1
- __LayoutConstants.__lock
- __LayoutConstants.__previousCLKDeviceVersion
- __LayoutConstants._constants
- __LayoutConstants._constants.0
- __LayoutConstants._constants.1
- __LayoutConstants._constants.2
- __LayoutConstants.constants.0
- __LayoutConstants.constants.1
- __OBJC_$_PROP_LIST_CLKUIColoringView.437
- ___45+[CLKUIAnalogHandFactoryCache sharedInstance]_block_invoke.60
- ___block_literal_global.185
- ___block_literal_global.77
- __swift_FORCE_LOAD_$_swiftDataDetection
- __swift_FORCE_LOAD_$_swiftDataDetection_$_ClockKitUI
- __swift_FORCE_LOAD_$_swift_errno
- __swift_FORCE_LOAD_$_swift_errno_$_ClockKitUI
- __swift_FORCE_LOAD_$_swift_math
- __swift_FORCE_LOAD_$_swift_math_$_ClockKitUI
- __swift_FORCE_LOAD_$_swift_signal
- __swift_FORCE_LOAD_$_swift_signal_$_ClockKitUI
- __swift_FORCE_LOAD_$_swift_stdio
- __swift_FORCE_LOAD_$_swift_stdio_$_ClockKitUI
- __swift_FORCE_LOAD_$_swift_time
- __swift_FORCE_LOAD_$_swift_time_$_ClockKitUI
- __swift_FORCE_LOAD_$_swiftsys_time
- __swift_FORCE_LOAD_$_swiftsys_time_$_ClockKitUI
- __swift_FORCE_LOAD_$_swiftunistd
- __swift_FORCE_LOAD_$_swiftunistd_$_ClockKitUI
- _objc_msgSend$_createMTLTextureWithBacking:numMipmapLevelsToDrop:device:encoder:
- _swift_bridgeObjectRelease_n
CStrings:
+ "%lu-%f-%f-%f-%f-%f-%f-%f-%f-%f-%f-%i-%i-%i-%f-%d-%d"
+ "@56@0:8{CGSize=dd}16@32@40@48"
+ "B48@0:8{CGRect={CGPoint=dd}{CGSize=dd}}16"
+ "CLKUICylindricalPickerCollectionViewLayout"
+ "NO:"
+ "T@\"CLKUIHandsView\",R,N,V_handsView"
+ "T@\"NSMutableArray\",&,N,V_attributes"
+ "T@\"NSMutableDictionary\",&,N,V_attributesByIndexPath"
+ "T@\"UIColor\",&,N,V_hourHandInlayColor"
+ "T@\"UIColor\",&,N,V_hourHandOutlineColor"
+ "T@\"UIColor\",&,N,V_hourInlayColor"
+ "T@\"UIColor\",&,N,V_inactiveHourHandInlayColor"
+ "T@\"UIColor\",&,N,V_inactiveHourHandOutlineColor"
+ "T@\"UIColor\",&,N,V_inactiveMinuteHandInlayColor"
+ "T@\"UIColor\",&,N,V_inactiveMinuteHandOutlineColor"
+ "T@\"UIColor\",&,N,V_minuteHandInlayColor"
+ "T@\"UIColor\",&,N,V_minuteHandOutlineColor"
+ "T@\"UIColor\",&,N,V_minuteInlayColor"
+ "TB,N,V_backgroundViewClipsToBounds"
+ "TB,N,V_inactiveBackgroundViewClipsToBounds"
+ "TB,N,V_outlineOnly"
+ "Td,N,V_farthestCellScaleFactor"
+ "Td,N,V_inlayAlpha"
+ "Td,R,N,V__capOffsetFromBoundsTop"
+ "__capOffsetFromBoundsTop"
+ "_attributes"
+ "_attributesByIndexPath"
+ "_backgroundViewClipsToBounds"
+ "_createHandOutlineImageWithSize:paths:colors:configuration:"
+ "_farthestCellScaleFactor"
+ "_handsViewClass"
+ "_hourHandInlayColor"
+ "_hourHandOutlineColor"
+ "_hourInlayColor"
+ "_inactiveBackgroundViewClipsToBounds"
+ "_inactiveHourHandInlayColor"
+ "_inactiveHourHandOutlineColor"
+ "_inactiveMinuteHandInlayColor"
+ "_inactiveMinuteHandOutlineColor"
+ "_inlayAlpha"
+ "_minuteHandInlayColor"
+ "_minuteHandOutlineColor"
+ "_minuteInlayColor"
+ "_outlineOnly"
+ "appendPath:"
+ "attributes"
+ "attributesByIndexPath"
+ "backgroundViewClipsToBounds"
+ "bezierPathWithCGPath:"
+ "collectionView"
+ "collectionViewContentSize"
+ "contentInset"
+ "contentOffset"
+ "createMTLTextureWithBacking:numMipmapLevelsToDrop:device:encoder:"
+ "distaceFromCenterForLayoutAttributes:"
+ "farthestCellScaleFactor"
+ "handsView"
+ "hourHandInlayColor"
+ "hourHandOutlineColor"
+ "hourInlayColor"
+ "inactiveBackgroundViewClipsToBounds"
+ "inactiveHourHandInlayColor"
+ "inactiveHourHandOutlineColor"
+ "inactiveMinuteHandInlayColor"
+ "inactiveMinuteHandOutlineColor"
+ "indexPathsForVisibleItems"
+ "inlayAlpha"
+ "layoutAttributesForElementsInRect:"
+ "layoutAttributesForItemAtIndexPath:"
+ "minuteHandInlayColor"
+ "minuteHandOutlineColor"
+ "minuteInlayColor"
+ "outlineOnly"
+ "prepareLayout"
+ "setAttributes:"
+ "setAttributesByIndexPath:"
+ "setBackgroundViewClipsToBounds:"
+ "setFarthestCellScaleFactor:"
+ "setHourHandInlayColor:"
+ "setHourHandOutlineColor:"
+ "setHourInlayColor:"
+ "setInactiveBackgroundViewClipsToBounds:"
+ "setInactiveHourHandInlayColor:"
+ "setInactiveHourHandOutlineColor:"
+ "setInactiveMinuteHandInlayColor:"
+ "setInactiveMinuteHandOutlineColor:"
+ "setInlayAlpha:"
+ "setMinuteHandInlayColor:"
+ "setMinuteHandOutlineColor:"
+ "setMinuteInlayColor:"
+ "setOutlineOnly:"
+ "shouldInvalidateLayoutForBoundsChange:"
+ "targetContentOffsetForProposedContentOffset:"
+ "targetContentOffsetForProposedContentOffset:withScrollingVelocity:"
+ "type:%lu-inlayInsetRadius:%f-handWidth:%f-handLength:%f-pegRadius:%f-pegStrokeWidth:%f-armLength:%f-armWidth:%f-tailLength:%f-directionalShadowOffset:%f/%f-roundedSecondHand:%i-excludePeg:%i-excludeSecondTail:%i-smoothingRadius:%f-removeInlay:%@-outlineOnly:%@"
+ "{CGPoint=dd}32@0:8{CGPoint=dd}16"
+ "{CGPoint=dd}48@0:8{CGPoint=dd}16{CGPoint=dd}32"
+ "\xe1"
+ "\xf0\x91"
+ "\xf0\xf0a"
- "%lu-%f-%f-%f-%f-%f-%f-%f-%f-%f-%f-%i-%i-%i-%f-%d"
- "_createMTLTextureWithBacking:numMipmapLevelsToDrop:device:encoder:"
- "type:%lu-inlayInsetRadius:%f-handWidth:%f-handLength:%f-pegRadius:%f-pegStrokeWidth:%f-armLength:%f-armWidth:%f-tailLength:%f-directionalShadowOffset:%f/%f-roundedSecondHand:%i-excludePeg:%i-excludeSecondTail:%i-smoothingRadius:%f-removeInlay:%@"
- "\xc1"
- "\xf0\x81"
- "\xf0\xf0Q"

```
