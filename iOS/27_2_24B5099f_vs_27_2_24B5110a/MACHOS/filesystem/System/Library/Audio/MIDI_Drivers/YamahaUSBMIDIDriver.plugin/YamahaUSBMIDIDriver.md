## YamahaUSBMIDIDriver

> `/System/Library/Audio/MIDI Drivers/YamahaUSBMIDIDriver.plugin/YamahaUSBMIDIDriver`

### Sections with Same Size but Changed Content

- `__TEXT.__unwind_info`
- `__DATA_CONST.__cfstring`
- `__DATA.__data`

```diff

-333.202.1.0.0
-  __TEXT.__text: 0x1decc
+333.203.0.0.0
+  __TEXT.__text: 0x1e0c4
   __TEXT.__realtime: 0x4c4
   __TEXT.__auth_stubs: 0x760
-  __TEXT.__const: 0x290
-  __TEXT.__cstring: 0x839
-  __TEXT.__gcc_except_tab: 0xd9c
-  __TEXT.__oslogstring: 0x3c7e
+  __TEXT.__const: 0x2a0
+  __TEXT.__cstring: 0x8a2
+  __TEXT.__gcc_except_tab: 0xd98
+  __TEXT.__oslogstring: 0x3dde
   __TEXT.__unwind_info: 0xb88
-  __DATA_CONST.__const: 0xc48
+  __DATA_CONST.__const: 0xc60
   __DATA_CONST.__cfstring: 0x360
   __DATA_CONST.__auth_got: 0x3b8
   __DATA_CONST.__got: 0xc8

   - /usr/lib/libc++.1.dylib
   Functions: 547
   Symbols:   151
-  CStrings:  354
+  CStrings:  359
 
Functions:
~ sub_5f94 : 448 -> 604
~ sub_638c -> sub_6428 : 2084 -> 2232
~ sub_13594 -> sub_136c4 : 3344 -> 3544
CStrings:
+ "%25s:%-5d USBDevice::LoadDescriptor - Refusing string descriptor bLength %d into a %zu byte buffer"
+ "%25s:%-5d [!]  FATAL: Could not retrieve Group Terminal Descriptors for USB MIDI interface %d alternate setting %d (error 0x%x)"
+ "%25s:%-5d [!]  FATAL: Expected %u byte(s) of group terminal block descriptors but got %u (error 0x%x)"
+ "%25s:%-5d [!]  FATAL: Rejecting Group Terminal Block descriptor header for USB MIDI interface %d alternate setting %d: %s (headerLength %u, buffer capacity %u): %s"
+ "%25s:%-5d [+] USBDevice::LoadGroupTerminalDescriptors(interface: %d, altSettingNumber: %d, buf:%p, bufCapacity:%zu, len:%d)"
+ "%25s:%-5d [-] USBDevice::LoadGroupTerminalDescriptors() - Refusing to request %u byte(s) into a %zu byte buffer"
+ "incomplete descriptor header"
+ "wTotalLength is not a whole number of descriptors"
+ "wTotalLength out of range"
- "%25s:%-5d      Unexpected group terminal descriptor length: %u"
- "%25s:%-5d      Unexpected total descriptor length: %u"
- "%25s:%-5d [!]  FATAL: Could not retrieve Group Terminal Descriptors for USB MIDI interface %d alternate setting %d. Expected header length %u but got %u"
- "%25s:%-5d [+] USBDevice::LoadGroupTerminalDescriptors(interface: %d, altSettingNumber: %d, buf:%p, len:%d)"
```
