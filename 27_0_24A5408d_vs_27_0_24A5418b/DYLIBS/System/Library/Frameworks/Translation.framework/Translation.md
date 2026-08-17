## Translation

> `/System/Library/Frameworks/Translation.framework/Translation`

```diff

-388.0.0.0.0
-  __TEXT.__text: 0x5cb08
+389.1.0.0.0
+  __TEXT.__text: 0x5ccc4
   __TEXT.__objc_methlist: 0x5e10
   __TEXT.__const: 0xf68
-  __TEXT.__cstring: 0x3414
-  __TEXT.__oslogstring: 0x5306
+  __TEXT.__cstring: 0x3464
+  __TEXT.__oslogstring: 0x5336
   __TEXT.__gcc_except_tab: 0xb44
   __TEXT.__ustring: 0x90
   __TEXT.__swift5_typeref: 0x607

   __TEXT.__swift_as_entry: 0x4c
   __TEXT.__swift_as_ret: 0x50
   __TEXT.__swift_as_cont: 0x84
-  __TEXT.__unwind_info: 0x1c78
+  __TEXT.__unwind_info: 0x1c80
   __TEXT.__eh_frame: 0x8e8
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0
   __TEXT.__objc_classname: 0x0
   __TEXT.__objc_methname: 0x0
   __TEXT.__objc_methtype: 0x0
-  __DATA_CONST.__const: 0x1ea0
+  __DATA_CONST.__const: 0x1ed0
   __DATA_CONST.__objc_classlist: 0x330
   __DATA_CONST.__objc_catlist: 0x38
   __DATA_CONST.__objc_protolist: 0x98

   __DATA_CONST.__objc_arraydata: 0x1a0
   __DATA_CONST.__got: 0x5a0
   __AUTH_CONST.__const: 0x1050
-  __AUTH_CONST.__cfstring: 0x3d60
+  __AUTH_CONST.__cfstring: 0x3e40
   __AUTH_CONST.__objc_const: 0xc0f8
   __AUTH_CONST.__objc_arrayobj: 0xf0
   __AUTH_CONST.__objc_intobj: 0x90

   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  Functions: 2896
-  Symbols:   5324
-  CStrings:  944
+  Functions: 2897
+  Symbols:   5325
+  CStrings:  952
 
Symbols:
+ __LTEngineInfoDescription
Functions:
+ __LTEngineInfoDescription
~ ___72-[_LTParagraphTranslationRequest _startTranslationWithTextService:done:]_block_invoke_2 : 168 -> 272
~ -[_LTTextToSpeechTranslationRequest translatorDidTranslate:] : 188 -> 300
~ -[_LTTranslationSession paragraphTranslation:result:error:] : 352 -> 464
CStrings:
+ "Translation completed using engine: %{public}@"
+ "ai-afm-lora"
+ "ai-ifp-lora"
+ "ai-mt-expert"
+ "none"
+ "traditional"
+ "traditional-server"
+ "unknown(%ld)"
```
