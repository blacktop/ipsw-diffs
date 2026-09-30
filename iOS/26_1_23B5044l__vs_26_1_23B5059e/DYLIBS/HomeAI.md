## HomeAI

> `/System/Library/PrivateFrameworks/HomeAI.framework/HomeAI`

```diff

-351.0.0.0.0
-  __TEXT.__text: 0x15b374
+351.2.1.0.0
+  __TEXT.__text: 0x15b73c
   __TEXT.__auth_stubs: 0x1c70
   __TEXT.__init_offsets: 0x10
-  __TEXT.__objc_methlist: 0x9aec
-  __TEXT.__const: 0x484d
+  __TEXT.__objc_methlist: 0x9af4
+  __TEXT.__const: 0x485d
   __TEXT.__cstring: 0xd13b
   __TEXT.__gcc_except_tab: 0xc400
-  __TEXT.__oslogstring: 0x76b3
+  __TEXT.__oslogstring: 0x76cf
   __TEXT.__dlopen_cstrs: 0x116
-  __TEXT.__unwind_info: 0x4e38
+  __TEXT.__unwind_info: 0x4e40
   __TEXT.__eh_frame: 0x1e4
   __TEXT.__objc_classname: 0x1816
-  __TEXT.__objc_methname: 0x15e56
+  __TEXT.__objc_methname: 0x15e8d
   __TEXT.__objc_methtype: 0x462c
   __TEXT.__objc_stubs: 0xe5e0
   __DATA_CONST.__got: 0xbc8

   __DATA_CONST.__objc_catlist: 0x8
   __DATA_CONST.__objc_protolist: 0x108
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x44a8
+  __DATA_CONST.__objc_selrefs: 0x44b8
   __DATA_CONST.__objc_protorefs: 0x10
   __DATA_CONST.__objc_superrefs: 0x5a8
   __DATA_CONST.__objc_arraydata: 0x618
   __AUTH_CONST.__auth_got: 0xe50
   __AUTH_CONST.__const: 0x45a0
   __AUTH_CONST.__cfstring: 0x8740
-  __AUTH_CONST.__objc_const: 0x14b30
+  __AUTH_CONST.__objc_const: 0x14b10
   __AUTH_CONST.__objc_intobj: 0x540
   __AUTH_CONST.__objc_arrayobj: 0x360
   __AUTH_CONST.__objc_doubleobj: 0x1b0

   - /usr/lib/libc++.1.dylib
   - /usr/lib/libcompression.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: C35C42F7-02BD-349C-8ECB-4247349F2AB8
-  Functions: 5220
-  Symbols:   17728
-  CStrings:  7908
+  UUID: 24C6E9DB-1AB3-3362-A911-9748D3CEA90F
+  Functions: 5225
+  Symbols:   17737
+  CStrings:  7911
 
Symbols:
+ -[HMIExternalPersonManager handleDataChanged]
+ -[HMIExternalPersonManager initWithUUID:homeUUID:watchdogTimer:]
+ -[HMIHomePersonManager handleDataChanged]
+ -[HMIHomePersonManager initWithUUID:homeUUID:watchdogTimer:]
+ -[HMIPersonDataSourceDisk removeFaceprintsWithUUIDs:completion:]
+ -[HMIPersonManager handleDataChanged]
+ ___113-[HMIUpdatePersonsModelTask subsampleFacesForPersons:withFaceObservationsMap:dataSource:vnUUIDToFaceCropUUIDMap:]_block_invoke.239
+ ___60-[HMIUpdatePersonsModelTask limitEnforcedSubsetFromPersons:]_block_invoke.235
+ ___block_literal_global.234
+ ___block_literal_global.237
+ ___block_literal_global.242
+ _objc_msgSend$initWithUUID:homeUUID:watchdogTimer:
- -[HMIPersonManager initWithUUID:]
- __OBJC_$_PROTOCOL_INSTANCE_METHODS_OPT_HMIPersonManagerDataSource
- ___113-[HMIUpdatePersonsModelTask subsampleFacesForPersons:withFaceObservationsMap:dataSource:vnUUIDToFaceCropUUIDMap:]_block_invoke.241
- ___60-[HMIUpdatePersonsModelTask limitEnforcedSubsetFromPersons:]_block_invoke.237
- ___block_literal_global.236
- ___block_literal_global.239
- _objc_msgSend$initWithUUID:homeUUID:
CStrings:
+ "%{public}@handleDataChanged"
+ "handleDataChanged"
+ "initWithUUID:homeUUID:watchdogTimer:"

```
