## STF

> `/System/Library/VideoProcessors/STF.bundle/STF`

### Sections with Same Size but Changed Content

- `__TEXT.__cstring`
- `__TEXT.__unwind_info`
- `__TEXT.__eh_frame`
- `__DATA_CONST.__const`
- `__DATA_CONST.__objc_classlist`
- `__DATA_CONST.__objc_protolist`
- `__DATA_CONST.__objc_protorefs`
- `__DATA_CONST.__objc_superrefs`
- `__AUTH_CONST.__const`
- `__AUTH_CONST.__cfstring`
- `__AUTH_CONST.__objc_intobj`
- `__AUTH.__data`
- `__DATA.__data`
- `__DATA_DIRTY.__objc_data`

```diff

-758.0.0.122.2
-  __TEXT.__text: 0xf9128
-  __TEXT.__objc_methlist: 0x171c
+761.0.0.0.3
+  __TEXT.__text: 0xf93d8
+  __TEXT.__objc_methlist: 0x1734
   __TEXT.__const: 0x580
-  __TEXT.__oslogstring: 0x1c4b
+  __TEXT.__oslogstring: 0x1cc9
   __TEXT.__cstring: 0x84c5
   __TEXT.__gcc_except_tab: 0x24c
   __TEXT.__unwind_info: 0xeb0

   __DATA_CONST.__objc_classlist: 0xa0
   __DATA_CONST.__objc_protolist: 0x50
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0xcf0
+  __DATA_CONST.__objc_selrefs: 0xd00
   __DATA_CONST.__objc_protorefs: 0x8
   __DATA_CONST.__objc_superrefs: 0x70
-  __DATA_CONST.__got: 0x190
+  __DATA_CONST.__got: 0x198
   __AUTH_CONST.__const: 0x388
   __AUTH_CONST.__cfstring: 0xfa0
-  __AUTH_CONST.__objc_const: 0x3dd0
+  __AUTH_CONST.__objc_const: 0x3e60
   __AUTH_CONST.__objc_intobj: 0x30
   __AUTH_CONST.__auth_got: 0x3c0
   __AUTH.__data: 0x8
-  __DATA.__objc_ivar: 0x468
+  __DATA.__objc_ivar: 0x478
   __DATA.__data: 0x3c0
   __DATA_DIRTY.__objc_data: 0x640
   __DATA_DIRTY.__common: 0x20

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libc++.1.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 2136
-  Symbols:   2495
-  CStrings:  1211
+  Functions: 2138
+  Symbols:   2504
+  CStrings:  1212
 
Symbols:
+ -[STFRingData quadraBinningFactor]
+ -[STFRingData setQuadraBinningFactor:]
+ _OBJC_IVAR_$_STFRingData._quadraBinningFactor
+ _OBJC_IVAR_$_STFVideoProcessorV1._framesSinceQuadraTransition
+ _OBJC_IVAR_$_STFVideoProcessorV1._previousQuadraBinningFactor
+ _OBJC_IVAR_$_STFVideoProcessorV1._quadraTransitionPending
+ _kFigCaptureStreamMetadata_QuadraBinningFactor
+ _objc_msgSend$quadraBinningFactor
+ _objc_msgSend$setQuadraBinningFactor:
CStrings:
+ "<<<< STF >>>> %s: Sensor/Binning Switch Detected Backwards at:%d and currentIndex:%d size:%d"
+ "<<<< STF >>>> %s: Sensor/Binning Switch Detected Forwards at:%d and currentIndex:%d"
+ "<<<< STF >>>> %s: quadra transition: clamping LTM application homography (delay=%u, framesSinceTransition=%d)"
- "<<<< STF >>>> %s: Sensor Switch Detected Backwards at:%d and currentIndex:%d size:%d"
- "<<<< STF >>>> %s: Sensor Switch Detected Forwards at:%d and currentIndex:%d"
```
