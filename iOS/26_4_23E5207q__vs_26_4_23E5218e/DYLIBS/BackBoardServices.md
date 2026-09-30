## BackBoardServices

> `/System/Library/PrivateFrameworks/BackBoardServices.framework/BackBoardServices`

```diff

-735.4.6.0.0
-  __TEXT.__text: 0x8575c
+735.4.7.0.0
+  __TEXT.__text: 0x85b48
   __TEXT.__auth_stubs: 0xd90
-  __TEXT.__objc_methlist: 0x7bbc
-  __TEXT.__const: 0x434
+  __TEXT.__objc_methlist: 0x7c04
+  __TEXT.__const: 0x44c
   __TEXT.__dlopen_cstrs: 0x18e
   __TEXT.__gcc_except_tab: 0x41c
-  __TEXT.__cstring: 0xb02c
+  __TEXT.__cstring: 0xb0bf
   __TEXT.__oslogstring: 0x20a9
   __TEXT.__ustring: 0x14
-  __TEXT.__unwind_info: 0x1ff8
+  __TEXT.__unwind_info: 0x2000
   __TEXT.__objc_classname: 0x1af9
-  __TEXT.__objc_methname: 0xd03a
+  __TEXT.__objc_methname: 0xd0f7
   __TEXT.__objc_methtype: 0x1fd7
   __TEXT.__objc_stubs: 0x6a80
   __DATA_CONST.__got: 0x768
-  __DATA_CONST.__const: 0x1758
+  __DATA_CONST.__const: 0x1770
   __DATA_CONST.__objc_classlist: 0x570
   __DATA_CONST.__objc_protolist: 0x168
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x2b00
+  __DATA_CONST.__objc_selrefs: 0x2b20
   __DATA_CONST.__objc_protorefs: 0xc0
   __DATA_CONST.__objc_superrefs: 0x3b8
   __DATA_CONST.__objc_arraydata: 0x70
   __AUTH_CONST.__auth_got: 0x6d8
   __AUTH_CONST.__const: 0x1428
-  __AUTH_CONST.__cfstring: 0x97e0
-  __AUTH_CONST.__objc_const: 0x102b8
+  __AUTH_CONST.__cfstring: 0x9860
+  __AUTH_CONST.__objc_const: 0x10378
   __AUTH_CONST.__objc_intobj: 0x180
   __AUTH_CONST.__objc_dictobj: 0x78
   __AUTH_CONST.__objc_arrayobj: 0x30
   __AUTH_CONST.__objc_floatobj: 0x10
   __AUTH.__objc_data: 0x23a0
-  __DATA.__objc_ivar: 0x7b0
+  __DATA.__objc_ivar: 0x7bc
   __DATA.__data: 0x10f0
   __DATA.__bss: 0x548
   __DATA_DIRTY.__objc_data: 0x12c0

   - /usr/lib/libMobileGestalt.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 39EE03D6-1D75-3534-8A1E-D487610A896E
-  Functions: 3120
-  Symbols:   9729
-  CStrings:  5700
+  UUID: 1F21D918-D1F8-330A-A0E7-5D637E98F61D
+  Functions: 3127
+  Symbols:   9745
+  CStrings:  5719
 
Symbols:
+ -[BKSHIDEventAuthenticationMessage touchIdentifier]
+ -[BKSMutableHIDEventAuthenticationMessage setTouchIdentifier:]
+ -[BKSMutableTouchAuthenticationSpecification setFinalSampleEvent:]
+ -[BKSMutableTouchAuthenticationSpecification setLongPressTimeout:]
+ -[BKSTouchAuthenticationSpecification finalSampleEvent]
+ -[BKSTouchAuthenticationSpecification longPressTimeout]
+ GCC_except_table1527
+ GCC_except_table1643
+ GCC_except_table1771
+ GCC_except_table1894
+ GCC_except_table1903
+ GCC_except_table2036
+ GCC_except_table2146
+ GCC_except_table2148
+ GCC_except_table2178
+ GCC_except_table2357
+ GCC_except_table2530
+ GCC_except_table2795
+ GCC_except_table2810
+ GCC_except_table2970
+ OBJC_IVAR_$_BKSHIDEventAuthenticationMessage._touchIdentifier
+ OBJC_IVAR_$_BKSTouchAuthenticationSpecification._finalSampleEvent
+ OBJC_IVAR_$_BKSTouchAuthenticationSpecification._longPressTimeout
+ _NSStringFromBKSTouchAuthenticationFinalSampleEvent
+ _QuartzCoreLibrary.11926
+ _QuartzCoreLibraryCore.frameworkLibrary.11941
+ _QuartzCoreLibraryCore.frameworkLibrary.8180
+ _QuartzCoreLibraryCore.frameworkLibrary.8993
+ ___Block_byref_object_copy_.9985
+ ___Block_byref_object_dispose_.9986
+ ___QuartzCoreLibraryCore_block_invoke.11942
+ ___QuartzCoreLibraryCore_block_invoke.8181
+ ___QuartzCoreLibraryCore_block_invoke.8994
+ ___block_literal_global.10047
+ ___block_literal_global.10228
+ ___block_literal_global.10469
+ ___block_literal_global.10719
+ ___block_literal_global.11530
+ ___block_literal_global.11712
+ ___block_literal_global.11917
+ ___block_literal_global.12010
+ ___block_literal_global.12139
+ ___block_literal_global.12654
+ ___block_literal_global.12886
+ ___block_literal_global.13171
+ ___block_literal_global.13271
+ ___block_literal_global.13376
+ ___block_literal_global.13509
+ ___block_literal_global.13793
+ ___block_literal_global.14009
+ ___block_literal_global.14598
+ ___block_literal_global.16.8097
+ ___block_literal_global.18.9177
+ ___block_literal_global.2.12883
+ ___block_literal_global.22.10209
+ ___block_literal_global.25.8106
+ ___block_literal_global.3.14012
+ ___block_literal_global.31.8112
+ ___block_literal_global.5756
+ ___block_literal_global.6052
+ ___block_literal_global.6293
+ ___block_literal_global.6438
+ ___block_literal_global.6777
+ ___block_literal_global.6791
+ ___block_literal_global.75.10013
+ ___block_literal_global.7752
+ ___block_literal_global.7930
+ ___block_literal_global.7932
+ ___block_literal_global.8013
+ ___block_literal_global.8086
+ ___block_literal_global.8418
+ ___block_literal_global.8721
+ ___block_literal_global.9190
+ ___block_literal_global.9386
+ ___block_literal_global.9722
+ ___block_literal_global.9862
+ ___getCADisplayClass_block_invoke.8992
+ _audit_stringQuartzCore.11945
+ _audit_stringQuartzCore.8196
+ _audit_stringQuartzCore.9009
+ _getCADisplayClass.8990
+ _getCADisplayClass.softClass.8991
+ _protobufSchema.onceToken.13162
+ _protobufSchema.onceToken.13507
+ _protobufSchema.onceToken.13790
+ _protobufSchema.onceToken.6291
+ _protobufSchema.onceToken.6436
+ _protobufSchema.onceToken.8415
+ _protobufSchema.onceToken.9383
+ _protobufSchema.onceToken.9859
+ _protobufSchema.schema.13163
+ _protobufSchema.schema.13508
+ _protobufSchema.schema.13791
+ _protobufSchema.schema.6292
+ _protobufSchema.schema.6437
+ _protobufSchema.schema.8416
+ _protobufSchema.schema.9384
+ _protobufSchema.schema.9860
+ _sharedInstance.__shared.13272
+ _sharedInstance.__sharedInstance.11562
+ _sharedInstance.controller.6792
+ _sharedInstance.onceToken.10046
+ _sharedInstance.onceToken.11561
+ _sharedInstance.onceToken.13270
+ _sharedInstance.onceToken.13642
+ _sharedInstance.onceToken.6776
+ _sharedInstance.onceToken.6790
+ _sharedInstance.onceToken.7929
+ _sharedInstance.service.13643
- GCC_except_table1522
- GCC_except_table1638
- GCC_except_table1766
- GCC_except_table1889
- GCC_except_table1898
- GCC_except_table2031
- GCC_except_table2139
- GCC_except_table2141
- GCC_except_table2171
- GCC_except_table2350
- GCC_except_table2516
- GCC_except_table2788
- GCC_except_table2803
- GCC_except_table2963
- _QuartzCoreLibrary.11890
- _QuartzCoreLibraryCore.frameworkLibrary.11905
- _QuartzCoreLibraryCore.frameworkLibrary.8152
- _QuartzCoreLibraryCore.frameworkLibrary.8961
- ___Block_byref_object_copy_.9945
- ___Block_byref_object_dispose_.9946
- ___QuartzCoreLibraryCore_block_invoke.11906
- ___QuartzCoreLibraryCore_block_invoke.8153
- ___QuartzCoreLibraryCore_block_invoke.8962
- ___block_literal_global.10007
- ___block_literal_global.10188
- ___block_literal_global.10428
- ___block_literal_global.10680
- ___block_literal_global.11494
- ___block_literal_global.11675
- ___block_literal_global.11881
- ___block_literal_global.11974
- ___block_literal_global.12103
- ___block_literal_global.12618
- ___block_literal_global.12851
- ___block_literal_global.13130
- ___block_literal_global.13231
- ___block_literal_global.13336
- ___block_literal_global.13469
- ___block_literal_global.13753
- ___block_literal_global.13969
- ___block_literal_global.14558
- ___block_literal_global.16.8069
- ___block_literal_global.18.9144
- ___block_literal_global.2.12848
- ___block_literal_global.22.10169
- ___block_literal_global.25.8078
- ___block_literal_global.3.13972
- ___block_literal_global.31.8084
- ___block_literal_global.5727
- ___block_literal_global.6024
- ___block_literal_global.6264
- ___block_literal_global.6409
- ___block_literal_global.6748
- ___block_literal_global.6762
- ___block_literal_global.75.9973
- ___block_literal_global.7724
- ___block_literal_global.7902
- ___block_literal_global.7904
- ___block_literal_global.7985
- ___block_literal_global.8058
- ___block_literal_global.8390
- ___block_literal_global.8690
- ___block_literal_global.9157
- ___block_literal_global.9352
- ___block_literal_global.9682
- ___block_literal_global.9822
- ___getCADisplayClass_block_invoke.8960
- _audit_stringQuartzCore.11909
- _audit_stringQuartzCore.8168
- _audit_stringQuartzCore.8977
- _getCADisplayClass.8958
- _getCADisplayClass.softClass.8959
- _protobufSchema.onceToken.13121
- _protobufSchema.onceToken.13467
- _protobufSchema.onceToken.13750
- _protobufSchema.onceToken.6262
- _protobufSchema.onceToken.6407
- _protobufSchema.onceToken.8387
- _protobufSchema.onceToken.9349
- _protobufSchema.onceToken.9819
- _protobufSchema.schema.13122
- _protobufSchema.schema.13468
- _protobufSchema.schema.13751
- _protobufSchema.schema.6263
- _protobufSchema.schema.6408
- _protobufSchema.schema.8388
- _protobufSchema.schema.9350
- _protobufSchema.schema.9820
- _sharedInstance.__shared.13232
- _sharedInstance.__sharedInstance.11525
- _sharedInstance.controller.6763
- _sharedInstance.onceToken.10006
- _sharedInstance.onceToken.11524
- _sharedInstance.onceToken.13230
- _sharedInstance.onceToken.13602
- _sharedInstance.onceToken.6747
- _sharedInstance.onceToken.6761
- _sharedInstance.onceToken.7901
- _sharedInstance.service.13603
CStrings:
+ "TI,R,N,V_touchIdentifier"
+ "Td,R,N,V_longPressTimeout"
+ "Tq,R,N,V_finalSampleEvent"
+ "_finalSampleEvent"
+ "_longPressTimeout"
+ "finalSampleEvent"
+ "finalSampleEvent > BKSTouchAuthenticationFinalSampleEventUnspecified"
+ "longPressTimeout"
+ "setFinalSampleEvent:"
+ "setLongPressTimeout:"
+ "touchUp"

```
