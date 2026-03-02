## GPUToolsCapture

> `/System/Library/PrivateFrameworks/GPUToolsCapture.framework/GPUToolsCapture`

```diff

-314.10.0.0.0
-  __TEXT.__text: 0x268784
-  __TEXT.__auth_stubs: 0x1780
+314.12.0.0.0
+  __TEXT.__text: 0x2785ec
+  __TEXT.__auth_stubs: 0x1770
   __TEXT.__objc_stubs: 0x17120
   __TEXT.__init_offsets: 0x4
   __TEXT.__objc_methlist: 0x12adc
-  __TEXT.__const: 0x46e0
-  __TEXT.__cstring: 0x27cc1
+  __TEXT.__const: 0x46c0
+  __TEXT.__cstring: 0x27a51
   __TEXT.__gcc_except_tab: 0xd38
   __TEXT.__objc_methname: 0x1a81e
   __TEXT.__objc_classname: 0x15f1
   __TEXT.__objc_methtype: 0xab28
   __TEXT.__oslogstring: 0x16fa
   __TEXT.__ustring: 0x20a
-  __TEXT.__unwind_info: 0x43d8
-  __DATA_CONST.__auth_got: 0xbd8
+  __TEXT.__unwind_info: 0x43d0
+  __DATA_CONST.__auth_got: 0xbd0
   __DATA_CONST.__got: 0x7f8
   __DATA_CONST.__auth_ptr: 0x10
   __DATA_CONST.__const: 0x1dd8

   - /usr/lib/libcompression.dylib
   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libz.1.dylib
-  UUID: 142F10CA-D09D-35F5-AC4A-9997167E7BC7
+  UUID: C875CFE8-8A80-3760-97CF-908532F35F72
   Functions: 7925
-  Symbols:   47148
-  CStrings:  9412
+  Symbols:   47147
+  CStrings:  9410
 
Symbols:
+ /Library/Caches/com.apple.xbs/D01B8030-B32B-4734-B85F-7B0938CB9278/TemporaryDirectory.6SJV6y/Binaries/GPUToolsDevice/install/TempContent/Objects/GPUToolsFoundation.build/GPUToolsCapture.build/DerivedSources/
+ /Library/Caches/com.apple.xbs/D01B8030-B32B-4734-B85F-7B0938CB9278/TemporaryDirectory.6SJV6y/Binaries/GPUToolsDevice/install/TempContent/Objects/GPUToolsFoundation.build/GPUToolsCapture.build/Objects-normal/arm64e/GPUToolsCapture_lto.o
+ GetStream.20267
+ StoreMTLCompileOptionsUsingEncode.16694
+ __ZNSt3__16vectorI16GTTelemetryLayerNS_9allocatorIS1_EEE20__throw_length_errorB9nqn210106Ev
+ __ZNSt3__16vectorI16GTTelemetryQueueNS_9allocatorIS1_EEE20__throw_length_errorB9nqn210106Ev
+ __ZNSt3__16vectorI16GTTelemetryQueueNS_9allocatorIS1_EEE9push_backB9nqn210106ERKS1_
+ __ZNSt3__16vectorI17GTTelemetryDeviceNS_9allocatorIS1_EEE20__throw_length_errorB9nqn210106Ev
+ __ZSt28__throw_bad_array_new_lengthB9nqn210106v
+ __block_descriptor_tmp.15387
+ __block_literal_global.15486
+ __block_literal_global.15556
+ __block_literal_global.15570
+ __block_literal_global.20652
+ name_array.16639
- /Library/Caches/com.apple.xbs/EC5DAD33-C7A6-479B-B9F7-2785559D39E5/TemporaryDirectory.7DxQry/Binaries/GPUToolsDevice/install/TempContent/Objects/GPUToolsFoundation.build/GPUToolsCapture.build/DerivedSources/
- /Library/Caches/com.apple.xbs/EC5DAD33-C7A6-479B-B9F7-2785559D39E5/TemporaryDirectory.7DxQry/Binaries/GPUToolsDevice/install/TempContent/Objects/GPUToolsFoundation.build/GPUToolsCapture.build/Objects-normal/arm64e/GPUToolsCapture_lto.o
- GetStream.20270
- StoreMTLCompileOptionsUsingEncode.16696
- __ZNSt3__132__internal_log_hardening_failureEPKc
- __ZNSt3__16vectorI16GTTelemetryLayerNS_9allocatorIS1_EEE20__throw_length_errorB9fon210106Ev
- __ZNSt3__16vectorI16GTTelemetryQueueNS_9allocatorIS1_EEE20__throw_length_errorB9fon210106Ev
- __ZNSt3__16vectorI16GTTelemetryQueueNS_9allocatorIS1_EEE9push_backB9fon210106ERKS1_
- __ZNSt3__16vectorI17GTTelemetryDeviceNS_9allocatorIS1_EEE20__throw_length_errorB9fon210106Ev
- __ZSt28__throw_bad_array_new_lengthB9fon210106v
- __block_descriptor_tmp.15389
- __block_literal_global.15488
- __block_literal_global.15558
- __block_literal_global.15572
- __block_literal_global.20655
- name_array.16641
Functions:
~ _GTTelemetry_removeStreamRef : 260 -> 168
~ _GTTelemetry_removeCommandQueue : 264 -> 172
~ _GTTelemetry_removeMTL4CommandQueue : 264 -> 172
~ _GTTelemetry_stats : 2248 -> 480
~ _GTTraceFuncToFbuf : 381132 -> 449328
~ _DumpDeviceResources : 82052 -> 81492
~ _WriteGTMTLSMFence : 620 -> 628
~ _WriteGTMTLSMEvent : 620 -> 628
~ _WriteGTMTLSMLateEvalEvent : 632 -> 640
~ _WriteGTMTLSMSharedEvent : 1148 -> 1108
~ _WriteGTMTLSMFunctionHandle : 1536 -> 1420
~ _WriteGTMTLSMVisibleFunctionTable : 1464 -> 1416
~ _WriteGTMTLIntersectionFunctionTable : 1876 -> 1744
~ _WriteGTMTLSMTextureViewPool : 1504 -> 1408
~ _WriteBufferInfo : 972 -> 916
CStrings:
- "/AppleInternal/Library/BuildRoots/4~CJInugDz3Hivhcv6JwAyROPneKktez0TvG7LEXg/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/__vector/vector.h:406: libc++ Hardening assertion __n < size() failed: vector[] index out of bounds\n"
- "/AppleInternal/Library/BuildRoots/4~CJInugDz3Hivhcv6JwAyROPneKktez0TvG7LEXg/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/__vector/vector.h:486: libc++ Hardening assertion !empty() failed: vector::pop_back called on an empty vector\n"

```
