## Accounts

> `/System/Library/Frameworks/Accounts.framework/Accounts`

```diff

-995.1.0.0.0
-  __TEXT.__text: 0x57fe4
-  __TEXT.__auth_stubs: 0xc90
-  __TEXT.__objc_methlist: 0x39a4
+999.4.0.0.0
+  __TEXT.__text: 0x590e0
+  __TEXT.__auth_stubs: 0xc80
+  __TEXT.__objc_methlist: 0x3fc4
   __TEXT.__const: 0xc8
-  __TEXT.__gcc_except_tab: 0x3e10
-  __TEXT.__cstring: 0x3ad8
-  __TEXT.__oslogstring: 0x5352
-  __TEXT.__unwind_info: 0x18b0
+  __TEXT.__gcc_except_tab: 0x3dc4
+  __TEXT.__cstring: 0x3b24
+  __TEXT.__oslogstring: 0x539a
+  __TEXT.__unwind_info: 0x1970
   __TEXT.__objc_classname: 0x549
-  __TEXT.__objc_methname: 0x812a
+  __TEXT.__objc_methname: 0x8195
   __TEXT.__objc_methtype: 0x1543
-  __TEXT.__objc_stubs: 0x5d60
+  __TEXT.__objc_stubs: 0x5da0
   __DATA_CONST.__got: 0x348
-  __DATA_CONST.__const: 0x2500
+  __DATA_CONST.__const: 0x2510
   __DATA_CONST.__objc_classlist: 0x190
   __DATA_CONST.__objc_catlist: 0x28
   __DATA_CONST.__objc_protolist: 0x60
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x1fe8
+  __DATA_CONST.__objc_selrefs: 0x2088
   __DATA_CONST.__objc_protorefs: 0x20
   __DATA_CONST.__objc_superrefs: 0x128
   __DATA_CONST.__objc_arraydata: 0x38
-  __AUTH_CONST.__auth_got: 0x658
+  __AUTH_CONST.__auth_got: 0x650
   __AUTH_CONST.__auth_ptr: 0x8
   __AUTH_CONST.__const: 0x420
-  __AUTH_CONST.__cfstring: 0x46c0
-  __AUTH_CONST.__objc_const: 0x6460
+  __AUTH_CONST.__cfstring: 0x4720
+  __AUTH_CONST.__objc_const: 0x58e8
   __AUTH_CONST.__objc_arrayobj: 0x60
   __AUTH_CONST.__objc_intobj: 0xd8
   __AUTH.__objc_data: 0x960
-  __DATA.__objc_ivar: 0x384
+  __DATA.__objc_ivar: 0x388
   __DATA.__data: 0x4d0
   __DATA.__bss: 0xf8
   __DATA_DIRTY.__objc_data: 0x640

   - /System/Library/PrivateFrameworks/UserManagement.framework/UserManagement
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 1814
-  Symbols:   2678
-  CStrings:  2758
+  Functions: 1885
+  Symbols:   2758
+  CStrings:  2766
 
Symbols:
+ _ACAccountTypeIdentifierDCA
+ _kACDDetachedCAFullAccessEntitlement
- _fmod
CStrings:
+ "\"ACMonitoredAccountStore UIApplicationDidBecomeActiveNotification received, refreshing\""
+ "\"ACMonitoredAccountStore: Failed to fetch accounts: %@\""
+ "\"ACMonitoredAccountStore: Fetched Accounts\""
+ "\"ACMonitoredAccountStore: Fetching accounts of account type %@...\""
+ "UIApplicationDidBecomeActiveNotification"
+ "_lock_accountWasAdded:"
+ "_lock_accountWasModified:"
+ "_lock_accountWasRemoved:"
+ "_lock_processAccountsListForNotifications:forType:"
+ "_monitoredAccountsCacheLock"
+ "com.apple.account.DCA"
+ "com.apple.account.dca.fullaccess"
+ "com.apple.gs.idms.pet"
- "\"ACMonitoredAccountStore: Attempting to reconnect to accountsd...\""
- "\"ACMonitoredAccountStore: Failed to reconnect to accountsd: %@\""
- "\"ACMonitoredAccountStore: Reconnected to accountsd\""
- "UIApplicationWillResignActiveNotification"
- "_processAccountsListForNotifications:forType:"

```
