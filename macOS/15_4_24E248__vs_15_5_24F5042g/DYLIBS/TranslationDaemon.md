## TranslationDaemon

> `/System/Library/PrivateFrameworks/TranslationDaemon.framework/Versions/A/TranslationDaemon`

```diff

-300.12.0.0.0
-  __TEXT.__text: 0x198a2c
+300.14.0.0.0
+  __TEXT.__text: 0x1996b0
   __TEXT.__auth_stubs: 0xb40
-  __TEXT.__objc_methlist: 0x18e88
+  __TEXT.__objc_methlist: 0x18e98
   __TEXT.__const: 0x3b0
-  __TEXT.__gcc_except_tab: 0x1b13c
-  __TEXT.__cstring: 0x5479
-  __TEXT.__oslogstring: 0xa5f9
+  __TEXT.__gcc_except_tab: 0x1b160
+  __TEXT.__cstring: 0x54ad
+  __TEXT.__oslogstring: 0xa801
   __TEXT.__dlopen_cstrs: 0xb2
-  __TEXT.__unwind_info: 0xf0d8
+  __TEXT.__unwind_info: 0xf0f0
   __TEXT.__objc_classname: 0x4691
-  __TEXT.__objc_methname: 0x1990a
+  __TEXT.__objc_methname: 0x19956
   __TEXT.__objc_methtype: 0xddd3
-  __TEXT.__objc_stubs: 0x115a0
+  __TEXT.__objc_stubs: 0x11600
   __DATA_CONST.__got: 0xc18
   __DATA_CONST.__const: 0x1448
   __DATA_CONST.__objc_classlist: 0x1168
   __DATA_CONST.__objc_catlist: 0x130
   __DATA_CONST.__objc_protolist: 0xd0
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x6210
+  __DATA_CONST.__objc_selrefs: 0x6228
   __DATA_CONST.__objc_superrefs: 0x10e8
   __DATA_CONST.__objc_arraydata: 0x90
   __AUTH_CONST.__auth_got: 0x5b8
   __AUTH_CONST.__auth_ptr: 0x8
   __AUTH_CONST.__const: 0x3390
-  __AUTH_CONST.__cfstring: 0x6da0
+  __AUTH_CONST.__cfstring: 0x6e40
   __AUTH_CONST.__objc_const: 0x2b3a8
   __AUTH_CONST.__objc_dictobj: 0x78
   __AUTH_CONST.__objc_doubleobj: 0x20

   - /usr/lib/libc++.1.dylib
   - /usr/lib/libmorphun.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 9725
-  Symbols:   22559
-  CStrings:  7692
+  Functions: 9734
+  Symbols:   22571
+  CStrings:  7710
 
Symbols:
+ +[_LTDAssetService preflightCheckForLocalePair:withModelURLs:]
+ +[_LTDAssetService preflightCheckForLocalePair:withModelURLs:].cold.1
+ +[_LTDAssetService preflightCheckForLocalePair:withModelURLs:].cold.2
+ +[_LTDAssetService preflightCheckForLocalePair:withModelURLs:].cold.3
+ +[_LTDAssetService preflightCheckForLocalePair:withModelURLs:].cold.4
+ +[_LTDAssetService preflightCheckForLocalePair:withModelURLs:].cold.5
+ +[_LTDAssetService preflightCheckForLocalePair:withModelURLs:].cold.6
+ -[_LTOfflineTranslationEngine _loadTranslatorForTask:].cold.2
+ __65-[_LTOfflineTranslationEngine _waitForLIDWithContext:completion:]_block_invoke.75
+ __73-[_LTOfflineTranslationEngine _translate:withContext:isFinal:completion:]_block_invoke.83
+ __74-[_LTOfflineTranslationEngine startSpeechTranslationWithContext:delegate:]_block_invoke.113
+ __74-[_LTOfflineTranslationEngine startSpeechTranslationWithContext:delegate:]_block_invoke.116
+ __74-[_LTOfflineTranslationEngine startSpeechTranslationWithContext:delegate:]_block_invoke.122
+ __74-[_LTOfflineTranslationEngine startSpeechTranslationWithContext:delegate:]_block_invoke.122.cold.1
+ __74-[_LTOfflineTranslationEngine startSpeechTranslationWithContext:delegate:]_block_invoke.122.cold.2
+ __74-[_LTOfflineTranslationEngine startSpeechTranslationWithContext:delegate:]_block_invoke.138
+ __80-[_LTOfflineTranslationEngine translate:withContext:paragraphResult:completion:]_block_invoke.67
+ __80-[_LTOfflineTranslationEngine translate:withContext:paragraphResult:completion:]_block_invoke.67.cold.1
+ __83-[_LTOfflineTranslationEngine _translateParagraph:withContext:toLocale:completion:]_block_invoke.47
+ __83-[_LTOfflineTranslationEngine _translateParagraph:withContext:toLocale:completion:]_block_invoke.50
+ __85-[_LTOfflineTranslationEngine startTextToSpeechTranslationWithContext:text:delegate:]_block_invoke.89
+ __85-[_LTOfflineTranslationEngine startTextToSpeechTranslationWithContext:text:delegate:]_block_invoke.93
+ __85-[_LTOfflineTranslationEngine startTextToSpeechTranslationWithContext:text:delegate:]_block_invoke.93.cold.1
+ __90-[_LTOfflineTranslationEngine _translate:withContext:toLocale:paragraphResult:completion:]_block_invoke.53
+ __90-[_LTOfflineTranslationEngine _translate:withContext:toLocale:paragraphResult:completion:]_block_invoke.56
+ __98-[_LTOfflineTranslationEngine _translateString:isFinal:withContext:toLocale:withSpans:completion:]_block_invoke.26
+ __block_literal_global.46
+ _objc_msgSend$hasSuffix:
+ _objc_msgSend$isReadableFileAtPath:
+ _objc_msgSend$preflightCheckForLocalePair:withModelURLs:
- __65-[_LTOfflineTranslationEngine _waitForLIDWithContext:completion:]_block_invoke.74
- __73-[_LTOfflineTranslationEngine _translate:withContext:isFinal:completion:]_block_invoke.82
- __74-[_LTOfflineTranslationEngine startSpeechTranslationWithContext:delegate:]_block_invoke.110
- __74-[_LTOfflineTranslationEngine startSpeechTranslationWithContext:delegate:]_block_invoke.114
- __74-[_LTOfflineTranslationEngine startSpeechTranslationWithContext:delegate:]_block_invoke.120
- __74-[_LTOfflineTranslationEngine startSpeechTranslationWithContext:delegate:]_block_invoke.121.cold.1
- __74-[_LTOfflineTranslationEngine startSpeechTranslationWithContext:delegate:]_block_invoke.121.cold.2
- __74-[_LTOfflineTranslationEngine startSpeechTranslationWithContext:delegate:]_block_invoke.137
- __80-[_LTOfflineTranslationEngine translate:withContext:paragraphResult:completion:]_block_invoke.66
- __80-[_LTOfflineTranslationEngine translate:withContext:paragraphResult:completion:]_block_invoke.66.cold.1
- __83-[_LTOfflineTranslationEngine _translateParagraph:withContext:toLocale:completion:]_block_invoke.46
- __83-[_LTOfflineTranslationEngine _translateParagraph:withContext:toLocale:completion:]_block_invoke.49
- __85-[_LTOfflineTranslationEngine startTextToSpeechTranslationWithContext:text:delegate:]_block_invoke.88
- __85-[_LTOfflineTranslationEngine startTextToSpeechTranslationWithContext:text:delegate:]_block_invoke.92
- __85-[_LTOfflineTranslationEngine startTextToSpeechTranslationWithContext:text:delegate:]_block_invoke.92.cold.1
- __90-[_LTOfflineTranslationEngine _translate:withContext:toLocale:paragraphResult:completion:]_block_invoke.52
- __90-[_LTOfflineTranslationEngine _translate:withContext:toLocale:paragraphResult:completion:]_block_invoke.55
- __98-[_LTOfflineTranslationEngine _translateString:isFinal:withContext:toLocale:withSpans:completion:]_block_invoke.25
CStrings:
+ "-file"
+ "/AssetsV"
+ "Offline translation is a passthrough, skip translator load"
+ "Offline translation preflight failed"
+ "Offline translation using asset info model URLs: %{public}@"
+ "Offline translation using context model URLs: %{public}@"
+ "Preflight MT URL does not match request locale pair: %{public}@ vs %{public}@"
+ "Preflight missing file %{public}@"
+ "Preflight missing quasar config at: %{public}@"
+ "Preflight missing symlink at: %{public}@"
+ "Preflight read of MT config %{public}@ failed: %@"
+ "Preflight unexpected format for quasar config %{public}@"
+ "block-definitions"
+ "hasSuffix:"
+ "isReadableFileAtPath:"
+ "mt-decoders"
+ "mt_app"
+ "preflightCheckForLocalePair:withModelURLs:"

```
