## CoreML

> `/System/Library/Frameworks/CoreML.framework/Versions/A/CoreML`

```diff

-3520.5.1.0.0
-  __TEXT.__text: 0x6eacb4
+3520.5.1.2.0
+  __TEXT.__text: 0x6eabd4
   __TEXT.__auth_stubs: 0x5450
   __TEXT.__init_offsets: 0x4
-  __TEXT.__objc_methlist: 0x102f0
+  __TEXT.__objc_methlist: 0x10338
   __TEXT.__const: 0x56bb0
   __TEXT.__dlopen_cstrs: 0x21e
   __TEXT.__constg_swiftt: 0x1ec8

   __TEXT.__swift5_assocty: 0x580
   __TEXT.__swift5_proto: 0x64c
   __TEXT.__swift5_types: 0x274
-  __TEXT.__cstring: 0x2e932
+  __TEXT.__cstring: 0x2e930
   __TEXT.__swift_as_entry: 0xc0
   __TEXT.__swift5_protos: 0x40
   __TEXT.__swift5_mpenum: 0x84
   __TEXT.__swift5_capture: 0xa64
   __TEXT.__swift_as_ret: 0x100
   __TEXT.__oslogstring: 0xb2d6
-  __TEXT.__gcc_except_tab: 0x3c238
+  __TEXT.__gcc_except_tab: 0x3c228
   __TEXT.__ustring: 0x204
   __TEXT.__unwind_info: 0x109d0
   __TEXT.__eh_frame: 0x54fc
   __TEXT.__objc_classname: 0x2930
-  __TEXT.__objc_methname: 0x28981
+  __TEXT.__objc_methname: 0x286e1
   __TEXT.__objc_methtype: 0xba7b
   __TEXT.__objc_stubs: 0x13f20
   __DATA_CONST.__got: 0x11b0

   __DATA_CONST.__objc_catlist: 0x70
   __DATA_CONST.__objc_protolist: 0x2b0
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x75a0
+  __DATA_CONST.__objc_selrefs: 0x75d0
   __DATA_CONST.__objc_protorefs: 0x150
   __DATA_CONST.__objc_superrefs: 0x7d8
   __DATA_CONST.__objc_arraydata: 0x160
   __AUTH_CONST.__auth_got: 0x2a40
   __AUTH_CONST.__const: 0x20f58
   __AUTH_CONST.__cfstring: 0xd3a0
-  __AUTH_CONST.__objc_const: 0x230c0
+  __AUTH_CONST.__objc_const: 0x23150
   __AUTH_CONST.__objc_doubleobj: 0x90
   __AUTH_CONST.__objc_intobj: 0x978
   __AUTH_CONST.__objc_arrayobj: 0x2b8

   - /usr/lib/swift/libswiftsimd.dylib
   Functions: 16909
   Symbols:   27312
-  CStrings:  11584
+  CStrings:  11589
 
Functions:
~ sub_18b7153d4 -> sub_18b71e3d4 : 88 -> 84
~ _ZNK3MPL6detail16ModelPackageImpl12getRootModelEv.cold.1 : 28 -> 32
~ __ZN8Archiver17_IArchiveDiskImplC2ERKNSt3__112basic_stringIcNS1_11char_traitsIcEENS1_9allocatorIcEEEENS_10FileFormatE : 2380 -> 2152
~ __ZN6google8protobuf8internal15ThreadSafeArena23AllocateAlignedFallbackEmPKSt9type_info : 272 -> 276
~ __ZN8Archiver13_OArchiveImplD1Ev : 28 -> 24
~ ___56+[MLBackgroundWatchdog watchdogWithTimeout:label:queue:]_block_invoke : 248 -> 252
CStrings:
+ " is not a valid .mlmodelc file because the first word is not recognizable. "
+ "3520.5.1.2"
+ "supportsMXUNarrowTileSizes"
+ "supportsPackUnpackSmallInteger"
+ "supportsRGBTextureBuffers"
+ "supportsSIMDGroupParallelForwardProgress"
+ "supportsTextureMultifetch"
+ "supportsTextureViewMinLOD"
- " is not a valid .mlmodelc file because the first word ("
- ") is not recognizable. "
- "3520.5.1"
```
