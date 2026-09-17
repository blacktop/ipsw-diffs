## libMTLHud.dylib

> `/usr/lib/libMTLHud.dylib`

### Sections with Same Size but Changed Content

- `__TEXT.__init_offsets`
- `__TEXT.__unwind_info`
- `__DATA_CONST.__const`
- `__DATA_CONST.__objc_classlist`
- `__DATA_CONST.__objc_catlist`
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
-  __TEXT.__text: 0x3e67c
-  __TEXT.__auth_stubs: 0xb50
-  __TEXT.__objc_stubs: 0x5720
+5.0.26.0.0
+  __TEXT.__text: 0x3e874
+  __TEXT.__auth_stubs: 0xb60
+  __TEXT.__objc_stubs: 0x5740
   __TEXT.__init_offsets: 0x4
-  __TEXT.__objc_methlist: 0x2204
+  __TEXT.__objc_methlist: 0x2214
   __TEXT.__const: 0x648
-  __TEXT.__gcc_except_tab: 0x21d0
-  __TEXT.__cstring: 0x7fe1
+  __TEXT.__gcc_except_tab: 0x21dc
+  __TEXT.__cstring: 0x7fe8
   __TEXT.__objc_classname: 0x4cf
-  __TEXT.__objc_methname: 0x5e26
+  __TEXT.__objc_methname: 0x5e01
   __TEXT.__objc_methtype: 0x4a26
   __TEXT.__ustring: 0x14c
   __TEXT.__oslogstring: 0x9a
   __TEXT.__unwind_info: 0x1440
   __DATA_CONST.__const: 0x1678
-  __DATA_CONST.__cfstring: 0x3d40
+  __DATA_CONST.__cfstring: 0x3d60
   __DATA_CONST.__objc_classlist: 0x120
   __DATA_CONST.__objc_catlist: 0x8
   __DATA_CONST.__objc_protolist: 0x70

   __DATA_CONST.__objc_arraydata: 0x528
   __DATA_CONST.__objc_arrayobj: 0xc0
   __DATA_CONST.__objc_dictobj: 0x50
-  __DATA_CONST.__auth_got: 0x5c0
+  __DATA_CONST.__auth_got: 0x5c8
   __DATA_CONST.__got: 0x310
   __DATA_CONST.__auth_ptr: 0x20
-  __DATA.__objc_const: 0x3e38
+  __DATA.__objc_const: 0x3e20
   __DATA.__objc_selrefs: 0x1cc0
-  __DATA.__objc_ivar: 0x240
+  __DATA.__objc_ivar: 0x23c
   __DATA.__objc_data: 0xb40
   __DATA.__data: 0x878
   __DATA.__thread_vars: 0x18

   - /usr/lib/libc++.1.dylib
   - /usr/lib/libobjc.A.dylib
   Functions: 1070
-  Symbols:   2777
+  Symbols:   2778
   CStrings:  2431
 
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
~ -[HUDMTLLayerTracking _snapshotDrawable:] : 688 -> 812
~ -[HUDMTLLayerOverlay layerTracking:presentDrawable:mtl4Queue:] : 2824 -> 2908
~ __Z28HUDUIOverlayGetPipelineStateP12HUDUIOverlayPU21objcproto10MTLTexture11objc_objectbb -> __Z28HUDUIOverlayGetPipelineStateP12HUDUIOverlayPU21objcproto10MTLTexture11objc_objectbbb : 1580 -> 1680
~ __ZL36_HUDUIFrameGetCompositeSourceTextureP10HUDUIFrame14MTLPixelFormat -> __ZL36_HUDUIFrameGetCompositeSourceTextureP10HUDUIFrame14MTLPixelFormatbb : 120 -> 172
~ __Z15_HUDUIDrawFrameP12HUDUIOverlayPU27objcproto16MTLCommandBuffer11objc_objectPKPU21objcproto10MTLTexture11objc_objectiS4_13MTLLoadActionbmbPU18objcproto8MTLEvent11objc_objectS9_yfbU13block_pointerFvPU34objcproto23MTLRenderCommandEncoder11objc_objectEU13block_pointerFvvE -> __Z15_HUDUIDrawFrameP12HUDUIOverlayPU27objcproto16MTLCommandBuffer11objc_objectPKPU21objcproto10MTLTexture11objc_objectiS4_13MTLLoadActionbmbPU18objcproto8MTLEvent11objc_objectS9_yfbbU13block_pointerFvPU34objcproto23MTLRenderCommandEncoder11objc_objectEU13block_pointerFvvE : 1764 -> 1772
~ _HUDUIDrawFrames : 3280 -> 3360
~ ____ZL22_HUDUIBlitFramesMetal4P12HUDUIOverlayPU27objcproto16MTL4CommandQueue11objc_objectPU21objcproto10MTLTexture11objc_objectP17HUDUIFrameContextjPU18objcproto8MTLEvent11objc_objectyU13block_pointerFvvE_block_invoke : 1124 -> 1152
~ ____ZL22_HUDUIBlitFramesMetal3P12HUDUIOverlayPU21objcproto10MTLTexture11objc_objectS2_P17HUDUIFrameContextjmPU18objcproto8MTLEvent11objc_objectyU13block_pointerFvvE_block_invoke : 660 -> 700
~ -[MTLHUDService metalFXFrameInterpolatorEncodingEndNoDirectObject:] : 252 -> 240
CStrings:
+ "Linear"
- "_metalFXFrameInterpolatorWaitCounter"
```
