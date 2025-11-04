## RawCamera

> `/System/Library/CoreServices/RawCamera.bundle/RawCamera`

```diff

-1756.40.8.0.0
-  __TEXT.__text: 0x1e0654
-  __TEXT.__auth_stubs: 0x17c0
+1756.60.6.122.2
+  __TEXT.__text: 0x1ec518
+  __TEXT.__auth_stubs: 0x1a60
   __TEXT.__objc_methlist: 0x16e4
-  __TEXT.__const: 0x14986
-  __TEXT.__gcc_except_tab: 0x2d8bc
-  __TEXT.__oslogstring: 0x1146
-  __TEXT.__cstring: 0xedf1
+  __TEXT.__const: 0x14f64
+  __TEXT.__gcc_except_tab: 0x2de5c
+  __TEXT.__oslogstring: 0x1b1b
+  __TEXT.__cstring: 0xeea2
+  __TEXT.__constg_swiftt: 0x288
+  __TEXT.__swift5_typeref: 0x167
+  __TEXT.__swift5_reflstr: 0x2d3
+  __TEXT.__swift5_fieldmd: 0x3f0
+  __TEXT.__swift5_types2: 0xc
+  __TEXT.__swift5_capture: 0x4c
+  __TEXT.__swift5_assocty: 0x48
+  __TEXT.__swift5_proto: 0x30
+  __TEXT.__swift5_types: 0x2c
   __TEXT.__dof_RawCamera: 0x8f7
-  __TEXT.__unwind_info: 0xb378
-  __TEXT.__eh_frame: 0x278
+  __TEXT.__unwind_info: 0xb5a8
+  __TEXT.__eh_frame: 0x470
   __TEXT.__objc_classname: 0x4b9
-  __TEXT.__objc_methname: 0x3755
-  __TEXT.__objc_methtype: 0xbed
+  __TEXT.__objc_methname: 0x3775
+  __TEXT.__objc_methtype: 0xc11
   __TEXT.__objc_stubs: 0x2d80
-  __DATA_CONST.__got: 0x9d8
-  __DATA_CONST.__const: 0x29b0
+  __DATA_CONST.__got: 0xa30
+  __DATA_CONST.__const: 0x29c0
   __DATA_CONST.__objc_classlist: 0x1e0
   __DATA_CONST.__objc_catlist: 0x20
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_selrefs: 0xcf0
   __DATA_CONST.__objc_superrefs: 0xf0
   __DATA_CONST.__objc_arraydata: 0x3980
-  __AUTH_CONST.__auth_got: 0xbf8
-  __AUTH_CONST.__const: 0x359e0
+  __AUTH_CONST.__auth_got: 0xd48
+  __AUTH_CONST.__const: 0x36250
   __AUTH_CONST.__cfstring: 0x18080
   __AUTH_CONST.__objc_const: 0x48b0
   __AUTH_CONST.__objc_arrayobj: 0x588

   __AUTH.__thread_vars: 0x30
   __AUTH.__thread_bss: 0x18
   __DATA.__objc_ivar: 0x428
-  __DATA.__data: 0x20688
-  __DATA.__bss: 0x6280
+  __DATA.__data: 0x208a0
+  __DATA.__bss: 0x6880
   __DATA.__common: 0x4
   __DATA_DIRTY.__objc_data: 0x12c0
   __DATA_DIRTY.__data: 0x48

   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libxml2.2.dylib
   - /usr/lib/libz.1.dylib
-  UUID: E90744D8-64D6-3583-9A61-9F65FB295D42
-  Functions: 6495
-  Symbols:   778
-  CStrings:  7500
+  - /usr/lib/swift/libswiftCore.dylib
+  - /usr/lib/swift/libswiftCoreFoundation.dylib
+  - /usr/lib/swift/libswiftDarwin.dylib
+  - /usr/lib/swift/libswiftDispatch.dylib
+  - /usr/lib/swift/libswiftObjectiveC.dylib
+  - /usr/lib/swift/libswiftXPC.dylib
+  - /usr/lib/swift/libswift_Builtin_float.dylib
+  UUID: CC572C09-F206-35B9-B4A1-AC090F22B328
+  Functions: 6718
+  Symbols:   814
+  CStrings:  7559
 
Symbols:
+ _CMPhotoDecompressionContainerGetImageCountWithOptions
+ _OBJC_CLASS_$_OS_dispatch_queue
+ __Block_copy
+ __Block_release
+ __ZTISt9bad_alloc
+ __ZTISt9exception
+ __swiftEmptyArrayStorage
+ __swift_FORCE_LOAD_$_swiftCoreFoundation
+ __swift_FORCE_LOAD_$_swiftDispatch
+ __swift_FORCE_LOAD_$_swiftFoundation
+ __swift_FORCE_LOAD_$_swiftObjectiveC
+ __swift_FORCE_LOAD_$_swiftXPC
+ __swift_FORCE_LOAD_$_swift_Builtin_float
+ _objc_opt_self
+ _swift_allocObject
+ _swift_arrayDestroy
+ _swift_beginAccess
+ _swift_cvw_allocateGenericValueMetadataWithLayoutString
+ _swift_cvw_assignWithCopy
+ _swift_cvw_assignWithTake
+ _swift_cvw_destroy
+ _swift_cvw_initWithCopy
+ _swift_cvw_initializeBufferWithCopyOfBuffer
+ _swift_deallocObject
+ _swift_endAccess
+ _swift_getGenericMetadata
+ _swift_getObjCClassMetadata
+ _swift_getTypeByMangledNameInContext2
+ _swift_getTypeByMangledNameInContextInMetadataState2
+ _swift_getWitnessTable
+ _swift_once
+ _swift_release
+ _swift_retain
+ _swift_runtimeSupportsNoncopyableTypes
+ _swift_slowAlloc
+ _swift_slowDealloc
+ _swift_willThrowTypedImpl
- _CMPhotoDecompressionContainerGetImageCount
CStrings:
+ "%{public}s Buffer size too small: %zu"
+ "%{public}s Destination buffer access would exceed bounds: %zu > %zu"
+ "%{public}s Error calling JxlDecoderSetPreferredColorProfile for original profile"
+ "%{public}s Error from JxlDecoderGetBasicInfo"
+ "%{public}s Error from JxlDecoderProcessInput, expected JXL_DEC_BASIC_INFO"
+ "%{public}s Error from JxlDecoderProcessInput, expected JXL_DEC_COLOR_ENCODING"
+ "%{public}s Error from JxlDecoderSetInput"
+ "%{public}s Exception in curve generation: %s"
+ "%{public}s Exception in readTile: %s"
+ "%{public}s Exception in renderSensorDataToBitmap: %s"
+ "%{public}s Exception in tile coordinate calculation for tile %u: %s"
+ "%{public}s Exception in tile count validation: %s"
+ "%{public}s Exception in tile processing: %s"
+ "%{public}s Exception in unpackSensorData: %s"
+ "%{public}s Failed to allocate staging buffer of size %zu: %s"
+ "%{public}s Failed to read first tile"
+ "%{public}s First tile offset out of bounds"
+ "%{public}s Incorrect number of tiles: expected %u, got %u"
+ "%{public}s Input buffer access out of bounds: %zu + 3 > %zu"
+ "%{public}s Integer overflow calculating buffer size in uint16s: %s"
+ "%{public}s Integer overflow calculating destination buffer size: %s"
+ "%{public}s Integer overflow calculating tile sizes: %s"
+ "%{public}s Integer overflow in alignedSensorRowBytes: %s"
+ "%{public}s Integer overflow in tile coordinate calculation for tile %u: %s"
+ "%{public}s Integer overflow in tile data length calculation: %s"
+ "%{public}s Integer overflow in unpackTile: %s"
+ "%{public}s Invalid first tile byte count"
+ "%{public}s Invalid float bit pattern 0x%04x at pixel (%zu, %zu), replacing with 0"
+ "%{public}s Invalid row bytes calculation at row %zu"
+ "%{public}s Invalid sensor height: %u"
+ "%{public}s Invalid sensor width: %u"
+ "%{public}s Invalid tile %zu byte count: %u"
+ "%{public}s Invalid tile byte count: %u"
+ "%{public}s Invalid tile data pointers: end < start"
+ "%{public}s Invalid tile height: %u"
+ "%{public}s Invalid tile width: %u"
+ "%{public}s No tiles available"
+ "%{public}s Row %zu is less than tile origin %u or src origin %u"
+ "%{public}s Skipping tile %u due to read error"
+ "%{public}s Sum of tile sizes exceeds file size"
+ "%{public}s Tile %zu data extends beyond file"
+ "%{public}s Tile %zu offset %u out of bounds (file size: %u)"
+ "%{public}s Tile data extends beyond file"
+ "%{public}s Tile index %u out of bounds"
+ "%{public}s Tile offset %u out of bounds (file size: %u)"
+ "%{public}s Too many tiles: %u"
+ "%{public}s Unexpected number of tiles"
+ "%{public}s Unknown exception in readTile"
+ "%{public}s Unknown exception in tile processing"
+ "CFujiCompressedUnpacker"
+ "T{CCameraProfile=^^?ii{CMatrix=II{vector<double, std::allocator<double>>=^d^d{?=^d}}}{CMatrix=II{vector<double, std::allocator<double>>=^d^d{?=^d}}}{CMatrix=II{vector<double, std::allocator<double>>=^d^d{?=^d}}}{CMatrix=II{vector<double, std::allocator<double>>=^d^d{?=^d}}}{CMatrix=II{vector<double, std::allocator<double>>=^d^d{?=^d}}}{CMatrix=II{vector<double, std::allocator<double>>=^d^d{?=^d}}}S{CMatrix=II{vector<double, std::allocator<double>>=^d^d{?=^d}}}{CMatrix=II{vector<double, std::allocator<double>>=^d^d{?=^d}}}},R,N"
+ "alignedSensorRowBytes"
+ "hasSupportedColorProfile"
+ "initializeCurve"
+ "operator()"
+ "readTile"
+ "renderSensorDataToBitmap"
+ "unpackSensorData"
+ "unpackTile"
+ "validateTileData"
+ "{CCameraProfile=^^?ii{CMatrix=II{vector<double, std::allocator<double>>=^d^d{?=^d}}}{CMatrix=II{vector<double, std::allocator<double>>=^d^d{?=^d}}}{CMatrix=II{vector<double, std::allocator<double>>=^d^d{?=^d}}}{CMatrix=II{vector<double, std::allocator<double>>=^d^d{?=^d}}}{CMatrix=II{vector<double, std::allocator<double>>=^d^d{?=^d}}}{CMatrix=II{vector<double, std::allocator<double>>=^d^d{?=^d}}}S{CMatrix=II{vector<double, std::allocator<double>>=^d^d{?=^d}}}{CMatrix=II{vector<double, std::allocator<double>>=^d^d{?=^d}}}}16@0:8"
+ "{CMatrix=II{vector<double, std::allocator<double>>=^d^d{?=^d}}}40@0:8@16Q24Q32"
+ "{CMatrix=II{vector<double, std::allocator<double>>=^d^d{?=^d}}}8@?0"
+ "{basic_string<char, std::char_traits<char>, std::allocator<char>>={?=(__rep={__short=[23c]b7b1}{__long=*Qb63b1})}}8@?0"
+ "{vector<double, std::allocator<double>>=^d^d{?=^d}}8@?0"
+ "{vector<int, std::allocator<int>>=^i^i{?=^i}}8@?0"
+ "{vector<unsigned int, std::allocator<unsigned int>>=^I^I{?=^I}}8@?0"
+ "{vector<unsigned short, std::allocator<unsigned short>>=^S^S{?=^S}}8@?0"
- "T{CCameraProfile=^^?ii{CMatrix=II{vector<double, std::allocator<double>>=^d^d^d}}{CMatrix=II{vector<double, std::allocator<double>>=^d^d^d}}{CMatrix=II{vector<double, std::allocator<double>>=^d^d^d}}{CMatrix=II{vector<double, std::allocator<double>>=^d^d^d}}{CMatrix=II{vector<double, std::allocator<double>>=^d^d^d}}{CMatrix=II{vector<double, std::allocator<double>>=^d^d^d}}S{CMatrix=II{vector<double, std::allocator<double>>=^d^d^d}}{CMatrix=II{vector<double, std::allocator<double>>=^d^d^d}}},R,N"
- "{CCameraProfile=^^?ii{CMatrix=II{vector<double, std::allocator<double>>=^d^d^d}}{CMatrix=II{vector<double, std::allocator<double>>=^d^d^d}}{CMatrix=II{vector<double, std::allocator<double>>=^d^d^d}}{CMatrix=II{vector<double, std::allocator<double>>=^d^d^d}}{CMatrix=II{vector<double, std::allocator<double>>=^d^d^d}}{CMatrix=II{vector<double, std::allocator<double>>=^d^d^d}}S{CMatrix=II{vector<double, std::allocator<double>>=^d^d^d}}{CMatrix=II{vector<double, std::allocator<double>>=^d^d^d}}}16@0:8"
- "{CMatrix=II{vector<double, std::allocator<double>>=^d^d^d}}40@0:8@16Q24Q32"
- "{CMatrix=II{vector<double, std::allocator<double>>=^d^d^d}}8@?0"
- "{basic_string<char, std::char_traits<char>, std::allocator<char>>=(__rep={__short=[23c]b7b1}{__long=*Qb63b1})}8@?0"
- "{vector<double, std::allocator<double>>=^d^d^d}8@?0"
- "{vector<int, std::allocator<int>>=^i^i^i}8@?0"
- "{vector<unsigned int, std::allocator<unsigned int>>=^I^I^I}8@?0"
- "{vector<unsigned short, std::allocator<unsigned short>>=^S^S^S}8@?0"

```
