## OpenAL

> `/System/Library/Frameworks/OpenAL.framework/OpenAL`

```diff

 84.1.0.0.0
-  __TEXT.__text: 0x254e4
-  __TEXT.__auth_stubs: 0x630
+  __TEXT.__text: 0x25404
+  __TEXT.__auth_stubs: 0x620
   __TEXT.__gcc_except_tab: 0x183c
   __TEXT.__const: 0x1ef
-  __TEXT.__cstring: 0x16c3
+  __TEXT.__cstring: 0x1562
   __TEXT.__oslogstring: 0x3246
   __TEXT.__dof_OpenAL: 0xcf6
   __TEXT.__unwind_info: 0xa38
   __DATA_CONST.__got: 0x50
   __DATA_CONST.__const: 0x70
-  __AUTH_CONST.__auth_got: 0x320
+  __AUTH_CONST.__auth_got: 0x318
   __AUTH_CONST.__const: 0x158
   __DATA.__data: 0x138
   __DATA.__common: 0x2a4

   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libc++.1.dylib
-  UUID: 86D22AD9-133D-3481-B2D0-A29C13C26AF7
+  UUID: 955C366F-B0F2-3DA2-BC45-E844F0D47A2E
   Functions: 416
-  Symbols:   1074
-  CStrings:  514
+  Symbols:   1073
+  CStrings:  513
 
Symbols:
+ __ZNSt12length_errorC1B9nqe210106EPKc
+ __ZNSt3__113__tree_removeB9nqe210106IPNS_16__tree_node_baseIPvEEEEvT_S5_
+ __ZNSt3__120__throw_length_errorB9nqe210106EPKc
+ __ZNSt3__127__tree_balance_after_insertB9nqe210106IPNS_16__tree_node_baseIPvEEEEvT_S5_
+ __ZNSt3__16vectorI10BufferInfoNS_9allocatorIS1_EEE20__throw_length_errorB9nqe210106Ev
+ __ZNSt3__16vectorI10BufferInfoNS_9allocatorIS1_EEE9push_backB9nqe210106EOS1_
+ __ZNSt3__16vectorI16SourceNotifyInfoNS_9allocatorIS1_EEE20__throw_length_errorB9nqe210106Ev
+ __ZNSt3__16vectorI16SourceNotifyInfoNS_9allocatorIS1_EEE9push_backB9nqe210106ERKS1_
+ __ZNSt3__16vectorI18SourceAttachedInfoNS_9allocatorIS1_EEE20__throw_length_errorB9nqe210106Ev
+ __ZNSt3__16vectorI18SourceAttachedInfoNS_9allocatorIS1_EEE9push_backB9nqe210106EOS1_
+ __ZSt28__throw_bad_array_new_lengthB9nqe210106v
- __ZNSt12length_errorC1B9foe210106EPKc
- __ZNSt3__113__tree_removeB9foe210106IPNS_16__tree_node_baseIPvEEEEvT_S5_
- __ZNSt3__120__throw_length_errorB9foe210106EPKc
- __ZNSt3__127__tree_balance_after_insertB9foe210106IPNS_16__tree_node_baseIPvEEEEvT_S5_
- __ZNSt3__132__internal_log_hardening_failureEPKc
- __ZNSt3__16vectorI10BufferInfoNS_9allocatorIS1_EEE20__throw_length_errorB9foe210106Ev
- __ZNSt3__16vectorI10BufferInfoNS_9allocatorIS1_EEE9push_backB9foe210106EOS1_
- __ZNSt3__16vectorI16SourceNotifyInfoNS_9allocatorIS1_EEE20__throw_length_errorB9foe210106Ev
- __ZNSt3__16vectorI16SourceNotifyInfoNS_9allocatorIS1_EEE9push_backB9foe210106ERKS1_
- __ZNSt3__16vectorI18SourceAttachedInfoNS_9allocatorIS1_EEE20__throw_length_errorB9foe210106Ev
- __ZNSt3__16vectorI18SourceAttachedInfoNS_9allocatorIS1_EEE9push_backB9foe210106EOS1_
- __ZSt28__throw_bad_array_new_lengthB9foe210106v
Functions:
~ __ZN9OALSource16FlushBufferQueueEv : 468 -> 368
~ __ZN9OALSource22RemoveBuffersFromQueueEjPj : 1376 -> 1336
~ __ZN9OALSource32PostRenderRemoveBuffersFromQueueEj : 588 -> 540
~ __ZN9OALSource27PostRenderAddBuffersToQueueEj : 584 -> 548
CStrings:
- "/AppleInternal/Library/BuildRoots/4~CJlJugCiV0CJNyANJ4OO3u5u3Tj_A1x-lrhCOFA/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/__vector/vector.h:1162: libc++ Hardening assertion __position != end() failed: vector::erase(iterator) called with a non-dereferenceable iterator\n"

```
