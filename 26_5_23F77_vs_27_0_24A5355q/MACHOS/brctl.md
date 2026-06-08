## brctl

> `/usr/bin/brctl`

```diff

-4479.122.1.0.0
-  __TEXT.__text: 0x1446c
-  __TEXT.__auth_stubs: 0xb70
-  __TEXT.__objc_stubs: 0x3060
-  __TEXT.__objc_methlist: 0x79c
-  __TEXT.__const: 0xf8
-  __TEXT.__gcc_except_tab: 0x994
-  __TEXT.__objc_classname: 0xda
-  __TEXT.__objc_methname: 0x2a95
-  __TEXT.__objc_methtype: 0x41c
-  __TEXT.__cstring: 0x44c7
+5044.0.0.0.0
+  __TEXT.__text: 0x140e8
+  __TEXT.__auth_stubs: 0xba0
+  __TEXT.__objc_stubs: 0x3240
+  __TEXT.__objc_methlist: 0x794
+  __TEXT.__const: 0xf0
+  __TEXT.__gcc_except_tab: 0x9bc
+  __TEXT.__objc_classname: 0xbb
+  __TEXT.__cstring: 0x457d
+  __TEXT.__objc_methname: 0x2ba4
+  __TEXT.__objc_methtype: 0x406
   __TEXT.__oslogstring: 0xd6
   __TEXT.__unwind_info: 0x3d0
-  __DATA_CONST.__auth_got: 0x5c8
-  __DATA_CONST.__got: 0x490
-  __DATA_CONST.__auth_ptr: 0x8
-  __DATA_CONST.__const: 0xfa0
+  __DATA_CONST.__const: 0x1010
   __DATA_CONST.__cfstring: 0x2260
   __DATA_CONST.__objc_classlist: 0x30
-  __DATA_CONST.__objc_catlist: 0x18
+  __DATA_CONST.__objc_catlist: 0x10
   __DATA_CONST.__objc_protolist: 0x18
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_superrefs: 0x28
   __DATA_CONST.__objc_arraydata: 0x100
   __DATA_CONST.__objc_arrayobj: 0x30
   __DATA_CONST.__objc_intobj: 0x30
-  __DATA.__objc_const: 0x1518
-  __DATA.__objc_selrefs: 0xd68
-  __DATA.__objc_ivar: 0x154
+  __DATA_CONST.__auth_got: 0x5e0
+  __DATA_CONST.__got: 0x498
+  __DATA_CONST.__auth_ptr: 0x8
+  __DATA.__objc_const: 0x14b8
+  __DATA.__objc_selrefs: 0xde8
+  __DATA.__objc_ivar: 0x150
   __DATA.__objc_data: 0x1e0
   __DATA.__data: 0x1e0
   __DATA.__bss: 0x58

   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libprequelite.dylib
   - /usr/lib/libsqlite3.dylib
-  UUID: A1B66F60-F777-3286-8CA1-F8079B33F20E
-  Functions: 258
-  Symbols:   344
-  CStrings:  1569
+  UUID: B3EC5A68-6F86-31D7-88D4-2BB781353603
+  Functions: 259
+  Symbols:   348
+  CStrings:  1587
 
Symbols:
+ _OBJC_CLASS_$_OSLogEventStore
+ _OBJC_CLASS_$_OSLogEventStream
+ _objc_claimAutoreleasedReturnValue
+ _objc_retainAutoreleaseReturnValue
+ _objc_retain_x3
+ _objc_retain_x5
- _OBJC_CLASS_$_OSLogPersistence
- _objc_retain_x28
CStrings:
+ " (counter saturated, actual count may be higher)"
+ "*** DROPPED LOGS: %u message%s lost%s ***\n"
+ "/usr/bin/brctl backup -o \"%@\""
+ "B8@?0"
+ "_streamDoneSema"
+ "activateStreamFromDate:toDate:"
+ "cannot open archive `%s`: %s\n"
+ "composedMessage"
+ "decomposedMessage"
+ "initWithSource:"
+ "localStore"
+ "logType"
+ "lossCount"
+ "newestDate"
+ "outputActivityEvent:"
+ "prepareWithCompletionHandler:"
+ "printLogWithFacility:subsystem:message:threadID:kind:sender:sendPID:depth:level:timestamp:timezone:sectionID:previousSectionID:"
+ "processIdentifier"
+ "processIdentifierVersion"
+ "s"
+ "setEventHandler:"
+ "setFilterPredicate:"
+ "setFlags:"
+ "setInvalidationHandler:"
+ "setTarget:"
+ "setUpgradeConfirmationHandler:"
+ "storeWithArchiveURL:"
+ "threadIdentifier"
+ "timeZone"
+ "v104@0:8@16@24r*32Q40i48@52i60i64i68@72@80@88@96"
+ "v16@?0@\"OSLogEventProxy\"8"
+ "v24@?0@\"OSLogEventSource\"8@\"NSError\"16"
+ "v24@?0Q8@\"OSLogEventStreamPosition\"16"
- "/usr/bin/brctl backup \"%@\" -o"
- "@\"NSMutableArray\""
- "B16@?0@\"OSActivityEvent\"8"
- "_allEvents"
- "_dumpSema"
- "br_isOversize"
- "bradditions"
- "cannot access archive `%s`: %s\n"
- "endDate"
- "enumerateFromStartDate:toEndDate:withBlock:"
- "oversize! "
- "printLogWithFacility:subsystem:message:threadID:kind:sender:sendPID:depth:level:timestamp:timezone:sectionID:isOversize:previousSectionID:"
- "reason"
- "setLogArchive:"
- "v108@0:8@16@24r*32Q40i48@52i60i64i68@72@80@88B96@100"

```
