## DialogEngine

> `/System/Library/PrivateFrameworks/DialogEngine.framework/DialogEngine`

```diff

-3401.2.1.0.0
-  __TEXT.__text: 0x4f90cc
+3401.5.1.0.0
+  __TEXT.__text: 0x4fa1c0
   __TEXT.__auth_stubs: 0x2050
   __TEXT.__init_offsets: 0x24
   __TEXT.__objc_methlist: 0x317c
-  __TEXT.__gcc_except_tab: 0x3b398
-  __TEXT.__const: 0x1b4bb
-  __TEXT.__cstring: 0x64462
+  __TEXT.__gcc_except_tab: 0x3b690
+  __TEXT.__const: 0x1b4d3
+  __TEXT.__cstring: 0x64a62
   __TEXT.__ustring: 0xaa
   __TEXT.__oslogstring: 0x27c
-  __TEXT.__unwind_info: 0x14080
+  __TEXT.__unwind_info: 0x140c8
   __TEXT.__objc_classname: 0x4a8
   __TEXT.__objc_methname: 0x66fc
   __TEXT.__objc_methtype: 0x6374

   - /usr/lib/libsqlite3.dylib
   - /usr/lib/libxml2.2.dylib
   - /usr/lib/libz.1.dylib
-  Functions: 15567
-  Symbols:   17883
-  CStrings:  27982
+  Functions: 15577
+  Symbols:   17894
+  CStrings:  28008
 
Symbols:
+ __ZN4siri12dialogengine12DBMonthToICUEi
+ __ZN4siri12dialogengine13DateIsHolidayERKNS0_9TimeStampERKNSt3__112basic_stringIcNS4_11char_traitsIcEENS4_9allocatorIcEEEESC_
+ __ZN4siri12dialogengine15GetICUDayOfWeekERKNS0_9TimeStampE
+ __ZN4siri12dialogengine16DBDayOfWeekToICUEi
+ __ZN4siri12dialogengine26GetDateOfNthWeekdayOfMonthEi15UCalendarMonths19UCalendarDaysOfWeeki
+ __ZNK4siri12dialogengine14Sqlite3DeleterclEP7sqlite3
- __ZN4siri12dialogengine13DateIsHolidayERKNS0_9TimeStampERKNSt3__112basic_stringIcNS4_11char_traitsIcEENS4_9allocatorIcEEEE
CStrings:
+ "3401.5.1"
+ "CAT Request (Dialog Engine 3401.5.1)"
+ "Could not get field from UCalendar: %!d(MISSING)"
+ "Found %!z(MISSING)u rows"
+ "GetDateOfNthWeekdayOfMonth: There aren't that many occurrences in this month"
+ "GetDateOfNthWeekdayOfMonth: invalid dayOfWeek"
+ "GetDateOfNthWeekdayOfMonth: invalid month"
+ "GetDateOfNthWeekdayOfMonth: invalid occurrence (cannot be 0)"
+ "GetDateOfNthWeekdayOfMonth: invalid occurrence (there cannot be more than 5 occurrences in a month)"
+ "GetDateOfNthWeekdayOfMonth: negative occurrence result = %!d(MISSING)"
+ "GetDateOfNthWeekdayOfMonth: positive occurrence result = %!d(MISSING)"
+ "GetDateOfNthWeekdayOfMonth: year = %!d(MISSING); month = %!d(MISSING) (0-11); dayOfWeek = %!d(MISSING) (1-7); occurrence = %!d(MISSING)"
+ "Invalid Holidata day of week: %!d(MISSING)"
+ "Invalid Holidata month number: %!d(MISSING)"
+ "MonthRelativeWeekDay"
+ "Result: %!s(MISSING)"
+ "[DateIsHolidayOther] Holiday type: [%!s(MISSING)]"
+ "[DateIsHolidayOther] holiday '%!s(MISSING)' for country '%!s(MISSING)' was not found in the database"
+ "[DateIsHolidayOther] holiday: month = %!d(MISSING); day of week = %!d(MISSING); occurrence = %!d(MISSING)"
+ "[DateIsHolidayOther] result = %!s(MISSING)"
+ "[DateIsHolidayOther] timeStamp = %!l(MISSING)d (%!s(MISSING)); holiday = [%!s(MISSING)]; country = [%!s(MISSING)]"
+ "[DateIsHolidayOther] timeStamp: year = %!d(MISSING); month = %!d(MISSING); day = %!d(MISSING)"
+ "[GetHolidayDate] GetDateOfNthWeekdayOfMonth failed to calculate a date. Bad inputs?"
+ "[GetHolidayDate] holiday '%!s(MISSING)' for country '%!s(MISSING)' or 'default' was not found in the database"
+ "[GetHolidayDate] holiday '%!s(MISSING)' for country '%!s(MISSING)' was not found in the database. Trying with country 'default'."
+ "[GetHolidayDate] holiday = [%!s(MISSING)]; calendarType = %!s(MISSING); textType = %!s(MISSING); holidayLocale = [%!s(MISSING)]; holidayYear = %!d(MISSING)"
+ "[GetHolidayDate] holiday: month = %!d(MISSING); day of week = %!d(MISSING); occurrence = %!d(MISSING)"
+ "dayofweek"
+ "dayordinal"
- "3401.2.1"
- "CAT Request (Dialog Engine 3401.2.1)"
- "thursday"

```
