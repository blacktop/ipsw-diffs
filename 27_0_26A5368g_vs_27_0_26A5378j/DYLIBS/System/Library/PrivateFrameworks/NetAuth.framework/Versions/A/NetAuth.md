## NetAuth

> `/System/Library/PrivateFrameworks/NetAuth.framework/Versions/A/NetAuth`

```diff

-  __TEXT.__text: 0xb4ec
-  __TEXT.__cstring: 0x9f6
+  __TEXT.__text: 0xb5e8
+  __TEXT.__cstring: 0xab7
   __TEXT.__const: 0x148
   __TEXT.__unwind_info: 0x268
   __TEXT.__auth_stubs: 0x0
   __DATA_CONST.__const: 0x560
   __DATA_CONST.__got: 0x0
   __AUTH_CONST.__const: 0x768
-  __AUTH_CONST.__cfstring: 0x840
+  __AUTH_CONST.__cfstring: 0x8a0
   __AUTH_CONST.__auth_got: 0x2b0
   __DATA.__bss: 0x43c
   __DATA.__common: 0x38

   - /System/Library/PrivateFrameworks/TCC.framework/Versions/A/TCC
   - /System/Library/PrivateFrameworks/login.framework/Versions/A/Frameworks/loginsupport.framework/Versions/A/loginsupport
   - /usr/lib/libSystem.B.dylib
-  Functions: 223
-  Symbols:   454
-  CStrings:  150
+  Functions: 224
+  Symbols:   455
+  CStrings:  156
 
Sections:
~ __TEXT.__unwind_info : content changed
~ __DATA_CONST.__const : content changed
~ __AUTH_CONST.__const : content changed
Symbols:
+ __GetTCCServiceForPath
Functions:
~ _NARequestTCCAccessForMountPoint : 1568 -> 1448
+ __GetTCCServiceForPath
~ _NATCCServiceForSubdirectory : 140 -> 144
~ _NATCCUsageDescriptionKeyForService : 136 -> 148
~ _NAUpdateAccount : 192 -> 240
CStrings:
+ "NARequestTCCAccessForMountPoint: caller is not sandboxed - skipping TCC pre-check"
+ "NARequestTCCAccessForMountPoint: sandbox_check error %d - treating as sandboxed"
+ "Update Account: no server port"

```
