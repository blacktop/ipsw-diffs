## AppleIntelKBLGraphicsMTLDriver

> `System/Library/Extensions/AppleIntelKBLGraphicsMTLDriver.bundle/Contents/MacOS/AppleIntelKBLGraphicsMTLDriver`

### Sections with Same Size but Changed Content

- `__TEXT.__init_offsets`
- `__TEXT.__const`
- `__TEXT.__gcc_except_tab`
- `__TEXT.__unwind_info`
- `__TEXT.__eh_frame`
- `__TEXT.__objc_methtype`
- `__DATA_CONST.__const`
- `__DATA_CONST.__cfstring`
- `__DATA.__objc_data`
- `__DATA.__data`

```diff

-24.5.8.0.0
-  __TEXT.__text: 0xbb78e
+24.5.9.0.0
+  __TEXT.__text: 0xbb79e
   __TEXT.__stubs: 0x474
   __TEXT.__init_offsets: 0xc
-  __TEXT.__objc_methlist: 0x7844
+  __TEXT.__objc_methlist: 0x7894
   __TEXT.__const: 0x551fd0
   __TEXT.__cstring: 0x25e85
   __TEXT.__gcc_except_tab: 0x14b4
   __TEXT.__unwind_info: 0x1ec0
   __TEXT.__eh_frame: 0x58
   __TEXT.__objc_classname: 0x8f5
-  __TEXT.__objc_methname: 0x126b0
+  __TEXT.__objc_methname: 0x12768
   __TEXT.__objc_methtype: 0x24675
   __DATA_CONST.__got: 0xa30
   __DATA_CONST.__const: 0x2eb8

   __DATA_CONST.__objc_classlist: 0x120
   __DATA_CONST.__objc_protolist: 0x1d0
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_const: 0x128e0
-  __DATA_CONST.__objc_selrefs: 0x3d70
+  __DATA_CONST.__objc_const: 0x129f8
+  __DATA_CONST.__objc_selrefs: 0x3da8
   __DATA.__objc_classrefs: 0x218
   __DATA.__objc_superrefs: 0x120
   __DATA.__objc_ivar: 0xaf8

   - /usr/lib/libobjc.A.dylib
   Functions: 2579
   Symbols:   4649
-  CStrings:  4686
+  CStrings:  4693
 
Functions:
~ -[MTLIGAccelDevice initWithAcceleratorPort:] : 600 -> 618
~ __ZL15fillTextureDataPK20MTLTextureDescriptorPU19objcproto9MTLDevice11objc_objectjbbbR25VendorNewTextureDataStrucRyS6_S6_S6_RjS7_ : 6171 -> 6169
CStrings:
+ "minLOD"
+ "supportsMXUNarrowTileSizes"
+ "supportsPackUnpackSmallInteger"
+ "supportsRGBTextureBuffers"
+ "supportsSIMDGroupParallelForwardProgress"
+ "supportsTextureMultifetch"
+ "supportsTextureViewMinLOD"
```
