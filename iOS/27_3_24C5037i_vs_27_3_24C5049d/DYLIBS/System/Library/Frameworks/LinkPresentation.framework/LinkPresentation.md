## LinkPresentation

> `/System/Library/Frameworks/LinkPresentation.framework/LinkPresentation`

### Sections with Same Size but Changed Content

- `__TEXT.__cstring`

```diff

-319.1.0.0.0
-  __TEXT.__text: 0x1099f0
-  __TEXT.__objc_methlist: 0x11224
+319.2.0.0.0
+  __TEXT.__text: 0x10a368
+  __TEXT.__objc_methlist: 0x11274
   __TEXT.__cstring: 0x8c81
-  __TEXT.__gcc_except_tab: 0x236d4
+  __TEXT.__gcc_except_tab: 0x237ec
   __TEXT.__const: 0x2584
   __TEXT.__ustring: 0x3f6
-  __TEXT.__oslogstring: 0x3bdb
+  __TEXT.__oslogstring: 0x3d8b
   __TEXT.__dlopen_cstrs: 0x9c7
   __TEXT.__swift5_typeref: 0xaf6
   __TEXT.__constg_swiftt: 0x864

   __TEXT.__swift_as_ret: 0x28
   __TEXT.__swift_as_cont: 0x4c
   __TEXT.__swift5_assocty: 0x108
-  __TEXT.__unwind_info: 0x8be8
+  __TEXT.__unwind_info: 0x8c10
   __TEXT.__eh_frame: 0xdc0
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0

   __DATA_CONST.__objc_catlist: 0xa0
   __DATA_CONST.__objc_protolist: 0x240
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x7b98
+  __DATA_CONST.__objc_selrefs: 0x7bc8
   __DATA_CONST.__objc_protorefs: 0xb8
   __DATA_CONST.__objc_superrefs: 0x5e8
   __DATA_CONST.__objc_arraydata: 0x1648
-  __DATA_CONST.__got: 0xf28
+  __DATA_CONST.__got: 0xf30
   __AUTH_CONST.__const: 0x1fd8
   __AUTH_CONST.__cfstring: 0xdd00
-  __AUTH_CONST.__objc_const: 0x2dee0
+  __AUTH_CONST.__objc_const: 0x2df90
   __AUTH_CONST.__objc_intobj: 0x390
   __AUTH_CONST.__objc_arrayobj: 0x648
   __AUTH_CONST.__objc_dictobj: 0xc8

   __AUTH_CONST.__auth_got: 0x10e8
   __AUTH.__objc_data: 0x36c0
   __AUTH.__data: 0x4d0
-  __DATA.__objc_ivar: 0x1818
+  __DATA.__objc_ivar: 0x1828
   __DATA.__data: 0x1c88
   __DATA.__common: 0x1d8
   __DATA_DIRTY.__objc_data: 0x22d8

   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  Functions: 6941
-  Symbols:   11751
-  CStrings:  2329
+  Functions: 6949
+  Symbols:   11762
+  CStrings:  2335
 
Symbols:
+ +[LPMetadataProvider _copyWebViewConfigurationWithNetworkAttributionSourceApplicationBundleIdentifier:sourceApplicationSecondaryIdentifier:]
+ -[LPFetcherConfiguration networkAttributionSourceApplicationBundleIdentifier]
+ -[LPFetcherConfiguration setNetworkAttributionSourceApplicationBundleIdentifier:]
+ -[LPMediaAssetFetcher _streamingVideo]
+ -[LPMetadataProviderSpecializationContext initWithOriginalURL:postRedirectURL:MIMEType:webView:hasLoadedResource:shouldFetchSubresources:allowedSpecializations:fetchIsNotUserInitiated:networkAttributionSourceApplicationBundleIdentifier:]
+ -[LPMetadataProviderSpecializationContext networkAttributionSourceApplicationBundleIdentifier]
+ -[LPVideo _networkAttributionSourceApplicationBundleIdentifier]
+ -[LPVideo set_networkAttributionSourceApplicationBundleIdentifier:]
+ _AVURLAssetClientBundleIdentifierKey
+ _OBJC_IVAR_$_LPFetcherConfiguration._networkAttributionSourceApplicationBundleIdentifier
+ _OBJC_IVAR_$_LPMediaAssetFetcher._networkAttributionSourceApplicationBundleIdentifier
+ _OBJC_IVAR_$_LPMetadataProviderSpecializationContext._networkAttributionSourceApplicationBundleIdentifier
+ _OBJC_IVAR_$_LPVideo._networkAttributionSourceApplicationBundleIdentifier
- -[LPMetadataProviderSpecializationContext initWithOriginalURL:postRedirectURL:MIMEType:webView:hasLoadedResource:shouldFetchSubresources:allowedSpecializations:fetchIsNotUserInitiated:]
- GCC_except_table96
CStrings:
+ "From %@"
+ "Invitation to Join Subscription"
+ "LPFetcherGroup<%d>: allocating web view for %@ (attributed=%d)"
+ "LPImageFetcher<%d>: allocating fallback web view, did not have webViewForProcessSharing (attributed=%d)"
+ "LPMediaAssetFetcher<%d>: creating asset (attributed=%d)"
+ "LPMetadataProvider<%d>: attributing network activity to %{public}@"
+ "LPMetadataProvider<%d>: creating web view (attributed=%d)"
+ "LPMetadataProvider<%d>: ignoring network attribution set after fetching started"
+ "LPMetadataProvider<%d>: not reusing client-provided WKWebView for fetching"
+ "LPRawURLContentsFetcher<%d>: allocating fallback web view, did not have webViewForProcessSharing (attributed=%d)"
- "Invitation from %@"
- "LPImageFetcher<%d>: allocating fallback web view, did not have webViewForProcessSharing"
- "LPRawURLContentsFetcher<%d>: allocating fallback web view, did not have webViewForProcessSharing"
- "Subscription Invitation"
```
