## TVMLKit

> `/System/Library/PrivateFrameworks/TVMLKit.framework/TVMLKit`

```diff

-1145.0.1.0.0
-  __TEXT.__text: 0xdaa30
-  __TEXT.__auth_stubs: 0x1030
-  __TEXT.__objc_methlist: 0x100d4
-  __TEXT.__const: 0x768
-  __TEXT.__cstring: 0x5078
+1145.0.3.0.0
+  __TEXT.__text: 0xdaba8
+  __TEXT.__auth_stubs: 0x1040
+  __TEXT.__objc_methlist: 0x100fc
+  __TEXT.__const: 0x778
+  __TEXT.__cstring: 0x5073
   __TEXT.__gcc_except_tab: 0x1c78
   __TEXT.__oslogstring: 0x155f
   __TEXT.__ustring: 0x4a
   __TEXT.__dlopen_cstrs: 0x66
-  __TEXT.__unwind_info: 0x33b0
+  __TEXT.__unwind_info: 0x33c0
   __TEXT.__objc_classname: 0x1faa
-  __TEXT.__objc_methname: 0x25bda
-  __TEXT.__objc_methtype: 0x7dd6
-  __TEXT.__objc_stubs: 0x19c40
+  __TEXT.__objc_methname: 0x25c7c
+  __TEXT.__objc_methtype: 0x7e07
+  __TEXT.__objc_stubs: 0x19c80
   __DATA_CONST.__got: 0xe60
   __DATA_CONST.__const: 0x3568
   __DATA_CONST.__objc_classlist: 0x7a8
   __DATA_CONST.__objc_catlist: 0xe0
   __DATA_CONST.__objc_protolist: 0x2b8
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x85e0
+  __DATA_CONST.__objc_selrefs: 0x8608
   __DATA_CONST.__objc_protorefs: 0xc0
   __DATA_CONST.__objc_superrefs: 0x590
   __DATA_CONST.__objc_arraydata: 0x88
-  __AUTH_CONST.__auth_got: 0x828
+  __AUTH_CONST.__auth_got: 0x830
   __AUTH_CONST.__const: 0x11e0
   __AUTH_CONST.__cfstring: 0x8720
-  __AUTH_CONST.__objc_const: 0x2f0d0
+  __AUTH_CONST.__objc_const: 0x2f108
   __AUTH_CONST.__objc_intobj: 0x990
   __AUTH_CONST.__objc_arrayobj: 0x168
   __AUTH_CONST.__objc_doubleobj: 0xa0

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libicucore.A.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: A4F9023A-F9B4-3CD2-A7B7-A504C02697B8
-  Functions: 5333
-  Symbols:   20015
-  CStrings:  9727
+  UUID: 330714C6-D3F7-3A55-B763-58B10C00FDE0
+  Functions: 5334
+  Symbols:   20020
+  CStrings:  9733
 
Symbols:
+ +[TVMLUtilities _isSolariumMetricsEnabled]
+ __UISolariumMetricsEnabled
+ ___block_literal_global.293
+ ___block_literal_global.295
+ ___block_literal_global.306
+ ___block_literal_global.308
+ ___block_literal_global.312
+ ___block_literal_global.315
+ __defaultPlaceholderImageForUserInterfaceStyle:.__once.291
+ _objc_msgSend$_isSolariumMetricsEnabled
+ _objc_msgSend$setAsymmetricFocusedSizeIncrease:
- ___block_literal_global.24
- ___block_literal_global.283
- ___block_literal_global.292
- ___block_literal_global.303
- ___block_literal_global.309
- ___block_literal_global.314
- ___block_literal_global.327
- ___block_literal_global.34
- ___block_literal_global.36
- __defaultPlaceholderImageForUserInterfaceStyle:.__once.288
Functions:
~ +[TVMLUtilities focusedSizeIncreaseForSize:upscaleFactor:useInSearchPartial:] : 80 -> 164
~ +[TVMLUtilities _isOSFeatureEnabled:] : 80 -> 144
+ +[TVMLUtilities _isSolariumMetricsEnabled]
+ -[TVButtonContent setFocusSizeIncrease:]
- -[TVButtonContent viewElement]
~ -[TVStyleSheetRegistry _createDefaultRootNodes] : 1620 -> 1588
~ -[TVMLViewFactory _listItemLockupWithElement:existingView:] : 844 -> 884
~ -[_TVListViewController _expectedCellSizeForElement:inSectionIndex:] : 1104 -> 1160
CStrings:
+ "B40@0:8@\"UISearchBar\"16@\"NSArray\"24@\"NSString\"32"
+ "_isSolariumMetricsEnabled"
+ "allowsNumberPadPopover"
+ "searchBar:shouldChangeTextInRanges:replacementText:"
+ "setAllowsNumberPadPopover:"
+ "setAsymmetricFocusedSizeIncrease:"
+ "solarium-metrics"
- "BaseStyleSheet_Legacy"

```
