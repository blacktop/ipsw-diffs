## MailUI

> `/System/Library/PrivateFrameworks/MailUI.framework/MailUI`

```diff

-3774.200.91.2.1
-  __TEXT.__text: 0xd144c
-  __TEXT.__auth_stubs: 0x1dc0
-  __TEXT.__objc_methlist: 0x42dc
-  __TEXT.__cstring: 0x4f7a
+3774.300.61.2.4
+  __TEXT.__text: 0xd1854
+  __TEXT.__auth_stubs: 0x1dd0
+  __TEXT.__objc_methlist: 0x42fc
+  __TEXT.__cstring: 0x4f8a
   __TEXT.__const: 0x39c4
-  __TEXT.__oslogstring: 0x38d7
+  __TEXT.__oslogstring: 0x3924
   __TEXT.__gcc_except_tab: 0x7a0
   __TEXT.__swift5_typeref: 0x13b6
   __TEXT.__swift5_capture: 0x694

   __TEXT.__swift5_proto: 0x268
   __TEXT.__swift5_types: 0x140
   __TEXT.__swift5_protos: 0x8
-  __TEXT.__unwind_info: 0x34e4
+  __TEXT.__unwind_info: 0x34f0
   __TEXT.__eh_frame: 0xf30
   __TEXT.__objc_classname: 0xc67
-  __TEXT.__objc_methname: 0xf24f
-  __TEXT.__objc_methtype: 0x28b1
+  __TEXT.__objc_methname: 0xf267
+  __TEXT.__objc_methtype: 0x28bd
   __TEXT.__objc_stubs: 0x8f60
   __DATA_CONST.__got: 0x630
   __DATA_CONST.__const: 0x17d8

   __DATA_CONST.__objc_catlist: 0xa0
   __DATA_CONST.__objc_protolist: 0x228
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_const: 0xa3e0
-  __DATA_CONST.__objc_selrefs: 0x32f8
+  __DATA_CONST.__objc_const: 0xa428
+  __DATA_CONST.__objc_selrefs: 0x3300
   __DATA_CONST.__objc_arraydata: 0x28
   __AUTH_CONST.__cfstring: 0x21e0
-  __AUTH_CONST.__objc_const: 0x1f70
+  __AUTH_CONST.__objc_const: 0x1fb8
   __AUTH_CONST.__const: 0x3490
   __AUTH_CONST.__objc_intobj: 0x48
   __AUTH_CONST.__objc_arrayobj: 0x30
   __AUTH_CONST.__objc_doubleobj: 0x10
   __AUTH_CONST.__auth_ptr: 0xd8
-  __AUTH_CONST.__auth_got: 0xef0
+  __AUTH_CONST.__auth_got: 0xef8
   __AUTH.__objc_data: 0xc10
   __AUTH.__data: 0x340
   __DATA.__objc_protorefs: 0xe8
-  __DATA.__objc_classrefs: 0x5d8
+  __DATA.__objc_classrefs: 0x5e0
   __DATA.__objc_superrefs: 0x188
   __DATA.__objc_ivar: 0x5a0
-  __DATA.__data: 0x1990
+  __DATA.__data: 0x1988
   __DATA.__bss: 0x2ca0
   __DATA.__common: 0x10
   __DATA_DIRTY.__objc_data: 0x1570
-  __DATA_DIRTY.__data: 0x1490
-  __DATA_DIRTY.__bss: 0x22f0
+  __DATA_DIRTY.__data: 0x1480
+  __DATA_DIRTY.__bss: 0x2300
   __DATA_DIRTY.__common: 0x18
   - /System/Library/Frameworks/AppIntents.framework/AppIntents
   - /System/Library/Frameworks/Contacts.framework/Contacts

   - /System/Library/Frameworks/MessageUI.framework/MessageUI
   - /System/Library/Frameworks/QuartzCore.framework/QuartzCore
   - /System/Library/Frameworks/QuickLookThumbnailing.framework/QuickLookThumbnailing
+  - /System/Library/Frameworks/SwiftUI.framework/SwiftUI
   - /System/Library/Frameworks/UIKit.framework/UIKit
   - /System/Library/Frameworks/UniformTypeIdentifiers.framework/UniformTypeIdentifiers
   - /System/Library/PrivateFrameworks/Email.framework/Email

   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  Functions: 4629
-  Symbols:   6829
-  CStrings:  3781
+  Functions: 4637
+  Symbols:   6842
+  CStrings:  3786
 
Symbols:
+ +[MessageListFetchHelper log]
+ -[MessageListFetchHelper fetchMailboxesIsUserInitiated:].cold.1
+ -[MessageListFetchHelper fetchMailboxesIsUserInitiated:].cold.2
+ __OBJC_$_CLASS_METHODS_MessageListFetchHelper
+ __OBJC_$_CLASS_PROP_LIST_MessageListFetchHelper
+ __OBJC_CLASS_PROTOCOLS_$_MessageListFetchHelper
+ ___100-[MessageListSectionDataSource _addedItemIDs:before:existingItemID:toThreadWithItemID:inCollection:]_block_invoke.128
+ ___100-[MessageListSectionDataSource _addedItemIDs:before:existingItemID:toThreadWithItemID:inCollection:]_block_invoke_2.129
+ ___108-[MessageListSectionDataSource _deleteItemsWithIDs:fromCollection:useImmediateCompletion:completionHandler:]_block_invoke.134
+ ___108-[MessageListSectionDataSource _deleteItemsWithIDs:fromCollection:useImmediateCompletion:completionHandler:]_block_invoke_2.138
+ ___29+[MessageListFetchHelper log]_block_invoke
+ ___62-[MessageListSectionDataSource _maybeReloadForTimedOutItemIDs]_block_invoke.112
+ ___62-[MessageListSectionDataSource collection:movedItemIDs:after:]_block_invoke.94
+ ___63-[MessageListSectionDataSource collection:movedItemIDs:before:]_block_invoke.93
+ ___63-[MessageListSectionDataSource collectionDidFinishInitialLoad:]_block_invoke.101
+ ___63-[MessageListSectionDataSource didFinishRecoveryForCollection:]_block_invoke.96
+ ___80-[MessageListSectionDataSource collection:replacedExistingItemID:withNewItemID:]_block_invoke.95
+ ___80-[MessageListSectionDataSource collection:replacedExistingItemID:withNewItemID:]_block_invoke.95.cold.1
+ ___83-[MessageListSectionDataSource collection:didFinishInitialLoadForThreadWithItemID:]_block_invoke.100
+ ___87-[MessageListSectionDataSource messageListItemForItemID:indexPath:receiver:completion:]_block_invoke.76
+ ___87-[MessageListSectionDataSource messageListItemForItemID:indexPath:receiver:completion:]_block_invoke.79
+ ___96-[MessageListSectionDataSource _recoverFailedItemIDsIfNeededForCollection:excluding:completion:]_block_invoke.143
+ ___96-[MessageListSectionDataSource _recoverFailedItemIDsIfNeededForCollection:excluding:completion:]_block_invoke.143.cold.1
+ ___96-[MessageListSectionDataSource _recoverFailedItemIDsIfNeededForCollection:excluding:completion:]_block_invoke.147
- ___100-[MessageListSectionDataSource _addedItemIDs:before:existingItemID:toThreadWithItemID:inCollection:]_block_invoke.127
- ___100-[MessageListSectionDataSource _addedItemIDs:before:existingItemID:toThreadWithItemID:inCollection:]_block_invoke_2.128
- ___108-[MessageListSectionDataSource _deleteItemsWithIDs:fromCollection:useImmediateCompletion:completionHandler:]_block_invoke.133
- ___108-[MessageListSectionDataSource _deleteItemsWithIDs:fromCollection:useImmediateCompletion:completionHandler:]_block_invoke_2.137
- ___62-[MessageListSectionDataSource _maybeReloadForTimedOutItemIDs]_block_invoke.111
- ___62-[MessageListSectionDataSource collection:movedItemIDs:after:]_block_invoke.93
- ___63-[MessageListSectionDataSource collection:movedItemIDs:before:]_block_invoke.92
- ___63-[MessageListSectionDataSource collectionDidFinishInitialLoad:]_block_invoke.100
- ___63-[MessageListSectionDataSource didFinishRecoveryForCollection:]_block_invoke.95
- ___80-[MessageListSectionDataSource collection:replacedExistingItemID:withNewItemID:]_block_invoke.94
- ___80-[MessageListSectionDataSource collection:replacedExistingItemID:withNewItemID:]_block_invoke.94.cold.1
- ___83-[MessageListSectionDataSource collection:didFinishInitialLoadForThreadWithItemID:]_block_invoke.99
- ___87-[MessageListSectionDataSource messageListItemForItemID:indexPath:receiver:completion:]_block_invoke.75
- ___87-[MessageListSectionDataSource messageListItemForItemID:indexPath:receiver:completion:]_block_invoke.77
- ___96-[MessageListSectionDataSource _recoverFailedItemIDsIfNeededForCollection:excluding:completion:]_block_invoke.142
- ___96-[MessageListSectionDataSource _recoverFailedItemIDsIfNeededForCollection:excluding:completion:]_block_invoke.142.cold.1
- ___96-[MessageListSectionDataSource _recoverFailedItemIDsIfNeededForCollection:excluding:completion:]_block_invoke.146
CStrings:
+ "B24@0:8^@16"
+ "Fetching (%p). _mailboxesNeedFetching: %{BOOL}d, userInitiated: %{BOOL}d"
+ "No mailboxes."
+ "Not fetching. _mailboxesNeedFetching: %{BOOL}d, userInitiated: %{BOOL}d"
+ "verifyContentVisibility:"
- "Current Indexing status:: PercentIndexed:%f MessagesIndexed:%lu TotalMessages:%lu"

```
