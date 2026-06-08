## coreduetd

> `/usr/libexec/coreduetd`

```diff

-1933.11.0.0.0
-  __TEXT.__text: 0x22d6c
-  __TEXT.__auth_stubs: 0x960
-  __TEXT.__objc_stubs: 0x51a0
-  __TEXT.__objc_methlist: 0x19f0
-  __TEXT.__objc_classname: 0x1ba
-  __TEXT.__objc_methname: 0x640c
-  __TEXT.__objc_methtype: 0x1ce6
-  __TEXT.__const: 0xf0
-  __TEXT.__cstring: 0x1c56
-  __TEXT.__oslogstring: 0x3597
-  __TEXT.__gcc_except_tab: 0x5f4
+1956.0.1.0.0
+  __TEXT.__text: 0x21160
+  __TEXT.__auth_stubs: 0x9b0
+  __TEXT.__objc_stubs: 0x5280
+  __TEXT.__objc_methlist: 0x1a18
+  __TEXT.__objc_classname: 0x199
+  __TEXT.__cstring: 0x1c83
+  __TEXT.__objc_methname: 0x6580
+  __TEXT.__objc_methtype: 0x1d60
+  __TEXT.__const: 0x100
+  __TEXT.__oslogstring: 0x371d
+  __TEXT.__gcc_except_tab: 0x490
   __TEXT.__dlopen_cstrs: 0x116
-  __TEXT.__unwind_info: 0x828
-  __DATA_CONST.__auth_got: 0x4c0
-  __DATA_CONST.__got: 0x4a8
-  __DATA_CONST.__auth_ptr: 0x8
-  __DATA_CONST.__const: 0xee8
-  __DATA_CONST.__cfstring: 0x1680
+  __TEXT.__unwind_info: 0x808
+  __DATA_CONST.__const: 0xf50
+  __DATA_CONST.__cfstring: 0x16a0
   __DATA_CONST.__objc_classlist: 0x70
   __DATA_CONST.__objc_protolist: 0x40
   __DATA_CONST.__objc_imageinfo: 0x8

   __DATA_CONST.__objc_arraydata: 0x368
   __DATA_CONST.__objc_dictobj: 0x28
   __DATA_CONST.__objc_arrayobj: 0x18
-  __DATA.__objc_const: 0x24d8
-  __DATA.__objc_selrefs: 0x1798
-  __DATA.__objc_ivar: 0x19c
+  __DATA_CONST.__auth_got: 0x4e8
+  __DATA_CONST.__got: 0x4b8
+  __DATA_CONST.__auth_ptr: 0x8
+  __DATA.__objc_const: 0x2508
+  __DATA.__objc_selrefs: 0x17d8
+  __DATA.__objc_ivar: 0x1a0
   __DATA.__objc_data: 0x460
   __DATA.__data: 0x300
   __DATA.__bss: 0x120

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libsqlite3.dylib
-  UUID: C960D9A9-5390-3124-8029-361C344E89BE
-  Functions: 669
-  Symbols:   314
-  CStrings:  1943
+  UUID: 3AEF0025-3E90-35D0-A527-53E2E827766C
+  Functions: 668
+  Symbols:   321
+  CStrings:  1960
 
Symbols:
+ _OBJC_CLASS_$_NSJSONSerialization
+ _OBJC_CLASS_$__PSContactCatalog
+ _objc_claimAutoreleasedReturnValue
+ _objc_retainAutoreleaseReturnValue
+ _objc_retain_x4
+ _objc_retain_x5
+ _objc_retain_x7
+ _objc_retain_x9
+ _os_unfair_lock_lock
+ _os_unfair_lock_unlock
- _objc_autorelease
- _objc_retain_x26
- _objc_retain_x27
CStrings:
+ "B8@?0"
+ "Contact catalog regeneration completed: traceId=%{public}@, success=%d, contacts=%lu, sizeBytes=%lu, latencyMs=%.2f, didComputePhotoStats=%d, photoStatsLatencyMs=%.2f"
+ "Contact catalog regeneration skipped - already in progress, traceId=%{public}@"
+ "Contact catalog regeneration skipped - device locked, traceId=%{public}@"
+ "JSONObjectWithData:options:error:"
+ "Regenerating contact catalog for client %{public}@, traceId=%{public}@"
+ "_catalogRegenInProgress"
+ "contacts"
+ "dataUsingEncoding:"
+ "generateContactCatalog:keepGoing:maxInteractions:lookbackPeriodInMonths:updateCatalog:"
+ "lastGenerationDidComputePhotoStats"
+ "lastGenerationPhotoStatsLatencyMs"
+ "lengthOfBytesUsingEncoding:"
+ "regenerateContactCatalogWithTraceId:reply:"
+ "service:account:identifier:alternateCallbackID:willSendWithContext:"
+ "v32@0:8@\"NSString\"16@?<v@?BQQBd>24"
+ "v56@0:8@\"IDSService\"16@\"IDSAccount\"24@\"NSString\"32@\"NSString\"40@\"IDSWillSendContext\"48"

```
