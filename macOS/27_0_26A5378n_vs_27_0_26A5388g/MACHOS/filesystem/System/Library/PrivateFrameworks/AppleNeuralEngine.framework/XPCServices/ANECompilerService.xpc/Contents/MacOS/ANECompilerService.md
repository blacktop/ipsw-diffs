## ANECompilerService

> `/System/Library/PrivateFrameworks/AppleNeuralEngine.framework/XPCServices/ANECompilerService.xpc/Contents/MacOS/ANECompilerService`

### Sections with Same Size but Changed Content

- `__DATA_CONST.__const`
- `__DATA_CONST.__objc_classlist`
- `__DATA_CONST.__objc_protolist`
- `__DATA_CONST.__objc_protorefs`
- `__DATA_CONST.__objc_superrefs`
- `__DATA_CONST.__objc_intobj`
- `__DATA_CONST.__got`
- `__DATA.__objc_const`
- `__DATA.__objc_data`

```diff

-382.11.1.0.0
-  __TEXT.__text: 0x1a970
-  __TEXT.__auth_stubs: 0x650
-  __TEXT.__objc_stubs: 0x21a0
-  __TEXT.__objc_methlist: 0x95c
-  __TEXT.__const: 0x110
-  __TEXT.__cstring: 0x12d5
-  __TEXT.__oslogstring: 0x21f5
+382.12.0.0.0
+  __TEXT.__text: 0x1b3b8
+  __TEXT.__auth_stubs: 0x670
+  __TEXT.__objc_stubs: 0x2200
+  __TEXT.__objc_methlist: 0x974
+  __TEXT.__const: 0x120
+  __TEXT.__cstring: 0x12f7
+  __TEXT.__oslogstring: 0x2359
   __TEXT.__objc_classname: 0x19e
-  __TEXT.__objc_methname: 0x24c0
-  __TEXT.__objc_methtype: 0x601
-  __TEXT.__gcc_except_tab: 0x1270
-  __TEXT.__unwind_info: 0x458
+  __TEXT.__objc_methname: 0x2534
+  __TEXT.__objc_methtype: 0x615
+  __TEXT.__gcc_except_tab: 0x12a8
+  __TEXT.__unwind_info: 0x460
   __DATA_CONST.__const: 0x380
-  __DATA_CONST.__cfstring: 0x18e0
+  __DATA_CONST.__cfstring: 0x1920
   __DATA_CONST.__objc_classlist: 0x80
   __DATA_CONST.__objc_catlist: 0x8
   __DATA_CONST.__objc_protolist: 0x28

   __DATA_CONST.__objc_protorefs: 0x10
   __DATA_CONST.__objc_superrefs: 0x20
   __DATA_CONST.__objc_intobj: 0x90
-  __DATA_CONST.__auth_got: 0x340
+  __DATA_CONST.__auth_got: 0x350
   __DATA_CONST.__got: 0x1b8
   __DATA.__objc_const: 0xd20
-  __DATA.__objc_selrefs: 0xa58
+  __DATA.__objc_selrefs: 0xa70
   __DATA.__objc_ivar: 0x24
   __DATA.__objc_data: 0x500
-  __DATA.__data: 0x3f0
+  __DATA.__data: 0x3f8
   __DATA.__bss: 0x88
   - /System/Library/Frameworks/CoreFoundation.framework/Versions/A/CoreFoundation
   - /System/Library/Frameworks/Foundation.framework/Versions/C/Foundation

   - /usr/lib/libcompression.dylib
   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libsandbox.1.dylib
-  Functions: 322
-  Symbols:   931
-  CStrings:  860
+  Functions: 326
+  Symbols:   939
+  CStrings:  871
 
Symbols:
+ +[_ANEStorageHelper isPath:safelyWithinDirectory:]
+ -[_ANEModelCacheManager scanAllPartitionsForModel:csIdentity:expunge:allowProcessModelShare:]
+ /AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.WvyX5Z/Binaries/AppleNeuralEngine_CompilerService/install/TempContent/Objects/AppleNeuralEngine.build/ANECompilerService.build/DerivedSources/
+ /AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.WvyX5Z/Binaries/AppleNeuralEngine_CompilerService/install/TempContent/Objects/AppleNeuralEngine.build/ANECompilerService.build/Objects-normal/arm64e/ANECompilerService_vers.o
+ /AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.WvyX5Z/Binaries/AppleNeuralEngine_CompilerService/install/TempContent/Objects/AppleNeuralEngine.build/ANECompilerService.build/Objects-normal/arm64e/NSFileManager+ANE.o
+ /AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.WvyX5Z/Binaries/AppleNeuralEngine_CompilerService/install/TempContent/Objects/AppleNeuralEngine.build/ANECompilerService.build/Objects-normal/arm64e/_ANECVAIRCompiler.o
+ /AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.WvyX5Z/Binaries/AppleNeuralEngine_CompilerService/install/TempContent/Objects/AppleNeuralEngine.build/ANECompilerService.build/Objects-normal/arm64e/_ANECompiler.o
+ /AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.WvyX5Z/Binaries/AppleNeuralEngine_CompilerService/install/TempContent/Objects/AppleNeuralEngine.build/ANECompilerService.build/Objects-normal/arm64e/_ANECompilerService.o
+ /AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.WvyX5Z/Binaries/AppleNeuralEngine_CompilerService/install/TempContent/Objects/AppleNeuralEngine.build/ANECompilerService.build/Objects-normal/arm64e/_ANECoreMLModelCompiler.o
+ /AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.WvyX5Z/Binaries/AppleNeuralEngine_CompilerService/install/TempContent/Objects/AppleNeuralEngine.build/ANECompilerService.build/Objects-normal/arm64e/_ANEDebugUtils.o
+ /AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.WvyX5Z/Binaries/AppleNeuralEngine_CompilerService/install/TempContent/Objects/AppleNeuralEngine.build/ANECompilerService.build/Objects-normal/arm64e/_ANEEspressoIRTranslator.o
+ /AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.WvyX5Z/Binaries/AppleNeuralEngine_CompilerService/install/TempContent/Objects/AppleNeuralEngine.build/ANECompilerService.build/Objects-normal/arm64e/_ANEInMemoryModelCacheManager.o
+ /AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.WvyX5Z/Binaries/AppleNeuralEngine_CompilerService/install/TempContent/Objects/AppleNeuralEngine.build/ANECompilerService.build/Objects-normal/arm64e/_ANEMILCompiler.o
+ /AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.WvyX5Z/Binaries/AppleNeuralEngine_CompilerService/install/TempContent/Objects/AppleNeuralEngine.build/ANECompilerService.build/Objects-normal/arm64e/_ANEMLIRCompiler.o
+ /AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.WvyX5Z/Binaries/AppleNeuralEngine_CompilerService/install/TempContent/Objects/AppleNeuralEngine.build/ANECompilerService.build/Objects-normal/arm64e/_ANEModelCacheManager.o
+ /AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.WvyX5Z/Binaries/AppleNeuralEngine_CompilerService/install/TempContent/Objects/AppleNeuralEngine.build/ANECompilerService.build/Objects-normal/arm64e/_ANEOptionKeys.o
+ /AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.WvyX5Z/Binaries/AppleNeuralEngine_CompilerService/install/TempContent/Objects/AppleNeuralEngine.build/ANECompilerService.build/Objects-normal/arm64e/_ANEPatchManager.o
+ /AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.WvyX5Z/Binaries/AppleNeuralEngine_CompilerService/install/TempContent/Objects/AppleNeuralEngine.build/ANECompilerService.build/Objects-normal/arm64e/_ANESandboxingHelper.o
+ /AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.WvyX5Z/Binaries/AppleNeuralEngine_CompilerService/install/TempContent/Objects/AppleNeuralEngine.build/ANECompilerService.build/Objects-normal/arm64e/_ANEStorageHelper.o
+ /AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.WvyX5Z/Binaries/AppleNeuralEngine_CompilerService/install/TempContent/Objects/AppleNeuralEngine.build/ANECompilerService.build/Objects-normal/arm64e/_ANETask.o
+ /AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.WvyX5Z/Binaries/AppleNeuralEngine_CompilerService/install/TempContent/Objects/AppleNeuralEngine.build/ANECompilerService.build/Objects-normal/arm64e/main.o
+ /AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.WvyX5Z/Sources/AppleNeuralEngine_CompilerService/ANECompilerService/
+ /AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.WvyX5Z/Sources/AppleNeuralEngine_CompilerService/Common/
+ /AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.WvyX5Z/Sources/AppleNeuralEngine_CompilerService/aned/
+ ___93-[_ANEModelCacheManager scanAllPartitionsForModel:csIdentity:expunge:allowProcessModelShare:]_block_invoke
+ ___block_descriptor_156_e8_32s40s48s56s64s72s80s88s96s104bs112r_e5_v8?0l
+ ___copy_helper_block_e8_32s40s48s56s64s72s80s88s96s104b112r
+ ___destroy_helper_block_e8_32s40s48s56s64s72s80s88s96s104s112r
+ __os_log_fault_impl
+ _kANEDCompilerQoSHintKey
+ _objc_msgSend$isPath:safelyWithinDirectory:
+ _objc_msgSend$scanAllPartitionsForModel:csIdentity:expunge:allowProcessModelShare:
+ _objc_msgSend$unsignedIntValue
+ _qos_class_self
- /AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.XAT1Ga/Binaries/AppleNeuralEngine_CompilerService/install/TempContent/Objects/AppleNeuralEngine.build/ANECompilerService.build/DerivedSources/
- /AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.XAT1Ga/Binaries/AppleNeuralEngine_CompilerService/install/TempContent/Objects/AppleNeuralEngine.build/ANECompilerService.build/Objects-normal/arm64e/ANECompilerService_vers.o
- /AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.XAT1Ga/Binaries/AppleNeuralEngine_CompilerService/install/TempContent/Objects/AppleNeuralEngine.build/ANECompilerService.build/Objects-normal/arm64e/NSFileManager+ANE.o
- /AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.XAT1Ga/Binaries/AppleNeuralEngine_CompilerService/install/TempContent/Objects/AppleNeuralEngine.build/ANECompilerService.build/Objects-normal/arm64e/_ANECVAIRCompiler.o
- /AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.XAT1Ga/Binaries/AppleNeuralEngine_CompilerService/install/TempContent/Objects/AppleNeuralEngine.build/ANECompilerService.build/Objects-normal/arm64e/_ANECompiler.o
- /AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.XAT1Ga/Binaries/AppleNeuralEngine_CompilerService/install/TempContent/Objects/AppleNeuralEngine.build/ANECompilerService.build/Objects-normal/arm64e/_ANECompilerService.o
- /AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.XAT1Ga/Binaries/AppleNeuralEngine_CompilerService/install/TempContent/Objects/AppleNeuralEngine.build/ANECompilerService.build/Objects-normal/arm64e/_ANECoreMLModelCompiler.o
- /AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.XAT1Ga/Binaries/AppleNeuralEngine_CompilerService/install/TempContent/Objects/AppleNeuralEngine.build/ANECompilerService.build/Objects-normal/arm64e/_ANEDebugUtils.o
- /AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.XAT1Ga/Binaries/AppleNeuralEngine_CompilerService/install/TempContent/Objects/AppleNeuralEngine.build/ANECompilerService.build/Objects-normal/arm64e/_ANEEspressoIRTranslator.o
- /AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.XAT1Ga/Binaries/AppleNeuralEngine_CompilerService/install/TempContent/Objects/AppleNeuralEngine.build/ANECompilerService.build/Objects-normal/arm64e/_ANEInMemoryModelCacheManager.o
- /AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.XAT1Ga/Binaries/AppleNeuralEngine_CompilerService/install/TempContent/Objects/AppleNeuralEngine.build/ANECompilerService.build/Objects-normal/arm64e/_ANEMILCompiler.o
- /AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.XAT1Ga/Binaries/AppleNeuralEngine_CompilerService/install/TempContent/Objects/AppleNeuralEngine.build/ANECompilerService.build/Objects-normal/arm64e/_ANEMLIRCompiler.o
- /AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.XAT1Ga/Binaries/AppleNeuralEngine_CompilerService/install/TempContent/Objects/AppleNeuralEngine.build/ANECompilerService.build/Objects-normal/arm64e/_ANEModelCacheManager.o
- /AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.XAT1Ga/Binaries/AppleNeuralEngine_CompilerService/install/TempContent/Objects/AppleNeuralEngine.build/ANECompilerService.build/Objects-normal/arm64e/_ANEOptionKeys.o
- /AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.XAT1Ga/Binaries/AppleNeuralEngine_CompilerService/install/TempContent/Objects/AppleNeuralEngine.build/ANECompilerService.build/Objects-normal/arm64e/_ANEPatchManager.o
- /AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.XAT1Ga/Binaries/AppleNeuralEngine_CompilerService/install/TempContent/Objects/AppleNeuralEngine.build/ANECompilerService.build/Objects-normal/arm64e/_ANESandboxingHelper.o
- /AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.XAT1Ga/Binaries/AppleNeuralEngine_CompilerService/install/TempContent/Objects/AppleNeuralEngine.build/ANECompilerService.build/Objects-normal/arm64e/_ANEStorageHelper.o
- /AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.XAT1Ga/Binaries/AppleNeuralEngine_CompilerService/install/TempContent/Objects/AppleNeuralEngine.build/ANECompilerService.build/Objects-normal/arm64e/_ANETask.o
- /AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.XAT1Ga/Binaries/AppleNeuralEngine_CompilerService/install/TempContent/Objects/AppleNeuralEngine.build/ANECompilerService.build/Objects-normal/arm64e/main.o
- /AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.XAT1Ga/Sources/AppleNeuralEngine_CompilerService/ANECompilerService/
- /AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.XAT1Ga/Sources/AppleNeuralEngine_CompilerService/Common/
- /AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.XAT1Ga/Sources/AppleNeuralEngine_CompilerService/aned/
- ___70-[_ANEModelCacheManager scanAllPartitionsForModel:csIdentity:expunge:]_block_invoke
- ___block_descriptor_136_e8_32s40s48s56s64s72s80s88s96bs104r_e5_v8?0l
- ___copy_helper_block_e8_32s40s48s56s64s72s80s88s96b104r
- ___destroy_helper_block_e8_32s40s48s56s64s72s80s88s96s104r
CStrings:
+ "%@: refusing expunge with allowProcessModelShare — would purge shared-bucket models on behalf of an unrelated csIdentity"
+ "%u qos:%u model.string_id:%llu csIdentity:%{public}@"
+ "<private>"
+ "ANECompilerService QoS: model.string_id=%llu clientQos=%u threadQos=%u"
+ "B40@0:8@16@24B32B36"
+ "_ANEC_ESPRESSO_TRANSLATE"
+ "_ANEC_QUEUE_WAIT"
+ "csIdentity:%{public}@ status:%u durationMs:%f"
+ "isPath:safelyWithinDirectory:"
+ "kANEDCompilerQoSHintKey"
+ "qos:%u model.string_id:%llu name:%{public}@ csIdentity:%{public}@"
+ "scanAllPartitionsForModel:csIdentity:expunge:allowProcessModelShare:"
+ "unsignedIntValue"
- "%u model.string_id:%llu"
- "model.string_id:%llu"
```
