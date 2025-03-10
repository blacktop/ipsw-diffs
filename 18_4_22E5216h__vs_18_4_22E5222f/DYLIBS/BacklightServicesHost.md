## BacklightServicesHost

> `/System/Library/PrivateFrameworks/BacklightServicesHost.framework/BacklightServicesHost`

```diff

-4.4.30.0.0
-  __TEXT.__text: 0x86158
-  __TEXT.__auth_stubs: 0xa90
+4.4.31.0.0
+  __TEXT.__text: 0x8617c
+  __TEXT.__auth_stubs: 0xaa0
   __TEXT.__objc_methlist: 0x798c
   __TEXT.__const: 0x3b8
-  __TEXT.__gcc_except_tab: 0x10ac
-  __TEXT.__cstring: 0x66c7
+  __TEXT.__gcc_except_tab: 0x10b0
+  __TEXT.__cstring: 0x66f0
   __TEXT.__oslogstring: 0xf51b
   __TEXT.__ustring: 0x2fe
   __TEXT.__unwind_info: 0x21a8

   __DATA_CONST.__objc_selrefs: 0x3090
   __DATA_CONST.__objc_superrefs: 0x458
   __DATA_CONST.__objc_arraydata: 0x78
-  __AUTH_CONST.__auth_got: 0x558
+  __AUTH_CONST.__auth_got: 0x560
   __AUTH_CONST.__const: 0xb40
-  __AUTH_CONST.__cfstring: 0x62e0
+  __AUTH_CONST.__cfstring: 0x6300
   __AUTH_CONST.__objc_const: 0x138c8
   __AUTH_CONST.__objc_intobj: 0xc0
   __AUTH_CONST.__objc_dictobj: 0x28

   - /System/Library/PrivateFrameworks/FrontBoard.framework/FrontBoard
   - /System/Library/PrivateFrameworks/FrontBoardServices.framework/FrontBoardServices
   - /System/Library/PrivateFrameworks/LoggingSupport.framework/LoggingSupport
+  - /System/Library/PrivateFrameworks/OSAnalytics.framework/OSAnalytics
   - /System/Library/PrivateFrameworks/PowerExperience.framework/PowerExperience
   - /System/Library/PrivateFrameworks/RunningBoardServices.framework/RunningBoardServices
   - /System/Library/PrivateFrameworks/SystemWake.framework/SystemWake

   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libtailspin.dylib
   Functions: 3275
-  Symbols:   3928
-  CStrings:  4988
+  Symbols:   3929
+  CStrings:  4989
 
Symbols:
+ _WriteStackshotReport_async
CStrings:
+ "backlightservices watchdog hang detected"

```
