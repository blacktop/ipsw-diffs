## AXRuntime

> `/System/Library/PrivateFrameworks/AXRuntime.framework/AXRuntime`

```diff

-3187.1.0.0.0
-  __TEXT.__text: 0x49c54
+3189.2.0.0.0
+  __TEXT.__text: 0x49e4c
   __TEXT.__auth_stubs: 0x14b0
-  __TEXT.__objc_methlist: 0x3698
+  __TEXT.__objc_methlist: 0x36c0
   __TEXT.__const: 0x458
   __TEXT.__cstring: 0x5c26
   __TEXT.__oslogstring: 0x12c1
   __TEXT.__gcc_except_tab: 0xb38
   __TEXT.__ustring: 0x4
   __TEXT.__dlopen_cstrs: 0x31a
-  __TEXT.__unwind_info: 0x13e8
+  __TEXT.__unwind_info: 0x13f0
   __TEXT.__objc_classname: 0x349
-  __TEXT.__objc_methname: 0x7a96
-  __TEXT.__objc_methtype: 0x1380
-  __TEXT.__objc_stubs: 0x5ce0
+  __TEXT.__objc_methname: 0x7ad6
+  __TEXT.__objc_methtype: 0x138b
+  __TEXT.__objc_stubs: 0x5d20
   __DATA_CONST.__got: 0x2d0
   __DATA_CONST.__const: 0x12b8
   __DATA_CONST.__objc_classlist: 0xe0
   __DATA_CONST.__objc_catlist: 0x48
   __DATA_CONST.__objc_protolist: 0x28
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x2250
+  __DATA_CONST.__objc_selrefs: 0x2260
   __DATA_CONST.__objc_superrefs: 0xa8
   __DATA_CONST.__objc_arraydata: 0xc0
   __AUTH_CONST.__auth_got: 0xa68
   __AUTH_CONST.__const: 0xba8
   __AUTH_CONST.__cfstring: 0x4f20
-  __AUTH_CONST.__objc_const: 0x3680
+  __AUTH_CONST.__objc_const: 0x3690
   __AUTH_CONST.__objc_intobj: 0x1620
   __AUTH_CONST.__objc_arrayobj: 0x90
   __AUTH_CONST.__objc_doubleobj: 0x20
   __AUTH.__objc_data: 0x690
   __DATA.__objc_ivar: 0x204
   __DATA.__data: 0x820
-  __DATA.__bss: 0x330
-  __DATA.__common: 0x28
+  __DATA.__bss: 0x338
+  __DATA.__common: 0x24
   __DATA_DIRTY.__objc_data: 0x230
   __DATA_DIRTY.__data: 0x90
   __DATA_DIRTY.__bss: 0x2b0
-  __DATA_DIRTY.__common: 0x10
+  __DATA_DIRTY.__common: 0x18
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/CoreGraphics.framework/CoreGraphics
   - /System/Library/Frameworks/CoreText.framework/CoreText

   - /usr/lib/libAccessibility.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: B26E5926-767C-371F-8EDD-0FAF205B17DF
-  Functions: 1753
-  Symbols:   5748
-  CStrings:  3184
+  UUID: 685CABB6-D969-3F42-9EAF-011E170070F6
+  Functions: 1756
+  Symbols:   5757
+  CStrings:  3187
 
Symbols:
+ -[AXElement focusedOccludedAppSceneIdentifiers]
+ -[AXElementFetcher _occludedAppSceneIdentifiers]
+ -[AXElementGroup indexOfObject:]
+ GCC_except_table119
+ GCC_except_table123
+ GCC_except_table246
+ GCC_except_table54
+ GCC_except_table66
+ GCC_except_table71
+ GCC_except_table77
+ GCC_except_table93
+ __AXDetermineRequestingClient._sIsAST
+ ___35-[AXUIMLElement _currentMLElements]_block_invoke.350
+ ___62+[AXUIMLElement _queue_createMLElements:postDelegateCallback:]_block_invoke.367
+ ___block_literal_global.300
+ ___block_literal_global.313
+ ___block_literal_global.334
+ ___block_literal_global.343
+ ___block_literal_global.345
+ ___block_literal_global.349
+ ___block_literal_global.350
+ ___block_literal_global.366
+ ___block_literal_global.373
+ ___block_literal_global.378
+ _objc_msgSend$_occludedAppSceneIdentifiers
+ _objc_msgSend$focusedOccludedAppSceneIdentifiers
- GCC_except_table118
- GCC_except_table122
- GCC_except_table245
- GCC_except_table53
- GCC_except_table65
- GCC_except_table70
- GCC_except_table76
- GCC_except_table92
- ___35-[AXUIMLElement _currentMLElements]_block_invoke.347
- ___62+[AXUIMLElement _queue_createMLElements:postDelegateCallback:]_block_invoke.364
- ___block_literal_global.294
- ___block_literal_global.310
- ___block_literal_global.331
- ___block_literal_global.337
- ___block_literal_global.342
- ___block_literal_global.346
- ___block_literal_global.347
- ___block_literal_global.363
- ___block_literal_global.370
- ___block_literal_global.372
Functions:
~ __AXDetermineRequestingClient : 160 -> 204
~ ____AXDetermineRequestingClient_block_invoke : 1236 -> 1224
~ _AXConvertOutgoingValue : 5816 -> 5824
+ -[AXElement focusedOccludedAppSceneIdentifiers]
+ -[AXElementFetcher _occludedAppSceneIdentifiers]
~ -[AXElementFetcher _fetchUnprocessedElements:] : 1388 -> 1428
~ -[AXElementFetcher _groupWithItems:groupTraits:scanningBehaviorTraits:label:identifier:currentPid:] : 868 -> 916
~ -[AXElementFetcher _fetchUnprocessedAppGroups] : 1348 -> 1372
+ -[AXElementGroup indexOfObject:]
CStrings:
+ "Q24@0:8@16"
+ "_occludedAppSceneIdentifiers"
+ "focusedOccludedAppSceneIdentifiers"

```
