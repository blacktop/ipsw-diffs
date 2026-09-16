## SetupAssistantSupport

> `/System/Library/PrivateFrameworks/SetupAssistantSupport.framework/SetupAssistantSupport`

```diff

-567.101.0.0.0
-  __TEXT.__text: 0x16088
+568.1.3.0.0
+  __TEXT.__text: 0x16104
   __TEXT.__objc_methlist: 0x19a4
   __TEXT.__const: 0xb0
-  __TEXT.__cstring: 0x1135
-  __TEXT.__oslogstring: 0xabe
-  __TEXT.__gcc_except_tab: 0x360
+  __TEXT.__cstring: 0x111e
+  __TEXT.__oslogstring: 0xaf4
+  __TEXT.__gcc_except_tab: 0x368
   __TEXT.__dlopen_cstrs: 0x6f4
-  __TEXT.__unwind_info: 0x660
+  __TEXT.__unwind_info: 0x668
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0
   __TEXT.__objc_classname: 0x0

   __DATA_CONST.__objc_classlist: 0xd8
   __DATA_CONST.__objc_protolist: 0x40
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x11f8
+  __DATA_CONST.__objc_selrefs: 0x1200
   __DATA_CONST.__objc_protorefs: 0x8
   __DATA_CONST.__objc_superrefs: 0x60
   __DATA_CONST.__got: 0x2c8
   __AUTH_CONST.__const: 0x40
-  __AUTH_CONST.__cfstring: 0x15a0
+  __AUTH_CONST.__cfstring: 0x1580
   __AUTH_CONST.__objc_const: 0x3048
   __AUTH_CONST.__objc_intobj: 0x90
   __AUTH_CONST.__auth_got: 0x0

   - /System/Library/Frameworks/Foundation.framework/Foundation
   - /System/Library/Frameworks/LocalAuthentication.framework/LocalAuthentication
   - /System/Library/Frameworks/Network.framework/Network
+  - /System/Library/Frameworks/SystemConfiguration.framework/SystemConfiguration
   - /System/Library/PrivateFrameworks/AppleAccount.framework/AppleAccount
   - /System/Library/PrivateFrameworks/AuthKit.framework/AuthKit
   - /System/Library/PrivateFrameworks/CoreTime.framework/CoreTime

   - /usr/lib/libMobileGestalt.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 622
-  Symbols:   1736
+  Functions: 623
+  Symbols:   1738
   CStrings:  324
 
Symbols:
+ _SCDynamicStoreCopyComputerName
+ _objc_msgSend$dateOfLastBackupWithError:
Functions:
~ -[SASProximityInformation loadInformation] : 4944 -> 5016
+ -[SASProximityInformation loadInformation].cold.4
CStrings:
+ "Failed to check if backup is supported on cellular: %{public}@"
+ "Failed to determine if initial mega backup completed: %@{public}"
+ "Failed to get date of last backup: %@"
- "Failed to check if backup is supported on cellular: %@"
- "Failed to determine if initial mega backup completed: %@"
- "UserAssignedDeviceName"
```
