## LocationSupport

> `/System/Library/PrivateFrameworks/LocationSupport.framework/LocationSupport`

```diff

-3072.0.40.0.1
+3072.0.42.0.0
   __TEXT.__text: 0x241a8
   __TEXT.__auth_stubs: 0xe40
   __TEXT.__objc_methlist: 0x174c
-  __TEXT.__const: 0x2e5
+  __TEXT.__const: 0x2dd
   __TEXT.__cstring: 0x2047
   __TEXT.__gcc_except_tab: 0x16d4
   __TEXT.__oslogstring: 0x5aeb

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libc++.1.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: D36BCBBD-9439-3651-9DAE-5F45163F10C0
+  UUID: 3C8004CA-A7E0-33C1-A786-C1ACA1747CC3
   Functions: 730
   Symbols:   469
   CStrings:  1197
CStrings:
+ "/AppleInternal/Library/BuildRoots/4~CJIqugClfI06gqfL8cT9eg8YQxQd7BXeh0K9Evc/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/__hash_table:1892: libc++ Hardening assertion __p != end() failed: unordered container::erase(iterator) called with a non-dereferenceable iterator\n"
+ "/AppleInternal/Library/BuildRoots/4~CJIqugClfI06gqfL8cT9eg8YQxQd7BXeh0K9Evc/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/__vector/vector.h:1162: libc++ Hardening assertion __position != end() failed: vector::erase(iterator) called with a non-dereferenceable iterator\n"
+ "/AppleInternal/Library/BuildRoots/4~CJIqugClfI06gqfL8cT9eg8YQxQd7BXeh0K9Evc/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/string_view:341: libc++ Hardening assertion (__end - __begin) >= 0 failed: std::string_view::string_view(iterator, sentinel) received invalid range\n"
+ "/Library/Caches/com.apple.xbs/78B5C499-61E1-4387-99FA-8BCCE417D80C/TemporaryDirectory.S7VCgV/Sources/CoreLocationFramework/Shared/IPC/CLConnection.mm"
+ "/Library/Caches/com.apple.xbs/78B5C499-61E1-4387-99FA-8BCCE417D80C/TemporaryDirectory.S7VCgV/Sources/CoreLocationFramework/Shared/IPC/CLConnectionClient.mm"
+ "/Library/Caches/com.apple.xbs/78B5C499-61E1-4387-99FA-8BCCE417D80C/TemporaryDirectory.S7VCgV/Sources/CoreLocationFramework/Shared/IPC/CLConnectionServer.mm"
+ "/Library/Caches/com.apple.xbs/78B5C499-61E1-4387-99FA-8BCCE417D80C/TemporaryDirectory.S7VCgV/Sources/CoreLocationFramework/Shared/Intersilo/CLDispatchSilo.m"
+ "/Library/Caches/com.apple.xbs/78B5C499-61E1-4387-99FA-8BCCE417D80C/TemporaryDirectory.S7VCgV/Sources/CoreLocationFramework/Shared/Intersilo/CLIntersiloInterface.mm"
+ "/Library/Caches/com.apple.xbs/78B5C499-61E1-4387-99FA-8BCCE417D80C/TemporaryDirectory.S7VCgV/Sources/CoreLocationFramework/Shared/Intersilo/CLIntersiloProxy.mm"
+ "/Library/Caches/com.apple.xbs/78B5C499-61E1-4387-99FA-8BCCE417D80C/TemporaryDirectory.S7VCgV/Sources/CoreLocationFramework/Shared/Intersilo/CLIntersiloService.m"
+ "/Library/Caches/com.apple.xbs/78B5C499-61E1-4387-99FA-8BCCE417D80C/TemporaryDirectory.S7VCgV/Sources/CoreLocationFramework/Shared/Intersilo/CLRunLoopSilo.m"
+ "/Library/Caches/com.apple.xbs/78B5C499-61E1-4387-99FA-8BCCE417D80C/TemporaryDirectory.S7VCgV/Sources/CoreLocationFramework/Shared/Intersilo/CLServiceVendor.mm"
+ "/Library/Caches/com.apple.xbs/78B5C499-61E1-4387-99FA-8BCCE417D80C/TemporaryDirectory.S7VCgV/Sources/CoreLocationFramework/Shared/Intersilo/CLSilo.m"
+ "/Library/Caches/com.apple.xbs/78B5C499-61E1-4387-99FA-8BCCE417D80C/TemporaryDirectory.S7VCgV/Sources/CoreLocationFramework/Shared/Intersilo/CLTimer.m"
+ "/Library/Caches/com.apple.xbs/78B5C499-61E1-4387-99FA-8BCCE417D80C/TemporaryDirectory.S7VCgV/Sources/CoreLocationFramework/Shared/Utilities/CLAutoCohortUtilities.mm"
- "/AppleInternal/Library/BuildRoots/4~CILXugDx32nSryXDAg0oKhE7cNZiTnzY8Tz5gec/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/__hash_table:1892: libc++ Hardening assertion __p != end() failed: unordered container::erase(iterator) called with a non-dereferenceable iterator\n"
- "/AppleInternal/Library/BuildRoots/4~CILXugDx32nSryXDAg0oKhE7cNZiTnzY8Tz5gec/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/__vector/vector.h:1162: libc++ Hardening assertion __position != end() failed: vector::erase(iterator) called with a non-dereferenceable iterator\n"
- "/AppleInternal/Library/BuildRoots/4~CILXugDx32nSryXDAg0oKhE7cNZiTnzY8Tz5gec/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/string_view:341: libc++ Hardening assertion (__end - __begin) >= 0 failed: std::string_view::string_view(iterator, sentinel) received invalid range\n"
- "/Library/Caches/com.apple.xbs/981DCE78-4EF2-43A1-B581-257023D8E82E/TemporaryDirectory.86TLii/Sources/CoreLocationFramework/Shared/IPC/CLConnection.mm"
- "/Library/Caches/com.apple.xbs/981DCE78-4EF2-43A1-B581-257023D8E82E/TemporaryDirectory.86TLii/Sources/CoreLocationFramework/Shared/IPC/CLConnectionClient.mm"
- "/Library/Caches/com.apple.xbs/981DCE78-4EF2-43A1-B581-257023D8E82E/TemporaryDirectory.86TLii/Sources/CoreLocationFramework/Shared/IPC/CLConnectionServer.mm"
- "/Library/Caches/com.apple.xbs/981DCE78-4EF2-43A1-B581-257023D8E82E/TemporaryDirectory.86TLii/Sources/CoreLocationFramework/Shared/Intersilo/CLDispatchSilo.m"
- "/Library/Caches/com.apple.xbs/981DCE78-4EF2-43A1-B581-257023D8E82E/TemporaryDirectory.86TLii/Sources/CoreLocationFramework/Shared/Intersilo/CLIntersiloInterface.mm"
- "/Library/Caches/com.apple.xbs/981DCE78-4EF2-43A1-B581-257023D8E82E/TemporaryDirectory.86TLii/Sources/CoreLocationFramework/Shared/Intersilo/CLIntersiloProxy.mm"
- "/Library/Caches/com.apple.xbs/981DCE78-4EF2-43A1-B581-257023D8E82E/TemporaryDirectory.86TLii/Sources/CoreLocationFramework/Shared/Intersilo/CLIntersiloService.m"
- "/Library/Caches/com.apple.xbs/981DCE78-4EF2-43A1-B581-257023D8E82E/TemporaryDirectory.86TLii/Sources/CoreLocationFramework/Shared/Intersilo/CLRunLoopSilo.m"
- "/Library/Caches/com.apple.xbs/981DCE78-4EF2-43A1-B581-257023D8E82E/TemporaryDirectory.86TLii/Sources/CoreLocationFramework/Shared/Intersilo/CLServiceVendor.mm"
- "/Library/Caches/com.apple.xbs/981DCE78-4EF2-43A1-B581-257023D8E82E/TemporaryDirectory.86TLii/Sources/CoreLocationFramework/Shared/Intersilo/CLSilo.m"
- "/Library/Caches/com.apple.xbs/981DCE78-4EF2-43A1-B581-257023D8E82E/TemporaryDirectory.86TLii/Sources/CoreLocationFramework/Shared/Intersilo/CLTimer.m"
- "/Library/Caches/com.apple.xbs/981DCE78-4EF2-43A1-B581-257023D8E82E/TemporaryDirectory.86TLii/Sources/CoreLocationFramework/Shared/Utilities/CLAutoCohortUtilities.mm"

```
