## aned

> `/usr/libexec/aned`

### Sections with Same Size but Changed Content

- `__DATA_CONST.__cfstring`
- `__DATA_CONST.__objc_protolist`
- `__DATA_CONST.__objc_protorefs`
- `__DATA_CONST.__objc_superrefs`
- `__DATA_CONST.__objc_intobj`
- `__DATA_CONST.__auth_ptr`
- `__DATA.__data`

```diff

-382.12.0.0.0
-  __TEXT.__text: 0x68888
-  __TEXT.__auth_stubs: 0xed0
-  __TEXT.__objc_stubs: 0x3320
-  __TEXT.__objc_methlist: 0x111c
+382.15.1.0.0
+  __TEXT.__text: 0x6c3f0
+  __TEXT.__auth_stubs: 0xf70
+  __TEXT.__objc_stubs: 0x34a0
+  __TEXT.__objc_methlist: 0x1184
   __TEXT.__const: 0x5cfc
-  __TEXT.__gcc_except_tab: 0x4e74
-  __TEXT.__cstring: 0x5b72
-  __TEXT.__oslogstring: 0x674e
-  __TEXT.__objc_classname: 0x22f
-  __TEXT.__objc_methname: 0x3c5c
-  __TEXT.__objc_methtype: 0xdd2
-  __TEXT.__unwind_info: 0x1828
-  __DATA_CONST.__const: 0x26a8
+  __TEXT.__gcc_except_tab: 0x5954
+  __TEXT.__cstring: 0x5b7d
+  __TEXT.__oslogstring: 0x6cd0
+  __TEXT.__objc_classname: 0x247
+  __TEXT.__objc_methname: 0x3ea7
+  __TEXT.__objc_methtype: 0xeaf
+  __TEXT.__unwind_info: 0x1868
+  __DATA_CONST.__const: 0x26c8
   __DATA_CONST.__cfstring: 0xb00
-  __DATA_CONST.__objc_classlist: 0x88
+  __DATA_CONST.__objc_classlist: 0x90
   __DATA_CONST.__objc_protolist: 0x60
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_protorefs: 0x10
   __DATA_CONST.__objc_superrefs: 0x60
+  __DATA_CONST.__objc_arraydata: 0x8
+  __DATA_CONST.__objc_arrayobj: 0x18
   __DATA_CONST.__objc_intobj: 0x18
-  __DATA_CONST.__auth_got: 0x780
-  __DATA_CONST.__got: 0x3b0
+  __DATA_CONST.__auth_got: 0x7d0
+  __DATA_CONST.__got: 0x3c0
   __DATA_CONST.__auth_ptr: 0x18
-  __DATA.__objc_const: 0x1c18
-  __DATA.__objc_selrefs: 0xf58
+  __DATA.__objc_const: 0x1cb8
+  __DATA.__objc_selrefs: 0xfc0
   __DATA.__objc_ivar: 0xe8
-  __DATA.__objc_data: 0x550
+  __DATA.__objc_data: 0x5a0
   __DATA.__data: 0x490
-  __DATA.__bss: 0x88
+  __DATA.__bss: 0x98
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/CoreServices.framework/CoreServices
   - /System/Library/Frameworks/Foundation.framework/Foundation

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libc++.1.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 2420
-  Symbols:   3666
-  CStrings:  1708
+  Functions: 2443
+  Symbols:   3711
+  CStrings:  1749
 
Symbols:
+ +[_ANECompileFlavorPolicy nonBondedCsIdentities]
+ +[_ANECompileFlavorPolicy shouldDisableBondedForCsIdentity:]
+ +[_ANEStorageHelper relevantContainerForPath:]
+ +[_ANEStorageHelper sourcePathForModelInStoreAt:]
+ -[_ANEModelCacheManager scanAllPartitionsForModel:csIdentity:appGroups:expunge:]
+ -[_ANEModelCacheManager scanAllPartitionsForModel:csIdentity:appGroups:expunge:allowProcessModelShare:]
+ -[_ANEServer _moveCachedModelFromSource:toDestination:withError:]
+ -[_ANEServer _updateSourcePathAt:to:withContainerAt:withContainer:withError:]
+ -[_ANEServer compileAsNeededAndLoadCachedModel:csIdentity:appGroups:sandboxExtension:options:qos:modelFilePath:modelAttributes:error:]
+ -[_ANEServer compiledModelExistsInCacheFor:limitToCurrentProcess:withReply:]
+ -[_ANEServer updateCachedModelLocationForModelTrackedByHash:toAppGroup:withReply:]
+ /Library/Caches/com.apple.xbs/<UUID>/TemporaryDirectory.<TMP>/Binaries/AppleNeuralEngine/install/TempContent/Objects/AppleNeuralEngine.build/aned.build/Objects-normal/arm64e/_ANECompileFlavorPolicy.o
+ ANECompileFlavorPolicy.m
+ GCC_except_table49
+ GCC_except_table55
+ _OBJC_CLASS_$_NSConstantArray
+ _OBJC_CLASS_$__ANECompileFlavorPolicy
+ _OBJC_METACLASS_$__ANECompileFlavorPolicy
+ __65-[_ANEServer _moveCachedModelFromSource:toDestination:withError:]_block_invoke
+ __77-[_ANEServer _updateSourcePathAt:to:withContainerAt:withContainer:withError:]_block_invoke
+ __OBJC_$_CLASS_METHODS__ANECompileFlavorPolicy
+ __OBJC_CLASS_RO_$__ANECompileFlavorPolicy
+ __OBJC_METACLASS_RO_$__ANECompileFlavorPolicy
+ __ZL26_ANELoadErrorForDriverCode9ANEReturnlP8NSStringb
+ ___103-[_ANEModelCacheManager scanAllPartitionsForModel:csIdentity:appGroups:expunge:allowProcessModelShare:]_block_invoke
+ ___134-[_ANEServer compileAsNeededAndLoadCachedModel:csIdentity:appGroups:sandboxExtension:options:qos:modelFilePath:modelAttributes:error:]_block_invoke
+ ___48+[_ANECompileFlavorPolicy nonBondedCsIdentities]_block_invoke
+ ___65-[_ANEServer _moveCachedModelFromSource:toDestination:withError:]_block_invoke
+ ___77-[_ANEServer _updateSourcePathAt:to:withContainerAt:withContainer:withError:]_block_invoke
+ _container_copy_from_path
+ _container_error_copy_unlocalized_description
+ _container_free_object
+ _container_get_path
+ _container_query_create_from_container
+ _container_query_free
+ _container_query_get_last_error
+ _container_query_get_single_result
+ _container_query_operation_set_flags
+ _container_serialize_copy_deserialized_reference
+ _container_serialize_copy_serialized_reference
+ _kANEErrorLoadStageKey
+ _kANEFDisableBondedNetworksKey
+ _objc_msgSend$_moveCachedModelFromSource:toDestination:withError:
+ _objc_msgSend$_updateSourcePathAt:to:withContainerAt:withContainer:withError:
+ _objc_msgSend$allValues
+ _objc_msgSend$appGroupIdentifiersFor:processIdentifier:
+ _objc_msgSend$compileAsNeededAndLoadCachedModel:csIdentity:appGroups:sandboxExtension:options:qos:modelFilePath:modelAttributes:error:
+ _objc_msgSend$dataWithBytesNoCopy:length:freeWhenDone:
+ _objc_msgSend$errorForCode:method:underlyingCode:additionalUserInfo:
+ _objc_msgSend$modelSourceContainerName
+ _objc_msgSend$moveCachedModelFromSource:toDestination:withReply:
+ _objc_msgSend$nonBondedCsIdentities
+ _objc_msgSend$numberWithInteger:
+ _objc_msgSend$relevantContainerForPath:
+ _objc_msgSend$scanAllPartitionsForModel:csIdentity:appGroups:expunge:
+ _objc_msgSend$scanAllPartitionsForModel:csIdentity:appGroups:expunge:allowProcessModelShare:
+ _objc_msgSend$shouldDisableBondedForCsIdentity:
+ _objc_msgSend$sourcePathForModelInStoreAt:
+ _objc_msgSend$updateSourcePathAt:to:withContainerAt:withContainer:withReply:
+ nonBondedCsIdentities.list
+ nonBondedCsIdentities.once
- -[_ANEModelCacheManager scanAllPartitionsForModel:csIdentity:expunge:]
- -[_ANEModelCacheManager scanAllPartitionsForModel:csIdentity:expunge:allowProcessModelShare:]
- -[_ANEServer _updateSourcePathAt:to:withError:]
- -[_ANEServer compileAsNeededAndLoadCachedModel:csIdentity:sandboxExtension:options:qos:modelFilePath:modelAttributes:error:]
- -[_ANEServer compiledModelExistsInCacheFor:withReply:]
- GCC_except_table42
- __47-[_ANEServer _updateSourcePathAt:to:withError:]_block_invoke
- ___124-[_ANEServer compileAsNeededAndLoadCachedModel:csIdentity:sandboxExtension:options:qos:modelFilePath:modelAttributes:error:]_block_invoke
- ___47-[_ANEServer _updateSourcePathAt:to:withError:]_block_invoke
- ___93-[_ANEModelCacheManager scanAllPartitionsForModel:csIdentity:expunge:allowProcessModelShare:]_block_invoke
- _objc_msgSend$_updateSourcePathAt:to:withError:
- _objc_msgSend$compileAsNeededAndLoadCachedModel:csIdentity:sandboxExtension:options:qos:modelFilePath:modelAttributes:error:
- _objc_msgSend$scanAllPartitionsForModel:csIdentity:expunge:
- _objc_msgSend$scanAllPartitionsForModel:csIdentity:expunge:allowProcessModelShare:
- _objc_msgSend$updateSourcePathAt:to:withReply:
- _objc_retain_x5
CStrings:
+ "%@/%@"
+ "%@: Attempted to update model from %@  to %@ (from hash=%@)"
+ "%@: Checking model exists in cache for %@: %d (in bundle=%@, from hash=%@)"
+ "%@: Checking model exists in cache for %@: %d (in group=%@, from hash=%@)"
+ "%@: DisableBondedNetworksKey set for csIdentity=%{public}@ (bonded flavor will be disabled if supported on this HW)"
+ "%@: Error deserializing container: %s"
+ "%@: Error executing query: %llu"
+ "%@: Error querying current version of deserialized container: %s"
+ "%@: FAILED to update model for app group %@ (from hash=%@): process not entitled for provided app-group, found %@"
+ "%@: FAILED to update model for app group, from: %@ to: %@, (from hash=%@): err=%@"
+ "%@: Failed to purge pre-compiled patched models for %@ of group %@: %@"
+ "%@: Full path: %{public}@ is member of container at path: %s. Relative component is: %s (error:%llu)"
+ "%@: Got container info: %{public}@"
+ "%@: Nil sourcePathname!"
+ "%@: Returning full path as: %@"
+ "%@: Returning path consisting of container path: %@ and relative path: %@. Resulting full path vended is: %@"
+ "%@: Successfully purged pre-compiled patched models for %@  of group %@"
+ "%@: nil patchedURL for modelURL=%@ — cannot patch"
+ "%@: nil patchedURL for modelURL=%@ — skipping purge"
+ "%@: stringByDeletingPathExtension returned nil for filename=%{public}@ (length=%lu)"
+ "%@: substringToIndex:%lu returned nil for filename=%{public}@"
+ "@84@0:8@16@24@32@40@48I56^@60^@68^@76"
+ "B44@0:8@16@24@32B40"
+ "B48@0:8@16@24@32B40B44"
+ "BEGIN: %@: : %@ : %@ : %@ : %@"
+ "END: %@ : %@ : %@ : %@ : %@"
+ "_ANECompileFlavorPolicy"
+ "_moveCachedModelFromSource:toDestination:withError:"
+ "_updateSourcePathAt:to:withContainerAt:withContainer:withError:"
+ "allValues"
+ "appGroupIdentifiersFor:processIdentifier:"
+ "com.topazlabs.TopazPhotoAI"
+ "compileAsNeededAndLoadCachedModel:csIdentity:appGroups:sandboxExtension:options:qos:modelFilePath:modelAttributes:error:"
+ "compiledModelExistsInCacheFor:limitToCurrentProcess:withReply:"
+ "dataWithBytesNoCopy:length:freeWhenDone:"
+ "errorForCode:method:underlyingCode:additionalUserInfo:"
+ "modelSourceContainerName"
+ "moveCachedModelFromSource:toDestination:withReply:"
+ "nonBondedCsIdentities"
+ "numberWithInteger:"
+ "relevantContainerForPath:"
+ "scanAllPartitionsForModel:csIdentity:appGroups:expunge:"
+ "scanAllPartitionsForModel:csIdentity:appGroups:expunge:allowProcessModelShare:"
+ "shouldDisableBondedForCsIdentity:"
+ "sourcePathForModelInStoreAt:"
+ "updateCachedModelLocationForModelTrackedByHash:toAppGroup:withReply:"
+ "updateSourcePathAt:to:withContainerAt:withContainer:withReply:"
+ "v36@0:8@\"NSString\"16B24@?<v@?B@\"NSError\">28"
+ "v36@0:8@16B24@?28"
+ "v40@0:8@\"NSURL\"16@\"NSURL\"24@?<v@?B@\"NSError\">32"
+ "v56@0:8@\"NSString\"16@\"NSString\"24@\"NSString\"32@\"NSData\"40@?<v@?B@\"NSError\">48"
+ "v56@0:8@16@24@32@40@?48"
- "/model.hwx"
- "/model.src"
- "@76@0:8@16@24@32@40I48^@52^@60^@68"
- "B36@0:8@16@24B32"
- "B40@0:8@16@24B32B36"
- "_updateSourcePathAt:to:withError:"
- "compileAsNeededAndLoadCachedModel:csIdentity:sandboxExtension:options:qos:modelFilePath:modelAttributes:error:"
- "compiledModelExistsInCacheFor:withReply:"
- "scanAllPartitionsForModel:csIdentity:expunge:"
- "scanAllPartitionsForModel:csIdentity:expunge:allowProcessModelShare:"
- "updateSourcePathAt:to:withReply:"
```
