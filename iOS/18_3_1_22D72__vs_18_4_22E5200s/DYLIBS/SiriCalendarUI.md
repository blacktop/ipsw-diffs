## SiriCalendarUI

> `/System/Library/PrivateFrameworks/SiriCalendarUI.framework/SiriCalendarUI`

```diff

-3402.37.1.0.0
-  __TEXT.__text: 0x39f0c
-  __TEXT.__auth_stubs: 0x1550
-  __TEXT.__const: 0x1560
-  __TEXT.__constg_swiftt: 0x770
-  __TEXT.__swift5_typeref: 0x2ade
+3404.20.1.0.0
+  __TEXT.__text: 0x23058
+  __TEXT.__auth_stubs: 0x14e0
+  __TEXT.__const: 0x1418
+  __TEXT.__cstring: 0x2a9
+  __TEXT.__constg_swiftt: 0x798
+  __TEXT.__swift5_typeref: 0x28be
   __TEXT.__swift5_builtin: 0x28
-  __TEXT.__swift5_reflstr: 0x61b
-  __TEXT.__swift5_assocty: 0x258
-  __TEXT.__swift5_fieldmd: 0x5ec
-  __TEXT.__swift5_proto: 0x7c
-  __TEXT.__swift5_types: 0x74
-  __TEXT.__oslogstring: 0x248
-  __TEXT.__swift5_capture: 0x2d4
-  __TEXT.__cstring: 0x649
+  __TEXT.__swift5_reflstr: 0x69b
+  __TEXT.__swift5_assocty: 0x270
+  __TEXT.__swift5_fieldmd: 0x650
+  __TEXT.__swift5_proto: 0x88
+  __TEXT.__swift5_types: 0x78
+  __TEXT.__oslogstring: 0x245
+  __TEXT.__swift5_capture: 0x2bc
   __TEXT.__swift5_mpenum: 0x8
-  __TEXT.__unwind_info: 0xb00
-  __TEXT.__eh_frame: 0x368
-  __TEXT.__objc_methname: 0x12a
-  __DATA_CONST.__got: 0x470
+  __TEXT.__unwind_info: 0x8c0
+  __TEXT.__eh_frame: 0x290
+  __TEXT.__objc_methname: 0x74
+  __DATA_CONST.__got: 0x458
   __DATA_CONST.__const: 0x120
   __DATA_CONST.__objc_classlist: 0x8
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x60
-  __AUTH_CONST.__auth_got: 0xaa8
-  __AUTH_CONST.__auth_ptr: 0x7e0
-  __AUTH_CONST.__const: 0x9d0
+  __DATA_CONST.__objc_selrefs: 0x40
+  __AUTH_CONST.__auth_got: 0xa70
+  __AUTH_CONST.__auth_ptr: 0x7b0
+  __AUTH_CONST.__const: 0xb10
   __AUTH_CONST.__objc_const: 0xb8
-  __AUTH.__data: 0xb50
-  __DATA.__data: 0xcc0
-  __DATA.__bss: 0x10e0
+  __AUTH.__data: 0xb58
+  __DATA.__data: 0xc70
+  __DATA.__bss: 0x1250
   __DATA.__common: 0x8
   - /System/Library/Frameworks/Combine.framework/Combine
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation

   - /usr/lib/swift/libswiftDarwin.dylib
   - /usr/lib/swift/libswiftDataDetection.dylib
   - /usr/lib/swift/libswiftDispatch.dylib
-  - /usr/lib/swift/libswiftFileProvider.dylib
   - /usr/lib/swift/libswiftIntents.dylib
   - /usr/lib/swift/libswiftMLCompute.dylib
   - /usr/lib/swift/libswiftMapKit.dylib

   - /usr/lib/swift/libswiftQuartzCore.dylib
   - /usr/lib/swift/libswiftSpatial.dylib
   - /usr/lib/swift/libswiftUniformTypeIdentifiers.dylib
+  - /usr/lib/swift/libswiftVideoToolbox.dylib
   - /usr/lib/swift/libswiftXPC.dylib
   - /usr/lib/swift/libswift_Builtin_float.dylib
   - /usr/lib/swift/libswift_errno.dylib

   - /usr/lib/swift/libswiftsimd.dylib
   - /usr/lib/swift/libswiftsys_time.dylib
   - /usr/lib/swift/libswiftunistd.dylib
-  Functions: 1005
-  Symbols:   337
-  CStrings:  59
+  Functions: 893
+  Symbols:   344
+  CStrings:  37
 
Symbols:
+ __swift_FORCE_LOAD_$_swiftVideoToolbox
+ _objc_retain_x21
+ _swift_allocateGenericValueMetadataWithLayoutString
+ _swift_enumFn_getEnumTag
+ _swift_generic_assignWithCopy
+ _swift_generic_assignWithTake
+ _swift_generic_destroy
+ _swift_generic_initWithCopy
+ _swift_generic_initWithTake
+ _swift_generic_initializeBufferWithCopyOfBuffer
+ _swift_getFunctionTypeMetadata0
+ _swift_initStructMetadataWithLayoutString
- _CUIKStringForRecurrenceRule
- _OBJC_CLASS_$_EKRecurrenceDayOfWeek
- _OBJC_CLASS_$_EKRecurrenceEnd
- _OBJC_CLASS_$_EKRecurrenceRule
- _OBJC_CLASS_$_NSNumber
- __swift_FORCE_LOAD_$_swiftFileProvider
- _objc_release
- _swift_allocateGenericValueMetadata
- _swift_arrayDestroy
- _swift_beginAccess
- _swift_endAccess
- _swift_initStructMetadata
CStrings:
+ "DELETE_EVENT"
+ "NEW_EVENT"
+ "UPDATE_EVENT"
- " events are also scheduled at this time"
- " is also scheduled at this time"
- "ATTENDEE_INVITATION"
- "Insufficient space allocated to copy string contents"
- "SCHEDULE_CONFLICT"
- "SEND_INVITATION_QUESTION"
- "Swift/ContiguousArrayBuffer.swift"
- "Swift/StringTesting.swift"
- "Swift/StringUTF8View.swift"
- "Swift/UnsafeBufferPointer.swift"
- "Swift/UnsafePointer.swift"
- "Swift/UnsafeRawPointer.swift"
- "Unexpectedly found nil while unwrapping an Optional value"
- "UnsafeMutableBufferPointer with negative count"
- "UnsafeMutablePointer.initialize overlapping range"
- "UnsafeMutablePointer.initialize with negative count"
- "UnsafeMutablePointer.moveInitialize with negative count"
- "UnsafeMutableRawPointer.initializeMemory overlapping range"
- "UnsafeMutableRawPointer.initializeMemory with negative count"
- "dayOfWeek:"
- "exclamationmark.circle"
- "initRecurrenceWithFrequency:interval:daysOfTheWeek:daysOfTheMonth:monthsOfTheYear:weeksOfTheYear:daysOfTheYear:setPositions:end:"
- "initWithEndDate:"
- "initWithOccurrenceCount:"
- "invalid Collection: less than 'count' elements in collection"

```
