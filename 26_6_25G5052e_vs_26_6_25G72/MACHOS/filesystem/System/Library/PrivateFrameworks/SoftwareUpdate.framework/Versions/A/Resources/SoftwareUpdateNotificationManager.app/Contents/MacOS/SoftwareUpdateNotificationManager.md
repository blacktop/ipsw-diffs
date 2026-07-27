## SoftwareUpdateNotificationManager

> `/System/Library/PrivateFrameworks/SoftwareUpdate.framework/Versions/A/Resources/SoftwareUpdateNotificationManager.app/Contents/MacOS/SoftwareUpdateNotificationManager`

### Sections with Same Size but Changed Content

- `__DATA_CONST.__auth_ptr`
- `__DATA_CONST.__const`
- `__DATA_CONST.__cfstring`
- `__DATA_CONST.__objc_protolist`
- `__DATA_CONST.__objc_protorefs`
- `__DATA_CONST.__objc_intobj`
- `__DATA_CONST.__objc_arraydata`
- `__DATA_CONST.__objc_dictobj`
- `__DATA.__data`

```diff

-2219.160.7.0.0
-  __TEXT.__text: 0x24cbc
+2219.160.9.0.0
+  __TEXT.__text: 0x23f88
   __TEXT.__auth_stubs: 0x3b0
-  __TEXT.__objc_stubs: 0x5140
-  __TEXT.__objc_methlist: 0x1bf4
+  __TEXT.__objc_stubs: 0x5000
+  __TEXT.__objc_methlist: 0x1b64
   __TEXT.__const: 0x108
   __TEXT.__gcc_except_tab: 0x690
   __TEXT.__cstring: 0x28ea
-  __TEXT.__objc_methname: 0x6ed2
-  __TEXT.__oslogstring: 0x33c5
-  __TEXT.__objc_classname: 0x2c7
-  __TEXT.__objc_methtype: 0xfeb
-  __TEXT.__unwind_info: 0x660
+  __TEXT.__objc_methname: 0x6d84
+  __TEXT.__oslogstring: 0x2f70
+  __TEXT.__objc_classname: 0x2af
+  __TEXT.__objc_methtype: 0xfda
+  __TEXT.__unwind_info: 0x648
   __DATA_CONST.__auth_got: 0x1e8
-  __DATA_CONST.__got: 0x7b0
+  __DATA_CONST.__got: 0x7a8
   __DATA_CONST.__auth_ptr: 0x8
   __DATA_CONST.__const: 0x868
   __DATA_CONST.__cfstring: 0x1f00
-  __DATA_CONST.__objc_classlist: 0x68
+  __DATA_CONST.__objc_classlist: 0x60
   __DATA_CONST.__objc_catlist: 0x18
   __DATA_CONST.__objc_protolist: 0x50
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_protorefs: 0x8
-  __DATA_CONST.__objc_superrefs: 0x50
+  __DATA_CONST.__objc_superrefs: 0x48
   __DATA_CONST.__objc_intobj: 0x90
   __DATA_CONST.__objc_arraydata: 0x50
   __DATA_CONST.__objc_dictobj: 0x78
-  __DATA.__objc_const: 0x20d0
-  __DATA.__objc_selrefs: 0x19b8
-  __DATA.__objc_ivar: 0x168
-  __DATA.__objc_data: 0x410
+  __DATA.__objc_const: 0x1fa0
+  __DATA.__objc_selrefs: 0x1960
+  __DATA.__objc_ivar: 0x15c
+  __DATA.__objc_data: 0x3c0
   __DATA.__data: 0x3c0
   __DATA.__bss: 0x40
   __DATA.__common: 0x8

   - /usr/lib/libIASUnifiedProgress.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 614
-  Symbols:   319
-  CStrings:  1712
+  Functions: 603
+  Symbols:   318
+  CStrings:  1679
 
Symbols:
+ _OBJC_CLASS_$_SUOSUAutoUpdatePolicy
- _OBJC_CLASS_$_SUUtilities
- _kAutoUpdatePolicyUpdateEligibilityPeriod
CStrings:
+ "arrayWithObject:"
+ "deviceStateAllowsAutoUpdateWithUpdateController:client:restartCountdownIsOngoing:"
+ "initWithSharedPrefs:"
- "%@: %@ is configured to auto-install-tonight."
- "%@: %@ is eligible for auto update."
- "%@: %@ is not eligible because it's an IA-based major update."
- "%@: %@ is not eligible for auto update because auto update is disabled."
- "%@: %@ is not eligible for auto update because automatic splat updates are disabled."
- "%@: %@ is not eligible for auto update because automatic updates are disabled."
- "%@: %@ is not eligible for auto update because it's a revoked splat."
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
