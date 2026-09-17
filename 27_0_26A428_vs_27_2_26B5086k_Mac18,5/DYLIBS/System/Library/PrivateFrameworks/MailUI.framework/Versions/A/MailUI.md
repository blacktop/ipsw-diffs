## MailUI

> `/System/Library/PrivateFrameworks/MailUI.framework/Versions/A/MailUI`

```diff

-3901.100.1.1.11
-  __TEXT.__text: 0x2fe1f4
-  __TEXT.__objc_methlist: 0xf95c
-  __TEXT.__cstring: 0x10da9
-  __TEXT.__const: 0x19724
-  __TEXT.__gcc_except_tab: 0x1208
-  __TEXT.__oslogstring: 0x7866
+3901.200.34.0.0
+  __TEXT.__text: 0x2fde0c
+  __TEXT.__objc_methlist: 0xf98c
+  __TEXT.__cstring: 0x10a39
+  __TEXT.__const: 0x195e4
+  __TEXT.__gcc_except_tab: 0x124c
+  __TEXT.__oslogstring: 0x7f36
   __TEXT.__dlopen_cstrs: 0xba
   __TEXT.__ustring: 0x30c
-  __TEXT.__swift5_typeref: 0x16856
-  __TEXT.__swift5_capture: 0x443c
-  __TEXT.__constg_swiftt: 0x3b60
+  __TEXT.__swift5_typeref: 0x16800
+  __TEXT.__swift5_capture: 0x442c
+  __TEXT.__constg_swiftt: 0x3ae8
   __TEXT.__swift5_builtin: 0x410
-  __TEXT.__swift5_reflstr: 0x2e31
-  __TEXT.__swift5_fieldmd: 0x2a88
+  __TEXT.__swift5_reflstr: 0x2e01
+  __TEXT.__swift5_fieldmd: 0x2a38
   __TEXT.__swift5_assocty: 0xf58
-  __TEXT.__swift5_proto: 0x598
-  __TEXT.__swift5_types: 0x460
+  __TEXT.__swift5_proto: 0x590
+  __TEXT.__swift5_types: 0x454
   __TEXT.__swift_as_entry: 0x188
   __TEXT.__swift_as_ret: 0x160
   __TEXT.__swift_as_cont: 0x264
   __TEXT.__swift5_protos: 0x20
   __TEXT.__swift5_mpenum: 0x28
-  __TEXT.__unwind_info: 0xd738
-  __TEXT.__eh_frame: 0x2f0c
+  __TEXT.__unwind_info: 0xd6e0
+  __TEXT.__eh_frame: 0x2ed4
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0
   __TEXT.__objc_classname: 0x0
   __TEXT.__objc_methname: 0x0
   __TEXT.__objc_methtype: 0x0
-  __DATA_CONST.__const: 0x1d20
-  __DATA_CONST.__objc_classlist: 0x608
-  __DATA_CONST.__objc_catlist: 0xb0
+  __DATA_CONST.__const: 0x1cc8
+  __DATA_CONST.__objc_classlist: 0x5f8
+  __DATA_CONST.__objc_catlist: 0xb8
   __DATA_CONST.__objc_protolist: 0x478
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0xa7d0
+  __DATA_CONST.__objc_selrefs: 0xa7c0
   __DATA_CONST.__objc_protorefs: 0x140
-  __DATA_CONST.__objc_superrefs: 0x378
+  __DATA_CONST.__objc_superrefs: 0x370
   __DATA_CONST.__objc_arraydata: 0x40
   __DATA_CONST.__got: 0x2448
-  __AUTH_CONST.__const: 0x11848
-  __AUTH_CONST.__cfstring: 0x8040
-  __AUTH_CONST.__objc_const: 0x1ade0
+  __AUTH_CONST.__const: 0x11808
+  __AUTH_CONST.__cfstring: 0x7c00
+  __AUTH_CONST.__objc_const: 0x1ae48
   __AUTH_CONST.__objc_intobj: 0x1e0
   __AUTH_CONST.__objc_arrayobj: 0x48
   __AUTH_CONST.__objc_floatobj: 0x10
-  __AUTH_CONST.__auth_got: 0x2ae0
-  __AUTH.__objc_data: 0x1918
-  __AUTH.__data: 0x10d8
-  __DATA.__objc_ivar: 0xe40
-  __DATA.__data: 0x74b0
+  __AUTH_CONST.__auth_got: 0x2b18
+  __AUTH.__objc_data: 0x1818
+  __AUTH.__data: 0x10b8
+  __DATA.__objc_ivar: 0xe54
+  __DATA.__data: 0x7490
   __DATA.__objc_stublist: 0x8
   __DATA.__common: 0x3d8
   __DATA_DIRTY.__objc_data: 0x2c70
-  __DATA_DIRTY.__data: 0x2980
-  __DATA_DIRTY.__bss: 0x41b0
+  __DATA_DIRTY.__data: 0x2960
+  __DATA_DIRTY.__bss: 0x40c0
   __DATA_DIRTY.__common: 0x58
   - /System/Library/Frameworks/Accounts.framework/Versions/A/Accounts
   - /System/Library/Frameworks/AddressBook.framework/Versions/A/AddressBook

   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  Functions: 14798
-  Symbols:   14792
-  CStrings:  2509
+  Functions: 14781
+  Symbols:   14790
+  CStrings:  2516
 
Symbols:
+ +[MUIWebAttachmentController log]
+ -[MUIAddressField currentSearchRequestNetworkStartTime]
+ -[MUIAddressField currentSearchRequestStartTime]
+ -[MUIAddressField setCurrentSearchRequestNetworkStartTime:]
+ -[MUIAddressField setCurrentSearchRequestStartTime:]
+ -[MUIMessageListViewController reportEngagementAction:onItemID:atIndexPath:]
+ -[MUIWKWebViewController _commitReloadForDocument:attachments:]
+ -[MUIWebAttachment cachedImageMetadata]
+ -[MUIWebAttachment hasImageMetadata]
+ -[MUIWebAttachment needsImageMetadataPrefetch]
+ -[MUIWebAttachment prefetchImageMetadataWithWebView:completionHandler:]
+ -[MUIWebAttachmentController _imageMetadata]
+ -[MessageListPositionHelper actuallyVisibleIndexPaths]
+ -[NSTextField(MailUI) mui_changeAttributedStringHighlightingUsingSelectedStyle:]
+ EFGetElapsedTimeSinceAbsoluteTime.onceToken
+ EFGetElapsedTimeSinceAbsoluteTime.sTimebaseInfo
+ GCC_except_table101
+ GCC_except_table111
+ GCC_except_table142
+ GCC_except_table84
+ GCC_except_table86
+ OBJC_IVAR_$_MUIAddressField._currentSearchRequestNetworkStartTime
+ OBJC_IVAR_$_MUIAddressField._currentSearchRequestStartTime
+ OBJC_IVAR_$_MUIWKWebViewController._reloadGeneration
+ OBJC_IVAR_$_MUIWebAttachment._cachedImageMetadata
+ OBJC_IVAR_$_MUIWebAttachment._hasImageMetadata
+ ShouldUpdateAccessibilityIdentifier
+ ShouldUpdateAccessibilityIdentifier.onceToken
+ ShouldUpdateAccessibilityIdentifier.shouldUpdateAccessibilityIdentifier
+ UpdateAccessibilityIdentifierIfNeeded
+ _OBJC_CLASS_$_ACAccount
+ _OBJC_CLASS_$_MCImageMetadataService
+ _ShouldUpdateAccessibilityIdentifier
+ _UpdateAccessibilityIdentifierIfNeeded
+ __41-[MUIWKWebViewController _reloadDocument]_block_invoke
+ __55-[MUIAddressField autocompleteFetch:didReceiveResults:]_block_invoke
+ __71-[MUIWebAttachment prefetchImageMetadataWithWebView:completionHandler:]_block_invoke
+ __OBJC_$_CATEGORY_INSTANCE_METHODS_NSTextField_$_MailUI
+ __OBJC_$_CATEGORY_NSTextField_$_MailUI
+ __OBJC_$_CLASS_METHODS_MUIWebAttachmentController
+ __OBJC_$_CLASS_PROP_LIST_MUIAddressField
+ ___33+[MUIWebAttachmentController log]_block_invoke
+ ___41-[MUIWKWebViewController _reloadDocument]_block_invoke
+ ___54-[MessageListPositionHelper actuallyVisibleIndexPaths]_block_invoke
+ ___59-[MUIWKWebViewController dataDetectorsExternalUIRequested:]_block_invoke_3
+ ___59-[MUIWKWebViewController dataDetectorsExternalUIRequested:]_block_invoke_4
+ ___71-[MUIWebAttachment prefetchImageMetadataWithWebView:completionHandler:]_block_invoke
+ ___80-[NSTextField(MailUI) mui_changeAttributedStringHighlightingUsingSelectedStyle:]_block_invoke
+ ___EFGetElapsedTimeSinceAbsoluteTime_block_invoke
+ ___ShouldUpdateAccessibilityIdentifier_block_invoke
+ ___block_descriptor_48_e8_32bs40r_e5_v8?0l
+ ___block_descriptor_48_e8_32bs40w_e43_v24?0"MCImageMetadataResult"8"NSError"16l
+ ___block_descriptor_48_e8_32r40r_e5_v8?0l
+ ___block_descriptor_64_e8_32s40s48r56r_e36_v40?0"NSColor"8{_NSRange=QQ}16^B32l
+ ___block_descriptor_64_e8_32s40s48s_e5_v8?0l
+ ___block_descriptor_72_e8_32s_e21_B16?0"NSIndexPath"8l
+ _kMUIShouldShowHasHighlightedInAccessibilityIdentifierKey
+ _mach_absolute_time
+ _mach_timebase_info
+ _objc_msgSend$_commitReloadForDocument:attachments:
+ _objc_msgSend$_delaysWebProcessLaunchUntilFirstLoad
+ _objc_msgSend$_imageMetadata
+ _objc_msgSend$_setDelaysWebProcessLaunchUntilFirstLoad:
+ _objc_msgSend$accessibilityIdentifier
+ _objc_msgSend$cachedImageMetadata
+ _objc_msgSend$currentSearchRequestNetworkStartTime
+ _objc_msgSend$currentSearchRequestStartTime
+ _objc_msgSend$handlerForURLScheme:
+ _objc_msgSend$isMultiPage
+ _objc_msgSend$isRetina
+ _objc_msgSend$metadataForImageData:webView:completionHandler:
+ _objc_msgSend$mui_changeAttributedStringHighlightingUsingSelectedStyle:
+ _objc_msgSend$needsImageMetadataPrefetch
+ _objc_msgSend$performSelector:
+ _objc_msgSend$pixelHeight
+ _objc_msgSend$pixelWidth
+ _objc_msgSend$prefetchImageMetadataWithWebView:completionHandler:
+ _objc_msgSend$setCurrentSearchRequestNetworkStartTime:
+ _objc_msgSend$setCurrentSearchRequestStartTime:
+ _objc_msgSend$sizeInPoints
- +[MUIMessageListTableCellView changeAttributedStringHighlighting:useSelectedStyle:]
- -[MUISegmentedToolbarItem initWithDictionaryRepresentation:]
- -[MUISegmentedToolbarItem setView:]
- -[MUISegmentedToolbarItem sizeToFit]
- -[MUISegmentedToolbarItem validate]
- -[MUISegmentedToolbarItem view]
- -[MUIWKWebViewController _imageAttachments]
- -[MessageListPositionHelper actuallyVisibleItemIDs]
- GCC_except_table106
- GCC_except_table140
- GCC_except_table141
- GCC_except_table83
- GCC_except_table85
- GCC_except_table96
- _MUISegmentedControlForDescriptors
- _MUIToolbarSegmentKeyAlternateImage
- _MUIToolbarSegmentKeyImage
- _MUIToolbarSegmentKeyLabel
- _MUIToolbarSegmentKeyMenu
- _MUIToolbarSegmentKeyTag
- _MUIToolbarSegmentKeyToolTip
- _MUIToolbarSegmentKeyWidth
- _MUIToolbarSegmentedItemGroupKeyIdentifier
- _MUIToolbarSegmentedItemGroupKeyItems
- _MUIToolbarSegmentedItemKeyIdentifier
- _MUIToolbarSegmentedItemKeyLabels
- _MUIToolbarSegmentedItemKeySegments
- _NSLog
- _OBJC_CLASS_$_MUISegmentedToolbarItem
- _OBJC_CLASS_$_NSSegmentedControl
- _OBJC_CLASS_$_NSToolbarItem
- _OBJC_CLASS_$__TtC6MailUI25CircularPlatformImageView
- _OBJC_METACLASS_$_MUISegmentedToolbarItem
- _OBJC_METACLASS_$_NSImageView
- _OBJC_METACLASS_$_NSToolbarItem
- _OBJC_METACLASS_$__TtC6MailUI25CircularPlatformImageView
- __59-[MUIWKWebViewController dataDetectorsExternalUIRequested:]_block_invoke
- __59-[MUIWKWebViewController dataDetectorsExternalUIRequested:]_block_invoke_2
- __DATA__TtC6MailUI25CircularPlatformImageView
- __INSTANCE_METHODS__TtC6MailUI25CircularPlatformImageView
- __METACLASS_DATA__TtC6MailUI25CircularPlatformImageView
- __OBJC_$_INSTANCE_METHODS_MUISegmentedToolbarItem
- __OBJC_$_PROP_LIST_MUISegmentedToolbarItem
- __OBJC_CLASS_RO_$_MUISegmentedToolbarItem
- __OBJC_METACLASS_RO_$_MUISegmentedToolbarItem
- ___51-[MessageListPositionHelper actuallyVisibleItemIDs]_block_invoke
- ___55-[MUIAddressField autocompleteFetch:didReceiveResults:]_block_invoke_2
- ___83+[MUIMessageListTableCellView changeAttributedStringHighlighting:useSelectedStyle:]_block_invoke
- ___MUISegmentedControlForDescriptors_block_invoke
- ___block_descriptor_40_e8_32s_e29_v32?0"NSDictionary"8Q16^B24l
- ___block_descriptor_48_e8_32s40s_e36_v40?0"NSColor"8{_NSRange=QQ}16^B32l
- ___block_descriptor_57_e8_32s40s48s_e5_v8?0l
- ___block_descriptor_72_e8_32s_e21_16?0"NSIndexPath"8l
- _associated conformance 6MailUI16PlatformLocationVSHAASQ
- _objc_msgSend$_setAllPossibleLabelsToFit:
- _objc_msgSend$aa_primaryAppleAccount
- _objc_msgSend$changeAttributedStringHighlighting:useSelectedStyle:
- _objc_msgSend$initWithDouble:
- _objc_msgSend$initWithItemIdentifier:
- _objc_msgSend$renderInContext:
- _objc_msgSend$setAlternateImage:forSegment:
- _objc_msgSend$setImage:forSegment:
- _objc_msgSend$setLabel:forSegment:
- _objc_msgSend$setMaxSize:
- _objc_msgSend$setMenu:forSegment:
- _objc_msgSend$setPaletteLabel:
- _objc_msgSend$setSegmentCount:
- _objc_msgSend$setShowsMenuIndicator:forSegment:
- _objc_msgSend$setTag:forSegment:
- _objc_msgSend$setToolTip:forSegment:
- _objc_msgSend$setTrackingMode:
- _objc_msgSend$setWidth:forSegment:
- _objc_msgSend$sharedHandler
- _objc_msgSend$targetForAction:to:from:
- _objc_msgSend$validateToolbarItem:
- _objc_msgSend$validateUserInterfaceItem:
- _symbolic SaySo15MUIGradientStopCG
- _symbolic So11NSImageViewC
- _symbolic So15CAGradientLayerC
- _symbolic _____ 6MailUI16PlatformLocationV
- _symbolic _____ 6MailUI25CircularPlatformImageViewC
- _type_layout_string 6MailUI16PlatformLocationV
CStrings:
+ "\r\n"
+ "&amp;"
+ "&gt;"
+ "&lt;"
+ ".hasHighlighted"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Applications/Xcode.app/Contents/Developer/Platforms/MacOSX.platform/Developer/SDKs/MacOSX27.2.Internal.sdk/System/Library/PrivateFrameworks/Email.framework/Headers/EMContentRequestOptions.h"
+ "<"
+ "</body></html>"
+ "<br>"
+ "<html><body dir=\"auto\">"
+ ">"
+ "Autocomplete %{public}s selector (%{public}@)."
+ "Autocomplete cancelled for request %{public}@."
+ "Autocomplete delegate called selectedResult (type=%ld, source=%ld): %{public}@"
+ "Autocomplete display completion string %{public}@"
+ "Autocomplete enqueued a delayed search for \"%{public}@\""
+ "Autocomplete enqueued a delayed search for \"%{public}@\" (forward typing)"
+ "Autocomplete enqueued fetch request using \"%{public}@\"."
+ "Autocomplete fetch %{public}@ did begin network activity after %.0f ms."
+ "Autocomplete fetch %{public}@ did end network activity after %.0f ms."
+ "Autocomplete fetch %{public}@ did not match current search request %{public}@; dropping %lu results (currentPrefix length=%lu)."
+ "Autocomplete fetch %{public}@ did not match last successful request %{public}@."
+ "Autocomplete fetch did finish %{public}@ after %.0f ms."
+ "Autocomplete fetch did receive %lu results from fetch %{public}@ after %.0f ms (sourceTypes=0x%lx)."
+ "Autocomplete fetch request for prefix \"%{public}@\" (length=%lu); currentSearchRequest %{public}@."
+ "Autocomplete presenting results for fetch %{public}@."
+ "Autocomplete selection did change %{public}@"
+ "Autocomplete updated current prefix to \"%{public}@\""
+ "Autocomplete window select result for string \"%{public}@\"."
+ "C\xf3"
+ "Error performing autocompletion: %{public}@"
+ "Image metadata prefetch returned no data: %{public}@"
+ "Image metadata prefetch timed out; will retry on next reload"
+ "Image metadata unavailable for TIFF; treating as not displayable inline"
+ "Inline TIFF decision deferred. Image metadata not yet available; will re-evaluate after prefetch"
+ "ShouldShowHasHighlightedInAccessibilityIdentifier"
+ "WebContentLaunch"
+ "WebKitImageMetadata"
+ "aa_primaryAppleAccount"
+ "const body = document.body;\n// The `Apple-mail-*` class strings and bare `attachment` tag are how MessageUI renders\n// inline photos/PDFs/files; we hardcode them because the ObjC constants aren't in scope here.\nconst preservedSelector = 'blockquote[type=\"cite\"], div#AppleMailSignature, attachment, ' +\n    '.Apple-mail-imageattach, .Apple-mail-pdf, .Apple-mail-fileattach';\n// Use querySelector + walk up so we find the body-level ancestor of a preserved\n// node even when MessageUI wraps it in a div (e.g., a blockquote nested inside\n// a `<div>` wrapper in a user-pasted reply). Iterating `body.children` and\n// matching directly would miss those.\nlet firstPreserved = body.querySelector(preservedSelector);\nwhile (firstPreserved && firstPreserved.parentNode !== body) {\n    firstPreserved = firstPreserved.parentNode;\n}\nif (firstPreserved === null) {\n    body.innerHTML = newHTML;\n    return;\n}\nwhile (body.firstChild && body.firstChild !== firstPreserved) {\n    body.removeChild(body.firstChild);\n}\nif (newHTML.length > 0) {\n    // Insert the parsed nodes directly via a <template> so we don't introduce an\n    // extra wrapper <div> — keeping the same DOM shape as the no-preserved-node\n    // path above (which assigns to `body.innerHTML` without a wrapper).\n    const template = document.createElement('template');\n    template.innerHTML = newHTML;\n    body.insertBefore(template.content, firstPreserved);\n}"
+ "delaysWebProcessLaunchUntilFirstLoad=%d"
+ "hand.raised.fill"
+ "v24@?0@\"MCImageMetadataResult\"8@\"NSError\"16"
- "!view || [view isKindOfClass:[NSSegmentedControl class]]"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Applications/Xcode.app/Contents/Developer/Platforms/MacOSX.platform/Developer/SDKs/MacOSX27.0.Internal.sdk/System/Library/PrivateFrameworks/Email.framework/Headers/EMContentRequestOptions.h"
- "Autocomplete %@ selector (%@)."
- "Autocomplete cancelled for request %@."
- "Autocomplete delegate called selectedResult: %@"
- "Autocomplete display completion string %@"
- "Autocomplete enqueued a delayed search for \"%@\""
- "Autocomplete enqueued fetch request using \"%@\"."
- "Autocomplete fetch %@ did not match current search request %@."
- "Autocomplete fetch %@ did not match last successful request %@."
- "Autocomplete fetch did finish %@."
- "Autocomplete fetch did receive results from fetch %@"
- "Autocomplete fetch request for prefix \"%@\"; currentSearchRequest %@."
- "Autocomplete presenting results for fetch %@."
- "Autocomplete selection did change %@"
- "Autocomplete updated current prefix to \"%@\""
- "Autocomplete window select result for string \"%@\"."
- "CNAutocompleteLogEnabled"
- "C\xd3"
- "Error performing autocompletion: %@"
- "MUISegmentedToolbarItem.m"
- "MUIToolbarSegmentKeyAlternateImage"
- "MUIToolbarSegmentKeyImage"
- "MUIToolbarSegmentKeyLabel"
- "MUIToolbarSegmentKeyMenu"
- "MUIToolbarSegmentKeyTag"
- "MUIToolbarSegmentKeyToolTip"
- "MUIToolbarSegmentKeyWidth"
- "MUIToolbarSegmentedItemGroupKeyIdentifier"
- "MUIToolbarSegmentedItemGroupKeyItems"
- "MUIToolbarSegmentedItemKeyIdentifier"
- "MUIToolbarSegmentedItemKeyLabels"
- "MUIToolbarSegmentedItemKeySegments"
- "const body = document.body;\nconst preservedSelector = 'blockquote[type=\"cite\"], div#AppleMailSignature';\n// Use querySelector + walk up so we find the body-level ancestor of a preserved\n// node even when MessageUI wraps it in a div (e.g., a blockquote nested inside\n// a `<div>` wrapper in a user-pasted reply). Iterating `body.children` and\n// matching directly would miss those.\nlet firstPreserved = body.querySelector(preservedSelector);\nwhile (firstPreserved && firstPreserved.parentNode !== body) {\n    firstPreserved = firstPreserved.parentNode;\n}\nif (firstPreserved === null) {\n    body.innerHTML = newHTML;\n    return;\n}\nwhile (body.firstChild && body.firstChild !== firstPreserved) {\n    body.removeChild(body.firstChild);\n}\nif (newHTML.length > 0) {\n    // Insert the parsed nodes directly via a <template> so we don't introduce an\n    // extra wrapper <div> — keeping the same DOM shape as the no-preserved-node\n    // path above (which assigns to `body.innerHTML` without a wrapper).\n    const template = document.createElement('template');\n    template.innerHTML = newHTML;\n    body.insertBefore(template.content, firstPreserved);\n}"
- "hand.slash"
- "v32@?0@\"NSDictionary\"8Q16^B24"
```
