## com.apple.DriverKit-AppleEthernetMLX5

> `/System/Library/DriverExtensions/com.apple.DriverKit-AppleEthernetMLX5.dext/com.apple.DriverKit-AppleEthernetMLX5`

### Sections with Same Size but Changed Content

- `__TEXT.__unwind_info`
- `__DATA_CONST.__const`
- `__DATA.__data`

```diff

 171.0.0.0.0
-  __TEXT.__text: 0x193e0
+  __TEXT.__text: 0x19420
   __TEXT.__auth_stubs: 0x660
   __TEXT.__cstring: 0x3ff3
   __TEXT.__const: 0x2268
Functions:
~ __ZN27DriverKit_AppleEthernetMLX519QueueInterrupt_ImplEP8OSActionyy : 108 -> 112
~ __ZN33DriverKit_AppleEthernetMLX5_IVars16allocDBFromPgDirER24AppleEthernetMLX5DBPgDirRN4mlx52DBE : 76 -> 84
~ __ZN33DriverKit_AppleEthernetMLX5_IVars7allocDBERN4mlx52DBE : 224 -> 240
~ __ZN39DriverKit_AppleEthernetMLX5_NetIf_IVars16dequeueTxPacketsEPN4mlx55EthSQE : 1012 -> 1016
~ __ZN39DriverKit_AppleEthernetMLX5_NetIf_IVars7drainSQERN4mlx55EthSQE : 524 -> 528
~ __ZN39DriverKit_AppleEthernetMLX5_NetIf_IVars23vportContextUpdateVlansEv : 784 -> 776
~ __ZN39DriverKit_AppleEthernetMLX5_NetIf_IVars14addVlanRuleSubEN4mlx514vlan_rule_typeEtPhS2_ : 320 -> 324
~ __ZNK19AppleEthernetMLX5EQ15queue_interruptEj : 1184 -> 1164
~ __ZN33DriverKit_AppleEthernetMLX5_IVars17setNicVPortMcListEiPyi : 332 -> 336
~ __ZN33DriverKit_AppleEthernetMLX5_IVars20queryNicVPortMacListEtN4mlx59list_typeEPA6_hPi : 332 -> 336
~ __ZN33DriverKit_AppleEthernetMLX5_IVars21modifyNicVPortMacListEN4mlx59list_typeEPA6_hi : 336 -> 340
~ __ZN39DriverKit_AppleEthernetMLX5_NetIf_IVars12openChannelsEv : 176 -> 180
~ __ZN39DriverKit_AppleEthernetMLX5_NetIf_IVars13closeChannelsEv : 208 -> 216
~ __ZN39DriverKit_AppleEthernetMLX5_NetIf_IVars11activateRQTEv : 232 -> 236
~ __ZN39DriverKit_AppleEthernetMLX5_NetIf_IVars14startInterfaceEv : 1720 -> 1744
```
