## libAppleArchive.dylib

> `/usr/lib/libAppleArchive.dylib`

```diff

-450.100.4.0.0
-  __TEXT.__text: 0x82d0c sha256:ac8ff1b143ccdbdbce7910a3e7e86fe7c3762d0f2002506856e43ec78206db30
-  __TEXT.__auth_stubs: 0xf20 sha256:ded8b79d05f1d97505314caf13dcca105bb4c1d98b3d728d8703b27f3e0bc893
-  __TEXT.__cstring: 0x13278 sha256:fb3dd24f975b5d11ce4ae8cad2e60857792a3b2ff427c29a7877ed649f32793c
-  __TEXT.__const: 0x960 sha256:8f3664a433c0f80d4b79a0d8b6342922b0b88306baa90eccaac11e7fc9a7e9c8
+462.0.0.0.0
+  __TEXT.__text: 0x832a8 sha256:65f8987ff730cc523e1560ebd1ed50b7851f919a9f7c4ad92965bdebc4001fa4
+  __TEXT.__cstring: 0x13398 sha256:9a6030759f26c5112f44cd5e053ba30113ddfa34f6e74ee40f1082de589ab624
+  __TEXT.__const: 0x920 sha256:a1fec1783b3f3e18d8af5f06edebdb5bf1943626a511fca12289c3401ea2f6d2
   __TEXT.__oslogstring: 0x31 sha256:a6c65adee221d702f1bf5c33a1c2c4473fcb49ccdec9a7ddf1d8f2caf2243697
-  __TEXT.__unwind_info: 0xd38 sha256:c7aba6556faef0ed0c62523537d100ce18ba80b1c915fddad3f04216aed94756
-  __TEXT.__eh_frame: 0x48 sha256:fda0a56791e974c064195e1a314d3435fe55193d0d1c1dd1d5919419e893dabf
-  __DATA_CONST.__got: 0xa0 sha256:b393978842a0fa3d3e1470196f098f473f9678e72463cb65ec4ab5581856c2e4
-  __DATA_CONST.__const: 0x158 sha256:c20bda61b773ed1b5a1a8f50a67526e8af7d2492b119ff16bde81ce36e08d899
+  __TEXT.__unwind_info: 0xd78 sha256:7bd281e6f732a5663c70475fd96ee575d12f5828b5b2b30cc0b15f29960a35c5
+  __TEXT.__eh_frame: 0x48 sha256:2113d412ac8d28d15ef6fc2382ec29b4c82bdaa72720751b14bcd2b7bc4a8b4b
+  __TEXT.__auth_stubs: 0x0
+  __DATA_CONST.__const: 0x158 sha256:7603a08ed962f636acc7e8fb348f5009c07473eacc6713df59f6104cb32f1a56
+  __DATA_CONST.__got: 0x0
+  __AUTH_CONST.__const: 0x80 sha256:e13264352353dc4ce25e3dad86d867fb5f2b5553e53d7e5f37fcf01e1e9ad401
+  __AUTH_CONST.__cfstring: 0x40 sha256:0a3fffbd141f2c0d6c1d7a0aa4317393c317f3435fe2b87f0d40b7bcbfb89c21
   __AUTH_CONST.__auth_got: 0x790 sha256:3fcb1e1041f63f752bdebe8f875700003bd95e3fc507c2143555443c145c9769
-  __AUTH_CONST.__const: 0x80 sha256:6b8ce68efec4e9c9bfa18c7312715b69e9b4f3a6e1429c636759e725dedc359f
-  __AUTH_CONST.__cfstring: 0x40 sha256:d2b7ca4cccc63acfb7393dbc80db3c8c8efe849ea91d5ff11ab10be064712b37
   __DATA_DIRTY.__data: 0x10 sha256:eba956dc8f5e792f083beb1e308446a00c07f6a663aebe3d3d7ecc6936d4a6ab
   __DATA_DIRTY.__bss: 0x8 sha256:af5570f5a1810b7af78caf4bc70a660f0df51e42baf91d4de5b2328de0e83dfc
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation

   - /usr/lib/libbz2.1.0.dylib
   - /usr/lib/libcompression.dylib
   - /usr/lib/liblzma.5.dylib
-  UUID: A62B1D7E-A757-3E9F-B09C-5AF57A402F1E
-  Functions: 1067
-  Symbols:   2182
-  CStrings:  2889
+  UUID: 47C41712-A8B1-360F-A123-CFB4944B32DF
+  Functions: 1071
+  Symbols:   2190
+  CStrings:  2904
 
Symbols:
+ _ChunkPipelineCreate
+ _ChunkPipelineDestroy
+ _CompressChunkProc
+ _PCompressLZRavenDecode
+ _PCompressLZRavenEncode
+ _ParallelCompressionAFSCFixupMetadataEx
+ _WriteAlignedChunkProc
+ _pthread_cond_signal
+ _qos_class_self
- _pthread_cond_broadcast
- _realloc
- _reallocToFit
CStrings:
+ "  Compression: %s\n"
+ "AAAFSCStreamOpen failed: %s"
+ "Broken pipeline"
+ "ChunkPipelineCreate"
+ "ChunkPipelineDestroy"
+ "Create chunk pipeline"
+ "Flush chunk pipeline"
+ "LZMA"
+ "LZRAVEN"
+ "ParallelCompressionAFSCFixupMetadataEx"
+ "Pipeline failed"
+ "Pipeline failed: using in-thread compression"
+ "SharedArrayPush: pthread_cond_signal failed\n"
+ "Write chunk"
+ "WriteAlignedChunkProc"
+ "hw.perflevel1.physicalcpu"
+ "lzraven"
- "ParallelCompressionAFSCFixupMetadata"
- "SharedArrayPush: pthread_cond_broadcast failed\n"

```
