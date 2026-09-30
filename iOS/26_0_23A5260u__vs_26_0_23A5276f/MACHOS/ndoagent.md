## ndoagent

> `/System/Library/PrivateFrameworks/NewDeviceOutreach.framework/ndoagent`

```diff

-491.0.0.0.0
-  __TEXT.__text: 0x6d4f8
-  __TEXT.__auth_stubs: 0x2740
-  __TEXT.__objc_stubs: 0x30a0
-  __TEXT.__objc_methlist: 0x14ac
+494.0.0.0.0
+  __TEXT.__text: 0x6e298
+  __TEXT.__auth_stubs: 0x2770
+  __TEXT.__objc_stubs: 0x30c0
+  __TEXT.__objc_methlist: 0x14b4
   __TEXT.__const: 0x6b24
-  __TEXT.__gcc_except_tab: 0x430
-  __TEXT.__objc_methname: 0x3e45
-  __TEXT.__oslogstring: 0x3876
-  __TEXT.__cstring: 0x2a01
+  __TEXT.__gcc_except_tab: 0x4b0
+  __TEXT.__objc_methname: 0x3f01
+  __TEXT.__oslogstring: 0x38a6
+  __TEXT.__cstring: 0x2a51
   __TEXT.__objc_classname: 0x294
   __TEXT.__objc_methtype: 0xd35
-  __TEXT.__swift5_typeref: 0x1392
-  __TEXT.__swift5_capture: 0x62c
+  __TEXT.__swift5_typeref: 0x1410
+  __TEXT.__swift5_capture: 0x69c
   __TEXT.__swift5_fieldmd: 0xfe4
   __TEXT.__constg_swiftt: 0xeb4
   __TEXT.__swift5_reflstr: 0x5d1

   __TEXT.__swift5_assocty: 0x60
   __TEXT.__swift_as_entry: 0x48
   __TEXT.__swift_as_ret: 0x4c
-  __TEXT.__unwind_info: 0x1b70
-  __TEXT.__eh_frame: 0x1730
-  __DATA_CONST.__auth_got: 0x13b0
+  __TEXT.__unwind_info: 0x1be0
+  __TEXT.__eh_frame: 0x1738
+  __DATA_CONST.__auth_got: 0x13c8
   __DATA_CONST.__got: 0x958
-  __DATA_CONST.__auth_ptr: 0x788
-  __DATA_CONST.__const: 0x3a68
+  __DATA_CONST.__auth_ptr: 0x790
+  __DATA_CONST.__const: 0x3b60
   __DATA_CONST.__cfstring: 0x1320
   __DATA_CONST.__objc_classlist: 0x110
   __DATA_CONST.__objc_catlist: 0x10

   __DATA_CONST.__objc_arrayobj: 0x18
   __DATA_CONST.__objc_intobj: 0x48
   __DATA.__objc_const: 0x4bf8
-  __DATA.__objc_selrefs: 0x1098
+  __DATA.__objc_selrefs: 0x10c8
   __DATA.__objc_ivar: 0x84
   __DATA.__objc_data: 0xf20
   __DATA.__data: 0x1590
-  __DATA.__bss: 0x9950
-  __DATA.__common: 0x1f8
+  __DATA.__bss: 0x9960
+  __DATA.__common: 0x220
   - /System/Library/Frameworks/Accounts.framework/Accounts
   - /System/Library/Frameworks/CoreBluetooth.framework/CoreBluetooth
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
-  - /System/Library/Frameworks/CoreGraphics.framework/CoreGraphics
   - /System/Library/Frameworks/CoreServices.framework/CoreServices
   - /System/Library/Frameworks/Foundation.framework/Foundation
   - /System/Library/Frameworks/Security.framework/Security

   - /usr/lib/swift/libswiftCoreFoundation.dylib
   - /usr/lib/swift/libswiftCoreImage.dylib
   - /usr/lib/swift/libswiftCoreMIDI.dylib
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
-  UUID: 9F10BDCA-0297-3BCF-A5DF-09CCDC1BB427
-  Functions: 2390
-  Symbols:   1063
-  CStrings:  1509
+  UUID: AB70AD46-BE91-3402-B976-AEBA20C7E41C
+  Functions: 2417
+  Symbols:   1062
+  CStrings:  1518
 
Symbols:
+ _$s10Foundation10URLRequestV36_unconditionallyBridgeFromObjectiveCyACSo12NSURLRequestCSgFZ
+ _$s10Foundation10URLRequestVMa
+ _$s6NDOAPI12NDOURLClientP4load7request4withy10Foundation10URLRequestV_ys6ResultOyAG4DataV_So13NSURLResponseCts5Error_pGctFTj
+ _$s6NDOAPI19NDOURLSessionClientC7sessionACSo12NSURLSessionC_tcfc
+ _os_transaction_create
- _$s6NDOAPI19NDOURLSessionClientC6sessonACSo12NSURLSessionC_tcfc
- __swift_FORCE_LOAD_$_swiftDarwin
- __swift_FORCE_LOAD_$_swift_DarwinFoundation1
- __swift_FORCE_LOAD_$_swift_DarwinFoundation2
- __swift_FORCE_LOAD_$_swift_DarwinFoundation3
- _swift_retain_n
CStrings:
+ "CompositionLayer. Creating URL session client"
+ "[bluetooth_accessory] %s Unknown notification type, not updating the User Agent"
+ "com.apple.ndoagent.bluetoothAccessory"
+ "com.apple.ndoagent.checkIn"
+ "handleBluetoothNotificationWithCompletion:"
+ "loadWithRequest:completion:"
+ "performCheckIn:withCompletion:"
+ "processBluetoothNotificationWithCompletion:"
+ "setHTTPCookieStorage:"
+ "setRequestCachePolicy:"
+ "setURLCache:"
+ "setURLCredentialStorage:"
+ "set_alternativeServicesStorage:"
- "[bluetooth_accessory] %s Unknow notification type, not updating the User Agent"
- "handleBluetoothNotification"
- "performCheckIn:"
- "processBluetoothNotification"

```
