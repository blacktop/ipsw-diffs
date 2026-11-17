## BackBoardHIDTouchEventProcessor

> `/System/Library/PrivateFrameworks/BackBoardHIDTouchEventProcessor.framework/BackBoardHIDTouchEventProcessor`

```diff

-877.3.5.0.0
-  __TEXT.__text: 0x5a92c
+877.3.9.0.0
+  __TEXT.__text: 0x5b040
   __TEXT.__objc_methlist: 0x3a10
   __TEXT.__const: 0x480
   __TEXT.__constg_swiftt: 0x124

   __TEXT.__cstring: 0x3514
   __TEXT.__swift5_types: 0x14
   __TEXT.__swift5_protos: 0x4
-  __TEXT.__gcc_except_tab: 0x5738
-  __TEXT.__oslogstring: 0x4849
+  __TEXT.__gcc_except_tab: 0x5898
+  __TEXT.__oslogstring: 0x4873
   __TEXT.__ustring: 0xc
-  __TEXT.__unwind_info: 0x1ea8
+  __TEXT.__unwind_info: 0x1ec8
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0
   __TEXT.__objc_classname: 0x0
   __TEXT.__objc_methname: 0x0
   __TEXT.__objc_methtype: 0x0
-  __DATA_CONST.__const: 0x1c60
+  __DATA_CONST.__const: 0x1c88
   __DATA_CONST.__objc_classlist: 0x2f8
   __DATA_CONST.__objc_catlist: 0x8
   __DATA_CONST.__objc_protolist: 0x158
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x2710
+  __DATA_CONST.__objc_selrefs: 0x2718
   __DATA_CONST.__objc_protorefs: 0x40
   __DATA_CONST.__objc_superrefs: 0x218
   __DATA_CONST.__objc_arraydata: 0x10

   __DATA.__data: 0x1028
   __DATA.__common: 0x1
   __DATA_DIRTY.__objc_data: 0x1220
-  __DATA_DIRTY.__bss: 0x58
+  __DATA_DIRTY.__bss: 0x50
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/CoreGraphics.framework/CoreGraphics
   - /System/Library/Frameworks/CoreText.framework/CoreText

   - /usr/lib/swift/libswiftXPC.dylib
   - /usr/lib/swift/libswift_Builtin_float.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  Functions: 1601
-  Symbols:   4003
+  Functions: 1605
+  Symbols:   4010
   CStrings:  986
 
Symbols:
+ -[BKDirectTouchState _detachedPathLocationsToDeliverThroughTouchDeliveryPolicyCancel:destination:]
+ -[BKDirectTouchState _touchIdentifiersToCancelForTouchDeliveryPolicyInDestination:]
+ -[BKTouchContactSet contactSetByAddingContactsFromSet:]
+ GCC_except_table1163
+ GCC_except_table1168
+ GCC_except_table1169
+ GCC_except_table1174
+ GCC_except_table1176
+ GCC_except_table1181
+ GCC_except_table1182
+ GCC_except_table1183
+ GCC_except_table1202
+ GCC_except_table1271
+ GCC_except_table1272
+ GCC_except_table1273
+ GCC_except_table1277
+ GCC_except_table1347
+ GCC_except_table1351
+ GCC_except_table1376
+ GCC_except_table1395
+ GCC_except_table1396
+ GCC_except_table1472
+ GCC_except_table1480
+ GCC_except_table1482
+ GCC_except_table1483
+ GCC_except_table1485
+ GCC_except_table1501
+ ___140-[BKDirectTouchState _appendSubsetOfHIDCollection:forDestination:toEventPoster:systemGestureIsPossible:pathLocations:initialTouchTimestamp:]_block_invoke
+ ___block_descriptor_40_ea8_32s_e24_B16?0"BKTouchContact"8ls32l8
- GCC_except_table1165
- GCC_except_table1166
- GCC_except_table1171
- GCC_except_table1172
- GCC_except_table1179
- GCC_except_table1180
- GCC_except_table1199
- GCC_except_table1261
- GCC_except_table1262
- GCC_except_table1263
- GCC_except_table1274
- GCC_except_table1344
- GCC_except_table1348
- GCC_except_table1373
- GCC_except_table1392
- GCC_except_table1393
- GCC_except_table1468
- GCC_except_table1473
- GCC_except_table1476
- GCC_except_table1478
- GCC_except_table1479
- GCC_except_table1497
CStrings:
+ "(Synth) TDPS said this context should cancel: %{public}@ (touches %{public}@)"
+ "TDPS said this context should cancel: %{public}@ (touches %{public}@)"
- "(Synth) TDPS said this context should cancel: %{public}@"
- "TDPS said this context should cancel: %{public}@"
```
