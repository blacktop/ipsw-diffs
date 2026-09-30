## SpotlightDaemon

> `/System/Library/PrivateFrameworks/SpotlightDaemon.framework/SpotlightDaemon`

```diff

-2465.1.2.0.0
-  __TEXT.__text: 0xc37d8
-  __TEXT.__objc_methlist: 0x4c6c
+2465.1.3.0.0
+  __TEXT.__text: 0xc3a00
+  __TEXT.__objc_methlist: 0x4c84
   __TEXT.__const: 0x410
-  __TEXT.__cstring: 0x9c05
+  __TEXT.__cstring: 0x9c86
   __TEXT.__gcc_except_tab: 0x48e4
-  __TEXT.__oslogstring: 0xd4c0
+  __TEXT.__oslogstring: 0xd4dc
   __TEXT.__dlopen_cstrs: 0x4a
   __TEXT.__unwind_info: 0x3508
   __TEXT.__objc_stubs: 0x0

   __DATA_CONST.__objc_protolist: 0x50
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__weak_got: 0x8
-  __DATA_CONST.__objc_selrefs: 0x3d68
+  __DATA_CONST.__objc_selrefs: 0x3d88
   __DATA_CONST.__objc_protorefs: 0x8
   __DATA_CONST.__objc_superrefs: 0x148
   __DATA_CONST.__objc_arraydata: 0x310
   __DATA_CONST.__got: 0xc10
   __AUTH_CONST.__const: 0x13a8
-  __AUTH_CONST.__cfstring: 0x81a0
+  __AUTH_CONST.__cfstring: 0x8200
   __AUTH_CONST.__objc_const: 0x63a8
   __AUTH_CONST.__weak_auth_got: 0x10
   __AUTH_CONST.__objc_arrayobj: 0x3a8

   __AUTH_CONST.__auth_got: 0x1130
   __AUTH.__objc_data: 0x230
   __DATA.__objc_ivar: 0x558
-  __DATA.__data: 0x418
+  __DATA.__data: 0x410
   __DATA.__common: 0x4
   __DATA_DIRTY.__objc_data: 0xfa0
-  __DATA_DIRTY.__data: 0x158
-  __DATA_DIRTY.__bss: 0x6d8
+  __DATA_DIRTY.__data: 0x160
+  __DATA_DIRTY.__bss: 0x738
   __DATA_DIRTY.__common: 0x18
   - /System/Library/Frameworks/Contacts.framework/Contacts
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation

   - /usr/lib/libc++.1.dylib
   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libutil.dylib
-  Functions: 3412
-  Symbols:   6830
-  CStrings:  2736
+  Functions: 3413
+  Symbols:   6835
+  CStrings:  2739
 
Symbols:
+ -[SPCoreSpotlightTask _knownDisabledBundleIDsFromBundleIDs:excludingFPBundleIDs:]
+ -[SPCoreSpotlightTask _makeNotificationSourcesQueryStringWithBundleIDs:]
+ -[SPCoreSpotlightTask _makePrefsQueryStringWithPrefsDisabledBundles:]
+ GCC_except_table79
+ GCC_except_table82
+ GCC_except_table88
+ GCC_except_table94
+ GCC_except_table98
+ _objc_msgSend$_knownDisabledBundleIDsFromBundleIDs:excludingFPBundleIDs:
+ _objc_msgSend$_makeNotificationSourcesQueryStringWithBundleIDs:
+ _objc_msgSend$_makePrefsQueryStringWithPrefsDisabledBundles:
+ _objc_msgSend$allDisabledBundlesSet
+ _objc_msgSend$federationDisabledBundles
- -[SPCoreSpotlightTask _makePrefsQueryStringWithBundleIDs:prefsDisabledBundles:]
- GCC_except_table77
- GCC_except_table78
- GCC_except_table86
- GCC_except_table89
- GCC_except_table90
- GCC_except_table96
- _objc_msgSend$_makePrefsQueryStringWithBundleIDs:prefsDisabledBundles:
CStrings:
+ " && _kMDItemBundleID!=\"com.apple.people.screenTimeRequest\" && _kMDItemBundleID!=\"com.apple.Preferences\""
+ "(!((%@) || (%@) || (%@) || (%@) || ((%@)%@)))"
+ "(_kMDItemBundleID = \"com.apple.usernotificationsd\" && %@)"
+ "(qid=%ld, bid=%s, context) Filtering out prefs disabled bundle %s"
+ "kMDItemCreator"
- "(!((%@) || (%@) || (%@) || ((%@) && _kMDItemBundleID!=\"com.apple.people.screenTimeRequest\")))"
- "Using disabledBundleIDs for (%ld, %s)"
```
