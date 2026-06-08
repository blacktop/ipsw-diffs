## libAppleArchive.dylib

> `/usr/lib/libAppleArchive.dylib`

```diff

-450.100.4.0.0
-  __TEXT.__text: 0x82d0c
-  __TEXT.__auth_stubs: 0xf20
-  __TEXT.__cstring: 0x13278
-  __TEXT.__const: 0x960
+462.0.0.0.0
+  __TEXT.__text: 0x832a8
+  __TEXT.__cstring: 0x13398
+  __TEXT.__const: 0x920
   __TEXT.__oslogstring: 0x31
-  __TEXT.__unwind_info: 0xd38
+  __TEXT.__unwind_info: 0xd78
   __TEXT.__eh_frame: 0x48
-  __DATA_CONST.__got: 0xa0
+  __TEXT.__auth_stubs: 0x0
   __DATA_CONST.__const: 0x158
-  __AUTH_CONST.__auth_got: 0x790
+  __DATA_CONST.__got: 0x0
   __AUTH_CONST.__const: 0x80
   __AUTH_CONST.__cfstring: 0x40
+  __AUTH_CONST.__auth_got: 0x790
   __DATA_DIRTY.__data: 0x10
   __DATA_DIRTY.__bss: 0x8
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
