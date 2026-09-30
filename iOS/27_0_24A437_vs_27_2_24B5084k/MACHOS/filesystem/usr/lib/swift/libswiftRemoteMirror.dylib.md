## libswiftRemoteMirror.dylib

> `/usr/lib/swift/libswiftRemoteMirror.dylib`

### Sections with Same Size but Changed Content

- `__TEXT.__init_offsets`
- `__TEXT.__unwind_info`
- `__DATA_CONST.__const`
- `__AUTH_CONST.__const`

```diff

-6.4.0.31.5
-  __TEXT.__text: 0xd3fc8
+6.4.0.34.1
+  __TEXT.__text: 0xd3fa8
   __TEXT.__init_offsets: 0x4
-  __TEXT.__cstring: 0x7148
+  __TEXT.__cstring: 0x7122
   __TEXT.__const: 0x7f0
   __TEXT.__unwind_info: 0x1d58
   __TEXT.__auth_stubs: 0x490

   - /usr/lib/libc++.1.dylib
   Functions: 2092
   Symbols:   2591
-  CStrings:  1644
+  CStrings:  1643
 
Functions:
~ __ZN5swift10reflection26ExistentialTypeInfoBuilder5buildEPNS_6remote16TypeInfoProviderE : 1252 -> 1236
~ __ZN5swift10reflection26ExistentialTypeInfoBuilder16examineProtocolsEv : 676 -> 684
~ __ZN5swift10reflection26ExistentialTypeInfoBuilder13buildMetatypeEPNS_6remote16TypeInfoProviderE : 640 -> 616
CStrings:
- "@objc existential with witness tables"
```
