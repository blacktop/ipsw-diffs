## libBKDM2.dylib

> `/usr/lib/libBKDM2.dylib`

```diff

-980.0.26.0.0
-  __TEXT.__text: 0x87dc0
+980.40.11.0.0
+  __TEXT.__text: 0x87f74
   __TEXT.__lazy_helpers: 0xa8
-  __TEXT.__objc_methlist: 0x61bc
-  __TEXT.__const: 0xd7f8
-  __TEXT.__cstring: 0x832a
-  __TEXT.__oslogstring: 0x52f7
+  __TEXT.__objc_methlist: 0x61d4
+  __TEXT.__const: 0xd802
+  __TEXT.__cstring: 0x83b3
+  __TEXT.__oslogstring: 0x52f6
   __TEXT.__gcc_except_tab: 0x1a88
   __TEXT.__ustring: 0x11c
-  __TEXT.__unwind_info: 0x1a20
+  __TEXT.__unwind_info: 0x1a30
   __TEXT.__eh_frame: 0x50
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0
   __TEXT.__objc_classname: 0x0
   __TEXT.__objc_methname: 0x0
   __TEXT.__objc_methtype: 0x0
-  __DATA_CONST.__const: 0x16d8
+  __DATA_CONST.__const: 0x16e8
   __DATA_CONST.__objc_classlist: 0xf8
   __DATA_CONST.__objc_protolist: 0x28
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x40b0
+  __DATA_CONST.__objc_selrefs: 0x40b8
   __DATA_CONST.__objc_superrefs: 0xd0
-  __DATA_CONST.__objc_arraydata: 0x4d8
+  __DATA_CONST.__objc_arraydata: 0x4e8
   __DATA_CONST.__got: 0x4a8
   __AUTH_CONST.__const: 0xc28
-  __AUTH_CONST.__cfstring: 0x6c40
+  __AUTH_CONST.__cfstring: 0x6cc0
   __AUTH_CONST.__objc_const: 0xa490
   __AUTH_CONST.__lazy_load_got: 0x10
   __AUTH_CONST.__objc_intobj: 0x420

   - /usr/lib/libSystemHealth.dylib
   - /usr/lib/libc++.1.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 3153
-  Symbols:   5708
-  CStrings:  1828
+  Functions: 3156
+  Symbols:   5714
+  CStrings:  1833
 
Symbols:
+ -[BioLog setPurgeableAtPath:directory:]
+ -[BiometricKitXPCServerPearl addDeviceSpecificProperties:]
+ GCC_except_table19
+ GCC_except_table33
+ GCC_except_table48
+ GCC_except_table51
+ GCC_except_table55
+ GCC_except_table70
+ __oidAppleExtendedKeyUsageSWUpdateSigning
+ _oidAppleExtendedKeyUsageSWUpdateSigning
- GCC_except_table45
- GCC_except_table50
- GCC_except_table52
- GCC_except_table69
Functions:
+ -[BiometricKitXPCServerPearl addDeviceSpecificProperties:]
~ -[BioLog init] : 1748 -> 1744
~ -[BioLog createFileAtPath:contents:attributes:purgeable:] : 204 -> 200
+ -[BioLog setPurgeableAtPath:directory:]
~ -[BioLog sequencePathForId:andSubdirectory:] : 244 -> 240
~ -[BioLog logSequenceInfo:withContext:orientation:identities:] : 13328 -> 13392
~ -[BioLog eventPathWithName:date:] : 344 -> 340
~ -[BioLog logSecureFrameMeta:timestamp:frameNumber:fromCameraID:] : 5788 -> 5784
+ -[BiometricKitXPCServerPearl addDeviceSpecificProperties:].cold.1
CStrings:
+ "BKDPHasFaceIDInExclave"
+ "BKDPRequiresFaceIDLatencyMitigation"
+ "BioLogRetention"
+ "Couldn't create OS Log for 'com.apple.BiometricKit.BioLogRetention'!\n"
+ "analytics_biolockout_reason"
+ "bioLogRetentionMarkFilesPurgeable"
+ "deviceProperties"
- "BioLog-Retention"
- "Couldn't create OS Log for 'com.apple.BiometricKit.BioLog-Retention'!\n"
```
