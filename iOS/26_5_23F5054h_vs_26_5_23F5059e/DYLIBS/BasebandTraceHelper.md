## BasebandTraceHelper

> `/System/Library/PrivateFrameworks/BasebandTraceHelper.framework/BasebandTraceHelper`

```diff

 1418.1.0.0.0
-  __TEXT.__text: 0x4cb24
-  __TEXT.__auth_stubs: 0x12e0
+  __TEXT.__text: 0x4c5c8
+  __TEXT.__auth_stubs: 0x12c0
   __TEXT.__init_offsets: 0x3c
-  __TEXT.__const: 0x2958
-  __TEXT.__gcc_except_tab: 0x4194
-  __TEXT.__cstring: 0x142d
+  __TEXT.__const: 0x2948
+  __TEXT.__gcc_except_tab: 0x3e7c
+  __TEXT.__cstring: 0x141a
   __TEXT.__oslogstring: 0x2d2a
-  __TEXT.__unwind_info: 0x1838
+  __TEXT.__unwind_info: 0x17e8
   __TEXT.__objc_methname: 0x150
   __TEXT.__objc_stubs: 0x220
   __DATA_CONST.__got: 0x2f8
   __DATA_CONST.__const: 0xac0
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_selrefs: 0x88
-  __AUTH_CONST.__auth_got: 0x988
+  __AUTH_CONST.__auth_got: 0x978
   __AUTH_CONST.__const: 0x2090
   __AUTH_CONST.__cfstring: 0x20
   __DATA.__data: 0x3d8

   - /usr/lib/libTelephonyUtilDynamic.dylib
   - /usr/lib/libc++.1.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 937F60D9-CAA3-3E7A-8A9C-1E09D112684B
+  UUID: CCDB235F-8FA2-3AA1-8808-8612CBFF3026
   Functions: 1082
-  Symbols:   3136
-  CStrings:  589
+  Symbols:   3123
+  CStrings:  588
 
Symbols:
- _TelephonyBasebandWatchdogStartWithStackshot
- _TelephonyBasebandWatchdogStop
Functions:
~ __ZN19TraceFileCollection14storeFile_syncEb : 1352 -> 1244
~ __ZN7support2fs11updateOwnerENSt3__112basic_stringIcNS1_11char_traitsIcEENS1_9allocatorIcEEEEjj : 1556 -> 1512
~ __ZN7support2fs5isDirERKNSt3__112basic_stringIcNS1_11char_traitsIcEENS1_9allocatorIcEEEE : 92 -> 164
~ __ZN7support2fs5chownERKNSt3__112basic_stringIcNS1_11char_traitsIcEENS1_9allocatorIcEEEEjj : 140 -> 48
~ __ZN7support2fs7readDirERKNSt3__112basic_stringIcNS1_11char_traitsIcEENS1_9allocatorIcEEEERNS1_6vectorIS7_NS5_IS7_EEEE : 464 -> 396
~ __ZN7support2fs8openFileERKNSt3__112basic_stringIcNS1_11char_traitsIcEENS1_9allocatorIcEEEEit : 160 -> 52
~ __ZN7support2fs9closeFileEi : 156 -> 72
~ __ZN7support2fs8copyFileERKNSt3__112basic_stringIcNS1_11char_traitsIcEENS1_9allocatorIcEEEES9_b : 1364 -> 1272
~ __ZN7support2fs8loadFileERKNSt3__112basic_stringIcNS1_11char_traitsIcEENS1_9allocatorIcEEEERNS1_6vectorIcS6_EE : 816 -> 736
~ __ZN7support2fs8loadFileERKNSt3__112basic_stringIcNS1_11char_traitsIcEENS1_9allocatorIcEEEERNS1_6vectorIhNS5_IhEEEE : 464 -> 372
~ __ZN7support2fs10fileExistsERKNSt3__112basic_stringIcNS1_11char_traitsIcEENS1_9allocatorIcEEEE : 168 -> 84
~ __ZN7support2fs20createUniqueFilenameENSt3__112basic_stringIcNS1_11char_traitsIcEENS1_9allocatorIcEEEE : 3224 -> 3264
~ __ZN7support2fs16createUniquePathENSt3__112basic_stringIcNS1_11char_traitsIcEENS1_9allocatorIcEEEE : 720 -> 728
~ __ZN7support2fs9createDirERKNSt3__112basic_stringIcNS1_11char_traitsIcEENS1_9allocatorIcEEEEtb : 744 -> 712
~ __ZN7support2fs6renameERKNSt3__112basic_stringIcNS1_11char_traitsIcEENS1_9allocatorIcEEEES9_ : 144 -> 64
~ __ZN7support2fs5chmodERKNSt3__112basic_stringIcNS1_11char_traitsIcEENS1_9allocatorIcEEEEt : 156 -> 48
~ __ZN7support2fs9removeDirERKNSt3__112basic_stringIcNS1_11char_traitsIcEENS1_9allocatorIcEEEE : 1252 -> 1208
~ __ZN7support2fs10removeFileERKNSt3__112basic_stringIcNS1_11char_traitsIcEENS1_9allocatorIcEEEE : 148 -> 100
~ __ZN7support2fs17removeDirContentsERKNSt3__112basic_stringIcNS1_11char_traitsIcEENS1_9allocatorIcEEEEm : 1508 -> 1544
~ __ZN7support2fs13moveDirUniqueERKNSt3__112basic_stringIcNS1_11char_traitsIcEENS1_9allocatorIcEEEES9_ : 292 -> 340
~ __ZN7support2fs7lockDirERKNSt3__112basic_stringIcNS1_11char_traitsIcEENS1_9allocatorIcEEEE : 212 -> 148
~ __ZN7support2fs9unlockDirEi : 184 -> 100
~ __ZN3abm5trace9TraceInfo9getHeaderEv : 1852 -> 1784
~ ____ZN19TraceFileCollection4initEv_block_invoke : 1172 -> 1228
~ __ZN19TraceFileCollection10clear_syncENSt3__112basic_stringIcNS0_11char_traitsIcEENS0_9allocatorIcEEEEb : 1096 -> 1028
~ __ZN19TraceFileCollection19finishSnapshot_syncERKNSt3__112basic_stringIcNS0_11char_traitsIcEENS0_9allocatorIcEEEES8_S8_NS0_10shared_ptrIN3abm5trace9TraceInfoEEE : 5664 -> 5616
~ __ZN19TraceFileCollection31updateInfoForSnapshotFiles_syncEjRKNSt3__112basic_stringIcNS0_11char_traitsIcEENS0_9allocatorIcEEEERS6_NS0_10shared_ptrIN3abm5trace9TraceInfoEEE : 4284 -> 4148
CStrings:
- "Watchdog timed out"

```
