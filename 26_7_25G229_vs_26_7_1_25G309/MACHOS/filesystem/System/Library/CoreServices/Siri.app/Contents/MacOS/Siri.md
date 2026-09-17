## Siri

> `System/Library/CoreServices/Siri.app/Contents/MacOS/Siri`

### Sections with Same Size but Changed Content

- `__TEXT.__objc_methlist`
- `__TEXT.__const`
- `__TEXT.__swift5_typeref`
- `__TEXT.__constg_swiftt`
- `__TEXT.__swift5_proto`
- `__TEXT.__swift_as_entry`
- `__TEXT.__swift_as_ret`
- `__TEXT.__unwind_info`
- `__TEXT.__eh_frame`
- `__DATA_CONST.__const`
- `__DATA_CONST.__cfstring`
- `__DATA_CONST.__objc_intobj`
- `__DATA.__objc_const`
- `__DATA.__objc_selrefs`
- `__DATA.__objc_data`
- `__DATA.__data`

```diff

-3525.5.2.0.0
-  __TEXT.__text: 0x27864
+3525.5.2.1.0
+  __TEXT.__text: 0x279f4
   __TEXT.__auth_stubs: 0xea0
   __TEXT.__objc_stubs: 0x59e0
   __TEXT.__objc_methlist: 0x2520

   __TEXT.__objc_methtype: 0x1bd1
   __TEXT.__cstring: 0x3d14
   __TEXT.__gcc_except_tab: 0x554
-  __TEXT.__oslogstring: 0x2948
+  __TEXT.__oslogstring: 0x29b8
   __TEXT.__swift5_typeref: 0x14e
   __TEXT.__swift5_capture: 0x50
   __TEXT.__constg_swiftt: 0x23c

   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  Functions: 916
+  Functions: 917
   Symbols:   518
-  CStrings:  2070
+  CStrings:  2071
 
CStrings:
+ "%s [Invocation] Accepting connection %@ entitled:%d"
+ "%s [Invocation] Process %@ is attempting to submit text to Siri without entitlement."
+ "%s [Invocation] Received Notification with identifier '%@' from pid %d"
- "%s [Invocation] Invoking Siri with entitlement."
- "%s [Invocation] Received Notification with identifier '%@'"
```
