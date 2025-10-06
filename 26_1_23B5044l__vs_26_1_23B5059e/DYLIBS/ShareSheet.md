## ShareSheet

> `/System/Library/PrivateFrameworks/ShareSheet.framework/ShareSheet`

```diff

-2094.20.31.2.1
-  __TEXT.__text: 0xc5fc4
+2094.20.65.0.0
+  __TEXT.__text: 0xc6e14
   __TEXT.__auth_stubs: 0xf40
-  __TEXT.__objc_methlist: 0x111dc
+  __TEXT.__objc_methlist: 0x1123c
   __TEXT.__const: 0x628
-  __TEXT.__gcc_except_tab: 0x22ec
-  __TEXT.__oslogstring: 0x6bee
-  __TEXT.__cstring: 0x6bdd
+  __TEXT.__gcc_except_tab: 0x22fc
+  __TEXT.__oslogstring: 0x6c18
+  __TEXT.__cstring: 0x6c2d
   __TEXT.__dlopen_cstrs: 0xa59
   __TEXT.__ustring: 0xca
-  __TEXT.__unwind_info: 0x3378
+  __TEXT.__unwind_info: 0x33b0
   __TEXT.__objc_classname: 0x24b3
-  __TEXT.__objc_methname: 0x2d90f
-  __TEXT.__objc_methtype: 0x7645
-  __TEXT.__objc_stubs: 0x1c620
-  __DATA_CONST.__got: 0xfd0
-  __DATA_CONST.__const: 0x2788
+  __TEXT.__objc_methname: 0x2db85
+  __TEXT.__objc_methtype: 0x7685
+  __TEXT.__objc_stubs: 0x1c780
+  __DATA_CONST.__got: 0xfe0
+  __DATA_CONST.__const: 0x2800
   __DATA_CONST.__objc_classlist: 0x640
   __DATA_CONST.__objc_catlist: 0x18
   __DATA_CONST.__objc_protolist: 0x3a8
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x8ba8
+  __DATA_CONST.__objc_selrefs: 0x8c08
   __DATA_CONST.__objc_protorefs: 0x58
   __DATA_CONST.__objc_superrefs: 0x408
   __DATA_CONST.__objc_arraydata: 0x678
   __AUTH_CONST.__auth_got: 0x7b0
   __AUTH_CONST.__const: 0x10a0
   __AUTH_CONST.__cfstring: 0x5760
-  __AUTH_CONST.__objc_const: 0x2a410
+  __AUTH_CONST.__objc_const: 0x2a448
   __AUTH_CONST.__objc_arrayobj: 0x510
   __AUTH_CONST.__objc_dictobj: 0x730
   __AUTH_CONST.__objc_intobj: 0x78
   __AUTH.__objc_data: 0x2300
   __AUTH.__data: 0x128
-  __DATA.__objc_ivar: 0x14bc
+  __DATA.__objc_ivar: 0x14c0
   __DATA.__data: 0x2be8
   __DATA.__bss: 0x7f8
   __DATA_DIRTY.__objc_data: 0x1b80

   - /System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 0DF17E66-4D40-3DF3-B45F-A99080FA0B8F
-  Functions: 5824
-  Symbols:   20836
-  CStrings:  9681
+  UUID: 60751474-0CAC-3FF5-8271-FF0BF6BA1ECE
+  Functions: 5837
+  Symbols:   20884
+  CStrings:  9700
 
Symbols:
+ +[UIAirDropGroupActivityCell _createLabelForSingleLine:isAccessibilityContentSize:]
+ +[UIAirDropGroupActivityCell _formattedDisplayName:ignoreNameWrapping:isAccessibilityContentSize:nameLabel:]
+ +[UIAirDropGroupActivityCell _labelFont]
+ +[UIAirDropGroupActivityCell _placeholderStringForSingleLine:isAccessibilityContentSize:]
+ +[UIAirDropGroupActivityCell maximumLabelHeightForNode:width:traitCollection:]
+ +[UIShareGroupActivityCell maximumLabelHeightForTitle:width:traitCollection:]
+ -[SHSheetContentLayoutProvider _createHorizontalLayoutSectionWithContext:iconWidth:sectionHeight:labelHeightCalculationBlock:]
+ -[UIActivityContentViewController _activityTitleForActivity:]
+ -[UIActivityContentViewController airDropNodeForItemIdentifier:]
+ -[UIActivityContentViewController titleForItemIdentifier:].cold.1
+ -[_UIActivityViewControllerPresentationController _updateCornerConfiguration]
+ -[_UIHostActivityProxy activityType]
+ -[_UISaveToCameraRollSaveItemsController backgroundQueueForFileReading]
+ GCC_except_table112
+ GCC_except_table122
+ _OBJC_CLASS_$_UICornerConfiguration
+ _OBJC_CLASS_$_UICornerRadius
+ _OBJC_IVAR_$__UISaveToCameraRollSaveItemsController._backgroundQueueForFileReading
+ __OBJC_$_CLASS_METHODS_UIAirDropGroupActivityCell
+ __OBJC_$_CLASS_METHODS_UIShareGroupActivityCell
+ ___58-[_UISaveToCameraRollSaveItemsController beginSavingItem:]_block_invoke.124
+ ___58-[_UISaveToCameraRollSaveItemsController beginSavingItem:]_block_invoke_2
+ ___65-[SHSheetContentLayoutProvider _layoutForAppsSectionWithContext:]_block_invoke
+ ___67-[SHSheetContentLayoutProvider _layoutForPeopleSectionWithContext:]_block_invoke
+ ___block_descriptor_48_e8_32s40s_e19_d24?0"NSUUID"8d16ls32l8s40l8
+ ___block_descriptor_56_e8_32s40s48r_e5_v8?0ls32l8s40l8r48l8
+ ___block_descriptor_56_e8_32s40s48s_e32_v28?0"UIImage"8B16"NSError"20ls32l8s40l8s48l8
+ ___block_literal_global.1027
+ ___block_literal_global.1031
+ ___block_literal_global.1038
+ ___block_literal_global.1042
+ ___block_literal_global.1048
+ ___block_literal_global.175
+ _objc_msgSend$_activityTitleForActivity:
+ _objc_msgSend$_createHorizontalLayoutSectionWithContext:iconWidth:sectionHeight:labelHeightCalculationBlock:
+ _objc_msgSend$_createLabelForSingleLine:isAccessibilityContentSize:
+ _objc_msgSend$_formattedDisplayName:ignoreNameWrapping:isAccessibilityContentSize:nameLabel:
+ _objc_msgSend$_placeholderStringForSingleLine:isAccessibilityContentSize:
+ _objc_msgSend$_setCornerConfiguration:
+ _objc_msgSend$_updateCornerConfiguration
+ _objc_msgSend$airDropNodeForItemIdentifier:
+ _objc_msgSend$backgroundQueueForFileReading
+ _objc_msgSend$configurationWithTopLeftRadius:topRightRadius:bottomLeftRadius:bottomRightRadius:
+ _objc_msgSend$containerConcentricRadiusWithMinimum:
+ _objc_msgSend$fixedRadius:
+ _objc_msgSend$imageWithConfiguration:
+ _objc_msgSend$leadingRect
+ _objc_msgSend$maximumLabelHeightForNode:width:traitCollection:
+ _objc_msgSend$maximumLabelHeightForTitle:width:traitCollection:
- -[SHSheetContentLayoutProvider _createHorizontalLayoutSectionWithContext:iconWidth:sectionHeight:]
- -[UIActivityContentViewController _activityTitleForHeroActionActivity:]
- -[UIAirDropGroupActivityCell _createLabelForSingleLine:]
- -[UIAirDropGroupActivityCell _labelFont]
- -[UIAirDropGroupActivityCell _placeholderStringForSingleLine:]
- GCC_except_table111
- GCC_except_table121
- GCC_except_table124
- GCC_except_table8
- _OUTLINED_FUNCTION_3
- ___block_literal_global.1024
- ___block_literal_global.1028
- ___block_literal_global.1035
- ___block_literal_global.1039
- ___block_literal_global.1045
- ___block_literal_global.168
- _objc_msgSend$_activityTitleForHeroActionActivity:
- _objc_msgSend$_createHorizontalLayoutSectionWithContext:iconWidth:sectionHeight:
- _objc_msgSend$_createLabelForSingleLine:
- _objc_msgSend$_placeholderStringForSingleLine:
- _objc_msgSend$actionIdentifiers
CStrings:
+ "@\"UIAirDropNode\"24@0:8@\"NSUUID\"16"
+ "@40@0:8@16B24B28@32"
+ "@48@0:8@16d24d32@?40"
+ "Couldn't find title for itemIdentifier:%@"
+ "T@\"NSObject<OS_dispatch_queue>\",R,N,V_backgroundQueueForFileReading"
+ "_activityTitleForActivity:"
+ "_backgroundQueueForFileReading"
+ "_createHorizontalLayoutSectionWithContext:iconWidth:sectionHeight:labelHeightCalculationBlock:"
+ "_createLabelForSingleLine:isAccessibilityContentSize:"
+ "_formattedDisplayName:ignoreNameWrapping:isAccessibilityContentSize:nameLabel:"
+ "_placeholderStringForSingleLine:isAccessibilityContentSize:"
+ "_setCornerConfiguration:"
+ "_updateCornerConfiguration"
+ "airDropNodeForItemIdentifier:"
+ "backgroundQueueForFileReading"
+ "com.apple.ShareSheet.UISaveToCameraRollActivity.FileReading"
+ "configurationWithTopLeftRadius:topRightRadius:bottomLeftRadius:bottomRightRadius:"
+ "containerConcentricRadiusWithMinimum:"
+ "d24@?0@\"NSUUID\"8d16"
+ "d40@0:8@16d24@32"
+ "fixedRadius:"
+ "imageWithConfiguration:"
+ "leadingRect"
+ "maximumLabelHeightForNode:width:traitCollection:"
+ "maximumLabelHeightForTitle:width:traitCollection:"
- "@20@0:8B16"
- "@40@0:8@16d24d32"
- "_activityTitleForHeroActionActivity:"
- "_createHorizontalLayoutSectionWithContext:iconWidth:sectionHeight:"
- "_createLabelForSingleLine:"
- "_placeholderStringForSingleLine:"

```
