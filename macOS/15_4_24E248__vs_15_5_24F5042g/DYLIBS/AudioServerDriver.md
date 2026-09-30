## AudioServerDriver

> `/System/Library/PrivateFrameworks/AudioServerDriver.framework/Versions/A/AudioServerDriver`

```diff

-1040.10.0.0.0
-  __TEXT.__text: 0x62fcc
+1050.4.1.0.0
+  __TEXT.__text: 0x63880
   __TEXT.__auth_stubs: 0xd50
-  __TEXT.__objc_methlist: 0x3554
-  __TEXT.__gcc_except_tab: 0x30d4
+  __TEXT.__objc_methlist: 0x35bc
+  __TEXT.__gcc_except_tab: 0x3140
   __TEXT.__const: 0x7ac
-  __TEXT.__cstring: 0x39dd
-  __TEXT.__oslogstring: 0x26d2
+  __TEXT.__cstring: 0x3b38
+  __TEXT.__oslogstring: 0x26f1
   __TEXT.__dof_ASDInterf: 0xe5f
-  __TEXT.__unwind_info: 0x1e90
+  __TEXT.__unwind_info: 0x1ed8
   __TEXT.__eh_frame: 0x100
-  __TEXT.__objc_classname: 0x3c6
-  __TEXT.__objc_methname: 0x5f48
+  __TEXT.__objc_classname: 0x3c7
+  __TEXT.__objc_methname: 0x5fa0
   __TEXT.__objc_methtype: 0x22cb
-  __TEXT.__objc_stubs: 0x3da0
+  __TEXT.__objc_stubs: 0x3dc0
   __DATA_CONST.__got: 0x268
   __DATA_CONST.__const: 0x1a0
   __DATA_CONST.__objc_classlist: 0x160
   __DATA_CONST.__objc_catlist: 0x8
   __DATA_CONST.__objc_protolist: 0x38
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x1600
+  __DATA_CONST.__objc_selrefs: 0x1610
   __DATA_CONST.__objc_superrefs: 0x138
   __DATA_CONST.__objc_arraydata: 0x10
   __AUTH_CONST.__auth_got: 0x6c0
-  __AUTH_CONST.__const: 0x10b0
-  __AUTH_CONST.__cfstring: 0x22e0
-  __AUTH_CONST.__objc_const: 0x6078
+  __AUTH_CONST.__const: 0x10e0
+  __AUTH_CONST.__cfstring: 0x2300
+  __AUTH_CONST.__objc_const: 0x60a8
   __AUTH_CONST.__objc_intobj: 0x18
   __AUTH_CONST.__objc_dictobj: 0x28
   __AUTH.__objc_data: 0xdc0
-  __DATA.__objc_ivar: 0x4bc
+  __DATA.__objc_ivar: 0x4c0
   __DATA.__data: 0x3c8
   __DATA.__bss: 0xf8
   __DATA.__common: 0x10

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libc++.1.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 2162
-  Symbols:   4225
-  CStrings:  2129
+  Functions: 2180
+  Symbols:   4257
+  CStrings:  2139
 
Symbols:
+ -[ASDAudioDevice setSupportsIsolatedIO:]
+ -[ASDAudioDevice supportsIsolatedIO]
+ -[ASDDSPAudioDevice setSupportsIsolatedIO:]
+ -[ASDDSPAudioDevice supportsIsolatedIO]
+ -[ASDDSPStream readIsolatedInputBlock]
+ -[ASDSRCAudioDevice setSupportsIsolatedIO:]
+ -[ASDSRCAudioDevice supportsIsolatedIO]
+ -[ASDSRCStream readIsolatedInputBlock]
+ GCC_except_table110
+ GCC_except_table123
+ GCC_except_table144
+ GCC_except_table145
+ GCC_except_table154
+ GCC_except_table157
+ GCC_except_table162
+ GCC_except_table186
+ GCC_except_table97
+ OBJC_IVAR_$_ASDAudioDevice._supportsIsolatedIO
+ _ZN18ASDDSPStreamHelper17readIsolatedInputEyjPK28AudioServerPlugInIOCycleInfo.cold.1
+ _ZN18ASDDSPStreamHelper17readIsolatedInputEyjPK28AudioServerPlugInIOCycleInfo.cold.2
+ _ZN18ASDDSPStreamHelper17readIsolatedInputEyjPK28AudioServerPlugInIOCycleInfo.cold.3
+ _ZN18ASDDSPStreamHelper17readIsolatedInputEyjPK28AudioServerPlugInIOCycleInfo.cold.4
+ _ZN18ASDDSPStreamHelper17readIsolatedInputEyjPK28AudioServerPlugInIOCycleInfo.cold.5
+ _ZN18ASDDSPStreamHelper17readIsolatedInputEyjPK28AudioServerPlugInIOCycleInfo.cold.6
+ _ZN18ASDDSPStreamHelper9readInputEjPK28AudioServerPlugInIOCycleInfoPvS3_j.cold.12
+ _ZN18ASDSRCStreamHelper17readIsolatedInputEyjPK28AudioServerPlugInIOCycleInfo.cold.1
+ _ZN18ASDSRCStreamHelper17readIsolatedInputEyjPK28AudioServerPlugInIOCycleInfo.cold.2
+ _ZN18ASDSRCStreamHelper17readIsolatedInputEyjPK28AudioServerPlugInIOCycleInfo.cold.3
+ __38-[ASDDSPStream readIsolatedInputBlock]_block_invoke.cold.1
+ __38-[ASDSRCStream readIsolatedInputBlock]_block_invoke.cold.1
+ __ZN18ASDDSPStreamHelper17readIsolatedInputEyjPK28AudioServerPlugInIOCycleInfo
+ __ZN18ASDDSPStreamHelper9DSPStream17readIsolatedInputEyjPK28AudioServerPlugInIOCycleInfo
+ __ZN18ASDDSPStreamHelper9DSPStreamC1E18ASDStreamDirection24CAStreamBasicDescriptionU13block_pointerFijPK28AudioServerPlugInIOCycleInfoPvS6_jES8_U13block_pointerFiyjS5_E
+ __ZN18ASDDSPStreamHelper9DSPStreamC2E18ASDStreamDirection24CAStreamBasicDescriptionU13block_pointerFijPK28AudioServerPlugInIOCycleInfoPvS6_jES8_U13block_pointerFiyjS5_E
+ __ZN18ASDSRCStreamHelper17readIsolatedInputEyjPK28AudioServerPlugInIOCycleInfo
+ __ZN18ASDSRCStreamHelper38ASDUnderlyingStreamDoIOOperationBlocksD1Ev
+ __ZNKSt3__129_AllocatorDestroyRangeReverseINS_9allocatorIN18ASDSRCStreamHelper38ASDUnderlyingStreamDoIOOperationBlocksEEEPS3_EclB8ne190102Ev
+ __ZNSt3__114__split_bufferIN18ASDSRCStreamHelper38ASDUnderlyingStreamDoIOOperationBlocksERNS_9allocatorIS2_EEE5clearB8ne190102Ev
+ __ZNSt3__16vectorIN18ASDDSPStreamHelper9DSPStreamENS_9allocatorIS2_EEE22__construct_one_at_endB8ne190102IJ18ASDStreamDirection27AudioStreamBasicDescriptionU8__strongU13block_pointerFijPK28AudioServerPlugInIOCycleInfoPvSC_jESF_U8__strongU13block_pointerFiyjSB_EEEEvDpOT_
+ __ZNSt3__16vectorIN18ASDDSPStreamHelper9DSPStreamENS_9allocatorIS2_EEE24__emplace_back_slow_pathIJ18ASDStreamDirection27AudioStreamBasicDescriptionU8__strongU13block_pointerFijPK28AudioServerPlugInIOCycleInfoPvSC_jESF_U8__strongU13block_pointerFiyjSB_EEEEPS2_DpOT_
+ __ZNSt3__16vectorIN18ASDSRCStreamHelper38ASDUnderlyingStreamDoIOOperationBlocksENS_9allocatorIS2_EEE12emplace_backIJRS2_EEES7_DpOT_
+ __ZNSt3__19allocatorIN18ASDSRCStreamHelper38ASDUnderlyingStreamDoIOOperationBlocksEE7destroyB8ne190102EPS2_
+ __ZNSt3__19allocatorIN18ASDSRCStreamHelper38ASDUnderlyingStreamDoIOOperationBlocksEE9constructB8ne190102IS2_JRS2_EEEvPT_DpOT0_
+ ___38-[ASDDSPStream readIsolatedInputBlock]_block_invoke
+ ___38-[ASDSRCStream readIsolatedInputBlock]_block_invoke
+ ___block_descriptor_40_ea8_32r_e187_i28?0Q8I16r^{AudioServerPlugInIOCycleInfo=QI{AudioTimeStamp=dQdQ{SMPTETime=ssIIIssss}II}{AudioTimeStamp=dQdQ{SMPTETime=ssIIIssss}II}{AudioTimeStamp=dQdQ{SMPTETime=ssIIIssss}II}(?=dd)d}20l
+ _objc_msgSend$supportsIsolatedIO
- GCC_except_table108
- GCC_except_table121
- GCC_except_table142
- GCC_except_table143
- GCC_except_table152
- GCC_except_table153
- GCC_except_table158
- GCC_except_table182
- GCC_except_table61
- GCC_except_table91
- GCC_except_table95
- __ZN18ASDDSPStreamHelper9DSPStreamC1E18ASDStreamDirection24CAStreamBasicDescriptionU13block_pointerFijPK28AudioServerPlugInIOCycleInfoPvS6_jES8_
- __ZN18ASDDSPStreamHelper9DSPStreamC2E18ASDStreamDirection24CAStreamBasicDescriptionU13block_pointerFijPK28AudioServerPlugInIOCycleInfoPvS6_jES8_
- __ZNSt3__114__split_bufferIN18ASDSRCStreamHelper38ASDUnderlyingStreamDoIOOperationBlocksERNS_9allocatorIS2_EEE17__destruct_at_endB8ne190102EPS2_
- __ZNSt3__119__allocator_destroyB8ne190102INS_9allocatorIN18ASDSRCStreamHelper38ASDUnderlyingStreamDoIOOperationBlocksEEENS_16reverse_iteratorIPS3_EES7_EEvRT_T0_T1_
- __ZNSt3__16vectorIN18ASDDSPStreamHelper9DSPStreamENS_9allocatorIS2_EEE22__construct_one_at_endB8ne190102IJ18ASDStreamDirection27AudioStreamBasicDescriptionU8__strongU13block_pointerFijPK28AudioServerPlugInIOCycleInfoPvSC_jESF_EEEvDpOT_
- __ZNSt3__16vectorIN18ASDDSPStreamHelper9DSPStreamENS_9allocatorIS2_EEE22__construct_one_at_endB8ne190102IJRKS2_EEEvDpOT_
- __ZNSt3__16vectorIN18ASDDSPStreamHelper9DSPStreamENS_9allocatorIS2_EEE24__emplace_back_slow_pathIJ18ASDStreamDirection27AudioStreamBasicDescriptionU8__strongU13block_pointerFijPK28AudioServerPlugInIOCycleInfoPvSC_jESF_EEEPS2_DpOT_
- __ZNSt3__16vectorIN18ASDSRCStreamHelper38ASDUnderlyingStreamDoIOOperationBlocksENS_9allocatorIS2_EEE22__base_destruct_at_endB8ne190102EPS2_
CStrings:
+ "\x06\x12\x123\xf0\x1f\x01"
+ " Failed bypassed DSP readInput"
+ "%@|    Supports Isolated IO: %@\n"
+ "-[ASDDSPStream readIsolatedInputBlock]_block_invoke"
+ "-[ASDSRCStream readIsolatedInputBlock]_block_invoke"
+ "/AppleInternal/Library/BuildRoots/1d1afd2a-039a-11f0-91c4-fe9e33ca05fa/Applications/Xcode.app/Contents/Developer/Platforms/MacOSX.platform/Developer/SDKs/MacOSX15.5.Internal.sdk/System/Library/PrivateFrameworks/AudioToolboxCore.framework/PrivateHeaders/DSPGraph_Box.h"
+ "/AppleInternal/Library/BuildRoots/1d1afd2a-039a-11f0-91c4-fe9e33ca05fa/Library/Caches/com.apple.xbs/Sources/AudioServerDriver/AudioServerDriver/ASDInterface.mm"
+ "/AppleInternal/Library/BuildRoots/1d1afd2a-039a-11f0-91c4-fe9e33ca05fa/Library/Caches/com.apple.xbs/Sources/AudioServerDriver/AudioServerDriver/DSP/ASDDSPStreamHelper.mm"
+ "/AppleInternal/Library/BuildRoots/1d1afd2a-039a-11f0-91c4-fe9e33ca05fa/Library/Caches/com.apple.xbs/Sources/AudioServerDriver/AudioServerDriver/DSP/ASDRingBufferStream.mm"
+ "/AppleInternal/Library/BuildRoots/1d1afd2a-039a-11f0-91c4-fe9e33ca05fa/Library/Caches/com.apple.xbs/Sources/AudioServerDriver/AudioServerDriver/DSP/ASDSRCStreamHelper.mm"
+ "/AppleInternal/Library/BuildRoots/1d1afd2a-039a-11f0-91c4-fe9e33ca05fa/Library/Caches/com.apple.xbs/Sources/AudioServerDriver/AudioServerDriver/DSP/DSPGraph_GraphBox.cpp"
+ "/AppleInternal/Library/BuildRoots/1d1afd2a-039a-11f0-91c4-fe9e33ca05fa/Library/Caches/com.apple.xbs/Sources/AudioServerDriver/AudioServerDriver/DSP/DSPGraph_GraphFactory.cpp"
+ "/AppleInternal/Library/BuildRoots/1d1afd2a-039a-11f0-91c4-fe9e33ca05fa/Library/Caches/com.apple.xbs/Sources/AudioServerDriver/Utility/CABufferList.h"
+ "/AppleInternal/Library/BuildRoots/1d1afd2a-039a-11f0-91c4-fe9e33ca05fa/Library/Caches/com.apple.xbs/Sources/AudioServerDriver/Utility/CALog.cpp"
+ "NULL == inIOCycleInfo"
+ "TB,N,V_supportsIsolatedIO"
+ "_supportsIsolatedIO"
+ "i28@?0Q8I16r^{AudioServerPlugInIOCycleInfo=QI{AudioTimeStamp=dQdQ{SMPTETime=ssIIIssss}II}{AudioTimeStamp=dQdQ{SMPTETime=ssIIIssss}II}{AudioTimeStamp=dQdQ{SMPTETime=ssIIIssss}II}(?=dd)d}20"
+ "setSupportsIsolatedIO:"
+ "supportsIsolatedIO"
+ "\xf0\xf0\xf0Q"
- "\x06\x12\x123\xff\x01"
- "/AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Applications/Xcode.app/Contents/Developer/Platforms/MacOSX.platform/Developer/SDKs/MacOSX15.4.Internal.sdk/System/Library/PrivateFrameworks/AudioToolboxCore.framework/PrivateHeaders/DSPGraph_Box.h"
- "/AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/AudioServerDriver/AudioServerDriver/ASDInterface.mm"
- "/AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/AudioServerDriver/AudioServerDriver/DSP/ASDDSPStreamHelper.mm"
- "/AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/AudioServerDriver/AudioServerDriver/DSP/ASDRingBufferStream.mm"
- "/AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/AudioServerDriver/AudioServerDriver/DSP/ASDSRCStreamHelper.mm"
- "/AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/AudioServerDriver/AudioServerDriver/DSP/DSPGraph_GraphBox.cpp"
- "/AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/AudioServerDriver/AudioServerDriver/DSP/DSPGraph_GraphFactory.cpp"
- "/AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/AudioServerDriver/Utility/CABufferList.h"
- "/AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/AudioServerDriver/Utility/CALog.cpp"
- "\xf0\xf0\xf0A"

```
