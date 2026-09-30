## IOMobileFramebuffer

> `/System/Library/PrivateFrameworks/IOMobileFramebuffer.framework/IOMobileFramebuffer`

```diff

-396.11.0.0.0
-  __TEXT.__text: 0xce18
-  __TEXT.__auth_stubs: 0x780
-  __TEXT.__const: 0xc0
-  __TEXT.__cstring: 0x19a2
-  __TEXT.__unwind_info: 0x390
-  __DATA_CONST.__got: 0x80
+397.9.0.0.0
+  __TEXT.__text: 0xd5e4
+  __TEXT.__auth_stubs: 0x790
+  __TEXT.__cstring: 0x1b0e
+  __TEXT.__const: 0xd8
+  __TEXT.__unwind_info: 0x3b0
+  __DATA_CONST.__got: 0x88
   __DATA_CONST.__const: 0xd8
-  __AUTH_CONST.__auth_got: 0x3c0
+  __AUTH_CONST.__auth_got: 0x3c8
   __AUTH_CONST.__auth_ptr: 0x8
-  __AUTH_CONST.__const: 0xb0
-  __AUTH_CONST.__cfstring: 0x7e0
-  __DATA.__data: 0x24
-  __DATA.__bss: 0x58
+  __AUTH_CONST.__const: 0x110
+  __AUTH_CONST.__cfstring: 0x800
+  __DATA.__data: 0x34
+  __DATA.__bss: 0x64
   __DATA_DIRTY.__data: 0xf0
-  __DATA_DIRTY.__bss: 0xc08
+  __DATA_DIRTY.__bss: 0xc10
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/IOKit.framework/Versions/A/IOKit
   - /System/Library/Frameworks/IOSurface.framework/IOSurface
   - /usr/lib/libSystem.B.dylib
-  Functions: 380
-  Symbols:   516
-  CStrings:  197
+  Functions: 400
+  Symbols:   538
+  CStrings:  208
 
Symbols:
+ _AppleDisplayManageDisplayWallDisable
+ _AppleDisplayManageDisplayWallEnable
+ _AppleDisplayManageDisplayWallStatus
+ _AppleDisplayManageDisplayWallValidateConfig
+ _AppleDisplayManagerDisplayWallEnumerate
+ _AppleDisplayManagerGetTypeID
+ _AppleDisplayManagerOpen
+ _AppleDisplayManagerOpenDefault
+ _IOMobileFramebufferSwapSetIndicatorBrightnessLimit
+ ___stdoutp
+ _fwrite
CStrings:
+ "<AppleDisplayManager %!p(MISSING) refcnt=%!d(MISSING)>"
+ "AppleDisplayManager"
+ "AppleDisplayManagerOpen"
+ "SwapSetIndicatorBrightnessLimit: Brightness control is not enabled\n"
+ "didn't find ADM service \n"
+ "found ADM service\n"
+ "kern_DisplayWallDisable called \n"
+ "kern_DisplayWallEnable called \n"
+ "kern_DisplayWallEnumerate called \n"
+ "kern_DisplayWallStatus called \n"
+ "kern_DisplayWallValidateConfig called \n"

```
