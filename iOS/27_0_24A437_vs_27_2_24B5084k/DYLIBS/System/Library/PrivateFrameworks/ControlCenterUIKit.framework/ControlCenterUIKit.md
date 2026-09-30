## ControlCenterUIKit

> `/System/Library/PrivateFrameworks/ControlCenterUIKit.framework/ControlCenterUIKit`

```diff

-704.0.2.0.0
-  __TEXT.__text: 0x47ac4
-  __TEXT.__objc_methlist: 0x57d8
-  __TEXT.__const: 0x1e28
-  __TEXT.__oslogstring: 0x6c3
-  __TEXT.__cstring: 0x16e1
+704.2.2.0.0
+  __TEXT.__text: 0x492f8
+  __TEXT.__objc_methlist: 0x5820
+  __TEXT.__const: 0x1df8
+  __TEXT.__oslogstring: 0x983
+  __TEXT.__cstring: 0x1801
   __TEXT.__gcc_except_tab: 0x1a8
-  __TEXT.__swift5_typeref: 0x779
-  __TEXT.__swift5_capture: 0x3fc
+  __TEXT.__swift5_typeref: 0x787
+  __TEXT.__swift5_capture: 0x43c
   __TEXT.__constg_swiftt: 0x818
   __TEXT.__swift5_reflstr: 0x2d3
   __TEXT.__swift5_fieldmd: 0x300

   __TEXT.__swift5_types: 0x5c
   __TEXT.__swift5_mpenum: 0x8
   __TEXT.__swift5_protos: 0x4
-  __TEXT.__unwind_info: 0x1df0
+  __TEXT.__unwind_info: 0x1e28
   __TEXT.__eh_frame: 0x40
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0

   __DATA_CONST.__objc_catlist: 0x50
   __DATA_CONST.__objc_protolist: 0x1b0
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x2e70
+  __DATA_CONST.__objc_selrefs: 0x2eb8
   __DATA_CONST.__objc_protorefs: 0x90
   __DATA_CONST.__objc_superrefs: 0xe8
   __DATA_CONST.__objc_arraydata: 0x18
-  __DATA_CONST.__got: 0x6d0
-  __AUTH_CONST.__const: 0x1728
+  __DATA_CONST.__got: 0x6f8
+  __AUTH_CONST.__const: 0x17f0
   __AUTH_CONST.__cfstring: 0xc80
-  __AUTH_CONST.__objc_const: 0x93f0
+  __AUTH_CONST.__objc_const: 0x9428
   __AUTH_CONST.__objc_intobj: 0xa8
   __AUTH_CONST.__objc_arrayobj: 0x30
-  __AUTH_CONST.__auth_got: 0x9e8
+  __AUTH_CONST.__auth_got: 0xa60
   __AUTH.__objc_data: 0x1898
   __AUTH.__data: 0x5b8
-  __DATA.__objc_ivar: 0x4ac
-  __DATA.__data: 0x15a0
+  __DATA.__objc_ivar: 0x4b0
+  __DATA.__data: 0x15c0
   __DATA.__common: 0x58
   __DATA_DIRTY.__objc_data: 0x488
   __DATA_DIRTY.__data: 0x28

   - /usr/lib/swift/libswift_Builtin_float.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  Functions: 2533
-  Symbols:   4102
-  CStrings:  227
+  Functions: 2558
+  Symbols:   4118
+  CStrings:  235
 
Symbols:
+ -[CCUIButtonModuleView _updateVisualStylingProviderIfNeeded]
+ -[CCUIRoundButton _accessibilityDelayBeforeUpdatingOnActivation]
+ -[CCUIRoundButton accessibilityDelayBeforeUpdatingOnActivation]
+ -[CCUIRoundButton setAccessibilityDelayBeforeUpdatingOnActivation:]
+ -[UIView(CCUIAdditions_Private) _controlCenterApplyPrimaryContentShadowWithOpacityScale:]
+ _OBJC_CLASS_$_UITouch
+ _OBJC_IVAR_$_CCUIRoundButton._accessibilityDelayBeforeUpdatingOnActivation
+ ___swift_closure_destructor.124Tm
+ ___swift_closure_destructor.181Tm
+ ___swift_closure_destructor.231Tm
+ __swiftImmortalRefCount
+ _memcpy
+ _objc_msgSend$_controlCenterApplyPrimaryContentShadowWithOpacityScale:
+ _objc_msgSend$_updateVisualStylingProviderIfNeeded
+ _objc_msgSend$isContextMenuInteractionEnabled
+ _objc_msgSend$isPresentingContextMenu
+ _objc_msgSend$performPrimaryAction
+ _objc_msgSend$phase
+ _symbolic _____y_____G s23_ContiguousArrayStorageC s5UInt8V
- ___swift_closure_destructor.115Tm
- ___swift_closure_destructor.172Tm
- ___swift_closure_destructor.222Tm
CStrings:
+ "[Control Template View] (%{public}s) Declining a context menu, the custom glyph view was hit"
+ "[Control Template View] (%{public}s) Declining a context menu, the delegate provided no menu"
+ "[Control Template View] (%{public}s) Declining a context menu, there is no context menu delegate"
+ "[Control Template View] (%{public}s) Presenting the context menu, UIControl's touch-down gesture did not recognize"
+ "[Control Template View] (%{public}s) Tap did not show a context menu, %{public}s [ showsMenuAsPrimaryAction: %{bool,public}d showsMenuAffordance: %{bool,public}d contextMenuInteractionEnabled: %{bool,public}d hasDelegate: %{bool,public}d gridSizeClass: %{public}ld ]"
+ "no delegate asked for the default action"
+ "showsMenuAsPrimaryAction is not set and there is no menu module delegate"
+ "the context menu interaction is not installed"
+ "the menu module delegate does not show its menu as the primary action"
+ "the menu would be anchored inside the custom glyph view"
- "Calistoga"
- "SwiftUI"
```
