## SoftwareUpdateSettings

> `/System/Library/PrivateFrameworks/SoftwareUpdateSettings.framework/SoftwareUpdateSettings`

```diff

-362.0.0.0.0
-  __TEXT.__text: 0x1d1cc
+384.0.0.0.0
+  __TEXT.__text: 0x1d818
   __TEXT.__auth_stubs: 0xa70
-  __TEXT.__objc_methlist: 0xd94
-  __TEXT.__cstring: 0x1e2a
-  __TEXT.__gcc_except_tab: 0x1b4
-  __TEXT.__oslogstring: 0x534
+  __TEXT.__objc_methlist: 0xd5c
+  __TEXT.__cstring: 0x1f7a
+  __TEXT.__gcc_except_tab: 0x1c4
+  __TEXT.__oslogstring: 0x5d4
   __TEXT.__dlopen_cstrs: 0xfe
   __TEXT.__const: 0x3e4
   __TEXT.__swift5_typeref: 0x15a

   __TEXT.__swift5_capture: 0x30
   __TEXT.__swift5_proto: 0x18
   __TEXT.__swift5_types: 0x14
-  __TEXT.__unwind_info: 0x4c0
-  __TEXT.__objc_classname: 0x2a0
-  __TEXT.__objc_methname: 0x432e
+  __TEXT.__unwind_info: 0x4c8
+  __TEXT.__objc_classname: 0x29d
+  __TEXT.__objc_methname: 0x4189
   __TEXT.__objc_methtype: 0xef5
-  __TEXT.__objc_stubs: 0x2e40
+  __TEXT.__objc_stubs: 0x2e80
   __DATA_CONST.__got: 0x378
-  __DATA_CONST.__const: 0x7c8
+  __DATA_CONST.__const: 0x868
   __DATA_CONST.__objc_classlist: 0x90
   __DATA_CONST.__objc_protolist: 0x30
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x1028
+  __DATA_CONST.__objc_selrefs: 0x1008
   __DATA_CONST.__objc_superrefs: 0x78
   __DATA_CONST.__objc_arraydata: 0xe0
   __AUTH_CONST.__auth_got: 0x548
   __AUTH_CONST.__auth_ptr: 0x108
-  __AUTH_CONST.__const: 0x1c0
-  __AUTH_CONST.__cfstring: 0x1ae0
-  __AUTH_CONST.__objc_const: 0x3418
+  __AUTH_CONST.__const: 0x1e0
+  __AUTH_CONST.__cfstring: 0x1be0
+  __AUTH_CONST.__objc_const: 0x3328
   __AUTH_CONST.__objc_dictobj: 0x118
   __AUTH_CONST.__objc_arrayobj: 0x18
   __AUTH_CONST.__objc_doubleobj: 0x30
   __AUTH.__objc_data: 0x5d8
   __AUTH.__data: 0xc0
-  __DATA.__objc_ivar: 0x154
+  __DATA.__objc_ivar: 0x134
   __DATA.__data: 0x378
-  __DATA.__bss: 0x430
+  __DATA.__bss: 0x440
   __DATA.__common: 0xa0
   __DATA_DIRTY.__objc_data: 0x50
   - /System/Library/Frameworks/Accounts.framework/Accounts

   - /usr/lib/swift/libswiftQuartzCore.dylib
   - /usr/lib/swift/libswiftSpatial.dylib
   - /usr/lib/swift/libswiftUniformTypeIdentifiers.dylib
+  - /usr/lib/swift/libswiftWebKit.dylib
   - /usr/lib/swift/libswiftXPC.dylib
+  - /usr/lib/swift/libswift_Builtin_float.dylib
+  - /usr/lib/swift/libswift_errno.dylib
+  - /usr/lib/swift/libswift_math.dylib
+  - /usr/lib/swift/libswift_signal.dylib
+  - /usr/lib/swift/libswift_stdio.dylib
+  - /usr/lib/swift/libswift_time.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  Functions: 521
-  Symbols:   593
-  CStrings:  1171
+  - /usr/lib/swift/libswiftsys_time.dylib
+  - /usr/lib/swift/libswiftunistd.dylib
+  Functions: 520
+  Symbols:   609
+  CStrings:  1168
 
Symbols:
+ __swift_FORCE_LOAD_$_swiftWebKit
+ __swift_FORCE_LOAD_$_swift_Builtin_float
+ __swift_FORCE_LOAD_$_swift_errno
+ __swift_FORCE_LOAD_$_swift_math
+ __swift_FORCE_LOAD_$_swift_signal
+ __swift_FORCE_LOAD_$_swift_stdio
+ __swift_FORCE_LOAD_$_swift_time
+ __swift_FORCE_LOAD_$_swiftsys_time
+ __swift_FORCE_LOAD_$_swiftunistd
+ _kSUSettingsUserDefaultsComingSoonTipLearnMoreLink
+ _kSUSettingsUserDefaultsComingSoonTipMessage
+ _kSUSettingsUserDefaultsComingSoonTipTitle
+ _kSUSettingsUserDefaultsHideComingSoonTip
+ _kSUSettingsUserDefaultsKeepPreviousMockingKitSesson
+ _kSUSettingsUserDefaultsNeRDProfileStatus
+ _kSUSettingsUserDefaultsShowComingSoonTip
+ _kSUSettingsUserDefaultsSkipMockingKitPIDValidation
CStrings:
+ "%!s(MISSING): Failed to mark terms as disagreed in iCloud with HTTP status %!l(MISSING)d"
+ "%!s(MISSING): Failed to mark terms as disagreed in iCloud with error %!@(MISSING)"
+ "%!s(MISSING): Marked terms as disagreed in iCloud"
+ "-[SUSSoftwareUpdateTermsManager _handleDisagreeFromObjectModel:]_block_invoke"
+ "AAiCloudTermsDisagreeRequest"
+ "SUSkipMockingKitPIDValidation"
+ "SupportedDeviceNames"
+ "SupportedDevices"
+ "T@\"NSString\",&,N,ScomingSoonTipLearnMoreLink:"
+ "T@\"NSString\",&,N,ScomingSoonTipMessage:"
+ "T@\"NSString\",&,N,ScomingSoonTipTitle:"
+ "TB,N,SisNeRDProfileStatusInstalled:"
+ "TB,N,SshouldBypassSystemRootWarning:"
+ "TB,N,SshouldHideComingSoonTip:"
+ "TB,N,SshouldKeepPreviousMockingKitSession:"
+ "TB,N,SshouldShowComingSoonTip:"
+ "TB,N,SshouldSkipMockingKitPIDValidation:"
+ "UnsupportedDevices"
+ "Whether Mocking Kit test plans sessions should be kept alive after the end of the test execution."
+ "Whether Mocking Kit test plans sessions should be kept bypass the Process ID validation."
+ "_MeasurementAlgorithm"
+ "_OSVersionCompatibilities"
+ "_handleDisagreeFromObjectModel:"
+ "disagreeUrl"
+ "isNeRDProfileStatusInstalled:"
+ "shouldBypassSystemRootWarning:"
+ "shouldHideComingSoonTip:"
+ "shouldKeepPreviousMockingKitSession:"
+ "shouldShowComingSoonTip:"
+ "shouldSkipMockingKitPIDValidation"
+ "shouldSkipMockingKitPIDValidation:"
+ "statusCode"
- "\x01\x13"
- ":"
- "T@\"NSString\",&,N,V_comingSoonTipLearnMoreLink"
- "T@\"NSString\",&,N,V_comingSoonTipMessage"
- "T@\"NSString\",&,N,V_comingSoonTipTitle"
- "TB,N,GisNeRDProfileStatusInstalled,V_isNeRDProfileStatusInstalled"
- "TB,N,GshouldBypassSystemRootWarning,V_bypassSystemRootWarning"
- "TB,N,GshouldHideComingSoonTip,V_hideComingSoonTip"
- "TB,N,GshouldKeepPreviousMockingKitSession,V_keepPreviousMockingKitSession"
- "TB,N,GshouldShowComingSoonTip,V_showComingSoonTip"
- "Whether or not Mocking Kit test plans sessions should be kept alive after the end of the test execution."
- "_bypassSystemRootWarning"
- "_comingSoonTipLearnMoreLink"
- "_comingSoonTipMessage"
- "_comingSoonTipTitle"
- "_hideComingSoonTip"
- "_isNeRDProfileStatusInstalled"
- "_keepPreviousMockingKitSession"
- "_showComingSoonTip"
- "bypassSystemRootWarning"
- "bypassSystemRootWarning:"
- "hideComingSoonTip"
- "hideComingSoonTip:"
- "keepPreviousMockingKitSession"
- "keepPreviousMockingKitSession:"
- "setBypassSystemRootWarning:"
- "setComingSoonTipLearnMoreLink:"
- "setComingSoonTipMessage:"
- "setComingSoonTipTitle:"
- "setHideComingSoonTip:"
- "setIsNeRDProfileStatusInstalled:"
- "setKeepPreviousMockingKitSession:"
- "setShowComingSoonTip:"
- "showComingSoonTip"
- "showComingSoonTip:"

```
