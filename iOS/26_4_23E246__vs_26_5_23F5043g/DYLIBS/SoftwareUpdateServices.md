## SoftwareUpdateServices

> `/System/Library/PrivateFrameworks/SoftwareUpdateServices.framework/SoftwareUpdateServices`

```diff

-950.102.1.0.0
-  __TEXT.__text: 0xc3960
+950.120.3.0.0
+  __TEXT.__text: 0xc3988
   __TEXT.__auth_stubs: 0xe40
   __TEXT.__objc_methlist: 0xb4f4
-  __TEXT.__const: 0x338
-  __TEXT.__cstring: 0x23a08
+  __TEXT.__const: 0x330
+  __TEXT.__cstring: 0x23a92
   __TEXT.__gcc_except_tab: 0x12c0
   __TEXT.__oslogstring: 0x85d
   __TEXT.__unwind_info: 0x36b0

   __DATA_CONST.__objc_arraydata: 0xa0
   __AUTH_CONST.__auth_got: 0x730
   __AUTH_CONST.__const: 0x7e0
-  __AUTH_CONST.__cfstring: 0x14d80
+  __AUTH_CONST.__cfstring: 0x14dc0
   __AUTH_CONST.__objc_const: 0x163a8
   __AUTH_CONST.__objc_intobj: 0x4c8
   __AUTH_CONST.__objc_dictobj: 0x78

   - /usr/lib/libc++.1.dylib
   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libz.1.dylib
-  UUID: 7F28B3FD-5F98-37B7-8835-E081E18B7652
+  UUID: 88922EE2-86A0-3278-ABBF-0F76934C8881
   Functions: 4698
   Symbols:   15571
-  CStrings:  10894
+  CStrings:  10899
 
Symbols:
+ ___block_literal_global.598
+ ___block_literal_global.649
+ ___block_literal_global.691
- ___block_literal_global.646
- ___block_literal_global.688
Functions:
~ sub_2749f177c -> sub_275d6e77c : 316 -> 344
~ -[SUManagerCore(Analytics) donateSUErrorToBiome:] : 228 -> 252
~ +[SUUtility translateErrorCodeFromError:] : 760 -> 804
~ +[SUUtility internalRecoveryStringForErrorCode:] : 688 -> 692
~ +[SUUtility autoDownloadTimeInterval] : 224 -> 188
~ -[SUDownloader _downloadFailedWithError:] : 1184 -> 1160
CStrings:
+ "%s: donating error to Biome: %@"
+ "-[SUManagerCore(Analytics) donateSUErrorToBiome:]"
+ "Battery level too low; charge the device and try again later"
+ "[Auto download] Beta: Downloading every 1 day"
- "[Auto download] Customer: Downloading every 5 days"

```
