## DriverKit

> `/System/Library/Frameworks/DriverKit.framework/DriverKit`

```diff

-427.120.2.0.0
-  __TEXT.__text: 0x35cec
+442.0.0.0.0
+  __TEXT.__text: 0x36428
   __TEXT.__auth_stubs: 0xbc0
   __TEXT.__init_offsets: 0x8
-  __TEXT.__const: 0x5d04
-  __TEXT.__cstring: 0x2e1e
+  __TEXT.__const: 0x5d44
+  __TEXT.__cstring: 0x2e46
   __TEXT.__oslogstring: 0xe
-  __TEXT.__unwind_info: 0x188
+  __TEXT.__unwind_info: 0x190
   __DATA_CONST.__got: 0x48
-  __DATA_CONST.__const: 0x470
+  __DATA_CONST.__const: 0x4b0
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__structlayouts: 0x10
   __DATA_CONST.__osclassinfo: 0x158
   __AUTH_CONST.__auth_got: 0x5e0
-  __AUTH_CONST.__const: 0x56c8
-  __DATA.__crash_info: 0x40
+  __AUTH_CONST.__const: 0x5698
+  __DATA.__crash_info: 0x148
   __DATA.__common: 0x170
   __DATA.__bss: 0x438
-  __DATA_DIRTY.__common: 0x310
+  __DATA_DIRTY.__common: 0x300
   __DATA_DIRTY.__bss: 0x1008
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libc++.1.dylib
-  UUID: 7C49ECDD-F1F1-3076-897C-B1840340E530
-  Functions: 1521
-  Symbols:   2915
-  CStrings:  466
+  UUID: EF61211F-0A46-33F0-909C-9FD3975A3D28
+  Functions: 1528
+  Symbols:   2926
+  CStrings:  468
 
Symbols:
+ _OSDataAppendBytes.cold.1
+ __ZN9IOService17CreatePMAssertionEjPybPFiP15OSMetaClassBase5IORPCE
+ __ZN9IOService18ReleasePMAssertionEyPFiP15OSMetaClassBase5IORPCE
+ __ZN9IOService24CreatePMAssertion_InvokeE5IORPCP15OSMetaClassBasePFiS2_jPybE
+ __ZN9IOService25ReleasePMAssertion_InvokeE5IORPCP15OSMetaClassBasePFiS2_yE
+ ____Z19OSObjectLogInternalP8OSObjectj_block_invoke.42
+ ____ZL31IOInterruptDispatchSourceThreadPv_block_invoke_2
+ ___block_descriptor_tmp.166
+ ___block_descriptor_tmp.170
+ ___block_descriptor_tmp.175
+ ___block_descriptor_tmp.177
+ ___block_descriptor_tmp.181
+ ___block_descriptor_tmp.187
+ ___block_descriptor_tmp.190
+ ___block_descriptor_tmp.194
+ ___block_descriptor_tmp.197
+ ___block_descriptor_tmp.246
+ ___block_descriptor_tmp.247
+ ___block_descriptor_tmp.27
+ ___block_descriptor_tmp.34
+ ___block_descriptor_tmp.41
+ ___block_descriptor_tmp.47
+ ___block_descriptor_tmp.56
+ ___block_descriptor_tmp.59
+ ___block_descriptor_tmp.62
+ ___block_descriptor_tmp.65
+ ___block_descriptor_tmp.68
+ _io_connect_map_shared_memory
- ____Z19OSObjectLogInternalP8OSObjectj_block_invoke.41
- ___block_descriptor_tmp.165
- ___block_descriptor_tmp.169
- ___block_descriptor_tmp.174
- ___block_descriptor_tmp.176
- ___block_descriptor_tmp.180
- ___block_descriptor_tmp.186
- ___block_descriptor_tmp.189
- ___block_descriptor_tmp.193
- ___block_descriptor_tmp.22
- ___block_descriptor_tmp.248
- ___block_descriptor_tmp.26
- ___block_descriptor_tmp.32
- ___block_descriptor_tmp.40
- ___block_descriptor_tmp.46
- ___block_descriptor_tmp.55
- ___block_descriptor_tmp.58
- ___block_descriptor_tmp.61
- ___block_descriptor_tmp.64
- ___block_descriptor_tmp.67
- ___block_descriptor_tmp.70
- ___block_descriptor_tmp.73
- ___block_descriptor_tmp.76
CStrings:
+ "OSDataAppendBytes"
+ "allocLen >= newLength"

```
