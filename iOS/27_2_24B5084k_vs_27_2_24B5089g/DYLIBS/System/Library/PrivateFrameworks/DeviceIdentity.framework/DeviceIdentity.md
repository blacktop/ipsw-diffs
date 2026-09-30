## DeviceIdentity

> `/System/Library/PrivateFrameworks/DeviceIdentity.framework/DeviceIdentity`

### Sections with Same Size but Changed Content

- `__TEXT.__cstring`

```diff

-1145.40.4.0.0
-  __TEXT.__text: 0x1d628
+1145.40.5.0.0
+  __TEXT.__text: 0x1d630
   __TEXT.__objc_methlist: 0x504
   __TEXT.__cstring: 0x42b8
   __TEXT.__gcc_except_tab: 0xaa0

   __AUTH_CONST.__objc_intobj: 0x1f8
   __AUTH_CONST.__auth_got: 0x4a0
   __DATA.__objc_ivar: 0x54
-  __DATA.__data: 0xd4
+  __DATA.__data: 0x4
   __DATA_DIRTY.__objc_data: 0xa0
-  __DATA_DIRTY.__data: 0x20
+  __DATA_DIRTY.__data: 0xf0
   __DATA_DIRTY.__bss: 0x58
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/CryptoTokenKit.framework/CryptoTokenKit
Functions:
~ _X509ExtensionParseBasicConstraints : 208 -> 204
~ _X509ChainBuildPathPartial : 488 -> 500
CStrings:
+ "iOS Device Activator (MobileActivation-1145.40.5)"
- "iOS Device Activator (MobileActivation-1145.40.4)"
```
