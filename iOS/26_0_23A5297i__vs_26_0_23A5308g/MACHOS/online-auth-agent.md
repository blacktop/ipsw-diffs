## online-auth-agent

> `/usr/libexec/online-auth-agent`

```diff

-463.0.4.0.0
-  __TEXT.__text: 0x41c1c
-  __TEXT.__auth_stubs: 0x1e80
+463.0.8.0.0
+  __TEXT.__text: 0x40b04
+  __TEXT.__auth_stubs: 0x1e90
   __TEXT.__objc_stubs: 0x17a0
-  __TEXT.__objc_methlist: 0x77c
+  __TEXT.__objc_methlist: 0x784
   __TEXT.__const: 0x226c
-  __TEXT.__cstring: 0x4557
-  __TEXT.__gcc_except_tab: 0x4d4
-  __TEXT.__objc_methname: 0x1c9b
-  __TEXT.__oslogstring: 0x37cb
+  __TEXT.__cstring: 0x4077
+  __TEXT.__gcc_except_tab: 0x438
+  __TEXT.__objc_methname: 0x1cf5
+  __TEXT.__oslogstring: 0x382b
   __TEXT.__objc_classname: 0xd5
   __TEXT.__objc_methtype: 0x381
-  __TEXT.__dlopen_cstrs: 0x12c
+  __TEXT.__dlopen_cstrs: 0x5e
   __TEXT.__swift5_typeref: 0x907
   __TEXT.__swift5_capture: 0x5e8
   __TEXT.__constg_swiftt: 0xbfc

   __TEXT.__swift5_types: 0xf0
   __TEXT.__swift5_protos: 0xc
   __TEXT.__swift5_assocty: 0x168
-  __TEXT.__unwind_info: 0xfc0
+  __TEXT.__unwind_info: 0xfa0
   __TEXT.__eh_frame: 0x1400
-  __DATA_CONST.__auth_got: 0xf50
-  __DATA_CONST.__got: 0x450
-  __DATA_CONST.__auth_ptr: 0x458
-  __DATA_CONST.__const: 0x2560
-  __DATA_CONST.__cfstring: 0x1560
+  __DATA_CONST.__auth_got: 0xf58
+  __DATA_CONST.__got: 0x488
+  __DATA_CONST.__auth_ptr: 0x468
+  __DATA_CONST.__const: 0x2530
+  __DATA_CONST.__cfstring: 0x1500
   __DATA_CONST.__objc_classlist: 0xa0
   __DATA_CONST.__objc_protolist: 0x30
   __DATA_CONST.__objc_imageinfo: 0x8

   __DATA_CONST.__objc_intobj: 0x48
   __DATA_CONST.__objc_arraydata: 0x10
   __DATA_CONST.__objc_dictobj: 0x28
-  __DATA.__objc_const: 0x1410
-  __DATA.__objc_selrefs: 0x958
+  __DATA.__objc_const: 0x1420
+  __DATA.__objc_selrefs: 0x960
   __DATA.__objc_ivar: 0x60
   __DATA.__objc_data: 0x4c0
   __DATA.__data: 0x1688
-  __DATA.__bss: 0x30a0
+  __DATA.__bss: 0x3050
   __DATA.__common: 0x118
   - /System/Library/Frameworks/CloudKit.framework/CloudKit
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation

   - /System/Library/Frameworks/Security.framework/Security
   - /System/Library/PrivateFrameworks/CoreAnalytics.framework/CoreAnalytics
   - /System/Library/PrivateFrameworks/CoreTime.framework/CoreTime
+  - /System/Library/PrivateFrameworks/DeviceIdentity.framework/DeviceIdentity
   - /System/Library/PrivateFrameworks/InstalledContentLibrary.framework/InstalledContentLibrary
   - /System/Library/PrivateFrameworks/MessageSecurity.framework/MessageSecurity
   - /System/Library/PrivateFrameworks/MobileAsset.framework/MobileAsset
   - /System/Library/PrivateFrameworks/MobileInstallation.framework/MobileInstallation
+  - /System/Library/PrivateFrameworks/ProfileValidatedAppIdentity.framework/ProfileValidatedAppIdentity
   - /System/Library/PrivateFrameworks/RunningBoardServices.framework/RunningBoardServices
   - /System/Library/PrivateFrameworks/SoftLinking.framework/SoftLinking
   - /usr/lib/libCoreEntitlements.dylib

   - /usr/lib/swift/libswift_Builtin_float.dylib
   - /usr/lib/swift/libswift_DarwinFoundation1.dylib
   - /usr/lib/swift/libswiftos.dylib
-  UUID: FB60BC2C-24C8-3972-B03E-10D491CF943D
-  Functions: 1364
-  Symbols:   439
-  CStrings:  1315
+  UUID: D8BE7EF0-3014-3EA8-8601-586A3C1583E6
+  Functions: 1342
+  Symbols:   447
+  CStrings:  1291
 
Symbols:
+ _DeviceIdentityIssueClientCertificateWithCompletion
+ _OBJC_CLASS_$_PVAppIdentityDigest
+ _PVAppIdentity_GenerateDigestWithCompletion
+ _kMAOptionsBAAAccessControls
+ _kMAOptionsBAAKeychainAccessGroup
+ _kMAOptionsBAAKeychainLabel
+ _kMAOptionsBAANetworkTimeoutInterval
+ _kMAOptionsBAASCRTAttestation
+ _kMAOptionsBAAValidity
- _objc_getClass
CStrings:
+ "DeviceIdentityIssueClientCertificate not available"
+ "PVAppIdentityDigest not supported"
+ "T@\"NSObject<OS_dispatch_semaphore>\",R,N,V_transactionSemaphore"
+ "_transactionSemaphore"
+ "transactionSemaphore"
- "AppIdentity.m"
- "Class getPVAppIdentityDigestClass(void)_block_invoke"
- "DeviceIdentityIssueClientCertificateWithCompletion"
- "PVAppIdentityDigest"
- "PVAppIdentity_GenerateDigestWithCompletion"
- "Unable to find class %s"
- "_transactionSem"
- "kMAOptionsBAAAccessControls"
- "kMAOptionsBAAKeychainAccessGroup"
- "kMAOptionsBAAKeychainLabel"
- "kMAOptionsBAANetworkTimeoutInterval"
- "kMAOptionsBAASCRTAttestation"
- "kMAOptionsBAAValidity"
- "online_auth_server.m"
- "softlink:o:path:/System/Library/PrivateFrameworks/ProfileValidatedAppIdentity.framework/ProfileValidatedAppIdentity"
- "softlink:r:path:/System/Library/PrivateFrameworks/DeviceIdentity.framework/DeviceIdentity"
- "typeof (kMAOptionsBAAAccessControls) getkMAOptionsBAAAccessControls(void)"
- "typeof (kMAOptionsBAAKeychainAccessGroup) getkMAOptionsBAAKeychainAccessGroup(void)"
- "typeof (kMAOptionsBAAKeychainLabel) getkMAOptionsBAAKeychainLabel(void)"
- "typeof (kMAOptionsBAANetworkTimeoutInterval) getkMAOptionsBAANetworkTimeoutInterval(void)"
- "typeof (kMAOptionsBAASCRTAttestation) getkMAOptionsBAASCRTAttestation(void)"
- "typeof (kMAOptionsBAAValidity) getkMAOptionsBAAValidity(void)"
- "void *DeviceIdentityLibrary(void)"
- "void *ProfileValidatedAppIdentityLibrary(void)"
- "void sl_PVAppIdentity_GenerateDigestWithCompletion(NSURL *__strong, NSData *__strong, dispatch_queue_t  _Nullable __strong, void (^__strong)(PVAppIdentityDigest *__strong))"
- "void wl_DeviceIdentityIssueClientCertificateWithCompletion(__strong dispatch_queue_t, NSDictionary *__strong, __strong MABAACompletionBlock)"

```
