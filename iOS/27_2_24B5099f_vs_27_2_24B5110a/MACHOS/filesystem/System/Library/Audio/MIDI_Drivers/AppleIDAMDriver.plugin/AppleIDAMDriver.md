## AppleIDAMDriver

> `/System/Library/Audio/MIDI Drivers/AppleIDAMDriver.plugin/AppleIDAMDriver`

### Sections with Same Size but Changed Content

- `__TEXT.__const`
- `__TEXT.__unwind_info`
- `__DATA_CONST.__cfstring`
- `__DATA.__data`

```diff

-333.202.1.0.0
-  __TEXT.__text: 0x1bfe8
+333.203.0.0.0
+  __TEXT.__text: 0x1c1e0
   __TEXT.__realtime: 0x4c4
   __TEXT.__auth_stubs: 0x780
   __TEXT.__const: 0x290
-  __TEXT.__gcc_except_tab: 0xc60
-  __TEXT.__oslogstring: 0x39c8
-  __TEXT.__cstring: 0x827
+  __TEXT.__gcc_except_tab: 0xc5c
+  __TEXT.__oslogstring: 0x3b28
+  __TEXT.__cstring: 0x890
   __TEXT.__unwind_info: 0xb80
-  __DATA_CONST.__const: 0xb60
+  __DATA_CONST.__const: 0xb78
   __DATA_CONST.__cfstring: 0x320
   __DATA_CONST.__auth_got: 0x3c8
   __DATA_CONST.__got: 0xc8

   - /usr/lib/libc++.1.dylib
   Functions: 538
   Symbols:   153
-  CStrings:  359
+  CStrings:  364
 
Functions:
~ sub_2438 : 448 -> 604
~ sub_2684 -> sub_2720 : 2084 -> 2232
~ sub_64a8 -> sub_65d8 : 3344 -> 3544
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
