## GenericHID

> `/System/Library/ScreenReader/BrailleDrivers/GenericHID.brailledriver/GenericHID`

```diff

-423.0.0.0.0
-  __TEXT.__text: 0x3574
-  __TEXT.__auth_stubs: 0x420
-  __TEXT.__objc_stubs: 0x980
-  __TEXT.__objc_methlist: 0x4dc
+424.2.0.0.0
+  __TEXT.__text: 0x4060
+  __TEXT.__auth_stubs: 0x460
+  __TEXT.__objc_stubs: 0xb20
+  __TEXT.__objc_methlist: 0x574
   __TEXT.__const: 0x40
-  __TEXT.__cstring: 0x1a8
-  __TEXT.__objc_classname: 0x8e
-  __TEXT.__objc_methname: 0xa09
-  __TEXT.__objc_methtype: 0x251
-  __TEXT.__oslogstring: 0x325
-  __TEXT.__unwind_info: 0xd8
-  __DATA_CONST.__auth_got: 0x218
-  __DATA_CONST.__got: 0x78
+  __TEXT.__cstring: 0x1fb
+  __TEXT.__objc_classname: 0x8f
+  __TEXT.__objc_methname: 0xb7a
+  __TEXT.__objc_methtype: 0x2ac
+  __TEXT.__oslogstring: 0x421
+  __TEXT.__unwind_info: 0x108
+  __DATA_CONST.__auth_got: 0x238
+  __DATA_CONST.__got: 0x88
   __DATA_CONST.__const: 0x110
-  __DATA_CONST.__cfstring: 0x160
+  __DATA_CONST.__cfstring: 0x1a0
   __DATA_CONST.__objc_classlist: 0x10
   __DATA_CONST.__objc_protolist: 0x28
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_protorefs: 0x8
   __DATA_CONST.__objc_superrefs: 0x8
   __DATA_CONST.__objc_intobj: 0x3f0
-  __DATA_CONST.__objc_arraydata: 0x230
+  __DATA_CONST.__objc_arraydata: 0x250
   __DATA_CONST.__objc_dictobj: 0xa0
-  __DATA_CONST.__objc_arrayobj: 0xd8
-  __DATA.__objc_const: 0x7a0
-  __DATA.__objc_selrefs: 0x3b8
-  __DATA.__objc_ivar: 0x64
+  __DATA_CONST.__objc_arrayobj: 0x108
+  __DATA.__objc_const: 0x840
+  __DATA.__objc_selrefs: 0x430
+  __DATA.__objc_ivar: 0x70
   __DATA.__objc_data: 0xa0
   __DATA.__data: 0x1f0
   __DATA.__bss: 0x10

   - /System/Library/PrivateFrameworks/ScreenReaderOutput.framework/ScreenReaderOutput
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 06C9B5AD-1287-36EE-9D87-566C96F386B8
-  Functions: 60
-  Symbols:   91
-  CStrings:  252
+  UUID: 27503B9A-5A2F-36DC-A634-DD4D99D4E7FE
+  Functions: 70
+  Symbols:   97
+  CStrings:  283
 
Symbols:
+ _OBJC_CLASS_$_NSAssertionHandler
+ _free
+ _kSCROBrailleUnicodeCharacterBase
+ _malloc_type_calloc
+ _objc_retain_x22
+ _objc_retain_x8
CStrings:
+ "@\"NSArray\""
+ "A row of Braille display does not support 8 dots, has maximum range of - %ld"
+ "Found less number of cells in the row %@ than was initially reported. Truncating to %@"
+ "Found less number of rows than was initially reported (%@). Ignoring remaining elements"
+ "Non-unicode character has been passed to setMainCellsArray."
+ "SCROGenericHIDDriver.m"
+ "Tq,R,N"
+ "_calculateMinRowSize:"
+ "_flushCells:withLength:forElement:"
+ "_parseElementsForUsages:intoArray:"
+ "_parseRowConfiguration"
+ "_physicalMainSizeArray"
+ "_physicalRowSize"
+ "_rowCount"
+ "characterAtIndex:"
+ "currentHandler"
+ "handleFailureInMethod:object:file:lineNumber:description:"
+ "integerValue"
+ "length"
+ "numberWithInteger:"
+ "q24@0:8@16"
+ "rowCount"
+ "rowSize"
+ "rowSizeArray"
+ "setMainCellsArray:"
+ "shouldUseMultiRow"
+ "v24@0:8@\"NSArray\"16"
+ "v32@0:8@16@24"
+ "v40@0:8r*16q24^{__IOHIDElement=}32"

```
