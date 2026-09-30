## MTLCompiler

> `/System/Library/PrivateFrameworks/MTLCompiler.framework/Versions/32024/MTLCompiler`

```diff

 382.5.3.0.0
-  __TEXT.__text: 0xb7a58
-  __TEXT.__gcc_except_tab: 0xa548
+  __TEXT.__text: 0xb8abc
+  __TEXT.__gcc_except_tab: 0xa6c4
   __TEXT.__const: 0x1288
-  __TEXT.__cstring: 0x96e7
+  __TEXT.__cstring: 0x9841
   __TEXT.__oslogstring: 0x4e7
-  __TEXT.__unwind_info: 0x2f58
+  __TEXT.__unwind_info: 0x2f90
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0
   __TEXT.__objc_methname: 0x0

   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_selrefs: 0xf0
   __DATA_CONST.__got: 0x0
-  __AUTH_CONST.__const: 0x16b0
+  __AUTH_CONST.__const: 0x1750
   __AUTH_CONST.__cfstring: 0x220
   __AUTH_CONST.__weak_auth_got: 0x50
   __AUTH_CONST.__auth_got: 0x10f8

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libc++.1.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 2144
-  Symbols:   3468
-  CStrings:  1639
+  Functions: 2155
+  Symbols:   3481
+  CStrings:  1653
 
Symbols:
+ GCC_except_table520
+ GCC_except_table523
+ __Z23createMTLYieldCheckPassRN14MTLBoundsCheck14SharedPassDataE
+ __ZN17MTLYieldCheckPass11runOnModuleERN4llvm6ModuleE
+ __ZN17MTLYieldCheckPass15instrumentDylibEv
+ __ZN17MTLYieldCheckPass23isYieldRelatedIntrinsicEN4llvm9StringRefE
+ __ZN17MTLYieldCheckPass2IDE
+ __ZN17MTLYieldCheckPassD0Ev
+ __ZN17MTLYieldCheckPassD1Ev
+ __ZNK13AirReflection16PersistentFnAttr8HashImplERN11flatbuffers16SignatureBuilderE
+ __ZNK13AirReflection26ForwardProgressUsageFnAttr8HashImplERN11flatbuffers16SignatureBuilderE
+ __ZNK13AirReflection4Node24node_as_PersistentFnAttrEv
+ __ZNK13AirReflection4Node34node_as_ForwardProgressUsageFnAttrEv
+ __ZNK17MTLYieldCheckPass11getPassNameEv
+ __ZTV17MTLYieldCheckPass
+ __ZZN14MTLBoundsCheck29MTLAddBoundsCheckPipelineToPMERN4llvm6legacy11PassManagerEPNS_14SharedPassDataERKNS_7OptionsEPNS_10StatisticsEENK4$_21clES3_
+ __ZZN14MTLBoundsCheck29MTLAddBoundsCheckPipelineToPMERN4llvm6legacy11PassManagerEPNS_14SharedPassDataERKNS_7OptionsEPNS_10StatisticsEENK4$_26clES3_
+ __ZZN14MTLBoundsCheck29MTLAddBoundsCheckPipelineToPMERN4llvm6legacy11PassManagerEPNS_14SharedPassDataERKNS_7OptionsEPNS_10StatisticsEENK4$_29clES3_
- GCC_except_table513
- GCC_except_table519
- __ZZN14MTLBoundsCheck29MTLAddBoundsCheckPipelineToPMERN4llvm6legacy11PassManagerEPNS_14SharedPassDataERKNS_7OptionsEPNS_10StatisticsEENK4$_20clES3_
- __ZZN14MTLBoundsCheck29MTLAddBoundsCheckPipelineToPMERN4llvm6legacy11PassManagerEPNS_14SharedPassDataERKNS_7OptionsEPNS_10StatisticsEENK4$_25clES3_
- __ZZN14MTLBoundsCheck29MTLAddBoundsCheckPipelineToPMERN4llvm6legacy11PassManagerEPNS_14SharedPassDataERKNS_7OptionsEPNS_10StatisticsEENK4$_28clES3_
CStrings:
+ "AirReflection.ForwardProgressUsageFnAttr"
+ "AirReflection.PersistentFnAttr"
+ "MTLYieldCheckPass"
+ "YieldCheck"
+ "air.atomic_wait_value"
+ "air.atomic_wait_with_predicate"
+ "air.simdgroup_atomic_notify"
+ "air.simdgroup_atomic_wait_explicit"
+ "air.yield_simdgroup"
+ "writeUsageCheck"
+ "yield is not permitted in a non-compute pipeline"
+ "yield.after"
+ "yield.noncompute.error"
+ "yield.ok"
```
