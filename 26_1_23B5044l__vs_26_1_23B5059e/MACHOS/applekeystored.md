## applekeystored

> `/usr/libexec/applekeystored`

```diff

-2155.40.5.0.0
-  __TEXT.__text: 0x69fd0
-  __TEXT.__auth_stubs: 0x1ae0
+2155.40.8.502.1
+  __TEXT.__text: 0x6c7b0
+  __TEXT.__auth_stubs: 0x1a70
   __TEXT.__objc_methlist: 0x104
-  __TEXT.__const: 0x62a5
+  __TEXT.__const: 0x62b5
   __TEXT.__swift5_entry: 0x8
-  __TEXT.__swift5_typeref: 0x1a3b
+  __TEXT.__swift5_typeref: 0x1a1f
   __TEXT.__constg_swiftt: 0x1c10
   __TEXT.__swift5_reflstr: 0x16a0
   __TEXT.__swift5_fieldmd: 0x218c
-  __TEXT.__oslogstring: 0x14d6
-  __TEXT.__cstring: 0x9e16
+  __TEXT.__oslogstring: 0x1596
+  __TEXT.__cstring: 0x9e1a
   __TEXT.__swift5_proto: 0x47c
   __TEXT.__swift5_types: 0x1d4
-  __TEXT.__swift5_capture: 0x170
+  __TEXT.__swift5_capture: 0x124
   __TEXT.__swift5_builtin: 0x104
   __TEXT.__swift5_mpenum: 0x8c
   __TEXT.__swift5_assocty: 0x348
   __TEXT.__objc_classname: 0x39
   __TEXT.__objc_methname: 0x275
   __TEXT.__objc_methtype: 0xad
-  __TEXT.__swift_as_entry: 0xb0
-  __TEXT.__swift_as_ret: 0xd0
+  __TEXT.__swift_as_entry: 0xc0
+  __TEXT.__swift_as_ret: 0xdc
   __TEXT.__swift5_protos: 0x10
-  __TEXT.__unwind_info: 0x19b0
-  __TEXT.__eh_frame: 0x3558
-  __DATA_CONST.__auth_got: 0xd70
+  __TEXT.__unwind_info: 0x1a10
+  __TEXT.__eh_frame: 0x37b0
+  __DATA_CONST.__auth_got: 0xd38
   __DATA_CONST.__got: 0x408
   __DATA_CONST.__auth_ptr: 0x8a0
-  __DATA_CONST.__const: 0x8fd8
+  __DATA_CONST.__const: 0x8f10
   __DATA_CONST.__objc_classlist: 0xb8
   __DATA_CONST.__objc_protolist: 0x30
   __DATA_CONST.__objc_imageinfo: 0x8

   __DATA.__objc_const: 0x1d80
   __DATA.__objc_selrefs: 0x100
   __DATA.__objc_data: 0x1e0
-  __DATA.__data: 0x6540
+  __DATA.__data: 0x6548
   __DATA.__bss: 0x8ef0
   __DATA.__common: 0x208
   - /AppleInternal/Library/Frameworks/TapToRadarKit.framework/TapToRadarKit

   - /usr/lib/libobjc.A.dylib
   - /usr/lib/swift/libswiftCore.dylib
   - /usr/lib/swift/libswiftCoreFoundation.dylib
-  - /usr/lib/swift/libswiftDarwin.dylib
   - /usr/lib/swift/libswiftDispatch.dylib
   - /usr/lib/swift/libswiftOSLog.dylib
   - /usr/lib/swift/libswiftObjectiveC.dylib

   - /usr/lib/swift/libswift_DarwinFoundation1.dylib
   - /usr/lib/swift/libswift_StringProcessing.dylib
   - /usr/lib/swift/libswiftos.dylib
-  UUID: 730120D3-189A-352C-B826-DC26F6CBEB3A
-  Functions: 2283
-  Symbols:   785
-  CStrings:  1839
+  UUID: A883FABA-E52C-3D50-9BA1-2F55F0DDE488
+  Functions: 2275
+  Symbols:   778
+  CStrings:  1840
 
Symbols:
- _$s6Darwin6S_IFMTs6UInt16Vvg
- _$s6Darwin7S_IFDIRs6UInt16Vvg
- _$s6Darwin7S_IFREGs6UInt16Vvg
- _container_traverse_directory
- _container_traverse_node_get_optional_dp_class
- _container_traverse_node_get_path
- _container_traverse_node_is_regular_file
CStrings:
+ "com.apple.fsdhelper"
+ "failed to get current protection class for %s: %@"
+ "getProtectionClass(for: %s) failed: errno(%@)"
+ "getProtectionClass(for: %s) skipped: file no longer exists"
+ "remediating file in dir: %s"
+ "remediator: operation not permitted after first unlock for: %s, unscheduling..."
+ "remediator: operation not permitted before first unlock for: %s, rescheduling..."
+ "set %s to protectionClass: %s"
+ "setProtectionClass(\"%s\") failed: errno(%@)"
+ "setProtectionClass(\"%s\") failed: operation not permitted"
+ "setProtectionClass(for: %s, protection: %{public}s) returned 0, but did not actually change the effective class"
- "B24@?0^v8^B16"
- "invalid protection class %u for %s"
- "markFileAsExceptionApplied(\"%s\") failed: %@"
- "remediateViolation unexpectedly returned allowed for %s"
- "remediation failed for directory %s: errno=%d"
- "setProtectionClass(\"%s\") failed: %@"
- "setProtectionClass(\"%s\") not permitted"
- "skipping directory %s: unexpected file type %hu"
- "skipping file %s: unexpected file type %hu"
- "skipping item %s: stat failed: %d"

```
