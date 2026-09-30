## WeatherCore

> `/System/Library/PrivateFrameworks/WeatherCore.framework/Versions/A/WeatherCore`

```diff

-764.0.0.0.0
-  __TEXT.__text: 0x1f565c
+768.0.0.0.0
+  __TEXT.__text: 0x1f5978
   __TEXT.__auth_stubs: 0x4380
-  __TEXT.__objc_methlist: 0x5c0
-  __TEXT.__const: 0x1811c
+  __TEXT.__objc_methlist: 0x5d8
+  __TEXT.__const: 0x1812c
   __TEXT.__cstring: 0xcea8
-  __TEXT.__oslogstring: 0xad97
+  __TEXT.__oslogstring: 0xad77
   __TEXT.__swift5_typeref: 0x7221
-  __TEXT.__swift5_fieldmd: 0x6088
-  __TEXT.__constg_swiftt: 0x58b0
-  __TEXT.__swift5_reflstr: 0x5841
+  __TEXT.__swift5_fieldmd: 0x60a0
+  __TEXT.__constg_swiftt: 0x58b8
+  __TEXT.__swift5_reflstr: 0x5871
   __TEXT.__swift5_builtin: 0x64
   __TEXT.__swift5_assocty: 0xfe0
   __TEXT.__swift5_protos: 0x154

   __TEXT.__swift5_types: 0x66c
   __TEXT.__swift5_capture: 0x1f14
   __TEXT.__swift5_mpenum: 0x18
-  __TEXT.__unwind_info: 0x8700
-  __TEXT.__eh_frame: 0xa478
+  __TEXT.__unwind_info: 0x8708
+  __TEXT.__eh_frame: 0xa474
   __TEXT.__objc_classname: 0x11a
-  __TEXT.__objc_methname: 0x569f
+  __TEXT.__objc_methname: 0x56bf
   __TEXT.__objc_methtype: 0xd2c
-  __TEXT.__objc_stubs: 0xc40
+  __TEXT.__objc_stubs: 0xca0
   __DATA_CONST.__got: 0xdf0
   __DATA_CONST.__const: 0x2b8
   __DATA_CONST.__objc_classlist: 0x3a8
   __DATA_CONST.__objc_catlist: 0x38
   __DATA_CONST.__objc_protolist: 0x60
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0xa48
+  __DATA_CONST.__objc_selrefs: 0xa50
   __DATA_CONST.__objc_protorefs: 0x38
   __DATA_CONST.__objc_superrefs: 0x30
   __DATA_CONST.__objc_arraydata: 0x10
   __AUTH_CONST.__auth_got: 0x21c8
   __AUTH_CONST.__auth_ptr: 0x1cc8
-  __AUTH_CONST.__const: 0x10700
+  __AUTH_CONST.__const: 0x10728
   __AUTH_CONST.__cfstring: 0x3a0
   __AUTH_CONST.__objc_const: 0x9f48
   __AUTH_CONST.__objc_arrayobj: 0x18
   __AUTH_CONST.__objc_intobj: 0x18
   __AUTH.__objc_data: 0xd40
-  __AUTH.__data: 0x5f30
+  __AUTH.__data: 0x5f38
   __DATA.__objc_ivar: 0x44
   __DATA.__data: 0x5fa0
   __DATA.__bss: 0x2b0f0

   - /usr/lib/swift/libswift_StringProcessing.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  Functions: 13672
-  Symbols:   6404
+  Functions: 13681
+  Symbols:   6412
   CStrings:  1251
 
Symbols:
+ +[WCCloudMigrator isRunningInTheWeatherAppProcess]
+ __38-[WCCloudMigrator eraseStoreIfNeeded:]_block_invoke.7
+ __56-[WCCloudMigrator migrateStore:toStore:completionBlock:]_block_invoke.2.cold.1
+ __56-[WCCloudMigrator migrateStore:toStore:completionBlock:]_block_invoke.3
+ __OBJC_$_CLASS_METHODS_WCCloudMigrator
+ _objc_msgSend$bundleIdentifier
+ _objc_msgSend$isRunningInTheWeatherAppProcess
+ _objc_msgSend$mainBundle
- __38-[WCCloudMigrator eraseStoreIfNeeded:]_block_invoke.6
- __56-[WCCloudMigrator migrateStore:toStore:completionBlock:]_block_invoke.1
- __56-[WCCloudMigrator migrateStore:toStore:completionBlock:]_block_invoke.1.cold.1
CStrings:
+ "The location is already in your list."
+ "shouldTrackComponentExposureEvents"
- "/api/v1/weather/{lang}/{latitude}/{longitude}"
- "Cannot add location as it is already saved."

```
