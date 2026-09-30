## WeatherDaemon

> `/System/Library/PrivateFrameworks/WeatherDaemon.framework/WeatherDaemon`

```diff

-1444.1.0.0.0
-  __TEXT.__text: 0x240f18
+1454.1.0.0.0
+  __TEXT.__text: 0x240cbc
   __TEXT.__objc_methlist: 0x66c
   __TEXT.__const: 0x1aeb8
-  __TEXT.__cstring: 0x3e05
-  __TEXT.__oslogstring: 0xd365
+  __TEXT.__cstring: 0x3ec5
+  __TEXT.__oslogstring: 0xd3b5
   __TEXT.__constg_swiftt: 0x57e4
   __TEXT.__swift5_typeref: 0x5f96
   __TEXT.__swift5_builtin: 0xb4

   __TEXT.__swift_as_entry: 0x348
   __TEXT.__swift_as_ret: 0x324
   __TEXT.__swift_as_cont: 0x638
-  __TEXT.__swift5_capture: 0x2874
+  __TEXT.__swift5_capture: 0x28b4
   __TEXT.__swift5_mpenum: 0x44
-  __TEXT.__unwind_info: 0x9140
+  __TEXT.__unwind_info: 0x9138
   __TEXT.__eh_frame: 0x10180
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0

   __DATA_CONST.__objc_selrefs: 0x5d0
   __DATA_CONST.__objc_protorefs: 0x60
   __DATA_CONST.__objc_superrefs: 0x8
-  __DATA_CONST.__got: 0x1140
-  __AUTH_CONST.__const: 0x14230
+  __DATA_CONST.__got: 0x1138
+  __AUTH_CONST.__const: 0x142d0
   __AUTH_CONST.__cfstring: 0x60
   __AUTH_CONST.__objc_const: 0x41e0
   __AUTH_CONST.__auth_got: 0x3158

   - /usr/lib/swift/libswift_StringProcessing.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  Functions: 15315
+  Functions: 15329
   Symbols:   4103
-  CStrings:  1334
+  CStrings:  1337
 
CStrings:
+ "CREATE INDEX IF NOT EXISTS index_dayForecast_id_startsAt ON dayForecast (id, startsAt);"
+ "CREATE INDEX IF NOT EXISTS index_hourForecast_id_startsAt ON hourForecast (id, startsAt);"
+ "Failed to create granular forecast indices (cache usable, unindexed): %@"
```
