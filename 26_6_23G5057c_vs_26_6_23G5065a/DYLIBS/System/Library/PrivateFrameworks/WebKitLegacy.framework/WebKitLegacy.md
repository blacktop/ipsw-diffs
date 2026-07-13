## WebKitLegacy

> `/System/Library/PrivateFrameworks/WebKitLegacy.framework/WebKitLegacy`

```diff

-  __TEXT.__text: 0x15c970
+  __TEXT.__text: 0x15c7b4
   __TEXT.__auth_stubs: 0x8dc0
   __TEXT.__objc_methlist: 0xf610
   __TEXT.__const: 0x220
Sections:
~ __TEXT.__objc_methlist : content changed
~ __TEXT.__const : content changed
~ __TEXT.__gcc_except_tab : content changed
~ __TEXT.__cstring : content changed
~ __TEXT.__unwind_info : content changed
~ __DATA_CONST.__got : content changed
~ __DATA_CONST.__const : content changed
~ __DATA_CONST.__objc_classlist : content changed
~ __DATA_CONST.__objc_catlist : content changed
~ __DATA_CONST.__objc_protolist : content changed
~ __DATA_CONST.__objc_selrefs : content changed
~ __DATA_CONST.__objc_protorefs : content changed
~ __DATA_CONST.__objc_superrefs : content changed
~ __DATA_CONST.__objc_arraydata : content changed
~ __AUTH_CONST.__const : content changed
~ __AUTH_CONST.__cfstring : content changed
~ __AUTH_CONST.__objc_const : content changed
~ __AUTH_CONST.__objc_intobj : content changed
~ __AUTH_CONST.__objc_dictobj : content changed
~ __AUTH_CONST.__objc_arrayobj : content changed
~ __AUTH.__objc_data : content changed
~ __AUTH.__data : content changed
~ __DATA.__data : content changed
~ __DATA_DIRTY.__objc_data : content changed
~ __DATA_DIRTY.__data : content changed
Symbols:
+ __ZN7WebCore19ResourceRequestBase11RequestDataaSEOS1_
- __ZN7WebCore15ResourceRequestaSEOS0_
Functions:
~ __ZN24WebResourceLoadScheduler16setDefersLoadingERN7WebCore14ResourceLoaderEb : 612 -> 804
~ __ZN7WebCore16WebSocketChannel19didOpenSocketStreamERNS_18SocketStreamHandleE : 908 -> 900
~ __ZN7WebCore15ResourceRequestaSEOS0_ -> __ZN7WebCore19ResourceRequestBase11RequestDataaSEOS1_ : 716 -> 548
~ __ZN7WebCore15ResourceRequestC1Ev : 296 -> 248
~ __ZN7WebCore15ResourceRequestD2Ev : 184 -> 152
~ __ZN7WebCore15ResourceRequestC1ERKS0_ : 604 -> 584
~ __ZN10PingHandle20willSendRequestAsyncEPN7WebCore14ResourceHandleEONS0_15ResourceRequestEONS0_16ResourceResponseEON3WTF17CompletionHandlerIFvS4_EEE : 952 -> 1020
~ __ZN10PingHandleD2Ev : 496 -> 464
~ -[WebPluginController webPlugInContainerLoadRequest:inFrame:] : 964 -> 932
~ __ZN7WebCore15ResourceRequestD1Ev : 184 -> 152
~ __ZN20WebFrameLoaderClient23dispatchWillSendRequestEPN7WebCore14DocumentLoaderEN3WTF23ObjectIdentifierGenericINS0_28ResourceLoaderIdentifierTypeENS3_38ObjectIdentifierThreadSafeAccessTraitsIyEEyEERNS0_15ResourceRequestERKNS0_16ResourceResponseE : 940 -> 908
~ __ZNK20WebFrameLoaderClient16actionDictionaryERKN7WebCore16NavigationActionEPNS0_9FormStateE : 636 -> 640
~ -[WebDataSource initWithRequest:] : 652 -> 620
~ -[WebFrame loadRequest:] : 912 -> 880
~ -[WebFrame _loadData:MIMEType:textEncodingName:baseURL:unreachableURL:] : 2868 -> 2776
~ __ZN3WTF20VectorTypeOperationsIN7WebCore14DOMCacheEngine17CrossThreadRecordEE8destructEPS3_S5_ : 720 -> 692
~ +[WebCache imageForURL:] : 708 -> 648
~ -[WebPDFViewPlaceholder simulateClickOnLinkToURL:] : 1680 -> 1620

```
