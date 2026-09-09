## com.apple.driver.AudioDMAFamily

> `com.apple.driver.AudioDMAFamily`

```diff

   __TEXT.__cstring: 0xe6b
   __TEXT.__os_log: 0x428
   __TEXT.__const: 0x20
-  __TEXT_EXEC.__text: 0x58e8
+  __TEXT_EXEC.__text: 0x59ac
   __TEXT_EXEC.__auth_stubs: 0x200
   __DATA.__data: 0xc8
   __DATA.__common: 0x60
Functions:
~ sub_fffffe0009acfe30 -> sub_fffffe0009b5f890 : 72 -> 76
~ sub_fffffe0009acfe80 -> sub_fffffe0009b5f8e4 : 52 -> 56
~ sub_fffffe0009acfecc -> sub_fffffe0009b5f934 : 72 -> 76
~ __ZN17AudioDMAEvolution11ADMAChannel21InternalConfiguration3setERKNS0_18InputConfigurationE : 1880 -> 1884
~ __ZN17AudioDMAEvolution11ADMAChannel21InternalConfiguration18updateStreamConfigEjhh : 1204 -> 1208
~ sub_fffffe0009ad0bfc -> sub_fffffe0009b60670 : 148 -> 152
~ sub_fffffe0009ad0c90 -> sub_fffffe0009b60708 : 120 -> 124
~ sub_fffffe0009ad0d10 -> sub_fffffe0009b6078c : 80 -> 84
~ sub_fffffe0009ad0d70 -> sub_fffffe0009b607f0 : 72 -> 76
~ sub_fffffe0009ad0dc0 -> sub_fffffe0009b60844 : 52 -> 56
~ sub_fffffe0009ad0df4 -> sub_fffffe0009b6087c : 52 -> 56
~ sub_fffffe0009ad0e38 -> sub_fffffe0009b608c4 : 68 -> 72
~ sub_fffffe0009ad0ea4 -> sub_fffffe0009b60934 : 72 -> 76
~ sub_fffffe0009ad0eec -> sub_fffffe0009b60980 : 104 -> 108
~ sub_fffffe0009ad0f68 -> sub_fffffe0009b60a00 : 88 -> 92
~ sub_fffffe0009ad0fc0 -> sub_fffffe0009b60a5c : 88 -> 92
~ __ZN17AudioDMAEvolution13parseBootArgsEPKcPNS_24ADMAChannelInterfaceImplE : 208 -> 212
~ __ZN17AudioDMAEvolution20ADMAChannelInterface17withRegistryEntryEP15IORegistryEntryP9IOService : 168 -> 172
~ __ZN17AudioDMAEvolution22fetchIndexAndDirectionEP15IORegistryEntryPNS_24ADMAChannelInterfaceImplEb : 1700 -> 1704
~ sub_fffffe0009ad1834 -> sub_fffffe0009b612e0 : 384 -> 388
~ __ZN17AudioDMAEvolution20ADMAChannelInterface5startEP9IOService : 3516 -> 3520
~ sub_fffffe0009ad2770 -> sub_fffffe0009b62224 : 96 -> 100
~ sub_fffffe0009ad27e0 -> sub_fffffe0009b62298 : 136 -> 140
~ sub_fffffe0009ad2868 -> sub_fffffe0009b62324 : 200 -> 204
~ sub_fffffe0009ad2930 -> sub_fffffe0009b623f0 : 136 -> 140
~ ____ZN17AudioDMAEvolution20ADMAChannelInterface10deactivateEv_block_invoke : 552 -> 556
~ sub_fffffe0009ad2be0 -> sub_fffffe0009b626a8 : 140 -> 144
~ ____ZN17AudioDMAEvolution20ADMAChannelInterface25setAudioStreamDescriptionERNS_20ChannelConfiguration6StreamE_block_invoke : 1028 -> 1032
~ sub_fffffe0009ad3070 -> sub_fffffe0009b62b40 : 140 -> 144
~ sub_fffffe0009ad30fc -> sub_fffffe0009b62bd0 : 476 -> 480
~ __ZNK17AudioDMAEvolution20ADMAChannelInterface28translateStreamConfigurationERKNS_20ChannelConfiguration6StreamEPS1_ : 924 -> 928
~ sub_fffffe0009ad3684 -> sub_fffffe0009b63160 : 140 -> 144
~ ____ZNK17AudioDMAEvolution20ADMAChannelInterface14getPathLatencyERj_block_invoke : 624 -> 628
~ sub_fffffe0009ad3980 -> sub_fffffe0009b63464 : 144 -> 148
~ ____ZN17AudioDMAEvolution20ADMAChannelInterface24transferMemoryDescriptorEP18IOMemoryDescriptorjjU13block_pointerFvRKNS0_25CompletionCallbackContextEE_block_invoke : 1720 -> 1724
~ sub_fffffe0009ad40ec -> sub_fffffe0009b63bd8 : 144 -> 148
~ ____ZN17AudioDMAEvolution20ADMAChannelInterface24transferMemoryDescriptorEP18IOMemoryDescriptorjU13block_pointerFvRKNS0_25CompletionCallbackContextEE_block_invoke : 1232 -> 1236
~ sub_fffffe0009ad464c -> sub_fffffe0009b64140 : 144 -> 148
~ ____ZN17AudioDMAEvolution20ADMAChannelInterface24transferMemoryDescriptorEP18IOMemoryDescriptorbU13block_pointerFvRKNS0_25CompletionCallbackContextEE_block_invoke : 1124 -> 1128
~ sub_fffffe0009ad4b40 -> sub_fffffe0009b6463c : 144 -> 148
~ ____ZN17AudioDMAEvolution20ADMAChannelInterface24transferMemoryDescriptorEP18IOMemoryDescriptorU13block_pointerFvRKNS0_25CompletionCallbackContextEEj_block_invoke : 1168 -> 1172
~ sub_fffffe0009ad5060 -> sub_fffffe0009b64b64 : 136 -> 140
~ ____ZN17AudioDMAEvolution20ADMAChannelInterface14abortTransfersEv_block_invoke : 576 -> 580
~ sub_fffffe0009ad5340 -> sub_fffffe0009b64e4c : 80 -> 84
~ __ZN17AudioDMAEvolution22fetchIndexAndDirectionEP15IORegistryEntryPNS_24ADMAChannelInterfaceImplEb : 456 -> 460
~ __ZN9os_detail21panic_trapping_policy4trapEPKc : 48 -> 52
~ __ZN17AudioDMAEvolution13parseBootArgsEPKcPNS_24ADMAChannelInterfaceImplE.cold.1 : 24 -> 28
~ __ZN17AudioDMAEvolution13parseBootArgsEPKcPNS_24ADMAChannelInterfaceImplE.cold.2 : 24 -> 28
~ __ZN17AudioDMAEvolution20ADMAChannelInterface21initWithRegistryEntryEP15IORegistryEntryP9IOService.cold.1 : 188 -> 192
```
