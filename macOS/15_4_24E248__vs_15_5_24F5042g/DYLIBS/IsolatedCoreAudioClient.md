## IsolatedCoreAudioClient

> `/System/Library/PrivateFrameworks/IsolatedCoreAudioClient.framework/Versions/A/IsolatedCoreAudioClient`

```diff

-5.514.0.0.0
-  __TEXT.__text: 0x260cc
-  __TEXT.__auth_stubs: 0x900
-  __TEXT.__objc_methlist: 0x85c
-  __TEXT.__const: 0x2fb0
-  __TEXT.__gcc_except_tab: 0x21d0
-  __TEXT.__cstring: 0x75c
-  __TEXT.__oslogstring: 0x2a3a
-  __TEXT.__unwind_info: 0x1270
-  __TEXT.__objc_classname: 0x211
-  __TEXT.__objc_methname: 0x1039
-  __TEXT.__objc_methtype: 0xc5a
-  __TEXT.__objc_stubs: 0xc20
+5.602.0.0.0
+  __TEXT.__text: 0x273e4
+  __TEXT.__auth_stubs: 0xa00
+  __TEXT.__objc_methlist: 0x884
+  __TEXT.__const: 0x300b
+  __TEXT.__gcc_except_tab: 0x2364
+  __TEXT.__cstring: 0x93f
+  __TEXT.__oslogstring: 0x2bc8
+  __TEXT.__unwind_info: 0x1300
+  __TEXT.__objc_classname: 0x213
+  __TEXT.__objc_methname: 0x10f6
+  __TEXT.__objc_methtype: 0xc66
+  __TEXT.__objc_stubs: 0xce0
   __DATA_CONST.__got: 0x140
   __DATA_CONST.__const: 0xe0
   __DATA_CONST.__objc_classlist: 0x48
   __DATA_CONST.__objc_catlist: 0x8
   __DATA_CONST.__objc_protolist: 0x48
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x460
+  __DATA_CONST.__objc_selrefs: 0x490
   __DATA_CONST.__objc_protorefs: 0x28
   __DATA_CONST.__objc_superrefs: 0x48
-  __AUTH_CONST.__auth_got: 0x490
+  __AUTH_CONST.__auth_got: 0x510
   __AUTH_CONST.__auth_ptr: 0x8
-  __AUTH_CONST.__const: 0x3040
-  __AUTH_CONST.__cfstring: 0x140
-  __AUTH_CONST.__objc_const: 0xd70
+  __AUTH_CONST.__const: 0x30d0
+  __AUTH_CONST.__cfstring: 0x160
+  __AUTH_CONST.__objc_const: 0xda8
   __AUTH.__objc_data: 0x2d0
-  __DATA.__objc_ivar: 0x60
+  __DATA.__objc_ivar: 0x64
   __DATA.__data: 0x368
-  __DATA.__bss: 0x240
+  __DATA.__bss: 0x250
   - /System/Library/Frameworks/CoreAudio.framework/Versions/A/CoreAudio
   - /System/Library/Frameworks/CoreFoundation.framework/Versions/A/CoreFoundation
   - /System/Library/Frameworks/Foundation.framework/Versions/C/Foundation

   - /usr/lib/libbsm.0.dylib
   - /usr/lib/libc++.1.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 1098
-  Symbols:   2338
-  CStrings:  513
+  Functions: 1116
+  Symbols:   2395
+  CStrings:  535
 
Symbols:
+ -[IsolatedCoreAudioClientNSXPCListenerDelegate initWithInterface:andEntitlement:]
+ -[IsolatedCoreAudioClientNSXPCListenerDelegate mEntitlementString]
+ -[IsolatedCoreAudioClientNSXPCListenerDelegate setMEntitlementString:]
+ -[IsolatedCoreAudioXPCSiphon startIO:targetTime:with:]
+ GCC_except_table1033
+ GCC_except_table1039
+ GCC_except_table1043
+ GCC_except_table1045
+ GCC_except_table107
+ GCC_except_table11
+ GCC_except_table1118
+ GCC_except_table1126
+ GCC_except_table1128
+ GCC_except_table1131
+ GCC_except_table1132
+ GCC_except_table115
+ GCC_except_table120
+ GCC_except_table124
+ GCC_except_table139
+ GCC_except_table146
+ GCC_except_table148
+ GCC_except_table157
+ GCC_except_table170
+ GCC_except_table175
+ GCC_except_table18
+ GCC_except_table193
+ GCC_except_table22
+ GCC_except_table27
+ GCC_except_table273
+ GCC_except_table277
+ GCC_except_table291
+ GCC_except_table307
+ GCC_except_table309
+ GCC_except_table31
+ GCC_except_table311
+ GCC_except_table315
+ GCC_except_table333
+ GCC_except_table334
+ GCC_except_table336
+ GCC_except_table337
+ GCC_except_table342
+ GCC_except_table348
+ GCC_except_table36
+ GCC_except_table360
+ GCC_except_table362
+ GCC_except_table365
+ GCC_except_table367
+ GCC_except_table368
+ GCC_except_table371
+ GCC_except_table374
+ GCC_except_table385
+ GCC_except_table388
+ GCC_except_table397
+ GCC_except_table413
+ GCC_except_table415
+ GCC_except_table417
+ GCC_except_table42
+ GCC_except_table422
+ GCC_except_table429
+ GCC_except_table433
+ GCC_except_table443
+ GCC_except_table454
+ GCC_except_table458
+ GCC_except_table462
+ GCC_except_table472
+ GCC_except_table474
+ GCC_except_table476
+ GCC_except_table477
+ GCC_except_table479
+ GCC_except_table480
+ GCC_except_table481
+ GCC_except_table482
+ GCC_except_table483
+ GCC_except_table484
+ GCC_except_table485
+ GCC_except_table486
+ GCC_except_table512
+ GCC_except_table514
+ GCC_except_table52
+ GCC_except_table522
+ GCC_except_table531
+ GCC_except_table550
+ GCC_except_table556
+ GCC_except_table559
+ GCC_except_table56
+ GCC_except_table561
+ GCC_except_table573
+ GCC_except_table575
+ GCC_except_table576
+ GCC_except_table577
+ GCC_except_table578
+ GCC_except_table579
+ GCC_except_table580
+ GCC_except_table581
+ GCC_except_table584
+ GCC_except_table599
+ GCC_except_table623
+ GCC_except_table633
+ GCC_except_table637
+ GCC_except_table638
+ GCC_except_table639
+ GCC_except_table640
+ GCC_except_table656
+ GCC_except_table659
+ GCC_except_table703
+ GCC_except_table706
+ GCC_except_table707
+ GCC_except_table709
+ GCC_except_table713
+ GCC_except_table714
+ GCC_except_table716
+ GCC_except_table719
+ GCC_except_table722
+ GCC_except_table729
+ GCC_except_table73
+ GCC_except_table734
+ GCC_except_table735
+ GCC_except_table766
+ GCC_except_table772
+ GCC_except_table774
+ GCC_except_table778
+ GCC_except_table78
+ GCC_except_table780
+ GCC_except_table806
+ GCC_except_table81
+ GCC_except_table830
+ GCC_except_table84
+ GCC_except_table874
+ GCC_except_table875
+ GCC_except_table879
+ GCC_except_table889
+ GCC_except_table896
+ GCC_except_table911
+ GCC_except_table914
+ GCC_except_table924
+ GCC_except_table925
+ GCC_except_table935
+ GCC_except_table942
+ GCC_except_table943
+ GCC_except_table944
+ GCC_except_table946
+ GCC_except_table947
+ GCC_except_table949
+ GCC_except_table969
+ GCC_except_table970
+ GCC_except_table982
+ GCC_except_table993
+ OBJC_IVAR_$_IsolatedCoreAudioClientNSXPCListenerDelegate._mEntitlementString
+ _MGGetBoolAnswer
+ _ZGVZL27sIsolatedCoreAudioClientLogvE4sLog.1067
+ _ZGVZL27sIsolatedCoreAudioClientLogvE4sLog.122
+ _ZGVZL27sIsolatedCoreAudioClientLogvE4sLog.183
+ _ZGVZL27sIsolatedCoreAudioClientLogvE4sLog.200
+ _ZGVZL27sIsolatedCoreAudioClientLogvE4sLog.23
+ _ZGVZL27sIsolatedCoreAudioClientLogvE4sLog.234
+ _ZGVZL27sIsolatedCoreAudioClientLogvE4sLog.344
+ _ZGVZL27sIsolatedCoreAudioClientLogvE4sLog.53
+ _ZGVZL27sIsolatedCoreAudioClientLogvE4sLog.651
+ _ZGVZL27sIsolatedCoreAudioClientLogvE4sLog.873
+ _ZGVZL27sIsolatedCoreAudioServerLogvE4sLog.166
+ _ZGVZL27sIsolatedCoreAudioServerLogvE4sLog.19
+ _ZGVZL27sIsolatedCoreAudioServerLogvE4sLog.273
+ _ZGVZL27sIsolatedCoreAudioServerLogvE4sLog.382
+ _ZGVZL27sIsolatedCoreAudioServerLogvE4sLog.422
+ _ZGVZL27sIsolatedCoreAudioServerLogvE4sLog.706
+ _ZGVZL27sIsolatedCoreAudioServerLogvE4sLog.934
+ _ZGVZL27sIsolatedCoreAudioSiphonLogvE4sLog.514
+ _ZGVZL27sIsolatedCoreAudioSiphonLogvE4sLog.572
+ _ZGVZL27sIsolatedCoreAudioSiphonLogvE4sLog.586
+ _ZGVZL27sIsolatedCoreAudioSiphonLogvE4sLog.906
+ _ZGVZL32sIsolatedCoreAudioMicActivityLogvE4sLog.616
+ _ZGVZL32sIsolatedCoreAudioMicActivityLogvE4sLog.772
+ _ZL27sIsolatedCoreAudioClientLogv.1064
+ _ZL27sIsolatedCoreAudioClientLogv.115
+ _ZL27sIsolatedCoreAudioClientLogv.178
+ _ZL27sIsolatedCoreAudioClientLogv.196
+ _ZL27sIsolatedCoreAudioClientLogv.230
+ _ZL27sIsolatedCoreAudioClientLogv.341
+ _ZL27sIsolatedCoreAudioClientLogv.50
+ _ZL27sIsolatedCoreAudioClientLogv.646
+ _ZL27sIsolatedCoreAudioClientLogv.870
+ _ZL27sIsolatedCoreAudioServerLogv.158
+ _ZL27sIsolatedCoreAudioServerLogv.17
+ _ZL27sIsolatedCoreAudioServerLogv.380
+ _ZL27sIsolatedCoreAudioServerLogv.417
+ _ZL27sIsolatedCoreAudioServerLogv.931
+ _ZL27sIsolatedCoreAudioSiphonLogv.512
+ _ZL27sIsolatedCoreAudioSiphonLogv.569
+ _ZL27sIsolatedCoreAudioSiphonLogv.583
+ _ZL27sIsolatedCoreAudioSiphonLogv.903
+ _ZL32sIsolatedCoreAudioMicActivityLogv.769
+ _ZZL27sIsolatedCoreAudioClientLogvE4sLog.1068
+ _ZZL27sIsolatedCoreAudioClientLogvE4sLog.125
+ _ZZL27sIsolatedCoreAudioClientLogvE4sLog.186
+ _ZZL27sIsolatedCoreAudioClientLogvE4sLog.203
+ _ZZL27sIsolatedCoreAudioClientLogvE4sLog.237
+ _ZZL27sIsolatedCoreAudioClientLogvE4sLog.25
+ _ZZL27sIsolatedCoreAudioClientLogvE4sLog.346
+ _ZZL27sIsolatedCoreAudioClientLogvE4sLog.56
+ _ZZL27sIsolatedCoreAudioClientLogvE4sLog.654
+ _ZZL27sIsolatedCoreAudioClientLogvE4sLog.876
+ _ZZL27sIsolatedCoreAudioServerLogvE4sLog.167
+ _ZZL27sIsolatedCoreAudioServerLogvE4sLog.22
+ _ZZL27sIsolatedCoreAudioServerLogvE4sLog.276
+ _ZZL27sIsolatedCoreAudioServerLogvE4sLog.383
+ _ZZL27sIsolatedCoreAudioServerLogvE4sLog.425
+ _ZZL27sIsolatedCoreAudioServerLogvE4sLog.709
+ _ZZL27sIsolatedCoreAudioServerLogvE4sLog.937
+ _ZZL27sIsolatedCoreAudioSiphonLogvE4sLog.515
+ _ZZL27sIsolatedCoreAudioSiphonLogvE4sLog.575
+ _ZZL27sIsolatedCoreAudioSiphonLogvE4sLog.589
+ _ZZL27sIsolatedCoreAudioSiphonLogvE4sLog.909
+ _ZZL32sIsolatedCoreAudioMicActivityLogvE4sLog.619
+ _ZZL32sIsolatedCoreAudioMicActivityLogvE4sLog.773
+ __56-[IsolatedCoreAudioXPCSiphon connectToUseCase:endpoint:]_block_invoke.25
+ __56-[IsolatedCoreAudioXPCSiphon connectToUseCase:endpoint:]_block_invoke.28
+ __Block_byref_object_copy_.239
+ __Block_byref_object_dispose_.240
+ __ZN38IsolatedCoreAudioClientExclaveKitProxy42ferryIsolatedAudioDataToSinkFromSampleTimeE18CoreAudioTimestamp
+ __ZN38IsolatedCoreAudioClientExclaveKitProxy44ferryIsolatedAudioDataFromSourceAtSampleTimeEv
+ __ZN38IsolatedCoreAudioClientExclaveKitProxy48ferryIsolatedAudioDataToScopedSinkFromSampleTimeEv
+ __ZN38IsolatedCoreAudioClientExclaveKitProxy6anchorEy
+ __ZN38IsolatedCoreAudioClientExclaveKitProxyD0Ev
+ __ZN38IsolatedCoreAudioClientExclaveKitProxyD1Ev
+ __ZN38IsolatedCoreAudioClientExclaveKitProxyD2Ev
+ __ZNK15SiphonClientMap28enableLapseHandlingForClientEj
+ __ZNK15SiphonClientMap36enableAvailabilityCallbacksForClientEj
+ __ZNKSt3__110__function6__funcIZ81-[IsolatedCoreAudioClientNSXPCListenerDelegate initWithInterface:andEntitlement:]E3$_0NS_9allocatorIS2_EEFviEE11target_typeEv
+ __ZNKSt3__110__function6__funcIZ81-[IsolatedCoreAudioClientNSXPCListenerDelegate initWithInterface:andEntitlement:]E3$_0NS_9allocatorIS2_EEFviEE6targetERKSt9type_info
+ __ZNKSt3__110__function6__funcIZ81-[IsolatedCoreAudioClientNSXPCListenerDelegate initWithInterface:andEntitlement:]E3$_0NS_9allocatorIS2_EEFviEE7__cloneEPNS0_6__baseIS5_EE
+ __ZNKSt3__110__function6__funcIZ81-[IsolatedCoreAudioClientNSXPCListenerDelegate initWithInterface:andEntitlement:]E3$_0NS_9allocatorIS2_EEFviEE7__cloneEv
+ __ZNSt3__110__function6__funcIZ81-[IsolatedCoreAudioClientNSXPCListenerDelegate initWithInterface:andEntitlement:]E3$_0NS_9allocatorIS2_EEFviEE18destroy_deallocateEv
+ __ZNSt3__110__function6__funcIZ81-[IsolatedCoreAudioClientNSXPCListenerDelegate initWithInterface:andEntitlement:]E3$_0NS_9allocatorIS2_EEFviEE7destroyEv
+ __ZNSt3__110__function6__funcIZ81-[IsolatedCoreAudioClientNSXPCListenerDelegate initWithInterface:andEntitlement:]E3$_0NS_9allocatorIS2_EEFviEED0Ev
+ __ZNSt3__110__function6__funcIZ81-[IsolatedCoreAudioClientNSXPCListenerDelegate initWithInterface:andEntitlement:]E3$_0NS_9allocatorIS2_EEFviEED1Ev
+ __ZNSt3__110__function6__funcIZ81-[IsolatedCoreAudioClientNSXPCListenerDelegate initWithInterface:andEntitlement:]E3$_0NS_9allocatorIS2_EEFviEEclEOi
+ __ZNSt3__110unique_ptrINS_5tupleIJNS0_INS_15__thread_structENS_14default_deleteIS2_EEEEZN17ClientLocalServer25tellServerToStartIOAtTimeEyE3$_0EEENS3_IS8_EEED1B8ne190102Ev
+ __ZNSt3__114__thread_proxyB8ne190102INS_5tupleIJNS_10unique_ptrINS_15__thread_structENS_14default_deleteIS3_EEEEZN17ClientLocalServer25tellServerToStartIOAtTimeEyE3$_0EEEEEPvSA_
+ __ZNSt3__115allocate_sharedB8ne190102I38IsolatedCoreAudioClientExclaveKitProxyNS_9allocatorIS1_EEJELi0EEENS_10shared_ptrIT_EERKT0_DpOT1_
+ __ZNSt3__120__shared_ptr_emplaceI38IsolatedCoreAudioClientExclaveKitProxyNS_9allocatorIS1_EEE16__on_zero_sharedEv
+ __ZNSt3__120__shared_ptr_emplaceI38IsolatedCoreAudioClientExclaveKitProxyNS_9allocatorIS1_EEE21__on_zero_shared_weakEv
+ __ZNSt3__120__shared_ptr_emplaceI38IsolatedCoreAudioClientExclaveKitProxyNS_9allocatorIS1_EEED0Ev
+ __ZNSt3__120__shared_ptr_emplaceI38IsolatedCoreAudioClientExclaveKitProxyNS_9allocatorIS1_EEED1Ev
+ __ZTI38IsolatedCoreAudioClientExclaveKitProxy
+ __ZTINSt3__110__function6__funcIZ81-[IsolatedCoreAudioClientNSXPCListenerDelegate initWithInterface:andEntitlement:]E3$_0NS_9allocatorIS2_EEFviEEE
+ __ZTINSt3__120__shared_ptr_emplaceI38IsolatedCoreAudioClientExclaveKitProxyNS_9allocatorIS1_EEEE
+ __ZTIZ81-[IsolatedCoreAudioClientNSXPCListenerDelegate initWithInterface:andEntitlement:]E3$_0
+ __ZTS38IsolatedCoreAudioClientExclaveKitProxy
+ __ZTSNSt3__110__function6__funcIZ81-[IsolatedCoreAudioClientNSXPCListenerDelegate initWithInterface:andEntitlement:]E3$_0NS_9allocatorIS2_EEFviEEE
+ __ZTSNSt3__120__shared_ptr_emplaceI38IsolatedCoreAudioClientExclaveKitProxyNS_9allocatorIS1_EEEE
+ __ZTSZ81-[IsolatedCoreAudioClientNSXPCListenerDelegate initWithInterface:andEntitlement:]E3$_0
+ __ZTV38IsolatedCoreAudioClientExclaveKitProxy
+ __ZTVNSt3__110__function6__funcIZ81-[IsolatedCoreAudioClientNSXPCListenerDelegate initWithInterface:andEntitlement:]E3$_0NS_9allocatorIS2_EEFviEEE
+ __ZTVNSt3__120__shared_ptr_emplaceI38IsolatedCoreAudioClientExclaveKitProxyNS_9allocatorIS1_EEEE
+ ____ZN19SiphonedAudioClient11startAtTimeEy_block_invoke
+ ____ZN38IsolatedCoreAudioClientExclaveKitProxy42ferryIsolatedAudioDataToSinkFromSampleTimeE18CoreAudioTimestamp_block_invoke
+ ___block_descriptor_tmp
+ ___copy_helper_block_e8_32r
+ ___destroy_helper_block_e8_32r
+ __block_descriptor_tmp.204
+ __block_descriptor_tmp.576
+ __block_literal_global.31
+ __block_literal_global.335
+ __block_literal_global.526
+ __block_literal_global.592
+ __block_literal_global.781
+ __block_literal_global.93
+ __destroy_helper_block_ea8_32.601
+ __destroy_helper_block_ea8_32.800
+ __os_crash
+ _objc_msgSend$boolValue
+ _objc_msgSend$mEntitlementString
+ _objc_msgSend$processIdentifier
+ _objc_msgSend$setMEntitlementString:
+ _objc_msgSend$startIO:targetTime:with:
+ _objc_msgSend$valueForEntitlement:
+ _objc_setProperty_nonatomic_copy
+ _printf
+ _tb_client_connection_activate
+ _tb_client_connection_create_with_endpoint
+ _tb_client_connection_message_construct
+ _tb_client_connection_message_destruct
+ _tb_conclave_endpoint_for_service
+ _tb_connection_send_query
+ _tb_endpoint_destruct
+ _tb_endpoint_set_interface_identifier
+ _tb_message_complete
+ _tb_message_decode_s32
+ _tb_message_precheck_encoding
+ _tb_message_raw_encode_u64
- -[IsolatedCoreAudioClientNSXPCListenerDelegate initWithInterface:]
- GCC_except_table1015
- GCC_except_table1021
- GCC_except_table1025
- GCC_except_table1027
- GCC_except_table104
- GCC_except_table1095
- GCC_except_table1096
- GCC_except_table1100
- GCC_except_table1108
- GCC_except_table1110
- GCC_except_table114
- GCC_except_table119
- GCC_except_table122
- GCC_except_table136
- GCC_except_table144
- GCC_except_table147
- GCC_except_table156
- GCC_except_table168
- GCC_except_table17
- GCC_except_table174
- GCC_except_table192
- GCC_except_table21
- GCC_except_table26
- GCC_except_table266
- GCC_except_table280
- GCC_except_table293
- GCC_except_table296
- GCC_except_table298
- GCC_except_table30
- GCC_except_table300
- GCC_except_table313
- GCC_except_table320
- GCC_except_table321
- GCC_except_table322
- GCC_except_table323
- GCC_except_table329
- GCC_except_table33
- GCC_except_table347
- GCC_except_table349
- GCC_except_table352
- GCC_except_table354
- GCC_except_table355
- GCC_except_table358
- GCC_except_table359
- GCC_except_table361
- GCC_except_table375
- GCC_except_table376
- GCC_except_table384
- GCC_except_table400
- GCC_except_table404
- GCC_except_table406
- GCC_except_table409
- GCC_except_table41
- GCC_except_table416
- GCC_except_table420
- GCC_except_table430
- GCC_except_table441
- GCC_except_table448
- GCC_except_table449
- GCC_except_table459
- GCC_except_table460
- GCC_except_table463
- GCC_except_table464
- GCC_except_table466
- GCC_except_table49
- GCC_except_table496
- GCC_except_table499
- GCC_except_table501
- GCC_except_table518
- GCC_except_table537
- GCC_except_table544
- GCC_except_table547
- GCC_except_table548
- GCC_except_table55
- GCC_except_table551
- GCC_except_table553
- GCC_except_table560
- GCC_except_table562
- GCC_except_table563
- GCC_except_table565
- GCC_except_table567
- GCC_except_table568
- GCC_except_table571
- GCC_except_table586
- GCC_except_table607
- GCC_except_table610
- GCC_except_table611
- GCC_except_table625
- GCC_except_table626
- GCC_except_table627
- GCC_except_table643
- GCC_except_table646
- GCC_except_table690
- GCC_except_table692
- GCC_except_table693
- GCC_except_table694
- GCC_except_table695
- GCC_except_table699
- GCC_except_table700
- GCC_except_table702
- GCC_except_table715
- GCC_except_table72
- GCC_except_table720
- GCC_except_table721
- GCC_except_table752
- GCC_except_table759
- GCC_except_table763
- GCC_except_table765
- GCC_except_table77
- GCC_except_table80
- GCC_except_table814
- GCC_except_table82
- GCC_except_table858
- GCC_except_table859
- GCC_except_table863
- GCC_except_table873
- GCC_except_table880
- GCC_except_table882
- GCC_except_table892
- GCC_except_table893
- GCC_except_table894
- GCC_except_table895
- GCC_except_table9
- GCC_except_table919
- GCC_except_table927
- GCC_except_table928
- GCC_except_table930
- GCC_except_table931
- GCC_except_table933
- GCC_except_table953
- GCC_except_table954
- GCC_except_table966
- GCC_except_table977
- _ZGVZL27sIsolatedCoreAudioClientLogvE4sLog.1042
- _ZGVZL27sIsolatedCoreAudioClientLogvE4sLog.119
- _ZGVZL27sIsolatedCoreAudioClientLogvE4sLog.179
- _ZGVZL27sIsolatedCoreAudioClientLogvE4sLog.196
- _ZGVZL27sIsolatedCoreAudioClientLogvE4sLog.22
- _ZGVZL27sIsolatedCoreAudioClientLogvE4sLog.231
- _ZGVZL27sIsolatedCoreAudioClientLogvE4sLog.337
- _ZGVZL27sIsolatedCoreAudioClientLogvE4sLog.629
- _ZGVZL27sIsolatedCoreAudioClientLogvE4sLog.853
- _ZGVZL27sIsolatedCoreAudioServerLogvE4sLog.162
- _ZGVZL27sIsolatedCoreAudioServerLogvE4sLog.18
- _ZGVZL27sIsolatedCoreAudioServerLogvE4sLog.267
- _ZGVZL27sIsolatedCoreAudioServerLogvE4sLog.375
- _ZGVZL27sIsolatedCoreAudioServerLogvE4sLog.415
- _ZGVZL27sIsolatedCoreAudioServerLogvE4sLog.684
- _ZGVZL27sIsolatedCoreAudioServerLogvE4sLog.914
- _ZGVZL27sIsolatedCoreAudioSiphonLogvE4sLog.497
- _ZGVZL27sIsolatedCoreAudioSiphonLogvE4sLog.553
- _ZGVZL27sIsolatedCoreAudioSiphonLogvE4sLog.567
- _ZGVZL27sIsolatedCoreAudioSiphonLogvE4sLog.886
- _ZGVZL32sIsolatedCoreAudioMicActivityLogvE4sLog.596
- _ZGVZL32sIsolatedCoreAudioMicActivityLogvE4sLog.753
- _ZL27sIsolatedCoreAudioClientLogv.1039
- _ZL27sIsolatedCoreAudioClientLogv.112
- _ZL27sIsolatedCoreAudioClientLogv.174
- _ZL27sIsolatedCoreAudioClientLogv.192
- _ZL27sIsolatedCoreAudioClientLogv.227
- _ZL27sIsolatedCoreAudioClientLogv.334
- _ZL27sIsolatedCoreAudioClientLogv.624
- _ZL27sIsolatedCoreAudioClientLogv.850
- _ZL27sIsolatedCoreAudioServerLogv.155
- _ZL27sIsolatedCoreAudioServerLogv.16
- _ZL27sIsolatedCoreAudioServerLogv.373
- _ZL27sIsolatedCoreAudioServerLogv.410
- _ZL27sIsolatedCoreAudioServerLogv.911
- _ZL27sIsolatedCoreAudioSiphonLogv.494
- _ZL27sIsolatedCoreAudioSiphonLogv.550
- _ZL27sIsolatedCoreAudioSiphonLogv.564
- _ZL27sIsolatedCoreAudioSiphonLogv.883
- _ZL32sIsolatedCoreAudioMicActivityLogv.750
- _ZZL27sIsolatedCoreAudioClientLogvE4sLog.1043
- _ZZL27sIsolatedCoreAudioClientLogvE4sLog.122
- _ZZL27sIsolatedCoreAudioClientLogvE4sLog.182
- _ZZL27sIsolatedCoreAudioClientLogvE4sLog.199
- _ZZL27sIsolatedCoreAudioClientLogvE4sLog.234
- _ZZL27sIsolatedCoreAudioClientLogvE4sLog.24
- _ZZL27sIsolatedCoreAudioClientLogvE4sLog.338
- _ZZL27sIsolatedCoreAudioClientLogvE4sLog.632
- _ZZL27sIsolatedCoreAudioClientLogvE4sLog.856
- _ZZL27sIsolatedCoreAudioServerLogvE4sLog.163
- _ZZL27sIsolatedCoreAudioServerLogvE4sLog.21
- _ZZL27sIsolatedCoreAudioServerLogvE4sLog.270
- _ZZL27sIsolatedCoreAudioServerLogvE4sLog.376
- _ZZL27sIsolatedCoreAudioServerLogvE4sLog.418
- _ZZL27sIsolatedCoreAudioServerLogvE4sLog.687
- _ZZL27sIsolatedCoreAudioServerLogvE4sLog.917
- _ZZL27sIsolatedCoreAudioSiphonLogvE4sLog.498
- _ZZL27sIsolatedCoreAudioSiphonLogvE4sLog.556
- _ZZL27sIsolatedCoreAudioSiphonLogvE4sLog.570
- _ZZL27sIsolatedCoreAudioSiphonLogvE4sLog.889
- _ZZL32sIsolatedCoreAudioMicActivityLogvE4sLog.599
- _ZZL32sIsolatedCoreAudioMicActivityLogvE4sLog.754
- __56-[IsolatedCoreAudioXPCSiphon connectToUseCase:endpoint:]_block_invoke.21
- __56-[IsolatedCoreAudioXPCSiphon connectToUseCase:endpoint:]_block_invoke.24
- __Block_byref_object_copy_.236
- __Block_byref_object_dispose_.237
- __ZNKSt3__110__function6__funcIZ66-[IsolatedCoreAudioClientNSXPCListenerDelegate initWithInterface:]E3$_0NS_9allocatorIS2_EEFviEE11target_typeEv
- __ZNKSt3__110__function6__funcIZ66-[IsolatedCoreAudioClientNSXPCListenerDelegate initWithInterface:]E3$_0NS_9allocatorIS2_EEFviEE6targetERKSt9type_info
- __ZNKSt3__110__function6__funcIZ66-[IsolatedCoreAudioClientNSXPCListenerDelegate initWithInterface:]E3$_0NS_9allocatorIS2_EEFviEE7__cloneEPNS0_6__baseIS5_EE
- __ZNKSt3__110__function6__funcIZ66-[IsolatedCoreAudioClientNSXPCListenerDelegate initWithInterface:]E3$_0NS_9allocatorIS2_EEFviEE7__cloneEv
- __ZNSt3__110__function6__funcIZ66-[IsolatedCoreAudioClientNSXPCListenerDelegate initWithInterface:]E3$_0NS_9allocatorIS2_EEFviEE18destroy_deallocateEv
- __ZNSt3__110__function6__funcIZ66-[IsolatedCoreAudioClientNSXPCListenerDelegate initWithInterface:]E3$_0NS_9allocatorIS2_EEFviEE7destroyEv
- __ZNSt3__110__function6__funcIZ66-[IsolatedCoreAudioClientNSXPCListenerDelegate initWithInterface:]E3$_0NS_9allocatorIS2_EEFviEED0Ev
- __ZNSt3__110__function6__funcIZ66-[IsolatedCoreAudioClientNSXPCListenerDelegate initWithInterface:]E3$_0NS_9allocatorIS2_EEFviEED1Ev
- __ZNSt3__110__function6__funcIZ66-[IsolatedCoreAudioClientNSXPCListenerDelegate initWithInterface:]E3$_0NS_9allocatorIS2_EEFviEEclEOi
- __ZNSt3__110unique_ptrINS_5tupleIJNS0_INS_15__thread_structENS_14default_deleteIS2_EEEEZN17ClientLocalServer19tellServerToStartIOEvE3$_0EEENS3_IS8_EEED1B8ne190102Ev
- __ZNSt3__114__thread_proxyB8ne190102INS_5tupleIJNS_10unique_ptrINS_15__thread_structENS_14default_deleteIS3_EEEEZN17ClientLocalServer19tellServerToStartIOEvE3$_0EEEEEPvSA_
- __ZNSt3__120__shared_ptr_emplaceI35StubbedIsolatedCoreAudioClientProxyNS_9allocatorIS1_EEE16__on_zero_sharedEv
- __ZNSt3__120__shared_ptr_emplaceI35StubbedIsolatedCoreAudioClientProxyNS_9allocatorIS1_EEE21__on_zero_shared_weakEv
- __ZNSt3__120__shared_ptr_emplaceI35StubbedIsolatedCoreAudioClientProxyNS_9allocatorIS1_EEED0Ev
- __ZNSt3__120__shared_ptr_emplaceI35StubbedIsolatedCoreAudioClientProxyNS_9allocatorIS1_EEED1Ev
- __ZTINSt3__110__function6__funcIZ66-[IsolatedCoreAudioClientNSXPCListenerDelegate initWithInterface:]E3$_0NS_9allocatorIS2_EEFviEEE
- __ZTINSt3__120__shared_ptr_emplaceI35StubbedIsolatedCoreAudioClientProxyNS_9allocatorIS1_EEEE
- __ZTIZ66-[IsolatedCoreAudioClientNSXPCListenerDelegate initWithInterface:]E3$_0
- __ZTSNSt3__110__function6__funcIZ66-[IsolatedCoreAudioClientNSXPCListenerDelegate initWithInterface:]E3$_0NS_9allocatorIS2_EEFviEEE
- __ZTSNSt3__120__shared_ptr_emplaceI35StubbedIsolatedCoreAudioClientProxyNS_9allocatorIS1_EEEE
- __ZTSZ66-[IsolatedCoreAudioClientNSXPCListenerDelegate initWithInterface:]E3$_0
- __ZTVNSt3__110__function6__funcIZ66-[IsolatedCoreAudioClientNSXPCListenerDelegate initWithInterface:]E3$_0NS_9allocatorIS2_EEFviEEE
- __ZTVNSt3__120__shared_ptr_emplaceI35StubbedIsolatedCoreAudioClientProxyNS_9allocatorIS1_EEEE
- __block_descriptor_tmp.200
- __block_descriptor_tmp.557
- __block_literal_global.23
- __block_literal_global.328
- __block_literal_global.507
- __block_literal_global.572
- __block_literal_global.762
- __block_literal_global.87
- __destroy_helper_block_ea8_32.581
- __destroy_helper_block_ea8_32.780
CStrings:
+ "\x03"
+ "%25s:%-5d CreateIsolatedAudioServicePortal unsupported"
+ "%25s:%-5d CreateIsolatedAudioSiphonPortal unsupported"
+ "%25s:%-5d Error getting IsolateCoreAudioClient TightBeam endpoint - this should not happen!!! ErrorCode: %u"
+ "%25s:%-5d Process %i does not have the %@ entitlement"
+ "%25s:%-5d SiphonedAudioClient::startAtTime - status = %d"
+ "%25s:%-5d translateFerryToSinkStatus encountered an error! Result: %d"
+ "/AppleInternal/Library/BuildRoots/1d1afd2a-039a-11f0-91c4-fe9e33ca05fa/Library/Caches/com.apple.xbs/Binaries/IsolatedCoreAudioClient/install/TempContent/Objects/IsolatedCoreAudioClient.build/IsolatedCoreAudioClient.build/DerivedSources/IsolatedCoreAudioClient_C.c"
+ "@\"NSString\""
+ "ExclaveCapability"
+ "IsolatedCoreAudioClientExclaveKitProxy.cpp"
+ "T@\"NSString\",C,N,V_mEntitlementString"
+ "TB_FATAL: invalid value: unexpected case value, %llx"
+ "TB_FATAL: invalid value: unexpected case value, %llx (%s:%d)\n"
+ "_mEntitlementString"
+ "boolValue"
+ "com.apple.isolatedcoreaudioclient.service"
+ "false"
+ "initWithInterface:andEntitlement:"
+ "mEntitlementString"
+ "processIdentifier"
+ "setMEntitlementString:"
+ "startIO:targetTime:with:"
+ "valueForEntitlement:"
- "initWithInterface:"
- "true"

```
