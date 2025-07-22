## FindMyCore

> `/System/Library/PrivateFrameworks/FindMyCore.framework/FindMyCore`

```diff

-442.30.6.9.13
-  __TEXT.__text: 0x749d4
-  __TEXT.__auth_stubs: 0x1d90
+442.30.6.9.19
+  __TEXT.__text: 0x76618
+  __TEXT.__auth_stubs: 0x1db0
   __TEXT.__objc_methlist: 0x154
-  __TEXT.__const: 0x8126
-  __TEXT.__cstring: 0x14bf
+  __TEXT.__const: 0x8146
+  __TEXT.__cstring: 0x151f
   __TEXT.__swift5_typeref: 0x20b4
   __TEXT.__swift5_capture: 0x1f8
-  __TEXT.__oslogstring: 0x2f2
+  __TEXT.__oslogstring: 0x661
   __TEXT.__constg_swiftt: 0x1740
   __TEXT.__swift5_builtin: 0x64
   __TEXT.__swift5_reflstr: 0x12e1

   __TEXT.__swift_as_ret: 0x148
   __TEXT.__swift5_protos: 0x2c
   __TEXT.__swift5_mpenum: 0x2c
-  __TEXT.__unwind_info: 0x2238
-  __TEXT.__eh_frame: 0x305c
+  __TEXT.__unwind_info: 0x2260
+  __TEXT.__eh_frame: 0x3104
   __TEXT.__objc_classname: 0x3b
   __TEXT.__objc_methname: 0x66d
   __TEXT.__objc_methtype: 0x100

   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_selrefs: 0x280
   __DATA_CONST.__objc_protorefs: 0x28
-  __AUTH_CONST.__auth_got: 0xec8
+  __AUTH_CONST.__auth_got: 0xed8
   __AUTH_CONST.__const: 0x4050
   __AUTH_CONST.__objc_const: 0x470
   __AUTH.__objc_data: 0x50
   __AUTH.__data: 0xcd0
-  __DATA.__data: 0x2208
+  __DATA.__data: 0x2258
   __DATA.__bss: 0xd530
   __DATA.__common: 0x28
   __DATA_DIRTY.__data: 0x90

   - /System/Library/PrivateFrameworks/CorePhoneNumbers.framework/CorePhoneNumbers
   - /System/Library/PrivateFrameworks/FeatureFlags.framework/FeatureFlags
   - /System/Library/PrivateFrameworks/FindMyBase.framework/FindMyBase
-  - /System/Library/PrivateFrameworks/FindMyDevice.framework/FindMyDevice
   - /System/Library/PrivateFrameworks/FindMyLocate.framework/FindMyLocate
   - /System/Library/PrivateFrameworks/SPOwner.framework/SPOwner
   - /usr/lib/libSystem.B.dylib

   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  UUID: 7A0B081D-4953-3897-AE8F-D33D63C35038
-  Functions: 3018
+  UUID: 504F1F15-EBB2-3621-B052-44061C27EB45
+  Functions: 3030
   Symbols:   1178
-  CStrings:  286
+  CStrings:  300
 
CStrings:
+ "CNContact fetch returned %ld results"
+ "CNContact fetch: expected 1 result, got %ld"
+ "CNContact fetch: expected 1 result, got %ld - contact identifiers: %s"
+ "CNContact fetch: no contact found containing main handle '%s', returning first result '%s'"
+ "CNContact fetch: no contacts found for handles"
+ "CNContact fetch: re-sorted contact selection changed from '%s' to '%s' based on main handle '%s'"
+ "Checking contact '%s' with handles: %s - contains main handle '%s': %{bool}d"
+ "Handle matching mismatch detected: allHandles match found but mainHandle does not match. MainHandle: %s, allHandles: %s"
+ "PersonModel+CNContact"
+ "PersonModel+Handles"
+ "PersonModel+List"
+ "PersonModel: %s is not favorite - contains:false"
+ "PersonModel: %s is not part of specificHandles - contains:false - handles: %s, specificHandles: %s"
+ "Starting CNContact fetch for handles: %s, main handle: '%s'"

```
