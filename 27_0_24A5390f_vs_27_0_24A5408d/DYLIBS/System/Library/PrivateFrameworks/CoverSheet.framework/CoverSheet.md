## CoverSheet

> `/System/Library/PrivateFrameworks/CoverSheet.framework/CoverSheet`

### Sections with Same Size but Changed Content

- `__DATA_CONST.__const`
- `__DATA_CONST.__objc_classlist`
- `__DATA_CONST.__objc_catlist`
- `__DATA_CONST.__objc_protolist`
- `__DATA_CONST.__objc_protorefs`
- `__DATA_CONST.__objc_superrefs`
- `__DATA_CONST.__objc_arraydata`
- `__AUTH_CONST.__const`
- `__AUTH_CONST.__objc_arrayobj`
- `__AUTH_CONST.__objc_intobj`
- `__AUTH_CONST.__objc_doubleobj`
- `__AUTH.__objc_data`
- `__DATA.__data`
- `__DATA_DIRTY.__objc_data`

```diff

-154.100.0.0.0
-  __TEXT.__text: 0x18c878
-  __TEXT.__objc_methlist: 0x16474
-  __TEXT.__const: 0x40f4
-  __TEXT.__cstring: 0xca68
-  __TEXT.__oslogstring: 0x8e9a
+159.0.2.0.0
+  __TEXT.__text: 0x18cbe4
+  __TEXT.__objc_methlist: 0x164bc
+  __TEXT.__const: 0x40fc
+  __TEXT.__cstring: 0xcb1a
+  __TEXT.__oslogstring: 0x8ef6
   __TEXT.__gcc_except_tab: 0x1270
   __TEXT.__ustring: 0xa4
   __TEXT.__dlopen_cstrs: 0x108
-  __TEXT.__unwind_info: 0x4848
+  __TEXT.__unwind_info: 0x4850
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0
   __TEXT.__objc_classname: 0x0

   __DATA_CONST.__objc_catlist: 0x38
   __DATA_CONST.__objc_protolist: 0x670
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0xc638
+  __DATA_CONST.__objc_selrefs: 0xc688
   __DATA_CONST.__objc_protorefs: 0x20
   __DATA_CONST.__objc_superrefs: 0x5f0
   __DATA_CONST.__objc_arraydata: 0x1078
-  __DATA_CONST.__got: 0x1588
+  __DATA_CONST.__got: 0x1590
   __AUTH_CONST.__const: 0xd10
-  __AUTH_CONST.__cfstring: 0xc7c0
-  __AUTH_CONST.__objc_const: 0x3c6c0
+  __AUTH_CONST.__cfstring: 0xc860
+  __AUTH_CONST.__objc_const: 0x3c750
   __AUTH_CONST.__objc_arrayobj: 0x1248
   __AUTH_CONST.__objc_intobj: 0x438
   __AUTH_CONST.__objc_doubleobj: 0x660
   __AUTH_CONST.__auth_got: 0xd28
   __AUTH.__objc_data: 0xf00
-  __DATA.__objc_ivar: 0x1b98
+  __DATA.__objc_ivar: 0x1ba4
   __DATA.__data: 0x56d0
   __DATA.__bss: 0x119
   __DATA.__common: 0x20

   - /usr/lib/libMobileGestalt.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 7937
-  Symbols:   18952
-  CStrings:  2657
+  Functions: 7943
+  Symbols:   18967
+  CStrings:  2663
 
Symbols:
+ -[CSCameraExtensionViewController _consumePendingLaunchActions]
+ -[CSCameraExtensionViewController didDeliverActionsToHostableEntity]
+ -[CSCameraExtensionViewController setDidDeliverActionsToHostableEntity:]
+ -[CSLockScreenPearlSettings matchPasscodeFallbackFailureSettings]
+ -[CSLockScreenPearlSettings matchPasscodeFallbackInterval]
+ -[CSLockScreenPearlSettings setMatchPasscodeFallbackFailureSettings:]
+ -[CSLockScreenPearlSettings setMatchPasscodeFallbackInterval:]
+ _OBJC_IVAR_$_CSCameraExtensionViewController._didDeliverActionsToHostableEntity
+ _OBJC_IVAR_$_CSLockScreenPearlSettings._matchPasscodeFallbackFailureSettings
+ _OBJC_IVAR_$_CSLockScreenPearlSettings._matchPasscodeFallbackInterval
+ _objc_msgSend$_FBSScene
+ _objc_msgSend$_consumePendingLaunchActions
+ _objc_msgSend$hardwareIdentifier
+ _objc_msgSend$serviceForDisplayUUID:
+ _objc_msgSend$setMatchPasscodeFallbackFailureSettings:
+ _objc_msgSend$setMatchPasscodeFallbackInterval:
+ _objc_msgSend$stringValue
- -[CSCameraExtensionViewController _launchActions]
- _objc_msgSend$_launchActions
CStrings:
+ "Face ID Match Passcode Fallback"
+ "Passcode Fallback Feedback"
+ "Passcode Fallback Interval (seconds, 0 disables)"
+ "[Notification Long Press Gesture] Window Scene is nil, will not send unocclude prox signal."
+ "matchPasscodeFallbackFailureSettings"
+ "matchPasscodeFallbackInterval"
```
