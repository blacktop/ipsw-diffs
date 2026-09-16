## iCloudQuotaUI

> `/System/Library/PrivateFrameworks/iCloudQuotaUI.framework/iCloudQuotaUI`

```diff

-301.24.0.27.0
-  __TEXT.__text: 0x15cc30
-  __TEXT.__objc_methlist: 0x9d94
-  __TEXT.__const: 0xac34
-  __TEXT.__gcc_except_tab: 0xeb8
-  __TEXT.__cstring: 0xae26
-  __TEXT.__oslogstring: 0xba92
+301.24.1.3.0
+  __TEXT.__text: 0x15d0bc
+  __TEXT.__objc_methlist: 0x9e64
+  __TEXT.__const: 0xac24
+  __TEXT.__gcc_except_tab: 0xe7c
+  __TEXT.__cstring: 0xae56
+  __TEXT.__oslogstring: 0xbba2
   __TEXT.__dlopen_cstrs: 0x691
   __TEXT.__swift5_typeref: 0x9eec
   __TEXT.__swift5_reflstr: 0x1af0

   __TEXT.__swift_as_cont: 0x180
   __TEXT.__swift5_builtin: 0x50
   __TEXT.__swift5_mpenum: 0x8
-  __TEXT.__unwind_info: 0x6ee8
+  __TEXT.__unwind_info: 0x6f00
   __TEXT.__eh_frame: 0x3598
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0
   __TEXT.__objc_classname: 0x0
   __TEXT.__objc_methname: 0x0
   __TEXT.__objc_methtype: 0x0
-  __DATA_CONST.__const: 0x2718
-  __DATA_CONST.__objc_classlist: 0x588
+  __DATA_CONST.__const: 0x2738
+  __DATA_CONST.__objc_classlist: 0x590
   __DATA_CONST.__objc_catlist: 0x88
   __DATA_CONST.__objc_protolist: 0x278
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x6b40
+  __DATA_CONST.__objc_selrefs: 0x6bc8
   __DATA_CONST.__objc_protorefs: 0x80
   __DATA_CONST.__objc_superrefs: 0x360
   __DATA_CONST.__objc_arraydata: 0x578
-  __DATA_CONST.__got: 0x1d18
+  __DATA_CONST.__got: 0x1d20
   __AUTH_CONST.__const: 0x6b60
-  __AUTH_CONST.__cfstring: 0x7f20
-  __AUTH_CONST.__objc_const: 0x21f70
+  __AUTH_CONST.__cfstring: 0x7fe0
+  __AUTH_CONST.__objc_const: 0x22090
   __AUTH_CONST.__objc_arrayobj: 0x120
   __AUTH_CONST.__objc_intobj: 0x198
   __AUTH_CONST.__objc_dictobj: 0x488
   __AUTH_CONST.__objc_doubleobj: 0x20
-  __AUTH_CONST.__auth_got: 0x2358
-  __AUTH.__objc_data: 0x39e8
+  __AUTH_CONST.__auth_got: 0x2368
+  __AUTH.__objc_data: 0x3a38
   __AUTH.__data: 0x25d8
-  __DATA.__objc_ivar: 0xbd8
+  __DATA.__objc_ivar: 0xbe4
   __DATA.__data: 0x4168
   __DATA.__common: 0x2a8
   __DATA_DIRTY.__objc_data: 0x478

   - /usr/lib/swift/libswift_StringProcessing.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  Functions: 8036
-  Symbols:   10878
-  CStrings:  2567
+  Functions: 8052
+  Symbols:   10921
+  CStrings:  2575
 
Symbols:
+ +[ICQUIOrientation supportedOrientations:isEnhancedLandscapeEnabled:]
+ +[ICQUIOrientation supportedOrientations]
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
+ GCC_except_table26
+ GCC_except_table44
+ GCC_except_table54
+ GCC_except_table58
+ GCC_except_table66
+ _ICQInAppActionIdentifierCancel
+ _ICQInAppActionIdentifierMoveToOnMyDevice
+ _ICQUIInAppMessageReasonRecoveryFailed
+ _ICQUIMessagePlacementInAppAlert
+ _OBJC_CLASS_$_ICQUIOrientation
+ _OBJC_IVAR_$_ICQInAppAction._actionIdentifier
+ _OBJC_IVAR_$_ICQInAppMessaging._mockOffer
+ _OBJC_IVAR_$_ICQLinkInAppAction._pendingItemsCount
+ _OBJC_METACLASS_$_ICQUIOrientation
+ __OBJC_$_CLASS_METHODS_ICQUIOrientation
+ __OBJC_CLASS_RO_$_ICQUIOrientation
+ __OBJC_METACLASS_RO_$_ICQUIOrientation
+ __UIEnhancedLandscapeEnabled
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
+ _objc_msgSend$setAllowsNonnumericFormatting:
+ _objc_msgSend$setCountStyle:
+ _objc_msgSend$setMockOffer:
+ _objc_msgSend$sharedAlbumMessageForOffer:placement:pendingItemsCount:
+ _objc_msgSend$stringFromByteCount:
+ _objc_msgSend$supportedOrientations
+ _objc_msgSend$supportedOrientations:isEnhancedLandscapeEnabled:
+ _os_variant_has_internal_diagnostics
- -[ICQLinkInAppAction addAlertFromLink:offer:]
- GCC_except_table49
- GCC_except_table59
- GCC_except_table60
- ___60-[ICQInternetPrivacyDetailSpecifierProvider _switchOffAlert]_block_invoke_3
- ___76-[ICQInAppMessaging _fetchSharedAlbumMessageForReason:placement:completion:]_block_invoke
- _objc_msgSend$addAlertFromLink:offer:
- _objc_msgSend$gigabytes
- _objc_msgSend$initWithOffer:alertKey:
- _objc_msgSend$sharedAlbumMessageForOffer:placement:
- _objc_msgSend$stringFromNumber:
- _objc_msgSend$stringFromUnit:
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
