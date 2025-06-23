## libauthinstall.dylib

> `/usr/lib/libauthinstall.dylib`

```diff

-1104.0.0.0.1
-  __TEXT.__text: 0x9863c
+1104.0.3.0.0
+  __TEXT.__text: 0x9848c
   __TEXT.__auth_stubs: 0x1920
   __TEXT.__objc_methlist: 0x27f4
-  __TEXT.__cstring: 0x1db43
+  __TEXT.__cstring: 0x1da7a
   __TEXT.__const: 0x6316
   __TEXT.__oslogstring: 0x53c
   __TEXT.__gcc_except_tab: 0x33c8
-  __TEXT.__unwind_info: 0x26b0
+  __TEXT.__unwind_info: 0x26a8
   __TEXT.__objc_classname: 0x8a8
   __TEXT.__objc_methname: 0x2923
   __TEXT.__objc_methtype: 0x776

   __DATA_CONST.__objc_arraydata: 0x10
   __AUTH_CONST.__auth_got: 0xca8
   __AUTH_CONST.__const: 0x1340
-  __AUTH_CONST.__cfstring: 0xe500
+  __AUTH_CONST.__cfstring: 0xe4e0
   __AUTH_CONST.__objc_const: 0x4c18
   __AUTH_CONST.__objc_dictobj: 0x28
   __AUTH_CONST.__objc_intobj: 0x78

   __AUTH.__data: 0x20
   __DATA.__objc_ivar: 0x328
   __DATA.__data: 0x928
-  __DATA.__bss: 0xd90
+  __DATA.__bss: 0xd88
   __DATA.__common: 0x10
   __DATA_DIRTY.__data: 0x38
   __DATA_DIRTY.__bss: 0x18

   - /usr/lib/libz.1.dylib
   - /usr/lib/updaters/libSavageRestoreInfo_iOS.dylib
   - /usr/lib/updaters/libT200Updater.dylib
-  UUID: 0C0945B8-979C-3EA4-8DAC-8B3F3048365F
-  Functions: 3176
-  Symbols:   9129
-  CStrings:  7007
+  UUID: 62FB6DDE-B745-3F52-BC34-E18FF9F26C72
+  Functions: 3174
+  Symbols:   9124
+  CStrings:  6998
 
Symbols:
+ _AMSupportPlatformCopyURLToNewTempDirectory
+ _AMSupportPlatformGetURLForTempDirectoryRoot
- _AMAuthInstallPlatformGetURLForTempDirectoryRoot
- _CFURLCreateFromFileSystemRepresentation
- __AMAuthInstallPlatformConstantsInitialize.cold.1
- __tempDirURL
- _mkdtemp
Functions:
- _AMAuthInstallPlatformCopyURLToNewTempDirectory
~ __AMAuthInstallPlatformConstantsInitialize : 316 -> 264
- _AMAuthInstallPlatformGetPlatformInfoString
+ _AMAuthInstallSupportGetURLForTempDirectoryRoot
- __AMAuthInstallPlatformConstantsInitialize.cold.1
CStrings:
+ "HelsinkiRestore-57.1.25"
+ "VinylRestore-144~127"
+ "libauthinstall_device-1104.0.3"
- "/tmp"
- "/tmp/%s"
- "AMAuthInstallPlatform.c"
- "AMAuthInstallPlatformCopyURLToNewTempDirectory"
- "HelsinkiRestore-57.1.22"
- "VinylRestore-143~561"
- "_AMAuthInstallPlatformTempDirURLInitialize"
- "_tempDirURL != NULL"
- "failed to create tmp dir: %s"
- "libauthinstall_device-1104.0.0.0.1"
- "tmp dir template: %s"

```
