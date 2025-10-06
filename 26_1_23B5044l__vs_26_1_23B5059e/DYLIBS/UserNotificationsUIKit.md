## UserNotificationsUIKit

> `/System/Library/PrivateFrameworks/UserNotificationsUIKit.framework/UserNotificationsUIKit`

```diff

-1003.1.11.0.0
-  __TEXT.__text: 0x1a6028
-  __TEXT.__auth_stubs: 0x28a0
-  __TEXT.__objc_methlist: 0x19f74
+1003.1.15.0.0
+  __TEXT.__text: 0x1a685c
+  __TEXT.__auth_stubs: 0x28b0
+  __TEXT.__objc_methlist: 0x1a06c
   __TEXT.__const: 0x3c04
   __TEXT.__gcc_except_tab: 0x2e10
-  __TEXT.__cstring: 0xd346
-  __TEXT.__oslogstring: 0xd67d
+  __TEXT.__cstring: 0xd376
+  __TEXT.__oslogstring: 0xd6ad
   __TEXT.__ustring: 0x22
   __TEXT.__swift5_typeref: 0x3b88
   __TEXT.__swift5_fieldmd: 0x1234

   __TEXT.__swift_as_entry: 0x2c
   __TEXT.__swift_as_ret: 0x1c
   __TEXT.__swift5_mpenum: 0x5c
-  __TEXT.__unwind_info: 0x7038
+  __TEXT.__unwind_info: 0x7060
   __TEXT.__eh_frame: 0xcb8
   __TEXT.__objc_classname: 0x3694
-  __TEXT.__objc_methname: 0x44926
+  __TEXT.__objc_methname: 0x449c4
   __TEXT.__objc_methtype: 0xbd12
-  __TEXT.__objc_stubs: 0x27580
+  __TEXT.__objc_stubs: 0x27600
   __DATA_CONST.__got: 0x17a0
-  __DATA_CONST.__const: 0x40e0
+  __DATA_CONST.__const: 0x40d0
   __DATA_CONST.__objc_classlist: 0x7b0
   __DATA_CONST.__objc_catlist: 0xc0
   __DATA_CONST.__objc_protolist: 0x5f0
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0xc550
+  __DATA_CONST.__objc_selrefs: 0xc570
   __DATA_CONST.__objc_protorefs: 0xc8
   __DATA_CONST.__objc_superrefs: 0x530
   __DATA_CONST.__objc_arraydata: 0x158
-  __AUTH_CONST.__auth_got: 0x1460
+  __AUTH_CONST.__auth_got: 0x1468
   __AUTH_CONST.__const: 0x5a58
   __AUTH_CONST.__cfstring: 0x7d40
-  __AUTH_CONST.__objc_const: 0x25340
+  __AUTH_CONST.__objc_const: 0x25418
   __AUTH_CONST.__objc_intobj: 0x330
   __AUTH_CONST.__objc_arrayobj: 0x150
   __AUTH_CONST.__objc_dictobj: 0x28
   __AUTH_CONST.__objc_doubleobj: 0x20
-  __AUTH.__objc_data: 0x2878
-  __AUTH.__data: 0x4f8
+  __AUTH.__objc_data: 0x2800
+  __AUTH.__data: 0x4d0
   __DATA.__objc_ivar: 0x1644
-  __DATA.__data: 0x5110
+  __DATA.__data: 0x5100
   __DATA.__objc_stublist: 0x8
-  __DATA.__bss: 0x1ab0
+  __DATA.__bss: 0x1910
   __DATA.__common: 0x60
-  __DATA_DIRTY.__objc_data: 0x34b0
-  __DATA_DIRTY.__data: 0x1548
-  __DATA_DIRTY.__bss: 0x12b0
+  __DATA_DIRTY.__objc_data: 0x3528
+  __DATA_DIRTY.__data: 0x15a0
+  __DATA_DIRTY.__bss: 0x1440
   __DATA_DIRTY.__common: 0x58
   - /System/Library/Frameworks/Charts.framework/Charts
   - /System/Library/Frameworks/Combine.framework/Combine

   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  UUID: E7CF304E-6446-3B2D-80CA-3E8FBBFEF37C
-  Functions: 10660
-  Symbols:   27933
-  CStrings:  13513
+  UUID: EC8D5067-E9E2-3D3C-9A42-F614DE91A9A0
+  Functions: 10683
+  Symbols:   27970
+  CStrings:  13520
 
Symbols:
+ -[NCNotificationListCell setSupportsMitosis:]
+ -[NCNotificationListCell supportsMitosis]
+ -[NCNotificationListSupplementaryHostingView setSupportsMitosis:]
+ -[NCNotificationListSupplementaryHostingView supportsMitosis]
+ -[NCNotificationListSupplementaryHostingViewController setSupportsMitosis:]
+ -[NCNotificationListSupplementaryHostingViewController supportsMitosis]
+ -[NCNotificationLongLookView setSupportsMitosis:]
+ -[NCNotificationLongLookView supportsMitosis]
+ -[NCNotificationRootList visibleRectBottomMarginForRollUnder]
+ -[NCNotificationShortLookView setSupportsMitosis:]
+ -[NCNotificationShortLookView supportsMitosis]
+ -[NCNotificationStructuredListViewController notificationRootListRequestsDiagnosticsDictionary:]
+ -[NCNotificationSummaryPlatterContainingView setSupportsMitosis:]
+ -[NCNotificationSummaryPlatterContainingView supportsMitosis]
+ -[NCNotificationViewController setSupportsMitosis:]
+ -[NCNotificationViewController supportsMitosis]
+ GCC_except_table114
+ GCC_except_table122
+ GCC_except_table184
+ GCC_except_table196
+ GCC_except_table202
+ GCC_except_table295
+ GCC_except_table84
+ GCC_except_table91
+ ___103-[NCNotificationRootList _migrateNonActiveHighlightNotificationRequestsFromHighlightToIncomingSection:]_block_invoke.198
+ ___103-[NCNotificationRootList _migrateNonActiveHighlightNotificationRequestsFromHighlightToIncomingSection:]_block_invoke_2.199
+ ___137-[NCNotificationRootList _migrateOnScheduleNotificationRequests:fromSection:toSection:clearRequests:filterForDestination:animateRemoval:]_block_invoke.203
+ ___137-[NCNotificationRootList _migrateOnScheduleNotificationRequests:fromSection:toSection:clearRequests:filterForDestination:animateRemoval:]_block_invoke_2.204
+ ___43-[NCNotificationRootList _digestTestRecipe]_block_invoke.310
+ ___66-[NCNotificationRootList _notificationMigrationOverrideTestRecipe]_block_invoke.317
+ ___84-[NCNotificationRootList _elevateGroupInOtherSectionsIfNeededWithRequest:toSection:]_block_invoke.205
+ ___block_literal_global.1112
+ ___block_literal_global.126
+ ___block_literal_global.143
+ ___block_literal_global.145
+ ___block_literal_global.184
+ ___block_literal_global.192
+ ___block_literal_global.194
+ _block_copy_helper.17
+ _block_copy_helper.23
+ _block_copy_helper.30
+ _block_copy_helper.39
+ _block_descriptor.19
+ _block_descriptor.25
+ _block_descriptor.32
+ _block_descriptor.41
+ _block_destroy_helper.18
+ _block_destroy_helper.24
+ _block_destroy_helper.31
+ _block_destroy_helper.40
+ _keypath_get_selector_supportsMitosis
+ _objc_msgSend$notificationRootListRequestsDiagnosticsDictionary:
+ _objc_msgSend$notificationStructuredListViewControllerRequestsDiagnosticsDictionary:
+ _objc_msgSend$setSupportsMitosis:
+ _objc_msgSend$supportsMitosis
- GCC_except_table104
- GCC_except_table195
- GCC_except_table201
- GCC_except_table294
- GCC_except_table40
- GCC_except_table83
- GCC_except_table88
- GCC_except_table93
- ___103-[NCNotificationRootList _migrateNonActiveHighlightNotificationRequestsFromHighlightToIncomingSection:]_block_invoke.194
- ___103-[NCNotificationRootList _migrateNonActiveHighlightNotificationRequestsFromHighlightToIncomingSection:]_block_invoke_2.198
- ___137-[NCNotificationRootList _migrateOnScheduleNotificationRequests:fromSection:toSection:clearRequests:filterForDestination:animateRemoval:]_block_invoke.199
- ___137-[NCNotificationRootList _migrateOnScheduleNotificationRequests:fromSection:toSection:clearRequests:filterForDestination:animateRemoval:]_block_invoke_2.203
- ___43-[NCNotificationRootList _digestTestRecipe]_block_invoke.309
- ___66-[NCNotificationRootList _notificationMigrationOverrideTestRecipe]_block_invoke.316
- ___84-[NCNotificationRootList _elevateGroupInOtherSectionsIfNeededWithRequest:toSection:]_block_invoke.204
- ___block_descriptor_33_e5_v8?0l
- ___block_literal_global.1108
- ___block_literal_global.142
- ___block_literal_global.144
- ___block_literal_global.183
- ___block_literal_global.191
- ___block_literal_global.193
- _block_copy_helper.15
- _block_descriptor.17
- _block_destroy_helper.16
CStrings:
+ "TB,N,VsupportsMitosis"
+ "notificationRootListRequestsDiagnosticsDictionary:"
+ "notificationStructuredListViewControllerRequestsDiagnosticsDictionary:"
+ "setSupportsMitosis:"
+ "supportsMitosis"
+ "visibleRectBottomMargin updated, layoutForRootListSizeChange"

```
