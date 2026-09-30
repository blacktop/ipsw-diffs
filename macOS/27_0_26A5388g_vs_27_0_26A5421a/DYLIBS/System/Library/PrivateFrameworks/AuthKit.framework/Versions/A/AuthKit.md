## AuthKit

> `/System/Library/PrivateFrameworks/AuthKit.framework/Versions/A/AuthKit`

```diff

-555.0.0.0.0
-  __TEXT.__text: 0x2c2798
-  __TEXT.__objc_methlist: 0x102ec
+559.0.0.0.0
+  __TEXT.__text: 0x2c25f4
+  __TEXT.__objc_methlist: 0x1032c
   __TEXT.__const: 0x3ac40
-  __TEXT.__cstring: 0x12997
-  __TEXT.__oslogstring: 0x1577c
-  __TEXT.__gcc_except_tab: 0x6630
+  __TEXT.__cstring: 0x129a0
+  __TEXT.__oslogstring: 0x1565d
+  __TEXT.__gcc_except_tab: 0x65d4
   __TEXT.__dlopen_cstrs: 0x250
   __TEXT.__ustring: 0x34a
-  __TEXT.__unwind_info: 0x4a28
+  __TEXT.__unwind_info: 0x4a20
   __TEXT.__eh_frame: 0xc0
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0
   __TEXT.__objc_classname: 0x0
   __TEXT.__objc_methname: 0x0
   __TEXT.__objc_methtype: 0x0
-  __DATA_CONST.__const: 0x5cf0
+  __DATA_CONST.__const: 0x5d00
   __DATA_CONST.__objc_classlist: 0x7b0
   __DATA_CONST.__objc_catlist: 0x88
   __DATA_CONST.__objc_protolist: 0x240
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x7ee8
+  __DATA_CONST.__objc_selrefs: 0x7f08
   __DATA_CONST.__objc_protorefs: 0xf0
   __DATA_CONST.__objc_superrefs: 0x4c8
   __DATA_CONST.__objc_arraydata: 0x368
   __DATA_CONST.__got: 0xa60
-  __AUTH_CONST.__const: 0xb710
+  __AUTH_CONST.__const: 0xb730
   __AUTH_CONST.__cfstring: 0x13c20
-  __AUTH_CONST.__objc_const: 0x2e0b0
+  __AUTH_CONST.__objc_const: 0x2e150
   __AUTH_CONST.__objc_intobj: 0x288
   __AUTH_CONST.__objc_dictobj: 0x438
   __AUTH_CONST.__objc_arrayobj: 0x90
-  __AUTH_CONST.__auth_got: 0x558
+  __AUTH_CONST.__auth_got: 0x568
   __AUTH.__objc_data: 0x3700
-  __DATA.__objc_ivar: 0x121c
+  __DATA.__objc_ivar: 0x1228
   __DATA.__data: 0x2098
   __DATA.__bss: 0x640
   __DATA.__common: 0xa20

   - /usr/lib/libMobileGestalt.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 6193
-  Symbols:   14575
-  CStrings:  4562
+  Functions: 6200
+  Symbols:   14588
+  CStrings:  4559
 
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
+ GCC_except_table104
+ GCC_except_table107
+ GCC_except_table113
+ GCC_except_table116
+ GCC_except_table120
+ GCC_except_table146
+ GCC_except_table157
+ GCC_except_table162
+ GCC_except_table170
+ GCC_except_table174
+ GCC_except_table177
+ GCC_except_table180
+ GCC_except_table183
+ GCC_except_table187
+ GCC_except_table194
+ GCC_except_table198
+ GCC_except_table202
+ GCC_except_table206
+ GCC_except_table211
+ GCC_except_table215
+ GCC_except_table244
+ GCC_except_table247
+ GCC_except_table253
+ GCC_except_table257
+ GCC_except_table296
+ OBJC_IVAR_$_AKAppleIDPasskeyAuthenticationController._silentCreateAuthorizationControllerProvider
+ OBJC_IVAR_$_AKRemoteDevice._isThisDevice
+ OBJC_IVAR_$_AKRemoteDevice._stableId
+ _AKDeviceCategoryListChangedNotification
+ _AKDeviceStableIdKey
+ _SecAccessControlCreateWithFlags
+ _SecKeyCreateRandomKey
+ ___87-[AKAppleIDPasskeyAuthenticationController silentCreateAuthorizationControllerProvider]_block_invoke
+ ___block_descriptor_32_e44_"ASAuthorizationController"16?0"NSArray"8l
+ _objc_msgSend$setProxyShouldIgnoreSilentRequestRequirements:
+ _objc_msgSend$silentCreateAuthorizationControllerProvider
- -[AKAccountManager setTrustedDeviceId:forAccount:]
- -[AKAccountManager trustedDeviceIdForAccount:]
- -[NSMutableURLRequest(AuthKit) ak_addTrustedDeviceIdHeader:]
- GCC_except_table105
- GCC_except_table108
- GCC_except_table117
- GCC_except_table147
- GCC_except_table152
- GCC_except_table167
- GCC_except_table171
- GCC_except_table175
- GCC_except_table178
- GCC_except_table184
- GCC_except_table188
- GCC_except_table192
- GCC_except_table195
- GCC_except_table203
- GCC_except_table212
- GCC_except_table241
- GCC_except_table248
- GCC_except_table254
- GCC_except_table258
- GCC_except_table297
- GCC_except_table393
- GCC_except_table394
- __AKHTTPHeaderTrustedDeviceId
- _kAKAnalyticsEventSigninTrustedDeviceId
- _kAKAnalyticsEventStableId
- _kAKAnalyticsEventUpgradeTrustedDeviceId
- _objc_msgSend$ak_addTrustedDeviceIdHeader:
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
