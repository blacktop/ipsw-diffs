## analyticsd

> `/System/Library/PrivateFrameworks/CoreAnalytics.framework/Support/analyticsd`

```diff

-415.0.0.0.0
-  __TEXT.__text: 0xfd1dc
+417.0.0.0.0
+  __TEXT.__text: 0xfd8ec
   __TEXT.__auth_stubs: 0x1a30
   __TEXT.__objc_stubs: 0x25e0
   __TEXT.__init_offsets: 0x20
   __TEXT.__objc_methlist: 0x56c
-  __TEXT.__cstring: 0xeafa
-  __TEXT.__const: 0x9ae5
-  __TEXT.__gcc_except_tab: 0xf9e8
+  __TEXT.__cstring: 0xeb0a
+  __TEXT.__const: 0x9b95
+  __TEXT.__gcc_except_tab: 0xfa18
   __TEXT.__oslogstring: 0x15325
   __TEXT.__objc_classname: 0x168
   __TEXT.__objc_methtype: 0x1786

   __TEXT.__swift5_typeref: 0x14
   __TEXT.__swift5_fieldmd: 0x10
   __TEXT.__swift5_types: 0x4
-  __TEXT.__unwind_info: 0x66f8
+  __TEXT.__unwind_info: 0x6720
   __DATA_CONST.__auth_got: 0xd30
   __DATA_CONST.__got: 0x570
   __DATA_CONST.__auth_ptr: 0x10
-  __DATA_CONST.__const: 0x97c0
+  __DATA_CONST.__const: 0x9800
   __DATA_CONST.__cfstring: 0xa80
   __DATA_CONST.__objc_classlist: 0x40
   __DATA_CONST.__objc_protolist: 0x38

   - /usr/lib/swift/libswiftObjectiveC.dylib
   - /usr/lib/swift/libswiftQuartzCore.dylib
   - /usr/lib/swift/libswiftXPC.dylib
+  - /usr/lib/swift/libswift_Builtin_float.dylib
+  - /usr/lib/swift/libswift_errno.dylib
+  - /usr/lib/swift/libswift_math.dylib
+  - /usr/lib/swift/libswift_signal.dylib
+  - /usr/lib/swift/libswift_stdio.dylib
+  - /usr/lib/swift/libswift_time.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  Functions: 4947
-  Symbols:   623
+  - /usr/lib/swift/libswiftsys_time.dylib
+  - /usr/lib/swift/libswiftunistd.dylib
+  Functions: 4954
+  Symbols:   631
   CStrings:  3144
 
Symbols:
+ __swift_FORCE_LOAD_$_swift_Builtin_float
+ __swift_FORCE_LOAD_$_swift_errno
+ __swift_FORCE_LOAD_$_swift_math
+ __swift_FORCE_LOAD_$_swift_signal
+ __swift_FORCE_LOAD_$_swift_stdio
+ __swift_FORCE_LOAD_$_swift_time
+ __swift_FORCE_LOAD_$_swiftsys_time
+ __swift_FORCE_LOAD_$_swiftunistd
CStrings:
+ "SELECT queried_state_value, queried_state_last_modified, queried_state_ttl FROM queried_states WHERE queried_state_name=?1 AND (queried_state_params = '' OR queried_state_params IS NULL OR  queried_state_params=?2) LIMIT 1;"
+ "char_traits<char_type>::to_char_type(current) == literal_text[0]"
- "SELECT queried_state_value, queried_state_last_modified, queried_state_ttl FROM queried_states WHERE queried_state_name=?1 AND (queried_state_params IS NULL OR queried_state_params=?2) LIMIT 1;"
- "std::char_traits<char_type>::to_char_type(current) == literal_text[0]"

```
