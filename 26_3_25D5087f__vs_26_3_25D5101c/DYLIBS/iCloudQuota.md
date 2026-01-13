## iCloudQuota

> `/System/Library/PrivateFrameworks/iCloudQuota.framework/Versions/A/iCloudQuota`

```diff

-301.23.2.2.0
-  __TEXT.__text: 0x75744
+301.23.3.2.0
+  __TEXT.__text: 0x757bc
   __TEXT.__auth_stubs: 0x1400
-  __TEXT.__objc_methlist: 0x5074
+  __TEXT.__objc_methlist: 0x5084
   __TEXT.__const: 0x1288
   __TEXT.__cstring: 0x4f60
   __TEXT.__gcc_except_tab: 0x664
-  __TEXT.__oslogstring: 0x6dde
+  __TEXT.__oslogstring: 0x6e1e
   __TEXT.__dlopen_cstrs: 0x235
   __TEXT.__ustring: 0x4
   __TEXT.__swift5_typeref: 0x712

   __TEXT.__objc_classname: 0x8b8
   __TEXT.__objc_methname: 0xbd13
   __TEXT.__objc_methtype: 0xe12
-  __TEXT.__objc_stubs: 0x7f00
+  __TEXT.__objc_stubs: 0x7ee0
   __DATA_CONST.__got: 0x6d0
   __DATA_CONST.__const: 0x930
   __DATA_CONST.__objc_classlist: 0x320

   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  UUID: 8E1A0CF6-9D79-3FE3-8601-F7DB9F62C0CA
-  Functions: 2736
-  Symbols:   5272
-  CStrings:  4499
+  UUID: 9568EEEE-BBE8-3802-84B8-63DC402BF930
+  Functions: 2738
+  Symbols:   5273
+  CStrings:  4500
 
Symbols:
+ +[ICQDaemonDefaultOffer clearPersistedObject]
+ +[ICQDaemonDefaultOffer clearPersistedObject].cold.1
- _objc_msgSend$_teardownCachedDefaultOfferAndNotify:
Functions:
~ -[ICQDaemonOfferManager _teardownCachedOffersAndNotify:] : 388 -> 376
~ -[ICQDaemonOfferManager _coalescedReconsiderOffersForAccount:isForBuddy:quotaReason:options:choiceHandler:completion:] : 1348 -> 1336
+ +[ICQDaemonDefaultOffer clearPersistedObject]
+ +[ICQDaemonDefaultOffer clearPersistedObject].cold.1
CStrings:
+ "Attempted to clear default offer - this should not happen!"

```
