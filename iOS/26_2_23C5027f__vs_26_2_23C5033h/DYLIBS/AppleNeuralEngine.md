## AppleNeuralEngine

> `/System/Library/PrivateFrameworks/AppleNeuralEngine.framework/AppleNeuralEngine`

```diff

 380.100.0.0.0
-  __TEXT.__text: 0x44950
+  __TEXT.__text: 0x44a1c
   __TEXT.__auth_stubs: 0xbd0
   __TEXT.__objc_methlist: 0x260c
   __TEXT.__const: 0x288
   __TEXT.__oslogstring: 0x80f8
   __TEXT.__cstring: 0x2da1
-  __TEXT.__gcc_except_tab: 0x5280
+  __TEXT.__gcc_except_tab: 0x5290
   __TEXT.__unwind_info: 0x1110
   __TEXT.__objc_classname: 0x2ef
   __TEXT.__objc_methname: 0x5f8a

   - /usr/lib/libcompression.dylib
   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libsandbox.1.dylib
-  UUID: 19444909-E827-37B8-96BF-5F815BE340FD
+  UUID: D241A5D3-E6EB-35E4-A306-71BBAE4045EF
   Functions: 1412
   Symbols:   4630
   CStrings:  2647
Functions:
~ __ZNKSt3__120__shared_ptr_pointerIPN3MIL10MILContextENS_14default_deleteIS2_EENS_9allocatorIS2_EEE13__get_deleterERKSt9type_info : 60 -> 64
~ -[_ANEVirtualClient(Private) doEvaluateWithModelLegacy:options:request:qos:completionEvent:error:] : 8516 -> 8536
~ -[_ANEVirtualClient compileModel:options:qos:error:] : 1728 -> 1748
~ -[_ANEVirtualClient unloadModel:options:qos:error:] : 2448 -> 2468
~ -[_ANEVirtualClient doEvaluateWithModel:options:request:qos:completionEvent:error:] : 6968 -> 6988
~ -[_ANEVirtualClient compiledModelExistsFor:] : 1016 -> 1036
~ -[_ANEVirtualClient purgeCompiledModel:] : 836 -> 856
~ -[_ANEVirtualClient compiledModelExistsMatchingHash:] : 1112 -> 1132
~ -[_ANEVirtualClient purgeCompiledModelMatchingHash:] : 848 -> 868
~ -[_ANEVirtualClient echo:] : 776 -> 796
~ -[_ANEVirtualClient doMapIOSurfacesWithModel:request:cacheInference:error:] : 3448 -> 3468

```
