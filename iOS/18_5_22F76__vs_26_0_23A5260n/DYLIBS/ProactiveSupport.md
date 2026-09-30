## ProactiveSupport

> `/System/Library/PrivateFrameworks/ProactiveSupport.framework/ProactiveSupport`

```diff

-408.0.0.0.0
-  __TEXT.__text: 0x61ecc
-  __TEXT.__auth_stubs: 0x20e0
-  __TEXT.__objc_methlist: 0x3d14
-  __TEXT.__const: 0xc5b
+412.0.0.0.0
+  __TEXT.__text: 0x627b4
+  __TEXT.__auth_stubs: 0x2120
+  __TEXT.__objc_methlist: 0x3d54
+  __TEXT.__const: 0xc8b
   __TEXT.__objc_databytes: 0x1
   __TEXT.__swift5_typeref: 0x225
   __TEXT.__swift5_capture: 0x9c

   __TEXT.__swift5_types: 0x2c
   __TEXT.__swift_as_entry: 0xc
   __TEXT.__swift_as_ret: 0x10
-  __TEXT.__gcc_except_tab: 0x1b64
-  __TEXT.__oslogstring: 0x42e4
+  __TEXT.__gcc_except_tab: 0x1b84
+  __TEXT.__oslogstring: 0x42e5
   __TEXT.__ustring: 0x13c
   __TEXT.__unwind_info: 0x1920
   __TEXT.__eh_frame: 0x480
-  __TEXT.__objc_classname: 0x98a
-  __TEXT.__objc_methname: 0x8bf8
-  __TEXT.__objc_methtype: 0x1c62
+  __TEXT.__objc_classname: 0x98b
+  __TEXT.__objc_methname: 0x8d83
+  __TEXT.__objc_methtype: 0x1a2c
   __TEXT.__objc_stubs: 0x6120
-  __DATA_CONST.__got: 0x630
-  __DATA_CONST.__const: 0x19f8
+  __DATA_CONST.__got: 0x638
+  __DATA_CONST.__const: 0x1a00
   __DATA_CONST.__objc_classlist: 0x348
   __DATA_CONST.__objc_catlist: 0x48
   __DATA_CONST.__objc_protolist: 0x48
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x2290
+  __DATA_CONST.__objc_selrefs: 0x22c0
   __DATA_CONST.__objc_protorefs: 0x20
   __DATA_CONST.__objc_superrefs: 0x228
   __DATA_CONST.__objc_arraydata: 0x18
-  __AUTH_CONST.__auth_got: 0x1088
-  __AUTH_CONST.__const: 0xce0
+  __AUTH_CONST.__auth_got: 0x10a8
+  __AUTH_CONST.__const: 0xcc0
   __AUTH_CONST.__cfstring: 0x4940
-  __AUTH_CONST.__objc_const: 0x6cb0
+  __AUTH_CONST.__objc_const: 0x6cd0
   __AUTH_CONST.__objc_intobj: 0x318
   __AUTH_CONST.__objc_arrayobj: 0x48
-  __AUTH.__objc_data: 0xe60
-  __AUTH.__data: 0x1f8
+  __AUTH.__objc_data: 0xfa0
+  __AUTH.__data: 0x220
   __AUTH.__objc_dataobj: 0x18
-  __DATA.__objc_ivar: 0x414
-  __DATA.__data: 0xa18
-  __DATA.__bss: 0x1780
-  __DATA_DIRTY.__objc_data: 0x1270
+  __DATA.__objc_ivar: 0x418
+  __DATA.__data: 0x9e8
+  __DATA.__bss: 0x1788
+  __DATA_DIRTY.__objc_data: 0x1130
   __DATA_DIRTY.__data: 0xc0
   __DATA_DIRTY.__bss: 0x40
   - /System/Library/Frameworks/Accelerate.framework/Accelerate

   - /usr/lib/swift/libswiftXPC.dylib
   - /usr/lib/swift/libswift_Builtin_float.dylib
   - /usr/lib/swift/libswift_Concurrency.dylib
-  - /usr/lib/swift/libswift_errno.dylib
-  - /usr/lib/swift/libswift_math.dylib
-  - /usr/lib/swift/libswift_signal.dylib
-  - /usr/lib/swift/libswift_stdio.dylib
-  - /usr/lib/swift/libswift_time.dylib
+  - /usr/lib/swift/libswift_DarwinFoundation1.dylib
+  - /usr/lib/swift/libswift_DarwinFoundation2.dylib
+  - /usr/lib/swift/libswift_DarwinFoundation3.dylib
   - /usr/lib/swift/libswiftos.dylib
-  - /usr/lib/swift/libswiftsys_time.dylib
-  - /usr/lib/swift/libswiftunistd.dylib
-  UUID: 63362AF0-A181-32A7-B016-EA1DF904950B
-  Functions: 1917
-  Symbols:   6195
-  CStrings:  3502
+  UUID: 0755F1E1-DF33-31B2-B9FD-81EF36958EC2
+  Functions: 1926
+  Symbols:   6211
+  CStrings:  3506
 
Symbols:
+ +[_PASDeviceState deviceLockState]
+ +[_PASDeviceState isDeviceFormattedForProtectionForDevice]
+ +[_PASDeviceState isDeviceUnlocked]
+ +[_PASDeviceState registerForLockStateChangeForDeviceNotifications:]
+ +[_PASDeviceState unregisterForLockStateChangeforDeviceNotifications:]
+ -[_PASXPCClientHelper initWithServiceName:connectionOptions:allowlistedServerInterface:allowlistedClientInterface:serverInitiatedRequestHandler:allowSystemToUserConnection:interruptionHandler:invalidationHandler:logHandle:]
+ GCC_except_table1017
+ GCC_except_table1025
+ GCC_except_table1032
+ GCC_except_table1048
+ GCC_except_table1055
+ GCC_except_table1217
+ GCC_except_table1233
+ GCC_except_table1234
+ GCC_except_table1238
+ GCC_except_table1239
+ GCC_except_table1243
+ GCC_except_table1258
+ GCC_except_table1288
+ GCC_except_table1295
+ GCC_except_table1297
+ GCC_except_table1300
+ GCC_except_table1303
+ GCC_except_table1305
+ GCC_except_table1313
+ GCC_except_table1315
+ GCC_except_table1318
+ GCC_except_table1319
+ GCC_except_table1321
+ GCC_except_table1322
+ GCC_except_table1341
+ GCC_except_table1354
+ GCC_except_table1356
+ GCC_except_table1357
+ GCC_except_table1387
+ GCC_except_table1391
+ GCC_except_table1396
+ GCC_except_table1399
+ GCC_except_table1403
+ GCC_except_table1435
+ GCC_except_table1441
+ GCC_except_table1449
+ GCC_except_table1556
+ GCC_except_table1557
+ GCC_except_table1583
+ GCC_except_table1585
+ GCC_except_table1604
+ GCC_except_table1611
+ GCC_except_table1613
+ GCC_except_table1618
+ GCC_except_table1630
+ GCC_except_table1643
+ GCC_except_table1649
+ GCC_except_table1666
+ GCC_except_table1667
+ GCC_except_table543
+ GCC_except_table552
+ GCC_except_table559
+ GCC_except_table560
+ GCC_except_table564
+ GCC_except_table637
+ GCC_except_table721
+ GCC_except_table723
+ GCC_except_table728
+ GCC_except_table796
+ GCC_except_table798
+ GCC_except_table801
+ GCC_except_table820
+ GCC_except_table826
+ GCC_except_table855
+ GCC_except_table863
+ GCC_except_table869
+ GCC_except_table907
+ GCC_except_table917
+ GCC_except_table936
+ GCC_except_table979
+ _CFAllocatorAllocateTyped
+ _OBJC_IVAR_$__PASXPCClientHelper._connectionOptions
+ __ZNSt12length_errorC1B8ne200100EPKc
+ __ZNSt3__110unique_ptrIN9proactive3pas18SynchronizedObjectIN12_GLOBAL__N_113HDGuardedDataENS2_6detail14RecursiveMutexEEENS_14default_deleteIS8_EEE5resetB8ne200100EPS8_
+ __ZNSt3__120__throw_length_errorB8ne200100EPKc
+ __ZNSt3__16vectorIDv8_fN12_GLOBAL__N_120SimdAlignedAllocatorIS1_EEE20__throw_length_errorB8ne200100Ev
+ __ZNSt3__16vectorIDv8_iN12_GLOBAL__N_120SimdAlignedAllocatorIS1_EEE20__throw_length_errorB8ne200100Ev
+ __ZNSt3__16vectorIhNS_9allocatorIhEEE18__insert_with_sizeB8ne200100IPKhS6_EENS_11__wrap_iterIPhEENS7_IS6_EET_T0_l
+ __ZNSt3__16vectorIhNS_9allocatorIhEEE20__throw_length_errorB8ne200100Ev
+ ___Block_byref_object_copy_.2105
+ ___Block_byref_object_copy_.2360
+ ___Block_byref_object_copy_.2487
+ ___Block_byref_object_copy_.2694
+ ___Block_byref_object_copy_.3005
+ ___Block_byref_object_copy_.3271
+ ___Block_byref_object_copy_.3441
+ ___Block_byref_object_copy_.4066
+ ___Block_byref_object_dispose_.2106
+ ___Block_byref_object_dispose_.2361
+ ___Block_byref_object_dispose_.2488
+ ___Block_byref_object_dispose_.2695
+ ___Block_byref_object_dispose_.3006
+ ___Block_byref_object_dispose_.3272
+ ___Block_byref_object_dispose_.3442
+ ___Block_byref_object_dispose_.4067
+ ___block_descriptor_56_e8_32s40bs_e5_v8?0ls32l8s40l8
+ ___block_literal_global.1219
+ ___block_literal_global.1581
+ ___block_literal_global.1773
+ ___block_literal_global.1956
+ ___block_literal_global.2111
+ ___block_literal_global.2348
+ ___block_literal_global.2444
+ ___block_literal_global.2490
+ ___block_literal_global.2527
+ ___block_literal_global.2922
+ ___block_literal_global.3078
+ ___block_literal_global.3577
+ ___block_literal_global.3994
+ ___block_literal_global.4068
+ ___block_literal_global.4132
+ ___block_literal_global.42
+ ___block_literal_global.49.3995
+ ___block_literal_global.57.3996
+ ___block_literal_global.60
+ ___block_literal_global.8.1944
+ ___block_literal_global.8.2102
+ ___block_literal_global.90.3938
+ ___handleFirstUnlockEvent_block_invoke
+ ___registerForLockStateChangesForDevice_block_invoke
+ ___unregisterForFirstUnlockEvents_block_invoke
+ __swiftEmptyDictionarySingleton
+ __swift_FORCE_LOAD_$_swift_DarwinFoundation1
+ __swift_FORCE_LOAD_$_swift_DarwinFoundation1_$_ProactiveSupport
+ __swift_FORCE_LOAD_$_swift_DarwinFoundation2
+ __swift_FORCE_LOAD_$_swift_DarwinFoundation2_$_ProactiveSupport
+ __swift_FORCE_LOAD_$_swift_DarwinFoundation3
+ __swift_FORCE_LOAD_$_swift_DarwinFoundation3_$_ProactiveSupport
+ _cfAllocateAlwaysFailing.1710
+ _corruptionError.2019
+ _deviceFormattedForContentProtection
+ _deviceLockState
+ _getLockStateChangedQueue
+ _handleFirstUnlockEvent.onceTokenUnlocked
+ _objc_msgSend$initWithServiceName:connectionOptions:allowlistedServerInterface:allowlistedClientInterface:serverInitiatedRequestHandler:allowSystemToUserConnection:interruptionHandler:invalidationHandler:logHandle:
+ _registerForLockStateChangesForDevice
+ _runWithGlobalPLPLock.lock.3365
+ _unregisterForLockStateChangesForDevice
- GCC_except_table1018
- GCC_except_table1026
- GCC_except_table1034
- GCC_except_table1049
- GCC_except_table1056
- GCC_except_table1206
- GCC_except_table1222
- GCC_except_table1223
- GCC_except_table1227
- GCC_except_table1228
- GCC_except_table1232
- GCC_except_table1236
- GCC_except_table1275
- GCC_except_table1277
- GCC_except_table1284
- GCC_except_table1289
- GCC_except_table1292
- GCC_except_table1294
- GCC_except_table1299
- GCC_except_table1302
- GCC_except_table1304
- GCC_except_table1307
- GCC_except_table1308
- GCC_except_table1311
- GCC_except_table1330
- GCC_except_table1343
- GCC_except_table1345
- GCC_except_table1346
- GCC_except_table1376
- GCC_except_table1377
- GCC_except_table1380
- GCC_except_table1385
- GCC_except_table1392
- GCC_except_table1424
- GCC_except_table1430
- GCC_except_table1438
- GCC_except_table1545
- GCC_except_table1546
- GCC_except_table1572
- GCC_except_table1574
- GCC_except_table1582
- GCC_except_table1596
- GCC_except_table1600
- GCC_except_table1602
- GCC_except_table1608
- GCC_except_table1627
- GCC_except_table1632
- GCC_except_table1655
- GCC_except_table1656
- GCC_except_table541
- GCC_except_table547
- GCC_except_table555
- GCC_except_table562
- GCC_except_table565
- GCC_except_table638
- GCC_except_table722
- GCC_except_table724
- GCC_except_table729
- GCC_except_table797
- GCC_except_table799
- GCC_except_table802
- GCC_except_table821
- GCC_except_table827
- GCC_except_table856
- GCC_except_table865
- GCC_except_table871
- GCC_except_table908
- GCC_except_table918
- GCC_except_table937
- GCC_except_table980
- _CFAllocatorAllocate
- __ZNK12_GLOBAL__N_114BuddyAllocator12heapContainsEPKv
- __ZNK12_GLOBAL__N_114BuddyAllocator13levelForBlockERKN9proactive3pas15SynchronizedPtrINS2_10buddyalloc11GuardedDataENS2_6detail8SpinLockEEEPKv
- __ZNKSt3__16vectorIDv8_fN12_GLOBAL__N_120SimdAlignedAllocatorIS1_EEE20__throw_length_errorB8ne190102Ev
- __ZNKSt3__16vectorIDv8_iN12_GLOBAL__N_120SimdAlignedAllocatorIS1_EEE20__throw_length_errorB8ne190102Ev
- __ZNKSt3__16vectorIhNS_9allocatorIhEEE20__throw_length_errorB8ne190102Ev
- __ZNSt12length_errorC1B8ne190102EPKc
- __ZNSt3__110unique_ptrIN9proactive3pas18SynchronizedObjectIN12_GLOBAL__N_113HDGuardedDataENS2_6detail14RecursiveMutexEEENS_14default_deleteIS8_EEE5resetB8ne190102EPS8_
- __ZNSt3__120__throw_length_errorB8ne190102EPKc
- __ZNSt3__16vectorIhNS_9allocatorIhEEE18__insert_with_sizeB8ne190102IPKhS6_EENS_11__wrap_iterIPhEENS7_IS6_EET_T0_l
- __Znwm
- ___Block_byref_object_copy_.2101
- ___Block_byref_object_copy_.2356
- ___Block_byref_object_copy_.2483
- ___Block_byref_object_copy_.2690
- ___Block_byref_object_copy_.3001
- ___Block_byref_object_copy_.3259
- ___Block_byref_object_copy_.3428
- ___Block_byref_object_copy_.4057
- ___Block_byref_object_dispose_.2102
- ___Block_byref_object_dispose_.2357
- ___Block_byref_object_dispose_.2484
- ___Block_byref_object_dispose_.2691
- ___Block_byref_object_dispose_.3002
- ___Block_byref_object_dispose_.3260
- ___Block_byref_object_dispose_.3429
- ___Block_byref_object_dispose_.4058
- ___block_literal_global.1218
- ___block_literal_global.1577
- ___block_literal_global.1769
- ___block_literal_global.1952
- ___block_literal_global.2107
- ___block_literal_global.2344
- ___block_literal_global.2440
- ___block_literal_global.2486
- ___block_literal_global.2523
- ___block_literal_global.2918
- ___block_literal_global.3066
- ___block_literal_global.3564
- ___block_literal_global.37
- ___block_literal_global.3981
- ___block_literal_global.4059
- ___block_literal_global.4123
- ___block_literal_global.46.3982
- ___block_literal_global.49.3983
- ___block_literal_global.54.3984
- ___block_literal_global.57.3985
- ___block_literal_global.8.1940
- ___block_literal_global.8.2098
- ___block_literal_global.90.3925
- ___registerOnceForFirstUnlock_block_invoke.44
- __swift_FORCE_LOAD_$_swift_errno
- __swift_FORCE_LOAD_$_swift_errno_$_ProactiveSupport
- __swift_FORCE_LOAD_$_swift_math
- __swift_FORCE_LOAD_$_swift_math_$_ProactiveSupport
- __swift_FORCE_LOAD_$_swift_signal
- __swift_FORCE_LOAD_$_swift_signal_$_ProactiveSupport
- __swift_FORCE_LOAD_$_swift_stdio
- __swift_FORCE_LOAD_$_swift_stdio_$_ProactiveSupport
- __swift_FORCE_LOAD_$_swift_time
- __swift_FORCE_LOAD_$_swift_time_$_ProactiveSupport
- __swift_FORCE_LOAD_$_swiftsys_time
- __swift_FORCE_LOAD_$_swiftsys_time_$_ProactiveSupport
- __swift_FORCE_LOAD_$_swiftunistd
- __swift_FORCE_LOAD_$_swiftunistd_$_ProactiveSupport
- _cfAllocateAlwaysFailing.1706
- _corruptionError.2015
- _objc_msgSend$initWithServiceName:allowlistedServerInterface:allowlistedClientInterface:serverInitiatedRequestHandler:allowSystemToUserConnection:interruptionHandler:invalidationHandler:logHandle:
- _runWithGlobalPLPLock.lock.3352
CStrings:
+ "@84@0:8@16Q24@32@40@48B56@?60@?68@76"
+ "Handler for MobileKeyBag class C unlock handler for system or user volume (handle call uuid:%@)"
+ "Ran MobileKeyBag class C unlock (handle call uuid:%@)"
+ "Running MobileKeyBag class C unlock (handle call uuid:%@)"
+ "_connectionOptions"
+ "deviceLockState"
+ "initWithServiceName:connectionOptions:allowlistedServerInterface:allowlistedClientInterface:serverInitiatedRequestHandler:allowSystemToUserConnection:interruptionHandler:invalidationHandler:logHandle:"
+ "isDeviceFormattedForProtectionForDevice"
+ "isDeviceUnlocked"
+ "registerForLockStateChangeForDeviceNotifications:"
+ "unregisterForLockStateChangeforDeviceNotifications:"
+ "v24@0:8r^{_PASDeviceStateSystemCallbacks=^?^?^?^?^?^?^?^?^?^?^?^?^?}16"
+ "{HDGuardedData=\"scores\"{SimdVector<float __attribute__((ext_vector_type(8))), float>=\"chunks\"{vector<float __attribute__((ext_vector_type(8))), (anonymous namespace)::SimdAlignedAllocator<float __attribute__((ext_vector_type(8)))>>=\"__begin_\"^\"__end_\"^\"__cap_\"^}\"count\"Q}\"abs\"{SimdVector<int __attribute__((ext_vector_type(8))), unsigned int>=\"chunks\"{vector<int __attribute__((ext_vector_type(8))), (anonymous namespace)::SimdAlignedAllocator<int __attribute__((ext_vector_type(8)))>>=\"__begin_\"^\"__end_\"^\"__cap_\"^}\"count\"Q}\"enumerationInProgress\"B}"
+ "{unique_ptr<proactive::pas::SynchronizedObject<(anonymous namespace)::HDGuardedData, proactive::pas::detail::RecursiveMutex>, std::default_delete<proactive::pas::SynchronizedObject<(anonymous namespace)::HDGuardedData, proactive::pas::detail::RecursiveMutex>>>=\"__ptr_\"^v}"
- "PAS : Current process is %@ Target process is %@"
- "PAS: Inside _PAS callback"
- "PAS: Resetting log"
- "Ran MobileKeyBag class C unlock block: %@"
- "Running MobileKeyBag class C unlock block: %@"
- "_PAS Telemetry : Sending"
- "v24@0:8r^{_PASDeviceStateSystemCallbacks=^?^?^?^?^?^?^?^?^?}16"
- "{HDGuardedData=\"scores\"{SimdVector<float __attribute__((ext_vector_type(8))), float>=\"chunks\"{vector<float __attribute__((ext_vector_type(8))), (anonymous namespace)::SimdAlignedAllocator<float __attribute__((ext_vector_type(8)))>>=\"__begin_\"^\"__end_\"^\"__end_cap_\"{__compressed_pair<float * __attribute__((ext_vector_type(8))), (anonymous namespace)::SimdAlignedAllocator<float __attribute__((ext_vector_type(8)))>>=\"__value_\"^}}\"count\"Q}\"abs\"{SimdVector<int __attribute__((ext_vector_type(8))), unsigned int>=\"chunks\"{vector<int __attribute__((ext_vector_type(8))), (anonymous namespace)::SimdAlignedAllocator<int __attribute__((ext_vector_type(8)))>>=\"__begin_\"^\"__end_\"^\"__end_cap_\"{__compressed_pair<int * __attribute__((ext_vector_type(8))), (anonymous namespace)::SimdAlignedAllocator<int __attribute__((ext_vector_type(8)))>>=\"__value_\"^}}\"count\"Q}\"enumerationInProgress\"B}"
- "{unique_ptr<proactive::pas::SynchronizedObject<(anonymous namespace)::HDGuardedData, proactive::pas::detail::RecursiveMutex>, std::default_delete<proactive::pas::SynchronizedObject<(anonymous namespace)::HDGuardedData, proactive::pas::detail::RecursiveMutex>>>=\"__ptr_\"{__compressed_pair<proactive::pas::SynchronizedObject<(anonymous namespace)::HDGuardedData, proactive::pas::detail::RecursiveMutex> *, std::default_delete<proactive::pas::SynchronizedObject<(anonymous namespace)::HDGuardedData, proactive::pas::detail::RecursiveMutex>>>=\"__value_\"^v}}"
- "\x88"

```
