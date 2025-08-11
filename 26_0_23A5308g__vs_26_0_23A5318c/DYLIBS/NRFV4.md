## NRFV4

> `/System/Library/VideoProcessors/NRFV4.bundle/NRFV4`

```diff

-664.0.0.0.2
-  __TEXT.__text: 0x25879c
-  __TEXT.__auth_stubs: 0xfb0
+664.2.5.0.0
+  __TEXT.__text: 0x25805c
+  __TEXT.__auth_stubs: 0xf80
   __TEXT.__objc_methlist: 0x103f0
   __TEXT.__const: 0x102790
-  __TEXT.__cstring: 0x2faad
+  __TEXT.__cstring: 0x2fa03
   __TEXT.__gcc_except_tab: 0x153c
   __TEXT.__oslogstring: 0x253fc
   __TEXT.__dlopen_cstrs: 0x10c
-  __TEXT.__unwind_info: 0x4888
+  __TEXT.__unwind_info: 0x4890
   __TEXT.__objc_classname: 0x2dc0
-  __TEXT.__objc_methname: 0x31863
-  __TEXT.__objc_methtype: 0x15efe
+  __TEXT.__objc_methname: 0x31888
+  __TEXT.__objc_methtype: 0x15efd
   __TEXT.__objc_stubs: 0x14ee0
-  __DATA_CONST.__got: 0xc10
+  __DATA_CONST.__got: 0xc08
   __DATA_CONST.__const: 0x12e0
   __DATA_CONST.__objc_classlist: 0xc98
   __DATA_CONST.__objc_catlist: 0x10

   __DATA_CONST.__objc_classrefs: 0x8
   __DATA_CONST.__objc_superrefs: 0x9a0
   __DATA_CONST.__objc_arraydata: 0xe40
-  __AUTH_CONST.__auth_got: 0x7f0
+  __AUTH_CONST.__auth_got: 0x7d8
   __AUTH_CONST.__const: 0x7e0
-  __AUTH_CONST.__cfstring: 0x12ec0
-  __AUTH_CONST.__objc_const: 0x328a8
+  __AUTH_CONST.__cfstring: 0x12e60
+  __AUTH_CONST.__objc_const: 0x328c8
   __AUTH_CONST.__objc_doubleobj: 0xa0
   __AUTH_CONST.__objc_arrayobj: 0xae0
   __AUTH_CONST.__objc_intobj: 0xa50
   __AUTH_CONST.__objc_floatobj: 0x60
   __AUTH_CONST.__objc_dictobj: 0x550
   __AUTH.__objc_data: 0x9b0
-  __DATA.__objc_ivar: 0x350c
+  __DATA.__objc_ivar: 0x3510
   __DATA.__data: 0xb48
   __DATA.__common: 0x20
   __DATA.__bss: 0x14

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libc++.1.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: B6EBC329-3369-3C5A-A4F7-B960360DA733
-  Functions: 12498
-  Symbols:   36746
-  CStrings:  18076
+  UUID: B34A1304-F7DC-3BC2-BC3E-1FD2FFA3EC8D
+  Functions: 12493
+  Symbols:   36735
+  CStrings:  18067
 
Symbols:
+ -[SoftISPInputFrame inputBufferRectWithinSensorCropRect]
+ _FigCaptureMetadataUtilitiesUpdateISPSpatialMetadataForStillImageCrop
+ _OBJC_IVAR_$_SoftISPInputFrame._inputBufferRectWithinSensorCropRect
- -[H13FastRawMBNRConfig(RawMBNR) updateRawMBNRConfigForInputFrame:bounds:band:rawMBNRConfig:].cold.2
- _FigCaptureMetadataUtilitiesUpdateDetectedObjectsInfoAndFacesArrayWithCropRect
- _FigCaptureNormalizedFocusWindowFromMetadata
- _FigCaptureSetNormalizedFocusWindowToMetadata
- _FigCaptureTransformRectToCoordinateSpaceOfRect
- _kFigCaptureStreamMetadata_FocusRegion
CStrings:
+ "InputBufferRectWithinSensorCropRect"
+ "_inputBufferRectWithinSensorCropRect"
+ "i48@0:8@16@24@32^{RNFConfig=BBCCS[4[3S]][4[33S]][257S]ff[4[2f]]f}40"
- "OptCenter"
- "RadScale"
- "X0"
- "Y0"
- "configRegister->optCenter.x == configMetadata->optCenter.x"
- "configRegister->optCenter.y == configMetadata->optCenter.y"
- "configRegister->radScale == configMetadata->radScale"
- "i48@0:8@16@24@32^{RNFConfig=BBCSCS[4[3S]][4[33S]][257S]ff[4[2f]]f}40"
- "optCenter"

```
