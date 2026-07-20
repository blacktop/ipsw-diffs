## EventKitUI

> `/System/Library/Frameworks/EventKitUI.framework/EventKitUI`

### Sections with Same Size but Changed Content

- `__TEXT.__const`
- `__TEXT.__swift5_typeref`
- `__TEXT.__constg_swiftt`
- `__TEXT.__swift5_proto`
- `__TEXT.__swift_as_entry`
- `__TEXT.__swift_as_ret`
- `__TEXT.__swift_as_cont`
- `__TEXT.__unwind_info`
- `__TEXT.__eh_frame`
- `__DATA_CONST.__const`
- `__DATA_CONST.__objc_classlist`
- `__DATA_CONST.__objc_catlist`
- `__DATA_CONST.__objc_protolist`
- `__DATA_CONST.__objc_protorefs`
- `__DATA_CONST.__objc_superrefs`
- `__DATA_CONST.__objc_arraydata`
- `__DATA_CONST.__got`
- `__AUTH_CONST.__const`
- `__AUTH_CONST.__cfstring`
- `__AUTH_CONST.__objc_arrayobj`
- `__AUTH_CONST.__objc_intobj`
- `__AUTH_CONST.__objc_doubleobj`
- `__AUTH_CONST.__objc_dictobj`
- `__AUTH_CONST.__objc_floatobj`
- `__AUTH.__objc_data`
- `__AUTH.__data`
- `__DATA.__objc_ivar`
- `__DATA.__data`
- `__DATA_DIRTY.__objc_data`

