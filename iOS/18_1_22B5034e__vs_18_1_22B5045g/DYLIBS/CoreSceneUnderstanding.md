## CoreSceneUnderstanding

> `/System/Library/PrivateFrameworks/CoreSceneUnderstanding.framework/CoreSceneUnderstanding`

```diff

-55.0.0.0.0
-  __TEXT.__text: 0xc1c54
-  __TEXT.__auth_stubs: 0x1490
+56.0.0.0.0
+  __TEXT.__text: 0xc3c34
+  __TEXT.__auth_stubs: 0x1500
   __TEXT.__init_offsets: 0x4
-  __TEXT.__objc_methlist: 0x3538
-  __TEXT.__const: 0x1eb0
-  __TEXT.__gcc_except_tab: 0xe784
-  __TEXT.__cstring: 0x8a65
-  __TEXT.__oslogstring: 0xa68
-  __TEXT.__swift5_typeref: 0x4b
-  __TEXT.__constg_swiftt: 0x70
+  __TEXT.__objc_methlist: 0x3650
+  __TEXT.__const: 0x1f10
+  __TEXT.__gcc_except_tab: 0xeaa8
+  __TEXT.__cstring: 0x8bc5
+  __TEXT.__oslogstring: 0xb68
+  __TEXT.__swift5_typeref: 0x69
+  __TEXT.__constg_swiftt: 0xe8
   __TEXT.__swift5_builtin: 0x14
   __TEXT.__swift5_mpenum: 0x8
-  __TEXT.__swift5_reflstr: 0x44
-  __TEXT.__swift5_fieldmd: 0x5c
+  __TEXT.__swift5_reflstr: 0x83
+  __TEXT.__swift5_fieldmd: 0x9c
   __TEXT.__swift5_proto: 0x8
-  __TEXT.__swift5_types: 0x8
-  __TEXT.__unwind_info: 0x43d0
+  __TEXT.__swift5_types: 0xc
+  __TEXT.__unwind_info: 0x44a0
   __TEXT.__eh_frame: 0x48
-  __TEXT.__objc_classname: 0xb26
-  __TEXT.__objc_methname: 0xb000
+  __TEXT.__objc_classname: 0xb29
+  __TEXT.__objc_methname: 0xb323
   __TEXT.__objc_methtype: 0x5a60
-  __TEXT.__objc_stubs: 0x45c0
-  __DATA_CONST.__got: 0x480
-  __DATA_CONST.__const: 0x758
-  __DATA_CONST.__objc_classlist: 0x300
+  __TEXT.__objc_stubs: 0x47e0
+  __DATA_CONST.__got: 0x488
+  __DATA_CONST.__const: 0x738
+  __DATA_CONST.__objc_classlist: 0x308
   __DATA_CONST.__objc_catlist: 0x8
   __DATA_CONST.__objc_protolist: 0x28
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x19d8
+  __DATA_CONST.__objc_selrefs: 0x1a68
   __DATA_CONST.__objc_superrefs: 0x208
-  __DATA_CONST.__objc_arraydata: 0x360
-  __AUTH_CONST.__auth_got: 0xa58
-  __AUTH_CONST.__auth_ptr: 0x90
+  __DATA_CONST.__objc_arraydata: 0x3f0
+  __AUTH_CONST.__auth_got: 0xa98
+  __AUTH_CONST.__auth_ptr: 0xa0
   __AUTH_CONST.__const: 0x2718
-  __AUTH_CONST.__cfstring: 0x33c0
-  __AUTH_CONST.__objc_const: 0x8ce8
-  __AUTH_CONST.__objc_intobj: 0x180
-  __AUTH_CONST.__objc_arrayobj: 0x240
-  __AUTH_CONST.__objc_dictobj: 0x78
+  __AUTH_CONST.__cfstring: 0x3480
+  __AUTH_CONST.__objc_const: 0x8ec8
+  __AUTH_CONST.__objc_intobj: 0x168
+  __AUTH_CONST.__objc_arrayobj: 0x258
+  __AUTH_CONST.__objc_dictobj: 0xa0
   __AUTH_CONST.__objc_floatobj: 0x10
-  __AUTH.__objc_data: 0x1e78
-  __AUTH.__data: 0x140
+  __AUTH.__objc_data: 0x1f80
+  __AUTH.__data: 0x168
   __AUTH.__thread_vars: 0x30
   __AUTH.__thread_bss: 0x9c9
-  __DATA.__objc_ivar: 0x684
-  __DATA.__data: 0x358
-  __DATA.__bss: 0x1c1
-  __DATA.__common: 0x3c8
+  __DATA.__objc_ivar: 0x6a0
+  __DATA.__data: 0x370
+  __DATA.__bss: 0x1d1
+  __DATA.__common: 0x3d8
   __DATA_DIRTY.__common: 0x8
   - /System/Library/Frameworks/Accelerate.framework/Accelerate
   - /System/Library/Frameworks/CoreData.framework/CoreData

   - /usr/lib/swift/libswiftsimd.dylib
   - /usr/lib/swift/libswiftsys_time.dylib
   - /usr/lib/swift/libswiftunistd.dylib
-  Functions: 2944
-  Symbols:   576
-  CStrings:  2802
+  Functions: 2992
+  Symbols:   581
+  CStrings:  2844
 
Symbols:
+ _OBJC_EHTYPE_$_NSException
+ _swift_endAccess
+ _swift_beginAccess
+ ___objc_personality_v0
+ _objc_retainAutoreleasedReturnValue
+ _swift_allocBox
- _swift_bridgeObjectRelease_n
CStrings:
+ "\x02\x14"
+ "setTextEncoderNetworkURL:"
+ "fetchWithAssetLock:error:"
+ "callStackSymbols"
+ "getAssetVersion"
+ "modelLock"
+ "_headModelURL"
+ "_tokenEmbeddingNetworkURL"
+ "_sideLoaded"
+ "Exception Name: %!@(MISSING)\nReason: %!@(MISSING)\nCall Stack: %!@(MISSING)"
+ "reason"
+ "headModelURL"
+ "getConfigurationForCSUSmileySpotter_v2_0_EnglishWithError:"
+ "Could not aquire lock for model catalog resource!"
+ "smileyspotter_v3.0_fjuxk2wg9j-59976md4_te-md4.mlmodelc"
+ "T@\"NSURL\",C,N,V_textEncoderNetworkURL"
+ "text_model_md4_mubb.mlmodelc"
+ "\x11\x11"
+ "setHeadModelURL:"
+ "textEncoderNetworkURL"
+ "_textEncoderNetworkURL"
+ "new ModelCatalog assets available for Smiley Spotter - reloading"
+ "loadModelCatalogResourcesWithAssetLock:Error:"
+ "absoluteString"
+ "assetVersionNumber"
+ "Tried to obtain an asset with a missing lock!"
+ "Predictor instance is nil, are you sure you loadedResources(...)?"
+ "token_model_md4_mubb.mlmodelc"
+ "T@\"NSURL\",C,N,V_tokenEmbeddingNetworkURL"
+ "overrideWithSideLoadedPathForSmileySpotterModel:"
+ "overrideWithSideLoadedPathForTokenEmbeddingModel:TextEmbeddingModel:"
+ "TB,N,V_sideLoaded"
+ "setTokenEmbeddingNetworkURL:"
+ "unsafeRunSmileySpotterOnTextEncoding:error:"
+ "Models side loaded from %!@(MISSING)"
+ "sideLoaded"
+ "TB,V_sideLoaded"
+ "tokenEmbeddingNetworkURL"
+ "T@\"NSURL\",&,V_headModelURL"
+ "fileURLWithPath:isDirectory:"
+ "private/var/mobile/Library/Application Support/com.apple.VisualGeneration/OVERRIDE"
+ "loadResourcesInternal:"
+ "!59"
+ "setSideLoaded:"
+ "getConfigurationFromModelCatalogForRevision_v4_1_Tier0WithError:"
+ "_assetVersionNumber"
+ "new ModelCatalog assets available for text encoder - reloading"
- "URLByAppendingPathComponent:"
- "\x01\x11"
- "!39"
- "path"
- "Smiley Spotter model file not found in bundle!"
- "fetchAndReturnError:"

```
