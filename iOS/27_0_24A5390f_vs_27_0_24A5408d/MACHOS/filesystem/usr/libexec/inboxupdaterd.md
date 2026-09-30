## inboxupdaterd

> `/usr/libexec/inboxupdaterd`

### Sections with Same Size but Changed Content

- `__DATA_CONST.__objc_classlist`
- `__DATA_CONST.__objc_catlist`
- `__DATA_CONST.__objc_protorefs`
- `__DATA_CONST.__objc_superrefs`
- `__DATA_CONST.__objc_intobj`
- `__DATA_CONST.__objc_arraydata`
- `__DATA_CONST.__objc_arrayobj`
- `__DATA_CONST.__objc_dictobj`
- `__DATA_CONST.__auth_ptr`
- `__DATA.__objc_data`

```diff

-274.0.9.0.0
-  __TEXT.__text: 0x8c1f8
-  __TEXT.__auth_stubs: 0x1530
-  __TEXT.__objc_stubs: 0x8860
-  __TEXT.__objc_methlist: 0x409c
-  __TEXT.__cstring: 0x5394
-  __TEXT.__objc_methname: 0x8ed6
-  __TEXT.__objc_classname: 0x670
-  __TEXT.__objc_methtype: 0x1779
-  __TEXT.__const: 0xcee3
-  __TEXT.__gcc_except_tab: 0x17d4
-  __TEXT.__oslogstring: 0xa7fc
+274.2.1.0.0
+  __TEXT.__text: 0x8cd98
+  __TEXT.__auth_stubs: 0x1520
+  __TEXT.__objc_stubs: 0x89a0
+  __TEXT.__objc_methlist: 0x4184
+  __TEXT.__cstring: 0x5510
+  __TEXT.__objc_methname: 0x90c2
+  __TEXT.__objc_classname: 0x687
+  __TEXT.__objc_methtype: 0x1795
+  __TEXT.__const: 0x11573
+  __TEXT.__gcc_except_tab: 0x1778
+  __TEXT.__oslogstring: 0xa882
   __TEXT.__dlopen_cstrs: 0x5a
-  __TEXT.__unwind_info: 0x1f68
-  __DATA_CONST.__const: 0xedc0
-  __DATA_CONST.__cfstring: 0x4c40
+  __TEXT.__unwind_info: 0x1f98
+  __DATA_CONST.__const: 0xf2d0
+  __DATA_CONST.__cfstring: 0x4cc0
   __DATA_CONST.__objc_classlist: 0x180
   __DATA_CONST.__objc_catlist: 0x10
-  __DATA_CONST.__objc_protolist: 0xd0
+  __DATA_CONST.__objc_protolist: 0xd8
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_protorefs: 0x8
   __DATA_CONST.__objc_superrefs: 0x110

   __DATA_CONST.__objc_arraydata: 0x4d8
   __DATA_CONST.__objc_arrayobj: 0x600
   __DATA_CONST.__objc_dictobj: 0x28
-  __DATA_CONST.__auth_got: 0xaa8
-  __DATA_CONST.__got: 0x5d8
+  __DATA_CONST.__auth_got: 0xaa0
+  __DATA_CONST.__got: 0x598
   __DATA_CONST.__auth_ptr: 0x28
-  __DATA.__objc_const: 0x9610
-  __DATA.__objc_selrefs: 0x2708
-  __DATA.__objc_ivar: 0x444
+  __DATA.__objc_const: 0x9a28
+  __DATA.__objc_selrefs: 0x2760
+  __DATA.__objc_ivar: 0x454
   __DATA.__objc_data: 0xf00
-  __DATA.__data: 0x2568
+  __DATA.__data: 0x25c8
   __DATA.__bss: 0x140
   __DATA.__common: 0x28
   - /System/Library/Frameworks/CloudKit.framework/CloudKit

   - /usr/lib/libarchive.2.dylib
   - /usr/lib/libauthinstall.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 4243
-  Symbols:   519
-  CStrings:  3741
+  Functions: 4272
+  Symbols:   510
+  CStrings:  3766
 
Symbols:
- _SecItemDelete
- _kMAOptionsBAAIgnoreExistingKeychainItems
- _kMAOptionsBAAKeychainAccessGroup
- _kMAOptionsBAAKeychainLabel
- _kSecAttrAccessGroup
- _kSecAttrLabel
- _kSecClass
- _kSecClassCertificate
- _kSecClassKey
CStrings:
+ "&A"
+ "@\"<MIBUWiFiHelperDelegate>\""
+ "BAA credential fetch failed after %lu attempt(s)"
+ "BAA credentials obtained on attempt %lu"
+ "BAA fetch aborted before attempt %lu: reporter invalidated"
+ "Dropping status report: reporter invalidated"
+ "Failed to create SecAccessControl on attempt %lu: %{public}@"
+ "Failed to generate BAA nonce on attempt %lu; aborting"
+ "Failed to obtain BAA certificates: %{public}@"
+ "MIBUWiFiHelperDelegate"
+ "Network dropped after going online; arming network-loss watchdog"
+ "Network lost for more than %d seconds after going online"
+ "Network restored; cancelling network-loss watchdog"
+ "Personalization network-loss watchdog timer fired!"
+ "Requesting BAA certs (attempt %lu/%lu)"
+ "Starting personalization network-loss watchdog timer with %ds timeout..."
+ "Stopping personalization network-loss watchdog timer..."
+ "Stopping status POST retries: reporter invalidated"
+ "T@\"<MIBUWiFiHelperDelegate>\",W,N,V_delegate"
+ "T@\"PCPersistentTimer\",&,N,V_networkLossWatchdogTimer"
+ "TB,N,V_lastNetworkAvailable"
+ "_fireWatchdogTimeoutWithError:"
+ "_invalidated"
+ "_isInvalidated"
+ "_lastNetworkAvailable"
+ "_networkLossWatchdogTimer"
+ "_startNetworkLossWatchdogTimer"
+ "_stopAllWatchdogTimers"
+ "_stopNetworkLossWatchdogTimer"
+ "com.apple.mobileinboxupdater.personalizationnetworkwatchdog"
+ "handleNetworkLossWatchdogTimer:"
+ "https://product-personalization-coreos.ext.pos.apple.com"
+ "lastNetworkAvailable"
+ "networkConnectivityDidDrop"
+ "networkConnectivityDidRestore"
+ "networkLossWatchdogTimer"
+ "setLastNetworkAvailable:"
+ "setNetworkLossWatchdogTimer:"
+ "wifiHelperDidLoseNetwork"
+ "wifiHelperDidRegainNetwork"
- "BAA cert request finished"
- "BAA credential fetch timed out after %d seconds"
- "Failed to create SecAccessControl: %{public}@"
- "Failed to delete BAA %{public}@ from keychain: %d"
- "Failed to fetch. err: %@"
- "Failed to generate BAA nonce; aborting credential fetch"
- "Failed to obtain BAA certificates: %@"
- "Requesting BAA certs"
- "_deleteBAAKeychainItems"
- "certificate"
- "dictionaryWithDictionary:"
- "https://production-personalization-coreos.ext.pos.apple.com"
- "inboxupdaterd"
- "initWithArray:"
- "key"
```
