## AXRuntime

> `/System/Library/PrivateFrameworks/AXRuntime.framework/AXRuntime`

### Sections with Same Size but Changed Content

- `__DATA_CONST.__objc_classlist`
- `__DATA_CONST.__objc_catlist`
- `__DATA_CONST.__objc_protolist`
- `__DATA_CONST.__objc_superrefs`
- `__DATA_CONST.__objc_arraydata`
- `__DATA_CONST.__got`
- `__AUTH_CONST.__const`
- `__AUTH_CONST.__objc_intobj`
- `__AUTH_CONST.__objc_arrayobj`
- `__AUTH_CONST.__objc_doubleobj`
- `__AUTH.__objc_data`
- `__DATA_DIRTY.__objc_data`

```diff

-3237.1.0.0.0
-  __TEXT.__text: 0x4df88
-  __TEXT.__objc_methlist: 0x38f4
-  __TEXT.__const: 0x448
+3240.3.0.0.0
+  __TEXT.__text: 0x4e6dc
+  __TEXT.__objc_methlist: 0x3954
+  __TEXT.__const: 0x458
   __TEXT.__dlopen_cstrs: 0x31a
-  __TEXT.__gcc_except_tab: 0xba4
-  __TEXT.__oslogstring: 0x1535
-  __TEXT.__cstring: 0x5d8e
+  __TEXT.__gcc_except_tab: 0xba0
+  __TEXT.__oslogstring: 0x16f9
+  __TEXT.__cstring: 0x5dc3
   __TEXT.__ustring: 0x4
-  __TEXT.__unwind_info: 0x1350
+  __TEXT.__unwind_info: 0x1390
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0
   __TEXT.__objc_classname: 0x0
   __TEXT.__objc_methname: 0x0
   __TEXT.__objc_methtype: 0x0
-  __DATA_CONST.__const: 0x1270
+  __DATA_CONST.__const: 0x1298
   __DATA_CONST.__objc_classlist: 0xe8
   __DATA_CONST.__objc_catlist: 0x48
   __DATA_CONST.__objc_protolist: 0x28
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x2408
+  __DATA_CONST.__objc_selrefs: 0x2440
   __DATA_CONST.__objc_superrefs: 0xa8
   __DATA_CONST.__objc_arraydata: 0xc0
   __DATA_CONST.__got: 0x2e8
   __AUTH_CONST.__const: 0xbc8
-  __AUTH_CONST.__cfstring: 0x50e0
-  __AUTH_CONST.__objc_const: 0x3a08
+  __AUTH_CONST.__cfstring: 0x5120
+  __AUTH_CONST.__objc_const: 0x3a28
   __AUTH_CONST.__objc_intobj: 0x1650
   __AUTH_CONST.__objc_arrayobj: 0x90
   __AUTH_CONST.__objc_doubleobj: 0x20
-  __AUTH_CONST.__auth_got: 0xaa0
+  __AUTH_CONST.__auth_got: 0xab0
   __AUTH.__objc_data: 0x640
-  __DATA.__objc_ivar: 0x23c
-  __DATA.__data: 0x8b8
-  __DATA.__bss: 0x300
+  __DATA.__objc_ivar: 0x240
+  __DATA.__data: 0x8c0
+  __DATA.__bss: 0x308
   __DATA.__common: 0x30
   __DATA_DIRTY.__objc_data: 0x2d0
   __DATA_DIRTY.__data: 0x50

   - /usr/lib/libAccessibility.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 1638
-  Symbols:   4005
-  CStrings:  947
+  Functions: 1652
+  Symbols:   4031
+  CStrings:  952
 
Symbols:
+ +[AXUIElement uiElementAtCoordinate:forApplication:contextId:displayId:allowSameProcess:coordinateIsInHostedCoordinates:]
+ -[AXElement _convertRectFromWindowCoordinates:]
+ -[AXElementFetcher _fuzzyMatchElement:candidate:]
+ -[AXElementFetcher findElementMatchingElement:allowFuzzyMatch:]
+ -[AXElementGroup _fuzzyMatchItem:candidate:]
+ -[AXElementGroup _unionOfChildFrames]
+ -[AXElementGroup firstDescendantMatchingItem:allowFuzzyMatch:]
+ -[_AXObjectCacheHelper .cxx_destruct]
+ GCC_except_table1178
+ GCC_except_table1330
+ GCC_except_table1333
+ GCC_except_table1362
+ GCC_except_table1379
+ GCC_except_table1393
+ GCC_except_table1471
+ GCC_except_table1499
+ GCC_except_table1546
+ GCC_except_table1607
+ GCC_except_table1615
+ GCC_except_table166
+ GCC_except_table169
+ GCC_except_table185
+ GCC_except_table240
+ GCC_except_table241
+ GCC_except_table259
+ GCC_except_table260
+ GCC_except_table264
+ GCC_except_table268
+ GCC_except_table277
+ GCC_except_table347
+ GCC_except_table349
+ GCC_except_table351
+ GCC_except_table365
+ GCC_except_table453
+ GCC_except_table459
+ GCC_except_table524
+ GCC_except_table545
+ GCC_except_table672
+ GCC_except_table678
+ GCC_except_table765
+ GCC_except_table769
+ GCC_except_table773
+ GCC_except_table783
+ GCC_except_table784
+ GCC_except_table785
+ GCC_except_table786
+ GCC_except_table838
+ GCC_except_table844
+ GCC_except_table919
+ GCC_except_table926
+ GCC_except_table930
+ GCC_except_table932
+ GCC_except_table956
+ GCC_except_table992
+ _AXAIWhiteGloveLoggingEnabled
+ _CGRectContainsRect
+ _OBJC_IVAR_$__AXObjectCacheHelper._weakElement
+ _UIAccessibilityTokenDynamicContentAnnouncement
+ __AXElementFromElementCache
+ __AXUIElementCopyElementAtPositionCommon
+ __AXUIElementCopyElementAtPositionInHostedCoordinatesWithParams
+ ___63-[AXElementFetcher findElementMatchingElement:allowFuzzyMatch:]_block_invoke
+ ____AXElementFromElementCache_block_invoke
+ ____AXUIElementCopyElementAtPositionCommon_block_invoke
+ ___block_descriptor_57_e8_32s40s48r_e5_v8?0ls32l8s40l8r48l8
+ __auditTokenCacheLock
+ _objc_msgSend$_convertRectFromWindowCoordinates:
+ _objc_msgSend$_fuzzyMatchElement:candidate:
+ _objc_msgSend$_fuzzyMatchItem:candidate:
+ _objc_msgSend$_unionOfChildFrames
+ _objc_msgSend$displayIdForContextId:
+ _objc_msgSend$findElementMatchingElement:allowFuzzyMatch:
+ _objc_msgSend$firstDescendantMatchingItem:allowFuzzyMatch:
+ _objc_msgSend$uiElementAtCoordinate:forApplication:contextId:displayId:allowSameProcess:coordinateIsInHostedCoordinates:
- GCC_except_table1169
- GCC_except_table1321
- GCC_except_table1324
- GCC_except_table1353
- GCC_except_table1368
- GCC_except_table1382
- GCC_except_table1460
- GCC_except_table1488
- GCC_except_table1535
- GCC_except_table1593
- GCC_except_table1601
- GCC_except_table164
- GCC_except_table167
- GCC_except_table173
- GCC_except_table238
- GCC_except_table239
- GCC_except_table257
- GCC_except_table258
- GCC_except_table262
- GCC_except_table266
- GCC_except_table275
- GCC_except_table344
- GCC_except_table346
- GCC_except_table358
- GCC_except_table39
- GCC_except_table446
- GCC_except_table452
- GCC_except_table517
- GCC_except_table538
- GCC_except_table665
- GCC_except_table671
- GCC_except_table758
- GCC_except_table762
- GCC_except_table766
- GCC_except_table776
- GCC_except_table777
- GCC_except_table778
- GCC_except_table779
- GCC_except_table822
- GCC_except_table836
- GCC_except_table911
- GCC_except_table914
- GCC_except_table918
- GCC_except_table924
- GCC_except_table948
- GCC_except_table984
- ___47-[AXElementFetcher findElementMatchingElement:]_block_invoke
- ____AXUIElementCopyElementAtPositionWithParams_block_invoke
CStrings:
+ "<oob>"
+ "UIAccessibilityTokenDynamicContentAnnouncement"
+ "_AXInternalRemoveFromElementCache called off the main thread — this indicates a client is releasing AX elements on a background thread (rdar://183478648)"
+ "rdar://159429576 _axUnit word enter position=%ld direction=%d stringLen=%ld tokenizerRange={loc=%ld,len=%ld} string=%{private}@"
+ "rdar://159429576 _axUnit word punctuation-attach initial={loc=%ld,len=%ld} final={loc=%ld,len=%ld} leadingAttached=%ld trailingAttached=%ld resultSubstring=%{private}@"
```
