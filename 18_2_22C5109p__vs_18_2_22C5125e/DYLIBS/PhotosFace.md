## PhotosFace

> `/System/Library/PrivateFrameworks/PhotosFace.framework/PhotosFace`

```diff

-72.0.0.0.0
-  __TEXT.__text: 0xe9398
-  __TEXT.__auth_stubs: 0x21b0
-  __TEXT.__cstring: 0x320c
-  __TEXT.__swift5_typeref: 0x2199
-  __TEXT.__swift5_reflstr: 0x1384
-  __TEXT.__swift5_assocty: 0x5c0
-  __TEXT.__const: 0x6318
-  __TEXT.__constg_swiftt: 0x3018
-  __TEXT.__swift5_fieldmd: 0x1ca4
+77.0.0.0.0
+  __TEXT.__text: 0xeb6b4
+  __TEXT.__auth_stubs: 0x2290
+  __TEXT.__cstring: 0x32ec
+  __TEXT.__swift5_typeref: 0x2225
+  __TEXT.__swift5_reflstr: 0x12a4
+  __TEXT.__swift5_assocty: 0x5a8
+  __TEXT.__const: 0x6188
+  __TEXT.__constg_swiftt: 0x2cac
+  __TEXT.__swift5_fieldmd: 0x1b94
   __TEXT.__swift5_builtin: 0xc8
   __TEXT.__swift5_mpenum: 0x6c
-  __TEXT.__swift5_proto: 0x4e0
-  __TEXT.__swift5_types: 0x24c
-  __TEXT.__swift5_capture: 0x6fc
+  __TEXT.__swift5_proto: 0x4d0
+  __TEXT.__swift5_types: 0x238
+  __TEXT.__swift5_capture: 0x704
   __TEXT.__swift5_protos: 0x24
-  __TEXT.__oslogstring: 0x6ef
-  __TEXT.__unwind_info: 0x4590
-  __TEXT.__eh_frame: 0xabb8
-  __TEXT.__objc_classname: 0x17
-  __TEXT.__objc_methname: 0x419
-  __TEXT.__objc_methtype: 0xad
-  __DATA_CONST.__got: 0x450
-  __DATA_CONST.__const: 0x320
+  __TEXT.__oslogstring: 0x9ff
+  __TEXT.__unwind_info: 0x4458
+  __TEXT.__eh_frame: 0xaca0
+  __TEXT.__objc_methname: 0x2da
+  __DATA_CONST.__got: 0x4a0
+  __DATA_CONST.__const: 0x2d8
   __DATA_CONST.__objc_classlist: 0x50
-  __DATA_CONST.__objc_protolist: 0x20
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_selrefs: 0x128
-  __DATA_CONST.__objc_protorefs: 0x10
-  __AUTH_CONST.__auth_got: 0x10d8
-  __AUTH_CONST.__auth_ptr: 0xa30
-  __AUTH_CONST.__const: 0x4530
-  __AUTH_CONST.__objc_const: 0xdd0
+  __AUTH_CONST.__auth_got: 0x1148
+  __AUTH_CONST.__auth_ptr: 0x9a0
+  __AUTH_CONST.__const: 0x41c8
+  __AUTH_CONST.__objc_const: 0xa98
   __AUTH.__objc_data: 0x50
-  __AUTH.__data: 0x1410
-  __DATA.__data: 0x3938
-  __DATA.__bss: 0x81a0
+  __AUTH.__data: 0x1360
+  __DATA.__data: 0x3710
+  __DATA.__bss: 0x7ea0
   __DATA.__common: 0x8
   __DATA_DIRTY.__objc_data: 0x50
-  __DATA_DIRTY.__data: 0xd90
-  __DATA_DIRTY.__bss: 0xa00
+  __DATA_DIRTY.__data: 0xb98
+  __DATA_DIRTY.__bss: 0xa80
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/CoreGraphics.framework/CoreGraphics
   - /System/Library/Frameworks/CryptoKit.framework/CryptoKit

   - /usr/lib/swift/libswiftsimd.dylib
   - /usr/lib/swift/libswiftsys_time.dylib
   - /usr/lib/swift/libswiftunistd.dylib
-  Functions: 4896
-  Symbols:   251
-  CStrings:  315
+  Functions: 4767
+  Symbols:   259
+  CStrings:  298
 
Symbols:
+ _objc_release_x28
+ _objc_retain_x28
+ _swift_getAtKeyPath
+ _swift_getErrorValue
+ _swift_getKeyPath
+ _swift_task_isCurrentExecutor
+ _swift_task_reportUnexpectedExecutor
CStrings:
+ "    DELETE FROM stored_photo WHERE photo_id IN ("
+ "%!s(MISSING): No More Requests, all done!"
+ "Deleting Stored Photos %!s(MISSING)"
+ "Fetch Album For Day Request: %!s(MISSING) %!s(MISSING)"
+ "Fetch Album Request: %!s(MISSING)"
+ "Fetch Galleries Request: %!s(MISSING)"
+ "Fetch Gallery For Day: %!s(MISSING) %!s(MISSING)"
+ "Fetch Shuffle By Day Request: %!s(MISSING)"
+ "Fetch Shuffle For Day Request: %!s(MISSING) %!s(MISSING)"
+ "Fetch Shuffle Request: %!s(MISSING)"
+ "List Albums Request"
+ "List Galleries Request"
+ "List Shuffles Request"
+ "Make Full Mask Request: %!s(MISSING)"
+ "NetworkRequestTimeout"
+ "PhotosFace/BroadcastSequence.swift"
+ "PhotosFace/MessageDemultiplexer.swift"
+ "PhotosFace/PhotosFaceDatabase.swift"
+ "PhotosFace/PhotosXPC.swift"
+ "PhotosFace/XPCEventStream.swift"
+ "Process Photos Request: %!s(MISSING)"
+ "Provide Album Asset List Request: %!s(MISSING)"
+ "Provide Shuffle Asset List Request: %!s(MISSING)"
+ "Send Message Request: %!s(MISSING)"
+ "TimeoutCheckFrequency"
+ "Track Album Request: %!s(MISSING)"
+ "Track Gallery Request: %!s(MISSING)"
+ "Track Shuffle Request: %!s(MISSING)"
+ "Untrack Album Request: %!s(MISSING)"
+ "Untrack Gallery Request: %!s(MISSING)"
+ "Untrack Shuffle Request: %!s(MISSING)"
- "    DELETE FROM stored_photo WHERE photo_id = ?"
- "#16@0:8"
- "@\"NSString\"16@0:8"
- "@16@0:8"
- "@24@0:8:16"
- "@32@0:8:16@24"
- "@40@0:8:16@24@32"
- "B16@0:8"
- "B24@0:8#16"
- "B24@0:8:16"
- "B24@0:8@\"Protocol\"16"
- "B24@0:8@16"
- "BufferSize"
- "DebugSQL"
- "Deleting Stored Photo %!s(MISSING)"
- "FixedDay"
- "IgnoreSyncCache"
- "NSObject"
- "OS_xpc_object"
- "Q16@0:8"
- "QUICTimeout"
- "T#,R"
- "T@\"NSString\",?,R,C"
- "T@\"NSString\",R,C"
- "TQ,R"
- "Vv16@0:8"
- "^{_NSZone=}16@0:8"
- "autorelease"
- "class"
- "conformsToProtocol:"
- "continuation"
- "debugDescription"
- "description"
- "hash"
- "isEqual:"
- "isKindOfClass:"
- "isMemberOfClass:"
- "isProxy"
- "performSelector:"
- "performSelector:withObject:"
- "performSelector:withObject:withObject:"
- "release"
- "respondsToSelector:"
- "retain"
- "retainCount"
- "self"
- "superclass"
- "zone"

```
