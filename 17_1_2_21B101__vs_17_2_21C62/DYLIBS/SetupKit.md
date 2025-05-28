## SetupKit

> `/System/Library/PrivateFrameworks/SetupKit.framework/SetupKit`

```diff

-730.4.0.0.0
-  __TEXT.__text: 0x26410
+730.8.3.0.0
+  __TEXT.__text: 0x27440
   __TEXT.__auth_stubs: 0x770
-  __TEXT.__objc_methlist: 0x1c84
+  __TEXT.__objc_methlist: 0x1d6c
   __TEXT.__const: 0x180
   __TEXT.__gcc_except_tab: 0xd50
-  __TEXT.__cstring: 0x70c2
-  __TEXT.__unwind_info: 0x968
-  __TEXT.__objc_classname: 0x3ad
+  __TEXT.__cstring: 0x72cc
+  __TEXT.__unwind_info: 0x9b0
+  __TEXT.__objc_classname: 0x3d9
   __TEXT.__objc_methname: 0x362a
   __TEXT.__objc_methtype: 0xb27
   __TEXT.__objc_stubs: 0x2b80
   __DATA_CONST.__got: 0x70
   __DATA_CONST.__const: 0xec8
-  __DATA_CONST.__objc_classlist: 0x100
+  __DATA_CONST.__objc_classlist: 0x110
   __DATA_CONST.__objc_protolist: 0x48
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_const: 0x45a0
+  __DATA_CONST.__objc_const: 0x4698
   __DATA_CONST.__objc_selrefs: 0xcf0
   __DATA_CONST.__objc_arraydata: 0x30
   __AUTH_CONST.__cfstring: 0xac0
-  __AUTH_CONST.__const: 0x680
-  __AUTH_CONST.__objc_const: 0x948
+  __AUTH_CONST.__const: 0x6e0
+  __AUTH_CONST.__objc_const: 0x9d8
   __AUTH_CONST.__objc_intobj: 0x168
   __AUTH_CONST.__objc_arrayobj: 0x90
   __AUTH_CONST.__auth_got: 0x3c8
-  __AUTH.__objc_data: 0xa00
+  __AUTH.__objc_data: 0xaa0
   __DATA.__objc_classrefs: 0x1c0
-  __DATA.__objc_superrefs: 0xa0
-  __DATA.__objc_ivar: 0x440
-  __DATA.__data: 0xbb0
+  __DATA.__objc_superrefs: 0xb0
+  __DATA.__objc_ivar: 0x44c
+  __DATA.__data: 0xc90
   __DATA.__bss: 0x10
   - /System/Library/Frameworks/CoreBluetooth.framework/CoreBluetooth
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation

   - /System/Library/PrivateFrameworks/NetworkRelay.framework/NetworkRelay
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 877
-  Symbols:   2971
-  CStrings:  1703
+  Functions: 904
+  Symbols:   3042
+  CStrings:  1716
 
Symbols:
+ -[SKSetupOSUpdateClient _activate]
+ -[SKSetupOSUpdateClient _prepareSteps]
+ -[SKSetupOSUpdateClient _run]
+ -[SKSetupOSUpdateClient init]
+ -[SKSetupOSUpdateServer .cxx_destruct]
+ -[SKSetupOSUpdateServer _activate]
+ -[SKSetupOSUpdateServer _bleAdvertiserEnsureStarted]
+ -[SKSetupOSUpdateServer _bleAdvertiserEnsureStopped]
+ -[SKSetupOSUpdateServer _bleAdvertiserShouldRun]
+ -[SKSetupOSUpdateServer _bleServerAcceptConnecton:]
+ -[SKSetupOSUpdateServer _bleServerEnsureStarted]
+ -[SKSetupOSUpdateServer _bleServerEnsureStopped]
+ -[SKSetupOSUpdateServer _invalidate]
+ -[SKSetupOSUpdateServer _oobEnsureStarted]
+ -[SKSetupOSUpdateServer _prepareSteps]
+ -[SKSetupOSUpdateServer _run]
+ -[SKSetupOSUpdateServer descriptionWithLevel:]
+ -[SKSetupOSUpdateServer init]
+ GCC_except_table124
+ GCC_except_table148
+ GCC_except_table150
+ GCC_except_table156
+ GCC_except_table162
+ GCC_except_table167
+ GCC_except_table180
+ GCC_except_table188
+ GCC_except_table217
+ GCC_except_table371
+ GCC_except_table441
+ GCC_except_table483
+ GCC_except_table489
+ GCC_except_table493
+ GCC_except_table537
+ GCC_except_table544
+ GCC_except_table555
+ GCC_except_table562
+ GCC_except_table629
+ GCC_except_table636
+ GCC_except_table643
+ GCC_except_table646
+ GCC_except_table751
+ GCC_except_table819
+ GCC_except_table852
+ GCC_except_table858
+ GCC_except_table862
+ _OBJC_CLASS_$_SKSetupOSUpdateClient
+ _OBJC_CLASS_$_SKSetupOSUpdateServer
+ _OBJC_IVAR_$_SKSetupOSUpdateServer._bleAdvertiser
+ _OBJC_IVAR_$_SKSetupOSUpdateServer._bleServer
+ _OBJC_IVAR_$_SKSetupOSUpdateServer._completed
+ _OBJC_METACLASS_$_SKSetupOSUpdateClient
+ _OBJC_METACLASS_$_SKSetupOSUpdateServer
+ __OBJC_$_INSTANCE_METHODS_SKSetupOSUpdateClient
+ __OBJC_$_INSTANCE_METHODS_SKSetupOSUpdateServer
+ __OBJC_$_INSTANCE_VARIABLES_SKSetupOSUpdateServer
+ __OBJC_CLASS_RO_$_SKSetupOSUpdateClient
+ __OBJC_CLASS_RO_$_SKSetupOSUpdateServer
+ __OBJC_METACLASS_RO_$_SKSetupOSUpdateClient
+ __OBJC_METACLASS_RO_$_SKSetupOSUpdateServer
+ ___29-[SKSetupOSUpdateClient _run]_block_invoke
+ ___38-[SKSetupOSUpdateClient _prepareSteps]_block_invoke
+ ___38-[SKSetupOSUpdateServer _prepareSteps]_block_invoke
+ ___42-[SKSetupOSUpdateServer _oobEnsureStarted]_block_invoke
+ ___48-[SKSetupOSUpdateServer _bleServerEnsureStarted]_block_invoke
+ ___48-[SKSetupOSUpdateServer _bleServerEnsureStarted]_block_invoke_2
+ ___51-[SKSetupOSUpdateServer _bleServerAcceptConnecton:]_block_invoke
+ ___52-[SKSetupOSUpdateServer _bleAdvertiserEnsureStarted]_block_invoke
+ ___Block_byref_object_copy_.1110
+ ___Block_byref_object_copy_.1519
+ ___Block_byref_object_copy_.1950
+ ___Block_byref_object_copy_.2163
+ ___Block_byref_object_copy_.382
+ ___Block_byref_object_copy_.556
+ ___Block_byref_object_copy_.756
+ ___Block_byref_object_copy_.913
+ ___Block_byref_object_dispose_.1111
+ ___Block_byref_object_dispose_.1520
+ ___Block_byref_object_dispose_.1951
+ ___Block_byref_object_dispose_.2164
+ ___Block_byref_object_dispose_.383
+ ___Block_byref_object_dispose_.557
+ ___Block_byref_object_dispose_.757
+ ___Block_byref_object_dispose_.914
+ ___block_literal_global.1213
+ ___block_literal_global.1275
+ ___block_literal_global.1314
+ ___block_literal_global.1376
+ ___block_literal_global.15
+ ___block_literal_global.1595
+ ___block_literal_global.1630
+ ___block_literal_global.1694
+ ___block_literal_global.19.2283
+ ___block_literal_global.21.2285
+ ___block_literal_global.22.1373
+ ___block_literal_global.2281
+ ___block_literal_global.23.1691
+ ___block_literal_global.23.2287
+ ___block_literal_global.24.1272
+ ___block_literal_global.297
+ ___block_literal_global.34.2259
+ ___block_literal_global.377
+ ___block_literal_global.47.2264
+ ___block_literal_global.476
+ ___block_literal_global.50.2253
+ ___block_literal_global.52
+ ___block_literal_global.53.2250
+ ___block_literal_global.593
+ ___block_literal_global.654
+ ___block_literal_global.820
+ ___block_literal_global.981
+ __unnamed_array_storage.1010
+ _gLogCategory_SKSetupOSUpdateClient
+ _gLogCategory_SKSetupOSUpdateServer
- GCC_except_table104
- GCC_except_table108
- GCC_except_table130
- GCC_except_table136
- GCC_except_table142
- GCC_except_table147
- GCC_except_table160
- GCC_except_table168
- GCC_except_table197
- GCC_except_table351
- GCC_except_table421
- GCC_except_table463
- GCC_except_table469
- GCC_except_table473
- GCC_except_table517
- GCC_except_table524
- GCC_except_table535
- GCC_except_table542
- GCC_except_table609
- GCC_except_table616
- GCC_except_table623
- GCC_except_table626
- GCC_except_table731
- GCC_except_table793
- GCC_except_table826
- GCC_except_table832
- GCC_except_table836
- ___Block_byref_object_copy_.1038
- ___Block_byref_object_copy_.1440
- ___Block_byref_object_copy_.1832
- ___Block_byref_object_copy_.2045
- ___Block_byref_object_copy_.315
- ___Block_byref_object_copy_.482
- ___Block_byref_object_copy_.682
- ___Block_byref_object_copy_.838
- ___Block_byref_object_dispose_.1039
- ___Block_byref_object_dispose_.1441
- ___Block_byref_object_dispose_.1833
- ___Block_byref_object_dispose_.2046
- ___Block_byref_object_dispose_.316
- ___Block_byref_object_dispose_.483
- ___Block_byref_object_dispose_.683
- ___Block_byref_object_dispose_.839
- ___block_literal_global.11
- ___block_literal_global.1139
- ___block_literal_global.1197
- ___block_literal_global.1235
- ___block_literal_global.1297
- ___block_literal_global.1516
- ___block_literal_global.1576
- ___block_literal_global.19.2164
- ___block_literal_global.21.2166
- ___block_literal_global.2162
- ___block_literal_global.22.1294
- ___block_literal_global.23.1573
- ___block_literal_global.23.2168
- ___block_literal_global.244
- ___block_literal_global.312
- ___block_literal_global.34.2140
- ___block_literal_global.403
- ___block_literal_global.47.2145
- ___block_literal_global.50.2134
- ___block_literal_global.519
- ___block_literal_global.53.2131
- ___block_literal_global.582
- ___block_literal_global.746
- ___block_literal_global.907
- __unnamed_array_storage.937
CStrings:
+ "-[SKSetupOSUpdateClient _run]"
+ "-[SKSetupOSUpdateServer _bleAdvertiserEnsureStarted]"
+ "-[SKSetupOSUpdateServer _bleAdvertiserEnsureStarted]_block_invoke"
+ "-[SKSetupOSUpdateServer _bleAdvertiserEnsureStopped]"
+ "-[SKSetupOSUpdateServer _bleServerAcceptConnecton:]"
+ "-[SKSetupOSUpdateServer _bleServerEnsureStarted]"
+ "-[SKSetupOSUpdateServer _bleServerEnsureStarted]_block_invoke"
+ "-[SKSetupOSUpdateServer _bleServerEnsureStarted]_block_invoke_2"
+ "-[SKSetupOSUpdateServer _bleServerEnsureStopped]"
+ "SKSetupOSUpdateClient"
+ "SKSetupOSUpdateServer"

```
