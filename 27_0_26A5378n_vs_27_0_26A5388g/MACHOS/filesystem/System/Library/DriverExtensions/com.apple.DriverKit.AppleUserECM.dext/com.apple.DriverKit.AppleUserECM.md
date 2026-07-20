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
   __TEXT.__cstring: 0x6d6
Functions:
~ sub_100006810 : 16 -> 40
~ sub_100006820 -> sub_100006838 : 40 -> 28
~ sub_100006848 -> sub_100006854 : 28 -> 12
~ sub_100006864 -> sub_100006860 : 12 -> 20
~ sub_100006870 -> sub_100006874 : 20 -> 12
~ __ZN12AppleUserECM8activateEv : 1200 -> 1192
~ __ZN12AppleUserECM24getFunctionalDescriptorsEv : 536 -> 584
~ __ZN12AppleUserECM17readInterruptPipeEv : 184 -> 192
~ __ZN12AppleUserECM23RxPacketsAvailable_ImplEP8OSAction : 120 -> 128
CStrings:
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.6ouHDr/Sources/AppleUSBNetworkingUser_driverkit/AppleUserECM/AppleUserECM.cpp"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.6ouHDr/Sources/AppleUSBNetworkingUser_driverkit/AppleUserECM/AppleUserECMData.cpp"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.DqcjOn/Sources/AppleUSBNetworkingUser_driverkit/AppleUserECM/AppleUserECM.cpp"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.DqcjOn/Sources/AppleUSBNetworkingUser_driverkit/AppleUserECM/AppleUserECMData.cpp"
```
