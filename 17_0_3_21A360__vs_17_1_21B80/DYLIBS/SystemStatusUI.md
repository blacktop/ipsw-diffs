## SystemStatusUI

> `/System/Library/PrivateFrameworks/SystemStatusUI.framework/SystemStatusUI`

```diff

-165.4.2.0.0
-  __TEXT.__text: 0x8d97c
-  __TEXT.__auth_stubs: 0x1350
-  __TEXT.__objc_methlist: 0x900c
-  __TEXT.__const: 0x2c70
+165.13.100.0.0
+  __TEXT.__text: 0x909a4
+  __TEXT.__auth_stubs: 0x1370
+  __TEXT.__objc_methlist: 0x9160
+  __TEXT.__const: 0x2c78
   __TEXT.__swift5_typeref: 0x20d0
-  __TEXT.__cstring: 0x2555
+  __TEXT.__cstring: 0x273f
   __TEXT.__swift5_capture: 0x74
   __TEXT.__swift5_reflstr: 0x218
   __TEXT.__swift5_assocty: 0x198

   __TEXT.__swift5_proto: 0xe0
   __TEXT.__swift5_types: 0x8c
   __TEXT.__swift5_protos: 0x4
-  __TEXT.__gcc_except_tab: 0xce4
+  __TEXT.__gcc_except_tab: 0xd88
   __TEXT.__ustring: 0xb0
   __TEXT.__oslogstring: 0x499
-  __TEXT.__unwind_info: 0x23b0
+  __TEXT.__unwind_info: 0x2408
   __TEXT.__eh_frame: 0x70
-  __TEXT.__objc_classname: 0x1afa
-  __TEXT.__objc_methname: 0x15447
-  __TEXT.__objc_methtype: 0x31b2
-  __TEXT.__objc_stubs: 0xf820
+  __TEXT.__objc_classname: 0x1b59
+  __TEXT.__objc_methname: 0x154fd
+  __TEXT.__objc_methtype: 0x31bd
+  __TEXT.__objc_stubs: 0xf940
   __DATA_CONST.__got: 0x560
-  __DATA_CONST.__const: 0x1ba0
-  __DATA_CONST.__objc_classlist: 0x570
+  __DATA_CONST.__const: 0x1be8
+  __DATA_CONST.__objc_classlist: 0x580
   __DATA_CONST.__objc_catlist: 0x90
   __DATA_CONST.__objc_protolist: 0x110
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_const: 0x1a3f0
-  __DATA_CONST.__objc_selrefs: 0x4b88
+  __DATA_CONST.__objc_const: 0x1a8b0
+  __DATA_CONST.__objc_selrefs: 0x4bd0
   __DATA_CONST.__objc_arraydata: 0x300
-  __AUTH_CONST.__const: 0x16d8
+  __AUTH_CONST.__const: 0x16b8
   __AUTH_CONST.__auth_ptr: 0x18
-  __AUTH_CONST.__cfstring: 0x34e0
-  __AUTH_CONST.__objc_const: 0x48d8
+  __AUTH_CONST.__cfstring: 0x3720
+  __AUTH_CONST.__objc_const: 0x49f8
   __AUTH_CONST.__objc_arrayobj: 0x300
   __AUTH_CONST.__objc_intobj: 0xd8
   __AUTH_CONST.__objc_doubleobj: 0x1b0
-  __AUTH_CONST.__auth_got: 0x9b8
-  __AUTH.__objc_data: 0xcf0
+  __AUTH_CONST.__auth_got: 0x9c8
+  __AUTH.__objc_data: 0xd90
   __AUTH.__data: 0x260
   __DATA.__objc_protorefs: 0x18
-  __DATA.__objc_classrefs: 0x958
+  __DATA.__objc_classrefs: 0x968
   __DATA.__objc_superrefs: 0x2d8
-  __DATA.__objc_ivar: 0x4f8
+  __DATA.__objc_ivar: 0x504
   __DATA.__data: 0x1310
   __DATA.__bss: 0x1df8
   __DATA.__common: 0x18

   - /System/Library/Frameworks/Symbols.framework/Symbols
   - /System/Library/Frameworks/UIKit.framework/UIKit
   - /System/Library/PrivateFrameworks/BaseBoard.framework/BaseBoard
+  - /System/Library/PrivateFrameworks/GraphicsServices.framework/GraphicsServices
   - /System/Library/PrivateFrameworks/PrototypeTools.framework/PrototypeTools
   - /System/Library/PrivateFrameworks/SystemStatus.framework/SystemStatus
   - /System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore

   - /usr/lib/swift/libswiftXPC.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  Functions: 4276
-  Symbols:   12018
-  CStrings:  4596
+  Functions: 4311
+  Symbols:   12128
+  CStrings:  4627
 
Symbols:
+ +[STUIStatusBarVisualProvider_CarPlayDualDriver intrinsicContentSizeForOrientation:]
+ +[STUIStatusBarVisualProvider_CarPlayDualPassenger intrinsicContentSizeForOrientation:]
+ -[STUIStatusBar reinitializeStatusBar]
+ -[STUIStatusBarDataAggregatorUpdateDelayToken dealloc]
+ -[STUIStatusBarDataAggregatorUpdateDelayToken timeoutBlock]
+ -[STUIStatusBarStyleRequest _descriptionBuilderWithMultilinePrefix:forDebug:]
+ -[STUIStatusBarStyleRequest debugDescriptionWithMultilinePrefix:]
+ -[STUIStatusBarStyleRequest descriptionBuilderWithMultilinePrefix:]
+ -[STUIStatusBarStyleRequest descriptionWithMultilinePrefix:]
+ -[STUIStatusBarStyleRequest description]
+ -[STUIStatusBarStyleRequest succinctDescriptionBuilder]
+ -[STUIStatusBarStyleRequest succinctDescription]
+ -[STUIStatusBarVisualProvider_CarPlayDualDriver .cxx_destruct]
+ -[STUIStatusBarVisualProvider_CarPlayDualDriver itemCreated:]
+ -[STUIStatusBarVisualProvider_CarPlayDualDriver orderedDisplayItemPlacementsInRegionWithIdentifier:]
+ -[STUIStatusBarVisualProvider_CarPlayDualDriver orderedDisplayItemPlacements]
+ -[STUIStatusBarVisualProvider_CarPlayDualDriver setOrderedDisplayItemPlacements:]
+ -[STUIStatusBarVisualProvider_CarPlayDualDriver setupInContainerView:]
+ -[STUIStatusBarVisualProvider_CarPlayDualPassenger .cxx_destruct]
+ -[STUIStatusBarVisualProvider_CarPlayDualPassenger itemCreated:]
+ -[STUIStatusBarVisualProvider_CarPlayDualPassenger orderedDisplayItemPlacementsInRegionWithIdentifier:]
+ -[STUIStatusBarVisualProvider_CarPlayDualPassenger orderedDisplayItemPlacements]
+ -[STUIStatusBarVisualProvider_CarPlayDualPassenger setOrderedDisplayItemPlacements:]
+ -[STUIStatusBarVisualProvider_CarPlayDualPassenger setupInContainerView:]
+ -[STUIStatusBarVisualProvider_DynamicSplit _calculateSquishyLayoutValuesForCutoutOffset:cutoutWidth:maxLeadingItems:maxTrailingItems:leadingScale:trailingScale:includingPrivacyIndicator:]
+ -[STUIStatusBarVisualProvider_DynamicSplit _updateSystemUpdateRegionEnablement:forTrailingNumberOfItems:]
+ GCC_except_table125
+ GCC_except_table49
+ GCC_except_table62
+ GCC_except_table89
+ GCC_except_table94
+ _DashBoardFrameworkBundle
+ _GSSystemRootDirectory
+ _NSSearchPathForDirectoriesInDomains
+ _OBJC_CLASS_$_STUIStatusBarVisualProvider_CarPlayDualDriver
+ _OBJC_CLASS_$_STUIStatusBarVisualProvider_CarPlayDualPassenger
+ _OBJC_IVAR_$_STUIStatusBarDataAggregatorUpdateDelayToken._timeoutBlock
+ _OBJC_IVAR_$_STUIStatusBarVisualProvider_CarPlayDualDriver._orderedDisplayItemPlacements
+ _OBJC_IVAR_$_STUIStatusBarVisualProvider_CarPlayDualPassenger._orderedDisplayItemPlacements
+ _OBJC_METACLASS_$_STUIStatusBarVisualProvider_CarPlayDualDriver
+ _OBJC_METACLASS_$_STUIStatusBarVisualProvider_CarPlayDualPassenger
+ _STUIStatusBarCarPlayDualLayoutDriverKey
+ _STUIStatusBarCarPlayDualLayoutPassengerKey
+ __OBJC_$_CLASS_METHODS_STUIStatusBarVisualProvider_CarPlayDualDriver
+ __OBJC_$_CLASS_METHODS_STUIStatusBarVisualProvider_CarPlayDualPassenger
+ __OBJC_$_INSTANCE_METHODS_STUIStatusBarVisualProvider_CarPlayDualDriver
+ __OBJC_$_INSTANCE_METHODS_STUIStatusBarVisualProvider_CarPlayDualPassenger
+ __OBJC_$_INSTANCE_VARIABLES_STUIStatusBarVisualProvider_CarPlayDualDriver
+ __OBJC_$_INSTANCE_VARIABLES_STUIStatusBarVisualProvider_CarPlayDualPassenger
+ __OBJC_$_PROP_LIST_STUIStatusBarVisualProvider_CarPlayDualDriver
+ __OBJC_$_PROP_LIST_STUIStatusBarVisualProvider_CarPlayDualPassenger
+ __OBJC_CLASS_PROTOCOLS_$_STUIStatusBarStyleRequest
+ __OBJC_CLASS_RO_$_STUIStatusBarVisualProvider_CarPlayDualDriver
+ __OBJC_CLASS_RO_$_STUIStatusBarVisualProvider_CarPlayDualPassenger
+ __OBJC_METACLASS_RO_$_STUIStatusBarVisualProvider_CarPlayDualDriver
+ __OBJC_METACLASS_RO_$_STUIStatusBarVisualProvider_CarPlayDualPassenger
+ __STUIStringFromStatusBarLegacyStyle
+ __STUIStringFromUILegibilityStyle
+ ___105-[STUIStatusBarVisualProvider_DynamicSplit avoidanceFrameUpdatedFromFrame:withAnimationSettings:options:]_block_invoke_3
+ ___38-[STUIStatusBar reinitializeStatusBar]_block_invoke
+ ___38-[STUIStatusBar reinitializeStatusBar]_block_invoke_2
+ ___38-[STUIStatusBar reinitializeStatusBar]_block_invoke_3
+ ___77-[STUIStatusBarStyleRequest _descriptionBuilderWithMultilinePrefix:forDebug:]_block_invoke
+ ___block_descriptor_40_e8_32s_e50_B32?0"STUIStatusBarDisplayItemPlacement"8Q16^B24ls32l8
+ ___block_literal_global.124
+ __updateSquishyRegionForDynamicValues
+ _objc_msgSend$appendBool:withName:ifEqualTo:
+ _objc_msgSend$containsIndex:
+ _objc_msgSend$foregroundAlpha
+ _objc_msgSend$isDoubleHeight
+ _objc_msgSend$isLegacy
+ _objc_msgSend$isPaused
+ _objc_msgSend$isTranslucent
+ _objc_msgSend$objectAtIndex:
+ _objc_msgSend$removeInteraction:
+ _objc_msgSend$stringForStatusBarStyle:
- GCC_except_table121
- GCC_except_table41
- GCC_except_table58
- GCC_except_table85
- GCC_except_table90
- ___block_descriptor_48_e8_32bs40w_e17_v16?0"NSTimer"8lw40l8s32l8
- ___block_literal_global.123
- ___block_literal_global.445
- _objc_msgSend$pathForResource:ofType:
CStrings:
+ "B24@0:8Q16"
+ "PrivateFrameworks/DashBoard.framework"
+ "STUIStatusBarCarPlayDualLayoutDriverKey"
+ "STUIStatusBarCarPlayDualLayoutPassengerKey"
+ "STUIStatusBarVisualProvider_CarPlayDualDriver"
+ "STUIStatusBarVisualProvider_CarPlayDualPassenger"
+ "T@?,R,C,N,V_timeoutBlock"
+ "UIStatusBarStyleBlackOpaque"
+ "UIStatusBarStyleDarkContent"
+ "UIStatusBarStyleDefault"
+ "UIStatusBarStyleLightContent"
+ "Unknown UIStatusBarStyle #%ld"
+ "Unknown _UILegibilityStyle #%ld"
+ "_UILegibilityStyleDarkContentWithLightShadow"
+ "_UILegibilityStyleDefault"
+ "_UILegibilityStyleLightContentWithDarkShadow"
+ "appendBool:withName:ifEqualTo:"
+ "containsIndex:"
+ "etc"
+ "foregroundAlpha"
+ "isDoubleHeight"
+ "isLegacy"
+ "isPaused"
+ "isTranslucent"
+ "objectAtIndex:"
+ "reinitializeStatusBar"
+ "removeInteraction:"
- "CarPlayArtwork"
- "bundle"
- "pathForResource:ofType:"

```
