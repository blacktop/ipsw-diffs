## FinanceDaemon

> `/System/Library/PrivateFrameworks/FinanceDaemon.framework/FinanceDaemon`

```diff

-224.1.3.0.0
-  __TEXT.__text: 0x1c5e50
-  __TEXT.__auth_stubs: 0x5c40
+224.1.4.0.0
+  __TEXT.__text: 0x1d66f0
+  __TEXT.__auth_stubs: 0x5f80
   __TEXT.__objc_methlist: 0x334
-  __TEXT.__const: 0x6098
-  __TEXT.__cstring: 0x5d1f
-  __TEXT.__oslogstring: 0x6ca1
-  __TEXT.__constg_swiftt: 0x2d88
-  __TEXT.__swift5_typeref: 0x3a18
-  __TEXT.__swift5_builtin: 0xa0
-  __TEXT.__swift5_reflstr: 0x3723
-  __TEXT.__swift5_fieldmd: 0x2bf0
+  __TEXT.__const: 0x6288
+  __TEXT.__cstring: 0x5f2f
+  __TEXT.__oslogstring: 0x6e21
+  __TEXT.__constg_swiftt: 0x2ed0
+  __TEXT.__swift5_typeref: 0x3b06
+  __TEXT.__swift5_builtin: 0xb4
+  __TEXT.__swift5_reflstr: 0x38d3
+  __TEXT.__swift5_fieldmd: 0x2d9c
   __TEXT.__swift5_assocty: 0x6a8
-  __TEXT.__swift5_proto: 0x558
-  __TEXT.__swift5_types: 0x308
-  __TEXT.__swift5_capture: 0x137c
+  __TEXT.__swift5_proto: 0x564
+  __TEXT.__swift5_types: 0x328
+  __TEXT.__swift5_capture: 0x138c
   __TEXT.__swift5_protos: 0xa4
-  __TEXT.__swift5_mpenum: 0x20
-  __TEXT.__unwind_info: 0x5570
-  __TEXT.__eh_frame: 0xec74
+  __TEXT.__swift5_mpenum: 0x28
+  __TEXT.__unwind_info: 0x56e8
+  __TEXT.__eh_frame: 0xf10c
   __TEXT.__objc_classname: 0xf2
-  __TEXT.__objc_methname: 0x2bbf
+  __TEXT.__objc_methname: 0x2d14
   __TEXT.__objc_methtype: 0x5b6
   __TEXT.__objc_stubs: 0x120
-  __DATA_CONST.__got: 0x12f8
+  __DATA_CONST.__got: 0x1390
   __DATA_CONST.__const: 0x148
-  __DATA_CONST.__objc_classlist: 0x168
+  __DATA_CONST.__objc_classlist: 0x178
   __DATA_CONST.__objc_protolist: 0x80
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0xc70
+  __DATA_CONST.__objc_selrefs: 0xcf0
   __DATA_CONST.__objc_protorefs: 0x40
   __DATA_CONST.__objc_superrefs: 0x10
-  __AUTH_CONST.__auth_got: 0x2e28
-  __AUTH_CONST.__auth_ptr: 0x1240
-  __AUTH_CONST.__const: 0x5d58
-  __AUTH_CONST.__objc_const: 0x35d0
-  __AUTH.__objc_data: 0x308
-  __AUTH.__data: 0x3128
+  __AUTH_CONST.__auth_got: 0x2fc8
+  __AUTH_CONST.__auth_ptr: 0x1418
+  __AUTH_CONST.__const: 0x6030
+  __AUTH_CONST.__objc_const: 0x3778
+  __AUTH.__objc_data: 0x358
+  __AUTH.__data: 0x32e0
   __DATA.__objc_ivar: 0x8
-  __DATA.__data: 0x2eb0
-  __DATA.__bss: 0x8fc0
+  __DATA.__data: 0x2f30
+  __DATA.__bss: 0x9040
   __DATA.__common: 0x48
   __DATA_DIRTY.__objc_data: 0x398
-  __DATA_DIRTY.__data: 0x25f8
-  __DATA_DIRTY.__bss: 0xb00
-  __DATA_DIRTY.__common: 0x18
+  __DATA_DIRTY.__data: 0x26c8
+  __DATA_DIRTY.__bss: 0xc00
+  __DATA_DIRTY.__common: 0x30
   - /System/Library/Frameworks/Accounts.framework/Accounts
   - /System/Library/Frameworks/CoreData.framework/CoreData
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation

   - /usr/lib/swift/libswiftsimd.dylib
   - /usr/lib/swift/libswiftsys_time.dylib
   - /usr/lib/swift/libswiftunistd.dylib
-  Functions: 5719
-  Symbols:   513
-  CStrings:  1595
+  Functions: 5826
+  Symbols:   519
+  CStrings:  1635
 
Symbols:
+ _OBJC_CLASS_$_UNNotificationAttachment
+ _OBJC_CLASS_$_UNNotificationContent
+ _PKOrderManagementNotificationsDisabledKey
+ _OBJC_CLASS_$_NSLocale
+ _swift_updateClassMetadata2
CStrings:
+ "ORDER_NOTIFICATION_TITLE_OPEN"
+ "Created order messages with IDs: %!s(MISSING)"
+ "Notifications disabled for order tracking, ignoring"
+ "_TtC13FinanceDaemon33OrderImportAnalyticsEventsBuilder"
+ "productQuantitySpecified"
+ "Failed to remove Wallet messages for order %!s(MISSING) with error: %!@(MISSING)"
+ "setShowsAsActiveUntilDate:"
+ "InsertOrUpdateOrder"
+ "preferredLanguages"
+ "fulfillmentsChange"
+ "storeIdentifier"
+ "com.apple.finance.orders.outdated"
+ "setAttachments:"
+ "WELCOME_NOTIFICATION_TITLE"
+ "Notifications disabled for this order, ignoring"
+ "_hasBeenOnboardedToOrders"
+ "Existing order with orderTypeIdentifier=%!s(MISSING) and orderIdentifier=%!s(MISSING) is newer, cannot update"
+ "walletPreferences"
+ "setArchiveDate:"
+ "hasBeenOnboardedToOrders"
+ "_TtC13FinanceDaemon20ManagedOrderImporter"
+ "_notificationsDisabled"
+ "setOrderData:"
+ "setThreadIdentifier:"
+ "returnIdentifier"
+ "orderContentModificationDate"
+ "merchant"
+ "paymentStatusChange"
+ "Insert"
+ "displayName"
+ "orderBarcodeProvided"
+ "WELCOME_NOTIFICATION_BODY"
+ "effectiveNotificationsEnabled"
+ "Update"
+ "ORDER_NOTIFICATION_BODY_OPEN"
+ "Error creating notification icon: %!@(MISSING)"
+ "notSpecified"
+ "setAutomaticUpdatesEnabledUntilDate:"
+ "setCancellationDate:"
+ "creationDate"
+ "attachmentWithIdentifier:URL:options:error:"
+ "com.apple.finance.orders.imported.success"
- "Unknown scheduling behavior"
- "FinanceDaemon/OrderNotifications.swift"

```
