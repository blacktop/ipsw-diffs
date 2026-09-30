## KeychainCircle

> `/System/Library/PrivateFrameworks/KeychainCircle.framework/KeychainCircle`

```diff

-61901.80.25.0.0
-  __TEXT.__text: 0x28c84
-  __TEXT.__auth_stubs: 0x1050
+61901.100.267.0.2
+  __TEXT.__text: 0x2a43c
+  __TEXT.__auth_stubs: 0xfe0
   __TEXT.__delay_helper: 0x1bc
-  __TEXT.__objc_methlist: 0x1ddc
+  __TEXT.__objc_methlist: 0x1e24
   __TEXT.__const: 0xd8
   __TEXT.__dlopen_cstrs: 0xae
-  __TEXT.__gcc_except_tab: 0x1640
+  __TEXT.__gcc_except_tab: 0x1618
   __TEXT.__cstring: 0x330e
-  __TEXT.__oslogstring: 0x397e
+  __TEXT.__oslogstring: 0x3a20
   __TEXT.__ustring: 0x32
-  __TEXT.__unwind_info: 0x810
+  __TEXT.__unwind_info: 0x928
   __TEXT.__objc_classname: 0x2e6
-  __TEXT.__objc_methname: 0x4219
+  __TEXT.__objc_methname: 0x4281
   __TEXT.__objc_methtype: 0xf65
-  __TEXT.__objc_stubs: 0x3040
+  __TEXT.__objc_stubs: 0x3080
   __DATA_CONST.__got: 0x2f8
   __DATA_CONST.__const: 0x11c0
   __DATA_CONST.__objc_classlist: 0xa8
   __DATA_CONST.__objc_catlist: 0x20
   __DATA_CONST.__objc_protolist: 0x38
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x1058
+  __DATA_CONST.__objc_selrefs: 0x1070
   __DATA_CONST.__objc_protorefs: 0x8
   __DATA_CONST.__objc_superrefs: 0x88
-  __AUTH_CONST.__auth_got: 0x838
+  __AUTH_CONST.__auth_got: 0x800
   __AUTH_CONST.__const: 0x1e0
   __AUTH_CONST.__cfstring: 0x3720
-  __AUTH_CONST.__objc_const: 0x2bb0
+  __AUTH_CONST.__objc_const: 0x2c10
   __AUTH_CONST.__objc_intobj: 0x60
   __AUTH.__objc_data: 0x5a0
-  __DATA.__objc_ivar: 0x20c
+  __DATA.__objc_ivar: 0x214
   __DATA.__data: 0x320
   __DATA.__bss: 0x140
   __DATA_DIRTY.__objc_data: 0xf0

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libcompression.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 0C7DB031-C966-3A9A-A175-32537DB3D7C4
-  Functions: 772
-  Symbols:   2957
-  CStrings:  2117
+  UUID: FEBC8EBF-FE49-3C83-84AD-076DF5DB1F4E
+  Functions: 778
+  Symbols:   2966
+  CStrings:  2123
 
Symbols:
+ -[KCJoiningAcceptSession failSOSForTests]
+ -[KCJoiningAcceptSession setFailSOSForTests:]
+ -[KCJoiningAcceptSession setFailSOSPropertyForTests:]
+ -[KCJoiningRequestCircleSession failSOSForTests]
+ -[KCJoiningRequestCircleSession setFailSOSForTests:]
+ -[KCJoiningRequestCircleSession setFailSOSPropertyForTests:]
+ GCC_except_table383
+ GCC_except_table391
+ GCC_except_table529
+ GCC_except_table539
+ GCC_except_table541
+ _OBJC_IVAR_$_KCJoiningAcceptSession._failSOSForTests
+ _OBJC_IVAR_$_KCJoiningRequestCircleSession._failSOSForTests
+ ___Block_byref_object_copy_.387
+ ___Block_byref_object_copy_.936
+ ___Block_byref_object_dispose_.388
+ ___Block_byref_object_dispose_.937
+ ___block_descriptor_tmp.1503
+ ___block_descriptor_tmp.1567
+ ___block_descriptor_tmp.1609
+ ___block_descriptor_tmp.1642
+ ___block_descriptor_tmp.71.1561
+ ___block_literal_global.1162
+ ___block_literal_global.1466
+ ___block_literal_global.1531
+ ___block_literal_global.1607
+ ___block_literal_global.429
+ _apply_block_1.1510
+ _apply_block_2.1541
+ _objc_msgSend$failSOSForTests
+ _objc_msgSend$setFailSOSForTests:
- GCC_except_table381
- GCC_except_table389
- GCC_except_table523
- GCC_except_table533
- GCC_except_table535
- ___Block_byref_object_copy_.377
- ___Block_byref_object_copy_.917
- ___Block_byref_object_dispose_.378
- ___Block_byref_object_dispose_.918
- ___block_descriptor_tmp.1484
- ___block_descriptor_tmp.1548
- ___block_descriptor_tmp.1590
- ___block_descriptor_tmp.1623
- ___block_descriptor_tmp.71.1542
- ___block_literal_global.1143
- ___block_literal_global.1447
- ___block_literal_global.1512
- ___block_literal_global.1588
- ___block_literal_global.419
- _apply_block_1.1491
- _apply_block_2.1522
- _objc_claimAutoreleasedReturnValue
- _objc_retainAutoreleaseReturnValue
- _objc_retain_x1
- _objc_retain_x3
- _objc_retain_x4
- _objc_retain_x5
- _objc_retain_x6
CStrings:
+ "2"
+ "TB,N,V_failSOSForTests"
+ "\\"
+ "_failSOSForTests"
+ "decryptAndVerify failed: %@, but continuing for Octagon"
+ "failSOSForTests"
+ "joining: failed to create encrypted peer info, %@, but continuing for Octagon"
+ "joining: failed to process SOS application: %@, but continuing for Octagon"
+ "joining: processCircleJoinData failed %@, but continuing for Octagon"
+ "setFailSOSForTests:"
+ "setFailSOSPropertyForTests:"
- "\""
- "L"
- "decryptAndVerify failed: %@"
- "joining: failed to process SOS application: %@"
- "joining: processCircleJoinData failed %@"

```
