## BackBoardHIDTouchEventProcessor

> `/System/Library/PrivateFrameworks/BackBoardHIDTouchEventProcessor.framework/Versions/A/BackBoardHIDTouchEventProcessor`

### Sections with Same Size but Changed Content

- `__TEXT.__constg_swiftt`
- `__TEXT.__swift5_typeref`
- `__TEXT.__swift5_types`
- `__TEXT.__swift5_protos`
- `__DATA_CONST.__objc_classlist`
- `__DATA_CONST.__objc_catlist`
- `__DATA_CONST.__objc_protolist`
- `__DATA_CONST.__objc_protorefs`
- `__DATA_CONST.__objc_superrefs`
- `__DATA_CONST.__objc_arraydata`
- `__DATA_CONST.__got`
- `__AUTH_CONST.__objc_intobj`
- `__AUTH_CONST.__objc_arrayobj`
- `__AUTH.__data`
- `__DATA.__data`

```diff

-868.0.0.0.0
-  __TEXT.__text: 0x3c180
-  __TEXT.__objc_methlist: 0x27b8
+873.200.0.0.0
+  __TEXT.__text: 0x3ceac
+  __TEXT.__objc_methlist: 0x27d0
   __TEXT.__const: 0x400
   __TEXT.__constg_swiftt: 0x124
   __TEXT.__swift5_typeref: 0x164

   __TEXT.__swift5_fieldmd: 0xfc
   __TEXT.__swift5_builtin: 0x28
   __TEXT.__swift5_capture: 0x20
-  __TEXT.__cstring: 0x1e1e
+  __TEXT.__cstring: 0x1e38
   __TEXT.__swift5_types: 0x14
   __TEXT.__swift5_protos: 0x4
-  __TEXT.__gcc_except_tab: 0x3cd0
-  __TEXT.__oslogstring: 0x2c0d
+  __TEXT.__gcc_except_tab: 0x3ea8
+  __TEXT.__oslogstring: 0x2c3d
   __TEXT.__ustring: 0xc
-  __TEXT.__unwind_info: 0x1308
+  __TEXT.__unwind_info: 0x1328
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0
   __TEXT.__objc_classname: 0x0
   __TEXT.__objc_methname: 0x0
   __TEXT.__objc_methtype: 0x0
-  __DATA_CONST.__const: 0x558
+  __DATA_CONST.__const: 0x538
   __DATA_CONST.__objc_classlist: 0x228
   __DATA_CONST.__objc_catlist: 0x8
   __DATA_CONST.__objc_protolist: 0x110
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x1ab0
+  __DATA_CONST.__objc_selrefs: 0x1ae0
   __DATA_CONST.__objc_protorefs: 0x38
   __DATA_CONST.__objc_superrefs: 0x168
   __DATA_CONST.__objc_arraydata: 0x10
   __DATA_CONST.__got: 0x560
-  __AUTH_CONST.__const: 0x18e0
-  __AUTH_CONST.__cfstring: 0x1fe0
-  __AUTH_CONST.__objc_const: 0x6ef8
+  __AUTH_CONST.__const: 0x1970
+  __AUTH_CONST.__cfstring: 0x2000
+  __AUTH_CONST.__objc_const: 0x6f20
   __AUTH_CONST.__objc_intobj: 0xd8
   __AUTH_CONST.__objc_arrayobj: 0x18
   __AUTH_CONST.__auth_got: 0x6b8
-  __AUTH.__objc_data: 0xa28
+  __AUTH.__objc_data: 0x9d8
   __AUTH.__data: 0xb8
-  __DATA.__objc_ivar: 0x548
+  __DATA.__objc_ivar: 0x54c
   __DATA.__data: 0xcc8
   __DATA.__bss: 0xf8
   __DATA.__common: 0x1
-  __DATA_DIRTY.__objc_data: 0xbe0
+  __DATA_DIRTY.__objc_data: 0xc30
   __DATA_DIRTY.__bss: 0x40
   - /System/Library/Frameworks/CoreFoundation.framework/Versions/A/CoreFoundation
   - /System/Library/Frameworks/CoreGraphics.framework/Versions/A/CoreGraphics

   - /usr/lib/swift/libswift_Builtin_float.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  Functions: 1118
-  Symbols:   3483
-  CStrings:  569
+  Functions: 1121
+  Symbols:   3498
+  CStrings:  571
 
Symbols:
+ -[BKDirectTouchState _cancelContacts:destinationPredicate:preserveHitTestPolicy:excludingContextIDs:]
+ -[BKDirectTouchState _removeContacts:fromDestinationPredicate:excludingContextIDs:]
+ -[BKHIDDirectTouchEventProcessor invalidate]
+ -[BKHIDDirectTouchEventProcessor setSessionID:]
+ GCC_except_table1030
+ GCC_except_table1039
+ GCC_except_table1041
+ GCC_except_table1043
+ GCC_except_table391
+ GCC_except_table395
+ GCC_except_table398
+ GCC_except_table409
+ GCC_except_table414
+ GCC_except_table418
+ GCC_except_table419
+ GCC_except_table420
+ GCC_except_table433
+ GCC_except_table434
+ GCC_except_table439
+ GCC_except_table444
+ GCC_except_table449
+ GCC_except_table456
+ GCC_except_table457
+ GCC_except_table461
+ GCC_except_table465
+ GCC_except_table466
+ GCC_except_table474
+ GCC_except_table480
+ GCC_except_table481
+ GCC_except_table489
+ GCC_except_table491
+ GCC_except_table493
+ GCC_except_table562
+ GCC_except_table606
+ GCC_except_table634
+ GCC_except_table658
+ GCC_except_table660
+ GCC_except_table662
+ GCC_except_table664
+ GCC_except_table682
+ GCC_except_table735
+ GCC_except_table743
+ GCC_except_table744
+ GCC_except_table751
+ GCC_except_table756
+ GCC_except_table760
+ GCC_except_table765
+ GCC_except_table771
+ GCC_except_table775
+ GCC_except_table779
+ GCC_except_table784
+ GCC_except_table786
+ GCC_except_table790
+ GCC_except_table791
+ GCC_except_table792
+ GCC_except_table811
+ GCC_except_table832
+ GCC_except_table833
+ GCC_except_table834
+ GCC_except_table838
+ GCC_except_table908
+ GCC_except_table914
+ GCC_except_table939
+ OBJC_IVAR_$_BKHIDDirectTouchEventProcessor._queue_invalidated
+ __83-[BKDirectTouchState _removeContacts:fromDestinationPredicate:excludingContextIDs:]_block_invoke
+ ___44-[BKHIDDirectTouchEventProcessor invalidate]_block_invoke
+ ___83-[BKDirectTouchState _removeContacts:fromDestinationPredicate:excludingContextIDs:]_block_invoke
+ ___block_descriptor_40_ea8_32w_e5_v8?0l
+ ___block_descriptor_40_ea8_32w_e8_v12?0I8l
+ ___block_descriptor_48_ea8_32s_e28_B16?0"BKTouchDestination"8l
+ ___block_descriptor_56_ea8_32s40s48w_e5_v8?0l
+ ___block_descriptor_64_ea8_32s40s48s_e35_v32?0q8"BKTouchDestination"16^B24l
+ ___copy_helper_block_ea8_32s40s48w
+ ___destroy_helper_block_ea8_32s40s48w
+ _objc_msgSend$contextIDsToAlwaysSendTouches
+ _objc_msgSend$removeDisappearanceObserver:
+ _objc_msgSend$restrictHitTestToTheseContextIDs
+ _objc_msgSend$setSessionID:
+ _objc_msgSend$shouldAvoidCancelingContinuingClients
+ _objc_msgSend$unregisterHandler:
- -[BKDirectTouchState _cancelContacts:destinationPredicate:preserveHitTestPolicy:]
- -[BKDirectTouchState _removeContacts:fromDestinationPredicate:]
- GCC_except_table1027
- GCC_except_table1032
- GCC_except_table1036
- GCC_except_table1037
- GCC_except_table394
- GCC_except_table397
- GCC_except_table401
- GCC_except_table403
- GCC_except_table407
- GCC_except_table415
- GCC_except_table417
- GCC_except_table425
- GCC_except_table427
- GCC_except_table436
- GCC_except_table438
- GCC_except_table443
- GCC_except_table445
- GCC_except_table450
- GCC_except_table458
- GCC_except_table462
- GCC_except_table463
- GCC_except_table470
- GCC_except_table471
- GCC_except_table472
- GCC_except_table486
- GCC_except_table488
- GCC_except_table559
- GCC_except_table603
- GCC_except_table631
- GCC_except_table647
- GCC_except_table648
- GCC_except_table652
- GCC_except_table661
- GCC_except_table679
- GCC_except_table730
- GCC_except_table731
- GCC_except_table732
- GCC_except_table738
- GCC_except_table747
- GCC_except_table757
- GCC_except_table762
- GCC_except_table763
- GCC_except_table768
- GCC_except_table777
- GCC_except_table781
- GCC_except_table782
- GCC_except_table787
- GCC_except_table789
- GCC_except_table808
- GCC_except_table822
- GCC_except_table823
- GCC_except_table824
- GCC_except_table835
- GCC_except_table905
- GCC_except_table911
- GCC_except_table936
- __63-[BKDirectTouchState _removeContacts:fromDestinationPredicate:]_block_invoke
- ___63-[BKDirectTouchState _removeContacts:fromDestinationPredicate:]_block_invoke
- ___block_descriptor_40_e28_B16?0"BKTouchDestination"8l
- ___block_descriptor_48_ea8_32s40w_e8_v12?0I8l
- ___block_descriptor_56_ea8_32s40s_e35_v32?0q8"BKTouchDestination"16^B24l
- ___copy_helper_block_ea8_32s40w
- ___destroy_helper_block_ea8_32s40w
CStrings:
+ "processor invalidated"
+ "touch processor deallocated without -invalidate"
```
