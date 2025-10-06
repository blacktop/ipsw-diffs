## CoreRE

> `/System/Library/PrivateFrameworks/CoreRE.framework/CoreRE`

```diff

-403.40.3.502.1
-  __TEXT.__text: 0x13d63f4
+403.40.6.0.0
+  __TEXT.__text: 0x13d64e8
   __TEXT.__auth_stubs: 0x6b10
   __TEXT.__objc_methlist: 0x3d60
   __TEXT.__const: 0xdba70

   __TEXT.__swift5_fieldmd: 0x44
   __TEXT.__swift5_reflstr: 0x1f
   __TEXT.__swift5_types: 0x8
-  __TEXT.__cstring: 0x99870
-  __TEXT.__gcc_except_tab: 0xd9cc
-  __TEXT.__oslogstring: 0x482b2
+  __TEXT.__cstring: 0x99857
+  __TEXT.__gcc_except_tab: 0xda18
+  __TEXT.__oslogstring: 0x4829b
   __TEXT.__ustring: 0x1a
   __TEXT.__dlopen_cstrs: 0xb0
-  __TEXT.__unwind_info: 0x5a88
+  __TEXT.__unwind_info: 0x5aa0
   __TEXT.__objc_classname: 0x7ad
   __TEXT.__objc_methname: 0x1024d
   __TEXT.__objc_methtype: 0xa078

   __AUTH.__thread_vars: 0xc0
   __AUTH.__thread_bss: 0x310
   __DATA.__objc_ivar: 0x3d4
-  __DATA.__data: 0x22ab0
-  __DATA.__bss: 0x7140
-  __DATA.__common: 0x56f0
+  __DATA.__data: 0x22aa0
+  __DATA.__bss: 0x4160
+  __DATA.__common: 0x56a0
   __DATA_DIRTY.__objc_ivar: 0x110
   __DATA_DIRTY.__objc_data: 0x5f0
   __DATA_DIRTY.__data: 0x3348
-  __DATA_DIRTY.__bss: 0x39648
-  __DATA_DIRTY.__common: 0x3768
+  __DATA_DIRTY.__bss: 0x3c638
+  __DATA_DIRTY.__common: 0x37b8
   - /System/Library/Frameworks/AVFAudio.framework/AVFAudio
   - /System/Library/Frameworks/AVFoundation.framework/AVFoundation
   - /System/Library/Frameworks/Accelerate.framework/Accelerate

   - /usr/lib/swift/libswift_Builtin_float.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  UUID: 446E37D4-23B5-33D4-8815-5E440BBB2B48
-  Functions: 73705
-  Symbols:   182415
-  CStrings:  23889
+  UUID: 8B0F3C7A-965A-336A-8FF9-368D4C665BB1
+  Functions: 73708
+  Symbols:   182423
+  CStrings:  23887
 
Symbols:
+ _.memset_pattern.74
+ __ZN2re4ecs232ImagePresentationComponentHelper4impl24isPresentingSpatialImageEPKNS0_6EntityE
+ __ZNK2re20AudioFileAssetLoader31readAudioFileAssetIntoPCMBufferEPKNS_14AudioFileAssetE
+ __ZNK2re20AudioFileAssetLoader31serializeAssetBlobFromPCMBufferERNS_12StreamWriterEP16AVAudioPCMBuffer
+ ____ZNK2re13ShaderManager29resolveShaderCompilationQueueIZNKS0_35scheduleAsyncFuncOnCompilationQueueEbyNS_15CompilationTypeENS_8StringIDENS_8FunctionIFvvEEEE3$_0EEvbyS2_S3_S6_T__block_invoke.49
+ ____ZNK2re13ShaderManager29resolveShaderCompilationQueueIZNKS0_37scheduleGroupNotifyOnCompilationQueueEbyNS_8dispatch5GroupENS_15CompilationTypeENS_8StringIDENS_8FunctionIFvvEEEE3$_0EEvbyS4_S5_S8_T__block_invoke.57
+ ____ZNK2re13ShaderManager29resolveShaderCompilationQueueIZNKS0_40scheduleAsyncGroupFuncOnCompilationQueueEbyNS_8dispatch5GroupENS_15CompilationTypeENS_8StringIDENS_8FunctionIFvvEEEE3$_0EEvbyS4_S5_S8_T__block_invoke.65
+ ___block_descriptor_tmp.48
+ ___block_descriptor_tmp.56
+ ___block_descriptor_tmp.60
- _.memset_pattern.73
- ____ZNK2re13ShaderManager29resolveShaderCompilationQueueIZNKS0_35scheduleAsyncFuncOnCompilationQueueEbyNS_15CompilationTypeENS_8StringIDENS_8FunctionIFvvEEEE3$_0EEvbyS2_S3_S6_T__block_invoke.48
- ____ZNK2re13ShaderManager29resolveShaderCompilationQueueIZNKS0_37scheduleGroupNotifyOnCompilationQueueEbyNS_8dispatch5GroupENS_15CompilationTypeENS_8StringIDENS_8FunctionIFvvEEEE3$_0EEvbyS4_S5_S8_T__block_invoke.56
- ____ZNK2re13ShaderManager29resolveShaderCompilationQueueIZNKS0_40scheduleAsyncGroupFuncOnCompilationQueueEbyNS_8dispatch5GroupENS_15CompilationTypeENS_8StringIDENS_8FunctionIFvvEEEE3$_0EEvbyS4_S5_S8_T__block_invoke.64
- ___block_descriptor_tmp.54
- ___block_descriptor_tmp.62
- ___block_descriptor_tmp.67
CStrings:
+ "[CoreRE] [AudioFileAssetLoader] Failed to serialize asset from url. dataWithContentsOfURL does not support query items."
- "Deleting Expired Buffer %llu - currentFrame = %d, lastFrameUsed = %d \n"
- "Deleting Expired Texture %llu - currentFrame = %d, lastFrameUsed = %d \n"
- "m_mixedSpillTextureAsset"

```
