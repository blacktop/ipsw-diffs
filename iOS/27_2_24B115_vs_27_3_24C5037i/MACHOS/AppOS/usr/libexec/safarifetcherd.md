## safarifetcherd

> `/usr/libexec/safarifetcherd`

### Sections with Same Size but Changed Content

- `__TEXT.__objc_methlist`
- `__DATA_CONST.__const`
- `__DATA_CONST.__cfstring`
- `__DATA_CONST.__objc_classlist`
- `__DATA_CONST.__objc_protolist`
- `__DATA_CONST.__objc_superrefs`
- `__DATA_CONST.__objc_intobj`
- `__DATA.__objc_data`
- `__DATA.__data`

```diff

-7625.2.8.10.6
-  __TEXT.__text: 0x94c0
+7626.1.12.10.3
+  __TEXT.__text: 0x92c4
   __TEXT.__auth_stubs: 0x800
-  __TEXT.__objc_stubs: 0x24c0
+  __TEXT.__objc_stubs: 0x22e0
   __TEXT.__objc_methlist: 0x14ac
   __TEXT.__gcc_except_tab: 0xb30
-  __TEXT.__const: 0x98
+  __TEXT.__const: 0x90
   __TEXT.__cstring: 0x451
-  __TEXT.__objc_methname: 0x580d
+  __TEXT.__objc_methname: 0x5687
   __TEXT.__objc_classname: 0x1a9
   __TEXT.__objc_methtype: 0x2a60
-  __TEXT.__oslogstring: 0x1011
+  __TEXT.__oslogstring: 0xff9
   __TEXT.__dlopen_cstrs: 0x4e
-  __TEXT.__unwind_info: 0x5d0
+  __TEXT.__unwind_info: 0x5c8
   __DATA_CONST.__const: 0x348
   __DATA_CONST.__cfstring: 0x480
   __DATA_CONST.__objc_classlist: 0x28

   __DATA_CONST.__objc_doubleobj: 0x10
   __DATA_CONST.__objc_intobj: 0x18
   __DATA_CONST.__auth_got: 0x418
-  __DATA_CONST.__got: 0x2f0
-  __DATA.__objc_const: 0x1770
-  __DATA.__objc_selrefs: 0x1218
+  __DATA_CONST.__got: 0x2e8
+  __DATA.__objc_const: 0x1778
+  __DATA.__objc_selrefs: 0x11a8
   __DATA.__objc_ivar: 0xf8
   __DATA.__objc_data: 0x190
   __DATA.__data: 0x488

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libc++.1.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 266
-  Symbols:   233
-  CStrings:  1063
+  Functions: 263
+  Symbols:   232
+  CStrings:  1048
 
Symbols:
+ _OBJC_CLASS_$_WBSUIReaderViewContext
- _OBJC_CLASS_$_WBSFeatureAvailability
- __SFReaderPageGroupIdentifier
CStrings:
+ "initWithConfiguration:operationMode:"
+ "readerControllerDidRequestSummarizationSettings:"
+ "renderViewFromArticleView:context:completionHandler:"
- "_attributedBundleIdentifier"
- "_grantAccessToAssetServices"
- "_setAlternateWebViewForNavigationGestures:"
- "_setBackgroundExtendsBeyondPage:"
- "_setGroupIdentifier:"
- "_setNeedsStorageAccessFromFileURLsQuirk:"
- "_setRelatedWebView:"
- "configuration"
- "didCreateReaderWebView:"
- "isReaderViewInSeparateProcessEnabled"
- "processPool"
- "readerURL"
- "renderViewFromArticleView:readerConfiguration:completionHandler:"
- "setReaderInitialTopScrollOffset:configuration:isViewingArchive:"
- "setUIDelegate:"
- "setUpReaderWebViewIfNeededWithTimeout:completionHandler:"
- "websiteDataStore"
- "will load readerURL: %@"
```
