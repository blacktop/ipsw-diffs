## AppleMipcRouter

> `/System/Library/PrivateFrameworks/AppleMipcRouter.framework/AppleMipcRouter`

```diff

-1397.0.0.0.0
-  __TEXT.__text: 0x4a94c
+1399.2.0.0.0
+  __TEXT.__text: 0x4a99c
   __TEXT.__auth_stubs: 0xa70
   __TEXT.__const: 0x3cf8
   __TEXT.__gcc_except_tab: 0x4750
-  __TEXT.__cstring: 0xd94
+  __TEXT.__cstring: 0xda4
   __TEXT.__oslogstring: 0x2135
   __TEXT.__unwind_info: 0x16a0
   __DATA_CONST.__got: 0x140

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libTelephonyUtilDynamic.dylib
   - /usr/lib/libc++.1.dylib
-  UUID: FECA303B-4CDE-323A-9AE9-EADE71E79161
+  UUID: 891EB13E-309D-36D1-81FE-B244897CF582
   Functions: 869
   Symbols:   2562
   CStrings:  362
Functions:
~ __ZNSt3__16vectorINS_4pairIN3abb6router7MessageENS_8functionIFvS4_EEEEENS_9allocatorIS8_EEE13shrink_to_fitEv : 268 -> 272
~ __ZNSt3__16vectorINS_4pairIN3abb6router7MessageENS_8functionIFvS4_EEEEENS_9allocatorIS8_EEE24__emplace_back_slow_pathIJS8_EEEPS8_DpOT_ : 420 -> 432
~ __ZNKSt3__120__shared_ptr_pointerIPN3abb6router5AgentEZN3ctu20SharedSynchronizableIS3_E15make_shared_ptrIS3_EENS_10shared_ptrIT_EEPSA_EUlS4_E_NS_9allocatorIS3_EEE13__get_deleterERKSt9type_info : 92 -> 108
~ ____ZN3abb6router7Gateway10sleep_syncEN8dispatch13group_sessionE_block_invoke : 1988 -> 2000
~ __ZNKSt3__120__shared_ptr_pointerIPN3abb6router7GatewayEZN3ctu20SharedSynchronizableIS3_E15make_shared_ptrIS3_EENS_10shared_ptrIT_EEPSA_EUlS4_E_NS_9allocatorIS3_EEE13__get_deleterERKSt9type_info : 92 -> 108
~ __ZN3abb6router11ClientProxy23trySendingRequests_syncEv : 1492 -> 1444
~ __ZNSt3__16vectorIN3abb6router7MessageENS_9allocatorIS3_EEE13shrink_to_fitEv : 532 -> 536
~ __ZNKSt3__120__shared_ptr_pointerIPN3abb6router11ClientProxyEZN3ctu20SharedSynchronizableIS3_E15make_shared_ptrIS3_EENS_10shared_ptrIT_EEPSA_EUlS4_E_NS_9allocatorIS3_EEE13__get_deleterERKSt9type_info : 92 -> 108
~ __ZNKSt3__120__shared_ptr_pointerIPN3abb6router12TimerServiceEZN3ctu20SharedSynchronizableINS5_20DispatchTimerServiceEE15make_shared_ptrIS3_EENS_10shared_ptrIT_EEPSB_EUlS4_E_NS_9allocatorIS3_EEE13__get_deleterERKSt9type_info : 92 -> 108
~ __ZNKSt3__120__shared_ptr_pointerIPN3abb6router6ServerEZN3ctu20SharedSynchronizableIS3_E15make_shared_ptrIS3_EENS_10shared_ptrIT_EEPSA_EUlS4_E_NS_9allocatorIS3_EEE13__get_deleterERKSt9type_info : 92 -> 108
~ __ZNKSt3__120__shared_ptr_pointerIPN3abb6router6Client5StateEZN3ctu20SharedSynchronizableIS4_E15make_shared_ptrIS4_EENS_10shared_ptrIT_EEPSB_EUlS5_E_NS_9allocatorIS4_EEE13__get_deleterERKSt9type_info : 92 -> 108
CStrings:
+ "{set<unsigned int, std::less<unsigned int>, std::allocator<unsigned int>>={__tree<unsigned int, std::less<unsigned int>, std::allocator<unsigned int>>=^v{?={__tree_end_node<std::__tree_node_base<void *> *>=^v}}{?=Q}}}8@?0"
- "{set<unsigned int, std::less<unsigned int>, std::allocator<unsigned int>>={__tree<unsigned int, std::less<unsigned int>, std::allocator<unsigned int>>=^v{__tree_end_node<std::__tree_node_base<void *> *>=^v}Q}}8@?0"

```
