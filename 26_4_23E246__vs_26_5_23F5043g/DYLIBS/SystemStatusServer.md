## SystemStatusServer

> `/System/Library/PrivateFrameworks/SystemStatusServer.framework/SystemStatusServer`

```diff

-252.4.6.0.0
-  __TEXT.__text: 0x1e8e8
-  __TEXT.__auth_stubs: 0x6b0
+252.5.1.0.0
+  __TEXT.__text: 0x1eb70
+  __TEXT.__auth_stubs: 0x700
   __TEXT.__objc_methlist: 0x1be0
-  __TEXT.__const: 0xc8
-  __TEXT.__cstring: 0x19da
-  __TEXT.__gcc_except_tab: 0x2b0
+  __TEXT.__const: 0xd0
+  __TEXT.__dlopen_cstrs: 0x52
+  __TEXT.__cstring: 0x1a07
+  __TEXT.__gcc_except_tab: 0x2bc
   __TEXT.__oslogstring: 0xa5e
-  __TEXT.__unwind_info: 0x7b0
+  __TEXT.__unwind_info: 0x7b8
   __TEXT.__objc_classname: 0x87f
   __TEXT.__objc_methname: 0x5368
   __TEXT.__objc_methtype: 0x18e2
   __TEXT.__objc_stubs: 0x3c00
-  __DATA_CONST.__got: 0x428
-  __DATA_CONST.__const: 0xd18
+  __DATA_CONST.__got: 0x420
+  __DATA_CONST.__const: 0xd58
   __DATA_CONST.__objc_classlist: 0x118
   __DATA_CONST.__objc_protolist: 0xf0
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_selrefs: 0x1280
   __DATA_CONST.__objc_superrefs: 0xf8
-  __AUTH_CONST.__auth_got: 0x368
+  __AUTH_CONST.__auth_got: 0x390
   __AUTH_CONST.__const: 0x2a0
   __AUTH_CONST.__cfstring: 0x1620
   __AUTH_CONST.__objc_const: 0x3e50
   __DATA.__objc_ivar: 0x274
   __DATA.__data: 0xb40
+  __DATA.__bss: 0x10
   __DATA_DIRTY.__objc_ivar: 0x8
   __DATA_DIRTY.__objc_data: 0xaf0
   __DATA_DIRTY.__bss: 0x50

   - /System/Library/Frameworks/CoreServices.framework/CoreServices
   - /System/Library/Frameworks/CoreTelephony.framework/CoreTelephony
   - /System/Library/Frameworks/Foundation.framework/Foundation
-  - /System/Library/PrivateFrameworks/AppSupport.framework/AppSupport
   - /System/Library/PrivateFrameworks/BaseBoard.framework/BaseBoard
   - /System/Library/PrivateFrameworks/RunningBoardServices.framework/RunningBoardServices
+  - /System/Library/PrivateFrameworks/SoftLinking.framework/SoftLinking
   - /System/Library/PrivateFrameworks/SystemStatus.framework/SystemStatus
   - /System/Library/PrivateFrameworks/TelephonyUtilities.framework/TelephonyUtilities
   - /usr/lib/libMobileGestalt.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 2F2DAE0A-4271-3DF0-BD5F-03C835F3AFAC
-  Functions: 699
-  Symbols:   2778
-  CStrings:  1513
+  UUID: 0C441379-A779-3BB6-AD3E-01C3A18FD8B0
+  Functions: 702
+  Symbols:   2792
+  CStrings:  1517
 
Symbols:
+ _AppSupportLibraryCore
+ _AppSupportLibraryCore.frameworkLibrary
+ ___53-[STTelephonyStateProvider subscriptionInfoDidChange]_block_invoke.71
+ ___53-[STTelephonyStateProvider subscriptionInfoDidChange]_block_invoke_2.75
+ ___86-[STTelephonyStateProvider _updateLastKnownNetworkCountryCodeInContext:withCTContext:]_block_invoke.47
+ ___AppSupportLibraryCore_block_invoke
+ ___block_descriptor_40_e8_32r_e5_v8?0lr32l8
+ ___block_literal_global.40
+ ___getRadiosPreferencesClass_block_invoke
+ __sl_dlopen
+ _abort_report_np
+ _audit_stringAppSupport
+ _free
+ _getRadiosPreferencesClass.softClass
+ _objc_autorelease
+ _objc_getClass
- _OBJC_CLASS_$_RadiosPreferences
- ___53-[STTelephonyStateProvider subscriptionInfoDidChange]_block_invoke.72
- ___53-[STTelephonyStateProvider subscriptionInfoDidChange]_block_invoke_2.76
- ___86-[STTelephonyStateProvider _updateLastKnownNetworkCountryCodeInContext:withCTContext:]_block_invoke.48
- ___block_literal_global.41
CStrings:
+ "%s"
+ "RadiosPreferences"
+ "Unable to find class %s"
+ "softlink:o:path:/System/Library/PrivateFrameworks/AppSupport.framework/AppSupport"

```
