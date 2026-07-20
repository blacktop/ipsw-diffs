## com.apple.DriverKit.AppleUserECM

> `/System/Library/DriverExtensions/com.apple.DriverKit.AppleUserECM.dext/com.apple.DriverKit.AppleUserECM`

### Sections with Same Size but Changed Content

- `__TEXT.__cstring`
- `__DATA_CONST.__const`

```diff

-73.0.0.0.0
-  __TEXT.__text: 0x60b4
+73.0.1.0.0
+  __TEXT.__text: 0x60e8
   __TEXT.__auth_stubs: 0x4c0
   __TEXT.__const: 0xbb0
   __TEXT.__cstring: 0x68a
Functions:
~ sub_100002fd8 : 16 -> 40
~ sub_100002fe8 -> sub_100003000 : 40 -> 28
~ sub_100003010 -> sub_10000301c : 28 -> 12
~ sub_10000302c -> sub_100003028 : 12 -> 20
~ sub_100003038 -> sub_10000303c : 20 -> 12
~ __ZN12AppleUserECM8activateEv : 1200 -> 1192
~ __ZN12AppleUserECM24getFunctionalDescriptorsEv : 536 -> 584
~ __ZN12AppleUserECM17readInterruptPipeEv : 184 -> 192
~ __ZN12AppleUserECM23RxPacketsAvailable_ImplEP8OSAction : 120 -> 128
```
