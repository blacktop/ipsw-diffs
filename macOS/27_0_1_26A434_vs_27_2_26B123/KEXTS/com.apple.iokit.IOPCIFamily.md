## com.apple.iokit.IOPCIFamily

> `com.apple.iokit.IOPCIFamily`

### Sections with Same Size but Changed Content

- `__TEXT.__cstring`

```diff

-764.0.0.0.0
+764.40.4.0.0
   __TEXT.__const: 0xf18
   __TEXT.__cstring: 0x76ed
   __TEXT.__os_log: 0x5085
-  __TEXT_EXEC.__text: 0x43f24
+  __TEXT_EXEC.__text: 0x43f8c
   __TEXT_EXEC.__auth_stubs: 0x960
   __DATA.__data: 0xcc
   __DATA.__common: 0x430
Symbols:
+ __ZZN11IOPCIBridge17createEventSourceEP8OSObjectPFvS1_P16IOPCIEventSourcePK10IOPCIEventEjE21kalloc_type_view_6410
+ __ZZN15IOPCI2PCIBridge21startBridgeInterruptsEP9IOServiceE21kalloc_type_view_5775
+ __ZZN15IOPCI2PCIBridge4stopEP9IOServiceE21kalloc_type_view_6205
+ __ZZN16IOPCIEventSource4freeEvE21kalloc_type_view_6547
- __ZZN11IOPCIBridge17createEventSourceEP8OSObjectPFvS1_P16IOPCIEventSourcePK10IOPCIEventEjE21kalloc_type_view_6401
- __ZZN15IOPCI2PCIBridge21startBridgeInterruptsEP9IOServiceE21kalloc_type_view_5766
- __ZZN15IOPCI2PCIBridge4stopEP9IOServiceE21kalloc_type_view_6196
- __ZZN16IOPCIEventSource4freeEvE21kalloc_type_view_6538
Functions:
~ __ZN11IOPCIBridge11pciMatchNubEP11IOPCIDeviceP12OSDictionaryPi : 632 -> 672
~ __ZN11IOPCIDevice21_ManageSession_InvokeE5IORPCP15OSMetaClassBasePFiS2_P9IOServicebjE : 240 -> 244
~ __ZN11IOPCIDevice35_CopyWCDeviceMemoryWithIndex_InvokeE5IORPCP15OSMetaClassBasePFiS2_yPP18IOMemoryDescriptorP9IOServiceE : 252 -> 256
~ __ZN11IOPCIDevice33_CopyDeviceMemoryWithIndex_InvokeE5IORPCP15OSMetaClassBasePFiS2_yPP18IOMemoryDescriptorP9IOServiceE : 252 -> 256
~ __ZN11IOPCIDevice20_MemoryAccess_InvokeE5IORPCP15OSMetaClassBasePFiS2_yyyPyP9IOServicejE : 244 -> 248
~ __ZN11IOPCIDevice24FindPCICapability_InvokeE5IORPCP15OSMetaClassBasePFiS2_jyPyE : 176 -> 180
~ __ZN11IOPCIDevice27GetBusDeviceFunction_InvokeE5IORPCP15OSMetaClassBasePFiS2_PhS3_S3_E : 176 -> 180
~ __ZN11IOPCIDevice28HasPCIPowerManagement_InvokeE5IORPCP15OSMetaClassBasePFiS2_yE : 164 -> 168
~ __ZN11IOPCIDevice31EnablePCIPowerManagement_InvokeE5IORPCP15OSMetaClassBasePFiS2_yE : 164 -> 168
~ __ZN11IOPCIDevice22SaveDeviceState_InvokeE5IORPCP15OSMetaClassBasePFiS2_jE : 164 -> 168
~ __ZN11IOPCIDevice25RestoreDeviceState_InvokeE5IORPCP15OSMetaClassBasePFiS2_jE : 164 -> 168
~ __ZN11IOPCIDevice17GetBARInfo_InvokeE5IORPCP15OSMetaClassBasePFiS2_hPhPyS3_E : 180 -> 184
~ __ZN11IOPCIDevice19SetLinkSpeed_InvokeE5IORPCP15OSMetaClassBasePFiS2_14IOPCILinkSpeedbE : 176 -> 180
~ __ZN11IOPCIDevice19GetLinkSpeed_InvokeE5IORPCP15OSMetaClassBasePFiS2_P14IOPCILinkSpeedE : 164 -> 168
~ __ZN11IOPCIDevice26ConfigureInterrupts_InvokeE5IORPCP15OSMetaClassBasePFiS2_jjjjE : 172 -> 176
~ __ZN11IOPCIDevice12Reset_InvokeE5IORPCP15OSMetaClassBasePFiS2_jjE : 168 -> 172
~ __ZN11IOPCIDevice19SetASPMState_InvokeE5IORPCP15OSMetaClassBasePFiS2_jE : 164 -> 168
CStrings:
+ "23:10:01"
+ "Oct 14 2026"
- "20:39:30"
- "Aug 11 2026"
```
