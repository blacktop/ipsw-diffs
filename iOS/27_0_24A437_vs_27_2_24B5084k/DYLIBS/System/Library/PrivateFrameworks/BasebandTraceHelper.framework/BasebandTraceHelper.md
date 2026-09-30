## BasebandTraceHelper

> `/System/Library/PrivateFrameworks/BasebandTraceHelper.framework/BasebandTraceHelper`

```diff

-1585.0.0.0.0
-  __TEXT.__text: 0x5a920
+1594.0.0.0.0
+  __TEXT.__text: 0x5ae14
   __TEXT.__init_offsets: 0x38
-  __TEXT.__const: 0x2e00
-  __TEXT.__gcc_except_tab: 0x4890
+  __TEXT.__const: 0x2e10
+  __TEXT.__gcc_except_tab: 0x4ba4
   __TEXT.__oslogstring: 0x36a1
-  __TEXT.__cstring: 0x13b0
-  __TEXT.__unwind_info: 0x1c90
+  __TEXT.__cstring: 0x13c3
+  __TEXT.__unwind_info: 0x1ce8
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0
   __TEXT.__objc_methname: 0x0

   - /usr/lib/libc++.1.dylib
   - /usr/lib/libobjc.A.dylib
   Functions: 1217
-  Symbols:   2230
-  CStrings:  616
+  Symbols:   2232
+  CStrings:  617
 
Symbols:
+ _TelephonyBasebandWatchdogStartWithStackshot
+ _TelephonyBasebandWatchdogStop
Functions:
~ __ZN19TraceFileCollection14storeFile_syncEb : 1208 -> 1332
~ __ZN7support2fs11updateOwnerENSt3__112basic_stringIcNS1_11char_traitsIcEENS1_9allocatorIcEEEEjj : 1816 -> 1860
~ __ZN7support2fs5isDirERKNSt3__112basic_stringIcNS1_11char_traitsIcEENS1_9allocatorIcEEEE : 164 -> 92
~ __ZN7support2fs5chownERKNSt3__112basic_stringIcNS1_11char_traitsIcEENS1_9allocatorIcEEEEjj : 48 -> 140
~ __ZN7support2fs7readDirERKNSt3__112basic_stringIcNS1_11char_traitsIcEENS1_9allocatorIcEEEERNS1_6vectorIS7_NS5_IS7_EEEE : 372 -> 440
~ __ZN7support2fs8openFileERKNSt3__112basic_stringIcNS1_11char_traitsIcEENS1_9allocatorIcEEEEit : 52 -> 160
~ __ZN7support2fs9closeFileEi : 72 -> 156
~ __ZN7support2fs8copyFileERKNSt3__112basic_stringIcNS1_11char_traitsIcEENS1_9allocatorIcEEEES9_b : 1276 -> 1368
~ __ZN7support2fs8loadFileERKNSt3__112basic_stringIcNS1_11char_traitsIcEENS1_9allocatorIcEEEERNS1_6vectorIcS6_EE : 688 -> 776
~ __ZN7support2fs8loadFileERKNSt3__112basic_stringIcNS1_11char_traitsIcEENS1_9allocatorIcEEEERNS1_6vectorIhNS5_IhEEEE : 364 -> 464
~ __ZN7support2fs10fileExistsERKNSt3__112basic_stringIcNS1_11char_traitsIcEENS1_9allocatorIcEEEE : 84 -> 168
~ __ZN7support2fs20createUniqueFilenameENSt3__112basic_stringIcNS1_11char_traitsIcEENS1_9allocatorIcEEEE : 6120 -> 6060
~ __ZN7support2fs16createUniquePathENSt3__112basic_stringIcNS1_11char_traitsIcEENS1_9allocatorIcEEEE : 1100 -> 1092
~ __ZN7support2fs9createDirERKNSt3__112basic_stringIcNS1_11char_traitsIcEENS1_9allocatorIcEEEEtb : 1368 -> 1296
~ __ZN7support2fsL17createDirInternalERKNSt3__112basic_stringIcNS1_11char_traitsIcEENS1_9allocatorIcEEEEt : 372 -> 452
~ __ZN7support2fs6renameERKNSt3__112basic_stringIcNS1_11char_traitsIcEENS1_9allocatorIcEEEES9_ : 64 -> 144
~ __ZN7support2fs5chmodERKNSt3__112basic_stringIcNS1_11char_traitsIcEENS1_9allocatorIcEEEEt : 48 -> 156
~ __ZN7support2fs9removeDirERKNSt3__112basic_stringIcNS1_11char_traitsIcEENS1_9allocatorIcEEEE : 1776 -> 1804
~ __ZN7support2fs10removeFileERKNSt3__112basic_stringIcNS1_11char_traitsIcEENS1_9allocatorIcEEEE : 100 -> 148
~ __ZN7support2fs17removeDirContentsERKNSt3__112basic_stringIcNS1_11char_traitsIcEENS1_9allocatorIcEEEEm : 2104 -> 2048
~ __ZN7support2fs13moveDirUniqueERKNSt3__112basic_stringIcNS1_11char_traitsIcEENS1_9allocatorIcEEEES9_ : 340 -> 292
~ __ZN7support2fs7lockDirERKNSt3__112basic_stringIcNS1_11char_traitsIcEENS1_9allocatorIcEEEE : 148 -> 212
~ __ZN7support2fs9unlockDirEi : 100 -> 184
~ __ZN3abm5trace9TraceInfo9getHeaderEv : 1724 -> 1800
~ __ZN19TraceFileCollection10clear_syncENSt3__112basic_stringIcNS0_11char_traitsIcEENS0_9allocatorIcEEEEb : 972 -> 996
~ __ZN19TraceFileCollection19finishSnapshot_syncERKNSt3__112basic_stringIcNS0_11char_traitsIcEENS0_9allocatorIcEEEES8_S8_NS0_10shared_ptrIN3abm5trace9TraceInfoEEE : 8636 -> 8684
~ __ZN19TraceFileCollection31updateInfoForSnapshotFiles_syncEjRKNSt3__112basic_stringIcNS0_11char_traitsIcEENS0_9allocatorIcEEEERS6_NS0_10shared_ptrIN3abm5trace9TraceInfoEEE : 6248 -> 6352
~ ____ZN19TraceFileCollection4initEv_block_invoke : 1160 -> 1116
CStrings:
+ "Watchdog timed out"
```
