## com.apple.DocumentManager.Service-AppExtension

> `/System/Library/AccessibilityBundles/com.apple.DocumentManager.Service-AppExtension.axbundle/com.apple.DocumentManager.Service-AppExtension`

```diff

-2963.10.30.1.0
-  __TEXT.__text: 0x47b0
+2994.2.0.0.0
+  __TEXT.__text: 0x4aa8
   __TEXT.__auth_stubs: 0x360
-  __TEXT.__objc_methlist: 0x704
-  __TEXT.__cstring: 0xebb
+  __TEXT.__objc_methlist: 0x71c
+  __TEXT.__cstring: 0xf15
   __TEXT.__const: 0x18
   __TEXT.__gcc_except_tab: 0x124
-  __TEXT.__unwind_info: 0x240
+  __TEXT.__unwind_info: 0x248
   __TEXT.__objc_classname: 0x571
-  __TEXT.__objc_methname: 0xc2d
+  __TEXT.__objc_methname: 0xc4e
   __TEXT.__objc_methtype: 0x70
-  __TEXT.__objc_stubs: 0xd20
+  __TEXT.__objc_stubs: 0xd80
   __DATA_CONST.__got: 0x110
   __DATA_CONST.__const: 0x210
   __DATA_CONST.__objc_classlist: 0x110
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x400
+  __DATA_CONST.__objc_selrefs: 0x418
   __DATA_CONST.__objc_superrefs: 0x68
   __AUTH_CONST.__auth_got: 0x1c0
   __AUTH_CONST.__const: 0x100
-  __AUTH_CONST.__cfstring: 0x1200
+  __AUTH_CONST.__cfstring: 0x1280
   __AUTH_CONST.__objc_const: 0x1360
   __AUTH.__objc_data: 0xaa0
   __DATA.__objc_ivar: 0x4

   - /usr/lib/libAccessibility.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 7439B275-6B5F-3F16-9664-A7532BD211EC
-  Functions: 145
-  Symbols:   691
-  CStrings:  480
+  UUID: CA29174C-0D4F-3011-9EB0-1815B2F1A297
+  Functions: 147
+  Symbols:   698
+  CStrings:  492
 
Symbols:
+ -[DOCMetadataKeyValueRowAccessibility _accessibilitySupplementaryFooterViews]
+ -[DOCMetadataKeyValueRowAccessibility _axMenuButton]
+ ___block_literal_global.280
+ ___block_literal_global.285
+ ___block_literal_global.294
+ _objc_msgSend$_axMenuButton
+ _objc_msgSend$isEnabled
+ _objc_msgSend$isHidden
- ___block_literal_global.277
- ___block_literal_global.282
- ___block_literal_global.291
Functions:
~ +[DOCItemInfoOpenButtonAccessibility _accessibilityPerformValidations:] : 4 -> 128
~ -[DOCItemInfoOpenButtonAccessibility accessibilityLabel] : 12 -> 208
~ -[DOCItemInfoOpenButtonAccessibility accessibilityTraits] : 16 -> 200
~ +[DOCMetadataKeyValueRowAccessibility _accessibilityPerformValidations:] : 128 -> 156
~ -[DOCMetadataKeyValueRowAccessibility accessibilityCustomActions] : 196 -> 220
+ -[DOCMetadataKeyValueRowAccessibility _accessibilitySupplementaryFooterViews]
+ +[DOCCopyableLabelAccessibility(SafeCategory) safeCategoryBaseClass]
CStrings:
+ "$__lazy_storage_$_menuButton"
+ "Optional<UIButton>"
+ "_axMenuButton"
+ "download.button"
+ "downloadButton"
+ "isEnabled"
+ "isHidden"
+ "openButton"

```
