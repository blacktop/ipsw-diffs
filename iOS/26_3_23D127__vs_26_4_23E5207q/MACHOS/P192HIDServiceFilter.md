## P192HIDServiceFilter

> `/System/Library/HIDPlugins/ServiceFilters/P192HIDServiceFilter.plugin/P192HIDServiceFilter`

```diff

-2222.80.22.0.0
-  __TEXT.__text: 0x6784
-  __TEXT.__auth_stubs: 0x700
-  __TEXT.__objc_methlist: 0x354
-  __TEXT.__const: 0x288
-  __TEXT.__cstring: 0x2bd
-  __TEXT.__swift5_typeref: 0x144
-  __TEXT.__objc_methname: 0x3ce
-  __TEXT.__swift5_capture: 0x50
-  __TEXT.__oslogstring: 0x281
-  __TEXT.__constg_swiftt: 0x418
-  __TEXT.__swift5_reflstr: 0x110
-  __TEXT.__swift5_fieldmd: 0x17c
-  __TEXT.__swift5_builtin: 0x3c
-  __TEXT.__swift5_assocty: 0x18
-  __TEXT.__swift5_proto: 0x10
-  __TEXT.__swift5_types: 0x1c
-  __TEXT.__objc_classname: 0x2d
-  __TEXT.__objc_methtype: 0x316
-  __TEXT.__unwind_info: 0x240
-  __DATA_CONST.__auth_got: 0x380
-  __DATA_CONST.__got: 0xd8
-  __DATA_CONST.__auth_ptr: 0xc0
-  __DATA_CONST.__const: 0x320
-  __DATA_CONST.__objc_classlist: 0x18
-  __DATA_CONST.__objc_protolist: 0x30
+2238.100.58.0.0
+  __TEXT.__text: 0x16ac
+  __TEXT.__auth_stubs: 0x380
+  __TEXT.__objc_stubs: 0x100
+  __TEXT.__objc_methlist: 0x27c
+  __TEXT.__const: 0x42
+  __TEXT.__objc_methname: 0x473
+  __TEXT.__swift5_typeref: 0x6c
+  __TEXT.__swift5_capture: 0x20
+  __TEXT.__objc_methtype: 0x343
+  __TEXT.__oslogstring: 0x61
+  __TEXT.__cstring: 0x31
+  __TEXT.__objc_classname: 0x2f
+  __TEXT.__constg_swiftt: 0x100
+  __TEXT.__swift5_reflstr: 0x2b
+  __TEXT.__swift5_fieldmd: 0x40
+  __TEXT.__swift5_types: 0x4
+  __TEXT.__unwind_info: 0xf8
+  __DATA_CONST.__auth_got: 0x1c8
+  __DATA_CONST.__got: 0x38
+  __DATA_CONST.__auth_ptr: 0x10
+  __DATA_CONST.__const: 0xb8
+  __DATA_CONST.__objc_classlist: 0x8
+  __DATA_CONST.__objc_protolist: 0x20
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_protorefs: 0x18
-  __DATA.__objc_const: 0xaa0
-  __DATA.__objc_selrefs: 0x1a8
-  __DATA.__objc_data: 0x458
-  __DATA.__data: 0x3f8
-  __DATA.__bss: 0x218
-  __DATA.__common: 0x30
-  - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
+  __DATA_CONST.__objc_protorefs: 0x10
+  __DATA.__objc_const: 0x278
+  __DATA.__objc_selrefs: 0x160
+  __DATA.__objc_data: 0x190
+  __DATA.__data: 0x130
+  __DATA.__common: 0x18
+  __DATA.__bss: 0x8
   - /System/Library/Frameworks/Foundation.framework/Foundation
   - /System/Library/Frameworks/IOKit.framework/Versions/A/IOKit
   - /System/Library/PrivateFrameworks/HID.framework/HID

   - /usr/lib/swift/libswiftXPC.dylib
   - /usr/lib/swift/libswift_Builtin_float.dylib
   - /usr/lib/swift/libswiftos.dylib
-  UUID: 3AE6FF13-A9EC-37D2-A901-70A0ED3837BA
-  Functions: 189
-  Symbols:   101
-  CStrings:  148
+  UUID: 6CBC110A-5575-3AE6-973C-495F7E4B1FDE
+  Functions: 53
+  Symbols:   61
+  CStrings:  97
 
Symbols:
- _OBJC_CLASS_$_HIDSensorTimeFilter
- _OBJC_CLASS_$_HIDTimeSync
- _OBJC_CLASS_$_NSArray
- _OBJC_CLASS_$_NSData
- _OBJC_CLASS_$_NSDictionary
- _OBJC_CLASS_$_NSMutableDictionary
- _OBJC_CLASS_$_NSNumber
- _OBJC_CLASS_$_OS_dispatch_queue
- _OBJC_CLASS_$__TtCs12_SwiftObject
- _OBJC_METACLASS_$_HIDSensorTimeFilter
- _OBJC_METACLASS_$__TtCs12_SwiftObject
- __swiftImmortalRefCount
- __swift_stdlib_bridgeErrorToNSError
- _mach_get_times
- _mach_timebase_info
- _malloc_size
- _memcpy
- _memmove
- _objc_release_x23
- _objc_release_x24
- _objc_release_x25
- _objc_release_x27
- _objc_release_x9
- _objc_retain_x21
- _objc_retain_x22
- _objc_retain_x24
- _objc_retain_x26
- _objc_retain_x27
- _swift_allocError
- _swift_beginAccess
- _swift_bridgeObjectRetain
- _swift_deallocClassInstance
- _swift_deallocPartialClassInstance
- _swift_dynamicCast
- _swift_endAccess
- _swift_errorRelease
- _swift_errorRetain
- _swift_getForeignTypeMetadata
- _swift_isUniquelyReferenced_nonNull_native
- _swift_willThrow
CStrings:
+ "P192HIDServiceFilter"
- "%s: first event:%u timestamp:%llu"
- "%s: machGetTimes:%d"
- "%s: streaming session sample time latency min:%llu max:%llu average:%llu"
- "%s: syncedTime:%@"
- "%s: timespec calculation would overflow"
- "%s: timespec calculation would underflow"
- "%s: timesync event:%ld, precision:%ld event stats:%@"
- "%s: timesync timstamp is in future use time of arrival current ts:%llu synce ts:%llu remote ts:%llu"
- "%s: unexpected timespec calculation error: %@"
- "%s:Timesync is not available"
- "ChildVendorMessage"
- "HIDEventDispatcher"
- "P192HIDServiceFilter.HIDSensorTimeFilter"
- "ServiceFilterDebug"
- "TimesyncPrecision"
- "_TtC20P192HIDServiceFilter5Stats"
- "__swift_objectForKeyedSubscript:"
- "com.apple.HIDSensorTimeFilter"
- "dispatchEvent:"
- "eventDispatcher"
- "eventStatistics"
- "initWithBytes:length:"
- "lastEMA"
- "latency"
- "logEvent"
- "propertyForKey:"
- "reportInterval"
- "serviceID"
- "serviceIDStr"
- "setEventHandler:"
- "smoothingFactor"
- "syncedTimeFromData:error:"
- "timeSyncFromHIDEventService:"
- "timebaseInfo"
- "timesync"
- "timesyncPrecision"
- "timesyncState"
- "v24@0:8@\"HIDEvent\"16"
- "v24@?0q8q16"
- "vMax"
- "vMin"

```
