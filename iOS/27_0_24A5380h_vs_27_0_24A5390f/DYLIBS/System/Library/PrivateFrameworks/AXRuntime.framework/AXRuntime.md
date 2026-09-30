## AXRuntime

> `/System/Library/PrivateFrameworks/AXRuntime.framework/AXRuntime`

### Sections with Same Size but Changed Content

- `__TEXT.__objc_methlist`
- `__TEXT.__gcc_except_tab`
- `__TEXT.__unwind_info`
- `__DATA_CONST.__objc_classlist`
- `__DATA_CONST.__objc_catlist`
- `__DATA_CONST.__objc_protolist`
- `__DATA_CONST.__objc_selrefs`
- `__DATA_CONST.__objc_superrefs`
- `__DATA_CONST.__objc_arraydata`
- `__DATA_CONST.__got`
- `__AUTH_CONST.__const`
- `__AUTH_CONST.__objc_const`
- `__AUTH_CONST.__objc_intobj`
- `__AUTH_CONST.__objc_arrayobj`
- `__AUTH_CONST.__objc_doubleobj`
- `__AUTH.__objc_data`
- `__DATA.__data`
- `__DATA_DIRTY.__objc_data`

```diff

-3234.5.0.0.0
-  __TEXT.__text: 0x4df30
+3237.1.0.0.0
+  __TEXT.__text: 0x4df88
   __TEXT.__objc_methlist: 0x38f4
   __TEXT.__const: 0x448
   __TEXT.__dlopen_cstrs: 0x31a
   __TEXT.__gcc_except_tab: 0xba4
   __TEXT.__oslogstring: 0x1535
-  __TEXT.__cstring: 0x5d6e
+  __TEXT.__cstring: 0x5d8e
   __TEXT.__ustring: 0x4
   __TEXT.__unwind_info: 0x1350
   __TEXT.__objc_stubs: 0x0

   __TEXT.__objc_classname: 0x0
   __TEXT.__objc_methname: 0x0
   __TEXT.__objc_methtype: 0x0
-  __DATA_CONST.__const: 0x1260
+  __DATA_CONST.__const: 0x1270
   __DATA_CONST.__objc_classlist: 0xe8
   __DATA_CONST.__objc_catlist: 0x48
   __DATA_CONST.__objc_protolist: 0x28

   __DATA_CONST.__objc_arraydata: 0xc0
   __DATA_CONST.__got: 0x2e8
   __AUTH_CONST.__const: 0xbc8
-  __AUTH_CONST.__cfstring: 0x50a0
+  __AUTH_CONST.__cfstring: 0x50e0
   __AUTH_CONST.__objc_const: 0x3a08
   __AUTH_CONST.__objc_intobj: 0x1650
   __AUTH_CONST.__objc_arrayobj: 0x90
   __AUTH_CONST.__objc_doubleobj: 0x20
-  __AUTH_CONST.__auth_got: 0xa98
+  __AUTH_CONST.__auth_got: 0xaa0
   __AUTH.__objc_data: 0x640
   __DATA.__objc_ivar: 0x23c
   __DATA.__data: 0x8b8

   - /usr/lib/libAccessibility.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 1637
-  Symbols:   4001
-  CStrings:  945
+  Functions: 1638
+  Symbols:   4005
+  CStrings:  947
 
Symbols:
+ GCC_except_table1169
+ GCC_except_table1321
+ GCC_except_table1324
+ GCC_except_table1353
+ GCC_except_table1368
+ GCC_except_table1382
+ GCC_except_table1460
+ GCC_except_table1488
+ GCC_except_table1535
+ GCC_except_table1593
+ GCC_except_table1601
+ GCC_except_table164
+ GCC_except_table167
+ GCC_except_table173
+ GCC_except_table175
+ GCC_except_table177
+ GCC_except_table179
+ GCC_except_table181
+ GCC_except_table183
+ GCC_except_table239
+ GCC_except_table258
+ GCC_except_table262
+ GCC_except_table266
+ GCC_except_table275
+ GCC_except_table344
+ GCC_except_table346
+ GCC_except_table358
+ GCC_except_table446
+ GCC_except_table452
+ GCC_except_table517
+ GCC_except_table538
+ GCC_except_table665
+ GCC_except_table671
+ GCC_except_table758
+ GCC_except_table762
+ GCC_except_table766
+ GCC_except_table779
+ GCC_except_table822
+ GCC_except_table830
+ GCC_except_table836
+ GCC_except_table911
+ GCC_except_table914
+ GCC_except_table918
+ GCC_except_table922
+ GCC_except_table924
+ GCC_except_table948
+ GCC_except_table984
+ _AXIsInternalInstall
+ _AXUIAccessibilitySpeechAttributeSSML
+ __AXRaiseIfCallingAXRuntimeOffMainThread
+ _kAXSimulatePressAtPointActionKeyDisplayID
- GCC_except_table1168
- GCC_except_table1320
- GCC_except_table1323
- GCC_except_table1352
- GCC_except_table1367
- GCC_except_table1381
- GCC_except_table1459
- GCC_except_table1487
- GCC_except_table1534
- GCC_except_table1592
- GCC_except_table1600
- GCC_except_table163
- GCC_except_table166
- GCC_except_table172
- GCC_except_table174
- GCC_except_table176
- GCC_except_table178
- GCC_except_table180
- GCC_except_table182
- GCC_except_table237
- GCC_except_table256
- GCC_except_table261
- GCC_except_table265
- GCC_except_table274
- GCC_except_table343
- GCC_except_table345
- GCC_except_table357
- GCC_except_table445
- GCC_except_table451
- GCC_except_table516
- GCC_except_table537
- GCC_except_table664
- GCC_except_table670
- GCC_except_table757
- GCC_except_table761
- GCC_except_table765
- GCC_except_table775
- GCC_except_table821
- GCC_except_table829
- GCC_except_table835
- GCC_except_table910
- GCC_except_table913
- GCC_except_table917
- GCC_except_table921
- GCC_except_table923
- GCC_except_table947
- GCC_except_table983
Functions:
~ __AXUIElementCopyElementAtPositionWithParams : 4040 -> 4052
+ __AXRaiseIfCallingAXRuntimeOffMainThread
~ __handleNonMainThreadCallback : 376 -> 232
~ __AXAddToElementCache : 272 -> 276
~ -[AXRemoteElement _getRemoteValuesOffMainThread:] : 476 -> 480
~ ___49-[AXRemoteElement _getRemoteValuesOffMainThread:]_block_invoke_2 : 136 -> 132
CStrings:
+ "AXSpeechAttributeSSML"
+ "displayID"
```
