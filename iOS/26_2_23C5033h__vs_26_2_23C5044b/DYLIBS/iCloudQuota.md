## iCloudQuota

> `/System/Library/PrivateFrameworks/iCloudQuota.framework/iCloudQuota`

```diff

-301.23.2.1.0
-  __TEXT.__text: 0x784e4
+301.23.2.2.0
+  __TEXT.__text: 0x78554
   __TEXT.__auth_stubs: 0x1680
   __TEXT.__objc_methlist: 0x580c
   __TEXT.__const: 0x1288
   __TEXT.__cstring: 0x6771
-  __TEXT.__oslogstring: 0x8029
+  __TEXT.__oslogstring: 0x80e9
   __TEXT.__gcc_except_tab: 0x6b8
   __TEXT.__dlopen_cstrs: 0x2f1
   __TEXT.__ustring: 0x152

   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  UUID: 69D075DA-D5B7-3E44-8248-863C6FC92D3E
-  Functions: 2895
-  Symbols:   8044
-  CStrings:  5176
+  UUID: 1B7BEF32-E30A-3A51-A607-582B251EE7B2
+  Functions: 2896
+  Symbols:   8046
+  CStrings:  5178
 
Symbols:
+ GCC_except_table109
+ GCC_except_table114
+ GCC_except_table94
+ ___84-[ICQDaemonOfferManager _persistAndNotifyMissingPlaceholdersForRequestType:account:]_block_invoke_2
- GCC_except_table108
- GCC_except_table113
- GCC_except_table93
Functions:
~ -[ICQDaemonOfferManager _persistAndNotifyMissingPlaceholdersForRequestType:account:] : 540 -> 656
+ ___84-[ICQDaemonOfferManager _persistAndNotifyMissingPlaceholdersForRequestType:account:]_block_invoke_2
~ +[ICQDaemonOfferConditions backupRestoreComplete] : 24 -> 8
CStrings:
+ "Event daemon offer / alerts / followups were torn down but will be replaced; not notifying clients until then"
+ "Event daemon offer / followups were torn down without replacement; notifying clients"

```
