## FocusUIModule

> `/System/Library/ControlCenter/Bundles/FocusUIModule.bundle/FocusUIModule`

```diff

-468.5.5.0.0
-  __TEXT.__text: 0x4de4
-  __TEXT.__auth_stubs: 0x3e0
-  __TEXT.__objc_stubs: 0x15a0
-  __TEXT.__objc_methlist: 0x84c
+498.0.1.0.0
+  __TEXT.__text: 0x4aa0
+  __TEXT.__auth_stubs: 0x3d0
+  __TEXT.__objc_stubs: 0x16a0
+  __TEXT.__objc_methlist: 0x8ac
   __TEXT.__const: 0x60
-  __TEXT.__gcc_except_tab: 0x100
-  __TEXT.__objc_methname: 0x1ea9
-  __TEXT.__cstring: 0x1fc
+  __TEXT.__gcc_except_tab: 0x110
+  __TEXT.__objc_methname: 0x1e75
   __TEXT.__oslogstring: 0x1a9
-  __TEXT.__objc_classname: 0xed
-  __TEXT.__objc_methtype: 0x79e
-  __TEXT.__unwind_info: 0x230
-  __DATA_CONST.__auth_got: 0x200
-  __DATA_CONST.__got: 0xf0
+  __TEXT.__cstring: 0x1f4
+  __TEXT.__objc_classname: 0x104
+  __TEXT.__objc_methtype: 0x81a
+  __TEXT.__unwind_info: 0x220
   __DATA_CONST.__const: 0x2f8
   __DATA_CONST.__cfstring: 0x200
   __DATA_CONST.__objc_classlist: 0x10
   __DATA_CONST.__objc_catlist: 0x8
-  __DATA_CONST.__objc_protolist: 0x38
+  __DATA_CONST.__objc_protolist: 0x40
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_superrefs: 0x10
   __DATA_CONST.__objc_arraydata: 0x18
   __DATA_CONST.__objc_arrayobj: 0x18
   __DATA_CONST.__objc_intobj: 0x18
-  __DATA.__objc_const: 0x1140
-  __DATA.__objc_selrefs: 0x808
-  __DATA.__objc_ivar: 0x90
+  __DATA_CONST.__auth_got: 0x1f8
+  __DATA_CONST.__got: 0xe8
+  __DATA.__objc_const: 0x1130
+  __DATA.__objc_selrefs: 0x850
+  __DATA.__objc_ivar: 0x88
   __DATA.__objc_data: 0xa0
-  __DATA.__data: 0x2a0
+  __DATA.__data: 0x300
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/CoreGraphics.framework/CoreGraphics
   - /System/Library/Frameworks/Foundation.framework/Foundation

   - /System/Library/PrivateFrameworks/FocusUI.framework/FocusUI
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 861B85BD-1A1F-3132-829A-DB46E56D9008
-  Functions: 112
-  Symbols:   129
-  CStrings:  459
+  UUID: 97156823-4EB1-3012-B519-D5B09D46221A
+  Functions: 110
+  Symbols:   125
+  CStrings:  465
 
Symbols:
+ _CCUIDefaultSupportedGridSizeClassesForChronoControls
+ _OBJC_CLASS_$_CCUIContentModulePreviewProvider
+ _OBJC_CLASS_$_CCUIContentModuleTemplatePreviewDescription
+ _OBJC_CLASS_$_CCUIGlyphButtonConfiguration
+ _objc_claimAutoreleasedReturnValue
+ _objc_release_x9
+ _objc_retainAutoreleaseReturnValue
+ _objc_retain_x1
+ _objc_retain_x3
+ _objc_retain_x8
- OBJC_IVAR_$_FCCCControlCenterModule._backgroundView
- OBJC_IVAR_$_FCCCControlCenterModule._contentRenderingMode
- _CCUIDefaultExpandedContentModuleWidth
- _CCUIExpandedModuleContinuousCornerRadius
- _CCUIReferenceScreenBounds
- _OBJC_CLASS_$_CCUIControlCenterMaterialView
- _OBJC_CLASS_$_CCUIRoundButton
- _OBJC_CLASS_$_UIDevice
- _OBJC_CLASS_$_UIImageSymbolConfiguration
- __os_feature_enabled_impl
- _objc_release_x1
- _objc_retainAutoreleasedReturnValue
- _objc_retain_x26
- _objc_retain_x27
CStrings:
+ "\nq"
+ "@\"<CCUIContentModulePreviewProviding>\"24@0:8@\"CCUIContentModulePreviewContext\"16"
+ "B24@0:8@\"CCUIControlTemplateView\"16"
+ "CCUIControlTemplateViewDelegate"
+ "Configuring glyph button with %{public}@ activity: %{public}@"
+ "_configureGlyphButtonIfNecessary"
+ "_glyphButtonNeedsUpdate"
+ "_referenceBounds"
+ "_removeGlyphButton"
+ "_removeInitialUseView"
+ "_setGlyphButtonNeedsUpdate"
+ "_systemImageNamed:"
+ "customGlyphView"
+ "defaultExpandedContentModuleWidth"
+ "expandedModuleContinuousCornerRadius"
+ "geometryProvider"
+ "glyphButtonConfiguration"
+ "initWithDescription:"
+ "initWithHighlightColor:"
+ "moduleViewControllerRequestsExpandModule:"
+ "performGlyphButtonActionForControlTemplateView:"
+ "performPrimaryActionForControlTemplateView:"
+ "performWithSender:target:"
+ "previewProviderForContext:"
+ "requestExpandModule"
+ "screen"
+ "setGlyphButtonConfiguration:"
+ "setGlyphImage:"
+ "setGlyphPackageDescription:"
+ "setGlyphStyle:"
+ "setGlyphSystemImageName:"
+ "setMenuAffordanceStyle:"
+ "setSelected:"
+ "setSelectedGlyphColor:"
+ "setUserInteractionEnabled:"
+ "supportsEdgeAlignedLayout"
+ "v24@0:8@\"FCCCModuleViewController\"16"
+ "window"
+ "windowScene"
- "\v\x81"
- "@\"CCUIRoundButton\""
- "Configuring round button with %{public}@ activity: %{public}@"
- "Solarium"
- "SwiftUI"
- "T@\"CCUIRoundButton\",&,N,G_roundButton,S_setRoundButton:,V_roundButton"
- "_backgroundView"
- "_configureRoundButtonIfNecessary"
- "_contentRenderingMode"
- "_invalidateInitialUseView"
- "_invalidateRoundButton"
- "_roundButton"
- "_setRoundButton:"
- "_systemImageNamed:withConfiguration:"
- "_userInterfaceStyleForSelectedAppearance:"
- "addAction:forControlEvents:"
- "configurationWithPointSize:"
- "controlCenterModuleBackgroundMaterial"
- "currentDevice"
- "fcui_animateWithDefaultParameters:completion:"
- "fcui_animateWithSelectionParameters:completion:"
- "initWithGlyphImage:highlightColor:highlightTintColor:useLightStyle:"
- "initWithGlyphPackageDescription:highlightColor:useLightStyle:"
- "insertSubview:aboveSubview:"
- "insertSubview:atIndex:"
- "q20@0:8B16"
- "removeAction:forControlEvents:"
- "roundButton"
- "setDynamicLayoutEnabled:"
- "setOverrideUserInterfaceStyle:"
- "setUseAlternateBackground:"
- "symbolScaleFactor"
- "userInterfaceIdiom"

```
