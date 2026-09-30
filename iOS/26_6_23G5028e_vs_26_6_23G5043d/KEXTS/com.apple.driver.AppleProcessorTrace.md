## com.apple.driver.AppleProcessorTrace

> `com.apple.driver.AppleProcessorTrace`

```diff

-78.100.33.0.0
-  __TEXT.__os_log: 0x195e sha256:3afd79eb9e76b1c57d92d0628ff9e1349ef8a23dac7bd964faff1831a86e297b
+78.160.3.0.0
+  __TEXT.__os_log: 0x19b1 sha256:ac2ec5a03f5fcd65b472b230b32be5f01a9122f6fb14fa32c63b7b2a6b2e5bb1
   __TEXT.__const: 0xa8 sha256:75fe82e567eabbbb9a7a62cf9a2eea29331b8130f2481346663e0f6ec4abd18d
-  __TEXT.__cstring: 0x52d0 sha256:405d8106516474755fb5760dead50b1ba68f8f4f810a2527d4aa25a3dd4befd3
-  __TEXT_EXEC.__text: 0x2fb60 sha256:d58bab38b2e981cf993d88422cf6d75009a350ce3478b343b5a5eddd2bf33ff4
+  __TEXT.__cstring: 0x5370 sha256:56d3572964ceea181c4a4d103362a83347b36e6b0084c764c459b4ca8b0744cf
+  __TEXT_EXEC.__text: 0x2f840 sha256:6572e8830613d1cdbc46fd0a0e8e9ab404544429e7d3a699aaae86f10c565510
   __TEXT_EXEC.__auth_stubs: 0x0
-  __DATA.__data: 0xc4 sha256:a21e03d55bb65093424118d802aeffb9f5f704b3616ed82c3671b5a32ca78db8
+  __DATA.__data: 0xc4 sha256:23c97719f64b82227cee183a721829724e68a48709ee5a3a4d7c8a3ffb9c4e31
   __DATA.__common: 0x6e8 sha256:7314b978571ffc723887d81a40c88dbd2de4b221b4a0149d14f284b074eec9f9
-  __DATA_CONST.__auth_got: 0x3c0 sha256:d1ed32e51a6306630b0a87522f5a46a4ab79624729f50d932091cfd583038013
-  __DATA_CONST.__got: 0xb0 sha256:5911551681634ffe54ec948283a0f7ff1528de808c3199025d06a74aba528f9f
-  __DATA_CONST.__mod_init_func: 0xd0 sha256:1a31d3ef435a8e4f202c1642374955e4c9ff5a1c6f96963fb288319e5594e379
-  __DATA_CONST.__mod_term_func: 0xd0 sha256:30766d955cff15a42ddced398719daae67fd02ddc9b66c1de3f7deb8ac84a97d
-  __DATA_CONST.__const: 0x9c08 sha256:36f74fa27349815a710e4a9c8448e4607e69847e6265bb9f4a1be43f148092cc
-  __DATA_CONST.__kalloc_type: 0x680 sha256:935f4b56bb753192906e731e97f0425659da9ededbf8d3300fc880e333ecb5af
-  __DATA_CONST.__kalloc_var: 0xf0 sha256:5f8091237633fb29d8d92ead57c0bdfbd071cbb3bca7bfd6a53ffd4df3237a29
-  UUID: 9A2BE757-F297-3D52-A60E-B2C2B23A26FB
-  Functions: 1143
+  __DATA_CONST.__auth_got: 0x3c0 sha256:5f278533f0768c8d9227de18055980ba643e66feaef0cd4bbaca7744cf4feb22
+  __DATA_CONST.__got: 0xb0 sha256:10f2ca2e360eaac6bfcc6a721d40bb752f692f134521dca7bd0b035a7e17e2b2
+  __DATA_CONST.__mod_init_func: 0xd0 sha256:485a054316726018b05bfd9f451283c37b764708443c687b6ef24bbfb98897cd
+  __DATA_CONST.__mod_term_func: 0xd0 sha256:2984fba6e7bdad147ccbd16bb7b35cb818b5e1e43e4d21b6decc1203eed6b8c1
+  __DATA_CONST.__const: 0x9c08 sha256:a2e4967dd0a2849d0ba22c208d49c32a7b4dd6a7ce7169e081b01518935435b4
+  __DATA_CONST.__kalloc_type: 0x680 sha256:e0941b2a13a469a381119262225a4facc4b44bdbc2612b4de80949a52b6e14c9
+  __DATA_CONST.__kalloc_var: 0xf0 sha256:0856a36061c74153a4f03333a44a0dbef98608840a6c87d034955d4e6a17048e
+  UUID: 112692C4-413F-32E3-BCDD-B7C37D0832B8
+  Functions: 1141
   Symbols:   0
-  CStrings:  492
+  CStrings:  498
 
CStrings:
+ "AppleProcessorTrace::hibernationSleep\n"
+ "AppleProcessorTrace::hibernationWake\n"
+ "AppleProcessorTrace::startTracingOnClustersGated(%p)\n"
+ "AppleProcessorTrace::stopTracingOnClustersGated\n"
+ "expectState(DriverState::Hibernating)"
+ "expectState(DriverState::Tracing) || expectState(DriverState::Paused)"
+ "void AppleProcessorTrace::hibernationSleep()"
+ "void AppleProcessorTrace::hibernationWake()"
+ "void AppleProcessorTrace::startTracingOnClustersGated(DriverState)"
+ "void AppleProcessorTrace::stopTracingOnClustersGated()"
- "AppleProcessorTrace::startTracingOnClusterGated\n"
- "AppleProcessorTrace::stopTracingOnClusterGated\n"
- "IOReturn AppleProcessorTrace::startTracingOnClusterGated(ml_topology_cluster_t)"
- "IOReturn AppleProcessorTrace::stopTracingOnClusterGated(ml_topology_cluster_t)"

```
