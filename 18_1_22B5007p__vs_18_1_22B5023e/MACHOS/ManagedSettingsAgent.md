## ManagedSettingsAgent

> `/System/Library/Frameworks/ManagedSettings.framework/ManagedSettingsAgent`

```diff

-214.0.0.0.0
-  __TEXT.__text: 0x7db08
+215.0.0.0.0
+  __TEXT.__text: 0x7d5c8
   __TEXT.__auth_stubs: 0x23f0
   __TEXT.__objc_stubs: 0x20
   __TEXT.__objc_methlist: 0x214

   __TEXT.__swift5_assocty: 0xa8
   __TEXT.__swift5_proto: 0x108
   __TEXT.__swift5_types: 0x84
-  __TEXT.__oslogstring: 0x1f32
+  __TEXT.__oslogstring: 0x1f82
   __TEXT.__swift5_protos: 0x2c
   __TEXT.__swift5_capture: 0x34c
-  __TEXT.__info_plist: 0x54f
+  __TEXT.__info_plist: 0x55b
   __TEXT.__unwind_info: 0xe28
   __TEXT.__eh_frame: 0x2000
   __DATA_CONST.__auth_got: 0x1200
   __DATA_CONST.__got: 0x8f0
-  __DATA_CONST.__auth_ptr: 0x4d8
-  __DATA_CONST.__const: 0x18f0
+  __DATA_CONST.__auth_ptr: 0x4e8
+  __DATA_CONST.__const: 0x1930
   __DATA_CONST.__objc_classlist: 0x88
   __DATA_CONST.__objc_catlist: 0x10
   __DATA_CONST.__objc_protolist: 0xb8

   __DATA.__objc_const: 0x19b8
   __DATA.__objc_selrefs: 0x2f0
   __DATA.__objc_data: 0x5f8
-  __DATA.__data: 0x1ac0
+  __DATA.__data: 0x1ad0
   __DATA.__bss: 0x1990
   __DATA.__common: 0x68
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation

   - /usr/lib/swift/libswiftQuartzCore.dylib
   - /usr/lib/swift/libswiftUniformTypeIdentifiers.dylib
   - /usr/lib/swift/libswiftXPC.dylib
+  - /usr/lib/swift/libswift_Builtin_float.dylib
+  - /usr/lib/swift/libswift_errno.dylib
+  - /usr/lib/swift/libswift_math.dylib
+  - /usr/lib/swift/libswift_signal.dylib
+  - /usr/lib/swift/libswift_stdio.dylib
+  - /usr/lib/swift/libswift_time.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
+  - /usr/lib/swift/libswiftsys_time.dylib
+  - /usr/lib/swift/libswiftunistd.dylib
   Functions: 1174
-  Symbols:   968
+  Symbols:   976
   CStrings:  451
 
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
+ "Clear all settings for store with record ID “%!{(MISSING)public}s,” container “%!{(MISSING)public}s” and name “%!{(MISSING)public}s.” Is internal: %!{(MISSING)public}s"
+ "Deleting stores “%!{(MISSING)public}s” with record ID “%!{(MISSING)public}s,” container “%!{(MISSING)public}s.” Is internal: %!{(MISSING)public}s"
+ "Get all settings for store with record ID “%!{(MISSING)public}s,” container “%!{(MISSING)public}s” and name “%!{(MISSING)public}s.” Is internal: %!{(MISSING)public}s"
+ "Get settings %!{(MISSING)public}s for store with record ID “%!{(MISSING)public}s,” container “%!{(MISSING)public}s” and name “%!{(MISSING)public}s.” Is internal: %!{(MISSING)public}s"
+ "Get store names for store with record ID “%!{(MISSING)public}s” and container “%!{(MISSING)public}s.” Is internal: %!{(MISSING)public}s"
+ "Get store properties for store with record ID “%!{(MISSING)public}s,” container “%!{(MISSING)public}s” and name “%!{(MISSING)public}s.” Is internal: %!{(MISSING)public}s"
+ "Remove values for settings %!{(MISSING)public}s for store with record ID “%!{(MISSING)public}s,” container “%!{(MISSING)public}s” and name “%!{(MISSING)public}s.” Is internal: %!{(MISSING)public}s"
+ "Set values %!{(MISSING)private}s for store with record ID “%!{(MISSING)public}s,” container “%!{(MISSING)public}s” and name “%!{(MISSING)public}s.” Is internal: %!{(MISSING)public}s"
+ "Update store properties %!s(MISSING) for store with record ID “%!{(MISSING)public}s,” container “%!{(MISSING)public}s” and name “%!{(MISSING)public}s.” Is internal: %!{(MISSING)public}s"
+ "Updating store with record ID “%!{(MISSING)public}s,” container “%!{(MISSING)public}s.” Is internal: %!{(MISSING)public}s"
- "Clear all settings for store with record ID “%!{(MISSING)public}s,” container “%!{(MISSING)public}s” and name “%!{(MISSING)public}s.” Is internal: %!s(MISSING)"
- "Deleting stores “%!{(MISSING)public}s” with record ID “%!{(MISSING)public}s,” container “%!{(MISSING)public}s.” Is internal: %!s(MISSING)"
- "Get all settings for store with record ID “%!{(MISSING)public}s,” container “%!{(MISSING)public}s” and name “%!{(MISSING)public}s.” Is internal: %!s(MISSING)"
- "Get settings %!{(MISSING)public}s for store with record ID “%!{(MISSING)public}s,” container “%!{(MISSING)public}s” and name “%!{(MISSING)public}s.” Is internal: %!s(MISSING)"
- "Get store names for store with record ID “%!{(MISSING)public}s” and container “%!{(MISSING)public}s.” Is internal: %!s(MISSING)"
- "Get store properties for store with record ID “%!{(MISSING)public}s,” container “%!{(MISSING)public}s” and name “%!{(MISSING)public}s.” Is internal: %!s(MISSING)"
- "Remove values for settings %!{(MISSING)public}s for store with record ID “%!{(MISSING)public}s,” container “%!{(MISSING)public}s” and name “%!{(MISSING)public}s.” Is internal: %!s(MISSING)"
- "Set values %!{(MISSING)public}s for store with record ID “%!{(MISSING)public}s,” container “%!{(MISSING)public}s” and name “%!{(MISSING)public}s.” Is internal: %!s(MISSING)"
- "Update store properties %!s(MISSING) for store with record ID “%!{(MISSING)public}s,” container “%!{(MISSING)public}s” and name “%!{(MISSING)public}s.” Is internal: %!s(MISSING)"
- "Updating store with record ID “%!{(MISSING)public}s,” container “%!{(MISSING)public}s.” Is internal: %!s(MISSING)"

```