## TextComposerRuntime

> `/System/Library/PrivateFrameworks/TextComposerRuntime.framework/Versions/A/TextComposerRuntime`

```diff

-  __TEXT.__text: 0x7179c
+  __TEXT.__text: 0x742cc
   __TEXT.__objc_methlist: 0x4f8
-  __TEXT.__const: 0x3b44
-  __TEXT.__cstring: 0x123f7
-  __TEXT.__oslogstring: 0x2593
+  __TEXT.__const: 0x3b64
+  __TEXT.__cstring: 0x12397
+  __TEXT.__oslogstring: 0x26b3
   __TEXT.__constg_swiftt: 0xaa4
-  __TEXT.__swift5_typeref: 0x17f1
+  __TEXT.__swift5_typeref: 0x1839
   __TEXT.__swift5_builtin: 0x64
   __TEXT.__swift5_reflstr: 0xb62
   __TEXT.__swift5_fieldmd: 0xf0c

   __TEXT.__swift5_types: 0xf4
   __TEXT.__swift_as_entry: 0x184
   __TEXT.__swift_as_ret: 0x19c
-  __TEXT.__swift_as_cont: 0x444
+  __TEXT.__swift_as_cont: 0x43c
   __TEXT.__swift5_protos: 0x10
-  __TEXT.__swift5_capture: 0xd04
-  __TEXT.__unwind_info: 0x1e70
-  __TEXT.__eh_frame: 0x5308
+  __TEXT.__swift5_capture: 0xdf4
+  __TEXT.__unwind_info: 0x1ec0
+  __TEXT.__eh_frame: 0x5370
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0
   __TEXT.__objc_classname: 0x0

   __DATA_CONST.__objc_classlist: 0x48
   __DATA_CONST.__objc_protolist: 0x28
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x398
+  __DATA_CONST.__objc_selrefs: 0x3a0
   __DATA_CONST.__objc_protorefs: 0x20
   __DATA_CONST.__got: 0x0
-  __AUTH_CONST.__const: 0x39a0
+  __AUTH_CONST.__const: 0x3c20
   __AUTH_CONST.__objc_const: 0xa90
-  __AUTH_CONST.__auth_got: 0x1678
-  __AUTH.__objc_data: 0x180
-  __AUTH.__data: 0x8b0
-  __DATA.__data: 0xcc0
-  __DATA.__bss: 0x4500
-  __DATA.__common: 0x78
-  __DATA_DIRTY.__objc_data: 0x120
-  __DATA_DIRTY.__data: 0x540
-  __DATA_DIRTY.__bss: 0x480
-  __DATA_DIRTY.__common: 0x28
+  __AUTH_CONST.__auth_got: 0x16a0
+  __AUTH.__objc_data: 0x130
+  __AUTH.__data: 0x5f0
+  __DATA.__data: 0xab8
+  __DATA.__bss: 0x3f80
+  __DATA.__common: 0x48
+  __DATA_DIRTY.__objc_data: 0x170
+  __DATA_DIRTY.__data: 0xa18
+  __DATA_DIRTY.__bss: 0xa00
+  __DATA_DIRTY.__common: 0x58
   - /System/Library/Frameworks/Foundation.framework/Versions/C/Foundation
   - /System/Library/Frameworks/FoundationModels.framework/Versions/A/FoundationModels
   - /System/Library/Frameworks/NaturalLanguage.framework/Versions/A/NaturalLanguage
   - /System/Library/PrivateFrameworks/Archetype.framework/Versions/A/Archetype
+  - /System/Library/PrivateFrameworks/CoreEmoji.framework/Versions/A/CoreEmoji
   - /System/Library/PrivateFrameworks/FeatureFlags.framework/Versions/A/FeatureFlags
   - /System/Library/PrivateFrameworks/GenerativeFunctionsInstrumentation.framework/Versions/A/GenerativeFunctionsInstrumentation
   - /System/Library/PrivateFrameworks/GenerativeModels.framework/Versions/A/GenerativeModels

   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  Functions: 2891
-  Symbols:   166
-  CStrings:  294
+  Functions: 2952
+  Symbols:   168
+  CStrings:  295
 
Sections:
~ __TEXT.__objc_methlist : content changed
~ __TEXT.__constg_swiftt : content changed
~ __TEXT.__swift5_builtin : content changed
~ __TEXT.__swift5_reflstr : content changed
~ __TEXT.__swift5_fieldmd : content changed
~ __TEXT.__swift5_assocty : content changed
~ __TEXT.__swift5_proto : content changed
~ __TEXT.__swift5_types : content changed
~ __TEXT.__swift_as_entry : content changed
~ __TEXT.__swift_as_ret : content changed
~ __TEXT.__swift5_protos : content changed
~ __DATA_CONST.__objc_classlist : content changed
~ __DATA_CONST.__objc_protolist : content changed
~ __DATA_CONST.__objc_protorefs : content changed
~ __AUTH_CONST.__objc_const : content changed
Symbols:
+ _CEMEnumerateEmojiTokensInStringWithBlock
+ _CEMStringContainsEmoji
CStrings:
+ "Falling back to legacy flow due to non-English preferred language: %s"
+ "[RewriteProcessor] Stripped extra emoji from rewrite output (%{public}ld → %{public}ld chars)"
+ "[RewriteSessionManager] Failed to mark follow-ups as seen at index %ld since no follow-ups were generated"
- " since no follow-ups were generated"
- "Failed to mark follow-ups as seen at index "

```
