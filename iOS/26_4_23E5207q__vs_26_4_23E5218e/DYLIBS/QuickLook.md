## QuickLook

> `/System/Library/Frameworks/QuickLook.framework/QuickLook`

```diff

-1016.205.2.0.0
-  __TEXT.__text: 0xdd3b0
+1016.205.3.0.0
+  __TEXT.__text: 0xdd304
   __TEXT.__auth_stubs: 0x2520
   __TEXT.__delay_helper: 0x948
   __TEXT.__objc_methlist: 0xb58c
-  __TEXT.__const: 0x31e4
+  __TEXT.__const: 0x3214
   __TEXT.__gcc_except_tab: 0x1954
-  __TEXT.__oslogstring: 0x5537
+  __TEXT.__oslogstring: 0x5657
   __TEXT.__cstring: 0x51dc
   __TEXT.__ustring: 0x1c
   __TEXT.__swift5_typeref: 0x19e8

   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  UUID: F6057061-2F7F-3305-9F23-9E3F07656B55
+  UUID: 726FB5A0-2A71-37E0-878D-F8E7DE03C99C
   Functions: 5521
   Symbols:   14102
   CStrings:  7250
Functions:
~ ___93-[QLItemPresenterViewController loadPreviewControllerWithContents:context:completionHandler:]_block_invoke_5 : 476 -> 480
~ sub_24299e668 -> sub_242a7f66c : 1216 -> 1204
~ sub_2429b836c -> sub_242a99364 : 2860 -> 2832
~ sub_2429bce94 -> sub_242a9de70 : 2668 -> 2636
~ sub_2429bdcc4 -> sub_242a9ec80 : 1152 -> 1144
~ sub_2429bfa58 -> sub_242aa0a0c : 2184 -> 2132
~ sub_2429c02e0 -> sub_242aa1260 : 2420 -> 2392
~ sub_2429c1dd8 -> sub_242aa2d3c : 1704 -> 1680
~ sub_2429cfb38 -> sub_242ab0a84 : 1232 -> 1240
CStrings:
+ "About to save edited copy (%{private}@) over item (%{private}@) at index %lu #PreviewController"
+ "Cancelled loading view controller because transformedContent is nil for item: %{private}@. #ItemPresenter"
+ "Could not create temporary directory because preview controller (%{private}@) is not the current preview controller (%{private}@) #PreviewCollection"
+ "Could not forward message to host because preview controller (%{private}@) is not the current preview controller (%{private}@) #PreviewCollection"
+ "Could not show share sheet for item %{private}@ because device is locked. #Sharing"
+ "Could not show share sheet for item %{private}@ using popover tracker because popover tracker is nil. #Sharing"
+ "Error while attempting to load controller for preview item (%{private}@): %@ #PreviewCollection"
+ "Finished loading controller for preview item (%{private}@) successfully. #PreviewCollection"
+ "Not saving changes for edited copy %{private}@ of item at index %lu because this version has already been forwarded to the delegate. #PreviewController"
+ "Passing URL: %{private}@ to UIDocumentInteractionController to share item: %{private}@. #Sharing"
+ "Passing no URL to UIDocumentInteractionController to share item: %{private}@. #Sharing"
+ "Preview controller: %{private}@ didUpdateContentsOfPreviewItem:%{private}@. #PreviewController"
+ "Preview controller: %{private}@ is handling updated item: %{private}@, with updated copy: %{private}@. #PreviewController"
+ "QLItemViewController (contents: %{private}@) did fail with error: %@. #PreviewCollection"
+ "The item (%{private}@) at index n°%lu is about to be updated with an edited copy (%{private}@) but it's not currently previewed. Current preview item index is %lu. #PreviewController"
+ "Unknown preview item type in -previewItemViewControllerClassName: for preview item %{private}@ #PreviewItem"
+ "Unsupported preview item type in -previewItemViewControllerClassName: for preview item %{private}@ #PreviewItem"
+ "Will _startLoadingPreviewWithContents because presenter successfully fetched content of preview item: %{private}@, contents: %{private}@. #PreviewController"
+ "Will show error view because presenter could not successfully fetch content of preview item: %{private}@, contents: %{private}@, error: %@. #PreviewController"
+ "Will show error view controller because can't preview item: %{private}@. #PreviewController"
+ "Won't show share for remote view again for item %{private}@ because it is already visible on screen. #Sharing"
+ "[API] currentPreviewItem called, returning %{private}@ #PreviewController"
- "About to save edited copy (%@) over item (%@) at index %lu #PreviewController"
- "Cancelled loading view controller because transformedContent is nil for item: %@. #ItemPresenter"
- "Could not create temporary directory because preview controller (%@) is not the current preview controller (%@) #PreviewCollection"
- "Could not forward message to host because preview controller (%@) is not the current preview controller (%@) #PreviewCollection"
- "Could not show share sheet for item %@ because device is locked. #Sharing"
- "Could not show share sheet for item %@ using popover tracker because popover tracker is nil. #Sharing"
- "Error while attempting to load controller for preview item (%@): %@ #PreviewCollection"
- "Finished loading controller for preview item (%@) successfully. #PreviewCollection"
- "Not saving changes for edited copy %@ of item at index %lu because this version has already been forwarded to the delegate. #PreviewController"
- "Passing URL: %@ to UIDocumentInteractionController to share item: %@. #Sharing"
- "Passing no URL to UIDocumentInteractionController to share item: %@. #Sharing"
- "Preview controller: %@ didUpdateContentsOfPreviewItem:%@. #PreviewController"
- "Preview controller: %@ is handling updated item: %@, with updated copy: %@. #PreviewController"
- "QLItemViewController (contents: %@) did fail with error: %@. #PreviewCollection"
- "The item (%@) at index n°%lu is about to be updated with an edited copy (%@) but it's not currently previewed. Current preview item index is %lu. #PreviewController"
- "Unknown preview item type in -previewItemViewControllerClassName: for preview item %@ #PreviewItem"
- "Unsupported preview item type in -previewItemViewControllerClassName: for preview item %@ #PreviewItem"
- "Will _startLoadingPreviewWithContents because presenter successfully fetched content of preview item: %@, contents: %@. #PreviewController"
- "Will show error view because presenter could not successfully fetch content of preview item: %@, contents: %@, error: %@. #PreviewController"
- "Will show error view controller because can't preview item: %@. #PreviewController"
- "Won't show share for remote view again for item %@ because it is already visible on screen. #Sharing"
- "[API] currentPreviewItem called, returning %@ #PreviewController"

```
