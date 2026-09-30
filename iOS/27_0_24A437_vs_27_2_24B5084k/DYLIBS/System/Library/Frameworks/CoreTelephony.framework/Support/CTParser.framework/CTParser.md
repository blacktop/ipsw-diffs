## CTParser

> `/System/Library/Frameworks/CoreTelephony.framework/Support/CTParser.framework/CTParser`

### Sections with Same Size but Changed Content

- `__TEXT.__cstring`

```diff

-13487.7.0.0.0
-  __TEXT.__text: 0x56a0
+13494.0.0.0.0
+  __TEXT.__text: 0x57a8
   __TEXT.__const: 0x515
-  __TEXT.__gcc_except_tab: 0x610
+  __TEXT.__gcc_except_tab: 0x5f8
   __TEXT.__cstring: 0x397
-  __TEXT.__oslogstring: 0x14e
-  __TEXT.__unwind_info: 0x558
+  __TEXT.__oslogstring: 0x166
+  __TEXT.__unwind_info: 0x560
   __TEXT.__auth_stubs: 0x0
   __DATA_CONST.__const: 0x18
   __DATA_CONST.__weak_got: 0x8

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libTelephonyUtilDynamic.dylib
   - /usr/lib/libc++.1.dylib
-  Functions: 225
-  Symbols:   448
-  CStrings:  34
+  Functions: 227
+  Symbols:   449
+  CStrings:  35
 
Symbols:
+ GCC_except_table32
+ GCC_except_table37
+ GCC_except_table50
+ GCC_except_table53
+ GCC_except_table60
+ __ZNK3xpc4dict15to_debug_stringEv
+ __os_log_debug_impl
- GCC_except_table25
- GCC_except_table35
- GCC_except_table41
- GCC_except_table49
- GCC_except_table51
- GCC_except_table57
Functions:
~ __ZN14CTParserClient15processResponseENSt3__110shared_ptrI19CTParserXPCResponseEE : 748 -> 780
+ __ZNK3xpc4dict15to_debug_stringEv
~ _OUTLINED_FUNCTION_1 : 20 -> 16
~ _OUTLINED_FUNCTION_2 : 12 -> 20
~ _OUTLINED_FUNCTION_3 : 16 -> 12
~ __ZN14CTParserClient15processResponseENSt3__110shared_ptrI19CTParserXPCResponseEE.cold.1 : 76 -> 124
~ __ZN14CTParserClient15processResponseENSt3__110shared_ptrI19CTParserXPCResponseEE.cold.2 : 104 -> 76
~ __ZN14CTParserClient15processResponseENSt3__110shared_ptrI19CTParserXPCResponseEE.cold.3 : 52 -> 104
+ __ZN14CTParserClient15processResponseENSt3__110shared_ptrI19CTParserXPCResponseEE.cold.4
CStrings:
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS27.2.Internal.sdk/usr/include/c++/v1/__vector/vector.h:1161: libc++ Hardening assertion __position != end() failed: vector::erase(iterator) called with a non-dereferenceable iterator\n"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS27.2.Internal.sdk/usr/include/c++/v1/__vector/vector.h:1171: libc++ Hardening assertion __first <= __last failed: vector::erase(first, last) called with invalid range\n"
+ "Received XPC object: %s"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS27.0.Internal.sdk/usr/include/c++/v1/__vector/vector.h:1161: libc++ Hardening assertion __position != end() failed: vector::erase(iterator) called with a non-dereferenceable iterator\n"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS27.0.Internal.sdk/usr/include/c++/v1/__vector/vector.h:1171: libc++ Hardening assertion __first <= __last failed: vector::erase(first, last) called with invalid range\n"
```
