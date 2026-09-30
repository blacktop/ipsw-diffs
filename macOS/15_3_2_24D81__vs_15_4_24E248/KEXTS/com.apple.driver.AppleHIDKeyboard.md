## com.apple.driver.AppleHIDKeyboard

> `com.apple.driver.AppleHIDKeyboard`

```diff

   __TEXT.__cstring: 0x797
   __TEXT.__os_log: 0x730
   __TEXT.__const: 0x7c
-  __TEXT_EXEC.__text: 0x5abc
+  __TEXT_EXEC.__text: 0x5b14
   __TEXT_EXEC.__auth_stubs: 0x0
   __DATA.__data: 0xc8
   __DATA.__common: 0x60

   __DATA_CONST.__mod_term_func: 0x10
   __DATA_CONST.__const: 0x1b60
   __DATA_CONST.__kalloc_type: 0x80
-  UUID: 1CE8FCE7-6CFC-36E4-BCC0-30AEAEB188A0
-  Functions: 104
-  Symbols:   594
+  UUID: 24CB0EFC-C780-3BB5-8DA4-B83138BDA846
+  Functions: 110
+  Symbols:   620
   CStrings:  130
 
Symbols:
+ _ZN27AppleHIDKeyboardEventDriver20turnOffCapsLockDelayEv.cold.1
+ _ZN27AppleHIDKeyboardEventDriver20turnOffCapsLockDelayEv.cold.2
+ _ZN27AppleHIDKeyboardEventDriver20turnOffCapsLockDelayEv.cold.3
+ _ZN27AppleHIDKeyboardEventDriver20turnOffCapsLockDelayEv.cold.4
+ _ZN27AppleHIDKeyboardEventDriver20turnOffCapsLockDelayEv.cold.5
+ _ZN27AppleHIDKeyboardEventDriver20turnOffCapsLockDelayEv.cold.6
+ _ZN27AppleHIDKeyboardEventDriver20turnOffCapsLockDelayEv.cold.7
+ _ZN29AppleHIDKeyboardEventDriverV226initKeyboardBacklightGatedEv.cold.1
+ _ZN29AppleHIDKeyboardEventDriverV226initKeyboardBacklightGatedEv.cold.2
+ _ZN29AppleHIDKeyboardEventDriverV226initKeyboardBacklightGatedEv.cold.3
+ _ZN29AppleHIDKeyboardEventDriverV226initKeyboardBacklightGatedEv.cold.4
+ _ZN29AppleHIDKeyboardEventDriverV226initKeyboardBacklightGatedEv.cold.5
+ _ZN29AppleHIDKeyboardEventDriverV226initKeyboardBacklightGatedEv.cold.6
+ _ZN29AppleHIDKeyboardEventDriverV226overrideKeyboardPropertiesEv.cold.1
+ _ZN29AppleHIDKeyboardEventDriverV226overrideKeyboardPropertiesEv.cold.2
+ _ZN29AppleHIDKeyboardEventDriverV226overrideKeyboardPropertiesEv.cold.3
+ _ZN29AppleHIDKeyboardEventDriverV226overrideKeyboardPropertiesEv.cold.4
+ _ZN29AppleHIDKeyboardEventDriverV226populateKeyboardPropertiesEh.cold.1
+ _ZN29AppleHIDKeyboardEventDriverV226populateKeyboardPropertiesEh.cold.2
+ _ZN29AppleHIDKeyboardEventDriverV226populateKeyboardPropertiesEh.cold.3
+ _ZNK7libkern17bounded_array_refIcN9os_detail21panic_trapping_policyEE5sliceEmm.cold.1
+ _ZNK7libkern17bounded_array_refIcN9os_detail21panic_trapping_policyEE5sliceEmm.cold.2
+ _ZNK7libkern17bounded_array_refIcN9os_detail21panic_trapping_policyEE5sliceEmm.cold.3
+ _ZNK7libkern17bounded_array_refIhN9os_detail21panic_trapping_policyEE5sliceEmm.cold.1
+ _ZNK7libkern17bounded_array_refIhN9os_detail21panic_trapping_policyEE5sliceEmm.cold.2
+ _ZNK7libkern17bounded_array_refIhN9os_detail21panic_trapping_policyEE5sliceEmm.cold.3
Functions:
~ __ZN27AppleHIDKeyboardEventDriver20turnOffCapsLockDelayEv : 488 -> 492
~ __ZN29AppleHIDKeyboardEventDriverV2C2EPK11OSMetaClass : 64 -> 72
~ __ZN29AppleHIDKeyboardEventDriverV2C1EPK11OSMetaClass : 64 -> 72
~ __ZN29AppleHIDKeyboardEventDriverV2C2Ev : 100 -> 108
~ __ZN29AppleHIDKeyboardEventDriverV24freeEv : 128 -> 132
~ __ZN29AppleHIDKeyboardEventDriverV25startEP9IOService : 872 -> 876
- __ZN29AppleHIDKeyboardEventDriverV211handleStartEP9IOService
~ __ZN29AppleHIDKeyboardEventDriverV218setFeatureReportWLEhPhj : 564 -> 560
~ __ZNK7libkern17bounded_array_refIhN9os_detail21panic_trapping_policyEE5sliceEmm : 100 -> 92
~ __ZN29AppleHIDKeyboardEventDriverV218getFeatureReportWLEhPhPj : 652 -> 648
~ __ZN29AppleHIDKeyboardEventDriverV226initKeyboardBacklightGatedEv : 2320 -> 2304
~ __ZN29AppleHIDKeyboardEventDriverV227sendKeyboardBrightnessEventEttt : 268 -> 296
~ __ZN29AppleHIDKeyboardEventDriverV228createCapsLockLanguageSwitchEPhj : 276 -> 272
~ __ZN29AppleHIDKeyboardEventDriverV217createFKeyMappingEPhj : 756 -> 748
- __ZNK7libkern17bounded_array_refIcN9os_detail21panic_trapping_policyEE5sliceEmm
~ __ZN29AppleHIDKeyboardEventDriverV218createStandardTypeEP18KeyboardFormatInfo : 216 -> 208
- sub_fffffe0009967544
~ __ZN29AppleHIDKeyboardEventDriverV215getUsageMappingE10KBMappings : 548 -> 544
~ __ZN29AppleHIDKeyboardEventDriverV230initKeyboardConfigurationGatedEv : 1316 -> 1312
~ __ZN29AppleHIDKeyboardEventDriverV226populateKeyboardPropertiesEh : 2040 -> 1932
~ __ZN29AppleHIDKeyboardEventDriverV226overrideKeyboardPropertiesEv : 1060 -> 1040
~ __ZN29AppleHIDKeyboardEventDriverV221handleInterruptReportEyP18IOMemoryDescriptor15IOHIDReportTypej : 968 -> 992
- __ZN9os_detail21panic_trapping_policy4trapEPKc

```
