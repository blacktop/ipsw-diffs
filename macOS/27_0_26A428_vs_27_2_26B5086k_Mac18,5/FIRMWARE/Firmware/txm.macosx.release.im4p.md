## txm.macosx.release.im4p

> `Firmware/txm.macosx.release.im4p`

### Sections with Same Size but Changed Content

- `__TEXT.__cstring`
- `__DATA_CONST.__auth_ptr`
- `__TEXT_BOOT_EXEC.__text`
- `__TEXT_BOOT_EXEC.__bootcode`
- `__DATA.__data`

```diff

   __TEXT.__const: 0x121c8
   __TEXT.__binname: 0x40
   __TEXT.__chain_starts: 0x14
-  __DATA_CONST.__const: 0x10120
+  __DATA_CONST.__const: 0x10148
   __DATA_CONST.__auth_ptr: 0x80
-  __TEXT_EXEC.__text: 0x4f96c
+  __TEXT_EXEC.__text: 0x4fb14
   __TEXT_EXEC.__exc: 0x8a0
   __TEXT_BOOT_EXEC.__text: 0x4060
   __TEXT_BOOT_EXEC.__bootcode: 0x278
Functions:
~ sub_fffffff017042870 : 1876 -> 1880
~ sub_fffffff0170435e0 -> sub_fffffff0170435e4 : 2824 -> 3020
~ sub_fffffff017052e98 -> sub_fffffff017052f60 : 524 -> 572
~ sub_fffffff0170530a4 -> sub_fffffff01705319c : 800 -> 916
~ sub_fffffff0170534d8 -> sub_fffffff017053644 : 440 -> 444
~ sub_fffffff017054a34 -> sub_fffffff017054ba4 : 144 -> 160
~ sub_fffffff017054ef4 -> sub_fffffff017055074 : 152 -> 156
~ sub_fffffff017055108 -> sub_fffffff01705528c : 160 -> 144
~ sub_fffffff0170551a8 -> sub_fffffff01705531c : 764 -> 808
~ sub_fffffff017080014 -> sub_fffffff0170801b4 : 252 -> 256
~ sub_fffffff0170803b4 -> sub_fffffff017080558 : 240 -> 244
~ sub_fffffff017081028 -> sub_fffffff0170811d0 : 272 -> 268
~ sub_fffffff0170813e4 -> sub_fffffff017081588 : 176 -> 180
CStrings:
+ "@(#)VERSION:Code Signing Monitor Image4 Module Version 7.0.0: Wed Sep  2 23:26:50 PDT 2026; root:AppleImage4_txm-374~7870/libimage4_TXM/RELEASE_ARM64E"
+ "Code Signing Monitor Image4 Module Version 7.0.0: Wed Sep  2 23:26:50 PDT 2026; root:AppleImage4_txm-374~7870/libimage4_TXM/RELEASE_ARM64E"
- "@(#)VERSION:Code Signing Monitor Image4 Module Version 7.0.0: Sat Aug  8 12:39:48 PDT 2026; root:AppleImage4_txm-374~7020/libimage4_TXM/RELEASE_ARM64E"
- "Code Signing Monitor Image4 Module Version 7.0.0: Sat Aug  8 12:39:48 PDT 2026; root:AppleImage4_txm-374~7020/libimage4_TXM/RELEASE_ARM64E"
```
