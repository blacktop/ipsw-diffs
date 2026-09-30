## IOAccelerator

> `/System/Library/PrivateFrameworks/IOAccelerator.framework/IOAccelerator`

```diff

-487.0.2.0.0
-  __TEXT.__text: 0x4260
+487.4.3.0.0
+  __TEXT.__text: 0x4274
   __TEXT.__auth_stubs: 0x470
   __TEXT.__objc_methlist: 0x68
   __TEXT.__const: 0x8
-  __TEXT.__cstring: 0x4d7
+  __TEXT.__cstring: 0x516
   __TEXT.__oslogstring: 0x4c
-  __TEXT.__unwind_info: 0x228
+  __TEXT.__unwind_info: 0x220
   __TEXT.__objc_classname: 0x10
   __TEXT.__objc_methname: 0x128
   __TEXT.__objc_methtype: 0x356

   - /System/Library/PrivateFrameworks/CoreAnalytics.framework/CoreAnalytics
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 4FF2D1C8-2B52-396B-BC17-368D8277653F
-  Functions: 217
-  Symbols:   432
+  UUID: D7ABFF7D-A971-3D6F-AD7D-9357C5211873
+  Functions: 218
+  Symbols:   434
   CStrings:  77
 
Symbols:
+ _OUTLINED_FUNCTION_0
Functions:
~ _IOAccelSharedDestroyDeviceShmem : 248 -> 252
~ _ioAccelSharedFinalize : 236 -> 232
- _IOAccelKillClient_LeakingContext
- -[IOAccelMTLEvent encodeKernelWaitEventCommandArgs:]
~ _IOAccelResourceCreateDataBuffer : 180 -> 192
+ _OUTLINED_FUNCTION_0
~ __ioAccelResourceListMergeGroup : 476 -> 480
+ _IOAccelKillClient_LeakingContext
+ -[IOAccelMTLEvent encodeKernelWaitEventCommandArgs:]
~ __IOAccelResourceAlloc.cold.1 : 20 -> 4
CStrings:
+ "/Library/Caches/com.apple.xbs/308693BE-CD25-478B-972B-FD8E0E779695/TemporaryDirectory.tEwBU4/Sources/IOAcceleratorFamily/Framework/IOAccelResourceRef.c"
- "/Library/Caches/com.apple.xbs/Sources/IOAcceleratorFamily/Framework/IOAccelResourceRef.c"

```
