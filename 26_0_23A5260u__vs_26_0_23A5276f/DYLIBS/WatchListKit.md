## WatchListKit

> `/System/Library/PrivateFrameworks/WatchListKit.framework/WatchListKit`

```diff

-902.0.0.0.0
-  __TEXT.__text: 0x66b50
+903.0.0.0.0
+  __TEXT.__text: 0x67168
   __TEXT.__auth_stubs: 0x810
-  __TEXT.__objc_methlist: 0x6fc4
+  __TEXT.__objc_methlist: 0x6ffc
   __TEXT.__const: 0x1a4
-  __TEXT.__cstring: 0x7a5d
+  __TEXT.__cstring: 0x7b4d
   __TEXT.__oslogstring: 0x6327
   __TEXT.__gcc_except_tab: 0x11b0
-  __TEXT.__unwind_info: 0x1dd8
+  __TEXT.__unwind_info: 0x1de8
   __TEXT.__objc_classname: 0x1321
-  __TEXT.__objc_methname: 0x105c2
+  __TEXT.__objc_methname: 0x10699
   __TEXT.__objc_methtype: 0x1da5
-  __TEXT.__objc_stubs: 0x9c60
+  __TEXT.__objc_stubs: 0x9d20
   __DATA_CONST.__got: 0x8f8
-  __DATA_CONST.__const: 0x2760
+  __DATA_CONST.__const: 0x2778
   __DATA_CONST.__objc_classlist: 0x560
   __DATA_CONST.__objc_catlist: 0x50
   __DATA_CONST.__objc_protolist: 0x98
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x38d0
+  __DATA_CONST.__objc_selrefs: 0x3918
   __DATA_CONST.__objc_protorefs: 0x20
   __DATA_CONST.__objc_superrefs: 0x4b0
   __DATA_CONST.__objc_arraydata: 0x628
   __AUTH_CONST.__auth_got: 0x418
   __AUTH_CONST.__const: 0xe80
-  __AUTH_CONST.__cfstring: 0xa340
+  __AUTH_CONST.__cfstring: 0xa3e0
   __AUTH_CONST.__objc_const: 0x11b00
   __AUTH_CONST.__objc_intobj: 0x378
   __AUTH_CONST.__objc_dictobj: 0x190

   - /usr/lib/libMobileGestalt.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: C8C50F1C-5148-3C41-A02C-31882972814D
-  Functions: 2742
-  Symbols:   10053
-  CStrings:  6427
+  UUID: 9E79EEE4-195E-35EC-B711-47ECD69B654E
+  Functions: 2747
+  Symbols:   10072
+  CStrings:  6446
 
Symbols:
+ +[WLKBadgingUtilities _createRequestContainer:]
+ +[WLKBadgingUtilities _returnListofBadgingActionMetrics]
+ +[WLKBadgingUtilities processStoredODJBadgingRequestActions]
+ +[WLKBadgingUtilities removeBadgeRequest:]
+ +[WLKBadgingUtilities storeBadgeRequest:]
+ _WLKNotificationActionMetricsDefaultsKey
+ _WLKNotificationBadgeIdentifierDefaultsKey
+ _WLKNotificationListOfODJBadges
+ _objc_msgSend$_createRequestContainer:
+ _objc_msgSend$_returnListofBadgingActionMetrics
+ _objc_msgSend$actionMetricsEvent
+ _objc_msgSend$badgeIdentifier
+ _objc_msgSend$enqueueEvent:
+ _objc_msgSend$initWithUnderlyingDictionary:
- ___block_literal_global.9
CStrings:
+ "WLKBadgingUtilities::removed badge request action metrics for id: %@"
+ "WLKBadgingUtilities::stored badge request action metrics for id: %@"
+ "WLKBadgingUtilities::submitted action metrics for badge identifier: %@"
+ "_createRequestContainer:"
+ "_returnListofBadgingActionMetrics"
+ "actionMetricsEvent"
+ "badgeIdentifier"
+ "enqueueEvent:"
+ "initWithUnderlyingDictionary:"
+ "listOfODJBadges"
+ "processStoredODJBadgingRequestActions"
+ "removeBadgeRequest:"
+ "storeBadgeRequest:"

```
