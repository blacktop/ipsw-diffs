## EventKitUI

> `/System/iOSSupport/System/Library/Frameworks/EventKitUI.framework/Versions/A/EventKitUI`

### Sections with Same Size but Changed Content

- `__TEXT.__const`
- `__TEXT.__cstring`
- `__TEXT.__constg_swiftt`
- `__TEXT.__swift5_typeref`
- `__TEXT.__swift5_proto`
- `__TEXT.__swift_as_entry`
- `__TEXT.__swift_as_ret`
- `__TEXT.__swift_as_cont`
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
-  __TEXT.__text: 0x1ec1f8
-  __TEXT.__objc_methlist: 0x1fc2c
+1568.0.0.0.0
+  __TEXT.__text: 0x1ec354
+  __TEXT.__objc_methlist: 0x1fd8c
   __TEXT.__const: 0x2e74
   __TEXT.__cstring: 0xc904
   __TEXT.__oslogstring: 0x779d
-  __TEXT.__gcc_except_tab: 0x3f70
+  __TEXT.__gcc_except_tab: 0x3f10
   __TEXT.__ustring: 0x862
   __TEXT.__dlopen_cstrs: 0x226
   __TEXT.__constg_swiftt: 0x1c84

   __TEXT.__swift_as_entry: 0x48
   __TEXT.__swift_as_ret: 0x3c
   __TEXT.__swift_as_cont: 0xac
-  __TEXT.__unwind_info: 0x7b68
+  __TEXT.__unwind_info: 0x7b60
   __TEXT.__eh_frame: 0xbec
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0

   __DATA_CONST.__objc_catlist: 0x80
   __DATA_CONST.__objc_protolist: 0x630
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0xf660
+  __DATA_CONST.__objc_selrefs: 0xf6d8
   __DATA_CONST.__objc_protorefs: 0xe0
   __DATA_CONST.__objc_superrefs: 0x8a8
   __DATA_CONST.__objc_arraydata: 0x1b8
   __DATA_CONST.__got: 0x1aa8
   __AUTH_CONST.__const: 0x2e80
   __AUTH_CONST.__cfstring: 0xad80
-  __AUTH_CONST.__objc_const: 0x30fd0
+  __AUTH_CONST.__objc_const: 0x31018
   __AUTH_CONST.__objc_arrayobj: 0x1e0
   __AUTH_CONST.__objc_intobj: 0x480
   __AUTH_CONST.__objc_doubleobj: 0x70

   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  Functions: 12220
-  Symbols:   24730
+  Functions: 12242
+  Symbols:   24764
   CStrings:  2275
 
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
+ GCC_except_table123
+ GCC_except_table126
+ GCC_except_table132
+ GCC_except_table18
+ OBJC_IVAR_$_EKDayViewController._hidesWeekNumberLabel
+ OBJC_IVAR_$_EKEventEditViewControllerModernImpl._notifyingEditViewDelegateCompletion
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
- GCC_except_table122
- GCC_except_table125
- GCC_except_table128
- GCC_except_table131
- GCC_except_table26
- GCC_except_table31
- OBJC_IVAR_$_EKDayPreviewController._originalEventEndDate
- OBJC_IVAR_$_EKDayPreviewController._originalEventStartDate
- ___54-[EKDayPreviewController _eventsForStartDate:endDate:]_block_invoke
- _objc_msgSend$refreshUIForUpdatedEvent
- _objc_msgSend$updateFromReminderForEvent:
CStrings:
+ "\xf0\xf0!!1"
- "\tZRC"
```
