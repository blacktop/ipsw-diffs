## OSUpdate

> `/System/Library/PrivateFrameworks/OSUpdate.framework/Versions/A/OSUpdate`

### Sections with Same Size but Changed Content

- `__TEXT.__cstring`
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

-2412.0.2.0.0
-  __TEXT.__text: 0x91e24
-  __TEXT.__objc_methlist: 0x7b2c
+2412.0.5.0.0
+  __TEXT.__text: 0x92b08
+  __TEXT.__objc_methlist: 0x7b9c
   __TEXT.__const: 0x1f1
   __TEXT.__cstring: 0x8102
-  __TEXT.__oslogstring: 0xd74e
+  __TEXT.__oslogstring: 0xdc19
   __TEXT.__gcc_except_tab: 0x1b54
   __TEXT.__ustring: 0xc
-  __TEXT.__unwind_info: 0x2008
+  __TEXT.__unwind_info: 0x2018
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0
   __TEXT.__objc_classname: 0x0
   __TEXT.__objc_methname: 0x0
   __TEXT.__objc_methtype: 0x0
   __DATA_CONST.__const: 0xd68
-  __DATA_CONST.__objc_classlist: 0x278
+  __DATA_CONST.__objc_classlist: 0x280
   __DATA_CONST.__objc_catlist: 0x10
   __DATA_CONST.__objc_protolist: 0x80
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x4b08
+  __DATA_CONST.__objc_selrefs: 0x4b28
   __DATA_CONST.__objc_protorefs: 0x20
-  __DATA_CONST.__objc_superrefs: 0x1d8
+  __DATA_CONST.__objc_superrefs: 0x1e0
   __DATA_CONST.__objc_arraydata: 0x6f8
-  __DATA_CONST.__got: 0xa50
+  __DATA_CONST.__got: 0xa58
   __AUTH_CONST.__const: 0x2d00
   __AUTH_CONST.__cfstring: 0x6100
-  __AUTH_CONST.__objc_const: 0xa000
+  __AUTH_CONST.__objc_const: 0xa100
   __AUTH_CONST.__objc_arrayobj: 0x60
   __AUTH_CONST.__objc_intobj: 0x198
   __AUTH_CONST.__objc_dictobj: 0x190
   __AUTH_CONST.__auth_got: 0x5e0
-  __AUTH.__objc_data: 0xbe0
-  __DATA.__objc_ivar: 0x780
+  __AUTH.__objc_data: 0xc30
+  __DATA.__objc_ivar: 0x788
   __DATA.__data: 0x612
   __DATA.__bss: 0x48
   __DATA_DIRTY.__objc_data: 0xcd0

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libbootpolicy.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 3342
-  Symbols:   7207
-  CStrings:  2221
+  Functions: 3350
+  Symbols:   7226
+  CStrings:  2239
 
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
- _OUTLINED_FUNCTION_19
- _objc_msgSend$initWithBackgroundDownloadsEnabled:splatEnabled:productKeysToAutoInstall:
CStrings:
+ "%@: %@ is configured to auto-install-tonight."
+ "%@: %@ is eligible for auto update."
+ "%@: %@ is not eligible because it's an IA-based major update."
+ "%@: %@ is not eligible for auto update because automatic splat updates are disabled."
+ "%@: %@ is not eligible for auto update because automatic updates are disabled."
+ "%@: %@ is not eligible for auto update because it's a revoked splat."
+ "%@: %@ is not eligible for auto update because it's disabled server-side for this product."
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
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.j7jzB6/Sources/AppleCredentialManager_ClientLibs/ACMLib/ACMLib.c"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.j7jzB6/Sources/AppleCredentialManager_ClientLibs/common/LibCall.c"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.wifYPg/Sources/AppleCredentialManager_ClientLibs/ACMLib/ACMLib.c"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.wifYPg/Sources/AppleCredentialManager_ClientLibs/common/LibCall.c"
```
