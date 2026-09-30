## ANECompilerService

> `/System/Library/PrivateFrameworks/AppleNeuralEngine.framework/XPCServices/ANECompilerService.xpc/Contents/MacOS/ANECompilerService`

### Sections with Same Size but Changed Content

- `__TEXT.__const`
- `__DATA_CONST.__objc_classlist`
- `__DATA_CONST.__objc_catlist`
- `__DATA_CONST.__objc_protolist`
- `__DATA_CONST.__objc_protorefs`
- `__DATA_CONST.__objc_superrefs`
- `__DATA_CONST.__objc_intobj`
- `__DATA.__objc_data`

```diff

-382.12.0.0.0
-  __TEXT.__text: 0x1b3b8
-  __TEXT.__auth_stubs: 0x670
-  __TEXT.__objc_stubs: 0x2200
-  __TEXT.__objc_methlist: 0x974
+382.15.1.0.0
+  __TEXT.__text: 0x1c49c
+  __TEXT.__auth_stubs: 0x720
+  __TEXT.__objc_stubs: 0x22c0
+  __TEXT.__objc_methlist: 0x9b4
   __TEXT.__const: 0x120
-  __TEXT.__cstring: 0x12f7
-  __TEXT.__oslogstring: 0x2359
+  __TEXT.__cstring: 0x1366
+  __TEXT.__oslogstring: 0x267e
   __TEXT.__objc_classname: 0x19e
-  __TEXT.__objc_methname: 0x2534
-  __TEXT.__objc_methtype: 0x615
-  __TEXT.__gcc_except_tab: 0x12a8
-  __TEXT.__unwind_info: 0x460
-  __DATA_CONST.__const: 0x380
-  __DATA_CONST.__cfstring: 0x1920
+  __TEXT.__objc_methname: 0x2644
+  __TEXT.__objc_methtype: 0x67b
+  __TEXT.__gcc_except_tab: 0x12d4
+  __TEXT.__unwind_info: 0x478
+  __DATA_CONST.__const: 0x3b0
+  __DATA_CONST.__cfstring: 0x1980
   __DATA_CONST.__objc_classlist: 0x80
   __DATA_CONST.__objc_catlist: 0x8
   __DATA_CONST.__objc_protolist: 0x28

   __DATA_CONST.__objc_protorefs: 0x10
   __DATA_CONST.__objc_superrefs: 0x20
   __DATA_CONST.__objc_intobj: 0x90
-  __DATA_CONST.__auth_got: 0x350
-  __DATA_CONST.__got: 0x1b8
-  __DATA.__objc_const: 0xd20
-  __DATA.__objc_selrefs: 0xa70
+  __DATA_CONST.__auth_got: 0x3a8
+  __DATA_CONST.__got: 0x1c0
+  __DATA.__objc_const: 0xd48
+  __DATA.__objc_selrefs: 0xaa8
   __DATA.__objc_ivar: 0x24
   __DATA.__objc_data: 0x500
-  __DATA.__data: 0x3f8
+  __DATA.__data: 0x400
   __DATA.__bss: 0x88
   - /System/Library/Frameworks/CoreFoundation.framework/Versions/A/CoreFoundation
   - /System/Library/Frameworks/Foundation.framework/Versions/C/Foundation

   - /usr/lib/libcompression.dylib
   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libsandbox.1.dylib
-  Functions: 326
-  Symbols:   939
-  CStrings:  871
+  Functions: 343
+  Symbols:   968
+  CStrings:  897
 
Symbols:
+ +[_ANECompiler applyBondedFlavor:toCompilerOptions:]
+ +[_ANEStorageHelper relevantContainerForPath:]
+ +[_ANEStorageHelper sourcePathForModelInStoreAt:]
+ -[_ANECompilerService moveCachedModelFromSource:toDestination:withReply:]
+ -[_ANECompilerService updateSourcePathAt:to:withContainerAt:withContainer:withReply:]
+ -[_ANEModelCacheManager scanAllPartitionsForModel:csIdentity:appGroups:expunge:]
+ -[_ANEModelCacheManager scanAllPartitionsForModel:csIdentity:appGroups:expunge:allowProcessModelShare:]
+ GCC_except_table13
+ GCC_except_table17
+ GCC_except_table4
+ GCC_except_table7
+ ___103-[_ANEModelCacheManager scanAllPartitionsForModel:csIdentity:appGroups:expunge:allowProcessModelShare:]_block_invoke
+ ___73-[_ANECompilerService moveCachedModelFromSource:toDestination:withReply:]_block_invoke
+ ___85-[_ANECompilerService updateSourcePathAt:to:withContainerAt:withContainer:withReply:]_block_invoke
+ ___block_descriptor_56_e8_32s40s48bs_e5_v8?0l
+ ___block_descriptor_80_e8_32s40s48s56s64bs_e5_v8?0l
+ ___copy_helper_block_e8_32s40s48s56s64b
+ ___destroy_helper_block_e8_32s40s48s56s64s
+ ___kCFBooleanTrue
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
+ _kANEFDisableBondedNetworksKey
+ _objc_msgSend$applyBondedFlavor:toCompilerOptions:
+ _objc_msgSend$description
+ _objc_msgSend$modelSourceContainerName
+ _objc_msgSend$moveItemAtURL:toURL:error:
+ _objc_msgSend$scanAllPartitionsForModel:csIdentity:appGroups:expunge:allowProcessModelShare:
+ _objc_msgSend$sourcePathForModelInStoreAt:
+ _objc_msgSend$writeToFile:options:error:
- -[_ANECompilerService updateSourcePathAt:to:withReply:]
- -[_ANEModelCacheManager scanAllPartitionsForModel:csIdentity:expunge:]
- -[_ANEModelCacheManager scanAllPartitionsForModel:csIdentity:expunge:allowProcessModelShare:]
- GCC_except_table15
- GCC_except_table5
- ___55-[_ANECompilerService updateSourcePathAt:to:withReply:]_block_invoke
- ___93-[_ANEModelCacheManager scanAllPartitionsForModel:csIdentity:expunge:allowProcessModelShare:]_block_invoke
- ___block_descriptor_64_e8_32s40s48bs_e5_v8?0l
- _objc_msgSend$scanAllPartitionsForModel:csIdentity:expunge:allowProcessModelShare:
CStrings:
+ "%@/%@"
+ "%@: Error deserializing container: %s"
+ "%@: Error executing query: %llu"
+ "%@: Error querying current version of deserialized container: %s"
+ "%@: FAILED storing containerInfo=%@ to %@ : err=%@"
+ "%@: Full path: %{public}@ is member of container at path: %s. Relative component is: %s (error:%llu)"
+ "%@: Nil sourcePathname!"
+ "%@: Returning full path as: %@"
+ "%@: Returning path consisting of container path: %@ and relative path: %@. Resulting full path vended is: %@"
+ "%@: nil patchedURL for modelURL=%@ — cannot patch"
+ "%@: nil patchedURL for modelURL=%@ — skipping purge"
+ "%@: stringByDeletingPathExtension returned nil for filename=%{public}@ (length=%lu)"
+ "%@: substringToIndex:%lu returned nil for filename=%{public}@"
+ "%s: DisableBondedNetworks set from ANEF flag (bonded flavor will be disabled if supported on this HW)"
+ "+[_ANECompiler applyBondedFlavor:toCompilerOptions:]"
+ "B44@0:8@16@24@32B40"
+ "B48@0:8@16@24@32B40B44"
+ "DisableBondedNetworks"
+ "applyBondedFlavor:toCompilerOptions:"
+ "kANEFDisableBondedNetworksKey"
+ "modelSourceContainerName"
+ "moveCachedModelFromSource:toDestination:withReply:"
+ "moveItemAtURL:toURL:error:"
+ "relevantContainerForPath:"
+ "scanAllPartitionsForModel:csIdentity:appGroups:expunge:"
+ "scanAllPartitionsForModel:csIdentity:appGroups:expunge:allowProcessModelShare:"
+ "sourcePathForModelInStoreAt:"
+ "updateSourcePathAt:to:withContainerAt:withContainer:withReply:"
+ "v40@0:8@\"NSURL\"16@\"NSURL\"24@?<v@?B@\"NSError\">32"
+ "v56@0:8@\"NSString\"16@\"NSString\"24@\"NSString\"32@\"NSData\"40@?<v@?B@\"NSError\">48"
+ "v56@0:8@16@24@32@40@?48"
+ "writeToFile:options:error:"
- "B36@0:8@16@24B32"
- "B40@0:8@16@24B32B36"
- "scanAllPartitionsForModel:csIdentity:expunge:"
- "scanAllPartitionsForModel:csIdentity:expunge:allowProcessModelShare:"
- "updateSourcePathAt:to:withReply:"
- "v40@0:8@\"NSString\"16@\"NSString\"24@?<v@?B@\"NSError\">32"
```
