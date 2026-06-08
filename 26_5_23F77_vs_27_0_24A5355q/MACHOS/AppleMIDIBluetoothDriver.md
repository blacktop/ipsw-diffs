## AppleMIDIBluetoothDriver

> `/System/Library/Audio/MIDI Drivers/AppleMIDIBluetoothDriver.plugin/AppleMIDIBluetoothDriver`

```diff

-324.501.0.6.0
-  __TEXT.__text: 0xecdc
-  __TEXT.__auth_stubs: 0x7b0
+328.0.0.0.0
+  __TEXT.__text: 0xd740
+  __TEXT.__realtime: 0x348
+  __TEXT.__auth_stubs: 0x6c0
   __TEXT.__objc_stubs: 0x11c0
-  __TEXT.__objc_methlist: 0x954
-  __TEXT.__cstring: 0x4f4
-  __TEXT.__gcc_except_tab: 0x498
-  __TEXT.__const: 0xf8
+  __TEXT.__objc_methlist: 0x96c
+  __TEXT.__cstring: 0x76f
+  __TEXT.__const: 0x110
+  __TEXT.__gcc_except_tab: 0x430
   __TEXT.__oslogstring: 0x2211
-  __TEXT.__objc_methname: 0x1810
+  __TEXT.__objc_methname: 0x187a
   __TEXT.__objc_classname: 0xb4
-  __TEXT.__objc_methtype: 0xae5
-  __TEXT.__unwind_info: 0x5a8
-  __DATA_CONST.__auth_got: 0x3e8
-  __DATA_CONST.__got: 0x148
-  __DATA_CONST.__const: 0x520
+  __TEXT.__objc_methtype: 0xb30
+  __TEXT.__unwind_info: 0x540
+  __DATA_CONST.__const: 0x4c8
   __DATA_CONST.__cfstring: 0x400
   __DATA_CONST.__objc_classlist: 0x28
   __DATA_CONST.__objc_protolist: 0x20
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_superrefs: 0x28
   __DATA_CONST.__objc_intobj: 0x18
-  __DATA.__objc_const: 0xd98
-  __DATA.__objc_selrefs: 0x6c8
+  __DATA_CONST.__auth_got: 0x370
+  __DATA_CONST.__got: 0x130
+  __DATA.__objc_const: 0xda8
+  __DATA.__objc_selrefs: 0x6d8
   __DATA.__objc_ivar: 0xcc
   __DATA.__objc_data: 0x190
   __DATA.__data: 0x248
-  __DATA.__bss: 0xe0
+  __DATA.__bss: 0x70
   - /System/Library/Frameworks/CoreBluetooth.framework/CoreBluetooth
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/CoreMIDI.framework/CoreMIDI

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libc++.1.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 744DF629-474C-3380-8AE6-627EFED0E601
-  Functions: 354
-  Symbols:   177
-  CStrings:  609
+  UUID: 343D1DFC-D793-33CE-8A76-24D6D62F2FD3
+  Functions: 329
+  Symbols:   158
+  CStrings:  611
 
Symbols:
+ _CAAssertRtn
+ __ZN5caulk14cf_preferences15interpret_int64EPKv
+ __ZN5caulk14cf_preferences7monitor12_add_handlerEPK10__CFStringS4_ONSt3__18functionIFbPKvEEE
+ __ZN5caulk14cf_preferences7monitor8instanceEv
+ __ZNSt3__112system_errorC1EiRKNS_14error_categoryE
+ __ZNSt3__112system_errorD1Ev
+ __ZNSt3__115system_categoryEv
+ __ZNSt3__132__internal_log_hardening_failureEPKc
- _CFBooleanGetTypeID
- _CFBooleanGetValue
- _CFGetTypeID
- _CFNumberGetTypeID
- _CFNumberGetValue
- _CFPreferencesCopyAppValue
- _CFPreferencesSynchronize
- _CFSetAddValue
- _CFSetApplyFunction
- _CFSetCreateMutable
- _CFStringGetCString
- _CFStringGetTypeID
- __ZNSt3__15mutex4lockEv
- __ZNSt3__15mutex6unlockEv
- __ZNSt3__15mutexD1Ev
- __ZNSt9exceptionD2Ev
- __ZTVN10__cxxabiv121__vmi_class_type_infoE
- ___cxa_guard_abort
- __dispatch_source_type_signal
- _dispatch_get_global_queue
- _dispatch_resume
- _dispatch_source_create
- _dispatch_source_set_event_handler
- _kCFPreferencesCurrentHost
- _kCFPreferencesCurrentUser
- _kCFTypeSetCallBacks
- _sscanf
CStrings:
+ "/AppleInternal/Library/BuildRoots/4~CQCfugB4hqQzUUPUbWkTvZ93lzJRAfAeo1l9qwc/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS27.0.Internal.sdk/usr/local/include/c++/previous/list:1420: libc++ Hardening assertion __p != end() failed: list::erase(iterator) called with a non-dereferenceable iterator\n"
+ "/AppleInternal/Library/BuildRoots/4~CQCfugB4hqQzUUPUbWkTvZ93lzJRAfAeo1l9qwc/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS27.0.Internal.sdk/usr/local/include/c++/previous/span:525: libc++ Hardening assertion __idx < size() failed: span<T>::operator[](index): index out of range\n"
+ "peripheral:didCompleteChannelSoundingSession:"
+ "peripheral:didReceiveChannelSoundingProcedureResults:error:"
+ "v40@0:8@\"CBPeripheral\"16@\"CBChannelSoundingProcedureResults\"24@\"NSError\"32"
- "%d"
- "CAException"
- "~MIDIPacketEmitter"

```
