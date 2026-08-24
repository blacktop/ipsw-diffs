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
-  __TEXT.__text: 0x8a690
-  __TEXT.__auth_stubs: 0x1380
-  __TEXT.__objc_stubs: 0x83c0
-  __TEXT.__objc_methlist: 0x3b6c
-  __TEXT.__cstring: 0x4d3e
-  __TEXT.__objc_methname: 0x861e
-  __TEXT.__objc_classname: 0x5af
-  __TEXT.__objc_methtype: 0x121b
-  __TEXT.__const: 0xced3
-  __TEXT.__gcc_except_tab: 0x1678
-  __TEXT.__oslogstring: 0xa3f1
-  __TEXT.__unwind_info: 0x1da8
-  __DATA_CONST.__const: 0xe788
-  __DATA_CONST.__cfstring: 0x4760
+274.1.1.0.0
+  __TEXT.__text: 0x8b1f4
+  __TEXT.__auth_stubs: 0x1370
+  __TEXT.__objc_stubs: 0x8500
+  __TEXT.__objc_methlist: 0x3c54
+  __TEXT.__cstring: 0x4eba
+  __TEXT.__objc_methname: 0x880a
+  __TEXT.__objc_classname: 0x5c6
+  __TEXT.__objc_methtype: 0x1237
+  __TEXT.__const: 0x11563
+  __TEXT.__gcc_except_tab: 0x161c
+  __TEXT.__oslogstring: 0xa477
+  __TEXT.__unwind_info: 0x1dd8
+  __DATA_CONST.__const: 0xec98
+  __DATA_CONST.__cfstring: 0x47e0
   __DATA_CONST.__objc_classlist: 0x168
   __DATA_CONST.__objc_catlist: 0x10
-  __DATA_CONST.__objc_protolist: 0xb0
+  __DATA_CONST.__objc_protolist: 0xb8
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_protorefs: 0x8
   __DATA_CONST.__objc_superrefs: 0xf8

   __DATA_CONST.__objc_arraydata: 0x408
   __DATA_CONST.__objc_arrayobj: 0x570
   __DATA_CONST.__objc_dictobj: 0x28
-  __DATA_CONST.__auth_got: 0x9d0
-  __DATA_CONST.__got: 0x538
+  __DATA_CONST.__auth_got: 0x9c8
+  __DATA_CONST.__got: 0x4f8
   __DATA_CONST.__auth_ptr: 0x28
-  __DATA.__objc_const: 0x8550
-  __DATA.__objc_selrefs: 0x24e8
-  __DATA.__objc_ivar: 0x408
+  __DATA.__objc_const: 0x8968
+  __DATA.__objc_selrefs: 0x2540
+  __DATA.__objc_ivar: 0x418
   __DATA.__objc_data: 0xe10
-  __DATA.__data: 0x29f0
+  __DATA.__data: 0x2a50
   __DATA.__bss: 0x130
   __DATA.__common: 0x28
   - /System/Library/Frameworks/CloudKit.framework/Versions/A/CloudKit

   - /usr/lib/libarchive.2.dylib
   - /usr/lib/libauthinstall.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 4090
-  Symbols:   473
-  CStrings:  3571
+  Functions: 4117
+  Symbols:   464
+  CStrings:  3596
 
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
