## com.apple.iokit.IOUserEthernet

> `com.apple.iokit.IOUserEthernet`

```diff

-77.0.0.0.0
+79.0.0.0.0
   __TEXT.__const: 0x18
   __TEXT.__cstring: 0xc71
-  __TEXT_EXEC.__text: 0x5bb4
+  __TEXT_EXEC.__text: 0x57a8
   __TEXT_EXEC.__auth_stubs: 0x0
   __DATA.__data: 0xc8
   __DATA.__common: 0xb8

   __DATA_CONST.__mod_term_func: 0x20
   __DATA_CONST.__const: 0x1d30
   __DATA_CONST.__kalloc_type: 0x180
-  UUID: 9FD17187-AB05-303D-8368-F2BED0CB3D72
+  UUID: 8FC0A712-92A2-3295-96BD-FE2133B8473E
   Functions: 166
   Symbols:   0
   CStrings:  124
Functions:
~ sub_fffffe000ada9eb0 -> sub_fffffe000a3da230 : 168 -> 164
~ __ZN32IOUserEthernetResourceUserClient19terminateControllerEv : 244 -> 208
~ sub_fffffe000adaa24c -> sub_fffffe000a3da5a4 : 212 -> 204
~ sub_fffffe000adaa378 -> sub_fffffe000a3da6c8 : 120 -> 112
~ __ZN32IOUserEthernetResourceUserClient11clientCloseEv : 180 -> 172
~ __ZN32IOUserEthernetResourceUserClient21createControllerGatedEP25IOExternalMethodArguments : 988 -> 876
~ __ZN32IOUserEthernetResourceUserClient16createControllerEP25IOExternalMethodArguments : 212 -> 204
~ sub_fffffe000adaaf4c -> sub_fffffe000a3db214 : 120 -> 108
~ sub_fffffe000adab490 -> sub_fffffe000a3db74c : 428 -> 404
~ sub_fffffe000adab63c -> sub_fffffe000a3db8e0 : 228 -> 220
~ __ZN24IOUserEthernetController18initWithPropertiesEP12OSDictionary : 2084 -> 1740
~ sub_fffffe000adabf44 -> sub_fffffe000a3dc088 : 296 -> 268
~ __ZN24IOUserEthernetController27startWithStateEventCallbackEP9IOServicePFvP8OSObjectPS_PvES3_S5_ : 1512 -> 1412
~ sub_fffffe000adac654 -> sub_fffffe000a3dc718 : 352 -> 336
~ sub_fffffe000adac7c8 -> sub_fffffe000a3dc87c : 276 -> 240
~ __ZN24IOUserEthernetController18configureInterfaceEP18IONetworkInterface : 444 -> 400
~ sub_fffffe000adacbc8 -> sub_fffffe000a3dcc2c : 92 -> 84
~ sub_fffffe000adacc24 -> sub_fffffe000a3dcc80 : 156 -> 140
~ sub_fffffe000adacdec -> sub_fffffe000a3dce38 : 32 -> 28
~ sub_fffffe000adace0c -> sub_fffffe000a3dce54 : 32 -> 28
~ __ZN24IOUserEthernetController11outputStartEP18IONetworkInterfacej : 688 -> 672
~ __ZN24IOUserEthernetController28invalidateStateEventCallbackEv : 288 -> 276
~ __ZN24IOUserEthernetController12reportLinkUpEb : 288 -> 280
~ __ZN24IOUserEthernetController18handleClientAttachEP9en_client : 944 -> 888
~ sub_fffffe000adad7e4 -> sub_fffffe000a3dd7cc : 628 -> 612
~ __ZN24IOUserEthernetController18handleClientDetachEP9en_client : 700 -> 668
~ __ZN24IOUserEthernetController15handleBSDAttachEP18IONetworkInterface : 340 -> 332
~ __ZN24IOUserEthernetController15handleBSDDetachEP18IONetworkInterface : 328 -> 320
~ __ZN24IOUserEthernetController12setLinkStateEb : 340 -> 332
~ __ZN24IOUserEthernetController22setIfpPowerSavingsMaskEb : 404 -> 388
~ __ZN23IOUserEthernetInterface21attachToDataLinkLayerEjPv : 292 -> 284
~ __ZN23IOUserEthernetInterface23detachFromDataLinkLayerEjPv : 384 -> 380
~ __ZN23IOUserEthernetInterface15registerServiceEj : 296 -> 280
~ __ZNK23IOUserEthernetInterface13getNamePrefixEv : 248 -> 240
~ sub_fffffe000adaf568 -> sub_fffffe000a3df4d4 : 92 -> 100

```
