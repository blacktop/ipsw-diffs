## AppleIntelICLGraphicsMTLDriver

> `System/Library/Extensions/AppleIntelICLGraphicsMTLDriver.bundle/Contents/MacOS/AppleIntelICLGraphicsMTLDriver`

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
-  __TEXT.__text: 0xc0652
+24.5.9.0.0
+  __TEXT.__text: 0xc0662
   __TEXT.__stubs: 0x492
   __TEXT.__init_offsets: 0xc
-  __TEXT.__objc_methlist: 0x7854
+  __TEXT.__objc_methlist: 0x78a4
   __TEXT.__const: 0x5d6de8
   __TEXT.__cstring: 0x26085
   __TEXT.__gcc_except_tab: 0x15d0
   __TEXT.__unwind_info: 0x1fd8
   __TEXT.__eh_frame: 0x58
   __TEXT.__objc_classname: 0x8f5
-  __TEXT.__objc_methname: 0x1267a
+  __TEXT.__objc_methname: 0x12732
   __TEXT.__objc_methtype: 0x2cdbc
   __DATA_CONST.__got: 0xa78
   __DATA_CONST.__const: 0x2df8

   __DATA_CONST.__objc_classlist: 0x120
   __DATA_CONST.__objc_protolist: 0x1d0
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_const: 0x12960
-  __DATA_CONST.__objc_selrefs: 0x3d80
+  __DATA_CONST.__objc_const: 0x12a78
+  __DATA_CONST.__objc_selrefs: 0x3db8
   __DATA.__objc_classrefs: 0x218
   __DATA.__objc_superrefs: 0x120
   __DATA.__objc_ivar: 0xb18

   - /usr/lib/libobjc.A.dylib
   Functions: 2647
   Symbols:   4743
-  CStrings:  4732
+  CStrings:  4739
 
Functions:
~ -[MTLIGAccelDevice initWithAcceleratorPort:] : 600 -> 618
~ __ZL15fillTextureDataPK20MTLTextureDescriptorPU19objcproto9MTLDevice11objc_objectjbbbR25VendorNewTextureDataStrucRyS6_S6_S6_ : 5878 -> 5876
CStrings:
+ "minLOD"
+ "supportsMXUNarrowTileSizes"
+ "supportsPackUnpackSmallInteger"
+ "supportsRGBTextureBuffers"
+ "supportsSIMDGroupParallelForwardProgress"
+ "supportsTextureMultifetch"
+ "supportsTextureViewMinLOD"
```
