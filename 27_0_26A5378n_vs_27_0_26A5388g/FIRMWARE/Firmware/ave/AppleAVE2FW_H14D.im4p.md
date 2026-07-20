## AppleAVE2FW_H14D.im4p

> `Firmware/ave/AppleAVE2FW_H14D.im4p`

### Sections with Same Size but Changed Content

- `__DATA._rtk_patchbay`
- `__DATA.__data`
- `__DATA._rtk_mtab`
- `__DATA.__const`

```diff

-  __TEXT.__text: 0xfc6a0
-  __TEXT.__const: 0x22c04
-  __TEXT.__cstring: 0x1622d
+  __TEXT.__text: 0xfd9b0
+  __TEXT.__const: 0x22c24
+  __TEXT.__cstring: 0x163ac
   __TEXT.__init_offsets: 0x0
   __TEXT.__chain_starts: 0x18
   __DATA._rtk_patchbay: 0x211

   __DATA._rtk_threads: 0x0
   __DATA.__constructor: 0x0
   __DATA.__zerofill: 0xd2ee0
-  Functions: 1159
-  Symbols:   1613
-  CStrings:  2523
+  Functions: 1162
+  Symbols:   1617
+  CStrings:  2531
 
Symbols:
+ __ZN10CAVEClient15GetCommandQueueE19_E_Proc_Mode_Queues
+ __ZN10CAVEClient22ProcessDirectFrameCmdsEi
+ __ZN20CAVECommonController12GetPicParamsEPv
+ __ZN9BlurRatio6updateERK10FrameStats
CStrings:
+ "!MIDR: 0x%x"
+ "%s::%s:%d  Failed to Queue AVE_Cmd_Process for client_id: %lld %lld"
+ "%s::%s:%d %s | Fail to dequeue frame %d"
+ "%s::%s:%d %s | Failed to enqueue frame %lld"
+ "%s::%s:%d BITBOX (%lld %lld) type %d current blur %d.%06d filtered blur %d.%06d transcodeBits %d cplxFiltered %d.%06d"
+ "%s::%s:%d Failed to Queue AVE_Cmd_Process for client_id: %lld %lld"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.sw8xfi/Sources/AppleAVE2FW/External/Algorithm/RateControl.cpp"
+ "9013.35.1"
+ "Caller is /AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.sw8xfi/Sources/AppleAVE2FW/External/Algorithm/RateControl.cpp:855"
+ "Caller is /AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.sw8xfi/Sources/AppleAVE2FW/External/Algorithm/RateControl.cpp:860"
+ "Caller is /AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.sw8xfi/Sources/AppleAVE2FW/External/Algorithm/RateControl.cpp:901"
+ "Caller is /AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.sw8xfi/Sources/AppleAVE2FW/External/Algorithm/RateControl.cpp:913"
+ "ProcessDirectFrameCmds"
+ "bDequeued"
+ "bEnqueueResult"
- "!MIDR: 0x%llx"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.VBnlrw/Sources/AppleAVE2FW/External/Algorithm/RateControl.cpp"
- "9013.12.1"
- "Caller is /AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.VBnlrw/Sources/AppleAVE2FW/External/Algorithm/RateControl.cpp:855"
- "Caller is /AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.VBnlrw/Sources/AppleAVE2FW/External/Algorithm/RateControl.cpp:860"
- "Caller is /AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.VBnlrw/Sources/AppleAVE2FW/External/Algorithm/RateControl.cpp:901"
- "Caller is /AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.VBnlrw/Sources/AppleAVE2FW/External/Algorithm/RateControl.cpp:913"
```
