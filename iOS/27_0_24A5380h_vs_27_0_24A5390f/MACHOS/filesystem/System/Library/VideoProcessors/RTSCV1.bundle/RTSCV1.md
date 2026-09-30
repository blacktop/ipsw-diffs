## RTSCV1

> `/System/Library/VideoProcessors/RTSCV1.bundle/RTSCV1`

### Sections with Same Size but Changed Content

- `__TEXT.__oslogstring`
- `__DATA_CONST.__cfstring`
- `__DATA_CONST.__objc_classlist`
- `__DATA_CONST.__objc_protolist`
- `__DATA_CONST.__objc_superrefs`
- `__DATA_CONST.__objc_intobj`
- `__DATA_CONST.__got`
- `__DATA.__objc_const`
- `__DATA.__objc_data`
- `__DATA.__data`

```diff

-758.0.0.122.2
-  __TEXT.__text: 0x15ca8
+761.0.0.0.3
+  __TEXT.__text: 0x15fd4
   __TEXT.__auth_stubs: 0x6b0
-  __TEXT.__objc_stubs: 0x16e0
-  __TEXT.__objc_methlist: 0xf34
+  __TEXT.__objc_stubs: 0x1700
+  __TEXT.__objc_methlist: 0xf44
   __TEXT.__const: 0x320
-  __TEXT.__cstring: 0x1cd5
+  __TEXT.__cstring: 0x1ce4
   __TEXT.__oslogstring: 0x2a2b
-  __TEXT.__objc_methname: 0x30fd
+  __TEXT.__objc_methname: 0x314b
   __TEXT.__objc_classname: 0x1c1
-  __TEXT.__objc_methtype: 0x1588
+  __TEXT.__objc_methtype: 0x159b
   __TEXT.__gcc_except_tab: 0x664
-  __TEXT.__unwind_info: 0x4b8
+  __TEXT.__unwind_info: 0x4c0
   __DATA_CONST.__cfstring: 0x180
   __DATA_CONST.__objc_classlist: 0x80
   __DATA_CONST.__objc_protolist: 0x20

   __DATA_CONST.__got: 0x1a0
   __DATA_CONST.__auth_ptr: 0x8
   __DATA.__objc_const: 0x2948
-  __DATA.__objc_selrefs: 0x878
+  __DATA.__objc_selrefs: 0x880
   __DATA.__objc_ivar: 0x2dc
   __DATA.__objc_data: 0x500
   __DATA.__data: 0x180

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libc++.1.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 350
-  Symbols:   991
-  CStrings:  949
+  Functions: 351
+  Symbols:   993
+  CStrings:  951
 
Symbols:
+ -[RTSCFaceReframingV1 _estimateMinShift:maxShift:forViewPortBox:withinBoundingRect:boundingCircle:]
+ -[RTSCFaceReframingV1 _preClampOffset:ofViewPort:toMinShift:maxShift:]
+ -[RTSCFaceReframingV1 _updateOffsetOfViewPortBox:withinBoundingRect:boundingCircle:]
+ _objc_msgSend$_estimateMinShift:maxShift:forViewPortBox:withinBoundingRect:boundingCircle:
+ _objc_msgSend$_preClampOffset:ofViewPort:toMinShift:maxShift:
+ _objc_msgSend$_updateOffsetOfViewPortBox:withinBoundingRect:boundingCircle:
- -[RTSCFaceReframingV1 _estimateMinShift:maxShift:forViewPortBox:withinBoundingRect:]
- -[RTSCFaceReframingV1 _updateOffsetOfViewPortBox:withinBoundingRect:]
- _objc_msgSend$_estimateMinShift:maxShift:forViewPortBox:withinBoundingRect:
- _objc_msgSend$_updateOffsetOfViewPortBox:withinBoundingRect:
CStrings:
+ "-[RTSCFaceReframingV1 _updateOffsetOfViewPortBox:withinBoundingRect:boundingCircle:]"
+ "56@0:816244048"
+ "80@0:816{CGRect={CGPoint=dd}{CGSize=dd}}3264"
+ "_estimateMinShift:maxShift:forViewPortBox:withinBoundingRect:boundingCircle:"
+ "_preClampOffset:ofViewPort:toMinShift:maxShift:"
+ "_updateOffsetOfViewPortBox:withinBoundingRect:boundingCircle:"
+ "v96@0:8^16^2432{CGRect={CGPoint=dd}{CGSize=dd}}4880"
- "-[RTSCFaceReframingV1 _updateOffsetOfViewPortBox:withinBoundingRect:]"
- "64@0:816{CGRect={CGPoint=dd}{CGSize=dd}}32"
- "_estimateMinShift:maxShift:forViewPortBox:withinBoundingRect:"
- "_updateOffsetOfViewPortBox:withinBoundingRect:"
- "v80@0:8^16^2432{CGRect={CGPoint=dd}{CGSize=dd}}48"
```
