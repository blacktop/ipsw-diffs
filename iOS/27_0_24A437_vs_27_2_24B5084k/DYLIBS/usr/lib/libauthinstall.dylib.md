## libauthinstall.dylib

> `/usr/lib/libauthinstall.dylib`

### Sections with Same Size but Changed Content

- `__TEXT.__cstring`

```diff

-1155.0.5.0.0
-  __TEXT.__text: 0xb7864
+1155.40.6.0.0
+  __TEXT.__text: 0xb78b0
   __TEXT.__objc_methlist: 0x2a64
   __TEXT.__cstring: 0x1ff77
   __TEXT.__const: 0x653c

   __DATA_CONST.__objc_selrefs: 0xd70
   __DATA_CONST.__objc_superrefs: 0x1f8
   __DATA_CONST.__objc_arraydata: 0x10
-  __DATA_CONST.__got: 0x410
+  __DATA_CONST.__got: 0x418
   __AUTH_CONST.__const: 0x15c0
   __AUTH_CONST.__cfstring: 0xfb40
   __AUTH_CONST.__objc_const: 0x4fd8

   - /usr/lib/updaters/libSavageRestoreInfo_iOS.dylib
   - /usr/lib/updaters/libT200Updater.dylib
   Functions: 3807
-  Symbols:   5314
+  Symbols:   5315
   CStrings:  4746
 
Symbols:
+ _kAMSupportHttpOptionRequestHTTPAllowed
Functions:
~ _AMAuthInstallApFinalize : 264 -> 288
~ _AMAuthInstallUpdaterPersonalize : 772 -> 796
~ _tss_submit_job_with_retry : 1836 -> 1876
~ _SEUpdaterGetTags : 2212 -> 2200
CStrings:
+ "HelsinkiRestore-58.1.4"
+ "VinylRestore-178~8275"
+ "libauthinstall_device-1155.40.6"
- "HelsinkiRestore-58.0.45"
- "VinylRestore-178~7453"
- "libauthinstall_device-1155.0.5"
```
