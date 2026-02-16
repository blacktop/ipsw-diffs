## SIDInferenceProvider

> `/System/Library/ExtensionKit/Extensions/SIDInferenceProvider.appex/SIDInferenceProvider`

```diff

-1.33.0.0.0
-  __TEXT.__text: 0xc7e0
-  __TEXT.__auth_stubs: 0xea0
-  __TEXT.__objc_stubs: 0x2c0
+1.36.0.0.0
+  __TEXT.__text: 0x112a8
+  __TEXT.__auth_stubs: 0xed0
+  __TEXT.__objc_stubs: 0x360
   __TEXT.__objc_methlist: 0x80
-  __TEXT.__const: 0x51a
+  __TEXT.__const: 0x55a
   __TEXT.__gcc_except_tab: 0x55c
-  __TEXT.__cstring: 0x79f
-  __TEXT.__objc_classname: 0x10
-  __TEXT.__objc_methname: 0x2b3
-  __TEXT.__objc_methtype: 0xa2f
-  __TEXT.__swift5_typeref: 0x18c
+  __TEXT.__cstring: 0x83f
+  __TEXT.__objc_classname: 0x81
+  __TEXT.__objc_methtype: 0xa06
+  __TEXT.__swift5_typeref: 0x1b8
+  __TEXT.__oslogstring: 0x54c
   __TEXT.__swift5_entry: 0x8
-  __TEXT.__constg_swiftt: 0x154
-  __TEXT.__swift5_fieldmd: 0x98
-  __TEXT.__swift5_reflstr: 0x5c
+  __TEXT.__constg_swiftt: 0x140
+  __TEXT.__swift5_fieldmd: 0x8c
+  __TEXT.__objc_methname: 0x2cd
+  __TEXT.__swift5_reflstr: 0x54
   __TEXT.__swift5_assocty: 0x90
-  __TEXT.__oslogstring: 0x8c
   __TEXT.__swift5_proto: 0x2c
   __TEXT.__swift5_types: 0x14
-  __TEXT.__swift_as_entry: 0x48
-  __TEXT.__swift_as_ret: 0x30
-  __TEXT.__unwind_info: 0x3c0
-  __TEXT.__eh_frame: 0x798
-  __DATA_CONST.__auth_got: 0x760
-  __DATA_CONST.__got: 0x218
-  __DATA_CONST.__auth_ptr: 0x1a8
-  __DATA_CONST.__const: 0x1b8
+  __TEXT.__swift_as_entry: 0x54
+  __TEXT.__swift_as_ret: 0x54
+  __TEXT.__unwind_info: 0x4a8
+  __TEXT.__eh_frame: 0xd30
+  __DATA_CONST.__auth_got: 0x778
+  __DATA_CONST.__got: 0x228
+  __DATA_CONST.__auth_ptr: 0x1b8
+  __DATA_CONST.__const: 0x1b0
   __DATA_CONST.__cfstring: 0x3a0
   __DATA_CONST.__objc_classlist: 0x10
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA.__objc_const: 0x188
+  __DATA.__objc_const: 0x1b0
   __DATA.__objc_selrefs: 0xd8
-  __DATA.__objc_data: 0xe8
-  __DATA.__data: 0x330
+  __DATA.__objc_data: 0x98
+  __DATA.__data: 0x318
   __DATA.__bss: 0x580
   __DATA.__common: 0x10
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation

   - /usr/lib/libc++.1.dylib
   - /usr/lib/libobjc.A.dylib
   - /usr/lib/swift/libswiftAccelerate.dylib
-  - /usr/lib/swift/libswiftCompression.dylib
   - /usr/lib/swift/libswiftCore.dylib
   - /usr/lib/swift/libswiftCoreAudio.dylib
   - /usr/lib/swift/libswiftCoreFoundation.dylib

   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  UUID: 91417251-8346-3CBD-AA7A-3F823BCFD01A
-  Functions: 180
-  Symbols:   186
-  CStrings:  125
+  UUID: 2F684033-03E2-3A55-B4F8-9AA1A6986E3A
+  Functions: 211
+  Symbols:   185
+  CStrings:  139
 
Symbols:
+ __ZNSt3__132__internal_log_hardening_failureEPKc
+ __swift_stdlib_bridgeErrorToNSError
+ _objc_release_x27
+ _objc_retain_x23
+ _swift_arrayDestroy
+ _swift_bridgeObjectRelease_n
- __swift_FORCE_LOAD_$_swiftCompression
- _objc_claimAutoreleasedReturnValue
- _objc_retain
- _objc_retain_x2
- _objc_retain_x3
- _objc_retain_x8
- _swift_updateClassMetadata2
CStrings:
+ "/AppleInternal/Library/BuildRoots/4~CH9kugDcmYeri276z06EC0xRIi63FPJkrN3EPjU/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/__vector/vector.h:406: libc++ Hardening assertion __n < size() failed: vector[] index out of bounds\n"
+ "@64@0:8{unordered_map<std::string, e5rt_io_port *, std::hash<std::string>, std::equal_to<std::string>, std::allocator<std::pair<const std::string, e5rt_io_port *>>>={__hash_table<std::__hash_value_type<std::string, e5rt_io_port *>, std::__unordered_map_hasher<std::string, std::pair<const std::string, e5rt_io_port *>, std::hash<std::string>, std::equal_to<std::string>>, std::__unordered_map_equal<std::string, std::pair<const std::string, e5rt_io_port *>, std::equal_to<std::string>, std::hash<std::string>>, std::allocator<std::pair<const std::string, e5rt_io_port *>>>={unique_ptr<std::__hash_node_base<std::__hash_node<std::__hash_value_type<std::string, e5rt_io_port *>, void *> *> *[], std::__bucket_list_deallocator<std::allocator<std::__hash_node_base<std::__hash_node<std::__hash_value_type<std::string, e5rt_io_port *>, void *> *> *>>>={?=^^v{__bucket_list_deallocator<std::allocator<std::__hash_node_base<std::__hash_node<std::__hash_value_type<std::string, e5rt_io_port *>, void *> *> *>>={?=Q}}}}{?={__hash_node_base<std::__hash_node<std::__hash_value_type<std::string, e5rt_io_port *>, void *> *>=^v}}{?=Q}{?=f}}}16^@56"
+ "E5RT compilation failed: "
+ "Expected inference workflow for use case: "
+ "Model is unavailable for identifier: "
+ "No workflow found for use case: "
+ "[SIDInferenceProvider][compileESOP] Calling SIDE5Operations.compileAndRetrieveESOP"
+ "[SIDInferenceProvider][compileESOP] Error details: %s"
+ "[SIDInferenceProvider][compileESOP] Retrieved model path: %s"
+ "[SIDInferenceProvider][compileESOP] SIDE5Operations.compileAndRetrieveESOP failed with error: %@"
+ "[SIDInferenceProvider][compileESOP] Successfully compiled ESOP for model: %s"
+ "[SIDInferenceProvider][getWorkflowAndESOP] Compiling ESOP for model: %s"
+ "[SIDInferenceProvider][getWorkflowAndESOP] Successfully compiled and cached ESOP for model: %s"
+ "[SIDInferenceProvider][getWorkflowAndESOP] Using cached ESOP for model: %s"
+ "[SIDInferenceProvider][loadAsset] ESOP already cached for model: %s"
+ "[SIDInferenceProvider][loadAsset] Successfully compiled and cached ESOP for model: %s"
+ "[SIDInferenceProvider][transitionAsset] Error during unload: %@"
+ "[SIDInferenceProvider][transitionAsset] Fetching workflow for asset identifier %s"
+ "[SIDInferenceProvider][transitionAsset] No cached ESOP found for asset: %s, model: %s"
+ "[SIDInferenceProvider][transitionAsset] No workflow found for asset: %s"
+ "[SIDInferenceProvider][transitionAsset] Successfully unloaded asset: %s, model: %s"
+ "cachedESOPs"
+ "{unordered_map<std::string, e5rt_io_port *, std::hash<std::string>, std::equal_to<std::string>, std::allocator<std::pair<const std::string, e5rt_io_port *>>>={__hash_table<std::__hash_value_type<std::string, e5rt_io_port *>, std::__unordered_map_hasher<std::string, std::pair<const std::string, e5rt_io_port *>, std::hash<std::string>, std::equal_to<std::string>>, std::__unordered_map_equal<std::string, std::pair<const std::string, e5rt_io_port *>, std::equal_to<std::string>, std::hash<std::string>>, std::allocator<std::pair<const std::string, e5rt_io_port *>>>={unique_ptr<std::__hash_node_base<std::__hash_node<std::__hash_value_type<std::string, e5rt_io_port *>, void *> *> *[], std::__bucket_list_deallocator<std::allocator<std::__hash_node_base<std::__hash_node<std::__hash_value_type<std::string, e5rt_io_port *>, void *> *> *>>>={?=^^v{__bucket_list_deallocator<std::allocator<std::__hash_node_base<std::__hash_node<std::__hash_value_type<std::string, e5rt_io_port *>, void *> *> *>>={?=Q}}}}{?={__hash_node_base<std::__hash_node<std::__hash_value_type<std::string, e5rt_io_port *>, void *> *>=^v}}{?=Q}{?=f}}}32@0:8^{e5rt_execution_stream_operation=}16^@24"
- "@64@0:8{unordered_map<std::string, e5rt_io_port *, std::hash<std::string>, std::equal_to<std::string>, std::allocator<std::pair<const std::string, e5rt_io_port *>>>={__hash_table<std::__hash_value_type<std::string, e5rt_io_port *>, std::__unordered_map_hasher<std::string, std::__hash_value_type<std::string, e5rt_io_port *>, std::hash<std::string>, std::equal_to<std::string>>, std::__unordered_map_equal<std::string, std::__hash_value_type<std::string, e5rt_io_port *>, std::equal_to<std::string>, std::hash<std::string>>, std::allocator<std::__hash_value_type<std::string, e5rt_io_port *>>>={unique_ptr<std::__hash_node_base<std::__hash_node<std::__hash_value_type<std::string, e5rt_io_port *>, void *> *> *[], std::__bucket_list_deallocator<std::allocator<std::__hash_node_base<std::__hash_node<std::__hash_value_type<std::string, e5rt_io_port *>, void *> *> *>>>={?=^^v{__bucket_list_deallocator<std::allocator<std::__hash_node_base<std::__hash_node<std::__hash_value_type<std::string, e5rt_io_port *>, void *> *> *>>={?=Q}}}}{?={__hash_node_base<std::__hash_node<std::__hash_value_type<std::string, e5rt_io_port *>, void *> *>=^v}}{?=Q}{?=f}}}16^@56"
- "ESOP is not loaded."
- "Failed to compile the model at "
- "Model is unavailable."
- "The workflow was not successfully loaded in loadAssets"
- "[SIDInferenceProvider][loadAsset] Retrieved model path: %s"
- "esopHandle"
- "workflow"
- "{unordered_map<std::string, e5rt_io_port *, std::hash<std::string>, std::equal_to<std::string>, std::allocator<std::pair<const std::string, e5rt_io_port *>>>={__hash_table<std::__hash_value_type<std::string, e5rt_io_port *>, std::__unordered_map_hasher<std::string, std::__hash_value_type<std::string, e5rt_io_port *>, std::hash<std::string>, std::equal_to<std::string>>, std::__unordered_map_equal<std::string, std::__hash_value_type<std::string, e5rt_io_port *>, std::equal_to<std::string>, std::hash<std::string>>, std::allocator<std::__hash_value_type<std::string, e5rt_io_port *>>>={unique_ptr<std::__hash_node_base<std::__hash_node<std::__hash_value_type<std::string, e5rt_io_port *>, void *> *> *[], std::__bucket_list_deallocator<std::allocator<std::__hash_node_base<std::__hash_node<std::__hash_value_type<std::string, e5rt_io_port *>, void *> *> *>>>={?=^^v{__bucket_list_deallocator<std::allocator<std::__hash_node_base<std::__hash_node<std::__hash_value_type<std::string, e5rt_io_port *>, void *> *> *>>={?=Q}}}}{?={__hash_node_base<std::__hash_node<std::__hash_value_type<std::string, e5rt_io_port *>, void *> *>=^v}}{?=Q}{?=f}}}32@0:8^{e5rt_execution_stream_operation=}16^@24"

```
