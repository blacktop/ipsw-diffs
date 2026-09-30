## LocationSupport

> `/System/Library/PrivateFrameworks/LocationSupport.framework/LocationSupport`

```diff

-3068.0.15.0.0
-  __TEXT.__text: 0x23adc
-  __TEXT.__auth_stubs: 0xe70
+3072.0.40.0.1
+  __TEXT.__text: 0x241a8
+  __TEXT.__auth_stubs: 0xe40
   __TEXT.__objc_methlist: 0x174c
-  __TEXT.__const: 0x2dd
-  __TEXT.__cstring: 0x192d
-  __TEXT.__gcc_except_tab: 0x16b0
+  __TEXT.__const: 0x2e5
+  __TEXT.__cstring: 0x2047
+  __TEXT.__gcc_except_tab: 0x16d4
   __TEXT.__oslogstring: 0x5aeb
-  __TEXT.__unwind_info: 0xc68
+  __TEXT.__unwind_info: 0xc90
   __TEXT.__objc_classname: 0x412
   __TEXT.__objc_methname: 0x2847
   __TEXT.__objc_methtype: 0x858

   __DATA_CONST.__objc_protorefs: 0x28
   __DATA_CONST.__objc_superrefs: 0xd0
   __DATA_CONST.__objc_arraydata: 0x8
-  __AUTH_CONST.__auth_got: 0x750
+  __AUTH_CONST.__auth_got: 0x738
   __AUTH_CONST.__const: 0x950
   __AUTH_CONST.__cfstring: 0x500
   __AUTH_CONST.__objc_const: 0x2b08

   __AUTH_CONST.__objc_arrayobj: 0x18
   __AUTH.__objc_data: 0x410
   __AUTH.__data: 0x8
-  __DATA.__objc_ivar: 0x11c
+  __DATA.__objc_ivar: 0x128
   __DATA.__data: 0x510
   __DATA.__bss: 0x28
   __DATA.__common: 0x8
-  __DATA_DIRTY.__objc_ivar: 0x34
+  __DATA_DIRTY.__objc_ivar: 0x28
   __DATA_DIRTY.__objc_data: 0x690
   __DATA_DIRTY.__data: 0x30
   __DATA_DIRTY.__bss: 0x148

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libc++.1.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: A9814D4D-662A-3543-9214-AB6E09411B36
+  UUID: D36BCBBD-9439-3651-9DAE-5F45163F10C0
   Functions: 730
-  Symbols:   472
-  CStrings:  1194
+  Symbols:   469
+  CStrings:  1197
 
Symbols:
+ __ZNSt3__132__internal_log_hardening_failureEPKc
+ _bzero
+ _objc_retain_x25
- _objc_claimAutoreleasedReturnValue
- _objc_release_x28
- _objc_retainAutoreleaseReturnValue
- _objc_retain_x1
- _objc_retain_x3
- _objc_retain_x4
CStrings:
+ "/AppleInternal/Library/BuildRoots/4~CILXugDx32nSryXDAg0oKhE7cNZiTnzY8Tz5gec/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/__hash_table:1892: libc++ Hardening assertion __p != end() failed: unordered container::erase(iterator) called with a non-dereferenceable iterator\n"
+ "/AppleInternal/Library/BuildRoots/4~CILXugDx32nSryXDAg0oKhE7cNZiTnzY8Tz5gec/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/__vector/vector.h:1162: libc++ Hardening assertion __position != end() failed: vector::erase(iterator) called with a non-dereferenceable iterator\n"
+ "/AppleInternal/Library/BuildRoots/4~CILXugDx32nSryXDAg0oKhE7cNZiTnzY8Tz5gec/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/string_view:341: libc++ Hardening assertion (__end - __begin) >= 0 failed: std::string_view::string_view(iterator, sentinel) received invalid range\n"
+ "/Library/Caches/com.apple.xbs/981DCE78-4EF2-43A1-B581-257023D8E82E/TemporaryDirectory.86TLii/Sources/CoreLocationFramework/Shared/IPC/CLConnection.mm"
+ "/Library/Caches/com.apple.xbs/981DCE78-4EF2-43A1-B581-257023D8E82E/TemporaryDirectory.86TLii/Sources/CoreLocationFramework/Shared/IPC/CLConnectionClient.mm"
+ "/Library/Caches/com.apple.xbs/981DCE78-4EF2-43A1-B581-257023D8E82E/TemporaryDirectory.86TLii/Sources/CoreLocationFramework/Shared/IPC/CLConnectionServer.mm"
+ "/Library/Caches/com.apple.xbs/981DCE78-4EF2-43A1-B581-257023D8E82E/TemporaryDirectory.86TLii/Sources/CoreLocationFramework/Shared/Intersilo/CLDispatchSilo.m"
+ "/Library/Caches/com.apple.xbs/981DCE78-4EF2-43A1-B581-257023D8E82E/TemporaryDirectory.86TLii/Sources/CoreLocationFramework/Shared/Intersilo/CLIntersiloInterface.mm"
+ "/Library/Caches/com.apple.xbs/981DCE78-4EF2-43A1-B581-257023D8E82E/TemporaryDirectory.86TLii/Sources/CoreLocationFramework/Shared/Intersilo/CLIntersiloProxy.mm"
+ "/Library/Caches/com.apple.xbs/981DCE78-4EF2-43A1-B581-257023D8E82E/TemporaryDirectory.86TLii/Sources/CoreLocationFramework/Shared/Intersilo/CLIntersiloService.m"
+ "/Library/Caches/com.apple.xbs/981DCE78-4EF2-43A1-B581-257023D8E82E/TemporaryDirectory.86TLii/Sources/CoreLocationFramework/Shared/Intersilo/CLRunLoopSilo.m"
+ "/Library/Caches/com.apple.xbs/981DCE78-4EF2-43A1-B581-257023D8E82E/TemporaryDirectory.86TLii/Sources/CoreLocationFramework/Shared/Intersilo/CLServiceVendor.mm"
+ "/Library/Caches/com.apple.xbs/981DCE78-4EF2-43A1-B581-257023D8E82E/TemporaryDirectory.86TLii/Sources/CoreLocationFramework/Shared/Intersilo/CLSilo.m"
+ "/Library/Caches/com.apple.xbs/981DCE78-4EF2-43A1-B581-257023D8E82E/TemporaryDirectory.86TLii/Sources/CoreLocationFramework/Shared/Intersilo/CLTimer.m"
+ "/Library/Caches/com.apple.xbs/981DCE78-4EF2-43A1-B581-257023D8E82E/TemporaryDirectory.86TLii/Sources/CoreLocationFramework/Shared/Utilities/CLAutoCohortUtilities.mm"
- "/Library/Caches/com.apple.xbs/Sources/CoreLocationFramework/Shared/IPC/CLConnection.mm"
- "/Library/Caches/com.apple.xbs/Sources/CoreLocationFramework/Shared/IPC/CLConnectionClient.mm"
- "/Library/Caches/com.apple.xbs/Sources/CoreLocationFramework/Shared/IPC/CLConnectionServer.mm"
- "/Library/Caches/com.apple.xbs/Sources/CoreLocationFramework/Shared/Intersilo/CLDispatchSilo.m"
- "/Library/Caches/com.apple.xbs/Sources/CoreLocationFramework/Shared/Intersilo/CLIntersiloInterface.mm"
- "/Library/Caches/com.apple.xbs/Sources/CoreLocationFramework/Shared/Intersilo/CLIntersiloProxy.mm"
- "/Library/Caches/com.apple.xbs/Sources/CoreLocationFramework/Shared/Intersilo/CLIntersiloService.m"
- "/Library/Caches/com.apple.xbs/Sources/CoreLocationFramework/Shared/Intersilo/CLRunLoopSilo.m"
- "/Library/Caches/com.apple.xbs/Sources/CoreLocationFramework/Shared/Intersilo/CLServiceVendor.mm"
- "/Library/Caches/com.apple.xbs/Sources/CoreLocationFramework/Shared/Intersilo/CLSilo.m"
- "/Library/Caches/com.apple.xbs/Sources/CoreLocationFramework/Shared/Intersilo/CLTimer.m"
- "/Library/Caches/com.apple.xbs/Sources/CoreLocationFramework/Shared/Utilities/CLAutoCohortUtilities.mm"

```
