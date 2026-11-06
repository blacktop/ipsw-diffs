## AppleMIDIUSBDriver

> `/System/Library/Extensions/AppleMIDIUSBDriver.plugin/Contents/MacOS/AppleMIDIUSBDriver`

### Sections with Same Size but Changed Content

- `__DATA_CONST.__cfstring`
- `__DATA.__data`

```diff

-333.0.0.0.0
-  __TEXT.__text: 0x1dba8
+333.204.0.0.0
+  __TEXT.__text: 0x1e1e8
   __TEXT.__realtime: 0x4c4
-  __TEXT.__auth_stubs: 0x800
-  __TEXT.__gcc_except_tab: 0xd3c
-  __TEXT.__cstring: 0x99d
-  __TEXT.__const: 0x293
-  __TEXT.__oslogstring: 0x4314
-  __TEXT.__unwind_info: 0xba8
-  __DATA_CONST.__const: 0xca0
+  __TEXT.__auth_stubs: 0x820
+  __TEXT.__gcc_except_tab: 0xda4
+  __TEXT.__cstring: 0xa1a
+  __TEXT.__const: 0x29b
+  __TEXT.__oslogstring: 0x44cb
+  __TEXT.__unwind_info: 0xbd0
+  __DATA_CONST.__const: 0xcb8
   __DATA_CONST.__cfstring: 0x400
-  __DATA_CONST.__auth_got: 0x408
-  __DATA_CONST.__got: 0xd8
+  __DATA_CONST.__auth_got: 0x418
+  __DATA_CONST.__got: 0xe0
   __DATA.__data: 0xb0
   __DATA.__bss: 0xd0
   - /System/Library/Frameworks/CoreFoundation.framework/Versions/A/CoreFoundation

   - /System/Library/PrivateFrameworks/caulk.framework/Versions/A/caulk
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libc++.1.dylib
-  Functions: 557
-  Symbols:   163
-  CStrings:  397
+  Functions: 562
+  Symbols:   166
+  CStrings:  404
 
Symbols:
+ _CFStringGetTypeID
+ __ZNSt13runtime_errorC1EPKc
+ __ZNSt13runtime_errorD1Ev
CStrings:
+ "%25s:%-5d USBDevice::InitLangIDs - no valid language ID reported; using default 0x%04x"
+ "%25s:%-5d USBDevice::LoadDescriptor - Refusing string descriptor bLength %d into a %zu byte buffer"
+ "%25s:%-5d [!]  FATAL: Could not retrieve Group Terminal Descriptors for USB MIDI interface %d alternate setting %d (error 0x%x)"
+ "%25s:%-5d [!]  FATAL: Expected %u byte(s) of group terminal block descriptors but got %u (error 0x%x)"
+ "%25s:%-5d [!]  FATAL: Rejecting Group Terminal Block descriptor header for USB MIDI interface %d alternate setting %d: %s (headerLength %u, buffer capacity %u): %s"
+ "%25s:%-5d [+] USBDevice::LoadGroupTerminalDescriptors(interface: %d, altSettingNumber: %d, buf:%p, bufCapacity:%zu, len:%d)"
+ "%25s:%-5d [-] USBDevice::LoadGroupTerminalDescriptors() - Refusing to request %u byte(s) into a %zu byte buffer"
+ "Could not construct"
+ "incomplete descriptor header"
+ "wTotalLength is not a whole number of descriptors"
+ "wTotalLength out of range"
- "%25s:%-5d      Unexpected group terminal descriptor length: %u"
- "%25s:%-5d      Unexpected total descriptor length: %u"
- "%25s:%-5d [!]  FATAL: Could not retrieve Group Terminal Descriptors for USB MIDI interface %d alternate setting %d. Expected header length %u but got %u"
- "%25s:%-5d [+] USBDevice::LoadGroupTerminalDescriptors(interface: %d, altSettingNumber: %d, buf:%p, len:%d)"
```
