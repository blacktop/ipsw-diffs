## SoftwareUpdateNotificationManager

> `/System/Library/PrivateFrameworks/SoftwareUpdate.framework/Versions/A/Resources/SoftwareUpdateNotificationManager.app/Contents/MacOS/SoftwareUpdateNotificationManager`

### Sections with Same Size but Changed Content

- `__DATA_CONST.__const`
- `__DATA_CONST.__cfstring`
- `__DATA_CONST.__objc_protolist`
- `__DATA_CONST.__objc_protorefs`
- `__DATA_CONST.__objc_intobj`
- `__DATA_CONST.__objc_dictobj`
- `__DATA_CONST.__auth_ptr`
- `__DATA.__data`

```diff

-2412.0.2.0.0
-  __TEXT.__text: 0x22d48
+2412.0.5.0.0
+  __TEXT.__text: 0x220f4
   __TEXT.__auth_stubs: 0x3c0
-  __TEXT.__objc_stubs: 0x5300
-  __TEXT.__objc_methlist: 0x1c8c
+  __TEXT.__objc_stubs: 0x51a0
+  __TEXT.__objc_methlist: 0x1bfc
   __TEXT.__const: 0x108
   __TEXT.__gcc_except_tab: 0x554
-  __TEXT.__cstring: 0x2a09
-  __TEXT.__objc_methname: 0x7001
-  __TEXT.__oslogstring: 0x352e
-  __TEXT.__objc_classname: 0x2dd
-  __TEXT.__objc_methtype: 0xfeb
-  __TEXT.__unwind_info: 0x610
+  __TEXT.__cstring: 0x2a07
+  __TEXT.__objc_methname: 0x6ea2
+  __TEXT.__oslogstring: 0x30c6
+  __TEXT.__objc_classname: 0x2c7
+  __TEXT.__objc_methtype: 0xfda
+  __TEXT.__unwind_info: 0x5f0
   __DATA_CONST.__const: 0x8a8
   __DATA_CONST.__cfstring: 0x1fe0
-  __DATA_CONST.__objc_classlist: 0x78
+  __DATA_CONST.__objc_classlist: 0x70
   __DATA_CONST.__objc_catlist: 0x18
   __DATA_CONST.__objc_protolist: 0x50
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_protorefs: 0x8
-  __DATA_CONST.__objc_superrefs: 0x50
+  __DATA_CONST.__objc_superrefs: 0x48
   __DATA_CONST.__objc_intobj: 0x90
   __DATA_CONST.__objc_arraydata: 0x50
   __DATA_CONST.__objc_dictobj: 0x78
   __DATA_CONST.__auth_got: 0x1f0
-  __DATA_CONST.__got: 0x7e8
+  __DATA_CONST.__got: 0x7e0
   __DATA_CONST.__auth_ptr: 0x8
-  __DATA.__objc_const: 0x2278
-  __DATA.__objc_selrefs: 0x1a28
-  __DATA.__objc_ivar: 0x170
-  __DATA.__objc_data: 0x4b0
+  __DATA.__objc_const: 0x2148
+  __DATA.__objc_selrefs: 0x19c8
+  __DATA.__objc_ivar: 0x164
+  __DATA.__objc_data: 0x460
   __DATA.__data: 0x3c0
   __DATA.__bss: 0x60
   __DATA.__common: 0x8

   - /usr/lib/libIASUnifiedProgress.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 628
-  Symbols:   325
-  CStrings:  1751
+  Functions: 617
+  Symbols:   324
+  CStrings:  1717
 
Symbols:
+ _OBJC_CLASS_$_SUOSUAutoUpdatePolicy
- _OBJC_CLASS_$_SUUtilities
- _kAutoUpdatePolicyUpdateEligibilityPeriod
CStrings:
+ "deviceStateAllowsAutoUpdateWithUpdateController:client:restartCountdownIsOngoing:"
+ "initWithSharedPrefs:"
- "%@: %@ is configured to auto-install-tonight."
- "%@: %@ is eligible for auto update."
- "%@: %@ is not eligible because it's an IA-based major update."
- "%@: %@ is not eligible for auto update because automatic splat updates are disabled."
- "%@: %@ is not eligible for auto update because automatic updates are disabled."
- "%@: %@ is not eligible for auto update because it's a revoked splat."
- "%@: %@ is not eligible for auto update because it's disabled server-side for this product."
- "%@: %@ is not eligible for auto update because it's ramped."
- "%@: Don't proceed with auto update b/c a foreground update is already in progress"
- "%@: Don't proceed with auto update b/c a restart countdown operation is ongoing"
- "%@: Don't proceed with auto update b/c already armed for later"
- "%@: Don't proceed with auto update b/c managed updates are scheduled"
- "%@: Don't proceed with auto update b/c no stashed keybag exists."
- "%@: Don't proceed with auto update b/c setup assistant is active"
- "%@: Don't proceed with auto update b/c updates are not downloaded yet"
- "%@: First attempted overnight install of %@ on %@ and is now ineligible."
- "%@: Splat is already applied: %@"
- "@\"SUSharedPrefs\""
- "SUOSUAutoUpdatePolicy"
- "T@\"SUOSUClient\",&,V_client"
- "T@\"SUSharedPrefs\",&,V_sharedPrefs"
- "_isProductEligibleForAutoUpdate:"
- "_sharedPrefs"
- "deviceStateAllowsAutoUpdate"
- "doesMacOSAutoUpdate"
- "firstInstallTonightDateForProductKey:"
- "foregroundMobileSoftwareUpdateInProgress"
- "initWithSharedPrefs:updateController:client:"
- "isAutoUpdateEligible"
- "isRamped"
- "managedInstallLaterUpdatesScheduled"
- "mobileKeyBagStashStateForUser:"
- "productKeysToAutoInstall"
- "setSharedPrefs:"
- "sharedPrefs"
- "uidFromCurrentAuditToken"
```
