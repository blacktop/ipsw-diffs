## MobileLookup

> `/System/Library/PrivateFrameworks/MobileLookup.framework/MobileLookup`

```diff

 22.0.0.0.0
-  __TEXT.__text: 0x20d8
-  __TEXT.__auth_stubs: 0x300
+  __TEXT.__text: 0x1f34
   __TEXT.__objc_methlist: 0x338
   __TEXT.__const: 0x90
-  __TEXT.__cstring: 0xb4
+  __TEXT.__cstring: 0xbe
   __TEXT.__oslogstring: 0x90
-  __TEXT.__unwind_info: 0x130
-  __TEXT.__objc_classname: 0xab
-  __TEXT.__objc_methname: 0xbee
-  __TEXT.__objc_methtype: 0x1ec
-  __TEXT.__objc_stubs: 0xbe0
-  __DATA_CONST.__got: 0xb0
+  __TEXT.__unwind_info: 0x110
+  __TEXT.__objc_stubs: 0x0
+  __TEXT.__auth_stubs: 0x0
+  __TEXT.__objc_classname: 0x0
+  __TEXT.__objc_methname: 0x0
+  __TEXT.__objc_methtype: 0x0
   __DATA_CONST.__const: 0x98
   __DATA_CONST.__objc_classlist: 0x38
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_selrefs: 0x3a0
   __DATA_CONST.__objc_superrefs: 0x28
-  __AUTH_CONST.__auth_got: 0x188
+  __DATA_CONST.__got: 0x0
   __AUTH_CONST.__const: 0x20
   __AUTH_CONST.__cfstring: 0x140
   __AUTH_CONST.__objc_const: 0x708
   __AUTH_CONST.__objc_doubleobj: 0x10
+  __AUTH_CONST.__auth_got: 0x0
   __AUTH.__objc_data: 0x230
   __DATA.__objc_ivar: 0x48
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation

   - /System/Library/PrivateFrameworks/SpringBoardServices.framework/SpringBoardServices
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 79D9FD8F-8DDB-340D-B00B-839C7FC81F5E
+  UUID: BAE26505-D18F-3F58-BC02-CFE95BE303DF
   Functions: 71
-  Symbols:   384
-  CStrings:  204
+  Symbols:   388
+  CStrings:  23
 
Symbols:
+ _objc_claimAutoreleasedReturnValue
+ _objc_release_x28
+ _objc_retainAutoreleaseReturnValue
+ _objc_retain_x2
+ _objc_retain_x25
+ _objc_retain_x4
+ _objc_retain_x8
- _objc_retainAutoreleasedReturnValue
- _objc_retain_x21
- _objc_retain_x27
Functions:
~ +[MLULookupItemContent contentWithURL:result:documentProperties:] : 152 -> 156
~ -[MLULookupItemContent setupViewControllerInCommitMode] : 272 -> 256
~ -[MLULookupItemContent commitPreviewInController:] : 316 -> 300
~ -[MLULookupItemContent dismissViewController] : 80 -> 76
~ -[MLULookupItemContent setPreviewViewController:] : 64 -> 12
~ -[MLULookupItemContent setCommitViewController:] : 64 -> 12
~ -[MLULookupItemContent setCommitURL:] : 64 -> 12
~ -[DDPreviewNavigationController previewActions] : 124 -> 116
~ -[MLULookupItemDDContent initWithURL:result:documentProperties:] : 504 -> 484
~ -[MLULookupItemDDContent commitURL] : 16 -> 20
~ -[MLULookupItemDDContent contact] : 16 -> 20
~ -[MLULookupItemDDContent setupViewControllerInCommitMode] : 20 -> 24
~ -[MLULookupItemRawTextContent initWithText:range:] : 232 -> 224
~ -[MLULookupItemRawTextContent setupViewControllerInCommitMode] : 72 -> 68
~ -[MLULookupItemAttachmentContent initWithAttachments:currentAttachmentIndex:] : 188 -> 184
~ -[MLUBlurryView _activateBlurring] : 300 -> 292
~ -[MLUBlurryView blurRadius] : 120 -> 116
~ -[MLUBlurryView setBlurRadius:] : 168 -> 164
~ -[MLUBlurryView setShouldRasterizeForTransition:] : 220 -> 208
~ -[MLUBlurryView shouldRasterizeForTransition] : 16 -> 20
~ -[MLULookupItem initWithURL:dataDetectorsResult:text:range:] : 188 -> 196
~ -[MLULookupItem _resolveURL:DDResult:focusRange:] : 208 -> 200
~ -[MLULookupItem _resolveText:focusRange:] : 388 -> 384
~ -[MLULookupItem resolve] : 224 -> 220
~ -[MLULookupItem webUrlToPresent] : 56 -> 8
~ -[MLULookupItem viewControllerToPresent] : 84 -> 76
~ -[MLULookupItem commit] : 132 -> 120
~ -[MLULookupItem commitType] : 60 -> 56
~ -[MLULookupItem commitWithTransitionForPreviewViewController:inViewController:completion:] : 1136 -> 1144
~ ___90-[MLULookupItem commitWithTransitionForPreviewViewController:inViewController:completion:]_block_invoke_2 : 96 -> 92
~ ___90-[MLULookupItem commitWithTransitionForPreviewViewController:inViewController:completion:]_block_invoke_3 : 92 -> 88
~ -[MLULookupItem setPreviewContent:] : 64 -> 12
~ -[MLULookupItem initWithAttachments:currentAttachment:].cold.1 : 156 -> 112
CStrings:
- ".cxx_destruct"
- "@\"DDPreviewAction\""
- "@\"MLULookupItemContent\""
- "@\"NSArray\""
- "@\"NSDictionary\""
- "@\"NSString\""
- "@\"NSURL\""
- "@\"UIViewController\""
- "@16@0:8"
- "@32@0:8@16Q24"
- "@40@0:8@16^{__DDResult=}24@32"
- "@40@0:8@16{_NSRange=QQ}24"
- "@56@0:8@16^{__DDResult=}24@32{_NSRange=QQ}40"
- "B"
- "B16@0:8"
- "B24@0:8@16"
- "B32@0:8@16Q24"
- "B40@0:8@16{_NSRange=QQ}24"
- "B48@0:8@16^{__DDResult=}24{_NSRange=QQ}32"
- "DDPreviewNavigationController"
- "MLUBlurryView"
- "MLULookupItem"
- "MLULookupItemAttachmentContent"
- "MLULookupItemContent"
- "MLULookupItemDDContent"
- "MLULookupItemRawTextContent"
- "Q"
- "Q16@0:8"
- "T@\"CNContact\",R,N"
- "T@\"MLULookupItemContent\",&,N,V_previewContent"
- "T@\"NSDictionary\",&,V_documentProperties"
- "T@\"NSURL\",&,N,V_commitURL"
- "T@\"UIViewController\",&,N,V_commitViewController"
- "T@\"UIViewController\",&,N,V_previewViewController"
- "TB,N,V_shouldRasterizeForTransition"
- "TB,V_valid"
- "TQ,N,V_commitType"
- "Td"
- "^{__DDResult=}"
- "_activateBlurring"
- "_attachments"
- "_commitType"
- "_commitURL"
- "_commitViewController"
- "_currentAttachmentIndex"
- "_ddResult"
- "_documentProperties"
- "_focusRange"
- "_hasActivated"
- "_previewAction"
- "_previewContent"
- "_previewViewController"
- "_proposedRange"
- "_resolveAttachments:currentAttachmentIndex:"
- "_resolveText:focusRange:"
- "_resolveURL:DDResult:focusRange:"
- "_resolved"
- "_shouldAnimatePropertyWithKey:"
- "_shouldRasterizeForTransition"
- "_text"
- "_url"
- "_valid"
- "addKeyframeWithRelativeStartTime:relativeDuration:animations:"
- "addObject:"
- "addSubview:"
- "animateKeyframesWithDuration:delay:options:animations:completion:"
- "arrayWithObjects:count:"
- "blurRadius"
- "bounds"
- "canOpenURL:"
- "canPreviewItem:"
- "children"
- "colorWithWhite:alpha:"
- "commit"
- "commitPreviewInController:"
- "commitType"
- "commitURL"
- "commitViewController"
- "commitWithTransitionForPreviewViewController:inViewController:completion:"
- "contact"
- "containsString:"
- "contentWithAttachments:currentAttachmentIndex:"
- "contentWithText:range:"
- "contentWithURL:result:documentProperties:"
- "count"
- "countByEnumeratingWithState:objects:count:"
- "d16@0:8"
- "dealloc"
- "defaultWorkspace"
- "dictionaryWithObjects:forKeys:count:"
- "dismissViewController"
- "dismissViewControllerAnimated:completion:"
- "documentProperties"
- "floatValue"
- "indexOfObject:"
- "init"
- "initWithAttachments:currentAttachment:"
- "initWithAttachments:currentAttachmentIndex:"
- "initWithBarButtonSystemItem:target:action:"
- "initWithFrame:"
- "initWithPreviewItems:"
- "initWithString:range:"
- "initWithText:range:"
- "initWithType:"
- "initWithURL:dataDetectorsResult:text:range:"
- "initWithURL:result:documentProperties:"
- "isEqualToString:"
- "layer"
- "length"
- "navigationItem"
- "numberWithDouble:"
- "objectAtIndexedSubscript:"
- "openURL:withOptions:"
- "parsecCollectionViewController"
- "performSelector:withObject:"
- "platterTitle"
- "presentingViewController"
- "previewActionForURL:result:context:"
- "previewActions"
- "previewContent"
- "previewViewController"
- "proposedRange"
- "pushViewController:animated:"
- "removeFromSuperview"
- "requiredEntitlements"
- "requiresEmbeddingNavigationController"
- "resolve"
- "scale"
- "screen"
- "setAlpha:"
- "setBackgroundColor:"
- "setBlurRadius:"
- "setCommitType:"
- "setCommitURL:"
- "setCommitViewController:"
- "setCurrentPreviewItemIndex:"
- "setDocumentProperties:"
- "setEdgesForExtendedLayout:"
- "setFilters:"
- "setHidden:"
- "setModalPresentationStyle:"
- "setName:"
- "setNavigationBarHidden:"
- "setNeedsStatusBarAppearanceUpdate"
- "setPreviewContent:"
- "setPreviewMode:"
- "setPreviewViewController:"
- "setRasterizationScale:"
- "setRightBarButtonItem:"
- "setShouldRasterize:"
- "setShouldRasterizeForTransition:"
- "setTitle:"
- "setTransform:"
- "setUserInteractionEnabled:"
- "setValid:"
- "setValue:forKey:"
- "setValue:forKeyPath:"
- "setupViewControllerInCommitMode"
- "sharedApplication"
- "shouldRasterizeForTransition"
- "snapshotViewAfterScreenUpdates:"
- "subviews"
- "superview"
- "v16@0:8"
- "v20@0:8B16"
- "v24@0:8@16"
- "v24@0:8Q16"
- "v24@0:8d16"
- "v40@0:8@16@24@?32"
- "valid"
- "valueForKeyPath:"
- "view"
- "viewController"
- "viewControllerToPresent"
- "visibleViewController"
- "wantsSeamlessCommit"
- "webUrlToPresent"
- "whiteColor"
- "window"
- "{_NSRange=\"location\"Q\"length\"Q}"
- "{_NSRange=QQ}16@0:8"

```
