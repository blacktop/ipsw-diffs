## AuthKit

> `/System/Library/PrivateFrameworks/AuthKit.framework/AuthKit`

### Sections with Same Size but Changed Content

- `__DATA_CONST.__objc_classlist`
- `__DATA_CONST.__objc_catlist`
- `__DATA_CONST.__objc_protolist`
- `__DATA_CONST.__objc_protorefs`
- `__DATA_CONST.__objc_superrefs`
- `__DATA_CONST.__objc_arraydata`
- `__DATA_CONST.__got`
- `__AUTH_CONST.__cfstring`
- `__AUTH_CONST.__objc_intobj`
- `__AUTH_CONST.__objc_dictobj`
- `__AUTH_CONST.__objc_arrayobj`
- `__AUTH.__objc_data`
- `__DATA.__data`
- `__DATA_DIRTY.__objc_data`

```diff

-555.0.0.0.0
-  __TEXT.__text: 0x1a1d68
-  __TEXT.__objc_methlist: 0x10544
+559.0.0.0.0
+  __TEXT.__text: 0x1a1bac
+  __TEXT.__objc_methlist: 0x10584
   __TEXT.__const: 0xd30
-  __TEXT.__cstring: 0x12f8f
-  __TEXT.__oslogstring: 0x15c80
-  __TEXT.__gcc_except_tab: 0x6694
+  __TEXT.__cstring: 0x12f98
+  __TEXT.__oslogstring: 0x15b61
+  __TEXT.__gcc_except_tab: 0x6638
   __TEXT.__dlopen_cstrs: 0x267
   __TEXT.__ustring: 0x34a
-  __TEXT.__unwind_info: 0x4880
+  __TEXT.__unwind_info: 0x4878
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0
   __TEXT.__objc_classname: 0x0
   __TEXT.__objc_methname: 0x0
   __TEXT.__objc_methtype: 0x0
-  __DATA_CONST.__const: 0x78f8
+  __DATA_CONST.__const: 0x7908
   __DATA_CONST.__objc_classlist: 0x7d0
   __DATA_CONST.__objc_catlist: 0x88
   __DATA_CONST.__objc_protolist: 0x240
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x81a0
+  __DATA_CONST.__objc_selrefs: 0x81c0
   __DATA_CONST.__objc_protorefs: 0xf0
   __DATA_CONST.__objc_superrefs: 0x4c8
   __DATA_CONST.__objc_arraydata: 0x358
   __DATA_CONST.__got: 0xbc8
-  __AUTH_CONST.__const: 0x13e0
+  __AUTH_CONST.__const: 0x1400
   __AUTH_CONST.__cfstring: 0x13fc0
-  __AUTH_CONST.__objc_const: 0x2e820
+  __AUTH_CONST.__objc_const: 0x2e8c0
   __AUTH_CONST.__objc_intobj: 0x300
   __AUTH_CONST.__objc_dictobj: 0x410
   __AUTH_CONST.__objc_arrayobj: 0x90
-  __AUTH_CONST.__auth_got: 0x518
+  __AUTH_CONST.__auth_got: 0x528
   __AUTH.__objc_data: 0x3890
-  __DATA.__objc_ivar: 0x123c
+  __DATA.__objc_ivar: 0x1248
   __DATA.__data: 0x1bf0
   __DATA.__bss: 0x6d0
   __DATA_DIRTY.__objc_data: 0x1590

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libcompression.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 6105
-  Symbols:   14633
-  CStrings:  4636
+  Functions: 6112
+  Symbols:   14640
+  CStrings:  4633
 
Symbols:
+ +[AKSecurityHelper secAccessControlCreateWithProtection:flags:error:]
+ +[AKSecurityHelper secKeyCreateRandomKeyWithParameters:error:]
+ -[AKAppleIDPasskeyAuthenticationController setSilentCreateAuthorizationControllerProvider:]
+ -[AKAppleIDPasskeyAuthenticationController silentCreateAuthorizationControllerProvider]
+ -[AKRemoteDevice isThisDevice]
+ -[AKRemoteDevice setIsThisDevice:]
+ -[AKRemoteDevice setStableId:]
+ -[AKRemoteDevice stableId]
+ -[AKTrustedDeviceId stableId]
+ GCC_except_table102
+ GCC_except_table140
+ GCC_except_table146
+ GCC_except_table151
+ GCC_except_table163
+ GCC_except_table169
+ GCC_except_table172
+ GCC_except_table176
+ GCC_except_table180
+ GCC_except_table183
+ GCC_except_table191
+ GCC_except_table200
+ GCC_except_table210
+ GCC_except_table234
+ GCC_except_table240
+ GCC_except_table244
+ GCC_except_table283
+ _AKDeviceCategoryListChangedNotification
+ _AKDeviceStableIdKey
+ _OBJC_IVAR_$_AKAppleIDPasskeyAuthenticationController._silentCreateAuthorizationControllerProvider
+ _OBJC_IVAR_$_AKRemoteDevice._isThisDevice
+ _OBJC_IVAR_$_AKRemoteDevice._stableId
+ _SecAccessControlCreateWithFlags
+ _SecKeyCreateRandomKey
+ ___87-[AKAppleIDPasskeyAuthenticationController silentCreateAuthorizationControllerProvider]_block_invoke
+ ___block_descriptor_32_e44_"ASAuthorizationController"16?0"NSArray"8l
+ _objc_msgSend$setProxyShouldIgnoreSilentRequestRequirements:
+ _objc_msgSend$silentCreateAuthorizationControllerProvider
- -[AKAccountManager setTrustedDeviceId:forAccount:]
- -[AKAccountManager trustedDeviceIdForAccount:]
- -[NSMutableURLRequest(AuthKit) ak_addTrustedDeviceIdHeader:]
- GCC_except_table110
- GCC_except_table114
- GCC_except_table141
- GCC_except_table147
- GCC_except_table152
- GCC_except_table156
- GCC_except_table170
- GCC_except_table177
- GCC_except_table188
- GCC_except_table192
- GCC_except_table196
- GCC_except_table201
- GCC_except_table232
- GCC_except_table235
- GCC_except_table241
- GCC_except_table245
- GCC_except_table379
- GCC_except_table380
- GCC_except_table97
- __AKHTTPHeaderTrustedDeviceId
- _kAKAnalyticsEventSigninTrustedDeviceId
- _kAKAnalyticsEventStableId
- _kAKAnalyticsEventUpgradeTrustedDeviceId
- _objc_msgSend$ak_addTrustedDeviceIdHeader:
- _objc_msgSend$setTrustedDeviceId:forAccount:
- _objc_msgSend$trustedDeviceIdForAccount:
- _objc_msgSend$trustedDeviceIdentifierForAccount:
CStrings:
+ "<%@:%p> Name: %@, SN: %@, SDID: %@, TrustedDeviceId: %@, Build: %@, OS: %@, Version: %@, Model: %@, Timestamp: %@, Trusted: %d, Safety State' %@, Circle Status: %d, Color Code: %@, Additional Info %@, services: %@, lastCacheUpdatedDate: %@, deletedDate: %@, removalReason: %ld, stableId: %@, isThisDevice: %d "
+ "@\"ASAuthorizationController\"16@?0@\"NSArray\"8"
+ "Basic server request reply received: %@"
+ "Dispatching basic server request to daemon with urlBagKey: %{public}@"
+ "Error: Got nil GS token data!"
+ "Fetch auth mode reply received: %@"
+ "OS_ELIGIBILITY_CONTEXT_ACCOUNT_AREA_ID"
+ "_isThisDevice"
+ "_stableId"
+ "com.apple.authkit.device-list-category-changed"
+ "sdid"
- "<%@:%p> Name: %@, SN: %@, SDID: %@, TrustedDeviceId: %@, Build: %@, OS: %@, Version: %@, Model: %@, Timestamp: %@, Trusted: %d, Safety State' %@, Circle Status: %d, Color Code: %@, Additional Info %@, services: %@, lastCacheUpdatedDate: %@, deletedDate: %@, removalReason: %ld "
- "Calling out to remote auth service to performBasicServerRequest with urlBagKey: %{public}@"
- "Error: We do not have a UI-capabable context on the client side!"
- "Exception caught while getting trusted device id: %@"
- "Exception caught while setting trusted device id: %@"
- "Found a mismatch in TDID for SDID. "
- "OS_ELIGIBILITY_CONTEXT_AREA_ID"
- "Result of remote call: %lu. Error: %{public}@"
- "X-Apple-I-Trusted-Device-Id"
- "com.apple.authkit.StableIDAvailability"
- "com.apple.authkit.TDIDAvailability.signin"
- "com.apple.authkit.TDIDAvailability.upgrade"
- "performBasicServerRequest completed with response: %{public}@"
- "performBasicServerRequest failed with error: %{public}@"
```
