## CalendarFoundation

> `/System/Library/PrivateFrameworks/CalendarFoundation.framework/CalendarFoundation`

```diff

-1547.0.0.0.0
-  __TEXT.__text: 0x555a8
+1547.1.1.1.0
+  __TEXT.__text: 0x55828
   __TEXT.__auth_stubs: 0x1070
-  __TEXT.__objc_methlist: 0x53c4
-  __TEXT.__cstring: 0x5fa2
+  __TEXT.__objc_methlist: 0x53dc
+  __TEXT.__cstring: 0x5fc2
   __TEXT.__const: 0x324
   __TEXT.__gcc_except_tab: 0x9d4
   __TEXT.__oslogstring: 0x353c

   __TEXT.__swift5_types: 0x8
   __TEXT.__unwind_info: 0x185c
   __TEXT.__objc_classname: 0xb4a
-  __TEXT.__objc_methname: 0xe288
+  __TEXT.__objc_methname: 0xe318
   __TEXT.__objc_methtype: 0x15c8
-  __TEXT.__objc_stubs: 0xa340
-  __DATA_CONST.__got: 0x2e0
-  __DATA_CONST.__const: 0x1610
+  __TEXT.__objc_stubs: 0xa3c0
+  __DATA_CONST.__got: 0x2e8
+  __DATA_CONST.__const: 0x1618
   __DATA_CONST.__objc_classlist: 0x320
   __DATA_CONST.__objc_catlist: 0xb0
   __DATA_CONST.__objc_protolist: 0xa8
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_const: 0x74d8
-  __DATA_CONST.__objc_selrefs: 0x3df0
+  __DATA_CONST.__objc_selrefs: 0x3e18
   __DATA_CONST.__objc_arraydata: 0x100
   __AUTH_CONST.__const: 0xc48
   __AUTH_CONST.__objc_const: 0x28a8
-  __AUTH_CONST.__cfstring: 0x8de0
+  __AUTH_CONST.__cfstring: 0x8e00
   __AUTH_CONST.__objc_arrayobj: 0x78
   __AUTH_CONST.__auth_got: 0x848
   __AUTH.__objc_data: 0xf00
   __AUTH.__data: 0x98
   __DATA.__objc_protorefs: 0x8
-  __DATA.__objc_classrefs: 0x410
+  __DATA.__objc_classrefs: 0x418
   __DATA.__objc_superrefs: 0x178
   __DATA.__objc_ivar: 0x314
   __DATA.__data: 0x970
-  __DATA.__bss: 0x5b0
+  __DATA.__bss: 0x5c0
   __DATA_DIRTY.__objc_data: 0xff0
   __DATA_DIRTY.__data: 0xc0
   __DATA_DIRTY.__bss: 0x340

   - /usr/lib/swift/libswiftObjectiveC.dylib
   - /usr/lib/swift/libswiftXPC.dylib
   - /usr/lib/swift/libswiftos.dylib
-  UUID: E64CF8EA-7ECD-3674-8939-06359EC6A3A8
-  Functions: 2390
-  Symbols:   8184
-  CStrings:  5361
+  UUID: 6890216C-3B6E-3C89-AC42-671B53C82968
+  Functions: 2392
+  Symbols:   8196
+  CStrings:  5368
 
Symbols:
+ +[CalChronometry _resetTodayRolloverTimer]
+ +[CalChronometry _todayRolloverTimerFired]
+ +[NSDate(CalClassAdditions) CalDateRangeStringWithStart:end:]
+ _CalChronometryTodayChangedNotification
+ _NSSystemClockDidChangeNotification
+ _OBJC_CLASS_$_NSTimer
+ __todayRolloverTimer
+ _objc_msgSend$_resetTodayRolloverTimer
+ _objc_msgSend$invalidate
+ _objc_msgSend$scheduledTimerWithTimeInterval:target:selector:userInfo:repeats:
+ _objc_msgSend$systemTimeZone
- +[NSDate(CalClassAdditions) CalTimeRangeStringWithStart:end:]
CStrings:
+ "CalChronometryTodayChangedNotification"
+ "CalDateRangeStringWithStart:end:"
+ "Date range %@ to %@"
+ "_resetTodayRolloverTimer"
+ "_todayRolloverTimerFired"
+ "invalidate"
+ "scheduledTimerWithTimeInterval:target:selector:userInfo:repeats:"
+ "systemTimeZone"
- "CalTimeRangeStringWithStart:end:"
- "Time range %@ to %@"

```
