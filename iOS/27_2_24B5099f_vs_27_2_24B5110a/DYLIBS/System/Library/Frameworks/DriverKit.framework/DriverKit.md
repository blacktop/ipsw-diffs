## DriverKit

> `/System/Library/Frameworks/DriverKit.framework/DriverKit`

```diff

-509.40.10.0.0
-  __TEXT.__text: 0x3774c
+509.40.11.0.0
+  __TEXT.__text: 0x384dc
   __TEXT.__init_offsets: 0x8
   __TEXT.__const: 0x5f7c
   __TEXT.__cstring: 0x2f92
Functions:
~ __ZN25IODataQueueDispatchSource4initEv : 196 -> 172
~ __ZThn24_N25IODataQueueDispatchSource4initEv : 8 -> 32
~ __ZN25IODataQueueDispatchSource17SendDataAvailableEv : 324 -> 108
~ __ZN25IODataQueueDispatchSource16SendDataServicedEv : 324 -> 124
~ __ZN25IODataQueueDispatchSource4freeEv : 256 -> 216
~ __ZL6ServerPvP17mach_msg_header_tS1_ : 696 -> 692
~ __ZN24IOBufferMemoryDescriptor13Create_InvokeE5IORPCPFiyyyPPS_E : 172 -> 208
~ __ZN24IOBufferMemoryDescriptor16SetLength_InvokeE5IORPCP15OSMetaClassBasePFiS2_yE : 152 -> 200
~ __ZN12IODMACommand13Create_InvokeE5IORPCPFiP9IOServiceyPK25IODMACommandSpecificationPPS_E : 224 -> 248
~ __ZN12IODMACommand20PrepareForDMA_InvokeE5IORPCP15OSMetaClassBasePFiS2_yP18IOMemoryDescriptoryyPyPjP16IOAddressSegmentE : 260 -> 292
~ __ZN12IODMACommand18CompleteDMA_InvokeE5IORPCP15OSMetaClassBasePFiS2_yE : 152 -> 200
~ __ZN12IODMACommand21GetPreparation_InvokeE5IORPCP15OSMetaClassBasePFiS2_PyS3_PP18IOMemoryDescriptorE : 180 -> 224
~ __ZN12IODMACommand23PerformOperation_InvokeE5IORPCP15OSMetaClassBasePFiS2_yyyyP18IOMemoryDescriptorE : 232 -> 256
~ __ZN25IODataQueueDispatchSource13Create_InvokeE5IORPCPFiyP15IODispatchQueuePPS_E : 224 -> 248
~ __ZN25IODataQueueDispatchSource30SetDataAvailableHandler_InvokeE5IORPCP15OSMetaClassBasePFiS2_P8OSActionE : 216 -> 240
~ __ZN25IODataQueueDispatchSource29SetDataServicedHandler_InvokeE5IORPCP15OSMetaClassBasePFiS2_P8OSActionE : 216 -> 240
~ __ZN25IODataQueueDispatchSource17CopyMemory_InvokeE5IORPCP15OSMetaClassBasePFiS2_PP18IOMemoryDescriptorE : 168 -> 216
~ __ZN25IODataQueueDispatchSource31CopyDataAvailableHandler_InvokeE5IORPCP15OSMetaClassBasePFiS2_PP8OSActionE : 168 -> 216
~ __ZN25IODataQueueDispatchSource30CopyDataServicedHandler_InvokeE5IORPCP15OSMetaClassBasePFiS2_PP8OSActionE : 168 -> 216
~ __ZN25IODataQueueDispatchSource20DataAvailable_InvokeE5IORPCP15OSMetaClassBasePFvS2_P8OSActionEPK11OSMetaClass : 180 -> 216
~ __ZN25IODataQueueDispatchSource19DataServiced_InvokeE5IORPCP15OSMetaClassBasePFvS2_P8OSActionEPK11OSMetaClass : 180 -> 216
~ __ZN15IODispatchQueue14SetPort_InvokeE5IORPCP15OSMetaClassBasePFiS2_jE : 152 -> 200
~ __ZN15IODispatchQueue13Create_InvokeE5IORPCPFiPKcyyPPS_E : 212 -> 236
~ __ZN16IODispatchSource16SetEnable_InvokeE5IORPCP15OSMetaClassBasePFiS2_bE : 152 -> 200
~ __ZN16IODispatchSource13Cancel_InvokeE5IORPCP15OSMetaClassBasePFiS2_U13block_pointerFvvEE : 152 -> 200
~ __ZN16IODispatchSource30SetEnableWithCompletion_InvokeE5IORPCP15OSMetaClassBasePFiS2_bU13block_pointerFvvEE : 160 -> 204
~ __ZN16IODispatchSource19CheckForWork_InvokeE5IORPCP15OSMetaClassBasePFiS2_S0_bE : 184 -> 228
~ __ZN11IOEventLink23SetEventlinkPort_InvokeE5IORPCP15OSMetaClassBasePFiS2_jE : 152 -> 200
~ __ZN11IOEventLink13Create_InvokeE5IORPCPFiP8OSStringP12IOUserClientPPS_E : 252 -> 276
~ __ZN11IOEventLink23InvalidateKernel_InvokeE5IORPCP15OSMetaClassBasePFiS2_P12IOUserClientE : 216 -> 240
~ __ZN20IOExtensiblePaniclog13Create_InvokeE5IORPCPFiP6OSDataP8OSStringjjPPS_E : 260 -> 284
~ __ZN20IOExtensiblePaniclog16SetActive_InvokeE5IORPCP15OSMetaClassBasePFiS2_E : 144 -> 196
~ __ZN20IOExtensiblePaniclog18SetInactive_InvokeE5IORPCP15OSMetaClassBasePFiS2_E : 144 -> 196
~ __ZN20IOExtensiblePaniclog17InsertData_InvokeE5IORPCP15OSMetaClassBasePFiS2_P6OSDataE : 220 -> 244
~ __ZN20IOExtensiblePaniclog17AppendData_InvokeE5IORPCP15OSMetaClassBasePFiS2_P6OSDataE : 220 -> 244
~ __ZN20IOExtensiblePaniclog27CopyMemoryDescriptor_InvokeE5IORPCP15OSMetaClassBasePFiS2_PP24IOBufferMemoryDescriptorE : 168 -> 216
~ __ZN20IOExtensiblePaniclog17SetUsedLen_InvokeE5IORPCP15OSMetaClassBasePFiS2_jE : 152 -> 200
~ __ZN25IOInterruptDispatchSource17SetHandler_InvokeE5IORPCP15OSMetaClassBasePFiS2_P8OSActionE : 216 -> 240
~ __ZN25IOInterruptDispatchSource13Create_InvokeE5IORPCPFiP9IOServicejP15IODispatchQueuePPS_E : 276 -> 292
~ __ZN25IOInterruptDispatchSource23GetInterruptType_InvokeE5IORPCPFiP9IOServicejPyE : 204 -> 228
~ __ZN25IOInterruptDispatchSource23GetLastInterrupt_InvokeE5IORPCP15OSMetaClassBasePFiS2_PyS3_E : 160 -> 204
~ __ZN25IOInterruptDispatchSource24InterruptOccurred_InvokeE5IORPCP15OSMetaClassBasePFvS2_P8OSActionyyEPK11OSMetaClass : 188 -> 224
~ __ZN18IOMemoryDescriptor17_CopyState_InvokeE5IORPCP15OSMetaClassBasePFiS2_P17_IOMDPrivateStateE : 152 -> 200
~ __ZN18IOMemoryDescriptor20CreateMapping_InvokeE5IORPCP15OSMetaClassBasePFiS2_yyyyyPP11IOMemoryMapE : 184 -> 228
~ __ZN18IOMemoryDescriptor32CreateSubMemoryDescriptor_InvokeE5IORPCPFiyyyPS_PS1_E : 228 -> 252
~ __ZN18IOMemoryDescriptor34CreateWithMemoryDescriptors_InvokeE5IORPCPFiyjPPS_S2_E : 280 -> 296
~ __ZN11IOMemoryMap17_CopyState_InvokeE5IORPCP15OSMetaClassBasePFiS2_P24_IOMemoryMapPrivateStateE : 152 -> 200
~ __ZN9IOService12Start_InvokeE5IORPCP15OSMetaClassBasePFiS2_PS_E : 212 -> 236
~ __ZN9IOService11Stop_InvokeE5IORPCP15OSMetaClassBasePFiS2_PS_E : 212 -> 236
~ __ZN9IOService25GetRegistryEntryID_InvokeE5IORPCP15OSMetaClassBasePFiS2_PyE : 152 -> 200
~ __ZN9IOService33CreateDefaultDispatchQueue_InvokeE5IORPCP15OSMetaClassBasePFiS2_PP15IODispatchQueueE : 168 -> 216
~ __ZN9IOService20SetPowerState_InvokeE5IORPCP15OSMetaClassBasePFiS2_jE : 152 -> 200
~ __ZN9IOService13Create_InvokeE5IORPCP15OSMetaClassBasePFiS2_PS_PKcPS3_E : 260 -> 284
~ __ZN9IOService24UserSetProperties_InvokeE5IORPCP15OSMetaClassBasePFiS2_P11OSContainerE : 220 -> 244
~ __ZN9IOService17Stop_async_InvokeE5IORPCP15OSMetaClassBasePFvS2_PS_E : 168 -> 200
~ __ZN9IOService21_NewUserClient_InvokeE5IORPCP15OSMetaClassBasePFiS2_jP12OSDictionaryPP12IOUserClientE : 244 -> 268
~ __ZN9IOService20ClientCrashed_InvokeE5IORPCP15OSMetaClassBasePFiS2_PS_yE : 216 -> 240
~ __ZN9IOService14SetName_InvokeE5IORPCP15OSMetaClassBasePFiS2_PKcE : 204 -> 228
~ __ZN9IOService22RegisterService_InvokeE5IORPCP15OSMetaClassBasePFiS2_E : 144 -> 196
~ __ZN9IOService21CopyProperties_InvokeE5IORPCP15OSMetaClassBasePFiS2_PP12OSDictionaryE : 180 -> 228
~ __ZN9IOService21SearchProperty_InvokeE5IORPCP15OSMetaClassBasePFiS2_PKcS4_yPP11OSContainerE : 260 -> 284
~ __ZN9IOService20SetProperties_InvokeE5IORPCP15OSMetaClassBasePFiS2_P12OSDictionaryE : 220 -> 244
~ __ZN9IOService17JoinPMTree_InvokeE5IORPCP15OSMetaClassBasePFiS2_E : 144 -> 196
~ __ZN9IOService23ChangePowerState_InvokeE5IORPCP15OSMetaClassBasePFiS2_jE : 152 -> 200
~ __ZN9IOService23SetPowerOverride_InvokeE5IORPCP15OSMetaClassBasePFiS2_bE : 152 -> 200
~ __ZN9IOService20NewUserClient_InvokeE5IORPCP15OSMetaClassBasePFiS2_jPP12IOUserClientE : 176 -> 220
~ __ZN9IOService16Terminate_InvokeE5IORPCP15OSMetaClassBasePFiS2_yE : 152 -> 200
~ __ZN9IOService29CopyProviderProperties_InvokeE5IORPCP15OSMetaClassBasePFiS2_P7OSArrayPS4_E : 252 -> 276
~ __ZN9IOService25RequireMaxBusStall_InvokeE5IORPCP15OSMetaClassBasePFiS2_yE : 152 -> 200
~ __ZN9IOService17AdjustBusy_InvokeE5IORPCP15OSMetaClassBasePFiS2_iE : 152 -> 200
~ __ZN9IOService19GetBusyState_InvokeE5IORPCP15OSMetaClassBasePFiS2_PjE : 152 -> 200
~ __ZN9IOService29CoreAnalyticsSendEvent_InvokeE5IORPCP15OSMetaClassBasePFiS2_yP8OSStringP12OSDictionaryE : 256 -> 280
~ __ZN9IOService19UpdateReport_InvokeE5IORPCP15OSMetaClassBasePFiS2_P6OSDatajPjyyP18IOMemoryDescriptorE : 264 -> 288
~ __ZN9IOService22ConfigureReport_InvokeE5IORPCP15OSMetaClassBasePFiS2_P6OSDatajPjE : 228 -> 252
~ __ZN9IOService16SetLegend_InvokeE5IORPCP15OSMetaClassBasePFiS2_P7OSArraybE : 224 -> 248
~ __ZN9IOService15CopyName_InvokeE5IORPCP15OSMetaClassBasePFiS2_PP8OSStringE : 180 -> 228
~ __ZN9IOService23StringFromReturn_InvokeE5IORPCP15OSMetaClassBasePFiS2_iPP8OSStringE : 188 -> 232
~ __ZN9IOService28_ClaimSystemWakeEvent_InvokeE5IORPCP15OSMetaClassBasePFiS2_PS_yPKcP11OSContainerE : 284 -> 308
~ __ZN9IOService41SendIOMessageServicePropertyChange_InvokeE5IORPCP15OSMetaClassBasePFiS2_E : 144 -> 196
~ __ZN9IOService21RemoveProperty_InvokeE5IORPCP15OSMetaClassBasePFiS2_P8OSStringE : 220 -> 244
~ __ZN9IOService41CopySystemStateNotificationService_InvokeE5IORPCP15OSMetaClassBasePFiS2_PPS_E : 168 -> 216
~ __ZN9IOService34StateNotificationItemCreate_InvokeE5IORPCP15OSMetaClassBasePFiS2_P8OSStringP12OSDictionaryE : 252 -> 276
~ __ZN9IOService31StateNotificationItemSet_InvokeE5IORPCP15OSMetaClassBasePFiS2_P8OSStringP12OSDictionaryE : 252 -> 276
~ __ZN9IOService32StateNotificationItemCopy_InvokeE5IORPCP15OSMetaClassBasePFiS2_P8OSStringPP12OSDictionaryE : 252 -> 276
~ __ZN9IOService24CreatePMAssertion_InvokeE5IORPCP15OSMetaClassBasePFiS2_jPybE : 164 -> 208
~ __ZN9IOService25ReleasePMAssertion_InvokeE5IORPCP15OSMetaClassBasePFiS2_yE : 152 -> 200
~ __ZN35IOServiceNotificationDispatchSource13Create_InvokeE5IORPCPFiP12OSDictionaryyP15IODispatchQueuePPS_E : 256 -> 280
~ __ZN35IOServiceNotificationDispatchSource17SetHandler_InvokeE5IORPCP15OSMetaClassBasePFiS2_P8OSActionE : 216 -> 240
~ __ZN35IOServiceNotificationDispatchSource31ServiceNotificationReady_InvokeE5IORPCP15OSMetaClassBasePFvS2_P8OSActionEPK11OSMetaClass : 180 -> 216
~ __ZN35IOServiceNotificationDispatchSource27CopyNextNotification_InvokeE5IORPCP15OSMetaClassBasePFiS2_PyPP9IOServiceS3_E : 180 -> 224
~ __ZN40IOServiceStateNotificationDispatchSource13Create_InvokeE5IORPCPFiP9IOServiceP7OSArrayP15IODispatchQueuePPS_E : 308 -> 328
~ __ZN40IOServiceStateNotificationDispatchSource17SetHandler_InvokeE5IORPCP15OSMetaClassBasePFiS2_P8OSActionE : 216 -> 240
~ __ZN40IOServiceStateNotificationDispatchSource29StateNotificationBegin_InvokeE5IORPCP15OSMetaClassBasePFiS2_E : 144 -> 196
~ __ZN40IOServiceStateNotificationDispatchSource29StateNotificationReady_InvokeE5IORPCP15OSMetaClassBasePFvS2_P8OSActionEPK11OSMetaClass : 180 -> 216
~ __ZN21IOTimerDispatchSource17SetHandler_InvokeE5IORPCP15OSMetaClassBasePFiS2_P8OSActionE : 216 -> 240
~ __ZN21IOTimerDispatchSource17WakeAtTime_InvokeE5IORPCP15OSMetaClassBasePFiS2_yyyE : 160 -> 204
~ __ZN21IOTimerDispatchSource13Create_InvokeE5IORPCPFiP15IODispatchQueuePPS_E : 216 -> 240
~ __ZN21IOTimerDispatchSource20TimerOccurred_InvokeE5IORPCP15OSMetaClassBasePFvS2_P8OSActionyEPK11OSMetaClass : 184 -> 220
~ __ZN12IOUserClient29CopyClientEntitlements_InvokeE5IORPCP15OSMetaClassBasePFiS2_PP12OSDictionaryE : 180 -> 228
~ __ZN12IOUserClient22_ExternalMethod_InvokeE5IORPCP15OSMetaClassBasePFiS2_yPKyjP6OSDataP18IOMemoryDescriptorPyPjyPS6_S8_P8OSActionE : 448 -> 472
~ __ZN12IOUserClient22AsyncCompletion_InvokeE5IORPCP15OSMetaClassBasePFvS2_P8OSActioniPKyjEPK11OSMetaClass : 208 -> 244
~ __ZN12IOUserClient30CopyClientMemoryForType_InvokeE5IORPCP15OSMetaClassBasePFiS2_yPyPP18IOMemoryDescriptorE : 180 -> 224
~ __ZN12IOUserClient39CreateMemoryDescriptorFromClient_InvokeE5IORPCP15OSMetaClassBasePFiS2_yjPK16IOAddressSegmentPP18IOMemoryDescriptorE : 188 -> 232
~ __ZN12IOUserServer11Exit_InvokeE5IORPCP15OSMetaClassBasePFiS2_PKcE : 204 -> 228
~ __ZN12IOUserServer17LoadModule_InvokeE5IORPCP15OSMetaClassBasePFiS2_PKcE : 204 -> 228
~ __ZN12IOUserServer13Create_InvokeE5IORPCPFiPKcyyP8OSStringPPS_E : 244 -> 268
~ __ZN12IOUserServer12Panic_InvokeE5IORPCP15OSMetaClassBasePFiS2_PKcE : 204 -> 228
~ __ZN11IOWorkGroup23SetWorkGroupPort_InvokeE5IORPCP15OSMetaClassBasePFiS2_jE : 152 -> 200
~ __ZN11IOWorkGroup13Create_InvokeE5IORPCPFiP8OSStringP12IOUserClientPPS_E : 252 -> 276
~ __ZN11IOWorkGroup23InvalidateKernel_InvokeE5IORPCP15OSMetaClassBasePFiS2_P12IOUserClientE : 216 -> 240
~ __ZN8OSAction9_DispatchEPS_5IORPC : 196 -> 160
~ __ZN8OSAction14Aborted_InvokeE5IORPCP15OSMetaClassBasePFvS2_E : 112 -> 160
~ __ZN8OSAction13Create_InvokeE5IORPCPFiP8OSObjectyymPPS_E : 228 -> 252
~ __ZN8OSAction25CreateWithTypeName_InvokeE5IORPCPFiP8OSObjectyymP8OSStringPPS_E : 260 -> 284
~ __ZN8OSObject23SetDispatchQueue_InvokeE5IORPCP15OSMetaClassBasePFiS2_PKcP15IODispatchQueueE : 244 -> 268
~ __ZN8OSObject24CopyDispatchQueue_InvokeE5IORPCP15OSMetaClassBasePFiS2_PKcPP15IODispatchQueueE : 224 -> 248
~ __ZN21_IOBlockStorageDevice33DoAsyncReadWriteCompletion_InvokeE5IORPCP15OSMetaClassBasePFvS2_P8OSActioniyEPK11OSMetaClass : 188 -> 224
~ __ZN21_IOBlockStorageDevice23DoAsyncReadWrite_InvokeE5IORPCP15OSMetaClassBasePFiS2_P18IOMemoryDescriptoryyP8OSActionE : 264 -> 288
~ __ZN21_IOBlockStorageDevice28CopyProducerDataQueue_InvokeE5IORPCP15OSMetaClassBasePFiS2_PP25IODataQueueDispatchSourceE : 168 -> 216
~ __ZN21_IOBlockStorageDevice28CopyReceiverDataQueue_InvokeE5IORPCP15OSMetaClassBasePFiS2_PP25IODataQueueDispatchSourceE : 168 -> 216
```
