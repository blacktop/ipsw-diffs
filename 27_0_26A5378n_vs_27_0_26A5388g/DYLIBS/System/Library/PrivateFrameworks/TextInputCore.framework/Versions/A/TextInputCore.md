## TextInputCore

> `/System/Library/PrivateFrameworks/TextInputCore.framework/Versions/A/TextInputCore`

### Sections with Same Size but Changed Content

- `__TEXT.__init_offsets`
- `__DATA_CONST.__const`
- `__DATA_CONST.__objc_classlist`
- `__DATA_CONST.__objc_catlist`
- `__DATA_CONST.__objc_protolist`
- `__DATA_CONST.__objc_superrefs`
- `__DATA_CONST.__got`
- `__AUTH_CONST.__objc_intobj`
- `__AUTH_CONST.__objc_dictobj`
- `__AUTH_CONST.__objc_doubleobj`
- `__AUTH.__objc_data`
- `__AUTH.__data`
- `__AUTH.__thread_vars`
- `__DATA.__data`
- `__DATA_DIRTY.__objc_data`

```diff

-3559.0.0.0.0
-  __TEXT.__text: 0x200fb8
+3562.0.0.0.0
+  __TEXT.__text: 0x20137c
   __TEXT.__init_offsets: 0xc0
-  __TEXT.__objc_methlist: 0x10018
-  __TEXT.__const: 0x2e30
-  __TEXT.__cstring: 0x12be5
+  __TEXT.__objc_methlist: 0x10060
+  __TEXT.__const: 0x2e10
+  __TEXT.__cstring: 0x12c69
   __TEXT.__dlopen_cstrs: 0x9d
-  __TEXT.__oslogstring: 0x3aaf
+  __TEXT.__oslogstring: 0x3b40
   __TEXT.__ustring: 0x7bc
-  __TEXT.__unwind_info: 0x6078
+  __TEXT.__unwind_info: 0x6080
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0
   __TEXT.__objc_classname: 0x0

   __DATA_CONST.__objc_catlist: 0x60
   __DATA_CONST.__objc_protolist: 0x180
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x94e8
+  __DATA_CONST.__objc_selrefs: 0x9518
   __DATA_CONST.__objc_superrefs: 0x6d8
-  __DATA_CONST.__objc_arraydata: 0xed8
+  __DATA_CONST.__objc_arraydata: 0xf28
   __DATA_CONST.__got: 0x14c0
-  __AUTH_CONST.__const: 0xbcb0
-  __AUTH_CONST.__cfstring: 0xfec0
-  __AUTH_CONST.__objc_const: 0x194c0
+  __AUTH_CONST.__const: 0xbd00
+  __AUTH_CONST.__cfstring: 0xff80
+  __AUTH_CONST.__objc_const: 0x195b0
   __AUTH_CONST.__weak_auth_got: 0x30
   __AUTH_CONST.__objc_intobj: 0x5e8
   __AUTH_CONST.__objc_dictobj: 0x118
-  __AUTH_CONST.__objc_arrayobj: 0x2e8
+  __AUTH_CONST.__objc_arrayobj: 0x300
   __AUTH_CONST.__objc_doubleobj: 0x10
   __AUTH_CONST.__auth_got: 0x1888
   __AUTH.__objc_data: 0x1fe0
   __AUTH.__data: 0x18
   __AUTH.__thread_vars: 0x30
   __AUTH.__thread_bss: 0x20
-  __DATA.__objc_ivar: 0x11bc
+  __DATA.__objc_ivar: 0x11d4
   __DATA.__data: 0x21c0
-  __DATA.__bss: 0x1790
+  __DATA.__bss: 0x17a0
   __DATA.__common: 0x408
   __DATA_DIRTY.__objc_data: 0x3110
   __DATA_DIRTY.__data: 0xb0

   - /usr/lib/libmecabra.dylib
   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libsqlite3.dylib
-  Functions: 10165
-  Symbols:   20460
-  CStrings:  3190
+  Functions: 10174
+  Symbols:   20478
+  CStrings:  3197
 
Symbols:
+ -[CoreTelephonyMockObject cellularImei1]
+ -[CoreTelephonyMockObject cellularImei2]
+ -[CoreTelephonyMockObject cellularNal]
+ -[CoreTelephonyMockObject initWithCellularEid:cellularImei:cellularImei1:cellularImei2:cellularNal:]
+ -[CoreTelephonyMockObject setCellularImei1:]
+ -[CoreTelephonyMockObject setCellularImei2:]
+ -[CoreTelephonyMockObject setCellularNal:]
+ OBJC_IVAR_$_CoreTelephonyMockObject._cellularImei1
+ OBJC_IVAR_$_CoreTelephonyMockObject._cellularImei2
+ OBJC_IVAR_$_CoreTelephonyMockObject._cellularNal
+ OBJC_IVAR_$_TIStickerCandidateGenerator._admissionLock
+ OBJC_IVAR_$_TIStickerCandidateGenerator._spotlightBackoffDeadlineNanos
+ OBJC_IVAR_$_TIStickerCandidateGenerator._spotlightQueryInFlight
+ __186-[TIStickerCandidateGenerator _spotlight_generateStickerCandidatesForTaxonomySearchableQueries:generativeEmojiSearchableQueries:withRenderTraits:shouldAppend:language:completionHandler:]_block_invoke_2
+ __ZZ61-[TIKeyboardInputManagerMecabra onScreenContextForCandidates]E25screenScrapingAllowedApps
+ __ZZ61-[TIKeyboardInputManagerMecabra onScreenContextForCandidates]E9onceToken
+ ___186-[TIStickerCandidateGenerator _spotlight_generateStickerCandidatesForTaxonomySearchableQueries:generativeEmojiSearchableQueries:withRenderTraits:shouldAppend:language:completionHandler:]_block_invoke_3
+ ___61-[TIKeyboardInputManagerMecabra onScreenContextForCandidates]_block_invoke
+ ___block_descriptor_56_8_32s40bs_e17_v16?0"NSArray"8l
+ _clock_gettime_nsec_np
- -[CoreTelephonyMockObject initWithCellularEid:cellularImei:]
- __ZNSt3__19to_stringEd
CStrings:
+ "%s  most_probable_lexicon_for_context_and_stems returned lexicon %u that is not owned by any loaded model; skipping single-model prediction step"
+ "DELETE FROM shapes WHERE timestamp <= ?"
+ "SELECT COUNT(*) FROM shapes WHERE string_representation LIKE ?"
+ "com.alibaba.dingtalklit"
+ "com.sina.weibo"
+ "com.soulapp.cn"
+ "com.ss.iphone.ugc.Aweme"
+ "com.tencent.ww"
+ "com.xingin.discover"
+ "unified_predictions"
- "';"
- "DELETE From shapes WHERE timestamp <= "
- "SELECT COUNT(*) FROM shapes WHERE string_representation LIKE '"
```
