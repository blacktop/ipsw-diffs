## PlatterKit

> `/System/Library/PrivateFrameworks/PlatterKit.framework/PlatterKit`

```diff

-340.4.3.0.0
-  __TEXT.__text: 0x24870
-  __TEXT.__auth_stubs: 0x730
-  __TEXT.__objc_methlist: 0x3830
-  __TEXT.__const: 0x1e8
-  __TEXT.__gcc_except_tab: 0x3cc
-  __TEXT.__cstring: 0xbae
+361.100.0.0.0
+  __TEXT.__text: 0x2533c
+  __TEXT.__auth_stubs: 0x740
+  __TEXT.__objc_methlist: 0x38d8
+  __TEXT.__const: 0x1f8
+  __TEXT.__gcc_except_tab: 0x3d4
+  __TEXT.__cstring: 0xbd4
   __TEXT.__oslogstring: 0x512
-  __TEXT.__unwind_info: 0xcd8
-  __TEXT.__objc_classname: 0x85e
-  __TEXT.__objc_methname: 0xacec
-  __TEXT.__objc_methtype: 0x233d
-  __TEXT.__objc_stubs: 0x78c0
-  __DATA_CONST.__got: 0x4e8
+  __TEXT.__unwind_info: 0xcf0
+  __TEXT.__objc_classname: 0x85f
+  __TEXT.__objc_methname: 0xafd5
+  __TEXT.__objc_methtype: 0x2349
+  __TEXT.__objc_stubs: 0x7b40
+  __DATA_CONST.__got: 0x4f0
   __DATA_CONST.__const: 0x838
   __DATA_CONST.__objc_classlist: 0x120
   __DATA_CONST.__objc_catlist: 0x18
   __DATA_CONST.__objc_protolist: 0xe8
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x2550
+  __DATA_CONST.__objc_selrefs: 0x25f8
   __DATA_CONST.__objc_protorefs: 0x38
   __DATA_CONST.__objc_superrefs: 0xf0
   __DATA_CONST.__objc_arraydata: 0x40
-  __AUTH_CONST.__auth_got: 0x3a8
+  __AUTH_CONST.__auth_got: 0x3b0
   __AUTH_CONST.__const: 0x120
-  __AUTH_CONST.__cfstring: 0x7e0
-  __AUTH_CONST.__objc_const: 0xb478
+  __AUTH_CONST.__cfstring: 0x820
+  __AUTH_CONST.__objc_const: 0xb5e8
   __AUTH_CONST.__objc_intobj: 0xf0
   __AUTH_CONST.__objc_arrayobj: 0x78
   __AUTH.__objc_data: 0x6e0
-  __DATA.__objc_ivar: 0x368
+  __DATA.__objc_ivar: 0x38c
   __DATA.__data: 0xae8
   __DATA.__bss: 0x30
   __DATA_DIRTY.__objc_data: 0x460

   - /System/Library/PrivateFrameworks/MaterialKit.framework/MaterialKit
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 86D5F319-BA05-33DA-B072-2374462FD512
-  Functions: 1118
-  Symbols:   4495
-  CStrings:  2064
+  UUID: 61BFD2A2-3263-39A1-A6C9-FD5147FBE8C5
+  Functions: 1132
+  Symbols:   4552
+  CStrings:  2099
 
Symbols:
+ -[PLPillView _configureBackgroundViewIfNecessary]
+ -[PLPillView _configureGlassIfNecessary]
+ -[PLPillView _setBackground:]
+ -[PLPillView hasShadow]
+ -[PLPillView setHasShadow:]
+ -[PLPillView setUsesBackgroundView:]
+ -[PLPillView usesBackgroundView]
+ -[PLPlatterActionButton isBackgroundGlass]
+ -[PLPlatterActionButton setIsBackgroundGlass:]
+ -[PLPlatterActionButton setTitleAlpha:]
+ -[PLPlatterActionButton titleAlpha]
+ -[PLPlatterActionButtonsView hasGlassBackground]
+ -[PLPlatterActionButtonsView initWithFrame:actions:cornerRadius:shouldVerticallyStack:shouldGetGlassBackground:glassState:glassSmoothness:glassId:]
+ -[PLPlatterActionButtonsView setHasGlassBackground:]
+ -[PLPlatterView _configureGlassIfNecessary]
+ -[PLPlatterView _setBackground:]
+ GCC_except_table9
+ _OBJC_CLASS_$__UIViewGlass
+ _OBJC_IVAR_$_PLPillView._hasClientSpecifiedBackground
+ _OBJC_IVAR_$_PLPillView._hasShadow
+ _OBJC_IVAR_$_PLPillView._usesBackgroundView
+ _OBJC_IVAR_$_PLPillView._wantsAutomaticGlass
+ _OBJC_IVAR_$_PLPlatterActionButton._isBackgroundGlass
+ _OBJC_IVAR_$_PLPlatterActionButton._titleAlpha
+ _OBJC_IVAR_$_PLPlatterActionButtonsView._hasGlassBackground
+ _OBJC_IVAR_$_PLPlatterView._hasClientSpecifiedBackground
+ _OBJC_IVAR_$_PLPlatterView._wantsAutomaticGlass
+ __UISolariumEnabled
+ ___147-[PLPlatterActionButtonsView initWithFrame:actions:cornerRadius:shouldVerticallyStack:shouldGetGlassBackground:glassState:glassSmoothness:glassId:]_block_invoke
+ _objc_msgSend$_background
+ _objc_msgSend$_configureGlassIfNecessary
+ _objc_msgSend$_setBackground:
+ _objc_msgSend$allObjects
+ _objc_msgSend$buttonsGlassBackgroundIdForSwipeInteraction:
+ _objc_msgSend$buttonsGlassBackgroundSmoothnessForSwipeInteraction:
+ _objc_msgSend$buttonsGlassBackgroundStateForSwipeInteraction:
+ _objc_msgSend$hasGlassBackground
+ _objc_msgSend$initWithFrame:actions:cornerRadius:shouldVerticallyStack:shouldGetGlassBackground:glassState:glassSmoothness:glassId:
+ _objc_msgSend$initWithVariant:size:
+ _objc_msgSend$initWithVariant:size:smoothness:
+ _objc_msgSend$isSubclassOfClass:
+ _objc_msgSend$reverseObjectEnumerator
+ _objc_msgSend$setAdaptiveInitialLuminance:
+ _objc_msgSend$setBackdropGroupName:
+ _objc_msgSend$setIdentifier:
+ _objc_msgSend$setIsBackgroundGlass:
+ _objc_msgSend$setSubvariant:
+ _objc_msgSend$setTitleAlpha:
+ _objc_msgSend$spacing
+ _objc_msgSend$usesBackgroundView
- -[PLPlatterActionButtonsView initWithFrame:actions:cornerRadius:shouldVerticallyStack:]
- -[PLPlatterActionButtonsView setButtonsStackView:]
- GCC_except_table8
- ___87-[PLPlatterActionButtonsView initWithFrame:actions:cornerRadius:shouldVerticallyStack:]_block_invoke
- _objc_msgSend$initWithFrame:actions:cornerRadius:shouldVerticallyStack:
CStrings:
+ "@96@0:8{CGRect={CGPoint=dd}{CGSize=dd}}16@48d56B64B68Q72d80q88"
+ "T@\"UIStackView\",R,N,V_buttonsStackView"
+ "TB,N,V_hasGlassBackground"
+ "TB,N,V_hasShadow"
+ "TB,N,V_isBackgroundGlass"
+ "Td,N,V_titleAlpha"
+ "_background"
+ "_configureGlassIfNecessary"
+ "_hasClientSpecifiedBackground"
+ "_hasGlassBackground"
+ "_hasShadow"
+ "_isBackgroundGlass"
+ "_setBackground:"
+ "_titleAlpha"
+ "_wantsAutomaticGlass"
+ "allObjects"
+ "buttonsGlassBackgroundIdForSwipeInteraction:"
+ "buttonsGlassBackgroundSmoothnessForSwipeInteraction:"
+ "buttonsGlassBackgroundStateForSwipeInteraction:"
+ "hasGlassBackground"
+ "initWithFrame:actions:cornerRadius:shouldVerticallyStack:shouldGetGlassBackground:glassState:glassSmoothness:glassId:"
+ "initWithVariant:size:"
+ "initWithVariant:size:smoothness:"
+ "isBackgroundGlass"
+ "isSubclassOfClass:"
+ "lockscreenControls"
+ "lockscreenElements"
+ "reverseObjectEnumerator"
+ "setAdaptiveInitialLuminance:"
+ "setBackdropGroupName:"
+ "setHasGlassBackground:"
+ "setIdentifier:"
+ "setIsBackgroundGlass:"
+ "setSubvariant:"
+ "setTitleAlpha:"
+ "spacing"
+ "titleAlpha"
- "@68@0:8{CGRect={CGPoint=dd}{CGSize=dd}}16@48d56B64"
- "T@\"UIStackView\",&,N,V_buttonsStackView"
- "initWithFrame:actions:cornerRadius:shouldVerticallyStack:"
- "setButtonsStackView:"

```
