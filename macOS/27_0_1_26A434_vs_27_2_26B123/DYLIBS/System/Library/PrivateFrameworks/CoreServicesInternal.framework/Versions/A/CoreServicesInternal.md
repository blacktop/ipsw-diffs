## CoreServicesInternal

> `/System/Library/PrivateFrameworks/CoreServicesInternal.framework/Versions/A/CoreServicesInternal`

```diff

-609.0.0.0.0
-  __TEXT.__text: 0x36a40
+609.1.7.0.0
+  __TEXT.__text: 0x36cf8
   __TEXT.__lazy_helpers: 0x690
   __TEXT.__cstring: 0x2798
   __TEXT.__const: 0x4f0
-  __TEXT.__oslogstring: 0x2c24
-  __TEXT.__unwind_info: 0xcb0
+  __TEXT.__oslogstring: 0x2c68
+  __TEXT.__unwind_info: 0xcc0
   __TEXT.__auth_stubs: 0x0
   __DATA_CONST.__const: 0x320
   __DATA_CONST.__got: 0x0

   __AUTH_CONST.__cfstring: 0x1a80
   __AUTH_CONST.__weak_auth_got: 0x18
   __AUTH_CONST.__lazy_load_got: 0xa0
-  __AUTH_CONST.__auth_got: 0xe50
+  __AUTH_CONST.__auth_got: 0xe58
   __AUTH_CONST.__auth_ptr: 0x0
   __DATA.__data: 0x58
   __DATA.__bss: 0x490

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libc++.1.dylib
   - /usr/lib/libfakelink.dylib
-  Functions: 785
-  Symbols:   1508
-  CStrings:  649
+  Functions: 788
+  Symbols:   1512
+  CStrings:  650
 
Symbols:
+ _FSMountGetCachedVolumeSize
+ _FSURLGetCachedVolumeTotalCapacity
+ _MountInfoGetCachedVolumeSize
+ __FSURLGetCachedVolumeTotalCapacity
Functions:
~ __ZL16matchURLPropertyPK7__CFURLPK10__CFStringPKv : 264 -> 356
~ __RevocableBookmarksCopyClients : 432 -> 472
~ __RevocableBookmarksCopyClientBundleIdentifiers : 424 -> 452
+ __FSURLGetCachedVolumeTotalCapacity
+ _ConvertCFAbsoluteTimeToUTCDateTime
+ _FSURLGetCachedVolumeTotalCapacity.cold.1
CStrings:
+ "_FSURLGetCachedVolumeTotalCapacity: false result with no real error"
```
