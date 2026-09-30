## libMTLHud.dylib

> `/usr/lib/libMTLHud.dylib`

### Sections with Same Size but Changed Content

- `__TEXT.__init_offsets`
- `__TEXT.__unwind_info`
- `__DATA_CONST.__const`
- `__DATA_CONST.__objc_classlist`
- `__DATA_CONST.__objc_protolist`
- `__DATA_CONST.__objc_superrefs`
- `__DATA_CONST.__objc_intobj`
- `__DATA_CONST.__objc_arraydata`
- `__DATA_CONST.__objc_arrayobj`
- `__DATA_CONST.__objc_dictobj`
- `__DATA_CONST.__got`
- `__DATA_CONST.__auth_ptr`
- `__DATA.__objc_selrefs`
- `__DATA.__objc_data`
- `__DATA.__data`
- `__DATA.__thread_vars`

```diff

-5.0.24.0.0
-  __TEXT.__text: 0x30c1c
-  __TEXT.__auth_stubs: 0xcc0
-  __TEXT.__objc_stubs: 0x3ba0
+5.0.26.0.0
+  __TEXT.__text: 0x30dd4
+  __TEXT.__auth_stubs: 0xcd0
+  __TEXT.__objc_stubs: 0x3bc0
   __TEXT.__init_offsets: 0x4
-  __TEXT.__objc_methlist: 0x1d0c
+  __TEXT.__objc_methlist: 0x1d1c
   __TEXT.__const: 0x448
-  __TEXT.__gcc_except_tab: 0x213c
-  __TEXT.__cstring: 0x79c6
+  __TEXT.__gcc_except_tab: 0x2148
+  __TEXT.__cstring: 0x79cd
   __TEXT.__objc_classname: 0x3be
-  __TEXT.__objc_methname: 0x4a31
+  __TEXT.__objc_methname: 0x4a0c
   __TEXT.__objc_methtype: 0x44b2
   __TEXT.__ustring: 0xb8
   __TEXT.__oslogstring: 0x9a
   __TEXT.__unwind_info: 0x1178
   __DATA_CONST.__const: 0x1000
-  __DATA_CONST.__cfstring: 0x3460
+  __DATA_CONST.__cfstring: 0x3480
   __DATA_CONST.__objc_classlist: 0xe8
   __DATA_CONST.__objc_protolist: 0x48
   __DATA_CONST.__objc_imageinfo: 0x8

   __DATA_CONST.__objc_arraydata: 0x4a8
   __DATA_CONST.__objc_arrayobj: 0x60
   __DATA_CONST.__objc_dictobj: 0x50
-  __DATA_CONST.__auth_got: 0x678
+  __DATA_CONST.__auth_got: 0x680
   __DATA_CONST.__got: 0x208
   __DATA_CONST.__auth_ptr: 0x20
-  __DATA.__objc_const: 0x34b0
+  __DATA.__objc_const: 0x3498
   __DATA.__objc_selrefs: 0x1548
-  __DATA.__objc_ivar: 0x1f8
+  __DATA.__objc_ivar: 0x1f4
   __DATA.__objc_data: 0x910
   __DATA.__data: 0x698
   __DATA.__thread_vars: 0x18

   - /usr/lib/libc++.1.dylib
   - /usr/lib/libobjc.A.dylib
   Functions: 897
-  Symbols:   2268
+  Symbols:   2269
   CStrings:  2028
 
Symbols:
+ _CFStringFind
+ __Z15_HUDUIDrawFrameP12HUDUIOverlayPU27objcproto16MTLCommandBuffer11objc_objectPKPU21objcproto10MTLTexture11objc_objectiS4_13MTLLoadActionbmbPU18objcproto8MTLEvent11objc_objectS9_yfbbU13block_pointerFvPU34objcproto23MTLRenderCommandEncoder11objc_objectEU13block_pointerFvvE
+ __Z28HUDUIOverlayGetPipelineStateP12HUDUIOverlayPU21objcproto10MTLTexture11objc_objectbbb
+ __ZL36_HUDUIFrameGetCompositeSourceTextureP10HUDUIFrame14MTLPixelFormatbb
+ ____Z15_HUDUIDrawFrameP12HUDUIOverlayPU27objcproto16MTLCommandBuffer11objc_objectPKPU21objcproto10MTLTexture11objc_objectiS4_13MTLLoadActionbmbPU18objcproto8MTLEvent11objc_objectS9_yfbbU13block_pointerFvPU34objcproto23MTLRenderCommandEncoder11objc_objectEU13block_pointerFvvE_block_invoke
+ ____ZL19_HUDUIBlitFrameMTL4P12HUDUIOverlayPU27objcproto16MTL4CommandQueue11objc_objectPU21objcproto10MTLTexture11objc_object13MTLLoadActionPU18objcproto8MTLEvent11objc_objectyU13block_pointerFvPU35objcproto24MTL4RenderCommandEncoder11objc_objectPU26objcproto15MTLResidencySet11objc_objectEU13block_pointerFvvEbb_block_invoke
+ _objc_msgSend$metalFXFrameInterpolatorDisable
- OBJC_IVAR_$_HUDMTLLayerTracking._metalFXFrameInterpolatorWaitCounter
- __Z15_HUDUIDrawFrameP12HUDUIOverlayPU27objcproto16MTLCommandBuffer11objc_objectPKPU21objcproto10MTLTexture11objc_objectiS4_13MTLLoadActionbmbPU18objcproto8MTLEvent11objc_objectS9_yfbU13block_pointerFvPU34objcproto23MTLRenderCommandEncoder11objc_objectEU13block_pointerFvvE
- __Z28HUDUIOverlayGetPipelineStateP12HUDUIOverlayPU21objcproto10MTLTexture11objc_objectbb
- __ZL36_HUDUIFrameGetCompositeSourceTextureP10HUDUIFrame14MTLPixelFormat
- ____Z15_HUDUIDrawFrameP12HUDUIOverlayPU27objcproto16MTLCommandBuffer11objc_objectPKPU21objcproto10MTLTexture11objc_objectiS4_13MTLLoadActionbmbPU18objcproto8MTLEvent11objc_objectS9_yfbU13block_pointerFvPU34objcproto23MTLRenderCommandEncoder11objc_objectEU13block_pointerFvvE_block_invoke
- ____ZL19_HUDUIBlitFrameMTL4P12HUDUIOverlayPU27objcproto16MTL4CommandQueue11objc_objectPU21objcproto10MTLTexture11objc_object13MTLLoadActionPU18objcproto8MTLEvent11objc_objectyU13block_pointerFvPU35objcproto24MTL4RenderCommandEncoder11objc_objectPU26objcproto15MTLResidencySet11objc_objectEU13block_pointerFvvEb_block_invoke
Functions:
~ -[HUDMTLLayerTracking _snapshotDrawable:] : 696 -> 816
~ -[HUDMTLLayerOverlay layerTracking:presentDrawable:mtl4Queue:] : 2736 -> 2816
~ __Z28HUDUIOverlayGetPipelineStateP12HUDUIOverlayPU21objcproto10MTLTexture11objc_objectbb -> __Z28HUDUIOverlayGetPipelineStateP12HUDUIOverlayPU21objcproto10MTLTexture11objc_objectbbb : 1452 -> 1504
~ __ZL36_HUDUIFrameGetCompositeSourceTextureP10HUDUIFrame14MTLPixelFormat -> __ZL36_HUDUIFrameGetCompositeSourceTextureP10HUDUIFrame14MTLPixelFormatbb : 116 -> 168
~ __Z15_HUDUIDrawFrameP12HUDUIOverlayPU27objcproto16MTLCommandBuffer11objc_objectPKPU21objcproto10MTLTexture11objc_objectiS4_13MTLLoadActionbmbPU18objcproto8MTLEvent11objc_objectS9_yfbU13block_pointerFvPU34objcproto23MTLRenderCommandEncoder11objc_objectEU13block_pointerFvvE -> __Z15_HUDUIDrawFrameP12HUDUIOverlayPU27objcproto16MTLCommandBuffer11objc_objectPKPU21objcproto10MTLTexture11objc_objectiS4_13MTLLoadActionbmbPU18objcproto8MTLEvent11objc_objectS9_yfbbU13block_pointerFvPU34objcproto23MTLRenderCommandEncoder11objc_objectEU13block_pointerFvvE : 1640 -> 1644
~ _HUDUIDrawFrames : 3032 -> 3096
~ ____ZL22_HUDUIBlitFramesMetal4P12HUDUIOverlayPU27objcproto16MTL4CommandQueue11objc_objectPU21objcproto10MTLTexture11objc_objectP17HUDUIFrameContextjPU18objcproto8MTLEvent11objc_objectyU13block_pointerFvvE_block_invoke : 1080 -> 1108
~ ____ZL22_HUDUIBlitFramesMetal3P12HUDUIOverlayPU21objcproto10MTLTexture11objc_objectS2_P17HUDUIFrameContextjmPU18objcproto8MTLEvent11objc_objectyU13block_pointerFvvE_block_invoke : 628 -> 680
~ -[MTLHUDService metalFXFrameInterpolatorEncodingEndNoDirectObject:] : 252 -> 240
CStrings:
+ "Linear"
- "_metalFXFrameInterpolatorWaitCounter"
```
