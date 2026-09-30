## libcryptex_core.dylib

> `/usr/lib/libcryptex_core.dylib`

```diff

-493.100.42.0.0
+493.100.51.0.0
   __TEXT.__text: 0x15e60
   __TEXT.__auth_stubs: 0xdf0
   __TEXT.__objc_methlist: 0x444

   - /System/Library/PrivateFrameworks/AppleKeyStore.framework/AppleKeyStore
   - /usr/lib/libMobileGestalt.dylib
   - /usr/lib/libSystem.B.dylib
+  - /usr/lib/libamsupport.dylib
   - /usr/lib/libauthinstall.dylib
   - /usr/lib/libimage4.dylib
   - /usr/lib/libobjc.A.dylib
Symbols:
+ _cryptex_tss_set_info_from_file
- _cryptex_tss_set_c411_from_file
CStrings:
+ "493.100.51"
+ "@(#)VERSION:Darwin Cryptex Core Interface Version 2.0.0: Fri Feb 21 20:08:03 PST 2025; root:libcryptex-493.100.51~147/libcryptex_core/RELEASE_ARM64E"
+ "Darwin Cryptex Core Interface Version 2.0.0: Fri Feb 21 20:08:03 PST 2025; root:libcryptex-493.100.51~147/libcryptex_core/RELEASE_ARM64E"
+ "T@\"NSData\",&,N,V_info_content"
+ "_info_content"
+ "info_content"
+ "setInfo_content:"
- "493.100.42"
- "@(#)VERSION:Darwin Cryptex Core Interface Version 2.0.0: Sun Feb 16 10:33:21 PST 2025; root:libcryptex-493.100.42~129/libcryptex_core/RELEASE_ARM64E"
- "Darwin Cryptex Core Interface Version 2.0.0: Sun Feb 16 10:33:21 PST 2025; root:libcryptex-493.100.42~129/libcryptex_core/RELEASE_ARM64E"
- "T@\"NSData\",&,N,V_c411_content"
- "_c411_content"
- "c411_content"
- "setC411_content:"

```
