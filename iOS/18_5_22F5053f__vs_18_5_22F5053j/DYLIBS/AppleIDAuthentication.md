## AppleIDAuthentication

> `/System/Library/Accounts/Authentication/AppleIDAuthentication.bundle/AppleIDAuthentication`

```diff

-1007.475.0.0.0
-  __TEXT.__text: 0xb140
+1007.476.0.0.0
+  __TEXT.__text: 0xb004
   __TEXT.__auth_stubs: 0x550
-  __TEXT.__objc_methlist: 0x444
+  __TEXT.__objc_methlist: 0x434
   __TEXT.__const: 0x88
-  __TEXT.__oslogstring: 0x287a
+  __TEXT.__oslogstring: 0x283b
   __TEXT.__cstring: 0x74b
   __TEXT.__gcc_except_tab: 0x1d0
   __TEXT.__dlopen_cstrs: 0x5a
   __TEXT.__unwind_info: 0x220
   __TEXT.__objc_classname: 0x96
-  __TEXT.__objc_methname: 0x1a2a
+  __TEXT.__objc_methname: 0x19eb
   __TEXT.__objc_methtype: 0x5e1
-  __TEXT.__objc_stubs: 0x1860
-  __DATA_CONST.__got: 0x2e0
+  __TEXT.__objc_stubs: 0x1800
+  __DATA_CONST.__got: 0x2d0
   __DATA_CONST.__const: 0x6b0
   __DATA_CONST.__objc_classlist: 0x18
   __DATA_CONST.__objc_protolist: 0x18
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x750
+  __DATA_CONST.__objc_selrefs: 0x738
   __DATA_CONST.__objc_superrefs: 0x8
   __DATA_CONST.__objc_arraydata: 0x80
   __AUTH_CONST.__auth_got: 0x2b8

   - /System/Library/Frameworks/Foundation.framework/Foundation
   - /System/Library/Frameworks/MobileCoreServices.framework/MobileCoreServices
   - /System/Library/Frameworks/Security.framework/Security
+  - /System/Library/PrivateFrameworks/AAAFoundation.framework/AAAFoundation
   - /System/Library/PrivateFrameworks/AccountsDaemon.framework/AccountsDaemon
   - /System/Library/PrivateFrameworks/AppSupport.framework/AppSupport
   - /System/Library/PrivateFrameworks/AppleAccount.framework/AppleAccount

   - /usr/lib/libMobileGestalt.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 118
-  Symbols:   189
-  CStrings:  507
+  Functions: 117
+  Symbols:   187
+  CStrings:  503
 
Symbols:
+ _OBJC_CLASS_$_AAFollowUpUtilities
- _AAFollowUpUserInfoClientName
- _AAFollowUpUserInfoProxiedDeviceData
- _OBJC_CLASS_$_NSMutableDictionary
CStrings:
+ "followUpPostAnalyticsInfoWithContext:identifier:error:"
+ "setAnalyticsInfo:"
- "Adding proxied device identifier to renew follow up user info."
- "_userInfoForRenewCredentialsFollowUpWithAccountStore:proxiedDevice:"
- "adamOrDisplayID"
- "copy"
- "initWithCapacity:"
- "setObject:forKeyedSubscript:"

```
