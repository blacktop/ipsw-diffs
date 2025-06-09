## nehelper

> `/usr/libexec/nehelper`

```diff

-2063.120.19.0.0
-  __TEXT.__text: 0x24cb0
-  __TEXT.__auth_stubs: 0x1140
-  __TEXT.__objc_stubs: 0x2860
-  __TEXT.__objc_methlist: 0x43c
-  __TEXT.__const: 0x10c
-  __TEXT.__gcc_except_tab: 0x9b8
-  __TEXT.__objc_methname: 0x1eac
-  __TEXT.__oslogstring: 0x4876
-  __TEXT.__cstring: 0x5c42
+2167.0.0.0.2
+  __TEXT.__text: 0x25644
+  __TEXT.__auth_stubs: 0x1130
+  __TEXT.__objc_stubs: 0x2920
+  __TEXT.__objc_methlist: 0x44c
+  __TEXT.__const: 0x11c
+  __TEXT.__gcc_except_tab: 0x9a4
+  __TEXT.__objc_methname: 0x1f3c
+  __TEXT.__oslogstring: 0x4a57
+  __TEXT.__cstring: 0x5cde
   __TEXT.__objc_classname: 0x1a5
   __TEXT.__objc_methtype: 0x261
-  __TEXT.__unwind_info: 0x410
-  __DATA_CONST.__auth_got: 0x8b0
-  __DATA_CONST.__got: 0x3a0
+  __TEXT.__unwind_info: 0x428
+  __DATA_CONST.__auth_got: 0x8a8
+  __DATA_CONST.__got: 0x390
   __DATA_CONST.__auth_ptr: 0x8
-  __DATA_CONST.__const: 0xc78
-  __DATA_CONST.__cfstring: 0x5000
+  __DATA_CONST.__const: 0xc98
+  __DATA_CONST.__cfstring: 0x5060
   __DATA_CONST.__objc_classlist: 0x80
   __DATA_CONST.__objc_protolist: 0x10
   __DATA_CONST.__objc_imageinfo: 0x8

   __DATA_CONST.__objc_arraydata: 0x1310
   __DATA_CONST.__objc_arrayobj: 0x30
   __DATA_CONST.__objc_dictobj: 0x50
-  __DATA.__objc_const: 0x1788
-  __DATA.__objc_selrefs: 0xab8
-  __DATA.__objc_ivar: 0xdc
+  __DATA.__objc_const: 0x17c8
+  __DATA.__objc_selrefs: 0xae8
+  __DATA.__objc_ivar: 0xe4
   __DATA.__objc_data: 0x500
   __DATA.__data: 0xc8
-  __DATA.__bss: 0x288
+  __DATA.__bss: 0x298
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/CoreLocation.framework/CoreLocation
   - /System/Library/Frameworks/CoreServices.framework/CoreServices

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libbsm.0.dylib
   - /usr/lib/libicucore.A.dylib
-  - /usr/lib/libnetwork.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: AACD319C-B261-363F-834A-1FF8D2EB1522
-  Functions: 241
-  Symbols:   391
-  CStrings:  2306
+  UUID: 951DB6D9-21A9-3A9A-87AD-9209DDCE6865
+  Functions: 246
+  Symbols:   388
+  CStrings:  2332
 
Symbols:
- _SecIdentityCreate
- _kSecClassIdentity
- _kSecClassKey
CStrings:
+ "%@ Unable to generate identity reference"
+ "%@ [%@] is not entitled to remove app push provider configuration"
+ "%@ [%@] is not entitled to remove hotspot provider configuration"
+ "%@ [%@] is not entitled to save app push provider configuration"
+ "%@ [%@] is not entitled to save hotspot provider configuration"
+ "19.0"
+ "9"
+ "APP_AUTHEN_HEADER_URL_FILTER"
+ "APP_WARNING_HEADER_URL_FILTER"
+ "APP_WARNING_URL_FILTER"
+ "LegacyAPI"
+ "URL filter"
+ "[%@] is denied Wi-Fi information access since it's linked with iOS SDK 19.0 or later. Use replacement API [NEHotspotNetwork fetchCurrentWithCompletionHandler:]"
+ "_isLegacyAPICaller"
+ "_netExtensionEntitlement"
+ "app [%@] does not own the configured evaluated SSIDs"
+ "app tracker queue"
+ "appBundleIdentifier"
+ "controlProviderBundleIdentifier"
+ "copySecIdentityRef"
+ "evaluatedSSIDs"
+ "failed to find Wi-Fi networks owned by app [%@]"
+ "hotspot"
+ "isEqualToSet:"
+ "isSubsetOfSet:"
+ "returning raw socket for domain: %d, protocol: %d"
+ "setWithArray:"
+ "socket(%d, SOCK_RAW, %d) failed: %d"
+ "socket-domain"
+ "socket-protocol"
+ "urlFilter"
- "%@ SecItemCopyMatching for cert failed %d"
- "%@ SecItemCopyMatching for identity failed %d"
- "%@ SecItemCopyMatching for key failed %d"
- ")"
- "Failed to create identity reference"
- "identity"
- "isModernSystem"
- "keyPersistentReference"

```
