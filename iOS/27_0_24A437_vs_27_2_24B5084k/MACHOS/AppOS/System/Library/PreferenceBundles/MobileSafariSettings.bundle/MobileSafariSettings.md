## MobileSafariSettings

> `/System/Library/PreferenceBundles/MobileSafariSettings.bundle/MobileSafariSettings`

### Sections with Same Size but Changed Content

- `__TEXT.__const`
- `__TEXT.__gcc_except_tab`
- `__TEXT.__constg_swiftt`
- `__TEXT.__swift5_typeref`
- `__TEXT.__swift_as_entry`
- `__TEXT.__swift_as_ret`
- `__TEXT.__swift_as_cont`
- `__TEXT.__unwind_info`
- `__TEXT.__eh_frame`
- `__DATA_CONST.__const`
- `__DATA_CONST.__objc_classlist`
- `__DATA_CONST.__objc_catlist`
- `__DATA_CONST.__objc_protolist`
- `__DATA_CONST.__objc_protorefs`
- `__DATA_CONST.__objc_superrefs`
- `__DATA_CONST.__got`
- `__DATA_CONST.__auth_ptr`
- `__DATA.__objc_selrefs`
- `__DATA.__objc_data`
- `__DATA.__data`

```diff

-7625.1.29.10.29
-  __TEXT.__text: 0x6d564
+7625.2.4.1.0
+  __TEXT.__text: 0x6d558
   __TEXT.__auth_stubs: 0x1e40
-  __TEXT.__objc_stubs: 0xd060
-  __TEXT.__objc_methlist: 0x4644
-  __TEXT.__objc_methname: 0x11f5e
+  __TEXT.__objc_stubs: 0xd040
+  __TEXT.__objc_methlist: 0x464c
+  __TEXT.__objc_methname: 0x11f7e
   __TEXT.__objc_classname: 0x1244
   __TEXT.__cstring: 0x5e3b
   __TEXT.__objc_methtype: 0x26e1

   __DATA_CONST.__auth_got: 0xf38
   __DATA_CONST.__got: 0x1110
   __DATA_CONST.__auth_ptr: 0x3b8
-  __DATA.__objc_const: 0x7ad8
+  __DATA.__objc_const: 0x7ae0
   __DATA.__objc_selrefs: 0x42d8
   __DATA.__objc_ivar: 0x4d0
   __DATA.__objc_data: 0x1ef0

   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
   Functions: 1958
-  Symbols:   5577
+  Symbols:   5576
   CStrings:  3734
 
Symbols:
+ _OBJC_CLASS_$_WBSUsageRetentionDonationManager
+ _objc_msgSend$clearDonatedEventsSinceDate:
- _OBJC_CLASS_$_WBSTrialManager
- _objc_msgSend$isAllowFavoritesInFrequentlyVisitedEnabled
- _objc_msgSend$shared
Functions:
~ -[FrequentlyVisitedSitesController _canonicalizedFavoritesURLStringSet] : 416 -> 372
~ -[SafariSettingsController _safariClearHistoryAndDataAddedAfterDate:beforeDate:profileIdentifier:clearAllProfiles:closeTabs:] : 2896 -> 2928
CStrings:
+ "clearDonatedEventsSinceDate:"
+ "profileConnectionDidReceiveAllowCloudSyncChangedNotification:userInfo:"
- "isAllowFavoritesInFrequentlyVisitedEnabled"
- "shared"
```
