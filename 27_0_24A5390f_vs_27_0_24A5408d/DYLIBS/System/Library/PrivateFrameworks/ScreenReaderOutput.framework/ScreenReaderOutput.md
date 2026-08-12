## ScreenReaderOutput

> `/System/Library/PrivateFrameworks/ScreenReaderOutput.framework/ScreenReaderOutput`

```diff

-462.0.0.0.0
-  __TEXT.__text: 0x9c970
-  __TEXT.__objc_methlist: 0x9000
+465.0.0.0.0
+  __TEXT.__text: 0x9cbf0
+  __TEXT.__objc_methlist: 0x9008
   __TEXT.__const: 0x183c
-  __TEXT.__cstring: 0x5a33
+  __TEXT.__cstring: 0x5b79
   __TEXT.__swift5_typeref: 0xeec
   __TEXT.__constg_swiftt: 0x960
   __TEXT.__swift5_builtin: 0xb4

   __TEXT.__objc_classname: 0x0
   __TEXT.__objc_methname: 0x0
   __TEXT.__objc_methtype: 0x0
-  __DATA_CONST.__const: 0x1248
+  __DATA_CONST.__const: 0x1270
   __DATA_CONST.__objc_classlist: 0x328
   __DATA_CONST.__objc_catlist: 0x28
   __DATA_CONST.__objc_protolist: 0x140
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x4770
+  __DATA_CONST.__objc_selrefs: 0x4780
   __DATA_CONST.__objc_protorefs: 0x48
   __DATA_CONST.__objc_superrefs: 0x210
   __DATA_CONST.__objc_arraydata: 0x380
   __DATA_CONST.__got: 0x790
   __AUTH_CONST.__const: 0x32a0
-  __AUTH_CONST.__cfstring: 0x54c0
+  __AUTH_CONST.__cfstring: 0x5680
   __AUTH_CONST.__objc_const: 0xbc58
-  __AUTH_CONST.__objc_intobj: 0xa38
+  __AUTH_CONST.__objc_intobj: 0xa68
   __AUTH_CONST.__objc_dictobj: 0xa0
   __AUTH_CONST.__objc_doubleobj: 0x10
   __AUTH_CONST.__objc_arrayobj: 0x18
-  __AUTH_CONST.__auth_got: 0x1098
+  __AUTH_CONST.__auth_got: 0x10a8
   __AUTH.__objc_data: 0x360
   __AUTH.__data: 0x80
   __DATA.__objc_ivar: 0x8c8

   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  Functions: 3973
-  Symbols:   7775
-  CStrings:  1062
+  Functions: 3974
+  Symbols:   7779
+  CStrings:  1077
 
Symbols:
+ -[SCROBrailleDisplayManager _eventQueue_begin]
+ GCC_except_table1203
+ GCC_except_table1210
+ GCC_except_table1332
+ GCC_except_table1537
+ GCC_except_table1657
+ GCC_except_table1796
+ GCC_except_table1798
+ GCC_except_table1806
+ GCC_except_table1816
+ GCC_except_table1900
+ GCC_except_table1945
+ GCC_except_table1949
+ GCC_except_table2061
+ GCC_except_table2082
+ GCC_except_table2087
+ GCC_except_table2093
+ GCC_except_table2192
+ GCC_except_table2379
+ GCC_except_table2397
+ GCC_except_table2515
+ GCC_except_table2519
+ GCC_except_table2528
+ GCC_except_table2532
+ GCC_except_table2536
+ GCC_except_table2541
+ GCC_except_table2543
+ GCC_except_table2546
+ GCC_except_table2890
+ GCC_except_table2906
+ GCC_except_table2927
+ GCC_except_table2990
+ GCC_except_table2992
+ GCC_except_table2995
+ GCC_except_table2997
+ GCC_except_table2999
+ _archive_read_close
+ _archive_read_free
+ _objc_msgSend$panFocusRequestToken
- GCC_except_table1202
- GCC_except_table1209
- GCC_except_table1331
- GCC_except_table1536
- GCC_except_table1656
- GCC_except_table1795
- GCC_except_table1797
- GCC_except_table1805
- GCC_except_table1815
- GCC_except_table1899
- GCC_except_table1944
- GCC_except_table1948
- GCC_except_table2060
- GCC_except_table2081
- GCC_except_table2086
- GCC_except_table2092
- GCC_except_table2191
- GCC_except_table2378
- GCC_except_table2396
- GCC_except_table2512
- GCC_except_table2518
- GCC_except_table2523
- GCC_except_table2529
- GCC_except_table2535
- GCC_except_table2540
- GCC_except_table2542
- GCC_except_table2545
- GCC_except_table2889
- GCC_except_table2905
- GCC_except_table2924
- GCC_except_table2989
- GCC_except_table2991
- GCC_except_table2993
- GCC_except_table2996
- GCC_except_table2998
Functions:
~ -[SCROBrailleDisplay _structuredBraillePanHandler:] : 380 -> 388
+ -[SCROBrailleDisplayManager _eventQueue_begin]
~ -[SCROBrailleDisplayManager _eventQueue_brailleDisplayDriverDidLoad:] : 2296 -> 2324
~ ___60-[SCROMobileBrailleDisplayInputManager _commandForHidUsage:]_block_invoke : 1652 -> 1700
~ -[SCROMobileBrailleDisplayInputManager buttonNamesForInputIdentifier:forDisplayWithToken:] : 1464 -> 1916
~ -[SCROServer _ensureResourcesExist] : 980 -> 932
CStrings:
+ "%d%@"
+ "HID.direction.center"
+ "HID.direction.down"
+ "HID.direction.left"
+ "HID.direction.right"
+ "HID.direction.up"
+ "HID.dpad.key"
+ "HID.dpad.numbered.key"
+ "HID.joystick.direction.key"
+ "HID.joystick.direction.numbered.key"
+ "HID.zoom.in"
+ "HID.zoom.out"
+ "VOTEventCommandBraille2DZoomIn"
+ "VOTEventCommandBraille2DZoomOut"
+ "com.apple.scrod.braille.display.active"
```
