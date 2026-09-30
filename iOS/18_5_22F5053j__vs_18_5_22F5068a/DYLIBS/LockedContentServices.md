## LockedContentServices

> `/System/Library/PrivateFrameworks/LockedContentServices.framework/LockedContentServices`

```diff

-58.4.10.0.0
-  __TEXT.__text: 0xd5fc
-  __TEXT.__auth_stubs: 0x5e0
-  __TEXT.__objc_methlist: 0xeb4
+58.4.10.100.0
+  __TEXT.__text: 0xd768
+  __TEXT.__auth_stubs: 0x5f0
+  __TEXT.__objc_methlist: 0xebc
   __TEXT.__const: 0xe8
-  __TEXT.__gcc_except_tab: 0x318
-  __TEXT.__oslogstring: 0xde5
+  __TEXT.__gcc_except_tab: 0x31c
+  __TEXT.__oslogstring: 0xe9e
   __TEXT.__cstring: 0xa75
   __TEXT.__unwind_info: 0x458
   __TEXT.__objc_classname: 0x344
-  __TEXT.__objc_methname: 0x2d46
-  __TEXT.__objc_methtype: 0x883
-  __TEXT.__objc_stubs: 0x2340
+  __TEXT.__objc_methname: 0x2de3
+  __TEXT.__objc_methtype: 0x8a2
+  __TEXT.__objc_stubs: 0x2360
   __DATA_CONST.__got: 0x258
   __DATA_CONST.__const: 0x5b0
   __DATA_CONST.__objc_classlist: 0x78
   __DATA_CONST.__objc_protolist: 0x90
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0xaf0
+  __DATA_CONST.__objc_selrefs: 0xaf8
   __DATA_CONST.__objc_superrefs: 0x68
-  __AUTH_CONST.__auth_got: 0x300
-  __AUTH_CONST.__const: 0x1a0
+  __AUTH_CONST.__auth_got: 0x308
+  __AUTH_CONST.__const: 0x180
   __AUTH_CONST.__cfstring: 0x900
-  __AUTH_CONST.__objc_const: 0x2e28
+  __AUTH_CONST.__objc_const: 0x2e68
   __AUTH.__objc_data: 0x140
-  __DATA.__objc_ivar: 0xfc
+  __DATA.__objc_ivar: 0x104
   __DATA.__data: 0x6c0
   __DATA.__bss: 0x28
   __DATA_DIRTY.__objc_data: 0x370

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
   Functions: 347
-  Symbols:   1528
-  CStrings:  756
+  Symbols:   1531
+  CStrings:  764
 
Symbols:
+ -[LCSCaptureApplicationMonitor _lock_captureApplicationsFromKnownExtensions:currentCaptureApplications:usingCachedLaunchOptions:]
+ -[LCSCaptureApplicationMonitor _lock_evaluateCaptureApplicationRequirementsForKnownExtensions:usingCachedLaunchOptions:]
+ -[LCSCaptureApplicationMonitor _updateCachedKnownCaptureApplications:]
+ GCC_except_table15
+ _BSDispatchQueueCreateSerialWithQoS
+ _OBJC_IVAR_$_LCSCaptureApplicationMonitor._cache_lock
+ _OBJC_IVAR_$_LCSCaptureApplicationMonitor._lock_cached_knownCaptureApplicationsByBundleIdentifier
+ ___129-[LCSCaptureApplicationMonitor _lock_captureApplicationsFromKnownExtensions:currentCaptureApplications:usingCachedLaunchOptions:]_block_invoke
+ ___block_descriptor_57_e8_32s40s48s_e34_v16?0"<LCSExtensionDescribing>"8ls32l8s40l8s48l8
+ _objc_msgSend$_lock_captureApplicationsFromKnownExtensions:currentCaptureApplications:usingCachedLaunchOptions:
+ _objc_msgSend$_lock_evaluateCaptureApplicationRequirementsForKnownExtensions:usingCachedLaunchOptions:
+ _objc_msgSend$_updateCachedKnownCaptureApplications:
- -[LCSCaptureApplicationMonitor _lock_captureApplicationsFromKnownExtensions:currentCaptureApplications:]
- -[LCSCaptureApplicationMonitor _lock_evaluateCaptureApplicationRequirementsForKnownExtensions:]
- GCC_except_table16
- GCC_except_table24
- ___104-[LCSCaptureApplicationMonitor _lock_captureApplicationsFromKnownExtensions:currentCaptureApplications:]_block_invoke
- ___74-[LCSCaptureApplicationMonitor knownCaptureApplicationsByBundleIdentifier]_block_invoke
- ___block_descriptor_56_e8_32s40s48s_e34_v16?0"<LCSExtensionDescribing>"8ls32l8s40l8s48l8
- ___block_literal_global.32
- _objc_msgSend$_lock_captureApplicationsFromKnownExtensions:currentCaptureApplications:
- _objc_msgSend$_lock_evaluateCaptureApplicationRequirementsForKnownExtensions:
CStrings:
+ "\x18"
+ "@28@0:8@16B24"
+ "@36@0:8@16@24B32"
+ "Capture Application (%@): Cached supported launch type is not found, trying again"
+ "Capture Application (%@): Using cached supported launch type: %@"
+ "Capture Application (%@): appHasCameraUsageDescription: %{BOOL}u; Extension (%@): extensionHasCameraUsageDescription: %{BOOL}u; supportedLaunchOptions: %@, visibilityHidden: %{BOOL}u"
+ "Reevaluating capture application requirements"
+ "_cache_lock"
+ "_lock_cached_knownCaptureApplicationsByBundleIdentifier"
+ "_lock_captureApplicationsFromKnownExtensions:currentCaptureApplications:usingCachedLaunchOptions:"
+ "_lock_evaluateCaptureApplicationRequirementsForKnownExtensions:usingCachedLaunchOptions:"
+ "_updateCachedKnownCaptureApplications:"
- "\x17"
- "Capture Application (%@): appHasCameraUsageDescription: %{BOOL}u; Extension (%@): extensionHasCameraUsageDescription: %{BOOL}u; bundleHasCaptureAppIntent %{BOOL}u, visibilityHidden: %{BOOL}u"
- "_lock_captureApplicationsFromKnownExtensions:currentCaptureApplications:"
- "_lock_evaluateCaptureApplicationRequirementsForKnownExtensions:"

```
