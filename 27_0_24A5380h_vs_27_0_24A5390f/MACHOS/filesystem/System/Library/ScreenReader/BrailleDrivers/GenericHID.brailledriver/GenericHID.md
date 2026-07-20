## GenericHID

> `/System/Library/ScreenReader/BrailleDrivers/GenericHID.brailledriver/GenericHID`

### Sections with Same Size but Changed Content

- `__DATA_CONST.__cfstring`
- `__DATA_CONST.__objc_protolist`
- `__DATA_CONST.__objc_protorefs`
- `__DATA_CONST.__objc_superrefs`
- `__DATA.__data`

```diff

-460.0.0.0.0
-  __TEXT.__text: 0x47a4
-  __TEXT.__auth_stubs: 0x480
-  __TEXT.__objc_stubs: 0xbe0
-  __TEXT.__objc_methlist: 0x59c
-  __TEXT.__const: 0x40
-  __TEXT.__cstring: 0x202
-  __TEXT.__objc_classname: 0x8b
-  __TEXT.__objc_methname: 0xc49
-  __TEXT.__objc_methtype: 0x2c8
-  __TEXT.__oslogstring: 0x4f7
-  __TEXT.__unwind_info: 0x100
-  __DATA_CONST.__const: 0x110
+462.0.0.0.0
+  __TEXT.__text: 0x4ee8
+  __TEXT.__auth_stubs: 0x4b0
+  __TEXT.__objc_stubs: 0xec0
+  __TEXT.__objc_methlist: 0x6a4
+  __TEXT.__const: 0x48
+  __TEXT.__cstring: 0x1ef
+  __TEXT.__objc_classname: 0xa6
+  __TEXT.__objc_methname: 0xfd7
+  __TEXT.__objc_methtype: 0x310
+  __TEXT.__oslogstring: 0x571
+  __TEXT.__unwind_info: 0x118
+  __DATA_CONST.__const: 0xa8
   __DATA_CONST.__cfstring: 0x1c0
-  __DATA_CONST.__objc_classlist: 0x10
+  __DATA_CONST.__objc_classlist: 0x18
   __DATA_CONST.__objc_protolist: 0x28
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_protorefs: 0x8
   __DATA_CONST.__objc_superrefs: 0x8
-  __DATA_CONST.__objc_intobj: 0x408
-  __DATA_CONST.__objc_arraydata: 0x270
-  __DATA_CONST.__objc_dictobj: 0xc8
-  __DATA_CONST.__objc_arrayobj: 0x108
-  __DATA_CONST.__auth_got: 0x248
-  __DATA_CONST.__got: 0x90
-  __DATA.__objc_const: 0x890
-  __DATA.__objc_selrefs: 0x458
-  __DATA.__objc_ivar: 0x78
-  __DATA.__objc_data: 0xa0
+  __DATA_CONST.__objc_intobj: 0x288
+  __DATA_CONST.__objc_arraydata: 0x1c8
+  __DATA_CONST.__objc_dictobj: 0xf0
+  __DATA_CONST.__objc_arrayobj: 0xd8
+  __DATA_CONST.__auth_got: 0x260
+  __DATA_CONST.__got: 0x98
+  __DATA.__objc_const: 0x9d8
+  __DATA.__objc_selrefs: 0x570
+  __DATA.__objc_ivar: 0x8c
+  __DATA.__objc_data: 0xf0
   __DATA.__data: 0x1f8
-  __DATA.__bss: 0x10
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/Foundation.framework/Foundation
   - /System/Library/Frameworks/IOKit.framework/Versions/A/IOKit

   - /System/Library/PrivateFrameworks/ScreenReaderOutput.framework/ScreenReaderOutput
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 70
-  Symbols:   99
-  CStrings:  284
+  Functions: 89
+  Symbols:   105
+  CStrings:  331
 
Symbols:
+ _IOHIDDeviceSetReport
+ _IOHIDElementGetReportID
+ _OBJC_CLASS_$_NSMutableData
+ _OBJC_CLASS_$_SCRO2DBrailleCanvas
+ _OBJC_CLASS_$_SCRO2DBrailleCanvasDescriptor
+ _OBJC_METACLASS_$_SCRO2DBrailleCanvas
+ _objc_alloc
+ _objc_retainAutorelease
+ _objc_retainAutoreleaseReturnValue
- _OBJC_CLASS_$_NSMutableIndexSet
- _dispatch_once
- _objc_retain_x21
CStrings:
+ "@\"SCRO2DBrailleCanvas\""
+ "@32@0:8Q16Q24"
+ "C"
+ "Failed to send tactile graphics report (result: 0x%x)"
+ "SCROMonarch2DBrailleCanvas"
+ "TI,N,V_groupOrdinal"
+ "Tactile graphics canvas ready: %ld x %ld pins, output reportID 0x%x"
+ "^{__IOHIDElement=}16@0:8"
+ "_assignGroupOrdinalsToControls:"
+ "_brailleCellsPerRow"
+ "_canvas"
+ "_copyTactileGraphicsPinOutputElement"
+ "_groupOrdinal"
+ "_setupTactileGraphicsCanvas"
+ "_tactileGraphicsHeight"
+ "_tactileGraphicsReportID"
+ "_tactileGraphicsWidth"
+ "appendBytes:length:"
+ "appendData:"
+ "brailleCellData"
+ "bytes"
+ "containsObject:"
+ "d16@0:8"
+ "dataWithCapacity:"
+ "detentCount"
+ "groupOrdinal"
+ "hasConsistentHorizontalPinSpacing"
+ "hasConsistentVerticalPinSpacing"
+ "horizontalPinSpacing"
+ "initWithCanvasDescriptor:"
+ "initWithWidth:height:"
+ "interCellHorizontalSpacing"
+ "interCellVerticalSpacing"
+ "modelIdentifierForPlist"
+ "pinHeightStyle"
+ "setCellHeight:"
+ "setCellWidth:"
+ "setDetentCount:"
+ "setGroupOrdinal:"
+ "setHasConsistentHorizontalPinSpacing:"
+ "setHasConsistentVerticalPinSpacing:"
+ "setHeight:"
+ "setHorizontalPinSpacing:"
+ "setInterCellHorizontalSpacing:"
+ "setInterCellVerticalSpacing:"
+ "setPinHeightStyle:"
+ "setSkipPinBetweenCellsHorizontally:"
+ "setSkipPinBetweenCellsVertically:"
+ "setVerticalPinSpacing:"
+ "setWidth:"
+ "skipPinBetweenCellsHorizontally"
+ "skipPinBetweenCellsVertically"
+ "supportsBrailleText"
+ "verticalPinSpacing"
- "enumerateIndexesUsingBlock:"
- "indexSetWithIndexesInRange:"
- "removeIndex:"
- "removeIndexesInRange:"
- "removeObjectsInArray:"
- "v24@?0Q8^B16"
- "v8@?0"
```
