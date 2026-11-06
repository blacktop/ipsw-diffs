## libimage4.dylib

> `/usr/lib/libimage4.dylib`

### Sections with Same Size but Changed Content

- `__TEXT.__cstring`
- `__TEXT.__info_plist`

```diff

 374.0.0.0.0
-  __TEXT.__text: 0x2bd20
-  __TEXT.__const: 0x1f570
+  __TEXT.__text: 0x2bd30
+  __TEXT.__const: 0x1f580
   __TEXT.__cstring: 0x6a3e
   __TEXT.__oslogstring: 0x7e
   __TEXT.__info_plist: 0x4d7
   __TEXT.__unwind_info: 0xa10
   __TEXT.__auth_stubs: 0x0
-  __DATA_CONST.__const: 0xa350
+  __DATA_CONST.__const: 0xa360
   __DATA_CONST.__image4_chp: 0x170
   __DATA_CONST.__image4_coproc: 0x48
   __DATA_CONST.__got: 0x0
   __AUTH_CONST.__const: 0x7b60
   __AUTH_CONST.__auth_got: 0x3b8
   __AUTH_CONST.__auth_ptr: 0x0
-  __AUTH.__data: 0x120
-  __DATA.__data: 0xb8
   __DATA.__bss: 0x18
   __DATA.__common: 0x8
-  __DATA_DIRTY.__data: 0x3b8
+  __DATA_DIRTY.__data: 0x590
   __DATA_DIRTY.__bss: 0xd8
   - /System/Library/Frameworks/CoreFoundation.framework/Versions/A/CoreFoundation
   - /System/Library/Frameworks/IOKit.framework/Versions/A/IOKit
   - /usr/lib/libImage4_V2.dylib
   - /usr/lib/libSystem.B.dylib
   Functions: 1144
-  Symbols:   2788
+  Symbols:   2790
   CStrings:  876
 
Symbols:
+ __oidAppleExtendedKeyUsageSWUpdateSigning
+ _oidAppleExtendedKeyUsageSWUpdateSigning
Functions:
~ _X509ExtensionParseBasicConstraints : 208 -> 212
~ _X509ChainBuildPathPartial : 484 -> 496
CStrings:
+ "@(#)VERSION:Darwin Image4 Library Version 7.0.0: Sat Oct  3 14:48:58 PDT 2026; root:AppleImage4_libraries-374~9633/libimage4/RELEASE_ARM64E"
+ "Darwin Image4 Library Version 7.0.0: Sat Oct  3 14:48:58 PDT 2026; root:AppleImage4_libraries-374~9633/libimage4/RELEASE_ARM64E"
- "@(#)VERSION:Darwin Image4 Library Version 7.0.0: Sat Aug  8 14:05:09 PDT 2026; root:AppleImage4_libraries-374~7699/libimage4/RELEASE_ARM64E"
- "Darwin Image4 Library Version 7.0.0: Sat Aug  8 14:05:09 PDT 2026; root:AppleImage4_libraries-374~7699/libimage4/RELEASE_ARM64E"
```
