## findmydeviced

> `/usr/libexec/findmydeviced`

```diff

-438.30.6.4.11
-  __TEXT.__text: 0x23b944
+438.31.8.11.1
+  __TEXT.__text: 0x23bb24
   __TEXT.__auth_stubs: 0xe70
-  __TEXT.__objc_stubs: 0x16800
+  __TEXT.__objc_stubs: 0x16880
   __TEXT.__objc_methlist: 0xe214
   __TEXT.__const: 0x2cd30
   __TEXT.__gcc_except_tab: 0x2b64
-  __TEXT.__objc_methname: 0x1c326
-  __TEXT.__oslogstring: 0x10963
+  __TEXT.__objc_methname: 0x1c3af
+  __TEXT.__oslogstring: 0x109b0
   __TEXT.__cstring: 0x8a67
   __TEXT.__objc_classname: 0x1aad
   __TEXT.__objc_methtype: 0x306d
   __TEXT.__unwind_info: 0x32d0
   __TEXT.__eh_frame: 0x50
   __DATA_CONST.__auth_got: 0x748
-  __DATA_CONST.__got: 0x8c8
+  __DATA_CONST.__got: 0x8d8
   __DATA_CONST.__auth_ptr: 0x8
-  __DATA_CONST.__const: 0xca58
+  __DATA_CONST.__const: 0xca98
   __DATA_CONST.__cfstring: 0xa8a0
   __DATA_CONST.__objc_classlist: 0x6d0
   __DATA_CONST.__objc_catlist: 0x60

   __DATA_CONST.__objc_dictobj: 0xc8
   __DATA_CONST.__linkguard: 0xe
   __DATA.__objc_const: 0x1c4f8
-  __DATA.__objc_selrefs: 0x6560
+  __DATA.__objc_selrefs: 0x6580
   __DATA.__objc_ivar: 0x10c4
   __DATA.__objc_data: 0x4420
   __DATA.__data: 0x2480

   - /System/Library/PrivateFrameworks/BaseBoard.framework/BaseBoard
   - /System/Library/PrivateFrameworks/BiometricKit.framework/BiometricKit
   - /System/Library/PrivateFrameworks/BluetoothManager.framework/BluetoothManager
+  - /System/Library/PrivateFrameworks/CoreCDP.framework/CoreCDP
   - /System/Library/PrivateFrameworks/FMCore.framework/FMCore
   - /System/Library/PrivateFrameworks/FMCoreLite.framework/FMCoreLite
   - /System/Library/PrivateFrameworks/FindMyDevice.framework/FindMyDevice

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/liblockdown.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 5846
-  Symbols:   581
-  CStrings:  8500
+  Functions: 5848
+  Symbols:   583
+  CStrings:  8506
 
Symbols:
+ _OBJC_CLASS_$_CDPStateController
+ _OBJC_CLASS_$_CDPContext
CStrings:
+ "unlockScreenTypeForPasscode:outSimplePasscodeType:"
+ "Could not update CDP with new passcode: %!@(MISSING)"
+ "Remote Lock: CDP update result %!i(MISSING)"
+ "contextForPrimaryAccount"
+ "initWithContext:"
+ "localSecretChangedTo:secretType:completion:"

```
