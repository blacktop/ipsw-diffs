## AppleNeuralEngine

> `/System/Library/PrivateFrameworks/AppleNeuralEngine.framework/Versions/A/AppleNeuralEngine`

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
- `__AUTH_CONST.__objc_dictobj`
- `__AUTH_CONST.__objc_intobj`
- `__AUTH_CONST.__objc_arrayobj`
- `__AUTH.__objc_data`
- `__DATA_DIRTY.__objc_data`
- `__DATA_DIRTY.__data`

```diff

-382.11.1.0.0
-  __TEXT.__text: 0x5cd10
-  __TEXT.__objc_methlist: 0x2b8c
-  __TEXT.__const: 0x2b8
-  __TEXT.__oslogstring: 0xb7ac
-  __TEXT.__cstring: 0x38bd
-  __TEXT.__gcc_except_tab: 0x67a4
-  __TEXT.__unwind_info: 0x1380
+382.12.0.0.0
+  __TEXT.__text: 0x5e448
+  __TEXT.__objc_methlist: 0x2b94
+  __TEXT.__const: 0x2c0
+  __TEXT.__oslogstring: 0xb967
+  __TEXT.__cstring: 0x38d5
+  __TEXT.__gcc_except_tab: 0x6804
+  __TEXT.__unwind_info: 0x1388
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
   __DATA_CONST.__got: 0x300
   __AUTH_CONST.__const: 0xd70
-  __AUTH_CONST.__cfstring: 0x4aa0
+  __AUTH_CONST.__cfstring: 0x4ac0
   __AUTH_CONST.__objc_const: 0x3cd0
   __AUTH_CONST.__weak_auth_got: 0x28
   __AUTH_CONST.__objc_dictobj: 0x50
   __AUTH_CONST.__objc_intobj: 0x30
   __AUTH_CONST.__objc_arrayobj: 0x60
-  __AUTH_CONST.__auth_got: 0x598
+  __AUTH_CONST.__auth_got: 0x5a0
   __AUTH.__objc_data: 0x410
   __DATA.__objc_ivar: 0x23c
-  __DATA.__data: 0x710
+  __DATA.__data: 0x718
   __DATA.__bss: 0x178
   __DATA_DIRTY.__objc_data: 0x7d0
   __DATA_DIRTY.__data: 0x10

   - /usr/lib/libcompression.dylib
   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libsandbox.1.dylib
-  Functions: 1771
-  Symbols:   2965
-  CStrings:  1427
+  Functions: 1780
+  Symbols:   2966
+  CStrings:  1439
 
Symbols:
+ +[_ANECloneHelper stageInBundleFileConstantsForModel:srcDir:dstDir:cloneDirectory:]
+ GCC_except_table77
+ GCC_except_table80
+ _OUTLINED_FUNCTION_39
+ __46-[_ANEClient doUnloadModel:options:qos:error:]_block_invoke
+ __71-[_ANEClient doPrepareChainingWithModel:options:chainingReq:qos:error:]_block_invoke
+ ___block_descriptor_116_e8_32s40s48s56s64r72r80r_e5_v8?0l
+ ___block_descriptor_124_e8_32s40s48s56s64s72r80r88r_e5_v8?0l
+ ___copy_helper_block_e8_32s40s48s56s64r72r80r
+ ___copy_helper_block_e8_32s40s48s56s64s72r80r88r
+ ___destroy_helper_block_e8_32s40s48s56s64r72r80r
+ ___destroy_helper_block_e8_32s40s48s56s64s72r80r88r
+ _kANEDCompilerQoSHintKey
+ _objc_msgSend$stageInBundleFileConstantsForModel:srcDir:dstDir:cloneDirectory:
+ _objc_msgSend$timeIntervalSinceDate:
+ _strnlen
- GCC_except_table58
- GCC_except_table68
- GCC_except_table72
- GCC_except_table75
- GCC_except_table78
- GCC_except_table83
- __44-[_ANEClient doLoadModel:options:qos:error:]_block_invoke_2
- ___44-[_ANEClient doLoadModel:options:qos:error:]_block_invoke_2
- ___45-[_ANEClient compileModel:options:qos:error:]_block_invoke_2
- ___46-[_ANEClient doUnloadModel:options:qos:error:]_block_invoke_2
- ___71-[_ANEClient doPrepareChainingWithModel:options:chainingReq:qos:error:]_block_invoke_2
- ___block_descriptor_100_e8_32s40s48s56s64r72r_e5_v8?0l
- ___block_descriptor_92_e8_32s40s48s56r64r_e5_v8?0l
- ___copy_helper_block_e8_32s40s48s56s64r72r
- ___destroy_helper_block_e8_32s40s48s56s64r72r
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
