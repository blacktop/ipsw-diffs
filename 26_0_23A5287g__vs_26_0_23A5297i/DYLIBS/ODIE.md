## ODIE

> `/System/Library/PrivateFrameworks/ODIE.framework/ODIE`

```diff

-3500.23.2.0.0
-  __TEXT.__text: 0x190b54
-  __TEXT.__auth_stubs: 0x1610
+3500.25.1.0.0
+  __TEXT.__text: 0x1b80e8
+  __TEXT.__auth_stubs: 0x16b0
   __TEXT.__delay_stubs: 0x58
   __TEXT.__delay_helper: 0xa4
   __TEXT.__objc_methlist: 0x244
-  __TEXT.__const: 0x6420
-  __TEXT.__constg_swiftt: 0x220c
-  __TEXT.__swift5_typeref: 0x17ba
-  __TEXT.__swift5_reflstr: 0xfd9
-  __TEXT.__swift5_fieldmd: 0x208c
-  __TEXT.__swift5_builtin: 0x140
-  __TEXT.__swift5_proto: 0x3e4
-  __TEXT.__swift5_types: 0x358
-  __TEXT.__cstring: 0x3d60
-  __TEXT.__swift5_mpenum: 0xd4
+  __TEXT.__const: 0x6584
+  __TEXT.__cstring: 0x4073
+  __TEXT.__swift5_typeref: 0x1991
+  __TEXT.__constg_swiftt: 0x26e0
+  __TEXT.__swift5_fieldmd: 0x2560
+  __TEXT.__swift5_builtin: 0x168
+  __TEXT.__swift5_reflstr: 0x12ae
+  __TEXT.__swift5_proto: 0x414
+  __TEXT.__swift5_types: 0x3a4
+  __TEXT.__oslogstring: 0x3
+  __TEXT.__swift5_protos: 0x6c
+  __TEXT.__swift5_mpenum: 0xc8
   __TEXT.__swift5_capture: 0x67c
-  __TEXT.__swift5_protos: 0x58
   __TEXT.__swift_as_entry: 0x1c
   __TEXT.__swift_as_ret: 0x18
-  __TEXT.__oslogstring: 0x3
-  __TEXT.__swift5_assocty: 0x230
-  __TEXT.__swift5_types2: 0x10
-  __TEXT.__unwind_info: 0x3aa8
-  __TEXT.__eh_frame: 0xda54
+  __TEXT.__swift5_types2: 0x1c
+  __TEXT.__swift5_assocty: 0x278
+  __TEXT.__unwind_info: 0x3d28
+  __TEXT.__eh_frame: 0xe784
   __TEXT.__objc_classname: 0x2d
   __TEXT.__objc_methname: 0x3bd
   __TEXT.__objc_methtype: 0x205
-  __DATA_CONST.__got: 0x348
+  __DATA_CONST.__got: 0x350
   __DATA_CONST.__const: 0xe8
-  __DATA_CONST.__objc_classlist: 0x78
+  __DATA_CONST.__objc_classlist: 0xa8
   __DATA_CONST.__objc_protolist: 0x40
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_selrefs: 0x1a8
   __DATA_CONST.__objc_protorefs: 0x20
-  __AUTH_CONST.__auth_got: 0xb18
-  __AUTH_CONST.__const: 0x6aa8
-  __AUTH_CONST.__objc_const: 0xee8
-  __AUTH.__objc_data: 0xa0
-  __AUTH.__data: 0xfe0
-  __DATA.__data: 0xea4
-  __DATA.__bss: 0x1e00
-  __DATA.__common: 0xc8
+  __AUTH_CONST.__auth_got: 0xb68
+  __AUTH_CONST.__const: 0x71c8
+  __AUTH_CONST.__objc_const: 0x1560
+  __AUTH.__objc_data: 0x50
+  __AUTH.__data: 0x15a0
+  __DATA.__data: 0xeec
+  __DATA.__common: 0xb0
+  __DATA.__bss: 0x2100
   - /System/Library/Frameworks/Foundation.framework/Foundation
   - /System/Library/Frameworks/IOSurface.framework/IOSurface
   - /System/Library/Frameworks/Metal.framework/Metal

   - /usr/lib/swift/libswiftAccelerate.dylib
   - /usr/lib/swift/libswiftCore.dylib
   - /usr/lib/swift/libswiftCoreFoundation.dylib
+  - /usr/lib/swift/libswiftDarwin.dylib
   - /usr/lib/swift/libswiftDispatch.dylib
   - /usr/lib/swift/libswiftMetal.dylib
   - /usr/lib/swift/libswiftOSLog.dylib

   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  UUID: 3CF068AA-095F-373B-A626-F1662495BECC
-  Functions: 4567
-  Symbols:   194
-  CStrings:  472
+  UUID: A0998356-1EA7-3C55-BAD6-5510F46F4A27
+  Functions: 4713
+  Symbols:   199
+  CStrings:  503
 
Symbols:
+ _close
+ _fstat
+ _getpagesize
+ _mmap
+ _munmap
+ _objc_retain_x23
- _objc_retain_x25
CStrings:
+ "\nbuilder debug:\n{ finished: "
+ ",\n{ writtenSize: "
+ ", \nwith capacity of "
+ ", serializeDefaults: "
+ ", with capacity of "
+ "Byte count must be a multiple of "
+ "Can only store scalars containing up to "
+ "No definition available for function '"
+ "ODIE/ElementWiseBinaryKernel.swift"
+ "ODIE/Scalar.swift"
+ "ODIE/TensorRequirements.swift"
+ "ODIX header missing."
+ "Trying to link non-function symbol as a function: "
+ "Unknown allocation type "
+ "] is not broadcastable."
+ "_TtC4ODIE13TensorBacking"
+ "_TtCV4ODIE10ByteBuffer7Storage"
+ "_TtCV4ODIE17FlatBufferBuilder13VTableStorage"
+ "_TtCV4ODIE17InferenceFunction14ExecutablePool"
+ "_TtCV4ODIE19_InternalByteBuffer7Storage"
+ "_TtCV4ODIE6Tensor11SharedBytes"
+ "_TtCV4ODIE8VerifierP33_EA900E0FB61CEF2950ED7DF4827DBA9B7Storage"
+ "apparentSize"
+ "buffer located at: "
+ "capacity"
+ "dependencies"
+ "depth"
+ "function"
+ "isOwned"
+ "layout"
+ "maxOffset"
+ "memory"
+ "memoryInUse"
+ "mutexBuffer"
+ "numOfFields"
+ "retainedBlob"
+ "size"
+ "storage"
+ "tableCount"
+ "unowned"
+ "writtenIndex"
- "Branch condition must be a scalar"
- "Expected output to be an NDArray"
- "External IO was not provided at index "
- "ODIE/ElementWiseKernel.swift"
- "Skipping initRegion since it could not be found."
- "_TtC4ODIE22CallableMemberFunction"
- "buffer with capacity of "
- "initRegions"
- "memberFunction"
- "registers"

```
