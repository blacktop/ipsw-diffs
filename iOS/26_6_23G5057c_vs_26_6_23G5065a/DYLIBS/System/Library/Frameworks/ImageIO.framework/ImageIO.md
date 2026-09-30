## ImageIO

> `/System/Library/Frameworks/ImageIO.framework/ImageIO`

### Sections with Same Size but Changed Content

- `__TEXT.__objc_methlist`
- `__TEXT.__eh_frame`
- `__DATA_CONST.__got`
- `__DATA_CONST.__const`
- `__DATA_CONST.__objc_classlist`
- `__DATA_CONST.__objc_protolist`
- `__DATA_CONST.__objc_selrefs`
- `__DATA_CONST.__objc_superrefs`
- `__DATA_CONST.__objc_arraydata`
- `__AUTH_CONST.__cfstring`
- `__AUTH_CONST.__objc_const`
- `__AUTH_CONST.__objc_doubleobj`
- `__AUTH_CONST.__objc_intobj`
- `__AUTH_CONST.__objc_floatobj`
- `__AUTH_CONST.__objc_dictobj`
- `__AUTH.__objc_data`
- `__AUTH.__data`
- `__DATA.__data`
- `__DATA_DIRTY.__data`

```diff

-  __TEXT.__text: 0x44979c
+  __TEXT.__text: 0x449afc
   __TEXT.__auth_stubs: 0x4280
   __TEXT.__objc_methlist: 0xd58
-  __TEXT.__const: 0x31588
-  __TEXT.__gcc_except_tab: 0x2659c
-  __TEXT.__cstring: 0x9e0ec
+  __TEXT.__const: 0x31648
+  __TEXT.__gcc_except_tab: 0x265a4
+  __TEXT.__cstring: 0x9e156
   __TEXT.__oslogstring: 0x17
   __TEXT.__ustring: 0x30
-  __TEXT.__unwind_info: 0xed38
+  __TEXT.__unwind_info: 0xed68
   __TEXT.__eh_frame: 0x3d0
   __TEXT.__objc_classname: 0xf1
   __TEXT.__objc_methname: 0x2e87

   __DATA_CONST.__objc_superrefs: 0x40
   __DATA_CONST.__objc_arraydata: 0x470
   __AUTH_CONST.__auth_got: 0x2158
-  __AUTH_CONST.__const: 0x3e198
+  __AUTH_CONST.__const: 0x3e2a8
   __AUTH_CONST.__cfstring: 0x35e20
   __AUTH_CONST.__objc_const: 0x10f8
   __AUTH_CONST.__objc_doubleobj: 0x20

   - /usr/lib/libexpat.1.dylib
   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libz.1.dylib
-  Functions: 15483
-  Symbols:   22798
-  CStrings:  17990
+  Functions: 15506
+  Symbols:   22829
+  CStrings:  17992
 
Symbols:
+ __ZNK3xdr18PixelFormatR8Unorm13bytesPerPixelEv
+ __ZNK3xdr19PixelFormatR16Float13bytesPerPixelEv
+ __ZNK3xdr19PixelFormatR16Unorm13bytesPerPixelEv
+ __ZNK3xdr19PixelFormatR32Float13bytesPerPixelEv
+ __ZNK3xdr19PixelFormatRG8Unorm13bytesPerPixelEv
+ __ZNK3xdr20PixelFormatRG16Unorm13bytesPerPixelEv
+ __ZNK3xdr21PixelFormatBGRA8Unorm13bytesPerPixelEv
+ __ZNK3xdr22PixelFormatRGBA16Float13bytesPerPixelEv
+ __ZNK3xdr22PixelFormatRGBA16Unorm13bytesPerPixelEv
+ __ZNK3xdr22PixelFormatRGBA32Float13bytesPerPixelEv
+ __ZNK3xdr23PixelFormatBGR10A2Unorm13bytesPerPixelEv
+ __ZNKSt3__120__shared_ptr_pointerIP11IIOColorMapNS_14default_deleteIS1_EENS_9allocatorIS1_EEE13__get_deleterERKSt9type_info
+ __ZNSt3__110shared_ptrI11IIOColorMapEaSB9fqe210106IS1_NS_14default_deleteIS1_EELi0EEERS2_ONS_10unique_ptrIT_T0_EE
+ __ZNSt3__115allocate_sharedB9fqe210106I11GIFColorMapNS_9allocatorIS1_EEJRP14ColorMapObjectELi0EEENS_10shared_ptrIT_EERKT0_DpOT1_
+ __ZNSt3__120__shared_ptr_emplaceI11GIFColorMapNS_9allocatorIS1_EEE16__on_zero_sharedEv
+ __ZNSt3__120__shared_ptr_emplaceI11GIFColorMapNS_9allocatorIS1_EEE21__on_zero_shared_weakEv
+ __ZNSt3__120__shared_ptr_emplaceI11GIFColorMapNS_9allocatorIS1_EEEC2B9fqe210106IJRP14ColorMapObjectES3_Li0EEES3_DpOT_
+ __ZNSt3__120__shared_ptr_emplaceI11GIFColorMapNS_9allocatorIS1_EEED0Ev
+ __ZNSt3__120__shared_ptr_emplaceI11GIFColorMapNS_9allocatorIS1_EEED1Ev
+ __ZNSt3__120__shared_ptr_pointerIP11IIOColorMapNS_14default_deleteIS1_EENS_9allocatorIS1_EEE16__on_zero_sharedEv
+ __ZNSt3__120__shared_ptr_pointerIP11IIOColorMapNS_14default_deleteIS1_EENS_9allocatorIS1_EEE21__on_zero_shared_weakEv
+ __ZNSt3__120__shared_ptr_pointerIP11IIOColorMapNS_14default_deleteIS1_EENS_9allocatorIS1_EEED0Ev
+ __ZNSt3__120__shared_ptr_pointerIP11IIOColorMapNS_14default_deleteIS1_EENS_9allocatorIS1_EEED1Ev
+ __ZTINSt3__114default_deleteI11IIOColorMapEE
+ __ZTINSt3__120__shared_ptr_emplaceI11GIFColorMapNS_9allocatorIS1_EEEE
+ __ZTINSt3__120__shared_ptr_pointerIP11IIOColorMapNS_14default_deleteIS1_EENS_9allocatorIS1_EEEE
+ __ZTSNSt3__114default_deleteI11IIOColorMapEE
+ __ZTSNSt3__120__shared_ptr_emplaceI11GIFColorMapNS_9allocatorIS1_EEEE
+ __ZTSNSt3__120__shared_ptr_pointerIP11IIOColorMapNS_14default_deleteIS1_EENS_9allocatorIS1_EEEE
+ __ZTVNSt3__120__shared_ptr_emplaceI11GIFColorMapNS_9allocatorIS1_EEEE
+ __ZTVNSt3__120__shared_ptr_pointerIP11IIOColorMapNS_14default_deleteIS1_EENS_9allocatorIS1_EEEE
CStrings:
+ "PixelBufferTexture"
+ "PixelBufferTexture: malformed pixel buffer - bytesPerRow %zu < %u * %zu for format %s"
+ "☀️ Using subsample factor: %u (%zu px)"
- "☀️ Using subsample factor: %u (%u px)"
```
