## WebKitLegacy

> `/System/Library/Frameworks/WebKit.framework/Versions/A/Frameworks/WebKitLegacy.framework/Versions/A/WebKitLegacy`

### Sections with Same Size but Changed Content

- `__TEXT.__eh_frame`
- `__DATA_CONST.__const`
- `__DATA_CONST.__objc_classlist`
- `__DATA_CONST.__objc_catlist`
- `__DATA_CONST.__objc_protolist`
- `__DATA_CONST.__objc_protorefs`
- `__DATA_CONST.__objc_superrefs`
- `__DATA_CONST.__objc_arraydata`
- `__DATA_CONST.__got`
- `__AUTH_CONST.__objc_intobj`
- `__AUTH_CONST.__objc_arrayobj`
- `__AUTH_CONST.__objc_dictobj`
- `__AUTH.__objc_data`
- `__AUTH.__data`
- `__DATA.__data`
- `__DATA_DIRTY.__objc_data`
- `__DATA_DIRTY.__data`

```diff

-625.1.22.11.4
-  __TEXT.__text: 0x1a2f1c
-  __TEXT.__objc_methlist: 0x10288
-  __TEXT.__const: 0x68a
+625.1.24.11.2
+  __TEXT.__text: 0x1a10f0
+  __TEXT.__objc_methlist: 0x10258
+  __TEXT.__const: 0x67a
   __TEXT.__getClass_cstr: 0x30
-  __TEXT.__gcc_except_tab: 0x14c20
-  __TEXT.__cstring: 0x1e640
-  __TEXT.__oslogstring: 0x155
+  __TEXT.__gcc_except_tab: 0x14988
+  __TEXT.__cstring: 0x1e9db
+  __TEXT.__oslogstring: 0x14a
   __TEXT.__ustring: 0x4
-  __TEXT.__unwind_info: 0x9d70
+  __TEXT.__unwind_info: 0x9c78
   __TEXT.__eh_frame: 0x80
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0

   __DATA_CONST.__objc_catlist: 0x98
   __DATA_CONST.__objc_protolist: 0x1a8
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x94c0
+  __DATA_CONST.__objc_selrefs: 0x94a0
   __DATA_CONST.__objc_protorefs: 0x58
   __DATA_CONST.__objc_superrefs: 0x368
   __DATA_CONST.__objc_arraydata: 0x38
   __DATA_CONST.__got: 0x1428
-  __AUTH_CONST.__const: 0x5338
-  __AUTH_CONST.__cfstring: 0xfe20
-  __AUTH_CONST.__objc_const: 0x114b0
+  __AUTH_CONST.__const: 0x5380
+  __AUTH_CONST.__cfstring: 0xffe0
+  __AUTH_CONST.__objc_const: 0x11490
   __AUTH_CONST.__weak_auth_got: 0x10
   __AUTH_CONST.__objc_intobj: 0x3d8
   __AUTH_CONST.__objc_arrayobj: 0x30
   __AUTH_CONST.__objc_dictobj: 0x28
-  __AUTH_CONST.__auth_got: 0x47b0
+  __AUTH_CONST.__auth_got: 0x47a8
   __AUTH.__objc_data: 0x2a30
   __AUTH.__data: 0xf0
   __DATA.__objc_ivar: 0x508

   - /usr/lib/libicucore.A.dylib
   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libsqlite3.dylib
-  Functions: 7532
-  Symbols:   15943
-  CStrings:  2517
+  Functions: 7535
+  Symbols:   15932
+  CStrings:  2532
 
Symbols:
+ GCC_except_table1000
+ GCC_except_table1008
+ GCC_except_table1019
+ GCC_except_table1044
+ GCC_except_table234
+ GCC_except_table241
+ GCC_except_table245
+ GCC_except_table247
+ GCC_except_table250
+ GCC_except_table253
+ GCC_except_table258
+ GCC_except_table264
+ GCC_except_table272
+ GCC_except_table280
+ GCC_except_table283
+ GCC_except_table288
+ GCC_except_table300
+ GCC_except_table302
+ GCC_except_table307
+ GCC_except_table310
+ GCC_except_table313
+ GCC_except_table330
+ GCC_except_table339
+ GCC_except_table348
+ GCC_except_table350
+ GCC_except_table362
+ GCC_except_table375
+ GCC_except_table383
+ GCC_except_table388
+ GCC_except_table455
+ GCC_except_table463
+ GCC_except_table529
+ GCC_except_table993
+ __ZN20LegacySocketProvider22createWebSocketChannelERN7WebCore8DocumentERNS0_22WebSocketChannelClientENS0_28IsInitiatedByDedicatedWorkerE
+ __ZN20WebFrameLoaderClient34dispatchGoToBackForwardItemAtIndexEi
+ __ZN20WebFrameLoaderClient36dispatchEnqueueHistoryTraversalDeltaEi
+ __ZN3WTF6Detail15CallableWrapperIZN7WebCore17HistoryItemClient35ignoreChangesForScopeDuringRedirectERKNS2_10LocalFrameEEUlvE_vJEE4callEv
+ __ZN3WTF6Detail15CallableWrapperIZN7WebCore17HistoryItemClient35ignoreChangesForScopeDuringRedirectERKNS2_10LocalFrameEEUlvE_vJEED0Ev
+ __ZN3WTF6Detail15CallableWrapperIZN7WebCore17HistoryItemClient35ignoreChangesForScopeDuringRedirectERKNS2_10LocalFrameEEUlvE_vJEED1Ev
+ __ZN3WTF6Logger5osLogER13WTFLogChannelRKNS_7CStringE
+ __ZN7WebCore12ChromeClient20requestStorageAccessEONS_17RegistrableDomainES2_RNS_10LocalFrameENS_18StorageAccessScopeENS_37HasUserGestureOrNoUserGestureRequiredEON3WTF17CompletionHandlerIFvNS_26RequestStorageAccessResultEEEE
+ __ZN7WebCore17HistoryItemClient35ignoreChangesForScopeDuringRedirectERKNS_10LocalFrameE
+ __ZN7WebCore19ResourceRequestBase11RequestDataaSEOS1_
+ __ZN7WebCore27SpeechRecognitionConnection28dispatchCaptureSourceCreatedEN3WTF23ObjectIdentifierGenericINS_47SpeechRecognitionConnectionClientIdentifierTypeENS1_38ObjectIdentifierMainThreadAccessTraitsIyEEyEERNS_19RealtimeMediaSourceE
+ __ZNK24WebResourceLoadScheduler34isHttpNavigationWithHTTPSOnlyErrorERKN7WebCore13ResourceErrorE
+ __ZNK3WTF17StringTypeAdapterINS_4UUIDEE6handleIZNKS2_6lengthEvEUlDpOT_E_EEDcOT_
+ __ZTVN3WTF6Detail15CallableWrapperIZN7WebCore17HistoryItemClient35ignoreChangesForScopeDuringRedirectERKNS2_10LocalFrameEEUlvE_vJEEE
- -[WebPreferences(WebPrivate) _forceFTPDirectoryListings]
- -[WebPreferences(WebPrivate) _ftpDirectoryTemplatePath]
- -[WebPreferences(WebPrivate) _setFTPDirectoryTemplatePath:]
- -[WebPreferences(WebPrivate) _setForceFTPDirectoryListings:]
- GCC_except_table1007
- GCC_except_table1018
- GCC_except_table1043
- GCC_except_table214
- GCC_except_table240
- GCC_except_table243
- GCC_except_table246
- GCC_except_table249
- GCC_except_table252
- GCC_except_table255
- GCC_except_table257
- GCC_except_table263
- GCC_except_table266
- GCC_except_table278
- GCC_except_table282
- GCC_except_table287
- GCC_except_table295
- GCC_except_table304
- GCC_except_table309
- GCC_except_table312
- GCC_except_table314
- GCC_except_table329
- GCC_except_table332
- GCC_except_table346
- GCC_except_table347
- GCC_except_table351
- GCC_except_table361
- GCC_except_table369
- GCC_except_table374
- GCC_except_table387
- GCC_except_table391
- GCC_except_table394
- GCC_except_table413
- GCC_except_table431
- GCC_except_table432
- GCC_except_table437
- GCC_except_table438
- GCC_except_table450
- GCC_except_table454
- GCC_except_table510
- GCC_except_table511
- GCC_except_table528
- GCC_except_table540
- GCC_except_table547
- GCC_except_table653
- GCC_except_table992
- GCC_except_table996
- __ZN20LegacySocketProvider22createWebSocketChannelERN7WebCore8DocumentERNS0_22WebSocketChannelClientE
- __ZN20WebFrameLoaderClient34dispatchGoToBackForwardItemAtIndexEiN7WebCore13FrameLoadTypeE
- __ZN7WebCore10LocalFrame6editorEv
- __ZN7WebCore12ChromeClient20requestStorageAccessEONS_17RegistrableDomainES2_RNS_10LocalFrameENS_18StorageAccessScopeENS_28HasOrShouldIgnoreUserGestureEON3WTF17CompletionHandlerIFvNS_26RequestStorageAccessResultEEEE
- __ZN7WebCore15ResourceRequestaSEOS0_
- __ZNK7WebCore9RenderBox11clientWidthEv
- __ZNK7WebCore9RenderBox12clientHeightEv
CStrings:
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.ItPWak/Sources/WebKitLegacy/Source/WebKitLegacy/WebCoreSupport/WebResourceLoadScheduler.mm"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.ItPWak/Sources/WebKitLegacy/Source/WebKitLegacy/mac/DOM/ExceptionHandlers.mm"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.ItPWak/Sources/WebKitLegacy/Source/WebKitLegacy/mac/WebCoreSupport/WebEditorClient.mm"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.ItPWak/Sources/WebKitLegacy/Source/WebKitLegacy/mac/WebCoreSupport/WebFrameLoaderClient.mm"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.ItPWak/Sources/WebKitLegacy/Source/WebKitLegacy/mac/WebView/WebFrame.mm"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.ItPWak/Sources/WebKitLegacy/Source/WebKitLegacy/mac/WebView/WebPreferences.mm"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.ItPWak/Sources/WebKitLegacy/Source/WebKitLegacy/mac/WebView/WebVideoFullscreenController.mm"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.ItPWak/Sources/WebKitLegacy/Source/WebKitLegacy/mac/WebView/WebView.mm"
+ "Always enable VPx software decoders"
+ "CSS random-item()"
+ "CSSRandomItemFunctionEnabled"
+ "Enable Global Privacy Control (GPC) Feature"
+ "Enable support for CSS Values and Units Module Level 5 random-item()"
+ "Expose the status of Global Privacy Control (GPC) API (navigtor.gloabalPrivacyControl)"
+ "Find in Video"
+ "FindInVideoEnabled"
+ "Force the layer-based SVG Engine (LBSE) to create a RenderLayer for every SVG renderer (debugging only)"
+ "Global Privacy Control API"
+ "Global Privacy Control Feature"
+ "GlobalPrivacyControlFeatureEnabled"
+ "GlobalPrivacyControlStatus"
+ "Include video subtitle/caption cues in Find-in-Page results"
+ "LBSE: Force layer creation for all SVG renderers"
+ "LayerBasedSVGEngineForceLayerCreationEnabled"
+ "SWVPDecodersAlwaysEnabled"
+ "T *WTF::CheckedPtr<WebCore::CSSImportRule>::operator->() const [T = WebCore::CSSImportRule, PtrTraits = WTF::RawPtrTraits<WebCore::CSSImportRule>]"
+ "WebKitCSSRandomItemFunctionEnabled"
+ "WebKitFindInVideoEnabled"
+ "WebKitGlobalPrivacyControlFeatureEnabled"
+ "WebKitGlobalPrivacyControlStatus"
+ "WebKitLayerBasedSVGEngineForceLayerCreationEnabled"
+ "WebKitNavigatorWebDriverActivePolicy"
+ "WebKitSWVPDecodersAlwaysEnabled"
+ "virtual bool WebResourceLoadScheduler::isHttpNavigationWithHTTPSOnlyError(const WebCore::ResourceError &) const"
- "%{public}s"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.6FUlRN/Sources/WebKitLegacy/Source/WebKitLegacy/WebCoreSupport/WebResourceLoadScheduler.mm"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.6FUlRN/Sources/WebKitLegacy/Source/WebKitLegacy/mac/DOM/ExceptionHandlers.mm"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.6FUlRN/Sources/WebKitLegacy/Source/WebKitLegacy/mac/WebCoreSupport/WebEditorClient.mm"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.6FUlRN/Sources/WebKitLegacy/Source/WebKitLegacy/mac/WebCoreSupport/WebFrameLoaderClient.mm"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.6FUlRN/Sources/WebKitLegacy/Source/WebKitLegacy/mac/WebView/WebFrame.mm"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.6FUlRN/Sources/WebKitLegacy/Source/WebKitLegacy/mac/WebView/WebPreferences.mm"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.6FUlRN/Sources/WebKitLegacy/Source/WebKitLegacy/mac/WebView/WebVideoFullscreenController.mm"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.6FUlRN/Sources/WebKitLegacy/Source/WebKitLegacy/mac/WebView/WebView.mm"
- "Enable Global Privacy Control (GPC) signal"
- "Global Privacy Control"
- "GlobalPrivacyControlEnabled"
- "Media Containment"
- "MediaContainmentEnabled"
- "Process complex media types in the web process"
- "WebKitFTPDirectoryTemplatePath"
- "WebKitForceFTPDirectoryListings"
- "WebKitGlobalPrivacyControlEnabled"
- "WebKitMediaContainmentEnabled"
```
