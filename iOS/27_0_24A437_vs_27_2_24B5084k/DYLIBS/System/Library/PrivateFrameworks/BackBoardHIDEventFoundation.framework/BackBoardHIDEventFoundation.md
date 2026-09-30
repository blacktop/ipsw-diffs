## BackBoardHIDEventFoundation

> `/System/Library/PrivateFrameworks/BackBoardHIDEventFoundation.framework/BackBoardHIDEventFoundation`

```diff

-877.0.0.0.0
-  __TEXT.__text: 0x3be38
+877.2.1.0.0
+  __TEXT.__text: 0x3c608
   __TEXT.__objc_methlist: 0x22e8
-  __TEXT.__const: 0x68c
+  __TEXT.__const: 0x684
   __TEXT.__constg_swiftt: 0x1b0
   __TEXT.__swift5_typeref: 0x225
   __TEXT.__swift5_reflstr: 0x12c
   __TEXT.__swift5_fieldmd: 0x1b0
   __TEXT.__swift5_builtin: 0x28
-  __TEXT.__cstring: 0x33af
+  __TEXT.__cstring: 0x3473
   __TEXT.__swift5_types: 0x24
   __TEXT.__swift5_proto: 0x24
   __TEXT.__swift5_mpenum: 0x8
   __TEXT.__swift5_assocty: 0x18
-  __TEXT.__gcc_except_tab: 0x3bc
-  __TEXT.__oslogstring: 0x3308
-  __TEXT.__unwind_info: 0xf08
+  __TEXT.__gcc_except_tab: 0x484
+  __TEXT.__oslogstring: 0x3440
+  __TEXT.__unwind_info: 0xf18
   __TEXT.__eh_frame: 0x158
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0
   __TEXT.__objc_classname: 0x0
   __TEXT.__objc_methname: 0x0
   __TEXT.__objc_methtype: 0x0
-  __DATA_CONST.__const: 0x15f8
+  __DATA_CONST.__const: 0x1620
   __DATA_CONST.__objc_classlist: 0x1b8
   __DATA_CONST.__objc_catlist: 0x8
   __DATA_CONST.__objc_protolist: 0x108
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x14a0
+  __DATA_CONST.__objc_selrefs: 0x14c0
   __DATA_CONST.__objc_protorefs: 0x28
   __DATA_CONST.__objc_superrefs: 0x118
   __DATA_CONST.__objc_arraydata: 0x290
   __DATA_CONST.__got: 0x408
   __AUTH_CONST.__const: 0xb58
-  __AUTH_CONST.__cfstring: 0x2b40
+  __AUTH_CONST.__cfstring: 0x2b80
   __AUTH_CONST.__objc_const: 0x6100
   __AUTH_CONST.__objc_intobj: 0x3d8
   __AUTH_CONST.__objc_dictobj: 0x28

   - /usr/lib/swift/libswiftXPC.dylib
   - /usr/lib/swift/libswift_Builtin_float.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  Functions: 1089
-  Symbols:   2898
-  CStrings:  688
+  Functions: 1092
+  Symbols:   2906
+  CStrings:  695
 
Symbols:
+ -[BKEventDeferringEnvironmentGraph _publishSelectionChangesForReason:]
+ GCC_except_table242
+ GCC_except_table282
+ GCC_except_table337
+ GCC_except_table395
+ GCC_except_table408
+ GCC_except_table411
+ GCC_except_table417
+ GCC_except_table420
+ GCC_except_table665
+ GCC_except_table668
+ GCC_except_table703
+ GCC_except_table752
+ GCC_except_table813
+ GCC_except_table826
+ GCC_except_table858
+ ___64-[BKEventDeferringEnvironmentGraph _requestsSortedByGraphDepth:]_block_invoke
+ ___66-[BKEventDeferringGraph requestSelectionChanges:forClientWithPID:]_block_invoke
+ ___76-[BKHIDEventDeliveryManager _lock_requestSelectionChanges:forClientWithPID:]_block_invoke_2
+ ___block_descriptor_40_e8_32s_e99_q24?0"BKSHIDEventDeferringSelectionChangeRequest"8"BKSHIDEventDeferringSelectionChangeRequest"16ls32l8
+ ___block_descriptor_44_e8_32s_e52_B16?0"BKSHIDEventDeferringSelectionChangeRequest"8ls32l8
+ ___block_descriptor_77_e8_32s40s48s56r64r_e48_v16?0"BKEventDeferringSelectionPathContainer"8lr56l8s32l8s40l8s48l8r64l8
+ _objc_msgSend$compare:
+ _objc_msgSend$numberWithUnsignedInteger:
+ _objc_msgSend$sortWithOptions:usingComparator:
+ _objc_msgSend$strongToStrongObjectsMapTable
- GCC_except_table241
- GCC_except_table281
- GCC_except_table336
- GCC_except_table394
- GCC_except_table407
- GCC_except_table410
- GCC_except_table416
- GCC_except_table419
- GCC_except_table664
- GCC_except_table667
- GCC_except_table702
- GCC_except_table751
- GCC_except_table812
- GCC_except_table824
- GCC_except_table856
- ___65-[BKEventDeferringGraph requestSelectionChange:forClientWithPID:]_block_invoke
- ___block_descriptor_44_e8_32s_e54_v24?0"BKEventDeferringEnvironmentGraph"8"NSArray"16ls32l8
- ___block_descriptor_61_e8_32s40s48s_e48_v16?0"BKEventDeferringSelectionPathContainer"8ls32l8s40l8s48l8
CStrings:
+ "[%{public}@ %p] admitted on %lu of %lu selection path(s) (%{public}@)"
+ "[%{public}@ %p] admitted on all %lu selection path(s) (%{public}@)"
+ "[%{public}@ %p] changeSelectionPath(%{public}@) reason:%{public}@  -> %{public}@ -- %{public}@"
+ "[%{public}@ %p] no selection path matched (%{public}@)"
+ "[%{public}@ %p] rejected on all %lu selection path(s) (%{public}@)"
+ "[%{public}@ %p] selection recorded reason:%{public}@ generation: %ld -- deferring chains resolve from this"
+ "q24@?0@\"BKSHIDEventDeferringSelectionChangeRequest\"8@\"BKSHIDEventDeferringSelectionChangeRequest\"16"
+ "selection recorded"
+ "selection recorded: target was already selected"
+ "selectionTransaction(%lu request(s))"
- "[%{public}@ %p] changeSelectionPath(%{public}@) reason:%{public}@  -> %{public}@ generation: %ld -- %{public}@"
- "[%{public}@ %p] selected (%{public}@)"
- "success"
```
