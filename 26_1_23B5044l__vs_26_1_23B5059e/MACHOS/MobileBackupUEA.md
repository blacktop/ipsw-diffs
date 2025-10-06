## MobileBackupUEA

> `/System/Library/UserEventPlugins/MobileBackupUEA.plugin/MobileBackupUEA`

```diff

-2899.40.32.0.0
-  __TEXT.__text: 0x9d90
+2899.40.40.0.0
+  __TEXT.__text: 0x9dcc
   __TEXT.__auth_stubs: 0x6b0
   __TEXT.__objc_stubs: 0x1440
   __TEXT.__objc_methlist: 0x6ec
-  __TEXT.__const: 0x170
+  __TEXT.__const: 0x160
   __TEXT.__oslogstring: 0xfa5
-  __TEXT.__cstring: 0x1a53
+  __TEXT.__cstring: 0x1a35
   __TEXT.__objc_classname: 0x85
   __TEXT.__objc_methname: 0x1a7e
   __TEXT.__objc_methtype: 0x587
-  __TEXT.__gcc_except_tab: 0x168
+  __TEXT.__gcc_except_tab: 0x184
   __TEXT.__unwind_info: 0x218
   __DATA.__auth_got: 0x368
-  __DATA.__got: 0x120
+  __DATA.__got: 0x128
   __DATA.__const: 0x358
   __DATA.__cfstring: 0x7c0
   __DATA.__objc_classlist: 0x18

   - /System/Library/PrivateFrameworks/ManagedConfiguration.framework/ManagedConfiguration
   - /System/Library/PrivateFrameworks/MobileBackup.framework/MobileBackup
   - /System/Library/PrivateFrameworks/MobileKeyBag.framework/MobileKeyBag
+  - /System/Library/PrivateFrameworks/PasscodeAndBiometricsSettings.framework/PasscodeAndBiometricsSettings
   - /System/Library/PrivateFrameworks/PersistentConnection.framework/PersistentConnection
   - /System/Library/PrivateFrameworks/SpringBoardServices.framework/SpringBoardServices
   - /System/Library/PrivateFrameworks/UserManagement.framework/UserManagement
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 96284937-5BFA-38AD-81E6-03F44752BA7A
+  UUID: 37283E9D-AC12-3E57-B4A0-00E31B45DCD9
   Functions: 152
-  Symbols:   192
-  CStrings:  712
+  Symbols:   193
+  CStrings:  711
 
Symbols:
+ _PABSUserChangedPasscodeNotification
Functions:
~ sub_23b4 -> sub_243c : 2700 -> 2760
CStrings:
+ "Received %{public}@"
- "Received %{public}s"
- "backupd-test-passcode-changed"

```
