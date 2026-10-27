## SetupAssistantFramework

> `/System/Library/PrivateFrameworks/SetupAssistantFramework.framework/Versions/A/SetupAssistantFramework`

```diff

-7548.0.0.0.0
-  __TEXT.__text: 0xc488
-  __TEXT.__objc_methlist: 0xfe0
+7550.2.3.0.0
+  __TEXT.__text: 0xce08
+  __TEXT.__objc_methlist: 0x1098
   __TEXT.__const: 0xb0
-  __TEXT.__cstring: 0x1928
+  __TEXT.__cstring: 0x1990
   __TEXT.__oslogstring: 0x1ba
   __TEXT.__gcc_except_tab: 0xa4
   __TEXT.__dlopen_cstrs: 0x4e
-  __TEXT.__unwind_info: 0x478
+  __TEXT.__unwind_info: 0x4b8
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0
   __TEXT.__objc_classname: 0x0

   __DATA_CONST.__objc_classlist: 0x68
   __DATA_CONST.__objc_protolist: 0x40
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x9a0
+  __DATA_CONST.__objc_selrefs: 0xa10
   __DATA_CONST.__objc_protorefs: 0x18
   __DATA_CONST.__objc_superrefs: 0x38
-  __DATA_CONST.__got: 0x188
+  __DATA_CONST.__got: 0x198
   __AUTH_CONST.__const: 0x310
-  __AUTH_CONST.__cfstring: 0x11e0
-  __AUTH_CONST.__objc_const: 0x23d0
+  __AUTH_CONST.__cfstring: 0x1220
+  __AUTH_CONST.__objc_const: 0x24c0
   __AUTH_CONST.__auth_got: 0x260
   __AUTH_CONST.__auth_ptr: 0x0
   __AUTH.__objc_data: 0x3c0

   - /System/Library/PrivateFrameworks/SystemAdministration.framework/Versions/A/SystemAdministration
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 347
-  Symbols:   935
-  CStrings:  213
+  Functions: 368
+  Symbols:   971
+  CStrings:  215
 
Symbols:
+ +[SAFacelessConfiguration guestVersionIsNewer:]
+ +[SAFacelessConfiguration shouldShowLicenseAgreementForHostVersion:hostLicenseVersion:]
+ +[SAFacelessConfiguration shouldShowLicenseAgreementForHostVersion:hostLicenseVersion:guestLicenseVersion:]
+ -[MBSAConnection deleteTelemetryPreRebootDurationWithCompletionBlock:]
+ -[MBSAConnection deleteTelemetrySessionIDWithCompletionBlock:]
+ -[MBSAConnection loadTelemetryPreRebootDurationWithCompletionBlock:]
+ -[MBSAConnection loadTelemetrySessionIDWithCompletionBlock:]
+ -[MBSAConnection performFastUserSwitchToLocallyCreatedUserWithUID:withPassword:isDemoUser:initialPerUserState:completionBlock:]
+ -[MBSAConnection persistTelemetryPreRebootDuration:withCompletionBlock:]
+ -[MBSAConnection persistTelemetrySessionID:withCompletionBlock:]
+ _MBDeleteTelemetryPreRebootDuration
+ _MBDeleteTelemetrySessionID
+ _MBLoadTelemetryPreRebootDuration
+ _MBLoadTelemetrySessionID
+ _MBPersistTelemetryPreRebootDuration
+ _MBPersistTelemetrySessionID
+ _OBJC_CLASS_$_NSData
+ _OBJC_CLASS_$_NSProcessInfo
+ ___127-[MBSAConnection performFastUserSwitchToLocallyCreatedUserWithUID:withPassword:isDemoUser:initialPerUserState:completionBlock:]_block_invoke
+ ___60-[MBSAConnection loadTelemetrySessionIDWithCompletionBlock:]_block_invoke
+ ___62-[MBSAConnection deleteTelemetrySessionIDWithCompletionBlock:]_block_invoke
+ ___64-[MBSAConnection persistTelemetrySessionID:withCompletionBlock:]_block_invoke
+ ___68-[MBSAConnection loadTelemetryPreRebootDurationWithCompletionBlock:]_block_invoke
+ ___70-[MBSAConnection deleteTelemetryPreRebootDurationWithCompletionBlock:]_block_invoke
+ ___72-[MBSAConnection persistTelemetryPreRebootDuration:withCompletionBlock:]_block_invoke
+ _objc_msgSend$dataWithBytes:length:
+ _objc_msgSend$dataWithContentsOfFile:
+ _objc_msgSend$deleteTelemetryPreRebootDurationWithCompletionBlock:
+ _objc_msgSend$deleteTelemetrySessionIDWithCompletionBlock:
+ _objc_msgSend$getBytes:length:
+ _objc_msgSend$guestVersionIsNewer:
+ _objc_msgSend$loadTelemetryPreRebootDurationWithCompletionBlock:
+ _objc_msgSend$loadTelemetrySessionIDWithCompletionBlock:
+ _objc_msgSend$operatingSystemVersion
+ _objc_msgSend$performFastUserSwitchToLocallyCreatedUserWithUID:withPassword:isDemoUser:initialPerUserState:completionBlock:
+ _objc_msgSend$persistTelemetryPreRebootDuration:withCompletionBlock:
+ _objc_msgSend$persistTelemetrySessionID:withCompletionBlock:
+ _objc_msgSend$processInfo
+ _objc_msgSend$shouldShowLicenseAgreementForHostVersion:hostLicenseVersion:guestLicenseVersion:
- -[MBSAConnection performFastUserSwitchToLocallyCreatedUserWithUID:withPassword:isDemoUser:completionBlock:]
- ___107-[MBSAConnection performFastUserSwitchToLocallyCreatedUserWithUID:withPassword:isDemoUser:completionBlock:]_block_invoke
- _objc_msgSend$performFastUserSwitchToLocallyCreatedUserWithUID:withPassword:isDemoUser:completionBlock:
CStrings:
+ "/.resolve/33/private/var/db/.TelemetryPreRebootDuration"
+ "/.resolve/33/private/var/db/.TelemetrySessionID"
```
