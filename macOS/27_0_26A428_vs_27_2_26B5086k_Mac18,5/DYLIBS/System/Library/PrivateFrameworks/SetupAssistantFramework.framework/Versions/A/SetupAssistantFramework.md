## SetupAssistantFramework

> `/System/Library/PrivateFrameworks/SetupAssistantFramework.framework/Versions/A/SetupAssistantFramework`

### Sections with Same Size but Changed Content

- `__TEXT.__cstring`

```diff

-7548.0.0.0.0
-  __TEXT.__text: 0xc044
-  __TEXT.__objc_methlist: 0xfe0
+7549.0.0.0.0
+  __TEXT.__text: 0xc298
+  __TEXT.__objc_methlist: 0x1008
   __TEXT.__const: 0xb0
   __TEXT.__cstring: 0x1928
   __TEXT.__oslogstring: 0x1ba
   __TEXT.__gcc_except_tab: 0xa4
   __TEXT.__dlopen_cstrs: 0x4e
-  __TEXT.__unwind_info: 0x530
+  __TEXT.__unwind_info: 0x540
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0
   __TEXT.__objc_classname: 0x0

   __DATA_CONST.__objc_classlist: 0x68
   __DATA_CONST.__objc_protolist: 0x40
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x9a0
+  __DATA_CONST.__objc_selrefs: 0x9c8
   __DATA_CONST.__objc_protorefs: 0x18
   __DATA_CONST.__objc_superrefs: 0x38
-  __DATA_CONST.__got: 0x188
+  __DATA_CONST.__got: 0x190
   __AUTH_CONST.__const: 0x310
   __AUTH_CONST.__cfstring: 0x11e0
   __AUTH_CONST.__objc_const: 0x23d0

   - /System/Library/PrivateFrameworks/SystemAdministration.framework/Versions/A/SystemAdministration
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 347
-  Symbols:   935
+  Functions: 350
+  Symbols:   943
   CStrings:  213
 
Symbols:
+ +[SAFacelessConfiguration guestVersionIsNewer:]
+ +[SAFacelessConfiguration shouldShowLicenseAgreementForHostVersion:hostLicenseVersion:]
+ +[SAFacelessConfiguration shouldShowLicenseAgreementForHostVersion:hostLicenseVersion:guestLicenseVersion:]
+ -[MBSAConnection performFastUserSwitchToLocallyCreatedUserWithUID:withPassword:isDemoUser:initialPerUserState:completionBlock:]
+ _OBJC_CLASS_$_NSProcessInfo
+ ___127-[MBSAConnection performFastUserSwitchToLocallyCreatedUserWithUID:withPassword:isDemoUser:initialPerUserState:completionBlock:]_block_invoke
+ _objc_msgSend$guestVersionIsNewer:
+ _objc_msgSend$operatingSystemVersion
+ _objc_msgSend$performFastUserSwitchToLocallyCreatedUserWithUID:withPassword:isDemoUser:initialPerUserState:completionBlock:
+ _objc_msgSend$processInfo
+ _objc_msgSend$shouldShowLicenseAgreementForHostVersion:hostLicenseVersion:guestLicenseVersion:
- -[MBSAConnection performFastUserSwitchToLocallyCreatedUserWithUID:withPassword:isDemoUser:completionBlock:]
- ___107-[MBSAConnection performFastUserSwitchToLocallyCreatedUserWithUID:withPassword:isDemoUser:completionBlock:]_block_invoke
- _objc_msgSend$performFastUserSwitchToLocallyCreatedUserWithUID:withPassword:isDemoUser:completionBlock:
CStrings:
+ "EA1666"
- "EA2005"
```
