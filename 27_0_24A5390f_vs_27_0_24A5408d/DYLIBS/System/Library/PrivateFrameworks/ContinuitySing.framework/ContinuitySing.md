## ContinuitySing

> `/System/Library/PrivateFrameworks/ContinuitySing.framework/ContinuitySing`

### Sections with Same Size but Changed Content

- `__TEXT.__objc_methlist`
- `__TEXT.__swift5_typeref`
- `__TEXT.__constg_swiftt`
- `__TEXT.__swift5_proto`
- `__TEXT.__swift_as_entry`
- `__TEXT.__swift_as_ret`
- `__TEXT.__swift_as_cont`
- `__TEXT.__unwind_info`
- `__TEXT.__eh_frame`
- `__DATA_CONST.__const`
- `__DATA_CONST.__objc_classlist`
- `__DATA_CONST.__objc_catlist`
- `__DATA_CONST.__objc_protolist`
- `__DATA_CONST.__objc_selrefs`
- `__DATA_CONST.__objc_protorefs`
- `__DATA_CONST.__objc_superrefs`
- `__DATA_CONST.__objc_arraydata`
- `__DATA_CONST.__got`
- `__AUTH_CONST.__const`
- `__AUTH_CONST.__objc_const`
- `__AUTH_CONST.__objc_intobj`
- `__AUTH_CONST.__objc_arrayobj`
- `__AUTH_CONST.__objc_doubleobj`
- `__AUTH.__objc_data`
- `__AUTH.__data`
- `__DATA.__data`

```diff

-761.0.0.0.3
-  __TEXT.__text: 0x5dc58
+764.22.5.122.2
+  __TEXT.__text: 0x5de10
   __TEXT.__objc_methlist: 0x3694
-  __TEXT.__const: 0xfa4
-  __TEXT.__gcc_except_tab: 0xb94
-  __TEXT.__cstring: 0x6169
-  __TEXT.__oslogstring: 0x3329
+  __TEXT.__const: 0xfb4
+  __TEXT.__gcc_except_tab: 0xb98
+  __TEXT.__cstring: 0x61b9
+  __TEXT.__oslogstring: 0x3389
   __TEXT.__ustring: 0x2a
   __TEXT.__swift5_typeref: 0x9f6
   __TEXT.__swift5_fieldmd: 0x378

   __DATA_CONST.__objc_arraydata: 0x20
   __DATA_CONST.__got: 0x9d8
   __AUTH_CONST.__const: 0x1400
-  __AUTH_CONST.__cfstring: 0x2ee0
+  __AUTH_CONST.__cfstring: 0x2f00
   __AUTH_CONST.__objc_const: 0x7320
   __AUTH_CONST.__objc_intobj: 0xa8
   __AUTH_CONST.__objc_arrayobj: 0x18

   - /usr/lib/swift/libswiftsimd.dylib
   Functions: 1915
   Symbols:   4138
-  CStrings:  943
+  CStrings:  946
 
Functions:
~ -[CSRemoteRequestClient dealloc] : 256 -> 296
~ -[CSRemoteRequestClient _registerForReactions] : 236 -> 332
~ ___74-[CSShieldManager _attemptMicrophoneConnectionOnRoute:isRetry:completion:]_block_invoke : 692 -> 716
~ ___49-[CSShieldViewController _activateEnableMicTimer]_block_invoke : 108 -> 160
~ -[CSPairingDevice preferredDeviceIdentifier] : 172 -> 400
CStrings:
+ "%s: preferredDeviceIdentifier %@ (sessionPairing:%@ peerVerified:%@ ids:%@ mediaRoute:%@)"
+ "%s: requested mic with result %@, error: %@, retry: %@"
+ "-[CSPairingDevice preferredDeviceIdentifier]"
+ "Enable microphone request timed out"
- "%s: requested mic with result %@, error: %@%@"
```
