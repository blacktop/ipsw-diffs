## txm.iphoneos.release.im4p

> `Firmware/txm.iphoneos.release.im4p`

### Sections with Same Size but Changed Content

- `__TEXT.__cstring`
- `__DATA_CONST.__const`
- `__DATA_CONST.__auth_ptr`
- `__TEXT_BOOT_EXEC.__text`
- `__DATA.__data`

```diff

   __TEXT.__chain_starts: 0x14
   __DATA_CONST.__const: 0xd5c8
   __DATA_CONST.__auth_ptr: 0x70
-  __TEXT_EXEC.__text: 0x49c28
+  __TEXT_EXEC.__text: 0x49c38
   __TEXT_EXEC.__exc: 0x8a0
   __TEXT_BOOT_EXEC.__text: 0x4060
   __TEXT_BOOT_EXEC.__bootcode: 0x278
Functions:
~ sub_fffffff0170631ec : 200 -> 204
~ sub_fffffff017064f0c -> sub_fffffff017064f10 : 492 -> 504
CStrings:
+ "@(#)VERSION:Code Signing Monitor Image4 Module Version 7.0.0: Sat Sep 12 03:03:29 PDT 2026; root:AppleImage4_txm-374~8103/libimage4_TXM/RELEASE_ARM64E"
+ "Code Signing Monitor Image4 Module Version 7.0.0: Sat Sep 12 03:03:29 PDT 2026; root:AppleImage4_txm-374~8103/libimage4_TXM/RELEASE_ARM64E"
- "@(#)VERSION:Code Signing Monitor Image4 Module Version 7.0.0: Wed Sep  2 23:49:02 PDT 2026; root:AppleImage4_txm-374~7872/libimage4_TXM/RELEASE_ARM64E"
- "Code Signing Monitor Image4 Module Version 7.0.0: Wed Sep  2 23:49:02 PDT 2026; root:AppleImage4_txm-374~7872/libimage4_TXM/RELEASE_ARM64E"
```
