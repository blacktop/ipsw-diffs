## diagnosticscheckupd

> `/usr/libexec/diagnosticscheckupd`

### Sections with Same Size but Changed Content

- `__TEXT.__objc_methlist`
- `__TEXT.__objc_methtype`
- `__TEXT.__gcc_except_tab`
- `__TEXT.__swift5_entry`
- `__TEXT.__swift5_protos`
- `__TEXT.__swift5_mpenum`
- `__TEXT.__swift_as_entry`
- `__TEXT.__swift_as_cont`
- `__TEXT.__swift_as_ret`
- `__TEXT.__eh_frame`
- `__DATA_CONST.__cfstring`
- `__DATA_CONST.__objc_classlist`
- `__DATA_CONST.__objc_catlist`
- `__DATA_CONST.__objc_protolist`
- `__DATA_CONST.__objc_protorefs`
- `__DATA_CONST.__objc_superrefs`
- `__DATA_CONST.__objc_intobj`
- `__DATA_CONST.__objc_arraydata`
- `__DATA_CONST.__objc_arrayobj`
- `__DATA_CONST.__got`
- `__DATA.__objc_selrefs`
- `__DATA.__objc_ivar`

```diff

-1374.0.27.0.0
-  __TEXT.__text: 0x492bc
-  __TEXT.__auth_stubs: 0x15d0
-  __TEXT.__objc_stubs: 0x5b40
+1374.2.1.0.0
+  __TEXT.__text: 0x4b264
+  __TEXT.__auth_stubs: 0x15e0
+  __TEXT.__objc_stubs: 0x5b80
   __TEXT.__objc_methlist: 0x380c
-  __TEXT.__cstring: 0x2ec9
-  __TEXT.__objc_methname: 0x8251
-  __TEXT.__objc_classname: 0xbe2
+  __TEXT.__cstring: 0x2ecd
+  __TEXT.__objc_methname: 0x8291
+  __TEXT.__objc_classname: 0xbef
   __TEXT.__objc_methtype: 0x26bb
-  __TEXT.__const: 0x1ea8
+  __TEXT.__const: 0x2088
   __TEXT.__gcc_except_tab: 0xb84
-  __TEXT.__oslogstring: 0x353a
+  __TEXT.__oslogstring: 0x374a
   __TEXT.__swift5_entry: 0x8
-  __TEXT.__constg_swiftt: 0x1534
-  __TEXT.__swift5_typeref: 0xbf3
-  __TEXT.__swift5_builtin: 0x78
-  __TEXT.__swift5_reflstr: 0x146d
-  __TEXT.__swift5_assocty: 0xd8
-  __TEXT.__swift5_fieldmd: 0xdf0
-  __TEXT.__swift5_proto: 0xe8
-  __TEXT.__swift5_types: 0xb0
-  __TEXT.__swift5_capture: 0x53c
+  __TEXT.__constg_swiftt: 0x15f0
+  __TEXT.__swift5_typeref: 0xc0e
+  __TEXT.__swift5_builtin: 0x8c
+  __TEXT.__swift5_reflstr: 0x1516
+  __TEXT.__swift5_assocty: 0xf0
+  __TEXT.__swift5_fieldmd: 0xe54
+  __TEXT.__swift5_proto: 0xf0
+  __TEXT.__swift5_types: 0xb8
+  __TEXT.__swift5_capture: 0x564
   __TEXT.__swift5_protos: 0x20
   __TEXT.__swift5_mpenum: 0x8
   __TEXT.__swift_as_entry: 0x2c
   __TEXT.__swift_as_cont: 0x38
   __TEXT.__swift_as_ret: 0x14
-  __TEXT.__unwind_info: 0x1340
+  __TEXT.__unwind_info: 0x1370
   __TEXT.__eh_frame: 0x7e8
-  __DATA_CONST.__const: 0x2ed8
+  __DATA_CONST.__const: 0x3018
   __DATA_CONST.__cfstring: 0x1680
   __DATA_CONST.__objc_classlist: 0x200
   __DATA_CONST.__objc_catlist: 0x8

   __DATA_CONST.__objc_arrayobj: 0x78
   __DATA_CONST.__objc_doubleobj: 0x10
   __DATA_CONST.__objc_floatobj: 0x20
-  __DATA_CONST.__auth_got: 0xaf8
+  __DATA_CONST.__auth_got: 0xb00
   __DATA_CONST.__got: 0x668
-  __DATA_CONST.__auth_ptr: 0x320
-  __DATA.__objc_const: 0xe290
+  __DATA_CONST.__auth_ptr: 0x328
+  __DATA.__objc_const: 0xe2f0
   __DATA.__objc_selrefs: 0x1df8
   __DATA.__objc_ivar: 0x2d4
-  __DATA.__objc_data: 0x1b78
-  __DATA.__data: 0x27d0
-  __DATA.__bss: 0x1b10
-  __DATA.__common: 0xe0
+  __DATA.__objc_data: 0x1bb8
+  __DATA.__data: 0x2850
+  __DATA.__bss: 0x1c10
+  __DATA.__common: 0xe8
   - /System/Library/Frameworks/Combine.framework/Combine
   - /System/Library/Frameworks/CoreBluetooth.framework/CoreBluetooth
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation

   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  Functions: 1833
-  Symbols:   638
-  CStrings:  2378
+  Functions: 1862
+  Symbols:   639
+  CStrings:  2389
 
Symbols:
+ _swift_retain_x1
CStrings:
+ "Device %s is not present is selectable allowlist, skipping"
+ "Device remained archived through confirmation delay - ending session"
+ "Device resumed (phase: %s) - cancelling pending session end"
+ "DeviceSessionManager: fatal session error, sessionDisplayState -> .error"
+ "DeviceSessionManager: session archived, sessionDisplayState -> .complete"
+ "DeviceSessionManager: suite cleared while .testing forcing idle"
+ "Ignoring self-service session vended after a technician flow; continuing to poll"
+ "Informing %ld client(s) of exit reason %ld"
+ "Selecting first device in required SN list: %s"
+ "endDiagnostics() called, pendingWork != nil: %{bool}d"
+ "filters"
+ "hasEnteredTechnicianFlow"
+ "hasReportedExitReason"
- "Device remained archived after confirmation delay - ending session"
- "Device transitioned away from archived - spurious archive, continuing session"
```
