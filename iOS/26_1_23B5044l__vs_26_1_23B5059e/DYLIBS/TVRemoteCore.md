## TVRemoteCore

> `/System/Library/PrivateFrameworks/TVRemoteCore.framework/TVRemoteCore`

```diff

-548.10.16.0.0
-  __TEXT.__text: 0x41c20
-  __TEXT.__auth_stubs: 0x6f0
-  __TEXT.__objc_methlist: 0x59ac
+548.10.21.0.0
+  __TEXT.__text: 0x41e34
+  __TEXT.__auth_stubs: 0x700
+  __TEXT.__objc_methlist: 0x59c4
   __TEXT.__const: 0x230
   __TEXT.__gcc_except_tab: 0xbec
-  __TEXT.__cstring: 0x2f24
-  __TEXT.__oslogstring: 0x69c2
-  __TEXT.__unwind_info: 0xff8
+  __TEXT.__cstring: 0x2ff8
+  __TEXT.__oslogstring: 0x69f6
+  __TEXT.__unwind_info: 0x1000
   __TEXT.__objc_classname: 0x828
-  __TEXT.__objc_methname: 0xc7b9
+  __TEXT.__objc_methname: 0xc7dc
   __TEXT.__objc_methtype: 0x209c
-  __TEXT.__objc_stubs: 0x7ec0
-  __DATA_CONST.__got: 0x490
+  __TEXT.__objc_stubs: 0x7f00
+  __DATA_CONST.__got: 0x498
   __DATA_CONST.__const: 0x1390
   __DATA_CONST.__objc_classlist: 0x218
   __DATA_CONST.__objc_catlist: 0x10
   __DATA_CONST.__objc_protolist: 0xd0
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x2e40
+  __DATA_CONST.__objc_selrefs: 0x2e48
   __DATA_CONST.__objc_protorefs: 0x18
   __DATA_CONST.__objc_superrefs: 0x1a0
-  __DATA_CONST.__objc_arraydata: 0xd0
-  __AUTH_CONST.__auth_got: 0x388
+  __DATA_CONST.__objc_arraydata: 0x128
+  __AUTH_CONST.__auth_got: 0x390
   __AUTH_CONST.__const: 0x440
-  __AUTH_CONST.__cfstring: 0x3dc0
+  __AUTH_CONST.__cfstring: 0x3e80
   __AUTH_CONST.__objc_const: 0x8870
   __AUTH_CONST.__objc_intobj: 0x258
   __AUTH_CONST.__objc_dictobj: 0x78
-  __AUTH_CONST.__objc_arrayobj: 0x48
+  __AUTH_CONST.__objc_arrayobj: 0x60
   __AUTH_CONST.__objc_doubleobj: 0x50
   __AUTH.__objc_data: 0x13b0
   __DATA.__objc_ivar: 0x5ac

   - /usr/lib/libMobileGestalt.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 965C8A95-740A-3AA6-80E6-C32D9B60F40B
-  Functions: 1855
-  Symbols:   6317
-  CStrings:  4124
+  UUID: 12519EB3-A89F-30AD-B403-3ADFB7249A6D
+  Functions: 1858
+  Symbols:   6327
+  CStrings:  4139
 
Symbols:
+ +[TVRCFeatures _deleteGlobalPrefs]
+ +[TVRCFeatures _deleteGlobalPrefs].cold.1
+ +[TVRCFeatures initialize]
+ -[TVRXDevice extendedDescription]
+ _CFPreferencesAppSynchronize
+ _kCFPreferencesAnyApplication
+ _objc_msgSend$_deleteGlobalPrefs
+ _objc_msgSend$appendCollectionSection:withName:skipIfEmpty:
+ _objc_msgSend$deviceImplSet
- -[TVRXDevice conciseDescription]
- _objc_msgSend$appendClass:withName:
CStrings:
+ "Deleting keys from GlobalPrefs"
+ "Failed to synchronize GlobalPrefs"
+ "Removing preferred device identifier keys"
+ "TVRCMostRecentlyConnectedIDKey"
+ "TVRemoteHintsDebugUI"
+ "TVRemoteIncludeRTInInfoPanel"
+ "TVRemotePersistHintsUI"
+ "TVRemotePickerDebugUI"
+ "TVRemoteReplaceMuteButtonWithContextMenu"
+ "TVRemoteShowCastTab"
+ "TVRemoteSwapBackPlayPauseButtons"
+ "TVRemoteTTRDisabled"
+ "TVRemoteUIWakeToRemoteOnLockScreenDisabled"
+ "_deleteGlobalPrefs"
+ "appendCollectionSection:withName:skipIfEmpty:"
+ "initialize"
- "; alternate identifiers=%@"
- "; classification=%@"
- "; deviceImplSet=%@"
- "; ids=%@"
- "; impl=%@"
- "Removing old preferred device identifier user defaults"
- "appendClass:withName:"
- "conciseDescription"

```
