## CalendarIntegrationSupport

> `/System/Library/PrivateFrameworks/CalendarIntegrationSupport.framework/CalendarIntegrationSupport`

```diff

-1190.0.0.0.0
-  __TEXT.__text: 0x211ac
-  __TEXT.__auth_stubs: 0x1010
+1192.0.0.0.0
+  __TEXT.__text: 0x21e9c
+  __TEXT.__auth_stubs: 0x1050
   __TEXT.__objc_methlist: 0xc8
-  __TEXT.__oslogstring: 0x8f7
+  __TEXT.__oslogstring: 0xa07
   __TEXT.__cstring: 0x754
   __TEXT.__const: 0xc94
-  __TEXT.__constg_swiftt: 0x794
+  __TEXT.__constg_swiftt: 0x7b4
   __TEXT.__swift5_typeref: 0x623
-  __TEXT.__swift5_reflstr: 0x4d0
-  __TEXT.__swift5_fieldmd: 0x680
+  __TEXT.__swift5_reflstr: 0x4f0
+  __TEXT.__swift5_fieldmd: 0x68c
   __TEXT.__swift5_builtin: 0x28
   __TEXT.__swift5_types: 0x74
   __TEXT.__swift5_proto: 0x88
   __TEXT.__swift5_capture: 0x20
   __TEXT.__swift5_protos: 0xc
   __TEXT.__swift5_mpenum: 0x8
-  __TEXT.__unwind_info: 0x760
-  __TEXT.__eh_frame: 0x810
+  __TEXT.__unwind_info: 0x790
+  __TEXT.__eh_frame: 0x848
   __TEXT.__objc_classname: 0x9c
-  __TEXT.__objc_methname: 0x99c
+  __TEXT.__objc_methname: 0x9dc
   __TEXT.__objc_methtype: 0x10c
   __TEXT.__objc_stubs: 0xc0
-  __DATA_CONST.__got: 0x1c8
-  __DATA_CONST.__const: 0xe8
+  __DATA_CONST.__got: 0x1d0
+  __DATA_CONST.__const: 0x128
   __DATA_CONST.__objc_classlist: 0x38
   __DATA_CONST.__objc_protolist: 0x48
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x360
+  __DATA_CONST.__objc_selrefs: 0x378
   __DATA_CONST.__objc_protorefs: 0x10
   __DATA_CONST.__objc_superrefs: 0x8
-  __AUTH_CONST.__auth_got: 0x810
+  __AUTH_CONST.__auth_got: 0x830
   __AUTH_CONST.__auth_ptr: 0x1f0
-  __AUTH_CONST.__const: 0xb20
+  __AUTH_CONST.__const: 0xb30
   __AUTH_CONST.__cfstring: 0x20
   __AUTH_CONST.__objc_const: 0xba8
   __AUTH.__objc_data: 0x48
-  __AUTH.__data: 0x1e0
   __DATA.__objc_ivar: 0x4
-  __DATA.__data: 0x4f0
-  __DATA.__common: 0x18
-  __DATA.__bss: 0xc80
+  __DATA.__data: 0x3c0
+  __DATA.__bss: 0xb80
   __DATA_DIRTY.__objc_data: 0xf8
-  __DATA_DIRTY.__data: 0x700
-  __DATA_DIRTY.__common: 0x18
-  __DATA_DIRTY.__bss: 0x280
+  __DATA_DIRTY.__data: 0xa60
+  __DATA_DIRTY.__common: 0x30
+  __DATA_DIRTY.__bss: 0x380
   - /System/Library/Frameworks/Accounts.framework/Accounts
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/EventKit.framework/EventKit

   - /usr/lib/swift/libswiftSpatial.dylib
   - /usr/lib/swift/libswiftUniformTypeIdentifiers.dylib
   - /usr/lib/swift/libswiftXPC.dylib
+  - /usr/lib/swift/libswift_Builtin_float.dylib
+  - /usr/lib/swift/libswift_errno.dylib
+  - /usr/lib/swift/libswift_math.dylib
+  - /usr/lib/swift/libswift_signal.dylib
+  - /usr/lib/swift/libswift_stdio.dylib
+  - /usr/lib/swift/libswift_time.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  Functions: 688
-  Symbols:   222
-  CStrings:  247
+  - /usr/lib/swift/libswiftsys_time.dylib
+  - /usr/lib/swift/libswiftunistd.dylib
+  Functions: 698
+  Symbols:   231
+  CStrings:  254
 
Symbols:
+ _OBJC_CLASS_$_EKObjectID
+ __swift_FORCE_LOAD_$_swift_Builtin_float
+ __swift_FORCE_LOAD_$_swift_errno
+ __swift_FORCE_LOAD_$_swift_math
+ __swift_FORCE_LOAD_$_swift_signal
+ __swift_FORCE_LOAD_$_swift_stdio
+ __swift_FORCE_LOAD_$_swift_time
+ __swift_FORCE_LOAD_$_swiftsys_time
+ __swift_FORCE_LOAD_$_swiftunistd
CStrings:
+ "Couldn't fetch contents of calendar to check for removed reminders"
+ "Couldn't find calendar with UUID %!{(MISSING)public}s while looking for reminders to remove in a full sync; skipping it."
+ "Couldn't turn object ID into an event"
+ "Failed to commit removals: %!@(MISSING)"
+ "Fetching contents of calendar returned unexpected results"
+ "calendarIdentifier"
+ "calendarWithIdentifier:"
+ "eventForObjectID:occurrenceDate:checkValid:"
+ "loadEventIDs:uniqueIDs:calendar:"
+ "uuid"
- "Failed to create predicate for events in calendar %!{(MISSING)public}@"
- "eventsMatchingPredicate:"
- "predicateForMasterEventsInCalendar:"

```
