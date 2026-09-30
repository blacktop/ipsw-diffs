## BusinessChatService

> `/System/Library/PrivateFrameworks/BusinessChatService.framework/BusinessChatService`

```diff

-30114.32.10.7.1
-  __TEXT.__text: 0x6d678
-  __TEXT.__auth_stubs: 0x9c0
-  __TEXT.__objc_methlist: 0x795c
-  __TEXT.__const: 0x240
-  __TEXT.__cstring: 0x8b13
-  __TEXT.__oslogstring: 0x4e34
-  __TEXT.__gcc_except_tab: 0x7c0
-  __TEXT.__unwind_info: 0x1560
+30114.34.9.10.5
+  __TEXT.__text: 0x721bc
+  __TEXT.__auth_stubs: 0x960
+  __TEXT.__objc_methlist: 0x791c
+  __TEXT.__const: 0x248
+  __TEXT.__cstring: 0x8b19
+  __TEXT.__oslogstring: 0x4ed5
+  __TEXT.__gcc_except_tab: 0x768
+  __TEXT.__unwind_info: 0x18e0
   __TEXT.__objc_classname: 0x1771
-  __TEXT.__objc_methname: 0xadfe
+  __TEXT.__objc_methname: 0xadf3
   __TEXT.__objc_methtype: 0x3153
-  __TEXT.__objc_stubs: 0x7a60
+  __TEXT.__objc_stubs: 0x7a40
   __DATA_CONST.__got: 0x3c8
   __DATA_CONST.__const: 0x1cf0
   __DATA_CONST.__objc_classlist: 0x4a0
   __DATA_CONST.__objc_catlist: 0x20
   __DATA_CONST.__objc_protolist: 0x308
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x2778
+  __DATA_CONST.__objc_selrefs: 0x2770
   __DATA_CONST.__objc_protorefs: 0x50
   __DATA_CONST.__objc_superrefs: 0x388
-  __AUTH_CONST.__auth_got: 0x4f0
+  __AUTH_CONST.__auth_got: 0x4c0
   __AUTH_CONST.__const: 0x220
-  __AUTH_CONST.__cfstring: 0x4980
-  __AUTH_CONST.__objc_const: 0xfdb0
+  __AUTH_CONST.__cfstring: 0x49c0
+  __AUTH_CONST.__objc_const: 0xfda8
   __AUTH_CONST.__objc_intobj: 0x18
   __AUTH.__objc_data: 0x190
-  __DATA.__objc_ivar: 0x4d0
+  __DATA.__objc_ivar: 0x510
   __DATA.__data: 0x2460
   __DATA.__bss: 0x10
-  __DATA_DIRTY.__objc_ivar: 0x2f8
+  __DATA_DIRTY.__objc_ivar: 0x2b8
   __DATA_DIRTY.__objc_data: 0x2cb0
   __DATA_DIRTY.__bss: 0xa8
   __DATA_DIRTY.__common: 0x10

   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libsqlite3.dylib
   - /usr/lib/libz.1.dylib
-  UUID: 5F6151D6-2957-3D8B-B02B-990DAD0EA4BB
-  Functions: 2383
-  Symbols:   8382
-  CStrings:  4378
+  UUID: F6362F1E-0BDE-3F8F-8D65-BA49078F1257
+  Functions: 2381
+  Symbols:   8383
+  CStrings:  4384
 
Symbols:
+ -[BCSIdentityService serialDispatchQueue]
+ GCC_except_table11
+ GCC_except_table53
+ _BCSErrorBlastDoorError
+ _OBJC_IVAR_$_BCSBatchQuery._itemIdentifiers
+ _OBJC_IVAR_$_BCSBatchQuery._shardIdentifiers
+ _OBJC_IVAR_$_BCSConfigResolutionMetric.cacheHitMeasurement
+ _OBJC_IVAR_$_BCSConfigResolutionMetric.timingMeasurement
+ _OBJC_IVAR_$_BCSFlagMeasurement._flag
+ _OBJC_IVAR_$_BCSFlagMeasurement._flagMeasurementType
+ _OBJC_IVAR_$_BCSFlagMeasurement._flagWasSet
+ _OBJC_IVAR_$_BCSFlagMeasurement._realTimeMeasurementHandlers
+ _OBJC_IVAR_$_BCSItemResolutionMetric.cacheHitMeasurement
+ _OBJC_IVAR_$_BCSItemResolutionMetric.timingMeasurement
+ _OBJC_IVAR_$_BCSShardResolutionMetric.cacheHitMeasurement
+ _OBJC_IVAR_$_BCSShardResolutionMetric.timingMeasurement
+ _OBJC_IVAR_$_BCSTimingMeasurement._endDate
+ _OBJC_IVAR_$_BCSTimingMeasurement._realTimeMeasurementHandlers
+ _OBJC_IVAR_$_BCSTimingMeasurement._startDate
+ _OBJC_IVAR_$_BCSTimingMeasurement._timingMeasurementType
- -[BCSBusinessQueryService dealloc]
- -[BCSBusinessQueryService invalidate]
- -[BCSXPCDaemonConnection dealloc]
- -[BCSXPCDaemonConnection invalidate]
- GCC_except_table13
- GCC_except_table55
- _objc_claimAutoreleasedReturnValue
- _objc_msgSend$invalidate
- _objc_retainAutoreleaseReturnValue
- _objc_retain_x4
- _objc_retain_x5
- _objc_retain_x6
- _objc_retain_x9
CStrings:
+ "Error generating BlastDoor preview. sourceURL is nil."
+ "Failed to get image data from BlastDoor. Error: %@"
+ "Failed to write image data at URL %@ to disk. Error: %@"
+ "Image URL is nil"
+ "Safe image not obtained from BlastDoor"
+ "Unable to write data to disk"
- "Successfully fetched megashard of type %@ but did receive a valid config (nil)"
- "invalidate"

```
