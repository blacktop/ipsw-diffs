## replayd

> `/usr/libexec/replayd`

```diff

-558.51.0.0.0
-  __TEXT.__text: 0x52ef8
-  __TEXT.__auth_stubs: 0xe80
+558.52.1.2.0
+  __TEXT.__text: 0x53048
+  __TEXT.__auth_stubs: 0xec0
   __TEXT.__objc_stubs: 0x7660
   __TEXT.__objc_methlist: 0x35c8
   __TEXT.__const: 0x194
-  __TEXT.__objc_methname: 0xb0cd
-  __TEXT.__cstring: 0xaf05
-  __TEXT.__oslogstring: 0x7e8e
+  __TEXT.__objc_methname: 0xb0d7
+  __TEXT.__cstring: 0xaf22
+  __TEXT.__oslogstring: 0x7ec7
   __TEXT.__objc_classname: 0x635
-  __TEXT.__objc_methtype: 0x1caa
+  __TEXT.__objc_methtype: 0x1cb8
   __TEXT.__gcc_except_tab: 0x6e8
   __TEXT.__info_plist: 0x503
-  __TEXT.__unwind_info: 0x1010
-  __DATA_CONST.__auth_got: 0x750
+  __TEXT.__unwind_info: 0x1018
+  __DATA_CONST.__auth_got: 0x770
   __DATA_CONST.__got: 0x5c0
-  __DATA_CONST.__const: 0x15f0
+  __DATA_CONST.__const: 0x1618
   __DATA_CONST.__cfstring: 0x3300
   __DATA_CONST.__objc_classlist: 0x160
   __DATA_CONST.__objc_catlist: 0x28

   __DATA_CONST.__objc_superrefs: 0xf8
   __DATA_CONST.__objc_intobj: 0x258
   __DATA_CONST.__objc_doubleobj: 0x20
-  __DATA.__objc_const: 0x99f8
+  __DATA.__objc_const: 0x9a18
   __DATA.__objc_selrefs: 0x24a8
-  __DATA.__objc_ivar: 0x4e8
+  __DATA.__objc_ivar: 0x4ec
   __DATA.__objc_data: 0xdc0
   __DATA.__data: 0xa38
   __DATA.__bss: 0x1c0

   - /System/Library/Frameworks/SystemConfiguration.framework/SystemConfiguration
   - /System/Library/Frameworks/UserNotifications.framework/UserNotifications
   - /System/Library/Frameworks/VideoToolbox.framework/VideoToolbox
+  - /System/Library/PrivateFrameworks/AppleKeyStore.framework/AppleKeyStore
   - /System/Library/PrivateFrameworks/AssertionServices.framework/AssertionServices
   - /System/Library/PrivateFrameworks/BackBoardServices.framework/BackBoardServices
   - /System/Library/PrivateFrameworks/BaseBoard.framework/BaseBoard

   - /usr/lib/libMobileGestalt.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 1724
-  Symbols:   429
-  CStrings:  3563
+  Functions: 1726
+  Symbols:   433
+  CStrings:  3567
 
Symbols:
+ _AKSEventsRegister
+ _AKSEventsUnregister
+ _CFGetTypeID
+ _CFNumberGetTypeID
+ _kAKSInfoExtendedLockState
- _FBSDisplayLayoutElementLockScreenIdentifier
CStrings:
+ "\x12\x81\x131\xf0c"
+ " [ERROR] %!{(MISSING)public}s:%!d(MISSING) unable to register for lock event"
+ "^{_AKSEvent=}"
+ "_aksEvent"
+ "v20@?0i8^{__CFDictionary=}12"
- "\x12\x81\x13!\xf0c"

```