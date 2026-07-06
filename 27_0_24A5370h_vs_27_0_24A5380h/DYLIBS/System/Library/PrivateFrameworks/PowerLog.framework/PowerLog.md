## PowerLog

> `/System/Library/PrivateFrameworks/PowerLog.framework/PowerLog`

```diff

-  __TEXT.__text: 0x1eac0
-  __TEXT.__objc_methlist: 0x14ac
+  __TEXT.__text: 0x1ee98
+  __TEXT.__objc_methlist: 0x150c
   __TEXT.__const: 0xf00
   __TEXT.__gcc_except_tab: 0x6c8
-  __TEXT.__cstring: 0x236f
-  __TEXT.__oslogstring: 0x3a03
+  __TEXT.__cstring: 0x23b6
+  __TEXT.__oslogstring: 0x3a2d
   __TEXT.__unwind_info: 0x7b8
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0
   __TEXT.__objc_classname: 0x0
   __TEXT.__objc_methname: 0x0
   __TEXT.__objc_methtype: 0x0
-  __DATA_CONST.__const: 0x660
+  __DATA_CONST.__const: 0x688
   __DATA_CONST.__objc_classlist: 0xa0
   __DATA_CONST.__objc_protolist: 0x28
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x1048
+  __DATA_CONST.__objc_selrefs: 0x1088
   __DATA_CONST.__objc_protorefs: 0x18
   __DATA_CONST.__objc_superrefs: 0x50
   __DATA_CONST.__objc_arraydata: 0x198
-  __DATA_CONST.__got: 0x1b8
+  __DATA_CONST.__got: 0x1c8
   __AUTH_CONST.__const: 0x540
-  __AUTH_CONST.__cfstring: 0x2920
-  __AUTH_CONST.__objc_const: 0x2238
+  __AUTH_CONST.__cfstring: 0x2980
+  __AUTH_CONST.__objc_const: 0x22c8
   __AUTH_CONST.__objc_intobj: 0x4c8
   __AUTH_CONST.__objc_arrayobj: 0x120
   __AUTH_CONST.__objc_doubleobj: 0x10
   __AUTH_CONST.__objc_dictobj: 0xc8
   __AUTH_CONST.__auth_got: 0x4c0
-  __AUTH.__objc_data: 0x410
-  __DATA.__objc_ivar: 0x1a8
+  __AUTH.__objc_data: 0x550
+  __DATA.__objc_ivar: 0x1b4
   __DATA.__data: 0x1e8
   __DATA.__bss: 0x160
   __DATA.__common: 0x8
-  __DATA_DIRTY.__objc_data: 0x230
+  __DATA_DIRTY.__objc_data: 0xf0
   __DATA_DIRTY.__data: 0x8
-  __DATA_DIRTY.__bss: 0x80
+  __DATA_DIRTY.__bss: 0x88
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/Foundation.framework/Foundation
   - /System/Library/PrivateFrameworks/AggregateDictionary.framework/AggregateDictionary

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libsqlite3.dylib
-  Functions: 825
-  Symbols:   2684
-  CStrings:  1010
+  Functions: 836
+  Symbols:   2719
+  CStrings:  1018
 
Sections:
~ __TEXT.__const : content changed
~ __TEXT.__gcc_except_tab : content changed
~ __TEXT.__unwind_info : content changed
~ __DATA_CONST.__objc_classlist : content changed
~ __DATA_CONST.__objc_protolist : content changed
~ __DATA_CONST.__objc_protorefs : content changed
~ __DATA_CONST.__objc_superrefs : content changed
~ __DATA_CONST.__objc_arraydata : content changed
~ __AUTH_CONST.__const : content changed
~ __AUTH_CONST.__objc_intobj : content changed
~ __AUTH_CONST.__objc_arrayobj : content changed
~ __AUTH_CONST.__objc_doubleobj : content changed
~ __AUTH_CONST.__objc_dictobj : content changed
~ __DATA.__data : content changed
~ __DATA_DIRTY.__data : content changed
Symbols:
+ -[PLClientLogger hasSeenFirstDrop]
+ -[PLClientLogger hourlyDropCount]
+ -[PLClientLogger hourlyWindowStart]
+ -[PLClientLogger sendHourlyDropSummaryWithTotalDrops:processName:]
+ -[PLClientLogger setHasSeenFirstDrop:]
+ -[PLClientLogger setHourlyDropCount:]
+ -[PLClientLogger setHourlyWindowStart:]
+ -[PLClientLogger trackHourlyClientDrops]
+ GCC_except_table53
+ GCC_except_table54
+ _OBJC_IVAR_$_PLClientLogger._hasSeenFirstDrop
+ _OBJC_IVAR_$_PLClientLogger._hourlyDropCount
+ _OBJC_IVAR_$_PLClientLogger._hourlyWindowStart
+ ___40-[PLClientLogger trackHourlyClientDrops]_block_invoke
+ ___40-[PLClientLogger trackHourlyClientDrops]_block_invoke_2
+ ___block_descriptor_52_e8_32s40s_e5_v8?0ls32l8s40l8
+ _isHourlyDropTrackingEnabled
+ _objc_msgSend$hasSeenFirstDrop
+ _objc_msgSend$hourlyDropCount
+ _objc_msgSend$hourlyWindowStart
+ _objc_msgSend$sendHourlyDropSummaryWithTotalDrops:processName:
+ _objc_msgSend$setHasSeenFirstDrop:
+ _objc_msgSend$setHourlyDropCount:
+ _objc_msgSend$setHourlyWindowStart:
+ _objc_msgSend$trackHourlyClientDrops
- GCC_except_table49
- GCC_except_table50
CStrings:
+ "ClientDroppedEvents: sending payload:  %@"
+ "Count"
+ "Process"
+ "XPCMetrics::ClientDroppedEvents"
+ "xpc_hourly_drop_tracking"

```
