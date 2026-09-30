## sysdiagnosed

> `/usr/libexec/sysdiagnosed`

```diff

-1527.0.0.0.0
-  __TEXT.__text: 0x65014
-  __TEXT.__auth_stubs: 0x16b0
-  __TEXT.__objc_stubs: 0x93c0
-  __TEXT.__objc_methlist: 0x3eb4
+1527.0.2.0.0
+  __TEXT.__text: 0x6581c
+  __TEXT.__auth_stubs: 0x16d0
+  __TEXT.__objc_stubs: 0x9440
+  __TEXT.__objc_methlist: 0x3ef4
   __TEXT.__const: 0x1cc
-  __TEXT.__cstring: 0x1067c
+  __TEXT.__cstring: 0x107c6
   __TEXT.__objc_classname: 0x3a7
-  __TEXT.__objc_methtype: 0x1685
-  __TEXT.__gcc_except_tab: 0x1268
-  __TEXT.__objc_methname: 0xa61c
-  __TEXT.__oslogstring: 0x8f10
+  __TEXT.__objc_methtype: 0x1694
+  __TEXT.__gcc_except_tab: 0x12a0
+  __TEXT.__objc_methname: 0xa697
+  __TEXT.__oslogstring: 0x8fc1
   __TEXT.__ustring: 0x4e8
-  __TEXT.__unwind_info: 0x11a0
-  __DATA_CONST.__auth_got: 0xb68
+  __TEXT.__unwind_info: 0x11d0
+  __DATA_CONST.__auth_got: 0xb78
   __DATA_CONST.__got: 0x3c0
   __DATA_CONST.__auth_ptr: 0x60
-  __DATA_CONST.__const: 0x13b0
-  __DATA_CONST.__cfstring: 0x11040
+  __DATA_CONST.__const: 0x1420
+  __DATA_CONST.__cfstring: 0x110e0
   __DATA_CONST.__objc_classlist: 0x138
   __DATA_CONST.__objc_protolist: 0x38
   __DATA_CONST.__objc_imageinfo: 0x8

   __DATA_CONST.__objc_arrayobj: 0x1350
   __DATA_CONST.__objc_intobj: 0x300
   __DATA_CONST.__objc_floatobj: 0x10
-  __DATA.__objc_const: 0x5270
-  __DATA.__objc_selrefs: 0x29a0
-  __DATA.__objc_ivar: 0x46c
+  __DATA.__objc_const: 0x52a0
+  __DATA.__objc_selrefs: 0x29c0
+  __DATA.__objc_ivar: 0x470
   __DATA.__objc_data: 0xc30
   __DATA.__data: 0x2d0
-  __DATA.__bss: 0x270
+  __DATA.__bss: 0x280
   - /AppleInternal/Library/Frameworks/TapToRadarKit.framework/TapToRadarKit
   - /System/Library/Frameworks/AudioToolbox.framework/AudioToolbox
   - /System/Library/Frameworks/CoreBluetooth.framework/CoreBluetooth

   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libsysdiagnose.dylib
   - /usr/lib/libtailspin.dylib
-  UUID: 643A6CB0-1FCA-3F69-BBD7-1E16585F3F3B
-  Functions: 1753
-  Symbols:   497
-  CStrings:  7426
+  UUID: F9EB6FC9-29B0-3EAD-91E1-4D6754034A18
+  Functions: 1768
+  Symbols:   499
+  CStrings:  7447
 
Symbols:
+ _xpc_dictionary_create_empty
+ _xpc_int64_create
CStrings:
+ "\nIncreasing log archive collection timeout (on an ERM device)"
+ "(NOT(SELF.lastPathComponent BEGINSWITH '%@-'))"
+ "(NOT(SELF.lastPathComponent CONTAINS '_%@-'))"
+ "(NOT(SELF.lastPathComponent CONTAINS '_%@_'))"
+ "Failed to create xpc_dictionary for helper connection. Cannot execute task: %@"
+ "T@\"NSObject<OS_xpc_object>\",&,V_extra_params"
+ "Will exclude logs for %lu processes"
+ "_extra_params"
+ "containerSizeCap"
+ "extra_params"
+ "setExtraParam:forVal:"
+ "setExtra_params:"
+ "setSizeCap:"
+ "setStartDate:andExecuteFromCallback:"
+ "sysdiagnoseExcludeProcessesCrashesAndSpins"
+ "v32@0:8r*16@24"
- "%@ AND %@"
- "setStartDate:AndExecuteFromCallback:"

```
