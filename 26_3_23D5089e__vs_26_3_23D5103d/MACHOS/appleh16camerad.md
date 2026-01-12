## appleh16camerad

> `/usr/sbin/appleh16camerad`

```diff

-5.301.3.0.0
-  __TEXT.__text: 0x835b4
-  __TEXT.__auth_stubs: 0x1fd0
-  __TEXT.__objc_stubs: 0x1440
+5.305.1.0.0
+  __TEXT.__text: 0x83c6c
+  __TEXT.__auth_stubs: 0x2030
+  __TEXT.__objc_stubs: 0x1460
   __TEXT.__init_offsets: 0x14
   __TEXT.__objc_methlist: 0x268
-  __TEXT.__gcc_except_tab: 0x230c
-  __TEXT.__const: 0x2de0
-  __TEXT.__cstring: 0x8b65
+  __TEXT.__gcc_except_tab: 0x233c
+  __TEXT.__const: 0x2e10
+  __TEXT.__cstring: 0x8b81
   __TEXT.__objc_classname: 0x89
-  __TEXT.__oslogstring: 0x5baf
-  __TEXT.__objc_methname: 0x1577
+  __TEXT.__oslogstring: 0x5df3
+  __TEXT.__objc_methname: 0x15c5
   __TEXT.__objc_methtype: 0x10b3
-  __TEXT.__unwind_info: 0x15c0
-  __DATA_CONST.__auth_got: 0xff8
-  __DATA_CONST.__got: 0xbc0
+  __TEXT.__unwind_info: 0x15d8
+  __DATA_CONST.__auth_got: 0x1028
+  __DATA_CONST.__got: 0xbe0
   __DATA_CONST.__auth_ptr: 0x60
-  __DATA_CONST.__const: 0xb170
-  __DATA_CONST.__cfstring: 0x3340
+  __DATA_CONST.__const: 0xb6d0
+  __DATA_CONST.__cfstring: 0x3380
   __DATA_CONST.__objc_classlist: 0x18
   __DATA_CONST.__objc_protolist: 0x18
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_classrefs: 0x50
   __DATA_CONST.__objc_superrefs: 0x18
-  __DATA_CONST.__objc_intobj: 0x120
+  __DATA_CONST.__objc_intobj: 0x138
   __DATA_CONST.__objc_arraydata: 0x58
   __DATA_CONST.__objc_arrayobj: 0x60
   __DATA.__objc_const: 0x5a8
-  __DATA.__objc_selrefs: 0x628
+  __DATA.__objc_selrefs: 0x630
   __DATA.__objc_ivar: 0x34
   __DATA.__objc_data: 0xf0
   __DATA.__data: 0x371d80
-  __DATA.__bss: 0x201
+  __DATA.__bss: 0x231
   __DATA.__common: 0x5c
   - /System/Library/Frameworks/AVFoundation.framework/AVFoundation
   - /System/Library/Frameworks/Accelerate.framework/Accelerate

   - /System/Library/PrivateFrameworks/CoreBrightness.framework/CoreBrightness
   - /System/Library/PrivateFrameworks/CoreRepairCore.framework/CoreRepairCore
   - /System/Library/PrivateFrameworks/GeoServices.framework/GeoServices
+  - /System/Library/PrivateFrameworks/ISPExclaveKitServices.framework/ISPExclaveKitServices
   - /System/Library/PrivateFrameworks/MSUDataAccessor.framework/MSUDataAccessor
   - /System/Library/PrivateFrameworks/PeridotDepth.framework/PeridotDepth
   - /System/Library/PrivateFrameworks/ProtocolBuffer.framework/ProtocolBuffer

   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libtailspin.dylib
   - /usr/lib/libz.1.dylib
-  UUID: FDEDAABC-FF55-3C5A-B999-A8054A2B312F
-  Functions: 1651
-  Symbols:   911
-  CStrings:  2448
+  UUID: 1F309B00-C568-3773-AD33-0C6F7EF4FD0C
+  Functions: 1654
+  Symbols:   921
+  CStrings:  2459
 
Symbols:
+ _CGRectGetMaxX
+ _CGRectGetMaxY
+ _CGRectIsNull
+ _VTSessionSetProperty
+ ___NSDictionary0__struct
+ ___cxa_guard_acquire
+ ___cxa_guard_release
+ _kCVPixelBufferBytesPerRowAlignmentKey
+ _kVTPixelTransferPropertyKey_DestinationRectangle
+ _kVTPixelTransferPropertyKey_SourceCropRectangle
CStrings:
+ "\tInvalid device\n"
+ "5.305.1"
+ "ERR: PDAF:Incorrect offset for ShiftMap (%d %d), ShiftMapAccumulate is returned to avoid outofbound access\n"
+ "ERR: PDAF:Incorrect shiftmap offsets (%d %d %d %d), ShiftMapAccumulate is returned to avoid outofbound access\n"
+ "ERR: ZF:Incorrect offset for ShiftMap (%d %d), ShiftMapAccumulate is returned to avoid outofbound access\n"
+ "ERR: ZF:Incorrect shiftmap offsets (%d %d %d %d), ShiftMapAccumulate is returned to avoid outofbound access\n"
+ "Pearl Calibration (MI): Color is cropped and not aligned with Pearl. Can't run.\n"
+ "Pearl Calibration (MI): Failed to allocate cropped color buffer\n"
+ "RunForRGBP"
+ "calcSensorCrop:onImageWithDimensions:metadataDictionary:negativeCropHandling:"
- "5.301.3"

```
