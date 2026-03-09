## libauthinstall.dylib

> `/usr/lib/libauthinstall.dylib`

```diff

 1104.100.23.0.0
-  __TEXT.__text: 0x9b1f8
+  __TEXT.__text: 0x9b298
   __TEXT.__auth_stubs: 0x1920
   __TEXT.__objc_methlist: 0x27f4
-  __TEXT.__cstring: 0x1f03e
+  __TEXT.__cstring: 0x1f093
   __TEXT.__const: 0x6416
   __TEXT.__oslogstring: 0x53c
   __TEXT.__gcc_except_tab: 0x365c

   __DATA_CONST.__objc_superrefs: 0x1f8
   __DATA_CONST.__objc_arraydata: 0x10
   __AUTH_CONST.__auth_got: 0xca8
-  __AUTH_CONST.__const: 0x1468
-  __AUTH_CONST.__cfstring: 0xee40
+  __AUTH_CONST.__const: 0x1498
+  __AUTH_CONST.__cfstring: 0xee80
   __AUTH_CONST.__objc_const: 0x4c18
   __AUTH_CONST.__objc_dictobj: 0x28
   __AUTH_CONST.__objc_intobj: 0x78

   - /usr/lib/updaters/libAppleTconUARPUpdater.dylib
   - /usr/lib/updaters/libSavageRestoreInfo_iOS.dylib
   - /usr/lib/updaters/libT200Updater.dylib
-  UUID: 078CA34E-C258-328A-B4B6-B9D08761BB98
+  UUID: 376698E1-B0BC-3933-802C-689DFE4058ED
   Functions: 3556
-  Symbols:   10022
-  CStrings:  7301
+  Symbols:   10025
+  CStrings:  7306
 
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
+ "VinylRestore-146~719"
- "VinylRestore-146~629"

```
