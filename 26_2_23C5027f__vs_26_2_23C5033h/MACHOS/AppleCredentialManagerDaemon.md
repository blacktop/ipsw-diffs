## AppleCredentialManagerDaemon

> `/System/Library/PrivateFrameworks/AppleCredentialManager.framework/AppleCredentialManagerDaemon`

```diff

-864.60.1.0.0
-  __TEXT.__text: 0x1461c
-  __TEXT.__auth_stubs: 0x4c0
-  __TEXT.__objc_stubs: 0x4c0
+864.60.2.502.1
+  __TEXT.__text: 0x14cb8
+  __TEXT.__auth_stubs: 0x4d0
+  __TEXT.__objc_stubs: 0x540
   __TEXT.__objc_methlist: 0x134
-  __TEXT.__objc_methname: 0x3cd
+  __TEXT.__objc_methname: 0x42a
   __TEXT.__objc_classname: 0x2f
   __TEXT.__objc_methtype: 0x92
-  __TEXT.__const: 0x110
-  __TEXT.__cstring: 0x253c
-  __TEXT.__oslogstring: 0x5a8
-  __TEXT.__unwind_info: 0x338
-  __DATA_CONST.__auth_got: 0x268
-  __DATA_CONST.__got: 0x80
+  __TEXT.__const: 0x128
+  __TEXT.__cstring: 0x25f0
+  __TEXT.__oslogstring: 0x6fa
+  __TEXT.__unwind_info: 0x348
+  __DATA_CONST.__auth_got: 0x270
+  __DATA_CONST.__got: 0x88
   __DATA_CONST.__auth_ptr: 0x18
   __DATA_CONST.__const: 0x138
   __DATA_CONST.__cfstring: 0x140

   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_superrefs: 0x10
   __DATA.__objc_const: 0x160
-  __DATA.__objc_selrefs: 0x140
+  __DATA.__objc_selrefs: 0x160
   __DATA.__objc_ivar: 0x4
   __DATA.__objc_data: 0xa0
   __DATA.__data: 0x3

   - /usr/lib/libMobileGestalt.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: F737814F-CB9C-312F-8115-1982E53BF7C0
-  Functions: 423
-  Symbols:   101
-  CStrings:  385
+  UUID: 81B0992B-01DF-33BF-B7F8-1DF59617A973
+  Functions: 426
+  Symbols:   103
+  CStrings:  401
 
Symbols:
+ _MCFeatureUSBRestrictedModeAllowed
+ _os_variant_is_darwinos
CStrings:
+ "%s: %s: %s set MCFeatureUSBRestrictedModeAllowed=%s (oldValue=%s -> newValue=%s, mcUpdatePerformed=%s).\n"
+ "%s: %s: Error %d reported while updating MCFeatureUSBRestrictedModeAllowed=%s: %s.\n"
+ "%s: %s: TRM allowedByManagedConfiguration=%s/%u/%u (willPublish=%s).\n"
+ "%s: %s: TRM switched to AlwaysAllow, reverting MCFeatureUSBRestrictedModeAllowed=NO->YES.\n"
+ "%s: %s: acmd started, handing control over to kext (allowedByManagedConfiguration=%s/%u/%u disabledByAppleSetup=%s isInternalBuild=%s isUSBTypeCSupported=%s switchToAlwaysAllow=%s).\n"
+ "%s: %s: darwinOS detected, TRM allowed.\n"
+ "<NULL>"
+ "Failed to"
+ "Successfully"
+ "code"
+ "com.apple.AppleCredentialManagerDaemon"
+ "description"
+ "errorCheckedSetBoolValue:forSetting:"
+ "isBoolSettingLockedDownByRestrictions:"
+ "isDisabledByManagedProfile"
+ "isDisabledByManagedState"
+ "mcIsUSBRestrictedModeAllowed"
+ "mcSetUSBRestrictedModeAllowed"
- "%s: %s: TRM allowed by ManagedConfiguration: %s (willPublish=%s).\n"
- "%s: %s: acmd started, handing control over to kext (TRM allowed by ManagedConfiguration: %s, disabled by AppleSetup: %s, isInternalBuild: %s, isUSBTypeCSupported: %s).\n"

```
