## AppleNeuralEngine

> `/System/Library/PrivateFrameworks/AppleNeuralEngine.framework/AppleNeuralEngine`

### Sections with Same Size but Changed Content

- `__DATA_CONST.__const`
- `__DATA_CONST.__objc_classlist`
- `__DATA_CONST.__objc_catlist`
- `__DATA_CONST.__objc_protolist`
- `__DATA_CONST.__weak_got`
- `__DATA_CONST.__objc_protorefs`
- `__DATA_CONST.__objc_superrefs`
- `__DATA_CONST.__objc_arraydata`
- `__DATA_CONST.__got`
- `__AUTH_CONST.__const`
- `__AUTH_CONST.__objc_const`
- `__AUTH_CONST.__weak_auth_got`
- `__AUTH_CONST.__objc_dictobj`
- `__AUTH_CONST.__objc_intobj`
- `__AUTH_CONST.__objc_arrayobj`
- `__AUTH.__objc_data`
- `__DATA_DIRTY.__objc_data`
- `__DATA_DIRTY.__data`

```diff

-382.11.0.0.0
-  __TEXT.__text: 0x569b4
-  __TEXT.__objc_methlist: 0x2b8c
-  __TEXT.__const: 0x2b0
-  __TEXT.__oslogstring: 0xb6c8
-  __TEXT.__cstring: 0x387b
-  __TEXT.__gcc_except_tab: 0x676c
-  __TEXT.__unwind_info: 0x1410
+382.12.0.0.0
+  __TEXT.__text: 0x57ec0
+  __TEXT.__objc_methlist: 0x2b94
+  __TEXT.__const: 0x2b8
+  __TEXT.__oslogstring: 0xb883
+  __TEXT.__cstring: 0x3893
+  __TEXT.__gcc_except_tab: 0x67d0
+  __TEXT.__unwind_info: 0x1418
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0
   __TEXT.__objc_classname: 0x0

   __DATA_CONST.__objc_protolist: 0x28
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__weak_got: 0x10
-  __DATA_CONST.__objc_selrefs: 0x1a18
+  __DATA_CONST.__objc_selrefs: 0x1a28
   __DATA_CONST.__objc_protorefs: 0x10
   __DATA_CONST.__objc_superrefs: 0xd8
   __DATA_CONST.__objc_arraydata: 0x120
   __DATA_CONST.__got: 0x2f8
   __AUTH_CONST.__const: 0x4d0
-  __AUTH_CONST.__cfstring: 0x4a60
+  __AUTH_CONST.__cfstring: 0x4a80
   __AUTH_CONST.__objc_const: 0x3cd0
   __AUTH_CONST.__weak_auth_got: 0x28
   __AUTH_CONST.__objc_dictobj: 0x50
   __AUTH_CONST.__objc_intobj: 0x30
   __AUTH_CONST.__objc_arrayobj: 0x60
-  __AUTH_CONST.__auth_got: 0x678
+  __AUTH_CONST.__auth_got: 0x680
   __AUTH.__objc_data: 0x4b0
   __DATA.__objc_ivar: 0x23c
-  __DATA.__data: 0x710
+  __DATA.__data: 0x718
   __DATA.__bss: 0x180
   __DATA_DIRTY.__objc_data: 0x730
   __DATA_DIRTY.__data: 0x10

   - /usr/lib/libcompression.dylib
   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libsandbox.1.dylib
-  Functions: 1718
-  Symbols:   2897
-  CStrings:  1421
+  Functions: 1726
+  Symbols:   2899
+  CStrings:  1433
 
Symbols:
+ +[_ANECloneHelper stageInBundleFileConstantsForModel:srcDir:dstDir:cloneDirectory:]
+ _OUTLINED_FUNCTION_39
+ ___block_descriptor_116_e8_32s40s48s56s64r72r80r_e5_v8?0ls32l8r64l8s40l8r72l8s48l8s56l8r80l8
+ ___block_descriptor_116_e8_32s40s48s56s64r72r80r_e5_v8?0ls32l8r64l8s40l8s48l8r72l8s56l8r80l8
+ ___block_descriptor_116_e8_32s40s48s56s64r72r80r_e5_v8?0ls32l8r64l8s40l8s48l8s56l8r72l8r80l8
+ ___block_descriptor_124_e8_32s40s48s56s64s72r80r88r_e5_v8?0ls32l8r72l8s40l8s48l8s56l8r80l8s64l8r88l8
+ ___block_descriptor_124_e8_32s40s48s56s64s72r80r88r_e5_v8?0ls32l8r72l8s40l8s48l8s56l8s64l8r80l8r88l8
+ _kANEDCompilerQoSHintKey
+ _objc_msgSend$stageInBundleFileConstantsForModel:srcDir:dstDir:cloneDirectory:
+ _objc_msgSend$timeIntervalSinceDate:
+ _strnlen
- ___44-[_ANEClient doLoadModel:options:qos:error:]_block_invoke_2
- ___45-[_ANEClient compileModel:options:qos:error:]_block_invoke_2
- ___46-[_ANEClient doUnloadModel:options:qos:error:]_block_invoke_2
- ___71-[_ANEClient doPrepareChainingWithModel:options:chainingReq:qos:error:]_block_invoke_2
- ___block_descriptor_100_e8_32s40s48s56s64r72r_e5_v8?0ls32l8s40l8r64l8s48l8s56l8r72l8
- ___block_descriptor_100_e8_32s40s48s56s64r72r_e5_v8?0ls32l8s40l8s48l8s56l8r64l8r72l8
- ___block_descriptor_92_e8_32s40s48s56r64r_e5_v8?0ls32l8r56l8s40l8s48l8r64l8
- ___block_descriptor_92_e8_32s40s48s56r64r_e5_v8?0ls32l8s40l8r56l8s48l8r64l8
- ___block_descriptor_92_e8_32s40s48s56r64r_e5_v8?0ls32l8s40l8s48l8r56l8r64l8
CStrings:
+ "%@: buildVersion (%zu bytes) larger than max buffer size %d, truncated\n"
+ "%@: copyfile(%@, %@) FAILED errno=%d (%s)"
+ "%@: createDirectory(%@) FAILED: %@"
+ "%@: in-bundle FileConstants rebase failed for %@"
+ "%@: in-bundle FileConstants staging failed for %@"
+ "_ANEF_COMPILE_PRIORITY_WAIT"
+ "_ANEF_LOAD_NEW_INSTANCE_PRIORITY_WAIT"
+ "_ANEF_LOAD_PRIORITY_WAIT"
+ "_ANEF_PREP_CHAIN_PRIORITY_WAIT"
+ "_ANEF_UNLOAD_PRIORITY_WAIT"
+ "kANEDCompilerQoSHintKey"
+ "qos:%u model.string_id:%llu priorityWaitMs:%f"
```
