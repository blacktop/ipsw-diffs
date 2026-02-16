## DesktopServicesHelper

> `/System/Library/PrivateFrameworks/DesktopServicesPriv.framework/DesktopServicesHelper`

```diff

-1827.3.2.0.0
-  __TEXT.__text: 0x6df8c
-  __TEXT.__auth_stubs: 0x17d0
-  __TEXT.__objc_stubs: 0x1d20
+1827.4.3.2.0
+  __TEXT.__text: 0x6fa58
+  __TEXT.__auth_stubs: 0x17b0
+  __TEXT.__objc_stubs: 0x1ce0
   __TEXT.__init_offsets: 0x4
   __TEXT.__objc_methlist: 0x78c
-  __TEXT.__const: 0x1840
-  __TEXT.__gcc_except_tab: 0x8e50
-  __TEXT.__cstring: 0x1b4a
+  __TEXT.__gcc_except_tab: 0x8d44
+  __TEXT.__cstring: 0x4256
+  __TEXT.__const: 0x17c8
   __TEXT.__oslogstring: 0x13c8
-  __TEXT.__objc_classname: 0x127
+  __TEXT.__objc_classname: 0x12b
   __TEXT.__ustring: 0x1a
-  __TEXT.__objc_methname: 0x1bec
-  __TEXT.__objc_methtype: 0xeb3
-  __TEXT.__unwind_info: 0x30c8
-  __DATA_CONST.__auth_got: 0xbf8
-  __DATA_CONST.__got: 0x4f8
-  __DATA_CONST.__const: 0x1c18
+  __TEXT.__objc_methname: 0x1bc3
+  __TEXT.__objc_methtype: 0xe9b
+  __TEXT.__unwind_info: 0x3178
+  __DATA_CONST.__auth_got: 0xbe8
+  __DATA_CONST.__got: 0x510
+  __DATA_CONST.__const: 0x1b58
   __DATA_CONST.__cfstring: 0x7c0
   __DATA_CONST.__objc_classlist: 0x38
   __DATA_CONST.__objc_catlist: 0x8

   __DATA_CONST.__objc_arrayobj: 0x18
   __DATA_CONST.__objc_intobj: 0x48
   __DATA.__objc_const: 0xce8
-  __DATA.__objc_selrefs: 0x8e8
+  __DATA.__objc_selrefs: 0x8d8
   __DATA.__objc_ivar: 0x78
   __DATA.__objc_data: 0x230
   __DATA.__data: 0x448
-  __DATA.__bss: 0x8a0
   __DATA.__common: 0x1be
+  __DATA.__bss: 0x8a0
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/CoreServices.framework/CoreServices
   - /System/Library/Frameworks/FileProvider.framework/FileProvider

   - /usr/lib/libbsm.0.dylib
   - /usr/lib/libc++.1.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: C77383A9-D82E-3C95-AA75-66081C7D39DD
-  Functions: 1790
-  Symbols:   557
-  CStrings:  950
+  UUID: 5EA394CF-E7A6-3696-A248-18769D011633
+  Functions: 1812
+  Symbols:   558
+  CStrings:  979
 
Symbols:
+ _CFPreferencesCopyValue
+ _CFStringAppendCString
+ __ZNSt3__132__internal_log_hardening_failureEPKc
+ _kCFPreferencesAnyApplication
+ _kCFPreferencesAnyHost
+ _kCFPreferencesCurrentUser
+ _objc_autorelease
+ _objc_retainAutoreleasedReturnValue
- _objc_claimAutoreleasedReturnValue
- _objc_retainAutoreleaseReturnValue
- _objc_retain_x3
- _objc_retain_x4
- _objc_retain_x5
- _objc_retain_x6
- _objc_retain_x9
CStrings:
+ "/AppleInternal/Library/BuildRoots/4~CHouugChnNzN38ZddrlHC4qh6QqD8sIFOvTYHfI/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/__algorithm/iterator_operations.h:209: libc++ Hardening assertion __count == 0 || (__dist < 0) == (__count < 0) failed: __sentinel must precede __iter when __count < 0\n"
+ "/AppleInternal/Library/BuildRoots/4~CHouugChnNzN38ZddrlHC4qh6QqD8sIFOvTYHfI/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/__algorithm/sort.h:293: libc++ Hardening assertion __k != __leftmost failed: Would read out of bounds, does your comparator satisfy the strict-weak ordering requirement?\n"
+ "/AppleInternal/Library/BuildRoots/4~CHouugChnNzN38ZddrlHC4qh6QqD8sIFOvTYHfI/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/__algorithm/sort.h:603: libc++ Hardening assertion __first != __end failed: Would read out of bounds, does your comparator satisfy the strict-weak ordering requirement?\n"
+ "/AppleInternal/Library/BuildRoots/4~CHouugChnNzN38ZddrlHC4qh6QqD8sIFOvTYHfI/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/__algorithm/sort.h:615: libc++ Hardening assertion __last != __begin failed: Would read out of bounds, does your comparator satisfy the strict-weak ordering requirement?\n"
+ "/AppleInternal/Library/BuildRoots/4~CHouugChnNzN38ZddrlHC4qh6QqD8sIFOvTYHfI/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/__algorithm/sort.h:633: libc++ Hardening assertion __first != __end failed: Would read out of bounds, does your comparator satisfy the strict-weak ordering requirement?\n"
+ "/AppleInternal/Library/BuildRoots/4~CHouugChnNzN38ZddrlHC4qh6QqD8sIFOvTYHfI/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/__algorithm/sort.h:638: libc++ Hardening assertion __last != __begin failed: Would read out of bounds, does your comparator satisfy the strict-weak ordering requirement?\n"
+ "/AppleInternal/Library/BuildRoots/4~CHouugChnNzN38ZddrlHC4qh6QqD8sIFOvTYHfI/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/__algorithm/sort.h:669: libc++ Hardening assertion __first != __end failed: Would read out of bounds, does your comparator satisfy the strict-weak ordering requirement?\n"
+ "/AppleInternal/Library/BuildRoots/4~CHouugChnNzN38ZddrlHC4qh6QqD8sIFOvTYHfI/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/__algorithm/sort.h:682: libc++ Hardening assertion __last != __begin failed: Would read out of bounds, does your comparator satisfy the strict-weak ordering requirement?\n"
+ "/AppleInternal/Library/BuildRoots/4~CHouugChnNzN38ZddrlHC4qh6QqD8sIFOvTYHfI/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/__algorithm/sort.h:692: libc++ Hardening assertion __first != __end failed: Would read out of bounds, does your comparator satisfy the strict-weak ordering requirement?\n"
+ "/AppleInternal/Library/BuildRoots/4~CHouugChnNzN38ZddrlHC4qh6QqD8sIFOvTYHfI/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/__algorithm/sort.h:697: libc++ Hardening assertion __last != __begin failed: Would read out of bounds, does your comparator satisfy the strict-weak ordering requirement?\n"
+ "/AppleInternal/Library/BuildRoots/4~CHouugChnNzN38ZddrlHC4qh6QqD8sIFOvTYHfI/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/__hash_table:1892: libc++ Hardening assertion __p != end() failed: unordered container::erase(iterator) called with a non-dereferenceable iterator\n"
+ "/AppleInternal/Library/BuildRoots/4~CHouugChnNzN38ZddrlHC4qh6QqD8sIFOvTYHfI/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/__utility/is_pointer_in_range.h:38: libc++ Hardening assertion std::__is_valid_range(__begin, __end) failed: [__begin, __end) is not a valid range\n"
+ "/AppleInternal/Library/BuildRoots/4~CHouugChnNzN38ZddrlHC4qh6QqD8sIFOvTYHfI/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/__vector/vector.h:1162: libc++ Hardening assertion __position != end() failed: vector::erase(iterator) called with a non-dereferenceable iterator\n"
+ "/AppleInternal/Library/BuildRoots/4~CHouugChnNzN38ZddrlHC4qh6QqD8sIFOvTYHfI/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/__vector/vector.h:1172: libc++ Hardening assertion __first <= __last failed: vector::erase(first, last) called with invalid range\n"
+ "/AppleInternal/Library/BuildRoots/4~CHouugChnNzN38ZddrlHC4qh6QqD8sIFOvTYHfI/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/__vector/vector.h:406: libc++ Hardening assertion __n < size() failed: vector[] index out of bounds\n"
+ "/AppleInternal/Library/BuildRoots/4~CHouugChnNzN38ZddrlHC4qh6QqD8sIFOvTYHfI/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/__vector/vector.h:410: libc++ Hardening assertion __n < size() failed: vector[] index out of bounds\n"
+ "/AppleInternal/Library/BuildRoots/4~CHouugChnNzN38ZddrlHC4qh6QqD8sIFOvTYHfI/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/__vector/vector.h:429: libc++ Hardening assertion !empty() failed: front() called on an empty vector\n"
+ "/AppleInternal/Library/BuildRoots/4~CHouugChnNzN38ZddrlHC4qh6QqD8sIFOvTYHfI/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/__vector/vector.h:433: libc++ Hardening assertion !empty() failed: back() called on an empty vector\n"
+ "/AppleInternal/Library/BuildRoots/4~CHouugChnNzN38ZddrlHC4qh6QqD8sIFOvTYHfI/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/__vector/vector.h:486: libc++ Hardening assertion !empty() failed: vector::pop_back called on an empty vector\n"
+ "/AppleInternal/Library/BuildRoots/4~CHouugChnNzN38ZddrlHC4qh6QqD8sIFOvTYHfI/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/deque:1565: libc++ Hardening assertion !empty() failed: deque::back called on an empty deque\n"
+ "/AppleInternal/Library/BuildRoots/4~CHouugChnNzN38ZddrlHC4qh6QqD8sIFOvTYHfI/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/deque:2310: libc++ Hardening assertion !empty() failed: deque::pop_back called on an empty deque\n"
+ "/AppleInternal/Library/BuildRoots/4~CHouugChnNzN38ZddrlHC4qh6QqD8sIFOvTYHfI/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/deque:2438: libc++ Hardening assertion __f != end() failed: deque::erase(iterator) called with a non-dereferenceable iterator\n"
+ "/AppleInternal/Library/BuildRoots/4~CHouugChnNzN38ZddrlHC4qh6QqD8sIFOvTYHfI/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/optional:796: libc++ Hardening assertion this->has_value() failed: optional operator-> called on a disengaged value\n"
+ "/AppleInternal/Library/BuildRoots/4~CHouugChnNzN38ZddrlHC4qh6QqD8sIFOvTYHfI/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/optional:806: libc++ Hardening assertion this->has_value() failed: optional operator* called on a disengaged value\n"
+ "/AppleInternal/Library/BuildRoots/4~CHouugChnNzN38ZddrlHC4qh6QqD8sIFOvTYHfI/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/string:1340: libc++ Hardening assertion __pos <= size() failed: string index out of bounds\n"
+ "/AppleInternal/Library/BuildRoots/4~CHouugChnNzN38ZddrlHC4qh6QqD8sIFOvTYHfI/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/string:1476: libc++ Hardening assertion !empty() failed: string::back(): string is empty\n"
+ "/AppleInternal/Library/BuildRoots/4~CHouugChnNzN38ZddrlHC4qh6QqD8sIFOvTYHfI/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/string:3371: libc++ Hardening assertion !empty() failed: string::pop_back(): string is already empty\n"
+ "/AppleInternal/Library/BuildRoots/4~CHouugChnNzN38ZddrlHC4qh6QqD8sIFOvTYHfI/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/string_view:329: libc++ Hardening assertion __len <= static_cast<size_type>(numeric_limits<difference_type>::max()) failed: string_view::string_view(_CharT *, size_t): length does not fit in difference_type\n"
+ "/AppleInternal/Library/BuildRoots/4~CHouugChnNzN38ZddrlHC4qh6QqD8sIFOvTYHfI/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/string_view:341: libc++ Hardening assertion (__end - __begin) >= 0 failed: std::string_view::string_view(iterator, sentinel) received invalid range\n"
+ "2 0"
+ "DOCFeature.override.DocumentManager."
+ "DSEnumeration_SMB_FPv2"
+ "DSEnumeration_USB_FPv2"
+ "DocumentManager"
+ "{unordered_map<NSProgress *, TKeyValueObserver, std::hash<NSProgress *>, std::equal_to<NSProgress *>, std::allocator<std::pair<NSProgress *const, TKeyValueObserver>>>=\"__table_\"{__hash_table<std::__hash_value_type<NSProgress *, TKeyValueObserver>, std::__unordered_map_hasher<NSProgress *, std::pair<NSProgress *const, TKeyValueObserver>, std::hash<NSProgress *>, std::equal_to<NSProgress *>>, std::__unordered_map_equal<NSProgress *, std::pair<NSProgress *const, TKeyValueObserver>, std::equal_to<NSProgress *>, std::hash<NSProgress *>>, std::allocator<std::pair<NSProgress *const, TKeyValueObserver>>>=\"__bucket_list_\"{unique_ptr<std::__hash_node_base<std::__hash_node<std::__hash_value_type<NSProgress *, TKeyValueObserver>, void *> *> *[], std::__bucket_list_deallocator<std::allocator<std::__hash_node_base<std::__hash_node<std::__hash_value_type<NSProgress *, TKeyValueObserver>, void *> *> *>>>=\"\"{?=\"__ptr_\"^^v\"__deleter_\"{__bucket_list_deallocator<std::allocator<std::__hash_node_base<std::__hash_node<std::__hash_value_type<NSProgress *, TKeyValueObserver>, void *> *> *>>=\"\"{?=\"__size_\"Q}}}}\"\"{?=\"__first_node_\"{__hash_node_base<std::__hash_node<std::__hash_value_type<NSProgress *, TKeyValueObserver>, void *> *>=\"__next_\"^v}}\"\"{?=\"__size_\"Q}\"\"{?=\"__max_load_factor_\"f}}}"
- "/.resolve"
- "FilesCopyOperationSizing"
- "_URLByRemovingResolveFlags"
- "_resolveFlags"
- "kFilesCopyOperationSizingMsg"
- "{unordered_map<NSProgress *, TKeyValueObserver, std::hash<NSProgress *>, std::equal_to<NSProgress *>, std::allocator<std::pair<NSProgress *const, TKeyValueObserver>>>=\"__table_\"{__hash_table<std::__hash_value_type<NSProgress *, TKeyValueObserver>, std::__unordered_map_hasher<NSProgress *, std::__hash_value_type<NSProgress *, TKeyValueObserver>, std::hash<NSProgress *>, std::equal_to<NSProgress *>>, std::__unordered_map_equal<NSProgress *, std::__hash_value_type<NSProgress *, TKeyValueObserver>, std::equal_to<NSProgress *>, std::hash<NSProgress *>>, std::allocator<std::__hash_value_type<NSProgress *, TKeyValueObserver>>>=\"__bucket_list_\"{unique_ptr<std::__hash_node_base<std::__hash_node<std::__hash_value_type<NSProgress *, TKeyValueObserver>, void *> *> *[], std::__bucket_list_deallocator<std::allocator<std::__hash_node_base<std::__hash_node<std::__hash_value_type<NSProgress *, TKeyValueObserver>, void *> *> *>>>=\"\"{?=\"__ptr_\"^^v\"__deleter_\"{__bucket_list_deallocator<std::allocator<std::__hash_node_base<std::__hash_node<std::__hash_value_type<NSProgress *, TKeyValueObserver>, void *> *> *>>=\"\"{?=\"__size_\"Q}}}}\"\"{?=\"__first_node_\"{__hash_node_base<std::__hash_node<std::__hash_value_type<NSProgress *, TKeyValueObserver>, void *> *>=\"__next_\"^v}}\"\"{?=\"__size_\"Q}\"\"{?=\"__max_load_factor_\"f}}}"

```
