## MailUI

> `/System/Library/PrivateFrameworks/MailUI.framework/Versions/A/MailUI`

### Sections with Same Size but Changed Content

- `__TEXT.__constg_swiftt`
- `__TEXT.__swift5_builtin`
- `__TEXT.__swift5_fieldmd`
- `__TEXT.__swift5_assocty`
- `__TEXT.__swift5_proto`
- `__TEXT.__swift5_types`
- `__TEXT.__swift_as_cont`
- `__TEXT.__swift5_protos`
- `__TEXT.__swift5_mpenum`
- `__TEXT.__unwind_info`
- `__TEXT.__eh_frame`
- `__DATA_CONST.__objc_classlist`
- `__DATA_CONST.__objc_catlist`
- `__DATA_CONST.__objc_protorefs`
- `__DATA_CONST.__objc_superrefs`
- `__DATA_CONST.__objc_arraydata`
- `__AUTH_CONST.__objc_intobj`
- `__AUTH_CONST.__objc_arrayobj`
- `__AUTH_CONST.__objc_floatobj`
- `__AUTH.__data`
- `__DATA.__objc_stublist`

```diff

-3895.100.17.0.0
-  __TEXT.__text: 0x3011f4
-  __TEXT.__objc_methlist: 0xf5dc
-  __TEXT.__cstring: 0x10709
-  __TEXT.__const: 0x195e4
+3897.100.8.1.1
+  __TEXT.__text: 0x3015b4
+  __TEXT.__objc_methlist: 0xf7ec
+  __TEXT.__cstring: 0x10789
+  __TEXT.__const: 0x195f4
   __TEXT.__gcc_except_tab: 0x1238
-  __TEXT.__oslogstring: 0x7656
+  __TEXT.__oslogstring: 0x7706
   __TEXT.__dlopen_cstrs: 0xba
   __TEXT.__ustring: 0x30c
-  __TEXT.__swift5_typeref: 0x164ba
-  __TEXT.__swift5_capture: 0x436c
+  __TEXT.__swift5_typeref: 0x164ce
+  __TEXT.__swift5_capture: 0x438c
   __TEXT.__constg_swiftt: 0x3ae8
   __TEXT.__swift5_builtin: 0x410
   __TEXT.__swift5_reflstr: 0x2da1

   __TEXT.__swift5_assocty: 0xf58
   __TEXT.__swift5_proto: 0x598
   __TEXT.__swift5_types: 0x458
-  __TEXT.__swift_as_entry: 0x180
-  __TEXT.__swift_as_ret: 0x158
+  __TEXT.__swift_as_entry: 0x184
+  __TEXT.__swift_as_ret: 0x15c
   __TEXT.__swift_as_cont: 0x258
   __TEXT.__swift5_protos: 0x20
   __TEXT.__swift5_mpenum: 0x28

   __TEXT.__objc_classname: 0x0
   __TEXT.__objc_methname: 0x0
   __TEXT.__objc_methtype: 0x0
-  __DATA_CONST.__const: 0x1cf0
+  __DATA_CONST.__const: 0x1d28
   __DATA_CONST.__objc_classlist: 0x608
   __DATA_CONST.__objc_catlist: 0xb0
-  __DATA_CONST.__objc_protolist: 0x458
+  __DATA_CONST.__objc_protolist: 0x460
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0xa5b0
+  __DATA_CONST.__objc_selrefs: 0xa6f8
   __DATA_CONST.__objc_protorefs: 0x130
   __DATA_CONST.__objc_superrefs: 0x378
   __DATA_CONST.__objc_arraydata: 0x40
-  __DATA_CONST.__got: 0x2400
-  __AUTH_CONST.__const: 0x11658
-  __AUTH_CONST.__cfstring: 0x7f20
-  __AUTH_CONST.__objc_const: 0x1aba8
+  __DATA_CONST.__got: 0x2410
+  __AUTH_CONST.__const: 0x116a8
+  __AUTH_CONST.__cfstring: 0x8020
+  __AUTH_CONST.__objc_const: 0x1ad60
   __AUTH_CONST.__objc_intobj: 0x1e0
   __AUTH_CONST.__objc_arrayobj: 0x48
   __AUTH_CONST.__objc_floatobj: 0x10
-  __AUTH_CONST.__auth_got: 0x2ac8
-  __AUTH.__objc_data: 0x1968
+  __AUTH_CONST.__auth_got: 0x2ac0
+  __AUTH.__objc_data: 0x1918
   __AUTH.__data: 0x10d8
-  __DATA.__objc_ivar: 0xe50
-  __DATA.__data: 0x7380
+  __DATA.__objc_ivar: 0xe58
+  __DATA.__data: 0x7340
   __DATA.__objc_stublist: 0x8
-  __DATA.__bss: 0x78e0
+  __DATA.__bss: 0x76e0
   __DATA.__common: 0x3d0
-  __DATA_DIRTY.__objc_data: 0x2c20
-  __DATA_DIRTY.__data: 0x2880
-  __DATA_DIRTY.__bss: 0x3fa0
+  __DATA_DIRTY.__objc_data: 0x2c70
+  __DATA_DIRTY.__data: 0x2950
+  __DATA_DIRTY.__bss: 0x41a0
   __DATA_DIRTY.__common: 0x58
   - /System/Library/Frameworks/Accounts.framework/Versions/A/Accounts
   - /System/Library/Frameworks/AddressBook.framework/Versions/A/AddressBook
   - /System/Library/Frameworks/AppIntents.framework/Versions/A/AppIntents
   - /System/Library/Frameworks/AppKit.framework/Versions/C/AppKit
-  - /System/Library/Frameworks/ColorSync.framework/Versions/A/ColorSync
   - /System/Library/Frameworks/Combine.framework/Versions/A/Combine
   - /System/Library/Frameworks/Contacts.framework/Versions/A/Contacts
   - /System/Library/Frameworks/ContactsUI.framework/Versions/A/ContactsUI

   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  Functions: 14697
-  Symbols:   14776
-  CStrings:  2483
+  Functions: 14703
+  Symbols:   14790
+  CStrings:  2491
 
Symbols:
+ +[CSSuggestion(MailUI) mui_personSuggestionForEmailAddresses:displayName:alternateDisplayNames:contactIdentifier:contactScope:userTypedText:currentSuggestion:]
+ -[MUIWKWebViewController _webView:webContentProcessDidTerminateWithReason:]
+ -[MUIWebDocumentView setWebContentProcessTerminationReason:]
+ -[MUIWebDocumentView webContentProcessTerminationReason]
+ OBJC_IVAR_$_MUIWKWebViewController._pendingWebProcessTerminationReason
+ OBJC_IVAR_$_MUIWebDocumentView._webContentProcessTerminationReason
+ _CGColorSpaceCreateWithName
+ _EMMessageListItemKeyPathSearchRelevanceScore
+ _MDItemContactIdentifier
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_OPT_WKNavigationDelegatePrivate
+ __OBJC_$_PROTOCOL_METHOD_TYPES_WKNavigationDelegatePrivate
+ __OBJC_$_PROTOCOL_REFS_WKNavigationDelegatePrivate
+ __OBJC_LABEL_PROTOCOL_$_WKNavigationDelegatePrivate
+ __OBJC_PROTOCOL_$_WKNavigationDelegatePrivate
+ ___swift_allocate_boxed_opaque_existential_0
+ _kCGColorSpaceSRGB
+ _objc_msgSend$setAttribute:forKey:
+ _objc_msgSend$setWebContentProcessTerminationReason:
+ _objc_msgSend$webContentProcessTerminationReason
+ _symbolic ypIegn_
+ _symbolic ypytIegnr_
- +[CSSuggestion(MailUI) mui_personSuggestionForEmailAddresses:displayName:alternateDisplayNames:contactScope:userTypedText:currentSuggestion:]
- -[MUIWKWebViewController webViewWebContentProcessDidTerminate:]
- _CGColorSpaceCreateWithICCData
- _ColorSyncProfileCopyData
- _ColorSyncProfileCreateWithName
- _EMMessageListItemKeyPathSearchRelevanceRank
- _kColorSyncSRGBProfile
CStrings:
+ " may not be available while Mail is indexing."
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.iALTLZ/Sources/Mail/MailUI/MailUI/common/Avatars/MUIAvatarImageGeneratorResult.h"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.iALTLZ/Sources/Mail/MailUI/MailUI/common/Avatars/MUIBusinessServiceProvider.h"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.iALTLZ/Sources/Mail/MailUI/MailUI/common/Avatars/MUISenderHeaderColors.h"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.iALTLZ/Sources/Mail/MailUI/MailUI/common/Bucket/About Categories/MUIAboutCategoriesViewController.h"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.iALTLZ/Sources/Mail/MailUI/MailUI/common/Bucket/Model/MUILastSeenBucketHelper.swift"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.iALTLZ/Sources/Mail/MailUI/MailUI/common/Conversation View/CatchUp/MUIManualSummaryController.h"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.iALTLZ/Sources/Mail/MailUI/MailUI/common/Conversation View/CatchUp/MUIManualSummaryViewManager.h"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.iALTLZ/Sources/Mail/MailUI/MailUI/common/Feedback/Model/FeedbackListViewModel.swift"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.iALTLZ/Sources/Mail/MailUI/MailUI/common/Message List/CatchUp/MUIHighlightedMessage.h"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.iALTLZ/Sources/Mail/MailUI/MailUI/common/Message List/CatchUp/MUIHighlightedMessagesController.h"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.iALTLZ/Sources/Mail/MailUI/MailUI/common/Search/Feedback/SearchTTR/Model/MUISearchTTRCollectedDiagnostics.h"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.iALTLZ/Sources/Mail/MailUI/MailUI/common/Search/SearchItem/DonationVisualizationIndexState.swift"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.iALTLZ/Sources/Mail/MailUI/MailUI/common/Search/Snippets/SnippetGenerator.swift"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.iALTLZ/Sources/Mail/MailUI/MailUI/common/Search/Suggestion/MUISiriResultsToken.h"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.iALTLZ/Sources/Mail/MailUI/MailUI/macOS/Categories/MUIRecategorizationMenuController.h"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.iALTLZ/Sources/Mail/MailUI/MailUI/macOS/Categories/MUIRecategorizationViewModel.h"
+ "New-search-available explanation. Placeholder is a time window like '6 months'."
+ "Search-indexing explanation shown while the index is still being prepared."
+ "Some search results may not be available while Mail is indexing. This may take more than a few days."
+ "Some search results older than "
+ "T"
+ "WebContent process became responsive: PID=%d"
+ "WebContent process became unresponsive: PID=%d enhancedSecurity=%{BOOL}d url=%{public}@"
+ "WebContent process terminated (retries exhausted): PID=%d crashCount=%lu reason=%{public}@ enhancedSecurity=%{BOOL}d url=%{public}@"
+ "WebContent process terminated (will retry): PID=%d crashCount=%lu reason=%{public}@ enhancedSecurity=%{BOOL}d url=%{public}@"
+ "WebContent process unresponsive timeout (killing): PID=%d crashCount=%lu enhancedSecurity=%{BOOL}d url=%{public}@"
+ "WebKitEnhancedSecurity"
+ "crash"
+ "exceeded CPU limit"
+ "exceeded memory limit"
+ "exceeded shared process crash limit"
+ "requested by client"
+ "unknown (%ld)"
+ "unresponsive timeout"
- " may not appear until complete."
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.ZXJuBs/Sources/Mail/MailUI/MailUI/common/Avatars/MUIAvatarImageGeneratorResult.h"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.ZXJuBs/Sources/Mail/MailUI/MailUI/common/Avatars/MUIBusinessServiceProvider.h"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.ZXJuBs/Sources/Mail/MailUI/MailUI/common/Avatars/MUISenderHeaderColors.h"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.ZXJuBs/Sources/Mail/MailUI/MailUI/common/Bucket/About Categories/MUIAboutCategoriesViewController.h"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.ZXJuBs/Sources/Mail/MailUI/MailUI/common/Bucket/Model/MUILastSeenBucketHelper.swift"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.ZXJuBs/Sources/Mail/MailUI/MailUI/common/Conversation View/CatchUp/MUIManualSummaryController.h"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.ZXJuBs/Sources/Mail/MailUI/MailUI/common/Conversation View/CatchUp/MUIManualSummaryViewManager.h"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.ZXJuBs/Sources/Mail/MailUI/MailUI/common/Feedback/Model/FeedbackListViewModel.swift"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.ZXJuBs/Sources/Mail/MailUI/MailUI/common/Message List/CatchUp/MUIHighlightedMessage.h"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.ZXJuBs/Sources/Mail/MailUI/MailUI/common/Message List/CatchUp/MUIHighlightedMessagesController.h"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.ZXJuBs/Sources/Mail/MailUI/MailUI/common/Search/Feedback/SearchTTR/Model/MUISearchTTRCollectedDiagnostics.h"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.ZXJuBs/Sources/Mail/MailUI/MailUI/common/Search/SearchItem/DonationVisualizationIndexState.swift"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.ZXJuBs/Sources/Mail/MailUI/MailUI/common/Search/Snippets/SnippetGenerator.swift"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.ZXJuBs/Sources/Mail/MailUI/MailUI/common/Search/Suggestion/MUISiriResultsToken.h"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.ZXJuBs/Sources/Mail/MailUI/MailUI/macOS/Categories/MUIRecategorizationMenuController.h"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.ZXJuBs/Sources/Mail/MailUI/MailUI/macOS/Categories/MUIRecategorizationViewModel.h"
- "Mail is organizing messages for better results. Some results older than "
- "Mail is organizing messages for better results. This may take more than a few days."
- "New-search-available explanation on macOS. Placeholder is a time window like '6 months'."
- "Search-indexing explanation on macOS while the index is still being prepared."
- "Web Content process with id %d became responsive"
- "WebContent process became unresponsive: PID=%d"
- "WebContent process terminated (retries exhausted): PID=%d crashCount=%lu"
- "WebContent process terminated (will retry): PID=%d crashCount=%lu"
- "WebContent process unresponsive timeout (killing): PID=%d crashCount=%lu"
- "failed to create sRGB profile"
```
