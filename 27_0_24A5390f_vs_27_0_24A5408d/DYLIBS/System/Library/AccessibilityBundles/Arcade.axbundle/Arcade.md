## Arcade

> `/System/Library/AccessibilityBundles/Arcade.axbundle/Arcade`

### Sections with Same Size but Changed Content

- `__TEXT.__const`
- `__DATA_CONST.__got`
- `__AUTH_CONST.__const`

```diff

-3045.0.0.0.0
-  __TEXT.__text: 0xa89c
-  __TEXT.__objc_methlist: 0x2784
+3048.0.0.0.0
+  __TEXT.__text: 0xa374
+  __TEXT.__objc_methlist: 0x265c
   __TEXT.__const: 0x20
   __TEXT.__gcc_except_tab: 0x54
-  __TEXT.__cstring: 0x36db
+  __TEXT.__cstring: 0x3574
   __TEXT.__ustring: 0xc
-  __TEXT.__unwind_info: 0x5b8
+  __TEXT.__unwind_info: 0x590
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0
   __TEXT.__objc_classname: 0x0
   __TEXT.__objc_methname: 0x0
   __TEXT.__objc_methtype: 0x0
-  __DATA_CONST.__const: 0x168
-  __DATA_CONST.__objc_classlist: 0x6a8
+  __DATA_CONST.__const: 0x140
+  __DATA_CONST.__objc_classlist: 0x678
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x530
-  __DATA_CONST.__objc_superrefs: 0x200
+  __DATA_CONST.__objc_selrefs: 0x518
+  __DATA_CONST.__objc_superrefs: 0x1f0
   __DATA_CONST.__got: 0x140
   __AUTH_CONST.__const: 0x100
-  __AUTH_CONST.__cfstring: 0x3980
-  __AUTH_CONST.__objc_const: 0x77d0
+  __AUTH_CONST.__cfstring: 0x3840
+  __AUTH_CONST.__objc_const: 0x7470
   __AUTH_CONST.__auth_got: 0x0
-  __AUTH.__objc_data: 0x4290
+  __AUTH.__objc_data: 0x40b0
   __DATA.__bss: 0x12
   - /System/Library/Frameworks/Accessibility.framework/Accessibility
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation

   - /usr/lib/libAccessibility.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 663
-  Symbols:   1982
-  CStrings:  496
+  Functions: 643
+  Symbols:   1929
+  CStrings:  486
 
Symbols:
+ GCC_except_table133
+ GCC_except_table143
+ GCC_except_table235
+ GCC_except_table348
- +[AccountActionSectionFooterViewAccessibility _accessibilityPerformValidations:]
- +[AccountActionSectionFooterViewAccessibility(SafeCategory) safeCategoryBaseClass]
- +[AccountActionSectionFooterViewAccessibility(SafeCategory) safeCategoryTargetClassName]
- +[AccountDetailCollectionViewCellAccessibility _accessibilityPerformValidations:]
- +[AccountDetailCollectionViewCellAccessibility(SafeCategory) safeCategoryBaseClass]
- +[AccountDetailCollectionViewCellAccessibility(SafeCategory) safeCategoryTargetClassName]
- +[AnnotationCollectionViewCellAccessibility _accessibilityPerformValidations:]
- +[AnnotationCollectionViewCellAccessibility(SafeCategory) safeCategoryBaseClass]
- +[AnnotationCollectionViewCellAccessibility(SafeCategory) safeCategoryTargetClassName]
- -[AccountActionSectionFooterViewAccessibility accessibilityLabel]
- -[AccountActionSectionFooterViewAccessibility isAccessibilityElement]
- -[AccountDetailCollectionViewCellAccessibility accessibilityLabel]
- -[AccountDetailCollectionViewCellAccessibility accessibilityTraits]
- -[AccountDetailCollectionViewCellAccessibility isAccessibilityElement]
- -[AnnotationCollectionViewCellAccessibility _accessibilityPerformLinkAction:]
- -[AnnotationCollectionViewCellAccessibility _axLinkLabel]
- -[AnnotationCollectionViewCellAccessibility accessibilityCustomActions]
- -[AnnotationCollectionViewCellAccessibility accessibilityLabel]
- -[AnnotationCollectionViewCellAccessibility isAccessibilityElement]
- GCC_except_table153
- GCC_except_table163
- GCC_except_table255
- GCC_except_table368
- _OBJC_CLASS_$_AccountActionSectionFooterViewAccessibility
- _OBJC_CLASS_$_AccountDetailCollectionViewCellAccessibility
- _OBJC_CLASS_$_AnnotationCollectionViewCellAccessibility
- _OBJC_CLASS_$___AccountActionSectionFooterViewAccessibility_super
- _OBJC_CLASS_$___AccountDetailCollectionViewCellAccessibility_super
- _OBJC_CLASS_$___AnnotationCollectionViewCellAccessibility_super
- _OBJC_METACLASS_$_AccountActionSectionFooterViewAccessibility
- _OBJC_METACLASS_$_AccountDetailCollectionViewCellAccessibility
- _OBJC_METACLASS_$_AnnotationCollectionViewCellAccessibility
- _OBJC_METACLASS_$___AccountActionSectionFooterViewAccessibility_super
- _OBJC_METACLASS_$___AccountDetailCollectionViewCellAccessibility_super
- _OBJC_METACLASS_$___AnnotationCollectionViewCellAccessibility_super
- __OBJC_$_CLASS_METHODS_AccountActionSectionFooterViewAccessibility(SafeCategory)
- __OBJC_$_CLASS_METHODS_AccountDetailCollectionViewCellAccessibility(SafeCategory)
- __OBJC_$_CLASS_METHODS_AnnotationCollectionViewCellAccessibility(SafeCategory)
- __OBJC_$_INSTANCE_METHODS_AccountActionSectionFooterViewAccessibility
- __OBJC_$_INSTANCE_METHODS_AccountDetailCollectionViewCellAccessibility
- __OBJC_$_INSTANCE_METHODS_AnnotationCollectionViewCellAccessibility
- __OBJC_CLASS_RO_$_AccountActionSectionFooterViewAccessibility
- __OBJC_CLASS_RO_$_AccountDetailCollectionViewCellAccessibility
- __OBJC_CLASS_RO_$_AnnotationCollectionViewCellAccessibility
- __OBJC_CLASS_RO_$___AccountActionSectionFooterViewAccessibility_super
- __OBJC_CLASS_RO_$___AccountDetailCollectionViewCellAccessibility_super
- __OBJC_CLASS_RO_$___AnnotationCollectionViewCellAccessibility_super
- __OBJC_METACLASS_RO_$_AccountActionSectionFooterViewAccessibility
- __OBJC_METACLASS_RO_$_AccountDetailCollectionViewCellAccessibility
- __OBJC_METACLASS_RO_$_AnnotationCollectionViewCellAccessibility
- __OBJC_METACLASS_RO_$___AccountActionSectionFooterViewAccessibility_super
- __OBJC_METACLASS_RO_$___AccountDetailCollectionViewCellAccessibility_super
- __OBJC_METACLASS_RO_$___AnnotationCollectionViewCellAccessibility_super
- ___77-[AnnotationCollectionViewCellAccessibility _accessibilityPerformLinkAction:]_block_invoke
- ___block_descriptor_40_e8_32s_e5_v8?0ls32l8
- _objc_msgSend$_axLinkLabel
- _objc_msgSend$accessibilityLinkLabelTapped
CStrings:
- "AccountActionSectionFooterViewAccessibility"
- "AccountDetailCollectionViewCellAccessibility"
- "AnnotationCollectionViewCellAccessibility"
- "Arcade.AccountActionSectionFooterView"
- "Arcade.AccountDetailCollectionViewCell"
- "Arcade.AnnotationCollectionViewCell"
- "accessibilityLinkLabel"
- "accessibilityLinkLabelTapped"
- "accessibilityTitleLabel, accessibilitySummaryLabel"
- "detailLabel"
```
