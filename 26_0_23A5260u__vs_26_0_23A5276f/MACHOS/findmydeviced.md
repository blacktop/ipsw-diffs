## findmydeviced

> `/usr/libexec/findmydeviced`

```diff

-452.30.5.13.0
-  __TEXT.__text: 0x22050c
+455.30.6.9.8
+  __TEXT.__text: 0x221550
   __TEXT.__auth_stubs: 0x1070
-  __TEXT.__objc_stubs: 0x16ca0
-  __TEXT.__objc_methlist: 0xf734
+  __TEXT.__objc_stubs: 0x16d40
+  __TEXT.__objc_methlist: 0xf7ac
   __TEXT.__const: 0x2db30
-  __TEXT.__gcc_except_tab: 0x2c58
-  __TEXT.__objc_methname: 0x1c7ef
-  __TEXT.__oslogstring: 0x11474
-  __TEXT.__cstring: 0x8d48
+  __TEXT.__gcc_except_tab: 0x2ce8
+  __TEXT.__objc_methname: 0x1c98d
+  __TEXT.__oslogstring: 0x11519
+  __TEXT.__cstring: 0x8eb8
   __TEXT.__objc_classname: 0x1a80
-  __TEXT.__objc_methtype: 0x30ff
+  __TEXT.__objc_methtype: 0x3142
   __TEXT.__constg_swiftt: 0x58
   __TEXT.__swift5_typeref: 0x77
   __TEXT.__swift5_reflstr: 0x8

   __TEXT.__swift5_types: 0x4
   __TEXT.__swift_as_entry: 0x24
   __TEXT.__swift_as_ret: 0x24
-  __TEXT.__unwind_info: 0x3520
+  __TEXT.__unwind_info: 0x3558
   __TEXT.__eh_frame: 0x378
   __DATA_CONST.__auth_got: 0x848
   __DATA_CONST.__got: 0x8e8
   __DATA_CONST.__auth_ptr: 0x20
-  __DATA_CONST.__const: 0xd5d8
+  __DATA_CONST.__const: 0xd5f8
   __DATA_CONST.__cfstring: 0xa860
   __DATA_CONST.__objc_classlist: 0x6d8
   __DATA_CONST.__objc_catlist: 0x50

   __DATA_CONST.__objc_floatobj: 0x30
   __DATA_CONST.__objc_dictobj: 0xc8
   __DATA_CONST.__linkguard: 0xe
-  __DATA.__objc_const: 0x19d08
-  __DATA.__objc_selrefs: 0x6798
-  __DATA.__objc_ivar: 0x10d4
+  __DATA.__objc_const: 0x19d48
+  __DATA.__objc_selrefs: 0x67e8
+  __DATA.__objc_ivar: 0x10d8
   __DATA.__objc_data: 0x44f0
   __DATA.__data: 0x2400
   __DATA.__bss: 0x808

   - /System/Library/PrivateFrameworks/AppleAccount.framework/AppleAccount
   - /System/Library/PrivateFrameworks/AssertionServices.framework/AssertionServices
   - /System/Library/PrivateFrameworks/AuthKit.framework/AuthKit
+  - /System/Library/PrivateFrameworks/BackgroundSystemTasks.framework/BackgroundSystemTasks
   - /System/Library/PrivateFrameworks/BaseBoard.framework/BaseBoard
   - /System/Library/PrivateFrameworks/BiometricKit.framework/BiometricKit
   - /System/Library/PrivateFrameworks/CoreCDP.framework/CoreCDP

   - /usr/lib/swift/libswiftCoreFoundation.dylib
   - /usr/lib/swift/libswiftCoreImage.dylib
   - /usr/lib/swift/libswiftCoreLocation.dylib
-  - /usr/lib/swift/libswiftDarwin.dylib
   - /usr/lib/swift/libswiftDispatch.dylib
   - /usr/lib/swift/libswiftMetal.dylib
   - /usr/lib/swift/libswiftOSLog.dylib

   - /usr/lib/swift/libswiftXPC.dylib
   - /usr/lib/swift/libswift_Builtin_float.dylib
   - /usr/lib/swift/libswift_Concurrency.dylib
-  - /usr/lib/swift/libswift_DarwinFoundation1.dylib
-  - /usr/lib/swift/libswift_DarwinFoundation2.dylib
-  - /usr/lib/swift/libswift_DarwinFoundation3.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  UUID: 7ED73AF0-0BAA-3C16-B2F4-14AB00202CA6
-  Functions: 6016
-  Symbols:   638
-  CStrings:  9912
+  UUID: 3DAF795A-1664-328F-A2DE-AE83FE34836A
+  Functions: 6033
+  Symbols:   634
+  CStrings:  9937
 
Symbols:
- __swift_FORCE_LOAD_$_swiftDarwin
- __swift_FORCE_LOAD_$_swift_DarwinFoundation1
- __swift_FORCE_LOAD_$_swift_DarwinFoundation2
- __swift_FORCE_LOAD_$_swift_DarwinFoundation3
CStrings:
+ "%s: Cleared a CFU"
+ "%s: Requested a CFU"
+ "%s: Timed out"
+ "-[FMDFMIPXPCServer clearTheftAndLossCFUWithReply:]"
+ "-[FMDFMIPXPCServer requestTheftAndLossCFUWithStrings:andReply:]"
+ "-[FMDSharedConfigurationManager clearTheftAndLossCFU]"
+ "-[FMDSharedConfigurationManager clearTheftAndLossCFU]_block_invoke_3"
+ "-[FMDSharedConfigurationManager requestTheftAndLossCFU:]"
+ "-[FMDSharedConfigurationManager requestTheftAndLossCFU:]_block_invoke_3"
+ "SecureLocationMonitor didUpdateLocations entered"
+ "SecureLocationMonitor didUpdateLocations for satellite location"
+ "T@\"NSObject<OS_dispatch_queue>\",&,N,V_stewieLocationManagerQueue"
+ "_stewieLocationManagerQueue"
+ "awarenessStrings"
+ "clearTheftAndLossCFU"
+ "clearTheftAndLossCFU:"
+ "clearTheftAndLossCFUWithReply:"
+ "com.apple.findmydevice.stewieLocationManagerQueue"
+ "deviceSupportsUltraLowPowerNetworking"
+ "liteLocationPublishRequestNotification:"
+ "requestTheftAndLossCFU:"
+ "requestTheftAndLossCFUWithString:andReply:"
+ "requestTheftAndLossCFUWithStrings:andReply:"
+ "setStewieLocationManagerQueue:"
+ "stewieLocationManagerQueue"
+ "v32@0:8@\"FMDSharedConfigurationFollowUpEntry\"16@?<v@?@\"NSError\">24"
- "com.apple.icloud.searchparty.secureLocations.stewiePublishRequest"

```
