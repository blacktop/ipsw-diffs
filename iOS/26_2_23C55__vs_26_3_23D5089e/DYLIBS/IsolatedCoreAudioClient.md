## IsolatedCoreAudioClient

> `/System/Library/PrivateFrameworks/IsolatedCoreAudioClient.framework/IsolatedCoreAudioClient`

```diff

-7.32.300.0.0
-  __TEXT.__text: 0x1bc5c
-  __TEXT.__auth_stubs: 0xa60
-  __TEXT.__objc_methlist: 0x884
-  __TEXT.__const: 0x282d
-  __TEXT.__gcc_except_tab: 0x1dc8
-  __TEXT.__cstring: 0x962
-  __TEXT.__oslogstring: 0x2b53
-  __TEXT.__unwind_info: 0xf58
-  __TEXT.__objc_classname: 0x213
-  __TEXT.__objc_methname: 0x10ed
-  __TEXT.__objc_methtype: 0xbfb
-  __TEXT.__objc_stubs: 0xbc0
-  __DATA_CONST.__got: 0x108
-  __DATA_CONST.__const: 0x1d0
+7.32.404.0.0
+  __TEXT.__text: 0x1b530
+  __TEXT.__auth_stubs: 0xa50
+  __TEXT.__objc_methlist: 0x7ec
+  __TEXT.__const: 0x2408
+  __TEXT.__gcc_except_tab: 0x1d50
+  __TEXT.__cstring: 0xb7b
+  __TEXT.__oslogstring: 0x2cc2
+  __TEXT.__unwind_info: 0xe08
+  __TEXT.__objc_classname: 0x1d0
+  __TEXT.__objc_methname: 0x10fe
+  __TEXT.__objc_methtype: 0xa32
+  __TEXT.__objc_stubs: 0xd60
+  __DATA_CONST.__got: 0x118
+  __DATA_CONST.__const: 0x238
   __DATA_CONST.__objc_classlist: 0x48
   __DATA_CONST.__objc_catlist: 0x8
-  __DATA_CONST.__objc_protolist: 0x48
+  __DATA_CONST.__objc_protolist: 0x38
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x488
-  __DATA_CONST.__objc_protorefs: 0x28
+  __DATA_CONST.__objc_selrefs: 0x4d8
+  __DATA_CONST.__objc_protorefs: 0x18
   __DATA_CONST.__objc_superrefs: 0x48
-  __AUTH_CONST.__auth_got: 0x540
-  __AUTH_CONST.__const: 0x24c0
-  __AUTH_CONST.__cfstring: 0x1c0
-  __AUTH_CONST.__objc_const: 0xda8
-  __DATA.__objc_ivar: 0x64
-  __DATA.__data: 0x360
-  __DATA.__bss: 0x218
-  __DATA_DIRTY.__objc_data: 0x2d0
-  __DATA_DIRTY.__bss: 0x20
+  __AUTH_CONST.__auth_got: 0x538
+  __AUTH_CONST.__const: 0x1f38
+  __AUTH_CONST.__cfstring: 0x280
+  __AUTH_CONST.__objc_const: 0xcb8
+  __AUTH_CONST.__objc_intobj: 0x18
+  __AUTH.__objc_data: 0x50
+  __DATA.__objc_ivar: 0x54
+  __DATA.__data: 0x2a0
+  __DATA.__bss: 0x2a8
+  __DATA_DIRTY.__objc_data: 0x280
+  __DATA_DIRTY.__bss: 0x10
   - /System/Library/Frameworks/CoreAudio.framework/CoreAudio
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/Foundation.framework/Foundation
+  - /System/Library/PrivateFrameworks/SoftLinking.framework/SoftLinking
   - /System/Library/PrivateFrameworks/Tightbeam.framework/Tightbeam
   - /System/Library/PrivateFrameworks/caulk.framework/caulk
   - /usr/lib/libMobileGestalt.dylib

   - /usr/lib/libbsm.0.dylib
   - /usr/lib/libc++.1.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: E11B8140-8196-388E-A802-86F4D2930A6E
-  Functions: 877
-  Symbols:   2850
-  CStrings:  539
+  UUID: C6ED6732-F799-380C-82BE-7AD8BDEEDFFB
+  Functions: 780
+  Symbols:   2606
+  CStrings:  559
 
Symbols:
+ +[TraceManager tailspinDumpOptions]
+ -[TraceManager clearDirectory]
+ -[TraceManager dumpTailspin:]
+ -[TraceManager dumpTailspinAsync:]
+ -[TraceManager init]
+ -[TraceManager setDefaultConfig]
+ -[TraceManager setTestConfig]
+ GCC_except_table110
+ GCC_except_table119
+ GCC_except_table120
+ GCC_except_table121
+ GCC_except_table122
+ GCC_except_table123
+ GCC_except_table130
+ GCC_except_table142
+ GCC_except_table144
+ GCC_except_table146
+ GCC_except_table147
+ GCC_except_table151
+ GCC_except_table153
+ GCC_except_table164
+ GCC_except_table167
+ GCC_except_table168
+ GCC_except_table185
+ GCC_except_table187
+ GCC_except_table189
+ GCC_except_table191
+ GCC_except_table194
+ GCC_except_table201
+ GCC_except_table204
+ GCC_except_table205
+ GCC_except_table216
+ GCC_except_table218
+ GCC_except_table227
+ GCC_except_table231
+ GCC_except_table234
+ GCC_except_table240
+ GCC_except_table241
+ GCC_except_table243
+ GCC_except_table244
+ GCC_except_table254
+ GCC_except_table280
+ GCC_except_table282
+ GCC_except_table284
+ GCC_except_table30
+ GCC_except_table301
+ GCC_except_table316
+ GCC_except_table322
+ GCC_except_table325
+ GCC_except_table327
+ GCC_except_table33
+ GCC_except_table332
+ GCC_except_table339
+ GCC_except_table341
+ GCC_except_table342
+ GCC_except_table343
+ GCC_except_table344
+ GCC_except_table345
+ GCC_except_table346
+ GCC_except_table35
+ GCC_except_table36
+ GCC_except_table367
+ GCC_except_table37
+ GCC_except_table372
+ GCC_except_table38
+ GCC_except_table393
+ GCC_except_table40
+ GCC_except_table402
+ GCC_except_table404
+ GCC_except_table405
+ GCC_except_table406
+ GCC_except_table408
+ GCC_except_table412
+ GCC_except_table416
+ GCC_except_table419
+ GCC_except_table426
+ GCC_except_table43
+ GCC_except_table432
+ GCC_except_table463
+ GCC_except_table466
+ GCC_except_table476
+ GCC_except_table477
+ GCC_except_table501
+ GCC_except_table545
+ GCC_except_table549
+ GCC_except_table570
+ GCC_except_table571
+ GCC_except_table580
+ GCC_except_table581
+ GCC_except_table593
+ GCC_except_table603
+ GCC_except_table645
+ GCC_except_table648
+ GCC_except_table652
+ GCC_except_table654
+ GCC_except_table66
+ GCC_except_table661
+ GCC_except_table665
+ GCC_except_table667
+ GCC_except_table668
+ GCC_except_table675
+ GCC_except_table69
+ GCC_except_table690
+ GCC_except_table691
+ GCC_except_table692
+ GCC_except_table694
+ GCC_except_table695
+ GCC_except_table701
+ GCC_except_table702
+ GCC_except_table703
+ GCC_except_table705
+ GCC_except_table706
+ GCC_except_table709
+ GCC_except_table715
+ GCC_except_table719
+ GCC_except_table721
+ GCC_except_table733
+ GCC_except_table74
+ GCC_except_table755
+ GCC_except_table756
+ GCC_except_table760
+ GCC_except_table766
+ GCC_except_table776
+ GCC_except_table778
+ GCC_except_table781
+ GCC_except_table782
+ GCC_except_table86
+ GCC_except_table90
+ GCC_except_table93
+ GCC_except_table95
+ GCC_except_table97
+ _NSFilePosixPermissions
+ _NSTemporaryDirectory
+ _OBJC_CLASS_$_NSConstantIntegerNumber
+ _OBJC_CLASS_$_NSDate
+ _OBJC_CLASS_$_NSDateFormatter
+ _OBJC_CLASS_$_NSDictionary
+ _OBJC_CLASS_$_NSFileManager
+ _OBJC_CLASS_$_NSString
+ _OBJC_CLASS_$_TraceManager
+ _OBJC_METACLASS_$_TraceManager
+ __OBJC_$_CLASS_METHODS_TraceManager
+ __OBJC_$_INSTANCE_METHODS_TraceManager
+ __OBJC_CLASS_RO_$_TraceManager
+ __OBJC_METACLASS_RO_$_TraceManager
+ __ZGVZL27sIsolatedCoreAudioClientLogvE4sLog.104
+ __ZGVZL27sIsolatedCoreAudioClientLogvE4sLog.1137
+ __ZGVZL27sIsolatedCoreAudioClientLogvE4sLog.155
+ __ZGVZL27sIsolatedCoreAudioClientLogvE4sLog.169
+ __ZGVZL27sIsolatedCoreAudioClientLogvE4sLog.195
+ __ZGVZL27sIsolatedCoreAudioClientLogvE4sLog.253
+ __ZGVZL27sIsolatedCoreAudioClientLogvE4sLog.38
+ __ZGVZL27sIsolatedCoreAudioClientLogvE4sLog.504
+ __ZGVZL27sIsolatedCoreAudioClientLogvE4sLog.599
+ __ZGVZL27sIsolatedCoreAudioClientLogvE4sLog.685
+ __ZGVZL27sIsolatedCoreAudioClientLogvE4sLog.767
+ __ZGVZL27sIsolatedCoreAudioServerLogvE4sLog.138
+ __ZGVZL27sIsolatedCoreAudioServerLogvE4sLog.235
+ __ZGVZL27sIsolatedCoreAudioServerLogvE4sLog.289
+ __ZGVZL27sIsolatedCoreAudioServerLogvE4sLog.333
+ __ZGVZL27sIsolatedCoreAudioServerLogvE4sLog.644
+ __ZGVZL27sIsolatedCoreAudioServerLogvE4sLog.942
+ __ZGVZL27sIsolatedCoreAudioSiphonLogvE4sLog.406
+ __ZGVZL27sIsolatedCoreAudioSiphonLogvE4sLog.462
+ __ZGVZL27sIsolatedCoreAudioSiphonLogvE4sLog.727
+ __ZL18libtailspinLibraryv
+ __ZL22libtailspinLibraryCorePPc
+ __ZL25soft_tailspin_config_freeP15tailspin_config
+ __ZL27sIsolatedCoreAudioClientLogv.1134
+ __ZL27sIsolatedCoreAudioClientLogv.150
+ __ZL27sIsolatedCoreAudioClientLogv.165
+ __ZL27sIsolatedCoreAudioClientLogv.191
+ __ZL27sIsolatedCoreAudioClientLogv.250
+ __ZL27sIsolatedCoreAudioClientLogv.501
+ __ZL27sIsolatedCoreAudioClientLogv.593
+ __ZL27sIsolatedCoreAudioClientLogv.682
+ __ZL27sIsolatedCoreAudioClientLogv.761
+ __ZL27sIsolatedCoreAudioClientLogv.97
+ __ZL27sIsolatedCoreAudioServerLogv.131
+ __ZL27sIsolatedCoreAudioServerLogv.287
+ __ZL27sIsolatedCoreAudioServerLogv.328
+ __ZL27sIsolatedCoreAudioServerLogv.939
+ __ZL27sIsolatedCoreAudioSiphonLogv.403
+ __ZL27sIsolatedCoreAudioSiphonLogv.459
+ __ZL27sIsolatedCoreAudioSiphonLogv.724
+ __ZL31soft_tailspin_config_apply_syncP15tailspin_config
+ __ZN16ICACFeatureFlags25allow_ferryerror_spindumpEv
+ __ZNSt3__110unique_ptrI19TraceManagerWrapperNS_14default_deleteIS1_EEE5resetB8ne200100EPS1_
+ __ZNSt3__110unique_ptrI21SingleUseTraceManagerNS_14default_deleteIS1_EEE5resetB8ne200100EPS1_
+ __ZNSt3__117__call_once_proxyB8ne200100INS_5tupleIJOZN16ICACFeatureFlags25allow_ferryerror_spindumpEvE3$_0EEEEEvPv
+ __ZZL22libtailspinLibraryCorePPcE16frameworkLibrary.0
+ __ZZL27sIsolatedCoreAudioClientLogvE4sLog.107
+ __ZZL27sIsolatedCoreAudioClientLogvE4sLog.1138
+ __ZZL27sIsolatedCoreAudioClientLogvE4sLog.158
+ __ZZL27sIsolatedCoreAudioClientLogvE4sLog.172
+ __ZZL27sIsolatedCoreAudioClientLogvE4sLog.198
+ __ZZL27sIsolatedCoreAudioClientLogvE4sLog.254
+ __ZZL27sIsolatedCoreAudioClientLogvE4sLog.41
+ __ZZL27sIsolatedCoreAudioClientLogvE4sLog.507
+ __ZZL27sIsolatedCoreAudioClientLogvE4sLog.602
+ __ZZL27sIsolatedCoreAudioClientLogvE4sLog.688
+ __ZZL27sIsolatedCoreAudioClientLogvE4sLog.768
+ __ZZL27sIsolatedCoreAudioServerLogvE4sLog.139
+ __ZZL27sIsolatedCoreAudioServerLogvE4sLog.238
+ __ZZL27sIsolatedCoreAudioServerLogvE4sLog.290
+ __ZZL27sIsolatedCoreAudioServerLogvE4sLog.336
+ __ZZL27sIsolatedCoreAudioServerLogvE4sLog.647
+ __ZZL27sIsolatedCoreAudioServerLogvE4sLog.945
+ __ZZL27sIsolatedCoreAudioSiphonLogvE4sLog.407
+ __ZZL27sIsolatedCoreAudioSiphonLogvE4sLog.465
+ __ZZL27sIsolatedCoreAudioSiphonLogvE4sLog.730
+ __ZZL32gettailspin_config_freeSymbolLocvE3ptr.0
+ __ZZL32gettailspin_enabled_setSymbolLocvE3ptr.0
+ __ZZL36gettailspin_buffer_size_setSymbolLocvE3ptr.0
+ __ZZL38getTSPDumpOptions_SymbolicateSymbolLocvE3ptr.0
+ __ZZL38gettailspin_config_apply_syncSymbolLocvE3ptr.0
+ __ZZL39getTSPDumpOptions_ReasonStringSymbolLocvE3ptr.0
+ __ZZL40getTSPDumpOptions_CollectOsLogsSymbolLocvE3ptr.0
+ __ZZL40getTSPDumpOptions_CollectTrialsSymbolLocvE3ptr.0
+ __ZZL45getTSPDumpOptions_CollectOsSignpostsSymbolLocvE3ptr.0
+ __ZZL45gettailspin_dump_output_with_optionsSymbolLocvE3ptr.0
+ __ZZL45gettailspin_full_sampling_period_setSymbolLocvE3ptr.0
+ __ZZL45gettailspin_kdbg_filter_subclass_setSymbolLocvE3ptr.0
+ __ZZL47getTSPDumpOptions_CollectAriadnePlistsSymbolLocvE3ptr.0
+ __ZZL47gettailspin_oncore_sampling_period_setSymbolLocvE3ptr.0
+ __ZZL50gettailspin_dump_output_with_options_syncSymbolLocvE3ptr.0
+ __ZZL53gettailspin_config_create_with_current_stateSymbolLocvE3ptr.0
+ __ZZL54gettailspin_config_create_with_default_configSymbolLocvE3ptr.0
+ __ZZN16ICACFeatureFlags25allow_ferryerror_spindumpEvE27s_allow_ferryerror_spindump
+ __ZZN16ICACFeatureFlags25allow_ferryerror_spindumpEvE4once
+ ___34-[TraceManager dumpTailspinAsync:]_block_invoke
+ ___Block_byref_object_copy_.200
+ ___Block_byref_object_dispose_.201
+ ____ZL22libtailspinLibraryCorePPc_block_invoke
+ ____ZL32gettailspin_config_freeSymbolLocv_block_invoke
+ ____ZL32gettailspin_enabled_setSymbolLocv_block_invoke
+ ____ZL36gettailspin_buffer_size_setSymbolLocv_block_invoke
+ ____ZL38getTSPDumpOptions_SymbolicateSymbolLocv_block_invoke
+ ____ZL38gettailspin_config_apply_syncSymbolLocv_block_invoke
+ ____ZL39getTSPDumpOptions_ReasonStringSymbolLocv_block_invoke
+ ____ZL40getTSPDumpOptions_CollectOsLogsSymbolLocv_block_invoke
+ ____ZL40getTSPDumpOptions_CollectTrialsSymbolLocv_block_invoke
+ ____ZL45getTSPDumpOptions_CollectOsSignpostsSymbolLocv_block_invoke
+ ____ZL45gettailspin_dump_output_with_optionsSymbolLocv_block_invoke
+ ____ZL45gettailspin_full_sampling_period_setSymbolLocv_block_invoke
+ ____ZL45gettailspin_kdbg_filter_subclass_setSymbolLocv_block_invoke
+ ____ZL47getTSPDumpOptions_CollectAriadnePlistsSymbolLocv_block_invoke
+ ____ZL47gettailspin_oncore_sampling_period_setSymbolLocv_block_invoke
+ ____ZL50gettailspin_dump_output_with_options_syncSymbolLocv_block_invoke
+ ____ZL53gettailspin_config_create_with_current_stateSymbolLocv_block_invoke
+ ____ZL54gettailspin_config_create_with_default_configSymbolLocv_block_invoke
+ ___block_descriptor_44_ea8_32s_e8_v12?0B8ls32l8
+ ___block_descriptor_48_ea8_32r_e5_v8?0lr32l8
+ ___block_descriptor_tmp.173
+ ___block_descriptor_tmp.466
+ ___block_literal_global.244
+ ___block_literal_global.419
+ ___kCFBooleanTrue
+ __os_feature_enabled_simple_impl
+ __sl_dlopen
+ _abort_report_np
+ _close
+ _dlerror
+ _dlsym
+ _free
+ _kdebug_trace
+ _objc_enumerationMutation
+ _objc_msgSend$UTF8String
+ _objc_msgSend$contentsOfDirectoryAtPath:error:
+ _objc_msgSend$countByEnumeratingWithState:objects:count:
+ _objc_msgSend$createDirectoryAtPath:withIntermediateDirectories:attributes:error:
+ _objc_msgSend$date
+ _objc_msgSend$defaultManager
+ _objc_msgSend$dictionaryWithObjects:forKeys:count:
+ _objc_msgSend$dumpTailspinAsync:
+ _objc_msgSend$initWithCString:
+ _objc_msgSend$removeItemAtPath:error:
+ _objc_msgSend$setDateFormat:
+ _objc_msgSend$setDefaultConfig
+ _objc_msgSend$setObject:forKeyedSubscript:
+ _objc_msgSend$stringByAppendingPathComponent:
+ _objc_msgSend$stringByReplacingOccurrencesOfString:withString:
+ _objc_msgSend$stringFromDate:
+ _objc_msgSend$stringWithFormat:
+ _objc_msgSend$tailspinDumpOptions
+ _objc_release_x26
+ _objc_release_x27
+ _objc_retainAutorelease
+ _objc_retain_x26
+ _open
- -[MADClientInterface .cxx_construct]
- -[MADClientInterface .cxx_destruct]
- -[MADClientInterface createClientReaper]
- -[MADClientInterface disableMicrophoneActivityDetection:]
- -[MADClientInterface enableMicrophoneActivityDetection:]
- -[MADClientInterface initForTest:]
- -[MADClientInterface init]
- -[MADClientInterface listenForMicrophoneActivity:reply:]
- -[MADClientInterface mMADMultiplexer]
- -[MADClientInterface mReverseConnections]
- -[MADClientInterface setMMADMultiplexer:]
- -[MADClientInterface setMReverseConnections:]
- -[MADClientInterface setupReverseConnection:]
- -[MADClientInterface stopListeningForMicrophoneActivity:]
- GCC_except_table103
- GCC_except_table107
- GCC_except_table116
- GCC_except_table125
- GCC_except_table126
- GCC_except_table127
- GCC_except_table129
- GCC_except_table134
- GCC_except_table136
- GCC_except_table148
- GCC_except_table152
- GCC_except_table154
- GCC_except_table155
- GCC_except_table158
- GCC_except_table159
- GCC_except_table161
- GCC_except_table17
- GCC_except_table172
- GCC_except_table175
- GCC_except_table18
- GCC_except_table184
- GCC_except_table19
- GCC_except_table193
- GCC_except_table195
- GCC_except_table197
- GCC_except_table199
- GCC_except_table20
- GCC_except_table202
- GCC_except_table209
- GCC_except_table21
- GCC_except_table212
- GCC_except_table213
- GCC_except_table22
- GCC_except_table224
- GCC_except_table226
- GCC_except_table235
- GCC_except_table247
- GCC_except_table248
- GCC_except_table249
- GCC_except_table250
- GCC_except_table251
- GCC_except_table252
- GCC_except_table262
- GCC_except_table288
- GCC_except_table290
- GCC_except_table300
- GCC_except_table309
- GCC_except_table324
- GCC_except_table333
- GCC_except_table335
- GCC_except_table338
- GCC_except_table340
- GCC_except_table349
- GCC_except_table351
- GCC_except_table352
- GCC_except_table353
- GCC_except_table354
- GCC_except_table355
- GCC_except_table358
- GCC_except_table375
- GCC_except_table380
- GCC_except_table401
- GCC_except_table410
- GCC_except_table411
- GCC_except_table414
- GCC_except_table415
- GCC_except_table42
- GCC_except_table434
- GCC_except_table45
- GCC_except_table46
- GCC_except_table47
- GCC_except_table48
- GCC_except_table482
- GCC_except_table484
- GCC_except_table488
- GCC_except_table489
- GCC_except_table49
- GCC_except_table491
- GCC_except_table494
- GCC_except_table497
- GCC_except_table504
- GCC_except_table509
- GCC_except_table510
- GCC_except_table52
- GCC_except_table541
- GCC_except_table544
- GCC_except_table554
- GCC_except_table555
- GCC_except_table556
- GCC_except_table558
- GCC_except_table579
- GCC_except_table62
- GCC_except_table623
- GCC_except_table627
- GCC_except_table646
- GCC_except_table656
- GCC_except_table657
- GCC_except_table658
- GCC_except_table659
- GCC_except_table672
- GCC_except_table673
- GCC_except_table674
- GCC_except_table683
- GCC_except_table688
- GCC_except_table698
- GCC_except_table707
- GCC_except_table720
- GCC_except_table730
- GCC_except_table764
- GCC_except_table771
- GCC_except_table786
- GCC_except_table787
- GCC_except_table788
- GCC_except_table790
- GCC_except_table791
- GCC_except_table793
- GCC_except_table797
- GCC_except_table798
- GCC_except_table799
- GCC_except_table801
- GCC_except_table802
- GCC_except_table804
- GCC_except_table805
- GCC_except_table81
- GCC_except_table811
- GCC_except_table815
- GCC_except_table817
- GCC_except_table853
- GCC_except_table854
- GCC_except_table858
- GCC_except_table864
- GCC_except_table874
- GCC_except_table876
- GCC_except_table879
- GCC_except_table880
- GCC_except_table92
- GCC_except_table96
- GCC_except_table99
- _AudioHardwareCreateAggregateDevice
- _AudioHardwareDestroyAggregateDevice
- _AudioObjectAddPropertyListener
- _AudioObjectGetPropertyDataSize
- _AudioObjectHasProperty
- _AudioObjectRemovePropertyListener
- _AudioObjectSetPropertyData
- _CFArrayCreate
- _CFDictionaryCreate
- _CFNumberCreate
- _CFRelease
- _CFRetain
- _CFStringCreateWithBytes
- _CFStringGetCStringPtr
- _CreateMicrophoneActivityPortal
- _OBJC_CLASS_$_MADClientInterface
- _OBJC_IVAR_$_MADClientInterface._mMADMultiplexer
- _OBJC_IVAR_$_MADClientInterface._mReverseConnections
- _OBJC_IVAR_$_MADClientInterface.mClient
- _OBJC_IVAR_$_MADClientInterface.mMTDCallbackReply
- _OBJC_METACLASS_$_MADClientInterface
- __OBJC_$_INSTANCE_METHODS_MADClientInterface
- __OBJC_$_INSTANCE_VARIABLES_MADClientInterface
- __OBJC_$_PROP_LIST_MADClientInterface
- __OBJC_$_PROTOCOL_INSTANCE_METHODS_MicActivityClientProtocol
- __OBJC_$_PROTOCOL_INSTANCE_METHODS_MicActivityReverseClientProtocol
- __OBJC_$_PROTOCOL_METHOD_TYPES_MicActivityClientProtocol
- __OBJC_$_PROTOCOL_METHOD_TYPES_MicActivityReverseClientProtocol
- __OBJC_CLASS_PROTOCOLS_$_MADClientInterface
- __OBJC_CLASS_RO_$_MADClientInterface
- __OBJC_LABEL_PROTOCOL_$_MicActivityClientProtocol
- __OBJC_LABEL_PROTOCOL_$_MicActivityReverseClientProtocol
- __OBJC_METACLASS_RO_$_MADClientInterface
- __OBJC_PROTOCOL_$_MicActivityClientProtocol
- __OBJC_PROTOCOL_$_MicActivityReverseClientProtocol
- __OBJC_PROTOCOL_REFERENCE_$_MicActivityClientProtocol
- __OBJC_PROTOCOL_REFERENCE_$_MicActivityReverseClientProtocol
- __ZGVZL27sIsolatedCoreAudioClientLogvE4sLog.1109
- __ZGVZL27sIsolatedCoreAudioClientLogvE4sLog.147
- __ZGVZL27sIsolatedCoreAudioClientLogvE4sLog.164
- __ZGVZL27sIsolatedCoreAudioClientLogvE4sLog.190
- __ZGVZL27sIsolatedCoreAudioClientLogvE4sLog.246
- __ZGVZL27sIsolatedCoreAudioClientLogvE4sLog.32
- __ZGVZL27sIsolatedCoreAudioClientLogvE4sLog.592
- __ZGVZL27sIsolatedCoreAudioClientLogvE4sLog.747
- __ZGVZL27sIsolatedCoreAudioClientLogvE4sLog.98
- __ZGVZL27sIsolatedCoreAudioServerLogvE4sLog.130
- __ZGVZL27sIsolatedCoreAudioServerLogvE4sLog.228
- __ZGVZL27sIsolatedCoreAudioServerLogvE4sLog.282
- __ZGVZL27sIsolatedCoreAudioServerLogvE4sLog.326
- __ZGVZL27sIsolatedCoreAudioServerLogvE4sLog.637
- __ZGVZL27sIsolatedCoreAudioServerLogvE4sLog.952
- __ZGVZL27sIsolatedCoreAudioSiphonLogvE4sLog.410
- __ZGVZL27sIsolatedCoreAudioSiphonLogvE4sLog.465
- __ZGVZL27sIsolatedCoreAudioSiphonLogvE4sLog.789
- __ZGVZL32sIsolatedCoreAudioMicActivityLogvE4sLog
- __ZGVZL32sIsolatedCoreAudioMicActivityLogvE4sLog.506
- __ZGVZL32sIsolatedCoreAudioMicActivityLogvE4sLog.691
- __ZL15micActivityFlag
- __ZL27sIsolatedCoreAudioClientLogv.1106
- __ZL27sIsolatedCoreAudioClientLogv.142
- __ZL27sIsolatedCoreAudioClientLogv.160
- __ZL27sIsolatedCoreAudioClientLogv.186
- __ZL27sIsolatedCoreAudioClientLogv.243
- __ZL27sIsolatedCoreAudioClientLogv.586
- __ZL27sIsolatedCoreAudioClientLogv.744
- __ZL27sIsolatedCoreAudioClientLogv.91
- __ZL27sIsolatedCoreAudioServerLogv.123
- __ZL27sIsolatedCoreAudioServerLogv.280
- __ZL27sIsolatedCoreAudioServerLogv.321
- __ZL27sIsolatedCoreAudioServerLogv.949
- __ZL27sIsolatedCoreAudioSiphonLogv.407
- __ZL27sIsolatedCoreAudioSiphonLogv.462
- __ZL27sIsolatedCoreAudioSiphonLogv.786
- __ZL32sIsolatedCoreAudioMicActivityLogv
- __ZN10applesauce2CF11TypeRefPairD1Ev
- __ZN10applesauce2CF13DictionaryRefD1Ev
- __ZN10applesauce2CF7TypeRefC1EPKc
- __ZN10applesauce2CF7TypeRefD1Ev
- __ZN10applesauce2CF7details20make_CFDictionaryRefERKSt16initializer_listINS0_11TypeRefPairEE
- __ZN10applesauce2CF8ArrayRefD2Ev
- __ZN10applesauce2CF9NumberRefD2Ev
- __ZN10applesauce2CF9ObjectRefIPK10__CFNumberED2Ev
- __ZN10applesauce2CF9ObjectRefIPKvED2Ev
- __ZN10applesauce2CF9StringRefD1Ev
- __ZN11HALTestImpl10DisableMTDEj
- __ZN11HALTestImpl12GetDeviceUIDEj
- __ZN11HALTestImpl12IsMTDEnabledEj
- __ZN11HALTestImpl13GetDeviceNameEj
- __ZN11HALTestImpl14IsProcessMutedEj
- __ZN11HALTestImpl15GetDefaultInputEv
- __ZN11HALTestImpl17EnableProcessMuteEj
- __ZN11HALTestImpl18DisableProcessMuteEj
- __ZN11HALTestImpl21CreateAggregateDeviceEv
- __ZN11HALTestImpl21IsMicActivityDetectedEj
- __ZN11HALTestImpl22DestroyAggregateDeviceEj
- __ZN11HALTestImpl24RegisterMTDStateListenerEjPKNSt3__18functionIFvbEEE
- __ZN11HALTestImpl26UnregisterMTDStateListenerEj
- __ZN11HALTestImpl9EnableMTDEj
- __ZN11HALTestImplD0Ev
- __ZN11HALTestImplD1Ev
- __ZN18HALBoilerplateImpl10DisableMTDEj
- __ZN18HALBoilerplateImpl11GetPropertyIN10applesauce2CF9StringRefEEEijRK26AudioObjectPropertyAddressRT_
- __ZN18HALBoilerplateImpl11GetPropertyIjEEijRK26AudioObjectPropertyAddressRT_
- __ZN18HALBoilerplateImpl11SetPropertyIjEEijRK26AudioObjectPropertyAddressRT_
- __ZN18HALBoilerplateImpl12GetDeviceUIDEj
- __ZN18HALBoilerplateImpl12IsMTDEnabledEj
- __ZN18HALBoilerplateImpl13GetDeviceNameEj
- __ZN18HALBoilerplateImpl14IsProcessMutedEj
- __ZN18HALBoilerplateImpl15GetDefaultInputEv
- __ZN18HALBoilerplateImpl16MTDStateListenerEjjPK26AudioObjectPropertyAddressPv
- __ZN18HALBoilerplateImpl17EnableProcessMuteEj
- __ZN18HALBoilerplateImpl17StringRefToStringEPK10__CFString
- __ZN18HALBoilerplateImpl18DisableProcessMuteEj
- __ZN18HALBoilerplateImpl19GetPropertyDataSizeEjRK26AudioObjectPropertyAddressRj
- __ZN18HALBoilerplateImpl21CreateAggregateDeviceEv
- __ZN18HALBoilerplateImpl21IsMicActivityDetectedEj
- __ZN18HALBoilerplateImpl22DestroyAggregateDeviceEj
- __ZN18HALBoilerplateImpl24RegisterMTDStateListenerEjPKNSt3__18functionIFvbEEE
- __ZN18HALBoilerplateImpl26UnregisterMTDStateListenerEj
- __ZN18HALBoilerplateImpl9EnableMTDEj
- __ZN18HALBoilerplateImplD0Ev
- __ZN18HALBoilerplateImplD1Ev
- __ZN24MicrophoneActivityPortalD0Ev
- __ZN24MicrophoneActivityPortalD1Ev
- __ZNKOSt3__18expectedINS_12basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEEEiE5valueB8ne200100Ev
- __ZNKOSt3__18expectedIjiE5valueB8ne200100Ev
- __ZNKSt3__110__function6__funcIN14MADMultiplexer29mMTDStateMultiplexingCallbackMUlbE_ENS_9allocatorIS3_EEFvbEE11target_typeEv
- __ZNKSt3__110__function6__funcIN14MADMultiplexer29mMTDStateMultiplexingCallbackMUlbE_ENS_9allocatorIS3_EEFvbEE6targetERKSt9type_info
- __ZNKSt3__110__function6__funcIN14MADMultiplexer29mMTDStateMultiplexingCallbackMUlbE_ENS_9allocatorIS3_EEFvbEE7__cloneEPNS0_6__baseIS6_EE
- __ZNKSt3__110__function6__funcIN14MADMultiplexer29mMTDStateMultiplexingCallbackMUlbE_ENS_9allocatorIS3_EEFvbEE7__cloneEv
- __ZNKSt3__110__function6__funcIZ40-[MADClientInterface createClientReaper]E3$_0NS_9allocatorIS2_EEFviEE11target_typeEv
- __ZNKSt3__110__function6__funcIZ40-[MADClientInterface createClientReaper]E3$_0NS_9allocatorIS2_EEFviEE6targetERKSt9type_info
- __ZNKSt3__110__function6__funcIZ40-[MADClientInterface createClientReaper]E3$_0NS_9allocatorIS2_EEFviEE7__cloneEPNS0_6__baseIS5_EE
- __ZNKSt3__110__function6__funcIZ40-[MADClientInterface createClientReaper]E3$_0NS_9allocatorIS2_EEFviEE7__cloneEv
- __ZNKSt3__110__function6__funcIZ56-[MADClientInterface listenForMicrophoneActivity:reply:]E3$_1NS_9allocatorIS2_EEFvbEE11target_typeEv
- __ZNKSt3__110__function6__funcIZ56-[MADClientInterface listenForMicrophoneActivity:reply:]E3$_1NS_9allocatorIS2_EEFvbEE6targetERKSt9type_info
- __ZNKSt3__110__function6__funcIZ56-[MADClientInterface listenForMicrophoneActivity:reply:]E3$_1NS_9allocatorIS2_EEFvbEE7__cloneEPNS0_6__baseIS5_EE
- __ZNKSt3__110__function6__funcIZ56-[MADClientInterface listenForMicrophoneActivity:reply:]E3$_1NS_9allocatorIS2_EEFvbEE7__cloneEv
- __ZNKSt3__119bad_expected_accessIvE4whatEv
- __ZNKSt3__18functionIFvbEEclEb
- __ZNSt13runtime_errorC1EPKc
- __ZNSt13runtime_errorD1Ev
- __ZNSt3__110__function12__value_funcIFvbEED2B8ne200100Ev
- __ZNSt3__110__function6__funcIN14MADMultiplexer29mMTDStateMultiplexingCallbackMUlbE_ENS_9allocatorIS3_EEFvbEE18destroy_deallocateEv
- __ZNSt3__110__function6__funcIN14MADMultiplexer29mMTDStateMultiplexingCallbackMUlbE_ENS_9allocatorIS3_EEFvbEE7destroyEv
- __ZNSt3__110__function6__funcIN14MADMultiplexer29mMTDStateMultiplexingCallbackMUlbE_ENS_9allocatorIS3_EEFvbEED0Ev
- __ZNSt3__110__function6__funcIN14MADMultiplexer29mMTDStateMultiplexingCallbackMUlbE_ENS_9allocatorIS3_EEFvbEED1Ev
- __ZNSt3__110__function6__funcIN14MADMultiplexer29mMTDStateMultiplexingCallbackMUlbE_ENS_9allocatorIS3_EEFvbEEclEOb
- __ZNSt3__110__function6__funcIZ40-[MADClientInterface createClientReaper]E3$_0NS_9allocatorIS2_EEFviEE18destroy_deallocateEv
- __ZNSt3__110__function6__funcIZ40-[MADClientInterface createClientReaper]E3$_0NS_9allocatorIS2_EEFviEE7destroyEv
- __ZNSt3__110__function6__funcIZ40-[MADClientInterface createClientReaper]E3$_0NS_9allocatorIS2_EEFviEED0Ev
- __ZNSt3__110__function6__funcIZ40-[MADClientInterface createClientReaper]E3$_0NS_9allocatorIS2_EEFviEED1Ev
- __ZNSt3__110__function6__funcIZ40-[MADClientInterface createClientReaper]E3$_0NS_9allocatorIS2_EEFviEEclEOi
- __ZNSt3__110__function6__funcIZ56-[MADClientInterface listenForMicrophoneActivity:reply:]E3$_1NS_9allocatorIS2_EEFvbEE18destroy_deallocateEv
- __ZNSt3__110__function6__funcIZ56-[MADClientInterface listenForMicrophoneActivity:reply:]E3$_1NS_9allocatorIS2_EEFvbEE7destroyEv
- __ZNSt3__110__function6__funcIZ56-[MADClientInterface listenForMicrophoneActivity:reply:]E3$_1NS_9allocatorIS2_EEFvbEED0Ev
- __ZNSt3__110__function6__funcIZ56-[MADClientInterface listenForMicrophoneActivity:reply:]E3$_1NS_9allocatorIS2_EEFvbEED1Ev
- __ZNSt3__110__function6__funcIZ56-[MADClientInterface listenForMicrophoneActivity:reply:]E3$_1NS_9allocatorIS2_EEFvbEEclEOb
- __ZNSt3__112__destroy_atB8ne200100IN10applesauce2CF13DictionaryRefELi0EEEvPT_
- __ZNSt3__115allocate_sharedB8ne200100I14MADMultiplexerNS_9allocatorIS1_EEJbELi0EEENS_10shared_ptrIT_EERKT0_DpOT1_
- __ZNSt3__115allocate_sharedB8ne200100I9MADClientNS_9allocatorIS1_EEJELi0EEENS_10shared_ptrIT_EERKT0_DpOT1_
- __ZNSt3__117__call_once_proxyB8ne200100INS_5tupleIJOZ30CreateMicrophoneActivityPortalE3$_0EEEEEvPv
- __ZNSt3__119bad_expected_accessIiED0Ev
- __ZNSt3__119bad_expected_accessIiED1Ev
- __ZNSt3__120__shared_ptr_emplaceI11HALTestImplNS_9allocatorIS1_EEE16__on_zero_sharedEv
- __ZNSt3__120__shared_ptr_emplaceI11HALTestImplNS_9allocatorIS1_EEE21__on_zero_shared_weakEv
- __ZNSt3__120__shared_ptr_emplaceI11HALTestImplNS_9allocatorIS1_EEED0Ev
- __ZNSt3__120__shared_ptr_emplaceI11HALTestImplNS_9allocatorIS1_EEED1Ev
- __ZNSt3__120__shared_ptr_emplaceI14MADMultiplexerNS_9allocatorIS1_EEE16__on_zero_sharedEv
- __ZNSt3__120__shared_ptr_emplaceI14MADMultiplexerNS_9allocatorIS1_EEE21__on_zero_shared_weakEv
- __ZNSt3__120__shared_ptr_emplaceI14MADMultiplexerNS_9allocatorIS1_EEED0Ev
- __ZNSt3__120__shared_ptr_emplaceI14MADMultiplexerNS_9allocatorIS1_EEED1Ev
- __ZNSt3__120__shared_ptr_emplaceI18HALBoilerplateImplNS_9allocatorIS1_EEE16__on_zero_sharedEv
- __ZNSt3__120__shared_ptr_emplaceI18HALBoilerplateImplNS_9allocatorIS1_EEE21__on_zero_shared_weakEv
- __ZNSt3__120__shared_ptr_emplaceI18HALBoilerplateImplNS_9allocatorIS1_EEED0Ev
- __ZNSt3__120__shared_ptr_emplaceI18HALBoilerplateImplNS_9allocatorIS1_EEED1Ev
- __ZNSt3__120__shared_ptr_emplaceI25MADClientProxyObjcWrapperNS_9allocatorIS1_EEE16__on_zero_sharedEv
- __ZNSt3__120__shared_ptr_emplaceI25MADClientProxyObjcWrapperNS_9allocatorIS1_EEE21__on_zero_shared_weakEv
- __ZNSt3__120__shared_ptr_emplaceI25MADClientProxyObjcWrapperNS_9allocatorIS1_EEED0Ev
- __ZNSt3__120__shared_ptr_emplaceI25MADClientProxyObjcWrapperNS_9allocatorIS1_EEED1Ev
- __ZNSt3__120__shared_ptr_emplaceI9MADClientNS_9allocatorIS1_EEE16__on_zero_sharedEv
- __ZNSt3__120__shared_ptr_emplaceI9MADClientNS_9allocatorIS1_EEE21__on_zero_shared_weakEv
- __ZNSt3__120__shared_ptr_emplaceI9MADClientNS_9allocatorIS1_EEED0Ev
- __ZNSt3__120__shared_ptr_emplaceI9MADClientNS_9allocatorIS1_EEED1Ev
- __ZNSt3__16vectorIN10applesauce2CF13DictionaryRefENS_9allocatorIS3_EEE16__destroy_vectorclB8ne200100Ev
- __ZNSt3__16vectorIN10applesauce2CF13DictionaryRefENS_9allocatorIS3_EEE20__throw_length_errorB8ne200100Ev
- __ZNSt3__16vectorIPKvNS_9allocatorIS2_EEE20__throw_length_errorB8ne200100Ev
- __ZNSt3__16vectorIPKvNS_9allocatorIS2_EEE7reserveEm
- __ZNSt3__19allocatorIPKvE17allocate_at_leastB8ne200100Em
- __ZTI11HALTestImpl
- __ZTI12HALInterface
- __ZTI18HALBoilerplateImpl
- __ZTI24MicrophoneActivityPortal
- __ZTIN14MADMultiplexer29mMTDStateMultiplexingCallbackMUlbE_E
- __ZTINSt3__110__function6__baseIFvbEEE
- __ZTINSt3__110__function6__funcIN14MADMultiplexer29mMTDStateMultiplexingCallbackMUlbE_ENS_9allocatorIS3_EEFvbEEE
- __ZTINSt3__110__function6__funcIZ40-[MADClientInterface createClientReaper]E3$_0NS_9allocatorIS2_EEFviEEE
- __ZTINSt3__110__function6__funcIZ56-[MADClientInterface listenForMicrophoneActivity:reply:]E3$_1NS_9allocatorIS2_EEFvbEEE
- __ZTINSt3__119bad_expected_accessIiEE
- __ZTINSt3__119bad_expected_accessIvEE
- __ZTINSt3__120__shared_ptr_emplaceI11HALTestImplNS_9allocatorIS1_EEEE
- __ZTINSt3__120__shared_ptr_emplaceI14MADMultiplexerNS_9allocatorIS1_EEEE
- __ZTINSt3__120__shared_ptr_emplaceI18HALBoilerplateImplNS_9allocatorIS1_EEEE
- __ZTINSt3__120__shared_ptr_emplaceI25MADClientProxyObjcWrapperNS_9allocatorIS1_EEEE
- __ZTINSt3__120__shared_ptr_emplaceI9MADClientNS_9allocatorIS1_EEEE
- __ZTISt13runtime_error
- __ZTIZ40-[MADClientInterface createClientReaper]E3$_0
- __ZTIZ56-[MADClientInterface listenForMicrophoneActivity:reply:]E3$_1
- __ZTS11HALTestImpl
- __ZTS12HALInterface
- __ZTS18HALBoilerplateImpl
- __ZTS24MicrophoneActivityPortal
- __ZTSN14MADMultiplexer29mMTDStateMultiplexingCallbackMUlbE_E
- __ZTSNSt3__110__function6__baseIFvbEEE
- __ZTSNSt3__110__function6__funcIN14MADMultiplexer29mMTDStateMultiplexingCallbackMUlbE_ENS_9allocatorIS3_EEFvbEEE
- __ZTSNSt3__110__function6__funcIZ40-[MADClientInterface createClientReaper]E3$_0NS_9allocatorIS2_EEFviEEE
- __ZTSNSt3__110__function6__funcIZ56-[MADClientInterface listenForMicrophoneActivity:reply:]E3$_1NS_9allocatorIS2_EEFvbEEE
- __ZTSNSt3__119bad_expected_accessIiEE
- __ZTSNSt3__120__shared_ptr_emplaceI11HALTestImplNS_9allocatorIS1_EEEE
- __ZTSNSt3__120__shared_ptr_emplaceI14MADMultiplexerNS_9allocatorIS1_EEEE
- __ZTSNSt3__120__shared_ptr_emplaceI18HALBoilerplateImplNS_9allocatorIS1_EEEE
- __ZTSNSt3__120__shared_ptr_emplaceI25MADClientProxyObjcWrapperNS_9allocatorIS1_EEEE
- __ZTSNSt3__120__shared_ptr_emplaceI9MADClientNS_9allocatorIS1_EEEE
- __ZTSZ40-[MADClientInterface createClientReaper]E3$_0
- __ZTSZ56-[MADClientInterface listenForMicrophoneActivity:reply:]E3$_1
- __ZTV11HALTestImpl
- __ZTV18HALBoilerplateImpl
- __ZTV24MicrophoneActivityPortal
- __ZTVNSt3__110__function6__funcIN14MADMultiplexer29mMTDStateMultiplexingCallbackMUlbE_ENS_9allocatorIS3_EEFvbEEE
- __ZTVNSt3__110__function6__funcIZ40-[MADClientInterface createClientReaper]E3$_0NS_9allocatorIS2_EEFviEEE
- __ZTVNSt3__110__function6__funcIZ56-[MADClientInterface listenForMicrophoneActivity:reply:]E3$_1NS_9allocatorIS2_EEFvbEEE
- __ZTVNSt3__119bad_expected_accessIiEE
- __ZTVNSt3__120__shared_ptr_emplaceI11HALTestImplNS_9allocatorIS1_EEEE
- __ZTVNSt3__120__shared_ptr_emplaceI14MADMultiplexerNS_9allocatorIS1_EEEE
- __ZTVNSt3__120__shared_ptr_emplaceI18HALBoilerplateImplNS_9allocatorIS1_EEEE
- __ZTVNSt3__120__shared_ptr_emplaceI25MADClientProxyObjcWrapperNS_9allocatorIS1_EEEE
- __ZTVNSt3__120__shared_ptr_emplaceI9MADClientNS_9allocatorIS1_EEEE
- __ZZ30CreateMicrophoneActivityPortalE6portal.0
- __ZZL27sIsolatedCoreAudioClientLogvE4sLog.101
- __ZZL27sIsolatedCoreAudioClientLogvE4sLog.1110
- __ZZL27sIsolatedCoreAudioClientLogvE4sLog.150
- __ZZL27sIsolatedCoreAudioClientLogvE4sLog.167
- __ZZL27sIsolatedCoreAudioClientLogvE4sLog.193
- __ZZL27sIsolatedCoreAudioClientLogvE4sLog.247
- __ZZL27sIsolatedCoreAudioClientLogvE4sLog.35
- __ZZL27sIsolatedCoreAudioClientLogvE4sLog.595
- __ZZL27sIsolatedCoreAudioClientLogvE4sLog.750
- __ZZL27sIsolatedCoreAudioServerLogvE4sLog.131
- __ZZL27sIsolatedCoreAudioServerLogvE4sLog.231
- __ZZL27sIsolatedCoreAudioServerLogvE4sLog.283
- __ZZL27sIsolatedCoreAudioServerLogvE4sLog.329
- __ZZL27sIsolatedCoreAudioServerLogvE4sLog.640
- __ZZL27sIsolatedCoreAudioServerLogvE4sLog.955
- __ZZL27sIsolatedCoreAudioSiphonLogvE4sLog.411
- __ZZL27sIsolatedCoreAudioSiphonLogvE4sLog.468
- __ZZL27sIsolatedCoreAudioSiphonLogvE4sLog.792
- __ZZL32sIsolatedCoreAudioMicActivityLogvE4sLog
- __ZZL32sIsolatedCoreAudioMicActivityLogvE4sLog.509
- __ZZL32sIsolatedCoreAudioMicActivityLogvE4sLog.692
- ___26-[MADClientInterface init]_block_invoke
- ___45-[MADClientInterface setupReverseConnection:]_block_invoke
- ___45-[MADClientInterface setupReverseConnection:]_block_invoke.16
- ___45-[MADClientInterface setupReverseConnection:]_block_invoke.19
- ___Block_byref_object_copy_.195
- ___Block_byref_object_dispose_.196
- ___block_descriptor_33_ea8_32c39_ZTSKZ26-[MADClientInterface init]E3$_2_e8_v12?0i8l
- ___block_descriptor_tmp.168
- ___block_descriptor_tmp.469
- ___block_literal_global.18
- ___block_literal_global.22
- ___block_literal_global.237
- ___block_literal_global.423
- ___block_literal_global.700
- ___copy_helper_block_ea8_32c39_ZTSKZ26-[MADClientInterface init]E3$_2
- ___destroy_helper_block_ea8_32.720
- _bzero
- _kCFTypeArrayCallBacks
- _kCFTypeDictionaryKeyCallBacks
- _kCFTypeDictionaryValueCallBacks
- _objc_msgSend$mMADMultiplexer
- _objc_msgSend$mReverseConnections
- _objc_msgSend$microphoneActivityStateChanged:reply:
- _objc_msgSend$setMMADMultiplexer:
- _objc_msgSend$setupReverseConnection:
CStrings:
+ ""
+ "%25s:%-5d Attempting to apply default tailspin config resulted in: %s"
+ "%25s:%-5d Attempting to apply testing config resulted in: %s"
+ "%25s:%-5d Attempting to dump %s tailspin"
+ "%25s:%-5d Cleared tailspin directory"
+ "%25s:%-5d Completed async tailspin drop - %@"
+ "%25s:%-5d Created tailspin at: %s"
+ "%25s:%-5d Creating default tailspin manager"
+ "%25s:%-5d Dropping tailspin to %@"
+ "%25s:%-5d Failed to create file descriptor - %@"
+ "%25s:%-5d Failed to create file descriptor for - %@"
+ "%25s:%-5d Failed to drop async tailspin - %@"
+ "%25s:%-5d Failed to drop tailspin - %@"
+ "%25s:%-5d IsolatedCoreAudioClientMultiplexer::stopIOIfNoClientsAreRunning No server IO running but we think some clients are running IO ???!!?"
+ "%25s:%-5d IsolatedCoreAudioClientMultiplexer::stopIOIfNoClientsAreRunning Stop requested, but no client IO (and server) is running IO"
+ "%25s:%-5d IsolatedCoreAudioClientMultiplexer::stopIOIfNoClientsAreRunning Stop requested, not stopping IO, as some clients still running"
+ "%25s:%-5d The tailspin dylib does not exist"
+ "%25s:%-5d Trace has already been written"
+ "%@/%@"
+ "%s"
+ "-"
+ "/tailspins"
+ "/usr/lib/libtailspin.dylib"
+ "/usr/local/lib/libtailspin.dylib"
+ "AudioHAL"
+ "AudioHAL_%@_%@.tailspin"
+ "ICAC Generated Dump"
+ "ICAC_Allow_FerryError_Spindump"
+ "IsolatedCoreAudioClientExclaveKitProxy_FerryError_"
+ "SingleUseTraceManager.mm"
+ "TSPDumpOptions_CollectAriadnePlists"
+ "TSPDumpOptions_CollectOsLogs"
+ "TSPDumpOptions_CollectOsSignposts"
+ "TSPDumpOptions_CollectTrials"
+ "TSPDumpOptions_ReasonString"
+ "TSPDumpOptions_Symbolicate"
+ "TraceManager"
+ "TraceManager.mm"
+ "UTF8String"
+ "clearDirectory"
+ "contentsOfDirectoryAtPath:error:"
+ "countByEnumeratingWithState:objects:count:"
+ "createDirectoryAtPath:withIntermediateDirectories:attributes:error:"
+ "date"
+ "defaultManager"
+ "dictionaryWithObjects:forKeys:count:"
+ "dumpTailspin:"
+ "dumpTailspinAsync:"
+ "failure"
+ "initWithCString:"
+ "removeItemAtPath:error:"
+ "setDateFormat:"
+ "setDefaultConfig"
+ "setObject:forKeyedSubscript:"
+ "setTestConfig"
+ "stringByAppendingPathComponent:"
+ "stringByReplacingOccurrencesOfString:withString:"
+ "stringFromDate:"
+ "stringWithFormat:"
+ "success"
+ "tailspinDumpOptions"
+ "tailspin_buffer_size_set"
+ "tailspin_config_apply_sync"
+ "tailspin_config_create_with_current_state"
+ "tailspin_config_create_with_default_config"
+ "tailspin_config_free"
+ "tailspin_dump_output_with_options"
+ "tailspin_dump_output_with_options_sync"
+ "tailspin_enabled_set"
+ "tailspin_full_sampling_period_set"
+ "tailspin_kdbg_filter_subclass_set"
+ "tailspin_oncore_sampling_period_set"
+ "v12@?0B8"
+ "yyyy-MM-dd_HH-mm-ss"
- "\""
- "%25s:%-5d CreateMicrophoneActivityPortal allocating portal"
- "%25s:%-5d Created the portal"
- "%25s:%-5d IsolatedCoreAudioClientMultiplexer::stopIOIfNoClientsAreRunning Stop requested, but no client IO is running IO"
- "%25s:%-5d MTDClientInterface - listenForMicrophoneActivity landed in the catch!"
- "%25s:%-5d MTDClientInterface constructor"
- "%25s:%-5d MTDClientInterface disableMicrophoneActivityDetection"
- "%25s:%-5d MTDClientInterface enableMicrophoneActivityDetection"
- "%25s:%-5d MTDClientInterface listenForMicrophoneActivity"
- "%25s:%-5d MTDClientInterface stopListeningForMicrophoneActivity"
- "%25s:%-5d MTDClientInterface test constructor"
- "%25s:%-5d Received CreateMicrophoneActivityPortal request"
- "@24@0:8@?16"
- "@?"
- "Could not construct"
- "DefaultInput"
- "DefaultInputUUID"
- "MADClientInterface"
- "MADClientInterface.mm"
- "MicActivityClientProtocol"
- "MicActivityReverseClientProtocol"
- "MicrophoneActivityPortal.mm"
- "T@\"NSMutableSet\",&,N,V_mReverseConnections"
- "T{shared_ptr<MADMultiplexer>=^{MADMultiplexer}^{__shared_weak_count}},N,V_mMADMultiplexer"
- "_mMADMultiplexer"
- "_mReverseConnections"
- "com.apple.audio.micactivityd"
- "com.apple.private.isolated.audio.coreaudioclient.micactivity"
- "disableMicrophoneActivityDetection:"
- "enableMicrophoneActivityDetection:"
- "initForTest:"
- "listenForMicrophoneActivity:reply:"
- "mClient"
- "mMADMultiplexer"
- "mMTDCallbackReply"
- "mReverseConnections"
- "master"
- "micactivityd input agg"
- "micactivityd-input-agg"
- "microphoneActivityStateChanged:reply:"
- "name"
- "private"
- "sIsolatedCoreAudioMicActivity"
- "setMMADMultiplexer:"
- "setMReverseConnections:"
- "setupReverseConnection:"
- "stopListeningForMicrophoneActivity:"
- "subdevices"
- "uid"
- "v24@0:8@?16"
- "v24@0:8@?<v@?i>16"
- "v28@0:8B16@?20"
- "v28@0:8B16@?<v@?i>20"
- "v32@0:8@\"NSXPCListenerEndpoint\"16@?<v@?i>24"
- "v32@0:8@16@?24"
- "v32@0:8{shared_ptr<MADMultiplexer>=^{MADMultiplexer}^{__shared_weak_count}}16"
- "vector"
- "{shared_ptr<MADClient>=\"__ptr_\"^{MADClient}\"__cntrl_\"^{__shared_weak_count}}"
- "{shared_ptr<MADMultiplexer>=\"__ptr_\"^{MADMultiplexer}\"__cntrl_\"^{__shared_weak_count}}"
- "{shared_ptr<MADMultiplexer>=^{MADMultiplexer}^{__shared_weak_count}}16@0:8"

```
