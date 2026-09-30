## com.apple.driver.AppleDisplayCrossbar

> `com.apple.driver.AppleDisplayCrossbar`

```diff

-414.0.0.0.2
+417.0.1.0.0
   __TEXT.__const: 0x26c sha256:2aa5b78cab13994616d9717065d19f56571d615c4e52662fea0c38511302704f
-  __TEXT.__cstring: 0x4d62 sha256:acd3c517a238fc0e80e5ed342304087fe31d4746d69c03534e4721e1e52193b9
-  __TEXT.__os_log: 0x6c22 sha256:91c1ac6d90cf72b6470b8f9de38cd4c1957d9a5edebf6b548343ef795e25345e
-  __TEXT_EXEC.__text: 0x3f3c4 sha256:064dc40f4af7fc641b2c5318426b80c1e4a75ed97bb3afa507642a7f5f083593
-  __TEXT_EXEC.__auth_stubs: 0x0
-  __DATA.__data: 0xc4 sha256:31647bc7dce3b3d08f2da8dc64d822bc0f5f7ae8e19590f3e0c824efec68a981
+  __TEXT.__cstring: 0x4cf4 sha256:5bf444c6fc2f4e59bd426829e67ff6ca6063cc6aa7490ea8cca4100b193851b3
+  __TEXT.__os_log: 0x6bc7 sha256:38d560405d5e8e5803372a632c8fce7540697a5dd83caa8acec125f80b4c41e1
+  __TEXT_EXEC.__text: 0x3f208 sha256:e7a4b00707ac92c57f98ed77639abf2cc0d1002c9aecbff74ff7046bf7128d1e
+  __TEXT_EXEC.__auth_stubs: 0x630 sha256:3654babd832b92580b84ccd0c6fd5dd2c3e0c67ff107b2084a89e88561b18d3f
+  __DATA.__data: 0xc4 sha256:e0548b7001eaafa9dbd7854eb76af08adee6e7e54de84e183e6f9031f7f7f25f
   __DATA.__common: 0x510 sha256:94637c6efefbdcc3d3bb74d61732b22250552654c8c11f0fa9c3b3ed11d38373
-  __DATA_CONST.__mod_init_func: 0xf8 sha256:e89eba44368f78c8c38a6a4bd1ec55db955d35cc8b19d6226472ef2bca0d55a6
-  __DATA_CONST.__mod_term_func: 0xf8 sha256:fd2ac3beb23e24be7c178724a028c6c67efc7be750218eba87d2dd2b49789c4c
-  __DATA_CONST.__const: 0x112c0 sha256:ca1dd01dc528f98ee976597d17ccfb2b8e36344af80e7ac61bf00311d5012042
-  __DATA_CONST.__kalloc_type: 0x800 sha256:f8215b5be4482652357ed147f7bfdc45403126c92c0486d919c5a5ed1ee1b46a
-  __DATA_CONST.__kalloc_var: 0xa0 sha256:ef23fb5c8caec703242647235c6670f8060f4e9cd5e40e0f9a85ec9753462786
-  __DATA_CONST.__auth_got: 0x310 sha256:cb2a6d4ef56089b1dd63a23eed1f76cde371877c1718176bda1c1a64f924e3a5
-  __DATA_CONST.__got: 0x100 sha256:2db7a76cfa034e51d801b94d3169776d7099bf8b1bbb5c03cd1079ed05e8d45b
-  UUID: 3ED6DFDE-7035-321C-B3F0-3021CBD82D53
-  Functions: 2200
+  __DATA_CONST.__mod_init_func: 0xf8 sha256:f0f6869b34626e358d04af2c8f9256d0db6515c7687061632f349b42b7e9cbf5
+  __DATA_CONST.__mod_term_func: 0xf8 sha256:8bbd89dc61b3ba3f49cff6b5f06d12ee3c8024f43fef8591ea952be94ccfe284
+  __DATA_CONST.__const: 0x11308 sha256:16c8e78960692d0cff0402643b9296310446b951ada8e1c7c2d7b7a7209e92f4
+  __DATA_CONST.__kalloc_type: 0x800 sha256:6b81d56eda16069933979ec6d5efbc1a3bcff55ddd0a3680a857350afd37ff9a
+  __DATA_CONST.__kalloc_var: 0xa0 sha256:3b2a89f6ee8c389c517678aa37983e6378df529568ac5a7b0e2b544e292ba1a8
+  __DATA_CONST.__auth_got: 0x318 sha256:921edcd3b3683f0865c3e5d7937070e666cb92d0d8c15b6192bae1b936be280f
+  __DATA_CONST.__got: 0xf8 sha256:6877061c13eb2ab8da8647724bad06390b757e48de12943ff30a14b00c7d5660
+  UUID: 53B508E8-8924-3D11-84A4-755CB94C1917
+  Functions: 2204
   Symbols:   0
-  CStrings:  820
+  CStrings:  816
 
CStrings:
+ "12222222222222222222222"
+ "IOAV[%d] %s<0x%llx>::%s: dfp(0x%llx): Domain%u, atc%u,%u (atc%u-%s): Bogus tile assignment detected (%d/%d/%d), revisit DFP display pipe assignment\n"
+ "IOAV[%d] %s<0x%llx>::%s: dfp(0x%llx): reallocate for newly available ext pipes\n"
+ "dfp(0x%llx): Domain%u, atc%u,%u (atc%u-%s): Bogus tile assignment detected (%d/%d/%d), revisit DFP display pipe assignment\n"
+ "dfp(0x%llx): reallocate for newly available ext pipes\n"
+ "role"
- "122222222222222222222"
- "IOAV[%d] %s<0x%llx>::%s: dfp(0x%llx): Domain%u, atc%u,%u (atc%u-%s): Bogus tile assignment detected, revisit DFP display pipe assignment\n"
- "IOAV[%d] %s<0x%llx>::%s: dfp(0x%llx): revisit DFP display pipe assignment for Dual cable display\n"
- "IOAV[%d] %s<0x%llx>::%s: dfp(0x%llx): revisit DFP display pipe assignment for HDMI\n"
- "allows-dual-pipe"
- "dfp(0x%llx): Domain%u, atc%u,%u (atc%u-%s): Bogus tile assignment detected, revisit DFP display pipe assignment\n"
- "dfp(0x%llx): revisit DFP display pipe assignment for Dual cable display\n"
- "dfp(0x%llx): revisit DFP display pipe assignment for HDMI\n"
- "dpxbar-dual-pipe"
- "supportsDualPipe"

```
