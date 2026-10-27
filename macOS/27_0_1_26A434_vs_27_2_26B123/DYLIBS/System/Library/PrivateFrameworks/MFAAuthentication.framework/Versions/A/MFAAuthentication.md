## MFAAuthentication

> `/System/Library/PrivateFrameworks/MFAAuthentication.framework/Versions/A/MFAAuthentication`

```diff

-1216.0.0.0.0
-  __TEXT.__text: 0x27a34
-  __TEXT.__objc_methlist: 0x4a4
-  __TEXT.__const: 0x68b23
-  __TEXT.__cstring: 0x1607
-  __TEXT.__gcc_except_tab: 0x90
-  __TEXT.__oslogstring: 0x4aaa
+1219.40.10.0.0
+  __TEXT.__text: 0x2a448
+  __TEXT.__objc_methlist: 0x4dc
+  __TEXT.__const: 0x68b33
+  __TEXT.__cstring: 0x198c
+  __TEXT.__oslogstring: 0x4e3a
+  __TEXT.__gcc_except_tab: 0x22c
   __TEXT.__ustring: 0xa
-  __TEXT.__unwind_info: 0x678
+  __TEXT.__dlopen_cstrs: 0x5a
+  __TEXT.__unwind_info: 0x6d8
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0
   __TEXT.__objc_classname: 0x0
   __TEXT.__objc_methname: 0x0
   __TEXT.__objc_methtype: 0x0
-  __DATA_CONST.__const: 0x5410
+  __DATA_CONST.__const: 0x5430
   __DATA_CONST.__objc_classlist: 0x20
   __DATA_CONST.__objc_catlist: 0x10
   __DATA_CONST.__objc_protolist: 0x8
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x4c0
+  __DATA_CONST.__objc_selrefs: 0x520
   __DATA_CONST.__objc_protorefs: 0x8
   __DATA_CONST.__objc_superrefs: 0x18
   __DATA_CONST.__objc_arraydata: 0x60
-  __DATA_CONST.__got: 0x1f0
-  __AUTH_CONST.__const: 0x790
-  __AUTH_CONST.__cfstring: 0x1900
+  __DATA_CONST.__got: 0x200
+  __AUTH_CONST.__const: 0x810
+  __AUTH_CONST.__cfstring: 0x1920
   __AUTH_CONST.__objc_const: 0x648
-  __AUTH_CONST.__objc_intobj: 0x90
+  __AUTH_CONST.__objc_intobj: 0xc0
   __AUTH_CONST.__objc_dictobj: 0x28
-  __AUTH_CONST.__auth_got: 0x668
+  __AUTH_CONST.__auth_got: 0x6a0
   __AUTH_CONST.__auth_ptr: 0x0
   __AUTH.__objc_data: 0x50
   __DATA.__objc_ivar: 0x10
   __DATA.__data: 0x60
-  __DATA.__bss: 0x80
+  __DATA.__bss: 0x90
   __DATA_DIRTY.__objc_data: 0xf0
   __DATA_DIRTY.__data: 0xc8
-  __DATA_DIRTY.__bss: 0x1a8
+  __DATA_DIRTY.__bss: 0x228
   __DATA_DIRTY.__common: 0x1c
   - /System/Library/Frameworks/CoreFoundation.framework/Versions/A/CoreFoundation
   - /System/Library/Frameworks/Foundation.framework/Versions/C/Foundation
   - /System/Library/Frameworks/IOKit.framework/Versions/A/IOKit
   - /System/Library/Frameworks/Security.framework/Versions/A/Security
+  - /System/Library/PrivateFrameworks/SoftLinking.framework/Versions/A/SoftLinking
   - /usr/lib/libMobileGestalt.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 748
-  Symbols:   1970
-  CStrings:  646
+  Functions: 796
+  Symbols:   2054
+  CStrings:  693
 
Symbols:
+ -[MFAACertificateManager verifyComponentType:forModuleMFi3Certificate:forAuthFlags:]
+ -[MFAACertificateManager verifyComponentType:forModuleMFi4Certificate:]
+ -[MFAACertificateManager verifyIndex:forModuleMFi4Certificate:forModule:]
+ -[MFAACertificateManager verifyModuleCertificate:forModule:forAuthFlags:forIndex:]
+ -[MFAACertificateManager verifyPartNumber:forModuleMFi4Certificate:forModule:]
+ DeviceIdentityFrameworkAvailable.available
+ DeviceIdentityLibraryCore.frameworkLibrary
+ GCC_except_table0
+ GCC_except_table50
+ GCC_except_table59
+ GCC_except_table7
+ MFAADeviceIdentityRequestCertificate
+ _DeviceIdentityLibrary
+ _DeviceIdentityLibraryCore
+ _OBJC_CLASS_$_NSArray
+ _OUTLINED_FUNCTION_53
+ _OUTLINED_FUNCTION_54
+ _OUTLINED_FUNCTION_55
+ _SecAccessControlCreate
+ _SecAccessControlSetProtection
+ _SecCertificateCopyComponentAttributes
+ __MFAADeviceIdentityRequestCertificate_block_invoke
+ ___DeviceIdentityLibraryCore_block_invoke
+ ___MFAADeviceIdentityRequestCertificate_block_invoke
+ ___acc_internalSettings_isInternalBuild_block_invoke
+ ___block_descriptor_40_e8_32r_e5_v8?0l
+ ___block_descriptor_89_e8_32s40s48r56r64r72r_e43_v32?0^{__SecKey=}8"NSArray"16"NSError"24l
+ ___copy_helper_block_e8_32r
+ ___copy_helper_block_e8_32s40s48r56r64r72r
+ ___destroy_helper_block_e8_32r
+ ___destroy_helper_block_e8_32s40s48r56r64r72r
+ ___getDeviceIdentityIssueClientCertificateWithCompletionSymbolLoc_block_invoke
+ ___getkMAOptionsBAAAccessControlsSymbolLoc_block_invoke
+ ___getkMAOptionsBAACertTypeMFiSymbolLoc_block_invoke
+ ___getkMAOptionsBAACertTypeSymbolLoc_block_invoke
+ ___getkMAOptionsBAAIgnoreExistingKeychainItemsSymbolLoc_block_invoke
+ ___getkMAOptionsBAAKeychainAccessGroupSymbolLoc_block_invoke
+ ___getkMAOptionsBAAKeychainLabelSymbolLoc_block_invoke
+ ___getkMAOptionsBAAMFiPropertiesSymbolLoc_block_invoke
+ ___getkMAOptionsBAAOIDMFiAccessoryPropertiesSymbolLoc_block_invoke
+ ___getkMAOptionsBAAOIDSToIncludeSymbolLoc_block_invoke
+ ___getkMAOptionsBAASCRTAttestationSymbolLoc_block_invoke
+ ___getkMAOptionsBAASkipNetworkRequestSymbolLoc_block_invoke
+ ___getkMAOptionsBAAValiditySymbolLoc_block_invoke
+ ___getkMAOptionsResuseExistingKeySymbolLoc_block_invoke
+ __sl_dlopen
+ _abort_report_np
+ _acc_internalSettings_boolForKey
+ _acc_internalSettings_integerForKey
+ _acc_internalSettings_isInternalBuild
+ _audit_stringDeviceIdentity
+ _dlerror
+ _dlsym
+ _getDeviceIdentityIssueClientCertificateWithCompletionSymbolLoc
+ _kSecAttrAccessibleAlwaysThisDeviceOnlyPrivate
+ _objc_msgSend$arrayWithObjects:count:
+ _objc_msgSend$initWithBytes:length:
+ _objc_msgSend$isEqualToNumber:
+ _objc_msgSend$numberWithUnsignedInt:
+ _objc_msgSend$setValue:forKey:
+ _objc_msgSend$subdataWithRange:
+ _objc_msgSend$timeIntervalSinceDate:
+ _objc_msgSend$verifyComponentType:forModuleMFi3Certificate:forAuthFlags:
+ _objc_msgSend$verifyComponentType:forModuleMFi4Certificate:
+ _objc_msgSend$verifyIndex:forModuleMFi4Certificate:forModule:
+ _objc_msgSend$verifyModuleCertificate:forModule:forAuthFlags:forIndex:
+ _objc_msgSend$verifyPartNumber:forModuleMFi4Certificate:forModule:
+ acc_internalSettings_boolForKey
+ acc_internalSettings_integerForKey
+ acc_internalSettings_isInternalBuild
+ acc_internalSettings_isInternalBuild.isInternalBuild
+ acc_internalSettings_isInternalBuild.onceToken
+ getDeviceIdentityIssueClientCertificateWithCompletionSymbolLoc.ptr
+ getkMAOptionsBAAAccessControlsSymbolLoc.ptr
+ getkMAOptionsBAACertTypeMFiSymbolLoc.ptr
+ getkMAOptionsBAACertTypeSymbolLoc.ptr
+ getkMAOptionsBAAIgnoreExistingKeychainItemsSymbolLoc.ptr
+ getkMAOptionsBAAKeychainAccessGroupSymbolLoc.ptr
+ getkMAOptionsBAAKeychainLabelSymbolLoc.ptr
+ getkMAOptionsBAAMFiPropertiesSymbolLoc.ptr
+ getkMAOptionsBAAOIDMFiAccessoryPropertiesSymbolLoc.ptr
+ getkMAOptionsBAAOIDSToIncludeSymbolLoc.ptr
+ getkMAOptionsBAASCRTAttestationSymbolLoc.ptr
+ getkMAOptionsBAASkipNetworkRequestSymbolLoc.ptr
+ getkMAOptionsBAAValiditySymbolLoc.ptr
+ getkMAOptionsResuseExistingKeySymbolLoc.ptr
- GCC_except_table45
- GCC_except_table54
CStrings:
+ "%s"
+ "%s: !certRef"
+ "%s: !componentAttributes"
+ "%s: !framework"
+ "%s: !retrievedIndex"
+ "%s: %@, options %@\n\n"
+ "%s: (moduleType=%d) found certPartNumber:%@"
+ "%s: (moduleType=%d) found index:%@"
+ "%s: (moduleType=%d) index:%@"
+ "%s: (moduleType=%d) productTypeString:%@"
+ "%s: Failed to create access control! error %@"
+ "%s: Failed to obtain valid certificates from server: %s\n"
+ "%s: Failed to set ACL protection to %@! error %@"
+ "%s: error: %s\n"
+ "%s:%d %@, IssueClientCertificate response took too long!!! %f seconds."
+ "%s:%d %@, got IssueClientCertificate response in %f seconds. error %@"
+ "%s:%d localAccessControl %@"
+ "%s[%lu]: data: (%zu bytes)\n%{coreacc:bytes}.*P"
+ "%s[%lu]: desc: %s\n\n"
+ "(moduleType=%d) Error: missing index"
+ "(moduleType=%d) Failure: cannot find part number"
+ "(moduleType=%d) Failure: part number is too short"
+ "-[MFAACertificateManager verifyIndex:forModuleMFi4Certificate:forModule:]"
+ "-[MFAACertificateManager verifyModuleCertificate:forModule:forAuthFlags:forIndex:]"
+ "-[MFAACertificateManager verifyPartNumber:forModuleMFi4Certificate:forModule:]"
+ "/System/Library/PrivateFrameworks/DeviceIdentity.framework/Contents/MacOS/DeviceIdentity"
+ "DeviceIdentityIssueClientCertificateWithCompletion"
+ "MFAADeviceIdentityRequestCertificate"
+ "MFAADeviceIdentityRequestCertificate_block_invoke"
+ "acc_internalSettings: internal-only setting %{public}@ active"
+ "acc_internalSettings: internal-only setting %{public}@ active (%ld)"
+ "iPhone19,4"
+ "kMAOptionsBAAAccessControls"
+ "kMAOptionsBAACertType"
+ "kMAOptionsBAACertTypeMFi"
+ "kMAOptionsBAAIgnoreExistingKeychainItems"
+ "kMAOptionsBAAKeychainAccessGroup"
+ "kMAOptionsBAAKeychainLabel"
+ "kMAOptionsBAAMFiProperties"
+ "kMAOptionsBAAOIDMFiAccessoryProperties"
+ "kMAOptionsBAAOIDSToInclude"
+ "kMAOptionsBAASCRTAttestation"
+ "kMAOptionsBAASkipNetworkRequest"
+ "kMAOptionsBAAValidity"
+ "kMAOptionsResuseExistingKey"
+ "softlink:r:path:/System/Library/PrivateFrameworks/DeviceIdentity.framework/DeviceIdentity"
+ "v32@?0^{__SecKey=}8@\"NSArray\"16@\"NSError\"24"
```
