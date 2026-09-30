## crash_mover

> `/usr/libexec/crash_mover`

```diff

-1049.0.0.0.0
-  __TEXT.__text: 0x1e64
-  __TEXT.__auth_stubs: 0x510
-  __TEXT.__objc_stubs: 0x440
-  __TEXT.__const: 0x18b
+1050.0.0.0.0
+  __TEXT.__text: 0x203c
+  __TEXT.__auth_stubs: 0x530
+  __TEXT.__objc_stubs: 0x4a0
+  __TEXT.__const: 0x193
   __TEXT.__gcc_except_tab: 0x34
-  __TEXT.__oslogstring: 0x5f3
-  __TEXT.__cstring: 0x2bf
-  __TEXT.__objc_methname: 0x31b
-  __TEXT.__unwind_info: 0xc0
-  __DATA_CONST.__auth_got: 0x298
-  __DATA_CONST.__got: 0xa0
+  __TEXT.__oslogstring: 0x6bf
+  __TEXT.__cstring: 0x2d8
+  __TEXT.__objc_methname: 0x35c
+  __TEXT.__unwind_info: 0xd0
+  __DATA_CONST.__auth_got: 0x2a8
+  __DATA_CONST.__got: 0xa8
   __DATA_CONST.__const: 0x138
-  __DATA_CONST.__cfstring: 0x160
+  __DATA_CONST.__cfstring: 0x180
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_arraydata: 0x20
   __DATA_CONST.__objc_dictobj: 0x28
   __DATA_CONST.__objc_arrayobj: 0x18
-  __DATA.__objc_selrefs: 0x110
+  __DATA.__objc_selrefs: 0x128
   __DATA.__data: 0x5
   __DATA.__bss: 0x20
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/Foundation.framework/Foundation
   - /System/Library/PrivateFrameworks/AggregateDictionary.framework/AggregateDictionary
+  - /System/Library/PrivateFrameworks/OSAnalytics.framework/OSAnalytics
   - /System/Library/PrivateFrameworks/PowerLog.framework/PowerLog
   - /usr/lib/libMobileGestalt.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/liblockdown.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 33D6D6D9-AC86-3D84-ACB2-43CE6CBC62DD
-  Functions: 22
-  Symbols:   110
-  CStrings:  107
+  UUID: 29EB7476-9BB5-3615-B03B-72E3F717B0B8
+  Functions: 26
+  Symbols:   113
+  CStrings:  115
 
Symbols:
+ _OBJC_CLASS_$_OSADefaults
+ _objc_opt_class
+ _objc_opt_isKindOfClass
CStrings:
+ "Configured value for crash_moverDisabledSince key is not in the expected format: deleting key"
+ "Received XPC error event: %s"
+ "crash_mover has been temporarily disabled."
+ "crash_mover was disabled over an hour ago: re-enabling crash_mover"
+ "crash_moverDisabledSince"
+ "objectForKey:"
+ "removeObjectForKey:"
+ "timeIntervalSinceReferenceDate"
- "Recieved XPC error event: %s"

```
