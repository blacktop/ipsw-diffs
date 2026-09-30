## NANDTaskScheduler

> `/usr/libexec/NANDTaskScheduler`

### Sections with Same Size but Changed Content

- `__TEXT.__objc_methlist`
- `__TEXT.__unwind_info`
- `__DATA_CONST.__const`
- `__DATA_CONST.__objc_classlist`
- `__DATA_CONST.__objc_protolist`
- `__DATA_CONST.__objc_protorefs`
- `__DATA_CONST.__objc_superrefs`
- `__DATA_CONST.__objc_arrayobj`
- `__DATA_CONST.__auth_ptr`
- `__DATA.__objc_const`
- `__DATA.__objc_data`
- `__DATA.__data`

```diff

-849.0.5.0.0
-  __TEXT.__text: 0xf904
+849.0.11.0.0
+  __TEXT.__text: 0xfdb4
   __TEXT.__auth_stubs: 0x810
-  __TEXT.__objc_stubs: 0x1600
+  __TEXT.__objc_stubs: 0x16a0
   __TEXT.__objc_methlist: 0x4c4
   __TEXT.__const: 0x1b0
   __TEXT.__gcc_except_tab: 0x294
-  __TEXT.__cstring: 0x12b4
-  __TEXT.__objc_methname: 0x15fe
-  __TEXT.__oslogstring: 0x2fcf
+  __TEXT.__cstring: 0x1323
+  __TEXT.__objc_methname: 0x16b2
+  __TEXT.__oslogstring: 0x30f5
   __TEXT.__objc_classname: 0xed
   __TEXT.__objc_methtype: 0x352
   __TEXT.__unwind_info: 0x310
   __DATA_CONST.__const: 0x690
-  __DATA_CONST.__cfstring: 0xa80
+  __DATA_CONST.__cfstring: 0xb20
   __DATA_CONST.__objc_classlist: 0x30
   __DATA_CONST.__objc_protolist: 0x20
   __DATA_CONST.__objc_imageinfo: 0x8

   __DATA_CONST.__objc_superrefs: 0x28
   __DATA_CONST.__objc_arraydata: 0x40
   __DATA_CONST.__objc_arrayobj: 0x48
-  __DATA_CONST.__objc_intobj: 0x18
+  __DATA_CONST.__objc_intobj: 0x30
   __DATA_CONST.__auth_got: 0x418
-  __DATA_CONST.__got: 0x1c0
+  __DATA_CONST.__got: 0x1d0
   __DATA_CONST.__auth_ptr: 0x8
   __DATA.__objc_const: 0xb10
-  __DATA.__objc_selrefs: 0x6d8
+  __DATA.__objc_selrefs: 0x700
   __DATA.__objc_ivar: 0x28
   __DATA.__objc_data: 0x1e0
   __DATA.__data: 0x618
   __DATA.__bss: 0x59
-  __DATA.__common: 0x68
+  __DATA.__common: 0x70
   - /System/Library/Frameworks/CoreData.framework/CoreData
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/Foundation.framework/Foundation

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
   Functions: 249
-  Symbols:   199
-  CStrings:  753
+  Symbols:   201
+  CStrings:  771
 
Symbols:
+ _OBJC_CLASS_$_BGSystemTaskProgressMetrics
+ _OBJC_CLASS_$_NSNumber
Functions:
~ sub_100007b10 : 284 -> 324
~ sub_100007c2c -> sub_100007c54 : 624 -> 748
~ sub_10000a354 -> sub_10000a3f8 : 7988 -> 8280
~ sub_10000d008 -> sub_10000d1d0 : 292 -> 320
~ sub_10000db18 -> sub_10000dcfc : 3072 -> 3788
CStrings:
+ "Failed to deregister selfActivations throughput: %@"
+ "Failed to register selfActivations throughput tracking: %@"
+ "Failed to report pctToHigh progress: %s"
+ "Failed to report pctToMed progress: %s"
+ "IdleStack poll: hourly stats pctToMed=%u pctToHigh=%u"
+ "Limited ping flavor (%s)."
+ "Restored limitedFlvr: %d"
+ "Task state saved persistently: stage=%d, sbarIdx=%u, priority=%d, limitedFlvr=%d"
+ "boolForKey:"
+ "dLastSelfActivations"
+ "dLimitedFlvr"
+ "idlestack.pctToHigh"
+ "idlestack.pctToMed"
+ "idlestack.selfActivations"
+ "initWithIdentifier:taskName:qos:workloadCategory:expectedMetricValue:itemsCompleted:totalItemCount:"
+ "new"
+ "numberWithUnsignedInt:"
+ "reportProgressMetrics:error:"
+ "report_hourly_stats - unexpected buf len %zu\n"
+ "resumed"
+ "setBool:forKey:"
- "Limited ping flavor requested."
- "No new slowInlineGC this round."
- "Task state saved persistently: stage=%d, sbarIdx=%u, priority=%d"
```
