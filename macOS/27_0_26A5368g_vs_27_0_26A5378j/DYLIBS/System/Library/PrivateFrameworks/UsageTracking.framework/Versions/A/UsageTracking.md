## UsageTracking

> `/System/Library/PrivateFrameworks/UsageTracking.framework/Versions/A/UsageTracking`

```diff

-  __TEXT.__text: 0x31510
-  __TEXT.__objc_methlist: 0x1694
+  __TEXT.__text: 0x31c0c
+  __TEXT.__objc_methlist: 0x16ac
   __TEXT.__const: 0x118
-  __TEXT.__gcc_except_tab: 0x9e4
+  __TEXT.__gcc_except_tab: 0xa08
   __TEXT.__cstring: 0x180f
-  __TEXT.__oslogstring: 0x1981
+  __TEXT.__oslogstring: 0x1ba0
   __TEXT.__unwind_info: 0x840
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0

   __DATA_CONST.__objc_classlist: 0xc0
   __DATA_CONST.__objc_protolist: 0x30
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x1398
+  __DATA_CONST.__objc_selrefs: 0x13a8
   __DATA_CONST.__objc_protorefs: 0x10
   __DATA_CONST.__objc_superrefs: 0x90
-  __DATA_CONST.__got: 0x360
-  __AUTH_CONST.__const: 0x1150
+  __DATA_CONST.__got: 0x368
+  __AUTH_CONST.__const: 0x1180
   __AUTH_CONST.__cfstring: 0x1320
-  __AUTH_CONST.__objc_const: 0x28c0
+  __AUTH_CONST.__objc_const: 0x28f0
   __AUTH_CONST.__objc_intobj: 0x60
   __AUTH_CONST.__auth_got: 0x0
-  __DATA.__objc_ivar: 0x1c0
+  __AUTH.__objc_data: 0xa0
+  __DATA.__objc_ivar: 0x1c4
   __DATA.__data: 0x240
   __DATA.__bss: 0x10
-  __DATA_DIRTY.__objc_data: 0x780
+  __DATA_DIRTY.__objc_data: 0x6e0
   __DATA_DIRTY.__bss: 0x30
   - /System/Library/Frameworks/CoreFoundation.framework/Versions/A/CoreFoundation
   - /System/Library/Frameworks/CoreServices.framework/Versions/A/CoreServices

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libicucore.A.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 716
-  Symbols:   1976
-  CStrings:  446
+  Functions: 724
+  Symbols:   1990
+  CStrings:  451
 
Sections:
~ __TEXT.__const : content changed
~ __TEXT.__cstring : content changed
~ __TEXT.__unwind_info : content changed
~ __DATA_CONST.__const : content changed
~ __DATA_CONST.__objc_classlist : content changed
~ __DATA_CONST.__objc_protolist : content changed
~ __DATA_CONST.__objc_protorefs : content changed
~ __DATA_CONST.__objc_superrefs : content changed
~ __AUTH_CONST.__cfstring : content changed
~ __AUTH_CONST.__objc_intobj : content changed
~ __DATA.__data : content changed
Symbols:
+ -[USUsageAccumulator _accumulateIntelligenceUsage:timestamp:]
+ -[USUsageAccumulator intelligenceUsageStartDates]
+ GCC_except_table32
+ GCC_except_table75
+ OBJC_IVAR_$_USUsageAccumulator._intelligenceUsageStartDates
+ _OBJC_CLASS_$_BMIntelligenceUsage
+ ___block_descriptor_64_e8_32s40s48s56r_e42_v32?0"USTrustIdentifier"8"NSDate"16^B24l
+ _objc_msgSend$_accumulateIntelligenceUsage:timestamp:
+ _objc_msgSend$intelligenceUsageStartDates
- GCC_except_table30
- GCC_except_table71
Functions:
~ -[USUsageAccumulator initWithApplicationCategories:webCategories:] : 452 -> 476
~ -[USUsageAccumulator accumulateEvent:timestamp:] : 436 -> 484
+ -[USUsageAccumulator _accumulateIntelligenceUsage:timestamp:]
~ -[USUsageAccumulator _stopAllUsageWithEndDate:] : 592 -> 732
+ __47-[USUsageAccumulator _stopAllUsageWithEndDate:]_block_invoke.17
~ -[USUsageAccumulator _aggregateStartDatesUsingEndDate:] : 2044 -> 2248
+ __55-[USUsageAccumulator _aggregateStartDatesUsingEndDate:]_block_invoke.28
+ -[USUsageAccumulator mediaNowPlayingStartDate]
~ -[USUsageAccumulator .cxx_destruct] : 236 -> 248
+ _OUTLINED_FUNCTION_5
+ -[USUsageAccumulator _accumulateIntelligenceUsage:timestamp:].cold.1
+ -[USUsageAccumulator _accumulateNotificationUsage:].cold.1
~ __47-[USUsageAccumulator _stopAllUsageWithEndDate:]_block_invoke.cold.1 : 132 -> 128
+ __47-[USUsageAccumulator _stopAllUsageWithEndDate:]_block_invoke.17.cold.1
CStrings:
+ "Ignoring intelligence usage start event for %{public}@ at %{public}@ because it already started at %{public}@"
+ "Intelligence usage for %{public}@ start date: %{public}@ is later than end date: %{public}@"
+ "Received intelligence usage end event at %{public}@ for %{public}@ that is earlier than its start date: %{public}@"
+ "Received intelligence usage end event for %{private}@ without a corresponding start event. This may be because the event was manually ended due to a backlight end event."
+ "Received malformed intelligence usage event: %{public}@"

```
