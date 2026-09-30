## aned

> `/usr/libexec/aned`

### Sections with Same Size but Changed Content

- `__DATA_CONST.__const`
- `__DATA_CONST.__objc_classlist`
- `__DATA_CONST.__objc_protolist`
- `__DATA_CONST.__objc_protorefs`
- `__DATA_CONST.__objc_superrefs`
- `__DATA_CONST.__objc_intobj`
- `__DATA_CONST.__auth_ptr`
- `__DATA.__objc_data`
- `__DATA.__data`

```diff

-382.11.1.0.0
-  __TEXT.__text: 0x69b0c
-  __TEXT.__auth_stubs: 0xd30
-  __TEXT.__objc_stubs: 0x3200
-  __TEXT.__objc_methlist: 0x10ec
-  __TEXT.__const: 0x5cec
-  __TEXT.__gcc_except_tab: 0x4b70
-  __TEXT.__cstring: 0x5ac8
-  __TEXT.__oslogstring: 0x6579
+382.12.0.0.0
+  __TEXT.__text: 0x6af20
+  __TEXT.__auth_stubs: 0xd40
+  __TEXT.__objc_stubs: 0x3300
+  __TEXT.__objc_methlist: 0x1124
+  __TEXT.__const: 0x5d0c
+  __TEXT.__gcc_except_tab: 0x4d00
+  __TEXT.__cstring: 0x5b68
+  __TEXT.__oslogstring: 0x67a5
   __TEXT.__objc_classname: 0x22f
-  __TEXT.__objc_methname: 0x3b48
-  __TEXT.__objc_methtype: 0xdad
-  __TEXT.__unwind_info: 0x17e0
+  __TEXT.__objc_methname: 0x3c83
+  __TEXT.__objc_methtype: 0xdd2
+  __TEXT.__unwind_info: 0x17f0
   __DATA_CONST.__const: 0x2778
-  __DATA_CONST.__cfstring: 0x9c0
+  __DATA_CONST.__cfstring: 0xaa0
   __DATA_CONST.__objc_classlist: 0x88
   __DATA_CONST.__objc_protolist: 0x60
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_protorefs: 0x10
   __DATA_CONST.__objc_superrefs: 0x60
   __DATA_CONST.__objc_intobj: 0x18
-  __DATA_CONST.__auth_got: 0x6b0
-  __DATA_CONST.__got: 0x398
+  __DATA_CONST.__auth_got: 0x6b8
+  __DATA_CONST.__got: 0x3a0
   __DATA_CONST.__auth_ptr: 0x18
-  __DATA.__objc_const: 0x1be8
-  __DATA.__objc_selrefs: 0xf20
-  __DATA.__objc_ivar: 0xe4
+  __DATA.__objc_const: 0x1c18
+  __DATA.__objc_selrefs: 0xf60
+  __DATA.__objc_ivar: 0xe8
   __DATA.__objc_data: 0x550
   __DATA.__data: 0x490
   __DATA.__bss: 0x88

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libc++.1.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 2445
-  Symbols:   3644
-  CStrings:  1690
+  Functions: 2452
+  Symbols:   3660
+  CStrings:  1713
 
Symbols:
+ +[_ANEStorageHelper isPath:safelyWithinDirectory:]
+ -[_ANEModelCacheManager scanAllPartitionsForModel:csIdentity:expunge:allowProcessModelShare:]
+ -[_ANEServer processNameForServiceUUID:]
+ -[_ANEServer selectCompilerService:isE5ML:qos:]
+ -[_ANEServer uuidANECompilerServiceBackground]
+ /AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.qpEGEH/Binaries/AppleNeuralEngine/install/TempContent/Objects/AppleNeuralEngine.build/aned.build/DerivedSources/
+ /AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.qpEGEH/Binaries/AppleNeuralEngine/install/TempContent/Objects/AppleNeuralEngine.build/aned.build/Objects-normal/arm64e/_ANEInMemoryModelCacheManager.o
+ /AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.qpEGEH/Binaries/AppleNeuralEngine/install/TempContent/Objects/AppleNeuralEngine.build/aned.build/Objects-normal/arm64e/_ANEMachoPatcher.o
+ /AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.qpEGEH/Binaries/AppleNeuralEngine/install/TempContent/Objects/AppleNeuralEngine.build/aned.build/Objects-normal/arm64e/_ANEModelCacheManager.o
+ /AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.qpEGEH/Binaries/AppleNeuralEngine/install/TempContent/Objects/AppleNeuralEngine.build/aned.build/Objects-normal/arm64e/_ANEPatchConfiguration.o
+ /AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.qpEGEH/Binaries/AppleNeuralEngine/install/TempContent/Objects/AppleNeuralEngine.build/aned.build/Objects-normal/arm64e/_ANEPatchManager.o
+ /AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.qpEGEH/Binaries/AppleNeuralEngine/install/TempContent/Objects/AppleNeuralEngine.build/aned.build/Objects-normal/arm64e/_ANEProgramCache.o
+ /AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.qpEGEH/Binaries/AppleNeuralEngine/install/TempContent/Objects/AppleNeuralEngine.build/aned.build/Objects-normal/arm64e/_ANEProgramCacheKey.o
+ /AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.qpEGEH/Binaries/AppleNeuralEngine/install/TempContent/Objects/AppleNeuralEngine.build/aned.build/Objects-normal/arm64e/_ANEProgramForLoad.o
+ /AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.qpEGEH/Binaries/AppleNeuralEngine/install/TempContent/Objects/AppleNeuralEngine.build/aned.build/Objects-normal/arm64e/_ANEServer.o
+ /AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.qpEGEH/Binaries/AppleNeuralEngine/install/TempContent/Objects/AppleNeuralEngine.build/aned.build/Objects-normal/arm64e/_ANEStorageHelper.o
+ /AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.qpEGEH/Binaries/AppleNeuralEngine/install/TempContent/Objects/AppleNeuralEngine.build/aned.build/Objects-normal/arm64e/_ANETask.o
+ /AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.qpEGEH/Binaries/AppleNeuralEngine/install/TempContent/Objects/AppleNeuralEngine.build/aned.build/Objects-normal/arm64e/_ANETemporaryFilesHandler.o
+ /AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.qpEGEH/Binaries/AppleNeuralEngine/install/TempContent/Objects/AppleNeuralEngine.build/aned.build/Objects-normal/arm64e/_ANETensorDebug.o
+ /AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.qpEGEH/Binaries/AppleNeuralEngine/install/TempContent/Objects/AppleNeuralEngine.build/aned.build/Objects-normal/arm64e/_ANEXPCServiceHelper.o
+ /AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.qpEGEH/Binaries/AppleNeuralEngine/install/TempContent/Objects/AppleNeuralEngine.build/aned.build/Objects-normal/arm64e/aned.o
+ /AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.qpEGEH/Binaries/AppleNeuralEngine/install/TempContent/Objects/AppleNeuralEngine.build/aned.build/Objects-normal/arm64e/aned_vers.o
+ /AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.qpEGEH/Sources/AppleNeuralEngine/Common/
+ /AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.qpEGEH/Sources/AppleNeuralEngine/aned/
+ GCC_except_table62
+ GCC_except_table65
+ OBJC_IVAR_$__ANEServer._uuidANECompilerServiceBackground
+ ___93-[_ANEModelCacheManager scanAllPartitionsForModel:csIdentity:expunge:allowProcessModelShare:]_block_invoke
+ ___block_descriptor_80_ea8_32s40s48r56r64r_e37_v28?0B8"NSDictionary"12"NSError"20l
+ ___copy_helper_block_ea8_32s40s48r56r64r
+ ___destroy_helper_block_ea8_32s40s48r56r64r
+ _kANEDCompilerQoSHintKey
+ _objc_msgSend$UUIDString
+ _objc_msgSend$allowProcessModelShareFor:
+ _objc_msgSend$containsObject:
+ _objc_msgSend$hasSuffix:
+ _objc_msgSend$isPath:safelyWithinDirectory:
+ _objc_msgSend$processNameForServiceUUID:
+ _objc_msgSend$scanAllPartitionsForModel:csIdentity:expunge:allowProcessModelShare:
+ _objc_msgSend$selectCompilerService:isE5ML:qos:
+ _qos_class_self
- /AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.E3DRpu/Binaries/AppleNeuralEngine/install/TempContent/Objects/AppleNeuralEngine.build/aned.build/DerivedSources/
- /AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.E3DRpu/Binaries/AppleNeuralEngine/install/TempContent/Objects/AppleNeuralEngine.build/aned.build/Objects-normal/arm64e/_ANEInMemoryModelCacheManager.o
- /AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.E3DRpu/Binaries/AppleNeuralEngine/install/TempContent/Objects/AppleNeuralEngine.build/aned.build/Objects-normal/arm64e/_ANEMachoPatcher.o
- /AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.E3DRpu/Binaries/AppleNeuralEngine/install/TempContent/Objects/AppleNeuralEngine.build/aned.build/Objects-normal/arm64e/_ANEModelCacheManager.o
- /AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.E3DRpu/Binaries/AppleNeuralEngine/install/TempContent/Objects/AppleNeuralEngine.build/aned.build/Objects-normal/arm64e/_ANEPatchConfiguration.o
- /AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.E3DRpu/Binaries/AppleNeuralEngine/install/TempContent/Objects/AppleNeuralEngine.build/aned.build/Objects-normal/arm64e/_ANEPatchManager.o
- /AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.E3DRpu/Binaries/AppleNeuralEngine/install/TempContent/Objects/AppleNeuralEngine.build/aned.build/Objects-normal/arm64e/_ANEProgramCache.o
- /AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.E3DRpu/Binaries/AppleNeuralEngine/install/TempContent/Objects/AppleNeuralEngine.build/aned.build/Objects-normal/arm64e/_ANEProgramCacheKey.o
- /AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.E3DRpu/Binaries/AppleNeuralEngine/install/TempContent/Objects/AppleNeuralEngine.build/aned.build/Objects-normal/arm64e/_ANEProgramForLoad.o
- /AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.E3DRpu/Binaries/AppleNeuralEngine/install/TempContent/Objects/AppleNeuralEngine.build/aned.build/Objects-normal/arm64e/_ANEServer.o
- /AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.E3DRpu/Binaries/AppleNeuralEngine/install/TempContent/Objects/AppleNeuralEngine.build/aned.build/Objects-normal/arm64e/_ANEStorageHelper.o
- /AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.E3DRpu/Binaries/AppleNeuralEngine/install/TempContent/Objects/AppleNeuralEngine.build/aned.build/Objects-normal/arm64e/_ANETask.o
- /AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.E3DRpu/Binaries/AppleNeuralEngine/install/TempContent/Objects/AppleNeuralEngine.build/aned.build/Objects-normal/arm64e/_ANETemporaryFilesHandler.o
- /AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.E3DRpu/Binaries/AppleNeuralEngine/install/TempContent/Objects/AppleNeuralEngine.build/aned.build/Objects-normal/arm64e/_ANETensorDebug.o
- /AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.E3DRpu/Binaries/AppleNeuralEngine/install/TempContent/Objects/AppleNeuralEngine.build/aned.build/Objects-normal/arm64e/_ANEXPCServiceHelper.o
- /AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.E3DRpu/Binaries/AppleNeuralEngine/install/TempContent/Objects/AppleNeuralEngine.build/aned.build/Objects-normal/arm64e/aned.o
- /AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.E3DRpu/Binaries/AppleNeuralEngine/install/TempContent/Objects/AppleNeuralEngine.build/aned.build/Objects-normal/arm64e/aned_vers.o
- /AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.E3DRpu/Sources/AppleNeuralEngine/Common/
- /AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.E3DRpu/Sources/AppleNeuralEngine/aned/
- GCC_except_table60
- GCC_except_table63
- ___70-[_ANEModelCacheManager scanAllPartitionsForModel:csIdentity:expunge:]_block_invoke
- ___block_descriptor_72_ea8_32s40r48r56r_e37_v28?0B8"NSDictionary"12"NSError"20l
- ___copy_helper_block_ea8_32s40r48r56r
- ___destroy_helper_block_ea8_32s40r48r56r
CStrings:
+ "%@: refusing expunge with allowProcessModelShare — would purge shared-bucket models on behalf of an unrelated csIdentity"
+ "%@|%@"
+ "%u %u model.string_id:%llu csIdentity:%{public}@"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.qpEGEH/Sources/AppleNeuralEngine/ext/polymer/anecommon/ane_loader/ZinComputeProgramLoader.cpp"
+ "@28@0:8B16B20I24"
+ "ANED QoS: model.string_id=%llu clientQos=%u threadQos=%u proc=%{public}@"
+ "B40@0:8@16@24B32B36"
+ "T@\"NSUUID\",R,N,V_uuidANECompilerServiceBackground"
+ "UUIDString"
+ "_ANED_COMPILE_CACHE_HIT"
+ "_ANED_COMPILE_CACHE_MISS"
+ "_ANED_COMPILE_XPC"
+ "_ANED_LOAD_SEMA_WAIT"
+ "_ANED_PREP_CHAIN_SEMA_WAIT"
+ "_ANED_UNLOAD_SEMA_WAIT"
+ "_uuidANECompilerServiceBackground"
+ "containsObject:"
+ "hasSuffix:"
+ "isPath:safelyWithinDirectory:"
+ "loadWaitTime"
+ "model.string_id:%llu csIdentity:%{public}@ status:%u"
+ "processNameForServiceUUID:"
+ "qos"
+ "qos:%u csIdentity:%{public}@ status:%u"
+ "qos:%u model.string_id:%llu"
+ "qos:%u model.string_id:%llu cacheURLIdentifier:%{public}@ csIdentity:%{public}@"
+ "qos:%u model.string_id:%llu cachedModel.length:%lu wiredMemory:%lu csIdentity:%{public}@"
+ "qos:%u model.string_id:%llu csIdentity:%{public}@"
+ "qos:%u model.string_id:%llu csIdentity:%{public}@ status:%u"
+ "qos:%u model.string_id:%llu numInputs:%u numOutputs:%u csIdentity:%{public}@"
+ "qos:%u model.string_id:%llu wiredMemory:%lu csIdentity:%{public}@"
+ "qos:%u qIdx:%lu model.string_id:%llu csIdentity:%{public}@ timedOut:%u"
+ "scanAllPartitionsForModel:csIdentity:expunge:allowProcessModelShare:"
+ "selectCompilerService:isE5ML:qos:"
+ "uuidANECompilerServiceBackground"
- "%u %u model.string_id:%llu"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.E3DRpu/Sources/AppleNeuralEngine/ext/polymer/anecommon/ane_loader/ZinComputeProgramLoader.cpp"
- "Using ANELargeModelCompilerService (modelType=%{public}@)"
- "Using primary (regular) ANECompilerService"
- "Using secondary (longer duration) ANECompilerService"
- "model.string_id:%llu status:%u"
- "qos:%u"
- "qos:%u model.string_id:%llu cachedModel.length:%lu wiredMemory:%lu"
- "qos:%u model.string_id:%llu numInputs:%u numOutputs:%u"
- "qos:%u model.string_id:%llu status:%u"
- "qos:%u model.string_id:%llu wiredMemory:%lu"
- "qos:%u status:%u"
```
