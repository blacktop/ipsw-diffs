## ContainerManagerCommon

> `/System/Library/PrivateFrameworks/ContainerManagerCommon.framework/ContainerManagerCommon`

```diff

-833.40.14.0.0
-  __TEXT.__text: 0x1010b4
-  __TEXT.__objc_methlist: 0xb3ac
-  __TEXT.__const: 0x15e0
-  __TEXT.__cstring: 0x9bc4
-  __TEXT.__swift5_typeref: 0x85b
-  __TEXT.__oslogstring: 0xfd87
+833.40.16.0.0
+  __TEXT.__text: 0x103ba4
+  __TEXT.__objc_methlist: 0xb454
+  __TEXT.__const: 0x1620
+  __TEXT.__cstring: 0xa053
+  __TEXT.__swift5_typeref: 0x889
+  __TEXT.__oslogstring: 0xfec7
   __TEXT.__constg_swiftt: 0x7b0
   __TEXT.__swift5_reflstr: 0x56a
   __TEXT.__swift5_fieldmd: 0x644

   __TEXT.__swift5_capture: 0xa8
   __TEXT.__swift5_mpenum: 0x10
   __TEXT.__swift5_protos: 0x18
-  __TEXT.__gcc_except_tab: 0x2544
+  __TEXT.__gcc_except_tab: 0x2550
   __TEXT.__ustring: 0x16c
-  __TEXT.__unwind_info: 0x3df0
-  __TEXT.__eh_frame: 0x958
+  __TEXT.__unwind_info: 0x3e60
+  __TEXT.__eh_frame: 0x9dc
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0
   __TEXT.__objc_classname: 0x0
   __TEXT.__objc_methname: 0x0
   __TEXT.__objc_methtype: 0x0
   __DATA_CONST.__const: 0x18e0
-  __DATA_CONST.__objc_classlist: 0x5d8
+  __DATA_CONST.__objc_classlist: 0x5e0
   __DATA_CONST.__objc_catlist: 0x30
   __DATA_CONST.__objc_protolist: 0x610
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x3960
+  __DATA_CONST.__objc_selrefs: 0x3968
   __DATA_CONST.__objc_protorefs: 0x1a8
   __DATA_CONST.__objc_superrefs: 0x4a8
   __DATA_CONST.__objc_arraydata: 0x2e8
-  __DATA_CONST.__got: 0x520
+  __DATA_CONST.__got: 0x540
   __AUTH_CONST.__const: 0x15c0
-  __AUTH_CONST.__cfstring: 0x4e20
-  __AUTH_CONST.__objc_const: 0x178d8
+  __AUTH_CONST.__cfstring: 0x4e40
+  __AUTH_CONST.__objc_const: 0x17a98
   __AUTH_CONST.__objc_dictobj: 0x118
   __AUTH_CONST.__objc_intobj: 0x15a8
   __AUTH_CONST.__objc_arrayobj: 0xf0
-  __AUTH_CONST.__auth_got: 0x13e0
-  __AUTH.__objc_data: 0xf40
-  __AUTH.__data: 0x1e8
-  __DATA.__objc_ivar: 0xc48
-  __DATA.__data: 0x3d50
+  __AUTH_CONST.__auth_got: 0x1430
+  __AUTH.__objc_data: 0xfb0
+  __AUTH.__data: 0x208
+  __DATA.__objc_ivar: 0xc4c
+  __DATA.__data: 0x3db0
   __DATA.__crash_info: 0x148
   __DATA.__common: 0x48
   __DATA_DIRTY.__objc_data: 0x3020

   - /usr/lib/swift/libswiftXPC.dylib
   - /usr/lib/swift/libswift_Builtin_float.dylib
   - /usr/lib/swift/libswiftos.dylib
-  Functions: 3856
-  Symbols:   8667
-  CStrings:  2107
+  Functions: 3885
+  Symbols:   8672
+  CStrings:  2137
 
Symbols:
+ +[MCMContainerCacheEntry(xattr) _identityRecordFromLegacyXattrsForFileHandle:usesInstanceUUID:]
+ +[MCMContainerCacheEntry(xattr) _removeLegacyIdentityXattrsForFileHandle:]
+ +[MCMContainerCacheEntry(xattr) identityRecordForFileHandle:usesInstanceUUID:]
+ +[MCMContainerCacheEntry(xattr) identityRecordForURL:usesInstanceUUID:]
+ +[MCMContainerCacheEntry(xattr) removeIdentityRecordForURL:]
+ +[MCMContainerCacheEntry(xattr) setIdentityRecord:forFileHandle:]
+ +[MCMContainerCacheEntry(xattr) setIdentityRecord:forURL:]
+ -[MCMContainerConfiguration supportsTransient]
+ GCC_except_table1009
+ GCC_except_table1043
+ GCC_except_table1045
+ GCC_except_table1101
+ GCC_except_table1110
+ GCC_except_table1114
+ GCC_except_table1164
+ GCC_except_table1181
+ GCC_except_table1183
+ GCC_except_table1187
+ GCC_except_table1192
+ GCC_except_table1195
+ GCC_except_table1201
+ GCC_except_table1203
+ GCC_except_table1205
+ GCC_except_table1207
+ GCC_except_table1210
+ GCC_except_table1212
+ GCC_except_table1216
+ GCC_except_table1218
+ GCC_except_table1220
+ GCC_except_table1226
+ GCC_except_table1229
+ GCC_except_table1231
+ GCC_except_table1239
+ GCC_except_table1254
+ GCC_except_table1258
+ GCC_except_table1260
+ GCC_except_table1315
+ GCC_except_table1325
+ GCC_except_table1356
+ GCC_except_table1597
+ GCC_except_table1747
+ GCC_except_table1751
+ GCC_except_table1905
+ GCC_except_table1911
+ GCC_except_table2014
+ GCC_except_table2151
+ GCC_except_table2294
+ GCC_except_table2312
+ GCC_except_table2377
+ GCC_except_table2423
+ GCC_except_table2439
+ GCC_except_table2460
+ GCC_except_table2529
+ GCC_except_table2541
+ GCC_except_table2610
+ GCC_except_table2620
+ GCC_except_table2645
+ GCC_except_table2668
+ GCC_except_table2678
+ GCC_except_table2703
+ GCC_except_table2706
+ GCC_except_table2709
+ GCC_except_table2714
+ GCC_except_table2762
+ GCC_except_table2766
+ GCC_except_table2933
+ GCC_except_table2937
+ GCC_except_table3017
+ GCC_except_table878
+ GCC_except_table956
+ _OBJC_CLASS_$_MCMContainerIdentityRecord
+ _OBJC_IVAR_$_MCMContainerConfiguration._supportsTransient
+ _OBJC_METACLASS_$_MCMContainerIdentityRecord
+ __DATA_MCMContainerIdentityRecord
+ __INSTANCE_METHODS_MCMContainerIdentityRecord
+ __IVARS_MCMContainerIdentityRecord
+ __METACLASS_DATA_MCMContainerIdentityRecord
+ __PROPERTIES_MCMContainerIdentityRecord
+ _memchr
+ _objc_msgSend$_identityRecordFromLegacyXattrsForFileHandle:usesInstanceUUID:
+ _objc_msgSend$_removeLegacyIdentityXattrsForFileHandle:
+ _objc_msgSend$_schemaVersion
+ _objc_msgSend$_uuid
+ _objc_msgSend$encodedStringWithError:
+ _objc_msgSend$identityRecordForFileHandle:usesInstanceUUID:
+ _objc_msgSend$identityRecordForURL:usesInstanceUUID:
+ _objc_msgSend$initWithBytes:length:error:
+ _objc_msgSend$initWithDomain:code:userInfo:
+ _objc_msgSend$initWithIdentifier:uuid:schemaVersion:instanceUUID:
+ _objc_msgSend$initWithUnsignedLongLong:
+ _objc_msgSend$setIdentityRecord:forFileHandle:
+ _objc_msgSend$supportsTransient
+ _symbolic SRy_____G s5UInt8V
+ _symbolic SS_ypt
+ _symbolic So6NSUUIDCSg
+ _symbolic _____ySS_yptG s23_ContiguousArrayStorageC
+ _uuid_parse
- +[MCMContainerCacheEntry(xattr) UUIDForFileHandle:]
- +[MCMContainerCacheEntry(xattr) UUIDForURL:]
- +[MCMContainerCacheEntry(xattr) identifierForFileHandle:]
- +[MCMContainerCacheEntry(xattr) identifierForURL:]
- +[MCMContainerCacheEntry(xattr) instanceUUIDForFileHandle:]
- +[MCMContainerCacheEntry(xattr) instanceUUIDForURL:]
- +[MCMContainerCacheEntry(xattr) schemaVersionForFileHandle:]
- +[MCMContainerCacheEntry(xattr) schemaVersionForURL:]
- +[MCMContainerCacheEntry(xattr) setIdentifier:forFileHandle:]
- +[MCMContainerCacheEntry(xattr) setIdentifier:forURL:]
- +[MCMContainerCacheEntry(xattr) setInstanceUUID:forFileHandle:]
- +[MCMContainerCacheEntry(xattr) setInstanceUUID:forURL:]
- +[MCMContainerCacheEntry(xattr) setSchemaVersion:forFileHandle:]
- +[MCMContainerCacheEntry(xattr) setSchemaVersion:forURL:]
- +[MCMContainerCacheEntry(xattr) setUUID:forFileHandle:]
- +[MCMContainerCacheEntry(xattr) setUUID:forURL:]
- GCC_except_table1008
- GCC_except_table1042
- GCC_except_table1044
- GCC_except_table1100
- GCC_except_table1109
- GCC_except_table1113
- GCC_except_table1163
- GCC_except_table1180
- GCC_except_table1182
- GCC_except_table1186
- GCC_except_table1191
- GCC_except_table1194
- GCC_except_table1200
- GCC_except_table1202
- GCC_except_table1204
- GCC_except_table1206
- GCC_except_table1209
- GCC_except_table1211
- GCC_except_table1215
- GCC_except_table1217
- GCC_except_table1219
- GCC_except_table1225
- GCC_except_table1228
- GCC_except_table1230
- GCC_except_table1238
- GCC_except_table1253
- GCC_except_table1257
- GCC_except_table1259
- GCC_except_table1314
- GCC_except_table1324
- GCC_except_table1355
- GCC_except_table1596
- GCC_except_table1746
- GCC_except_table1750
- GCC_except_table1904
- GCC_except_table1910
- GCC_except_table2013
- GCC_except_table2150
- GCC_except_table2293
- GCC_except_table2310
- GCC_except_table2376
- GCC_except_table2422
- GCC_except_table2438
- GCC_except_table2459
- GCC_except_table2528
- GCC_except_table2540
- GCC_except_table2609
- GCC_except_table2619
- GCC_except_table2644
- GCC_except_table2667
- GCC_except_table2677
- GCC_except_table2702
- GCC_except_table2705
- GCC_except_table2708
- GCC_except_table2713
- GCC_except_table2761
- GCC_except_table2765
- GCC_except_table2932
- GCC_except_table2936
- GCC_except_table3016
- GCC_except_table877
- GCC_except_table955
- _objc_msgSend$UUIDForFileHandle:
- _objc_msgSend$UUIDForURL:
- _objc_msgSend$identifierForFileHandle:
- _objc_msgSend$identifierForURL:
- _objc_msgSend$instanceUUIDForFileHandle:
- _objc_msgSend$instanceUUIDForURL:
- _objc_msgSend$schemaVersionForFileHandle:
- _objc_msgSend$schemaVersionForURL:
- _objc_msgSend$setIdentifier:forFileHandle:
- _objc_msgSend$setInstanceUUID:forFileHandle:
- _objc_msgSend$setSchemaVersion:forFileHandle:
- _objc_msgSend$setUUID:forFileHandle:
- _objc_msgSend$setXattr:valueAsNumber:error:
- _objc_msgSend$setXattr:valueAsUUID:error:
CStrings:
+ " UTF-8 bytes, outside [1, "
+ " bytes, over the "
+ " exceeds its field"
+ ", instanceUUID = "
+ ", schemaVersion = "
+ "00000000-0000-0000-0000-000000000000"
+ "<MCMContainerIdentityRecord: identifier = "
+ "Attempting to recover from corrupt metadata for [%@]; identifier = [🔒%{private}@], uuid = %@, schemaVersion = %@"
+ "Cache entry failed verification, identifier doesn't match; cacheEntry = %@, current identifier = [🔒%{private}@]"
+ "Container did not have a usable identity record ([🔒%{private}@]|%@|%@|%@), reading plist (slow); path = %@"
+ "Container owned by non-existent user ([🔒%{private}@]|%@|%@|%@), deleting; path = %@, error = %@"
+ "ContainerManagerCommon_Internal.MCMContainerIdentityRecord"
+ "Could not clear superseded xattr [%@]; error = %@"
+ "Could not clear xattr identity from [🔒%{private}@]; error = %@"
+ "Could not read superseded identity xattr [%@]; error = %@"
+ "Failed to encode identity record [%@]; error = %@"
+ "Failed to read xattr identity; error = %@"
+ "Failed to set xattr identity; error = %@"
+ "Identifier is not an acceptable value to record"
+ "Identity record does not begin with ["
+ "Identity record has no newline introducing the identifier"
+ "Identity record identifier is "
+ "Identity record identifier is not an acceptable "
+ "Identity record identifier is not valid UTF-8"
+ "Identity record identifier label is missing at offset "
+ "Identity record instance-uuid field is unterminated"
+ "Identity record instance-uuid is neither ["
+ "Identity record instance-uuid label is malformed"
+ "Identity record length "
+ "Identity record on [🔒%{private}@] did not validate, falling back; error = %@"
+ "Identity record schema field is malformed"
+ "Identity record uuid field is malformed"
+ "Identity record version "
+ "Identity record version field is malformed"
+ "MobileContainerManager-833.40.16~79"
+ "Rejecting transient query; container class does not support transient containers; containerClass = %{public}@"
+ "Upgrading superseded per-field identity xattrs to a single identity record; record = %@"
+ "com.apple.containermanager.identity"
+ "identifier: "
+ "instance-uuid: "
+ "schema: "
+ "uuid: "
+ "v: "
- "Attempting to recover from corrupt metadata for [%@]; identifier = %@, uuid = %@, schemaVersion = %@"
- "Cache entry failed verification, identifier doesn't match; cacheEntry = %@, current identifier = %@"
- "Container did not have xattr (%@|%@|%@|%@), reading plist (slow); path = %@"
- "Container owned by non-existent user (%@|%@|%@|%@), deleting; path = %@, error = %@"
- "Failed to get xattr identifier; error = %@"
- "Failed to get xattr instance uuid; error = %@"
- "Failed to get xattr schemaVersion; error = %@"
- "Failed to get xattr uuid; error = %@"
- "Failed to set xattr identifier; error = %@"
- "Failed to set xattr instance uuid; error = %@"
- "Failed to set xattr schemaVersion; error = %@"
- "Failed to set xattr uuid; error = %@"
- "MobileContainerManager-833.40.14~50"
```
