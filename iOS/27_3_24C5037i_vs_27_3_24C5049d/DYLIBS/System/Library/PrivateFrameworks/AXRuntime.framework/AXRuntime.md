## AXRuntime

> `/System/Library/PrivateFrameworks/AXRuntime.framework/AXRuntime`

```diff

-3245.8.14.0.0
-  __TEXT.__text: 0x4d7c0
-  __TEXT.__objc_methlist: 0x396c
-  __TEXT.__const: 0x458
+3245.8.23.0.0
+  __TEXT.__text: 0x4e054
+  __TEXT.__objc_methlist: 0x39b8
+  __TEXT.__const: 0x468
   __TEXT.__dlopen_cstrs: 0x303
-  __TEXT.__gcc_except_tab: 0xc00
-  __TEXT.__oslogstring: 0x17ea
-  __TEXT.__cstring: 0x5da8
+  __TEXT.__gcc_except_tab: 0xc20
+  __TEXT.__oslogstring: 0x1854
+  __TEXT.__cstring: 0x5db7
   __TEXT.__ustring: 0x4
-  __TEXT.__unwind_info: 0x17c0
+  __TEXT.__unwind_info: 0x17d8
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0
   __TEXT.__objc_classname: 0x0

   __DATA_CONST.__objc_catlist: 0x48
   __DATA_CONST.__objc_protolist: 0x28
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x2450
+  __DATA_CONST.__objc_selrefs: 0x2480
   __DATA_CONST.__objc_superrefs: 0xa8
-  __DATA_CONST.__objc_arraydata: 0xc0
-  __DATA_CONST.__got: 0x2e0
-  __AUTH_CONST.__const: 0xbc8
+  __DATA_CONST.__objc_arraydata: 0xc8
+  __DATA_CONST.__got: 0x2e8
+  __AUTH_CONST.__const: 0xbe8
   __AUTH_CONST.__cfstring: 0x5160
-  __AUTH_CONST.__objc_const: 0x3a28
-  __AUTH_CONST.__objc_intobj: 0x1668
-  __AUTH_CONST.__objc_arrayobj: 0x90
+  __AUTH_CONST.__objc_const: 0x3a30
+  __AUTH_CONST.__objc_intobj: 0x1698
+  __AUTH_CONST.__objc_arrayobj: 0xa8
   __AUTH_CONST.__objc_doubleobj: 0x20
-  __AUTH_CONST.__auth_got: 0xad8
+  __AUTH_CONST.__auth_got: 0xae8
   __AUTH.__objc_data: 0x640
   __DATA.__objc_ivar: 0x240
   __DATA.__data: 0x8d0

   - /usr/lib/libAccessibility.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 1662
-  Symbols:   3276
-  CStrings:  966
+  Functions: 1670
+  Symbols:   3291
+  CStrings:  969
 
Symbols:
+ +[AXClientSideValueTransformer displayIdForSystemDisplayIdentifier:]
+ +[AXUIElement _uiElementAtCoordinate:forApplication:contextId:displayId:allowSameProcess:coordinateIsInHostedCoordinates:hitTestType:prefetchAttributes:]
+ +[AXUIElement uiElementAtCoordinate:displayId:allowSameProcess:prefetchAttributes:]
+ -[AXElement convertPath:frame:fromContextId:displayId:]
+ -[AXUIElement prefetchCachedAttributes]
+ GCC_except_table1006
+ GCC_except_table1190
+ GCC_except_table1192
+ GCC_except_table1346
+ GCC_except_table1349
+ GCC_except_table1378
+ GCC_except_table1395
+ GCC_except_table1410
+ GCC_except_table1488
+ GCC_except_table1516
+ GCC_except_table1563
+ GCC_except_table1624
+ GCC_except_table1633
+ GCC_except_table175
+ GCC_except_table178
+ GCC_except_table194
+ GCC_except_table249
+ GCC_except_table250
+ GCC_except_table268
+ GCC_except_table269
+ GCC_except_table273
+ GCC_except_table277
+ GCC_except_table286
+ GCC_except_table360
+ GCC_except_table374
+ GCC_except_table462
+ GCC_except_table468
+ GCC_except_table533
+ GCC_except_table553
+ GCC_except_table60
+ GCC_except_table680
+ GCC_except_table686
+ GCC_except_table76
+ GCC_except_table774
+ GCC_except_table783
+ GCC_except_table793
+ GCC_except_table794
+ GCC_except_table795
+ GCC_except_table796
+ GCC_except_table844
+ GCC_except_table858
+ GCC_except_table933
+ GCC_except_table936
+ GCC_except_table944
+ GCC_except_table946
+ GCC_except_table970
+ _AXBoundingRectForPoints
+ _AXLogSubsystem
+ _AXRuntimeLogAttributeCacheTracing.log
+ _AXRuntimeLogAttributeCacheTracing.onceToken
+ _CFArrayGetFirstIndexOfValue
+ __AXResolvePairedDisplayId
+ ___55-[AXElement convertPath:frame:fromContextId:displayId:]_block_invoke
+ ___55-[AXElement convertPath:frame:fromContextId:displayId:]_block_invoke_2
+ ___AXRuntimeLogAttributeCacheTracing_block_invoke
+ ___block_descriptor_40_e8_32bs_e32_B32?0"AXRemoteElement"8Q16^B24ls32l8
+ _displayIdForSystemDisplayIdentifier:.DisplayIDsBySystemDisplayIdentifier
+ _displayIdForSystemDisplayIdentifier:.DisplayIDsLock
+ _os_log_create
- GCC_except_table1000
- GCC_except_table1184
- GCC_except_table1186
- GCC_except_table1339
- GCC_except_table1342
- GCC_except_table1371
- GCC_except_table1388
- GCC_except_table1403
- GCC_except_table1481
- GCC_except_table1509
- GCC_except_table1556
- GCC_except_table1617
- GCC_except_table1625
- GCC_except_table173
- GCC_except_table176
- GCC_except_table182
- GCC_except_table247
- GCC_except_table248
- GCC_except_table266
- GCC_except_table267
- GCC_except_table271
- GCC_except_table275
- GCC_except_table284
- GCC_except_table354
- GCC_except_table372
- GCC_except_table460
- GCC_except_table466
- GCC_except_table531
- GCC_except_table551
- GCC_except_table59
- GCC_except_table678
- GCC_except_table684
- GCC_except_table75
- GCC_except_table771
- GCC_except_table775
- GCC_except_table789
- GCC_except_table790
- GCC_except_table791
- GCC_except_table792
- GCC_except_table838
- GCC_except_table846
- GCC_except_table927
- GCC_except_table930
- GCC_except_table934
- GCC_except_table938
- GCC_except_table964
- ___49-[AXElement convertPath:fromContextId:displayId:]_block_invoke
- ___49-[AXElement convertPath:fromContextId:displayId:]_block_invoke_2
- ___block_descriptor_40_e8_32bs_e15_B32?08Q16^B24ls32l8
Functions:
~ _AXUIElementCopyAttributeValueRecursive : 1644 -> 1924
~ _AXUIElementCopyMultipleAttributeValues : 1740 -> 1960
+ __AXResolvePairedDisplayId
+ _AXBoundingRectForPoints
~ +[AXRemoteElement remoteElementsForBlock:] : 268 -> 212
~ +[AXUIElement applyElementAttributeCacheScheme:] : 1612 -> 1620
~ +[AXUIElement uiElementAtCoordinate:forApplication:contextId:displayId:allowSameProcess:coordinateIsInHostedCoordinates:hitTestType:] : 700 -> 40
+ +[AXUIElement _uiElementAtCoordinate:forApplication:contextId:displayId:allowSameProcess:coordinateIsInHostedCoordinates:hitTestType:prefetchAttributes:]
~ +[AXUIElement uiElementAtCoordinate:displayId:allowSameProcess:] : 212 -> 8
+ +[AXUIElement uiElementAtCoordinate:displayId:allowSameProcess:prefetchAttributes:]
~ -[AXUIElement _cachedValueForAttribute:] : 420 -> 440
+ -[AXUIElement prefetchCachedAttributes]
~ -[AXUIElement arrayWithAXAttribute:] : 584 -> 696
~ -[AXUIElement valueArrayWithAXAttributes:] : 588 -> 700
+ ___AXRuntimeLogAttributeCacheTracing_block_invoke
~ -[AXElement convertPath:fromContextId:displayId:] : 404 -> 16
+ -[AXElement convertPath:frame:fromContextId:displayId:]
~ -[AXElement simulateTapWithFingerIndex:withPoint:] : 508 -> 560
+ +[AXClientSideValueTransformer displayIdForSystemDisplayIdentifier:]
CStrings:
+ "DynamicTracing"
+ "System display identifier %{public}@ is display %u"
+ "Unable to resolve system display identifier %{public}@"
```
