## WebKitLegacy

> `/System/iOSSupport/System/Library/PrivateFrameworks/WebKitLegacy.framework/Versions/A/WebKitLegacy`

### Sections with Same Size but Changed Content

- `__TEXT.__objc_methlist`
- `__TEXT.__const`
- `__TEXT.__gcc_except_tab`
- `__TEXT.__cstring`
- `__TEXT.__unwind_info`
- `__DATA_CONST.__got`
- `__DATA_CONST.__const`
- `__DATA_CONST.__objc_classlist`
- `__DATA_CONST.__objc_catlist`
- `__DATA_CONST.__objc_protolist`
- `__DATA_CONST.__objc_selrefs`
- `__DATA_CONST.__objc_protorefs`
- `__DATA_CONST.__objc_superrefs`
- `__DATA_CONST.__objc_arraydata`
- `__AUTH_CONST.__auth_got`
- `__AUTH_CONST.__const`
- `__AUTH_CONST.__cfstring`
- `__AUTH_CONST.__objc_const`
- `__AUTH_CONST.__objc_intobj`
- `__AUTH_CONST.__objc_dictobj`
- `__AUTH_CONST.__objc_arrayobj`
- `__AUTH.__objc_data`
- `__AUTH.__data`
- `__DATA.__data`
- `__DATA_DIRTY.__objc_data`
- `__DATA_DIRTY.__data`

```diff

-624.4.2.11.2
-  __TEXT.__text: 0x1596f8
+624.4.5.11.5
+  __TEXT.__text: 0x159564
   __TEXT.__auth_stubs: 0x8c50
   __TEXT.__objc_methlist: 0xf4e0
   __TEXT.__const: 0x1f0
Symbols:
+ __ZN7WebCore19ResourceRequestBase11RequestDataaSEOS1_
- __ZN7WebCore15ResourceRequestaSEOS0_
Functions:
~ -[WebFrame _loadData:MIMEType:textEncodingName:baseURL:unreachableURL:] : 1940 -> 1892
~ -[WebFrame loadRequest:] : 916 -> 884
~ __ZN24WebResourceLoadScheduler16setDefersLoadingERN7WebCore14ResourceLoaderEb : 612 -> 804
~ __ZN7WebCore16WebSocketChannel19didOpenSocketStreamERNS_18SocketStreamHandleE : 908 -> 900
~ __ZN7WebCore15ResourceRequestaSEOS0_ -> __ZN7WebCore19ResourceRequestBase11RequestDataaSEOS1_ : 716 -> 548
~ __ZN7WebCore15ResourceRequestC1Ev : 296 -> 248
~ __ZN7WebCore15ResourceRequestD2Ev : 184 -> 152
~ __ZN7WebCore15ResourceRequestC1ERKS0_ : 604 -> 584
~ __ZN10PingHandle20willSendRequestAsyncEPN7WebCore14ResourceHandleEONS0_15ResourceRequestEONS0_16ResourceResponseEON3WTF17CompletionHandlerIFvS4_EEE : 932 -> 1000
~ __ZN10PingHandleD2Ev : 496 -> 464
~ -[WebPluginController webPlugInContainerLoadRequest:inFrame:] : 972 -> 936
~ __ZN7WebCore15ResourceRequestD1Ev : 184 -> 152
~ __ZN20WebFrameLoaderClient23dispatchWillSendRequestEPN7WebCore14DocumentLoaderEN3WTF23ObjectIdentifierGenericINS0_28ResourceLoaderIdentifierTypeENS3_38ObjectIdentifierThreadSafeAccessTraitsIyEEyEERNS0_15ResourceRequestERKNS0_16ResourceResponseE : 940 -> 908
~ __ZNK20WebFrameLoaderClient16actionDictionaryERKN7WebCore16NavigationActionEPNS0_9FormStateE : 636 -> 640
~ -[WebDataSource initWithRequest:] : 656 -> 624
~ __ZN3WTF20VectorTypeOperationsIN7WebCore14DOMCacheEngine17CrossThreadRecordEE8destructEPS3_S5_ : 720 -> 692
~ +[WebCache imageForURL:] : 708 -> 648
~ -[WebPDFViewPlaceholder simulateClickOnLinkToURL:] : 1680 -> 1620
CStrings:
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.O4NlI0/Sources/WebKitLegacy_iosmac/Source/WebKitLegacy/WebCoreSupport/WebResourceLoadScheduler.mm"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.O4NlI0/Sources/WebKitLegacy_iosmac/Source/WebKitLegacy/ios/Misc/WebGeolocationCoreLocationProvider.mm"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.O4NlI0/Sources/WebKitLegacy_iosmac/Source/WebKitLegacy/mac/DOM/ExceptionHandlers.mm"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.O4NlI0/Sources/WebKitLegacy_iosmac/Source/WebKitLegacy/mac/WebCoreSupport/WebEditorClient.mm"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.O4NlI0/Sources/WebKitLegacy_iosmac/Source/WebKitLegacy/mac/WebCoreSupport/WebFrameLoaderClient.mm"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.O4NlI0/Sources/WebKitLegacy_iosmac/Source/WebKitLegacy/mac/WebView/WebFrame.mm"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.O4NlI0/Sources/WebKitLegacy_iosmac/Source/WebKitLegacy/mac/WebView/WebPreferences.mm"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.wpkslj/Sources/WebKitLegacy_iosmac/Source/WebKitLegacy/WebCoreSupport/WebResourceLoadScheduler.mm"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.wpkslj/Sources/WebKitLegacy_iosmac/Source/WebKitLegacy/ios/Misc/WebGeolocationCoreLocationProvider.mm"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.wpkslj/Sources/WebKitLegacy_iosmac/Source/WebKitLegacy/mac/DOM/ExceptionHandlers.mm"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.wpkslj/Sources/WebKitLegacy_iosmac/Source/WebKitLegacy/mac/WebCoreSupport/WebEditorClient.mm"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.wpkslj/Sources/WebKitLegacy_iosmac/Source/WebKitLegacy/mac/WebCoreSupport/WebFrameLoaderClient.mm"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.wpkslj/Sources/WebKitLegacy_iosmac/Source/WebKitLegacy/mac/WebView/WebFrame.mm"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.wpkslj/Sources/WebKitLegacy_iosmac/Source/WebKitLegacy/mac/WebView/WebPreferences.mm"
```
