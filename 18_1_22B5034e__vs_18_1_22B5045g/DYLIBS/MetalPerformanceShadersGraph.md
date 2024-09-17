## MetalPerformanceShadersGraph

> `/System/Library/Frameworks/MetalPerformanceShadersGraph.framework/MetalPerformanceShadersGraph`

```diff

-5.0.24.0.0
-  __TEXT.__text: 0x1099c98
-  __TEXT.__auth_stubs: 0x2680
+5.1.3.0.0
+  __TEXT.__text: 0x109a96c
+  __TEXT.__auth_stubs: 0x26a0
   __TEXT.__mpsgraph_init_: 0x6c
-  __TEXT.__objc_methlist: 0x608c
-  __TEXT.__gcc_except_tab: 0x57198
-  __TEXT.__cstring: 0xfbaab
-  __TEXT.__const: 0x59004
+  __TEXT.__objc_methlist: 0x60a4
+  __TEXT.__gcc_except_tab: 0x571a8
+  __TEXT.__cstring: 0xfbac9
+  __TEXT.__const: 0x58fd4
   __TEXT.__oslogstring: 0x51
-  __TEXT.__unwind_info: 0x275c0
+  __TEXT.__unwind_info: 0x275f0
   __TEXT.__eh_frame: 0x2458
-  __TEXT.__objc_classname: 0x1b21
-  __TEXT.__objc_methname: 0x1293b
-  __TEXT.__objc_methtype: 0x407f
-  __TEXT.__objc_stubs: 0x8ec0
+  __TEXT.__objc_classname: 0x1b1f
+  __TEXT.__objc_methname: 0x1295d
+  __TEXT.__objc_methtype: 0x416e
+  __TEXT.__objc_stubs: 0x8ee0
   __DATA_CONST.__got: 0x718
   __DATA_CONST.__const: 0x24138
   __DATA_CONST.__objc_classlist: 0x6f8
   __DATA_CONST.__objc_protolist: 0x38
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x3120
+  __DATA_CONST.__objc_selrefs: 0x3128
   __DATA_CONST.__objc_superrefs: 0x1b0
   __DATA_CONST.__objc_arraydata: 0xea0
-  __AUTH_CONST.__auth_got: 0x1350
+  __AUTH_CONST.__auth_got: 0x1360
   __AUTH_CONST.__auth_ptr: 0x60
   __AUTH_CONST.__const: 0x5ca08
-  __AUTH_CONST.__cfstring: 0xe9a0
-  __AUTH_CONST.__objc_const: 0xf100
+  __AUTH_CONST.__cfstring: 0xe9e0
+  __AUTH_CONST.__objc_const: 0xf120
   __AUTH_CONST.__objc_intobj: 0x510
   __AUTH_CONST.__objc_arrayobj: 0x1e90
   __AUTH_CONST.__objc_dictobj: 0x118

   __DATA.__data: 0x5e90
   __DATA.__common: 0x170a
   __DATA.__bss: 0x440
-  __DATA_DIRTY.__objc_ivar: 0x83c
+  __DATA_DIRTY.__objc_ivar: 0x840
   __DATA_DIRTY.__objc_data: 0x50
   __DATA_DIRTY.__data: 0xa8
   __DATA_DIRTY.__common: 0x3d8

   - /usr/lib/libc++.1.dylib
   - /usr/lib/libncurses.5.4.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 56792
-  Symbols:   62772
-  CStrings:  33007
+  Functions: 56800
+  Symbols:   62783
+  CStrings:  33011
 
Symbols:
+ _objc_sync_enter
+ _objc_sync_exit
CStrings:
+ "StringRef llvm::getTypeName() [DesiredTypeName = mlir::mps::(anonymous namespace)::LowerDequantize]"
+ "h%!d(MISSING)"
+ "getUserSetMinimumDeploymentTarget"
+ "validateMinimumDeploymentTargetVersion:forPlatform:"
+ "@56@0:8Q16{optional<MPSGraphOperatingSystemVersion>=(?=c{MPSGraphOperatingSystemVersion=qqq})B}24"
+ "v56@0:8{optional<MPSGraphOperatingSystemVersion>=(?=c{MPSGraphOperatingSystemVersion=qqq})B}16Q48"
+ "{optional<MPSGraphOperatingSystemVersion>=(?=c{MPSGraphOperatingSystemVersion=qqq})B}16@0:8"
+ "Expected to only find one core op."
+ "5.1.3"
+ "_userSetMinimumDeploymentTarget"
- "T@\"NSString\",&,V_minimumDeploymentTarget"
- "StringRef llvm::getTypeName() [DesiredTypeName = mlir::mps::(anonymous namespace)::MPS_LowerDequantize]"
- "validateMinimumDeploymentTargetForPlatform"
- "@48@0:8Q16{MPSGraphOperatingSystemVersion=qqq}24"
- "5.0.24"

```
