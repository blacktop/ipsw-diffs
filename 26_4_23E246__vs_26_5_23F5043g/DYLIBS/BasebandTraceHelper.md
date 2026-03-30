## BasebandTraceHelper

> `/System/Library/PrivateFrameworks/BasebandTraceHelper.framework/BasebandTraceHelper`

```diff

 1418.1.0.0.0
-  __TEXT.__text: 0x4c5c8
-  __TEXT.__auth_stubs: 0x12c0
+  __TEXT.__text: 0x4cb24
+  __TEXT.__auth_stubs: 0x12e0
   __TEXT.__init_offsets: 0x3c
-  __TEXT.__const: 0x2948
-  __TEXT.__gcc_except_tab: 0x3e7c
-  __TEXT.__cstring: 0x141a
+  __TEXT.__const: 0x2958
+  __TEXT.__gcc_except_tab: 0x4194
+  __TEXT.__cstring: 0x142d
   __TEXT.__oslogstring: 0x2d2a
-  __TEXT.__unwind_info: 0x17e8
+  __TEXT.__unwind_info: 0x1838
   __TEXT.__objc_methname: 0x150
   __TEXT.__objc_stubs: 0x220
   __DATA_CONST.__got: 0x2f8
   __DATA_CONST.__const: 0xac0
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_selrefs: 0x88
-  __AUTH_CONST.__auth_got: 0x978
+  __AUTH_CONST.__auth_got: 0x988
   __AUTH_CONST.__const: 0x2090
   __AUTH_CONST.__cfstring: 0x20
   __DATA.__data: 0x3d8

   - /usr/lib/libTelephonyUtilDynamic.dylib
   - /usr/lib/libc++.1.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 575EBF64-167D-341F-91C5-2BAF6DEA1B0E
+  UUID: E752A0AD-F9BB-3F21-8CFE-609474CF4F14
   Functions: 1082
-  Symbols:   3123
-  CStrings:  588
+  Symbols:   3136
+  CStrings:  589
 
Symbols:
+ _TelephonyBasebandWatchdogStartWithStackshot
+ _TelephonyBasebandWatchdogStop
Functions:
~ __ZN19TraceFileCollection14storeFile_syncEb : 1244 -> 1352
~ __ZN7support2fs11updateOwnerENSt3__112basic_stringIcNS1_11char_traitsIcEENS1_9allocatorIcEEEEjj : 1512 -> 1556
~ __ZN7support2fs5isDirERKNSt3__112basic_stringIcNS1_11char_traitsIcEENS1_9allocatorIcEEEE : 164 -> 92
~ __ZN7support2fs5chownERKNSt3__112basic_stringIcNS1_11char_traitsIcEENS1_9allocatorIcEEEEjj : 48 -> 140
~ __ZN7support2fs7readDirERKNSt3__112basic_stringIcNS1_11char_traitsIcEENS1_9allocatorIcEEEERNS1_6vectorIS7_NS5_IS7_EEEE : 396 -> 464
~ __ZN7support2fs8openFileERKNSt3__112basic_stringIcNS1_11char_traitsIcEENS1_9allocatorIcEEEEit : 52 -> 160
~ __ZN7support2fs9closeFileEi : 72 -> 156
~ __ZN7support2fs8copyFileERKNSt3__112basic_stringIcNS1_11char_traitsIcEENS1_9allocatorIcEEEES9_b : 1272 -> 1364
~ __ZN7support2fs8loadFileERKNSt3__112basic_stringIcNS1_11char_traitsIcEENS1_9allocatorIcEEEERNS1_6vectorIcS6_EE : 736 -> 816
~ __ZN7support2fs8loadFileERKNSt3__112basic_stringIcNS1_11char_traitsIcEENS1_9allocatorIcEEEERNS1_6vectorIhNS5_IhEEEE : 372 -> 464
~ __ZN7support2fs10fileExistsERKNSt3__112basic_stringIcNS1_11char_traitsIcEENS1_9allocatorIcEEEE : 84 -> 168
~ __ZN7support2fs20createUniqueFilenameENSt3__112basic_stringIcNS1_11char_traitsIcEENS1_9allocatorIcEEEE : 3264 -> 3224
~ __ZN7support2fs16createUniquePathENSt3__112basic_stringIcNS1_11char_traitsIcEENS1_9allocatorIcEEEE : 728 -> 720
~ __ZN7support2fs9createDirERKNSt3__112basic_stringIcNS1_11char_traitsIcEENS1_9allocatorIcEEEEtb : 712 -> 744
~ __ZN7support2fs6renameERKNSt3__112basic_stringIcNS1_11char_traitsIcEENS1_9allocatorIcEEEES9_ : 64 -> 144
~ __ZN7support2fs5chmodERKNSt3__112basic_stringIcNS1_11char_traitsIcEENS1_9allocatorIcEEEEt : 48 -> 156
~ __ZN7support2fs9removeDirERKNSt3__112basic_stringIcNS1_11char_traitsIcEENS1_9allocatorIcEEEE : 1208 -> 1252
~ __ZN7support2fs10removeFileERKNSt3__112basic_stringIcNS1_11char_traitsIcEENS1_9allocatorIcEEEE : 100 -> 148
~ __ZN7support2fs17removeDirContentsERKNSt3__112basic_stringIcNS1_11char_traitsIcEENS1_9allocatorIcEEEEm : 1544 -> 1508
~ __ZN7support2fs13moveDirUniqueERKNSt3__112basic_stringIcNS1_11char_traitsIcEENS1_9allocatorIcEEEES9_ : 340 -> 292
~ __ZN7support2fs7lockDirERKNSt3__112basic_stringIcNS1_11char_traitsIcEENS1_9allocatorIcEEEE : 148 -> 212
~ __ZN7support2fs9unlockDirEi : 100 -> 184
~ __ZN3abm5trace9TraceInfo9getHeaderEv : 1784 -> 1852
~ ____ZN19TraceFileCollection4initEv_block_invoke : 1228 -> 1172
~ __ZN19TraceFileCollection10clear_syncENSt3__112basic_stringIcNS0_11char_traitsIcEENS0_9allocatorIcEEEEb : 1028 -> 1096
~ __ZN19TraceFileCollection19finishSnapshot_syncERKNSt3__112basic_stringIcNS0_11char_traitsIcEENS0_9allocatorIcEEEES8_S8_NS0_10shared_ptrIN3abm5trace9TraceInfoEEE : 5616 -> 5664
~ __ZN19TraceFileCollection31updateInfoForSnapshotFiles_syncEjRKNSt3__112basic_stringIcNS0_11char_traitsIcEENS0_9allocatorIcEEEERS6_NS0_10shared_ptrIN3abm5trace9TraceInfoEEE : 4148 -> 4284
CStrings:
+ "Watchdog timed out"

```
