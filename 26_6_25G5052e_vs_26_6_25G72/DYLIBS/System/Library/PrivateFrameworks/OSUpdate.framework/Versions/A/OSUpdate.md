## OSUpdate

> `/System/Library/PrivateFrameworks/OSUpdate.framework/Versions/A/OSUpdate`

### Sections with Same Size but Changed Content

- `__TEXT.__gcc_except_tab`
- `__DATA_CONST.__const`
- `__DATA_CONST.__objc_catlist`
- `__DATA_CONST.__objc_protolist`
- `__DATA_CONST.__objc_protorefs`
- `__DATA_CONST.__objc_arraydata`
- `__AUTH_CONST.__const`
- `__AUTH_CONST.__cfstring`
- `__AUTH_CONST.__objc_arrayobj`
- `__AUTH_CONST.__objc_intobj`
- `__AUTH_CONST.__objc_dictobj`
- `__DATA.__data`
- `__DATA_DIRTY.__objc_data`

```diff

-2219.160.7.0.0
-  __TEXT.__text: 0x9d2ec
+2219.160.9.0.0
+  __TEXT.__text: 0x9e138
   __TEXT.__auth_stubs: 0xb70
-  __TEXT.__objc_methlist: 0x79ec
+  __TEXT.__objc_methlist: 0x7a5c
   __TEXT.__const: 0x1f1
-  __TEXT.__cstring: 0x8203
-  __TEXT.__oslogstring: 0xd7c4
+  __TEXT.__cstring: 0x81fe
+  __TEXT.__oslogstring: 0xdc7c
   __TEXT.__gcc_except_tab: 0x1e84
   __TEXT.__ustring: 0xc
-  __TEXT.__unwind_info: 0x20d8
-  __TEXT.__objc_classname: 0x93b
-  __TEXT.__objc_methname: 0x1715b
-  __TEXT.__objc_methtype: 0x22ee
-  __TEXT.__objc_stubs: 0xf500
-  __DATA_CONST.__got: 0xa78
+  __TEXT.__unwind_info: 0x20f0
+  __TEXT.__objc_classname: 0x951
+  __TEXT.__objc_methname: 0x1725b
+  __TEXT.__objc_methtype: 0x231b
+  __TEXT.__objc_stubs: 0xf560
+  __DATA_CONST.__got: 0xa80
   __DATA_CONST.__const: 0xd50
-  __DATA_CONST.__objc_classlist: 0x270
+  __DATA_CONST.__objc_classlist: 0x278
   __DATA_CONST.__objc_catlist: 0x10
   __DATA_CONST.__objc_protolist: 0x80
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x4ac0
+  __DATA_CONST.__objc_selrefs: 0x4ae0
   __DATA_CONST.__objc_protorefs: 0x20
-  __DATA_CONST.__objc_superrefs: 0x1d0
+  __DATA_CONST.__objc_superrefs: 0x1d8
   __DATA_CONST.__objc_arraydata: 0x698
   __AUTH_CONST.__auth_got: 0x5c8
   __AUTH_CONST.__const: 0x2d20
   __AUTH_CONST.__cfstring: 0x6140
-  __AUTH_CONST.__objc_const: 0x9da8
+  __AUTH_CONST.__objc_const: 0x9ea8
   __AUTH_CONST.__objc_arrayobj: 0x60
   __AUTH_CONST.__objc_intobj: 0x198
   __AUTH_CONST.__objc_dictobj: 0x190
-  __AUTH.__objc_data: 0xcd0
-  __DATA.__objc_ivar: 0x760
+  __AUTH.__objc_data: 0xd20
+  __DATA.__objc_ivar: 0x768
   __DATA.__data: 0x612
   __DATA.__bss: 0x60
   __DATA_DIRTY.__objc_data: 0xb90

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libbootpolicy.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 3323
-  Symbols:   7176
-  CStrings:  5803
+  Functions: 3331
+  Symbols:   7197
+  CStrings:  5830
 
Symbols:
+ -[SUOSUAutoUpdatePolicy .cxx_destruct]
+ -[SUOSUAutoUpdatePolicy deviceStateAllowsAutoUpdateWithUpdateController:client:restartCountdownIsOngoing:]
+ -[SUOSUAutoUpdatePolicy initWithSharedPrefs:]
+ -[SUOSUAutoUpdatePolicy isProductEligibleForAutoUpdate:]
+ -[SUOSUAutoUpdatePolicy productsEligibleForAutoUpdateFromProducts:]
+ -[SUOSUAutoUpdatePolicy setSharedPrefs:]
+ -[SUOSUAutoUpdatePolicy sharedPrefs]
+ -[SUOSUBackgroundDownloadEvaluator autoUpdatePolicy]
+ -[SUOSUBackgroundDownloadEvaluator initWithBackgroundDownloadsEnabled:splatEnabled:productKeysToAutoInstall:autoUpdatePolicy:]
+ OBJC_IVAR_$_SUOSUAutoUpdatePolicy._sharedPrefs
+ OBJC_IVAR_$_SUOSUBackgroundDownloadEvaluator._autoUpdatePolicy
+ _OBJC_CLASS_$_SUOSUAutoUpdatePolicy
+ _OBJC_METACLASS_$_SUOSUAutoUpdatePolicy
+ _OUTLINED_FUNCTION_31
+ __OBJC_$_INSTANCE_METHODS_SUOSUAutoUpdatePolicy
+ __OBJC_$_INSTANCE_VARIABLES_SUOSUAutoUpdatePolicy
+ __OBJC_$_PROP_LIST_SUOSUAutoUpdatePolicy
+ __OBJC_CLASS_RO_$_SUOSUAutoUpdatePolicy
+ __OBJC_METACLASS_RO_$_SUOSUAutoUpdatePolicy
+ _objc_msgSend$autoUpdatePolicy
+ _objc_msgSend$foregroundMobileSoftwareUpdateInProgress
+ _objc_msgSend$initWithBackgroundDownloadsEnabled:splatEnabled:productKeysToAutoInstall:autoUpdatePolicy:
+ _objc_msgSend$isProductEligibleForAutoUpdate:
- -[SUOSUBackgroundDownloadEvaluator initWithBackgroundDownloadsEnabled:splatEnabled:productKeysToAutoInstall:]
- _objc_msgSend$initWithBackgroundDownloadsEnabled:splatEnabled:productKeysToAutoInstall:
CStrings:
+ "%@: %@ is configured to auto-install-tonight."
+ "%@: %@ is eligible for auto update."
+ "%@: %@ is not eligible because it's an IA-based major update."
+ "%@: %@ is not eligible for auto update because auto update is disabled."
+ "%@: %@ is not eligible for auto update because automatic splat updates are disabled."
+ "%@: %@ is not eligible for auto update because automatic updates are disabled."
+ "%@: %@ is not eligible for auto update because it's a revoked splat."
+ "%@: %@ is not eligible for auto update because it's ramped."
+ "%@: Don't proceed with auto update b/c a foreground update is already in progress"
+ "%@: Don't proceed with auto update b/c a restart countdown operation is ongoing"
+ "%@: Don't proceed with auto update b/c already armed for later"
+ "%@: Don't proceed with auto update b/c managed updates are scheduled"
+ "%@: Don't proceed with auto update b/c no stashed keybag exists."
+ "%@: Don't proceed with auto update b/c setup assistant is active"
+ "%@: Don't proceed with auto update b/c updates are not downloaded yet"
+ "%@: First attempted overnight install of %@ on %@ and is now ineligible."
+ "%@: Only the minor update will auto-install, preferring it over the major for background download."
+ "%@: Splat is already applied: %@"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.2BQrQO/Sources/AppleCredentialManager_ClientLibs/ACMLib/ACMLib.c"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.2BQrQO/Sources/AppleCredentialManager_ClientLibs/common/LibCall.c"
+ "@\"SUOSUAutoUpdatePolicy\""
+ "@40@0:8B16B20@24@32"
+ "B36@0:8@16@24B32"
+ "SUOSUAutoUpdatePolicy"
+ "T@\"SUOSUAutoUpdatePolicy\",R,V_autoUpdatePolicy"
+ "_autoUpdatePolicy"
+ "autoUpdatePolicy"
+ "deviceStateAllowsAutoUpdateWithUpdateController:client:restartCountdownIsOngoing:"
+ "initWithBackgroundDownloadsEnabled:splatEnabled:productKeysToAutoInstall:autoUpdatePolicy:"
+ "isProductEligibleForAutoUpdate:"
+ "macOS Tahoe"
+ "productsEligibleForAutoUpdateFromProducts:"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.HwY5nz/Sources/AppleCredentialManager_ClientLibs/ACMLib/ACMLib.c"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.HwY5nz/Sources/AppleCredentialManager_ClientLibs/common/LibCall.c"
- "@32@0:8B16B20@24"
- "initWithBackgroundDownloadsEnabled:splatEnabled:productKeysToAutoInstall:"
- "macOS Tahoe Beta"
```
