## UsageTracking

> `/System/Library/PrivateFrameworks/UsageTracking.framework/UsageTracking`

```diff

-  __TEXT.__text: 0x29a90
-  __TEXT.__objc_methlist: 0x1704
+  __TEXT.__text: 0x2a118
+  __TEXT.__objc_methlist: 0x171c
   __TEXT.__const: 0x108
-  __TEXT.__gcc_except_tab: 0x784
+  __TEXT.__gcc_except_tab: 0x7a8
   __TEXT.__cstring: 0x1385
-  __TEXT.__oslogstring: 0x1268
+  __TEXT.__oslogstring: 0x1487
   __TEXT.__unwind_info: 0x720
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0
   __TEXT.__objc_classname: 0x0
   __TEXT.__objc_methname: 0x0
   __TEXT.__objc_methtype: 0x0
-  __DATA_CONST.__const: 0xec8
+  __DATA_CONST.__const: 0xef0
   __DATA_CONST.__objc_classlist: 0xc0
   __DATA_CONST.__objc_protolist: 0x48
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x1420
+  __DATA_CONST.__objc_selrefs: 0x1430
   __DATA_CONST.__objc_protorefs: 0x18
   __DATA_CONST.__objc_superrefs: 0x88
-  __DATA_CONST.__got: 0x318
+  __DATA_CONST.__got: 0x320
   __AUTH_CONST.__const: 0xc0
   __AUTH_CONST.__cfstring: 0xe80
-  __AUTH_CONST.__objc_const: 0x2930
+  __AUTH_CONST.__objc_const: 0x2960
   __AUTH_CONST.__objc_intobj: 0x60
   __AUTH_CONST.__auth_got: 0x0
-  __AUTH.__objc_data: 0x50
-  __DATA.__objc_ivar: 0x1a8
+  __AUTH.__objc_data: 0xf0
+  __DATA.__objc_ivar: 0x1ac
   __DATA.__data: 0x360
   __DATA.__bss: 0x10
-  __DATA_DIRTY.__objc_data: 0x730
+  __DATA_DIRTY.__objc_data: 0x690
   __DATA_DIRTY.__bss: 0x20
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/CoreServices.framework/CoreServices

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libicucore.A.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 614
-  Symbols:   2476
-  CStrings:  340
+  Functions: 623
+  Symbols:   2501
+  CStrings:  345
 
Sections:
~ __TEXT.__const : content changed
~ __TEXT.__cstring : content changed
~ __TEXT.__unwind_info : content changed
~ __DATA_CONST.__objc_classlist : content changed
~ __DATA_CONST.__objc_protolist : content changed
~ __DATA_CONST.__objc_protorefs : content changed
~ __DATA_CONST.__objc_superrefs : content changed
~ __AUTH_CONST.__const : content changed
~ __AUTH_CONST.__cfstring : content changed
~ __AUTH_CONST.__objc_intobj : content changed
~ __DATA.__data : content changed
Symbols:
+ -[USUsageAccumulator _accumulateIntelligenceUsage:timestamp:]
+ -[USUsageAccumulator intelligenceUsageStartDates]
+ GCC_except_table30
+ GCC_except_table65
+ _OBJC_CLASS_$_BMIntelligenceUsage
+ _OBJC_IVAR_$_USUsageAccumulator._intelligenceUsageStartDates
+ ___block_descriptor_64_e8_32s40s48s56r_e42_v32?0"USTrustIdentifier"8"NSDate"16^B24ls32l8s40l8s48l8r56l8
+ _objc_msgSend$_accumulateIntelligenceUsage:timestamp:
+ _objc_msgSend$intelligenceUsageStartDates
- GCC_except_table61
CStrings:
+ "Ignoring intelligence usage start event for %{public}@ at %{public}@ because it already started at %{public}@"
+ "Intelligence usage for %{public}@ start date: %{public}@ is later than end date: %{public}@"
+ "Received intelligence usage end event at %{public}@ for %{public}@ that is earlier than its start date: %{public}@"
+ "Received intelligence usage end event for %{private}@ without a corresponding start event. This may be because the event was manually ended due to a backlight end event."
+ "Received malformed intelligence usage event: %{public}@"

```
