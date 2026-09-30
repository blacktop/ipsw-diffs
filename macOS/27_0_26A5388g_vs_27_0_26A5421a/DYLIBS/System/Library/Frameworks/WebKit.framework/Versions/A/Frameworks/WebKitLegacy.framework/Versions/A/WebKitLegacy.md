## WebKitLegacy

> `/System/Library/Frameworks/WebKit.framework/Versions/A/Frameworks/WebKitLegacy.framework/Versions/A/WebKitLegacy`

```diff

-625.1.24.11.2
-  __TEXT.__text: 0x1a10f0
+625.1.29.11.25
+  __TEXT.__text: 0x1a0f70
   __TEXT.__objc_methlist: 0x10258
   __TEXT.__const: 0x67a
   __TEXT.__getClass_cstr: 0x30
-  __TEXT.__gcc_except_tab: 0x14988
-  __TEXT.__cstring: 0x1e9db
+  __TEXT.__gcc_except_tab: 0x1497c
+  __TEXT.__cstring: 0x1e896
   __TEXT.__oslogstring: 0x14a
   __TEXT.__ustring: 0x4
   __TEXT.__unwind_info: 0x9c78

   __DATA_CONST.__objc_superrefs: 0x368
   __DATA_CONST.__objc_arraydata: 0x38
   __DATA_CONST.__got: 0x1428
-  __AUTH_CONST.__const: 0x5380
-  __AUTH_CONST.__cfstring: 0xffe0
+  __AUTH_CONST.__const: 0x5390
+  __AUTH_CONST.__cfstring: 0xfee0
   __AUTH_CONST.__objc_const: 0x11490
   __AUTH_CONST.__weak_auth_got: 0x10
   __AUTH_CONST.__objc_intobj: 0x3d8

   - /usr/lib/libicucore.A.dylib
   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libsqlite3.dylib
-  Functions: 7535
-  Symbols:   15932
-  CStrings:  2532
+  Functions: 7536
+  Symbols:   15937
+  CStrings:  2524
 
Symbols:
+ GCC_except_table214
+ GCC_except_table235
+ GCC_except_table240
+ GCC_except_table243
+ GCC_except_table246
+ GCC_except_table249
+ GCC_except_table252
+ GCC_except_table255
+ GCC_except_table257
+ GCC_except_table263
+ GCC_except_table266
+ GCC_except_table278
+ GCC_except_table282
+ GCC_except_table287
+ GCC_except_table295
+ GCC_except_table304
+ GCC_except_table309
+ GCC_except_table312
+ GCC_except_table314
+ GCC_except_table329
+ GCC_except_table332
+ GCC_except_table347
+ GCC_except_table351
+ GCC_except_table361
+ GCC_except_table369
+ GCC_except_table374
+ GCC_except_table387
+ GCC_except_table391
+ GCC_except_table454
+ GCC_except_table528
+ GCC_except_table540
+ GCC_except_table547
+ __ZN20WebFrameLoaderClient34dispatchGoToBackForwardItemAtIndexEiN7WebCore13FrameLoadTypeE
+ __ZN7WebCore12ChromeClient20transcodeChosenFilesEON3WTF6VectorINS1_6StringELm0ENS1_15CrashOnOverflowELm16ENS1_10FastMallocEEEOS3_S8_ONS1_17CompletionHandlerIFvS7_EEE
+ __ZN7WebCore12ChromeClient26showWritingToolsAffordanceEv
+ __ZNK7WebCore12ChromeClient21writingToolsAvailableEv
- GCC_except_table241
- GCC_except_table245
- GCC_except_table247
- GCC_except_table248
- GCC_except_table251
- GCC_except_table254
- GCC_except_table258
- GCC_except_table264
- GCC_except_table272
- GCC_except_table280
- GCC_except_table283
- GCC_except_table288
- GCC_except_table300
- GCC_except_table302
- GCC_except_table307
- GCC_except_table310
- GCC_except_table313
- GCC_except_table321
- GCC_except_table330
- GCC_except_table339
- GCC_except_table350
- GCC_except_table362
- GCC_except_table375
- GCC_except_table383
- GCC_except_table388
- GCC_except_table455
- GCC_except_table463
- GCC_except_table529
- GCC_except_table541
- __ZN20WebFrameLoaderClient34dispatchGoToBackForwardItemAtIndexEi
- __ZN20WebFrameLoaderClient36dispatchEnqueueHistoryTraversalDeltaEi
Functions:
~ +[WebPreferences initialize] : 13112 -> 13080
- __ZN20WebFrameLoaderClient36dispatchEnqueueHistoryTraversalDeltaEi
~ -[WebView(WebPrivate) setSelectTrailingWhitespaceEnabled:] : 76 -> 68
~ __ZN7WebCore20CacheStorageProvider28createCacheStorageConnectionEv : 84 -> 88
+ __ZNK7WebCore12ChromeClient21writingToolsAvailableEv
+ __ZN7WebCore12ChromeClient33hasActiveNowPlayingSessionChangedEb
~ +[WebPreferences(WebPrivateExperimentalFeatures) _experimentalFeatures] : 25448 -> 25076
~ +[WebPreferences(WebPrivateInternalFeatures) _internalFeatures] : 13908 -> 14008
~ -[WebView(WebViewInternalPreferencesChangedGenerated) _preferencesChangedGenerated:] : 23972 -> 23888
CStrings:
- "Enable Global Privacy Control (GPC) Feature"
- "Expose the status of Global Privacy Control (GPC) API (navigtor.gloabalPrivacyControl)"
- "Global Privacy Control API"
- "Global Privacy Control Feature"
- "GlobalPrivacyControlFeatureEnabled"
- "GlobalPrivacyControlStatus"
- "WebKitGlobalPrivacyControlFeatureEnabled"
- "WebKitGlobalPrivacyControlStatus"
```
