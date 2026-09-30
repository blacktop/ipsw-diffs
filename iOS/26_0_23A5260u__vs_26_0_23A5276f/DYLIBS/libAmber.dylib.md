## libAmber.dylib

> `/usr/lib/libAmber.dylib`

```diff

-28.0.0.0.0
-  __TEXT.__text: 0xb45b8
+29.0.0.0.0
+  __TEXT.__text: 0xb4928
   __TEXT.__auth_stubs: 0x10c0
   __TEXT.__objc_methlist: 0x20c
-  __TEXT.__gcc_except_tab: 0x9b8c
-  __TEXT.__cstring: 0x10e6a
+  __TEXT.__gcc_except_tab: 0x9c04
+  __TEXT.__cstring: 0x10f02
   __TEXT.__const: 0x1d96
   __TEXT.__oslogstring: 0x3
-  __TEXT.__unwind_info: 0x3988
+  __TEXT.__unwind_info: 0x39c8
   __TEXT.__objc_classname: 0x85
   __TEXT.__objc_methname: 0x6f7
   __TEXT.__objc_methtype: 0x1c8

   __DATA_CONST.__objc_selrefs: 0x270
   __DATA_CONST.__objc_superrefs: 0x18
   __AUTH_CONST.__auth_got: 0x870
-  __AUTH_CONST.__const: 0x3f88
+  __AUTH_CONST.__const: 0x40e8
   __AUTH_CONST.__cfstring: 0x200
   __AUTH_CONST.__objc_const: 0x470
   __AUTH.__objc_data: 0xf0

   - /usr/lib/libc++.1.dylib
   - /usr/lib/libcompression.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 19F6713A-20C8-3AFD-BB1F-2B36C6301E4F
-  Functions: 2306
-  Symbols:   6552
-  CStrings:  2825
+  UUID: C3FEAD81-EABD-3E76-8EFC-BA0311C576F9
+  Functions: 2313
+  Symbols:   6569
+  CStrings:  2831
 
Symbols:
+ GCC_except_table129
+ GCC_except_table144
+ GCC_except_table45
+ GCC_except_table79
+ GCC_except_table92
+ _AmberBlockDeviceLoadObject
+ _AmberBlockDeviceLoadPrologue
+ _AmberBlockDeviceStoreObject
+ _AmberDaemonProxyConnectNBD
+ __ZN5amber11BlockDevice10loadObjectERKNS_15ObjectStorePathERNS_6BufferEy
+ __ZN5amber11BlockDevice11storeObjectERKNS_15ObjectStorePathERKNS_15ConstMemoryViewEy
+ __ZN5amber16BlockPermutation26createWithPrefetchSequenceERKNS_11ArrayObjectINS_15ObjectStorePathEEEyjjjy
+ __ZN5amber20DirectoryObjectStore4loadERKNS_15ObjectStorePathERNS_6BufferEb
+ __ZN5amber24S3ObjectStoreBlockDevice10loadObjectERKNS_15ObjectStorePathERNS_6BufferEy
+ __ZN5amber24S3ObjectStoreBlockDevice11storeObjectERKNS_15ObjectStorePathERKNS_15ConstMemoryViewEy
+ __ZN5amber31DirectoryObjectStoreBlockDevice10loadObjectERKNS_15ObjectStorePathERNS_6BufferEy
+ __ZN5amber31DirectoryObjectStoreBlockDevice11storeObjectERKNS_15ObjectStorePathERKNS_15ConstMemoryViewEy
- GCC_except_table107
- GCC_except_table131
- GCC_except_table132
- GCC_except_table140
- _AmberBlockDeviceLoadPrologueWithSnapshotID
- _AmberBlockPermutationSerializedSize
- _AmberDaemonProxyConnect
- __ZN5amber20DirectoryObjectStore4loadERKNS_15ObjectStorePathERNS_6BufferE
- __ZNK5amber16BlockPermutation14serializedSizeEy
CStrings:
+ "29"
+ "AmberBlockDeviceLoadObject"
+ "AmberBlockDeviceLoadPrologue"
+ "AmberBlockDeviceStoreObject"
+ "DirectoryObjectStore size mismatch (load)"
+ "DirectoryObjectStore size mismatch (store)"
+ "createWithPrefetchSequence"
+ "invalid prefetch sequence"
+ "loadObject"
+ "storeObject"
- "28"
- "AmberBlockDeviceLoadPrologueWithSnapshotID"
- "serializedSize"
- "store object persistence companion"

```
