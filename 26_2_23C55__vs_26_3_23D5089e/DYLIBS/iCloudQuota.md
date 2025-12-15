## iCloudQuota

> `/System/Library/PrivateFrameworks/iCloudQuota.framework/iCloudQuota`

```diff

-301.23.2.2.0
-  __TEXT.__text: 0x78554
+301.23.3.1.0
+  __TEXT.__text: 0x785c4
   __TEXT.__auth_stubs: 0x1680
-  __TEXT.__objc_methlist: 0x580c
+  __TEXT.__objc_methlist: 0x581c
   __TEXT.__const: 0x1288
   __TEXT.__cstring: 0x6771
-  __TEXT.__oslogstring: 0x80e9
+  __TEXT.__oslogstring: 0x8129
   __TEXT.__gcc_except_tab: 0x6b8
   __TEXT.__dlopen_cstrs: 0x2f1
   __TEXT.__ustring: 0x152

   __TEXT.__objc_classname: 0xa79
   __TEXT.__objc_methname: 0xd560
   __TEXT.__objc_methtype: 0xfd7
-  __TEXT.__objc_stubs: 0x8fc0
+  __TEXT.__objc_stubs: 0x8fa0
   __DATA_CONST.__got: 0x7e8
   __DATA_CONST.__const: 0x1d00
   __DATA_CONST.__objc_classlist: 0x388

   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  UUID: 1B7BEF32-E30A-3A51-A607-582B251EE7B2
-  Functions: 2896
-  Symbols:   8046
-  CStrings:  5178
+  UUID: 7D199097-18FF-3120-8AA9-556F655AA3FE
+  Functions: 2898
+  Symbols:   8049
+  CStrings:  5179
 
Symbols:
+ +[ICQDaemonDefaultOffer clearPersistedObject]
+ +[ICQDaemonDefaultOffer clearPersistedObject].cold.1
- _objc_msgSend$_teardownCachedDefaultOfferAndNotify:
Functions:
+ +[ICQDaemonDefaultOffer clearPersistedObject]
~ -[ICQDaemonOfferManager _teardownCachedOffersAndNotify:] : 372 -> 360
~ -[ICQDaemonOfferManager _coalescedReconsiderOffersForAccount:isForBuddy:quotaReason:options:choiceHandler:completion:] : 1224 -> 1212
+ +[ICQDaemonDefaultOffer clearPersistedObject].cold.1
CStrings:
+ "Attempted to clear default offer - this should not happen!"

```
