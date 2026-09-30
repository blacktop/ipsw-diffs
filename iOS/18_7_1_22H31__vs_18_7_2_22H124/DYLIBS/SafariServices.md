## SafariServices

> `/System/Library/Frameworks/SafariServices.framework/SafariServices`

```diff

-621.4.1.10.1
-  __TEXT.__text: 0x166b18
+621.5.1.10.7
+  __TEXT.__text: 0x166c84
   __TEXT.__auth_stubs: 0x18a0
   __TEXT.__objc_methlist: 0x1b50c
   __TEXT.__const: 0x2a96
   __TEXT.__cstring: 0xdade
-  __TEXT.__gcc_except_tab: 0xdc44
+  __TEXT.__gcc_except_tab: 0xdc50
   __TEXT.__oslogstring: 0x79cd
-  __TEXT.__ustring: 0x406e
+  __TEXT.__ustring: 0x40cc
   __TEXT.__dlopen_cstrs: 0xb7d
   __TEXT.__constg_swiftt: 0x50
   __TEXT.__swift5_typeref: 0x6

   __TEXT.__swift5_types: 0x4
   __TEXT.__unwind_info: 0x81a0
   __TEXT.__objc_classname: 0x4bc3
-  __TEXT.__objc_methname: 0x57ec5
+  __TEXT.__objc_methname: 0x57ee7
   __TEXT.__objc_methtype: 0x1337d
-  __TEXT.__objc_stubs: 0x35060
-  __DATA_CONST.__got: 0x21b0
+  __TEXT.__objc_stubs: 0x35080
+  __DATA_CONST.__got: 0x21b8
   __DATA_CONST.__const: 0x6e48
   __DATA_CONST.__objc_classlist: 0xa20
   __DATA_CONST.__objc_catlist: 0x110
   __DATA_CONST.__objc_protolist: 0x8b0
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x11aa8
+  __DATA_CONST.__objc_selrefs: 0x11ab0
   __DATA_CONST.__objc_protorefs: 0x108
   __DATA_CONST.__objc_superrefs: 0x888
   __DATA_CONST.__objc_arraydata: 0x700
   __AUTH_CONST.__auth_got: 0xc68
   __AUTH_CONST.__const: 0x1a68
-  __AUTH_CONST.__cfstring: 0xc720
+  __AUTH_CONST.__cfstring: 0xc740
   __AUTH_CONST.__objc_const: 0x2c158
   __AUTH_CONST.__objc_intobj: 0xab0
   __AUTH_CONST.__objc_arrayobj: 0x9d8

   - /usr/lib/swift/libswiftsimd.dylib
   - /usr/lib/swift/libswiftsys_time.dylib
   - /usr/lib/swift/libswiftunistd.dylib
-  UUID: B8C2666A-9E19-3D66-9250-7B18E4129982
+  UUID: D9065386-1649-314D-B328-DED8F73DBB50
   Functions: 8750
-  Symbols:   34412
-  CStrings:  18092
+  Symbols:   34414
+  CStrings:  18094
 
Symbols:
+ +[SFDialog(SafariServicesExtras) allowDownloadDialogWithDownload:initiatingSecurityOrigin:navigatedWebView:allowViewAction:completionHandler:]
+ _WBSAboutSrcdocString
+ ___142+[SFDialog(SafariServicesExtras) allowDownloadDialogWithDownload:initiatingSecurityOrigin:navigatedWebView:allowViewAction:completionHandler:]_block_invoke
+ ___142+[SFDialog(SafariServicesExtras) allowDownloadDialogWithDownload:initiatingSecurityOrigin:navigatedWebView:allowViewAction:completionHandler:]_block_invoke_2
+ _objc_msgSend$safari_looksLikeAboutSrcdocURL
- +[SFDialog(SafariServicesExtras) allowDownloadDialogWithDownload:initiatingSecurityOrigin:presentingURL:allowViewAction:completionHandler:]
- ___139+[SFDialog(SafariServicesExtras) allowDownloadDialogWithDownload:initiatingSecurityOrigin:presentingURL:allowViewAction:completionHandler:]_block_invoke
- ___139+[SFDialog(SafariServicesExtras) allowDownloadDialogWithDownload:initiatingSecurityOrigin:presentingURL:allowViewAction:completionHandler:]_block_invoke_2
Functions:
~ -[SFBrowserServiceViewController _didResolveDestinationURL:pendingAppLinkCheck:] : 336 -> 340
~ +[SFDialog(SafariServicesExtras) allowDownloadDialogWithDownload:initiatingSecurityOrigin:presentingURL:allowViewAction:completionHandler:] -> +[SFDialog(SafariServicesExtras) allowDownloadDialogWithDownload:initiatingSecurityOrigin:navigatedWebView:allowViewAction:completionHandler:] : 936 -> 1232
~ -[_SFBrowserContentViewController _updateNavigationBar] : 1200 -> 1264
CStrings:
+ "allowDownloadDialogWithDownload:initiatingSecurityOrigin:navigatedWebView:allowViewAction:completionHandler:"
+ "safari_looksLikeAboutSrcdocURL"
- "allowDownloadDialogWithDownload:initiatingSecurityOrigin:presentingURL:allowViewAction:completionHandler:"

```
