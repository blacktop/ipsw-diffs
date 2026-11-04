## QuickSpeak

> `/System/Library/AccessibilityBundles/QuickSpeak.bundle/QuickSpeak`

```diff

-3245.8.9.0.0
-  __TEXT.__text: 0x96b4
-  __TEXT.__objc_methlist: 0x1044
-  __TEXT.__const: 0x58
+3245.8.14.0.0
+  __TEXT.__text: 0x9e08
+  __TEXT.__objc_methlist: 0x1124
+  __TEXT.__const: 0x60
   __TEXT.__gcc_except_tab: 0x294
-  __TEXT.__cstring: 0xe8c
-  __TEXT.__oslogstring: 0x379
-  __TEXT.__unwind_info: 0x378
+  __TEXT.__cstring: 0xf74
+  __TEXT.__oslogstring: 0x3c1
+  __TEXT.__unwind_info: 0x3a0
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0
   __TEXT.__objc_classname: 0x0
   __TEXT.__objc_methname: 0x0
   __TEXT.__objc_methtype: 0x0
   __DATA_CONST.__const: 0x280
-  __DATA_CONST.__objc_classlist: 0xe0
+  __DATA_CONST.__objc_classlist: 0x110
   __DATA_CONST.__objc_catlist: 0x8
   __DATA_CONST.__objc_protolist: 0x28
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0xd78
+  __DATA_CONST.__objc_selrefs: 0xda0
   __DATA_CONST.__objc_protorefs: 0x8
-  __DATA_CONST.__objc_superrefs: 0x48
-  __DATA_CONST.__got: 0x190
+  __DATA_CONST.__objc_superrefs: 0x58
+  __DATA_CONST.__got: 0x1a0
   __AUTH_CONST.__const: 0x200
-  __AUTH_CONST.__cfstring: 0x1020
-  __AUTH_CONST.__objc_const: 0x1ab0
+  __AUTH_CONST.__cfstring: 0x11a0
+  __AUTH_CONST.__objc_const: 0x1e10
   __AUTH_CONST.__auth_got: 0x0
-  __AUTH.__objc_data: 0x8c0
+  __AUTH.__objc_data: 0xaa0
   __DATA.__objc_ivar: 0x44
   __DATA.__data: 0x1e0
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation

   - /usr/lib/libAccessibility.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 216
-  Symbols:   610
-  CStrings:  167
+  Functions: 230
+  Symbols:   657
+  CStrings:  181
 
Symbols:
+ +[MainViewController_QSExtras _accessibilityPerformValidations:]
+ +[MainViewController_QSExtras(SafeCategory) safeCategoryBaseClass]
+ +[MainViewController_QSExtras(SafeCategory) safeCategoryTargetClassName]
+ +[UICollectionView_QSExtras(SafeCategory) safeCategoryBaseClass]
+ +[UICollectionView_QSExtras(SafeCategory) safeCategoryTargetClassName]
+ +[UITableView_QSExtras(SafeCategory) safeCategoryBaseClass]
+ +[UITableView_QSExtras(SafeCategory) safeCategoryTargetClassName]
+ -[MainViewController_QSExtras _accessibilityProvidesQuickSpeakContent]
+ -[MainViewController_QSExtras _accessibilityQuickSpeakContent]
+ -[MainViewController_QSExtras _accessibilityShouldUpdateQuickSpeakContent]
+ -[NSObject_QSExtras _accessibilityProvidesQuickSpeakContent]
+ -[UICollectionView_QSExtras targetForAction:withSender:]
+ -[UITableView_QSExtras targetForAction:withSender:]
+ GCC_except_table148
+ GCC_except_table163
+ GCC_except_table190
+ GCC_except_table191
+ GCC_except_table211
+ GCC_except_table34
+ _NSStringFromSelector
+ _OBJC_CLASS_$_MainViewController_QSExtras
+ _OBJC_CLASS_$_NSListFormatter
+ _OBJC_CLASS_$_UICollectionView_QSExtras
+ _OBJC_CLASS_$_UIResponder
+ _OBJC_CLASS_$_UITableView_QSExtras
+ _OBJC_CLASS_$___MainViewController_QSExtras_super
+ _OBJC_CLASS_$___UICollectionView_QSExtras_super
+ _OBJC_CLASS_$___UITableView_QSExtras_super
+ _OBJC_METACLASS_$_MainViewController_QSExtras
+ _OBJC_METACLASS_$_UICollectionView_QSExtras
+ _OBJC_METACLASS_$_UITableView_QSExtras
+ _OBJC_METACLASS_$___MainViewController_QSExtras_super
+ _OBJC_METACLASS_$___UICollectionView_QSExtras_super
+ _OBJC_METACLASS_$___UITableView_QSExtras_super
+ _QSResponderChainTargetForQuickSpeakAction
+ __OBJC_$_CLASS_METHODS_MainViewController_QSExtras(SafeCategory)
+ __OBJC_$_CLASS_METHODS_UICollectionView_QSExtras(SafeCategory)
+ __OBJC_$_CLASS_METHODS_UITableView_QSExtras(SafeCategory)
+ __OBJC_$_INSTANCE_METHODS_MainViewController_QSExtras
+ __OBJC_$_INSTANCE_METHODS_UICollectionView_QSExtras
+ __OBJC_$_INSTANCE_METHODS_UITableView_QSExtras
+ __OBJC_CLASS_RO_$_MainViewController_QSExtras
+ __OBJC_CLASS_RO_$_UICollectionView_QSExtras
+ __OBJC_CLASS_RO_$_UITableView_QSExtras
+ __OBJC_CLASS_RO_$___MainViewController_QSExtras_super
+ __OBJC_CLASS_RO_$___UICollectionView_QSExtras_super
+ __OBJC_CLASS_RO_$___UITableView_QSExtras_super
+ __OBJC_METACLASS_RO_$_MainViewController_QSExtras
+ __OBJC_METACLASS_RO_$_UICollectionView_QSExtras
+ __OBJC_METACLASS_RO_$_UITableView_QSExtras
+ __OBJC_METACLASS_RO_$___MainViewController_QSExtras_super
+ __OBJC_METACLASS_RO_$___UICollectionView_QSExtras_super
+ __OBJC_METACLASS_RO_$___UITableView_QSExtras_super
- GCC_except_table141
- GCC_except_table149
- GCC_except_table176
- GCC_except_table177
- GCC_except_table183
- GCC_except_table28
CStrings:
+ ":"
+ "CUIKCalendarModel"
+ "EKCalendarItem"
+ "Ignoring non-responder target %{public}@ for %{public}@ from %{public}@"
+ "MainViewController"
+ "MainViewController_QSExtras"
+ "UICollectionView"
+ "UICollectionView_QSExtras"
+ "UITableView"
+ "UITableView_QSExtras"
+ "com.apple.mobilecal"
+ "model"
+ "selectedOccurrences"
+ "targetForAction:withSender:"
```
