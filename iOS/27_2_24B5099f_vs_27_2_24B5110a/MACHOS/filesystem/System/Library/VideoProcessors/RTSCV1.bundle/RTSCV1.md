## RTSCV1

> `System/Library/VideoProcessors/RTSCV1.bundle/RTSCV1`

### Sections with Same Size but Changed Content

- `__TEXT.__objc_methlist`
- `__TEXT.__gcc_except_tab`
- `__TEXT.__unwind_info`
- `__DATA_CONST.__cfstring`
- `__DATA_CONST.__objc_intobj`
- `__DATA.__objc_const`
- `__DATA.__objc_selrefs`
- `__DATA.__data`

```diff

-764.40.7.0.0
-  __TEXT.__text: 0xf2c8
+764.42.8.0.0
+  __TEXT.__text: 0xf334
   __TEXT.__auth_stubs: 0x660
   __TEXT.__objc_stubs: 0x1720
   __TEXT.__objc_methlist: 0xf74
Functions:
~ -[RTSCProcessorV1 _updateOutputFOV] : 996 -> 1088
~ -[RTSCProcessorV1 _updateStabilization] : 392 -> 404
~ -[RTSCProcessorV1 _calculateCropRectForOutputFOV:] : 380 -> 368
~ -[RTSCProcessorV1 _confineCropRectToValidImageCircle:] : 288 -> 304
```
