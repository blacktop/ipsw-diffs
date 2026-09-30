## devicecheckd

> `/System/Library/PrivateFrameworks/DeviceCheckInternal.framework/devicecheckd`

```diff

-123.0.0.0.0
-  __TEXT.__text: 0x47d0
-  __TEXT.__auth_stubs: 0x550
+125.0.0.0.0
+  __TEXT.__text: 0x4a80
+  __TEXT.__auth_stubs: 0x560
   __TEXT.__objc_stubs: 0x660
-  __TEXT.__objc_methlist: 0x4a4
+  __TEXT.__objc_methlist: 0x4c4
   __TEXT.__objc_classname: 0xab
-  __TEXT.__objc_methname: 0xa97
-  __TEXT.__objc_methtype: 0x53b
-  __TEXT.__cstring: 0x433
+  __TEXT.__objc_methname: 0xad8
+  __TEXT.__objc_methtype: 0x546
+  __TEXT.__cstring: 0x44e
   __TEXT.__const: 0x28
   __TEXT.__gcc_except_tab: 0xc0
-  __TEXT.__oslogstring: 0x5c4
+  __TEXT.__oslogstring: 0x640
   __TEXT.__unwind_info: 0x198
-  __DATA_CONST.__auth_got: 0x2b8
+  __DATA_CONST.__auth_got: 0x2c0
   __DATA_CONST.__got: 0x100
   __DATA_CONST.__const: 0x340
   __DATA_CONST.__cfstring: 0x220

   __DATA_CONST.__objc_protorefs: 0x8
   __DATA_CONST.__objc_superrefs: 0x10
   __DATA.__objc_const: 0x6f0
-  __DATA.__objc_selrefs: 0x300
+  __DATA.__objc_selrefs: 0x310
   __DATA.__objc_ivar: 0x1c
   __DATA.__objc_data: 0x190
   __DATA.__data: 0x120
-  __DATA.__bss: 0x80
+  __DATA.__bss: 0x88
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/Foundation.framework/Foundation
   - /System/Library/Frameworks/Security.framework/Security

   - /System/Library/PrivateFrameworks/DeviceIdentity.framework/DeviceIdentity
   - /System/Library/PrivateFrameworks/MobileAsset.framework/MobileAsset
   - /usr/lib/libSystem.B.dylib
+  - /usr/lib/libbsm.0.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: D7EB513C-DC8B-3E6B-9519-6445E497B594
-  Functions: 96
-  Symbols:   126
-  CStrings:  247
+  UUID: 2F515650-8E9B-39C7-A482-4FEFB2BBF356
+  Functions: 99
+  Symbols:   127
+  CStrings:  253
 
Symbols:
+ _proc_pidinfo
CStrings:
+ "%25s:%-5d App Attest Action Extension feature flag enabled { enabled=%d }."
+ "%25s:%-5d proc_pidinfo failed. { ErrorCode: %d }"
+ "B20@0:8i16"
+ "actionExtensionAttestation"
+ "entitlementsValidatedForPID:"
+ "isActionExtensionAttestationEnabled"

```
