## nearbyd

> `/usr/libexec/nearbyd`

```diff

-458.0.3.0.0
-  __TEXT.__text: 0x42dbac
-  __TEXT.__auth_stubs: 0x2900
+458.0.6.0.0
+  __TEXT.__text: 0x42e3c4
+  __TEXT.__auth_stubs: 0x2910
   __TEXT.__objc_stubs: 0x10f80
   __TEXT.__init_offsets: 0x5e8
   __TEXT.__objc_methlist: 0x9a0c
-  __TEXT.__gcc_except_tab: 0x46f9c
+  __TEXT.__gcc_except_tab: 0x4703c
   __TEXT.__const: 0x2d4de0
-  __TEXT.__cstring: 0x30862
+  __TEXT.__cstring: 0x308e2
   __TEXT.__objc_methname: 0x19ed8
-  __TEXT.__oslogstring: 0x4c23f
+  __TEXT.__oslogstring: 0x4c264
   __TEXT.__objc_classname: 0x185b
   __TEXT.__objc_methtype: 0x1c185
   __TEXT.__swift5_typeref: 0x7d

   __TEXT.__swift5_fieldmd: 0x28
   __TEXT.__swift5_types: 0x4
   __TEXT.__info_plist: 0x3fc
-  __TEXT.__unwind_info: 0x17430
+  __TEXT.__unwind_info: 0x17458
   __TEXT.__eh_frame: 0x38
-  __DATA_CONST.__auth_got: 0x1498
-  __DATA_CONST.__got: 0x970
+  __DATA_CONST.__auth_got: 0x14a0
+  __DATA_CONST.__got: 0x980
   __DATA_CONST.__auth_ptr: 0x80
-  __DATA_CONST.__const: 0x1f600
-  __DATA_CONST.__cfstring: 0x117a0
+  __DATA_CONST.__const: 0x1f688
+  __DATA_CONST.__cfstring: 0x117c0
   __DATA_CONST.__objc_classlist: 0x4a8
   __DATA_CONST.__objc_catlist: 0x18
   __DATA_CONST.__objc_protolist: 0x258

   __DATA.__objc_ivar: 0x12d0
   __DATA.__objc_data: 0x2f48
   __DATA.__data: 0x302c
-  __DATA.__bss: 0xc1c0
+  __DATA.__bss: 0xc1d0
   __DATA.__common: 0xca0
   - /System/Library/Frameworks/AVFAudio.framework/AVFAudio
   - /System/Library/Frameworks/AVFoundation.framework/AVFoundation

   - /usr/lib/swift/libswiftDispatch.dylib
   - /usr/lib/swift/libswiftObjectiveC.dylib
   - /usr/lib/swift/libswiftXPC.dylib
+  - /usr/lib/swift/libswift_Builtin_float.dylib
+  - /usr/lib/swift/libswift_errno.dylib
+  - /usr/lib/swift/libswift_math.dylib
+  - /usr/lib/swift/libswift_signal.dylib
+  - /usr/lib/swift/libswift_stdio.dylib
+  - /usr/lib/swift/libswift_time.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  Functions: 18747
-  Symbols:   990
-  CStrings:  16497
+  - /usr/lib/swift/libswiftsys_time.dylib
+  - /usr/lib/swift/libswiftunistd.dylib
+  Functions: 18753
+  Symbols:   1001
+  CStrings:  16503
 
Symbols:
+ __swift_FORCE_LOAD_$_swift_Builtin_float
+ __swift_FORCE_LOAD_$_swift_errno
+ __swift_FORCE_LOAD_$_swift_math
+ __swift_FORCE_LOAD_$_swift_signal
+ __swift_FORCE_LOAD_$_swift_stdio
+ __swift_FORCE_LOAD_$_swift_time
+ __swift_FORCE_LOAD_$_swiftsys_time
+ __swift_FORCE_LOAD_$_swiftunistd
+ __xpc_type_bool
+ __xpc_type_uint64
+ _xpc_bool_get_value
+ _xpc_uint64_get_value
- _xpc_dictionary_get_bool
CStrings:
+ "#coex,parseIncomingEvent-Received msg from UCM: BT [Power: %!s(MISSING), Band: %!s(MISSING)], Cellular [Power: %!s(MISSING), Band: %!s(MISSING)], WiFi [Power: %!s(MISSING), Channel: %!s(MISSING)], R1DutyCycleNeeded: %!s(MISSING)"
+ "#ses-acwg,Applying additional start time offset for Ch5 coex"
+ "#ses-carkey,Applying additional start time offset for Ch5 coex"
+ "/AppleInternal/Library/BuildRoots/a9331c2c-4f73-11ef-8db8-b60714381f84/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS18.0.Internal.sdk/usr/local/include/google/protobuf/repeated_field.h"
+ "/AppleInternal/Library/BuildRoots/a9331c2c-4f73-11ef-8db8-b60714381f84/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS18.0.Internal.sdk/usr/local/include/google/protobuf/wire_format_lite_inl.h"
+ "Not expected to handle coex event %!s(MISSING)"
+ "R2ChannelToTriggerGpioBlankingChanged"
+ "R2NbChannelIdxToTriggerGpioBlankingChanged"
+ "RadioStateUpdate"
+ "UCMDutyCycleAllowance"
+ "marconi"
+ "rdar://130935626 - CN Ch5 mitigation"
- "#coex,parseIncomingEvent-Invalid BtBand %!u(MISSING) from UCM"
- "#coex,parseIncomingEvent-Invalid WiFiChannel %!u(MISSING) from UCM"
- "#coex,parseIncomingEvent-Recevied msg from UCM: BtPowerState(%!d(MISSING)), CellularPowerState(%!d(MISSING)), WiFiPowerState(%!d(MISSING)), BtBand(%!d(MISSING)), CellularBand(%!d(MISSING)), WiFiChannel(%!d(MISSING)), R1DutyCycleNeeded(%!d(MISSING))"
- "/AppleInternal/Library/BuildRoots/0af4df6a-42a2-11ef-b9e2-1aec23608739/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS18.0.Internal.sdk/usr/local/include/google/protobuf/repeated_field.h"
- "/AppleInternal/Library/BuildRoots/0af4df6a-42a2-11ef-b9e2-1aec23608739/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS18.0.Internal.sdk/usr/local/include/google/protobuf/wire_format_lite_inl.h"
- "Not expected to handle this coex event"

```
