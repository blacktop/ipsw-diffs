## com.apple.driver.usb.cdc.ncm

> `com.apple.driver.usb.cdc.ncm`

```diff

-391.0.0.0.0
-  __TEXT.__cstring: 0x2329 sha256:2a72c937fe0d541b9e01d3d586de9b3653b4fd6424f3bfbc4b2932d2f9fdc71f
-  __TEXT.__const: 0xba sha256:acc87f9873e55c1c566c5b78ca1529c2bf2c9a907579ed1202129281f95275f6
-  __TEXT_EXEC.__text: 0xd510 sha256:d368e350f18655d79dc7304a7746a2e76df0a6d2813c06fabe3dc855e5335350
+375.100.5.0.0
+  __TEXT.__const: 0xb0 sha256:d4b05572c2fcc9a983217401b0ba216b693d367fe86da03d778e3991156f3a3c
+  __TEXT.__cstring: 0xd9c sha256:062d12b5c57dcfd494dbd77c6af39ec595ecba7fd3cf956d1bb59fdcb063730e
+  __TEXT_EXEC.__text: 0x82a4 sha256:17a1c70e002a433a4c769eb6dfce183003d947810f7c5fedfb8b61acf36588d0
   __TEXT_EXEC.__auth_stubs: 0x0
-  __DATA.__data: 0xc8 sha256:6aeb5c7c2b49d1cb1193bf36cf807f387b307f92c358e3fcf0a06293175cc2bf
-  __DATA.__common: 0xd8 sha256:a5645e7a3fa0866cde8842c4dab96567507c3d1a3c028b816bc63f6966367b70
+  __DATA.__data: 0xc8 sha256:191d8f60411481d4affa367d453da524478cdbd7f59ada5f49a7d20712cec0a7
+  __DATA.__common: 0x60 sha256:2ea9ab9198d1638007400cd2c3bef1cc745b864b76011a0e1bc52180ac6452d4
   __DATA.__bss: 0x4 sha256:df3f619804a92fdb4057192dc43dd748ea778adc52bc498ce80524c014b81119
-  __DATA_CONST.__mod_init_func: 0x20 sha256:af22a14e92058fafd9b3b821e502bf114bf0426579d0a8a50a2e143561c5fb99
-  __DATA_CONST.__mod_term_func: 0x20 sha256:617a7fa7e5d3784789ddf1d14532462b8433ee61fbdac2ce0f1630d521e66f15
-  __DATA_CONST.__const: 0x3438 sha256:f935610fb18fe5557675454a256828290db901c79556e125d9db00f9a32924ae
-  __DATA_CONST.__kalloc_type: 0x140 sha256:64254288e361d0fcee087abd6175807b0d76f4ef25af4d64aa1631dc492cd7fa
-  __DATA_CONST.__auth_got: 0x2b0 sha256:bd65bac57b9ca33956a53ea5b0c38c5582b60e6938a01f0a8637a4c7a4eddefb
-  __DATA_CONST.__got: 0x80 sha256:310d117c0f0604fbb5fd6928a4162c66b0f285c7c58e8e8417a1edf2eb562625
-  UUID: 04806805-38F7-398F-BAEF-599628B4E895
-  Functions: 337
-  Symbols:   920
-  CStrings:  233
+  __DATA_CONST.__auth_got: 0x2a0 sha256:5b5c601ebc3c2ff6fd6049c11d062848ea125cb599305ab60cf7d17e1da6614e
+  __DATA_CONST.__got: 0x78 sha256:61ca55bdc6011cab9b1907f831113c3b6e5f41f327cdc5688f1693388fa1aec1
+  __DATA_CONST.__mod_init_func: 0x10 sha256:625a3eacad1d51cc2862eb93dbfdeb09260e3729afbd9d482f7e404ef497685c
+  __DATA_CONST.__mod_term_func: 0x10 sha256:d0ef85d1cd7c275ba06785a70b84b73ce65b09cf0f3d85eb13960fe8a0a39200
+  __DATA_CONST.__const: 0x1838 sha256:56549c1627bd375320d5efda7927d3d2e8ecef151004caee0e6d5fd9bc2dd211
+  __DATA_CONST.__kalloc_type: 0x100 sha256:7b96dc06c0b91d3ef017c55b254b5d9a9900e2b870439e3dba68159b9b261cae
+  UUID: CCAAF303-7C4E-312C-B12F-AC707AA61E56
+  Functions: 188
+  Symbols:   721
+  CStrings:  132
 
Symbols:
+ _IOFreeTypeImpl
+ _IOMallocTypeImpl
+ _IOSleep
+ _ZN15AppleUSBNCMData28waitForMatchingControlDriverEv.cold.1
+ __ZN15AppleUSBNCMData18matchControlDriverEv
+ __ZN15AppleUSBNCMData28waitForMatchingControlDriverEv
+ __ZN15AppleUSBNCMData5probeEP9IOServicePi
+ __ZN18AppleUSBCDCControl4freeEv
+ __ZN9IOService15serviceMatchingEPKcP12OSDictionary
+ __ZN9IOService19getMatchingServicesEP12OSDictionary
+ __ZZN15AppleUSBNCMData11freeRecordsEvE21kalloc_type_view_1503
+ __ZZN15AppleUSBNCMData12allocRecordsEvE21kalloc_type_view_1428
+ _bzero
+ _clock_interval_to_deadline
- _GLOBAL__sub_I_AppleUSBNCM11Control.cpp
- _GLOBAL__sub_I_AppleUSBNCM11Data.cpp
- _IOFreeDataShareable
- _IOMallocDataShareable
- _OUTLINED_FUNCTION_26
- _OUTLINED_FUNCTION_27
- _OUTLINED_FUNCTION_28
- _OUTLINED_FUNCTION_29
- _OUTLINED_FUNCTION_30
- _OUTLINED_FUNCTION_31
- _OUTLINED_FUNCTION_32
- _OUTLINED_FUNCTION_33
- _OUTLINED_FUNCTION_34
- _OUTLINED_FUNCTION_35
- _OUTLINED_FUNCTION_36
- _OUTLINED_FUNCTION_37
- _OUTLINED_FUNCTION_38
- _OUTLINED_FUNCTION_39
- _OUTLINED_FUNCTION_40
- _ZN15AppleUSBNCMData13willTerminateEP9IOServicej.cold.1
- _ZN15AppleUSBNCMData16setDataAlternateEv.cold.1
- _ZN15AppleUSBNCMData29setPropertiesForInterfaceRoleEv.cold.1
- _ZN15AppleUSBNCMData29setPropertiesForInterfaceRoleEv.cold.2
- _ZN15AppleUSBNCMData31configureBSDInterfaceThreadCallEPvS0_.cold.1
- _ZN15AppleUSBNCMData4initEP12OSDictionary.cold.1
- _ZN15AppleUSBNCMData4stopEP9IOService.cold.1
- _ZN15AppleUSBNCMData5startEP9IOService.cold.2
- _ZN15AppleUSBNCMData7armReadEP15InputPipeRecord.cold.1
- _ZN15AppleUSBNCMData7armReadEP15InputPipeRecord.cold.2
- _ZN15AppleUSBNCMData7armReadEv.cold.1
- _ZN20AppleUSBNCM11Control5startEP9IOService.cold.1
- __Z23copyBSDNameForInterfaceP18IONetworkInterfacePc
- __ZL21AppleUSBNCM11Data_ktv
- __ZL24AppleUSBNCM11Control_ktv
- __ZL25AppleUSBNCMDataPoller_ktv
- __ZN13IOEventSource10gMetaClassE
- __ZN13IOEventSource11setWorkLoopEP10IOWorkLoop
- __ZN13IOEventSource23_RESERVEDIOEventSource0Ev
- __ZN13IOEventSource23_RESERVEDIOEventSource1Ev
- __ZN13IOEventSource23_RESERVEDIOEventSource2Ev
- __ZN13IOEventSource23_RESERVEDIOEventSource3Ev
- __ZN13IOEventSource23_RESERVEDIOEventSource4Ev
- __ZN13IOEventSource23_RESERVEDIOEventSource5Ev
- __ZN13IOEventSource23_RESERVEDIOEventSource6Ev
- __ZN13IOEventSource23_RESERVEDIOEventSource7Ev
- __ZN13IOEventSource4freeEv
- __ZN13IOEventSource4initEP8OSObjectPFvS1_zE
- __ZN13IOEventSource6enableEv
- __ZN13IOEventSource7disableEv
- __ZN13IOEventSource7setNextEPS_
- __ZN13IOEventSource8openGateEv
- __ZN13IOEventSource9closeGateEv
- __ZN13IOEventSource9setActionEPFvP8OSObjectzE
- __ZN13IOEventSourceC2EPK11OSMetaClass
- __ZN13IOEventSourceD2Ev
- __ZN15AppleUSBNCMData15selectNTBFormatEv
- __ZN15AppleUSBNCMData25notificationCallbackGatedEP18AppleUSBNCMControlPvP18USBCDCNotification_vfpthunk_
- __ZN17AppleUSBNCM11Data10gMetaClassE
- __ZN17AppleUSBNCM11Data10superClassE
- __ZN17AppleUSBNCM11Data13configureDataEv
- __ZN17AppleUSBNCM11Data15selectNTBFormatEv
- __ZN17AppleUSBNCM11Data23configureMediumHandlingEv
- __ZN17AppleUSBNCM11Data25notificationCallbackGatedEP18AppleUSBNCMControlPvP18USBCDCNotification
- __ZN17AppleUSBNCM11Data6enableEP18IONetworkInterface
- __ZN17AppleUSBNCM11Data7disableEP18IONetworkInterface
- __ZN17AppleUSBNCM11Data9MetaClassC1Ev
- __ZN17AppleUSBNCM11Data9MetaClassC2Ev
- __ZN17AppleUSBNCM11Data9MetaClassD0Ev
- __ZN17AppleUSBNCM11Data9MetaClassD1Ev
- __ZN17AppleUSBNCM11Data9metaClassE
- __ZN17AppleUSBNCM11DataC1EPK11OSMetaClass
- __ZN17AppleUSBNCM11DataC1Ev
- __ZN17AppleUSBNCM11DataC2EPK11OSMetaClass
- __ZN17AppleUSBNCM11DataC2Ev
- __ZN17AppleUSBNCM11DataD0Ev
- __ZN17AppleUSBNCM11DataD1Ev
- __ZN17AppleUSBNCM11DataD2Ev
- __ZN17AppleUSBNCM11DatadlEPvm
- __ZN17AppleUSBNCM11DatanwEm
- __ZN18AppleUSBNCMControl17copyDataInterfaceEv
- __ZN18AppleUSBNCMControl27getMACAddressFromDescriptorEh
- __ZN18AppleUSBNCMControl4freeEv
- __ZN18AppleUSBNCMControl5probeEP9IOServicePi
- __ZN20AppleUSBNCM11Control10gMetaClassE
- __ZN20AppleUSBNCM11Control10superClassE
- __ZN20AppleUSBNCM11Control22getExtendedFeatureWakeE15NCMWakeTypeCodePvPth
- __ZN20AppleUSBNCM11Control22setExtendedFeatureWakeE15NCMWakeTypeCodePvt
- __ZN20AppleUSBNCM11Control23getExtendedCapabilitiesEPvPt
- __ZN20AppleUSBNCM11Control24cacheExtendedDescriptorsEv
- __ZN20AppleUSBNCM11Control25getExtendedCapabilityModeEP25NCMExtendedCapabilityMode
- __ZN20AppleUSBNCM11Control25parseExtendedCapabilitiesEPKvt
- __ZN20AppleUSBNCM11Control25setExtendedCapabilityModeE25NCMExtendedCapabilityMode
- __ZN20AppleUSBNCM11Control27getExtendedFeatureWakeGatedEP15NCMWakeTypeCodePvPtPh
- __ZN20AppleUSBNCM11Control27getExtendedFeatureWakeGatedEP15NCMWakeTypeCodePvPtPh_vfpthunk_
- __ZN20AppleUSBNCM11Control27setExtendedFeatureWakeGatedEP15NCMWakeTypeCodePvPt
- __ZN20AppleUSBNCM11Control27setExtendedFeatureWakeGatedEP15NCMWakeTypeCodePvPt_vfpthunk_
- __ZN20AppleUSBNCM11Control28getExtendedCapabilitiesGatedEPvPt
- __ZN20AppleUSBNCM11Control28getExtendedCapabilitiesGatedEPvPt_vfpthunk_
- __ZN20AppleUSBNCM11Control30getExtendedCapabilityModeGatedEP25NCMExtendedCapabilityMode
- __ZN20AppleUSBNCM11Control30getExtendedCapabilityModeGatedEP25NCMExtendedCapabilityMode_vfpthunk_
- __ZN20AppleUSBNCM11Control30setExtendedCapabilityModeGatedEP25NCMExtendedCapabilityMode
- __ZN20AppleUSBNCM11Control30setExtendedCapabilityModeGatedEP25NCMExtendedCapabilityMode_vfpthunk_
- __ZN20AppleUSBNCM11Control32getExtendedFeatureMediumHandlingEP9NCMMedium
- __ZN20AppleUSBNCM11Control32getExtendedFeatureReceiveOffloadE25NCMReceiveOffloadTypeCodePvPt
- __ZN20AppleUSBNCM11Control32setExtendedFeatureMediumHandlingE9NCMMedium
- __ZN20AppleUSBNCM11Control32setExtendedFeatureReceiveOffloadE25NCMReceiveOffloadTypeCodePvt
- __ZN20AppleUSBNCM11Control33getExtendedFeaturePresenceOffloadE26NCMPresenceOffloadTypeCodePvPt
- __ZN20AppleUSBNCM11Control33setExtendedFeaturePresenceOffloadE26NCMPresenceOffloadTypeCodePvt
- __ZN20AppleUSBNCM11Control37getExtendedFeatureMediumHandlingGatedEP9NCMMedium
- __ZN20AppleUSBNCM11Control37getExtendedFeatureMediumHandlingGatedEP9NCMMedium_vfpthunk_
- __ZN20AppleUSBNCM11Control37getExtendedFeatureReceiveOffloadGatedEP25NCMReceiveOffloadTypeCodePvPt
- __ZN20AppleUSBNCM11Control37getExtendedFeatureReceiveOffloadGatedEP25NCMReceiveOffloadTypeCodePvPt_vfpthunk_
- __ZN20AppleUSBNCM11Control37setExtendedFeatureMediumHandlingGatedEP9NCMMedium
- __ZN20AppleUSBNCM11Control37setExtendedFeatureMediumHandlingGatedEP9NCMMedium_vfpthunk_
- __ZN20AppleUSBNCM11Control37setExtendedFeatureReceiveOffloadGatedEP25NCMReceiveOffloadTypeCodePvPt
- __ZN20AppleUSBNCM11Control37setExtendedFeatureReceiveOffloadGatedEP25NCMReceiveOffloadTypeCodePvPt_vfpthunk_
- __ZN20AppleUSBNCM11Control38getExtendedFeaturePresenceOffloadGatedEP26NCMPresenceOffloadTypeCodePvPt
- __ZN20AppleUSBNCM11Control38getExtendedFeaturePresenceOffloadGatedEP26NCMPresenceOffloadTypeCodePvPt_vfpthunk_
- __ZN20AppleUSBNCM11Control38setExtendedFeaturePresenceOffloadGatedEP26NCMPresenceOffloadTypeCodePvPt
- __ZN20AppleUSBNCM11Control38setExtendedFeaturePresenceOffloadGatedEP26NCMPresenceOffloadTypeCodePvPt_vfpthunk_
- __ZN20AppleUSBNCM11Control5probeEP9IOServicePi
- __ZN20AppleUSBNCM11Control5startEP9IOService
- __ZN20AppleUSBNCM11Control9MetaClassC1Ev
- __ZN20AppleUSBNCM11Control9MetaClassC2Ev
- __ZN20AppleUSBNCM11Control9MetaClassD0Ev
- __ZN20AppleUSBNCM11Control9MetaClassD1Ev
- __ZN20AppleUSBNCM11Control9metaClassE
- __ZN20AppleUSBNCM11ControlC1EPK11OSMetaClass
- __ZN20AppleUSBNCM11ControlC1Ev
- __ZN20AppleUSBNCM11ControlC2EPK11OSMetaClass
- __ZN20AppleUSBNCM11ControlC2Ev
- __ZN20AppleUSBNCM11ControlD0Ev
- __ZN20AppleUSBNCM11ControlD1Ev
- __ZN20AppleUSBNCM11ControlD2Ev
- __ZN20AppleUSBNCM11ControldlEPvm
- __ZN20AppleUSBNCM11ControlnwEm
- __ZN21AppleUSBNCMDataPoller10gMetaClassE
- __ZN21AppleUSBNCMDataPoller10superClassE
- __ZN21AppleUSBNCMDataPoller12checkForWorkEv
- __ZN21AppleUSBNCMDataPoller9MetaClassC1Ev
- __ZN21AppleUSBNCMDataPoller9MetaClassC2Ev
- __ZN21AppleUSBNCMDataPoller9MetaClassD0Ev
- __ZN21AppleUSBNCMDataPoller9MetaClassD1Ev
- __ZN21AppleUSBNCMDataPoller9metaClassE
- __ZN21AppleUSBNCMDataPollerC1EPK11OSMetaClass
- __ZN21AppleUSBNCMDataPollerC1Ev
- __ZN21AppleUSBNCMDataPollerC2EPK11OSMetaClass
- __ZN21AppleUSBNCMDataPollerC2Ev
- __ZN21AppleUSBNCMDataPollerD0Ev
- __ZN21AppleUSBNCMDataPollerD1Ev
- __ZN21AppleUSBNCMDataPollerD2Ev
- __ZN21AppleUSBNCMDataPollerdlEPvm
- __ZN21AppleUSBNCMDataPollernwEm
- __ZN8OSObject8DispatchE5IORPC
- __ZNK13IOEventSource11getWorkLoopEv
- __ZNK13IOEventSource7getNextEv
- __ZNK13IOEventSource8onThreadEv
- __ZNK13IOEventSource9getActionEv
- __ZNK13IOEventSource9isEnabledEv
- __ZNK17AppleUSBNCM11Data12getMetaClassEv
- __ZNK17AppleUSBNCM11Data9MetaClass5allocEv
- __ZNK20AppleUSBNCM11Control12getMetaClassEv
- __ZNK20AppleUSBNCM11Control9MetaClass5allocEv
- __ZNK21AppleUSBNCMDataPoller12getMetaClassEv
- __ZNK21AppleUSBNCMDataPoller9MetaClass5allocEv
- __ZTV17AppleUSBNCM11Data
- __ZTV20AppleUSBNCM11Control
- __ZTV21AppleUSBNCMDataPoller
- __ZTVN17AppleUSBNCM11Data9MetaClassE
- __ZTVN20AppleUSBNCM11Control9MetaClassE
- __ZTVN21AppleUSBNCMDataPoller9MetaClassE
- _dumpExtendedCapabilityDescriptor
- _snprintf
CStrings:
+ "%06lu.%06u %s::%s: %x \n"
+ "%06lu.%06u %s::%s: CRC Mode: %u status: %d\n"
+ "%06lu.%06u %s::%s: Datagram limit: %u status: %d\n"
+ "%06lu.%06u %s::%s: NTB Input size: %u status: %d\n"
+ "%06lu.%06u %s::%s: NTB format: %u status: %d\n"
+ "%06lu.%06u %s::%s: Setting CarPlay properties."
+ "%06lu.%06u %s::%s: Status: 0x%x\n"
+ "%06lu.%06u %s::%s: Unsupported role: %s\n"
+ "%06lu.%06u %s::%s: [IN] max size: %u divisor: %u payload remainder: %u alignment: %u\n"
+ "%06lu.%06u %s::%s: [OUT] max size: %u divisor: %u payload remainder: %u alignment: %u max datagrams: %u\n"
+ "%06lu.%06u %s::%s: capabilities %#lx\n"
+ "%06lu.%06u %s::%s: error waiting for BSD name %#x\n"
+ "%06lu.%06u %s::%s: fNetifEnabled %d, result %#x, bytesTransferred %d\n"
+ "%06lu.%06u %s::%s: failed to clear stall : 0x%x\n"
+ "%06lu.%06u %s::%s: filter: %u status: %#x\n"
+ "%06lu.%06u %s::%s: filter: %u status: %d\n"
+ "%06lu.%06u %s::%s: len: %u status: %d\n"
+ "%06lu.%06u %s::%s: length: %u supported formats: %u reserved: %u\n"
+ "%06lu.%06u %s::%s: linkStatus %d\n"
+ "%06lu.%06u %s::%s: linkStatus %d, fNetifEnabled %d\n"
+ "%06lu.%06u %s::%s: provider %p\n"
+ "%06lu.%06u %s::%s: re-enqueue after stall returned 0x%x\n"
+ "%06lu.%06u %s::%s: result %#x\n"
+ "%06lu.%06u %s::%s: result %d\n"
+ "%06lu.%06u %s::%s: result: %#x\n"
+ "%06lu.%06u %s::%s: result: %d\n"
+ "%06lu.%06u %s::%s: result: %d, IN EP 0x%x, OUT EP 0x%x\n"
+ "%06lu.%06u %s::%s: start waiting for BSD name\n"
+ "%06lu.%06u %s::%s: status %#x\n"
+ "%06lu.%06u %s::%s: terminating\n"
+ "%06lu.%06u %s::%s: unable to acquire ifnet pointer\n"
+ "%06lu.%06u %s::%s: unable to allocate thread call\n"
+ "%06lu.%06u %s::%s: unhandled notification %d\n"
+ "%06lu.%06u %s::%s: upSpeed %d, downSpeed %d\n"
+ "11"
+ "12111112122212121111111221211111111111211221121112211112111121111211112111121111211112111121111211112111121111211112111121111211112111121111121111121111121111121111121111121111121111121111121111121111121111121111121111121111121121122111112222222222221121112"
+ "1211111212221212111111211121121111222222222222222222"
+ "site.OutputPipeRecordQueue"
- "%06lu.%06u [0x%llx] %s::%s: "
- "%06lu.%06u [0x%llx] %s::%s:       • ARP: %s\n"
- "%06lu.%06u [0x%llx] %s::%s:       • Checksum: %s\n"
- "%06lu.%06u [0x%llx] %s::%s:       • Coalescing: %s\n"
- "%06lu.%06u [0x%llx] %s::%s:       • NS: %s\n"
- "%06lu.%06u [0x%llx] %s::%s:       • RSS: %s\n"
- "%06lu.%06u [0x%llx] %s::%s:       • Segmentation (TSO): %s\n"
- "%06lu.%06u [0x%llx] %s::%s:       • Store Bad Packets: %s\n"
- "%06lu.%06u [0x%llx] %s::%s:       • VLAN: %s\n"
- "%06lu.%06u [0x%llx] %s::%s:       • mDNS: %s\n"
- "%06lu.%06u [0x%llx] %s::%s:     - Any Packet: %s\n"
- "%06lu.%06u [0x%llx] %s::%s:     - Feature Flags: 0x%02x\n"
- "%06lu.%06u [0x%llx] %s::%s:     - Magic Packet: %s\n"
- "%06lu.%06u [0x%llx] %s::%s:     - Media Connect: %s\n"
- "%06lu.%06u [0x%llx] %s::%s:     - Media Disconnect: %s\n"
- "%06lu.%06u [0x%llx] %s::%s:     - Medium Type: %s (0x%02x)\n"
- "%06lu.%06u [0x%llx] %s::%s:     - Parameters: 0x%08x\n"
- "%06lu.%06u [0x%llx] %s::%s:     - Pattern Filter: %s\n"
- "%06lu.%06u [0x%llx] %s::%s:     - Presence Offload: %s\n"
- "%06lu.%06u [0x%llx] %s::%s:     - Receive Offload: %s\n"
- "%06lu.%06u [0x%llx] %s::%s:     - Speed: %u\n"
- "%06lu.%06u [0x%llx] %s::%s:     - TCP/UDP Port: %s\n"
- "%06lu.%06u [0x%llx] %s::%s:     - Transmit Offload: %s\n"
- "%06lu.%06u [0x%llx] %s::%s:     - mDNS Responder: %s\n"
- "%06lu.%06u [0x%llx] %s::%s:   Medium Handling: %s\n"
- "%06lu.%06u [0x%llx] %s::%s:   Offload Support: %s\n"
- "%06lu.%06u [0x%llx] %s::%s:   Wake Support: %s\n"
- "%06lu.%06u [0x%llx] %s::%s: %x \n"
- "%06lu.%06u [0x%llx] %s::%s: Attempting to fetch extended capabilities\n"
- "%06lu.%06u [0x%llx] %s::%s: Attempting to switch to NCM 1.1 mode\n"
- "%06lu.%06u [0x%llx] %s::%s: CRC Mode: %u status: %d\n"
- "%06lu.%06u [0x%llx] %s::%s: Datagram limit: %u status: %d\n"
- "%06lu.%06u [0x%llx] %s::%s: Device feature summary:\n"
- "%06lu.%06u [0x%llx] %s::%s: Device supports ARP presence offload\n"
- "%06lu.%06u [0x%llx] %s::%s: Device supports NS presence offload\n"
- "%06lu.%06u [0x%llx] %s::%s: Device supports RSS receive offload\n"
- "%06lu.%06u [0x%llx] %s::%s: Device supports VLAN receive offload\n"
- "%06lu.%06u [0x%llx] %s::%s: Device supports VLAN transmit offload\n"
- "%06lu.%06u [0x%llx] %s::%s: Device supports checksum receive offload\n"
- "%06lu.%06u [0x%llx] %s::%s: Device supports checksum transmit offload\n"
- "%06lu.%06u [0x%llx] %s::%s: Device supports coalescing receive offload\n"
- "%06lu.%06u [0x%llx] %s::%s: Device supports mDNS presence offload\n"
- "%06lu.%06u [0x%llx] %s::%s: Device supports segmentation transmit offload (TSO)\n"
- "%06lu.%06u [0x%llx] %s::%s: Device supports store bad packets receive offload\n"
- "%06lu.%06u [0x%llx] %s::%s: Device supports unknown feature selector: 0x%02x\n"
- "%06lu.%06u [0x%llx] %s::%s: Device supports unknown presence offload type: 0x%02x\n"
- "%06lu.%06u [0x%llx] %s::%s: Device supports unknown receive offload type: 0x%02x\n"
- "%06lu.%06u [0x%llx] %s::%s: Device supports unknown transmit offload type: 0x%02x\n"
- "%06lu.%06u [0x%llx] %s::%s: Device supports unknown wake type: 0x%02x\n"
- "%06lu.%06u [0x%llx] %s::%s: Extended Capabilities length: %u status: 0x%x\n"
- "%06lu.%06u [0x%llx] %s::%s: Extended Capability Mode: %u status: 0x%x\n"
- "%06lu.%06u [0x%llx] %s::%s: Medium Handling descriptor too small (%u bytes)\n"
- "%06lu.%06u [0x%llx] %s::%s: Medium Type: %u status: 0x%x\n"
- "%06lu.%06u [0x%llx] %s::%s: NCM 1.0 probe result %p, score %d\n"
- "%06lu.%06u [0x%llx] %s::%s: NCM 1.1 driver: device supports extended capabilities, probe score increased to %d\n"
- "%06lu.%06u [0x%llx] %s::%s: NCM 1.1 probe result %p, score %d\n"
- "%06lu.%06u [0x%llx] %s::%s: NTB Input size: %u status: %d\n"
- "%06lu.%06u [0x%llx] %s::%s: NTB format: %u status: %d\n"
- "%06lu.%06u [0x%llx] %s::%s: Parsing NCM Extended Capabilities (total length: %u)\n"
- "%06lu.%06u [0x%llx] %s::%s: Presence Offload Type: %u length: %u status: 0x%x\n"
- "%06lu.%06u [0x%llx] %s::%s: Presence Offload descriptor too small (%u bytes)\n"
- "%06lu.%06u [0x%llx] %s::%s: Receive Offload Type: %u length: %u status: 0x%x\n"
- "%06lu.%06u [0x%llx] %s::%s: Receive Offload descriptor too small (%u bytes)\n"
- "%06lu.%06u [0x%llx] %s::%s: Successfully switched to NCM 1.1 mode\n"
- "%06lu.%06u [0x%llx] %s::%s: Transmit Offload descriptor too small (%u bytes)\n"
- "%06lu.%06u [0x%llx] %s::%s: Wake Type: %u length: %u status: 0x%x\n"
- "%06lu.%06u [0x%llx] %s::%s: [IN] max size: %u divisor: %u payload remainder: %u alignment: %u\n"
- "%06lu.%06u [0x%llx] %s::%s: [OUT] max size: %u divisor: %u payload remainder: %u alignment: %u max datagrams: %u\n"
- "%06lu.%06u [0x%llx] %s::%s: _dataInterface %p\n"
- "%06lu.%06u [0x%llx] %s::%s: fEaddr : %02x:%02x:%02x:%02x:%02x:%02x, stringIndex %d\n"
- "%06lu.%06u [0x%llx] %s::%s: filter: %u status: %#x\n"
- "%06lu.%06u [0x%llx] %s::%s: filter: %u status: %d\n"
- "%06lu.%06u [0x%llx] %s::%s: len: %u status: %d\n"
- "%06lu.%06u [0x%llx] %s::%s: length: %u supported formats: %u reserved: %u\n"
- "%06lu.%06u [0x%llx] %s::%s: result %d\n"
- "%06lu.%06u [0x%llx] %s::%s: result %d for [0x%llx]\n"
- "%06lu.%06u [0x%llx] %s::%s: result: %d\n"
- "%06lu.%06u [0x%llx] %s::%s: returning %p\n"
- "%06lu.%06u [0x%llx][%s] %s::%s: Setting CarPlay properties."
- "%06lu.%06u [0x%llx][%s] %s::%s: Status: 0x%x\n"
- "%06lu.%06u [0x%llx][%s] %s::%s: Unsupported role: %s\n"
- "%06lu.%06u [0x%llx][%s] %s::%s: bNotification 0x%x\n"
- "%06lu.%06u [0x%llx][%s] %s::%s: capabilities %#lx\n"
- "%06lu.%06u [0x%llx][%s] %s::%s: error waiting for BSD name %#x\n"
- "%06lu.%06u [0x%llx][%s] %s::%s: fNetifEnabled %d, result %#x, bytesTransferred %d\n"
- "%06lu.%06u [0x%llx][%s] %s::%s: failed to clear stall : 0x%x\n"
- "%06lu.%06u [0x%llx][%s] %s::%s: linkStatus %d\n"
- "%06lu.%06u [0x%llx][%s] %s::%s: linkStatus %d, fNetifEnabled %d\n"
- "%06lu.%06u [0x%llx][%s] %s::%s: newMedium, bMediumType 0x%x, bmFeatureFlags 0x%x, dwSpeed 0x%x, bmMediumParameters 0x%x\n"
- "%06lu.%06u [0x%llx][%s] %s::%s: provider %p\n"
- "%06lu.%06u [0x%llx][%s] %s::%s: provider %p, fControlDriver %p\n"
- "%06lu.%06u [0x%llx][%s] %s::%s: re-enqueue after stall returned 0x%x\n"
- "%06lu.%06u [0x%llx][%s] %s::%s: result %#x\n"
- "%06lu.%06u [0x%llx][%s] %s::%s: result %d\n"
- "%06lu.%06u [0x%llx][%s] %s::%s: result: %#x\n"
- "%06lu.%06u [0x%llx][%s] %s::%s: result: %d\n"
- "%06lu.%06u [0x%llx][%s] %s::%s: result: %d, IN EP 0x%x, OUT EP 0x%x\n"
- "%06lu.%06u [0x%llx][%s] %s::%s: start waiting for BSD name\n"
- "%06lu.%06u [0x%llx][%s] %s::%s: status %#x\n"
- "%06lu.%06u [0x%llx][%s] %s::%s: terminating\n"
- "%06lu.%06u [0x%llx][%s] %s::%s: unable to acquire ifnet pointer\n"
- "%06lu.%06u [0x%llx][%s] %s::%s: unable to allocate thread call\n"
- "%06lu.%06u [0x%llx][%s] %s::%s: unhandled notification %d\n"
- "%06lu.%06u [0x%llx][%s] %s::%s: upSpeed %d, downSpeed %d\n"
- "121111121222121211111112212111111111211211211122111121111211112111121111211112111121111211112111121111211112111121111211112111121111211111211111211111211111211111211111211111211111211111211111211111211111211111211111211111211222211221111122222222112111211222222222"
- "12111112122212121111112111211211112222222222222222221"
- "1211111212221212111111211121121111222222222222222222122222222"
- "121112111"
- "AppleUSBNCM11Control"
- "AppleUSBNCM11Data"
- "AppleUSBNCMDataPoller"
- "Ethernet"
- "NCMOperatingMode"
- "NO"
- "Unknown"
- "Virtual Wire"
- "YES"
- "cacheExtendedDescriptors"
- "copyDataInterface"
- "getExtendedCapabilities"
- "getExtendedCapabilityMode"
- "getExtendedFeatureMediumHandling"
- "getExtendedFeaturePresenceOffload"
- "getExtendedFeatureReceiveOffload"
- "getExtendedFeatureWake"
- "getMACAddressFromDescriptor"
- "idProduct"
- "idVendor"
- "ncm11-enabled"
- "parseExtendedCapabilities"
- "probe"
- "setExtendedCapabilityMode"
- "setExtendedFeatureMediumHandling"
- "setExtendedFeaturePresenceOffload"
- "setExtendedFeatureReceiveOffload"
- "setExtendedFeatureWake"
- "site.AppleUSBNCM11Control"
- "site.AppleUSBNCM11Data"
- "site.AppleUSBNCMDataPoller"

```
