## CoreMIDI

> `/System/Library/Frameworks/CoreMIDI.framework/CoreMIDI`

```diff

-324.0.0.0.0
-  __TEXT.__text: 0xa5c38
+324.300.0.0.0
+  __TEXT.__text: 0xa5d64
   __TEXT.__auth_stubs: 0x1d50
   __TEXT.__objc_methlist: 0x15a0
   __TEXT.__const: 0x9b4
   __TEXT.__dlopen_cstrs: 0x4e
-  __TEXT.__gcc_except_tab: 0xde20
+  __TEXT.__gcc_except_tab: 0xde44
   __TEXT.__cstring: 0x44f5
-  __TEXT.__oslogstring: 0x2b71
-  __TEXT.__unwind_info: 0x3eb0
+  __TEXT.__oslogstring: 0x2bb6
+  __TEXT.__unwind_info: 0x3eb8
   __TEXT.__objc_classname: 0x1f4
   __TEXT.__objc_methname: 0x2dd9
   __TEXT.__objc_methtype: 0x112a

   - /usr/lib/libbsm.0.dylib
   - /usr/lib/libc++.1.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 2491246B-A50D-315A-8572-C818AEFEDB89
+  UUID: 1E95819A-036A-3495-855C-12A264D89921
   Functions: 2631
-  Symbols:   7866
-  CStrings:  1901
+  Symbols:   7867
+  CStrings:  1902
 
Symbols:
+ GCC_except_table1640
+ ___block_descriptor_tmp.3047
+ ___block_descriptor_tmp.3166
+ ___block_descriptor_tmp.3877
- ___block_descriptor_tmp.3046
- ___block_descriptor_tmp.3165
- ___block_descriptor_tmp.3876
Functions:
~ __ZN14MIDIProcessXPC8InitOnceEv : 152 -> 164
~ __ZN14MIDIProcessXPC10InitializeEv : 416 -> 432
~ __ZNSt3__110__function6__funcIZN14MIDIProcessXPCC1EvE3$_0NS_9allocatorIS3_EEFvRN4swix12ipc_endpointERKN10applesauce3xpc6objectEEEclES8_SD_ : 40 -> 312
~ __ZN14MIDIProcessXPCC1Ev : 1572 -> 1568
~ __ZN11MIDIProcess14deleteInThreadEv : 112 -> 116
CStrings:
+ "%25s:%-5d MIDIProcess -> Connection was invalidated with error \"%s\"."

```
