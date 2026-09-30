## BasebandTraceHelper

> `/System/Library/PrivateFrameworks/BasebandTraceHelper.framework/BasebandTraceHelper`

```diff

 1249.1.0.0.0
-  __TEXT.__text: 0x44ee8
-  __TEXT.__auth_stubs: 0x1270
+  __TEXT.__text: 0x449d0
+  __TEXT.__auth_stubs: 0x1250
   __TEXT.__init_offsets: 0x30
-  __TEXT.__const: 0x275c
-  __TEXT.__gcc_except_tab: 0x39f0
-  __TEXT.__cstring: 0x19ee
+  __TEXT.__const: 0x274c
+  __TEXT.__gcc_except_tab: 0x36e4
+  __TEXT.__cstring: 0x19db
   __TEXT.__oslogstring: 0x2519
-  __TEXT.__unwind_info: 0x15a0
+  __TEXT.__unwind_info: 0x1548
   __TEXT.__objc_methname: 0x119
   __TEXT.__objc_stubs: 0x1a0
   __DATA_CONST.__got: 0x258
   __DATA_CONST.__const: 0x7f8
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_selrefs: 0x68
-  __AUTH_CONST.__auth_got: 0x948
+  __AUTH_CONST.__auth_got: 0x938
   __AUTH_CONST.__const: 0x2248
   __AUTH_CONST.__cfstring: 0x20
   __DATA.__data: 0x370

   - /usr/lib/libTelephonyUtilDynamic.dylib
   - /usr/lib/libc++.1.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: A9237EDC-DD6D-3C74-A21C-3699C22A2E09
+  UUID: F67D478C-2733-3E79-9A5B-36DA38AC4FA6
   Functions: 969
-  Symbols:   2848
-  CStrings:  559
+  Symbols:   2835
+  CStrings:  558
 
Symbols:
- _TelephonyBasebandWatchdogStartWithStackshot
- _TelephonyBasebandWatchdogStop
Functions:
~ __ZN7support2fs11updateOwnerENSt3__112basic_stringIcNS1_11char_traitsIcEENS1_9allocatorIcEEEEjj : 1568 -> 1528
~ __ZN7support2fs5isDirERKNSt3__112basic_stringIcNS1_11char_traitsIcEENS1_9allocatorIcEEEE : 92 -> 164
~ __ZN7support2fs5chownERKNSt3__112basic_stringIcNS1_11char_traitsIcEENS1_9allocatorIcEEEEjj : 140 -> 48
~ __ZN7support2fs7readDirERKNSt3__112basic_stringIcNS1_11char_traitsIcEENS1_9allocatorIcEEEERNS1_6vectorIS7_NS5_IS7_EEEE : 464 -> 396
~ __ZN7support2fs8openFileERKNSt3__112basic_stringIcNS1_11char_traitsIcEENS1_9allocatorIcEEEEit : 160 -> 52
~ __ZN7support2fs9closeFileEi : 156 -> 72
~ __ZN7support2fs8copyFileERKNSt3__112basic_stringIcNS1_11char_traitsIcEENS1_9allocatorIcEEEES9_b : 1152 -> 1060
~ __ZN7support2fs8loadFileERKNSt3__112basic_stringIcNS1_11char_traitsIcEENS1_9allocatorIcEEEERNS1_6vectorIcS6_EE : 824 -> 744
~ __ZN7support2fs8loadFileERKNSt3__112basic_stringIcNS1_11char_traitsIcEENS1_9allocatorIcEEEERNS1_6vectorIhNS5_IhEEEE : 456 -> 364
~ __ZN7support2fs10fileExistsERKNSt3__112basic_stringIcNS1_11char_traitsIcEENS1_9allocatorIcEEEE : 168 -> 84
~ __ZN7support2fs20createUniqueFilenameENSt3__112basic_stringIcNS1_11char_traitsIcEENS1_9allocatorIcEEEE : 3596 -> 3640
~ __ZN7support2fs16createUniquePathENSt3__112basic_stringIcNS1_11char_traitsIcEENS1_9allocatorIcEEEE : 724 -> 732
~ __ZN7support2fs9createDirERKNSt3__112basic_stringIcNS1_11char_traitsIcEENS1_9allocatorIcEEEEtb : 744 -> 712
~ __ZN7support2fs6renameERKNSt3__112basic_stringIcNS1_11char_traitsIcEENS1_9allocatorIcEEEES9_ : 144 -> 64
~ __ZN7support2fs5chmodERKNSt3__112basic_stringIcNS1_11char_traitsIcEENS1_9allocatorIcEEEEt : 156 -> 48
~ __ZN7support2fs9removeDirERKNSt3__112basic_stringIcNS1_11char_traitsIcEENS1_9allocatorIcEEEE : 1284 -> 1220
~ __ZN7support2fs10removeFileERKNSt3__112basic_stringIcNS1_11char_traitsIcEENS1_9allocatorIcEEEE : 148 -> 100
~ __ZN7support2fs17removeDirContentsERKNSt3__112basic_stringIcNS1_11char_traitsIcEENS1_9allocatorIcEEEEm : 1548 -> 1608
~ __ZN7support2fs13moveDirUniqueERKNSt3__112basic_stringIcNS1_11char_traitsIcEENS1_9allocatorIcEEEES9_ : 292 -> 340
~ __ZN7support2fs7lockDirERKNSt3__112basic_stringIcNS1_11char_traitsIcEENS1_9allocatorIcEEEE : 212 -> 148
~ __ZN7support2fs9unlockDirEi : 184 -> 100
~ __ZN3abm5trace9TraceInfo9getHeaderEv : 1892 -> 1824
~ ____ZN19TraceFileCollection4initEv_block_invoke : 1208 -> 1264
~ __ZN19TraceFileCollection14storeFile_syncEb : 1380 -> 1300
~ __ZN19TraceFileCollection10clear_syncENSt3__112basic_stringIcNS0_11char_traitsIcEENS0_9allocatorIcEEEEb : 1104 -> 1036
~ __ZN19TraceFileCollection19finishSnapshot_syncERKNSt3__112basic_stringIcNS0_11char_traitsIcEENS0_9allocatorIcEEEES8_S8_NS0_10shared_ptrIN3abm5trace9TraceInfoEEE : 5628 -> 5588
~ __ZN19TraceFileCollection31updateInfoForSnapshotFiles_syncEjRKNSt3__112basic_stringIcNS0_11char_traitsIcEENS0_9allocatorIcEEEERS6_NS0_10shared_ptrIN3abm5trace9TraceInfoEEE : 4312 -> 4196
CStrings:
- "Watchdog timed out"

```
