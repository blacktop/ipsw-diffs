## HighlightAlerts

> `/System/Library/Health/FeedItemPlugins/HighlightAlerts.healthplugin/HighlightAlerts`

```diff

-6087.1.2.1.0
-  __TEXT.__text: 0x75048
-  __TEXT.__auth_stubs: 0x25d0
+6093.0.0.0.0
+  __TEXT.__text: 0x75660
+  __TEXT.__auth_stubs: 0x25e0
   __TEXT.__objc_methlist: 0x3e4
   __TEXT.__cstring: 0x265b
   __TEXT.__const: 0x38e4
-  __TEXT.__constg_swiftt: 0x12bc
+  __TEXT.__constg_swiftt: 0x12c4
   __TEXT.__swift5_typeref: 0xd6f
   __TEXT.__swift5_builtin: 0x64
   __TEXT.__swift5_reflstr: 0x110c
   __TEXT.__swift5_fieldmd: 0x10a4
   __TEXT.__swift5_assocty: 0x420
-  __TEXT.__oslogstring: 0x31ec
+  __TEXT.__oslogstring: 0x326c
   __TEXT.__swift5_proto: 0x33c
   __TEXT.__swift5_types: 0x130
-  __TEXT.__swift5_capture: 0x978
+  __TEXT.__swift5_capture: 0x988
   __TEXT.__swift5_protos: 0xc
   __TEXT.__swift_as_entry: 0x2c
   __TEXT.__swift_as_ret: 0x34
-  __TEXT.__unwind_info: 0x12c0
-  __TEXT.__eh_frame: 0x1090
+  __TEXT.__unwind_info: 0x12c8
+  __TEXT.__eh_frame: 0x10b8
   __TEXT.__objc_classname: 0x4e
   __TEXT.__objc_methname: 0x1044
   __TEXT.__objc_methtype: 0x1a2

   __DATA_CONST.__objc_selrefs: 0x628
   __DATA_CONST.__objc_protorefs: 0x18
   __DATA_CONST.__objc_superrefs: 0x8
-  __AUTH_CONST.__auth_got: 0x12f0
-  __AUTH_CONST.__const: 0x3ad0
+  __AUTH_CONST.__auth_got: 0x12f8
+  __AUTH_CONST.__const: 0x3af8
   __AUTH_CONST.__cfstring: 0x100
   __AUTH_CONST.__objc_const: 0x1240
   __AUTH.__objc_data: 0xa8

   __DATA.__bss: 0x36d0
   __DATA.__common: 0x10
   __DATA_DIRTY.__objc_data: 0x908
-  __DATA_DIRTY.__data: 0x17e8
+  __DATA_DIRTY.__data: 0x17f0
   __DATA_DIRTY.__bss: 0x2f80
   __DATA_DIRTY.__common: 0x80
   - /System/Library/Frameworks/Combine.framework/Combine

   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  UUID: A1406A1D-77ED-36F0-BDD5-515D434CA90E
-  Functions: 1833
+  UUID: F58E12A7-0C01-379B-8455-C516F099E269
+  Functions: 1836
   Symbols:   253
-  CStrings:  640
+  CStrings:  641
 
CStrings:
+ "%{public}s: did not find alert state for %{private}s. Submitting feed item and persisting new alert state: %{private}s"
+ "%{public}s: error while fetching alert state for %{private}s. Ignoring result and relying on the next generation pass."
- "%{public}s: couldn't fetch alert state for %{private}s. Submitting feed item and persisting new alert state: %{private}s"

```
