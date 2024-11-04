## libswiftCore.dylib

> `/usr/lib/swift/libswiftCore.dylib`

```diff

-6.0.0.7.44
-  __TEXT.__text: 0x4a5a9c
-  __TEXT.__auth_stubs: 0xc80
+6.0.3.1.3
+  __TEXT.__text: 0x4a4728
+  __TEXT.__auth_stubs: 0xc70
   __TEXT.__delay_stubs: 0x108
   __TEXT.__delay_helper: 0x258
   __TEXT.__init_offsets: 0x18
-  __TEXT.__objc_methlist: 0x1a04
+  __TEXT.__objc_methlist: 0xfc4
   __TEXT.__const: 0xb1544
   __TEXT.__lldbsummaries: 0x46
-  __TEXT.__cstring: 0x12be0
+  __TEXT.__cstring: 0x1241c
   __TEXT.__swift5_typeref: 0x57d7
   __TEXT.__swift5_capture: 0x3ac
   __TEXT.__swift5_reflstr: 0x1251

   __TEXT.__swift5_types: 0x8e4
   __TEXT.__oslogstring: 0xb7
   __TEXT.__gcc_except_tab: 0xd8
-  __TEXT.__unwind_info: 0xaca0
+  __TEXT.__unwind_info: 0xac88
   __TEXT.__eh_frame: 0x88b4
   __TEXT.__objc_classname: 0x139
   __TEXT.__objc_methname: 0x891

   __DATA_CONST.__objc_selrefs: 0x390
   __DATA_CONST.__objc_protorefs: 0x58
   __DATA_CONST.__objc_superrefs: 0x40
-  __AUTH_CONST.__auth_got: 0x680
+  __AUTH_CONST.__auth_got: 0x678
   __AUTH_CONST.__auth_ptr: 0x58
   __AUTH_CONST.__const: 0x14ff0
   __AUTH_CONST.__objc_const: 0x4bd0

   __DATA.__objc_ivar: 0x38
   __DATA.__data: 0xbc8
   __DATA.__crash_info: 0x40
-  __DATA.__bss: 0xfef8
-  __DATA.__common: 0x78
-  __DATA_DIRTY.__objc_data: 0xdb8
+  __DATA.__bss: 0xfef0
+  __DATA.__common: 0x58
+  __DATA_DIRTY.__objc_data: 0x2048
   __DATA_DIRTY.__data: 0x2fc0
-  __DATA_DIRTY.__bss: 0x15b18
+  __DATA_DIRTY.__bss: 0x15ad0
   __DATA_DIRTY.__common: 0x50
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/Foundation.framework/Foundation
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libc++.1.dylib
   - /usr/lib/libobjc.A.dylib
+  - /usr/lib/libswiftPrespecialized.dylib
   - /usr/lib/swift/libswiftObjectiveC.dylib
-  Functions: 21163
-  Symbols:   30969
-  CStrings:  2900
+  Functions: 21159
+  Symbols:   30964
+  CStrings:  2872
 
Symbols:
- __dyld_is_preoptimized_objc_image_loaded
CStrings:
+ "%!u(MISSING) %!s(MISSING) 0x%!t(MISSING)x\n"
+ "Enable use of prespecializations library."
+ "Prespecializations library: Disabling, SWIFT_DEBUG_ENABLE_LIB_PRESPECIALIZED = %!d(MISSING)\n"
+ "Prespecializations library: Not calling _dyld_get_swift_prespecialized_data dyld_shared_cache_some_image_overridden = %!d(MISSING)\n"
+ "SWIFT_DEBUG_ENABLE_LIB_PRESPECIALIZED"
+ "SWIFT_DEBUG_ENABLE_LIB_PRESPECIALIZED="
- "Disabling metadata, SWIFT_DEBUG_ENABLE_LIB_PRESPECIALIZED_METADATA is false."
- "Enable use of descriptor map in prespecializations library."
- "Enable use of metadata in prespecializations library."
- "Prespecializations library:   descriptorMap=%!p(MISSING)\n"
- "Prespecializations library:   disabledProcessTable=%!p(MISSING)\n"
- "Prespecializations library:   metadataMap=%!p(MISSING)\n"
- "Prespecializations library:   optionFlags=%!z(MISSING)x\n"
- "Prespecializations library:   pointerKeyedMetadataMap=%!p(MISSING)\n"
- "Prespecializations library: %!s(MISSING)\n"
- "Prespecializations library: Descriptor table lookup of '%!(BADPREC)%!s(MISSING)' returned NULL pointer to descriptor pointer.\n"
- "Prespecializations library: Did not find descriptor for key '%!(BADPREC)%!s(MISSING)'.\n"
- "Prespecializations library: Disabling prespecialized metadata, dyld_shared_cache_some_image_overridden = %!d(MISSING)\n"
- "Prespecializations library: Failed to build demangling for node %!p(MISSING).\n"
- "Prespecializations library: Failed to build demangling for simplified node %!p(MISSING).\n\n"
- "Prespecializations library: Failed to build simplified mangling for node %!p(MISSING).\n"
- "Prespecializations library: Found descriptor %!p(MISSING) for key '%!(BADPREC)%!s(MISSING)'.\n"
- "Prespecializations library: Hash table lookup checked %!u(MISSING) loaded entries, %!u(MISSING) total entries, starting data pointer %!p(MISSING), starting auxiliary pointer %!p(MISSING).\n"
- "Prespecializations library: Looking up descriptor named '%!(BADPREC)%!s(MISSING)'.\n"
- "Prespecializations library: Returning data pointer %!p(MISSING)\n"
- "Prespecializations library: Setting descriptorMapEnabled=%!s(MISSING) from SWIFT_DEBUG_ENABLE_LIB_PRESPECIALIZED_DESCRIPTOR_LOOKUP.\n"
- "Prespecializations library: Setting descriptorMapEnabled=%!s(MISSING) from the option flags.\n"
- "Prespecializations library: Toggling descriptorMapEnabled to %!s(MISSING) togglePrespecializationDescriptorMap is set.\n"
- "SWIFT_DEBUG_ENABLE_LIB_PRESPECIALIZED_DESCRIPTOR_LOOKUP"
- "SWIFT_DEBUG_ENABLE_LIB_PRESPECIALIZED_DESCRIPTOR_LOOKUP="
- "SWIFT_DEBUG_ENABLE_LIB_PRESPECIALIZED_METADATA"
- "SWIFT_DEBUG_ENABLE_LIB_PRESPECIALIZED_METADATA="
- "SWIFT_DEBUG_VALIDATE_LIB_PRESPECIALIZED_DESCRIPTOR_LOOKUP"
- "SWIFT_DEBUG_VALIDATE_LIB_PRESPECIALIZED_DESCRIPTOR_LOOKUP="
- "Searching for type descriptor, prespecialized descriptor map returned %!p(MISSING), but scan returned %!p(MISSING). Node tree:\n%!s(MISSING)"
- "Unable to obtain Swift runtime path\n"
- "Validate results from the prespecializations map descriptor map by comparing to a full scan."
- "swift runtime: unable to locate swift-backtrace; disabling backtracing.\n"
- "swift-backtrace"
- "togglePrespecializationDescriptorMap"

```
