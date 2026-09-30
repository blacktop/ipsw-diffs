## BasebandTraceHelper

> `/System/Library/PrivateFrameworks/BasebandTraceHelper.framework/BasebandTraceHelper`

```diff

 1397.0.0.0.0
-  __TEXT.__text: 0x4cb78
-  __TEXT.__auth_stubs: 0x12b0
+  __TEXT.__text: 0x4c63c
+  __TEXT.__auth_stubs: 0x1290
   __TEXT.__init_offsets: 0x3c
-  __TEXT.__const: 0x2968
-  __TEXT.__gcc_except_tab: 0x405c
-  __TEXT.__cstring: 0x13dd
+  __TEXT.__const: 0x2948
+  __TEXT.__gcc_except_tab: 0x3d44
+  __TEXT.__cstring: 0x13ca
   __TEXT.__oslogstring: 0x2d8d
-  __TEXT.__unwind_info: 0x17d8
+  __TEXT.__unwind_info: 0x1788
   __TEXT.__objc_methname: 0x150
   __TEXT.__objc_stubs: 0x220
   __DATA_CONST.__got: 0x2f8
   __DATA_CONST.__const: 0xae0
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_selrefs: 0x88
-  __AUTH_CONST.__auth_got: 0x970
+  __AUTH_CONST.__auth_got: 0x960
   __AUTH_CONST.__const: 0x2018
   __AUTH_CONST.__cfstring: 0x20
   __DATA.__data: 0x3d8

   - /usr/lib/libTelephonyUtilDynamic.dylib
   - /usr/lib/libc++.1.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: F95F9DCD-75A3-301A-A0F2-9C522B6BB877
+  UUID: 3906ED8E-9148-3232-897A-F4D0F4F6B197
   Functions: 1071
-  Symbols:   3102
-  CStrings:  591
+  Symbols:   3089
+  CStrings:  590
 
Symbols:
- _TelephonyBasebandWatchdogStartWithStackshot
- _TelephonyBasebandWatchdogStop
Functions:
~ __ZN19TraceFileCollection14storeFile_syncEb : 1348 -> 1228
~ __ZN7support2fs11updateOwnerENSt3__112basic_stringIcNS1_11char_traitsIcEENS1_9allocatorIcEEEEjj : 1552 -> 1508
~ __ZN7support2fs5isDirERKNSt3__112basic_stringIcNS1_11char_traitsIcEENS1_9allocatorIcEEEE : 92 -> 164
~ __ZN7support2fs5chownERKNSt3__112basic_stringIcNS1_11char_traitsIcEENS1_9allocatorIcEEEEjj : 140 -> 48
~ __ZN7support2fs7readDirERKNSt3__112basic_stringIcNS1_11char_traitsIcEENS1_9allocatorIcEEEERNS1_6vectorIS7_NS5_IS7_EEEE : 464 -> 396
~ __ZN7support2fs8openFileERKNSt3__112basic_stringIcNS1_11char_traitsIcEENS1_9allocatorIcEEEEit : 160 -> 52
~ __ZN7support2fs9closeFileEi : 156 -> 72
~ __ZN7support2fs8copyFileERKNSt3__112basic_stringIcNS1_11char_traitsIcEENS1_9allocatorIcEEEES9_b : 1364 -> 1272
~ __ZN7support2fs8loadFileERKNSt3__112basic_stringIcNS1_11char_traitsIcEENS1_9allocatorIcEEEERNS1_6vectorIcS6_EE : 820 -> 740
~ __ZN7support2fs8loadFileERKNSt3__112basic_stringIcNS1_11char_traitsIcEENS1_9allocatorIcEEEERNS1_6vectorIhNS5_IhEEEE : 464 -> 372
~ __ZN7support2fs10fileExistsERKNSt3__112basic_stringIcNS1_11char_traitsIcEENS1_9allocatorIcEEEE : 168 -> 84
~ __ZN7support2fs20createUniqueFilenameENSt3__112basic_stringIcNS1_11char_traitsIcEENS1_9allocatorIcEEEE : 3296 -> 3364
~ __ZN7support2fs16createUniquePathENSt3__112basic_stringIcNS1_11char_traitsIcEENS1_9allocatorIcEEEE : 720 -> 728
~ __ZN7support2fs9createDirERKNSt3__112basic_stringIcNS1_11char_traitsIcEENS1_9allocatorIcEEEEtb : 744 -> 712
~ __ZN7support2fs6renameERKNSt3__112basic_stringIcNS1_11char_traitsIcEENS1_9allocatorIcEEEES9_ : 144 -> 64
~ __ZN7support2fs5chmodERKNSt3__112basic_stringIcNS1_11char_traitsIcEENS1_9allocatorIcEEEEt : 156 -> 48
~ __ZN7support2fs9removeDirERKNSt3__112basic_stringIcNS1_11char_traitsIcEENS1_9allocatorIcEEEE : 1252 -> 1208
~ __ZN7support2fs10removeFileERKNSt3__112basic_stringIcNS1_11char_traitsIcEENS1_9allocatorIcEEEE : 148 -> 100
~ __ZN7support2fs17removeDirContentsERKNSt3__112basic_stringIcNS1_11char_traitsIcEENS1_9allocatorIcEEEEm : 1524 -> 1584
~ __ZN7support2fs13moveDirUniqueERKNSt3__112basic_stringIcNS1_11char_traitsIcEENS1_9allocatorIcEEEES9_ : 292 -> 340
~ __ZN7support2fs7lockDirERKNSt3__112basic_stringIcNS1_11char_traitsIcEENS1_9allocatorIcEEEE : 212 -> 148
~ __ZN7support2fs9unlockDirEi : 184 -> 100
~ __ZN3abm5trace9TraceInfo9getHeaderEv : 1884 -> 1816
~ ____ZN19TraceFileCollection4initEv_block_invoke : 1208 -> 1264
~ __ZN19TraceFileCollection10clear_syncENSt3__112basic_stringIcNS0_11char_traitsIcEENS0_9allocatorIcEEEEb : 1104 -> 1036
~ __ZN19TraceFileCollection19finishSnapshot_syncERKNSt3__112basic_stringIcNS0_11char_traitsIcEENS0_9allocatorIcEEEES8_S8_NS0_10shared_ptrIN3abm5trace9TraceInfoEEE : 5728 -> 5700
~ __ZN19TraceFileCollection31updateInfoForSnapshotFiles_syncEjRKNSt3__112basic_stringIcNS0_11char_traitsIcEENS0_9allocatorIcEEEERS6_NS0_10shared_ptrIN3abm5trace9TraceInfoEEE : 4296 -> 4132
CStrings:
- "Watchdog timed out"

```
