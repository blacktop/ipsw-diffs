## Translation

> `/System/Library/Frameworks/Translation.framework/Versions/A/Translation`

```diff

-300.2.0.0.0
-  __TEXT.__text: 0x4a720
-  __TEXT.__auth_stubs: 0xb40
-  __TEXT.__objc_methlist: 0x4500
+300.12.0.0.0
+  __TEXT.__text: 0x4a764
+  __TEXT.__auth_stubs: 0xb80
+  __TEXT.__objc_methlist: 0x4aa0
   __TEXT.__const: 0x558
-  __TEXT.__cstring: 0x285e
-  __TEXT.__oslogstring: 0x3d86
+  __TEXT.__cstring: 0x283e
+  __TEXT.__oslogstring: 0x3ed6
   __TEXT.__gcc_except_tab: 0xa10
-  __TEXT.__swift5_typeref: 0x219
+  __TEXT.__swift5_typeref: 0x24f
   __TEXT.__swift5_capture: 0xb0
   __TEXT.__constg_swiftt: 0x1fc
   __TEXT.__swift5_reflstr: 0x1f2
   __TEXT.__swift5_fieldmd: 0x1fc
   __TEXT.__swift5_proto: 0x24
   __TEXT.__swift5_types: 0x28
+  __TEXT.__swift_as_entry: 0x24
+  __TEXT.__swift_as_ret: 0x24
   __TEXT.__swift5_assocty: 0x48
-  __TEXT.__unwind_info: 0x15a0
+  __TEXT.__unwind_info: 0x1598
   __TEXT.__eh_frame: 0x3c0
-  __TEXT.__objc_classname: 0xa05
-  __TEXT.__objc_methname: 0x9b49
+  __TEXT.__objc_classname: 0xa08
+  __TEXT.__objc_methname: 0x9b85
   __TEXT.__objc_methtype: 0x178b
-  __TEXT.__objc_stubs: 0x55a0
-  __DATA_CONST.__got: 0x3f0
-  __DATA_CONST.__const: 0x550
+  __TEXT.__objc_stubs: 0x55e0
+  __DATA_CONST.__got: 0x408
+  __DATA_CONST.__const: 0x520
   __DATA_CONST.__objc_classlist: 0x270
   __DATA_CONST.__objc_catlist: 0x30
   __DATA_CONST.__objc_protolist: 0x88
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x1f58
+  __DATA_CONST.__objc_selrefs: 0x1ff8
   __DATA_CONST.__objc_protorefs: 0x18
   __DATA_CONST.__objc_superrefs: 0x220
   __DATA_CONST.__objc_arraydata: 0x48
-  __AUTH_CONST.__auth_got: 0x5b0
-  __AUTH_CONST.__const: 0x21b0
-  __AUTH_CONST.__cfstring: 0x2a60
-  __AUTH_CONST.__objc_const: 0xa020
+  __AUTH_CONST.__auth_got: 0x5d0
+  __AUTH_CONST.__const: 0x2200
+  __AUTH_CONST.__cfstring: 0x2a80
+  __AUTH_CONST.__objc_const: 0x9618
   __AUTH_CONST.__objc_arrayobj: 0x30
   __AUTH_CONST.__objc_intobj: 0x78
   __AUTH_CONST.__objc_dictobj: 0x28
   __AUTH.__objc_data: 0x1310
   __AUTH.__data: 0x440
-  __DATA.__objc_ivar: 0x6bc
-  __DATA.__data: 0x920
+  __DATA.__objc_ivar: 0x6c4
+  __DATA.__data: 0x940
   __DATA.__bss: 0x5a0
   __DATA.__common: 0x30
   __DATA_DIRTY.__objc_data: 0x500

   - /usr/lib/swift/libswiftsimd.dylib
   - /usr/lib/swift/libswiftsys_time.dylib
   - /usr/lib/swift/libswiftunistd.dylib
-  UUID: 1547BDDB-A362-3130-B6F8-17A580EF76F1
-  Functions: 2227
-  Symbols:   4447
-  CStrings:  2991
+  UUID: 0EE400A7-AD2D-3CEC-B317-3FD37CC19EA6
+  Functions: 2244
+  Symbols:   4484
+  CStrings:  3006
 
Symbols:
+ +[_LTDisambiguableResult isGenderDisambiguationEnabled].cold.1
+ +[_LTLanguageStatusMulticaster shared].cold.1
+ +[_LTPreflightChecker _sharedQueue].cold.1
+ +[_LTTextSession synchronizationQueue].cold.1
+ +[_LTTextToSpeechSanitizer _regularExpression].cold.1
+ -[_LTTextSessionRequest didStartTranslating]
+ OBJC_IVAR_$__LTTextSessionRequest._hasReceivedFirstItem
+ OBJC_IVAR_$__LTTextSessionRequest._signpostID
+ _LTOSLogAssets.cold.1
+ _LTOSLogDisambiguation.cold.1
+ _LTOSLogOnboarding.cold.1
+ _LTOSLogRomanization.cold.1
+ _LTOSLogSELFLogging.cold.1
+ _LTOSLogSpeech.cold.1
+ _LTOSLogTTS.cold.1
+ _LTOSLogTextAPI.cold.1
+ _LTOSLogTranslationEngine.cold.1
+ _LTOSLogUserFeedback.cold.1
+ _LTOSLogXPC.cold.1
+ _NSInvalidArgumentException
+ ___swift_async_entry_functlets
+ ___swift_async_ret_functlets
+ ___swift_destroy_boxed_opaque_existential_0
+ ___swift_project_boxed_opaque_existential_0
+ __os_signpost_emit_with_name_impl
+ __swift_get_extra_inhabitant_index.18Tm
+ __swift_store_extra_inhabitant_index.19Tm
+ _arc4random
+ _objc_msgSend$didStartTranslating
+ _objc_msgSend$raise
+ _os_signpost_enabled
+ _os_signpost_id_generate
+ _symbolic ScESg
+ _symbolic SccySo13_LTTextResultC______pG s5ErrorP
+ _symbolic Sccyyt______pG s5ErrorP
+ block_copy_helper.34
+ block_copy_helper.40
+ block_copy_helper.46
+ block_copy_helper.8
+ block_descriptor.10
+ block_descriptor.36
+ block_descriptor.42
+ block_descriptor.48
+ block_destroy_helper.35
+ block_destroy_helper.41
+ block_destroy_helper.47
+ block_destroy_helper.9
+ objectdestroy.32Tm
- _OUTLINED_FUNCTION_8
- __swift_get_extra_inhabitant_index.16Tm
- __swift_store_extra_inhabitant_index.17Tm
- _swift_arrayDestroy
- _swift_bridgeObjectRelease_n
- _swift_isUniquelyReferenced_nonNull_native
- block_copy_helper.36
- block_copy_helper.42
- block_descriptor.38
- block_descriptor.44
- block_descriptor.8
- block_destroy_helper.37
- block_destroy_helper.43
- objectdestroy.30Tm
CStrings:
+ "Finished preflight checks with error"
+ "Got Task.CancellationError, no need to convert it"
+ "Null value for locale when encoding LTTranslationResult"
+ "PreflightChecks"
+ "Received result for input item %zu after completion handler was already called, likely because an error previously occurred; early returning"
+ "ResolvedSourceLocale"
+ "ResolvedTargetLocale"
+ "Successfully translated first item"
+ "Translating first item finished with error"
+ "Translation"
+ "Translation finished successfully"
+ "Translation finished with error"
+ "TranslationFirstItem"
+ "_hasReceivedFirstItem"
+ "_signpostID"
+ "didStartTranslating"
+ "raise"
- "Received result for input item %zu after completion handler was already called, likely because an error previously ocurred; early returning"
- "Swift/UnsafePointer.swift"
- "UnsafeMutablePointer.initialize overlapping range"

```
