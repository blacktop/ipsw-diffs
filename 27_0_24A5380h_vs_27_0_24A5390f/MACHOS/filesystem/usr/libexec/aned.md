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

-382.11.0.0.0
-  __TEXT.__text: 0x67460
-  __TEXT.__auth_stubs: 0xec0
-  __TEXT.__objc_stubs: 0x3220
-  __TEXT.__objc_methlist: 0x10e4
-  __TEXT.__const: 0x5cec
-  __TEXT.__gcc_except_tab: 0x4ce0
-  __TEXT.__cstring: 0x5ad2
-  __TEXT.__oslogstring: 0x6522
+382.12.0.0.0
+  __TEXT.__text: 0x68888
+  __TEXT.__auth_stubs: 0xed0
+  __TEXT.__objc_stubs: 0x3320
+  __TEXT.__objc_methlist: 0x111c
+  __TEXT.__const: 0x5cfc
+  __TEXT.__gcc_except_tab: 0x4e74
+  __TEXT.__cstring: 0x5b72
+  __TEXT.__oslogstring: 0x674e
   __TEXT.__objc_classname: 0x22f
-  __TEXT.__objc_methname: 0x3b21
-  __TEXT.__objc_methtype: 0xdad
-  __TEXT.__unwind_info: 0x1818
+  __TEXT.__objc_methname: 0x3c5c
+  __TEXT.__objc_methtype: 0xdd2
+  __TEXT.__unwind_info: 0x1828
   __DATA_CONST.__const: 0x26a8
-  __DATA_CONST.__cfstring: 0xa20
+  __DATA_CONST.__cfstring: 0xb00
   __DATA_CONST.__objc_classlist: 0x88
   __DATA_CONST.__objc_protolist: 0x60
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_protorefs: 0x10
   __DATA_CONST.__objc_superrefs: 0x60
   __DATA_CONST.__objc_intobj: 0x18
-  __DATA_CONST.__auth_got: 0x778
-  __DATA_CONST.__got: 0x3a8
+  __DATA_CONST.__auth_got: 0x780
+  __DATA_CONST.__got: 0x3b0
   __DATA_CONST.__auth_ptr: 0x18
-  __DATA.__objc_const: 0x1be8
-  __DATA.__objc_selrefs: 0xf18
-  __DATA.__objc_ivar: 0xe4
+  __DATA.__objc_const: 0x1c18
+  __DATA.__objc_selrefs: 0xf58
+  __DATA.__objc_ivar: 0xe8
   __DATA.__objc_data: 0x550
   __DATA.__data: 0x490
   __DATA.__bss: 0x88

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libc++.1.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 2413
-  Symbols:   3652
-  CStrings:  1685
+  Functions: 2420
+  Symbols:   3666
+  CStrings:  1708
 
Symbols:
+ +[_ANEStorageHelper isPath:safelyWithinDirectory:]
+ -[_ANEModelCacheManager scanAllPartitionsForModel:csIdentity:expunge:allowProcessModelShare:]
+ -[_ANEServer processNameForServiceUUID:]
+ -[_ANEServer selectCompilerService:isE5ML:qos:]
+ -[_ANEServer uuidANECompilerServiceBackground]
+ OBJC_IVAR_$__ANEServer._uuidANECompilerServiceBackground
+ ___93-[_ANEModelCacheManager scanAllPartitionsForModel:csIdentity:expunge:allowProcessModelShare:]_block_invoke
+ ___block_descriptor_80_ea8_32s40s48r56r64r_e37_v28?0B8"NSDictionary"12"NSError"20lr48l8r56l8r64l8s32l8s40l8
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
- GCC_except_table49
- GCC_except_table9
- ___70-[_ANEModelCacheManager scanAllPartitionsForModel:csIdentity:expunge:]_block_invoke
- ___block_descriptor_72_ea8_32s40r48r56r_e37_v28?0B8"NSDictionary"12"NSError"20lr40l8r48l8r56l8s32l8
CStrings:
+ "%@: refusing expunge with allowProcessModelShare — would purge shared-bucket models on behalf of an unrelated csIdentity"
+ "%@|%@"
+ "%u %u model.string_id:%llu csIdentity:%{public}@"
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
