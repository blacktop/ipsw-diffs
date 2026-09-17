## libauthinstall.dylib

> `/usr/lib/libauthinstall.dylib`

### Sections with Same Size but Changed Content

- `__TEXT.__cstring`

```diff

-1155.0.5.0.0
-  __TEXT.__text: 0xaffdc
+1155.40.6.0.0
+  __TEXT.__text: 0xb0050
   __TEXT.__objc_methlist: 0x262c
   __TEXT.__cstring: 0x21a53
   __TEXT.__const: 0xc2c1

   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__weak_got: 0x10
   __DATA_CONST.__objc_selrefs: 0xbf8
-  __DATA_CONST.__got: 0x180
+  __DATA_CONST.__got: 0x188
   __AUTH_CONST.__const: 0x1630
   __AUTH_CONST.__cfstring: 0xf120
   __AUTH_CONST.__objc_const: 0x4908

   - /usr/lib/updaters/libAppleTconUARPUpdater.dylib
   - /usr/lib/updaters/libT200Updater.dylib
   Functions: 3824
-  Symbols:   5423
+  Symbols:   5424
   CStrings:  4817
 
Symbols:
+ _kAMSupportHttpOptionRequestHTTPAllowed
Functions:
~ _AMAuthInstallApFinalize : 264 -> 288
~ _AMAuthInstallUpdaterPersonalize : 772 -> 796
~ _tss_submit_job_with_retry : 1800 -> 1868
CStrings:
+ "Helsinki_Restore_Host-58.1.4"
+ "libauthinstall-1155.40.6"
- "Helsinki_Restore_Host-58.0.45"
- "libauthinstall-1155.0.5"
```
