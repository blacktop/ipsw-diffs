## AXRuntime

> `/System/Library/PrivateFrameworks/AXRuntime.framework/Versions/A/AXRuntime`

```diff

-3237.0.0.0.0
-  __TEXT.__text: 0x46474
-  __TEXT.__objc_methlist: 0x3380
-  __TEXT.__const: 0x3e8
+3240.0.1.2.0
+  __TEXT.__text: 0x46bb0
+  __TEXT.__objc_methlist: 0x33c8
+  __TEXT.__const: 0x3f8
   __TEXT.__dlopen_cstrs: 0xbb
-  __TEXT.__gcc_except_tab: 0x74c
-  __TEXT.__oslogstring: 0x10f5
-  __TEXT.__cstring: 0x56ac
+  __TEXT.__gcc_except_tab: 0x748
+  __TEXT.__oslogstring: 0x12b9
+  __TEXT.__cstring: 0x56e1
   __TEXT.__ustring: 0x4
-  __TEXT.__unwind_info: 0x1068
+  __TEXT.__unwind_info: 0x10b0
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0
   __TEXT.__objc_classname: 0x0

   __DATA_CONST.__objc_catlist: 0x48
   __DATA_CONST.__objc_protolist: 0x28
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x2050
+  __DATA_CONST.__objc_selrefs: 0x2080
   __DATA_CONST.__objc_superrefs: 0x98
   __DATA_CONST.__objc_arraydata: 0xb8
   __DATA_CONST.__got: 0x2b8
-  __AUTH_CONST.__const: 0x1390
-  __AUTH_CONST.__cfstring: 0x4e80
-  __AUTH_CONST.__objc_const: 0x3560
+  __AUTH_CONST.__const: 0x13c0
+  __AUTH_CONST.__cfstring: 0x4ec0
+  __AUTH_CONST.__objc_const: 0x3580
   __AUTH_CONST.__objc_intobj: 0x1578
   __AUTH_CONST.__objc_arrayobj: 0x78
   __AUTH_CONST.__objc_doubleobj: 0x10
-  __AUTH_CONST.__auth_got: 0x920
+  __AUTH_CONST.__auth_got: 0x938
   __AUTH.__objc_data: 0x500
-  __DATA.__objc_ivar: 0x204
-  __DATA.__data: 0x8b8
+  __DATA.__objc_ivar: 0x208
+  __DATA.__data: 0x8c0
   __DATA.__bss: 0x188
   __DATA.__common: 0x2c
   __DATA_DIRTY.__objc_data: 0x2d0

   - /usr/lib/libAccessibility.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 1492
-  Symbols:   3585
-  CStrings:  854
+  Functions: 1503
+  Symbols:   3607
+  CStrings:  859
 
Symbols:
+ -[AXElement _convertRectFromWindowCoordinates:]
+ -[AXElementFetcher _fuzzyMatchElement:candidate:]
+ -[AXElementFetcher findElementMatchingElement:allowFuzzyMatch:]
+ -[AXElementGroup _fuzzyMatchItem:candidate:]
+ -[AXElementGroup _unionOfChildFrames]
+ -[AXElementGroup firstDescendantMatchingItem:allowFuzzyMatch:]
+ -[_AXObjectCacheHelper .cxx_destruct]
+ GCC_except_table1022
+ GCC_except_table1174
+ GCC_except_table1179
+ GCC_except_table1211
+ GCC_except_table1230
+ GCC_except_table1248
+ GCC_except_table1327
+ GCC_except_table1355
+ GCC_except_table1402
+ GCC_except_table1467
+ GCC_except_table348
+ GCC_except_table352
+ GCC_except_table354
+ GCC_except_table450
+ GCC_except_table456
+ GCC_except_table521
+ GCC_except_table665
+ GCC_except_table675
+ GCC_except_table762
+ GCC_except_table766
+ GCC_except_table770
+ GCC_except_table780
+ GCC_except_table781
+ GCC_except_table782
+ GCC_except_table783
+ GCC_except_table836
+ OBJC_IVAR_$__AXObjectCacheHelper._weakElement
+ _AXAIWhiteGloveLoggingEnabled
+ _CGRectContainsRect
+ _CGRectIsEmpty
+ _UIAccessibilityTokenDynamicContentAnnouncement
+ __AXElementFromElementCache
+ ___63-[AXElementFetcher findElementMatchingElement:allowFuzzyMatch:]_block_invoke
+ ____AXElementFromElementCache_block_invoke
+ ___block_descriptor_57_e8_32s40s48r_e5_v8?0l
+ _objc_msgSend$_convertRectFromWindowCoordinates:
+ _objc_msgSend$_fuzzyMatchElement:candidate:
+ _objc_msgSend$_fuzzyMatchItem:candidate:
+ _objc_msgSend$_unionOfChildFrames
+ _objc_msgSend$displayIdForContextId:
+ _objc_msgSend$findElementMatchingElement:allowFuzzyMatch:
+ _objc_msgSend$firstDescendantMatchingItem:allowFuzzyMatch:
- GCC_except_table1016
- GCC_except_table1168
- GCC_except_table1173
- GCC_except_table1205
- GCC_except_table1222
- GCC_except_table1240
- GCC_except_table1319
- GCC_except_table1347
- GCC_except_table1394
- GCC_except_table1456
- GCC_except_table347
- GCC_except_table351
- GCC_except_table39
- GCC_except_table445
- GCC_except_table451
- GCC_except_table516
- GCC_except_table660
- GCC_except_table670
- GCC_except_table757
- GCC_except_table761
- GCC_except_table765
- GCC_except_table775
- GCC_except_table776
- GCC_except_table777
- GCC_except_table778
- GCC_except_table831
- ___47-[AXElementFetcher findElementMatchingElement:]_block_invoke
CStrings:
+ "<oob>"
+ "UIAccessibilityTokenDynamicContentAnnouncement"
+ "_AXInternalRemoveFromElementCache called off the main thread — this indicates a client is releasing AX elements on a background thread (rdar://183478648)"
+ "rdar://159429576 _axUnit word enter position=%ld direction=%d stringLen=%ld tokenizerRange={loc=%ld,len=%ld} string=%{private}@"
+ "rdar://159429576 _axUnit word punctuation-attach initial={loc=%ld,len=%ld} final={loc=%ld,len=%ld} leadingAttached=%ld trailingAttached=%ld resultSubstring=%{private}@"
```
