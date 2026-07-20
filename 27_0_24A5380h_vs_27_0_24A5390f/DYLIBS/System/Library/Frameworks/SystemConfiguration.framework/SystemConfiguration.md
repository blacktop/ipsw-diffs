## SystemConfiguration

> `/System/Library/Frameworks/SystemConfiguration.framework/SystemConfiguration`

### Sections with Same Size but Changed Content

- `__TEXT.__const`
- `__DATA_CONST.__const`
- `__AUTH_CONST.__const`
- `__AUTH_CONST.__cfstring`

```diff

-1441.0.0.0.0
-  __TEXT.__text: 0x79760
+1444.0.0.0.0
+  __TEXT.__text: 0x7981c
   __TEXT.__const: 0x2c0
   __TEXT.__cstring: 0x6467
   __TEXT.__oslogstring: 0x58f5
-  __TEXT.__unwind_info: 0xd20
+  __TEXT.__unwind_info: 0xd28
   __TEXT.__auth_stubs: 0x0
   __DATA_CONST.__const: 0x2cd8
   __DATA_CONST.__got: 0x0
   __AUTH_CONST.__const: 0xbf0
   __AUTH_CONST.__cfstring: 0x6ce0
-  __AUTH_CONST.__auth_got: 0xf88
+  __AUTH_CONST.__auth_got: 0xf90
   __DATA.__data: 0x4c8
   __DATA.__crash_info: 0x148
   __DATA.__bss: 0x2d8

   - /System/Library/Frameworks/Security.framework/Security
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libbsm.0.dylib
-  Functions: 1309
-  Symbols:   2370
+  Functions: 1310
+  Symbols:   2372
   CStrings:  2039
 
Symbols:
+ ___SCNetworkReachabilityPathUsesCellular
+ _nw_interface_copy_delegate_interface
Functions:
~ ___SCNetworkReachabilityGetFlagsFromPath : 1316 -> 1304
+ ___SCNetworkReachabilityPathUsesCellular
```
