## ANECompilerService

> `/System/Library/PrivateFrameworks/AppleNeuralEngine.framework/XPCServices/ANECompilerService.xpc/ANECompilerService`

### Sections with Same Size but Changed Content

- `__DATA_CONST.__const`
- `__DATA_CONST.__objc_classlist`
- `__DATA_CONST.__objc_catlist`
- `__DATA_CONST.__objc_protolist`
- `__DATA_CONST.__objc_protorefs`
- `__DATA_CONST.__objc_superrefs`
- `__DATA_CONST.__objc_intobj`
- `__DATA_CONST.__got`
- `__DATA.__objc_const`
- `__DATA.__objc_data`

```diff

-382.11.0.0.0
-  __TEXT.__text: 0x1819c
-  __TEXT.__auth_stubs: 0x7d0
-  __TEXT.__objc_stubs: 0x2160
-  __TEXT.__objc_methlist: 0x954
-  __TEXT.__const: 0x100
-  __TEXT.__cstring: 0x1255
-  __TEXT.__oslogstring: 0x20e8
+382.12.0.0.0
+  __TEXT.__text: 0x18b64
+  __TEXT.__auth_stubs: 0x7f0
+  __TEXT.__objc_stubs: 0x21c0
+  __TEXT.__objc_methlist: 0x96c
+  __TEXT.__const: 0x110
+  __TEXT.__cstring: 0x1277
+  __TEXT.__oslogstring: 0x224c
   __TEXT.__objc_classname: 0x19e
-  __TEXT.__objc_methname: 0x246d
-  __TEXT.__objc_methtype: 0x601
-  __TEXT.__gcc_except_tab: 0x1210
-  __TEXT.__unwind_info: 0x428
+  __TEXT.__objc_methname: 0x24e1
+  __TEXT.__objc_methtype: 0x615
+  __TEXT.__gcc_except_tab: 0x1248
+  __TEXT.__unwind_info: 0x430
   __DATA_CONST.__const: 0x320
-  __DATA_CONST.__cfstring: 0x1880
+  __DATA_CONST.__cfstring: 0x18c0
   __DATA_CONST.__objc_classlist: 0x80
   __DATA_CONST.__objc_catlist: 0x8
   __DATA_CONST.__objc_protolist: 0x28

   __DATA_CONST.__objc_protorefs: 0x10
   __DATA_CONST.__objc_superrefs: 0x20
   __DATA_CONST.__objc_intobj: 0x60
-  __DATA_CONST.__auth_got: 0x400
+  __DATA_CONST.__auth_got: 0x410
   __DATA_CONST.__got: 0x1b8
   __DATA.__objc_const: 0xd20
-  __DATA.__objc_selrefs: 0xa40
+  __DATA.__objc_selrefs: 0xa58
   __DATA.__objc_ivar: 0x24
   __DATA.__objc_data: 0x500
-  __DATA.__data: 0x3f0
+  __DATA.__data: 0x3f8
   __DATA.__bss: 0x88
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/Foundation.framework/Foundation

   - /usr/lib/libcompression.dylib
   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libsandbox.1.dylib
-  Functions: 291
-  Symbols:   933
-  CStrings:  842
+  Functions: 295
+  Symbols:   940
+  CStrings:  853
 
Symbols:
+ +[_ANEStorageHelper isPath:safelyWithinDirectory:]
+ -[_ANEModelCacheManager scanAllPartitionsForModel:csIdentity:expunge:allowProcessModelShare:]
+ ___93-[_ANEModelCacheManager scanAllPartitionsForModel:csIdentity:expunge:allowProcessModelShare:]_block_invoke
+ ___block_descriptor_156_e8_32s40s48s56s64s72s80s88s96s104bs112r_e5_v8?0ls32l8s40l8s48l8s56l8s104l8s64l8r112l8s72l8s80l8s88l8s96l8
+ __os_log_fault_impl
+ _kANEDCompilerQoSHintKey
+ _objc_msgSend$isPath:safelyWithinDirectory:
+ _objc_msgSend$scanAllPartitionsForModel:csIdentity:expunge:allowProcessModelShare:
+ _objc_msgSend$unsignedIntValue
+ _qos_class_self
- GCC_except_table9
- ___70-[_ANEModelCacheManager scanAllPartitionsForModel:csIdentity:expunge:]_block_invoke
- ___block_descriptor_136_e8_32s40s48s56s64s72s80s88s96bs104r_e5_v8?0ls32l8s96l8s40l8s48l8r104l8s56l8s64l8s72l8s80l8s88l8
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
