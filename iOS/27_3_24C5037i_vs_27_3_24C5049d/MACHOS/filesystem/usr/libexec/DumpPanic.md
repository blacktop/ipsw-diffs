## DumpPanic

> `/usr/libexec/DumpPanic`

### Sections with Same Size but Changed Content

- `__TEXT.__gcc_except_tab`
- `__TEXT.__eh_frame`
- `__DATA_CONST.__objc_classlist`
- `__DATA_CONST.__objc_protolist`
- `__DATA_CONST.__objc_superrefs`
- `__DATA_CONST.__objc_arraydata`
- `__DATA_CONST.__objc_arrayobj`
- `__DATA_CONST.__objc_dictobj`
- `__DATA_CONST.__objc_intobj`

```diff

-41.60.2.0.0
-  __TEXT.__text: 0x2c190
-  __TEXT.__auth_stubs: 0x11f0
-  __TEXT.__objc_stubs: 0x26c0
-  __TEXT.__objc_methlist: 0x8dc
-  __TEXT.__cstring: 0x2b0b
+41.60.3.0.0
+  __TEXT.__text: 0x2ce68
+  __TEXT.__auth_stubs: 0x1270
+  __TEXT.__objc_stubs: 0x2700
+  __TEXT.__objc_methlist: 0x90c
+  __TEXT.__cstring: 0x2b3b
   __TEXT.__objc_classname: 0x12c
-  __TEXT.__objc_methtype: 0x546
-  __TEXT.__objc_methname: 0x204d
-  __TEXT.__const: 0x2f0
+  __TEXT.__objc_methtype: 0x55b
+  __TEXT.__objc_methname: 0x20bd
+  __TEXT.__const: 0x3c0
   __TEXT.__gcc_except_tab: 0xbdc
-  __TEXT.__oslogstring: 0x4e98
+  __TEXT.__oslogstring: 0x4ec8
   __TEXT.__ustring: 0x1c6
-  __TEXT.__constg_swiftt: 0x90
-  __TEXT.__swift5_typeref: 0x8b
-  __TEXT.__swift5_reflstr: 0x27
-  __TEXT.__swift5_fieldmd: 0x34
-  __TEXT.__swift5_types: 0x4
-  __TEXT.__unwind_info: 0xde0
+  __TEXT.__constg_swiftt: 0xdc
+  __TEXT.__swift5_typeref: 0xc3
+  __TEXT.__swift5_reflstr: 0x60
+  __TEXT.__swift5_fieldmd: 0x4c
+  __TEXT.__swift5_builtin: 0x14
+  __TEXT.__swift5_assocty: 0x18
+  __TEXT.__swift5_proto: 0xc
+  __TEXT.__swift5_types: 0x8
+  __TEXT.__unwind_info: 0xe10
   __TEXT.__eh_frame: 0xa0
-  __DATA_CONST.__const: 0x780
-  __DATA_CONST.__cfstring: 0x2400
+  __DATA_CONST.__const: 0x7a0
+  __DATA_CONST.__cfstring: 0x2440
   __DATA_CONST.__objc_classlist: 0x70
   __DATA_CONST.__objc_protolist: 0x10
   __DATA_CONST.__objc_imageinfo: 0x8

   __DATA_CONST.__objc_arrayobj: 0xc0
   __DATA_CONST.__objc_dictobj: 0x78
   __DATA_CONST.__objc_intobj: 0x78
-  __DATA_CONST.__auth_got: 0x910
-  __DATA_CONST.__got: 0x2b0
-  __DATA_CONST.__auth_ptr: 0x78
-  __DATA.__objc_const: 0x1140
-  __DATA.__objc_selrefs: 0xb20
+  __DATA_CONST.__auth_got: 0x950
+  __DATA_CONST.__got: 0x2c0
+  __DATA_CONST.__auth_ptr: 0xd0
+  __DATA.__objc_const: 0x11a0
+  __DATA.__objc_selrefs: 0xb40
   __DATA.__objc_ivar: 0xac
-  __DATA.__objc_data: 0x528
-  __DATA.__data: 0x3b8
+  __DATA.__objc_data: 0x568
+  __DATA.__data: 0x3e0
   __DATA.__common: 0x28
   __INFO_FILTER.__disable: 0x0
   - /AppleInternal/Library/Frameworks/TapToRadarKit.framework/TapToRadarKit

   - /usr/lib/swift/libswiftXPC.dylib
   - /usr/lib/swift/libswift_Builtin_float.dylib
   - /usr/lib/swift/libswiftos.dylib
-  Functions: 898
-  Symbols:   408
-  CStrings:  1368
+  Functions: 915
+  Symbols:   430
+  CStrings:  1379
 
Symbols:
+ _$s15CoreDiagnostics18PanicPatternActionO21collectFullLogArchiveyA2CmFWC
+ _$s8RawValueSYTl
+ _$sBi64_WV
+ _$sSH13_rawHashValue4seedS2i_tFTq
+ _$sSH4hash4intoys6HasherVz_tFTq
+ _$sSH9hashValueSivgTq
+ _$sSHMp
+ _$sSHSQTb
+ _$sSQ2eeoiySbx_xtFZTq
+ _$sSQMp
+ _$sSSN
+ _$sSY8rawValue03RawB0QzvgTq
+ _$sSY8rawValuexSg03RawB0Qz_tcfCTq
+ _$sSYMp
+ _$ss6HasherV5_seedABSi_tcfC
+ _$ss6HasherV8_combineyySuF
+ _$ss6HasherV9_finalizeSiyF
+ _swift_arrayInitWithCopy
+ _swift_arrayInitWithTakeBackToFront
+ _swift_arrayInitWithTakeFrontToBack
+ _swift_release_x8
+ _swift_release_x9
CStrings:
+ "\n\nFull log archive requested by pattern(s): %@"
+ ", "
+ "Full log archive requested by %s"
+ "No matched panic pattern with a donate type"
+ "Tq,N,VcollectionLevel"
+ "collectionLevel"
+ "collectionPatternUUIDs"
+ "q"
+ "q16@0:8"
+ "setCollectionLevel:"
+ "setCollectionPatternUUIDs:"
+ "v24@0:8q16"
- "Failed to find matched panic pattern"
```
