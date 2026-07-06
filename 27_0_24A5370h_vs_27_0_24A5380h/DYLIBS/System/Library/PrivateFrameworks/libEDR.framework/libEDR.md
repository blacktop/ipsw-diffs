## libEDR

> `/System/Library/PrivateFrameworks/libEDR.framework/libEDR`

```diff

-  __TEXT.__text: 0xfac8
+  __TEXT.__text: 0xfac0
   __TEXT.__const: 0x1848
   __TEXT.__gcc_except_tab: 0x6fc
-  __TEXT.__oslogstring: 0xe25
-  __TEXT.__cstring: 0x1e49
+  __TEXT.__oslogstring: 0xe4a
+  __TEXT.__cstring: 0x1e21
   __TEXT.__unwind_info: 0x4d8
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0

   - /usr/lib/libobjc.A.dylib
   Functions: 237
   Symbols:   199
-  CStrings:  402
+  CStrings:  401
 
Sections:
~ __TEXT.__const : content changed
~ __TEXT.__gcc_except_tab : content changed
~ __TEXT.__unwind_info : content changed
~ __DATA_CONST.__const : content changed
~ __DATA_CONST.__weak_got : content changed
~ __DATA_CONST.__objc_selrefs : content changed
~ __AUTH_CONST.__const : content changed
~ __AUTH_CONST.__cfstring : content changed
~ __AUTH_CONST.__weak_auth_got : content changed
Functions:
~ _EDRServerSetDisplayBrightnessForDisplay : 852 -> 832
~ _EDRServerAddDisplay : 392 -> 396
~ sub_2b7ed4a4c -> sub_2b7fc0a3c : 820 -> 828
CStrings:
+ "libEDR - EDRServerSetDisplayBrightnessForDisplay: (display: %d, targetBrightness: %f, maxLuminance: %f, ambientIlluminance: %f, brightnessScaler: %f)\n"
- "EDRServerSetDisplayBrightnessForDisplay"
- "libEDR - %s: (display: %d, targetBrightness: %f, maxLuminance: %f, ambientIlluminance: %f, brightnessScaler: %f)\n"

```
