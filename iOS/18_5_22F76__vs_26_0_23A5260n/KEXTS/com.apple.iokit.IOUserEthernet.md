## com.apple.iokit.IOUserEthernet

> `com.apple.iokit.IOUserEthernet`

```diff

-76.100.1.0.0
+77.0.0.0.0
   __TEXT.__const: 0x18
   __TEXT.__cstring: 0xc71
-  __TEXT_EXEC.__text: 0x5bb4
+  __TEXT_EXEC.__text: 0x5bbc
   __TEXT_EXEC.__auth_stubs: 0x0
   __DATA.__data: 0xc8
   __DATA.__common: 0xb8

   __DATA_CONST.__mod_term_func: 0x20
   __DATA_CONST.__const: 0x1d30
   __DATA_CONST.__kalloc_type: 0x180
-  UUID: 9B95D943-73A1-39D3-B3D9-D25A87E1D8D8
+  UUID: 4ABEC651-DBF1-33B9-A1F1-AEC9238B12BB
   Functions: 166
   Symbols:   0
   CStrings:  124
Functions:
~ sub_fffffff00a84ee68 -> sub_fffffff00ac71288 : 44 -> 48
~ sub_fffffff00a84f48c -> sub_fffffff00ac718b0 : 72 -> 88
~ sub_fffffff00a84fc58 -> sub_fffffff00ac7208c : 44 -> 48
~ __ZN24IOUserEthernetController23initializeKernelControlEPb : 208 -> 204
~ __ZN24IOUserEthernetController27startWithStateEventCallbackEP9IOServicePFvP8OSObjectPS_PvES3_S5_ : 1520 -> 1512
~ __ZN24IOUserEthernetController18configureInterfaceEP18IONetworkInterface : 440 -> 444
~ __ZN24IOUserEthernetController14setEnableStateEb : 232 -> 236
~ __ZN24IOUserEthernetController11outputStartEP18IONetworkInterfacej : 684 -> 688
~ __ZN24IOUserEthernetController18handleClientAttachEP9en_client : 948 -> 944
~ __ZN24IOUserEthernetController19handleClientPacketsEP9en_clientP6__mbuf : 636 -> 628
~ __ZN24IOUserEthernetController12setLinkStateEb : 344 -> 340

```
