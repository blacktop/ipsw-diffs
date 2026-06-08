## AudioServerDriverTransports_IOP

> `/System/Library/PrivateFrameworks/AudioServerDriverTransports_IOP.framework/AudioServerDriverTransports_IOP`

```diff

-340.16.0.0.0
-  __TEXT.__text: 0xedc0
-  __TEXT.__auth_stubs: 0x730
-  __TEXT.__objc_methlist: 0xc8c
-  __TEXT.__gcc_except_tab: 0x137c
-  __TEXT.__const: 0x150
-  __TEXT.__oslogstring: 0xe8a
-  __TEXT.__cstring: 0xe6a
-  __TEXT.__unwind_info: 0x7d0
-  __TEXT.__objc_classname: 0x366
-  __TEXT.__objc_methname: 0x1454
-  __TEXT.__objc_methtype: 0x840
-  __TEXT.__objc_stubs: 0x14a0
-  __DATA_CONST.__got: 0x178
-  __DATA_CONST.__const: 0x120
-  __DATA_CONST.__objc_classlist: 0xc8
+400.29.0.0.0
+  __TEXT.__text: 0x19558
+  __TEXT.__objc_methlist: 0xfcc
+  __TEXT.__gcc_except_tab: 0x1c48
+  __TEXT.__const: 0x280
+  __TEXT.__oslogstring: 0x140d
+  __TEXT.__cstring: 0x188f
+  __TEXT.__unwind_info: 0xd80
+  __TEXT.__objc_stubs: 0x0
+  __TEXT.__auth_stubs: 0x0
+  __TEXT.__objc_classname: 0x0
+  __TEXT.__objc_methname: 0x0
+  __TEXT.__objc_methtype: 0x0
+  __DATA_CONST.__const: 0x1a0
+  __DATA_CONST.__objc_classlist: 0xe8
   __DATA_CONST.__objc_catlist: 0x8
   __DATA_CONST.__objc_protolist: 0x20
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x6f0
-  __DATA_CONST.__objc_superrefs: 0x90
-  __AUTH_CONST.__auth_got: 0x3b0
-  __AUTH_CONST.__const: 0x228
-  __AUTH_CONST.__cfstring: 0x360
-  __AUTH_CONST.__objc_const: 0x17d8
+  __DATA_CONST.__weak_got: 0x8
+  __DATA_CONST.__objc_selrefs: 0x950
+  __DATA_CONST.__objc_superrefs: 0xa0
+  __DATA_CONST.__got: 0x1b8
+  __AUTH_CONST.__const: 0x870
+  __AUTH_CONST.__cfstring: 0x300
+  __AUTH_CONST.__objc_const: 0x1c68
+  __AUTH_CONST.__weak_auth_got: 0x18
   __AUTH_CONST.__objc_intobj: 0x180
+  __AUTH_CONST.__auth_got: 0x0
   __AUTH.__objc_data: 0x230
-  __DATA.__objc_ivar: 0x64
-  __DATA.__data: 0x188
-  __DATA.__bss: 0x18
-  __DATA_DIRTY.__objc_data: 0x5a0
+  __DATA.__objc_ivar: 0x88
+  __DATA.__data: 0x190
+  __DATA.__bss: 0x8
+  __DATA.__common: 0x1
+  __DATA_DIRTY.__objc_data: 0x6e0
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/Foundation.framework/Foundation
   - /System/Library/Frameworks/IOKit.framework/Versions/A/IOKit

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libc++.1.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 55AC0575-618C-3FBA-A3D1-37271EF77F44
-  Functions: 455
-  Symbols:   1585
-  CStrings:  600
+  UUID: 2C3F141B-3B78-3E61-B0A8-8A4CC4FCFF13
+  Functions: 771
+  Symbols:   2283
+  CStrings:  358
 
Symbols:
+ +[ASDTIOPAudioCMDevice createUserClientForIOObject:andIDValue:]
+ +[ASDTIOPAudioStreamCMDevice ioServiceDependenciesForConfig:]
+ +[ASDTIOPAudioStreamCMService createUserClientForIOObject:andIDValue:]
+ +[ASDTIOPAudioStreamCMService forIOObject:andIDValue:]
+ +[ASDTIOPAudioStreamCMServiceManager ioServiceClassName]
+ +[ASDTIOPAudioStreamCMServiceManager ioServiceIDProperty]
+ +[ASDTIOPAudioStreamCMStream forConfig:iopConfig:withDevice:]
+ -[ASDTIOPAudioCMDevice clientManagerUserClient]
+ -[ASDTIOPAudioStreamCMDevice .cxx_construct]
+ -[ASDTIOPAudioStreamCMDevice .cxx_destruct]
+ -[ASDTIOPAudioStreamCMDevice _updateTimestampPeriod:]
+ -[ASDTIOPAudioStreamCMDevice addStreams:]
+ -[ASDTIOPAudioStreamCMDevice addStreams:].cold.1
+ -[ASDTIOPAudioStreamCMDevice getZeroTimestampBlock]
+ -[ASDTIOPAudioStreamCMDevice performPowerStateIdle:]
+ -[ASDTIOPAudioStreamCMDevice performPowerStatePrepare:]
+ -[ASDTIOPAudioStreamCMDevice performPowerStatePrepare:].cold.1
+ -[ASDTIOPAudioStreamCMDevice performPowerStatePrewarm:]
+ -[ASDTIOPAudioStreamCMDevice performPowerStatePrewarm:].cold.1
+ -[ASDTIOPAudioStreamCMDevice requestConfigurationChange:]
+ -[ASDTIOPAudioStreamCMDevice setStreamCMService:]
+ -[ASDTIOPAudioStreamCMDevice setTimestampMemoryMap:]
+ -[ASDTIOPAudioStreamCMDevice setupSamplingRates:]
+ -[ASDTIOPAudioStreamCMDevice setupSamplingRates:].cold.1
+ -[ASDTIOPAudioStreamCMDevice setupSamplingRates:].cold.2
+ -[ASDTIOPAudioStreamCMDevice setupSamplingRates:].cold.3
+ -[ASDTIOPAudioStreamCMDevice streamCMService]
+ -[ASDTIOPAudioStreamCMDevice subclassInitWithConfig:]
+ -[ASDTIOPAudioStreamCMDevice timeInterface]
+ -[ASDTIOPAudioStreamCMDevice timestampMemoryMap]
+ -[ASDTIOPAudioStreamCMDevice updateFromRegistry]
+ -[ASDTIOPAudioStreamCMDevice updateFromRegistry].cold.1
+ -[ASDTIOPAudioStreamCMService clockDomain]
+ -[ASDTIOPAudioStreamCMService clockDomain].cold.1
+ -[ASDTIOPAudioStreamCMService getBooleanControl:withValue:]
+ -[ASDTIOPAudioStreamCMService getBooleanControl:withValue:].cold.1
+ -[ASDTIOPAudioStreamCMService getBooleanControl:withValue:].cold.2
+ -[ASDTIOPAudioStreamCMService mapMemoryForStream:]
+ -[ASDTIOPAudioStreamCMService mapMemoryForStream:].cold.1
+ -[ASDTIOPAudioStreamCMService selectStreamDescriptionAtIndex:forStream:]
+ -[ASDTIOPAudioStreamCMService selectStreamDescriptionAtIndex:forStream:].cold.1
+ -[ASDTIOPAudioStreamCMService setBooleanControl:withValue:]
+ -[ASDTIOPAudioStreamCMService setBooleanControl:withValue:].cold.1
+ -[ASDTIOPAudioStreamCMService streamCMUserClient]
+ -[ASDTIOPAudioStreamCMService streams]
+ -[ASDTIOPAudioStreamCMService streams].cold.1
+ -[ASDTIOPAudioStreamCMServiceManager serviceForIOObject:andIDValue:]
+ -[ASDTIOPAudioStreamCMStream .cxx_construct]
+ -[ASDTIOPAudioStreamCMStream .cxx_destruct]
+ -[ASDTIOPAudioStreamCMStream bufferFrames]
+ -[ASDTIOPAudioStreamCMStream bufferMapping]
+ -[ASDTIOPAudioStreamCMStream bufferMemory]
+ -[ASDTIOPAudioStreamCMStream changePhysicalFormat:]
+ -[ASDTIOPAudioStreamCMStream getZeroTimestampBlock]
+ -[ASDTIOPAudioStreamCMStream identifier]
+ -[ASDTIOPAudioStreamCMStream initWithConfig:iopConfig:withDevice:]
+ -[ASDTIOPAudioStreamCMStream mapPacketBuffer]
+ -[ASDTIOPAudioStreamCMStream packetCount]
+ -[ASDTIOPAudioStreamCMStream pmIdleStream:]
+ -[ASDTIOPAudioStreamCMStream pmOnStream]
+ -[ASDTIOPAudioStreamCMStream pmPrepareStream:]
+ -[ASDTIOPAudioStreamCMStream readOrWriteBlock]
+ -[ASDTIOPAudioStreamCMStream setBufferFrames:]
+ -[ASDTIOPAudioStreamCMStream setBufferMemory:]
+ -[ASDTIOPAudioStreamCMStream setGetZeroTimestampBlock:]
+ -[ASDTIOPAudioStreamCMStream setPacketCount:]
+ -[ASDTIOPAudioStreamCMStream setPhysicalFormat:]
+ -[ASDTIOPAudioStreamCMStream setupPhysicalFormat:]
+ -[ASDTIOPAudioStreamCMStream streamCMDevice]
+ -[ASDTIOPAudioStreamCMStream streamCMService]
+ -[ASDTIOPAudioStreamCMStream updateFromRegistry:]
+ -[NSDictionary(ASDTStreamCM) asdtStreamCMAvailableFormats]
+ -[NSDictionary(ASDTStreamCM) asdtStreamCMBufferFrames]
+ -[NSDictionary(ASDTStreamCM) asdtStreamCMCurrentFormat]
+ -[NSDictionary(ASDTStreamCM) asdtStreamCMFormat]
+ -[NSDictionary(ASDTStreamCM) asdtStreamCMIdentifierStr]
+ -[NSDictionary(ASDTStreamCM) asdtStreamCMIdentifier]
+ -[NSDictionary(ASDTStreamCM) asdtStreamCMInfoForStream:]
+ -[NSDictionary(ASDTStreamCM) asdtStreamCMInfoForStreamStr:]
+ -[NSDictionary(ASDTStreamCM) asdtStreamCMLatency]
+ -[NSDictionary(ASDTStreamCM) asdtStreamCMPacketCount]
+ -[NSDictionary(ASDTStreamCM) asdtStreamCMSafetyOffset]
+ -[NSDictionary(ASDTStreamCM) asdtStreamCMTerminalType]
+ GCC_except_table37
+ _OBJC_CLASS_$_ASDTIOPAudioStreamCMDevice
+ _OBJC_CLASS_$_ASDTIOPAudioStreamCMDeviceFactory
+ _OBJC_CLASS_$_ASDTIOPAudioStreamCMService
+ _OBJC_CLASS_$_ASDTIOPAudioStreamCMServiceManager
+ _OBJC_CLASS_$_ASDTIOPAudioStreamCMStream
+ _OBJC_CLASS_$_ASDTIOServiceMemory
+ _OBJC_CLASS_$_ASDTStream
+ _OBJC_CLASS_$_NSMutableArray
+ _OBJC_CLASS_$_NSMutableOrderedSet
+ _OBJC_IVAR_$_ASDTIOPAudioStreamCMDevice._streamCMService
+ _OBJC_IVAR_$_ASDTIOPAudioStreamCMDevice._timeInterface
+ _OBJC_IVAR_$_ASDTIOPAudioStreamCMDevice._timestampMemoryMap
+ _OBJC_IVAR_$_ASDTIOPAudioStreamCMStream._bufferFrames
+ _OBJC_IVAR_$_ASDTIOPAudioStreamCMStream._bufferMapping
+ _OBJC_IVAR_$_ASDTIOPAudioStreamCMStream._bufferMemory
+ _OBJC_IVAR_$_ASDTIOPAudioStreamCMStream._getZeroTimestampBlock
+ _OBJC_IVAR_$_ASDTIOPAudioStreamCMStream._identifier
+ _OBJC_IVAR_$_ASDTIOPAudioStreamCMStream._packetCount
+ _OBJC_METACLASS_$_ASDTIOPAudioStreamCMDevice
+ _OBJC_METACLASS_$_ASDTIOPAudioStreamCMDeviceFactory
+ _OBJC_METACLASS_$_ASDTIOPAudioStreamCMService
+ _OBJC_METACLASS_$_ASDTIOPAudioStreamCMServiceManager
+ _OBJC_METACLASS_$_ASDTIOPAudioStreamCMStream
+ _OBJC_METACLASS_$_ASDTStream
+ __OBJC_$_CATEGORY_NSDictionary_$_ASDTStreamCM
+ __OBJC_$_CLASS_METHODS_ASDTIOPAudioStreamCMDevice
+ __OBJC_$_CLASS_METHODS_ASDTIOPAudioStreamCMService
+ __OBJC_$_CLASS_METHODS_ASDTIOPAudioStreamCMServiceManager
+ __OBJC_$_CLASS_METHODS_ASDTIOPAudioStreamCMStream
+ __OBJC_$_INSTANCE_METHODS_ASDTIOPAudioStreamCMDevice
+ __OBJC_$_INSTANCE_METHODS_ASDTIOPAudioStreamCMService
+ __OBJC_$_INSTANCE_METHODS_ASDTIOPAudioStreamCMServiceManager
+ __OBJC_$_INSTANCE_METHODS_ASDTIOPAudioStreamCMStream
+ __OBJC_$_INSTANCE_METHODS_NSDictionary(ASDTStreamCM|ASDTIOPAudioConfig)
+ __OBJC_$_INSTANCE_VARIABLES_ASDTIOPAudioStreamCMDevice
+ __OBJC_$_INSTANCE_VARIABLES_ASDTIOPAudioStreamCMStream
+ __OBJC_$_PROP_LIST_ASDTIOPAudioStreamCMDevice
+ __OBJC_$_PROP_LIST_ASDTIOPAudioStreamCMService
+ __OBJC_$_PROP_LIST_ASDTIOPAudioStreamCMStream
+ __OBJC_CLASS_PROTOCOLS_$_ASDTIOPAudioStreamCMDevice
+ __OBJC_CLASS_RO_$_ASDTIOPAudioStreamCMDevice
+ __OBJC_CLASS_RO_$_ASDTIOPAudioStreamCMDeviceFactory
+ __OBJC_CLASS_RO_$_ASDTIOPAudioStreamCMService
+ __OBJC_CLASS_RO_$_ASDTIOPAudioStreamCMServiceManager
+ __OBJC_CLASS_RO_$_ASDTIOPAudioStreamCMStream
+ __OBJC_METACLASS_RO_$_ASDTIOPAudioStreamCMDevice
+ __OBJC_METACLASS_RO_$_ASDTIOPAudioStreamCMDeviceFactory
+ __OBJC_METACLASS_RO_$_ASDTIOPAudioStreamCMService
+ __OBJC_METACLASS_RO_$_ASDTIOPAudioStreamCMServiceManager
+ __OBJC_METACLASS_RO_$_ASDTIOPAudioStreamCMStream
+ __ZL15gASDTIOPLogType
+ __ZN10applesauce2CF8ArrayRefD2Ev
+ __ZN19RTKitAudioFramework11gLogChannelE
+ __ZN19RTKitAudioFramework12RingBufferV211AtomicIndex6kMagicE
+ __ZN19RTKitAudioFramework12RingBufferV211setItemSizeEj
+ __ZN19RTKitAudioFramework12RingBufferV212ControlBlock6kMagicE
+ __ZN19RTKitAudioFramework12RingBufferV216writeAtomicIndexERNS0_11AtomicIndexE
+ __ZN19RTKitAudioFramework12RingBufferV217writeControlBlockERKNS0_11AtomicIndexERKNS0_12ControlBlockE
+ __ZN19RTKitAudioFramework12RingBufferV24initEv
+ __ZN19RTKitAudioFramework12RingBufferV25resetEv
+ __ZN19RTKitAudioFramework12RingBufferV25writeERKNS_8IOBufferEPNS_12ElementArrayIS1_EE
+ __ZN19RTKitAudioFramework12RingBufferV2C1ERNS_6BufferES2_S2_jj
+ __ZN19RTKitAudioFramework12RingBufferV2C2ERNS_6BufferES2_S2_jj
+ __ZN19RTKitAudioFramework12RingBufferV2D0Ev
+ __ZN19RTKitAudioFramework12RingBufferV2D1Ev
+ __ZN19RTKitAudioFramework13IMappedBuffer10clearStateEv
+ __ZN19RTKitAudioFramework13IMappedBuffer10resetFlagsEj
+ __ZN19RTKitAudioFramework13IMappedBuffer11removeFlagsEj
+ __ZN19RTKitAudioFramework13IMappedBuffer8addFlagsEj
+ __ZN19RTKitAudioFramework13getLogChannelEv
+ __ZN19RTKitAudioFramework13setLogChannelEP8os_log_s
+ __ZN19RTKitAudioFramework14initLogChannelEv
+ __ZN19RTKitAudioFramework15XnuMappedBuffer5unmapEv
+ __ZN19RTKitAudioFramework15XnuMappedBuffer5writeERKNS_8IOBufferEj
+ __ZN19RTKitAudioFramework15XnuMappedBuffer8mapLocalEPvm
+ __ZN19RTKitAudioFramework15XnuMappedBuffer9mapByNameEym
+ __ZN19RTKitAudioFramework15XnuMappedBuffer9mapRemoteEmm
+ __ZN19RTKitAudioFramework15XnuMappedBufferC1ERNS0_6ConfigE
+ __ZN19RTKitAudioFramework15XnuMappedBufferC2ERNS0_6ConfigE
+ __ZN19RTKitAudioFramework15XnuMappedBufferD0Ev
+ __ZN19RTKitAudioFramework15XnuMappedBufferD1Ev
+ __ZN19RTKitAudioFramework15XnuMappedBufferD2Ev
+ __ZN19RTKitAudioFramework16gLogChannelIsSetE
+ __ZN19RTKitAudioFramework17AudioOutputWriter13_doTSTrackingERKNS_23AudioOutputRingBufferV213TimestampDataERS2_
+ __ZN19RTKitAudioFramework17AudioOutputWriter15getDMATimestampERNS_23AudioOutputRingBufferV213TimestampDataE
+ __ZN19RTKitAudioFramework17AudioOutputWriter17getWriteTimestampERNS_23AudioOutputRingBufferV213TimestampDataE
+ __ZN19RTKitAudioFramework17AudioOutputWriter4initEv
+ __ZN19RTKitAudioFramework17AudioOutputWriter5resetEv
+ __ZN19RTKitAudioFramework17AudioOutputWriter5writeERKNS_8IOBufferE
+ __ZN19RTKitAudioFramework17AudioOutputWriter5writeEyRKNS_8IOBufferE
+ __ZN19RTKitAudioFramework17AudioOutputWriterC1ERNS_23AudioOutputRingBufferV2ERNS_13TimeGeneratorEjj
+ __ZN19RTKitAudioFramework17AudioOutputWriterC2ERNS_23AudioOutputRingBufferV2ERNS_13TimeGeneratorEjj
+ __ZN19RTKitAudioFramework17AudioOutputWriterD0Ev
+ __ZN19RTKitAudioFramework17AudioOutputWriterD1Ev
+ __ZN19RTKitAudioFramework17AudioRingBufferV220setStreamDescriptionERKNS_17StreamDescriptionE
+ __ZN19RTKitAudioFramework17AudioRingBufferV24initEv
+ __ZN19RTKitAudioFramework17AudioRingBufferV25resetEv
+ __ZN19RTKitAudioFramework17AudioRingBufferV2D0Ev
+ __ZN19RTKitAudioFramework17AudioRingBufferV2D1Ev
+ __ZN19RTKitAudioFramework18RingBufferV2Reader21_getCurrentReaderInfoERNS0_10ReaderInfoE
+ __ZN19RTKitAudioFramework18RingBufferV2Reader23_resetCurrentReaderInfoERNS0_10ReaderInfoE
+ __ZN19RTKitAudioFramework18RingBufferV2Reader4initEv
+ __ZN19RTKitAudioFramework18RingBufferV2Reader4readEPvm
+ __ZN19RTKitAudioFramework18RingBufferV2Reader4readERNS_8IOBufferERm
+ __ZN19RTKitAudioFramework18RingBufferV2Reader4readEyRNS_8IOBufferERm
+ __ZN19RTKitAudioFramework18RingBufferV2Reader5_readERyRjjRNS_8IOBufferERm
+ __ZN19RTKitAudioFramework18RingBufferV2Reader5resetEj
+ __ZN19RTKitAudioFramework18RingBufferV2Reader6_resetERNS_12RingBufferV212ControlBlockEj
+ __ZN19RTKitAudioFramework18RingBufferV2ReaderC1ERNS_12RingBufferV2Ej
+ __ZN19RTKitAudioFramework18RingBufferV2ReaderC2ERNS_12RingBufferV2Ej
+ __ZN19RTKitAudioFramework18RingBufferV2ReaderD0Ev
+ __ZN19RTKitAudioFramework18RingBufferV2ReaderD1Ev
+ __ZN19RTKitAudioFramework18RingBufferV2Writer11setItemSizeEm
+ __ZN19RTKitAudioFramework18RingBufferV2Writer16setWritePositionEy
+ __ZN19RTKitAudioFramework18RingBufferV2Writer22incrementWritePositionEm
+ __ZN19RTKitAudioFramework18RingBufferV2Writer4initEv
+ __ZN19RTKitAudioFramework18RingBufferV2Writer5resetEv
+ __ZN19RTKitAudioFramework18RingBufferV2Writer5writeENS_12RingBufferV212ControlBlockERKNS_8IOBufferEPNS_12ElementArrayIS3_EE
+ __ZN19RTKitAudioFramework18RingBufferV2Writer5writeEPvm
+ __ZN19RTKitAudioFramework18RingBufferV2Writer5writeERKNS_8IOBufferEPNS_12ElementArrayIS1_EE
+ __ZN19RTKitAudioFramework18RingBufferV2Writer5writeEyRKNS_8IOBufferEPNS_12ElementArrayIS1_EE
+ __ZN19RTKitAudioFramework18RingBufferV2WriterC1ERNS_12RingBufferV2E
+ __ZN19RTKitAudioFramework18RingBufferV2WriterC2ERNS_12RingBufferV2E
+ __ZN19RTKitAudioFramework18RingBufferV2WriterD0Ev
+ __ZN19RTKitAudioFramework18RingBufferV2WriterD1Ev
+ __ZN19RTKitAudioFramework20MappedSubrangeBuffer10clearStateEv
+ __ZN19RTKitAudioFramework20MappedSubrangeBuffer11setSubRangeEjm
+ __ZN19RTKitAudioFramework20MappedSubrangeBuffer5writeERKNS_8IOBufferEj
+ __ZN19RTKitAudioFramework20MappedSubrangeBufferC1ERNS_13IMappedBufferE
+ __ZN19RTKitAudioFramework20MappedSubrangeBufferC2ERNS_13IMappedBufferE
+ __ZN19RTKitAudioFramework20MappedSubrangeBufferD0Ev
+ __ZN19RTKitAudioFramework20MappedSubrangeBufferD1Ev
+ __ZN19RTKitAudioFramework23AudioOutputRingBufferV213readTimestampEjRNS0_13TimestampDataE
+ __ZN19RTKitAudioFramework23AudioOutputRingBufferV214writeTimestampERKNS0_13TimestampDataE
+ __ZN19RTKitAudioFramework23AudioOutputRingBufferV220setStreamDescriptionERKNS_17StreamDescriptionE
+ __ZN19RTKitAudioFramework23AudioOutputRingBufferV24initEv
+ __ZN19RTKitAudioFramework23AudioOutputRingBufferV25resetEv
+ __ZN19RTKitAudioFramework23AudioOutputRingBufferV25writeERKNS_8IOBufferE
+ __ZN19RTKitAudioFramework23AudioOutputRingBufferV2D0Ev
+ __ZN19RTKitAudioFramework23AudioOutputRingBufferV2D1Ev
+ __ZN19RTKitAudioFramework23AudioPacketRingBufferV220setStreamDescriptionERKNS_17StreamDescriptionE
+ __ZN19RTKitAudioFramework23AudioPacketRingBufferV24initEv
+ __ZN19RTKitAudioFramework23AudioPacketRingBufferV25resetEv
+ __ZN19RTKitAudioFramework23AudioPacketRingBufferV2D0Ev
+ __ZN19RTKitAudioFramework23AudioPacketRingBufferV2D1Ev
+ __ZN19RTKitAudioFramework23AudioRingBufferV2WriterD0Ev
+ __ZN19RTKitAudioFramework23AudioRingBufferV2WriterD1Ev
+ __ZN19RTKitAudioFramework29AudioPacketRingBufferV2Reader13readAllCommonEPNS_9Interface12Audio3PacketERmbNS_12RingBufferV214CacheOperationEb
+ __ZN19RTKitAudioFramework29AudioPacketRingBufferV2Reader13readForPacketERKNS_9Interface12Audio3PacketENS_8IOBufferERm
+ __ZN19RTKitAudioFramework29AudioPacketRingBufferV2Reader4initEv
+ __ZN19RTKitAudioFramework29AudioPacketRingBufferV2Reader4readERNS_9Interface12Audio3PacketENS_12RingBufferV214CacheOperationE
+ __ZN19RTKitAudioFramework29AudioPacketRingBufferV2Reader4readERNS_9Interface12Audio3PacketENS_8IOBufferE
+ __ZN19RTKitAudioFramework29AudioPacketRingBufferV2Reader4readEyNS_8IOBufferERm
+ __ZN19RTKitAudioFramework29AudioPacketRingBufferV2Reader5resetEj
+ __ZN19RTKitAudioFramework29AudioPacketRingBufferV2Reader7peekAllEPNS_9Interface12Audio3PacketERmbNS_12RingBufferV214CacheOperationE
+ __ZN19RTKitAudioFramework29AudioPacketRingBufferV2Reader7readAllEPNS_9Interface12Audio3PacketERmbNS_12RingBufferV214CacheOperationE
+ __ZN19RTKitAudioFramework29AudioPacketRingBufferV2ReaderD0Ev
+ __ZN19RTKitAudioFramework29AudioPacketRingBufferV2ReaderD1Ev
+ __ZN19RTKitAudioFramework6Buffer10clearStateEv
+ __ZN19RTKitAudioFramework6Buffer3setEjmh
+ __ZN19RTKitAudioFramework6Buffer4initEPvm
+ __ZN19RTKitAudioFramework6Buffer5clearEv
+ __ZN19RTKitAudioFramework6Buffer5writeERKNS_8IOBufferEj
+ __ZN19RTKitAudioFramework6BufferC1ERS0_jm
+ __ZN19RTKitAudioFramework6BufferC2ERS0_jm
+ __ZN19RTKitAudioFramework6BufferC2ERS0_jm.cold.1
+ __ZN19RTKitAudioFramework6BufferD0Ev
+ __ZN19RTKitAudioFramework6BufferD1Ev
+ __ZN19RTKitAudioFramework8IOBuffer11setItemSizeEm
+ __ZN19RTKitAudioFramework8IOBuffer3setEPvmm
+ __ZN19RTKitAudioFramework8IOBuffer3setEPvmm.cold.1
+ __ZN19RTKitAudioFramework8IOBufferC1EPKvmm
+ __ZN19RTKitAudioFramework8IOBufferC2EPKvmm
+ __ZN19RTKitAudioFramework8IOBufferC2EPKvmm.cold.1
+ __ZN19RTKitAudioFramework8IOBufferpLEm
+ __ZN19RTKitAudioFramework8IOPAudio13BufferMapping10mapAsOwnerEv
+ __ZN19RTKitAudioFramework8IOPAudio13BufferMapping10readyCheckEv
+ __ZN19RTKitAudioFramework8IOPAudio13BufferMapping13mapAsConsumerEv
+ __ZN19RTKitAudioFramework8IOPAudio13BufferMapping13setBufferSpecERKNS_10BufferSpecE
+ __ZN19RTKitAudioFramework8IOPAudio13BufferMapping3mapEv
+ __ZN19RTKitAudioFramework8IOPAudio13BufferMapping4_mapEv
+ __ZN19RTKitAudioFramework8IOPAudio13BufferMapping5unmapEv
+ __ZN19RTKitAudioFramework8IOPAudio13BufferMappingC1ERNS1_6ConfigE
+ __ZN19RTKitAudioFramework8IOPAudio13BufferMappingC2ERNS1_6ConfigE
+ __ZN19RTKitAudioFramework8IOPAudio13BufferMappingD0Ev
+ __ZN19RTKitAudioFramework8IOPAudio13BufferMappingD1Ev
+ __ZN19RTKitAudioFramework8IOPAudio16XnuBufferMapping10readyCheckEv
+ __ZN19RTKitAudioFramework8IOPAudio16XnuBufferMapping3mapEv
+ __ZN19RTKitAudioFramework8IOPAudio16XnuBufferMapping5unmapEv
+ __ZN19RTKitAudioFramework8IOPAudio16XnuBufferMappingC1ENS_15XnuMappedBuffer6ConfigERNS0_23PacketRingBufferMappingE
+ __ZN19RTKitAudioFramework8IOPAudio16XnuBufferMappingC2ENS_15XnuMappedBuffer6ConfigERNS0_23PacketRingBufferMappingE
+ __ZN19RTKitAudioFramework8IOPAudio16XnuBufferMappingD0Ev
+ __ZN19RTKitAudioFramework8IOPAudio16XnuBufferMappingD1Ev
+ __ZN19RTKitAudioFramework8IOPAudio18InputBufferMapping21_setStreamDescriptionERKNS_17StreamDescriptionE
+ __ZN19RTKitAudioFramework8IOPAudio18InputBufferMapping28bufferSizesForPacketCapacityEmRmS2_
+ __ZN19RTKitAudioFramework8IOPAudio18InputBufferMappingC1ERNS0_23PacketRingBufferMapping6ConfigERKNS_17StreamDescriptionE
+ __ZN19RTKitAudioFramework8IOPAudio18InputBufferMappingC2ERNS0_23PacketRingBufferMapping6ConfigERKNS_17StreamDescriptionE
+ __ZN19RTKitAudioFramework8IOPAudio18InputBufferMappingD0Ev
+ __ZN19RTKitAudioFramework8IOPAudio18InputBufferMappingD1Ev
+ __ZN19RTKitAudioFramework8IOPAudio19OutputBufferMapping21_setStreamDescriptionERKNS_17StreamDescriptionE
+ __ZN19RTKitAudioFramework8IOPAudio19OutputBufferMapping28bufferSizesForPacketCapacityEmRmS2_
+ __ZN19RTKitAudioFramework8IOPAudio19OutputBufferMappingC1ERNS0_23PacketRingBufferMapping6ConfigERKNS_17StreamDescriptionE
+ __ZN19RTKitAudioFramework8IOPAudio19OutputBufferMappingC2ERNS0_23PacketRingBufferMapping6ConfigERKNS_17StreamDescriptionE
+ __ZN19RTKitAudioFramework8IOPAudio19OutputBufferMappingD0Ev
+ __ZN19RTKitAudioFramework8IOPAudio19OutputBufferMappingD1Ev
+ __ZN19RTKitAudioFramework8IOPAudio21XnuInputBufferMappingC1EPvmRKNS_17StreamDescriptionE
+ __ZN19RTKitAudioFramework8IOPAudio21XnuInputBufferMappingC2EPvmRKNS_17StreamDescriptionE
+ __ZN19RTKitAudioFramework8IOPAudio21XnuInputBufferMappingD0Ev
+ __ZN19RTKitAudioFramework8IOPAudio21XnuInputBufferMappingD1Ev
+ __ZN19RTKitAudioFramework8IOPAudio22XnuOutputBufferMappingC1EPvmjRKNS_17StreamDescriptionERNS_13TimeGeneratorE
+ __ZN19RTKitAudioFramework8IOPAudio22XnuOutputBufferMappingC2EPvmjRKNS_17StreamDescriptionERNS_13TimeGeneratorE
+ __ZN19RTKitAudioFramework8IOPAudio22XnuOutputBufferMappingD0Ev
+ __ZN19RTKitAudioFramework8IOPAudio22XnuOutputBufferMappingD1Ev
+ __ZN19RTKitAudioFramework8IOPAudio23PacketRingBufferMapping10mapAsOwnerEv
+ __ZN19RTKitAudioFramework8IOPAudio23PacketRingBufferMapping10readyCheckEv
+ __ZN19RTKitAudioFramework8IOPAudio23PacketRingBufferMapping13mapAsConsumerEv
+ __ZN19RTKitAudioFramework8IOPAudio23PacketRingBufferMapping19setupDataRingBufferEv
+ __ZN19RTKitAudioFramework8IOPAudio23PacketRingBufferMapping20setStreamDescriptionERKNS_17StreamDescriptionE
+ __ZN19RTKitAudioFramework8IOPAudio23PacketRingBufferMapping20setupSubrangeBuffersEv
+ __ZN19RTKitAudioFramework8IOPAudio23PacketRingBufferMapping5unmapEv
+ __ZN19RTKitAudioFramework8IOPAudio23PacketRingBufferMapping9getHeaderEv
+ __ZN19RTKitAudioFramework8IOPAudio23PacketRingBufferMappingC2ERNS1_6ConfigE
+ __ZN19RTKitAudioFramework8IOPAudio23PacketRingBufferMappingD0Ev
+ __ZN19RTKitAudioFramework8IOPAudio23PacketRingBufferMappingD1Ev
+ __ZN4ASDT12IOUserClient12ConvertValueERKN10applesauce2CF7TypeRefERNS2_8ArrayRefE
+ __ZN4ASDT13RTKAFwkHelper25streamDescriptionFromADBDERK27AudioStreamBasicDescriptionRN19RTKitAudioFramework17StreamDescriptionE
+ __ZN4ASDT8IOPAudio13BufferMapping13timeForFramesEj
+ __ZN4ASDT8IOPAudio13BufferMapping16getZeroTimestampERNS1_9TimestampE
+ __ZN4ASDT8IOPAudio13BufferMapping18calculateZTSPeriodEv
+ __ZN4ASDT8IOPAudio13BufferMapping6createEbRNS_13TimeInterfaceEPvjjjjRK27AudioStreamBasicDescription
+ __ZN4ASDT8IOPAudio13BufferMapping6createEbRNS_13TimeInterfaceEPvjjjjRK27AudioStreamBasicDescription.cold.1
+ __ZN4ASDT8IOPAudio13BufferMapping6createEbRNS_13TimeInterfaceEPvjjjjRK27AudioStreamBasicDescription.cold.2
+ __ZN4ASDT8IOPAudio13BufferMapping6createEbRNS_13TimeInterfaceEPvjjjjRK27AudioStreamBasicDescription.cold.3
+ __ZN4ASDT8IOPAudio13BufferMapping9checkSeedEj
+ __ZN4ASDT8IOPAudio13BufferMappingC2ERNS_13TimeInterfaceEjj
+ __ZN4ASDT8IOPAudio13BufferMappingD0Ev
+ __ZN4ASDT8IOPAudio13BufferMappingD1Ev
+ __ZN4ASDT8IOPAudio18InputBufferMapping10readyCheckEv
+ __ZN4ASDT8IOPAudio18InputBufferMapping12getTimestampERNS0_13BufferMapping9TimestampE
+ __ZN4ASDT8IOPAudio18InputBufferMapping19updateAvailableDataEv
+ __ZN4ASDT8IOPAudio18InputBufferMapping4initEv
+ __ZN4ASDT8IOPAudio18InputBufferMapping4readEyjPv
+ __ZN4ASDT8IOPAudio18InputBufferMapping5writeEyjPKv
+ __ZN4ASDT8IOPAudio18InputBufferMapping7prepareEv
+ __ZN4ASDT8IOPAudio18InputBufferMappingC1ERNS_13TimeInterfaceEPvjjjRKN19RTKitAudioFramework17StreamDescriptionE
+ __ZN4ASDT8IOPAudio18InputBufferMappingC2ERNS_13TimeInterfaceEPvjjjRKN19RTKitAudioFramework17StreamDescriptionE
+ __ZN4ASDT8IOPAudio18InputBufferMappingD0Ev
+ __ZN4ASDT8IOPAudio18InputBufferMappingD1Ev
+ __ZN4ASDT8IOPAudio19OutputBufferMapping10readyCheckEv
+ __ZN4ASDT8IOPAudio19OutputBufferMapping12getTimestampERNS0_13BufferMapping9TimestampE
+ __ZN4ASDT8IOPAudio19OutputBufferMapping4initEv
+ __ZN4ASDT8IOPAudio19OutputBufferMapping4readEyjPv
+ __ZN4ASDT8IOPAudio19OutputBufferMapping5writeEyjPKv
+ __ZN4ASDT8IOPAudio19OutputBufferMapping7prepareEv
+ __ZN4ASDT8IOPAudio19OutputBufferMappingC1ERNS_13TimeInterfaceEPvjjjjRKN19RTKitAudioFramework17StreamDescriptionE
+ __ZN4ASDT8IOPAudio19OutputBufferMappingC2ERNS_13TimeInterfaceEPvjjjjRKN19RTKitAudioFramework17StreamDescriptionE
+ __ZN4ASDT8IOPAudio19OutputBufferMappingD0Ev
+ __ZN4ASDT8IOPAudio19OutputBufferMappingD1Ev
+ __ZN4ASDT8IOPAudio8StreamCM10UserClient11MapIOBufferEN19RTKitAudioFramework16StreamIdentifierE
+ __ZN4ASDT8IOPAudio8StreamCM10UserClient11MapIOBufferEN19RTKitAudioFramework16StreamIdentifierE.cold.1
+ __ZN4ASDT8IOPAudio8StreamCM10UserClient14CopyStreamInfoEv
+ __ZN4ASDT8IOPAudio8StreamCM10UserClient14CopyStreamInfoEv.cold.1
+ __ZN4ASDT8IOPAudio8StreamCM10UserClient14GetClockDomainEv
+ __ZN4ASDT8IOPAudio8StreamCM10UserClient14GetClockDomainEv.cold.1
+ __ZN4ASDT8IOPAudio8StreamCM10UserClient16ConvertTimestampEyRy
+ __ZN4ASDT8IOPAudio8StreamCM10UserClient16ConvertTimestampEyRy.cold.1
+ __ZN4ASDT8IOPAudio8StreamCM10UserClient16ConvertTimestampEyRy.cold.2
+ __ZN4ASDT8IOPAudio8StreamCM10UserClient17GetBooleanControlEN19RTKitAudioFramework8IOPAudio9Tightbeam17ControlIdentifierERb
+ __ZN4ASDT8IOPAudio8StreamCM10UserClient17GetBooleanControlEN19RTKitAudioFramework8IOPAudio9Tightbeam17ControlIdentifierERb.cold.1
+ __ZN4ASDT8IOPAudio8StreamCM10UserClient17GetBooleanControlEN19RTKitAudioFramework8IOPAudio9Tightbeam17ControlIdentifierERb.cold.2
+ __ZN4ASDT8IOPAudio8StreamCM10UserClient17SetBooleanControlEN19RTKitAudioFramework8IOPAudio9Tightbeam17ControlIdentifierEb
+ __ZN4ASDT8IOPAudio8StreamCM10UserClient17SetBooleanControlEN19RTKitAudioFramework8IOPAudio9Tightbeam17ControlIdentifierEb.cold.1
+ __ZN4ASDT8IOPAudio8StreamCM10UserClient23SelectStreamDescriptionEN19RTKitAudioFramework16StreamIdentifierEj
+ __ZN4ASDT8IOPAudio8StreamCM10UserClient23SelectStreamDescriptionEN19RTKitAudioFramework16StreamIdentifierEj.cold.1
+ __ZN4ASDT8IOPAudio8StreamCM10UserClient26MapTypeAndOptionsForStreamEN19RTKitAudioFramework16StreamIdentifierERjS5_
+ __ZN4ASDT8IOPAudio8StreamCM10UserClientD0Ev
+ __ZN4ASDT8IOPAudio8StreamCM10UserClientD1Ev
+ __ZN8ASDTTime8addTicksERKS_
+ __ZN8ASDTTime8subTicksERKS_
+ __ZN8ASDTTimeC1Ex12ASDTTimeKind
+ __ZN8ASDTTimeC1Ext12ASDTTimeKind
+ __ZNK19RTKitAudioFramework12RingBufferV213isBufferReadyEv
+ __ZNK19RTKitAudioFramework12RingBufferV214getAtomicIndexERNS0_11AtomicIndexE
+ __ZNK19RTKitAudioFramework12RingBufferV215advancePositionERji
+ __ZNK19RTKitAudioFramework12RingBufferV215getControlBlockERKNS0_11AtomicIndexERNS0_12ControlBlockE
+ __ZNK19RTKitAudioFramework12RingBufferV221positionToVirtAddressEy
+ __ZNK19RTKitAudioFramework12RingBufferV24peekEjjRNS_12ElementArrayINS_8IOBufferEEE
+ __ZNK19RTKitAudioFramework12RingBufferV24readEjRNS_8IOBufferE
+ __ZNK19RTKitAudioFramework12RingBufferV26assumeEym
+ __ZNK19RTKitAudioFramework12RingBufferV27releaseEym
+ __ZNK19RTKitAudioFramework13IMappedBuffer14assumeSubrangeEjm
+ __ZNK19RTKitAudioFramework13IMappedBuffer15releaseSubrangeEjm
+ __ZNK19RTKitAudioFramework15XnuMappedBuffer15_assumeSubrangeEjm
+ __ZNK19RTKitAudioFramework15XnuMappedBuffer16_releaseSubrangeEjm
+ __ZNK19RTKitAudioFramework15XnuMappedBuffer4peekEjRNS_8IOBufferE
+ __ZNK19RTKitAudioFramework15XnuMappedBuffer4readEjRNS_8IOBufferE
+ __ZNK19RTKitAudioFramework18RingBufferV2Reader16_validateSessionERNS_12RingBufferV212ControlBlockE
+ __ZNK19RTKitAudioFramework18RingBufferV2Reader21_validateReadPositionERNS_12RingBufferV212ControlBlockE
+ __ZNK19RTKitAudioFramework18RingBufferV2Reader22getCurrentControlBlockERNS_12RingBufferV212ControlBlockE
+ __ZNK19RTKitAudioFramework18RingBufferV2Reader4peekEjRNS_12ElementArrayINS_8IOBufferEEE
+ __ZNK19RTKitAudioFramework18RingBufferV2Reader5_peekERNS_12RingBufferV212ControlBlockEjRNS_12ElementArrayINS_8IOBufferEEE
+ __ZNK19RTKitAudioFramework20MappedSubrangeBuffer11getPhysAddrEv
+ __ZNK19RTKitAudioFramework20MappedSubrangeBuffer14assumeSubrangeEjm
+ __ZNK19RTKitAudioFramework20MappedSubrangeBuffer14getAlignedSizeEv
+ __ZNK19RTKitAudioFramework20MappedSubrangeBuffer15releaseSubrangeEjm
+ __ZNK19RTKitAudioFramework20MappedSubrangeBuffer4peekEjRNS_8IOBufferE
+ __ZNK19RTKitAudioFramework20MappedSubrangeBuffer4readEjRNS_8IOBufferE
+ __ZNK19RTKitAudioFramework20MappedSubrangeBuffer7isValidEv
+ __ZNK19RTKitAudioFramework23AudioPacketRingBufferV26assumeERKNS_9Interface12Audio3PacketE
+ __ZNK19RTKitAudioFramework23AudioPacketRingBufferV26assumeEym
+ __ZNK19RTKitAudioFramework6Buffer14assumeSubrangeEjm
+ __ZNK19RTKitAudioFramework6Buffer15releaseSubrangeEjm
+ __ZNK19RTKitAudioFramework6Buffer4peekEjRNS_8IOBufferE
+ __ZNK19RTKitAudioFramework6Buffer4readEjRNS_8IOBufferE
+ __ZNK19RTKitAudioFramework8IOPAudio13BufferMapping13getBufferSpecEv
+ __ZNK19RTKitAudioFramework8IOPAudio18InputBufferMapping20getStreamDescriptionEv
+ __ZNK19RTKitAudioFramework8IOPAudio19OutputBufferMapping20getStreamDescriptionEv
+ __ZNK4ASDT12IOUserClient12CopyPropertyIN10applesauce2CF8ArrayRefEEEbRKNS3_9StringRefERT_
+ __ZNK4ASDT8IOPAudio18InputBufferMapping20getStreamDescriptionEv
+ __ZNK4ASDT8IOPAudio19OutputBufferMapping20getStreamDescriptionEv
+ __ZNSt12length_errorC1B9fqe220100EPKc
+ __ZNSt3__111shared_lockINS_12shared_mutexEED2B9fqe220100Ev
+ __ZNSt3__111unique_lockINS_12shared_mutexEED2B9fqe220100Ev
+ __ZNSt3__112basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEE20__throw_length_errorB9fqe220100Ev
+ __ZNSt3__112basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEE22__init_internal_bufferB9fqe220100Em
+ __ZNSt3__120__throw_length_errorB9fqe220100EPKc
+ __ZTIN19RTKitAudioFramework8IOPAudio16XnuBufferMappingE
+ __ZTIN4ASDT8IOPAudio13BufferMappingE
+ __ZTIN4ASDT8IOPAudio18InputBufferMappingE
+ __ZTIN4ASDT8IOPAudio19OutputBufferMappingE
+ __ZTIN4ASDT8IOPAudio8StreamCM10UserClientE
+ __ZTSN19RTKitAudioFramework8IOPAudio16XnuBufferMappingE
+ __ZTSN4ASDT8IOPAudio13BufferMappingE
+ __ZTSN4ASDT8IOPAudio18InputBufferMappingE
+ __ZTSN4ASDT8IOPAudio19OutputBufferMappingE
+ __ZTSN4ASDT8IOPAudio8StreamCM10UserClientE
+ __ZTVN10__cxxabiv117__class_type_infoE
+ __ZTVN19RTKitAudioFramework12RingBufferV2E
+ __ZTVN19RTKitAudioFramework15XnuMappedBufferE
+ __ZTVN19RTKitAudioFramework17AudioOutputWriterE
+ __ZTVN19RTKitAudioFramework17AudioRingBufferV2E
+ __ZTVN19RTKitAudioFramework18RingBufferV2ReaderE
+ __ZTVN19RTKitAudioFramework18RingBufferV2WriterE
+ __ZTVN19RTKitAudioFramework20MappedSubrangeBufferE
+ __ZTVN19RTKitAudioFramework23AudioOutputRingBufferV2E
+ __ZTVN19RTKitAudioFramework23AudioPacketRingBufferV2E
+ __ZTVN19RTKitAudioFramework23AudioRingBufferV2WriterE
+ __ZTVN19RTKitAudioFramework29AudioPacketRingBufferV2ReaderE
+ __ZTVN19RTKitAudioFramework6BufferE
+ __ZTVN19RTKitAudioFramework8IOPAudio13BufferMappingE
+ __ZTVN19RTKitAudioFramework8IOPAudio16XnuBufferMappingE
+ __ZTVN19RTKitAudioFramework8IOPAudio18InputBufferMappingE
+ __ZTVN19RTKitAudioFramework8IOPAudio19OutputBufferMappingE
+ __ZTVN19RTKitAudioFramework8IOPAudio21XnuInputBufferMappingE
+ __ZTVN19RTKitAudioFramework8IOPAudio22XnuOutputBufferMappingE
+ __ZTVN19RTKitAudioFramework8IOPAudio23PacketRingBufferMappingE
+ __ZTVN4ASDT13TimeInterfaceE
+ __ZTVN4ASDT8IOPAudio13BufferMappingE
+ __ZTVN4ASDT8IOPAudio18InputBufferMappingE
+ __ZTVN4ASDT8IOPAudio19OutputBufferMappingE
+ __ZTVN4ASDT8IOPAudio8StreamCM10UserClientE
+ __ZZ14ASDTIOPLogTypeE9onceToken
+ ___46-[ASDTIOPAudioStreamCMStream readOrWriteBlock]_block_invoke
+ ___51-[ASDTIOPAudioStreamCMStream changePhysicalFormat:]_block_invoke
+ ___51-[ASDTIOPAudioStreamCMStream getZeroTimestampBlock]_block_invoke
+ ___57-[ASDTIOPAudioStreamCMDevice requestConfigurationChange:]_block_invoke
+ ___NSArray0__struct
+ ___block_descriptor_40_e182_i28?0Q8I16r^{AudioServerPlugInIOCycleInfo=QI{AudioTimeStamp=dQdQ{SMPTETime=ssIIIssss}II}{AudioTimeStamp=dQdQ{SMPTETime=ssIIIssss}II}{AudioTimeStamp=dQdQ{SMPTETime=ssIIIssss}II}dd}20l
+ ___block_descriptor_48_ea8_32bs40w_e5_v8?0ls32l8w40l8
+ ___block_descriptor_48_ea8_32s40w_e5_v8?0lw40l8s32l8
+ ___block_descriptor_56_ea8_32s_e190_i40?0I8r^{AudioServerPlugInIOCycleInfo=QI{AudioTimeStamp=dQdQ{SMPTETime=ssIIIssss}II}{AudioTimeStamp=dQdQ{SMPTETime=ssIIIssss}II}{AudioTimeStamp=dQdQ{SMPTETime=ssIIIssss}II}dd}12^v20^v28I36ls32l8
+ ___block_descriptor_56_ea8_32s_e20_i36?0^d8^Q16^Q24I32ls32l8
+ ___block_descriptor_97_e190_i40?0I8r^{AudioServerPlugInIOCycleInfo=QI{AudioTimeStamp=dQdQ{SMPTETime=ssIIIssss}II}{AudioTimeStamp=dQdQ{SMPTETime=ssIIIssss}II}{AudioTimeStamp=dQdQ{SMPTETime=ssIIIssss}II}dd}12^v20^v28I36l
+ ___cxa_pure_virtual
+ _abort
+ _bzero
+ _kASDTConfigDirectionOutput
+ _memcpy
+ _memset
+ _objc_alloc_init
+ _objc_claimAutoreleasedReturnValue
+ _objc_msgSend$_updateSafetyOffsets:
+ _objc_msgSend$_updateTimestampPeriod:
+ _objc_msgSend$addEntriesFromDictionary:
+ _objc_msgSend$addInputStream:
+ _objc_msgSend$addObject:
+ _objc_msgSend$addOutputStream:
+ _objc_msgSend$allStreams
+ _objc_msgSend$allValues
+ _objc_msgSend$array
+ _objc_msgSend$arrayWithCapacity:
+ _objc_msgSend$asdtArrayForKey:
+ _objc_msgSend$asdtDictionaryForKey:
+ _objc_msgSend$asdtName
+ _objc_msgSend$asdtNumberForKey:
+ _objc_msgSend$asdtStreamCMAvailableFormats
+ _objc_msgSend$asdtStreamCMBufferFrames
+ _objc_msgSend$asdtStreamCMCurrentFormat
+ _objc_msgSend$asdtStreamCMFormat
+ _objc_msgSend$asdtStreamCMIdentifier
+ _objc_msgSend$asdtStreamCMIdentifierStr
+ _objc_msgSend$asdtStreamCMInfoForStreamStr:
+ _objc_msgSend$asdtStreamCMLatency
+ _objc_msgSend$asdtStreamCMPacketCount
+ _objc_msgSend$asdtStreamCMSafetyOffset
+ _objc_msgSend$asdtStreamCMTerminalType
+ _objc_msgSend$audioStreamBasicDescription
+ _objc_msgSend$bufferFrames
+ _objc_msgSend$bufferMemory
+ _objc_msgSend$clientManagerUserClient
+ _objc_msgSend$clockDomain
+ _objc_msgSend$containsObject:
+ _objc_msgSend$createUserClientForIOObject:andIDValue:
+ _objc_msgSend$dictionaryWithCapacity:
+ _objc_msgSend$direction
+ _objc_msgSend$forConfig:iopConfig:withDevice:
+ _objc_msgSend$forUserClient:memoryType:options:
+ _objc_msgSend$getZeroTimestampBlock
+ _objc_msgSend$initWithConfig:iopConfig:withDevice:
+ _objc_msgSend$isEqual:
+ _objc_msgSend$latency
+ _objc_msgSend$mapMemoryForStream:
+ _objc_msgSend$mapPacketBuffer
+ _objc_msgSend$objectAtIndexedSubscript:
+ _objc_msgSend$orderedSetWithCapacity:
+ _objc_msgSend$packetCount
+ _objc_msgSend$physicalFormats
+ _objc_msgSend$requestConfigurationChange:
+ _objc_msgSend$safetyOffset
+ _objc_msgSend$sampleRate
+ _objc_msgSend$samplingRate
+ _objc_msgSend$samplingRates
+ _objc_msgSend$selectStreamDescriptionAtIndex:forStream:
+ _objc_msgSend$setBitsPerChannel:
+ _objc_msgSend$setBufferFrames:
+ _objc_msgSend$setBufferMemory:
+ _objc_msgSend$setBytesPerFrame:
+ _objc_msgSend$setBytesPerPacket:
+ _objc_msgSend$setChannelsPerFrame:
+ _objc_msgSend$setFormatFlags:
+ _objc_msgSend$setFormatID:
+ _objc_msgSend$setFramesPerPacket:
+ _objc_msgSend$setMaximumSampleRate:
+ _objc_msgSend$setMinimumSampleRate:
+ _objc_msgSend$setPacketCount:
+ _objc_msgSend$setSampleRate:
+ _objc_msgSend$setStreamCMService:
+ _objc_msgSend$setTimestampPeriod:
+ _objc_msgSend$setupPhysicalFormat:
+ _objc_msgSend$size
+ _objc_msgSend$streamCMDevice
+ _objc_msgSend$streamCMService
+ _objc_msgSend$streamCMUserClient
+ _objc_msgSend$streams
+ _objc_msgSend$timeInterface
+ _objc_msgSend$unsignedIntValue
+ _objc_msgSend$updateFromRegistry
+ _objc_msgSend$updateFromRegistry:
+ _objc_msgSend$voidRef
+ _objc_retain
+ _objc_retain_x2
+ _objc_retain_x25
+ _objc_retain_x28
+ _objc_retain_x3
+ _objc_retain_x8
+ _objc_setProperty_nonatomic_copy
- +[ASDTBootArgs getBool:]
- +[ASDTBootArgs getString:]
- +[ASDTBootArgs getUInt64:]
- +[ASDTBootArgs get]
- +[ASDTBootArgs initBootArgsFrom:]
- +[ASDTBootArgs initBootArgs]
- +[ASDTBootArgs initBootArgs].cold.1
- -[ASDTIOPAudioCMDevice initForIOObject:andIDValue:].cold.2
- _ASDTIOPLogType.onceToken
- _OBJC_CLASS_$_ASDTBootArgs
- _OBJC_CLASS_$_NSMutableData
- _OBJC_CLASS_$_NSObject
- _OBJC_METACLASS_$_ASDTBootArgs
- __OBJC_$_CATEGORY_INSTANCE_METHODS_NSDictionary_$_ASDTIOPAudioConfig
- __OBJC_$_CATEGORY_NSDictionary_$_ASDTIOPAudioConfig
- __OBJC_$_CLASS_METHODS_ASDTBootArgs
- __OBJC_CLASS_RO_$_ASDTBootArgs
- __OBJC_METACLASS_RO_$_ASDTBootArgs
- __ZNSt12length_errorC1B9nqe210106EPKc
- __ZNSt3__111shared_lockINS_12shared_mutexEED2B9nqe210106Ev
- __ZNSt3__111unique_lockINS_12shared_mutexEED2B9nqe210106Ev
- __ZNSt3__112basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEE20__throw_length_errorB9nqe210106Ev
- __ZNSt3__120__throw_length_errorB9nqe210106EPKc
- ___19+[ASDTBootArgs get]_block_invoke
- ___block_descriptor_40_e187_i28?0Q8I16r^{AudioServerPlugInIOCycleInfo=QI{AudioTimeStamp=dQdQ{SMPTETime=ssIIIssss}II}{AudioTimeStamp=dQdQ{SMPTETime=ssIIIssss}II}{AudioTimeStamp=dQdQ{SMPTETime=ssIIIssss}II}(?=dd)d}20l
- ___block_descriptor_40_e5_v8?0l
- ___block_descriptor_97_e195_i40?0I8r^{AudioServerPlugInIOCycleInfo=QI{AudioTimeStamp=dQdQ{SMPTETime=ssIIIssss}II}{AudioTimeStamp=dQdQ{SMPTETime=ssIIIssss}II}{AudioTimeStamp=dQdQ{SMPTETime=ssIIIssss}II}(?=dd)d}12^v20^v28I36l
- ___error
- _gASDTIOPLogType
- _gBootArgs
- _get.onceToken
- _objc_msgSend$componentsSeparatedByString:
- _objc_msgSend$copy
- _objc_msgSend$dataWithLength:
- _objc_msgSend$dictionary
- _objc_msgSend$get
- _objc_msgSend$getString:
- _objc_msgSend$getUInt64:
- _objc_msgSend$initBootArgs
- _objc_msgSend$initBootArgsFrom:
- _objc_msgSend$objectAtIndex:
- _objc_release_x9
- _objc_retainAutoreleasedReturnValue
- _objc_retain_x23
- _strerror
- _strtoull
- _sysctlbyname
CStrings:
+ "!(delta < 0)"
+ "!(delta >= (mRingBuffer.getSampleBuffer().getItemCapacity() - mReverseSafetyFrames))"
+ "!(inOutItemCount > cb.mItemCount)"
+ "!(numRead != inBufferFrameSize)"
+ "%@: Attempt to update from registry while running."
+ "%@: Current sampling rate is not in available formats."
+ "%@: Failed opening kernel IOService."
+ "%@: Failed to create stream for config: %@"
+ "%@: Failed to enable service."
+ "%@: Failed to select stream description %u on stream '%s'."
+ "%@: Failed to update stream %@ with config: %@"
+ "%@: Get boolean control '%s'"
+ "%@: No stream formats defined."
+ "%@: No streams defined."
+ "%@: Set boolean control '%s' to %hhu"
+ "%@: Stream %@ buffer frames (%u) does not match first stream's: %u"
+ "%@:%@: Failed buffer mapping prepare: %x"
+ "%@:%@: Failed ready check: %x"
+ "%@:%@: Failed to %s: %x"
+ "%@:%@: Failed to convertTimestamp."
+ "%@:%@: Failed to create buffer mapping of packet buffer memory."
+ "%@:%@: Failed to get packet buffer memory!"
+ "%@:%@: Failed to getZeroTimestamp: %x"
+ "%@:%@: Failed to select a physical format."
+ "%@:%@: Not running."
+ "%s: CopyStreamInfo: Property missing"
+ "%s: Failed ConvertTimestamp"
+ "%s: Failed ConvertTimestamp: Bad outCount."
+ "%s: Failed GetBooleanControl"
+ "%s: Failed GetBooleanControl: Bad valueCount."
+ "%s: Failed SelectStreamDescription"
+ "%s: Failed SetBooleanControl"
+ "%s: GetClockDomain: Property missing"
+ "-[ASDTIOPAudioStreamCMService clockDomain]"
+ "-[ASDTIOPAudioStreamCMService getBooleanControl:withValue:]"
+ "-[ASDTIOPAudioStreamCMService mapMemoryForStream:]"
+ "-[ASDTIOPAudioStreamCMService selectStreamDescriptionAtIndex:forStream:]"
+ "-[ASDTIOPAudioStreamCMService setBooleanControl:withValue:]"
+ "-[ASDTIOPAudioStreamCMService streams]"
+ "2"
+ "ASDTIOPAudioStreamCMService.mm"
+ "Base"
+ "Buffer size is too small: %u < %zu"
+ "Buffer.cpp"
+ "Failed init %sput BufferMapping of size %u"
+ "IOBuffer.cpp"
+ "IOPAudioStreamCMDevice"
+ "Stream array contains invalid or missing identifier: %@"
+ "[AUD] [AUD]:(%s, %d)"
+ "[AUD] cond \"%s\" fail, %s() ln %d, stat %#x"
+ "[AUD] exp \"%s\" fail, %s(), ln %d, stat %#x"
+ "[AUD] ptr \"%s\" is null, cant cont, %s(), ln %d, stat %#x"
+ "_doTSTracking"
+ "_map"
+ "_read"
+ "_setStreamDescription(getStreamDescription())"
+ "_setStreamDescription(inStreamDescription)"
+ "available stream descriptions"
+ "buffer frames"
+ "com.apple.audio.RTKAFwk"
+ "getTimestamp"
+ "getTimestamp(timestamp)"
+ "getZeroTimestamp"
+ "header->magic == Header::kMagic"
+ "i28@?0Q8I16r^{AudioServerPlugInIOCycleInfo=QI{AudioTimeStamp=dQdQ{SMPTETime=ssIIIssss}II}{AudioTimeStamp=dQdQ{SMPTETime=ssIIIssss}II}{AudioTimeStamp=dQdQ{SMPTETime=ssIIIssss}II}dd}20"
+ "i40@?0I8r^{AudioServerPlugInIOCycleInfo=QI{AudioTimeStamp=dQdQ{SMPTETime=ssIIIssss}II}{AudioTimeStamp=dQdQ{SMPTETime=ssIIIssss}II}{AudioTimeStamp=dQdQ{SMPTETime=ssIIIssss}II}dd}12^v20^v28I36"
+ "in"
+ "init"
+ "iob"
+ "isBufferReady()"
+ "mConfig.mappedBuffer.mapByName(mConfig.identifier, mappingSize)"
+ "mConfig.mappedBuffer.mapLocal(reinterpret_cast<void*>(mConfig.address), mappingSize)"
+ "mConfig.mappedBuffer.mapRemote(static_cast<physAddr_t>(mConfig.address), mappingSize)"
+ "mMapping.getReader().init()"
+ "mMapping.getReader().read(inSampleTime, buffer, numRead)"
+ "mMapping.getReader().reset()"
+ "mMapping.getWriter().getDMATimestamp(dmaTimestamp)"
+ "mMapping.getWriter().init()"
+ "mMapping.getWriter().reset()"
+ "mMapping.getWriter().write(inSampleTime, buffer)"
+ "mMapping.map()"
+ "mOffsetWithinParent == kInvalidOffset || mOffsetWithinParent == inOffset"
+ "mPacketReader.init()"
+ "mPacketReader.reset(inBackOff)"
+ "mParentBuffer._assumeSubrange(alignedStartOffset, alignedSize)"
+ "mParentBuffer._releaseSubrange(alignedStartOffset, alignedSize)"
+ "mParentBuffer.assumeSubrange(mOffsetWithinParent + inOffset, outDest.byteSize())"
+ "mRingBuffer.assume(inoutPacket)"
+ "mRingBuffer.getSampleBuffer().getAtomicIndex(idx)"
+ "mRingBuffer.getSampleBuffer().getControlBlock(idx, cb)"
+ "mSampleReader.init()"
+ "mSampleReader.reset()"
+ "mTimestampBuffer.read(inPosition, iob)"
+ "nToBePeeked * mItemSize == mData.peek(readPosition * mItemSize, iob)"
+ "nToBeRead * mItemSize == mData.read(readPosition * mItemSize, iob)"
+ "nToBeWritten * mItemSize == mData.write(iob, cb.mWritePosition * mItemSize)"
+ "nextOutPacketVecIdx < inOutPacketVecSize"
+ "numRead: %zu, inBufferFrameSize: %u, inSampleTime: %llu, %llu"
+ "out"
+ "outValue"
+ "packet count"
+ "packetCountValid"
+ "peek"
+ "prepare"
+ "read"
+ "readAllCommon"
+ "readPacketResult"
+ "readTimestamp"
+ "readyCheck"
+ "reset"
+ "safety offset in frames"
+ "selected stream description"
+ "setStreamDescription"
+ "setSubRange"
+ "setupDataRingBuffer"
+ "setupSubrangeBuffers"
+ "streamDescription.isValid()"
+ "streams"
+ "terminal type"
+ "updateAvailableData"
+ "updateAvailableData()"
+ "write"
+ "writeAtomicIndex(index)"
+ "writeControlBlock(index, cb)"
- ""
- " "
- "#16@0:8"
- "%@: Failed to create ClientManager user client"
- ".cxx_construct"
- ".cxx_destruct"
- "="
- "@\"ASDTIOPAudioCMDevice\""
- "@\"ASDTIOPAudioIOBufferDevice\""
- "@\"ASDTIOPAudioIsolatedIOBufferDevice\""
- "@\"ASDTIOPAudioLPMicStream\""
- "@\"ASDTIOPAudioVTDevice\""
- "@\"ASDTNonSecurePathEnableProperty\""
- "@\"NSArray\"24@0:8@\"NSDictionary\"16"
- "@\"NSString\"16@0:8"
- "@16@0:8"
- "@24@0:8:16"
- "@24@0:8@\"NSDictionary\"16"
- "@24@0:8@16"
- "@28@0:8I16@20"
- "@32@0:8:16@24"
- "@32@0:8@16@24"
- "@32@0:8@16I24I28"
- "@40@0:8:16@24@32"
- "@40@0:8@16@24@32"
- "@?16@0:8"
- "ASDTBootArgs"
- "ASDTConcreteCustomProperty"
- "ASDTExclavesStatusTrackerHostProtocol"
- "ASDTIOPAudioCMDevice"
- "ASDTIOPAudioCMPowerStateProperty"
- "ASDTIOPAudioCMServiceManager"
- "ASDTIOPAudioConfig"
- "ASDTIOPAudioIOBufferDevice"
- "ASDTIOPAudioIOBufferServiceManager"
- "ASDTIOPAudioIsolatedIOBufferDevice"
- "ASDTIOPAudioIsolatedIOBufferServiceManager"
- "ASDTIOPAudioLPMicDeviceFactory"
- "ASDTIOPAudioLPMicServiceManager"
- "ASDTIOPAudioLPMicStream"
- "ASDTIOPAudioVTDevice"
- "ASDTIOPAudioVTProperty"
- "ASDTIOPAudioVTServiceManager"
- "ASDTIOPAudioVTUInt32Property"
- "ASDTIOServiceDependency"
- "B16@0:8"
- "B20@0:8I16"
- "B24@0:8#16"
- "B24@0:8:16"
- "B24@0:8@\"Protocol\"16"
- "B24@0:8@16"
- "B24@0:8@?16"
- "B24@0:8I16I20"
- "B24@0:8Q16"
- "B24@0:8^B16"
- "B24@0:8^I16"
- "B24@0:8^{AudioStreamBasicDescription=dIIIIIIII}16"
- "B24@0:8^{StreamDescription=dIIIIIIIIII}16"
- "B28@0:8I16@20"
- "B28@0:8Q16I24"
- "B28@0:8r^{AudioStreamBasicDescription=dIIIIIIII}16I24"
- "Failed to load boot args: [%d] %s"
- "I16@0:8"
- "NSObject"
- "Q"
- "Q16@0:8"
- "Q24@0:8@16"
- "T#,R"
- "T@\"ASDTIOPAudioCMDevice\",&,N,V_clientManager"
- "T@\"ASDTIOPAudioIOBufferDevice\",&,N,V_ioBufferDevice"
- "T@\"ASDTIOPAudioIsolatedIOBufferDevice\",&,N,V_isolatedIOBufferDevice"
- "T@\"ASDTIOPAudioLPMicDevice\",R,N"
- "T@\"ASDTIOPAudioLPMicStream\",W,N,V_inputStream"
- "T@\"ASDTIOPAudioVTDevice\",W,N,V_vtDevice"
- "T@\"ASDTNonSecurePathEnableProperty\",&,N,V_nonSecureInputEnableProperty"
- "T@\"NSDictionary\",R,N"
- "T@\"NSString\",?,R,C"
- "T@\"NSString\",R,C"
- "TB,R,N"
- "TI,N,V_enableDirection"
- "TI,N,V_powerStateDirection"
- "TI,N,V_powerStateDisabled"
- "TI,N,V_powerStateEnabled"
- "TI,R,N"
- "TQ,R"
- "T^*,R,N"
- "T^v,R,N"
- "UTF8String"
- "Vv16@0:8"
- "^*16@0:8"
- "^v16@0:8"
- "^{EngineStatus=QQQQ}16@0:8"
- "^{_NSZone=}16@0:8"
- "_clientManager"
- "_enableDirection"
- "_exclavesStatusTracker"
- "_exclavesStatusTrackerOnce"
- "_initialSampleTime"
- "_inputStream"
- "_ioBufferDevice"
- "_ioBufferMap"
- "_ioBufferSize"
- "_isolatedIOBufferDevice"
- "_lpMicEngineStatus"
- "_memoryMap"
- "_nonSecureInputEnableProperty"
- "_openCount"
- "_openLock"
- "_powerStateDirection"
- "_powerStateDisabled"
- "_powerStateEnabled"
- "_vtDevice"
- "addCustomProperties:"
- "addCustomProperty:"
- "allocExclavesAudioBuffer:"
- "arrayWithObjects:count:"
- "asdtAddMissingEntriesFromDictionary:"
- "asdtAddNonSecurePathEnable"
- "asdtDeviceUID"
- "asdtEquivalentNativeFloatPacked"
- "asdtExclavesBufferName"
- "asdtFourCCForKey:withDefault:"
- "asdtIOPAudioCMEnablePropertyDirection"
- "asdtIOPAudioCMPowerStatePropertyDirection"
- "asdtIOPAudioCMPowerStatePropertyDisabled"
- "asdtIOPAudioCMPowerStatePropertyEnabled"
- "asdtIOThreadChangeEvent"
- "asdtIOThreadChangeIsolatedUseCase"
- "asdtIOThreadUseCaseIsFirstOrWasLast"
- "asdtServiceID"
- "autorelease"
- "availablePastDataFrames"
- "bytes"
- "bytesPerFrame"
- "checkPropertyValue:"
- "class"
- "clearBuffer"
- "clientManager"
- "clientType"
- "close"
- "componentsSeparatedByString:"
- "configDictForService:"
- "conformsToProtocol:"
- "copy"
- "count"
- "countByEnumeratingWithState:objects:count:"
- "createForInput"
- "dataWithBytes:length:"
- "dataWithLength:"
- "dealloc"
- "debugDescription"
- "dependencyForID:andConfiguration:"
- "description"
- "device"
- "deviceName"
- "deviceUID"
- "dictionary"
- "dictionaryWithDictionary:"
- "dictionaryWithObjects:forKeys:count:"
- "disableInDirection:"
- "enableDirection"
- "enableInDirection:"
- "enableListeningOnGesturePropertyForService:"
- "enableListeningPropertyForService:"
- "enabled"
- "eventInfo"
- "exclavesAudioBuffer"
- "exclavesBufferName"
- "exclavesReadInput"
- "exclavesSensorName"
- "exclavesStatusTracker"
- "firstObject"
- "forIOObject:andIDValue:"
- "freeExclavesAudioBuffer"
- "get"
- "getBool:"
- "getBytes:length:"
- "getChannelMask:"
- "getConfigurationInfo"
- "getCurrentPowerState:"
- "getDebugEnabled:"
- "getEnableState:"
- "getEnabledChannelMask:"
- "getIsEnabled:"
- "getModelCRC:"
- "getNodeProperty:withValue:"
- "getStreamDescription:"
- "getString:"
- "getUInt64:"
- "getZeroTimestampBlock"
- "hash"
- "i20@0:8i16"
- "i24@0:8@16"
- "i24@0:8Q16"
- "i28@0:8Q16I24"
- "i28@?0Q8I16r^{AudioServerPlugInIOCycleInfo=QI{AudioTimeStamp=dQdQ{SMPTETime=ssIIIssss}II}{AudioTimeStamp=dQdQ{SMPTETime=ssIIIssss}II}{AudioTimeStamp=dQdQ{SMPTETime=ssIIIssss}II}(?=dd)d}20"
- "i32@0:8@16Q24"
- "i36@0:8@16I24Q28"
- "i40@?0I8r^{AudioServerPlugInIOCycleInfo=QI{AudioTimeStamp=dQdQ{SMPTETime=ssIIIssss}II}{AudioTimeStamp=dQdQ{SMPTETime=ssIIIssss}II}{AudioTimeStamp=dQdQ{SMPTETime=ssIIIssss}II}(?=dd)d}12^v20^v28I36"
- "idValue"
- "initBootArgs"
- "initBootArgsFrom:"
- "initForIOObject:andIDValue:"
- "initWithAudioStreamBasicDescription:"
- "initWithConfig:"
- "initWithConfig:propertyDataType:qualifierDataType:"
- "initWithConfig:withDevice:"
- "initWithConfig:withDeviceManager:andPlugin:"
- "inputSafetyOffset"
- "inputStream"
- "inputStreams"
- "ioBufferDevice"
- "ioBufferFramesSizeMax"
- "ioBufferFramesUnexpectedSizeCount"
- "ioBufferRef"
- "ioBufferSize"
- "ioBufferSizeFrames"
- "ioObject"
- "ioServiceClassName"
- "ioServiceDependenciesForConfig:"
- "ioServiceIDProperty"
- "ioThreadStateChange:"
- "isConfigured"
- "isEqual:"
- "isEqualToString:"
- "isKindOfClass:"
- "isMemberOfClass:"
- "isProxy"
- "isRunning"
- "isolatedIOBufferDevice"
- "isolatedUseCaseID"
- "kern.bootargs"
- "length"
- "lpMicDevice"
- "lpMicEngineStatus"
- "makePowerRequestForState:andDirection:"
- "mapIOBuffer"
- "matchedIOServiceForID:"
- "maximumPastDataFrames"
- "modelName"
- "mutableBytes"
- "mutableCopy"
- "name"
- "nonSecureInputEnableProperty"
- "nonSecureInputEnabled"
- "numberWithDouble:"
- "numberWithUnsignedInt:"
- "objectAtIndex:"
- "objectForKey:"
- "open"
- "owner"
- "parent"
- "performPowerStateIdle:"
- "performPowerStatePrepare:"
- "performPowerStatePrewarm:"
- "performSelector:"
- "performSelector:withObject:"
- "performSelector:withObject:withObject:"
- "phraseDetectEvent"
- "physicalFormat"
- "pmIdleStream:"
- "pmPrepareStream:"
- "pmPrewarmStream:"
- "powerStateDirection"
- "powerStateDisabled"
- "powerStateEnabled"
- "propertyValueSize"
- "q"
- "ramper"
- "readIsolatedInputBlock"
- "release"
- "releaseIOBuffer"
- "respondsToSelector:"
- "retain"
- "retainCount"
- "retrievePropertyValue"
- "retrieveUInt32Value:"
- "selector"
- "self"
- "serviceForIOObject:andIDValue:"
- "setCacheMode:"
- "setClientManager:"
- "setClockDomain:"
- "setConfigurationInfo:"
- "setDebugEnabled:"
- "setDeviceName:"
- "setEnableDirection:"
- "setEnabled:"
- "setEnabledChannelMask:"
- "setInputStream:"
- "setIoBufferDevice:"
- "setIsolatedIOBufferDevice:"
- "setIsolatedUseCaseID:"
- "setLatency:"
- "setLength:"
- "setModelName:"
- "setNodeProperty:withValue:"
- "setNonSecureInputEnableProperty:"
- "setObject:forKey:"
- "setPhraseDetectEventBlock:"
- "setPhysicalFormat:"
- "setPhysicalFormats:"
- "setPowerStateDirection:"
- "setPowerStateDisabled:"
- "setPowerStateEnabled:"
- "setPropertyValueSize:"
- "setPropertyValueWithResult:"
- "setSafetyOffset:"
- "setSamplingRate:"
- "setSamplingRates:"
- "setStreamDescription:withBufferFrameSize:"
- "setTransportType:"
- "setVtDevice:"
- "setupClientIO:withBufferFrameSize:"
- "setupCustomProperties:"
- "setupExclavesStatusTracker"
- "setupIO"
- "setupIsolatedIOForStream:frameSize:useCase:"
- "setupIsolatedIOForUseCase:withFrameSize:"
- "setupPhysicalFormats:"
- "setupSamplingRates:"
- "startStream"
- "stopStream"
- "storePropertyValue:"
- "storeUInt32Value:"
- "streamName"
- "stringWithUTF8String:"
- "subclassInitWithConfig:"
- "superclass"
- "teardownClientIO:"
- "teardownIO"
- "teardownIsolatedIOForStream:useCase:"
- "teardownIsolatedIOForUseCase:"
- "timestampPeriod"
- "transportType"
- "updateFromStreamDescription"
- "updateFromStreamDescription:"
- "v16@0:8"
- "v20@0:8I16"
- "v24@0:8@16"
- "vtDevice"
- "zone"
- "{IOMemoryMap=\"_vptr$IOMemoryMap\"^^?\"mConnection\"{IOConnect=\"_vptr$IOConnect\"^^?\"mObject\"{shared_ptr<ASDT::IOConnect::Object>=\"__ptr_\"^{Object}\"__cntrl_\"^{__shared_weak_count}}\"mMutex\"{mutex=\"__m_\"{_opaque_pthread_mutex_t=\"__sig\"q\"__opaque\"[56c]}}\"mIsOpen\"B}\"mAddress\"^v\"mSize\"I\"mType\"I}"
- "{mutex=\"__m_\"{_opaque_pthread_mutex_t=\"__sig\"q\"__opaque\"[56c]}}"
- "{unique_ptr<ASDT::Exclaves::StatusTracker, std::default_delete<ASDT::Exclaves::StatusTracker>>=\"\"{?=\"__ptr_\"^{StatusTracker}}}"
- "{unique_ptr<ASDT::IOPAudio::ClientManager::UserClient, std::default_delete<ASDT::IOPAudio::ClientManager::UserClient>>=\"\"{?=\"__ptr_\"^{UserClient}}}"
- "{unique_ptr<ASDT::IOPAudio::IOBuffer::UserClient, std::default_delete<ASDT::IOPAudio::IOBuffer::UserClient>>=\"\"{?=\"__ptr_\"^{UserClient}}}"
- "{unique_ptr<ASDT::IOPAudio::IsolatedIOBuffer::UserClient, std::default_delete<ASDT::IOPAudio::IsolatedIOBuffer::UserClient>>=\"\"{?=\"__ptr_\"^{UserClient}}}"
- "{unique_ptr<ASDT::IOPAudio::LPMic::UserClient, std::default_delete<ASDT::IOPAudio::LPMic::UserClient>>=\"\"{?=\"__ptr_\"^{UserClient}}}"
- "{unique_ptr<ASDT::IOPAudio::VoiceTrigger::UserClient, std::default_delete<ASDT::IOPAudio::VoiceTrigger::UserClient>>=\"\"{?=\"__ptr_\"^{UserClient}}}"

```
