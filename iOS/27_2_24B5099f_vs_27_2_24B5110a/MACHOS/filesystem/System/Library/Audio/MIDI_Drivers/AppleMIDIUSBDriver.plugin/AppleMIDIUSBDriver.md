## AppleMIDIUSBDriver

> `System/Library/Audio/MIDI Drivers/AppleMIDIUSBDriver.plugin/AppleMIDIUSBDriver`

### Sections with Same Size but Changed Content

- `__TEXT.__unwind_info`
- `__DATA_CONST.__cfstring`
- `__DATA.__data`

```diff

-333.202.1.0.0
-  __TEXT.__text: 0x1eb94
+333.203.0.0.0
+  __TEXT.__text: 0x1ed8c
   __TEXT.__realtime: 0x4c4
   __TEXT.__auth_stubs: 0x770
-  __TEXT.__gcc_except_tab: 0xdbc
-  __TEXT.__cstring: 0x8e6
-  __TEXT.__const: 0x293
-  __TEXT.__oslogstring: 0x43cb
+  __TEXT.__gcc_except_tab: 0xdb8
+  __TEXT.__cstring: 0x94f
+  __TEXT.__const: 0x29b
+  __TEXT.__oslogstring: 0x452b
   __TEXT.__unwind_info: 0xbd0
-  __DATA_CONST.__const: 0xc50
+  __DATA_CONST.__const: 0xc68
   __DATA_CONST.__cfstring: 0x3e0
   __DATA_CONST.__auth_got: 0x3c0
   __DATA_CONST.__got: 0xd0

   - /usr/lib/libc++.1.dylib
   Functions: 572
   Symbols:   153
-  CStrings:  390
+  CStrings:  395
 
Functions:
~ sub_4d58 : 448 -> 604
~ sub_5150 -> sub_51ec : 2084 -> 2232
~ sub_169ec -> sub_16b1c : 3344 -> 3544
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
