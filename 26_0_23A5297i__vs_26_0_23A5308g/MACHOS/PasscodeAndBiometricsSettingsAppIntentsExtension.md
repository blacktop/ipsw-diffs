## PasscodeAndBiometricsSettingsAppIntentsExtension

> `/System/Library/ExtensionKit/Extensions/PasscodeAndBiometricsSettingsAppIntentsExtension.appex/PasscodeAndBiometricsSettingsAppIntentsExtension`

```diff

-12.2.0.0.0
-  __TEXT.__text: 0x64f4
-  __TEXT.__auth_stubs: 0x7e0
-  __TEXT.__objc_stubs: 0xa0
-  __TEXT.__objc_methlist: 0x44
+14.0.0.0.0
+  __TEXT.__text: 0x6cbc
+  __TEXT.__auth_stubs: 0x840
+  __TEXT.__objc_stubs: 0x120
+  __TEXT.__objc_methlist: 0x50
   __TEXT.__const: 0xae2
-  __TEXT.__gcc_except_tab: 0x30
-  __TEXT.__cstring: 0x1902
+  __TEXT.__gcc_except_tab: 0x48
+  __TEXT.__cstring: 0x1992
   __TEXT.__objc_classname: 0x21
-  __TEXT.__objc_methname: 0x129
+  __TEXT.__oslogstring: 0x32
+  __TEXT.__objc_methname: 0x1ac
   __TEXT.__objc_methtype: 0x14
   __TEXT.__dlopen_cstrs: 0xe6
   __TEXT.__constg_swiftt: 0x118

   __TEXT.__swift5_fieldmd: 0x154
   __TEXT.__swift5_types: 0x1c
   __TEXT.__swift_as_entry: 0x34
-  __TEXT.__swift_as_ret: 0x24
+  __TEXT.__swift_as_ret: 0x28
   __TEXT.__swift5_proto: 0x84
-  __TEXT.__swift5_reflstr: 0x228
+  __TEXT.__swift5_reflstr: 0x22b
   __TEXT.__swift5_assocty: 0x120
-  __TEXT.__unwind_info: 0x2f0
-  __TEXT.__eh_frame: 0x250
-  __DATA_CONST.__auth_got: 0x400
-  __DATA_CONST.__got: 0xd0
+  __TEXT.__unwind_info: 0x328
+  __TEXT.__eh_frame: 0x288
+  __DATA_CONST.__auth_got: 0x430
+  __DATA_CONST.__got: 0xd8
   __DATA_CONST.__auth_ptr: 0x478
-  __DATA_CONST.__const: 0x4f8
-  __DATA_CONST.__cfstring: 0x20
+  __DATA_CONST.__const: 0x588
   __DATA_CONST.__objc_classlist: 0x10
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA.__objc_const: 0xd8
-  __DATA.__objc_selrefs: 0x70
+  __DATA.__objc_selrefs: 0x98
   __DATA.__objc_data: 0x108
   __DATA.__data: 0x1d8
-  __DATA.__bss: 0x10c0
+  __DATA.__bss: 0x10e0
   __DATA.__common: 0x30
   - /System/Library/Frameworks/AppIntents.framework/AppIntents
-  - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/Foundation.framework/Foundation
   - /System/Library/Frameworks/LocalAuthentication.framework/LocalAuthentication
   - /System/Library/Frameworks/UIKit.framework/UIKit

   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  UUID: 8FFE54AB-53B4-3182-A241-B736C14BBB24
-  Functions: 204
-  Symbols:   95
-  CStrings:  123
+  UUID: C30A3929-3420-3F3C-9F49-C4E4FD72AA23
+  Functions: 219
+  Symbols:   102
+  CStrings:  136
 
Symbols:
+ __NSConcreteGlobalBlock
+ ___assert_rtn
+ __dispatch_main_q
+ __os_log_error_impl
+ _objc_alloc
+ _objc_retain_x1
+ _objc_retain_x20
+ _os_log_create
+ _os_log_type_enabled
- _NSLog
- ___CFConstantStringClassReference
CStrings:
+ "PABSLogForCategory"
+ "PABSLogging.m"
+ "Passcode"
+ "PasscodeAndBiometricsSettings"
+ "SFAuthenticationManager"
+ "Unlock using Vision: %@"
+ "Unlock with nearby devices"
+ "Use this option to unlock your device using nearby devices like your Apple\u00a0Watch or Vision Pro"
+ "Vision Pro unlock"
+ "canUseVisionToUnlockWithCompletionHandler:"
+ "category < PABSLoggingCategoryCount"
+ "count"
+ "initWithQueue:"
+ "isSupportedForType:"
+ "listCandidateDevicesForType:completionHandler:"
+ "v24@?0@\"NSSet\"8@\"NSError\"16"
- "Unlock with Apple Watch"
- "When you're wearing a mask or sunglasses and your Apple Watch, you can simply raise and glance at your device to unlock it."

```
