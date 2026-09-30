## RTBuddyCrashlogDecoder

> `/System/Library/PrivateFrameworks/RTBuddyCrashlogDecoder.framework/RTBuddyCrashlogDecoder`

```diff

-693.80.3.0.1
-  __TEXT.__text: 0x264c
-  __TEXT.__auth_stubs: 0x190
+693.100.47.0.0
+  __TEXT.__text: 0x2824
+  __TEXT.__auth_stubs: 0x1a0
   __TEXT.__const: 0x11
-  __TEXT.__cstring: 0x1893
-  __TEXT.__unwind_info: 0xf8
+  __TEXT.__cstring: 0x1af4
+  __TEXT.__unwind_info: 0x100
   __DATA_CONST.__got: 0x38
   __DATA_CONST.__const: 0x628
-  __AUTH_CONST.__auth_got: 0xc8
+  __AUTH_CONST.__auth_got: 0xd0
   __AUTH_CONST.__const: 0x260
-  __AUTH_CONST.__cfstring: 0x5e0
+  __AUTH_CONST.__cfstring: 0x600
   __DATA.__data: 0xb8
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libc++.1.dylib
-  UUID: B3ACDCD2-D139-3D63-AA40-6E6E0B07088F
-  Functions: 48
-  Symbols:   146
-  CStrings:  297
+  UUID: 62F7CA95-4F66-362F-B1A8-038DAE61AF7F
+  Functions: 50
+  Symbols:   151
+  CStrings:  305
 
Symbols:
+ __ZL16getExceptionName14CrashLogType_t
+ __ZL37multi_agent_crashlog_find_first_crashP26RTK_scrlg_section_writer_sPKhPmPy
+ __ZNSt3__132__internal_log_hardening_failureEPKc
CStrings:
+ "/AppleInternal/Library/BuildRoots/4~CH4KugBVYp3alghYrol5M31uhWqfg8MJ6N0fo2k/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/array:275: libc++ Hardening assertion __n < _Size failed: out-of-bounds access in std::array<T, N>\n"
+ "Invalid crash log"
+ "Multilog crash with invalid (short) log length. %u bytes. Minimum valid length is %lu \n"
+ "Multilog crash with invalid header signature: 0x%x, should be 0x%x\n"
+ "Multilog crash with unsupported log (major version: %u, should be %u)\n"
+ "No crashlog entry found in multi-crashlog header"
+ "agent_id"

```
