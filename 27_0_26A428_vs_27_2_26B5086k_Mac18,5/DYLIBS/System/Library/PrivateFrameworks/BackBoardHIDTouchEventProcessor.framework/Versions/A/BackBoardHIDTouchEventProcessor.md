## BackBoardHIDTouchEventProcessor

> `/System/Library/PrivateFrameworks/BackBoardHIDTouchEventProcessor.framework/Versions/A/BackBoardHIDTouchEventProcessor`

```diff

-877.0.0.0.0
-  __TEXT.__text: 0x3bc54
-  __TEXT.__objc_methlist: 0x27d0
+877.2.1.0.0
+  __TEXT.__text: 0x3c0c8
+  __TEXT.__objc_methlist: 0x27e0
   __TEXT.__const: 0x400
   __TEXT.__constg_swiftt: 0x124
   __TEXT.__swift5_typeref: 0x164

   __TEXT.__swift5_fieldmd: 0xfc
   __TEXT.__swift5_builtin: 0x28
   __TEXT.__swift5_capture: 0x20
-  __TEXT.__cstring: 0x1e38
+  __TEXT.__cstring: 0x1e4f
   __TEXT.__swift5_types: 0x14
   __TEXT.__swift5_protos: 0x4
-  __TEXT.__gcc_except_tab: 0x3ea8
-  __TEXT.__oslogstring: 0x2c6b
+  __TEXT.__gcc_except_tab: 0x3f2c
+  __TEXT.__oslogstring: 0x2cc2
   __TEXT.__ustring: 0xc
-  __TEXT.__unwind_info: 0x1610
+  __TEXT.__unwind_info: 0x1638
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0
   __TEXT.__objc_classname: 0x0
   __TEXT.__objc_methname: 0x0
   __TEXT.__objc_methtype: 0x0
-  __DATA_CONST.__const: 0x538
+  __DATA_CONST.__const: 0x540
   __DATA_CONST.__objc_classlist: 0x228
   __DATA_CONST.__objc_catlist: 0x8
   __DATA_CONST.__objc_protolist: 0x110
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x1ae0
+  __DATA_CONST.__objc_selrefs: 0x1ae8
   __DATA_CONST.__objc_protorefs: 0x38
   __DATA_CONST.__objc_superrefs: 0x168
   __DATA_CONST.__objc_arraydata: 0x10
   __DATA_CONST.__got: 0x560
-  __AUTH_CONST.__const: 0x1970
-  __AUTH_CONST.__cfstring: 0x2000
+  __AUTH_CONST.__const: 0x19c0
+  __AUTH_CONST.__cfstring: 0x2020
   __AUTH_CONST.__objc_const: 0x6f20
   __AUTH_CONST.__objc_intobj: 0xd8
   __AUTH_CONST.__objc_arrayobj: 0x18

   - /usr/lib/swift/libswift_Builtin_float.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  Functions: 1121
-  Symbols:   3500
-  CStrings:  571
+  Functions: 1125
+  Symbols:   3508
+  CStrings:  573
 
Symbols:
+ -[BKDirectTouchState _cancelContacts:destinationPredicate:preserveHitTestPolicy:excludingContextIDs:preserveDestinations:]
+ -[BKHIDDirectTouchEventProcessor gestureCancelTouchesWithIdentifiers:]
+ GCC_except_table1034
+ GCC_except_table1042
+ GCC_except_table1044
+ GCC_except_table1045
+ GCC_except_table1047
+ GCC_except_table468
+ GCC_except_table469
+ GCC_except_table477
+ GCC_except_table478
+ GCC_except_table482
+ GCC_except_table483
+ GCC_except_table492
+ GCC_except_table494
+ GCC_except_table496
+ GCC_except_table565
+ GCC_except_table609
+ GCC_except_table637
+ GCC_except_table661
+ GCC_except_table663
+ GCC_except_table665
+ GCC_except_table667
+ GCC_except_table685
+ GCC_except_table738
+ GCC_except_table746
+ GCC_except_table747
+ GCC_except_table754
+ GCC_except_table759
+ GCC_except_table763
+ GCC_except_table768
+ GCC_except_table774
+ GCC_except_table778
+ GCC_except_table782
+ GCC_except_table787
+ GCC_except_table789
+ GCC_except_table794
+ GCC_except_table795
+ GCC_except_table796
+ GCC_except_table815
+ GCC_except_table835
+ GCC_except_table836
+ GCC_except_table837
+ GCC_except_table842
+ GCC_except_table912
+ GCC_except_table918
+ GCC_except_table943
+ ___64-[BKDirectTouchState gestureCancelTouchesWithIdentifiers:count:]_block_invoke
+ ___70-[BKHIDDirectTouchEventProcessor gestureCancelTouchesWithIdentifiers:]_block_invoke
+ ___70-[BKHIDDirectTouchEventProcessor gestureCancelTouchesWithIdentifiers:]_block_invoke_2
+ ___block_descriptor_48_ea8_32s40s_e17_v16?0"NSArray"8l
- -[BKDirectTouchState _cancelContacts:destinationPredicate:preserveHitTestPolicy:excludingContextIDs:]
- GCC_except_table1030
- GCC_except_table1035
- GCC_except_table1038
- GCC_except_table1040
- GCC_except_table1041
- GCC_except_table473
- GCC_except_table474
- GCC_except_table475
- GCC_except_table480
- GCC_except_table481
- GCC_except_table489
- GCC_except_table491
- GCC_except_table562
- GCC_except_table606
- GCC_except_table634
- GCC_except_table650
- GCC_except_table651
- GCC_except_table655
- GCC_except_table682
- GCC_except_table733
- GCC_except_table734
- GCC_except_table735
- GCC_except_table741
- GCC_except_table749
- GCC_except_table750
- GCC_except_table760
- GCC_except_table765
- GCC_except_table766
- GCC_except_table771
- GCC_except_table780
- GCC_except_table784
- GCC_except_table785
- GCC_except_table790
- GCC_except_table792
- GCC_except_table811
- GCC_except_table825
- GCC_except_table826
- GCC_except_table827
- GCC_except_table828
- GCC_except_table908
- GCC_except_table914
- GCC_except_table939
CStrings:
+ "SystemGestureProcessor"
+ "gesture cancel touches with identifiers: %{public}@"
+ "too many touch identifiers passed to GestureCancelTouchesWithIdentifiers (%d)"
- "gesture cancelled contact for pathIndex:%d"
```
