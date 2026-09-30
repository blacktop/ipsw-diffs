## AOSAccounts

> `/System/Library/PrivateFrameworks/AOSAccounts.framework/Versions/A/AOSAccounts`

```diff

-233.0.0.0.0
-  __TEXT.__text: 0x3bf34
-  __TEXT.__objc_methlist: 0xb94
+234.0.0.0.0
+  __TEXT.__text: 0x3c26c
+  __TEXT.__objc_methlist: 0xb9c
   __TEXT.__const: 0x31c
-  __TEXT.__cstring: 0xdce6
+  __TEXT.__cstring: 0xddee
   __TEXT.__oslogstring: 0x60
-  __TEXT.__gcc_except_tab: 0x4c90
-  __TEXT.__ustring: 0x446
-  __TEXT.__unwind_info: 0x1740
+  __TEXT.__gcc_except_tab: 0x4cac
+  __TEXT.__ustring: 0x4e8
+  __TEXT.__unwind_info: 0x1748
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0
   __TEXT.__objc_classname: 0x0

   __DATA_CONST.__objc_protolist: 0x48
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__weak_got: 0x8
-  __DATA_CONST.__objc_selrefs: 0xe00
+  __DATA_CONST.__objc_selrefs: 0xe18
   __DATA_CONST.__objc_protorefs: 0x18
   __DATA_CONST.__objc_superrefs: 0x28
   __DATA_CONST.__objc_arraydata: 0x50
   __DATA_CONST.__got: 0x678
   __AUTH_CONST.__const: 0x2518
-  __AUTH_CONST.__cfstring: 0x8c80
+  __AUTH_CONST.__cfstring: 0x8d20
   __AUTH_CONST.__objc_const: 0x12e8
   __AUTH_CONST.__weak_auth_got: 0x28
   __AUTH_CONST.__objc_arrayobj: 0x90

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libc++.1.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 1056
-  Symbols:   2805
-  CStrings:  1442
+  Functions: 1058
+  Symbols:   2812
+  CStrings:  1447
 
Symbols:
+ +[MMiCloudAccountsMigrator deleteMobileMeAccountsPlistIfNeeded]
+ _CFPreferencesCopyKeyList
+ _CFPreferencesSetValue
+ _CFPropertyListCreateDeepCopy
+ _MMServiceMerge
+ _dataClassListByAddingNeededDataClasses
+ _objc_msgSend$deleteMobileMeAccountsPlistIfNeeded
+ _objc_msgSend$fileExistsAtPath:
+ _objc_msgSend$removeItemAtPath:error:
- __Z14MMServiceMergeP9__CFArrayPK14__CFDictionary
- __Z38dataClassListByAddingNeededDataClassesPK9__CFArray
CStrings:
+ " [%s]  : No provider for account %@ service %@ — returning NULL for _kEnabledKey"
+ "Library/Preferences/MobileMeAccounts.plist"
+ "iCloudAccountMigrator: Deleted MobileMeAccounts.plist (rdar://148540841)"
+ "iCloudAccountMigrator: Failed to delete MobileMeAccounts.plist: %@"
+ "iCloudAccountMigrator: MobileMeAccounts.plist does not exist, nothing to delete."
```
