## EmbeddingCore

> `/System/Library/PrivateFrameworks/EmbeddingCore.framework/EmbeddingCore`

```diff

-470.4.2.0.0
-  __TEXT.__text: 0x697e8
-  __TEXT.__objc_methlist: 0x19cc
+470.7.1.0.0
+  __TEXT.__text: 0x68b2c
+  __TEXT.__objc_methlist: 0x194c
   __TEXT.__const: 0x1180
-  __TEXT.__gcc_except_tab: 0x7340
-  __TEXT.__cstring: 0x5ae2
-  __TEXT.__oslogstring: 0x192f
+  __TEXT.__gcc_except_tab: 0x7220
+  __TEXT.__cstring: 0x5a82
+  __TEXT.__oslogstring: 0x169f
   __TEXT.__dlopen_cstrs: 0x5e
   __TEXT.__swift5_typeref: 0xd9
   __TEXT.__constg_swiftt: 0x1b8

   __TEXT.__swift5_fieldmd: 0xec
   __TEXT.__swift5_proto: 0x8
   __TEXT.__swift5_types: 0x14
-  __TEXT.__unwind_info: 0x2f10
+  __TEXT.__unwind_info: 0x2ec0
   __TEXT.__eh_frame: 0xb0
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0

   __TEXT.__objc_methname: 0x0
   __TEXT.__objc_methtype: 0x0
   __DATA_CONST.__const: 0x5d8
-  __DATA_CONST.__objc_classlist: 0x190
+  __DATA_CONST.__objc_classlist: 0x188
   __DATA_CONST.__objc_protolist: 0x18
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__weak_got: 0x18
-  __DATA_CONST.__objc_selrefs: 0xd38
-  __DATA_CONST.__objc_superrefs: 0xa0
-  __DATA_CONST.__objc_arraydata: 0x378
+  __DATA_CONST.__objc_selrefs: 0xd28
+  __DATA_CONST.__objc_superrefs: 0x98
+  __DATA_CONST.__objc_arraydata: 0x370
   __DATA_CONST.__got: 0x3c8
   __AUTH_CONST.__const: 0x1920
-  __AUTH_CONST.__cfstring: 0x1b20
-  __AUTH_CONST.__objc_const: 0x3aa8
+  __AUTH_CONST.__cfstring: 0x1aa0
+  __AUTH_CONST.__objc_const: 0x39a0
   __AUTH_CONST.__weak_auth_got: 0x50
-  __AUTH_CONST.__objc_intobj: 0x168
-  __AUTH_CONST.__objc_arrayobj: 0x240
+  __AUTH_CONST.__objc_intobj: 0x150
+  __AUTH_CONST.__objc_arrayobj: 0x228
   __AUTH_CONST.__objc_dictobj: 0x78
   __AUTH_CONST.__objc_floatobj: 0x10
   __AUTH_CONST.__auth_got: 0xa88
   __AUTH.__objc_data: 0xa0
   __AUTH.__thread_vars: 0x30
   __AUTH.__thread_bss: 0x10
-  __DATA.__objc_ivar: 0x284
+  __DATA.__objc_ivar: 0x278
   __DATA.__data: 0xc4
   __DATA.__common: 0x2fd
-  __DATA_DIRTY.__objc_data: 0x11c0
+  __DATA_DIRTY.__objc_data: 0x1170
   __DATA_DIRTY.__data: 0x3d8
   __DATA_DIRTY.__bss: 0xe0
   __DATA_DIRTY.__common: 0xf0

   - /usr/lib/swift/libswiftXPC.dylib
   - /usr/lib/swift/libswift_Builtin_float.dylib
   - /usr/lib/swift/libswiftos.dylib
-  Functions: 2096
-  Symbols:   3345
-  CStrings:  745
+  Functions: 2075
+  Symbols:   3326
+  CStrings:  729
 
Symbols:
+ -[MADCrossEncoderRequestContext batchSizeOverride]
+ -[MADCrossEncoderRequestContext setBatchSizeOverride:]
+ GCC_except_table146
+ _OBJC_CLASS_$_NSCache
+ _OBJC_IVAR_$_MADCrossEncoder._documentTokenCache
+ _OBJC_IVAR_$_MADCrossEncoder._documentTokenCacheMaxEntryBytes
+ _OBJC_IVAR_$_MADCrossEncoderRequestContext._batchSizeOverride
+ __ZL13PickBatchSizemm
- +[MADSafariTextEmbeddingAdapter createForEmbeddingVersion:computeUnits:extendedContextLength:]
- -[MADSafariTextEmbeddingAdapter .cxx_destruct]
- -[MADSafariTextEmbeddingAdapter _loadResources]
- -[MADSafariTextEmbeddingAdapter _runWithSpatial:eosPosition:output:]
- -[MADSafariTextEmbeddingAdapter initWithComputeUnits:extendedContextLength:]
- -[MADSafariTextEmbeddingAdapter loadResources]
- -[MADSafariTextEmbeddingAdapter runWithSpatial:eosPosition:output:]
- -[MADTextEncoderE5MLNetworkOutput eosPosition]
- -[MADTextEncoderE5MLNetworkOutput setEosPosition:]
- -[MADTextEncoderOutput eosPosition]
- -[MADTextEncoderOutput setEosPosition:]
- _OBJC_CLASS_$_MADSafariTextEmbeddingAdapter
- _OBJC_IVAR_$_MADSafariTextEmbeddingAdapter._computeUnits
- _OBJC_IVAR_$_MADSafariTextEmbeddingAdapter._extendedContextLength
- _OBJC_IVAR_$_MADSafariTextEmbeddingAdapter._inference
- _OBJC_IVAR_$_MADSafariTextEmbeddingAdapter._queue
- _OBJC_IVAR_$_MADTextEncoderE5MLNetworkOutput._eosPosition
- _OBJC_IVAR_$_MADTextEncoderOutput._eosPosition
- _OBJC_METACLASS_$_MADSafariTextEmbeddingAdapter
- __OBJC_$_CLASS_METHODS_MADSafariTextEmbeddingAdapter
- __OBJC_$_INSTANCE_METHODS_MADSafariTextEmbeddingAdapter
- __OBJC_$_INSTANCE_VARIABLES_MADSafariTextEmbeddingAdapter
- __OBJC_CLASS_RO_$_MADSafariTextEmbeddingAdapter
- __OBJC_METACLASS_RO_$_MADSafariTextEmbeddingAdapter
- __ZL13PickBatchSizem
- ___46-[MADSafariTextEmbeddingAdapter loadResources]_block_invoke
- ___67-[MADSafariTextEmbeddingAdapter runWithSpatial:eosPosition:output:]_block_invoke
CStrings:
+ "#"
- "MADSafariTextEmbeddingAdapter"
- "MADSafariTextEmbeddingAdapter_loadResources"
- "MADSafariTextEmbeddingAdapter_run"
- "SystemSearch/v8.0.0"
- "[Text|SafariAdapter] Embedding version %d has no Safari head"
- "[Text|SafariAdapter] adapter inference failed (%@)"
- "[Text|SafariAdapter] adapter model not found in bundle"
- "[Text|SafariAdapter] adapter produced no output"
- "[Text|SafariAdapter] failed to create eos_pos input (%@)"
- "[Text|SafariAdapter] failed to create spatial input (%@)"
- "[Text|SafariAdapter] failed to load adapter model"
- "[Text|SafariAdapter] failed to load adapter model (%@)"
- "[Text|SafariAdapter] failed to set inputs (%@)"
- "[Text|SafariAdapter] spatial length (%@) does not match the selected function's input (%@)"
- "eos_pos"
- "md8-safari-adapter"
- "spatial"
```
