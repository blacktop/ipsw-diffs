## analyticsd

> `/System/Library/PrivateFrameworks/CoreAnalytics.framework/Support/analyticsd`

```diff

-496.60.2.0.0
-  __TEXT.__text: 0x126564
-  __TEXT.__auth_stubs: 0x1b00
+501.100.11.0.0
+  __TEXT.__text: 0x12462c
+  __TEXT.__auth_stubs: 0x1ad0
   __TEXT.__objc_stubs: 0x2760
   __TEXT.__init_offsets: 0x20
-  __TEXT.__objc_methlist: 0xa04
-  __TEXT.__cstring: 0x13291
-  __TEXT.__const: 0xaf3d
-  __TEXT.__gcc_except_tab: 0x129e8
-  __TEXT.__oslogstring: 0x1722c
+  __TEXT.__objc_methlist: 0xa14
+  __TEXT.__cstring: 0x159fa
+  __TEXT.__const: 0xac67
+  __TEXT.__gcc_except_tab: 0x12d64
+  __TEXT.__oslogstring: 0x174de
   __TEXT.__objc_classname: 0x168
   __TEXT.__objc_methtype: 0x1463
-  __TEXT.__objc_methname: 0x2885
-  __TEXT.__unwind_info: 0x75b0
-  __DATA_CONST.__auth_got: 0xd98
-  __DATA_CONST.__got: 0x5d0
+  __TEXT.__objc_methname: 0x2880
+  __TEXT.__unwind_info: 0x77c0
+  __DATA_CONST.__auth_got: 0xd80
+  __DATA_CONST.__got: 0x5c8
   __DATA_CONST.__auth_ptr: 0x8
-  __DATA_CONST.__const: 0xad58
+  __DATA_CONST.__const: 0xad98
   __DATA_CONST.__cfstring: 0xaa0
   __DATA_CONST.__objc_classlist: 0x38
   __DATA_CONST.__objc_protolist: 0x38

   - /usr/lib/libc++.1.dylib
   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libsqlite3.dylib
-  UUID: 43ADF139-A5B6-3469-93A7-4A87ACF699F8
-  Functions: 5670
-  Symbols:   648
-  CStrings:  3800
+  UUID: 2A4423AF-5F72-3B50-B552-D8B0EC3310D0
+  Functions: 5782
+  Symbols:   644
+  CStrings:  3845
 
Symbols:
+ __ZNSt3__132__internal_log_hardening_failureEPKc
+ _objc_retain_x27
+ _objc_retain_x28
- _OBJC_CLASS_$_NSBundle
- _objc_claimAutoreleasedReturnValue
- _objc_retainAutoreleaseReturnValue
- _objc_retain_x1
- _objc_retain_x2
- _objc_retain_x3
- _objc_retain_x9
CStrings:
+ " - "
+ "&(mpos->first) == s_data.cont.back().second"
+ ".XPC"
+ "/AppleInternal/Library/BuildRoots/4~CH-kugCSNxlzBMFB_ZM8YSYv_Du9IUDoW-iXb3k/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/__hash_table:1892: libc++ Hardening assertion __p != end() failed: unordered container::erase(iterator) called with a non-dereferenceable iterator\n"
+ "/AppleInternal/Library/BuildRoots/4~CH-kugCSNxlzBMFB_ZM8YSYv_Du9IUDoW-iXb3k/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/__utility/is_pointer_in_range.h:38: libc++ Hardening assertion std::__is_valid_range(__begin, __end) failed: [__begin, __end) is not a valid range\n"
+ "/AppleInternal/Library/BuildRoots/4~CH-kugCSNxlzBMFB_ZM8YSYv_Du9IUDoW-iXb3k/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/__vector/vector.h:1162: libc++ Hardening assertion __position != end() failed: vector::erase(iterator) called with a non-dereferenceable iterator\n"
+ "/AppleInternal/Library/BuildRoots/4~CH-kugCSNxlzBMFB_ZM8YSYv_Du9IUDoW-iXb3k/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/__vector/vector.h:1172: libc++ Hardening assertion __first <= __last failed: vector::erase(first, last) called with invalid range\n"
+ "/AppleInternal/Library/BuildRoots/4~CH-kugCSNxlzBMFB_ZM8YSYv_Du9IUDoW-iXb3k/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/__vector/vector.h:406: libc++ Hardening assertion __n < size() failed: vector[] index out of bounds\n"
+ "/AppleInternal/Library/BuildRoots/4~CH-kugCSNxlzBMFB_ZM8YSYv_Du9IUDoW-iXb3k/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/__vector/vector.h:410: libc++ Hardening assertion __n < size() failed: vector[] index out of bounds\n"
+ "/AppleInternal/Library/BuildRoots/4~CH-kugCSNxlzBMFB_ZM8YSYv_Du9IUDoW-iXb3k/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/__vector/vector.h:425: libc++ Hardening assertion !empty() failed: front() called on an empty vector\n"
+ "/AppleInternal/Library/BuildRoots/4~CH-kugCSNxlzBMFB_ZM8YSYv_Du9IUDoW-iXb3k/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/__vector/vector.h:433: libc++ Hardening assertion !empty() failed: back() called on an empty vector\n"
+ "/AppleInternal/Library/BuildRoots/4~CH-kugCSNxlzBMFB_ZM8YSYv_Du9IUDoW-iXb3k/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/__vector/vector.h:486: libc++ Hardening assertion !empty() failed: vector::pop_back called on an empty vector\n"
+ "/AppleInternal/Library/BuildRoots/4~CH-kugCSNxlzBMFB_ZM8YSYv_Du9IUDoW-iXb3k/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/__vector/vector_bool.h:301: libc++ Hardening assertion !empty() failed: vector<bool>::back() called on an empty vector\n"
+ "/AppleInternal/Library/BuildRoots/4~CH-kugCSNxlzBMFB_ZM8YSYv_Du9IUDoW-iXb3k/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/__vector/vector_bool.h:333: libc++ Hardening assertion !empty() failed: vector<bool>::pop_back called on an empty vector\n"
+ "/AppleInternal/Library/BuildRoots/4~CH-kugCSNxlzBMFB_ZM8YSYv_Du9IUDoW-iXb3k/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/array:271: libc++ Hardening assertion __n < _Size failed: out-of-bounds access in std::array<T, N>\n"
+ "/AppleInternal/Library/BuildRoots/4~CH-kugCSNxlzBMFB_ZM8YSYv_Du9IUDoW-iXb3k/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/deque:1565: libc++ Hardening assertion !empty() failed: deque::back called on an empty deque\n"
+ "/AppleInternal/Library/BuildRoots/4~CH-kugCSNxlzBMFB_ZM8YSYv_Du9IUDoW-iXb3k/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/deque:1572: libc++ Hardening assertion !empty() failed: deque::back called on an empty deque\n"
+ "/AppleInternal/Library/BuildRoots/4~CH-kugCSNxlzBMFB_ZM8YSYv_Du9IUDoW-iXb3k/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/deque:2310: libc++ Hardening assertion !empty() failed: deque::pop_back called on an empty deque\n"
+ "/AppleInternal/Library/BuildRoots/4~CH-kugCSNxlzBMFB_ZM8YSYv_Du9IUDoW-iXb3k/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/deque:2464: libc++ Hardening assertion __f <= __l failed: deque::erase(first, last) called with an invalid range\n"
+ "/AppleInternal/Library/BuildRoots/4~CH-kugCSNxlzBMFB_ZM8YSYv_Du9IUDoW-iXb3k/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/list:1402: libc++ Hardening assertion !empty() failed: list::pop_front() called with empty list\n"
+ "/AppleInternal/Library/BuildRoots/4~CH-kugCSNxlzBMFB_ZM8YSYv_Du9IUDoW-iXb3k/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/list:1420: libc++ Hardening assertion __p != end() failed: list::erase(iterator) called with a non-dereferenceable iterator\n"
+ "/AppleInternal/Library/BuildRoots/4~CH-kugCSNxlzBMFB_ZM8YSYv_Du9IUDoW-iXb3k/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/list:836: libc++ Hardening assertion !empty() failed: list::back called on empty list\n"
+ "/AppleInternal/Library/BuildRoots/4~CH-kugCSNxlzBMFB_ZM8YSYv_Du9IUDoW-iXb3k/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/optional:796: libc++ Hardening assertion this->has_value() failed: optional operator-> called on a disengaged value\n"
+ "/AppleInternal/Library/BuildRoots/4~CH-kugCSNxlzBMFB_ZM8YSYv_Du9IUDoW-iXb3k/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/optional:801: libc++ Hardening assertion this->has_value() failed: optional operator-> called on a disengaged value\n"
+ "/AppleInternal/Library/BuildRoots/4~CH-kugCSNxlzBMFB_ZM8YSYv_Du9IUDoW-iXb3k/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/optional:806: libc++ Hardening assertion this->has_value() failed: optional operator* called on a disengaged value\n"
+ "/AppleInternal/Library/BuildRoots/4~CH-kugCSNxlzBMFB_ZM8YSYv_Du9IUDoW-iXb3k/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/optional:811: libc++ Hardening assertion this->has_value() failed: optional operator* called on a disengaged value\n"
+ "/AppleInternal/Library/BuildRoots/4~CH-kugCSNxlzBMFB_ZM8YSYv_Du9IUDoW-iXb3k/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/streambuf:279: libc++ Hardening assertion std::__is_valid_range(__gbeg, __gnext) failed: [gbeg, gnext) must be a valid range\n"
+ "/AppleInternal/Library/BuildRoots/4~CH-kugCSNxlzBMFB_ZM8YSYv_Du9IUDoW-iXb3k/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/streambuf:280: libc++ Hardening assertion std::__is_valid_range(__gbeg, __gend) failed: [gbeg, gend) must be a valid range\n"
+ "/AppleInternal/Library/BuildRoots/4~CH-kugCSNxlzBMFB_ZM8YSYv_Du9IUDoW-iXb3k/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/streambuf:281: libc++ Hardening assertion std::__is_valid_range(__gnext, __gend) failed: [gnext, gend) must be a valid range\n"
+ "/AppleInternal/Library/BuildRoots/4~CH-kugCSNxlzBMFB_ZM8YSYv_Du9IUDoW-iXb3k/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/string:1332: libc++ Hardening assertion __pos <= size() failed: string index out of bounds\n"
+ "/AppleInternal/Library/BuildRoots/4~CH-kugCSNxlzBMFB_ZM8YSYv_Du9IUDoW-iXb3k/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/string:1340: libc++ Hardening assertion __pos <= size() failed: string index out of bounds\n"
+ "/AppleInternal/Library/BuildRoots/4~CH-kugCSNxlzBMFB_ZM8YSYv_Du9IUDoW-iXb3k/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/string:1476: libc++ Hardening assertion !empty() failed: string::back(): string is empty\n"
+ "/AppleInternal/Library/BuildRoots/4~CH-kugCSNxlzBMFB_ZM8YSYv_Du9IUDoW-iXb3k/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/string:3362: libc++ Hardening assertion __first <= __last failed: string::erase(first, last) called with invalid range\n"
+ "/AppleInternal/Library/BuildRoots/4~CHnfugBQfFiUsKTOUfg69qHXhLEu9BfmOtFN7Ag/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/string:3362: libc++ Hardening assertion __first <= __last failed: string::erase(first, last) called with invalid range\n"
+ "DELETE FROM queried_states WHERE queried_state_name=?1 AND (queried_state_params = '' OR queried_state_params IS NULL OR queried_state_params=?2);"
+ "[State Store] Error preparing database queried_states-remove-with-params query; %s"
+ "[State Store] Error preparing database queried_states-remove-with-params query[null database]"
+ "[State Store] Failed to remove queried_state (name='%{public}s', params='%{public}s'); %s"
+ "[State Store] Failed to remove queried_state (name='%{public}s', params='%{public}s')[null database]"
+ "[StateCache] Invalidating cache entry for state: %s with params: %s"
+ "[TrialStateRelay] Extension token is null"
+ "[TrialStateRelay] Failed to consume extension: %i"
+ "[TrialStateRelay] No sandbox extensions present, attempting to retry"
+ "[TrialStateRelay] Sandbox extension token query returned error: %@"
+ "[TrialStateRelay] Successfully consumed sandbox token %@"
+ "[TrialStateRelay] Successfully obtained sandbox extensions on retry"
+ "[TrialStateRelay] Triggering namespace reload after obtaining extensions"
+ "[TrialStateResolver] Sandbox extensions became available, reloading Trial namespaces"
+ "_getSandboxExtensions"
+ "_value"
+ "initWithEffectiveBundlePath:delegate:onQueue:"
+ "removeModifyEvent"
- "[TrialStateRelay] Trial: Extension token is null"
- "[TrialStateRelay] Trial: Failed to consume extension: %i"
- "[TrialStateRelay] Trial: sandbox extension token query returned: %@"
- "[TrialStateRelay] TrialIdentifier: experimentIdentifiers nil. No active experiment"
- "bundleWithPath:"
- "clientWithIdentifier:"
- "initWithEffectiveBundle:delegate:onQueue:"
- "removeModifyEvents"

```
