## libParallelCompression.dylib

> `/usr/lib/libParallelCompression.dylib`

```diff

-450.100.4.0.0
-  __TEXT.__text: 0x54e78
-  __TEXT.__auth_stubs: 0xd30
-  __TEXT.__cstring: 0xf447
-  __TEXT.__const: 0x850
+462.0.0.0.0
+  __TEXT.__text: 0x55c14
+  __TEXT.__cstring: 0xf55e
+  __TEXT.__const: 0x830
   __TEXT.__oslogstring: 0x31
-  __TEXT.__unwind_info: 0x948
+  __TEXT.__unwind_info: 0x968
   __TEXT.__eh_frame: 0x48
-  __DATA_CONST.__got: 0x38
+  __TEXT.__auth_stubs: 0x0
   __DATA_CONST.__const: 0x118
-  __AUTH_CONST.__auth_got: 0x698
+  __DATA_CONST.__got: 0x0
   __AUTH_CONST.__const: 0xd8
   __AUTH_CONST.__cfstring: 0x20
-  __DATA.__data: 0x10
-  __DATA.__bss: 0x8
+  __AUTH_CONST.__auth_got: 0x698
+  __DATA_DIRTY.__data: 0x10
+  __DATA_DIRTY.__bss: 0x8
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
