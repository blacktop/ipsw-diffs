## iCloudQuotaUI

> `/System/Library/PrivateFrameworks/iCloudQuotaUI.framework/Versions/A/iCloudQuotaUI`

```diff

-301.24.0.27.0
-  __TEXT.__text: 0x9c92c
-  __TEXT.__objc_methlist: 0x1eac
+301.24.1.3.0
+  __TEXT.__text: 0x9d108
+  __TEXT.__objc_methlist: 0x1f5c
   __TEXT.__const: 0x7464
-  __TEXT.__gcc_except_tab: 0x648
-  __TEXT.__cstring: 0x4daa
-  __TEXT.__oslogstring: 0x365b
+  __TEXT.__gcc_except_tab: 0x610
+  __TEXT.__cstring: 0x4dda
+  __TEXT.__oslogstring: 0x376b
   __TEXT.__dlopen_cstrs: 0x218
   __TEXT.__swift5_typeref: 0x74d6
   __TEXT.__swift5_reflstr: 0x14e2

   __TEXT.__swift_as_ret: 0x78
   __TEXT.__swift5_builtin: 0x3c
   __TEXT.__swift_as_cont: 0x3c
-  __TEXT.__unwind_info: 0x33c8
+  __TEXT.__unwind_info: 0x33d8
   __TEXT.__eh_frame: 0x1298
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0
   __TEXT.__objc_classname: 0x0
   __TEXT.__objc_methname: 0x0
   __TEXT.__objc_methtype: 0x0
-  __DATA_CONST.__const: 0x518
+  __DATA_CONST.__const: 0x538
   __DATA_CONST.__objc_classlist: 0x120
   __DATA_CONST.__objc_catlist: 0x18
   __DATA_CONST.__objc_protolist: 0x60
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x1ca0
+  __DATA_CONST.__objc_selrefs: 0x1d18
   __DATA_CONST.__objc_protorefs: 0x10
   __DATA_CONST.__objc_superrefs: 0x60
   __DATA_CONST.__objc_arraydata: 0x478
-  __DATA_CONST.__got: 0xa98
+  __DATA_CONST.__got: 0xaa0
   __AUTH_CONST.__const: 0x4b30
-  __AUTH_CONST.__cfstring: 0x3280
-  __AUTH_CONST.__objc_const: 0x4f08
+  __AUTH_CONST.__cfstring: 0x3340
+  __AUTH_CONST.__objc_const: 0x4f98
   __AUTH_CONST.__objc_intobj: 0x48
   __AUTH_CONST.__objc_dictobj: 0x398
   __AUTH_CONST.__objc_arrayobj: 0xf0
-  __AUTH_CONST.__auth_got: 0x13d8
+  __AUTH_CONST.__auth_got: 0x13e0
   __AUTH.__objc_data: 0x988
   __AUTH.__data: 0x1960
-  __DATA.__objc_ivar: 0x1ec
+  __DATA.__objc_ivar: 0x1f8
   __DATA.__data: 0x2100
   __DATA.__common: 0x258
   __DATA_DIRTY.__objc_data: 0x3d8

   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  Functions: 3749
-  Symbols:   3338
-  CStrings:  915
+  Functions: 3764
+  Symbols:   3371
+  CStrings:  923
 
Symbols:
+ -[ICQInAppAction actionIdentifier]
+ -[ICQInAppAction setActionIdentifier:]
+ -[ICQInAppAlert initWithOffer:alertKey:pendingItemsCount:]
+ -[ICQInAppMessaging _actionsForBannerSpecification:offer:pendingItemsCount:]
+ -[ICQInAppMessaging _fetchSharedAlbumMessageForReason:placement:pendingItemsCount:completion:]
+ -[ICQInAppMessaging fetchAlertForReason:placement:completion:]
+ -[ICQInAppMessaging fetchMessageForReason:placement:pendingItemsCount:withCompletion:]
+ -[ICQInAppMessaging fetchMessageWithPlacement:pendingItemsCount:completion:]
+ -[ICQInAppMessaging mockOffer]
+ -[ICQInAppMessaging setMockOffer:]
+ -[ICQInAppMessaging sharedAlbumMessageForOffer:placement:pendingItemsCount:]
+ -[ICQLinkInAppAction addAlertFromLink:offer:pendingItemsCount:]
+ -[ICQLinkInAppAction initWithLink:inOffer:pendingItemsCount:]
+ -[ICQLinkInAppAction pendingItemsCount]
+ -[ICQLinkInAppAction setPendingItemsCount:]
+ GCC_except_table48
+ GCC_except_table49
+ GCC_except_table57
+ GCC_except_table58
+ GCC_except_table68
+ GCC_except_table82
+ OBJC_IVAR_$_ICQInAppAction._actionIdentifier
+ OBJC_IVAR_$_ICQInAppMessaging._mockOffer
+ OBJC_IVAR_$_ICQLinkInAppAction._pendingItemsCount
+ _ICQActionParameterServerLinkIdentifierKey
+ _ICQInAppActionIdentifierCancel
+ _ICQInAppActionIdentifierMoveToOnMyDevice
+ _ICQUIInAppMessageReasonRecoveryFailed
+ _ICQUIMessagePlacementInAppAlert
+ __94-[ICQInAppMessaging _fetchSharedAlbumMessageForReason:placement:pendingItemsCount:completion:]_block_invoke
+ ___68-[ICQInAppMessaging observeValueForKeyPath:ofObject:change:context:]_block_invoke
+ ___94-[ICQInAppMessaging _fetchSharedAlbumMessageForReason:placement:pendingItemsCount:completion:]_block_invoke
+ _objc_msgSend$_actionsForBannerSpecification:offer:pendingItemsCount:
+ _objc_msgSend$_fetchSharedAlbumMessageForReason:placement:pendingItemsCount:completion:
+ _objc_msgSend$actionIdentifier
+ _objc_msgSend$addAlertFromLink:offer:pendingItemsCount:
+ _objc_msgSend$initWithLink:inOffer:pendingItemsCount:
+ _objc_msgSend$initWithOffer:alertKey:pendingItemsCount:
+ _objc_msgSend$mockOffer
+ _objc_msgSend$normalizedPendingItemsCount:
+ _objc_msgSend$pendingItemsCount
+ _objc_msgSend$setActionIdentifier:
+ _objc_msgSend$setMockOffer:
+ _objc_msgSend$sharedAlbumMessageForOffer:placement:pendingItemsCount:
+ _os_variant_has_internal_diagnostics
- -[ICQLinkInAppAction addAlertFromLink:offer:]
- GCC_except_table31
- GCC_except_table45
- GCC_except_table46
- GCC_except_table52
- GCC_except_table63
- GCC_except_table76
- __76-[ICQInAppMessaging _fetchSharedAlbumMessageForReason:placement:completion:]_block_invoke
- ___76-[ICQInAppMessaging _fetchSharedAlbumMessageForReason:placement:completion:]_block_invoke
- _objc_msgSend$addAlertFromLink:offer:
- _objc_msgSend$initWithOffer:alertKey:
- _objc_msgSend$sharedAlbumMessageForOffer:placement:
CStrings:
+ "InAppAlert"
+ "RecoveryFailed"
+ "Shared Collections: fetchMessageForReason:placement:pendingItemsCount: called with reason: %@, placement: %@, count: %@"
+ "cancelBtnId"
+ "debug-mock-offer"
+ "fetchAlertForReason:%{public}@ placement:%{public}@ not yet implemented, returning unavailable error."
+ "fetchMessageForReason:placement: called with reason: %@, placement: %@"
+ "fetchMessageWithPlacement called with placement: %@"
+ "fetchMessageWithPlacement:pendingItemsCount: called with placement: %@, count: %@"
+ "moveToOnMyDeviceBtnId"
+ "pendingItemsCount"
- "INTERNET_PRIVACY_OPEN_SYSTEM_STATUS_BUTTON_TITLE"
- "Shared Collections: fetchMessageForReason:placement: called with reason: %@, placement: %@"
- "Shared Collections: fetchMessageWithPlacement called with placement: %@"
```
