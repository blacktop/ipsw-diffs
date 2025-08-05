## ImageIO

> `/System/Library/Frameworks/ImageIO.framework/ImageIO`

```diff

-2769.0.4.0.0
-  __TEXT.__text: 0x3a1278
-  __TEXT.__auth_stubs: 0x41d0
+2772.0.1.0.0
+  __TEXT.__text: 0x3a1bd0
+  __TEXT.__auth_stubs: 0x41f0
   __TEXT.__objc_methlist: 0xd20
   __TEXT.__const: 0x2ebb8
-  __TEXT.__gcc_except_tab: 0x21064
-  __TEXT.__cstring: 0x9b091
+  __TEXT.__gcc_except_tab: 0x2113c
+  __TEXT.__cstring: 0x9b2d2
   __TEXT.__oslogstring: 0x17
   __TEXT.__ustring: 0x30
-  __TEXT.__unwind_info: 0xd1d0
+  __TEXT.__unwind_info: 0xd1e0
   __TEXT.__eh_frame: 0x308
   __TEXT.__objc_classname: 0xe0
   __TEXT.__objc_methname: 0x2e13

   __DATA_CONST.__objc_selrefs: 0xb10
   __DATA_CONST.__objc_superrefs: 0x38
   __DATA_CONST.__objc_arraydata: 0x20
-  __AUTH_CONST.__auth_got: 0x2100
-  __AUTH_CONST.__const: 0x3c838
-  __AUTH_CONST.__cfstring: 0x35c40
+  __AUTH_CONST.__auth_got: 0x2110
+  __AUTH_CONST.__const: 0x3c840
+  __AUTH_CONST.__cfstring: 0x35c60
   __AUTH_CONST.__objc_const: 0x1020
   __AUTH_CONST.__objc_doubleobj: 0x20
   __AUTH_CONST.__objc_intobj: 0x30

   __AUTH.__data: 0x1d0
   __DATA.__objc_ivar: 0x9c
   __DATA.__data: 0x2bb0
-  __DATA.__bss: 0x4f30
-  __DATA.__common: 0x1eb0
+  __DATA.__bss: 0x4f20
+  __DATA.__common: 0x1e98
   __DATA_DIRTY.__data: 0x168
   __DATA_DIRTY.__crash_info: 0x148
-  __DATA_DIRTY.__common: 0xdf3
-  __DATA_DIRTY.__bss: 0xb18
+  __DATA_DIRTY.__common: 0xe0b
+  __DATA_DIRTY.__bss: 0xb20
   - /System/Library/Frameworks/Accelerate.framework/Accelerate
   - /System/Library/Frameworks/ColorSync.framework/ColorSync
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation

   - /usr/lib/libexpat.1.dylib
   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libz.1.dylib
-  UUID: 0790DC31-EFD2-3F72-ACCC-CF1DB5D7C790
-  Functions: 13128
-  Symbols:   40970
-  CStrings:  24698
+  UUID: 633AA0C4-EE47-3391-A4C4-7DF22E9B11C5
+  Functions: 13129
+  Symbols:   40975
+  CStrings:  24708
 
Symbols:
+ _IOSurfaceAcceleratorCreate
+ _IOSurfaceAcceleratorTransformSurface
+ __ZN13IIOReadPlugin14callInitializeERb
+ __ZN25IIOIOSurfaceWrapper_CIF1035copy_and_colormatch_CIF10_to_P3_MSRE6CGRectP13vImage_BufferS2_S2_
+ ___block_descriptor_tmp.111
+ ___block_literal_global.113
- __ZN13IIOReadPlugin14callInitializeEv
- ___block_descriptor_tmp.108
- ___block_literal_global.110
CStrings:
+ "*** ERROR: IOSurfaceSetBulkAttachments2 -dst- failed [%ld]\n"
+ "*** ERROR: NULL buffer data - p3Temp.data: %p, finalTemp.data: %p\n"
+ "*** ERROR: copy_and_colormatch_CIF10_to_P3_MSR returned: %d\n"
+ "*** ERROR: unexpected _componentType (%d)\n"
+ "*** NOTE: skipping layer#%d {%d, %d, %d, %d}\n"
+ "*** TransformSurface-band err 0x%x (%d)\n"
+ "*** WARNING: channel[%d] row[%d] PackBits data truncated - expected %lld literal bytes, only %lld available, copying what we can\n"
+ "*** WARNING: channel[%d] row[%d] PackBits data truncated - missing repeat byte, preserving partial decode\n"
+ "*** WARNING: channel[%d] row[%d] clamping literal count from %lld to %lld to avoid buffer overrun\n"
+ "*** WARNING: channel[%d] row[%d] clamping repeat count from %lld to %lld to avoid buffer overrun\n"
+ "*** falling back to standard 'IOSurfaceCreate'\n"
+ "com.apple.springboard"
+ "copy_and_colormatch_CIF10_to_P3_MSR"
- "*** ERROR: channel[%d] row[%d] discarding %lld bytes to avoid buffer overrun"
- "*** ERROR: channel[%d] row[%d] discarding %lld bytes to avoid buffer overrun\n"
- "*** ERROR: channel[%d] row[%d] terminating PackBitsDecode due to lack of data\n"
- "*** ERROR: skipping layer#%d {%d, %d, %d, %d}\n"

```
