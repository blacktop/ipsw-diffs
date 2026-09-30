## libATCommandStudioDynamic.dylib

> `/usr/lib/libATCommandStudioDynamic.dylib`

```diff

-1397.0.0.0.0
-  __TEXT.__text: 0x57298
-  __TEXT.__auth_stubs: 0xe80
+1399.2.0.0.0
+  __TEXT.__text: 0x5785c
+  __TEXT.__auth_stubs: 0xe90
   __TEXT.__init_offsets: 0x10
   __TEXT.__const: 0x1b5c
-  __TEXT.__gcc_except_tab: 0x59c0
-  __TEXT.__cstring: 0x1d39
-  __TEXT.__oslogstring: 0x2645
-  __TEXT.__unwind_info: 0x22b0
+  __TEXT.__gcc_except_tab: 0x5a94
+  __TEXT.__cstring: 0x1d3e
+  __TEXT.__oslogstring: 0x2666
+  __TEXT.__unwind_info: 0x22c8
   __DATA_CONST.__got: 0x190
   __DATA_CONST.__const: 0xa48
-  __AUTH_CONST.__auth_got: 0x748
+  __AUTH_CONST.__auth_got: 0x750
   __AUTH_CONST.__const: 0x24d8
   __DATA.__common: 0x10
   __DATA_DIRTY.__data: 0x108

   - /usr/lib/libTelephonyUtilDynamic.dylib
   - /usr/lib/libc++.1.dylib
   - /usr/lib/libmav_ipc_router_dynamic.dylib
-  UUID: E5BDF071-AF5E-3383-A14D-579D707AC832
+  UUID: 02B93BAB-9A47-3AD9-B6EC-DBB2E1F5AED3
   Functions: 1423
-  Symbols:   3538
-  CStrings:  539
+  Symbols:   3537
+  CStrings:  540
 
Symbols:
+ _.str.29
+ __ZN3qmi16createRawRequestEhNS_11buffer_viewEm
Functions:
~ __ZNK13QMIServiceMsg9serializeEv : 376 -> 452
~ __ZN3qmi6Client5State4sendERNS0_9SendProxyE : 1264 -> 1480
~ __ZN3qmi6Client5State9send_syncERKN3xpc4dictEiRK13QMIServiceMsgRKN8dispatch5blockIU13block_pointerFvS8_EEE : 1660 -> 1656
~ __ZN3qmi11ClientProxy5State15handleSend_syncERKN3xpc4dictERKNS2_6objectE : 752 -> 1448
~ __ZNKSt3__120__shared_ptr_pointerIPN3qmi6Client8XPCStateEZN3ctu20SharedSynchronizableINS2_5StateEE15make_shared_ptrIS3_EENS_10shared_ptrIT_EEPSB_EUlS4_E_NS_9allocatorIS3_EEE13__get_deleterERKSt9type_info : 92 -> 108
~ __ZNKSt3__120__shared_ptr_pointerIPN3qmi6Client10LocalStateEZN3ctu20SharedSynchronizableINS2_5StateEE15make_shared_ptrIS3_EENS_10shared_ptrIT_EEPSB_EUlS4_E_NS_9allocatorIS3_EEE13__get_deleterERKSt9type_info : 92 -> 108
~ __ZNKSt3__120__shared_ptr_pointerIPN3qmi21QmiClientProxyAdapterEZN3ctu20SharedSynchronizableINS1_11ClientProxy5StateEE15make_shared_ptrIS2_EENS_10shared_ptrIT_EEPSB_EUlS3_E_NS_9allocatorIS2_EEE13__get_deleterERKSt9type_info : 92 -> 108
~ __ZNKSt3__120__shared_ptr_pointerIPN3qmi16TransactionQueue5StateENS3_7DeleterENS_9allocatorIS3_EEE13__get_deleterERKSt9type_info : 108 -> 124
~ __ZNKSt3__120__shared_ptr_pointerIPN4QMux5StateEZN3ctu20SharedSynchronizableIS2_E15make_shared_ptrIS2_EENS_10shared_ptrIT_EEPS9_EUlS3_E_NS_9allocatorIS2_EEE13__get_deleterERKSt9type_info : 92 -> 108
~ __ZN13QMIServiceMsg17createFromRawDataEPKhth : 8 -> 204
~ __ZN13QMIServiceMsg17createFromRawDataERKNSt3__16vectorIhNS0_9allocatorIhEEEEh : 8 -> 92
~ __ZNK13QMIServiceMsg9serializeEPvm : 284 -> 352
~ __ZNKSt3__120__shared_ptr_pointerIP26ATCSExceptionHandlerGlobalNS_10shared_ptrIS1_E27__shared_ptr_default_deleteIS1_S1_EENS_9allocatorIS1_EEE13__get_deleterERKSt9type_info : 108 -> 124
~ __ZNKSt3__120__shared_ptr_pointerIPN3qmi6Server5StateEZN3ctu20SharedSynchronizableIS3_E15make_shared_ptrIS3_EENS_10shared_ptrIT_EEPSA_EUlS4_E_NS_9allocatorIS3_EEE13__get_deleterERKSt9type_info : 92 -> 108
~ __ZNKSt3__120__shared_ptr_pointerIPN3qmi18QMuxServerAccepter5StateEZN3ctu20SharedSynchronizableIS3_E15make_shared_ptrIS3_EENS_10shared_ptrIT_EEPSA_EUlS4_E_NS_9allocatorIS3_EEE13__get_deleterERKSt9type_info : 92 -> 108
~ __ZNKSt3__120__shared_ptr_pointerIP10QMIControlNS1_7DeleterENS_9allocatorIS1_EEE13__get_deleterERKSt9type_info : 108 -> 124
CStrings:
+ "#I [%s]: Sending RAW Request: %s"
+ "{QMIWakeReason={vector<unsigned char, std::allocator<unsigned char>>=**{?=*}}Q}8@?0"
+ "{set<std::pair<const qmi::ServiceType, const unsigned short>, std::less<std::pair<const qmi::ServiceType, const unsigned short>>, std::allocator<std::pair<const qmi::ServiceType, const unsigned short>>>={__tree<std::pair<const qmi::ServiceType, const unsigned short>, std::less<std::pair<const qmi::ServiceType, const unsigned short>>, std::allocator<std::pair<const qmi::ServiceType, const unsigned short>>>=^v{?={__tree_end_node<std::__tree_node_base<void *> *>=^v}}{?=Q}}}8@?0"
+ "{vector<qmi::ClientProxy, std::allocator<qmi::ClientProxy>>=^{ClientProxy}^{ClientProxy}{?=^{ClientProxy}}}8@?0"
- "{QMIWakeReason={vector<unsigned char, std::allocator<unsigned char>>=***}Q}8@?0"
- "{set<std::pair<const qmi::ServiceType, const unsigned short>, std::less<std::pair<const qmi::ServiceType, const unsigned short>>, std::allocator<std::pair<const qmi::ServiceType, const unsigned short>>>={__tree<std::pair<const qmi::ServiceType, const unsigned short>, std::less<std::pair<const qmi::ServiceType, const unsigned short>>, std::allocator<std::pair<const qmi::ServiceType, const unsigned short>>>=^v{__tree_end_node<std::__tree_node_base<void *> *>=^v}Q}}8@?0"
- "{vector<qmi::ClientProxy, std::allocator<qmi::ClientProxy>>=^{ClientProxy}^{ClientProxy}^{ClientProxy}}8@?0"

```
