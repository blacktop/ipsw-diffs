## spindump

> `/usr/sbin/spindump`

```diff

-412.0.0.0.0
-  __TEXT.__text: 0x11fb38
-  __TEXT.__auth_stubs: 0x1510
-  __TEXT.__objc_stubs: 0x4a00
+412.0.1.0.0
+  __TEXT.__text: 0x120e64
+  __TEXT.__auth_stubs: 0x1520
+  __TEXT.__objc_stubs: 0x4a40
   __TEXT.__objc_methlist: 0xcd0
-  __TEXT.__const: 0x2a8
-  __TEXT.__oslogstring: 0x3358b
-  __TEXT.__cstring: 0x1aa75
+  __TEXT.__const: 0x2b0
+  __TEXT.__cstring: 0x1ad3a
+  __TEXT.__oslogstring: 0x33833
   __TEXT.__objc_classname: 0x16f
   __TEXT.__objc_methtype: 0x596
   __TEXT.__gcc_except_tab: 0x4ef0
-  __TEXT.__objc_methname: 0x48c7
-  __TEXT.__unwind_info: 0x1708
-  __DATA_CONST.__auth_got: 0xa98
-  __DATA_CONST.__got: 0x330
+  __TEXT.__objc_methname: 0x48e9
+  __TEXT.__unwind_info: 0x1728
+  __DATA_CONST.__auth_got: 0xaa0
+  __DATA_CONST.__got: 0x338
   __DATA_CONST.__auth_ptr: 0x48
-  __DATA_CONST.__const: 0x2090
-  __DATA_CONST.__cfstring: 0xd5a0
+  __DATA_CONST.__const: 0x2110
+  __DATA_CONST.__cfstring: 0xd680
   __DATA_CONST.__objc_classlist: 0x98
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_superrefs: 0x68

   __DATA_CONST.__objc_arraydata: 0x48
   __DATA_CONST.__objc_arrayobj: 0x48
   __DATA.__objc_const: 0x2560
-  __DATA.__objc_selrefs: 0x1348
+  __DATA.__objc_selrefs: 0x1358
   __DATA.__objc_ivar: 0x284
   __DATA.__objc_data: 0x5f0
   __DATA.__data: 0x1c
   __DATA.__crash_info: 0x148
-  __DATA.__bss: 0x910
+  __DATA.__bss: 0x920
   __DATA.__common: 0x70
   - /System/Library/Frameworks/AppKit.framework/Versions/C/AppKit
   - /System/Library/Frameworks/CoreFoundation.framework/Versions/A/CoreFoundation

   - /usr/lib/libsystemstats.dylib
   - /usr/lib/libtailspin.dylib
   - /usr/lib/libz.1.dylib
-  UUID: 5BD94F47-7EBD-33CF-A7AA-A27022571074
-  Functions: 2668
-  Symbols:   451
-  CStrings:  7860
+  UUID: 2E09D695-630A-3BDC-B6BA-64CF449995BB
+  Functions: 2687
+  Symbols:   453
+  CStrings:  7891
 
Symbols:
+ _OBJC_CLASS_$_BGRepeatingSystemTaskRequest
+ _write
CStrings:
+ "/Library/Application Support/CrashReporter/SubmitDiagInfo.config"
+ "Enable spin submissions task already exists"
+ "Non-internal build, not overwriting enablement spin submissions"
+ "Overwrote SubmitDiagInfo.config successfully"
+ "Running enable spin submission task"
+ "Submitted enable spin submission task successfully"
+ "Unable to format: Enable spin submissions task already exists"
+ "Unable to format: Non-internal build, not overwriting enablement spin submissions"
+ "Unable to format: Overwrote SubmitDiagInfo.config successfully"
+ "Unable to format: Running enable spin submission task"
+ "Unable to format: Submitted enable spin submission task successfully"
+ "Unable to format: Unable to open SubmitDiagInfo.config: %d (%s)"
+ "Unable to open SubmitDiagInfo.config: %d (%s)"
+ "com.apple.spindump.enable_spin_submissions"
+ "setInterval:"
+ "setShouldWakeDevice:"
+ "v16@?0@\"BGSystemTask\"8"
+ "{\n  \"log_types\": {\n    \"23\": {\n      \"sample\": [\n        50,\n        0\n      ]\n    },\n    \"22\": {\n      \"sample\": [\n        20,\n        0\n      ]\n    },\n    \"25\": {\n      \"sample\": [\n        120,\n        0\n      ]\n    },\n    \"11\": {\n      \"sample\": [\n        1,\n        0\n      ]\n    }\n  }\n}"

```
