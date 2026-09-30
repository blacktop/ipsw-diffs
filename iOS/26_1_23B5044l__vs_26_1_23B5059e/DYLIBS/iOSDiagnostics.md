## iOSDiagnostics

> `/System/Library/PrivateFrameworks/iOSDiagnostics.framework/iOSDiagnostics`

```diff

-1066.40.34.0.0
-  __TEXT.__text: 0x5060
-  __TEXT.__auth_stubs: 0x3a0
-  __TEXT.__objc_methlist: 0x904
-  __TEXT.__const: 0x88
-  __TEXT.__cstring: 0xa30
-  __TEXT.__oslogstring: 0x33b
+1066.40.45.0.0
+  __TEXT.__text: 0x521c
+  __TEXT.__auth_stubs: 0x3d0
+  __TEXT.__objc_methlist: 0x91c
+  __TEXT.__const: 0x90
+  __TEXT.__cstring: 0xa51
+  __TEXT.__oslogstring: 0x396
   __TEXT.__gcc_except_tab: 0xd4
   __TEXT.__unwind_info: 0x1e8
   __TEXT.__objc_classname: 0x269
-  __TEXT.__objc_methname: 0x16d8
+  __TEXT.__objc_methname: 0x16e7
   __TEXT.__objc_methtype: 0x55f
-  __TEXT.__objc_stubs: 0x12a0
+  __TEXT.__objc_stubs: 0x12c0
   __DATA_CONST.__got: 0x128
   __DATA_CONST.__const: 0x348
   __DATA_CONST.__objc_classlist: 0x40
   __DATA_CONST.__objc_protolist: 0x68
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x658
+  __DATA_CONST.__objc_selrefs: 0x660
   __DATA_CONST.__objc_protorefs: 0x30
   __DATA_CONST.__objc_superrefs: 0x28
   __DATA_CONST.__objc_arraydata: 0x8
-  __AUTH_CONST.__auth_got: 0x1e0
-  __AUTH_CONST.__const: 0x40
-  __AUTH_CONST.__cfstring: 0x520
+  __AUTH_CONST.__auth_got: 0x1f8
+  __AUTH_CONST.__const: 0x60
+  __AUTH_CONST.__cfstring: 0x560
   __AUTH_CONST.__objc_const: 0x1a20
   __AUTH_CONST.__objc_arrayobj: 0x18
   __AUTH.__objc_data: 0x280
   __DATA.__objc_ivar: 0x64
   __DATA.__data: 0x4e0
+  __DATA.__bss: 0x10
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/Foundation.framework/Foundation
   - /System/Library/Frameworks/UIKit.framework/UIKit

   - /System/Library/PrivateFrameworks/RunningBoardServices.framework/RunningBoardServices
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: E8DC380B-4959-3B5C-85B8-9A4FFB088E3B
-  Functions: 163
-  Symbols:   786
-  CStrings:  455
+  UUID: ED47BDEB-DCD9-32F5-A1BA-BBA0B3F8DFB1
+  Functions: 166
+  Symbols:   800
+  CStrings:  463
 
Symbols:
+ +[DADiagnosticResponder sharedInstance]
+ +[DADiagnosticResponder sharedInstance].cold.1
+ _CFPreferencesGetAppBooleanValue
+ __OBJC_$_CLASS_METHODS_DADiagnosticResponder
+ ___39+[DADiagnosticResponder sharedInstance]_block_invoke
+ _dispatch_once
+ _objc_msgSend$sharedInstance
+ _objc_release_x1
+ _objc_retainAutoreleaseReturnValue
+ _sharedInstance.onceToken
+ _sharedInstance.singleton
- _BKSDisplayBrightnessIsAutoBrightnessAvailable
CStrings:
+ "BKEnableALS"
+ "Resetting auto screen brightness"
+ "Resetting screen brightness"
+ "Setting auto brightness to %d"
+ "com.apple.backboardd"
+ "sharedInstance"

```
