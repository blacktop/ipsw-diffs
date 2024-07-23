## MDMClientLibrary

> `/System/Library/PrivateFrameworks/MDMClientLibrary.framework/MDMClientLibrary`

```diff

-4.30.0.0.0
-  __TEXT.__text: 0x15cbc
-  __TEXT.__auth_stubs: 0x690
-  __TEXT.__objc_methlist: 0x10ec
-  __TEXT.__const: 0xa9
-  __TEXT.__gcc_except_tab: 0x3a8
-  __TEXT.__cstring: 0x1cdb
-  __TEXT.__oslogstring: 0x1cea
-  __TEXT.__dlopen_cstrs: 0x5a
-  __TEXT.__unwind_info: 0x4f0
-  __TEXT.__objc_classname: 0x2ab
-  __TEXT.__objc_methname: 0x3eee
-  __TEXT.__objc_methtype: 0x820
-  __TEXT.__objc_stubs: 0x2d80
-  __DATA_CONST.__got: 0x360
-  __DATA_CONST.__const: 0xdf8
-  __DATA_CONST.__objc_classlist: 0xb0
-  __DATA_CONST.__objc_protolist: 0x60
+4.34.0.0.0
+  __TEXT.__text: 0x19180
+  __TEXT.__auth_stubs: 0x8a0
+  __TEXT.__objc_methlist: 0x12ec
+  __TEXT.__const: 0xc9
+  __TEXT.__gcc_except_tab: 0x43c
+  __TEXT.__cstring: 0x1fb3
+  __TEXT.__oslogstring: 0x28a1
+  __TEXT.__dlopen_cstrs: 0xb7
+  __TEXT.__unwind_info: 0x5c0
+  __TEXT.__objc_classname: 0x2ff
+  __TEXT.__objc_methname: 0x4608
+  __TEXT.__objc_methtype: 0x890
+  __TEXT.__objc_stubs: 0x3160
+  __DATA_CONST.__got: 0x388
+  __DATA_CONST.__const: 0x1040
+  __DATA_CONST.__objc_classlist: 0xc0
+  __DATA_CONST.__objc_protolist: 0x68
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0xee8
+  __DATA_CONST.__objc_selrefs: 0x1068
   __DATA_CONST.__objc_protorefs: 0x10
-  __DATA_CONST.__objc_superrefs: 0x60
-  __AUTH_CONST.__auth_got: 0x358
-  __AUTH_CONST.__const: 0x380
-  __AUTH_CONST.__cfstring: 0x2c60
-  __AUTH_CONST.__objc_const: 0x3428
+  __DATA_CONST.__objc_superrefs: 0x70
+  __AUTH_CONST.__auth_got: 0x460
+  __AUTH_CONST.__const: 0x3a0
+  __AUTH_CONST.__cfstring: 0x2f80
+  __AUTH_CONST.__objc_const: 0x3a40
   __AUTH_CONST.__objc_intobj: 0x30
-  __AUTH.__objc_data: 0x50
-  __DATA.__objc_ivar: 0xec
-  __DATA.__data: 0x480
-  __DATA.__bss: 0x100
+  __AUTH.__objc_data: 0xf0
+  __DATA.__objc_ivar: 0x108
+  __DATA.__data: 0x4e0
+  __DATA.__bss: 0x110
   __DATA_DIRTY.__objc_data: 0x690
   __DATA_DIRTY.__bss: 0x40
   - /System/Library/Frameworks/Accounts.framework/Accounts
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
+  - /System/Library/Frameworks/CoreServices.framework/CoreServices
   - /System/Library/Frameworks/Foundation.framework/Foundation
+  - /System/Library/Frameworks/Security.framework/Security
+  - /System/Library/PrivateFrameworks/AppleMobileFileIntegrity.framework/AppleMobileFileIntegrity
   - /System/Library/PrivateFrameworks/DEPClientLibrary.framework/DEPClientLibrary
   - /System/Library/PrivateFrameworks/DMCUtilities.framework/DMCUtilities
   - /System/Library/PrivateFrameworks/SoftLinking.framework/SoftLinking
   - /usr/lib/libSystem.B.dylib
+  - /usr/lib/libmis.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 447
-  Symbols:   992
+  Functions: 506
+  Symbols:   1091
   CStrings:  0
 
Symbols:
+ _AMFIMDMModeEnroll
+ _AMFIMDMModeRemove
+ _AMFIProfileRemoveTrust
+ _AMFIProfileRequiresReboot
+ _AMFIProfileScheduleTrust
+ _AMFIProfileSetTrust
+ _AMFISupervisedModeSetState
+ _CFBooleanGetTypeID
+ _CFBooleanGetValue
+ _CFGetTypeID
+ _DMCLocalizedFormat
+ _DMCLocalizedStringByDevice
+ _DMCSendUPPTrustFailedNotification
+ _DMCSendUPPValidationOfflineNotification
+ _MISCopyErrorStringForErrorCode
+ _MISEnumerateInstalledProvisioningProfiles
+ _MISEnumerateTrustedUPPs
+ _MISProfileGetValue
+ _MISProvisioningProfileGetEntitlements
+ _MISProvisioningProfileGetUUID
+ _MISProvisioningProfileGrantsEntitlement
+ _MISProvisioningProfileIsAppleInternalProfile
+ _MISProvisioningProfileIsForLocalProvisioning
+ _MISProvisioningProfileProvisionsAllDevices
+ _MISUPPTrusted
+ _MISValidateUPP
+ _MISXMLProvisioningProfileGetDeveloperCertificates
+ _NSLog
+ _OBJC_CLASS_$_DMCAlertManager
+ _OBJC_CLASS_$_LSApplicationRecord
+ _OBJC_CLASS_$_MDMProvisioningProfile
+ _OBJC_CLASS_$_MDMProvisioningProfileTrust
+ _OBJC_METACLASS_$_MDMProvisioningProfile
+ _OBJC_METACLASS_$_MDMProvisioningProfileTrust
+ _SecCertificateCopySubjectSummary
+ _SecCertificateCreateWithData
+ _kCFBooleanTrue
+ _objc_autoreleasePoolPop
+ _objc_autoreleasePoolPush
+ _objc_getClass

```
