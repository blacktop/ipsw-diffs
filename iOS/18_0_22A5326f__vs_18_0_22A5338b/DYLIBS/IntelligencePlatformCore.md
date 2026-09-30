## IntelligencePlatformCore

> `/System/Library/PrivateFrameworks/IntelligencePlatformCore.framework/IntelligencePlatformCore`

```diff

-110.1.0.0.0
-  __TEXT.__text: 0xb4507c
-  __TEXT.__auth_stubs: 0x9f20
-  __TEXT.__objc_methlist: 0x1678
-  __TEXT.__cstring: 0x42b5c
-  __TEXT.__swift5_typeref: 0x1c962
-  __TEXT.__const: 0x670a1
-  __TEXT.__constg_swiftt: 0x2175c
-  __TEXT.__swift5_reflstr: 0x23c8f
-  __TEXT.__swift5_fieldmd: 0x248a0
+111.0.2.1.0
+  __TEXT.__text: 0xb358fc
+  __TEXT.__auth_stubs: 0x9ec0
+  __TEXT.__objc_methlist: 0x1658
+  __TEXT.__cstring: 0x42b33
+  __TEXT.__swift5_typeref: 0x1c7de
+  __TEXT.__const: 0x66261
+  __TEXT.__constg_swiftt: 0x21704
+  __TEXT.__swift5_reflstr: 0x23c1f
+  __TEXT.__swift5_fieldmd: 0x248c4
   __TEXT.__swift5_builtin: 0x4b0
   __TEXT.__swift5_mpenum: 0x15c
-  __TEXT.__swift5_assocty: 0x2e00
-  __TEXT.__swift5_proto: 0x5c3c
+  __TEXT.__swift5_assocty: 0x2dd0
+  __TEXT.__swift5_proto: 0x5c1c
   __TEXT.__swift5_types: 0x1f64
   __TEXT.__swift5_protos: 0x360
-  __TEXT.__oslogstring: 0x1e6e3
-  __TEXT.__swift5_capture: 0x3d40
+  __TEXT.__oslogstring: 0x1e693
+  __TEXT.__swift5_capture: 0x3b34
   __TEXT.__gcc_except_tab: 0x148
   __TEXT.__dlopen_cstrs: 0xc0
-  __TEXT.__unwind_info: 0x295f8
-  __TEXT.__eh_frame: 0x5e108
+  __TEXT.__unwind_info: 0x292e0
+  __TEXT.__eh_frame: 0x5df10
   __TEXT.__objc_classname: 0x4a5
-  __TEXT.__objc_methname: 0x9e9f
-  __TEXT.__objc_methtype: 0x23b2
-  __TEXT.__objc_stubs: 0x1140
-  __DATA_CONST.__got: 0x43b0
-  __DATA_CONST.__const: 0x7f0
+  __TEXT.__objc_methname: 0x9efc
+  __TEXT.__objc_methtype: 0x23ca
+  __TEXT.__objc_stubs: 0x1160
+  __DATA_CONST.__got: 0x4248
+  __DATA_CONST.__const: 0x818
   __DATA_CONST.__objc_classlist: 0x1188
   __DATA_CONST.__objc_protolist: 0x240
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x21e8
+  __DATA_CONST.__objc_selrefs: 0x21f0
   __DATA_CONST.__objc_protorefs: 0x118
   __DATA_CONST.__objc_superrefs: 0x80
-  __AUTH_CONST.__auth_got: 0x4fa0
-  __AUTH_CONST.__auth_ptr: 0x4900
-  __AUTH_CONST.__const: 0x410c8
+  __AUTH_CONST.__auth_got: 0x4f70
+  __AUTH_CONST.__auth_ptr: 0x49b8
+  __AUTH_CONST.__const: 0x40f90
   __AUTH_CONST.__cfstring: 0x360
-  __AUTH_CONST.__objc_const: 0x2dbf0
+  __AUTH_CONST.__objc_const: 0x2dc18
   __AUTH.__objc_data: 0x3ae8
-  __AUTH.__data: 0x17ac8
+  __AUTH.__data: 0x17b58
   __DATA.__objc_ivar: 0xc4
   __DATA.__data: 0x12d38
-  __DATA.__bss: 0x78c40
-  __DATA.__common: 0x1af0
+  __DATA.__bss: 0x78a40
+  __DATA.__common: 0x1af8
   __DATA_DIRTY.__objc_data: 0x3c08
-  __DATA_DIRTY.__data: 0x226e0
-  __DATA_DIRTY.__bss: 0x295a0
+  __DATA_DIRTY.__data: 0x225c0
+  __DATA_DIRTY.__bss: 0x293a0
   __DATA_DIRTY.__common: 0x17b0
   - /System/Library/Frameworks/Accelerate.framework/Accelerate
   - /System/Library/Frameworks/AppIntents.framework/AppIntents

   - /usr/lib/swift/libswiftsimd.dylib
   - /usr/lib/swift/libswiftsys_time.dylib
   - /usr/lib/swift/libswiftunistd.dylib
-  Functions: 58500
-  Symbols:   877
-  CStrings:  9686
+  Functions: 58156
+  Symbols:   875
+  CStrings:  9691
 
Symbols:
+ _BMUseCaseIncrementalViews
- _OBJC_CLASS_$_BMStreamDatastore
- _objc_retain_x13
- _swift_deallocBox
CStrings:
+ "@56@0:8@16@24@32@40^@48"
+ "SELECT * FROM interactions WHERE id = ?"
+ "SiriRemembersViewGenerator: Dropping indexes"
+ "SiriRemembersViewGenerator: Hit id change count limit of %!l(MISSING)d"
+ "SiriRemembersViewGenerator: Restoring indexes"
+ "UPDATE interactionEntities SET parameter = ? WHERE interactionRowid = ? AND entityRowid = ? AND parameter != ?"
+ "_TtCCO24IntelligencePlatformCore14ViewGeneration26SiriRemembersViewGenerator11DiffTracker"
+ "changes"
+ "dateByAddingTimeInterval:"
+ "deletedEventTimestampsForStream:account:device:from:error:"
+ "diffWriter"
+ "eventTimestamp"
+ "indexSQL"
+ "interactionsSelectStatement"
+ "interactions_sourceStreams"
+ "sqlite3MediumCacheSpillSize"
+ "tombstonePublisherWithUseCase:account:device:options:"
+ "tombstonePublisherWithUseCase:device:options:"
+ "tombstonePublisherWithUseCase:options:"
+ "v16@?0@\"BMStoreEvent\"8"
- "IntelligencePlatformCore/ViewGeneration+SiriRemembers.swift"
- "Processing tombstones on device or account streams not currently supported"
- "Received nil date"
- "Received nil predicate"
- "SiriRemembersViewGenerator: ProcessingStateCache: mapping %!s(MISSING) to %!s(MISSING)"
- "SiriRemembersViewGenerator: receiveInput: Unhandled Processing State: "
- "SiriRemembersViewGenerator: receiveInput: skipping %!s(MISSING) since it is already processed."
- "UPDATE interactionEntities SET parameter = ? WHERE interactionRowid = ? AND entityRowid = ?"
- "_TtC24IntelligencePlatformCore20CalendarEventsSignal"
- "calendarEventsSignal"
- "deletedEventTimestampsForStream:error:"
- "frame"
- "hasAttendees"
- "initWithStream:permission:config:includeTombstones:"
- "newEnumeratorFromStartTime:options:"

```
