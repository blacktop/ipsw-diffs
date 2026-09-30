## sharingd

> `/usr/libexec/sharingd`

### Sections with Same Size but Changed Content

- `__TEXT.__objc_methlist`
- `__TEXT.__const`
- `__TEXT.__gcc_except_tab`
- `__TEXT.__swift5_typeref`
- `__TEXT.__constg_swiftt`
- `__TEXT.__swift5_proto`
- `__TEXT.__swift_as_entry`
- `__TEXT.__swift5_capture`
- `__TEXT.__swift_as_ret`
- `__TEXT.__swift5_mpenum`
- `__DATA_CONST.__const`
- `__DATA_CONST.__cfstring`
- `__DATA_CONST.__objc_intobj`
- `__DATA_CONST.__got`
- `__DATA_CONST.__auth_ptr`
- `__DATA.__objc_const`
- `__DATA.__objc_selrefs`
- `__DATA.__objc_data`
- `__DATA.__data`

```diff

-2131.20.65.2.1
-  __TEXT.__text: 0x67b928
+2131.20.71.0.0
+  __TEXT.__text: 0x67ba80
   __TEXT.__auth_stubs: 0xb180
   __TEXT.__objc_stubs: 0x378e0
   __TEXT.__objc_methlist: 0x1e694

   __TEXT.__objc_methtype: 0xbcc2
   __TEXT.__const: 0x160a8
   __TEXT.__gcc_except_tab: 0x68cc
-  __TEXT.__oslogstring: 0x3d653
+  __TEXT.__oslogstring: 0x3d6c3
   __TEXT.__ustring: 0x94
   __TEXT.__dlopen_cstrs: 0x438
   __TEXT.__swift5_typeref: 0x816a

   __TEXT.__swift5_proto: 0xce0
   __TEXT.__swift5_types: 0x5fc
   __TEXT.__swift_as_entry: 0xe60
-  __TEXT.__swift_as_cont: 0x222c
+  __TEXT.__swift_as_cont: 0x2230
   __TEXT.__swift5_capture: 0x52a4
   __TEXT.__swift_as_ret: 0xf78
   __TEXT.__swift5_mpenum: 0x24
-  __TEXT.__unwind_info: 0x19c60
-  __TEXT.__eh_frame: 0x2590c
+  __TEXT.__unwind_info: 0x19c68
+  __TEXT.__eh_frame: 0x25934
   __DATA_CONST.__const: 0x1ce28
   __DATA_CONST.__cfstring: 0x198c0
   __DATA_CONST.__objc_classlist: 0xe20

   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  Functions: 26462
+  Functions: 26464
   Symbols:   5076
-  CStrings:  27634
+  CStrings:  27635
 
CStrings:
+ "Became the console user, re-evaluating AirDrop receive"
+ "No longer the console user, stopping AirDrop receive"
+ "Not the console user session, deferring AirDrop receive start"
+ "updateServerState canRun(appService=%{bool}d, bonjour=%{bool}d, nearField=%{bool}d) inputs(currentConsoleUser=%{bool}d, screenStateSupportsAirDrop=%{bool}d, isAirDropDiscoverable=%{bool}d, isNearbySharingEnabled=%{bool}d, wirelessEnabled=%{bool}d, bluetoothEnabledIncludingRestricted=%{bool}d)"
- "User is logged in, starting app service server if needed"
- "User logged out, stopping servers"
- "updateServerState canRun(appService=%{bool}d, bonjour=%{bool}d, nearField=%{bool}d) inputs(screenStateSupportsAirDrop=%{bool}d, isAirDropDiscoverable=%{bool}d, isNearbySharingEnabled=%{bool}d, wirelessEnabled=%{bool}d, bluetoothEnabledIncludingRestricted=%{bool}d)"
```
