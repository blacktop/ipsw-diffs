## BackBoardHIDEventFoundation

> `/System/Library/PrivateFrameworks/BackBoardHIDEventFoundation.framework/BackBoardHIDEventFoundation`

```diff

-877.2.2.0.0
-  __TEXT.__text: 0x3c61c
-  __TEXT.__objc_methlist: 0x22e8
+877.3.5.0.0
+  __TEXT.__text: 0x3ccd4
+  __TEXT.__objc_methlist: 0x22f8
   __TEXT.__const: 0x684
   __TEXT.__constg_swiftt: 0x1b0
   __TEXT.__swift5_typeref: 0x225

   __TEXT.__swift5_proto: 0x24
   __TEXT.__swift5_mpenum: 0x8
   __TEXT.__swift5_assocty: 0x18
-  __TEXT.__gcc_except_tab: 0x484
-  __TEXT.__oslogstring: 0x3440
-  __TEXT.__unwind_info: 0xf18
+  __TEXT.__gcc_except_tab: 0x48c
+  __TEXT.__oslogstring: 0x34a8
+  __TEXT.__unwind_info: 0xf28
   __TEXT.__eh_frame: 0x158
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0

   __DATA_CONST.__objc_catlist: 0x8
   __DATA_CONST.__objc_protolist: 0x108
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x14c0
+  __DATA_CONST.__objc_selrefs: 0x14c8
   __DATA_CONST.__objc_protorefs: 0x28
   __DATA_CONST.__objc_superrefs: 0x118
   __DATA_CONST.__objc_arraydata: 0x290

   - /usr/lib/swift/libswiftXPC.dylib
   - /usr/lib/swift/libswift_Builtin_float.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  Functions: 1092
-  Symbols:   2430
-  CStrings:  695
+  Functions: 1096
+  Symbols:   2434
+  CStrings:  696
 
Symbols:
+ -[BKEventDeferringEnvironmentGraph _derivedPathForTreeContainingNode:selectionPath:]
+ -[BKEventDeferringEnvironmentGraph _grantAuthorizesSelectionForPID:toNode:onSelectionPath:derivedTargets:coveringGrantor:]
+ -[BKEventDeferringEnvironmentGraph _latestConstrainedSiblingTargetForTarget:siblingTargets:siblingNodes:predicateTargets:selectionPath:]
+ -[BKEventDeferringEnvironmentGraph _targetIsEffectivelySelected:selectionPath:pathIdentifier:derivedTargets:visited:]
+ -[BKEventDeferringEnvironmentGraph _targetsOnPath:]
+ -[BKEventDeferringSelectionPathContainer _assertion:isFromSourcePIDs:]
+ -[BKEventDeferringSelectionPathContainer recordSelectionHistoryForTarget:parentTarget:]
+ GCC_except_table814
+ GCC_except_table830
+ GCC_except_table862
- -[BKEventDeferringEnvironmentGraph _grantAuthorizesSelectionForPID:toNode:onSelectionPath:]
- -[BKEventDeferringEnvironmentGraph _targetIsEffectivelySelected:selectionPath:pathIdentifier:visited:]
- -[BKEventDeferringSelectionPathContainer latestConstrainedSiblingTargetForTarget:siblingTargets:]
- GCC_except_table813
- GCC_except_table826
- GCC_except_table858
CStrings:
+ "[%{public}@ %p] changeSelectionPath(%{public}@) recorded intent below grantor %{public}@ for %{public}@"
```
