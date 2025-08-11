## iOSDiagnostics

> `/System/Library/PrivateFrameworks/iOSDiagnostics.framework/iOSDiagnostics`

```diff

-1066.0.73.0.0
-  __TEXT.__text: 0x4dd0
-  __TEXT.__auth_stubs: 0x380
-  __TEXT.__objc_methlist: 0x8cc
+1066.2.1.0.0
+  __TEXT.__text: 0x502c
+  __TEXT.__auth_stubs: 0x3a0
+  __TEXT.__objc_methlist: 0x904
   __TEXT.__const: 0x88
   __TEXT.__cstring: 0xa30
   __TEXT.__oslogstring: 0x33b
   __TEXT.__gcc_except_tab: 0xd4
-  __TEXT.__unwind_info: 0x1d8
+  __TEXT.__unwind_info: 0x1e0
   __TEXT.__objc_classname: 0x269
-  __TEXT.__objc_methname: 0x159e
+  __TEXT.__objc_methname: 0x16c9
   __TEXT.__objc_methtype: 0x55f
-  __TEXT.__objc_stubs: 0x11a0
+  __TEXT.__objc_stubs: 0x1260
   __DATA_CONST.__got: 0x130
-  __DATA_CONST.__const: 0x320
+  __DATA_CONST.__const: 0x348
   __DATA_CONST.__objc_classlist: 0x40
   __DATA_CONST.__objc_protolist: 0x68
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x618
+  __DATA_CONST.__objc_selrefs: 0x648
   __DATA_CONST.__objc_protorefs: 0x30
   __DATA_CONST.__objc_superrefs: 0x28
   __DATA_CONST.__objc_arraydata: 0x8
-  __AUTH_CONST.__auth_got: 0x1d0
+  __AUTH_CONST.__auth_got: 0x1e0
   __AUTH_CONST.__const: 0x40
   __AUTH_CONST.__cfstring: 0x520
-  __AUTH_CONST.__objc_const: 0x19e0
+  __AUTH_CONST.__objc_const: 0x1a20
   __AUTH_CONST.__objc_arrayobj: 0x18
   __AUTH.__objc_data: 0x280
-  __DATA.__objc_ivar: 0x60
+  __DATA.__objc_ivar: 0x64
   __DATA.__data: 0x4e0
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/Foundation.framework/Foundation

   - /System/Library/PrivateFrameworks/RunningBoardServices.framework/RunningBoardServices
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 217436E8-9D0C-3818-AF61-0422E681751A
-  Functions: 158
-  Symbols:   765
-  CStrings:  444
+  UUID: 27C08E60-C8DD-336E-8EA2-0EF5B27D59DA
+  Functions: 163
+  Symbols:   785
+  CStrings:  453
 
Symbols:
+ -[DADiagnosticResponder autoBrightnessEnabledUserSetting]
+ -[DADiagnosticResponder resetScreenBrightness:]
+ -[DADiagnosticResponder screenBrightnessUserSetting]
+ -[DADiagnosticResponder setAutoBrightness:]
+ -[DADiagnosticResponder setAutoBrightnessEnabledUserSetting:]
+ -[DADiagnosticResponder setScreenBrightnessUserSetting:]
+ _BKSDisplayBrightnessIsAutoBrightnessAvailable
+ _BKSDisplayBrightnessSetAutoBrightnessEnabled
+ _OBJC_IVAR_$_DADiagnosticResponder._autoBrightnessEnabledUserSetting
+ ___47-[DADiagnosticResponder resetScreenBrightness:]_block_invoke
+ ___block_descriptor_50_e8_32bs_e5_v8?0ls32l8
+ _objc_msgSend$autoBrightnessEnabledUserSetting
+ _objc_msgSend$numberWithBool:
+ _objc_msgSend$screenBrightnessUserSetting
+ _objc_msgSend$setAutoBrightness:
+ _objc_msgSend$setAutoBrightnessEnabledUserSetting:
+ _objc_msgSend$setScreenBrightnessUserSetting:
- -[DADiagnosticResponder resetScreenBrightness]
- ___46-[DADiagnosticResponder resetScreenBrightness]_block_invoke
CStrings:
+ "T@\"NSNumber\",&,N,V_autoBrightnessEnabledUserSetting"
+ "T@\"NSNumber\",&,N,V_screenBrightnessUserSetting"
+ "_autoBrightnessEnabledUserSetting"
+ "autoBrightnessEnabledUserSetting"
+ "numberWithBool:"
+ "resetScreenBrightness:"
+ "screenBrightnessUserSetting"
+ "setAutoBrightness:"
+ "setAutoBrightnessEnabledUserSetting:"
+ "setScreenBrightnessUserSetting:"
- "resetScreenBrightness"

```
