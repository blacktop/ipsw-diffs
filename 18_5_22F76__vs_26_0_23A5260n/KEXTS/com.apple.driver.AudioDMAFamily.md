## com.apple.driver.AudioDMAFamily

> `com.apple.driver.AudioDMAFamily`

```diff

-450.4.0.0.0
+500.80.0.0.0
   __TEXT.__const: 0x30
-  __TEXT.__cstring: 0xeb2
+  __TEXT.__cstring: 0xee4
   __TEXT.__os_log: 0x428
-  __TEXT_EXEC.__text: 0x5bbc
+  __TEXT_EXEC.__text: 0x5d94
   __TEXT_EXEC.__auth_stubs: 0x0
   __DATA.__data: 0xc8
   __DATA.__common: 0x60
   __DATA_CONST.__auth_got: 0xf8
-  __DATA_CONST.__got: 0x40
+  __DATA_CONST.__got: 0x48
   __DATA_CONST.__mod_init_func: 0x10
   __DATA_CONST.__mod_term_func: 0x10
   __DATA_CONST.__const: 0xe40
   __DATA_CONST.__kalloc_type: 0x80
   __DATA_CONST.__kalloc_var: 0xa0
-  UUID: B66DCA42-D59C-3A92-A291-C2FFA0FD4585
+  UUID: A009673C-F3DA-35F6-ACA8-120060983450
   Functions: 78
   Symbols:   0
-  CStrings:  123
+  CStrings:  125
 
Functions:
~ __ZN17AudioDMAEvolution11ADMAChannel21InternalConfiguration3setERKNS0_18InputConfigurationE : 1880 -> 1884
~ sub_fffffff009cd14e4 -> sub_fffffff00a0165e8 : 88 -> 112
~ __ZN17AudioDMAEvolution11ADMAChannel21InternalConfiguration18updateStreamConfigEjhh : 1180 -> 1208
~ sub_fffffff009cd1aa0 -> sub_fffffff00a016bd8 : 116 -> 120
~ __ZN17AudioDMAEvolution22fetchIndexAndDirectionEP15IORegistryEntryPNS_24ADMAChannelInterfaceImplE -> __ZN17AudioDMAEvolution22fetchIndexAndDirectionEP15IORegistryEntryPNS_24ADMAChannelInterfaceImplEb : 348 -> 536
~ __ZN17AudioDMAEvolution20ADMAChannelInterface21initWithRegistryEntryEP15IORegistryEntryP9IOService : 2012 -> 2020
~ __ZN17AudioDMAEvolution20ADMAChannelInterface5startEP9IOService : 3692 -> 3920
~ ____ZN17AudioDMAEvolution20ADMAChannelInterface25setAudioStreamDescriptionERNS_20ChannelConfiguration6StreamE_block_invoke : 1068 -> 1064
~ sub_fffffff009cd4138 -> sub_fffffff00a019418 : 472 -> 476
~ ____ZNK17AudioDMAEvolution20ADMAChannelInterface14getPathLatencyEv_block_invoke : 924 -> 920
~ ____ZN17AudioDMAEvolution20ADMAChannelInterface24transferMemoryDescriptorEP18IOMemoryDescriptorjjU13block_pointerFvRKNS0_25CompletionCallbackContextEE_block_invoke : 1832 -> 1828
~ ____ZN17AudioDMAEvolution20ADMAChannelInterface24transferMemoryDescriptorEP18IOMemoryDescriptorjU13block_pointerFvRKNS0_25CompletionCallbackContextEE_block_invoke : 1384 -> 1380
~ ____ZN17AudioDMAEvolution20ADMAChannelInterface24transferMemoryDescriptorEP18IOMemoryDescriptorbU13block_pointerFvRKNS0_25CompletionCallbackContextEE_block_invoke : 1232 -> 1236
~ ____ZN17AudioDMAEvolution20ADMAChannelInterface24transferMemoryDescriptorEP18IOMemoryDescriptorU13block_pointerFvRKNS0_25CompletionCallbackContextEEj_block_invoke : 1332 -> 1328
CStrings:
+ "20:39:14"
+ "::strlen(channelIndexSubstr) < ::strlen(nodeDesignator)"
+ "May 30 2025"
+ "fetchIndexAndDirection(this, pimpl, true)"
+ "initial-trigger-us"
+ "max-fifo-depth-bytes"
+ "max-fifo-depth-us"
- "20:46:35"
- "::strlen(channelIndexSubstr) < ::strlen(nodeName)"
- "Apr 22 2025"
- "fetchIndexAndDirection(this, pimpl)"
- "max-fifo-depth-bits"

```
