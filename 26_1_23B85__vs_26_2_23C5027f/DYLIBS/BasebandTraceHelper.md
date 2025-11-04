## BasebandTraceHelper

> `/System/Library/PrivateFrameworks/BasebandTraceHelper.framework/BasebandTraceHelper`

```diff

-1397.0.0.0.0
-  __TEXT.__text: 0x4c63c
-  __TEXT.__auth_stubs: 0x1290
+1399.2.0.0.0
+  __TEXT.__text: 0x4cc8c
+  __TEXT.__auth_stubs: 0x12b0
   __TEXT.__init_offsets: 0x3c
-  __TEXT.__const: 0x2948
-  __TEXT.__gcc_except_tab: 0x3d44
-  __TEXT.__cstring: 0x13ca
+  __TEXT.__const: 0x2968
+  __TEXT.__gcc_except_tab: 0x4060
+  __TEXT.__cstring: 0x13e5
   __TEXT.__oslogstring: 0x2d8d
-  __TEXT.__unwind_info: 0x1788
+  __TEXT.__unwind_info: 0x17d8
   __TEXT.__objc_methname: 0x150
   __TEXT.__objc_stubs: 0x220
   __DATA_CONST.__got: 0x2f8
   __DATA_CONST.__const: 0xae0
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_selrefs: 0x88
-  __AUTH_CONST.__auth_got: 0x960
+  __AUTH_CONST.__auth_got: 0x970
   __AUTH_CONST.__const: 0x2018
   __AUTH_CONST.__cfstring: 0x20
   __DATA.__data: 0x3d8

   - /usr/lib/libTelephonyUtilDynamic.dylib
   - /usr/lib/libc++.1.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 3906ED8E-9148-3232-897A-F4D0F4F6B197
+  UUID: 83CA12DA-7EEE-3CBA-AB66-7BB80BEECE31
   Functions: 1071
-  Symbols:   3089
-  CStrings:  590
+  Symbols:   3102
+  CStrings:  591
 
Symbols:
+ _TelephonyBasebandWatchdogStartWithStackshot
+ _TelephonyBasebandWatchdogStop
Functions:
~ __ZN19TraceFileCollection14storeFile_syncEb : 1228 -> 1348
~ __ZNKSt3__120__shared_ptr_pointerIP3TCPZN3ctu20SharedSynchronizableIS1_E15make_shared_ptrIS1_EENS_10shared_ptrIT_EEPS8_EUlS2_E_NS_9allocatorIS1_EEE13__get_deleterERKSt9type_info : 92 -> 108
~ __ZN7support3log32global_client_descriptor_manager23get_descriptor_instanceERKNSt3__112basic_stringIcNS2_11char_traitsIcEENS2_9allocatorIcEEEESA_ : 2344 -> 2320
~ __ZNKSt3__120__shared_ptr_pointerIPN7support3log8delegate7contextENS_10shared_ptrIS4_E27__shared_ptr_default_deleteIS4_S4_EENS_9allocatorIS4_EEE13__get_deleterERKSt9type_info : 108 -> 124
~ __ZNKSt3__120__shared_ptr_pointerIPN7support3log7managerENS_10shared_ptrIS3_E27__shared_ptr_default_deleteIS3_S3_EENS_9allocatorIS3_EEE13__get_deleterERKSt9type_info : 108 -> 124
~ __ZNKSt3__120__shared_ptr_pointerIPN7support7parsers3acp10SuperFrameENS_10shared_ptrIS4_E27__shared_ptr_default_deleteIS4_S4_EENS_9allocatorIS4_EEE13__get_deleterERKSt9type_info : 108 -> 124
~ __ZNKSt3__120__shared_ptr_pointerIPN7support7parsers3acp12BaseACPChunkENS_10shared_ptrIS4_E27__shared_ptr_default_deleteIS4_S4_EENS_9allocatorIS4_EEE13__get_deleterERKSt9type_info : 108 -> 124
~ __ZNKSt3__120__shared_ptr_pointerIPN7support7parsers3acp11LSCACPChunkENS_10shared_ptrIS4_E27__shared_ptr_default_deleteIS4_S4_EENS_9allocatorIS4_EEE13__get_deleterERKSt9type_info : 108 -> 124
~ __ZNKSt3__120__shared_ptr_pointerIPN7support7parsers3acp12ParserEngineEZN3ctu20SharedSynchronizableIS4_E15make_shared_ptrIS4_EENS_10shared_ptrIT_EEPSB_EUlS5_E_NS_9allocatorIS4_EEE13__get_deleterERKSt9type_info : 92 -> 108
~ ____ZNK3ctu20SharedSynchronizableI16DataRateObserverE20execute_wrapped_syncIZZNS1_10start_syncEvENK3$_0clEvEUlvE_EEDTclsr8dispatchE4syncLDnEclsr3stdE7forwardIT_Efp_EEEOS6__block_invoke : 1272 -> 1276
~ __ZNKSt3__120__shared_ptr_pointerIPN7support4misc10safe_timerENS_14default_deleteIS3_EENS_9allocatorIS3_EEE13__get_deleterERKSt9type_info : 108 -> 124
~ ____ZNK3ctu20SharedSynchronizableI16DataRateObserverE20execute_wrapped_syncIZNS1_13gatherSamplesEvE3$_0EEDTclsr8dispatchE4syncLDnEclsr3stdE7forwardIT_Efp_EEEOS5__block_invoke : 332 -> 344
~ __ZN7support2fs11updateOwnerENSt3__112basic_stringIcNS1_11char_traitsIcEENS1_9allocatorIcEEEEjj : 1508 -> 1552
~ __ZN7support2fs5isDirERKNSt3__112basic_stringIcNS1_11char_traitsIcEENS1_9allocatorIcEEEE : 164 -> 92
~ __ZN7support2fs5chownERKNSt3__112basic_stringIcNS1_11char_traitsIcEENS1_9allocatorIcEEEEjj : 48 -> 140
~ __ZN7support2fs7readDirERKNSt3__112basic_stringIcNS1_11char_traitsIcEENS1_9allocatorIcEEEERNS1_6vectorIS7_NS5_IS7_EEEE : 396 -> 464
~ __ZN7support2fs8openFileERKNSt3__112basic_stringIcNS1_11char_traitsIcEENS1_9allocatorIcEEEEit : 52 -> 160
~ __ZN7support2fs9closeFileEi : 72 -> 156
~ __ZN7support2fs8copyFileERKNSt3__112basic_stringIcNS1_11char_traitsIcEENS1_9allocatorIcEEEES9_b : 1272 -> 1364
~ __ZN7support2fs8loadFileERKNSt3__112basic_stringIcNS1_11char_traitsIcEENS1_9allocatorIcEEEERNS1_6vectorIcS6_EE : 740 -> 820
~ __ZN7support2fs8loadFileERKNSt3__112basic_stringIcNS1_11char_traitsIcEENS1_9allocatorIcEEEERNS1_6vectorIhNS5_IhEEEE : 372 -> 464
~ __ZN7support2fs10fileExistsERKNSt3__112basic_stringIcNS1_11char_traitsIcEENS1_9allocatorIcEEEE : 84 -> 168
~ __ZN7support2fs20createUniqueFilenameENSt3__112basic_stringIcNS1_11char_traitsIcEENS1_9allocatorIcEEEE : 3364 -> 3296
~ __ZN7support2fs16createUniquePathENSt3__112basic_stringIcNS1_11char_traitsIcEENS1_9allocatorIcEEEE : 728 -> 720
~ __ZN7support2fs9createDirERKNSt3__112basic_stringIcNS1_11char_traitsIcEENS1_9allocatorIcEEEEtb : 712 -> 744
~ __ZN7support2fs6renameERKNSt3__112basic_stringIcNS1_11char_traitsIcEENS1_9allocatorIcEEEES9_ : 64 -> 144
~ __ZN7support2fs5chmodERKNSt3__112basic_stringIcNS1_11char_traitsIcEENS1_9allocatorIcEEEEt : 48 -> 156
~ __ZN7support2fs9removeDirERKNSt3__112basic_stringIcNS1_11char_traitsIcEENS1_9allocatorIcEEEE : 1208 -> 1252
~ __ZN7support2fs10removeFileERKNSt3__112basic_stringIcNS1_11char_traitsIcEENS1_9allocatorIcEEEE : 100 -> 148
~ __ZN7support2fs17removeDirContentsERKNSt3__112basic_stringIcNS1_11char_traitsIcEENS1_9allocatorIcEEEEm : 1584 -> 1524
~ __ZN7support2fs13moveDirUniqueERKNSt3__112basic_stringIcNS1_11char_traitsIcEENS1_9allocatorIcEEEES9_ : 340 -> 292
~ __ZN7support2fs7lockDirERKNSt3__112basic_stringIcNS1_11char_traitsIcEENS1_9allocatorIcEEEE : 148 -> 212
~ __ZN7support2fs9unlockDirEi : 100 -> 184
~ __ZNSt3__16vectorINS_12basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEEENS4_IS6_EEE24__emplace_back_slow_pathIJRKS6_EEEPS6_DpOT_ : 340 -> 344
~ __ZNKSt3__120__shared_ptr_pointerIPNS_13__empty_stateIcEENS_10shared_ptrIS2_E27__shared_ptr_default_deleteIS2_S2_EENS_9allocatorIS2_EEE13__get_deleterERKSt9type_info : 108 -> 124
~ __ZNSt3__16vectorINS_7__stateIcEENS_9allocatorIS2_EEE24__emplace_back_slow_pathIJS2_EEEPS2_DpOT_ : 380 -> 384
~ __ZNKSt3__120__shared_ptr_pointerIP20BasebandTransportMAVZN3ctu20SharedSynchronizableI17BasebandTransportE15make_shared_ptrIS1_EENS_10shared_ptrIT_EEPS9_EUlS2_E_NS_9allocatorIS1_EEE13__get_deleterERKSt9type_info : 92 -> 108
~ __ZNKSt3__120__shared_ptr_pointerIP20BasebandTransportICEZN3ctu20SharedSynchronizableI17BasebandTransportE15make_shared_ptrIS1_EENS_10shared_ptrIT_EEPS9_EUlS2_E_NS_9allocatorIS1_EEE13__get_deleterERKSt9type_info : 92 -> 108
~ __ZNKSt3__120__shared_ptr_pointerIP17BasebandTransportZN3ctu20SharedSynchronizableIS1_E15make_shared_ptrIS1_EENS_10shared_ptrIT_EEPS8_EUlS2_E_NS_9allocatorIS1_EEE13__get_deleterERKSt9type_info : 92 -> 108
~ __ZNKSt3__120__shared_ptr_pointerIP9TraceFileNS_10shared_ptrIS1_E27__shared_ptr_default_deleteIS1_S1_EENS_9allocatorIS1_EEE13__get_deleterERKSt9type_info : 108 -> 124
~ __ZNKSt3__120__shared_ptr_pointerIPN3abm5trace11TraceReaderENS_10shared_ptrIS3_E27__shared_ptr_default_deleteIS3_S3_EENS_9allocatorIS3_EEE13__get_deleterERKSt9type_info : 108 -> 124
~ __ZN3abm5trace9TraceInfo4pushENS0_14TraceInfoEntryE : 1848 -> 1852
~ __ZN3abm5trace9TraceInfo9getHeaderEv : 1816 -> 1884
~ __ZNKSt3__120__shared_ptr_pointerIPN3abm5trace9TraceInfoENS_10shared_ptrIS3_E27__shared_ptr_default_deleteIS3_S3_EENS_9allocatorIS3_EEE13__get_deleterERKSt9type_info : 108 -> 124
~ __ZNKSt3__120__shared_ptr_pointerIP10SharedDataNS_10shared_ptrIS1_E27__shared_ptr_default_deleteIS1_S1_EENS_9allocatorIS1_EEE13__get_deleterERKSt9type_info : 108 -> 124
~ ____ZN19TraceFileCollection4initEv_block_invoke : 1264 -> 1208
~ __ZN19TraceFileCollection10clear_syncENSt3__112basic_stringIcNS0_11char_traitsIcEENS0_9allocatorIcEEEEb : 1036 -> 1104
~ __ZN19TraceFileCollection19finishSnapshot_syncERKNSt3__112basic_stringIcNS0_11char_traitsIcEENS0_9allocatorIcEEEES8_S8_NS0_10shared_ptrIN3abm5trace9TraceInfoEEE : 5700 -> 5728
~ __ZN19TraceFileCollection31updateInfoForSnapshotFiles_syncEjRKNSt3__112basic_stringIcNS0_11char_traitsIcEENS0_9allocatorIcEEEERS6_NS0_10shared_ptrIN3abm5trace9TraceInfoEEE : 4132 -> 4296
~ __ZNKSt3__120__shared_ptr_pointerIP19TraceFileCollectionZN3ctu20SharedSynchronizableIS1_E15make_shared_ptrIS1_EENS_10shared_ptrIT_EEPS8_EUlS2_E_NS_9allocatorIS1_EEE13__get_deleterERKSt9type_info : 92 -> 108
CStrings:
+ "Watchdog timed out"
+ "v32@?0{basic_string<char, std::char_traits<char>, std::allocator<char>>={?=(__rep={__short=[23c]b7b1}{__long=*Qb63b1})}}8"
+ "{vector<DataRateObserver::Sample, std::allocator<DataRateObserver::Sample>>=^{Sample}^{Sample}{?=^{Sample}}}8@?0"
- "v32@?0{basic_string<char, std::char_traits<char>, std::allocator<char>>=(__rep={__short=[23c]b7b1}{__long=*Qb63b1})}8"
- "{vector<DataRateObserver::Sample, std::allocator<DataRateObserver::Sample>>=^{Sample}^{Sample}^{Sample}}8@?0"

```
