## libauthinstall.dylib

> `/usr/lib/libauthinstall.dylib`

```diff

 1104.80.2.0.0
-  __TEXT.__text: 0x9c1e8
+  __TEXT.__text: 0x9c288
   __TEXT.__auth_stubs: 0x1930
   __TEXT.__objc_methlist: 0x27f4
-  __TEXT.__cstring: 0x1ee84
+  __TEXT.__cstring: 0x1eed9
   __TEXT.__const: 0x6346
   __TEXT.__oslogstring: 0x53c
   __TEXT.__gcc_except_tab: 0x35e4

   __DATA_CONST.__objc_superrefs: 0x1f8
   __DATA_CONST.__objc_arraydata: 0x10
   __AUTH_CONST.__auth_got: 0xcb0
-  __AUTH_CONST.__const: 0x13c8
-  __AUTH_CONST.__cfstring: 0xede0
+  __AUTH_CONST.__const: 0x13f8
+  __AUTH_CONST.__cfstring: 0xee20
   __AUTH_CONST.__objc_const: 0x4c18
   __AUTH_CONST.__objc_dictobj: 0x28
   __AUTH_CONST.__objc_intobj: 0x78

   - /usr/lib/updaters/libAppleTconUARPUpdater.dylib
   - /usr/lib/updaters/libSavageRestoreInfo_iOS.dylib
   - /usr/lib/updaters/libT200Updater.dylib
-  UUID: CB6AE046-55DE-3164-9F48-4470D97B2B7D
+  UUID: 2ABCDD2B-737F-3598-BAB6-FB92FF7C8802
   Functions: 3273
-  Symbols:   9404
-  CStrings:  7275
+  Symbols:   9407
+  CStrings:  7280
 
Symbols:
+ _BanyanUARPRestoreInfoCopyFirmware
+ _BanyanUARPRestoreInfoCreateRequest
+ _BanyanUARPRestoreInfoGetTags
Functions:
~ __AMAuthInstallUpdaterSetInfoWithUARPCallbacks : 3064 -> 3216
~ _AMAuthInstallUpdaterSetInfoWithCallbacks : 76 -> 80
~ _AMAuthInstallUpdaterSetInfoWithUARPCallbacks : 80 -> 84
CStrings:
+ "%@ updater queryPersonalizationInfo call failed, error=%@"
+ "Banyan"
+ "PersonalizationInfo"
+ "VinylRestore-144~8262"
- "VinylRestore-144~8228"

```
