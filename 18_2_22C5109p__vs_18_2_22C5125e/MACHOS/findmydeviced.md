## findmydeviced

> `/usr/libexec/findmydeviced`

```diff

-438.32.7.13.6
-  __TEXT.__text: 0x24059c
-  __TEXT.__auth_stubs: 0x1010
-  __TEXT.__objc_stubs: 0x168c0
-  __TEXT.__objc_methlist: 0xe244
+438.32.7.13.9
+  __TEXT.__text: 0x240bac
+  __TEXT.__auth_stubs: 0x1030
+  __TEXT.__objc_stubs: 0x16920
+  __TEXT.__objc_methlist: 0xe274
   __TEXT.__const: 0x2cc50
   __TEXT.__gcc_except_tab: 0x2b84
-  __TEXT.__objc_methname: 0x1c3fc
-  __TEXT.__oslogstring: 0x10b4a
-  __TEXT.__cstring: 0x8aed
+  __TEXT.__objc_methname: 0x1c45a
+  __TEXT.__oslogstring: 0x10ba9
+  __TEXT.__cstring: 0x8b4d
   __TEXT.__objc_classname: 0x1ac9
-  __TEXT.__objc_methtype: 0x306d
+  __TEXT.__objc_methtype: 0x309b
   __TEXT.__constg_swiftt: 0x50
   __TEXT.__swift5_typeref: 0x5c
   __TEXT.__swift5_fieldmd: 0x10

   __TEXT.__swift5_types: 0x4
   __TEXT.__unwind_info: 0x33d8
   __TEXT.__eh_frame: 0x358
-  __DATA_CONST.__auth_got: 0x818
-  __DATA_CONST.__got: 0x8f8
+  __DATA_CONST.__auth_got: 0x828
+  __DATA_CONST.__got: 0x908
   __DATA_CONST.__auth_ptr: 0x10
-  __DATA_CONST.__const: 0xd398
-  __DATA_CONST.__cfstring: 0xa8a0
+  __DATA_CONST.__const: 0xd3c8
+  __DATA_CONST.__cfstring: 0xa8e0
   __DATA_CONST.__objc_classlist: 0x6d8
   __DATA_CONST.__objc_catlist: 0x60
   __DATA_CONST.__objc_protolist: 0x200

   __DATA_CONST.__objc_floatobj: 0x30
   __DATA_CONST.__objc_dictobj: 0xc8
   __DATA_CONST.__linkguard: 0xe
-  __DATA.__objc_const: 0x1c5a8
-  __DATA.__objc_selrefs: 0x6590
+  __DATA.__objc_const: 0x1c5c8
+  __DATA.__objc_selrefs: 0x65a8
   __DATA.__objc_ivar: 0x10c4
   __DATA.__objc_data: 0x44e0
   __DATA.__data: 0x2580
-  __DATA.__bss: 0x7e0
+  __DATA.__bss: 0x7f0
   __DATA.__common: 0x69
   - /System/Library/Frameworks/Accounts.framework/Accounts
   - /System/Library/Frameworks/CFNetwork.framework/CFNetwork

   - /usr/lib/swift/libswiftDarwin.dylib
   - /usr/lib/swift/libswiftDispatch.dylib
   - /usr/lib/swift/libswiftMetal.dylib
+  - /usr/lib/swift/libswiftOSLog.dylib
   - /usr/lib/swift/libswiftObjectiveC.dylib
   - /usr/lib/swift/libswiftQuartzCore.dylib
   - /usr/lib/swift/libswiftXPC.dylib

   - /usr/lib/swift/libswiftsimd.dylib
   - /usr/lib/swift/libswiftsys_time.dylib
   - /usr/lib/swift/libswiftunistd.dylib
-  Functions: 5898
-  Symbols:   633
-  CStrings:  8520
+  Functions: 5904
+  Symbols:   638
+  CStrings:  8531
 
Symbols:
+ _MAEReissueUCRTWithError
+ _MAEUCRTUpgradeRequired
+ __swift_FORCE_LOAD_$_swiftOSLog
+ _kFMDOptionsActivationLockPET
+ _kFMDOptionsActivationLockUsername
CStrings:
+ "Is UCRT Success: %!s(MISSING),: Error: %!@(MISSING)"
+ "UCRT Upgrade required %!s(MISSING)"
+ "UCRT upgrade check failed because: %!@(MISSING)"
+ "Username or password is not correct types"
+ "Vv32@0:8@\"NSDictionary\"16@?<v@?B@\"NSError\">24"
+ "_hasUCRTHealingAccessEntitlement"
+ "attemptUCRTHealing:completion:"
+ "com.apple.icloud.FindMyDevice.ucrt.healing.access"
+ "false"
+ "healUCRT"
+ "validateParamsForUCRTHealing:"

```
