## IOAccelerator

> `/System/Library/PrivateFrameworks/IOAccelerator.framework/IOAccelerator`

```diff

-487.4.3.0.0
-  __TEXT.__text: 0x4274
-  __TEXT.__auth_stubs: 0x470
+490.0.0.0.0
+  __TEXT.__text: 0x42b8
   __TEXT.__objc_methlist: 0x68
   __TEXT.__const: 0x8
   __TEXT.__cstring: 0x516
   __TEXT.__oslogstring: 0x4c
-  __TEXT.__unwind_info: 0x220
-  __TEXT.__objc_classname: 0x10
-  __TEXT.__objc_methname: 0x128
-  __TEXT.__objc_methtype: 0x356
-  __TEXT.__objc_stubs: 0x20
-  __DATA_CONST.__got: 0x40
+  __TEXT.__unwind_info: 0x228
+  __TEXT.__objc_stubs: 0x0
+  __TEXT.__auth_stubs: 0x0
+  __TEXT.__objc_classname: 0x0
+  __TEXT.__objc_methname: 0x0
+  __TEXT.__objc_methtype: 0x0
   __DATA_CONST.__const: 0x120
   __DATA_CONST.__objc_classlist: 0x8
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_selrefs: 0x48
   __DATA_CONST.__objc_superrefs: 0x8
-  __AUTH_CONST.__auth_got: 0x240
+  __DATA_CONST.__got: 0x0
   __AUTH_CONST.__const: 0x300
   __AUTH_CONST.__cfstring: 0xa0
   __AUTH_CONST.__objc_const: 0x130
+  __AUTH_CONST.__auth_got: 0x240
   __AUTH.__objc_data: 0x28
   __DATA.__objc_ivar: 0x10
   __DATA.__bss: 0x50

   - /System/Library/PrivateFrameworks/CoreAnalytics.framework/CoreAnalytics
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 866232D9-FC04-3E38-9B1A-01E3EFB0645A
+  UUID: 1E7B3A40-0F5C-3E6F-9978-32D11A42B712
   Functions: 218
   Symbols:   434
-  CStrings:  77
+  CStrings:  52
 
Functions:
~ ___IOAccelInitCommPage_block_invoke -> _IOAccelMemoryInfoRegisterAPICollectionBlock : 80 -> 172
~ _IOAccelInitCommPage.cold.1 -> _IOAccelInitCommPage : 20 -> 44
~ _IOAccelInitCommPage -> _IOAccelInitCommPage.cold.1 : 44 -> 20
~ ___IOAccelMemoryInfoRegisterAPICollectionBlock_block_invoke -> ___IOAccelInitCommPage_block_invoke : 164 -> 80
~ _IOAccelDeviceCreateWithAPIProperty : 768 -> 784
~ _ioAccelContextFinalize : 104 -> 108
~ _IOAccelDeviceTestEventFast : 96 -> 104
~ _IOAccelResourceListAddResourceNoThreshold : 412 -> 424
~ _IOAccelResourceListAddResource : 404 -> 416
~ __ioAccelResourceListMergeGroup : 480 -> 496
~ _IOAccelResourceListShowResources : 176 -> 184
~ _ioAccelResourceListAddNewGroupAndResource : 240 -> 244
~ _ioAccelResourceListMergeNewResource : 220 -> 224
~ _IOAccelMemoryInfoDeregisterAPICollectionBlock : 80 -> 96
~ ___launchMemlistConnection_block_invoke : 328 -> 332
~ _IOAccelDeviceCreateWithAPIProperty.cold.1 : 128 -> 84
CStrings:
- "@24@0:8^{__IOAccelShared={__CFRuntimeBase=QAQ}^{__IOAccelDevice}I@?Q{os_unfair_lock_s=I}^{IOAcceldirtyRingRO}^{IOAcceldirtyRingRW}^{IOAccelDirtyResourceCommand}I{os_unfair_lock_s=I}{shmemlog_list=^{_s_shmemlog_}}^Q}16"
- "@32@0:8^{__IOAccelShared={__CFRuntimeBase=QAQ}^{__IOAccelDevice}I@?Q{os_unfair_lock_s=I}^{IOAcceldirtyRingRO}^{IOAcceldirtyRingRW}^{IOAccelDirtyResourceCommand}I{os_unfair_lock_s=I}{shmemlog_list=^{_s_shmemlog_}}^Q}16Q24"
- "B16@0:8"
- "I"
- "I24@0:8^{IOAccelKernelCommandSignalOrWaitEventArgs=ISSQ}16"
- "I32@0:8^{IOAccelKernelCommandSignalOrWaitEventArgs=ISSQ}16Q24"
- "I36@0:8^{IOAccelKernelCommandSignalOrWaitEventArgs=ISSQ}16Q24I32"
- "IOAccelMTLEvent"
- "Q"
- "TB,R"
- "^{__IOAccelShared={__CFRuntimeBase=QAQ}^{__IOAccelDevice}I@?Q{os_unfair_lock_s=I}^{IOAcceldirtyRingRO}^{IOAcceldirtyRingRW}^{IOAccelDirtyResourceCommand}I{os_unfair_lock_s=I}{shmemlog_list=^{_s_shmemlog_}}^Q}"
- "_eventName"
- "_eventOptions"
- "_globalTraceObjectID"
- "_sharedRef"
- "dealloc"
- "encodeKernelSignalEventCommandArgs:value:"
- "encodeKernelWaitEventCommandArgs:"
- "encodeKernelWaitEventCommandArgs:value:"
- "encodeKernelWaitEventCommandArgs:value:timeout:"
- "init"
- "initWithShared:"
- "initWithShared:options:"
- "supportsRollback"
- "v16@0:8"

```
