## txm.iphoneos.release.im4p

> `Firmware/txm.iphoneos.release.im4p`

### Sections with Same Size but Changed Content

- `__TEXT.__cstring`
- `__DATA_CONST.__auth_ptr`
- `__TEXT_BOOT_EXEC.__text`
- `__TEXT_BOOT_EXEC.__bootcode`
- `__DATA.__data`

```diff

   __TEXT.__const: 0x12338
   __TEXT.__binname: 0x40
   __TEXT.__chain_starts: 0x14
-  __DATA_CONST.__const: 0xd5a0
+  __DATA_CONST.__const: 0xd5c8
   __DATA_CONST.__auth_ptr: 0x70
-  __TEXT_EXEC.__text: 0x49a90
+  __TEXT_EXEC.__text: 0x49c28
   __TEXT_EXEC.__exc: 0x8a0
   __TEXT_BOOT_EXEC.__text: 0x4060
   __TEXT_BOOT_EXEC.__bootcode: 0x278
Functions:
~ sub_fffffff01703e9f0 : 1868 -> 1872
~ sub_fffffff01703f758 -> sub_fffffff01703f75c : 2824 -> 3008
~ sub_fffffff01704f014 -> sub_fffffff01704f0d0 : 524 -> 572
~ sub_fffffff01704f220 -> sub_fffffff01704f30c : 800 -> 916
~ sub_fffffff017050bb4 -> sub_fffffff017050d14 : 144 -> 160
~ sub_fffffff017051074 -> sub_fffffff0170511e4 : 152 -> 156
~ sub_fffffff017051288 -> sub_fffffff0170513fc : 160 -> 144
~ sub_fffffff017051328 -> sub_fffffff01705148c : 764 -> 808
~ sub_fffffff0170763b8 -> sub_fffffff017076548 : 252 -> 256
~ sub_fffffff017076764 -> sub_fffffff0170768f8 : 240 -> 244
~ sub_fffffff0170773d0 -> sub_fffffff017077568 : 268 -> 264
~ sub_fffffff017077784 -> sub_fffffff017077918 : 176 -> 180
CStrings:
+ "@(#)VERSION:Code Signing Monitor Image4 Module Version 7.0.0: Wed Sep  2 23:49:02 PDT 2026; root:AppleImage4_txm-374~7872/libimage4_TXM/RELEASE_ARM64E"
+ "Code Signing Monitor Image4 Module Version 7.0.0: Wed Sep  2 23:49:02 PDT 2026; root:AppleImage4_txm-374~7872/libimage4_TXM/RELEASE_ARM64E"
- "@(#)VERSION:Code Signing Monitor Image4 Module Version 7.0.0: Sat Aug  8 13:15:17 PDT 2026; root:AppleImage4_txm-374~7022/libimage4_TXM/RELEASE_ARM64E"
- "Code Signing Monitor Image4 Module Version 7.0.0: Sat Aug  8 13:15:17 PDT 2026; root:AppleImage4_txm-374~7022/libimage4_TXM/RELEASE_ARM64E"
```
