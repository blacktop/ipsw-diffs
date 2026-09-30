## MediaControls

> `/System/Library/AccessibilityBundles/MediaControls.axbundle/MediaControls`

### Sections with Same Size but Changed Content

- `__TEXT.__const`
- `__DATA_CONST.__const`
- `__DATA_CONST.__got`
- `__AUTH_CONST.__const`
- `__DATA_DIRTY.__objc_data`

```diff

-3042.0.0.0.0
-  __TEXT.__text: 0xa1f8
-  __TEXT.__objc_methlist: 0x1284
+3045.0.0.0.0
+  __TEXT.__text: 0xa7a4
+  __TEXT.__objc_methlist: 0x1304
   __TEXT.__const: 0x40
   __TEXT.__gcc_except_tab: 0x19c
-  __TEXT.__cstring: 0x2201
+  __TEXT.__cstring: 0x23ca
   __TEXT.__oslogstring: 0x4b
-  __TEXT.__unwind_info: 0x458
+  __TEXT.__unwind_info: 0x468
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0
   __TEXT.__objc_classname: 0x0
   __TEXT.__objc_methname: 0x0
   __TEXT.__objc_methtype: 0x0
   __DATA_CONST.__const: 0x378
-  __DATA_CONST.__objc_classlist: 0x2e8
+  __DATA_CONST.__objc_classlist: 0x2f8
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x680
-  __DATA_CONST.__objc_superrefs: 0x100
+  __DATA_CONST.__objc_selrefs: 0x690
+  __DATA_CONST.__objc_superrefs: 0x108
   __DATA_CONST.__got: 0x178
   __AUTH_CONST.__const: 0x120
-  __AUTH_CONST.__cfstring: 0x2ee0
-  __AUTH_CONST.__objc_const: 0x3450
+  __AUTH_CONST.__cfstring: 0x3080
+  __AUTH_CONST.__objc_const: 0x3570
   __AUTH_CONST.__auth_got: 0x0
-  __AUTH.__objc_data: 0xa0
+  __AUTH.__objc_data: 0x140
   __DATA.__bss: 0x20
   __DATA_DIRTY.__objc_data: 0x1c70
   __DATA_DIRTY.__bss: 0x8

   - /usr/lib/libMobileGestalt.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 358
-  Symbols:   1152
-  CStrings:  415
+  Functions: 367
+  Symbols:   1173
+  CStrings:  434
 
Symbols:
+ +[MediaControlsModuleSessionViewAccessibility _accessibilityPerformValidations:]
+ +[MediaControlsModuleSessionViewAccessibility(SafeCategory) safeCategoryBaseClass]
+ +[MediaControlsModuleSessionViewAccessibility(SafeCategory) safeCategoryTargetClassName]
+ -[MediaControlsModuleSessionViewAccessibility _accessibilitySupplementaryFooterViews]
+ -[MediaControlsModuleSessionViewAccessibility _axHeaderView]
+ -[MediaControlsModuleSessionViewAccessibility _axIsCollapsed]
+ -[MediaControlsModuleSessionViewAccessibility accessibilityLabel]
+ -[MediaControlsModuleSessionViewAccessibility accessibilityTraits]
+ -[MediaControlsModuleSessionViewAccessibility isAccessibilityElement]
+ GCC_except_table171
+ GCC_except_table195
+ GCC_except_table203
+ GCC_except_table220
+ GCC_except_table273
+ GCC_except_table308
+ GCC_except_table345
+ GCC_except_table75
+ GCC_except_table78
+ _OBJC_CLASS_$_MediaControlsModuleSessionViewAccessibility
+ _OBJC_CLASS_$___MediaControlsModuleSessionViewAccessibility_super
+ _OBJC_METACLASS_$_MediaControlsModuleSessionViewAccessibility
+ _OBJC_METACLASS_$___MediaControlsModuleSessionViewAccessibility_super
+ __OBJC_$_CLASS_METHODS_MediaControlsModuleSessionViewAccessibility(SafeCategory)
+ __OBJC_$_INSTANCE_METHODS_MediaControlsModuleSessionViewAccessibility
+ __OBJC_CLASS_RO_$_MediaControlsModuleSessionViewAccessibility
+ __OBJC_CLASS_RO_$___MediaControlsModuleSessionViewAccessibility_super
+ __OBJC_METACLASS_RO_$_MediaControlsModuleSessionViewAccessibility
+ __OBJC_METACLASS_RO_$___MediaControlsModuleSessionViewAccessibility_super
+ _objc_msgSend$_axHeaderView
+ _objc_msgSend$_axIsCollapsed
- GCC_except_table166
- GCC_except_table190
- GCC_except_table198
- GCC_except_table211
- GCC_except_table264
- GCC_except_table299
- GCC_except_table336
- GCC_except_table70
- GCC_except_table73
CStrings:
+ "MediaControls.MediaControlsModuleNowPlayingView"
+ "MediaControls.MediaControlsModuleSessionView"
+ "MediaControls.SessionAccessoryView"
+ "MediaControls.SessionHeaderView"
+ "MediaControls.TransportButton"
+ "MediaControlsModuleNowPlayingView"
+ "MediaControlsModuleSessionViewAccessibility"
+ "RoutePickerSessionViewState"
+ "SessionAccessoryView"
+ "SessionActionButton"
+ "SessionHeaderView"
+ "TransportButton"
+ "accessoryView"
+ "actionButton"
+ "headerOnly"
+ "headerView"
+ "mode"
+ "nowPlayingView"
+ "sessionViewState"
```
