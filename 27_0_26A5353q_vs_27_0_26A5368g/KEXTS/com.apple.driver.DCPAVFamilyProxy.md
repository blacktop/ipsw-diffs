## com.apple.driver.DCPAVFamilyProxy

> `com.apple.driver.DCPAVFamilyProxy`

```diff

-450.0.0.0.0
+452.0.1.0.0
   __TEXT.__const: 0x278 sha256:b1071b444351ee14b1ec902d43a116ea222875972ebfd838224ba574d1fd9f2f
-  __TEXT.__cstring: 0x2377 sha256:47be0dc23a299104ba16d987ca769606073b0602e17a0ee54bbbc624bd09b5c9
-  __TEXT.__os_log: 0x1219 sha256:00fa0172b81e5cfdd89bd58db88f3700282f2e02ea5422c1b357623f598df009
-  __TEXT_EXEC.__text: 0x16100 sha256:1df099af40e96b9a61dfe2a1617523bcdd2eb594c812f9d29f32a6ea92a27b87
-  __TEXT_EXEC.__auth_stubs: 0x0
-  __DATA.__data: 0xc8 sha256:3a1b4413fc5903e57865aca735f77e34fe05dcaaa40aa360bde92def5bdaad31
+  __TEXT.__cstring: 0x2400 sha256:8a3e41ecea4fc6808ecf658881b03bea0bbcca994e3a19efd154d1c073203d73
+  __TEXT.__os_log: 0x1254 sha256:aab9c2a2d16d60a34111c9a2ccebdb7c027cb7af1c9380384e24a5839cecf121
+  __TEXT_EXEC.__text: 0x1646c sha256:d5aba04ac14dff74959883fa508e25cbb81615bd1005d03e32a92f294701b5e5
+  __TEXT_EXEC.__auth_stubs: 0x620 sha256:75dfe430b25d05ad25717b721d1344f2dfaa57aa0ba6985f28f5ee574967b760
+  __DATA.__data: 0xc8 sha256:61164bdb06c7fb8b13b50aba89ebacec3dd7d76c3d1e5f2f4567aafb8a0a8cea
   __DATA.__common: 0x308 sha256:508f5ba745944e982367cdbcd6a240acc7f895583df43b519b7d6745f5d86f7b
   __DATA.__bss: 0x8 sha256:af5570f5a1810b7af78caf4bc70a660f0df51e42baf91d4de5b2328de0e83dfc
-  __DATA_CONST.__mod_init_func: 0x98 sha256:9c82dab3533ff79a1bd557792945a3dd7a6a3aa86bfc15f55b8065764d63ab7e
-  __DATA_CONST.__mod_term_func: 0x98 sha256:a33128d4f8f1b2a6162acd3781d12e1f042184d1218486ca75f8b6b43f18f894
-  __DATA_CONST.__const: 0xd200 sha256:9fa75dd8ea7acd2019823925b74206deb4517cafcba075d7c90c1321a12c488d
-  __DATA_CONST.__kalloc_type: 0x4c0 sha256:0114242048cbe82b3aa5df04085c90b7b6bd1eb22e74c9348ce3ebc86d2ce6e6
-  __DATA_CONST.__kalloc_var: 0x140 sha256:e33f38f3058e0426dc118cc83f675ac35a785bbd7363cf8ed0a18c6afbfd7210
-  __DATA_CONST.__auth_got: 0x300 sha256:fe455ca9a8275ae5d35654fee5c87a921ca6c1b2b3c09b3575b47f4a769cfafd
-  __DATA_CONST.__got: 0x118 sha256:00f98d646f2758ff866ab7e60d575aea4494f295eb682b2e5cef8a533502b97d
-  UUID: 06E25172-9152-3339-B894-DC48CCD4BB53
-  Functions: 884
-  Symbols:   1682
-  CStrings:  276
+  __DATA_CONST.__mod_init_func: 0x98 sha256:f22c86939309e344da70820565eefec9523a8cfaf93f6e8b571dafd90fb53999
+  __DATA_CONST.__mod_term_func: 0x98 sha256:36559a4046f0105f74f825168b12b2df3b5bfa154cdf582c7285dded7f2e927c
+  __DATA_CONST.__const: 0xd250 sha256:1db15693c9d21e93e18eeefcd82732d0b7dff027b014c11cc62e6d06d2865cd0
+  __DATA_CONST.__kalloc_type: 0x4c0 sha256:2fb303408e75885c5006b7dccbd5a98934fd13928523962fd81a833fba396bd4
+  __DATA_CONST.__kalloc_var: 0x140 sha256:19fe488b869580ba9f3eed5bfdc737fdfb60e584b1fa855c111402c1f33ba1b1
+  __DATA_CONST.__auth_got: 0x310 sha256:6345696cd23b293c1e5ab9c22fdeffe0d9de39c6faa925719c4f08d80e439b87
+  __DATA_CONST.__got: 0x120 sha256:de01f5b2515860db04656547fbfdf917eefd141023defc8051abd435dd3439d8
+  UUID: FAE1514C-9C4C-35C5-9C9A-9251455E0B45
+  Functions: 891
+  Symbols:   1694
+  CStrings:  281
 
Symbols:
+ __ZN20DCPAVControllerProxy12requestResetEv
+ __ZN20DCPAVControllerProxy18sendDisplayMessageEh
+ __ZN20DCPAVControllerProxy24handleSendDisplayMessageEPS_PKN8DCPAVIPC7MessageE
+ __ZN26IOAVCommandDelegateService18sendDisplayMessageEh
+ __ZN26IOAVCommandDelegateService30registerCommandDelegateServiceEP9IOServiceP32IOAVCommandDelegateHostInterface
+ __ZN32IOAVCommandDelegateHostInterface27requestEnterCriticalSessionEb
+ __ZN9OSBoolean9metaClassE
+ __ZThn1560_N20DCPAVControllerProxy12requestResetEv
+ __ZThn1560_N20DCPAVControllerProxyD0Ev
+ __ZThn1560_N20DCPAVControllerProxyD1Ev
+ __ZZN20DCPAVControllerProxy18sendDisplayMessageEhE11_os_log_fmt
+ __ZZN20DCPAVControllerProxy5startEP9IOServiceE8commands
+ __block_descriptor_tmp.14
+ __block_descriptor_tmp.22
- __block_descriptor_tmp.12
- __block_descriptor_tmp.18
- __block_descriptor_tmp.7
CStrings:
+ "1211111212221212112222211221221111212112121121211212112121121211212112121121211212112121121211212112121121211212112121121211212112121121211212112121121211212112121121211212112121121211212112122211121"
+ "IOAV[%d] %s<0x%llx>::%s: _delegateService is not available"
+ "RequiresCommandDelegate"
+ "SendDisplayMessage"
+ "_delegateService is not available"
+ "sendDisplayMessage"
+ "v56@?0^{IOService=^^?i^{ExpansionData}^{OSDictionary}^{OSDictionary}^{ExpansionData}^{IOService}i^{IOService}[2I]QQ^{IOServicePM}B^vi^{IOInterruptSource}}8^{AFKEndpointInterface=^^?i^{ExpansionData}^{OSDictionary}^{OSDictionary}^{ExpansionData}^{IOService}i^{IOService}[2I]QQ^{IOServicePM}B^vi^{IOInterruptSource}^{AFKUserDataPipe}^{IOService}^{IOWorkLoop}^{OSArray}B}16I24Q28r^v36Q44I52"
+ "v60@?0^{IOService=^^?i^{ExpansionData}^{OSDictionary}^{OSDictionary}^{ExpansionData}^{IOService}i^{IOService}[2I]QQ^{IOServicePM}B^vi^{IOInterruptSource}}8^{AFKEndpointInterface=^^?i^{ExpansionData}^{OSDictionary}^{OSDictionary}^{ExpansionData}^{IOService}i^{IOService}[2I]QQ^{IOServicePM}B^vi^{IOInterruptSource}^{AFKUserDataPipe}^{IOService}^{IOWorkLoop}^{OSArray}B}16^v24i32Q36r^v44Q52"
+ "v64@?0^{IOService=^^?i^{ExpansionData}^{OSDictionary}^{OSDictionary}^{ExpansionData}^{IOService}i^{IOService}[2I]QQ^{IOServicePM}B^vi^{IOInterruptSource}}8^{AFKEndpointInterface=^^?i^{ExpansionData}^{OSDictionary}^{OSDictionary}^{ExpansionData}^{IOService}i^{IOService}[2I]QQ^{IOServicePM}B^vi^{IOInterruptSource}^{AFKUserDataPipe}^{IOService}^{IOWorkLoop}^{OSArray}B}16^{AFKEPCommandContextInterface=^^?}24I32Q36r^v44Q52I60"
- "12111112122212121122222112212211112121121211212112121121211212112121121211212112121121211212112121121211212112121121211212112121121211212112121121211212112121121211212112121121211212112121121222112"
- "v56@?0^{IOService=^^?i^{ExpansionData}^{OSDictionary}^{OSDictionary}^{ExpansionData}^{IOService}i^{IOService}[2I]QQ^{IOServicePM}B^vi^{IOInterruptSource}}8^{AFKEndpointInterface=^^?i^{ExpansionData}^{OSDictionary}^{OSDictionary}^{ExpansionData}^{IOService}i^{IOService}[2I]QQ^{IOServicePM}B^vi^{IOInterruptSource}^{AFKUserDataPipe}^{IOService}^{OSArray}B}16I24Q28r^v36Q44I52"
- "v60@?0^{IOService=^^?i^{ExpansionData}^{OSDictionary}^{OSDictionary}^{ExpansionData}^{IOService}i^{IOService}[2I]QQ^{IOServicePM}B^vi^{IOInterruptSource}}8^{AFKEndpointInterface=^^?i^{ExpansionData}^{OSDictionary}^{OSDictionary}^{ExpansionData}^{IOService}i^{IOService}[2I]QQ^{IOServicePM}B^vi^{IOInterruptSource}^{AFKUserDataPipe}^{IOService}^{OSArray}B}16^v24i32Q36r^v44Q52"
- "v64@?0^{IOService=^^?i^{ExpansionData}^{OSDictionary}^{OSDictionary}^{ExpansionData}^{IOService}i^{IOService}[2I]QQ^{IOServicePM}B^vi^{IOInterruptSource}}8^{AFKEndpointInterface=^^?i^{ExpansionData}^{OSDictionary}^{OSDictionary}^{ExpansionData}^{IOService}i^{IOService}[2I]QQ^{IOServicePM}B^vi^{IOInterruptSource}^{AFKUserDataPipe}^{IOService}^{OSArray}B}16^{AFKEPCommandContextInterface=^^?}24I32Q36r^v44Q52I60"

```
