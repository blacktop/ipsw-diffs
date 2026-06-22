## com.apple.driver.AppleProcessorTrace

> `com.apple.driver.AppleProcessorTrace`

```diff

-125.0.0.0.0
-  __TEXT.__os_log: 0x194f sha256:e6caa829974a036ea2e0f9a372f104dca8d2f67534ef0f1729c849483bf8f488
+129.0.0.0.0
+  __TEXT.__os_log: 0x19a2 sha256:7051f4a8afd4b8d13502f97b0ab83bd2b4e35e702672cd97f24a0ea7419f13d7
   __TEXT.__const: 0xa8 sha256:1c7d36281974e00a4330cc2886544c1e3f1e6f8cc63f65ae4bfa9357f2fdb1d5
-  __TEXT.__cstring: 0x5403 sha256:4b0ef578ceebbc0ba6fe9ec5ab54f349a51acd636592aa110219680c7d0b54ce
-  __TEXT_EXEC.__text: 0x33ca4 sha256:dec26b6062b0896bbf53f8919b094b6e97c758a7dbcfd68f6a6782f8726c63f3
-  __TEXT_EXEC.__auth_stubs: 0x0
-  __DATA.__data: 0xc4 sha256:86814e4b7667d515b78c197b46666d9073caa25347a62cb55f33ef164e5af0b6
+  __TEXT.__cstring: 0x548e sha256:f0eaae8c0ffded76d0d80dc19174404e81314f4c6a05d81cc7cf27a1cf7f0f13
+  __TEXT_EXEC.__text: 0x338e4 sha256:6d27f95feaeca091cc85d8620a61b22c8e05aee4ddd8944e22c0327343f73fbc
+  __TEXT_EXEC.__auth_stubs: 0x780 sha256:b8e29f4f82b20917ba8c0e1af0f40b3ec754eb69d2cbe513f5fe211cf2e14a43
+  __DATA.__data: 0xc4 sha256:c2a50b2b999d170c9d4128d6279a18a39848b880755fa6f82112f267b11fca0d
   __DATA.__common: 0x6e8 sha256:7314b978571ffc723887d81a40c88dbd2de4b221b4a0149d14f284b074eec9f9
-  __DATA_CONST.__mod_init_func: 0xd0 sha256:d4cb7cc36fa8260f090fe7ed068de8982e3d9d505ce226b0475590ae3069707c
-  __DATA_CONST.__mod_term_func: 0xd0 sha256:a68cc6190bd0e8296cc31a44021b5f1db33c3055c1c13bd33d1ed4f54633742b
-  __DATA_CONST.__const: 0x9cf0 sha256:8c7a091df33a506a39c310dbbe1b4eb40846bd046c96853b7f2ca148fca84797
-  __DATA_CONST.__weak_auth_got: 0xb0 sha256:07277f1d5288e399432dc6d2e9b7f5be6c50c6eb4ba0ff2e0af17be4ffce814a
-  __DATA_CONST.__kalloc_type: 0x680 sha256:26a2a8c29203ba353af2947bcf434d5a946786ca600022066fd5e491921288ae
-  __DATA_CONST.__kalloc_var: 0xf0 sha256:e24b6f5bbefdb6948187ada814f9f2048abd3fee6eb9941370b4011de4126a24
-  __DATA_CONST.__auth_got: 0x310 sha256:98d6cbb65b65a4988cbf6e584aeaead9ff53680a1aa79a5ce9f778b260899858
-  __DATA_CONST.__got: 0xb0 sha256:808c3e91437ba6cfa4394eb4f0a6ac44582d42ce441641b60da272821a6559b7
-  UUID: 04ED7DC7-B49E-3321-B65A-D3CBE8D2397F
-  Functions: 1166
+  __DATA_CONST.__mod_init_func: 0xd0 sha256:9154e1f15169022088e4855ea35837c8dbbdd74efa4209087aed3f77cdfc0b74
+  __DATA_CONST.__mod_term_func: 0xd0 sha256:22de20e3986cba7a223bef7884511127e6a597ea90aa555427429bd29d86211b
+  __DATA_CONST.__const: 0x9d90 sha256:82d6813c60d38714be7ad95e4cf80f6611f588289a077434445bbcdf6afd3f00
+  __DATA_CONST.__weak_auth_got: 0xb0 sha256:e52a6789b14e39a421f066226064609ee146824fbacde4546fad0a4d137fee0c
+  __DATA_CONST.__kalloc_type: 0x680 sha256:e42fc3996877c9f3ab9e805513ba0c15226b30914bd3806023032cc17fd2ba07
+  __DATA_CONST.__kalloc_var: 0xf0 sha256:5575610f1a14ffce0a3985e36225b4acc3980ae1c440e10f39153b4d3a60e650
+  __DATA_CONST.__auth_got: 0x310 sha256:44bdaabe2626137b7f52914ed2aeec18fdb683781bd4504f70b8d1e59732edad
+  __DATA_CONST.__got: 0xb0 sha256:22d293398dcca58c879d03a5d2d4213e6a58b6c4c0023958671eb2b8e2a8af69
+  UUID: F998EB29-625A-3DE5-B16B-8595C54240D6
+  Functions: 1184
   Symbols:   0
-  CStrings:  494
+  CStrings:  500
 
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
+ "void AppleProcessorTrace::startTracingOnTraceableCores()"
+ "void AppleProcessorTrace::stopTracingOnClustersGated()"
- "AppleProcessorTrace::startTracingOnClusterGated\n"
- "AppleProcessorTrace::stopTracingOnClusterGated\n"
- "IOReturn AppleProcessorTrace::startTracingOnClusterGated(ml_topology_cluster_t)"
- "IOReturn AppleProcessorTrace::stopTracingOnClusterGated(ml_topology_cluster_t)"
- "void AppleProcessorTrace::startTracingOnTraceableCores(ml_topology_cluster_t)"

```
