## AMSAccountSyncNotificationPlugin

> `/System/Library/Accounts/Notification/AMSAccountSyncNotificationPlugin.bundle/AMSAccountSyncNotificationPlugin`

```diff

-7.3.4.0.0
-  __TEXT.__text: 0x2b64
-  __TEXT.__auth_stubs: 0x360
+7.4.38.2.4
+  __TEXT.__text: 0x2770
+  __TEXT.__auth_stubs: 0x300
   __TEXT.__objc_methlist: 0x17c
-  __TEXT.__const: 0x68
-  __TEXT.__cstring: 0x2b9
-  __TEXT.__gcc_except_tab: 0x24
-  __TEXT.__oslogstring: 0x76c
-  __TEXT.__dlopen_cstrs: 0x56
-  __TEXT.__unwind_info: 0xe0
-  __TEXT.__objc_classname: 0x89
-  __TEXT.__objc_methname: 0xafc
+  __TEXT.__const: 0x60
+  __TEXT.__cstring: 0x26f
+  __TEXT.__oslogstring: 0x737
+  __TEXT.__unwind_info: 0xc8
+  __TEXT.__objc_classname: 0x88
+  __TEXT.__objc_methname: 0xb24
   __TEXT.__objc_methtype: 0x2d5
-  __TEXT.__objc_stubs: 0x920
-  __DATA_CONST.__got: 0x78
-  __DATA_CONST.__const: 0x180
+  __TEXT.__objc_stubs: 0x940
+  __DATA_CONST.__got: 0x88
+  __DATA_CONST.__const: 0x120
   __DATA_CONST.__objc_classlist: 0x18
   __DATA_CONST.__objc_catlist: 0x10
   __DATA_CONST.__objc_protolist: 0x10
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_const: 0x5f8
-  __DATA_CONST.__objc_selrefs: 0x2b0
-  __AUTH_CONST.__cfstring: 0x280
+  __DATA_CONST.__objc_selrefs: 0x2b8
+  __DATA_CONST.__objc_classrefs: 0x70
+  __DATA_CONST.__objc_superrefs: 0x18
+  __AUTH_CONST.__cfstring: 0x2a0
   __AUTH_CONST.__objc_const: 0x1a0
   __AUTH_CONST.__const: 0x20
-  __AUTH_CONST.__auth_got: 0x1c0
+  __AUTH_CONST.__auth_got: 0x188
   __AUTH.__objc_data: 0xa0
-  __DATA.__objc_classrefs: 0x68
-  __DATA.__objc_superrefs: 0x18
   __DATA.__objc_ivar: 0x10
   __DATA.__data: 0xc0
-  __DATA.__bss: 0x18
   __DATA_DIRTY.__objc_data: 0x50
   - /System/Library/Frameworks/Accounts.framework/Accounts
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/Foundation.framework/Foundation
   - /System/Library/PrivateFrameworks/AccountsDaemon.framework/AccountsDaemon
+  - /System/Library/PrivateFrameworks/AppleAccount.framework/AppleAccount
   - /System/Library/PrivateFrameworks/AppleMediaServices.framework/AppleMediaServices
   - /System/Library/PrivateFrameworks/AuthKit.framework/AuthKit
   - /System/Library/PrivateFrameworks/IDS.framework/IDS
-  - /System/Library/PrivateFrameworks/SoftLinking.framework/SoftLinking
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 513F2D2B-1DA7-3104-A9B6-DC5B039FFA6E
-  Functions: 39
-  Symbols:   106
+  UUID: E2C326D7-2E5D-3F3B-8650-B52AF57F5D17
+  Functions: 33
+  Symbols:   102
   CStrings:  244
 
Symbols:
+ _OBJC_CLASS_$_NSString
+ _kAASaveOptionCompanionDeviceClientInfoKey
+ _kAASaveOptionCompanionDeviceUDIDKey
+ _objc_retain_x24
- __Block_object_dispose
- __Unwind_Resume
- ___objc_personality_v0
- __sl_dlopen
- _abort_report_np
- _dlerror
- _dlsym
- _free
CStrings:
+ "%@: "
+ "%@: [%@] "
+ "%{public}@Not syncing. Only the account's enableICMLStateReason was changed. account = %{public}@"
+ "T@\"NSString\",?,R,C"
+ "stringWithFormat:"
- "%s"
- "%{public}@: [%{public}@] Not syncing. Only the account's cookies (modified=%d), enableICMLStateReason (modified=%d) were changed. account = %{public}@"
- "cookies"
- "kAASaveOptionCompanionDeviceClientInfoKey"
- "kAASaveOptionCompanionDeviceUDIDKey"
- "softlink:r:path:/System/Library/PrivateFrameworks/AppleAccount.framework/AppleAccount"

```
