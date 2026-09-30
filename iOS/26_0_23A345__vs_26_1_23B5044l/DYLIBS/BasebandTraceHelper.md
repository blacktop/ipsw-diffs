## BasebandTraceHelper

> `/System/Library/PrivateFrameworks/BasebandTraceHelper.framework/BasebandTraceHelper`

```diff

-1391.0.0.0.0
-  __TEXT.__text: 0x4c634
-  __TEXT.__auth_stubs: 0x1290
+1397.0.0.0.0
+  __TEXT.__text: 0x4cb78
+  __TEXT.__auth_stubs: 0x12b0
   __TEXT.__init_offsets: 0x3c
-  __TEXT.__const: 0x2948
-  __TEXT.__gcc_except_tab: 0x3d40
-  __TEXT.__cstring: 0x13ca
-  __TEXT.__oslogstring: 0x2de9
-  __TEXT.__unwind_info: 0x1788
+  __TEXT.__const: 0x2968
+  __TEXT.__gcc_except_tab: 0x405c
+  __TEXT.__cstring: 0x13dd
+  __TEXT.__oslogstring: 0x2d8d
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
-  UUID: 61AF8A3D-1D15-359B-B6FD-8962496956AB
+  UUID: 019D2084-C523-3993-BA5F-B963A95E4B82
   Functions: 1071
-  Symbols:   3089
+  Symbols:   3102
   CStrings:  591
 
Symbols:
+ _TelephonyBasebandWatchdogStartWithStackshot
+ _TelephonyBasebandWatchdogStop
Functions:
~ __ZN19TraceFileCollection14storeFile_syncEb : 1228 -> 1348
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
~ ____ZNK3ctu20SharedSynchronizableI21TraceDataRateObserverE20execute_wrapped_syncIZNS1_8snapshotENSt3__110shared_ptrIN3abm5trace9TraceInfoEEEE3$_0EEDTclsr8dispatchE4syncLDnEclsr3stdE7forwardIT_Efp_EEEOSB__block_invoke : 3712 -> 3720
~ __ZN3abm5trace9TraceInfo9getHeaderEv : 1816 -> 1884
~ ____ZN19TraceFileCollection4initEv_block_invoke : 1264 -> 1208
~ __ZN19TraceFileCollection10clear_syncENSt3__112basic_stringIcNS0_11char_traitsIcEENS0_9allocatorIcEEEEb : 1036 -> 1104
~ __ZN19TraceFileCollection19finishSnapshot_syncERKNSt3__112basic_stringIcNS0_11char_traitsIcEENS0_9allocatorIcEEEES8_S8_NS0_10shared_ptrIN3abm5trace9TraceInfoEEE : 5700 -> 5728
~ __ZN19TraceFileCollection31updateInfoForSnapshotFiles_syncEjRKNSt3__112basic_stringIcNS0_11char_traitsIcEENS0_9allocatorIcEEEERS6_NS0_10shared_ptrIN3abm5trace9TraceInfoEEE : 4132 -> 4296
CStrings:
+ "The interval between this report and the last report is less than 10 minutes, aborting report"
+ "Watchdog timed out"
- "#I Start time: %s, end time: %s, amount: %f MB, duration: %f seconds, data rate: %f Mbps"
- "#I The interval between this report and the last report is less than 10 minutes, aborting report"

```
