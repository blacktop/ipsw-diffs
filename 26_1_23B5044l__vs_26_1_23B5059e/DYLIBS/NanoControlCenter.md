## NanoControlCenter

> `/System/Library/PrivateFrameworks/NanoControlCenter.framework/NanoControlCenter`

```diff

-64.0.0.0.0
-  __TEXT.__text: 0xf1098
+65.1.0.0.0
+  __TEXT.__text: 0xf2304
   __TEXT.__auth_stubs: 0x2fd0
   __TEXT.__objc_methlist: 0x151c
-  __TEXT.__const: 0xc0f8
-  __TEXT.__cstring: 0x568e
-  __TEXT.__oslogstring: 0x1f7d
+  __TEXT.__const: 0xc108
+  __TEXT.__cstring: 0x567e
+  __TEXT.__oslogstring: 0x1fbd
   __TEXT.__constg_swiftt: 0x39fc
   __TEXT.__swift5_typeref: 0x842d
   __TEXT.__swift5_builtin: 0x1cc

   __TEXT.__swift5_proto: 0x5cc
   __TEXT.__swift5_types: 0x334
   __TEXT.__swift5_mpenum: 0x68
-  __TEXT.__swift5_capture: 0xd38
-  __TEXT.__swift_as_entry: 0x130
-  __TEXT.__swift_as_ret: 0xf8
+  __TEXT.__swift5_capture: 0xd4c
+  __TEXT.__swift_as_entry: 0x134
+  __TEXT.__swift_as_ret: 0xfc
   __TEXT.__swift5_protos: 0x18
-  __TEXT.__unwind_info: 0x3b08
-  __TEXT.__eh_frame: 0x435c
+  __TEXT.__unwind_info: 0x3b48
+  __TEXT.__eh_frame: 0x4494
   __TEXT.__objc_classname: 0x18c
   __TEXT.__objc_methname: 0x26bd
   __TEXT.__objc_methtype: 0x66f

   __DATA_CONST.__objc_protorefs: 0x60
   __DATA_CONST.__objc_superrefs: 0x8
   __AUTH_CONST.__auth_got: 0x17f0
-  __AUTH_CONST.__const: 0x6980
+  __AUTH_CONST.__const: 0x69a8
   __AUTH_CONST.__cfstring: 0xc0
   __AUTH_CONST.__objc_const: 0x4868
   __AUTH.__objc_data: 0x1788

   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  UUID: 8CC9705E-020E-351B-B074-7D390FDB8FC3
-  Functions: 5102
+  UUID: 1CC26F04-0080-3DD5-9282-52652D896F15
+  Functions: 5113
   Symbols:   2387
-  CStrings:  1365
+  CStrings:  1367
 
Symbols:
+ _NPSHasCompletedInitialSync
+ _objectdestroy.351Tm
- _objectdestroy.345Tm
- _os_variant_has_internal_ui
CStrings:
+ "%s couldn't match pendingControl: %s. Keeping as pending."
+ "%s didPair: %{BOOL}d; initialSyncComplete: %{BOOL}d"
+ "%s displayed button IDs: %s"
+ "%s initialSyncComplete: %{BOOL}d"
+ "resetButtonModelStorage()"
- "%s - Internal and found service with .featureOff, inferring available when #SUI enabled"
- "%s didPair: %{BOOL}d"
- "com.apple.Skipper.StewieStateMonitor"

```
