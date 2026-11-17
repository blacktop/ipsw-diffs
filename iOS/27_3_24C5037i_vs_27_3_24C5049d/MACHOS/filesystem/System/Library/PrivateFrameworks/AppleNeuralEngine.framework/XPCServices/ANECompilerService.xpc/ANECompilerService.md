## ANECompilerService

> `/System/Library/PrivateFrameworks/AppleNeuralEngine.framework/XPCServices/ANECompilerService.xpc/ANECompilerService`

### Sections with Same Size but Changed Content

- `__DATA_CONST.__objc_catlist`
- `__DATA_CONST.__objc_protolist`
- `__DATA_CONST.__objc_protorefs`
- `__DATA_CONST.__auth_ptr`
- `__DATA.__data`

```diff

-382.102.2.0.0
-  __TEXT.__text: 0x191a4
-  __TEXT.__auth_stubs: 0x890
-  __TEXT.__objc_stubs: 0x2280
-  __TEXT.__objc_methlist: 0x9ac
-  __TEXT.__const: 0x118
-  __TEXT.__cstring: 0x12e5
-  __TEXT.__oslogstring: 0x2554
-  __TEXT.__objc_classname: 0x19e
-  __TEXT.__objc_methname: 0x25fa
-  __TEXT.__objc_methtype: 0x67b
-  __TEXT.__gcc_except_tab: 0x1120
-  __TEXT.__unwind_info: 0x558
-  __DATA_CONST.__const: 0x2f8
-  __DATA_CONST.__cfstring: 0x1940
-  __DATA_CONST.__objc_classlist: 0x80
+382.200.2.0.0
+  __TEXT.__text: 0x1c528
+  __TEXT.__auth_stubs: 0x8d0
+  __TEXT.__objc_stubs: 0x2840
+  __TEXT.__objc_methlist: 0xb8c
+  __TEXT.__const: 0x130
+  __TEXT.__cstring: 0x135b
+  __TEXT.__oslogstring: 0x29d2
+  __TEXT.__objc_classname: 0x1f8
+  __TEXT.__objc_methname: 0x2b87
+  __TEXT.__objc_methtype: 0x706
+  __TEXT.__gcc_except_tab: 0x1190
+  __TEXT.__unwind_info: 0x628
+  __DATA_CONST.__const: 0x390
+  __DATA_CONST.__cfstring: 0x1a60
+  __DATA_CONST.__objc_classlist: 0xa0
   __DATA_CONST.__objc_catlist: 0x8
   __DATA_CONST.__objc_protolist: 0x28
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_protorefs: 0x10
-  __DATA_CONST.__objc_superrefs: 0x20
-  __DATA_CONST.__objc_intobj: 0x60
-  __DATA_CONST.__auth_got: 0x460
-  __DATA_CONST.__got: 0x1c0
+  __DATA_CONST.__objc_superrefs: 0x28
+  __DATA_CONST.__objc_arraydata: 0x8
+  __DATA_CONST.__objc_arrayobj: 0x18
+  __DATA_CONST.__objc_intobj: 0x78
+  __DATA_CONST.__auth_got: 0x480
+  __DATA_CONST.__got: 0x1e8
   __DATA_CONST.__auth_ptr: 0x8
-  __DATA.__objc_const: 0xd48
-  __DATA.__objc_selrefs: 0xa90
-  __DATA.__objc_ivar: 0x24
-  __DATA.__objc_data: 0x500
+  __DATA.__objc_const: 0x1088
+  __DATA.__objc_selrefs: 0xc18
+  __DATA.__objc_ivar: 0x38
+  __DATA.__objc_data: 0x640
   __DATA.__data: 0x408
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/Foundation.framework/Foundation

   - /usr/lib/libcompression.dylib
   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libsandbox.1.dylib
-  Functions: 313
-  Symbols:   959
-  CStrings:  877
+  Functions: 369
+  Symbols:   1102
+  CStrings:  976
 
Symbols:
+ +[_ANECacheMaintenance accessTimeForPath:]
+ +[_ANECacheMaintenance isPath:safelyWithinDirectory:]
+ +[_ANECacheMaintenance removeEntriesAtPath:notAccessedFor:]
+ +[_ANECacheMaintenance setAccessTime:forPath:]
+ +[_ANECacheMaintenance updateAccessTimeForPath:]
+ +[_ANECompileContentKey contentKeyForInputPath:options:modelType:]
+ +[_ANECompileContentKey inputsDigestForPath:]
+ +[_ANECompileContentKey inputsFingerprintForPath:]
+ +[_ANECompileContentKey optionsDigestForOptions:]
+ +[_ANECompileContentKey optionsToSkipList]
+ +[_ANEEquivalenceIndex churnFaultThreshold]
+ +[_ANEEquivalenceIndex serialQueue]
+ -[_ANEEquivalenceIndex .cxx_destruct]
+ -[_ANEEquivalenceIndex _loadLocked]
+ -[_ANEEquivalenceIndex _resolutionForEntry:contentKey:index:dirty:]
+ -[_ANEEquivalenceIndex _safeLeafPathForName:]
+ -[_ANEEquivalenceIndex _saveLocked:]
+ -[_ANEEquivalenceIndex evictContentKey:]
+ -[_ANEEquivalenceIndex initWithModelIdentityDirectory:]
+ -[_ANEEquivalenceIndex recordContentKey:leafName:]
+ -[_ANEEquivalenceIndex resolveContentKey:]
+ -[_ANEEquivalenceResolution .cxx_destruct]
+ -[_ANEEquivalenceResolution dupCount]
+ -[_ANEEquivalenceResolution leafName]
+ -[_ANEEquivalenceResolution leafPath]
+ -[_ANEEquivalenceResolution setDupCount:]
+ -[_ANEEquivalenceResolution setLeafName:]
+ -[_ANEEquivalenceResolution setLeafPath:]
+ -[_ANEModelCacheManager _contentKeyForModel:options:fingerprint:]
+ -[_ANEModelCacheManager _indexForModel:csIdentity:options:]
+ -[_ANEModelCacheManager effectiveBundleIDForModel:bundleID:]
+ -[_ANEModelCacheManager equivalentCompiledModelForModel:csIdentity:options:modelAttributes:contentKey:inputsFingerprint:]
+ -[_ANEModelCacheManager evictEquivalenceForModel:csIdentity:options:contentKey:]
+ -[_ANEModelCacheManager modelIdentityDirectoryForModel:bundleID:useSourceURL:]
+ -[_ANEModelCacheManager recordEquivalenceForModel:csIdentity:options:contentKey:inputsFingerprint:leafPath:]
+ /Library/Caches/com.apple.xbs/<UUID>/TemporaryDirectory.<TMP>/Binaries/AppleNeuralEngine_CompilerService/install/TempContent/Objects/AppleNeuralEngine.build/ANECompilerService.build/Objects-normal/arm64e/_ANECacheMaintenance.o
+ /Library/Caches/com.apple.xbs/<UUID>/TemporaryDirectory.<TMP>/Binaries/AppleNeuralEngine_CompilerService/install/TempContent/Objects/AppleNeuralEngine.build/ANECompilerService.build/Objects-normal/arm64e/_ANECompileContentKey.o
+ /Library/Caches/com.apple.xbs/<UUID>/TemporaryDirectory.<TMP>/Binaries/AppleNeuralEngine_CompilerService/install/TempContent/Objects/AppleNeuralEngine.build/ANECompilerService.build/Objects-normal/arm64e/_ANEEquivalenceIndex.o
+ GCC_except_table13
+ GCC_except_table19
+ GCC_except_table45
+ _ANECacheMaintenance.m
+ _ANECompileContentKey.m
+ _ANEEquivalenceIndex.m
+ _ANEStandardizedPath
+ _NSFileType
+ _NSFileTypeRegular
+ _OBJC_CLASS_$_NSConstantArray
+ _OBJC_CLASS_$_NSJSONSerialization
+ _OBJC_CLASS_$_NSUUID
+ _OBJC_CLASS_$__ANECacheMaintenance
+ _OBJC_CLASS_$__ANECompileContentKey
+ _OBJC_CLASS_$__ANEEquivalenceIndex
+ _OBJC_CLASS_$__ANEEquivalenceResolution
+ _OBJC_IVAR_$__ANEEquivalenceIndex._identityDirURL
+ _OBJC_IVAR_$__ANEEquivalenceIndex._indexPath
+ _OBJC_IVAR_$__ANEEquivalenceResolution._dupCount
+ _OBJC_IVAR_$__ANEEquivalenceResolution._leafName
+ _OBJC_IVAR_$__ANEEquivalenceResolution._leafPath
+ _OBJC_METACLASS_$__ANECacheMaintenance
+ _OBJC_METACLASS_$__ANECompileContentKey
+ _OBJC_METACLASS_$__ANEEquivalenceIndex
+ _OBJC_METACLASS_$__ANEEquivalenceResolution
+ __OBJC_$_CLASS_METHODS__ANECacheMaintenance
+ __OBJC_$_CLASS_METHODS__ANECompileContentKey
+ __OBJC_$_CLASS_METHODS__ANEEquivalenceIndex
+ __OBJC_$_CLASS_PROP_LIST__ANEEquivalenceIndex
+ __OBJC_$_INSTANCE_METHODS__ANEEquivalenceIndex
+ __OBJC_$_INSTANCE_METHODS__ANEEquivalenceResolution
+ __OBJC_$_INSTANCE_VARIABLES__ANEEquivalenceIndex
+ __OBJC_$_INSTANCE_VARIABLES__ANEEquivalenceResolution
+ __OBJC_$_PROP_LIST__ANEEquivalenceResolution
+ __OBJC_CLASS_RO_$__ANECacheMaintenance
+ __OBJC_CLASS_RO_$__ANECompileContentKey
+ __OBJC_CLASS_RO_$__ANEEquivalenceIndex
+ __OBJC_CLASS_RO_$__ANEEquivalenceResolution
+ __OBJC_METACLASS_RO_$__ANECacheMaintenance
+ __OBJC_METACLASS_RO_$__ANECompileContentKey
+ __OBJC_METACLASS_RO_$__ANEEquivalenceIndex
+ __OBJC_METACLASS_RO_$__ANEEquivalenceResolution
+ ___35+[_ANEEquivalenceIndex serialQueue]_block_invoke
+ ___40-[_ANEEquivalenceIndex evictContentKey:]_block_invoke
+ ___42+[_ANECompileContentKey optionsToSkipList]_block_invoke
+ ___42-[_ANEEquivalenceIndex resolveContentKey:]_block_invoke
+ ___50-[_ANEEquivalenceIndex recordContentKey:leafName:]_block_invoke
+ ___78-[_ANEModelCacheManager modelIdentityDirectoryForModel:bundleID:useSourceURL:]_block_invoke
+ ___block_descriptor_40_e8_32r_e31_v24?0"NSString"8"NSString"16lr32l8
+ ___block_descriptor_64_e8_32s40s48s56r_e5_v8?0ls32l8s40l8s48l8r56l8
+ __saveLocked:.atomicUnsupported
+ _kANECacheTrashDirectoryName
+ _lstat
+ _objc_msgSend$UUID
+ _objc_msgSend$UUIDString
+ _objc_msgSend$_contentKeyForModel:options:fingerprint:
+ _objc_msgSend$_indexForModel:csIdentity:options:
+ _objc_msgSend$_loadLocked
+ _objc_msgSend$_resolutionForEntry:contentKey:index:dirty:
+ _objc_msgSend$_safeLeafPathForName:
+ _objc_msgSend$_saveLocked:
+ _objc_msgSend$accessTimeForPath:
+ _objc_msgSend$churnFaultThreshold
+ _objc_msgSend$contentKeyForInputPath:options:modelType:
+ _objc_msgSend$contentsOfDirectoryAtPath:error:
+ _objc_msgSend$dataUsingEncoding:
+ _objc_msgSend$dataWithJSONObject:options:error:
+ _objc_msgSend$dictionaryWithContentsOfFile:
+ _objc_msgSend$dupCount
+ _objc_msgSend$effectiveBundleIDForModel:bundleID:
+ _objc_msgSend$equivalenceIndexName
+ _objc_msgSend$evictContentKey:
+ _objc_msgSend$evictEquivalenceForModel:csIdentity:options:contentKey:
+ _objc_msgSend$hexStringForData:
+ _objc_msgSend$hexStringForFileAtPath:
+ _objc_msgSend$initWithModelIdentityDirectory:
+ _objc_msgSend$inputsDigestForPath:
+ _objc_msgSend$inputsFingerprintForPath:
+ _objc_msgSend$insertObject:atIndex:
+ _objc_msgSend$isValidJSONObject:
+ _objc_msgSend$leafName
+ _objc_msgSend$leafPath
+ _objc_msgSend$memoryMapModelAtPath:modelAttributes:
+ _objc_msgSend$modelAttributes
+ _objc_msgSend$modelIdentityDirectoryForModel:bundleID:useSourceURL:
+ _objc_msgSend$optionsDigestForOptions:
+ _objc_msgSend$optionsToSkipList
+ _objc_msgSend$recordContentKey:leafName:
+ _objc_msgSend$resolveContentKey:
+ _objc_msgSend$serialQueue
+ _objc_msgSend$setAccessTime:forPath:
+ _objc_msgSend$setCacheURLIdentifier:
+ _objc_msgSend$setDupCount:
+ _objc_msgSend$setLeafName:
+ _objc_msgSend$setLeafPath:
+ _objc_msgSend$sortedArrayUsingSelector:
+ _objc_msgSend$string
+ _objc_msgSend$updateAccessTimeForPath:
+ _objc_msgSend$updateModelAttributes:state:
+ _objc_msgSend$writeToURL:options:error:
+ _objc_retain_x5
+ _objc_setProperty_nonatomic_copy
+ _optionsToSkipList.onceToken
+ _optionsToSkipList.skipList
+ _rename
+ _serialQueue.onceToken
+ _serialQueue.queue
- GCC_except_table12
- _objc_msgSend$setAccessTime:forModelFilePath:
CStrings:
+ "%@-%@"
+ "%@: FAILED writing %{public}@ : %{public}@"
+ "%@: Skipping update for path=%@"
+ "%@: atomic write unavailable (%{public}@); writing the index in place from now on. A torn index is tolerable because an unparseable one is read as empty."
+ "%@: compile inputs changed while compiling; not recording leaf=%{public}@"
+ "%@: could not hash %@"
+ "%@: could not move %@ to trash : errno=%d"
+ "%@: could not remove %@ : error=%@"
+ "%@: equivalence candidate unmappable: %@"
+ "%@: getxattr(%@, %@) failed : errno=%d"
+ "%@: getxattr(%@, %@) missing attribute"
+ "%@: identity path traversal rejected: %@"
+ "%@: input path does not exist: %@"
+ "%@: no regular files under %@"
+ "%@: nothing to reclaim at %@ : error=%@"
+ "%@: options are not a valid JSON object"
+ "%@: options not canonicalizable: %@"
+ "%@: refusing to record leaf with no binary: %{public}@"
+ "%@: refusing unsafe leafName=%{public}@"
+ "%@: removed %lu of %lu entries from %@"
+ "%@: serialise failed for %{public}@ : %{public}@"
+ "%@: setxattr(%@, %@) failed : errno=%d"
+ "%@: subpathsOfDirectoryAtPath:%@ failed : err=%@"
+ "%@_%@"
+ "%@|%@"
+ "."
+ ".trash"
+ "@40@0:8@16@24^@32"
+ "@48@0:8@16@24@32^B40"
+ "@64@0:8@16@24@32^@40^@48^@56"
+ "B64@0:8@16@24@32@40@48@56"
+ "Recovered compiled model by equivalence: leaf=%{public}@ dups=%lu csIdentity=%{public}@"
+ "T@\"NSString\",C,N,V_leafName"
+ "T@\"NSString\",C,N,V_leafPath"
+ "TQ,N,V_dupCount"
+ "TQ,R,N"
+ "UUID"
+ "UUIDString"
+ "_ANECacheMaintenance"
+ "_ANECompileContentKey"
+ "_ANEEquivalenceIndex"
+ "_ANEEquivalenceResolution"
+ "_contentKeyForModel:options:fingerprint:"
+ "_dupCount"
+ "_identityDirURL"
+ "_indexForModel:csIdentity:options:"
+ "_indexPath"
+ "_leafName"
+ "_leafPath"
+ "_loadLocked"
+ "_resolutionForEntry:contentKey:index:dirty:"
+ "_safeLeafPathForName:"
+ "_saveLocked:"
+ "accessTimeForPath:"
+ "churnFaultThreshold"
+ "com.apple.ane.aned.equivalenceIndex"
+ "compile-cache key churn: %lu redundant compiles avoided for identity %{public}@ (leaf %{public}@). A client is varying _ANEModel.key for identical compile inputs."
+ "contentKeyForInputPath:options:modelType:"
+ "contentsOfDirectoryAtPath:error:"
+ "dataUsingEncoding:"
+ "dataWithJSONObject:options:error:"
+ "dictionaryWithContentsOfFile:"
+ "dupCount"
+ "dups"
+ "effectiveBundleIDForModel:bundleID:"
+ "equivalence index entry rejected: unsafe leaf name %{public}@ in %{public}@"
+ "equivalence leaf %{public}@ has no binary; dropping entry"
+ "equivalenceIndexName"
+ "equivalentCompiledModelForModel:csIdentity:options:modelAttributes:contentKey:inputsFingerprint:"
+ "evictContentKey:"
+ "evictEquivalenceForModel:csIdentity:options:contentKey:"
+ "hexStringForData:"
+ "hexStringForFileAtPath:"
+ "initWithModelIdentityDirectory:"
+ "inputsDigestForPath:"
+ "inputsFingerprintForPath:"
+ "insertObject:atIndex:"
+ "isValidJSONObject:"
+ "leaf"
+ "leafName"
+ "leafPath"
+ "modelAttributes"
+ "modelIdentityDirectoryForModel:bundleID:useSourceURL:"
+ "optionsDigestForOptions:"
+ "optionsToSkipList"
+ "recordContentKey:leafName:"
+ "recordEquivalenceForModel:csIdentity:options:contentKey:inputsFingerprint:leafPath:"
+ "removeEntriesAtPath:notAccessedFor:"
+ "resolveContentKey:"
+ "serialQueue"
+ "setAccessTime:forPath:"
+ "setCacheURLIdentifier:"
+ "setDupCount:"
+ "setLeafName:"
+ "setLeafPath:"
+ "sortedArrayUsingSelector:"
+ "string"
+ "updateAccessTimeForPath:"
+ "updateModelAttributes:state:"
+ "v24@0:8Q16"
+ "v32@0:8@16d24"
+ "v48@0:8@16@24@32@40"
+ "writeToURL:options:error:"
+ "|%@:%llu:%llu:%ld.%09ld:%ld.%09ld"
+ "|%lu:%@=%@"
- "%@: +setAccessTime:forFilePath failed"
- "%@: Skipping update for filePath=%@"
- "%@: filePath=%@"
- "%@: getxattr(%@, %@, %p, %lu) failed  : errno=%d"
- "%@: getxattr(%@, %@, %p, %lu) missing attribute  : errno=%d"
- "%@: setxattr(%@, %@, %p, %lu) failed  : errno=%d"
```
