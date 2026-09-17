## BackBoardHIDEventFoundation

> `/System/Library/PrivateFrameworks/BackBoardHIDEventFoundation.framework/Versions/A/BackBoardHIDEventFoundation`

```diff

-877.0.0.0.0
-  __TEXT.__text: 0x43024
+877.2.1.0.0
+  __TEXT.__text: 0x438d0
   __TEXT.__objc_methlist: 0x23c0
-  __TEXT.__const: 0x694
+  __TEXT.__const: 0x68c
   __TEXT.__constg_swiftt: 0x1b0
   __TEXT.__swift5_typeref: 0x225
   __TEXT.__swift5_reflstr: 0x12c
   __TEXT.__swift5_fieldmd: 0x1bc
   __TEXT.__swift5_builtin: 0x28
-  __TEXT.__cstring: 0x33bb
+  __TEXT.__cstring: 0x347f
   __TEXT.__swift5_types: 0x24
   __TEXT.__swift5_proto: 0x24
   __TEXT.__swift5_mpenum: 0x8
   __TEXT.__swift5_assocty: 0x18
-  __TEXT.__gcc_except_tab: 0x4a0
-  __TEXT.__oslogstring: 0x33b0
-  __TEXT.__unwind_info: 0xfa8
+  __TEXT.__gcc_except_tab: 0x568
+  __TEXT.__oslogstring: 0x34e8
+  __TEXT.__unwind_info: 0xfc0
   __TEXT.__eh_frame: 0x158
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0

   __DATA_CONST.__objc_catlist: 0x8
   __DATA_CONST.__objc_protolist: 0x108
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x1540
+  __DATA_CONST.__objc_selrefs: 0x1560
   __DATA_CONST.__objc_protorefs: 0x28
   __DATA_CONST.__objc_superrefs: 0x120
   __DATA_CONST.__objc_arraydata: 0x290
   __DATA_CONST.__got: 0x438
-  __AUTH_CONST.__const: 0x1e48
-  __AUTH_CONST.__cfstring: 0x2ba0
+  __AUTH_CONST.__const: 0x1e78
+  __AUTH_CONST.__cfstring: 0x2be0
   __AUTH_CONST.__objc_const: 0x62e8
   __AUTH_CONST.__objc_intobj: 0x3d8
   __AUTH_CONST.__objc_dictobj: 0x28

   - /usr/lib/swift/libswift_Builtin_float.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  Functions: 1150
-  Symbols:   2957
-  CStrings:  701
+  Functions: 1155
+  Symbols:   2967
+  CStrings:  708
 
Symbols:
+ -[BKEventDeferringEnvironmentGraph _publishSelectionChangesForReason:]
+ GCC_except_table275
+ GCC_except_table315
+ GCC_except_table372
+ GCC_except_table432
+ GCC_except_table445
+ GCC_except_table450
+ GCC_except_table457
+ GCC_except_table460
+ GCC_except_table495
+ GCC_except_table499
+ GCC_except_table726
+ GCC_except_table729
+ GCC_except_table766
+ GCC_except_table813
+ GCC_except_table874
+ GCC_except_table887
+ GCC_except_table919
+ ___64-[BKEventDeferringEnvironmentGraph _requestsSortedByGraphDepth:]_block_invoke
+ ___66-[BKEventDeferringGraph requestSelectionChanges:forClientWithPID:]_block_invoke
+ ___76-[BKHIDEventDeliveryManager _lock_requestSelectionChanges:forClientWithPID:]_block_invoke_2
+ ___block_descriptor_40_e8_32s_e99_q24?0"BKSHIDEventDeferringSelectionChangeRequest"8"BKSHIDEventDeferringSelectionChangeRequest"16l
+ ___block_descriptor_44_e8_32s_e52_B16?0"BKSHIDEventDeferringSelectionChangeRequest"8l
+ ___block_descriptor_77_e8_32s40s48s56r64r_e48_v16?0"BKEventDeferringSelectionPathContainer"8l
+ ___copy_helper_block_e8_32s40s48s56r64r
+ ___destroy_helper_block_e8_32s40s48s56r64r
+ _objc_msgSend$compare:
+ _objc_msgSend$numberWithUnsignedInteger:
+ _objc_msgSend$sortWithOptions:usingComparator:
+ _objc_msgSend$strongToStrongObjectsMapTable
- GCC_except_table274
- GCC_except_table314
- GCC_except_table371
- GCC_except_table431
- GCC_except_table444
- GCC_except_table449
- GCC_except_table456
- GCC_except_table459
- GCC_except_table494
- GCC_except_table498
- GCC_except_table725
- GCC_except_table728
- GCC_except_table765
- GCC_except_table812
- GCC_except_table873
- GCC_except_table885
- GCC_except_table917
- ___65-[BKEventDeferringGraph requestSelectionChange:forClientWithPID:]_block_invoke
- ___block_descriptor_44_e8_32s_e54_v24?0"BKEventDeferringEnvironmentGraph"8"NSArray"16l
- ___block_descriptor_61_e8_32s40s48s_e48_v16?0"BKEventDeferringSelectionPathContainer"8l
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
