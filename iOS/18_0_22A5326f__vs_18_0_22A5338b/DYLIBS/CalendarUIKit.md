## CalendarUIKit

> `/System/Library/PrivateFrameworks/CalendarUIKit.framework/CalendarUIKit`

```diff

-1235.0.0.0.0
-  __TEXT.__text: 0x15e0a4
-  __TEXT.__auth_stubs: 0x3ab0
-  __TEXT.__objc_methlist: 0x6aa0
+1237.0.0.0.0
+  __TEXT.__text: 0x15d234
+  __TEXT.__auth_stubs: 0x3af0
+  __TEXT.__objc_methlist: 0x6ac8
   __TEXT.__const: 0xad34
   __TEXT.__cstring: 0x9cbd
-  __TEXT.__oslogstring: 0x4742
-  __TEXT.__gcc_except_tab: 0xed8
+  __TEXT.__oslogstring: 0x4132
+  __TEXT.__gcc_except_tab: 0xe7c
   __TEXT.__ustring: 0x1e92
   __TEXT.__dlopen_cstrs: 0x68
   __TEXT.__swift5_typeref: 0xc62a

   __TEXT.__swift5_mpenum: 0x8
   __TEXT.__unwind_info: 0x5378
   __TEXT.__eh_frame: 0x1f80
-  __TEXT.__objc_classname: 0x111a
-  __TEXT.__objc_methname: 0x183f5
+  __TEXT.__objc_classname: 0x111b
+  __TEXT.__objc_methname: 0x18492
   __TEXT.__objc_methtype: 0x24cf
-  __TEXT.__objc_stubs: 0x12180
-  __DATA_CONST.__got: 0x15b8
+  __TEXT.__objc_stubs: 0x121c0
+  __DATA_CONST.__got: 0x15c8
   __DATA_CONST.__const: 0x1f68
   __DATA_CONST.__objc_classlist: 0x448
   __DATA_CONST.__objc_catlist: 0xd0
   __DATA_CONST.__objc_protolist: 0x168
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x5d10
+  __DATA_CONST.__objc_selrefs: 0x5d30
   __DATA_CONST.__objc_protorefs: 0x80
   __DATA_CONST.__objc_superrefs: 0x230
   __DATA_CONST.__objc_arraydata: 0x110
-  __AUTH_CONST.__auth_got: 0x1d68
-  __AUTH_CONST.__auth_ptr: 0x1068
+  __AUTH_CONST.__auth_got: 0x1d88
+  __AUTH_CONST.__auth_ptr: 0x1078
   __AUTH_CONST.__const: 0x6098
   __AUTH_CONST.__cfstring: 0x8160
-  __AUTH_CONST.__objc_const: 0xda60
+  __AUTH_CONST.__objc_const: 0xdad0
   __AUTH_CONST.__objc_intobj: 0x2b8
   __AUTH_CONST.__objc_arrayobj: 0x78
   __AUTH_CONST.__objc_doubleobj: 0x10
   __AUTH.__objc_data: 0xb38
   __AUTH.__data: 0x1a18
-  __DATA.__objc_ivar: 0x740
+  __DATA.__objc_ivar: 0x74c
   __DATA.__data: 0x4168
-  __DATA.__bss: 0x107c0
+  __DATA.__bss: 0x107d0
   __DATA.__common: 0x50
   __DATA_DIRTY.__objc_data: 0x2368
   __DATA_DIRTY.__data: 0x828

   - /System/Library/Frameworks/UniformTypeIdentifiers.framework/UniformTypeIdentifiers
   - /System/Library/Frameworks/WidgetKit.framework/WidgetKit
   - /System/Library/Frameworks/_MapKit_SwiftUI.framework/_MapKit_SwiftUI
+  - /System/Library/PrivateFrameworks/AppProtection.framework/AppProtection
   - /System/Library/PrivateFrameworks/AppSupport.framework/AppSupport
   - /System/Library/PrivateFrameworks/CalendarDatabase.framework/CalendarDatabase
   - /System/Library/PrivateFrameworks/CalendarFoundation.framework/CalendarFoundation

   - /usr/lib/swift/libswiftsimd.dylib
   - /usr/lib/swift/libswiftsys_time.dylib
   - /usr/lib/swift/libswiftunistd.dylib
-  Functions: 8198
-  Symbols:   4124
-  CStrings:  5964
+  Functions: 8170
+  Symbols:   4097
+  CStrings:  5940
 
Symbols:
+ _APHiddenAppsChangedNotificationCStr
+ _APLockedAppsChangedNotificationCStr
+ _OBJC_CLASS_$_EKAppProtectionUtils
+ _notify_cancel
+ _notify_check
+ _notify_register_check
+ _notify_register_dispatch
- _OBJC_CLASS_$_NSOrderedSet
CStrings:
+ "\x12#!\x11\x12!!\x14\x11\x15\x15"
+ "_apHiddenNotificationToken"
+ "_apLockedNotificationToken"
+ "_cachedHiddenAppsHash"
+ "_calendarsExcludingLockedReminder:"
+ "_reminderCalendar"
+ "clearLocationCache"
+ "initWithSet:"
+ "isIntegration"
+ "isReminderAppLocked"
+ "setByAddingObjectsFromArray:"
- "\x12#!\x11\x12!!\x14\x15\x15"
- "Accumulating occurrences that collide with occurrence: [%!@(MISSING)]"
- "Added first partition: [%!@(MISSING)]"
- "Analyzing occurrence as potential collision candidate: [%!@(MISSING)]"
- "Analyzing occurrence bucket [%!l(MISSING)u / %!l(MISSING)u]: [%!@(MISSING)]"
- "Analyzing partition: [%!@(MISSING)]"
- "Capped visible text height to: [%!f(MISSING)].  Occurrence: [%!@(MISSING)]"
- "Capping top boundary at [%!f(MISSING)] for partition: [%!@(MISSING)]"
- "Created new partition at index [%!l(MISSING)u] for occurrence: [%!@(MISSING)]"
- "Current occurrence [%!l(MISSING)u / %!l(MISSING)u]: [%!@(MISSING)]"
- "End of collision zone: [%!f(MISSING)]"
- "EventLoader: Occurrences came back for a range that's already loaded, which shouldn't have happened.\nLoaded range: [%!@(MISSING), %!@(MISSING)]"
- "Found collision: [%!@(MISSING)]"
- "Generating new partitions based on the last [%!l(MISSING)u] occurrence buckets"
- "Last partition encountered.  Putting all remaining colliding occurrences into this bucket."
- "Layout commencing for occurrences between start date: [%!@(MISSING)] and end date: [%!@(MISSING)]"
- "Layout complete for occurrences between start date: [%!@(MISSING)] and end date: [%!@(MISSING)]"
- "Layout duration: [%!f(MISSING)] seconds"
- "New bucket created: [%!@(MISSING)]"
- "New index of first remaining occurrence: [%!l(MISSING)u / %!l(MISSING)u]"
- "No more colliding events found"
- "No more colliding occurrences left, though there are buckets available."
- "No more stacked occurrences.  Collapsing partition [%!@(MISSING)] with previous partition [%!@(MISSING)]."
- "No occurrences in bucket"
- "No occurrences to lay out"
- "Number of occurrences to lay out: [%!l(MISSING)u]"
- "Placing colliding occurrences into buckets"
- "Popped occurrence: [%!@(MISSING)]"
- "Preparing to fit [%!l(MISSING)u] colliding occurrences into [%!l(MISSING)u] buckets"
- "Pushed occurrence [%!@(MISSING)] onto existing partition stack: [%!@(MISSING)]"
- "Stamping final frames onto occurrences"
- "_uniqueEventsFromArray:"
- "combinedWidthOfPartitions: [%!f(MISSING)]"
- "orderedSetWithArray:"
- "removeObjectsInRange:"

```
