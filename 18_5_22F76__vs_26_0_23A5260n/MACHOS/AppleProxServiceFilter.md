## AppleProxServiceFilter

> `/System/Library/HIDPlugins/ServiceFilters/AppleProxServiceFilter.plugin/AppleProxServiceFilter`

```diff

-44.5.0.0.0
-  __TEXT.__text: 0x9038
-  __TEXT.__auth_stubs: 0x960
+48.0.0.0.0
+  __TEXT.__text: 0x8ff4
+  __TEXT.__auth_stubs: 0x950
   __TEXT.__objc_stubs: 0xcc0
   __TEXT.__init_offsets: 0x4
-  __TEXT.__objc_methlist: 0x8f4
+  __TEXT.__objc_methlist: 0x90c
   __TEXT.__gcc_except_tab: 0xae8
-  __TEXT.__const: 0x1e0
+  __TEXT.__const: 0x210
   __TEXT.__cstring: 0xe27
   __TEXT.__oslogstring: 0xa35
-  __TEXT.__objc_methname: 0x1595
+  __TEXT.__objc_methname: 0x15d1
   __TEXT.__objc_classname: 0xae
-  __TEXT.__objc_methtype: 0x66f
-  __TEXT.__swift5_typeref: 0xb2
+  __TEXT.__objc_methtype: 0x6dd
+  __TEXT.__swift5_typeref: 0xba
   __TEXT.__constg_swiftt: 0x194
   __TEXT.__swift5_reflstr: 0x60
   __TEXT.__swift5_fieldmd: 0x98
   __TEXT.__swift5_builtin: 0x14
-  __TEXT.__swift5_types: 0x14
+  __TEXT.__swift5_types: 0x18
   __TEXT.__swift5_protos: 0x4
   __TEXT.__swift5_proto: 0xc
   __TEXT.__unwind_info: 0x390
-  __TEXT.__eh_frame: 0xa8
-  __DATA_CONST.__auth_got: 0x4c0
-  __DATA_CONST.__got: 0x110
+  __TEXT.__eh_frame: 0x80
+  __DATA_CONST.__auth_got: 0x4b8
+  __DATA_CONST.__got: 0x118
   __DATA_CONST.__auth_ptr: 0x88
-  __DATA_CONST.__const: 0x198
+  __DATA_CONST.__const: 0x178
   __DATA_CONST.__cfstring: 0x13a0
   __DATA_CONST.__objc_classlist: 0x38
   __DATA_CONST.__objc_catlist: 0x8

   __DATA_CONST.__objc_intobj: 0x90
   __DATA_CONST.__objc_arraydata: 0x30
   __DATA_CONST.__objc_arrayobj: 0x48
-  __DATA.__objc_const: 0xe30
-  __DATA.__objc_selrefs: 0x648
+  __DATA.__objc_const: 0xe40
+  __DATA.__objc_selrefs: 0x658
   __DATA.__objc_ivar: 0x94
   __DATA.__objc_data: 0x200
-  __DATA.__data: 0x310
+  __DATA.__data: 0x318
   __DATA.__bss: 0x1d0
   __DATA.__common: 0x10
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation

   - /usr/lib/swift/libswiftObjectiveC.dylib
   - /usr/lib/swift/libswiftXPC.dylib
   - /usr/lib/swift/libswift_Builtin_float.dylib
-  - /usr/lib/swift/libswift_errno.dylib
-  - /usr/lib/swift/libswift_math.dylib
-  - /usr/lib/swift/libswift_signal.dylib
-  - /usr/lib/swift/libswift_stdio.dylib
-  - /usr/lib/swift/libswift_time.dylib
+  - /usr/lib/swift/libswift_DarwinFoundation1.dylib
+  - /usr/lib/swift/libswift_DarwinFoundation2.dylib
+  - /usr/lib/swift/libswift_DarwinFoundation3.dylib
   - /usr/lib/swift/libswiftos.dylib
-  - /usr/lib/swift/libswiftsys_time.dylib
-  - /usr/lib/swift/libswiftunistd.dylib
-  UUID: 2867B610-EB37-3BDE-96F3-010F81A7886D
-  Functions: 243
-  Symbols:   181
-  CStrings:  790
+  UUID: C7BDDE69-2552-3FB2-A665-15C3DFD16567
+  Functions: 244
+  Symbols:   176
+  CStrings:  795
 
Symbols:
+ __swift_FORCE_LOAD_$_swift_DarwinFoundation1
+ __swift_FORCE_LOAD_$_swift_DarwinFoundation2
+ __swift_FORCE_LOAD_$_swift_DarwinFoundation3
+ _swift_allocError
- __swift_FORCE_LOAD_$_swift_errno
- __swift_FORCE_LOAD_$_swift_math
- __swift_FORCE_LOAD_$_swift_signal
- __swift_FORCE_LOAD_$_swift_stdio
- __swift_FORCE_LOAD_$_swift_time
- __swift_FORCE_LOAD_$_swiftsys_time
- __swift_FORCE_LOAD_$_swiftunistd
- _mach_get_times
- _objc_retain_x26
CStrings:
+ "@\"HIDEvent\"32@0:8@\"HIDEvent\"16@\"HIDConnection\"24"
+ "filterEvent:forClient:"
+ "filterSetProperty:forKey:forClient:"
+ "timestampUsToContinousMach:"
+ "v40@0:8^@16@\"NSString\"24@\"HIDConnection\"32"
+ "v40@0:8^@16@24@32"
- "timestampUsToAbsoluteMach:"

```
