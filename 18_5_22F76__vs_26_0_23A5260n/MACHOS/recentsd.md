## recentsd

> `/System/Library/PrivateFrameworks/CoreRecents.framework/recentsd`

```diff

-1212.500.41.0.0
-  __TEXT.__text: 0x16f50
-  __TEXT.__auth_stubs: 0xcd0
-  __TEXT.__objc_stubs: 0x3dc0
-  __TEXT.__objc_methlist: 0x1374
+1222.100.4.0.0
+  __TEXT.__text: 0x17dfc
+  __TEXT.__auth_stubs: 0xd20
+  __TEXT.__objc_stubs: 0x3f60
+  __TEXT.__objc_methlist: 0x1414
   __TEXT.__const: 0x10c
-  __TEXT.__objc_methname: 0x3816
-  __TEXT.__cstring: 0x481a
-  __TEXT.__objc_classname: 0x2dc
-  __TEXT.__objc_methtype: 0xa2a
-  __TEXT.__gcc_except_tab: 0x2f4
-  __TEXT.__oslogstring: 0x1270
-  __TEXT.__unwind_info: 0x740
-  __DATA_CONST.__auth_got: 0x678
-  __DATA_CONST.__got: 0x350
-  __DATA_CONST.__const: 0xb78
-  __DATA_CONST.__cfstring: 0x1d60
-  __DATA_CONST.__objc_classlist: 0xd0
+  __TEXT.__objc_methname: 0x39af
+  __TEXT.__cstring: 0x4891
+  __TEXT.__objc_classname: 0x301
+  __TEXT.__objc_methtype: 0xaa7
+  __TEXT.__gcc_except_tab: 0x30c
+  __TEXT.__oslogstring: 0x1310
+  __TEXT.__unwind_info: 0x780
+  __DATA_CONST.__auth_got: 0x6a0
+  __DATA_CONST.__got: 0x378
+  __DATA_CONST.__const: 0xbe0
+  __DATA_CONST.__cfstring: 0x1da0
+  __DATA_CONST.__objc_classlist: 0xd8
   __DATA_CONST.__objc_catlist: 0x30
   __DATA_CONST.__objc_protolist: 0x48
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_protorefs: 0x8
-  __DATA_CONST.__objc_superrefs: 0xc8
+  __DATA_CONST.__objc_superrefs: 0xd0
   __DATA_CONST.__objc_intobj: 0x48
   __DATA_CONST.__objc_arraydata: 0x30
   __DATA_CONST.__objc_arrayobj: 0x30
-  __DATA.__objc_const: 0x22f8
-  __DATA.__objc_selrefs: 0x1160
-  __DATA.__objc_ivar: 0x180
-  __DATA.__objc_data: 0x820
+  __DATA.__objc_const: 0x23c0
+  __DATA.__objc_selrefs: 0x11d8
+  __DATA.__objc_ivar: 0x184
+  __DATA.__objc_data: 0x870
   __DATA.__data: 0x370
-  __DATA.__bss: 0x90
+  __DATA.__bss: 0xa0
   - /System/Library/Frameworks/Accounts.framework/Accounts
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/Foundation.framework/Foundation

   - /System/Library/PrivateFrameworks/AppSupport.framework/AppSupport
   - /System/Library/PrivateFrameworks/AppleAccount.framework/AppleAccount
   - /System/Library/PrivateFrameworks/ContactsFoundation.framework/ContactsFoundation
+  - /System/Library/PrivateFrameworks/CorePhoneNumbers.framework/CorePhoneNumbers
   - /System/Library/PrivateFrameworks/CoreRecents.framework/CoreRecents
   - /System/Library/PrivateFrameworks/EmailAddressing.framework/EmailAddressing
   - /System/Library/PrivateFrameworks/MailServices.framework/MailServices

   - /usr/lib/libicucore.A.dylib
   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libsqlite3.dylib
-  UUID: E795B0BB-A3FF-37BC-A890-916414F98C38
-  Functions: 552
-  Symbols:   326
-  CStrings:  1545
+  UUID: 7410BAB1-3293-34D0-B700-5D67EF8840A1
+  Functions: 568
+  Symbols:   336
+  CStrings:  1573
 
Symbols:
+ _CFNotificationCenterPostNotification
+ _CRAcceptedIntroductionsDidChangeNotification
+ _CRRecentsDomainAcceptedIntroductions
+ _OBJC_CLASS_$_CNCoalescingTimer
+ _OBJC_CLASS_$_CNPair
+ _OBJC_CLASS_$_CNSchedulerProvider
+ _objc_opt_new
+ _objc_retainBlock
+ _objc_retain_x3
+ _objc_retain_x5
CStrings:
+ "B52@0:8@16@24@32B40^@44"
+ "Did execute count recents for query %{public}@ (%{public}@) error: %@"
+ "Error removing records: %{public}@"
+ "SELECT COUNT(*)\n  FROM recents\n  JOIN contacts ON contacts.recent_id = recents.ROWID\n"
+ "T@\"NSDictionary\",&,N,V_cloudStores"
+ "Will count recents for query %{public}@ for %{public}@"
+ "_CRRecentsLibraryCloudStoresBuilder"
+ "_initializeCloudStores"
+ "_registerForRemoteKVSChanges"
+ "_startCoordinatingChanges"
+ "_storeDescriptions"
+ "addStoreForDomain:storeIdentifier:"
+ "backgroundScheduler"
+ "buildStores"
+ "com.apple.introductions.accepted"
+ "copyRecentContactsWithIDs:"
+ "countOfRecentsForQuery:error:"
+ "countRecentsUsingQuery:completion:"
+ "first"
+ "handleEvent"
+ "initWithDelay:options:block:schedulerProvider:downstreamScheduler:"
+ "pairWithFirst:second:"
+ "postNotificationIfNecessaryForUpdatedDomain:"
+ "q32@0:8@16^@24"
+ "recentContactsWithIDs:completion:"
+ "removeRecentContactsWithRecentIDs:syncKeys:domain:completion:"
+ "removeRecentContactsWithRecentIDs:syncKeys:domain:removeInUbiquitousStore:error:"
+ "second"
+ "v32@0:8@\"CRSearchQuery\"16@?<v@?q@\"NSError\">24"
+ "v48@0:8@\"NSArray\"16@\"NSArray\"24@\"NSString\"32@?<v@?@\"NSError\">40"
+ "v48@0:8@16@24@32@?40"
- "T@\"NSMutableDictionary\",&,N,V_cloudStores"
- "_initializeStoreForRecentsDomain:storeIdentifier:"
- "removeRecentContactsWithRecentIDs:syncKeys:domain:"
- "removeRecentContactsWithRecentIDs:syncKeys:domain:removeInUbiquitousStore:"
- "v40@0:8@\"NSArray\"16@\"NSArray\"24@\"NSString\"32"

```
