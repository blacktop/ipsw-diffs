## EXSurface

> `/System/ExclaveKit/System/Library/PrivateFrameworks/EXSurface.framework/EXSurface`

```diff

-14.0.3.0.0
-  __TEXT.__text: 0x4c70
-  __TEXT.__auth_stubs: 0x5f0
+14.2.7.0.0
+  __TEXT.__text: 0x51c4
+  __TEXT.__auth_stubs: 0x620
   __TEXT.__objc_stubs: 0x520
-  __TEXT.__objc_methlist: 0x7dc
-  __TEXT.__cstring: 0x6a7
-  __TEXT.__objc_methname: 0x923
+  __TEXT.__objc_methlist: 0x7fc
+  __TEXT.__cstring: 0x707
+  __TEXT.__objc_methname: 0x957
   __TEXT.__objc_classname: 0x14f
-  __TEXT.__objc_methtype: 0x44c
+  __TEXT.__objc_methtype: 0x477
   __TEXT.__const: 0x1f2
   __TEXT.__constg_swiftt: 0x104
   __TEXT.__swift5_typeref: 0x176

   __TEXT.__swift5_builtin: 0x28
   __TEXT.__swift5_mpenum: 0x1c
   __TEXT.__swift5_protos: 0x4
-  __TEXT.__unwind_info: 0x220
-  __TEXT.__eh_frame: 0x180
-  __DATA.__auth_got: 0x300
-  __DATA.__got: 0x58
-  __DATA.__auth_ptr: 0x78
+  __TEXT.__unwind_info: 0x250
+  __TEXT.__eh_frame: 0x220
+  __DATA.__auth_got: 0x318
+  __DATA.__got: 0x70
+  __DATA.__auth_ptr: 0x80
   __DATA.__const: 0x388
   __DATA.__cfstring: 0x40
   __DATA.__objc_classlist: 0x68
   __DATA.__objc_protolist: 0x18
   __DATA.__objc_imageinfo: 0x8
   __DATA.__objc_const: 0x1778
-  __DATA.__objc_selrefs: 0x228
+  __DATA.__objc_selrefs: 0x238
   __DATA.__objc_superrefs: 0x58
-  __DATA.__objc_ivar: 0xc0
+  __DATA.__objc_ivar: 0xbc
   __DATA.__objc_data: 0x480
   __DATA.__data: 0x170
   __DATA.__bss: 0x110

   - /System/ExclaveKit/usr/lib/swift/libswift_math.dylib
   - /System/ExclaveKit/usr/lib/swift/libswift_stdio.dylib
   - /System/ExclaveKit/usr/lib/swift/libswift_time.dylib
-  Functions: 242
-  Symbols:   675
-  CStrings:  246
+  Functions: 250
+  Symbols:   688
+  CStrings:  250
 
Symbols:
+ +[EXSurfaceMemoryRegion newMemoryRegionWithSegAccess:error:]
+ -[EXSurface getMutableBytesWithHandler:]
+ -[EXSurfacePlane getMutableBytesWithHandler:]
+ _$sSo20EXSurfaceImageLayoutP0A0E22withUnsafeMutableBytesyyySvSgXEF
+ _$sSo20EXSurfaceImageLayoutP0A0E22withUnsafeMutableBytesyyySvSgXEFyyXEfU_TA
+ _$sSo21EXSurfaceMemoryRegionC0A0E04makebC09segAccess0E7BackingABSg06SharedB007SegmentF0C_AH0iG0CSgtKFZ
+ _$sSo21EXSurfaceMemoryRegionC0A0E04makebC09segAccessABSg06SharedB007SegmentF0C_tKFZ
+ _$sSo9EXSurfaceCAAE22withUnsafeMutableBytesyyySvSgXEF
+ _$ss20withExtendedLifetimeyq0_x_q0_yq_YKXEtq_YKs5ErrorR_Ri_zRi_0_r1_lF
+ _$ss5NeverON
+ _$ss5NeverOs5ErrorsWP
+ _$sytN
+ _objc_autorelease
+ _puts
+ _swift_unknownObjectRetain
- OBJC_IVAR_$_EXSurfaceMemoryRegionExclaveKit._segBacking
- _$sSo21EXSurfaceMemoryRegionC0A0E04makebC09segAccess0E7BackingABSg06SharedB007SegmentF0C_AH0iG0CtKFZ
CStrings:
+ "@32@0:8^{sharedmemory_segaccess_s=}16^@24"
+ "[EXSurfaceMemoryRegion WARNING] Please use newMemoryRegionWithSegAccess without segBacking."
+ "getMutableBytesWithHandler:"
+ "newMemoryRegionWithSegAccess:error:"
+ "v24@0:8@?16"
+ "v24@0:8@?<v@?^v>16"
- "^{sharedmemory_segbacking_s=}"
- "_segBacking"

```