```diff

-1565.0.0.0.0
-  __TEXT.__text: 0x1f6e2c
-  __TEXT.__objc_methlist: 0x200ac
+1568.0.0.0.0
+  __TEXT.__text: 0x1f6f90
+  __TEXT.__objc_methlist: 0x2020c
   __TEXT.__const: 0x2e94
-  __TEXT.__cstring: 0xd174
-  __TEXT.__gcc_except_tab: 0x401c
+  __TEXT.__cstring: 0xd184
+  __TEXT.__gcc_except_tab: 0x3fbc
   __TEXT.__oslogstring: 0x7b37
   __TEXT.__ustring: 0x862
   __TEXT.__dlopen_cstrs: 0x36b

   __DATA_CONST.__objc_catlist: 0x80
   __DATA_CONST.__objc_protolist: 0x658
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0xfae0
+  __DATA_CONST.__objc_selrefs: 0xfb58
   __DATA_CONST.__objc_protorefs: 0xe0
   __DATA_CONST.__objc_superrefs: 0x8b8
   __DATA_CONST.__objc_arraydata: 0x1c0
   __DATA_CONST.__got: 0x1bd8
   __AUTH_CONST.__const: 0x2ee0
   __AUTH_CONST.__cfstring: 0xb4c0
-  __AUTH_CONST.__objc_const: 0x315e8
+  __AUTH_CONST.__objc_const: 0x31630
   __AUTH_CONST.__objc_arrayobj: 0x1f8
   __AUTH_CONST.__objc_intobj: 0x570
   __AUTH_CONST.__objc_doubleobj: 0x70

   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  Functions: 12336
-  Symbols:   24993
+  Functions: 12358
+  Symbols:   25026
   CStrings:  2364
 
Symbols:
+ -[EKCalendarChooser isScrolledToTop]
+ -[EKCalendarChooser scrollToTop]
+ -[EKCalendarChooserDefaultImpl isScrolledToTop]
+ -[EKCalendarChooserDefaultImpl scrollToTop]
+ -[EKCalendarChooserOOPWrapperImpl isScrolledToTop]
+ -[EKCalendarChooserOOPWrapperImpl scrollToTop]
+ -[EKDayViewController hidesWeekNumberLabel]
+ -[EKDayViewController setHidesWeekNumberLabel:]
+ -[EKEventEditViewController refreshUIForUpdatedEvent:]
+ -[EKEventEditViewControllerDefaultImpl applyMagicComposeSnapshot:]
+ -[EKEventEditViewControllerDefaultImpl magicComposeSnapshot]
+ -[EKEventEditViewControllerDefaultImpl refreshUIForUpdatedEvent:]
+ -[EKEventEditViewControllerDefaultImpl willDeselectTab]
+ -[EKEventEditViewControllerDefaultImpl willSelectTab]
+ -[EKEventEditViewControllerModernImpl _notifyEditViewDelegateDidCompleteWithAction:]
+ -[EKEventEditViewControllerModernImpl _shouldHideTitleInEditingModeFromDelegate]
+ -[EKEventEditViewControllerModernImpl applyMagicComposeSnapshot:]
+ -[EKEventEditViewControllerModernImpl magicComposeSnapshot]
+ -[EKEventEditViewControllerModernImpl refreshUIForUpdatedEvent:]
+ -[EKEventEditViewControllerModernImpl willDeselectTab]
+ -[EKEventEditViewControllerModernImpl willSelectTab]
+ -[EKEventEditViewControllerOOPWrapperImpl applyMagicComposeSnapshot:]
+ -[EKEventEditViewControllerOOPWrapperImpl magicComposeSnapshot]
+ -[EKEventEditViewControllerOOPWrapperImpl refreshUIForUpdatedEvent:]
+ -[EKEventEditViewControllerOOPWrapperImpl willDeselectTab]
+ -[EKEventEditViewControllerOOPWrapperImpl willSelectTab]
+ -[EKExpandedReminderStackViewController showViewController:sender:animated:completion:]
+ GCC_except_table124
+ GCC_except_table130
+ GCC_except_table133
+ _OBJC_IVAR_$_EKDayViewController._hidesWeekNumberLabel
+ _OBJC_IVAR_$_EKEventEditViewControllerModernImpl._notifyingEditViewDelegateCompletion
+ _objc_msgSend$_notifyEditViewDelegateDidCompleteWithAction:
+ _objc_msgSend$_shouldHideTitleInEditingModeFromDelegate
+ _objc_msgSend$adjustedContentInset
+ _objc_msgSend$applyMagicComposeSnapshot:
+ _objc_msgSend$eventViewControllerShouldHideTitleInEditingMode:
+ _objc_msgSend$hidesWeekNumberLabel
+ _objc_msgSend$isScrolledToTop
+ _objc_msgSend$loadViewIfNeeded
+ _objc_msgSend$magicComposeSnapshot
+ _objc_msgSend$modalPresentationStyle
+ _objc_msgSend$refreshUIForUpdatedEvent:
+ _objc_msgSend$scrollToTop
+ _objc_msgSend$updateFromReminderForEvent:suppressMagicComposeRewrite:
+ _objc_msgSend$updateHideTitleInEditingMode:
+ _objc_msgSend$willDeselectTab
+ _objc_msgSend$willSelectTab
- -[EKEventEditViewController refreshUIForUpdatedEvent]
- -[EKEventEditViewControllerDefaultImpl refreshUIForUpdatedEvent]
- -[EKEventEditViewControllerModernImpl refreshUIForUpdatedEvent]
- -[EKEventEditViewControllerOOPWrapperImpl refreshUIForUpdatedEvent]
- GCC_except_table109
- GCC_except_table123
- GCC_except_table126
- GCC_except_table132
- GCC_except_table26
- GCC_except_table31
- _OBJC_IVAR_$_EKDayPreviewController._originalEventEndDate
- _OBJC_IVAR_$_EKDayPreviewController._originalEventStartDate
- ___54-[EKDayPreviewController _eventsForStartDate:endDate:]_block_invoke
- _objc_msgSend$refreshUIForUpdatedEvent
- _objc_msgSend$updateFromReminderForEvent:
CStrings:
+ "\xf0\xf0!!1"
- "\tZRC"
```
