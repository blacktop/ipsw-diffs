## nexusd

> `/usr/libexec/nexusd`

```diff

-750.47.0.0.0
-  __TEXT.__text: 0xb70
-  __TEXT.__auth_stubs: 0x2e0
-  __TEXT.__swift5_typeref: 0x10
+750.52.0.0.0
+  __TEXT.__text: 0xd80
+  __TEXT.__auth_stubs: 0x350
+  __TEXT.__cstring: 0x84
   __TEXT.__swift5_entry: 0x8
   __TEXT.__const: 0x30
   __TEXT.__constg_swiftt: 0x28
+  __TEXT.__swift5_typeref: 0x10
   __TEXT.__swift5_fieldmd: 0x10
   __TEXT.__swift5_types: 0x4
   __TEXT.__gcc_except_tab: 0xc4
-  __TEXT.__cstring: 0x60
   __TEXT.__oslogstring: 0x184
   __TEXT.__objc_classname: 0x1
   __TEXT.__info_plist: 0x4d3
-  __TEXT.__unwind_info: 0x98
-  __DATA_CONST.__auth_got: 0x178
-  __DATA_CONST.__got: 0x40
+  __TEXT.__unwind_info: 0xa8
+  __TEXT.__eh_frame: 0x44
+  __DATA_CONST.__auth_got: 0x1b0
+  __DATA_CONST.__got: 0x48
   __DATA_CONST.__auth_ptr: 0x10
-  __DATA_CONST.__const: 0xd0
+  __DATA_CONST.__const: 0xd8
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA.__data: 0x20
   __DATA.__bss: 0x10

   - /usr/lib/swift/libswiftIOKit.dylib
   - /usr/lib/swift/libswiftOSLog.dylib
   - /usr/lib/swift/libswiftObjectiveC.dylib
+  - /usr/lib/swift/libswiftUniformTypeIdentifiers.dylib
   - /usr/lib/swift/libswiftXPC.dylib
+  - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
-  Functions: 14
-  Symbols:   71
-  CStrings:  8
+  Functions: 16
+  Symbols:   80
+  CStrings:  9
 
Symbols:
+ _$sScA15unownedExecutorScevgTj
+ _$sScM6sharedScMvgZ
+ _$sScMMa
+ _$sScMScAsWP
+ __swift_FORCE_LOAD_$_swiftUniformTypeIdentifiers
+ _swift_errorInMain
+ _swift_release
+ _swift_task_isCurrentExecutor
+ _swift_task_reportUnexpectedExecutor
CStrings:
+ "nexusd/nexusd.swift"

```
