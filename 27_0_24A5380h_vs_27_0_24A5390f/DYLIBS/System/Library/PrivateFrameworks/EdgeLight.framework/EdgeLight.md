## EdgeLight

> `/System/Library/PrivateFrameworks/EdgeLight.framework/EdgeLight`

### Sections with Same Size but Changed Content

- `__TEXT.__unwind_info`
- `__DATA_CONST.__const`
- `__DATA_CONST.__objc_classlist`
- `__DATA_CONST.__objc_protolist`
- `__DATA_CONST.__objc_superrefs`
- `__DATA_CONST.__got`
- `__AUTH_CONST.__const`
- `__AUTH_CONST.__cfstring`
- `__AUTH.__objc_data`
- `__DATA.__data`

```diff

-556.0.0.0.1
-  __TEXT.__text: 0x4e80
-  __TEXT.__objc_methlist: 0x7f8
+558.0.0.0.0
+  __TEXT.__text: 0x4e90
+  __TEXT.__objc_methlist: 0x810
   __TEXT.__const: 0x160
   __TEXT.__gcc_except_tab: 0xbc
   __TEXT.__oslogstring: 0x418

   __DATA_CONST.__objc_classlist: 0x58
   __DATA_CONST.__objc_protolist: 0x18
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x608
+  __DATA_CONST.__objc_selrefs: 0x618
   __DATA_CONST.__objc_superrefs: 0x30
   __DATA_CONST.__got: 0xc0
   __AUTH_CONST.__const: 0x60
   __AUTH_CONST.__cfstring: 0x720
-  __AUTH_CONST.__objc_const: 0x13f8
+  __AUTH_CONST.__objc_const: 0x1408
   __AUTH_CONST.__auth_got: 0x0
   __AUTH.__objc_data: 0x370
   __DATA.__objc_ivar: 0x128

   - /System/Library/PrivateFrameworks/CMImaging.framework/CMImaging
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 183
-  Symbols:   562
+  Functions: 185
+  Symbols:   566
   CStrings:  97
 
Symbols:
+ -[CNUMetalContext fullRangeVertexBuf]
+ -[CNUMetalContext renderPipelineStateForVertexFunction:vertexDescriptor:fragmentFunction:constants:colorAttachmentDescriptorArrray:depthAttachmentPixelFormat:]
+ _objc_msgSend$fullRangeVertexBuf
+ _objc_msgSend$renderPipelineStateForVertexFunction:vertexDescriptor:fragmentFunction:constants:colorAttachmentDescriptorArrray:depthAttachmentPixelFormat:
```
