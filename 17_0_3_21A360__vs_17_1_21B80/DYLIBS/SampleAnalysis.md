## SampleAnalysis

> `/System/Library/PrivateFrameworks/SampleAnalysis.framework/SampleAnalysis`

```diff

-340.0.0.0.0
-  __TEXT.__text: 0xc6dfc
+341.0.0.0.0
+  __TEXT.__text: 0xc7390
   __TEXT.__auth_stubs: 0x1550
   __TEXT.__objc_methlist: 0x49ec
   __TEXT.__const: 0x138
-  __TEXT.__cstring: 0x141b5
-  __TEXT.__oslogstring: 0xa192
-  __TEXT.__gcc_except_tab: 0x65a0
+  __TEXT.__cstring: 0x14203
+  __TEXT.__oslogstring: 0xa23a
+  __TEXT.__gcc_except_tab: 0x65e0
   __TEXT.__dlopen_cstrs: 0x4e
-  __TEXT.__unwind_info: 0x1d34
+  __TEXT.__unwind_info: 0x1d5c
   __TEXT.__objc_classname: 0x8c2
   __TEXT.__objc_methname: 0xae5e
   __TEXT.__objc_methtype: 0x14d7
   __TEXT.__objc_stubs: 0x6ac0
   __DATA_CONST.__got: 0xe0
-  __DATA_CONST.__const: 0x2fc8
+  __DATA_CONST.__const: 0x3038
   __DATA_CONST.__objc_classlist: 0x330
   __DATA_CONST.__objc_catlist: 0x10
   __DATA_CONST.__objc_protolist: 0x40

   __DATA_CONST.__objc_arraydata: 0x60
   __AUTH_CONST.__cfstring: 0x9980
   __AUTH_CONST.__objc_const: 0x0
-  __AUTH_CONST.__const: 0x2c0
+  __AUTH_CONST.__const: 0x320
   __AUTH_CONST.__objc_intobj: 0x138
   __AUTH_CONST.__objc_arrayobj: 0x90
   __AUTH_CONST.__auth_got: 0xac0

   __DATA.__thread_bss: 0x11
   __DATA.__common: 0x498
   __DATA.__bss: 0x38
-  __DATA_DIRTY.__const: 0x6e0
+  __DATA_DIRTY.__const: 0x6c0
   __DATA_DIRTY.__objc_const: 0x2be8
   __DATA_DIRTY.__objc_ivar: 0x2c
   __DATA_DIRTY.__objc_data: 0x1fe0
-  __DATA_DIRTY.__bss: 0x3f8
+  __DATA_DIRTY.__bss: 0x408
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/CoreServices.framework/CoreServices
   - /System/Library/Frameworks/Foundation.framework/Foundation

   - /usr/lib/libdscsym.dylib
   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libz.1.dylib
-  Functions: 2375
-  Symbols:   8039
-  CStrings:  5578
+  Functions: 2381
+  Symbols:   8056
+  CStrings:  5584
 
Symbols:
+ -[SASampleStore enumerateTasksWithLiveness:]
+ -[SASampleStore taskForMicrostackshotTask:loadInfos:numLoadInfos:sharedCache:loadInfosIsPartial:timestamp:architecture:needAOTInfo:isFromCurrentBoot:]
+ -[SATask correspondsToName:mainBinaryLoadInfo:architecture:sharedCache:]
+ -[SATask fixupFrameInstructionsWithDataGatheringOptions:mightBeAlive:inspectedLiveTask:uuidsWithNewInstructions:]
+ -[SATask isFromCurrentBootCycle]
+ GCC_except_table161
+ GCC_except_table198
+ GCC_except_table210
+ GCC_except_table227
+ GCC_except_table261
+ GCC_except_table400
+ GCC_except_table403
+ GCC_except_table404
+ GCC_except_table407
+ _.str.80
+ _SATimeOfBootForLiveMachine
+ ___116-[SASampleStore _addKCDataStackshot:timestamp:sampleIndex:shouldSkipSampleOut:primaryDataIsKPerf:addStaticInfoOnly:]_block_invoke.278
+ ___116-[SASampleStore _addKCDataStackshot:timestamp:sampleIndex:shouldSkipSampleOut:primaryDataIsKPerf:addStaticInfoOnly:]_block_invoke.286
+ ___116-[SASampleStore _addKCDataStackshot:timestamp:sampleIndex:shouldSkipSampleOut:primaryDataIsKPerf:addStaticInfoOnly:]_block_invoke.324
+ ___116-[SASampleStore _addKCDataStackshot:timestamp:sampleIndex:shouldSkipSampleOut:primaryDataIsKPerf:addStaticInfoOnly:]_block_invoke.328
+ ___116-[SASampleStore _addKCDataStackshot:timestamp:sampleIndex:shouldSkipSampleOut:primaryDataIsKPerf:addStaticInfoOnly:]_block_invoke.332
+ ___116-[SASampleStore _addKCDataStackshot:timestamp:sampleIndex:shouldSkipSampleOut:primaryDataIsKPerf:addStaticInfoOnly:]_block_invoke.337
+ ___116-[SASampleStore _addKCDataStackshot:timestamp:sampleIndex:shouldSkipSampleOut:primaryDataIsKPerf:addStaticInfoOnly:]_block_invoke.341
+ ___116-[SASampleStore _addKCDataStackshot:timestamp:sampleIndex:shouldSkipSampleOut:primaryDataIsKPerf:addStaticInfoOnly:]_block_invoke.346
+ ___116-[SASampleStore _addKCDataStackshot:timestamp:sampleIndex:shouldSkipSampleOut:primaryDataIsKPerf:addStaticInfoOnly:]_block_invoke.356
+ ___116-[SASampleStore _addKCDataStackshot:timestamp:sampleIndex:shouldSkipSampleOut:primaryDataIsKPerf:addStaticInfoOnly:]_block_invoke.361
+ ___116-[SASampleStore _addKCDataStackshot:timestamp:sampleIndex:shouldSkipSampleOut:primaryDataIsKPerf:addStaticInfoOnly:]_block_invoke.365
+ ___116-[SASampleStore _addKCDataStackshot:timestamp:sampleIndex:shouldSkipSampleOut:primaryDataIsKPerf:addStaticInfoOnly:]_block_invoke.371
+ ___116-[SASampleStore _addKCDataStackshot:timestamp:sampleIndex:shouldSkipSampleOut:primaryDataIsKPerf:addStaticInfoOnly:]_block_invoke.375
+ ___116-[SASampleStore _addKCDataStackshot:timestamp:sampleIndex:shouldSkipSampleOut:primaryDataIsKPerf:addStaticInfoOnly:]_block_invoke.379
+ ___116-[SASampleStore _addKCDataStackshot:timestamp:sampleIndex:shouldSkipSampleOut:primaryDataIsKPerf:addStaticInfoOnly:]_block_invoke.387
+ ___116-[SASampleStore _addKCDataStackshot:timestamp:sampleIndex:shouldSkipSampleOut:primaryDataIsKPerf:addStaticInfoOnly:]_block_invoke.420
+ ___116-[SASampleStore _addKCDataStackshot:timestamp:sampleIndex:shouldSkipSampleOut:primaryDataIsKPerf:addStaticInfoOnly:]_block_invoke_2.326
+ ___116-[SASampleStore _addKCDataStackshot:timestamp:sampleIndex:shouldSkipSampleOut:primaryDataIsKPerf:addStaticInfoOnly:]_block_invoke_2.351
+ ___116-[SASampleStore _addKCDataStackshot:timestamp:sampleIndex:shouldSkipSampleOut:primaryDataIsKPerf:addStaticInfoOnly:]_block_invoke_2.367
+ ___116-[SASampleStore _addKCDataStackshot:timestamp:sampleIndex:shouldSkipSampleOut:primaryDataIsKPerf:addStaticInfoOnly:]_block_invoke_2.399
+ ___116-[SASampleStore _addKCDataStackshot:timestamp:sampleIndex:shouldSkipSampleOut:primaryDataIsKPerf:addStaticInfoOnly:]_block_invoke_2.421
+ ___28-[SASampleStore postprocess]_block_invoke.161
+ ___28-[SASampleStore postprocess]_block_invoke_2.164
+ ___28-[SASampleStore postprocess]_block_invoke_3.168
+ ___31+[SASharedCache addDSCSymData:]_block_invoke.474
+ ___44-[SASampleStore enumerateTasksWithLiveness:]_block_invoke
+ ___48+[SASharedCache sharedCacheWithDyldSharedCache:]_block_invoke.465
+ ___ReadAheadTaskLevelInfo_block_invoke.1538
+ ___ReadAheadTaskLevelInfo_block_invoke.1542
+ ___ReadAheadTaskLevelInfo_block_invoke.1545
+ ___SATimeOfBootForLiveMachine_block_invoke
+ ___block_descriptor_32_e23_i48?0r*8r*16r*24Q32Q40l
+ ___block_descriptor_48_e8_32s40bs_e41_v32?0"NSNumber"8"NSMutableArray"16^B24ls32l8s40l8
+ ___block_descriptor_56_e8_32s40s48r_e19_v20?0"SATask"8B16ls32l8s40l8r48l8
+ ___block_descriptor_56_e8_32s40s_e19_v20?0"SATask"8B16ls32l8s40l8
+ ___block_literal_global.138
+ ___block_literal_global.1525
+ ___block_literal_global.1551
+ ___block_literal_global.1561
+ ___block_literal_global.1563
+ ___block_literal_global.163
+ ___block_literal_global.166
+ ___block_literal_global.171
+ ___block_literal_global.173
+ ___block_literal_global.175
+ ___block_literal_global.198
+ ___block_literal_global.200
+ ___block_literal_global.224
+ ___block_literal_global.233
+ ___block_literal_global.281
+ ___block_literal_global.288
+ ___block_literal_global.434
+ ___block_literal_global.457
+ ___block_literal_global.459
+ ___block_literal_global.462
+ ___block_literal_global.464
+ ___block_literal_global.472
+ ___block_literal_global.490
+ ___block_literal_global.505
+ ___block_literal_global.508
+ ___block_literal_global.59
+ ___block_literal_global.738
+ ___block_literal_global.83
+ ___block_literal_global.93
- -[SASampleStore taskForMicrostackshotTask:loadInfos:numLoadInfos:sharedCache:loadInfosIsPartial:timestamp:architecture:needAOTInfo:]
- -[SATask _matchesName:]
- -[SATask fixupFrameInstructionsWithDataGatheringOptions:inspectedLiveTask:uuidsWithNewInstructions:]
- GCC_except_table103
- GCC_except_table106
- GCC_except_table226
- GCC_except_table259
- GCC_except_table398
- GCC_except_table401
- GCC_except_table402
- GCC_except_table405
- _.str.77
- ___116-[SASampleStore _addKCDataStackshot:timestamp:sampleIndex:shouldSkipSampleOut:primaryDataIsKPerf:addStaticInfoOnly:]_block_invoke.277
- ___116-[SASampleStore _addKCDataStackshot:timestamp:sampleIndex:shouldSkipSampleOut:primaryDataIsKPerf:addStaticInfoOnly:]_block_invoke.285
- ___116-[SASampleStore _addKCDataStackshot:timestamp:sampleIndex:shouldSkipSampleOut:primaryDataIsKPerf:addStaticInfoOnly:]_block_invoke.323
- ___116-[SASampleStore _addKCDataStackshot:timestamp:sampleIndex:shouldSkipSampleOut:primaryDataIsKPerf:addStaticInfoOnly:]_block_invoke.327
- ___116-[SASampleStore _addKCDataStackshot:timestamp:sampleIndex:shouldSkipSampleOut:primaryDataIsKPerf:addStaticInfoOnly:]_block_invoke.331
- ___116-[SASampleStore _addKCDataStackshot:timestamp:sampleIndex:shouldSkipSampleOut:primaryDataIsKPerf:addStaticInfoOnly:]_block_invoke.335
- ___116-[SASampleStore _addKCDataStackshot:timestamp:sampleIndex:shouldSkipSampleOut:primaryDataIsKPerf:addStaticInfoOnly:]_block_invoke.340
- ___116-[SASampleStore _addKCDataStackshot:timestamp:sampleIndex:shouldSkipSampleOut:primaryDataIsKPerf:addStaticInfoOnly:]_block_invoke.345
- ___116-[SASampleStore _addKCDataStackshot:timestamp:sampleIndex:shouldSkipSampleOut:primaryDataIsKPerf:addStaticInfoOnly:]_block_invoke.355
- ___116-[SASampleStore _addKCDataStackshot:timestamp:sampleIndex:shouldSkipSampleOut:primaryDataIsKPerf:addStaticInfoOnly:]_block_invoke.360
- ___116-[SASampleStore _addKCDataStackshot:timestamp:sampleIndex:shouldSkipSampleOut:primaryDataIsKPerf:addStaticInfoOnly:]_block_invoke.364
- ___116-[SASampleStore _addKCDataStackshot:timestamp:sampleIndex:shouldSkipSampleOut:primaryDataIsKPerf:addStaticInfoOnly:]_block_invoke.370
- ___116-[SASampleStore _addKCDataStackshot:timestamp:sampleIndex:shouldSkipSampleOut:primaryDataIsKPerf:addStaticInfoOnly:]_block_invoke.374
- ___116-[SASampleStore _addKCDataStackshot:timestamp:sampleIndex:shouldSkipSampleOut:primaryDataIsKPerf:addStaticInfoOnly:]_block_invoke.378
- ___116-[SASampleStore _addKCDataStackshot:timestamp:sampleIndex:shouldSkipSampleOut:primaryDataIsKPerf:addStaticInfoOnly:]_block_invoke.381
- ___116-[SASampleStore _addKCDataStackshot:timestamp:sampleIndex:shouldSkipSampleOut:primaryDataIsKPerf:addStaticInfoOnly:]_block_invoke.419
- ___116-[SASampleStore _addKCDataStackshot:timestamp:sampleIndex:shouldSkipSampleOut:primaryDataIsKPerf:addStaticInfoOnly:]_block_invoke_2.325
- ___116-[SASampleStore _addKCDataStackshot:timestamp:sampleIndex:shouldSkipSampleOut:primaryDataIsKPerf:addStaticInfoOnly:]_block_invoke_2.350
- ___116-[SASampleStore _addKCDataStackshot:timestamp:sampleIndex:shouldSkipSampleOut:primaryDataIsKPerf:addStaticInfoOnly:]_block_invoke_2.366
- ___116-[SASampleStore _addKCDataStackshot:timestamp:sampleIndex:shouldSkipSampleOut:primaryDataIsKPerf:addStaticInfoOnly:]_block_invoke_2.398
- ___116-[SASampleStore _addKCDataStackshot:timestamp:sampleIndex:shouldSkipSampleOut:primaryDataIsKPerf:addStaticInfoOnly:]_block_invoke_2.420
- ___28-[SASampleStore postprocess]_block_invoke.160
- ___28-[SASampleStore postprocess]_block_invoke_2.163
- ___28-[SASampleStore postprocess]_block_invoke_3.167
- ___31+[SASharedCache addDSCSymData:]_block_invoke.471
- ___ReadAheadTaskLevelInfo_block_invoke.1537
- ___ReadAheadTaskLevelInfo_block_invoke.1541
- ___ReadAheadTaskLevelInfo_block_invoke.1544
- ___block_descriptor_56_e8_32s40s_e41_v32?0"NSNumber"8"NSMutableArray"16^B24ls32l8s40l8
- ___block_literal_global.1524
- ___block_literal_global.1550
- ___block_literal_global.1560
- ___block_literal_global.1562
- ___block_literal_global.162
- ___block_literal_global.165
- ___block_literal_global.170
- ___block_literal_global.172
- ___block_literal_global.174
- ___block_literal_global.197
- ___block_literal_global.199
- ___block_literal_global.223
- ___block_literal_global.232
- ___block_literal_global.280
- ___block_literal_global.287
- ___block_literal_global.433
- ___block_literal_global.456
- ___block_literal_global.458
- ___block_literal_global.461
- ___block_literal_global.463
- ___block_literal_global.471
- ___block_literal_global.489
- ___block_literal_global.504
- ___block_literal_global.506
- ___block_literal_global.507
- ___block_literal_global.56
- ___block_literal_global.735
- ___block_literal_global.80
- ___block_literal_global.91
CStrings:
+ "%@: live process has changed %@ -> %@"
+ "Unable to find shared cache %@ in live system nor via dscsym"
+ "Unable to find shared cache %@ in live system, but found via dscsym"
+ "_pid != SA_KERNEL_PID"
+ "correspondsToName called for kernel"
+ "v20@?0@\"SATask\"8B16"
- "%@: live process has changed to %@"

```
