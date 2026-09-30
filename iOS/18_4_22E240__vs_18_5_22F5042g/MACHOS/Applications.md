## Applications

> `/System/Library/Assistant/Plugins/Applications.assistantBundle/Applications`

```diff

-115.4.3.0.0
-  __TEXT.__text: 0x107e4
-  __TEXT.__auth_stubs: 0x700
+115.5.1.0.0
+  __TEXT.__text: 0x107cc
+  __TEXT.__auth_stubs: 0x6f0
   __TEXT.__objc_stubs: 0x2260
   __TEXT.__objc_methlist: 0x974
   __TEXT.__const: 0x96
-  __TEXT.__oslogstring: 0x2674
-  __TEXT.__cstring: 0x205b
+  __TEXT.__oslogstring: 0x2684
+  __TEXT.__cstring: 0x203b
   __TEXT.__objc_classname: 0x217
   __TEXT.__objc_methname: 0x1ea5
   __TEXT.__objc_methtype: 0x780

   __TEXT.__swift_as_ret: 0x8
   __TEXT.__unwind_info: 0x410
   __TEXT.__eh_frame: 0x120
-  __DATA_CONST.__auth_got: 0x390
+  __DATA_CONST.__auth_got: 0x388
   __DATA_CONST.__got: 0x390
   __DATA_CONST.__auth_ptr: 0x18
   __DATA_CONST.__const: 0x5f8

   - /usr/lib/swift/libswiftsys_time.dylib
   - /usr/lib/swift/libswiftunistd.dylib
   Functions: 347
-  Symbols:   317
-  CStrings:  834
+  Symbols:   316
+  CStrings:  832
 
Symbols:
+ _AFIsPersistentSiriAvailable
- _AFDeviceSupportsSystemAssistantExperience
- __os_feature_enabled_impl
CStrings:
+ "%s com.apple.siri.applications: Setting doNotDismissSiri to YES since Persistent Siri is available"
- "%s com.apple.siri.applications: Setting doNotDismissSiri to YES since SAE is enabled"
- "SiriUI"
- "persistent_siri"

```
