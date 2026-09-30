## com.apple.driver.EXDisplayPipeH18P

> `com.apple.driver.EXDisplayPipeH18P`

```diff

-8.1.12.0.0
-  __TEXT.__const: 0x48 sha256:2ebe29cb9960ec44a95633a43686a84a0a6be2e7d5d49ec099d5c458f6db9c52
-  __TEXT.__cstring: 0x285c sha256:d4fe840dcb5683ef7b28b9c938fff49fccbe8a4c06ef90f2e802ce4ca7bf9198
-  __TEXT_EXEC.__text: 0x8e54 sha256:ebfddbaba482162e353b3c0f31e0ab6b0ff3de6842c7e36c862217b0803ff40c
+9.1.40.0.0
+  __TEXT.__const: 0x50 sha256:867020d5ccdd502201b0b2050ec25193dc505704269d5484075e931c6ce99fce
+  __TEXT.__cstring: 0x29ea sha256:d719c7ef839e964238f4d8e74947bb2eb0ff86e9ae0be51bdbfd008e902ba1b6
+  __TEXT_EXEC.__text: 0x98e8 sha256:196ca41de52ed24983198ab4b0cdb2ea9e6f868c14fcdf3b723932c9459b0ac7
   __TEXT_EXEC.__auth_stubs: 0x0
-  __DATA.__data: 0xc4 sha256:038500dc8d3bfc325d891455830782c7bda0d8e2d753579c8b878ff656b9b124
+  __DATA.__data: 0xc4 sha256:c1a23cadfcde33daf122e42befa60a3e52ea62fb4a8bbbd382ef0dcdc8a73609
   __DATA.__common: 0x60 sha256:2ea9ab9198d1638007400cd2c3bef1cc745b864b76011a0e1bc52180ac6452d4
-  __DATA.__bss: 0x40 sha256:f5a5fd42d16a20302798ef6ed309979b43003d2320d9f0e8ea9831a92759fb4b
-  __DATA_CONST.__auth_got: 0x238 sha256:b626bca17080d7a5ac97cfad2a02bdf38142fd025de77229ccb1f2114d36c192
-  __DATA_CONST.__got: 0x30 sha256:9cf838f0cf5d33a0461320e859678ce34d430e1f35f1600847935922cc1f8918
-  __DATA_CONST.__mod_init_func: 0x18 sha256:b7b45ed83205b0748e050ea0e30254609a713f6a243a26fffb1148b6b136f2dd
-  __DATA_CONST.__mod_term_func: 0x10 sha256:939c284b3cedada62dcd331b379cbe1901183c13383247f65183750d1286cbed
-  __DATA_CONST.__const: 0xf80 sha256:103e70d6fdcbc72451fa7994f12d787efe596de32e779e1a9d9cd7722754e631
-  __DATA_CONST.__kalloc_type: 0x80 sha256:350350c8271c6551e43586e5c9f74cb4243ce5301ac7cdefd028a2d53022d604
-  UUID: D125ACA7-3F96-3FF3-83F0-4C5AEB506261
-  Functions: 178
+  __DATA.__bss: 0x10 sha256:374708fff7719dd5979ec875d56cd2286f6d3cf7ec317a3b25632aab28ec37bb
+  __DATA_CONST.__mod_init_func: 0x18 sha256:4148e714e7b9304edb326d7c0c36e584f579c5370e44f28b91b2da1cedbc705d
+  __DATA_CONST.__mod_term_func: 0x10 sha256:96482457fddc529792c15f19b871037286fab60660006abd00946981992ac18d
+  __DATA_CONST.__const: 0xfb0 sha256:3a0ed20c2ad8d24becd820aec79e629ae3392a2b8cc19dc17fbf19f338fc81d2
+  __DATA_CONST.__kalloc_type: 0x80 sha256:94f7e269757c53eadb88f687ba8d2626154eb78ed74b9a152016f1c467fe7566
+  __DATA_CONST.__auth_got: 0x258 sha256:9a877f4eba13b8c678eead70cfcc954b07049db3c18471181dd83fee9065fd2b
+  __DATA_CONST.__got: 0x38 sha256:ce66b9cf1696b0418bd81aacf9d79cdc20419cb0f8cb0deaf846f62ee46243d4
+  UUID: 4F33BEAC-8E9F-3099-BFEB-0478DD39F174
+  Functions: 187
   Symbols:   0
-  CStrings:  240
+  CStrings:  250
 
CStrings:
+ "%s.%s.stream0"
+ "12111112122212121222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222111221111111111111111112111112"
+ "EXDisplayPipe: error: getFrameInfo(...) failed\n"
+ "EXDisplayPipe: error: structureOutputSize mismatch for GetFrameInfo\n"
+ "EXDisplayPipe::%s get_display_index failed\n"
+ "EXDisplayPipe::%s parse_edt_properties failed\n"
+ "[EXDisplayPipe]: %s: disp_index %d \n"
+ "[EXDisplayPipe]: %s: disp_index_prop is NULL \n"
+ "[EXDisplayPipe]: %s: edk_service %s \n"
+ "[EXDisplayPipe]: %s: edk_service_prop is NULL \n"
+ "[EXDisplayPipe]: %s: exclave_service %s \n"
+ "[EXDisplayPipe]: %s: exclave_service_prop is NULL \n"
+ "[EXDisplayPipe]: %s: m_display_index %d \n"
+ "display-index"
+ "display_id"
+ "exclave-edk-service"
+ "exclave-service"
+ "exdisplaypipe"
+ "parse_edt_properties"
+ "v48@?0{exdisplaypipetightbeamcommon_exdisplaypipeframeinfo__opt_s=B{exdisplaypipetightbeamcommon_exdisplaypipeframeinfo_s=Bffffffff}}8"
- "%s.%s.stream%u"
- "12111112122212121222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222111211111111111111111111212"
- "EXDisplayPipe: set DART power: %u\n"
- "EXDisplayPipe::%s failed to retrieve mapper SCA (1)\n"
- "EXDisplayPipe::%s failed to retrieve mapper SCL (0)\n"
- "EXDisplayPipe::%s: submitChillPillMetrics failed\n"
- "EXDisplayPipe::%s: submitFailureCounters failed\n"
- "EXDisplayPipe::%s: submitFailureRatios failed\n"
- "EXDisplayPipe::%s: submitFailureTimes failed\n"
- "submitTelemetry"

```
