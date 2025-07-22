## LiveTranscription

> `/System/Library/PrivateFrameworks/LiveTranscription.framework/LiveTranscription`

```diff

-539.0.0.0.0
-  __TEXT.__text: 0x2cfcc
+541.2.0.0.0
+  __TEXT.__text: 0x2e10c
   __TEXT.__auth_stubs: 0xf80
-  __TEXT.__objc_methlist: 0x1524
+  __TEXT.__objc_methlist: 0x1544
   __TEXT.__const: 0x7e0
-  __TEXT.__cstring: 0xf1a
+  __TEXT.__cstring: 0xf2a
   __TEXT.__gcc_except_tab: 0x88
-  __TEXT.__oslogstring: 0x2584
+  __TEXT.__oslogstring: 0x2634
   __TEXT.__dlopen_cstrs: 0x6a
-  __TEXT.__swift5_typeref: 0x400
+  __TEXT.__swift5_typeref: 0x440
   __TEXT.__swift5_reflstr: 0x1fa
   __TEXT.__swift5_assocty: 0x78
   __TEXT.__constg_swiftt: 0x4d4

   __TEXT.__swift5_capture: 0x2fc
   __TEXT.__swift_as_entry: 0x70
   __TEXT.__swift_as_ret: 0x78
-  __TEXT.__unwind_info: 0xa20
-  __TEXT.__eh_frame: 0xb20
+  __TEXT.__unwind_info: 0xa40
+  __TEXT.__eh_frame: 0xb80
   __TEXT.__objc_classname: 0x21b
-  __TEXT.__objc_methname: 0x3555
+  __TEXT.__objc_methname: 0x35ca
   __TEXT.__objc_methtype: 0xbfe
   __TEXT.__objc_stubs: 0x2760
   __DATA_CONST.__got: 0x3c8

   __DATA_CONST.__objc_catlist: 0x8
   __DATA_CONST.__objc_protolist: 0x50
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0xdd8
+  __DATA_CONST.__objc_selrefs: 0xdf8
   __DATA_CONST.__objc_protorefs: 0x10
   __DATA_CONST.__objc_superrefs: 0x60
   __AUTH_CONST.__auth_got: 0x7d0

   __AUTH.__objc_data: 0xa08
   __AUTH.__data: 0x148
   __DATA.__objc_ivar: 0x180
-  __DATA.__data: 0x6a0
+  __DATA.__data: 0x6b0
   __DATA.__bss: 0x688
   __DATA.__common: 0x68
   __DATA_DIRTY.__objc_data: 0x248

   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  UUID: FAC8A2F8-85AB-3527-88AD-4EBD88E89EC8
-  Functions: 995
-  Symbols:   1977
-  CStrings:  1146
+  UUID: BE593A46-CD8F-398C-8E8A-9BEBDA9797F9
+  Functions: 1003
+  Symbols:   1980
+  CStrings:  1154
 
Symbols:
+ ___49-[AXLTSpeechTranscriber setupTranscriberIfNeeded]_block_invoke.304
+ ___51-[AXLTAudioOutTranscriber setupTranscriberIfNeeded]_block_invoke.286
+ ___51-[AXLTAudioOutTranscriber setupTranscriberIfNeeded]_block_invoke.290
+ ___54-[AXLTTranscriber _downloadAndInstallSpeechRecognizer]_block_invoke.295
+ ___54-[AXLTTranscriber _downloadAndInstallSpeechRecognizer]_block_invoke_2.296
+ ___79-[AXLTLanguageAssetManager downloadSpeechAssetForTaskHint:progress:completion:]_block_invoke.284
+ ___80-[AXLTTranscriber startTranscriptionForPID:appName:callback:completionCallback:]_block_invoke.286
+ ___block_literal_global.310
+ _symbolic Si6offset______7elementt 10Foundation6LocaleV
+ _symbolic Si6offset______7elementtSg 10Foundation6LocaleV
+ _symbolic _____ySSG s23_ContiguousArrayStorageC
- ___49-[AXLTSpeechTranscriber setupTranscriberIfNeeded]_block_invoke.310
- ___51-[AXLTAudioOutTranscriber setupTranscriberIfNeeded]_block_invoke.289
- ___51-[AXLTAudioOutTranscriber setupTranscriberIfNeeded]_block_invoke.293
- ___54-[AXLTTranscriber _downloadAndInstallSpeechRecognizer]_block_invoke.298
- ___54-[AXLTTranscriber _downloadAndInstallSpeechRecognizer]_block_invoke_2.299
- ___79-[AXLTLanguageAssetManager downloadSpeechAssetForTaskHint:progress:completion:]_block_invoke.287
- ___80-[AXLTTranscriber startTranscriptionForPID:appName:callback:completionCallback:]_block_invoke.289
- ___block_literal_global.313
CStrings:
+ "Default locale test success, input: %s, expected: %s, got: %s, %s"
+ "Testing locales"
+ "TranscriberV2: Searching default locale for languageCode: %s from locales: %s"
+ "TranscriberV2: default is locale with language with language region: %s"
+ "TranscriberV2: localeIDsWithLanguageCode: %s"
+ "defaultLocaleWithCompletion:"
+ "formattedLocaleIDsFrom:"
+ "installedLocalesWithCompletion:"
+ "supportedLocalesWithCompletion:"
- "TranscriberV2: default is locale with language region: %s"
- "TranscriberV2: languageCode: %s locales: %s"

```
