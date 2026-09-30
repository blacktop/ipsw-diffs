## MobileLookup

> `/System/Library/PrivateFrameworks/MobileLookup.framework/MobileLookup`

```diff

 22.0.0.0.0
-  __TEXT.__text: 0x1f34
-  __TEXT.__auth_stubs: 0x340
+  __TEXT.__text: 0x20d8
+  __TEXT.__auth_stubs: 0x300
   __TEXT.__objc_methlist: 0x338
   __TEXT.__const: 0x90
   __TEXT.__cstring: 0xb4
   __TEXT.__oslogstring: 0x90
-  __TEXT.__unwind_info: 0x110
+  __TEXT.__unwind_info: 0x130
   __TEXT.__objc_classname: 0xab
   __TEXT.__objc_methname: 0xbee
   __TEXT.__objc_methtype: 0x1ec

   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_selrefs: 0x3a0
   __DATA_CONST.__objc_superrefs: 0x28
-  __AUTH_CONST.__auth_got: 0x1a8
+  __AUTH_CONST.__auth_got: 0x188
   __AUTH_CONST.__const: 0x20
   __AUTH_CONST.__cfstring: 0x140
   __AUTH_CONST.__objc_const: 0x708

   - /System/Library/PrivateFrameworks/SpringBoardServices.framework/SpringBoardServices
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: DC89B4D8-ABB3-33C1-B2F6-00E0D08E1AD8
+  UUID: D38A2508-1521-3B40-8AB9-8B32FBBC6F83
   Functions: 71
-  Symbols:   388
+  Symbols:   384
   CStrings:  204
 
Symbols:
+ _objc_retainAutoreleasedReturnValue
+ _objc_retain_x21
+ _objc_retain_x27
- _objc_claimAutoreleasedReturnValue
- _objc_release_x28
- _objc_retainAutoreleaseReturnValue
- _objc_retain_x2
- _objc_retain_x25
- _objc_retain_x4
- _objc_retain_x8
Functions:
~ +[MLULookupItemContent contentWithURL:result:documentProperties:] : 156 -> 152
~ -[MLULookupItemContent setupViewControllerInCommitMode] : 256 -> 272
~ -[MLULookupItemContent commitPreviewInController:] : 300 -> 316
~ -[MLULookupItemContent dismissViewController] : 76 -> 80
~ -[MLULookupItemContent setPreviewViewController:] : 12 -> 64
~ -[MLULookupItemContent setCommitViewController:] : 12 -> 64
~ -[MLULookupItemContent setCommitURL:] : 12 -> 64
~ -[DDPreviewNavigationController previewActions] : 116 -> 124
~ -[MLULookupItemDDContent initWithURL:result:documentProperties:] : 480 -> 504
~ -[MLULookupItemDDContent commitType] : 92 -> 96
~ -[MLULookupItemRawTextContent initWithText:range:] : 224 -> 232
~ -[MLULookupItemRawTextContent setupViewControllerInCommitMode] : 68 -> 72
~ -[MLULookupItemAttachmentContent initWithAttachments:currentAttachmentIndex:] : 184 -> 188
~ -[MLUBlurryView _activateBlurring] : 292 -> 300
~ -[MLUBlurryView blurRadius] : 112 -> 120
~ -[MLUBlurryView setBlurRadius:] : 160 -> 168
~ -[MLUBlurryView setShouldRasterizeForTransition:] : 204 -> 220
~ -[MLULookupItem initWithURL:dataDetectorsResult:text:range:] : 196 -> 188
~ -[MLULookupItem _resolveAttachments:currentAttachmentIndex:] : 476 -> 480
~ -[MLULookupItem _resolveURL:DDResult:focusRange:] : 200 -> 208
~ -[MLULookupItem _resolveText:focusRange:] : 384 -> 388
~ -[MLULookupItem resolve] : 220 -> 224
~ -[MLULookupItem webUrlToPresent] : 8 -> 56
~ -[MLULookupItem viewControllerToPresent] : 76 -> 84
~ -[MLULookupItem commit] : 120 -> 132
~ -[MLULookupItem commitType] : 56 -> 60
~ -[MLULookupItem commitWithTransitionForPreviewViewController:inViewController:completion:] : 1140 -> 1136
~ ___90-[MLULookupItem commitWithTransitionForPreviewViewController:inViewController:completion:]_block_invoke_2 : 92 -> 96
~ ___90-[MLULookupItem commitWithTransitionForPreviewViewController:inViewController:completion:]_block_invoke_3 : 88 -> 92
~ -[MLULookupItem setPreviewContent:] : 12 -> 64

```
