## hangtracerd

> `/usr/libexec/hangtracerd`

```diff

-385.0.0.0.0
-  __TEXT.__text: 0x33be8
-  __TEXT.__auth_stubs: 0xee0
+397.0.0.0.0
+  __TEXT.__text: 0x34b80
+  __TEXT.__auth_stubs: 0xeb0
   __TEXT.__objc_stubs: 0x5580
-  __TEXT.__objc_methlist: 0x20a4
-  __TEXT.__const: 0x2d0
-  __TEXT.__cstring: 0x4891
+  __TEXT.__objc_methlist: 0x20d4
+  __TEXT.__const: 0x3c8
+  __TEXT.__gcc_except_tab: 0x3ac
+  __TEXT.__objc_methname: 0x8a1c
+  __TEXT.__cstring: 0x493d
+  __TEXT.__objc_classname: 0x32a
+  __TEXT.__objc_methtype: 0x1071
   __TEXT.__oslogstring: 0x6428
-  __TEXT.__objc_classname: 0x328
-  __TEXT.__objc_methname: 0x892c
-  __TEXT.__objc_methtype: 0x1055
-  __TEXT.__gcc_except_tab: 0x3b8
-  __TEXT.__unwind_info: 0xa40
-  __DATA_CONST.__auth_got: 0x780
+  __TEXT.__unwind_info: 0xb00
+  __DATA_CONST.__auth_got: 0x768
   __DATA_CONST.__got: 0x440
   __DATA_CONST.__auth_ptr: 0x10
-  __DATA_CONST.__const: 0x1f10
-  __DATA_CONST.__cfstring: 0x5e20
+  __DATA_CONST.__const: 0x1f78
+  __DATA_CONST.__cfstring: 0x5fc0
   __DATA_CONST.__objc_classlist: 0xf0
   __DATA_CONST.__objc_protolist: 0x58
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_protorefs: 0x8
   __DATA_CONST.__objc_superrefs: 0xa0
+  __DATA_CONST.__objc_intobj: 0x90
   __DATA_CONST.__objc_arraydata: 0x90
   __DATA_CONST.__objc_arrayobj: 0x18
-  __DATA_CONST.__objc_intobj: 0x90
-  __DATA_CONST.__objc_dictobj: 0x78
   __DATA_CONST.__objc_doubleobj: 0x10
-  __DATA.__objc_const: 0x4a40
-  __DATA.__objc_selrefs: 0x1b10
-  __DATA.__objc_ivar: 0x430
+  __DATA_CONST.__objc_dictobj: 0x78
+  __DATA.__objc_const: 0x4aa0
+  __DATA.__objc_selrefs: 0x1b28
+  __DATA.__objc_ivar: 0x438
   __DATA.__objc_data: 0x960
   __DATA.__data: 0x540
   __DATA.__bss: 0x538
-  __DATA.__common: 0x68
+  __DATA.__common: 0x70
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/CoreGraphics.framework/CoreGraphics
   - /System/Library/Frameworks/CoreServices.framework/CoreServices

   - /System/Library/Frameworks/UserNotifications.framework/UserNotifications
   - /System/Library/PrivateFrameworks/AppleMobileFileIntegrity.framework/AppleMobileFileIntegrity
   - /System/Library/PrivateFrameworks/CoreAnalytics.framework/CoreAnalytics
+  - /System/Library/PrivateFrameworks/CoreSVG.framework/CoreSVG
   - /System/Library/PrivateFrameworks/CoreSymbolication.framework/CoreSymbolication
   - /System/Library/PrivateFrameworks/CrashReporterSupport.framework/CrashReporterSupport
   - /System/Library/PrivateFrameworks/FrontBoardServices.framework/FrontBoardServices

   - /System/Library/PrivateFrameworks/SpringBoardServices.framework/SpringBoardServices
   - /System/Library/PrivateFrameworks/UIKitServices.framework/UIKitServices
   - /System/Library/PrivateFrameworks/ktrace.framework/ktrace
+  - /usr/lib/libIOReport.dylib
   - /usr/lib/libMemoryResourceException.dylib
   - /usr/lib/libMobileGestalt.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libarchive.2.dylib
   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libtailspin.dylib
-  UUID: B0957EF7-AA25-35DF-861E-C25389F0628B
-  Functions: 1161
-  Symbols:   389
-  CStrings:  3631
+  UUID: 066BB342-7E82-3A2C-99F0-66D20D143201
+  Functions: 1193
+  Symbols:   386
+  CStrings:  3666
 
Symbols:
+ _objc_retainAutoreleasedReturnValue
- _objc_claimAutoreleasedReturnValue
- _objc_retainAutoreleaseReturnValue
- _objc_retain_x3
- _objc_retain_x6
CStrings:
+ "@\"HTSystemConditionsColors\""
+ "ARKit"
+ "BackBoard"
+ "Camera"
+ "HangTracerEnableSystemConditionsHUD"
+ "Power Exceptions"
+ "SecInit"
+ "Security Soft Traps"
+ "T@\"HTSystemConditionsColors\",R,N,V_systemConditionsColors"
+ "TB,R,V_isSystemConditionsHUDEnabled"
+ "_isSystemConditionsHUDEnabled"
+ "_systemConditionsColors"
+ "arkit"
+ "backboard"
+ "camera"
+ "initPropertySystemConditionsHUDEnabled:"
+ "isSystemConditionsHUDEnabled"
+ "power exceptions"
+ "secinit"
+ "security soft traps"
+ "systemConditionsColors"
+ "\x91"

```
