## NetAuth

> `/System/Library/PrivateFrameworks/NetAuth.framework/Versions/A/NetAuth`

### Sections with Same Size but Changed Content

- `__TEXT.__unwind_info`
- `__DATA_CONST.__const`
- `__AUTH_CONST.__const`

```diff

-183.6.3.0.0
-  __TEXT.__text: 0xb470
+183.6.5.0.0
+  __TEXT.__text: 0xb524
   __TEXT.__auth_stubs: 0x560
-  __TEXT.__cstring: 0xa15
+  __TEXT.__cstring: 0xab7
   __TEXT.__const: 0x148
   __TEXT.__unwind_info: 0x268
   __DATA_CONST.__got: 0x88
   __DATA_CONST.__const: 0x560
   __AUTH_CONST.__auth_got: 0x2b0
   __AUTH_CONST.__const: 0x768
-  __AUTH_CONST.__cfstring: 0x860
+  __AUTH_CONST.__cfstring: 0x8a0
   __DATA.__bss: 0x43c
   __DATA.__common: 0x38
   - /System/Library/Frameworks/CoreFoundation.framework/Versions/A/CoreFoundation

   - /System/Library/PrivateFrameworks/TCC.framework/Versions/A/TCC
   - /System/Library/PrivateFrameworks/login.framework/Versions/A/Frameworks/loginsupport.framework/Versions/A/loginsupport
   - /usr/lib/libSystem.B.dylib
-  Functions: 223
-  Symbols:   368
-  CStrings:  85
+  Functions: 224
+  Symbols:   369
+  CStrings:  87
 
Symbols:
+ __GetTCCServiceForPath
Functions:
~ _NARequestTCCAccessForMountPoint : 1508 -> 1380
+ __GetTCCServiceForPath
CStrings:
+ "NARequestTCCAccessForMountPoint: caller is not sandboxed - skipping TCC pre-check"
+ "NARequestTCCAccessForMountPoint: sandbox_check error %d - treating as sandboxed"
```
