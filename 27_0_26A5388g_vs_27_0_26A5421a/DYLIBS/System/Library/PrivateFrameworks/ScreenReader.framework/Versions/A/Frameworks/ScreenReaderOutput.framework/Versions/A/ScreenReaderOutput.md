## ScreenReaderOutput

> `/System/Library/PrivateFrameworks/ScreenReader.framework/Versions/A/Frameworks/ScreenReaderOutput.framework/Versions/A/ScreenReaderOutput`

```diff

-1045.0.0.0.0
-  __TEXT.__text: 0xa7718
-  __TEXT.__objc_methlist: 0x93c0
+1048.3.0.0.0
+  __TEXT.__text: 0xa7b70
+  __TEXT.__objc_methlist: 0x93d0
   __TEXT.__const: 0x1938
-  __TEXT.__cstring: 0x643b
+  __TEXT.__cstring: 0x6581
   __TEXT.__swift5_typeref: 0xeec
   __TEXT.__constg_swiftt: 0x960
   __TEXT.__swift5_builtin: 0xb4

   __TEXT.__objc_classname: 0x0
   __TEXT.__objc_methname: 0x0
   __TEXT.__objc_methtype: 0x0
-  __DATA_CONST.__const: 0x340
+  __DATA_CONST.__const: 0x390
   __DATA_CONST.__objc_classlist: 0x338
   __DATA_CONST.__objc_catlist: 0x28
   __DATA_CONST.__objc_protolist: 0x140
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x4938
+  __DATA_CONST.__objc_selrefs: 0x4948
   __DATA_CONST.__objc_protorefs: 0x48
   __DATA_CONST.__objc_superrefs: 0x218
   __DATA_CONST.__objc_arraydata: 0x3f8
   __DATA_CONST.__got: 0x808
   __AUTH_CONST.__const: 0x44e8
-  __AUTH_CONST.__cfstring: 0x6320
+  __AUTH_CONST.__cfstring: 0x64e0
   __AUTH_CONST.__objc_const: 0xc148
-  __AUTH_CONST.__objc_intobj: 0x11e8
+  __AUTH_CONST.__objc_intobj: 0x1218
   __AUTH_CONST.__objc_dictobj: 0xa0
   __AUTH_CONST.__objc_doubleobj: 0x10
   __AUTH_CONST.__objc_arrayobj: 0x60
-  __AUTH_CONST.__auth_got: 0xee0
+  __AUTH_CONST.__auth_got: 0xef0
   __AUTH.__objc_data: 0x400
   __AUTH.__data: 0x70
   __DATA.__objc_ivar: 0x90c

   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  Functions: 4082
-  Symbols:   7918
-  CStrings:  1167
+  Functions: 4083
+  Symbols:   7922
+  CStrings:  1182
 
Symbols:
+ -[SCROBrailleDisplayManager _eventQueue_begin]
+ GCC_except_table1296
+ GCC_except_table1303
+ GCC_except_table1425
+ GCC_except_table1630
+ GCC_except_table1752
+ GCC_except_table1893
+ GCC_except_table1895
+ GCC_except_table1904
+ GCC_except_table1916
+ GCC_except_table2000
+ GCC_except_table2045
+ GCC_except_table2051
+ GCC_except_table2165
+ GCC_except_table2186
+ GCC_except_table2195
+ GCC_except_table2203
+ GCC_except_table2306
+ GCC_except_table2490
+ GCC_except_table2511
+ GCC_except_table2623
+ GCC_except_table2627
+ GCC_except_table2636
+ GCC_except_table2640
+ GCC_except_table2644
+ GCC_except_table2649
+ GCC_except_table2651
+ GCC_except_table2654
+ GCC_except_table2998
+ GCC_except_table3016
+ GCC_except_table3037
+ GCC_except_table3100
+ GCC_except_table3102
+ GCC_except_table3105
+ GCC_except_table3107
+ GCC_except_table3109
+ _archive_read_close
+ _archive_read_free
+ _objc_msgSend$panFocusRequestToken
- GCC_except_table1295
- GCC_except_table1302
- GCC_except_table1424
- GCC_except_table1629
- GCC_except_table1751
- GCC_except_table1892
- GCC_except_table1894
- GCC_except_table1903
- GCC_except_table1915
- GCC_except_table1999
- GCC_except_table2044
- GCC_except_table2050
- GCC_except_table2164
- GCC_except_table2185
- GCC_except_table2194
- GCC_except_table2202
- GCC_except_table2305
- GCC_except_table2489
- GCC_except_table2510
- GCC_except_table2620
- GCC_except_table2626
- GCC_except_table2631
- GCC_except_table2637
- GCC_except_table2643
- GCC_except_table2648
- GCC_except_table2650
- GCC_except_table2653
- GCC_except_table2997
- GCC_except_table3015
- GCC_except_table3034
- GCC_except_table3099
- GCC_except_table3101
- GCC_except_table3103
- GCC_except_table3106
- GCC_except_table3108
Functions:
~ -[SCROBrailleDisplay _structuredBraillePanHandler:] : 400 -> 396
~ -[SCROBrailleDisplayInputManager buttonNameForInputIdentifier:forDisplayWithToken:] : 1880 -> 2348
+ -[SCROBrailleDisplayManager _eventQueue_begin]
~ -[SCROBrailleDisplayManager _eventQueue_brailleDisplayDriverDidLoad:] : 2272 -> 2304
~ ___60-[SCROMobileBrailleDisplayInputManager _commandForHidUsage:]_block_invoke : 1656 -> 1704
~ -[SCROMobileBrailleDisplayInputManager buttonNamesForInputIdentifier:forDisplayWithToken:] : 1552 -> 2020
~ -[SCROServer _ensureResourcesExist] : 1024 -> 972
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
