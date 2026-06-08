## libParallelCompression.dylib

> `/usr/lib/libParallelCompression.dylib`

```diff

-450.100.4.0.0
-  __TEXT.__text: 0x54e78 sha256:e066d00f8c21cabfb63481e87a6fadb577d2d5ed589e722f2f4598e988e7e6a6
-  __TEXT.__auth_stubs: 0xd30 sha256:83f869d81722093788e94010e788e7481cc68ea401b97cf8ed4fda942a96f8d4
-  __TEXT.__cstring: 0xf447 sha256:5e033b0dbf517c20579a8da6460abe08f1bb83dcca4028fbc3e7703dfc13f62c
-  __TEXT.__const: 0x850 sha256:de81f99d9b3a2b23c81fc484a3656b83b62de53910c486c7be59122ad5831690
+462.0.0.0.0
+  __TEXT.__text: 0x55c14 sha256:0285c8691aa6c18c691e5275597733cebf9a241f8576e8c5fd2cfe1b32a6433b
+  __TEXT.__cstring: 0xf55e sha256:2d2f7573aff193b9e7b5f0aadae4ad4460c0de612c02ad2fef16c384657fb160
+  __TEXT.__const: 0x830 sha256:824b6e4fda8b34f56ef77de2aaf7d5f409e15e21bbcb832093d0cf5d84de5b34
   __TEXT.__oslogstring: 0x31 sha256:a6c65adee221d702f1bf5c33a1c2c4473fcb49ccdec9a7ddf1d8f2caf2243697
-  __TEXT.__unwind_info: 0x948 sha256:cfa408ea8fc94c012ff6572021fa27d804d8d48d2e2615a6f2346e7066fc5d51
-  __TEXT.__eh_frame: 0x48 sha256:dcf42518e371077b3524e555e3f70acce6f0ca3a7482687e95ba3b472a566181
-  __DATA_CONST.__got: 0x38 sha256:d4817aa5497628e7c77e6b606107042bbba3130888c5f47a375e6179be789fbb
-  __DATA_CONST.__const: 0x118 sha256:fb579df42ad2b31a7bb8dd46fee3fc7795dd3ae8af5087aff2c0b1668fe77a77
+  __TEXT.__unwind_info: 0x968 sha256:a879ee5e55bdbda35f9c798b0761659d4e34fcc996ef1eb8e71c88501a90ac28
+  __TEXT.__eh_frame: 0x48 sha256:2f28c5b5a87d8b547c59c5538a0cf88bfdac5b9ba2f584640fdc3d54a4656ecb
+  __TEXT.__auth_stubs: 0x0
+  __DATA_CONST.__const: 0x118 sha256:3d0a3f95f39c4f81a2baed266ede29ff08c59159834dc00db0c8ce38a5141bfd
+  __DATA_CONST.__got: 0x0
+  __AUTH_CONST.__const: 0xd8 sha256:c9fed8f150fb0c518aa5d2360696daec80afa30dc5f09659c29cb8595d09a393
+  __AUTH_CONST.__cfstring: 0x20 sha256:6cfc98e309b9a97bd24be092423de18ec0ad566ed0352595269f568d28d04db9
   __AUTH_CONST.__auth_got: 0x698 sha256:2c1ba820624d828583e4fb518e3399bfa987f6c161d7749fad46a2ef2f5d8711
-  __AUTH_CONST.__const: 0xd8 sha256:940072c8b62f070d88a342bddd534bf2719d2bd21730acf1e2c8bafe948d4585
-  __AUTH_CONST.__cfstring: 0x20 sha256:af6fb382423a9387b6c40d816fb3837b74930b508753b74ecba5b05a382db20f
-  __DATA.__data: 0x10 sha256:eba956dc8f5e792f083beb1e308446a00c07f6a663aebe3d3d7ecc6936d4a6ab
-  __DATA.__bss: 0x8 sha256:af5570f5a1810b7af78caf4bc70a660f0df51e42baf91d4de5b2328de0e83dfc
+  __DATA_DIRTY.__data: 0x10 sha256:eba956dc8f5e792f083beb1e308446a00c07f6a663aebe3d3d7ecc6936d4a6ab
+  __DATA_DIRTY.__bss: 0x8 sha256:af5570f5a1810b7af78caf4bc70a660f0df51e42baf91d4de5b2328de0e83dfc
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libbz2.1.0.dylib
   - /usr/lib/libcompression.dylib
   - /usr/lib/liblzma.5.dylib
-  UUID: 22CBF2A6-C4F2-3E6E-A1CB-9FD047C1B576
-  Functions: 753
-  Symbols:   1667
-  CStrings:  2246
+  UUID: 194A8F5C-7E0B-33C6-803F-08C68A8940D7
+  Functions: 757
+  Symbols:   1674
+  CStrings:  2261
 
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
- _OUTLINED_FUNCTION_1
- _OUTLINED_FUNCTION_2
- _pthread_cond_broadcast
- _realloc
- _reallocToFit
CStrings:
+ "  Compression: %s\n"
+ "  compression: %s\n"
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
