## PowerLog

> `/System/Library/PrivateFrameworks/PowerLog.framework/Versions/A/PowerLog`

```diff

-  __TEXT.__text: 0x1c324
-  __TEXT.__objc_methlist: 0x127c
+  __TEXT.__text: 0x1c724
+  __TEXT.__objc_methlist: 0x12dc
   __TEXT.__const: 0x1e0
   __TEXT.__gcc_except_tab: 0x694
-  __TEXT.__cstring: 0x206d
-  __TEXT.__oslogstring: 0x385b
-  __TEXT.__unwind_info: 0x718
+  __TEXT.__cstring: 0x20b4
+  __TEXT.__oslogstring: 0x3885
+  __TEXT.__unwind_info: 0x720
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0
   __TEXT.__objc_classname: 0x0

   __DATA_CONST.__objc_classlist: 0x98
   __DATA_CONST.__objc_protolist: 0x8
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0xdf8
+  __DATA_CONST.__objc_selrefs: 0xe38
   __DATA_CONST.__objc_protorefs: 0x8
   __DATA_CONST.__objc_superrefs: 0x50
   __DATA_CONST.__objc_arraydata: 0x178
-  __DATA_CONST.__got: 0x178
-  __AUTH_CONST.__const: 0x8a0
-  __AUTH_CONST.__cfstring: 0x2520
-  __AUTH_CONST.__objc_const: 0x1f70
+  __DATA_CONST.__got: 0x188
+  __AUTH_CONST.__const: 0x8d0
+  __AUTH_CONST.__cfstring: 0x2580
+  __AUTH_CONST.__objc_const: 0x2000
   __AUTH_CONST.__objc_intobj: 0x3d8
   __AUTH_CONST.__objc_arrayobj: 0x120
   __AUTH_CONST.__objc_doubleobj: 0x10
   __AUTH_CONST.__objc_dictobj: 0xa0
   __AUTH_CONST.__auth_got: 0x0
-  __AUTH.__objc_data: 0x3c0
-  __DATA.__objc_ivar: 0x1a0
+  __AUTH.__objc_data: 0x500
+  __DATA.__objc_ivar: 0x1ac
   __DATA.__data: 0x60
-  __DATA.__bss: 0x88
-  __DATA_DIRTY.__objc_data: 0x230
-  __DATA_DIRTY.__bss: 0x74
+  __DATA.__bss: 0x90
+  __DATA_DIRTY.__objc_data: 0xf0
+  __DATA_DIRTY.__bss: 0x71
   - /System/Library/Frameworks/CoreFoundation.framework/Versions/A/CoreFoundation
   - /System/Library/Frameworks/Foundation.framework/Versions/C/Foundation
   - /System/Library/PrivateFrameworks/CoreAnalytics.framework/Versions/A/CoreAnalytics
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libsqlite3.dylib
-  Functions: 785
-  Symbols:   1707
-  CStrings:  929
+  Functions: 796
+  Symbols:   1731
+  CStrings:  937
 
Sections:
~ __TEXT.__const : content changed
~ __TEXT.__gcc_except_tab : content changed
~ __DATA_CONST.__const : content changed
~ __DATA_CONST.__objc_classlist : content changed
~ __DATA_CONST.__objc_protolist : content changed
~ __DATA_CONST.__objc_protorefs : content changed
~ __DATA_CONST.__objc_superrefs : content changed
~ __DATA_CONST.__objc_arraydata : content changed
~ __AUTH_CONST.__objc_intobj : content changed
~ __AUTH_CONST.__objc_arrayobj : content changed
~ __AUTH_CONST.__objc_doubleobj : content changed
~ __AUTH_CONST.__objc_dictobj : content changed
~ __DATA.__data : content changed
Symbols:
+ -[PLClientLogger hasSeenFirstDrop]
+ -[PLClientLogger hourlyDropCount]
+ -[PLClientLogger hourlyWindowStart]
+ -[PLClientLogger sendHourlyDropSummaryWithTotalDrops:processName:]
+ -[PLClientLogger setHasSeenFirstDrop:]
+ -[PLClientLogger setHourlyDropCount:]
+ -[PLClientLogger setHourlyWindowStart:]
+ -[PLClientLogger trackHourlyClientDrops]
+ GCC_except_table62
+ GCC_except_table63
+ OBJC_IVAR_$_PLClientLogger._hasSeenFirstDrop
+ OBJC_IVAR_$_PLClientLogger._hourlyDropCount
+ OBJC_IVAR_$_PLClientLogger._hourlyWindowStart
+ __40-[PLClientLogger trackHourlyClientDrops]_block_invoke
+ ___40-[PLClientLogger trackHourlyClientDrops]_block_invoke
+ ___block_descriptor_52_e8_32s40s_e5_v8?0l
+ _isHourlyDropTrackingEnabled
+ _objc_msgSend$hasSeenFirstDrop
+ _objc_msgSend$hourlyDropCount
+ _objc_msgSend$hourlyWindowStart
+ _objc_msgSend$sendHourlyDropSummaryWithTotalDrops:processName:
+ _objc_msgSend$setHasSeenFirstDrop:
+ _objc_msgSend$setHourlyDropCount:
+ _objc_msgSend$setHourlyWindowStart:
+ _objc_msgSend$trackHourlyClientDrops
- GCC_except_table58
- GCC_except_table59
CStrings:
+ "ClientDroppedEvents: sending payload:  %@"
+ "Count"
+ "Process"
+ "XPCMetrics::ClientDroppedEvents"
+ "xpc_hourly_drop_tracking"

```
