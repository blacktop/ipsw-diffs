## MediaServices

> `/System/Library/PrivateFrameworks/MediaServices.framework/MediaServices`

```diff

-4023.200.34.0.0
-  __TEXT.__text: 0x4ece8
-  __TEXT.__auth_stubs: 0x1bc0
-  __TEXT.__objc_methlist: 0x4844
+4023.310.4.0.0
+  __TEXT.__text: 0x506c4
+  __TEXT.__auth_stubs: 0x1bf0
+  __TEXT.__objc_methlist: 0x4924
   __TEXT.__const: 0x288
-  __TEXT.__gcc_except_tab: 0xb7c
-  __TEXT.__cstring: 0x5761
-  __TEXT.__oslogstring: 0x2490
+  __TEXT.__gcc_except_tab: 0xbf8
+  __TEXT.__cstring: 0x581b
+  __TEXT.__oslogstring: 0x27c1
   __TEXT.__dlopen_cstrs: 0x11d
   __TEXT.__ustring: 0x18
-  __TEXT.__unwind_info: 0x14c0
-  __TEXT.__objc_classname: 0x9ba
-  __TEXT.__objc_methname: 0xabb9
-  __TEXT.__objc_methtype: 0x1964
-  __TEXT.__objc_stubs: 0x73a0
+  __TEXT.__unwind_info: 0x1518
+  __TEXT.__objc_classname: 0xa20
+  __TEXT.__objc_methname: 0xad9f
+  __TEXT.__objc_methtype: 0x1a20
+  __TEXT.__objc_stubs: 0x7520
   __DATA_CONST.__got: 0x268
-  __DATA_CONST.__const: 0x14d8
-  __DATA_CONST.__objc_classlist: 0x2c0
+  __DATA_CONST.__const: 0x1550
+  __DATA_CONST.__objc_classlist: 0x2d0
   __DATA_CONST.__objc_catlist: 0x98
-  __DATA_CONST.__objc_protolist: 0x80
+  __DATA_CONST.__objc_protolist: 0x90
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_const: 0x6888
-  __DATA_CONST.__objc_selrefs: 0x29a8
+  __DATA_CONST.__objc_const: 0x6c70
+  __DATA_CONST.__objc_selrefs: 0x2a08
   __DATA_CONST.__objc_arraydata: 0x120
-  __AUTH_CONST.__cfstring: 0x53c0
-  __AUTH_CONST.__objc_const: 0x27e8
-  __AUTH_CONST.__const: 0x540
+  __AUTH_CONST.__cfstring: 0x5460
+  __AUTH_CONST.__objc_const: 0x2878
+  __AUTH_CONST.__const: 0x580
   __AUTH_CONST.__objc_arrayobj: 0x30
   __AUTH_CONST.__objc_intobj: 0x198
   __AUTH_CONST.__objc_dictobj: 0x28
   __AUTH_CONST.__auth_ptr: 0x8
-  __AUTH_CONST.__auth_got: 0xdf8
-  __AUTH.__objc_data: 0x1310
+  __AUTH_CONST.__auth_got: 0xe10
+  __AUTH.__objc_data: 0x13b0
   __DATA.__objc_protorefs: 0x18
-  __DATA.__objc_classrefs: 0x3a0
-  __DATA.__objc_superrefs: 0x218
-  __DATA.__objc_ivar: 0x5b8
-  __DATA.__data: 0x728
-  __DATA.__bss: 0x90
+  __DATA.__objc_classrefs: 0x3c8
+  __DATA.__objc_superrefs: 0x228
+  __DATA.__objc_ivar: 0x5e8
+  __DATA.__data: 0x7e8
+  __DATA.__bss: 0xd4
   __DATA_DIRTY.__objc_data: 0x870
   __DATA_DIRTY.__data: 0x8
   __DATA_DIRTY.__bss: 0xd0

   - /System/Library/PrivateFrameworks/IDS.framework/IDS
   - /System/Library/PrivateFrameworks/PersistentConnection.framework/PersistentConnection
   - /System/Library/PrivateFrameworks/ProtocolBuffer.framework/ProtocolBuffer
+  - /System/Library/PrivateFrameworks/RunningBoardServices.framework/RunningBoardServices
   - /System/Library/PrivateFrameworks/SoftLinking.framework/SoftLinking
   - /System/Library/PrivateFrameworks/TCC.framework/TCC
   - /System/Library/PrivateFrameworks/Trial.framework/Trial

   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libsqlite3.dylib
   - /usr/lib/libz.1.dylib
-  Functions: 1911
-  Symbols:   6678
-  CStrings:  3434
+  Functions: 1937
+  Symbols:   6803
+  CStrings:  3485
 
Symbols:
+ -[MSVExtendableBackgroundTaskProvider .cxx_destruct]
+ -[MSVExtendableBackgroundTaskProvider _assertionInvalidated:error:]
+ -[MSVExtendableBackgroundTaskProvider _locked_acquireAssertion:]
+ -[MSVExtendableBackgroundTaskProvider _locked_needsAssertion]
+ -[MSVExtendableBackgroundTaskProvider _locked_releaseAssertion]
+ -[MSVExtendableBackgroundTaskProvider _locked_removeAllTasksWithError:]
+ -[MSVExtendableBackgroundTaskProvider _locked_taskCount]
+ -[MSVExtendableBackgroundTaskProvider _taskDidTimeout:]
+ -[MSVExtendableBackgroundTaskProvider beginTaskWithExpirationHandler:]
+ -[MSVExtendableBackgroundTaskProvider beginTaskWithName:expirationHandler:]
+ -[MSVExtendableBackgroundTaskProvider endTask:]
+ -[MSVExtendableBackgroundTaskProvider initWithRunningRBSDomain:name:invalidationDuration:]
+ -[MSVLRUDictionary enumerateKeysAndObjectsUsingBlock:]
+ -[_MSVSQLSonicAssertion .cxx_destruct]
+ -[_MSVSQLSonicAssertion description]
+ -[_MSVSQLSonicAssertion invalidate]
+ GCC_except_table1084
+ GCC_except_table1124
+ GCC_except_table1130
+ GCC_except_table117
+ GCC_except_table129
+ GCC_except_table1334
+ GCC_except_table1441
+ GCC_except_table1445
+ GCC_except_table1447
+ GCC_except_table1449
+ GCC_except_table1451
+ GCC_except_table1453
+ GCC_except_table1455
+ GCC_except_table1457
+ GCC_except_table1459
+ GCC_except_table1463
+ GCC_except_table1532
+ GCC_except_table1540
+ GCC_except_table1541
+ GCC_except_table1542
+ GCC_except_table1546
+ GCC_except_table1549
+ GCC_except_table1553
+ GCC_except_table1555
+ GCC_except_table1557
+ GCC_except_table1558
+ GCC_except_table1563
+ GCC_except_table159
+ GCC_except_table1656
+ GCC_except_table170
+ GCC_except_table1732
+ GCC_except_table1736
+ GCC_except_table1738
+ GCC_except_table1773
+ GCC_except_table1797
+ GCC_except_table1802
+ GCC_except_table1818
+ GCC_except_table1819
+ GCC_except_table1820
+ GCC_except_table242
+ GCC_except_table248
+ GCC_except_table256
+ GCC_except_table281
+ GCC_except_table449
+ GCC_except_table458
+ GCC_except_table522
+ GCC_except_table584
+ GCC_except_table586
+ GCC_except_table591
+ GCC_except_table593
+ GCC_except_table594
+ GCC_except_table595
+ GCC_except_table601
+ GCC_except_table631
+ GCC_except_table639
+ GCC_except_table726
+ GCC_except_table746
+ GCC_except_table864
+ GCC_except_table919
+ GCC_except_table920
+ GCC_except_table924
+ GCC_except_table933
+ GCC_except_table940
+ GCC_except_table942
+ GCC_except_table971
+ GCC_except_table989
+ GCC_except_table993
+ GCC_except_table997
+ _MSVFastHexStringFromBytes.hexCharacters.3364
+ _MSVGetDeviceHardwarePlatform
+ _MSVGetDeviceHardwarePlatform.__hardwarePlatform
+ _MSVGetDeviceHardwarePlatform.onceToken
+ _OBJC_CLASS_$_MSVExtendableBackgroundTaskProvider
+ _OBJC_CLASS_$_RBSAssertion
+ _OBJC_CLASS_$_RBSDomainAttribute
+ _OBJC_CLASS_$_RBSTarget
+ _OBJC_CLASS_$__MSVSQLSonicAssertion
+ _OBJC_IVAR_$_MSVExtendableBackgroundTaskProvider._assertion
+ _OBJC_IVAR_$_MSVExtendableBackgroundTaskProvider._assertionCreatedTime
+ _OBJC_IVAR_$_MSVExtendableBackgroundTaskProvider._assertionInvalidationNonce
+ _OBJC_IVAR_$_MSVExtendableBackgroundTaskProvider._domain
+ _OBJC_IVAR_$_MSVExtendableBackgroundTaskProvider._expirationHandlers
+ _OBJC_IVAR_$_MSVExtendableBackgroundTaskProvider._explanationForExtension
+ _OBJC_IVAR_$_MSVExtendableBackgroundTaskProvider._invalidationDuration
+ _OBJC_IVAR_$_MSVExtendableBackgroundTaskProvider._lastIdentifier
+ _OBJC_IVAR_$_MSVExtendableBackgroundTaskProvider._lock
+ _OBJC_IVAR_$_MSVExtendableBackgroundTaskProvider._name
+ _OBJC_IVAR_$_MSVExtendableBackgroundTaskProvider._timeoutGuards
+ _OBJC_IVAR_$__MSVSQLSonicAssertion._name
+ _OBJC_METACLASS_$_MSVExtendableBackgroundTaskProvider
+ _OBJC_METACLASS_$__MSVSQLSonicAssertion
+ __OBJC_$_INSTANCE_METHODS_MSVExtendableBackgroundTaskProvider
+ __OBJC_$_INSTANCE_METHODS__MSVSQLSonicAssertion
+ __OBJC_$_INSTANCE_VARIABLES_MSVExtendableBackgroundTaskProvider
+ __OBJC_$_INSTANCE_VARIABLES__MSVSQLSonicAssertion
+ __OBJC_$_PROP_LIST_MSVExtendableBackgroundTaskProvider
+ __OBJC_$_PROP_LIST__MSVSQLProcessAssertion
+ __OBJC_$_PROP_LIST__MSVSQLSonicAssertion
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_OPT_RBSAssertionObserving
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS__MSVSQLAssertion
+ __OBJC_$_PROTOCOL_METHOD_TYPES_RBSAssertionObserving
+ __OBJC_$_PROTOCOL_METHOD_TYPES__MSVSQLAssertion
+ __OBJC_$_PROTOCOL_REFS_RBSAssertionObserving
+ __OBJC_$_PROTOCOL_REFS__MSVSQLAssertion
+ __OBJC_CLASS_PROTOCOLS_$_MSVExtendableBackgroundTaskProvider
+ __OBJC_CLASS_PROTOCOLS_$__MSVSQLProcessAssertion
+ __OBJC_CLASS_PROTOCOLS_$__MSVSQLSonicAssertion
+ __OBJC_CLASS_RO_$_MSVExtendableBackgroundTaskProvider
+ __OBJC_CLASS_RO_$__MSVSQLSonicAssertion
+ __OBJC_LABEL_PROTOCOL_$_RBSAssertionObserving
+ __OBJC_LABEL_PROTOCOL_$__MSVSQLAssertion
+ __OBJC_METACLASS_RO_$_MSVExtendableBackgroundTaskProvider
+ __OBJC_METACLASS_RO_$__MSVSQLSonicAssertion
+ __OBJC_PROTOCOL_$_RBSAssertionObserving
+ __OBJC_PROTOCOL_$__MSVSQLAssertion
+ ___35-[_MSVSQLSonicAssertion invalidate]_block_invoke
+ ___39+[_MSVSQLSonicAssertion hasEntitlement]_block_invoke
+ ___63-[MSVExtendableBackgroundTaskProvider _locked_releaseAssertion]_block_invoke
+ ___64-[MSVExtendableBackgroundTaskProvider _locked_acquireAssertion:]_block_invoke
+ ___71-[MSVExtendableBackgroundTaskProvider _locked_removeAllTasksWithError:]_block_invoke
+ ___75-[MSVExtendableBackgroundTaskProvider beginTaskWithName:expirationHandler:]_block_invoke
+ ___Block_byref_object_copy_.1570
+ ___Block_byref_object_copy_.1984
+ ___Block_byref_object_copy_.2516
+ ___Block_byref_object_copy_.2828
+ ___Block_byref_object_copy_.3320
+ ___Block_byref_object_copy_.3358
+ ___Block_byref_object_copy_.3633
+ ___Block_byref_object_copy_.3784
+ ___Block_byref_object_copy_.3929
+ ___Block_byref_object_copy_.4188
+ ___Block_byref_object_copy_.4947
+ ___Block_byref_object_copy_.5288
+ ___Block_byref_object_copy_.5647
+ ___Block_byref_object_copy_.596
+ ___Block_byref_object_dispose_.1571
+ ___Block_byref_object_dispose_.1985
+ ___Block_byref_object_dispose_.2517
+ ___Block_byref_object_dispose_.2829
+ ___Block_byref_object_dispose_.3321
+ ___Block_byref_object_dispose_.3359
+ ___Block_byref_object_dispose_.3634
+ ___Block_byref_object_dispose_.3785
+ ___Block_byref_object_dispose_.3930
+ ___Block_byref_object_dispose_.4189
+ ___Block_byref_object_dispose_.4948
+ ___Block_byref_object_dispose_.5289
+ ___Block_byref_object_dispose_.5648
+ ___Block_byref_object_dispose_.597
+ ___MSVGetDeviceHardwarePlatform_block_invoke
+ ___assertion.5178
+ ___assertionCount.5176
+ ___assertionCreatedTime
+ ___assertionInvalidationNonce.5177
+ ___assertionLock.5175
+ ___block_descriptor_48_e8_32r40w_e34_v24?0"RBSAssertion"8"NSError"16lw40l8r32l8
+ ___block_descriptor_48_e8_32s40s_e40_v32?0"NSNumber"8"MSVBlockGuard"16^B24ls32l8s40l8
+ ___block_descriptor_48_e8_32w_e8_v16?0q8lw32l8
+ ___block_literal_global.1064
+ ___block_literal_global.120.2054
+ ___block_literal_global.128.4185
+ ___block_literal_global.1452
+ ___block_literal_global.146
+ ___block_literal_global.148
+ ___block_literal_global.1667
+ ___block_literal_global.1756
+ ___block_literal_global.1884
+ ___block_literal_global.1925
+ ___block_literal_global.2033
+ ___block_literal_global.2380
+ ___block_literal_global.2740
+ ___block_literal_global.2772
+ ___block_literal_global.2895
+ ___block_literal_global.3624
+ ___block_literal_global.3788
+ ___block_literal_global.4148
+ ___block_literal_global.4895
+ ___block_literal_global.5241
+ ___block_literal_global.5295
+ ___block_literal_global.5570
+ ___block_literal_global.629
+ ___block_literal_global.844
+ __unnamed_array_storage.3041
+ _hasEntitlement.hasEntitlement
+ _hasEntitlement.onceToken
+ _objc_msgSend$_assertionInvalidated:error:
+ _objc_msgSend$_locked_acquireAssertion:
+ _objc_msgSend$_locked_needsAssertion
+ _objc_msgSend$_locked_removeAllTasksWithError:
+ _objc_msgSend$_locked_taskCount
+ _objc_msgSend$_taskDidTimeout:
+ _objc_msgSend$acquireWithError:
+ _objc_msgSend$acquireWithInvalidationHandler:
+ _objc_msgSend$attributeWithDomain:name:
+ _objc_msgSend$currentProcess
+ _objc_msgSend$hasBoolEntitlement:
+ _objc_msgSend$initWithExplanation:target:attributes:
+ _objc_opt_self
+ _os_unfair_recursive_lock_lock_with_options
+ _os_unfair_recursive_lock_unlock
- GCC_except_table1060
- GCC_except_table1100
- GCC_except_table1106
- GCC_except_table1314
- GCC_except_table141
- GCC_except_table1417
- GCC_except_table1421
- GCC_except_table1423
- GCC_except_table1425
- GCC_except_table1427
- GCC_except_table1429
- GCC_except_table1431
- GCC_except_table1433
- GCC_except_table1435
- GCC_except_table1439
- GCC_except_table1512
- GCC_except_table1513
- GCC_except_table1515
- GCC_except_table1517
- GCC_except_table1518
- GCC_except_table152
- GCC_except_table1520
- GCC_except_table1521
- GCC_except_table1522
- GCC_except_table1526
- GCC_except_table1529
- GCC_except_table1543
- GCC_except_table1636
- GCC_except_table1711
- GCC_except_table1715
- GCC_except_table1717
- GCC_except_table1752
- GCC_except_table1771
- GCC_except_table1776
- GCC_except_table1792
- GCC_except_table1793
- GCC_except_table1794
- GCC_except_table224
- GCC_except_table230
- GCC_except_table238
- GCC_except_table263
- GCC_except_table431
- GCC_except_table440
- GCC_except_table500
- GCC_except_table562
- GCC_except_table564
- GCC_except_table569
- GCC_except_table571
- GCC_except_table572
- GCC_except_table573
- GCC_except_table579
- GCC_except_table609
- GCC_except_table617
- GCC_except_table704
- GCC_except_table724
- GCC_except_table840
- GCC_except_table892
- GCC_except_table895
- GCC_except_table896
- GCC_except_table900
- GCC_except_table909
- GCC_except_table918
- GCC_except_table947
- GCC_except_table965
- GCC_except_table969
- GCC_except_table973
- _MSVFastHexStringFromBytes.hexCharacters.3161
- ___Block_byref_object_copy_.1376
- ___Block_byref_object_copy_.1786
- ___Block_byref_object_copy_.2314
- ___Block_byref_object_copy_.2625
- ___Block_byref_object_copy_.3115
- ___Block_byref_object_copy_.3153
- ___Block_byref_object_copy_.3414
- ___Block_byref_object_copy_.3561
- ___Block_byref_object_copy_.3705
- ___Block_byref_object_copy_.3966
- ___Block_byref_object_copy_.4724
- ___Block_byref_object_copy_.4962
- ___Block_byref_object_copy_.5321
- ___Block_byref_object_dispose_.1377
- ___Block_byref_object_dispose_.1787
- ___Block_byref_object_dispose_.2315
- ___Block_byref_object_dispose_.2626
- ___Block_byref_object_dispose_.3116
- ___Block_byref_object_dispose_.3154
- ___Block_byref_object_dispose_.3415
- ___Block_byref_object_dispose_.3562
- ___Block_byref_object_dispose_.3706
- ___Block_byref_object_dispose_.3967
- ___Block_byref_object_dispose_.4725
- ___Block_byref_object_dispose_.4963
- ___Block_byref_object_dispose_.5322
- ___block_literal_global.120.1856
- ___block_literal_global.1261
- ___block_literal_global.128.3963
- ___block_literal_global.143
- ___block_literal_global.1469
- ___block_literal_global.1557
- ___block_literal_global.1684
- ___block_literal_global.1724
- ___block_literal_global.1835
- ___block_literal_global.2178
- ___block_literal_global.2538
- ___block_literal_global.2570
- ___block_literal_global.2692
- ___block_literal_global.3405
- ___block_literal_global.3565
- ___block_literal_global.3926
- ___block_literal_global.4672
- ___block_literal_global.4969
- ___block_literal_global.5244
- ___block_literal_global.525
- ___block_literal_global.732
- ___block_literal_global.952
- __unnamed_array_storage.2836
CStrings:
+ "\x02!!\x12"
+ " (extension)"
+ "@\"<_MSVSQLAssertion>\""
+ "@\"RBSAssertion\""
+ "@40@0:8@16@24d32"
+ "HardwarePlatform"
+ "MSVExtendableBackgroundTaskProvider"
+ "MSVExtendableBackgroundTaskProvider %p Invalidated RBSAssertion %p"
+ "MSVExtendableBackgroundTaskProvider %p RBSAssertion %p invalidated with error: %{public}@"
+ "MSVExtendableBackgroundTaskProvider %p Task #%ld ended"
+ "MSVExtendableBackgroundTaskProvider %p Task #%ld ended [%{public}@]"
+ "MSVExtendableBackgroundTaskProvider %p Task #%ld expired"
+ "MSVExtendableBackgroundTaskProvider %p Task #%ld started [%{public}@]"
+ "MSVExtendableBackgroundTaskProvider %p Took RBSAssertion %p %{public}@ [%{public}@]"
+ "RBSAssertionObserving"
+ "SonicBackgroundTask"
+ "[MSVQRConnection] <%p> Clear connection."
+ "[MSVQRConnection] <%p> Clear group session."
+ "[MSVQRConnection] <%p> Register plugin."
+ "[SQL] Acquired RBSAssertion %p"
+ "[SQL] Failed to acquire RBSAssertion %p error=%{public}@"
+ "[SQL] Invalidating RBSAssertion %p Timeout"
+ "[SQL] Invalidating existing RBSAssertion %p"
+ "[SQL] Taking RBSAssertion"
+ "_MSVSQLAssertion"
+ "_MSVSQLSonicAssertion"
+ "_assertionCreatedTime"
+ "_assertionInvalidated:error:"
+ "_domain"
+ "_expirationHandlers"
+ "_explanationForExtension"
+ "_invalidationDuration"
+ "_locked_acquireAssertion:"
+ "_locked_needsAssertion"
+ "_locked_removeAllTasksWithError:"
+ "_locked_taskCount"
+ "_taskDidTimeout:"
+ "acquireWithError:"
+ "acquireWithInvalidationHandler:"
+ "assertion:didInvalidateWithError:"
+ "assertionWillInvalidate:"
+ "attributeWithDomain:name:"
+ "com.apple.runningboard.sonic"
+ "com.apple.sonic.backgroundtask"
+ "currentProcess"
+ "initWithExplanation:target:attributes:"
+ "initWithRunningRBSDomain:name:invalidationDuration:"
+ "v24@0:8@\"RBSAssertion\"16"
+ "v24@?0@\"RBSAssertion\"8@\"NSError\"16"
+ "v32@0:8@\"RBSAssertion\"16@\"NSError\"24"
+ "v32@?0@\"NSNumber\"8@\"MSVBlockGuard\"16^B24"
+ "{os_unfair_recursive_lock_s=\"ourl_lock\"{os_unfair_lock_s=\"_os_unfair_lock_opaque\"I}\"ourl_count\"I}"
- "@\"_MSVSQLProcessAssertion\""

```
