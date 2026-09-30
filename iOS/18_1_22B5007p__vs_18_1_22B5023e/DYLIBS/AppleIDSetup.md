## AppleIDSetup

> `/System/Library/PrivateFrameworks/AppleIDSetup.framework/AppleIDSetup`

```diff

-45.1.0.0.0
-  __TEXT.__text: 0x1bbaac
+48.1.1.0.0
+  __TEXT.__text: 0x1bdfac
   __TEXT.__auth_stubs: 0x24c0
   __TEXT.__objc_methlist: 0xb80
-  __TEXT.__const: 0x18538
-  __TEXT.__cstring: 0x36f6
-  __TEXT.__oslogstring: 0x34a2
-  __TEXT.__swift5_typeref: 0x6452
-  __TEXT.__constg_swiftt: 0x6280
+  __TEXT.__const: 0x186a8
+  __TEXT.__cstring: 0x3806
+  __TEXT.__oslogstring: 0x3600
+  __TEXT.__swift5_typeref: 0x648e
+  __TEXT.__constg_swiftt: 0x6394
   __TEXT.__swift5_builtin: 0x294
-  __TEXT.__swift5_reflstr: 0x3239
-  __TEXT.__swift5_fieldmd: 0x5540
+  __TEXT.__swift5_reflstr: 0x32a9
+  __TEXT.__swift5_fieldmd: 0x55f0
   __TEXT.__swift5_assocty: 0x718
-  __TEXT.__swift5_proto: 0x19b8
-  __TEXT.__swift5_types: 0x700
-  __TEXT.__swift5_capture: 0x1798
+  __TEXT.__swift5_proto: 0x19c8
+  __TEXT.__swift5_types: 0x708
+  __TEXT.__swift5_capture: 0x1a48
   __TEXT.__swift5_mpenum: 0xc8
   __TEXT.__swift5_protos: 0x9c
-  __TEXT.__unwind_info: 0x8360
-  __TEXT.__eh_frame: 0xc7e4
+  __TEXT.__unwind_info: 0x83c0
+  __TEXT.__eh_frame: 0xc5dc
   __TEXT.__objc_classname: 0x1be
-  __TEXT.__objc_methname: 0x2218
+  __TEXT.__objc_methname: 0x223e
   __TEXT.__objc_methtype: 0x68c
   __TEXT.__objc_stubs: 0x2c0
-  __DATA_CONST.__got: 0x7d0
-  __DATA_CONST.__const: 0xb90
-  __DATA_CONST.__objc_classlist: 0x188
+  __DATA_CONST.__got: 0x7e8
+  __DATA_CONST.__const: 0xbf0
+  __DATA_CONST.__objc_classlist: 0x190
   __DATA_CONST.__objc_catlist: 0x8
   __DATA_CONST.__objc_protolist: 0xa0
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x868
+  __DATA_CONST.__objc_selrefs: 0x880
   __DATA_CONST.__objc_protorefs: 0x60
   __DATA_CONST.__objc_superrefs: 0x48
   __AUTH_CONST.__auth_got: 0x1268
-  __AUTH_CONST.__auth_ptr: 0xbd8
-  __AUTH_CONST.__const: 0xe650
+  __AUTH_CONST.__auth_ptr: 0xb48
+  __AUTH_CONST.__const: 0xec08
   __AUTH_CONST.__cfstring: 0x20
-  __AUTH_CONST.__objc_const: 0x5128
-  __AUTH.__objc_data: 0x2158
-  __AUTH.__data: 0x2248
+  __AUTH_CONST.__objc_const: 0x5258
+  __AUTH.__objc_data: 0x21a8
+  __AUTH.__data: 0x23c0
   __DATA.__objc_ivar: 0xac
-  __DATA.__data: 0x7828
-  __DATA.__bss: 0x31558
-  __DATA.__common: 0xb8
+  __DATA.__data: 0x7978
+  __DATA.__bss: 0x316d8
+  __DATA.__common: 0xc8
   __DATA_DIRTY.__objc_data: 0x50
   __DATA_DIRTY.__data: 0x998
   __DATA_DIRTY.__bss: 0x900

   - /usr/lib/swift/libswiftUniformTypeIdentifiers.dylib
   - /usr/lib/swift/libswiftWebKit.dylib
   - /usr/lib/swift/libswiftXPC.dylib
+  - /usr/lib/swift/libswift_Builtin_float.dylib
   - /usr/lib/swift/libswift_Concurrency.dylib
+  - /usr/lib/swift/libswift_errno.dylib
+  - /usr/lib/swift/libswift_math.dylib
+  - /usr/lib/swift/libswift_signal.dylib
+  - /usr/lib/swift/libswift_stdio.dylib
+  - /usr/lib/swift/libswift_time.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  Functions: 10848
-  Symbols:   656
-  CStrings:  1159
+  - /usr/lib/swift/libswiftsys_time.dylib
+  - /usr/lib/swift/libswiftunistd.dylib
+  Functions: 10938
+  Symbols:   669
+  CStrings:  1176
 
Symbols:
+ _OBJC_CLASS_$_AKAccountManager
+ __swift_FORCE_LOAD_$_swift_Builtin_float
+ __swift_FORCE_LOAD_$_swift_errno
+ __swift_FORCE_LOAD_$_swift_math
+ __swift_FORCE_LOAD_$_swift_signal
+ __swift_FORCE_LOAD_$_swift_stdio
+ __swift_FORCE_LOAD_$_swift_time
+ __swift_FORCE_LOAD_$_swiftsys_time
+ __swift_FORCE_LOAD_$_swiftunistd
- _swift_taskGroup_destroy
- _swift_taskGroup_initialize
CStrings:
+ "Client decided to cancel basic login"
+ "Missing account class found for the account %!@(MISSING)"
+ "Missing account class found for the account: %!@(MISSING)"
+ "SECOND_FACTOR_ALERT_MESSAGE"
+ "SECOND_FACTOR_ALERT_TITLE"
+ "Setup report is missing altDSID. Ending analytics event with missing account class."
+ "Unable to calculate duration for AISSetupAnalyticsEvent \nstartDate: (%!s(MISSING)) \nendDate: (%!s(MISSING))"
+ "_TtC12AppleIDSetup22AISSetupAnalyticsEvent"
+ "aa_accountClass"
+ "accountClass"
+ "analytics"
+ "com.apple.appleidsetup.setup"
+ "didSucceed"
+ "isNull"
+ "setupAnalyticsEvent"
+ "sharedInstance"
+ "v24@?0@\"NSNumber\"8@\"NSError\"16"

```
