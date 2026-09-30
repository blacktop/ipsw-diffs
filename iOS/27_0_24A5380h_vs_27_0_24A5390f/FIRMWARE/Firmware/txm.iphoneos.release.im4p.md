## txm.iphoneos.release.im4p

> `Firmware/txm.iphoneos.release.im4p`

### Sections with Same Size but Changed Content

- `__DATA_CONST.__const`
- `__DATA_CONST.__auth_ptr`
- `__TEXT_BOOT_EXEC.__text`
- `__DATA.__data`

```diff

-217.0.0.0.0
-  __TEXT.__cstring: 0x63ce
-  __TEXT.__const: 0xff28
+217.0.1.0.0
+  __TEXT.__cstring: 0x64ca
+  __TEXT.__const: 0xff88
   __TEXT.__binname: 0x40
   __TEXT.__chain_starts: 0x14
   __DATA_CONST.__const: 0xd198
   __DATA_CONST.__auth_ptr: 0x70
-  __TEXT_EXEC.__text: 0x490b8
+  __TEXT_EXEC.__text: 0x49238
   __TEXT_EXEC.__exc: 0x8a0
   __TEXT_BOOT_EXEC.__text: 0x4060
   __TEXT_BOOT_EXEC.__bootcode: 0x278
   __DATA.__data: 0x2d0
   __DATA.__common: 0xf80
   __DATA.__bss: 0x598
-  Functions: 1089
+  Functions: 1090
   Symbols:   1
-  CStrings:  728
+  CStrings:  734
 
CStrings:
+ "@(#)VERSION:Code Signing Monitor Image4 Module Version 7.0.0: Fri Jul 10 21:20:27 PDT 2026; root:AppleImage4_txm-374~3979/libimage4_TXM/RELEASE_ARM64E"
+ "Code Signing Monitor Image4 Module Version 7.0.0: Fri Jul 10 21:20:27 PDT 2026; root:AppleImage4_txm-374~3979/libimage4_TXM/RELEASE_ARM64E"
+ "PlatformCode-Strict"
+ "cs-system-policy"
+ "cs-system-policy property is not a NULL terminated string"
+ "developer mode disabled due to platform code strict policy"
+ "missing data for cs-system-policy property"
+ "txm.iphoneos.release.TrustedExecutionMonitor_Guarded-217.0.1"
+ "unable to find cs-system-policy property in /chosen"
- "@(#)VERSION:Code Signing Monitor Image4 Module Version 7.0.0: Fri Jun 26 21:01:06 PDT 2026; root:AppleImage4_txm-374~2547/libimage4_TXM/RELEASE_ARM64E"
- "Code Signing Monitor Image4 Module Version 7.0.0: Fri Jun 26 21:01:06 PDT 2026; root:AppleImage4_txm-374~2547/libimage4_TXM/RELEASE_ARM64E"
- "txm.iphoneos.release.TrustedExecutionMonitor_Guarded-217"
```
