## AppleMIDIBluetoothDriver

> `/System/Library/Audio/MIDI Drivers/AppleMIDIBluetoothDriver.plugin/AppleMIDIBluetoothDriver`

```diff

-324.300.0.0.0
-  __TEXT.__text: 0xf4c0
-  __TEXT.__auth_stubs: 0x7b0
+324.501.0.3.0
+  __TEXT.__text: 0xebf4
+  __TEXT.__auth_stubs: 0x7c0
   __TEXT.__objc_stubs: 0x11c0
   __TEXT.__objc_methlist: 0x954
-  __TEXT.__cstring: 0x4f4
-  __TEXT.__gcc_except_tab: 0x4c0
+  __TEXT.__cstring: 0x8ac
+  __TEXT.__gcc_except_tab: 0x480
   __TEXT.__const: 0xf8
   __TEXT.__oslogstring: 0x2211
   __TEXT.__objc_methname: 0x1810
   __TEXT.__objc_classname: 0xb4
   __TEXT.__objc_methtype: 0xae5
-  __TEXT.__unwind_info: 0x5b8
-  __DATA_CONST.__auth_got: 0x3e8
+  __TEXT.__unwind_info: 0x5a8
+  __DATA_CONST.__auth_got: 0x3f0
   __DATA_CONST.__got: 0x148
-  __DATA_CONST.__const: 0x500
+  __DATA_CONST.__const: 0x520
   __DATA_CONST.__cfstring: 0x400
   __DATA_CONST.__objc_classlist: 0x28
   __DATA_CONST.__objc_protolist: 0x20

   __DATA.__objc_selrefs: 0x6c8
   __DATA.__objc_ivar: 0xcc
   __DATA.__objc_data: 0x190
-  __DATA.__data: 0x238
+  __DATA.__data: 0x248
   __DATA.__bss: 0xe0
   - /System/Library/Frameworks/CoreBluetooth.framework/CoreBluetooth
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libc++.1.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 10C0B7E3-871F-3BD8-A6E7-DFCF64547EC1
-  Functions: 344
-  Symbols:   177
-  CStrings:  609
+  UUID: 61894740-B3D1-348D-BFD1-8B00D11D3C5B
+  Functions: 356
+  Symbols:   178
+  CStrings:  612
 
Symbols:
+ __ZNSt3__132__internal_log_hardening_failureEPKc
CStrings:
+ "/AppleInternal/Library/BuildRoots/4~CHoJugCzhrKAFuXkd3a9noWrgfH5lo9T3jXIPsg/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/__vector/vector.h:433: libc++ Hardening assertion !empty() failed: back() called on an empty vector\n"
+ "/AppleInternal/Library/BuildRoots/4~CHoJugCzhrKAFuXkd3a9noWrgfH5lo9T3jXIPsg/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/list:1420: libc++ Hardening assertion __p != end() failed: list::erase(iterator) called with a non-dereferenceable iterator\n"
+ "/AppleInternal/Library/BuildRoots/4~CHoJugCzhrKAFuXkd3a9noWrgfH5lo9T3jXIPsg/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/span:525: libc++ Hardening assertion __idx < size() failed: span<T>::operator[](index): index out of range\n"

```
