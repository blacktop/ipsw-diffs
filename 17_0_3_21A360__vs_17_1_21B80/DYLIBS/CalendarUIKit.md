## CalendarUIKit

> `/System/Library/PrivateFrameworks/CalendarUIKit.framework/CalendarUIKit`

```diff

-1205.0.0.0.0
-  __TEXT.__text: 0x63d78
+1205.1.1.1.0
+  __TEXT.__text: 0x63ddc
   __TEXT.__auth_stubs: 0xdd0
-  __TEXT.__objc_methlist: 0x5abc
+  __TEXT.__objc_methlist: 0x5ab4
   __TEXT.__const: 0x3c6
-  __TEXT.__cstring: 0x67ff
+  __TEXT.__cstring: 0x67ef
   __TEXT.__oslogstring: 0x3659
   __TEXT.__gcc_except_tab: 0x600
-  __TEXT.__ustring: 0x14d4
+  __TEXT.__ustring: 0x14e0
   __TEXT.__constg_swiftt: 0x50
   __TEXT.__swift5_typeref: 0x6
   __TEXT.__swift5_fieldmd: 0x10
   __TEXT.__swift5_types: 0x4
-  __TEXT.__unwind_info: 0x18a8
+  __TEXT.__unwind_info: 0x18b0
   __TEXT.__objc_classname: 0xd67
-  __TEXT.__objc_methname: 0x13d25
-  __TEXT.__objc_methtype: 0x1a8c
-  __TEXT.__objc_stubs: 0xf700
-  __DATA_CONST.__got: 0x4d8
+  __TEXT.__objc_methname: 0x13d11
+  __TEXT.__objc_methtype: 0x1a9d
+  __TEXT.__objc_stubs: 0xf6e0
+  __DATA_CONST.__got: 0x4d0
   __DATA_CONST.__const: 0x14a8
   __DATA_CONST.__objc_classlist: 0x370
   __DATA_CONST.__objc_catlist: 0xc8
   __DATA_CONST.__objc_protolist: 0x88
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_const: 0x9d60
-  __DATA_CONST.__objc_selrefs: 0x4cc8
+  __DATA_CONST.__objc_const: 0x9d80
+  __DATA_CONST.__objc_selrefs: 0x4cb8
   __DATA_CONST.__objc_arraydata: 0x108
   __AUTH_CONST.__cfstring: 0x7360
   __AUTH_CONST.__objc_const: 0x0
   __AUTH_CONST.__objc_intobj: 0x270
   __AUTH_CONST.__objc_arrayobj: 0x60
+  __AUTH_CONST.__const: 0x60
   __AUTH_CONST.__objc_doubleobj: 0x10
   __AUTH_CONST.__auth_got: 0x6f8
   __AUTH.__data: 0x98
   __DATA.__objc_protorefs: 0x10
-  __DATA.__objc_classrefs: 0x680
+  __DATA.__objc_classrefs: 0x678
   __DATA.__objc_superrefs: 0x1d0
-  __DATA.__objc_ivar: 0x5c4
+  __DATA.__objc_ivar: 0x5c8
   __DATA.__data: 0x698
   __DATA.__bss: 0x2c0
   __DATA.__common: 0x240
-  __DATA_DIRTY.__const: 0x840
+  __DATA_DIRTY.__const: 0x7e0
   __DATA_DIRTY.__objc_const: 0x2cd0
   __DATA_DIRTY.__objc_data: 0x2210
   __DATA_DIRTY.__data: 0x18

   - /usr/lib/swift/libswiftXPC.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  UUID: B3A47213-1122-32ED-956D-37588DDEA2AF
-  Functions: 2599
-  Symbols:   9117
-  CStrings:  5636
+  UUID: AD361AB6-4DFF-3E56-BA00-4AC09D7F2A05
+  Functions: 2598
+  Symbols:   9113
+  CStrings:  5635
 
Symbols:
+ -[CUIKCalendarModel _cachedFakeTodayIndexLocked]
+ -[CUIKCalendarModel _sectionForCachedOccurrencesOnDate:sectionExistsForDay:usingFilter:]
+ -[CUIKCalendarModel dateForCachedOccurrencesInSection:usingFilter:holdingCachedFakeTodayIndexLock:]
+ GCC_except_table95
+ GCC_except_table98
+ _OBJC_IVAR_$_CUIKCalendarModel._cachedFakeTodayIndexLock
+ ___block_literal_global.264
+ ___block_literal_global.266
+ ___block_literal_global.278
+ _objc_msgSend$_cachedFakeTodayIndexLocked
+ _objc_msgSend$_sectionForCachedOccurrencesOnDate:sectionExistsForDay:usingFilter:
+ _objc_msgSend$dateForCachedOccurrencesInSection:usingFilter:holdingCachedFakeTodayIndexLock:
- -[CUIKCalendarModel cachedFakeTodayIndex]
- -[CUIKCalendarModel closestOccurrenceToTomorrowForEventUID:]
- -[CUIKCalendarModel fetchCachedDaysInBackgroundStartingFromSection:]
- -[CUIKCalendarModel sectionForCachedOccurrencesOnDate:sectionExistsForDay:usingFilter:]
- GCC_except_table96
- GCC_except_table99
- _OBJC_CLASS_$_EKObjectID
- ___block_literal_global.265
- ___block_literal_global.267
- ___block_literal_global.276
- ___block_literal_global.279
- _kCADMainDatabaseID
- _objc_msgSend$cachedFakeTodayIndex
- _objc_msgSend$fetchCachedDaysInBackgroundStartingFromSection:usingFilter:
- _objc_msgSend$objectIDWithEntityType:rowID:databaseID:
- _objc_msgSend$sectionForCachedOccurrencesOnDate:sectionExistsForDay:usingFilter:
CStrings:
+ "\x12#!\x11\x12!!\x13\x15\x13"
+ "@32@0:8q16B24B28"
+ "_cachedFakeTodayIndexLock"
+ "_cachedFakeTodayIndexLocked"
+ "_sectionForCachedOccurrencesOnDate:sectionExistsForDay:usingFilter:"
+ "dateForCachedOccurrencesInSection:usingFilter:holdingCachedFakeTodayIndexLock:"
- "\x12#!\x11\x12\x11!\x13\x15\x13"
- "%@\\U00A0%@"
- "cachedFakeTodayIndex"
- "closestOccurrenceToTomorrowForEventUID:"
- "fetchCachedDaysInBackgroundStartingFromSection:"
- "objectIDWithEntityType:rowID:databaseID:"
- "sectionForCachedOccurrencesOnDate:sectionExistsForDay:usingFilter:"

```
