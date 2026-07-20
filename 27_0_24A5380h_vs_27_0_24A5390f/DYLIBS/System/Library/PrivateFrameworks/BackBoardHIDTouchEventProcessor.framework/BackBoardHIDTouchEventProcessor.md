## BackBoardHIDTouchEventProcessor

> `/System/Library/PrivateFrameworks/BackBoardHIDTouchEventProcessor.framework/BackBoardHIDTouchEventProcessor`

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
- `__AUTH_CONST.__const`
- `__AUTH_CONST.__objc_intobj`
- `__AUTH_CONST.__objc_arrayobj`
- `__AUTH.__data`
- `__DATA.__data`

```diff

-868.0.0.0.0
-  __TEXT.__text: 0x5a880
-  __TEXT.__objc_methlist: 0x39f0
+873.100.0.0.0
+  __TEXT.__text: 0x5b868
+  __TEXT.__objc_methlist: 0x3a08
   __TEXT.__const: 0x480
   __TEXT.__constg_swiftt: 0x124
   __TEXT.__swift5_typeref: 0x164

   __TEXT.__swift5_fieldmd: 0xf0
   __TEXT.__swift5_builtin: 0x28
   __TEXT.__swift5_capture: 0x20
-  __TEXT.__cstring: 0x34b3
+  __TEXT.__cstring: 0x34fd
   __TEXT.__swift5_types: 0x14
   __TEXT.__swift5_protos: 0x4
-  __TEXT.__gcc_except_tab: 0x5420
-  __TEXT.__oslogstring: 0x471e
+  __TEXT.__gcc_except_tab: 0x562c
+  __TEXT.__oslogstring: 0x47a1
   __TEXT.__ustring: 0xc
-  __TEXT.__unwind_info: 0x1b10
+  __TEXT.__unwind_info: 0x1b38
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0
   __TEXT.__objc_classname: 0x0
   __TEXT.__objc_methname: 0x0
   __TEXT.__objc_methtype: 0x0
-  __DATA_CONST.__const: 0x1c00
+  __DATA_CONST.__const: 0x1c30
   __DATA_CONST.__objc_classlist: 0x2f8
   __DATA_CONST.__objc_catlist: 0x8
   __DATA_CONST.__objc_protolist: 0x158
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x26d8
+  __DATA_CONST.__objc_selrefs: 0x2708
   __DATA_CONST.__objc_protorefs: 0x40
   __DATA_CONST.__objc_superrefs: 0x218
   __DATA_CONST.__objc_arraydata: 0x10
   __DATA_CONST.__got: 0x780
   __AUTH_CONST.__const: 0x860
-  __AUTH_CONST.__cfstring: 0x3e60
-  __AUTH_CONST.__objc_const: 0xa978
+  __AUTH_CONST.__cfstring: 0x3ea0
+  __AUTH_CONST.__objc_const: 0xa9c0
   __AUTH_CONST.__objc_intobj: 0x1f8
   __AUTH_CONST.__objc_arrayobj: 0x18
-  __AUTH_CONST.__auth_got: 0x9a0
-  __AUTH.__objc_data: 0xe38
+  __AUTH_CONST.__auth_got: 0x9b8
+  __AUTH.__objc_data: 0xc58
   __AUTH.__data: 0xb8
-  __DATA.__objc_ivar: 0x944
+  __DATA.__objc_ivar: 0x94c
   __DATA.__data: 0x1028
   __DATA.__bss: 0x100
   __DATA.__common: 0x1
-  __DATA_DIRTY.__objc_data: 0xff0
+  __DATA_DIRTY.__objc_data: 0x11d0
   __DATA_DIRTY.__bss: 0x50
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/CoreGraphics.framework/CoreGraphics

   - /usr/lib/swift/libswiftXPC.dylib
   - /usr/lib/swift/libswift_Builtin_float.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  Functions: 1592
-  Symbols:   5016
-  CStrings:  980
+  Functions: 1596
+  Symbols:   5036
+  CStrings:  983
 
Symbols:
+ -[BKDirectTouchState _cancelContacts:destinationPredicate:preserveHitTestPolicy:excludingContextIDs:]
+ -[BKDirectTouchState _removeContacts:fromDestinationPredicate:excludingContextIDs:]
+ -[BKHIDDirectTouchEventProcessor invalidate]
+ -[BKHIDDirectTouchEventProcessor setSessionID:]
+ -[BKMousePointerController _locked_interfaceOrientationForBuiltRegionWithDisplayUUID:]
+ GCC_except_table1061
+ GCC_except_table1067
+ GCC_except_table1091
+ GCC_except_table1093
+ GCC_except_table1119
+ GCC_except_table1127
+ GCC_except_table1128
+ GCC_except_table1130
+ GCC_except_table1135
+ GCC_except_table1138
+ GCC_except_table1140
+ GCC_except_table1143
+ GCC_except_table1149
+ GCC_except_table1155
+ GCC_except_table1160
+ GCC_except_table1161
+ GCC_except_table1166
+ GCC_except_table1168
+ GCC_except_table1173
+ GCC_except_table1174
+ GCC_except_table1175
+ GCC_except_table1194
+ GCC_except_table1262
+ GCC_except_table1263
+ GCC_except_table1264
+ GCC_except_table1269
+ GCC_except_table1343
+ GCC_except_table1368
+ GCC_except_table1387
+ GCC_except_table1388
+ GCC_except_table1463
+ GCC_except_table147
+ GCC_except_table1471
+ GCC_except_table1473
+ GCC_except_table1474
+ GCC_except_table1476
+ GCC_except_table1492
+ GCC_except_table153
+ GCC_except_table168
+ GCC_except_table175
+ GCC_except_table192
+ GCC_except_table197
+ GCC_except_table217
+ GCC_except_table223
+ GCC_except_table227
+ GCC_except_table243
+ GCC_except_table344
+ GCC_except_table385
+ GCC_except_table395
+ GCC_except_table402
+ GCC_except_table412
+ GCC_except_table414
+ GCC_except_table421
+ GCC_except_table423
+ GCC_except_table429
+ GCC_except_table431
+ GCC_except_table441
+ GCC_except_table443
+ GCC_except_table446
+ GCC_except_table519
+ GCC_except_table522
+ GCC_except_table530
+ GCC_except_table538
+ GCC_except_table545
+ GCC_except_table555
+ GCC_except_table557
+ GCC_except_table568
+ GCC_except_table570
+ GCC_except_table579
+ GCC_except_table581
+ GCC_except_table634
+ GCC_except_table649
+ GCC_except_table652
+ GCC_except_table655
+ GCC_except_table662
+ GCC_except_table673
+ GCC_except_table677
+ GCC_except_table681
+ GCC_except_table683
+ GCC_except_table686
+ GCC_except_table687
+ GCC_except_table691
+ GCC_except_table701
+ GCC_except_table704
+ GCC_except_table710
+ GCC_except_table711
+ GCC_except_table718
+ GCC_except_table719
+ GCC_except_table724
+ GCC_except_table727
+ GCC_except_table728
+ GCC_except_table733
+ GCC_except_table738
+ GCC_except_table743
+ GCC_except_table746
+ GCC_except_table747
+ GCC_except_table751
+ GCC_except_table755
+ GCC_except_table756
+ GCC_except_table769
+ GCC_except_table772
+ GCC_except_table774
+ GCC_except_table780
+ GCC_except_table781
+ GCC_except_table783
+ GCC_except_table852
+ GCC_except_table905
+ GCC_except_table932
+ GCC_except_table953
+ GCC_except_table955
+ GCC_except_table958
+ GCC_except_table960
+ GCC_except_table978
+ _BKLogEventDelivery
+ _BSInterfaceOrientationDescription
+ _OBJC_IVAR_$_BKHIDDirectTouchEventProcessor._queue_invalidated
+ _OBJC_IVAR_$_BKMousePointerController._interfaceOrientationByDisplayUUID
+ ___44-[BKHIDDirectTouchEventProcessor invalidate]_block_invoke
+ ___83-[BKDirectTouchState _removeContacts:fromDestinationPredicate:excludingContextIDs:]_block_invoke
+ ___83-[BKDirectTouchState _removeContacts:fromDestinationPredicate:excludingContextIDs:]_block_invoke_2
+ ___block_descriptor_40_ea8_32w_e5_v8?0lw32l8
+ ___block_descriptor_40_ea8_32w_e8_v12?0I8lw32l8
+ ___block_descriptor_48_ea8_32s_e28_B16?0"BKTouchDestination"8ls32l8
+ ___block_descriptor_56_ea8_32s40s48w_e5_v8?0lw48l8s32l8s40l8
+ ___block_descriptor_64_ea8_32s40s48s_e35_v32?0q8"BKTouchDestination"16^B24ls32l8s40l8s48l8
+ ___block_descriptor_72_e8_32s40s48s56s64r_e36_v32?0"NSString"8"CADisplay"16^B24ls32l8s40l8s48l8r64l8s56l8
+ _objc_msgSend$contextIDsToAlwaysSendTouches
+ _objc_msgSend$removeDisappearanceObserver:
+ _objc_msgSend$restrictHitTestToTheseContextIDs
+ _objc_msgSend$setClientConnectionIdentifier:
+ _objc_msgSend$setSessionID:
+ _objc_msgSend$shouldAvoidCancelingContinuingClients
+ _objc_msgSend$unregisterHandler:
+ _objc_retain_x10
- -[BKDirectTouchState _cancelContacts:destinationPredicate:preserveHitTestPolicy:]
- -[BKDirectTouchState _removeContacts:fromDestinationPredicate:]
- GCC_except_table1057
- GCC_except_table1063
- GCC_except_table1087
- GCC_except_table1089
- GCC_except_table1114
- GCC_except_table1115
- GCC_except_table1116
- GCC_except_table1117
- GCC_except_table1123
- GCC_except_table1131
- GCC_except_table1132
- GCC_except_table1139
- GCC_except_table1142
- GCC_except_table1147
- GCC_except_table1148
- GCC_except_table1153
- GCC_except_table1159
- GCC_except_table1164
- GCC_except_table1165
- GCC_except_table1170
- GCC_except_table1190
- GCC_except_table1252
- GCC_except_table1253
- GCC_except_table1254
- GCC_except_table1255
- GCC_except_table1335
- GCC_except_table1364
- GCC_except_table1383
- GCC_except_table1384
- GCC_except_table145
- GCC_except_table1459
- GCC_except_table1464
- GCC_except_table1467
- GCC_except_table1469
- GCC_except_table1470
- GCC_except_table1488
- GCC_except_table152
- GCC_except_table166
- GCC_except_table174
- GCC_except_table191
- GCC_except_table196
- GCC_except_table216
- GCC_except_table222
- GCC_except_table226
- GCC_except_table242
- GCC_except_table343
- GCC_except_table384
- GCC_except_table386
- GCC_except_table396
- GCC_except_table404
- GCC_except_table413
- GCC_except_table419
- GCC_except_table422
- GCC_except_table427
- GCC_except_table430
- GCC_except_table440
- GCC_except_table442
- GCC_except_table444
- GCC_except_table515
- GCC_except_table521
- GCC_except_table525
- GCC_except_table531
- GCC_except_table539
- GCC_except_table553
- GCC_except_table556
- GCC_except_table567
- GCC_except_table569
- GCC_except_table574
- GCC_except_table580
- GCC_except_table632
- GCC_except_table640
- GCC_except_table650
- GCC_except_table654
- GCC_except_table661
- GCC_except_table663
- GCC_except_table675
- GCC_except_table678
- GCC_except_table682
- GCC_except_table685
- GCC_except_table689
- GCC_except_table692
- GCC_except_table695
- GCC_except_table703
- GCC_except_table708
- GCC_except_table716
- GCC_except_table717
- GCC_except_table720
- GCC_except_table723
- GCC_except_table726
- GCC_except_table729
- GCC_except_table732
- GCC_except_table737
- GCC_except_table742
- GCC_except_table745
- GCC_except_table749
- GCC_except_table753
- GCC_except_table754
- GCC_except_table761
- GCC_except_table762
- GCC_except_table773
- GCC_except_table775
- GCC_except_table776
- GCC_except_table848
- GCC_except_table901
- GCC_except_table928
- GCC_except_table942
- GCC_except_table943
- GCC_except_table945
- GCC_except_table948
- GCC_except_table974
- ___63-[BKDirectTouchState _removeContacts:fromDestinationPredicate:]_block_invoke
- ___63-[BKDirectTouchState _removeContacts:fromDestinationPredicate:]_block_invoke_2
- ___block_descriptor_40_e28_B16?0"BKTouchDestination"8l
- ___block_descriptor_40_e8_32w_e5_v8?0lw32l8
- ___block_descriptor_48_ea8_32s40w_e8_v12?0I8lw40l8s32l8
- ___block_descriptor_56_ea8_32s40s_e35_v32?0q8"BKTouchDestination"16^B24ls32l8s40l8
- ___block_descriptor_64_e8_32s40s48s56r_e36_v32?0"NSString"8"CADisplay"16^B24ls32l8s40l8r56l8s48l8
CStrings:
+ "can't dispatch event %{public}@ to target %{public}@: invalid client connection identifier / task name 0x%X"
+ "processor invalidated"
+ "region build: display:%{public}@ orientation:%{public}@ transformedBounds:%{public}@"
+ "touch processor deallocated without -invalidate"
- "can't dispatch pointer event to invalid client task name 0x%X"
```
