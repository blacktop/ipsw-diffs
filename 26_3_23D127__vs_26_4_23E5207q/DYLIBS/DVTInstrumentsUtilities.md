## DVTInstrumentsUtilities

> `/System/Library/PrivateFrameworks/DVTInstrumentsUtilities.framework/DVTInstrumentsUtilities`

```diff

-64573.4.1.0.0
-  __TEXT.__text: 0x2c0ec
-  __TEXT.__auth_stubs: 0x13d0
-  __TEXT.__objc_methlist: 0x2ec4
-  __TEXT.__const: 0x126c
-  __TEXT.__cstring: 0x58a7
-  __TEXT.__gcc_except_tab: 0x153c
+64575.69.1.0.0
+  __TEXT.__text: 0x2e648
+  __TEXT.__auth_stubs: 0x13e0
+  __TEXT.__objc_methlist: 0x2ee4
+  __TEXT.__const: 0x154c
+  __TEXT.__cstring: 0x5df6
+  __TEXT.__gcc_except_tab: 0x1358
   __TEXT.__oslogstring: 0x799
   __TEXT.__ustring: 0x34
-  __TEXT.__constg_swiftt: 0xe8
-  __TEXT.__swift5_typeref: 0x17d
+  __TEXT.__constg_swiftt: 0x12c
+  __TEXT.__swift5_typeref: 0x1b7
   __TEXT.__swift5_builtin: 0x14
-  __TEXT.__swift5_reflstr: 0xc5
-  __TEXT.__swift5_fieldmd: 0x13c
-  __TEXT.__swift5_types: 0x1c
-  __TEXT.__swift5_assocty: 0x38
-  __TEXT.__swift5_proto: 0x48
-  __TEXT.__unwind_info: 0x1288
-  __TEXT.__eh_frame: 0x1c8
-  __TEXT.__objc_classname: 0xac6
-  __TEXT.__objc_methname: 0x5871
-  __TEXT.__objc_methtype: 0x1c11
-  __TEXT.__objc_stubs: 0x43c0
+  __TEXT.__swift5_reflstr: 0xeb
+  __TEXT.__swift5_fieldmd: 0x198
+  __TEXT.__swift5_types: 0x24
+  __TEXT.__swift5_assocty: 0x68
+  __TEXT.__swift5_proto: 0x7c
+  __TEXT.__unwind_info: 0x1370
+  __TEXT.__eh_frame: 0x210
+  __TEXT.__objc_classname: 0xad4
+  __TEXT.__objc_methname: 0x58bf
+  __TEXT.__objc_methtype: 0x1bfc
+  __TEXT.__objc_stubs: 0x4400
   __DATA_CONST.__got: 0x558
-  __DATA_CONST.__const: 0x2248
+  __DATA_CONST.__const: 0x2260
   __DATA_CONST.__objc_classlist: 0x290
   __DATA_CONST.__objc_catlist: 0x78
   __DATA_CONST.__objc_protolist: 0x98
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x1890
+  __DATA_CONST.__objc_selrefs: 0x18a0
   __DATA_CONST.__objc_protorefs: 0x10
   __DATA_CONST.__objc_superrefs: 0x150
   __DATA_CONST.__objc_arraydata: 0x120
-  __AUTH_CONST.__auth_got: 0xa00
-  __AUTH_CONST.__const: 0xaf0
-  __AUTH_CONST.__cfstring: 0x8700
-  __AUTH_CONST.__objc_const: 0x61d0
+  __AUTH_CONST.__auth_got: 0xa08
+  __AUTH_CONST.__const: 0xcc8
+  __AUTH_CONST.__cfstring: 0x87c0
+  __AUTH_CONST.__objc_const: 0x61e8
   __AUTH_CONST.__objc_intobj: 0x180
   __AUTH_CONST.__objc_dictobj: 0xa0
   __AUTH.__objc_data: 0x19c0
   __AUTH.__data: 0x28
   __DATA.__objc_ivar: 0x31c
-  __DATA.__data: 0x960
-  __DATA.__bss: 0xc10
+  __DATA.__data: 0x9a8
+  __DATA.__bss: 0x1290
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/Foundation.framework/Foundation
   - /usr/lib/libSystem.B.dylib

   - /usr/lib/swift/libswift_Builtin_float.dylib
   - /usr/lib/swift/libswift_StringProcessing.dylib
   - /usr/lib/swift/libswiftos.dylib
-  UUID: CC046E73-1EAC-3430-BED9-ADAD2817DA4D
-  Functions: 1335
-  Symbols:   572
-  CStrings:  3700
+  UUID: 9273A0CE-A4A6-3615-8C3A-F6056BCA3211
+  Functions: 1403
+  Symbols:   569
+  CStrings:  3718
 
Symbols:
+ __ZNSt3__132__internal_log_hardening_failureEPKc
+ _bzero
+ _objc_retain_x28
- _objc_claimAutoreleasedReturnValue
- _objc_retainAutoreleaseReturnValue
- _objc_retain_x4
- _objc_retain_x6
- _objc_retain_x8
- _objc_retain_x9
CStrings:
+ "+[NSProcessInfo(DVTInstrumentsUtilities) xr_isRunningVirtualized]"
+ "/AppleInternal/Library/BuildRoots/4~CHwHugDti1ao2c-t1Sw163hH_KuVIA7UiQj_CgA/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/__hash_table:1892: libc++ Hardening assertion __p != end() failed: unordered container::erase(iterator) called with a non-dereferenceable iterator\n"
+ "/AppleInternal/Library/BuildRoots/4~CHwHugDti1ao2c-t1Sw163hH_KuVIA7UiQj_CgA/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/__vector/vector.h:1172: libc++ Hardening assertion __first <= __last failed: vector::erase(first, last) called with invalid range\n"
+ "/AppleInternal/Library/BuildRoots/4~CHwHugDti1ao2c-t1Sw163hH_KuVIA7UiQj_CgA/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/__vector/vector.h:406: libc++ Hardening assertion __n < size() failed: vector[] index out of bounds\n"
+ "/AppleInternal/Library/BuildRoots/4~CHwHugDti1ao2c-t1Sw163hH_KuVIA7UiQj_CgA/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/array:271: libc++ Hardening assertion __n < _Size failed: out-of-bounds access in std::array<T, N>\n"
+ "Build/Products"
+ "EL0"
+ "EL0/1"
+ "EL1"
+ "Invalid engineering type"
+ "KDebug Category"
+ "KdebugSignpostHelpURL"
+ "Tagged Backtrace"
+ "XREngineeringValueFormatter.m"
+ "bundleURL"
+ "tagged backtrace"
+ "tagged-backtrace"
+ "xr_isAppleInternal"
+ "xr_isLikelyInferior"
+ "xr_isRunningVirtualized"
+ "{unordered_map<unsigned long long, id, std::hash<unsigned long long>, std::equal_to<unsigned long long>, std::allocator<std::pair<const unsigned long long, id>>>=\"__table_\"{__hash_table<std::__hash_value_type<unsigned long long, id>, std::__unordered_map_hasher<unsigned long long, std::pair<const unsigned long long, id>, std::hash<unsigned long long>, std::equal_to<unsigned long long>>, std::__unordered_map_equal<unsigned long long, std::pair<const unsigned long long, id>, std::equal_to<unsigned long long>, std::hash<unsigned long long>>, std::allocator<std::pair<const unsigned long long, id>>>=\"__bucket_list_\"{unique_ptr<std::__hash_node_base<std::__hash_node<std::__hash_value_type<unsigned long long, id>, void *> *> *[], std::__bucket_list_deallocator<std::allocator<std::__hash_node_base<std::__hash_node<std::__hash_value_type<unsigned long long, id>, void *> *> *>>>=\"\"{?=\"__ptr_\"^^v\"__deleter_\"{__bucket_list_deallocator<std::allocator<std::__hash_node_base<std::__hash_node<std::__hash_value_type<unsigned long long, id>, void *> *> *>>=\"\"{?=\"__size_\"Q}}}}\"\"{?=\"__first_node_\"{__hash_node_base<std::__hash_node<std::__hash_value_type<unsigned long long, id>, void *> *>=\"__next_\"^v}}\"\"{?=\"__size_\"Q}\"\"{?=\"__max_load_factor_\"f}}}"
- "+[NSProcessInfo(DVTInstrumentsUtilities) isRunningVirtualized]"
- "KDebug Plist Subtrack Name"
- "isAppleInternal"
- "isRunningVirtualized"
- "{unordered_map<unsigned long long, id, std::hash<unsigned long long>, std::equal_to<unsigned long long>, std::allocator<std::pair<const unsigned long long, id>>>=\"__table_\"{__hash_table<std::__hash_value_type<unsigned long long, id>, std::__unordered_map_hasher<unsigned long long, std::__hash_value_type<unsigned long long, id>, std::hash<unsigned long long>, std::equal_to<unsigned long long>>, std::__unordered_map_equal<unsigned long long, std::__hash_value_type<unsigned long long, id>, std::equal_to<unsigned long long>, std::hash<unsigned long long>>, std::allocator<std::__hash_value_type<unsigned long long, id>>>=\"__bucket_list_\"{unique_ptr<std::__hash_node_base<std::__hash_node<std::__hash_value_type<unsigned long long, id>, void *> *> *[], std::__bucket_list_deallocator<std::allocator<std::__hash_node_base<std::__hash_node<std::__hash_value_type<unsigned long long, id>, void *> *> *>>>=\"\"{?=\"__ptr_\"^^v\"__deleter_\"{__bucket_list_deallocator<std::allocator<std::__hash_node_base<std::__hash_node<std::__hash_value_type<unsigned long long, id>, void *> *> *>>=\"\"{?=\"__size_\"Q}}}}\"\"{?=\"__first_node_\"{__hash_node_base<std::__hash_node<std::__hash_value_type<unsigned long long, id>, void *> *>=\"__next_\"^v}}\"\"{?=\"__size_\"Q}\"\"{?=\"__max_load_factor_\"f}}}"

```
