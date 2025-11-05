## com.apple.driver.AppleT8103PCIe

> `com.apple.driver.AppleT8103PCIe`

```diff

-824.60.9.0.0
-  __TEXT.__cstring: 0x1604
+824.100.33.0.0
+  __TEXT.__cstring: 0x1634
   __TEXT.__const: 0x15c
-  __TEXT_EXEC.__text: 0x6d20
+  __TEXT_EXEC.__text: 0x6d44
   __TEXT_EXEC.__auth_stubs: 0x0
   __DATA.__data: 0x1c0
   __DATA.__common: 0xb0

   __DATA_CONST.__got: 0x40
   __DATA_CONST.__mod_init_func: 0x20
   __DATA_CONST.__mod_term_func: 0x20
-  __DATA_CONST.__const: 0x3540
+  __DATA_CONST.__const: 0x3640
   __DATA_CONST.__kalloc_type: 0x100
-  UUID: CE6E3425-61CD-30EC-9D32-8F900220D939
-  Functions: 215
-  Symbols:   733
-  CStrings:  142
+  UUID: 9CB487C1-950D-3299-AFE5-C8EE7BCF0282
+  Functions: 214
+  Symbols:   749
+  CStrings:  143
 
Symbols:
+ __ZN17AppleEmbeddedPCIE16deviceMemoryReadEP18IOMemoryDescriptoryPvy
+ __ZN17AppleEmbeddedPCIE16deviceMemoryReadEP18IOMemoryDescriptoryS1_yy
+ __ZN21AppleEmbeddedPCIEPort11configRead8E17IOPCIAddressSpacehPh
+ __ZN21AppleEmbeddedPCIEPort12configRead16E17IOPCIAddressSpacehPt
+ __ZN21AppleEmbeddedPCIEPort12configRead32E17IOPCIAddressSpacehPj
+ __ZN21AppleEmbeddedPCIEPort12configWrite8E17IOPCIAddressSpacehh
+ __ZN21AppleEmbeddedPCIEPort13configWrite16E17IOPCIAddressSpaceht
+ __ZN21AppleEmbeddedPCIEPort13configWrite32E17IOPCIAddressSpacehj
+ __ZN21AppleEmbeddedPCIEPort23getLinkRcvryDebugTracerEPvPj
+ __ZN21AppleEmbeddedPCIEPort23getLinkSpeedDebugTracerEPvPj
+ __ZN21AppleEmbeddedPCIEPort26_captureLinkRcvryDebugHistEv
+ __ZN21AppleEmbeddedPCIEPort26_resetLinkSpeedDebugTracerEv
+ __ZN21AppleEmbeddedPCIEPort27_enableLinkRcvryDebugTracerEv
+ __ZN21AppleEmbeddedPCIEPort27_enableLinkSpeedDebugTracerEv
+ __ZN21AppleEmbeddedPCIEPort27captureLinkRcvryDebugTracerEv
+ __ZN21AppleEmbeddedPCIEPort27captureLinkSpeedDebugTracerEv
+ __ZN21AppleEmbeddedPCIEPort28_captureLinkRcvryDebugTracerEv
+ __ZN21AppleEmbeddedPCIEPort28_captureLinkSpeedDebugTracerEv
- __ZN11IOPCIBridge16deviceMemoryReadEP18IOMemoryDescriptoryPvy
- __ZN11IOPCIBridge16deviceMemoryReadEP18IOMemoryDescriptoryS1_yy
Functions:
~ __ZN18AppleT8103PCIePort24serializedConfigRegSpaceEv : 444 -> 448
~ __ZN18AppleT810xPCIePort18_enableRASCountersEv : 176 -> 180
~ __ZN18AppleT810xPCIePort19_captureRASCountersEv : 128 -> 140
~ __ZN18AppleT810xPCIePort24_captureLTSSMDebugTracerEv : 600 -> 624
~ __ZN18AppleT810xPCIePort14configMSIRangeEv : 528 -> 508
- sub_fffffe000a078154
~ __ZN18AppleT810xPCIePort22_initializeRootComplexEv : 536 -> 540
~ __ZN18AppleT810xPCIePort13enablePortPTMEb : 688 -> 676
~ __ZN18AppleT810xPCIePort13getLinkStatusEv : 68 -> 64
~ __ZN18AppleT810xPCIePort12setLinkSpeedEjb : 376 -> 372
~ __ZN18AppleT810xPCIePort23_updateRIDToSIDMappingsEj : 196 -> 232
~ __ZN18AppleT810xPCIePort4freeEv : 104 -> 108
~ __ZNK14AppleT810xPCIe24dtRegMapApcieAxi2AfIndexEv : 68 -> 76
~ __ZNK14AppleT810xPCIe21dtRegMapPMGRFuseIndexEv : 68 -> 76
~ __ZNK14AppleT810xPCIe24dtRegMapApcieCommonIndexEv : 68 -> 76
CStrings:
+ "121111121222121211111121111221111111111111111111111121222222221112112222111111122222222222222222222222222222222221221221221221221221221221221221221221221221221221221221221221221221221221221221221221221221221221221221221221221221221221221221221221221221221221221221221221221221221221221221221221221221221212222222222222222222222222222222222222222222222222222222222222222221112221211122122122212212"
+ "Multiple bad request interrupt bits set."
- "12111112122212121111112111122111111111111111111111212222222211121122221111111222222222222222222222222222222222212212212212212212212212212212212212212212212212212212212212212212212212212212212212212212212212212212212212212212212212212212212212212212212212212212212212212212212212212212212212212212212212122222222222222222222222222222222222222222222222222222222222222222211121122122122212212"

```
