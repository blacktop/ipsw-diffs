## com.apple.driver.AppleT8140PCIe

> `com.apple.driver.AppleT8140PCIe`

```diff

-824.120.3.0.0
-  __TEXT.__cstring: 0x24e5
+936.0.6.0.0
+  __TEXT.__cstring: 0x299a
+  __TEXT.__os_log: 0x1b46
   __TEXT.__const: 0x16e
-  __TEXT_EXEC.__text: 0xdc1c
+  __TEXT_EXEC.__text: 0x1b6b4
   __TEXT_EXEC.__auth_stubs: 0x0
   __DATA.__data: 0x3d8
   __DATA.__common: 0xb0
-  __DATA_CONST.__auth_got: 0x128
-  __DATA_CONST.__got: 0x40
+  __DATA_CONST.__auth_got: 0x158
+  __DATA_CONST.__got: 0x68
   __DATA_CONST.__mod_init_func: 0x20
   __DATA_CONST.__mod_term_func: 0x20
-  __DATA_CONST.__const: 0x24c0
+  __DATA_CONST.__const: 0x24f0
   __DATA_CONST.__kalloc_type: 0x100
-  UUID: 5F3DE1FA-76F8-3F7B-9CEC-B7442F05175B
-  Functions: 360
+  UUID: 487C5BB3-9961-389C-9006-C99AEC8E44D0
+  Functions: 315
   Symbols:   0
-  CStrings:  219
+  CStrings:  283
 
CStrings:
+ "\"Dynamic SID configuration failed\" @%s:%d"
+ "(sid != 0) || !valid"
+ "121111121222121211111121111221111111111111111111111112122222222111211222211111112222222222222222222222222222222222122122122122122122122122122122122122122122122122122122122122122122122122122122122122122122122122122122122122122122122122122122122122122122122122122122122122122122122122122122122122122122122121222222222222222222222222222222222222222222222222222222222222222222111222221211121221211221221221212212122122222"
+ "1211111212221212111111211112211111111111111111111111121222222221112112222111111122222222222222222222222222222222221221221221221221221221221221221221221221221221221221221221221221221221221221221221221221221221221221221221221221221221221221221221221221221221221221221221221221221221221221221221221221221221212222222222222222222222222222222222222222222222222222222222222222221112222212111212212112212212212212122122121221222222"
+ "12111112122212121111121212222221122211221111111211222111111122112212221122122122122111112"
+ "[PCIe:%u %llu ns] AppleT8132PCIe::%s APCIe AXI2AF reg index = %d\n"
+ "[PCIe:%u %llu ns] AppleT8132PCIe::%s APCIe Common reg index = %d\n"
+ "[PCIe:%u %llu ns] AppleT8132PCIe::%s AXI2AF: 0x%llx = 0x%x\n"
+ "[PCIe:%u %llu ns] AppleT8132PCIe::%s CIO3PLL_CORE: 0x%llx = 0x%x\n"
+ "[PCIe:%u %llu ns] AppleT8132PCIe::%s Done waiting\n"
+ "[PCIe:%u %llu ns] AppleT8132PCIe::%s PCIECLKGEN: 0x%llx = 0x%x\n"
+ "[PCIe:%u %llu ns] AppleT8132PCIe::%s PHY %d reg index = %d\n"
+ "[PCIe:%u %llu ns] AppleT8132PCIe::%s Port %d Config reg index = %d\n"
+ "[PCIe:%u %llu ns] AppleT8132PCIe::%s Port %d DART reg index = %d\n"
+ "[PCIe:%u %llu ns] AppleT8132PCIe::%s Port %d INTR2AXI reg index = %d\n"
+ "[PCIe:%u %llu ns] AppleT8132PCIe::%s Port %d LTSSM debug reg index = %d\n"
+ "[PCIe:%u %llu ns] AppleT8132PCIe::%s Port %d PHY_GLUE reg index = %d\n"
+ "[PCIe:%u %llu ns] AppleT8132PCIe::%s Port %d PHY_IP reg index = %d\n"
+ "[PCIe:%u %llu ns] AppleT8132PCIe::%s Port %d link recovery reg index = %d\n"
+ "[PCIe:%u %llu ns] AppleT8132PCIe::%s Port %d link speed reg index = %d\n"
+ "[PCIe:%u %llu ns] AppleT8132PCIe::%s Waiting for gtb_initialized\n"
+ "[PCIe:%u %llu ns] AppleT8132PCIe::%s Waiting for max_pclk_good\n"
+ "[PCIe:%u %llu ns] AppleT8132PCIe::%s Waiting for refpll_clk_good\n"
+ "[PCIe:%u %llu ns] AppleT8132PCIe::%s Waiting for sleep_b_big_out\n"
+ "[PCIe:%u %llu ns] AppleT8132PCIe::%s Waiting for sleep_b_sml_out\n"
+ "[PCIe:%u %llu ns] AppleT8132PCIe::%s _axi2afRegistersBaseAddress = %p _axi2afRegistersBaseAddressPhys = %p\n"
+ "[PCIe:%u %llu ns] AppleT8132PCIe::%s _cio3pllcoreRegistersBaseAddress = %p _cio3pllcoreRegistersBaseAddressPhys = %p\n"
+ "[PCIe:%u %llu ns] AppleT8132PCIe::%s _pcieclkgenRegistersBaseAddress = %p _pcieclkgenRegistersBaseAddressPhys = %p\n"
+ "[PCIe:%u %llu ns] AppleT8132PCIe::%s _phyIPRegistersBaseAddress = %p _phyIPRegistersBaseAddressPhys = %p\n"
+ "[PCIe:%u %llu ns] AppleT8132PCIe::%s _phyRegistersBaseAddress = %p _phyRegistersBaseAddressPhys = %p\n"
+ "[PCIe:%u %llu ns] AppleT8132PCIe::%s phy IP: 0x%llx = 0x%x\n"
+ "[PCIe:%u %llu ns] AppleT8140PCIe::%s APCIe AXI2AF reg index = %d\n"
+ "[PCIe:%u %llu ns] AppleT8140PCIe::%s APCIe Common reg index = %d\n"
+ "[PCIe:%u %llu ns] AppleT8140PCIe::%s Done waiting\n"
+ "[PCIe:%u %llu ns] AppleT8140PCIe::%s PHY %d reg index = %d\n"
+ "[PCIe:%u %llu ns] AppleT8140PCIe::%s Port %d Config reg index = %d\n"
+ "[PCIe:%u %llu ns] AppleT8140PCIe::%s Port %d INTR2AXI reg index = %d\n"
+ "[PCIe:%u %llu ns] AppleT8140PCIe::%s Port %d LTSSM debug reg index = %d\n"
+ "[PCIe:%u %llu ns] AppleT8140PCIe::%s Port %d Link Speed Debug reg index = %d\n"
+ "[PCIe:%u %llu ns] AppleT8140PCIe::%s Port %d PHY_GLUE reg index = %d\n"
+ "[PCIe:%u %llu ns] AppleT8140PCIe::%s Waiting for gtb_initialized\n"
+ "[PCIe:%u %llu ns] AppleT8140PCIe::%s Waiting for refpll_clk_good\n"
+ "[PCIe:%u %llu ns] apcie[%u:%s]::%s DART: 0x%llx = 0x%x\n"
+ "[PCIe:%u %llu ns] apcie[%u:%s]::%s INTR2AXI: 0x%llx = 0x%x\n"
+ "[PCIe:%u %llu ns] apcie[%u:%s]::%s LTSSM debug: 0x%llx = 0x%x\n"
+ "[PCIe:%u %llu ns] apcie[%u:%s]::%s Link Recovery: 0x%llx = 0x%x\n"
+ "[PCIe:%u %llu ns] apcie[%u:%s]::%s Link recovery debug: 0x%llx = 0x%x\n"
+ "[PCIe:%u %llu ns] apcie[%u:%s]::%s Link speed debg: 0x%llx = 0x%x\n\n"
+ "[PCIe:%u %llu ns] apcie[%u:%s]::%s Link speed debug: 0x%llx = 0x%x\n"
+ "[PCIe:%u %llu ns] apcie[%u:%s]::%s Link speed debug: 0x%llx = 0x%x\n\n"
+ "[PCIe:%u %llu ns] apcie[%u:%s]::%s PHY lane: 0x%llx = 0x%x\n"
+ "[PCIe:%u %llu ns] apcie[%u:%s]::%s PTM enabled\n"
+ "[PCIe:%u %llu ns] apcie[%u:%s]::%s Unable to allocate buffer for RAS counter capture\n"
+ "[PCIe:%u %llu ns] apcie[%u:%s]::%s Unable to allocate buffer for link recovery debug tracer!\n"
+ "[PCIe:%u %llu ns] apcie[%u:%s]::%s Unable to allocate buffer for link speed debug tracer\n"
+ "[PCIe:%u %llu ns] apcie[%u:%s]::%s Unable to allocate buffer for ltssm debug tracer\n"
+ "[PCIe:%u %llu ns] apcie[%u:%s]::%s _expressCapOffset = 0x%x\n"
+ "[PCIe:%u %llu ns] apcie[%u:%s]::%s expected link width = %d\n"
+ "[PCIe:%u %llu ns] apcie[%u:%s]::%s getLinkRcvryDebugTracer buf is Null!\n"
+ "[PCIe:%u %llu ns] apcie[%u:%s]::%s getLinkRcvryDebugTracer size is Null!\n"
+ "[PCIe:%u %llu ns] apcie[%u:%s]::%s getLinkSpeedDebugTracer buf is Null!\n"
+ "[PCIe:%u %llu ns] apcie[%u:%s]::%s getLinkSpeedDebugTracer size is Null!\n"
+ "[PCIe:%u %llu ns] apcie[%u:%s]::%s link speed debug tracer empty,  number speed changes: 0x%08x\n"
+ "[PCIe:%u %llu ns] apcie[%u:%s]::%s link speed debug tracer empty, status 0x%08x\n"
+ "[PCIe:%u %llu ns] apcie[%u:%s]::%s ltssm debug tracer empty or too large, status 0x%08x\n"
+ "[PCIe:%u %llu ns] apcie[%u:%s]::%s maximumLinkSpeed = %d\n"
+ "disable-cplerr-panic"
- "12111112122212121111112111122111111111111111111111112122222222111211222211111112222222222222222222222222222222222122122122122122122122122122122122122122122122122122122122122122122122122122122122122122122122122122122122122122122122122122122122122122122122122122122122122122122122122122122122122122122122121222222222222222222222222222222222222222222222222222222222222222222111222121211221221221212212122122222"
- "121111121222121211111121111221111111111111111111111121222222221112112222111111122222222222222222222222222222222221221221221221221221221221221221221221221221221221221221221221221221221221221221221221221221221221221221221221221221221221221221221221221221221221221221221221221221221221221221221221221221221212222222222222222222222222222222222222222222222222222222222222222221112221212112212212212212122122121221222222"
- "12111112122212121111112122222211222112211111121122211111112211221221122122122122111112"
- "AppleT8132PCIe::%s APCIe AXI2AF reg index = %d\n"
- "AppleT8132PCIe::%s APCIe Common reg index = %d\n"
- "AppleT8132PCIe::%s AXI2AF: 0x%llx = 0x%x\n"
- "AppleT8132PCIe::%s CIO3PLL_CORE: 0x%llx = 0x%x\n"
- "AppleT8132PCIe::%s Done waiting\n"
- "AppleT8132PCIe::%s PCIECLKGEN: 0x%llx = 0x%x\n"
- "AppleT8132PCIe::%s PHY %d reg index = %d\n"
- "AppleT8132PCIe::%s Port %d Config reg index = %d\n"
- "AppleT8132PCIe::%s Port %d DART reg index = %d\n"
- "AppleT8132PCIe::%s Port %d INTR2AXI reg index = %d\n"
- "AppleT8132PCIe::%s Port %d LTSSM debug reg index = %d\n"
- "AppleT8132PCIe::%s Port %d PHY_GLUE reg index = %d\n"
- "AppleT8132PCIe::%s Port %d PHY_IP reg index = %d\n"
- "AppleT8132PCIe::%s Port %d link recovery reg index = %d\n"
- "AppleT8132PCIe::%s Port %d link speed reg index = %d\n"
- "AppleT8132PCIe::%s Waiting for gtb_initialized\n"
- "AppleT8132PCIe::%s Waiting for max_pclk_good\n"
- "AppleT8132PCIe::%s Waiting for refpll_clk_good\n"
- "AppleT8132PCIe::%s Waiting for sleep_b_big_out\n"
- "AppleT8132PCIe::%s Waiting for sleep_b_sml_out\n"
- "AppleT8132PCIe::%s _axi2afRegistersBaseAddress = %p _axi2afRegistersBaseAddressPhys = %p\n"
- "AppleT8132PCIe::%s _cio3pllcoreRegistersBaseAddress = %p _cio3pllcoreRegistersBaseAddressPhys = %p\n"
- "AppleT8132PCIe::%s _pcieclkgenRegistersBaseAddress = %p _pcieclkgenRegistersBaseAddressPhys = %p\n"
- "AppleT8132PCIe::%s _phyIPRegistersBaseAddress = %p _phyIPRegistersBaseAddressPhys = %p\n"
- "AppleT8132PCIe::%s _phyRegistersBaseAddress = %p _phyRegistersBaseAddressPhys = %p\n"
- "AppleT8132PCIe::%s phy IP: 0x%llx = 0x%x\n"
- "AppleT8140PCIe::%s APCIe AXI2AF reg index = %d\n"
- "AppleT8140PCIe::%s APCIe Common reg index = %d\n"
- "AppleT8140PCIe::%s Done waiting\n"
- "AppleT8140PCIe::%s PHY %d reg index = %d\n"
- "AppleT8140PCIe::%s Port %d Config reg index = %d\n"
- "AppleT8140PCIe::%s Port %d INTR2AXI reg index = %d\n"
- "AppleT8140PCIe::%s Port %d LTSSM debug reg index = %d\n"
- "AppleT8140PCIe::%s Port %d Link Speed Debug reg index = %d\n"
- "AppleT8140PCIe::%s Port %d PHY_GLUE reg index = %d\n"
- "AppleT8140PCIe::%s Waiting for gtb_initialized\n"
- "AppleT8140PCIe::%s Waiting for refpll_clk_good\n"
- "apcie[%u:%s]::%s DART: 0x%llx = 0x%x\n"
- "apcie[%u:%s]::%s INTR2AXI: 0x%llx = 0x%x\n"
- "apcie[%u:%s]::%s LTSSM debug: 0x%llx = 0x%x\n"
- "apcie[%u:%s]::%s Link Recovery: 0x%llx = 0x%x\n"
- "apcie[%u:%s]::%s Link recovery debug: 0x%llx = 0x%x\n"
- "apcie[%u:%s]::%s Link speed debg: 0x%llx = 0x%x\n\n"
- "apcie[%u:%s]::%s Link speed debug: 0x%llx = 0x%x\n"
- "apcie[%u:%s]::%s Link speed debug: 0x%llx = 0x%x\n\n"
- "apcie[%u:%s]::%s PHY lane: 0x%llx = 0x%x\n"
- "apcie[%u:%s]::%s PTM enabled\n"
- "apcie[%u:%s]::%s Unable to allocate buffer for RAS counter capture\n"
- "apcie[%u:%s]::%s Unable to allocate buffer for link recovery debug tracer!\n"
- "apcie[%u:%s]::%s Unable to allocate buffer for link speed debug tracer\n"
- "apcie[%u:%s]::%s Unable to allocate buffer for ltssm debug tracer\n"
- "apcie[%u:%s]::%s _expressCapOffset = 0x%x\n"
- "apcie[%u:%s]::%s expected link width = %d\n"
- "apcie[%u:%s]::%s getLinkRcvryDebugTracer buf is Null!\n"
- "apcie[%u:%s]::%s getLinkRcvryDebugTracer size is Null!\n"
- "apcie[%u:%s]::%s getLinkSpeedDebugTracer buf is Null!\n"
- "apcie[%u:%s]::%s getLinkSpeedDebugTracer size is Null!\n"
- "apcie[%u:%s]::%s link speed debug tracer empty,  number speed changes: 0x%08x\n"
- "apcie[%u:%s]::%s link speed debug tracer empty, status 0x%08x\n"
- "apcie[%u:%s]::%s ltssm debug tracer empty or too large, status 0x%08x\n"
- "apcie[%u:%s]::%s maximumLinkSpeed = %d\n"

```
