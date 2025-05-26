## Summaries

> `/System/Library/Health/FeedItemPlugins/Summaries.healthplugin/Summaries`

```diff

-4146.0.1.7.0
-  __TEXT.__text: 0x2ca54c
-  __TEXT.__auth_stubs: 0x5400
+4146.1.11.3.0
+  __TEXT.__text: 0x29109c
+  __TEXT.__auth_stubs: 0x53f0
   __TEXT.__objc_methlist: 0xc8
-  __TEXT.__swift5_typeref: 0x3296
-  __TEXT.__const: 0x8084
-  __TEXT.__cstring: 0xc758
-  __TEXT.__constg_swiftt: 0x3df0
+  __TEXT.__swift5_typeref: 0x329e
+  __TEXT.__const: 0x80a4
+  __TEXT.__cstring: 0xc428
+  __TEXT.__constg_swiftt: 0x3e00
   __TEXT.__swift5_builtin: 0x118
   __TEXT.__swift5_reflstr: 0x3926
   __TEXT.__swift5_assocty: 0xe70
   __TEXT.__swift5_fieldmd: 0x2900
-  __TEXT.__swift5_capture: 0x27f4
+  __TEXT.__swift5_capture: 0x22a0
   __TEXT.__swift5_proto: 0x7a8
   __TEXT.__swift5_types: 0x334
   __TEXT.__swift5_mpenum: 0x10
   __TEXT.__swift5_protos: 0x58
-  __TEXT.__unwind_info: 0x529c
-  __TEXT.__eh_frame: 0x2fb0
+  __TEXT.__unwind_info: 0x50cc
+  __TEXT.__eh_frame: 0x2fe8
   __TEXT.__objc_classname: 0x67
   __TEXT.__objc_methname: 0x3604
   __TEXT.__objc_methtype: 0x252
-  __DATA_CONST.__got: 0x13e0
+  __DATA_CONST.__got: 0x1410
   __DATA_CONST.__const: 0x168
   __DATA_CONST.__objc_classlist: 0x210
   __DATA_CONST.__objc_catlist: 0x10
   __DATA_CONST.__objc_protolist: 0x40
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_const: 0x35c0
-  __DATA_CONST.__objc_selrefs: 0x13c8
-  __AUTH_CONST.__const: 0x9d50
+  __DATA_CONST.__objc_selrefs: 0x13c0
+  __AUTH_CONST.__const: 0x9550
   __AUTH_CONST.__auth_ptr: 0x448
   __AUTH_CONST.__objc_const: 0x80
-  __AUTH_CONST.__auth_got: 0x2a00
-  __AUTH.__data: 0x2258
+  __AUTH_CONST.__auth_got: 0x29f8
+  __AUTH.__data: 0x21f0
   __AUTH.__objc_data: 0x380
   __DATA.__objc_protorefs: 0x20
   __DATA.__objc_classrefs: 0x500
   __DATA.__objc_data: 0xd8
-  __DATA.__data: 0x1bf8
+  __DATA.__data: 0x1cc8
   __DATA.__objc_stublist: 0x30
   __DATA.__bss: 0x5180
   __DATA.__common: 0xa0
   __DATA_DIRTY.__objc_data: 0x1470
-  __DATA_DIRTY.__data: 0x86d0
+  __DATA_DIRTY.__data: 0x8650
   __DATA_DIRTY.__bss: 0x6a80
   __DATA_DIRTY.__common: 0x420
   - /System/Library/Frameworks/Combine.framework/Combine

   - /usr/lib/swift/libswiftXPC.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  Functions: 7749
+  Functions: 7533
   Symbols:   423
-  CStrings:  1618
+  CStrings:  1610
 
CStrings:
+ "Map<AnyPublisher<DataTypeContentConfigurationContext, Never>, Request>"
+ "SummariesSharableModelGeneratorPipeline"
+ "[%s] Anchored change received, emitting generation signal for %s"
+ "[%s] Unanchored change received, emitting unanchored generation signal for %s"
+ "[%s]_%s_%s: Failed to create requests publisher: %s"
+ "[%s]_<%s>_%s: Emitting reuse for %ld shared summaries"
+ "[%s]_<%s>_%s: Emitting updateAnchorMetadata for %ld sharable models to anchor %s"
- "[%s)]_%s: Emitting request through unanchored changes publisher: %s"
- "[%s)]_%s: Received upstream request, passing through unanchored changes publisher: %s"
- "[%s]_%s: Given anchor is nil and we have a previous model for %s, generation is not necessary"
- "[%s]_%s: New change and anchor for %s, generation is necessary"
- "[%s]_%s: No previous model for %s, generation is necessary"
- "[%s]_%s: No relevant change emitted for %s, using existing data with new anchor"
- "[%s]_%s: Previous anchor is the same for %s, generation is not necessary"
- "[%s]_%s: Previous data is unreadable for %s, generation is necessary"
- "[%s]_%s: Previous model for %s has different version %s instead of %s, generation is necessary"
- "[%s]_%s: Previous model has different anchor %@ compared to %@, comparing change"
- "[%s]_%s: Previous summary data for %s has different version %s instead of %s, generation is necessary"
- "[%s]_%s: Processing %ld previous model to compute new model for %s and typeState %s"
- "[%s]_%s: Received a change with an anchor in background mode for %s, generating new model regardless of anchor value"
- "[%s]_%s: more than one previous model returned for identifier %s: %s"
- "[%s]_%s: request for %s is for unanchored change, generation is necessary"

```
