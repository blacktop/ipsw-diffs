## OpenAL

> `/System/iOSSupport/System/Library/Frameworks/OpenAL.framework/Versions/A/OpenAL`

```diff

 82.0.0.0.0
-  __TEXT.__text: 0x26f80
+  __TEXT.__text: 0x26a8c
   __TEXT.__auth_stubs: 0x760
-  __TEXT.__gcc_except_tab: 0x161c
+  __TEXT.__gcc_except_tab: 0x1604
   __TEXT.__cstring: 0x638a
   __TEXT.__const: 0x188
   __TEXT.__dof_OpenAL: 0xcf6
-  __TEXT.__unwind_info: 0xa48
+  __TEXT.__unwind_info: 0xa08
   __DATA_CONST.__got: 0x50
   __DATA_CONST.__const: 0xd8
   __AUTH_CONST.__auth_got: 0x3b8

   - /System/Library/Frameworks/CoreFoundation.framework/Versions/A/CoreFoundation
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libc++.1.dylib
-  UUID: 9F231396-D31B-375F-AADB-CA58DF4C02F3
-  Functions: 423
+  UUID: FDCD3D44-F4D4-3464-9BDA-5D996B3748B3
+  Functions: 401
   Symbols:   727
   CStrings:  725
 
Symbols:
+ _ZN5CALog5printEiPKc.cold.1
+ _ZN5CALog8InstanceEv.cold.1
+ __ZNKSt3__16vectorI10BufferInfoNS_9allocatorIS1_EEE20__throw_length_errorB8ne190102Ev
+ __ZNKSt3__16vectorI16SourceNotifyInfoNS_9allocatorIS1_EEE20__throw_length_errorB8ne190102Ev
+ __ZNKSt3__16vectorI18SourceAttachedInfoNS_9allocatorIS1_EEE20__throw_length_errorB8ne190102Ev
+ __ZNKSt3__16vectorINS_4pairIyPN5CALog5ScopeEEENS_9allocatorIS5_EEE20__throw_length_errorB8ne190102Ev
+ __ZNSt12length_errorC1B8ne190102EPKc
+ __ZNSt3__113__tree_removeB8ne190102IPNS_16__tree_node_baseIPvEEEEvT_S5_
+ __ZNSt3__120__throw_length_errorB8ne190102EPKc
+ __ZNSt3__127__tree_balance_after_insertB8ne190102IPNS_16__tree_node_baseIPvEEEEvT_S5_
+ __ZSt28__throw_bad_array_new_lengthB8ne190102v
- __ZN18AttachedSourceList3AddER18SourceAttachedInfo
- __ZN9OALSource26PrepBufferQueueForPlaybackEv
- __ZNKSt3__16vectorI10BufferInfoNS_9allocatorIS1_EEE20__throw_length_errorB8ne180100Ev
- __ZNKSt3__16vectorI16SourceNotifyInfoNS_9allocatorIS1_EEE20__throw_length_errorB8ne180100Ev
- __ZNKSt3__16vectorI18SourceAttachedInfoNS_9allocatorIS1_EEE20__throw_length_errorB8ne180100Ev
- __ZNKSt3__16vectorINS_4pairIyPN5CALog5ScopeEEENS_9allocatorIS5_EEE20__throw_length_errorB8ne180100Ev
- __ZNSt12length_errorC1B8ne180100EPKc
- __ZNSt3__113__tree_removeB8ne180100IPNS_16__tree_node_baseIPvEEEEvT_S5_
- __ZNSt3__120__throw_length_errorB8ne180100EPKc
- __ZNSt3__127__tree_balance_after_insertB8ne180100IPNS_16__tree_node_baseIPvEEEEvT_S5_
- __ZSt28__throw_bad_array_new_lengthB8ne180100v
CStrings:
+ "/AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/EmbeddedOpenAL/Aspen/OpenAL/oalBuffer.cpp"
+ "/AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/EmbeddedOpenAL/Aspen/OpenAL/oalCaptureDevice.cpp"
+ "/AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/EmbeddedOpenAL/Aspen/OpenAL/oalCaptureMixer.cpp"
+ "/AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/EmbeddedOpenAL/Aspen/OpenAL/oalContext.cpp"
+ "/AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/EmbeddedOpenAL/Aspen/OpenAL/oalDevice.cpp"
+ "/AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/EmbeddedOpenAL/Aspen/OpenAL/oalImp.cpp"
+ "/AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/EmbeddedOpenAL/Aspen/OpenAL/oalSource.cpp"
- "/AppleInternal/Library/BuildRoots/d187755d-b9a3-11ef-83e5-aabfac210453/Library/Caches/com.apple.xbs/Sources/EmbeddedOpenAL/Aspen/OpenAL/oalBuffer.cpp"
- "/AppleInternal/Library/BuildRoots/d187755d-b9a3-11ef-83e5-aabfac210453/Library/Caches/com.apple.xbs/Sources/EmbeddedOpenAL/Aspen/OpenAL/oalCaptureDevice.cpp"
- "/AppleInternal/Library/BuildRoots/d187755d-b9a3-11ef-83e5-aabfac210453/Library/Caches/com.apple.xbs/Sources/EmbeddedOpenAL/Aspen/OpenAL/oalCaptureMixer.cpp"
- "/AppleInternal/Library/BuildRoots/d187755d-b9a3-11ef-83e5-aabfac210453/Library/Caches/com.apple.xbs/Sources/EmbeddedOpenAL/Aspen/OpenAL/oalContext.cpp"
- "/AppleInternal/Library/BuildRoots/d187755d-b9a3-11ef-83e5-aabfac210453/Library/Caches/com.apple.xbs/Sources/EmbeddedOpenAL/Aspen/OpenAL/oalDevice.cpp"
- "/AppleInternal/Library/BuildRoots/d187755d-b9a3-11ef-83e5-aabfac210453/Library/Caches/com.apple.xbs/Sources/EmbeddedOpenAL/Aspen/OpenAL/oalImp.cpp"
- "/AppleInternal/Library/BuildRoots/d187755d-b9a3-11ef-83e5-aabfac210453/Library/Caches/com.apple.xbs/Sources/EmbeddedOpenAL/Aspen/OpenAL/oalSource.cpp"

```
