## iCalendar

> `/System/Library/PrivateFrameworks/iCalendar.framework/iCalendar`

```diff

-  __TEXT.__text: 0x2b374
+  __TEXT.__text: 0x2b218
   __TEXT.__objc_methlist: 0x398c
   __TEXT.__cstring: 0x2a53
   __TEXT.__oslogstring: 0x4ed
Sections:
~ __TEXT.__objc_methlist : content changed
~ __TEXT.__gcc_except_tab : content changed
~ __TEXT.__unwind_info : content changed
~ __DATA_CONST.__const : content changed
~ __DATA_CONST.__objc_classlist : content changed
~ __DATA_CONST.__objc_catlist : content changed
~ __DATA_CONST.__objc_protolist : content changed
~ __DATA_CONST.__objc_selrefs : content changed
~ __DATA_CONST.__objc_superrefs : content changed
~ __DATA_CONST.__objc_arraydata : content changed
~ __DATA_CONST.__got : content changed
~ __AUTH_CONST.__const : content changed
~ __AUTH_CONST.__cfstring : content changed
~ __AUTH_CONST.__objc_const : content changed
~ __AUTH_CONST.__objc_arrayobj : content changed
~ __DATA.__data : content changed
~ __DATA_DIRTY.__objc_data : content changed
Functions:
~ -[NSString(VCSUtilities) VCS_uncommentedAddress] : 744 -> 736
~ +[ICSDuration(iCalendarImport) durationFromRFC2445UTF8String:] : 652 -> 660
~ -[VCSRecurrenceRule initWithString:] : 588 -> 572
~ -[VCSRecurrenceRule decodeWeekly:] : 120 -> 108
~ -[VCSRecurrenceRule decodeMonthlyByPos:] : 188 -> 164
~ -[VCSRecurrenceRule decodeMonthlyByDay:] : 136 -> 124
~ -[VCSRecurrenceRule decodeYearlyByMonth:] : 136 -> 124
~ -[VCSRecurrenceRule decodeYearlyByDay:] : 136 -> 124
~ -[VCSRecurrenceRule decodeWeekdayList:] : 304 -> 312
~ _ICSEncodeBase64 : 492 -> 484
~ +[VCSDate dateListFromData:] : 412 -> 404
~ +[ICSRecurrenceRule(Internal) recurrenceRuleFromICSCString:withTokenizer:] : 4336 -> 4084

```
