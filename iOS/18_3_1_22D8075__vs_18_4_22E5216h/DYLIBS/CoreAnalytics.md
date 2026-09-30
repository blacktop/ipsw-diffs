## CoreAnalytics

> `/System/Library/PrivateFrameworks/CoreAnalytics.framework/CoreAnalytics`

```diff

-419.60.7.0.0
-  __TEXT.__text: 0x2527c
-  __TEXT.__auth_stubs: 0xec0
-  __TEXT.__objc_methlist: 0x188
-  __TEXT.__gcc_except_tab: 0x2d84
-  __TEXT.__const: 0x1752
-  __TEXT.__cstring: 0x2750
-  __TEXT.__oslogstring: 0xdb6
-  __TEXT.__swift5_typeref: 0x6b
-  __TEXT.__constg_swiftt: 0x68
-  __TEXT.__swift5_reflstr: 0x17
-  __TEXT.__swift5_fieldmd: 0x28
-  __TEXT.__swift5_types: 0x4
-  __TEXT.__unwind_info: 0x1008
-  __TEXT.__objc_classname: 0x53
-  __TEXT.__objc_methname: 0x61e
-  __TEXT.__objc_methtype: 0x244
+430.100.6.0.0
+  __TEXT.__text: 0x248cc
+  __TEXT.__auth_stubs: 0xe10
+  __TEXT.__objc_methlist: 0x158
+  __TEXT.__gcc_except_tab: 0x2d7c
+  __TEXT.__const: 0x16e2
+  __TEXT.__cstring: 0x2470
+  __TEXT.__oslogstring: 0xd35
+  __TEXT.__swift5_typeref: 0x2b
+  __TEXT.__unwind_info: 0xf68
+  __TEXT.__objc_classname: 0x3c
+  __TEXT.__objc_methname: 0x4df
+  __TEXT.__objc_methtype: 0x1b2
   __TEXT.__objc_stubs: 0x500
-  __DATA_CONST.__got: 0x1c0
+  __DATA_CONST.__got: 0x1d8
   __DATA_CONST.__const: 0x4f8
-  __DATA_CONST.__objc_classlist: 0x18
-  __DATA_CONST.__objc_protolist: 0x20
+  __DATA_CONST.__objc_classlist: 0x10
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x1a0
-  __DATA_CONST.__objc_protorefs: 0x10
+  __DATA_CONST.__objc_selrefs: 0x198
   __DATA_CONST.__objc_superrefs: 0x10
-  __AUTH_CONST.__auth_got: 0x778
-  __AUTH_CONST.__auth_ptr: 0x20
-  __AUTH_CONST.__const: 0x950
+  __AUTH_CONST.__auth_got: 0x720
+  __AUTH_CONST.__auth_ptr: 0x28
+  __AUTH_CONST.__const: 0x938
   __AUTH_CONST.__cfstring: 0x160
-  __AUTH_CONST.__objc_const: 0x620
-  __AUTH.__objc_data: 0x188
-  __AUTH.__data: 0x30
+  __AUTH_CONST.__objc_const: 0x2a0
+  __AUTH.__objc_data: 0xa0
   __DATA.__objc_ivar: 0x20
-  __DATA.__data: 0x110
-  __DATA.__bss: 0x18
-  __DATA.__common: 0x18
+  __DATA.__data: 0x30
+  __DATA.__bss: 0x20
+  __DATA.__common: 0x20
   __DATA_DIRTY.__bss: 0x120
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/Foundation.framework/Foundation
   - /System/Library/PrivateFrameworks/AppleSauce.framework/AppleSauce
+  - /System/Library/PrivateFrameworks/OSAnalytics.framework/OSAnalytics
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libc++.1.dylib
   - /usr/lib/libobjc.A.dylib

   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsys_time.dylib
   - /usr/lib/swift/libswiftunistd.dylib
-  Functions: 704
-  Symbols:   1026
-  CStrings:  560
+  Functions: 672
+  Symbols:   1011
+  CStrings:  503
 
Symbols:
+ _OBJC_CLASS_$_OSADefaults
+ __ZNSt3__117bad_function_callD1Ev
+ __ZTINSt3__117bad_function_callE
+ __ZTVNSt3__117bad_function_callE
+ ___chkstk_darwin
+ __swiftImmortalRefCount
+ _swift_dynamicCast
+ _swift_getObjCClassMetadata
+ _xpc_array_create_empty
+ _xpc_dictionary_set_string
- _OBJC_CLASS_$__TtC13CoreAnalytics23AnalyticsXPCQueryClient
- _OBJC_METACLASS_$__TtC13CoreAnalytics23AnalyticsXPCQueryClient
- __Block_copy
- __ZNKSt9exception4whatEv
- _objc_allocWithZone
- _objc_release_x27
- _swift_arrayDestroy
- _swift_beginAccess
- _swift_deletedMethodError
- _swift_initStackObject
- _swift_isaMask
- _swift_lookUpClassMethod
- _swift_unknownObjectRetain_n
- _xpc_dictionary_set_int64
- _xpc_is_system_session
CStrings:
+ "GreyMatterAvailable"
+ "Unable to unwrap availability reasons array"
+ "Unable to unwrap availability string"
+ "Unexpected object for key: %s"
+ "availability"
+ "reasons"
- "#16@0:8"
- "@\"NSString\"16@0:8"
- "@24@0:8:16"
- "@32@0:8:16@24"
- "@40@0:8:16@24@32"
- "B24@0:8#16"
- "B24@0:8:16"
- "B24@0:8@\"Protocol\"16"
- "Cannot set target user session for remoted connection because we failed to get the foreground user's uid: %d"
- "Fatal error"
- "Got unexpected response from analyticsagent"
- "Insufficient space allocated to copy string contents"
- "NSObject"
- "OS_xpc_object"
- "Q16@0:8"
- "Received an XPC error reply: %s"
- "Swift/ContiguousArrayBuffer.swift"
- "Swift/StringTesting.swift"
- "Swift/StringUTF8View.swift"
- "Swift/UnsafeBufferPointer.swift"
- "Swift/UnsafePointer.swift"
- "Swift/UnsafeRawPointer.swift"
- "T#,R"
- "T@\"NSString\",?,R,C"
- "T@\"NSString\",R,C"
- "TQ,R"
- "Unexpected XPC: %{public}s"
- "Unexpectedly found nil while unwrapping an Optional value"
- "UnsafeMutableBufferPointer with negative count"
- "UnsafeMutablePointer.initialize overlapping range"
- "UnsafeMutableRawPointer.initializeMemory overlapping range"
- "Vv16@0:8"
- "XPC error: %{public}s"
- "^{_NSZone=}16@0:8"
- "_TtC13CoreAnalytics23AnalyticsXPCQueryClient"
- "_connection"
- "analytics_user_data"
- "autorelease"
- "class"
- "com.apple.analyticsagent"
- "conformsToProtocol:"
- "debugDescription"
- "description"
- "hash"
- "invalid Collection: less than 'count' elements in collection"
- "isEqual:"
- "isKindOfClass:"
- "isMemberOfClass:"
- "isProxy"
- "keyMapping"
- "performSelector:"
- "performSelector:withObject:"
- "performSelector:withObject:withObject:"
- "release"
- "respondsToSelector:"
- "retain"
- "retainCount"
- "self"
- "superclass"
- "v16@?0@\"<OS_xpc_object>\"8"
- "zone"

```
