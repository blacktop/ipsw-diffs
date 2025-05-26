## SoftwareUpdateServicesUI

> `/System/Library/PrivateFrameworks/SoftwareUpdateServicesUI.framework/SoftwareUpdateServicesUI`

```diff

-185.0.0.0.0
-  __TEXT.__text: 0x873c
+192.40.1.0.0
+  __TEXT.__text: 0x8820
   __TEXT.__auth_stubs: 0x2f0
-  __TEXT.__objc_methlist: 0x844
+  __TEXT.__objc_methlist: 0x864
   __TEXT.__const: 0x80
-  __TEXT.__cstring: 0xca0
+  __TEXT.__cstring: 0xcbd
   __TEXT.__oslogstring: 0x39c
   __TEXT.__gcc_except_tab: 0x50
   __TEXT.__unwind_info: 0x13c
   __TEXT.__objc_classname: 0x291
-  __TEXT.__objc_methname: 0x1758
-  __TEXT.__objc_methtype: 0x388
-  __TEXT.__objc_stubs: 0x1060
+  __TEXT.__objc_methname: 0x17e0
+  __TEXT.__objc_methtype: 0x387
+  __TEXT.__objc_stubs: 0x1080
   __DATA_CONST.__got: 0x38
-  __DATA_CONST.__const: 0xfe0
+  __DATA_CONST.__const: 0xff0
   __DATA_CONST.__objc_classlist: 0x88
   __DATA_CONST.__objc_catlist: 0x10
   __DATA_CONST.__objc_protolist: 0x28
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_const: 0x15e0
-  __DATA_CONST.__objc_selrefs: 0x688
+  __DATA_CONST.__objc_const: 0x1680
+  __DATA_CONST.__objc_selrefs: 0x6a0
   __AUTH_CONST.__objc_const: 0x620
-  __AUTH_CONST.__cfstring: 0xf80
+  __AUTH_CONST.__cfstring: 0xfc0
   __AUTH_CONST.__auth_ptr: 0x8
   __AUTH_CONST.__const: 0x120
   __AUTH_CONST.__auth_got: 0x188

   __DATA.__objc_protorefs: 0x18
   __DATA.__objc_classrefs: 0x100
   __DATA.__objc_superrefs: 0x40
-  __DATA.__objc_ivar: 0x7c
+  __DATA.__objc_ivar: 0x88
   __DATA.__data: 0x280
   __DATA.__bss: 0x48
   __DATA_DIRTY.__objc_data: 0x140

   - /System/Library/PrivateFrameworks/SoftwareUpdateServices.framework/SoftwareUpdateServices
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 208
-  Symbols:   1313
-  CStrings:  533
+  Functions: 211
+  Symbols:   1325
+  CStrings:  543
 
Symbols:
+ -[SUSUIAuthenticationAlertAction autoInstallForecast]
+ -[SUSUIAuthenticationAlertAction initWithDescriptor:autoInstallForecast:forInstallTonight:canDeferInstallation:completionQueue:completionBlock:]
+ -[SUSUICommandLineToolClient ddmInstallNow]
+ -[SUSUIPreferences IWillRebootLater]
+ -[SUSUIPreferences isSharedIPad]
+ _OBJC_IVAR_$_SUSUIAuthenticationAlertAction._autoInstallForecast
+ _OBJC_IVAR_$_SUSUIPreferences._IWillRebootLater
+ _OBJC_IVAR_$_SUSUIPreferences._isSharedIPad
+ _OBJC_IVAR_$_SUSUIPreferences._isSharedIpad
+ _SUSUIAuthenticationAlertActionInputAutoInstallForecast
+ ___144-[SUSUIAuthenticationAlertAction initWithDescriptor:autoInstallForecast:forInstallTonight:canDeferInstallation:completionQueue:completionBlock:]_block_invoke
+ _kSUSUIPreferenceIWillRebootLater
+ _kSUSUIPreferenceIsSharedIPad
+ _objc_msgSend$ddmInstallNow
- -[SUSUIAuthenticationAlertAction autoInstallOperation]
- -[SUSUIAuthenticationAlertAction initWithDescriptor:autoInstallOperation:forInstallTonight:canDeferInstallation:completionQueue:completionBlock:]
- _OBJC_IVAR_$_SUSUIAuthenticationAlertAction._autoInstallOperation
- _SUSUIAuthenticationAlertActionInputAutoInstallOperation
- ___145-[SUSUIAuthenticationAlertAction initWithDescriptor:autoInstallOperation:forInstallTonight:canDeferInstallation:completionQueue:completionBlock:]_block_invoke
CStrings:
+ "@\"SUAutoInstallForecast\""
+ "IWillRebootLater"
+ "T@\"SUAutoInstallForecast\",R,&,N"
+ "TB,R,N,V_IWillRebootLater"
+ "TB,R,N,V_isSharedIPad"
+ "_IWillRebootLater"
+ "_autoInstallForecast"
+ "_isSharedIPad"
+ "_isSharedIpad"
+ "_susAutoInstallForecast"
+ "autoInstallForecast"
+ "ddmInstallNow"
+ "initWithDescriptor:autoInstallForecast:forInstallTonight:canDeferInstallation:completionQueue:completionBlock:"
+ "isSharedIPad"
- "@\"SUAutoInstallOperation\""
- "T@\"SUAutoInstallOperation\",R,&,N"
- "_autoInstallOperation"
- "_susAutoInstallOperation"
- "autoInstallOperation"
- "initWithDescriptor:autoInstallOperation:forInstallTonight:canDeferInstallation:completionQueue:completionBlock:"

```
