## com.apple.DriverKit-AppleEthernetIXL

> `/System/Library/DriverExtensions/com.apple.DriverKit-AppleEthernetIXL.dext/com.apple.DriverKit-AppleEthernetIXL`

```diff

-62.120.2.0.0
-  __TEXT.__text: 0x1bd60
-  __TEXT.__auth_stubs: 0x560
-  __TEXT.__const: 0xef8
-  __TEXT.__cstring: 0x4039
-  __TEXT.__oslogstring: 0x1a2f
-  __DATA_CONST.__auth_got: 0x2b0
+62.140.2.0.0
+  __TEXT.__text: 0x1ba00
+  __TEXT.__auth_stubs: 0x5a0
+  __TEXT.__const: 0xb38
+  __TEXT.__cstring: 0x3f19
+  __TEXT.__oslogstring: 0x19ea
+  __DATA_CONST.__auth_got: 0x2d0
   __DATA_CONST.__got: 0x48
-  __DATA_CONST.__const: 0x10d8
-  __DATA_CONST.__osclassinfo: 0x38
+  __DATA_CONST.__const: 0xd40
+  __DATA_CONST.__osclassinfo: 0x20
   __DATA.__data: 0x548
-  __DATA.__common: 0x48
+  __DATA.__bss: 0xc
+  __DATA.__common: 0x30
   - /System/DriverKit/System/Library/Frameworks/DriverKit.framework/DriverKit
   - /System/DriverKit/System/Library/Frameworks/NetworkingDriverKit.framework/NetworkingDriverKit
   - /System/DriverKit/System/Library/Frameworks/PCIDriverKit.framework/PCIDriverKit
   - /System/DriverKit/usr/lib/libc++.dylib
-  UUID: 60C891B5-13F4-33CB-9CE4-FB9EB5ABFD55
-  Functions: 535
-  Symbols:   505
-  CStrings:  612
+  UUID: F2B5527A-531A-351A-9480-98AAED0C2C81
+  Functions: 522
+  Symbols:   484
+  CStrings:  605
 
Symbols:
+ __NSConcreteGlobalBlock
+ __ZN15OSMetaClassBase6InvokeE5IORPC
+ __ZN16IODispatchSource6CancelEU13block_pointerFvvEPFiP15OSMetaClassBase5IORPCE
+ __ZN25IODataQueueDispatchSource15IsDataAvailableEv
+ __ZN30IOUserNetworkRxSubmissionQueue12_SetDoorbellEP25IOInterruptDispatchSourcePFiP15OSMetaClassBase5IORPCE
+ __ZN30IOUserNetworkTxSubmissionQueue12_SetDoorbellEP25IOInterruptDispatchSourcePFiP15OSMetaClassBase5IORPCE
+ __ZN32DriverKit_AppleEthernetIXL_NetIf11PlaceHolderEPFiP15OSMetaClassBase5IORPCE
+ __ZN32DriverKit_AppleEthernetIXL_NetIf13getTSOOptionsEP23IOUserNetworkTSOOptions
+ __ZN32DriverKit_AppleEthernetIXL_NetIf16PlaceHolder_ImplEv
+ __ZN32DriverKit_AppleEthernetIXL_NetIf18PlaceHolder_InvokeE5IORPCP15OSMetaClassBasePFvS2_E
+ __ZN32DriverKit_AppleEthernetIXL_NetIf18getHardwareAddressEP10ether_addr
+ __ZN32DriverKit_AppleEthernetIXL_NetIf18setHardwareAssistsEjj
+ __ZN32DriverKit_AppleEthernetIXL_NetIf9Stop_ImplEP9IOService
+ __ZNK19IOUserNetworkPacket19GetPacketBufferPoolEPP29IOUserNetworkPacketBufferPool
+ __ZThn48_N32DriverKit_AppleEthernetIXL_NetIf13getTSOOptionsEP23IOUserNetworkTSOOptions
+ __ZThn48_N32DriverKit_AppleEthernetIXL_NetIf18getHardwareAddressEP10ether_addr
+ __ZThn48_N32DriverKit_AppleEthernetIXL_NetIf18setHardwareAssistsEjj
- _OSAction_DriverKit_AppleEthernetIXL_LegacyInterrupt_Class
- _OSAction_DriverKit_AppleEthernetIXL_NetIf_RxSubmit_Class
- _OSAction_DriverKit_AppleEthernetIXL_NetIf_TxSubmit_Class
- __ZN21IOUserNetworkEthernet13getTSOOptionsEP23IOUserNetworkTSOOptions
- __ZN21IOUserNetworkEthernet18getHardwareAddressEP10ether_addr
- __ZN21IOUserNetworkEthernet18setHardwareAssistsEjj
- __ZN25IODataQueueDispatchSource20DataAvailable_InvokeE5IORPCP15OSMetaClassBasePFvS2_P8OSActionEPK11OSMetaClass
- __ZN25IODataQueueDispatchSource23SetDataAvailableHandlerEP8OSActionPFiP15OSMetaClassBase5IORPCE
- __ZN26DriverKit_AppleEthernetIXL20LegacyInterrupt_ImplEP8OSActionyy
- __ZN26DriverKit_AppleEthernetIXL27CreateActionLegacyInterruptEmPP8OSAction
- __ZN32DriverKit_AppleEthernetIXL_NetIf13RxSubmit_ImplEP8OSAction
- __ZN32DriverKit_AppleEthernetIXL_NetIf13TxSubmit_ImplEP8OSAction
- __ZN32DriverKit_AppleEthernetIXL_NetIf20CreateActionRxSubmitEmPP8OSAction
- __ZN32DriverKit_AppleEthernetIXL_NetIf20CreateActionTxSubmitEmPP8OSAction
- __ZN50OSAction_DriverKit_AppleEthernetIXL_NetIf_RxSubmit8DispatchE5IORPC
- __ZN50OSAction_DriverKit_AppleEthernetIXL_NetIf_RxSubmit9_DispatchEPS_5IORPC
- __ZN50OSAction_DriverKit_AppleEthernetIXL_NetIf_TxSubmit8DispatchE5IORPC
- __ZN50OSAction_DriverKit_AppleEthernetIXL_NetIf_TxSubmit9_DispatchEPS_5IORPC
- __ZN51OSAction_DriverKit_AppleEthernetIXL_LegacyInterrupt8DispatchE5IORPC
- __ZN51OSAction_DriverKit_AppleEthernetIXL_LegacyInterrupt9_DispatchEPS_5IORPC
- __ZN59OSAction_DriverKit_AppleEthernetIXL_NetIf_RxSubmitMetaClass3NewEP8OSObject
- __ZN59OSAction_DriverKit_AppleEthernetIXL_NetIf_RxSubmitMetaClass8DispatchE5IORPC
- __ZN59OSAction_DriverKit_AppleEthernetIXL_NetIf_TxSubmitMetaClass3NewEP8OSObject
- __ZN59OSAction_DriverKit_AppleEthernetIXL_NetIf_TxSubmitMetaClass8DispatchE5IORPC
- __ZN60OSAction_DriverKit_AppleEthernetIXL_LegacyInterruptMetaClass3NewEP8OSObject
- __ZN60OSAction_DriverKit_AppleEthernetIXL_LegacyInterruptMetaClass8DispatchE5IORPC
- __ZTV50OSAction_DriverKit_AppleEthernetIXL_NetIf_RxSubmit
- __ZTV50OSAction_DriverKit_AppleEthernetIXL_NetIf_TxSubmit
- __ZTV51OSAction_DriverKit_AppleEthernetIXL_LegacyInterrupt
- __ZTV59OSAction_DriverKit_AppleEthernetIXL_NetIf_RxSubmitMetaClass
- __ZTV59OSAction_DriverKit_AppleEthernetIXL_NetIf_TxSubmitMetaClass
- __ZTV60OSAction_DriverKit_AppleEthernetIXL_LegacyInterruptMetaClass
- __ZThn48_N21IOUserNetworkEthernet13getTSOOptionsEP23IOUserNetworkTSOOptions
- __ZThn48_N21IOUserNetworkEthernet18getHardwareAddressEP10ether_addr
- __ZThn48_N21IOUserNetworkEthernet18setHardwareAssistsEjj
- _gOSAction_DriverKit_AppleEthernetIXL_LegacyInterruptMetaClass
- _gOSAction_DriverKit_AppleEthernetIXL_NetIf_RxSubmitMetaClass
- _gOSAction_DriverKit_AppleEthernetIXL_NetIf_TxSubmitMetaClass
CStrings:
+ "!IOUserNetworkPacketBufferPool::CreateWithOptions(pciDev, poolName, &poolOptions, &rx_pool)"
+ "!IOUserNetworkPacketBufferPool::CreateWithOptions(pciDev, poolName, &poolOptions, &tx_pool)"
+ "!IOUserNetworkRxCompletionQueue::Create(rx_pool, owner, RX_RING_SIZE, 0, dq, &rx_ring[i].cmp_q)"
+ "!IOUserNetworkRxSubmissionQueue::Create(rx_pool, owner, RX_RING_SIZE, 0, dq, &rx_ring[i].sub_q)"
+ "!IOUserNetworkTxCompletionQueue::Create(tx_pool, owner, TX_RING_SIZE >> 1, 0, dq, &tx_ring[i].cmp_q)"
+ "!IOUserNetworkTxSubmissionQueue::Create(tx_pool, owner, TX_RING_SIZE >> 1, 0, dq, &tx_ring[i].sub_q)"
+ "!owner->registerEthernetInterface(queues, rx_num_queues * 4, tx_pool, rx_pool)"
+ "!rx_ring[i].sub_q->_SetDoorbell(mdev->intSource[1 + i])"
+ "!tx_ring[i].sub_q->_SetDoorbell(mdev->intSource[1 + i])"
+ "PlaceHolder_Impl"
+ "false"
+ "ixl:(%s): %s(%d): %p\n"
+ "tx"
- "!IOUserNetworkPacketBufferPool::CreateWithOptions(pciDev, poolName, &poolOptions, &pool)"
- "!IOUserNetworkRxCompletionQueue::Create(pool, owner, RX_RING_SIZE, 0, dq, &rx_ring[i].cmp_q)"
- "!IOUserNetworkRxSubmissionQueue::Create(pool, owner, RX_RING_SIZE, 0, dq, &rx_ring[i].sub_q)"
- "!IOUserNetworkTxCompletionQueue::Create(pool, owner, TX_RING_SIZE, 0, dq, &tx_ring[i].cmp_q)"
- "!IOUserNetworkTxSubmissionQueue::Create(pool, owner, TX_RING_SIZE, 0, dq, &tx_ring[i].sub_q)"
- "!owner->CreateActionRxSubmit(sizeof(void*), &rx_ring[i].sub_a)"
- "!owner->CreateActionTxSubmit(sizeof(void*), &tx_ring[i].sub_a)"
- "!owner->RegisterEthernetInterface(*uc_addr, pool, queues, rx_num_queues << 2)"
- "!rx_ring[i].sub->SetDataAvailableHandler(rx_ring[0].sub_a)"
- "!rx_ring[i].sub_q->CopyDataQueue(&rx_ring[i].sub)"
- "!tx_ring[i].sub->SetDataAvailableHandler(tx_ring[i].sub_a)"
- "!tx_ring[i].sub_q->CopyDataQueue(&tx_ring[i].sub)"
- "OSAction_DriverKit_AppleEthernetIXL_LegacyInterrupt"
- "OSAction_DriverKit_AppleEthernetIXL_NetIf_RxSubmit"
- "OSAction_DriverKit_AppleEthernetIXL_NetIf_TxSubmit"
- "RxSubmit_Impl"
- "TxSubmit_Impl"
- "ixl:(%s): %s(%d): called with state != DEV_NET_STATE_ACTIVATED\n"
- "ixl:(%s): %s(%d): icr0=%x\n"
- "legacyIntrHandler"

```
