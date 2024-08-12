## CalendarDatabase

> `/System/Library/PrivateFrameworks/CalendarDatabase.framework/CalendarDatabase`

```diff

-1250.0.0.0.0
-  __TEXT.__text: 0xd789c
+1251.0.0.0.0
+  __TEXT.__text: 0xd7b54
   __TEXT.__auth_stubs: 0x1f90
   __TEXT.__objc_methlist: 0x19f0
-  __TEXT.__cstring: 0x1df7c
+  __TEXT.__cstring: 0x1dfe9
   __TEXT.__const: 0x74c
   __TEXT.__gcc_except_tab: 0x1880
   __TEXT.__oslogstring: 0xc122
   __TEXT.__dlopen_cstrs: 0x60
-  __TEXT.__unwind_info: 0x2b80
+  __TEXT.__unwind_info: 0x2b88
   __TEXT.__objc_classname: 0x567
   __TEXT.__objc_methname: 0x8cea
   __TEXT.__objc_methtype: 0x4513

   __AUTH_CONST.__auth_got: 0xfd8
   __AUTH_CONST.__auth_ptr: 0x10
   __AUTH_CONST.__const: 0x2150
-  __AUTH_CONST.__cfstring: 0xc4e0
+  __AUTH_CONST.__cfstring: 0xc520
   __AUTH_CONST.__objc_const: 0x3cb0
   __AUTH_CONST.__objc_arrayobj: 0x30
   __AUTH_CONST.__objc_intobj: 0x30
-  __AUTH.__objc_data: 0x910
+  __AUTH.__objc_data: 0x820
   __DATA.__objc_ivar: 0x1a0
   __DATA.__data: 0x700
   __DATA.__bss: 0x2d0
-  __DATA_DIRTY.__objc_data: 0x3c0
+  __DATA_DIRTY.__objc_data: 0x4b0
   __DATA_DIRTY.__data: 0x250
   __DATA_DIRTY.__common: 0x30
   __DATA_DIRTY.__bss: 0x170

   - /usr/lib/libcompression.dylib
   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libsqlite3.dylib
-  Functions: 4115
-  Symbols:   5606
-  CStrings:  4622
+  Functions: 4117
+  Symbols:   5608
+  CStrings:  4624
 
Symbols:
+ _CalEventCopyRowIDsAndUniqueIdentifiersInCalendar
CStrings:
+ "SELECT ROWID, unique_identifier FROM CalendarItem WHERE calendar_id = ?"
+ "commit at /Library/Caches/com.apple.xbs/Sources/CalendarDatabase/CalendarDatabase/CalEventOccurrenceCache.m:3694"
+ "commit at /Library/Caches/com.apple.xbs/Sources/CalendarDatabase/CalendarDatabase/CalEventOccurrenceCache.m:3728"
+ "commit at /Library/Caches/com.apple.xbs/Sources/CalendarDatabase/CalendarDatabase/CalEventOccurrenceCache.m:4110"
+ "occurrence_date > ? AND event_id = ?"
+ "read at /Library/Caches/com.apple.xbs/Sources/CalendarDatabase/CalendarDatabase/CalEventOccurrenceCache.m:2076"
+ "read at /Library/Caches/com.apple.xbs/Sources/CalendarDatabase/CalendarDatabase/CalEventOccurrenceCache.m:2192"
+ "read at /Library/Caches/com.apple.xbs/Sources/CalendarDatabase/CalendarDatabase/CalEventOccurrenceCache.m:2245"
+ "read at /Library/Caches/com.apple.xbs/Sources/CalendarDatabase/CalendarDatabase/CalEventOccurrenceCache.m:2663"
+ "read at /Library/Caches/com.apple.xbs/Sources/CalendarDatabase/CalendarDatabase/CalEventOccurrenceCache.m:2875"
+ "read at /Library/Caches/com.apple.xbs/Sources/CalendarDatabase/CalendarDatabase/CalEventOccurrenceCache.m:2962"
+ "read at /Library/Caches/com.apple.xbs/Sources/CalendarDatabase/CalendarDatabase/CalEventOccurrenceCache.m:3115"
+ "read at /Library/Caches/com.apple.xbs/Sources/CalendarDatabase/CalendarDatabase/CalEventOccurrenceCache.m:4083"
+ "rollback at /Library/Caches/com.apple.xbs/Sources/CalendarDatabase/CalendarDatabase/CalEventOccurrenceCache.m:2133"
+ "rollback at /Library/Caches/com.apple.xbs/Sources/CalendarDatabase/CalendarDatabase/CalEventOccurrenceCache.m:2196"
+ "rollback at /Library/Caches/com.apple.xbs/Sources/CalendarDatabase/CalendarDatabase/CalEventOccurrenceCache.m:2264"
+ "rollback at /Library/Caches/com.apple.xbs/Sources/CalendarDatabase/CalendarDatabase/CalEventOccurrenceCache.m:2691"
+ "rollback at /Library/Caches/com.apple.xbs/Sources/CalendarDatabase/CalendarDatabase/CalEventOccurrenceCache.m:2774"
+ "rollback at /Library/Caches/com.apple.xbs/Sources/CalendarDatabase/CalendarDatabase/CalEventOccurrenceCache.m:2947"
+ "rollback at /Library/Caches/com.apple.xbs/Sources/CalendarDatabase/CalendarDatabase/CalEventOccurrenceCache.m:3002"
+ "rollback at /Library/Caches/com.apple.xbs/Sources/CalendarDatabase/CalendarDatabase/CalEventOccurrenceCache.m:3169"
+ "rollback at /Library/Caches/com.apple.xbs/Sources/CalendarDatabase/CalendarDatabase/CalEventOccurrenceCache.m:4086"
+ "write at /Library/Caches/com.apple.xbs/Sources/CalendarDatabase/CalendarDatabase/CalEventOccurrenceCache.m:3665"
+ "write at /Library/Caches/com.apple.xbs/Sources/CalendarDatabase/CalendarDatabase/CalEventOccurrenceCache.m:3720"
+ "write at /Library/Caches/com.apple.xbs/Sources/CalendarDatabase/CalendarDatabase/CalEventOccurrenceCache.m:4094"
+ "write at /Library/Caches/com.apple.xbs/Sources/CalendarDatabase/CalendarDatabase/CalEventOccurrenceCache.m:4100"
- "commit at /Library/Caches/com.apple.xbs/Sources/CalendarDatabase/CalendarDatabase/CalEventOccurrenceCache.m:3675"
- "commit at /Library/Caches/com.apple.xbs/Sources/CalendarDatabase/CalendarDatabase/CalEventOccurrenceCache.m:3709"
- "commit at /Library/Caches/com.apple.xbs/Sources/CalendarDatabase/CalendarDatabase/CalEventOccurrenceCache.m:4091"
- "read at /Library/Caches/com.apple.xbs/Sources/CalendarDatabase/CalendarDatabase/CalEventOccurrenceCache.m:2077"
- "read at /Library/Caches/com.apple.xbs/Sources/CalendarDatabase/CalendarDatabase/CalEventOccurrenceCache.m:2173"
- "read at /Library/Caches/com.apple.xbs/Sources/CalendarDatabase/CalendarDatabase/CalEventOccurrenceCache.m:2226"
- "read at /Library/Caches/com.apple.xbs/Sources/CalendarDatabase/CalendarDatabase/CalEventOccurrenceCache.m:2644"
- "read at /Library/Caches/com.apple.xbs/Sources/CalendarDatabase/CalendarDatabase/CalEventOccurrenceCache.m:2856"
- "read at /Library/Caches/com.apple.xbs/Sources/CalendarDatabase/CalendarDatabase/CalEventOccurrenceCache.m:2943"
- "read at /Library/Caches/com.apple.xbs/Sources/CalendarDatabase/CalendarDatabase/CalEventOccurrenceCache.m:3096"
- "read at /Library/Caches/com.apple.xbs/Sources/CalendarDatabase/CalendarDatabase/CalEventOccurrenceCache.m:4064"
- "rollback at /Library/Caches/com.apple.xbs/Sources/CalendarDatabase/CalendarDatabase/CalEventOccurrenceCache.m:2116"
- "rollback at /Library/Caches/com.apple.xbs/Sources/CalendarDatabase/CalendarDatabase/CalEventOccurrenceCache.m:2177"
- "rollback at /Library/Caches/com.apple.xbs/Sources/CalendarDatabase/CalendarDatabase/CalEventOccurrenceCache.m:2245"
- "rollback at /Library/Caches/com.apple.xbs/Sources/CalendarDatabase/CalendarDatabase/CalEventOccurrenceCache.m:2672"
- "rollback at /Library/Caches/com.apple.xbs/Sources/CalendarDatabase/CalendarDatabase/CalEventOccurrenceCache.m:2755"
- "rollback at /Library/Caches/com.apple.xbs/Sources/CalendarDatabase/CalendarDatabase/CalEventOccurrenceCache.m:2928"
- "rollback at /Library/Caches/com.apple.xbs/Sources/CalendarDatabase/CalendarDatabase/CalEventOccurrenceCache.m:2983"
- "rollback at /Library/Caches/com.apple.xbs/Sources/CalendarDatabase/CalendarDatabase/CalEventOccurrenceCache.m:3150"
- "rollback at /Library/Caches/com.apple.xbs/Sources/CalendarDatabase/CalendarDatabase/CalEventOccurrenceCache.m:4067"
- "write at /Library/Caches/com.apple.xbs/Sources/CalendarDatabase/CalendarDatabase/CalEventOccurrenceCache.m:3646"
- "write at /Library/Caches/com.apple.xbs/Sources/CalendarDatabase/CalendarDatabase/CalEventOccurrenceCache.m:3701"
- "write at /Library/Caches/com.apple.xbs/Sources/CalendarDatabase/CalendarDatabase/CalEventOccurrenceCache.m:4075"
- "write at /Library/Caches/com.apple.xbs/Sources/CalendarDatabase/CalendarDatabase/CalEventOccurrenceCache.m:4081"

```
