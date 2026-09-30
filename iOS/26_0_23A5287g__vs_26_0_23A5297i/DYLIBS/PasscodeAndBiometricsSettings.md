## PasscodeAndBiometricsSettings

> `/System/Library/PrivateFrameworks/PasscodeAndBiometricsSettings.framework/PasscodeAndBiometricsSettings`

```diff

-11.0.0.0.0
-  __TEXT.__text: 0x2fd84
+12.2.0.0.0
+  __TEXT.__text: 0x2fe48
   __TEXT.__auth_stubs: 0xc40
   __TEXT.__delay_stubs: 0x2c
   __TEXT.__delay_helper: 0xc8
   __TEXT.__objc_methlist: 0x1fc4
   __TEXT.__const: 0x4d4
   __TEXT.__gcc_except_tab: 0xad8
-  __TEXT.__cstring: 0x30cf
-  __TEXT.__oslogstring: 0x45c6
+  __TEXT.__cstring: 0x30df
+  __TEXT.__oslogstring: 0x45f3
   __TEXT.__dlopen_cstrs: 0x443
   __TEXT.__ustring: 0x4e
   __TEXT.__constg_swiftt: 0xe0

   __DATA_CONST.__objc_arraydata: 0x8
   __AUTH_CONST.__auth_got: 0x638
   __AUTH_CONST.__const: 0x448
-  __AUTH_CONST.__cfstring: 0x2ac0
+  __AUTH_CONST.__cfstring: 0x2ae0
   __AUTH_CONST.__objc_const: 0x1f78
   __AUTH_CONST.__objc_intobj: 0x1c8
   __AUTH_CONST.__objc_arrayobj: 0x18

   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  UUID: 22618D6E-9532-3BD7-8560-5A4A66AC7D2F
+  UUID: 2AF5FE09-1E0D-35A2-B55B-9F7A1D02FED8
   Functions: 1035
   Symbols:   3695
-  CStrings:  2363
+  CStrings:  2365
 
Functions:
~ -[PABSPasscodeLockController setupPasscodeGroupSpecifier:onOffButtonSpecifier:] : 968 -> 1112
~ sub_26abba248 -> sub_26bca62d8 : 1156 -> 1208
CStrings:
+ "PASSCODE_PLACARD"
+ "PASSCODE_TOGGLE"
+ "Passcode Group: Passcode On/Off enablement status [%@] | needsAppleIDAuthWhichNeedsInternet [%@] | isMC [%@] | sdpIsON [%@] | isEnrolledInBiometrics [%@] | parentSpecifier [%@] | retrievedCreds [%@]"
- "PRIVACY_PLACARD"
- "Passcode Group: Passcode On/Off enablement status [%@] | needsAppleIDAuthWhichNeedsInternet [%@] | isMC [%@] | sdpIsON [%@] | isEnrolledInBiometrics [%@]"

```
