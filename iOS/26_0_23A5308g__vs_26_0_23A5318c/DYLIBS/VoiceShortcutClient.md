## VoiceShortcutClient

> `/System/Library/PrivateFrameworks/VoiceShortcutClient.framework/VoiceShortcutClient`

```diff

-4032.1.0.0.0
-  __TEXT.__text: 0x12c5c0
-  __TEXT.__auth_stubs: 0x3510
-  __TEXT.__objc_methlist: 0xc30c
-  __TEXT.__const: 0xbba8
+4033.0.3.4.0
+  __TEXT.__text: 0x12db8c
+  __TEXT.__auth_stubs: 0x35d0
+  __TEXT.__objc_methlist: 0xc434
+  __TEXT.__const: 0xbbd8
   __TEXT.__dlopen_cstrs: 0xdb4
-  __TEXT.__cstring: 0x1768f
-  __TEXT.__swift5_typeref: 0x2c97
+  __TEXT.__cstring: 0x17732
+  __TEXT.__swift5_typeref: 0x2caf
   __TEXT.__swift5_reflstr: 0x11fa
   __TEXT.__swift5_assocty: 0x360
   __TEXT.__constg_swiftt: 0x2c58

   __TEXT.__swift5_mpenum: 0x74
   __TEXT.__oslogstring: 0x395b
   __TEXT.__swift5_protos: 0x30
-  __TEXT.__gcc_except_tab: 0x1a6c
+  __TEXT.__gcc_except_tab: 0x1be0
   __TEXT.__ustring: 0x14e
-  __TEXT.__unwind_info: 0x5d70
-  __TEXT.__eh_frame: 0x5160
-  __TEXT.__objc_classname: 0x22e6
-  __TEXT.__objc_methname: 0x1b85c
-  __TEXT.__objc_methtype: 0x47cb
-  __TEXT.__objc_stubs: 0x11900
-  __DATA_CONST.__got: 0x1168
-  __DATA_CONST.__const: 0x3410
-  __DATA_CONST.__objc_classlist: 0x920
+  __TEXT.__unwind_info: 0x5dd0
+  __TEXT.__eh_frame: 0x5100
+  __TEXT.__objc_classname: 0x230b
+  __TEXT.__objc_methname: 0x1bb20
+  __TEXT.__objc_methtype: 0x482e
+  __TEXT.__objc_stubs: 0x11a00
+  __DATA_CONST.__got: 0x11a0
+  __DATA_CONST.__const: 0x3438
+  __DATA_CONST.__objc_classlist: 0x930
   __DATA_CONST.__objc_catlist: 0xc0
   __DATA_CONST.__objc_protolist: 0x170
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x5c10
+  __DATA_CONST.__objc_selrefs: 0x5c90
   __DATA_CONST.__objc_protorefs: 0x98
-  __DATA_CONST.__objc_superrefs: 0x780
+  __DATA_CONST.__objc_superrefs: 0x790
   __DATA_CONST.__objc_arraydata: 0x1a00
-  __AUTH_CONST.__auth_got: 0x1a98
+  __AUTH_CONST.__auth_got: 0x1b00
   __AUTH_CONST.__const: 0x7c08
-  __AUTH_CONST.__cfstring: 0x18620
-  __AUTH_CONST.__objc_const: 0x18cd0
+  __AUTH_CONST.__cfstring: 0x18660
+  __AUTH_CONST.__objc_const: 0x19070
   __AUTH_CONST.__objc_intobj: 0x4998
   __AUTH_CONST.__objc_arrayobj: 0x150
   __AUTH_CONST.__objc_dictobj: 0x208
-  __AUTH.__objc_data: 0x39f0
-  __AUTH.__data: 0x1a50
-  __DATA.__objc_ivar: 0xc40
-  __DATA.__data: 0x3718
+  __AUTH.__objc_data: 0x3a90
+  __AUTH.__data: 0x1a40
+  __DATA.__objc_ivar: 0xc78
+  __DATA.__data: 0x3758
   __DATA.__bss: 0x143e8
   __DATA.__common: 0x28
   __DATA_DIRTY.__objc_data: 0x21e8

   - /System/Library/PrivateFrameworks/SpringBoardServices.framework/SpringBoardServices
   - /usr/lib/libMobileGestalt.dylib
   - /usr/lib/libSystem.B.dylib
+  - /usr/lib/libc++.1.dylib
   - /usr/lib/libobjc.A.dylib
   - /usr/lib/swift/libswiftAccelerate.dylib
   - /usr/lib/swift/libswiftCompression.dylib

   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  UUID: 03D800D1-3253-3D01-AAB2-EF4D265275AC
-  Functions: 9131
-  Symbols:   18769
-  CStrings:  12523
+  UUID: 7CF5E15F-5D9D-3D7C-BB32-55803BB5615F
+  Functions: 9138
+  Symbols:   18898
+  CStrings:  12575
 
Symbols:
+ -[WFDebouncer .cxx_destruct]
+ -[WFDebouncer addTarget:action:]
+ -[WFDebouncer dealloc]
+ -[WFDebouncer delay]
+ -[WFDebouncer fire]
+ -[WFDebouncer firingReasons]
+ -[WFDebouncer initWithDelay:maximumDelay:queue:]
+ -[WFDebouncer initWithDelay:maximumDelay:queue:userInfo:unboundedFiringReasons:]
+ -[WFDebouncer initWithDelay:queue:]
+ -[WFDebouncer isPendingFire]
+ -[WFDebouncer maximumDelay]
+ -[WFDebouncer pokeWithReason:userInfo:]
+ -[WFDebouncer poke]
+ -[WFDebouncer removeTarget:action:]
+ -[WFDebouncer resetDelayTimer]
+ -[WFDebouncer setPendingFire:]
+ -[WFDebouncer unboundedFiringReasons]
+ -[WFDebouncer userInfo]
+ -[WFDebouncerPokeReason .cxx_destruct]
+ -[WFDebouncerPokeReason reason]
+ -[WFDebouncerPokeReason setReason:]
+ -[WFDebouncerPokeReason setUserInfo:]
+ -[WFDebouncerPokeReason userInfo]
+ GCC_except_table3483
+ GCC_except_table3484
+ GCC_except_table3485
+ GCC_except_table3486
+ GCC_except_table3491
+ GCC_except_table3492
+ GCC_except_table3497
+ GCC_except_table3498
+ GCC_except_table3499
+ GCC_except_table3501
+ GCC_except_table3541
+ GCC_except_table3631
+ GCC_except_table3660
+ GCC_except_table3661
+ GCC_except_table3662
+ GCC_except_table3867
+ GCC_except_table3874
+ GCC_except_table3877
+ GCC_except_table3880
+ GCC_except_table3882
+ GCC_except_table3890
+ GCC_except_table3995
+ GCC_except_table3999
+ GCC_except_table4012
+ GCC_except_table4119
+ GCC_except_table4203
+ GCC_except_table4206
+ GCC_except_table4209
+ GCC_except_table4212
+ GCC_except_table4215
+ GCC_except_table4220
+ GCC_except_table4224
+ GCC_except_table4227
+ GCC_except_table4229
+ GCC_except_table4232
+ GCC_except_table4235
+ GCC_except_table4242
+ GCC_except_table4247
+ GCC_except_table4252
+ GCC_except_table4268
+ GCC_except_table4272
+ GCC_except_table4284
+ GCC_except_table4316
+ _BiomeLibraryLibraryCore.frameworkLibrary.20332
+ _ContentKitLibrary.18921
+ _ContentKitLibraryCore.frameworkLibrary.18932
+ _NSSelectorFromString
+ _OBJC_CLASS_$_NSMapTable
+ _OBJC_CLASS_$_WFDebouncer
+ _OBJC_CLASS_$_WFDebouncerPokeReason
+ _OBJC_IVAR_$_WFDebouncer._delay
+ _OBJC_IVAR_$_WFDebouncer._delayTimer
+ _OBJC_IVAR_$_WFDebouncer._firingReasons
+ _OBJC_IVAR_$_WFDebouncer._firingReasonsQueue
+ _OBJC_IVAR_$_WFDebouncer._maximumDelay
+ _OBJC_IVAR_$_WFDebouncer._maximumDelayTimer
+ _OBJC_IVAR_$_WFDebouncer._pendingFire
+ _OBJC_IVAR_$_WFDebouncer._queue
+ _OBJC_IVAR_$_WFDebouncer._targetTable
+ _OBJC_IVAR_$_WFDebouncer._transaction
+ _OBJC_IVAR_$_WFDebouncer._unboundedFiringReasons
+ _OBJC_IVAR_$_WFDebouncer._userInfo
+ _OBJC_IVAR_$_WFDebouncerPokeReason._reason
+ _OBJC_IVAR_$_WFDebouncerPokeReason._userInfo
+ _OBJC_METACLASS_$_WFDebouncer
+ _OBJC_METACLASS_$_WFDebouncerPokeReason
+ _UIKitLibrary.19444
+ _UIKitLibraryCore.frameworkLibrary.18957
+ _UIKitLibraryCore.frameworkLibrary.19454
+ __OBJC_$_INSTANCE_METHODS_WFDebouncer
+ __OBJC_$_INSTANCE_METHODS_WFDebouncerPokeReason
+ __OBJC_$_INSTANCE_VARIABLES_WFDebouncer
+ __OBJC_$_INSTANCE_VARIABLES_WFDebouncerPokeReason
+ __OBJC_$_PROP_LIST_WFDebouncer
+ __OBJC_$_PROP_LIST_WFDebouncerPokeReason
+ __OBJC_CLASS_RO_$_WFDebouncer
+ __OBJC_CLASS_RO_$_WFDebouncerPokeReason
+ __OBJC_METACLASS_RO_$_WFDebouncer
+ __OBJC_METACLASS_RO_$_WFDebouncerPokeReason
+ __ZNSt20bad_array_new_lengthC1Ev
+ __ZNSt20bad_array_new_lengthD1Ev
+ __ZNSt3__114__split_bufferIPU8__strongP21WFDebouncerPokeReasonNS_9allocatorIS4_EEE12emplace_backIJRS4_EEEvDpOT_
+ __ZNSt3__119__allocate_at_leastB8ne200100INS_9allocatorIPU8__strongP21WFDebouncerPokeReasonEEEENS_19__allocation_resultINS_16allocator_traitsIT_E7pointerEEERS9_m
+ __ZNSt3__15dequeIU8__strongP21WFDebouncerPokeReasonNS_9allocatorIS3_EEE9pop_frontEv
+ __ZNSt3__15dequeIU8__strongP21WFDebouncerPokeReasonNS_9allocatorIS3_EEED2B8ne200100Ev
+ __ZSt28__throw_bad_array_new_lengthB8ne200100v
+ __ZTISt20bad_array_new_length
+ __ZdlPv
+ __ZdlPvSt19__type_descriptor_t
+ __ZnwmSt19__type_descriptor_t
+ ___19-[WFDebouncer poke]_block_invoke
+ ___32-[WFDebouncer addTarget:action:]_block_invoke
+ ___32-[WFDebouncer restartDelayTimer]_block_invoke
+ ___35-[WFDebouncer removeTarget:action:]_block_invoke
+ ___39-[WFDebouncer pokeWithReason:userInfo:]_block_invoke
+ ___48-[WFDebouncer startMaximumDelayTimerIfNecessary]_block_invoke
+ ___BiomeLibraryLibraryCore_block_invoke.20333
+ ___Block_byref_object_copy_.18941
+ ___Block_byref_object_copy_.20872
+ ___Block_byref_object_dispose_.18942
+ ___Block_byref_object_dispose_.20873
+ ___ContentKitLibraryCore_block_invoke.18933
+ ___UIKitLibraryCore_block_invoke.18958
+ ___UIKitLibraryCore_block_invoke.19455
+ ___block_descriptor_40_ea8_32s_e5_v8?0ls32l8
+ ___block_descriptor_48_ea8_32s40s_e5_v8?0ls32l8s40l8
+ ___block_descriptor_56_ea8_32s40s_e5_v8?0ls32l8s40l8
+ ___block_literal_global.17479
+ ___block_literal_global.18111
+ ___block_literal_global.18173
+ ___block_literal_global.185.20877
+ ___block_literal_global.18951
+ ___block_literal_global.19001
+ ___block_literal_global.19012
+ ___block_literal_global.19270
+ ___block_literal_global.194.20870
+ ___block_literal_global.19531
+ ___block_literal_global.20012
+ ___block_literal_global.20200
+ ___block_literal_global.21023
+ ___block_literal_global.50.17760
+ ___cxa_allocate_exception
+ ___cxa_throw
+ ___getBiomeLibrarySymbolLoc_block_invoke.20323
+ ___getWFContentItemClass_block_invoke.18945
+ ___getWFStringContentItemClass_block_invoke.18920
+ ___gxx_personality_v0
+ ___unnamed_16
+ _audit_stringBiomeLibrary.20337
+ _audit_stringContentKit.18938
+ _audit_stringUIKit.18961
+ _audit_stringUIKit.19458
+ _block_copy_helper.226
+ _block_descriptor.228
+ _block_destroy_helper.227
+ _dispatch_activate
+ _getBiomeLibrarySymbolLoc.ptr.20322
+ _getWFContentItemClass.softClass.18944
+ _getWFStringContentItemClass.softClass.18919
+ _objc_msgSend$daemonProvider
+ _objc_msgSend$delay
+ _objc_msgSend$fire
+ _objc_msgSend$initWithDelay:maximumDelay:queue:
+ _objc_msgSend$initWithDelay:maximumDelay:queue:userInfo:unboundedFiringReasons:
+ _objc_msgSend$maximumDelay
+ _objc_msgSend$poke
+ _objc_msgSend$unboundedFiringReasons
+ _objc_msgSend$weakToStrongObjectsMapTable
+ _os_transaction_create
+ _os_transaction_needs_more_time
+ _symbolic Say_____G So18OS_dispatch_sourceC8DispatchE19MemoryPressureEventV
+ _symbolic _____y_____G s23_ContiguousArrayStorageC So18OS_dispatch_sourceC8DispatchE19MemoryPressureEventV
- GCC_except_table3507
- GCC_except_table3597
- GCC_except_table3626
- GCC_except_table3627
- GCC_except_table3628
- GCC_except_table3833
- GCC_except_table3840
- GCC_except_table3843
- GCC_except_table3846
- GCC_except_table3848
- GCC_except_table3856
- GCC_except_table3961
- GCC_except_table3965
- GCC_except_table3978
- GCC_except_table4085
- GCC_except_table4135
- GCC_except_table4164
- GCC_except_table4172
- GCC_except_table4175
- GCC_except_table4178
- GCC_except_table4181
- GCC_except_table4186
- GCC_except_table4190
- GCC_except_table4193
- GCC_except_table4195
- GCC_except_table4201
- GCC_except_table4208
- GCC_except_table4213
- GCC_except_table4218
- GCC_except_table4234
- GCC_except_table4238
- GCC_except_table4250
- GCC_except_table4282
- _BiomeLibraryLibraryCore.frameworkLibrary.20232
- _ContentKitLibrary.18822
- _ContentKitLibraryCore.frameworkLibrary.18833
- _UIKitLibrary.19345
- _UIKitLibraryCore.frameworkLibrary.18858
- _UIKitLibraryCore.frameworkLibrary.19355
- ___BiomeLibraryLibraryCore_block_invoke.20233
- ___Block_byref_object_copy_.18842
- ___Block_byref_object_copy_.20772
- ___Block_byref_object_dispose_.18843
- ___Block_byref_object_dispose_.20773
- ___ContentKitLibraryCore_block_invoke.18834
- ___UIKitLibraryCore_block_invoke.18859
- ___UIKitLibraryCore_block_invoke.19356
- ___block_descriptor_40_e8_32s_e5_v8?0ls32l8
- ___block_descriptor_48_e8_32s40s_e5_v8?0ls32l8s40l8
- ___block_literal_global.17380
- ___block_literal_global.18012
- ___block_literal_global.18074
- ___block_literal_global.185.20777
- ___block_literal_global.18852
- ___block_literal_global.18902
- ___block_literal_global.18913
- ___block_literal_global.19171
- ___block_literal_global.194.20770
- ___block_literal_global.19432
- ___block_literal_global.19912
- ___block_literal_global.20100
- ___block_literal_global.20923
- ___block_literal_global.50.17661
- ___getBiomeLibrarySymbolLoc_block_invoke.20223
- ___getWFContentItemClass_block_invoke.18846
- ___getWFStringContentItemClass_block_invoke.18821
- ___unnamed_15
- ___unnamed_20
- _audit_stringBiomeLibrary.20237
- _audit_stringContentKit.18839
- _audit_stringUIKit.18862
- _audit_stringUIKit.19359
- _block_copy_helper.229
- _block_descriptor.231
- _block_destroy_helper.230
- _getBiomeLibrarySymbolLoc.ptr.20222
- _getWFContentItemClass.softClass.18845
- _getWFStringContentItemClass.softClass.18820
- _objc_msgSend$sharedProvider
CStrings:
+ "!&"
+ "@\"NSMapTable\""
+ "@\"NSObject<OS_os_transaction>\""
+ "@40@0:8d16d24@32"
+ "@52@0:8d16d24@32@40B48"
+ "T@\"NSArray\",R,N,V_firingReasons"
+ "T@\"NSString\",C,N,V_reason"
+ "T@,&,N,V_userInfo"
+ "T@,R,N,V_userInfo"
+ "TB,R,N,GisPendingFire"
+ "TB,R,N,V_unboundedFiringReasons"
+ "Td,R,N,V_delay"
+ "Td,R,N,V_maximumDelay"
+ "WFDebouncer"
+ "WFDebouncer.mm"
+ "WFDebouncerPokeReason"
+ "_delay"
+ "_delayTimer"
+ "_firingReasons"
+ "_firingReasonsQueue"
+ "_maximumDelay"
+ "_maximumDelayTimer"
+ "_pendingFire"
+ "_queue"
+ "_targetTable"
+ "_transaction"
+ "_unboundedFiringReasons"
+ "addTarget:action:"
+ "cachePurgeDebouncer"
+ "cachePurgeDispatchQueue"
+ "cachePurgeDispatchSource"
+ "cachePurgeNotificationObserver"
+ "com.apple.shortcuts.WFDebouncer"
+ "com.apple.shortcuts.WFDebouncer.pending-fire"
+ "com.apple.shortcuts.appIntentsMetadataProvider.cachePurge"
+ "daemonProvider"
+ "delay"
+ "firingReasons"
+ "initWithDelay:maximumDelay:queue:"
+ "initWithDelay:maximumDelay:queue:userInfo:unboundedFiringReasons:"
+ "initWithDelay:queue:"
+ "initWithMetadataProvider:cacheLifetime:"
+ "isPendingFire"
+ "maximumDelay"
+ "pendingFire"
+ "poke"
+ "pokeWithReason:userInfo:"
+ "removeTarget:action:"
+ "setReason:"
+ "target"
+ "unboundedFiringReasons"
+ "v32@0:8@16:24"
+ "weakToStrongObjectsMapTable"
- "com.apple.shortcuts.appIntentsMetadataProvider.memoryPressure"
- "memoryPressureDispatchQueue"
- "memoryPressureDispatchSource"
- "notificationObserver"

```
