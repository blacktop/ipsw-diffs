## PassKitUI

> `/System/iOSSupport/System/Library/AccessibilityBundles/PassKitUI.axbundle/Contents/MacOS/PassKitUI`

```diff

-  __TEXT.__text: 0x133b4
-  __TEXT.__objc_methlist: 0x2a54
+  __TEXT.__text: 0x159f4
+  __TEXT.__objc_methlist: 0x2c94
   __TEXT.__const: 0x18
   __TEXT.__gcc_except_tab: 0x258
-  __TEXT.__cstring: 0x3fe7
+  __TEXT.__cstring: 0x428c
   __TEXT.__ustring: 0x4
-  __TEXT.__unwind_info: 0x840
+  __TEXT.__unwind_info: 0x8c8
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0
   __TEXT.__objc_classname: 0x0
   __TEXT.__objc_methname: 0x0
   __TEXT.__objc_methtype: 0x0
-  __DATA_CONST.__const: 0x558
-  __DATA_CONST.__objc_classlist: 0x6f0
+  __DATA_CONST.__const: 0x618
+  __DATA_CONST.__objc_classlist: 0x720
   __DATA_CONST.__objc_protolist: 0x10
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0xad8
+  __DATA_CONST.__objc_selrefs: 0xbb0
   __DATA_CONST.__objc_protorefs: 0x8
-  __DATA_CONST.__objc_superrefs: 0x220
-  __DATA_CONST.__got: 0x218
-  __AUTH_CONST.__const: 0x2a0
-  __AUTH_CONST.__cfstring: 0x5300
-  __AUTH_CONST.__objc_const: 0x7ed8
+  __DATA_CONST.__objc_superrefs: 0x240
+  __DATA_CONST.__got: 0x228
+  __AUTH_CONST.__const: 0x320
+  __AUTH_CONST.__cfstring: 0x56a0
+  __AUTH_CONST.__objc_const: 0x8238
   __AUTH_CONST.__objc_intobj: 0x18
   __AUTH_CONST.__auth_got: 0x0
-  __AUTH.__objc_data: 0x910
+  __AUTH.__objc_data: 0xaf0
   __DATA.__objc_ivar: 0x10
   __DATA.__data: 0xd8
   __DATA.__bss: 0x11

   - /usr/lib/libAXSafeCategoryBundle.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 748
-  Symbols:   2360
-  CStrings:  1374
+  Functions: 799
+  Symbols:   2476
+  CStrings:  1433
 
Sections:
~ __DATA_CONST.__objc_protolist : content changed
~ __DATA_CONST.__objc_protorefs : content changed
~ __AUTH_CONST.__objc_intobj : content changed
~ __DATA.__data : content changed
~ __DATA_DIRTY.__objc_data : content changed
Symbols:
+ +[PKEditUserPassFieldCellAccessibility _accessibilityPerformValidations:]
+ +[PKEditUserPassFieldCellAccessibility(SafeCategory) safeCategoryBaseClass]
+ +[PKEditUserPassFieldCellAccessibility(SafeCategory) safeCategoryTargetClassName]
+ +[PKPassBucketViewAccessibility _accessibilityPerformValidations:]
+ +[PKPassBucketViewAccessibility(SafeCategory) safeCategoryBaseClass]
+ +[PKPassBucketViewAccessibility(SafeCategory) safeCategoryTargetClassName]
+ +[PKPassFaceViewAccessibility _accessibilityPerformValidations:]
+ +[PKPassFieldViewAccessibility _accessibilityPerformValidations:]
+ +[PassTemplateCellAccessibility _accessibilityPerformValidations:]
+ +[PassTemplateCellAccessibility(SafeCategory) safeCategoryBaseClass]
+ +[PassTemplateCellAccessibility(SafeCategory) safeCategoryTargetClassName]
+ -[PKEditUserPassFieldCellAccessibility accessibilityLabel]
+ -[PKEditUserPassFieldCellAccessibility accessibilityTraits]
+ -[PKEditUserPassFieldCellAccessibility isAccessibilityElement]
+ -[PKEditUserPassFieldCellAccessibility shouldGroupAccessibilityChildren]
+ -[PKPassBucketViewAccessibility _axEditUserPassController]
+ -[PKPassBucketViewAccessibility _axIsEmptyAddableBucket]
+ -[PKPassBucketViewAccessibility _axShouldActAsAddButton]
+ -[PKPassBucketViewAccessibility accessibilityActivate]
+ -[PKPassBucketViewAccessibility accessibilityLabel]
+ -[PKPassBucketViewAccessibility accessibilityTraits]
+ -[PKPassBucketViewAccessibility isAccessibilityElement]
+ -[PKPassFaceViewAccessibility _axUpdateLogoSymbolAccessibility]
+ -[PKPassFaceViewAccessibility setEditingMode:]
+ -[PKPassFieldViewAccessibility _axAddField:]
+ -[PKPassFieldViewAccessibility _axBucketView:canAcceptField:]
+ -[PKPassFieldViewAccessibility _axBucketView]
+ -[PKPassFieldViewAccessibility _axCanAddToBucketView:]
+ -[PKPassFieldViewAccessibility _axCollectBucketViewsInView:into:]
+ -[PKPassFieldViewAccessibility _axDeleteField:]
+ -[PKPassFieldViewAccessibility _axEditUserPassController]
+ -[PKPassFieldViewAccessibility _axIndexOfFieldKey:inBucket:]
+ -[PKPassFieldViewAccessibility _axMoveDescriptorForward:]
+ -[PKPassFieldViewAccessibility _axMoveFieldBackward:]
+ -[PKPassFieldViewAccessibility _axMoveFieldForward:]
+ -[PKPassFieldViewAccessibility _axOrderedBucketViews]
+ -[PKPassFieldViewAccessibility _axPerformMoveForward:]
+ -[PKPassFieldViewAccessibility accessibilityCustomActions]
+ -[PassTemplateCellAccessibility accessibilityActivate]
+ -[PassTemplateCellAccessibility accessibilityLabel]
+ -[PassTemplateCellAccessibility accessibilityTraits]
+ -[PassTemplateCellAccessibility isAccessibilityElement]
+ GCC_except_table496
+ GCC_except_table499
+ GCC_except_table503
+ GCC_except_table569
+ GCC_except_table571
+ GCC_except_table592
+ GCC_except_table626
+ GCC_except_table648
+ GCC_except_table653
+ GCC_except_table664
+ GCC_except_table693
+ GCC_except_table749
+ _CGRectGetMinX
+ _OBJC_CLASS_$_NSNull
+ _OBJC_CLASS_$_PKEditUserPassFieldCellAccessibility
+ _OBJC_CLASS_$_PKPassBucketViewAccessibility
+ _OBJC_CLASS_$_PassTemplateCellAccessibility
+ _OBJC_CLASS_$___PKEditUserPassFieldCellAccessibility_super
+ _OBJC_CLASS_$___PKPassBucketViewAccessibility_super
+ _OBJC_CLASS_$___PassTemplateCellAccessibility_super
+ _OBJC_METACLASS_$_PKEditUserPassFieldCellAccessibility
+ _OBJC_METACLASS_$_PKPassBucketViewAccessibility
+ _OBJC_METACLASS_$_PassTemplateCellAccessibility
+ _OBJC_METACLASS_$___PKEditUserPassFieldCellAccessibility_super
+ _OBJC_METACLASS_$___PKPassBucketViewAccessibility_super
+ _OBJC_METACLASS_$___PassTemplateCellAccessibility_super
+ __OBJC_$_CLASS_METHODS_PKEditUserPassFieldCellAccessibility(SafeCategory)
+ __OBJC_$_CLASS_METHODS_PKPassBucketViewAccessibility(SafeCategory)
+ __OBJC_$_CLASS_METHODS_PassTemplateCellAccessibility(SafeCategory)
+ __OBJC_$_INSTANCE_METHODS_PKEditUserPassFieldCellAccessibility
+ __OBJC_$_INSTANCE_METHODS_PKPassBucketViewAccessibility
+ __OBJC_$_INSTANCE_METHODS_PassTemplateCellAccessibility
+ __OBJC_CLASS_RO_$_PKEditUserPassFieldCellAccessibility
+ __OBJC_CLASS_RO_$_PKPassBucketViewAccessibility
+ __OBJC_CLASS_RO_$_PassTemplateCellAccessibility
+ __OBJC_CLASS_RO_$___PKEditUserPassFieldCellAccessibility_super
+ __OBJC_CLASS_RO_$___PKPassBucketViewAccessibility_super
+ __OBJC_CLASS_RO_$___PassTemplateCellAccessibility_super
+ __OBJC_METACLASS_RO_$_PKEditUserPassFieldCellAccessibility
+ __OBJC_METACLASS_RO_$_PKPassBucketViewAccessibility
+ __OBJC_METACLASS_RO_$_PassTemplateCellAccessibility
+ __OBJC_METACLASS_RO_$___PKEditUserPassFieldCellAccessibility_super
+ __OBJC_METACLASS_RO_$___PKPassBucketViewAccessibility_super
+ __OBJC_METACLASS_RO_$___PassTemplateCellAccessibility_super
+ ___44-[PKPassFieldViewAccessibility _axAddField:]_block_invoke
+ ___47-[PKPassFieldViewAccessibility _axDeleteField:]_block_invoke
+ ___47-[PKPassFieldViewAccessibility _axDeleteField:]_block_invoke_2
+ ___53-[PKPassFieldViewAccessibility _axOrderedBucketViews]_block_invoke
+ ___54-[PKPassBucketViewAccessibility accessibilityActivate]_block_invoke
+ ___54-[PKPassFieldViewAccessibility _axPerformMoveForward:]_block_invoke
+ ___54-[PKPassFieldViewAccessibility _axPerformMoveForward:]_block_invoke_2
+ ___54-[PassTemplateCellAccessibility accessibilityActivate]_block_invoke
+ ___54-[PassTemplateCellAccessibility accessibilityActivate]_block_invoke_2
+ ___60-[PKPassFieldViewAccessibility _axIndexOfFieldKey:inBucket:]_block_invoke
+ ___NSArray0__struct
+ ___block_descriptor_32_e27_q24?0"UIView"8"UIView"16l
+ ___block_descriptor_40_e8_32s_e15_B32?08Q16^B24ls32l8
+ ___block_descriptor_48_e8_32s40s_e5_v8?0ls32l8s40l8
+ ___block_descriptor_56_e8_32s40s48s_e5_v8?0ls32l8s40l8s48l8
+ ___block_descriptor_72_e8_32s40s48s_e5_v8?0ls32l8s40l8s48l8
+ _objc_msgSend$_axBucketView
+ _objc_msgSend$_axBucketView:canAcceptField:
+ _objc_msgSend$_axCanAddToBucketView:
+ _objc_msgSend$_axCollectBucketViewsInView:into:
+ _objc_msgSend$_axEditUserPassController
+ _objc_msgSend$_axIndexOfFieldKey:inBucket:
+ _objc_msgSend$_axIsEmptyAddableBucket
+ _objc_msgSend$_axMoveDescriptorForward:
+ _objc_msgSend$_axOrderedBucketViews
+ _objc_msgSend$_axPerformMoveForward:
+ _objc_msgSend$_axShouldActAsAddButton
+ _objc_msgSend$_axUpdateLogoSymbolAccessibility
+ _objc_msgSend$_insertField:afterField:animated:
+ _objc_msgSend$convertRect:toView:
+ _objc_msgSend$null
+ _objc_msgSend$passView:tappedBucketView:tappedFieldView:fieldViewBeforeTap:fieldViewAfterTap:
+ _objc_msgSend$passView:tappedDeleteForFieldView:
+ _objc_msgSend$passViewTapped:
+ _objc_msgSend$safeSwiftValueForKey:
+ _objc_msgSend$setValue:forKey:
+ _objc_msgSend$sortUsingComparator:
+ _objc_msgSend$unsignedIntegerValue
+ _objc_msgSend$validateClass:hasSwiftField:withSwiftType:
+ _objc_retain_x23
- GCC_except_table445
- GCC_except_table448
- GCC_except_table452
- GCC_except_table518
- GCC_except_table520
- GCC_except_table541
- GCC_except_table575
- GCC_except_table597
- GCC_except_table602
- GCC_except_table613
- GCC_except_table642
- GCC_except_table698
- ___58-[PKPassGroupViewAccessibility accessibilityPerformEscape]_block_invoke_2
- _objc_msgSend$_groupViewTapped
CStrings:
+ "PKEditUserPassFieldCell"
+ "PKEditUserPassFieldCellAccessibility"
+ "PKEditUserPassViewController"
+ "PKPassBucketTemplate"
+ "PKPassBucketView"
+ "PKPassBucketViewAccessibility"
+ "PassTemplateCellAccessibility"
+ "_TtC9PassKitUIP33_037FB033FDC36CE1EB569B2819F9225016PassTemplateCell"
+ "_fieldView"
+ "_insertField:afterField:animated:"
+ "_logoSystemImageView"
+ "add.field.action"
+ "after"
+ "bucket"
+ "bucketTemplate"
+ "delete.field.action"
+ "editingMode"
+ "field"
+ "field.deleted.announcement"
+ "field.moved.announcement"
+ "isSentinel"
+ "key"
+ "maxFields"
+ "move.field.backward.action"
+ "move.field.forward.action"
+ "nameLabel"
+ "pass.logo.symbol.button"
+ "passView:tappedBucketView:tappedFieldView:fieldViewBeforeTap:fieldViewAfterTap:"
+ "passView:tappedDeleteForFieldView:"
+ "q24@?0@\"UIView\"8@\"UIView\"16"
+ "row"
+ "setEditingMode:"
+ "type"
- "_groupViewTapped"
- "_modalGroupIndex"
- "_modallyPresentedGroupView"

```
