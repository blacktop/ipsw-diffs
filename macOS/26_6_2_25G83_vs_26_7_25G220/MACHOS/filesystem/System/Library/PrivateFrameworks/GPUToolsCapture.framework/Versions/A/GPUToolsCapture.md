## GPUToolsCapture

> `System/Library/PrivateFrameworks/GPUToolsCapture.framework/Versions/A/GPUToolsCapture`

### Sections with Same Size but Changed Content

- `__TEXT.__gcc_except_tab`
- `__TEXT.__unwind_info`
- `__DATA_CONST.__got`
- `__DATA_CONST.__const`
- `__DATA_CONST.__cfstring`
- `__DATA_CONST.__objc_classlist`
- `__DATA_CONST.__objc_protolist`
- `__DATA_CONST.__objc_protorefs`
- `__DATA_CONST.__objc_superrefs`
- `__DATA_CONST.__objc_intobj`
- `__DATA.__objc_data`
- `__DATA.__data`

```diff

 314.14.0.0.0
-  __TEXT.__text: 0x29b120
+  __TEXT.__text: 0x29b1bc
   __TEXT.__auth_stubs: 0x16e0
-  __TEXT.__objc_stubs: 0x18760
+  __TEXT.__objc_stubs: 0x18780
   __TEXT.__init_offsets: 0x4
-  __TEXT.__objc_methlist: 0x13bbc
-  __TEXT.__const: 0x4698
+  __TEXT.__objc_methlist: 0x13c1c
+  __TEXT.__const: 0x46a0
   __TEXT.__cstring: 0x27c06
   __TEXT.__gcc_except_tab: 0x2db0
-  __TEXT.__objc_methname: 0x1cfae
+  __TEXT.__objc_methname: 0x1d066
   __TEXT.__objc_classname: 0x1ab1
   __TEXT.__objc_methtype: 0xc442
   __TEXT.__oslogstring: 0x17a1

   __DATA_CONST.__objc_dictobj: 0xa0
   __DATA_CONST.__objc_arrayobj: 0x30
   __AUTH_CONST.__interpose: 0x80
-  __DATA.__objc_const: 0x1ca28
-  __DATA.__objc_selrefs: 0x7260
+  __DATA.__objc_const: 0x1cb40
+  __DATA.__objc_selrefs: 0x7298
   __DATA.__objc_ivar: 0xb70
   __DATA.__objc_data: 0x2670
   __DATA.__data: 0x3bc0

   - /usr/lib/libcompression.dylib
   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libz.1.dylib
-  Functions: 8236
-  Symbols:   14943
-  CStrings:  8985
+  Functions: 8237
+  Symbols:   14945
+  CStrings:  8992
 
Symbols:
+ -[CaptureMTLTexture minLOD]
+ _objc_msgSend$minLOD
Functions:
+ -[CaptureMTLTexture minLOD]
~ _TranslateGTMTLTileRenderPipelineDescriptor : 940 -> 1028
~ _MakeMTLTileRenderPipelineDescriptor : 756 -> 816
CStrings:
+ "minLOD"
+ "supportsMXUNarrowTileSizes"
+ "supportsPackUnpackSmallInteger"
+ "supportsRGBTextureBuffers"
+ "supportsSIMDGroupParallelForwardProgress"
+ "supportsTextureMultifetch"
+ "supportsTextureViewMinLOD"
```
