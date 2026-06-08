## DeviceManagementClientAccountNotificationPlugin

> `/System/Library/Accounts/Notification/DeviceManagementClientAccountNotificationPlugin.bundle/DeviceManagementClientAccountNotificationPlugin`

```diff

-59.120.4.0.0
-  __TEXT.__text: 0x8d8
-  __TEXT.__auth_stubs: 0x1a0
-  __TEXT.__objc_stubs: 0x2c0
-  __TEXT.__objc_methlist: 0x1b4
-  __TEXT.__const: 0x78
+105.0.0.0.0
+  __TEXT.__text: 0xa38
+  __TEXT.__auth_stubs: 0x1b0
+  __TEXT.__objc_stubs: 0x3c0
+  __TEXT.__objc_methlist: 0x1cc
+  __TEXT.__const: 0x80
+  __TEXT.__oslogstring: 0x277
   __TEXT.__cstring: 0x5d
-  __TEXT.__oslogstring: 0x1a1
   __TEXT.__objc_classname: 0x43
-  __TEXT.__objc_methname: 0x49f
+  __TEXT.__objc_methname: 0x59b
   __TEXT.__objc_methtype: 0x220
-  __TEXT.__unwind_info: 0x78
-  __DATA_CONST.__auth_got: 0xd8
-  __DATA_CONST.__got: 0x50
+  __TEXT.__unwind_info: 0x88
   __DATA_CONST.__const: 0x40
   __DATA_CONST.__cfstring: 0xe0
   __DATA_CONST.__objc_classlist: 0x8
   __DATA_CONST.__objc_protolist: 0x10
   __DATA_CONST.__objc_imageinfo: 0x8
+  __DATA_CONST.__auth_got: 0xe0
+  __DATA_CONST.__got: 0x58
   __DATA.__objc_const: 0x230
-  __DATA.__objc_selrefs: 0x190
+  __DATA.__objc_selrefs: 0x1d0
   __DATA.__objc_data: 0x50
   __DATA.__data: 0xc0
   - /System/Library/Frameworks/Accounts.framework/Accounts

   - /System/Library/PrivateFrameworks/AccountsDaemon.framework/AccountsDaemon
   - /System/Library/PrivateFrameworks/DMCEnrollmentLibrary.framework/DMCEnrollmentLibrary
   - /System/Library/PrivateFrameworks/DMCUtilities.framework/DMCUtilities
+  - /System/Library/PrivateFrameworks/MDM.framework/MDM
   - /System/Library/PrivateFrameworks/MDMClientLibrary.framework/MDMClientLibrary
   - /System/Library/PrivateFrameworks/ManagedConfiguration.framework/ManagedConfiguration
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 45825A48-8C75-3884-BFCF-A073C4EBD959
-  Functions: 6
-  Symbols:   47
-  CStrings:  104
+  UUID: 3B461C90-B61F-3B8D-AD85-ABF29BBBF34C
+  Functions: 8
+  Symbols:   49
+  CStrings:  115
 
Symbols:
+ _DMCIsDevicePasscodeSet
+ _MDMCreateExtractableLAContextWithPasscode
+ _OBJC_CLASS_$_MCProfileConnection
+ _objc_claimAutoreleasedReturnValue
+ _objc_retain_x8
- _objc_retainAutoreleasedReturnValue
- _objc_retain_x21
- _objc_retain_x28
CStrings:
+ "DMCAccountNotificationPlugin failed to update device passcode with error: %{public}@"
+ "DMCAccountNotificationPlugin no raw password from account"
+ "DMCAccountNotificationPlugin updating device passcode with account: %@"
+ "_aa_rawPassword"
+ "_changeDevicePasscodeIfNeededWithAccount:"
+ "aa_isManagedAppleID"
+ "changePasscodeWithOldPasscodeContext:newPasscodeContext:outError:"
+ "externalizedContext"
+ "inSharediPadTemporarySession"
+ "sharedConnection"
+ "useManagedAccountPasswordAsDevicePasscode"

```
